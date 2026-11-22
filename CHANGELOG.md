# Changelog

All notable changes to this repository. The first tag is `v0.1.0`.

## Unreleased

### Added
- Cursor: `.cursor-plugin/marketplace.json` and `plugin/.cursor-plugin/plugin.json`.
- Agent Plugins 1.0 manifest `plugin/plugin.json`, read by GitHub Copilot (VS Code, Copilot CLI) and Cursor; Copilot also reads the existing `.claude-plugin/marketplace.json`.
- Google Antigravity: `plugin/.antigravity-plugin/plugin.json`, valid against Antigravity's published schema.
- `scripts/check.py` validates the new manifests and marketplace; install notes for Cursor, Copilot, Antigravity, OpenClaw, Gemini CLI and skills-only hosts (OpenCode, Windsurf, Cline, Goose, Amp) in `docs/INSTALL.md` (none of these hosts was run).

### Changed
- `evaluate` and `validate` descriptions extended after trigger-eval misses (see `docs/EVALS.md`).

## 0.1.0 - 2026-11-11

### Added
- CI validates every skill with the official `skills-ref` validator (pinned commit).
- `plugin/evals/`: 16 behavior cases and 128 trigger cases; `docs/EVALS.md` records how to run them and the 2026-11-11 results.
- `docs/SMOKE-TEST.md`: install smoke test for Claude Code and Codex in a scratch config directory.
- `plugin/assets/icon.svg`, referenced as the Codex `composerIcon` and `logo`.
- Each of `plan` and `evaluate` gained a `references/` template; every skill has a worked example.
- `docs/PROVENANCE.md`: upstream commit, per-skill blob hashes, and status.
- `.gitattributes` normalizing line endings to LF.
- `tests/test_check.py`: tests for the checker.
- `scripts/progress.py`: progress bar for `TODO.md`.
- `plugin/evals/`: first eval case (`validate-incomplete`).
- `.github/dependabot.yml` for GitHub Actions updates.
- `AGENTS.md` / `CLAUDE.md` contributor notes, `TODO.md` review findings and plan.
- Claude plugin manifest: `license`, `repository`, `keywords`.

### Changed
- `investigate` shortened again (about 930 words of body); about 20 default-behavior restatements removed across skills; `validate` and `review` descriptions extended after trigger-eval misses.
- CI also installs a pinned Claude Code and runs `claude plugin validate` on the marketplace and the plugin.
- All skills use the same section names (`Output`, `Relationship to other skills`, `Examples`), enforced by `scripts/check.py`, which also checks Codex listing limits.
- Codex manifest: shorter `shortDescription`, icons; Codex marketplace gained `interface.displayName`.
- `docs/INSTALL.md`: name-collision behavior recorded from a real check.
- All skills: descriptions rewritten as triggers with sibling boundaries (`define` is now on-demand); symmetric Relationships sections limited to confusable neighbors; one untrusted-content sentence; removed author-facing disclaimers and the `analyze` Specializations section.
- `plan`, `review`, `validate`, `research`, `evaluate`, `investigate`, `define`: content gaps closed (default severity scale, intermittent result class, verdict definitions, UNKNOWN-gate handling, no-user fallback, native plan mode, plan file writing); compact worked examples added; `investigate` shortened from about 1,520 to 1,130 words; `define` decision gates split into bullets.
- `scripts/check.py`: relationships must be reciprocated; README skill table must match `plugin/skills`.
- `evaluate`, `research`, `investigate`: removed references to artifacts that exist only upstream.
- `scripts/check.py`: rewritten into testable functions; enforces Agent Skills limits, marketplace source resolution, and manifest consistency.
- CI runs the checker tests and triggers on `push` to `main` and on pull requests.
- Claude plugin manifest no longer pins `version`, so installs are expected to follow the source commit (unverified).
- One description string across manifests and marketplaces; the skill count is no longer hardcoded.
- README and `docs/INSTALL.md` rewritten; marketplace installation is marked untested.

### Fixed
- README, install docs, and release checklist no longer contradict each other on licensing (Apache-2.0).
