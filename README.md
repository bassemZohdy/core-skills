# core-skills

Eight independent, platform-agnostic reusable skills: define, research, analyze, evaluate, review, validate, plan, investigate.

## Layout

Canonical skill definitions are in `plugin/skills/<name>/SKILL.md`. The Claude plugin metadata is in `plugin/.claude-plugin/plugin.json`. Codex and compatible hosts can load the same skill directories.

## Installation

For Claude Code, use the local plugin rooted at `plugin/` or copy `plugin/skills/*` to `~/.claude/skills/`. For Codex and other Agent Skills hosts, copy the skill directories to `~/.agents/skills/` or the corresponding configured location. Marketplace publishing has not been verified.

## Principles

Each skill works independently; no skill requires a specific agent model, advisor, subagent, or orchestration engine. Delegation and parallelism are optional. Execute, Deliver, and Submit remain candidates, not included core skills.

## Migration status

This is a pre-release migration. Define, Review, and Validate preserve their existing reviewed definitions from `bassemZohdy/ai-skills` including their Apache-2.0 headers. The other five are initial drafts pending deeper review. The source repository is unchanged. No repository-wide license is asserted until provenance and licensing are reviewed.

Run `python3 scripts/check.py` for structural checks; this does not prove behavioral compatibility.
