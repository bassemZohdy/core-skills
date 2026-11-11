# Install smoke test

Run after a change to manifests or marketplaces, and before tagging a release. Use a scratch config directory so your own setup is untouched: set `CLAUDE_CONFIG_DIR` (Claude Code) or `CODEX_HOME` (Codex) to a new empty directory for the commands below, and delete it afterwards. Codex warns that it cannot create PATH aliases when `CODEX_HOME` is under a temp directory; the install still works.

## Claude Code

```text
claude plugin marketplace add <path-or-owner/repo>
claude plugin install core-skills@core-skills
claude plugin list
```

Expect: the plugin is `enabled`, and eight `skills/<name>/SKILL.md` files exist under `<config>/plugins/cache/core-skills/core-skills/<version>/`. With no `version` in the manifest, the version shown is the source commit's short SHA. To see the registered names in a session, run `claude -p --plugin-dir ./plugin --output-format stream-json --verbose --max-turns 1 "ok"` and read the `skills` list in the `init` event: eight `core-skills:<name>` entries and no bare `plan` or `review`.

## Codex

```text
codex plugin marketplace add <path-or-owner/repo>
codex plugin list
codex plugin add core-skills@core-skills
codex plugin list
```

Expect: `core-skills@core-skills` shows `installed, enabled` at version `0.1.0`, and eight `skills/<name>/SKILL.md` files plus `assets/icon.svg` under `<CODEX_HOME>/plugins/cache/core-skills/core-skills/0.1.0/`. Invoking a skill (`$plan`) needs a signed-in Codex, which a scratch home does not have; run `codex exec '$plan ...'` in your real config, then run `codex plugin remove` and `codex plugin marketplace remove` to undo it.

## Record

Write the date, host versions, source used (local path or GitHub), and the result in the release checklist.

## Results

| Date | Host | Source | Result |
| --- | --- | --- | --- |
| 2026-11-11 | Claude Code 2.1.322 | GitHub `bassemZohdy/core-skills` at f856710 | installed, enabled, 8 skills, version = commit SHA |
| 2026-11-11 | Claude Code 2.1.322 | installed copy from GitHub at 000d08f, loaded with `--plugin-dir` | `/core-skills:plan` ran and followed the skill |
| 2026-11-11 | Codex 0.167.0 | GitHub `bassemZohdy/core-skills` at f856710 | installed, enabled, 0.1.0, 8 skills and icon |
| 2026-11-11 | Codex 0.167.0 | GitHub, real Codex config, removed afterwards | `$plan` ran: Codex said it would use the plan skill and returned the three requested lines |
