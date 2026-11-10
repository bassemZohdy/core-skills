# core-skills

Independent, platform-agnostic reusable skills: define, research, analyze, evaluate, review, validate, plan, investigate.

## Layout

Canonical skill definitions are in `plugin/skills/<name>/SKILL.md`. The Claude plugin metadata is in `plugin/.claude-plugin/plugin.json`. Codex and compatible hosts can load the same skill directories.

## Installation

For Claude Code, use the local plugin rooted at `plugin/` or copy `plugin/skills/*` to `~/.claude/skills/`. For Codex and other Agent Skills hosts, copy the skill directories to `~/.agents/skills/` or the corresponding configured location. Marketplace installation (Claude and Codex) is documented in [docs/INSTALL.md](docs/INSTALL.md) but has not yet been tested end to end, and marketplace publishing has not been verified.

## Principles

Each skill works independently; no skill requires a specific agent model, advisor, subagent, or orchestration engine. Delegation and parallelism are optional. Execute, Deliver, and Submit remain candidates, not included core skills.

## Migration status

The eight skill definitions were migrated from `bassemZohdy/ai-skills` main and may since have been edited here. See [docs/PROVENANCE.md](docs/PROVENANCE.md) for the upstream commit, per-skill status, and review status. Cross-agent behavioral evaluation remains pending.

Run `python3 scripts/check.py` for structural checks; this does not prove behavioral compatibility.

## License

Licensed under the Apache License 2.0 ([LICENSE](LICENSE)). Each `SKILL.md` declares `license: Apache-2.0`, and both plugin manifests carry the same identifier. Maintained by Bassem Zohdy (author in the plugin manifests). The skills were migrated from `bassemZohdy/ai-skills`, which uses the same license; see [docs/PROVENANCE.md](docs/PROVENANCE.md).
