"""Dependency-free structural and packaging validation for core-skills.

Usage: python scripts/check.py

Checks skill frontmatter against the Agent Skills limits, the Claude and Codex
manifests and marketplace files, and consistency between them. It does not launch
Claude or Codex and cannot establish runtime behavior.
"""
from pathlib import Path
import json
import re
import sys

ROOT_DEFAULT = Path(__file__).resolve().parents[1]

NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_KEYS = ("name", "description", "license")
MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_LINES = 500
MIN_BODY_WORDS = 200
EXPECTED_LICENSE = "Apache-2.0"
PLUGIN_NAME = "core-skills"
# Bold labels that appear in relationship sections but are not skills.
NON_SKILL_TERMS = {"interview"}
RELATIONSHIP_HEADINGS = ("Boundaries", "Boundaries and integration")


def parse_frontmatter(text):
    """Return (metadata, body, error). Supports flat `key: value` scalars only."""
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if match is None:
        return None, text, "invalid frontmatter"
    metadata = {}
    for raw in match.group(1).split("\n"):
        if not raw.strip():
            continue
        line = re.match(r"([A-Za-z][\w-]*):\s*(.*)$", raw)
        if line is None:
            return None, text, f"unsupported frontmatter line: {raw[:40]!r}"
        key, value = line.group(1), line.group(2).strip()
        if key in metadata:
            return None, text, f"duplicate frontmatter key: {key}"
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        elif ": " in value or " #" in value:
            return None, text, f"unquoted value for {key!r} contains ': ' or ' #' (invalid in strict YAML)"
        metadata[key] = value
    return metadata, text[match.end():], None


def relationship_terms(body):
    """Yield bold skill-like labels from relationship/boundary sections."""
    parts = re.split(r"(?m)^#{2,3} +(.+)$", body)
    for title, text in zip(parts[1::2], parts[2::2]):
        title = title.strip()
        if "Relationship" in title or title in RELATIONSHIP_HEADINGS:
            for match in re.finditer(r"(?m)^- \*\*([A-Z][A-Za-z]+):?\*\*", text):
                yield match.group(1).lower()


def check_skills(root, errors):
    """Validate every skill directory; return the set of discovered skill names."""
    skills_dir = root / "plugin" / "skills"
    if not skills_dir.is_dir():
        errors.append("missing: plugin/skills")
        return set()
    names = {p.name for p in skills_dir.iterdir() if p.is_dir()}
    if not names:
        errors.append("no skill directories found in plugin/skills")
    bodies = {}
    for name in sorted(names):
        file = skills_dir / name / "SKILL.md"
        try:
            contents = file.read_text(encoding="utf-8")
        except OSError:
            errors.append(f"missing: plugin/skills/{name}/SKILL.md")
            continue
        metadata, body, error = parse_frontmatter(contents)
        if error:
            errors.append(f"{name}: {error}")
            continue
        bodies[name] = body
        for key in REQUIRED_KEYS:
            if not metadata.get(key):
                errors.append(f"{name}: missing {key}")
        for key in sorted(set(metadata) - ALLOWED_KEYS):
            errors.append(f"{name}: unknown frontmatter key {key!r}")
        if metadata.get("name") != name:
            errors.append(f"{name}: name mismatch ({metadata.get('name')!r})")
        if not NAME_RE.fullmatch(name) or len(name) > MAX_NAME:
            errors.append(f"{name}: name must be lowercase alphanumeric with single hyphens, at most {MAX_NAME} characters")
        description = metadata.get("description", "")
        if len(description) > MAX_DESCRIPTION:
            errors.append(f"{name}: description is {len(description)} characters (limit {MAX_DESCRIPTION})")
        if metadata.get("license") and metadata["license"] != EXPECTED_LICENSE:
            errors.append(f"{name}: unexpected license {metadata['license']!r}")
        lines = contents.count("\n") + 1
        if lines >= MAX_LINES:
            errors.append(f"{name}: {lines} lines (keep SKILL.md under {MAX_LINES})")
        if len(body.split()) < MIN_BODY_WORDS or not re.search(r"(?m)^## ", body):
            errors.append(f"{name}: body looks like a stub (needs {MIN_BODY_WORDS}+ words and a '## ' section)")
    for name, body in bodies.items():
        for term in relationship_terms(body):
            if term not in names and term not in NON_SKILL_TERMS:
                errors.append(f"{name}: relationship section names unknown skill {term!r}")
    return names


def load_json(path, root, errors):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        errors.append(f"{path.relative_to(root)}: {exc}")
        return {}


def check_marketplace(label, marketplace, root, plugin_dir, manifest_rel, errors):
    if marketplace.get("name") != PLUGIN_NAME:
        errors.append(f"{label} marketplace name mismatch")
    entries = marketplace.get("plugins", [])
    if not (isinstance(entries, list) and len(entries) == 1 and isinstance(entries[0], dict)):
        errors.append(f"{label}: expected one plugin entry")
        return
    entry = entries[0]
    if entry.get("name") != PLUGIN_NAME:
        errors.append(f"{label}: entry name mismatch")
    source = entry.get("source")
    if isinstance(source, dict):
        source = source.get("path") if source.get("source") == "local" else None
    if not (isinstance(source, str) and source.startswith("./")):
        errors.append(f"{label}: marketplace source must be a local './' path")
        return
    target = (root / source[2:]).resolve()
    if target != plugin_dir.resolve():
        errors.append(f"{label}: marketplace source {source!r} does not point at plugin/")
    elif not (target / manifest_rel).is_file():
        errors.append(f"{label}: no {manifest_rel} under {source!r}")


def check_manifests(root, errors):
    plugin_dir = root / "plugin"
    claude = load_json(plugin_dir / ".claude-plugin" / "plugin.json", root, errors)
    codex = load_json(plugin_dir / ".codex-plugin" / "plugin.json", root, errors)
    market_claude = load_json(root / ".claude-plugin" / "marketplace.json", root, errors)
    market_codex = load_json(root / ".agents" / "plugins" / "marketplace.json", root, errors)
    for label, manifest in (("Claude", claude), ("Codex", codex)):
        if manifest.get("name") != PLUGIN_NAME:
            errors.append(f"{label}: wrong plugin name")
        if not manifest.get("description"):
            errors.append(f"{label}: missing description")
        # The Claude manifest deliberately omits `version`: Claude Code docs say a pinned
        # version blocks updates until the string changes, and an omitted one lets installs
        # follow the source (commit-based for git sources; not yet verified for this
        # relative-path marketplace source). Codex requires a version.
        version_ok = (label == "Claude" and "version" not in manifest) or bool(
            re.fullmatch(r"\d+\.\d+\.\d+", manifest.get("version", "")))
        if not version_ok:
            errors.append(f"{label}: invalid version")
    if "version" in claude and claude["version"] != codex.get("version"):
        errors.append("plugin versions differ")
    if codex.get("skills") != "./skills/":
        errors.append("Codex skill path must be ./skills/")
    elif not (plugin_dir / "skills").is_dir():
        errors.append("Codex skill path ./skills/ does not exist")
    for label, manifest in (("Claude", claude), ("Codex", codex)):
        if manifest.get("license") != EXPECTED_LICENSE:
            errors.append(f"{label} manifest license mismatch")
    descriptions = {claude.get("description"), codex.get("description"),
                    market_claude.get("metadata", {}).get("description"),
                    *(e.get("description") for e in market_claude.get("plugins", []) if isinstance(e, dict))}
    if len(descriptions) != 1:
        errors.append(f"manifest descriptions differ: {len(descriptions)} distinct values")
    for key in ("repository", "keywords"):
        if claude.get(key) is None or claude.get(key) != codex.get(key):
            errors.append(f"Claude and Codex manifests differ on {key}")
    check_marketplace("Claude", market_claude, root, plugin_dir, Path(".claude-plugin/plugin.json"), errors)
    check_marketplace("Codex", market_codex, root, plugin_dir, Path(".codex-plugin/plugin.json"), errors)


def check_readme_table(root, names, errors):
    """The README skill table must list exactly the skills found in plugin/skills."""
    try:
        text = (root / "README.md").read_text(encoding="utf-8")
    except OSError:
        errors.append("missing README.md")
        return
    listed = set(re.findall(r"(?m)^\| `([a-z0-9-]+)` \|", text))
    if listed != names:
        errors.append(f"README skill table differs from plugin/skills: {sorted(listed ^ names)}")


def run_checks(root=ROOT_DEFAULT):
    """Return (errors, skill_count) for the repository at `root`."""
    root = Path(root)
    errors = []
    names = check_skills(root, errors)
    check_manifests(root, errors)
    check_readme_table(root, names, errors)
    for required in ("LICENSE", "docs/INSTALL.md"):
        if not (root / required).is_file():
            errors.append(f"missing {required}")
    return errors, len(names)


def main():
    errors, count = run_checks()
    if errors:
        print(f"FAIL: {len(errors)} packaging errors")
        for error in errors:
            print(" - " + error)
        return 1
    print(f"PASS: {count} skill definitions, metadata, licenses, manifests, marketplaces, paths, and install docs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
