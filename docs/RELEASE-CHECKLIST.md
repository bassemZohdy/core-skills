# Release checklist

- [x] Create a single repository and plugin identity: `core-skills`.
- [x] Preserve the reviewed `define`, `review`, and `validate` definitions from `ai-skills`.
- [x] Scaffold the other five skills.
- [x] Replace five initial placeholders with their existing upstream implementations from merged PRs #21–#24.
- [ ] Complete behavioral evaluations against realistic tasks and review cross-skill boundaries.
- [ ] Add automated behavior/evaluation coverage beyond structural checks.
- [ ] Confirm plugin installation on supported Claude and Codex versions.
- [x] Decide and verify project-wide licensing and attribution (Apache-2.0; `LICENSE` identical to upstream; README states license and author).
- [ ] Publish only after release checks pass.
- [ ] Versioning: the Claude manifest intentionally has no `version` so installs are expected to follow the source commit (unverified for this relative-path source; decision D2 in `TODO.md`); the Codex manifest requires one and stays at `0.1.0`. Revisit when tagging the first release.
- [ ] Act on the baseline (2026-11-11, 16 cases, 1 run per arm, $2.27): mean delta 0.00, skill fired in 6 of 16 with-arm runs; see `TODO.md` T12.
