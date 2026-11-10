"""Dependency-free structural and packaging validation for core-skills."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugin"
NAMES = ("define", "research", "analyze", "evaluate", "review", "validate", "plan", "investigate")
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def load_json(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")
        return {}

for name in NAMES:
    file = PLUGIN / "skills" / name / "SKILL.md"
    try:
        contents = file.read_text(encoding="utf-8")
    except OSError:
        errors.append(f"missing: {file.relative_to(ROOT)}")
        continue
    match = re.match(r"\A---\n(.*?)\n---\n", contents, re.S)
    check(match is not None, f"{name}: invalid frontmatter")
    if match:
        metadata = match.group(1)
        for key in ("name", "description", "license"):
            check(re.search(rf"(?m)^{key}:\s*\S", metadata) is not None, f"{name}: missing {key}")
        check(re.search(rf"(?m)^name:\s*{re.escape(name)}\s*$", metadata) is not None,
              f"{name}: name mismatch")
        check(re.search(r"(?m)^license:\s*Apache-2\.0\s*$", metadata) is not None,
              f"{name}: unexpected license")
    check(len(contents.strip()) > 600, f"{name}: suspiciously short definition")

skills_dir = PLUGIN / "skills"
actual = {p.name for p in skills_dir.iterdir() if p.is_dir()} if skills_dir.exists() else set()
check(actual == set(NAMES), f"skill folder mismatch: {sorted(actual ^ set(NAMES))}")

claude = load_json(PLUGIN / ".claude-plugin" / "plugin.json")
codex = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
market_claude = load_json(ROOT / ".claude-plugin" / "marketplace.json")
market_codex = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
for label, manifest in (("Claude", claude), ("Codex", codex)):
    check(manifest.get("name") == "core-skills", f"{label}: wrong plugin name")
    check(bool(manifest.get("description")), f"{label}: missing description")
    check(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", ""))), f"{label}: invalid version")
check(claude.get("version") == codex.get("version"), "plugin versions differ")
check(codex.get("skills") == "./skills/", "Codex skill path must be ./skills/")
check(codex.get("license") == "Apache-2.0", "Codex manifest license mismatch")
check(claude.get("license") == "Apache-2.0", "Claude manifest license mismatch")
for label, marketplace in (("Claude", market_claude), ("Codex", market_codex)):
    check(marketplace.get("name") == "core-skills", f"{label} marketplace name mismatch")
    entries = marketplace.get("plugins", [])
    check(isinstance(entries, list) and len(entries) == 1, f"{label}: expected one plugin entry")
    if isinstance(entries, list) and len(entries) == 1 and isinstance(entries[0], dict):
        entry = entries[0]
        check(entry.get("name") == "core-skills", f"{label}: entry name mismatch")
        source = entry.get("source")
        expected = "./plugin" if label == "Claude" else {"source": "local", "path": "./plugin"}
        check(source == expected, f"{label}: wrong marketplace path")
check((ROOT / "LICENSE").exists(), "missing LICENSE")
check((ROOT / "docs" / "INSTALL.md").exists(), "missing install instructions")
if errors:
    print("FAIL: " + str(len(errors)) + " packaging errors")
    for error in errors:
        print(" - " + error)
    sys.exit(1)
print("PASS: 8 skill definitions, metadata, licenses, manifests, marketplaces, paths, and install docs")
