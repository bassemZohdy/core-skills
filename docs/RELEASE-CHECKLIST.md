# Release checklist

- [x] Create a single repository and plugin identity: `core-skills`.
- [x] Preserve the reviewed `define`, `review`, and `validate` definitions from `ai-skills`.
- [x] Scaffold the other five skills.
- [x] Replace five initial placeholders with their existing upstream implementations from merged PRs #21–#24.
- [ ] Complete behavioral evaluations against realistic tasks and review cross-skill boundaries.
- [ ] Add automated behavior/evaluation coverage beyond structural checks.
- [x] Confirm plugin installation on supported Claude and Codex versions: Claude Code 2.1.322 and Codex 0.167.0 on Windows, from the GitHub source, 2026-11-11 (CLI install, and one skill invoked on each host; see `docs/SMOKE-TEST.md`).
- [x] Decide and verify project-wide licensing and attribution (Apache-2.0; `LICENSE` identical to upstream; README states license and author).
- [ ] Publish only after release checks pass.
- [x] Versioning: the Claude manifest intentionally has no `version`; verified 2026-11-11 that installs take the source commit's short SHA as the version. The Codex manifest requires one and stays at `0.1.0`. Revisit when tagging the first release.
- [x] Baseline acted on: 3-run with/without run (16 cases, $7.01), plugin 44/48 vs baseline 38/48 criteria passes; see `docs/EVALS.md`.
- [x] Trigger descriptions rewritten (T06-T08); 48 trigger cases, 2 runs: all 24 near-misses passed, 21 of 24 should-fire cases fired in both runs (`docs/EVALS.md`).
