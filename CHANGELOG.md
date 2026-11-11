# Changelog

All notable changes to this repository. No release has been tagged yet; the first tag is planned after the P0 and P1 tasks in `TODO.md`.

## Unreleased

### Added
- `docs/PROVENANCE.md`: upstream commit, per-skill blob hashes, and status.
- `.gitattributes` normalizing line endings to LF.
- `tests/test_check.py`: tests for the checker.
- `scripts/progress.py`: progress bar for `TODO.md`.
- `plugin/evals/`: first eval case (`validate-incomplete`).
- `.github/dependabot.yml` for GitHub Actions updates.
- `AGENTS.md` / `CLAUDE.md` contributor notes, `TODO.md` review findings and plan.
- Claude plugin manifest: `license`, `repository`, `keywords`.

### Changed
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
