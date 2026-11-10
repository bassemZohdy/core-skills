"""Tests for scripts/check.py: a clean copy passes and each rule fails when broken."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
import check  # noqa: E402

COPIED = ("plugin", ".claude-plugin", ".agents", "LICENSE", "docs/INSTALL.md")


class CheckTests(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.root = Path(self._tmp.name)
        for item in COPIED:
            source, target = REPO / item, self.root / item
            target.parent.mkdir(parents=True, exist_ok=True)
            if source.is_dir():
                shutil.copytree(source, target)
            else:
                shutil.copy(source, target)

    def skill(self, name="plan"):
        return self.root / "plugin" / "skills" / name / "SKILL.md"

    def edit(self, path, old, new, count=1):
        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), count, f"fixture drift: {old!r} in {path.name}")
        path.write_text(text.replace(old, new), encoding="utf-8", newline="")

    def edit_json(self, relative, mutate):
        path = self.root / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        mutate(data)
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def assertFails(self, fragment):
        errors, _ = check.run_checks(self.root)
        self.assertTrue(any(fragment in e for e in errors), f"expected {fragment!r} in {errors}")

    def test_clean_copy_passes(self):
        errors, count = check.run_checks(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(count, 8)

    def test_name_mismatch(self):
        self.edit(self.skill(), "\nname: plan\n", "\nname: planner\n")
        self.assertFails("plan: name mismatch")

    def test_missing_license_key(self):
        self.edit(self.skill(), "\nlicense: Apache-2.0\n", "\n")
        self.assertFails("plan: missing license")

    def test_unknown_frontmatter_key(self):
        self.edit(self.skill(), "\nlicense: Apache-2.0\n", "\nlicense: Apache-2.0\nversion: 1\n")
        self.assertFails("unknown frontmatter key 'version'")

    def test_overlong_description(self):
        text = self.skill().read_text(encoding="utf-8")
        start = text.index("description: ") + len("description: ")
        end = text.index("\n", start)
        self.edit(self.skill(), text[start:end], "x" * 1100)
        self.assertFails("description is 1100 characters")

    def test_unquoted_colon_in_description(self):
        self.edit(self.skill(), "description: ", "description: Note: ")
        self.assertFails("invalid in strict YAML")

    def test_stub_body(self):
        text = self.skill().read_text(encoding="utf-8")
        frontmatter = text[: text.index("\n---\n", 4) + 5]
        self.skill().write_text(frontmatter + "\n# Plan\n\nTODO\n", encoding="utf-8", newline="")
        self.assertFails("body looks like a stub")

    def test_too_many_lines(self):
        with self.skill().open("a", encoding="utf-8", newline="") as handle:
            handle.write("filler\n" * 500)
        self.assertFails("lines (keep SKILL.md under 500)")

    def test_unknown_skill_in_relationships(self):
        self.edit(self.skill(), "- **Analyze:**", "- **Frobnicate:** not a skill.\n- **Analyze:**")
        self.assertFails("names unknown skill 'frobnicate'")

    def test_missing_skill_file(self):
        self.skill("review").unlink()
        self.assertFails("missing: plugin/skills/review/SKILL.md")

    def test_marketplace_wrong_path(self):
        self.edit_json(".claude-plugin/marketplace.json",
                       lambda d: d["plugins"][0].update(source="./nowhere"))
        self.assertFails("does not point at plugin/")

    def test_codex_marketplace_wrong_path(self):
        self.edit_json(".agents/plugins/marketplace.json",
                       lambda d: d["plugins"][0]["source"].update(path="./nowhere"))
        self.assertFails("Codex: marketplace source './nowhere' does not point at plugin/")

    def test_description_drift(self):
        self.edit_json("plugin/.codex-plugin/plugin.json", lambda d: d.update(description="Drifted"))
        self.assertFails("manifest descriptions differ")

    def test_claude_version_must_match_codex_when_set(self):
        self.edit_json("plugin/.claude-plugin/plugin.json", lambda d: d.update(version="9.9.9"))
        self.assertFails("plugin versions differ")

    def test_codex_requires_valid_version(self):
        self.edit_json("plugin/.codex-plugin/plugin.json", lambda d: d.update(version="latest"))
        self.assertFails("Codex: invalid version")

    def test_license_mismatch(self):
        self.edit_json("plugin/.claude-plugin/plugin.json", lambda d: d.update(license="MIT"))
        self.assertFails("Claude manifest license mismatch")


if __name__ == "__main__":
    unittest.main()
