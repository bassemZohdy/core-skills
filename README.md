# core-skills

Independent, platform-agnostic skills for clear, evidence-based work with AI agents. Each works on its own; none requires a particular model, subagent, or orchestration engine.

| Skill | Use it to |
| --- | --- |
| `define` | Keep technical terms and concept boundaries accurate; settle what a term means. |
| `research` | Find and assess external evidence, check current status, fact-check claims. |
| `analyze` | Explain components, relationships, causes, and trade-offs of a subject. |
| `evaluate` | Judge one option, or compare options, against explicit criteria. |
| `review` | Critique a document, code, design, or plan for defects and risks. |
| `validate` | Check a result against requirements or acceptance criteria and report pass, fail, or incomplete. |
| `plan` | Turn a goal into a sequenced plan with deliverables, dependencies, and risks. |
| `investigate` | Discover what is unknown about a need, incident, or question through targeted inquiry. |

## Install

> Installing from the GitHub marketplace was tested on Claude Code 2.1.322 and Codex 0.167.0 (2026-11-11) with the CLI commands in [docs/INSTALL.md](docs/INSTALL.md). The in-session slash forms below and Codex's interactive `/plugins` browser were not tested.

Claude Code:

```text
/plugin install core-skills --marketplace bassemZohdy/core-skills
```

Codex:

```text
codex plugin marketplace add bassemZohdy/core-skills
```

then open `/plugins` in the Codex CLI.

## Use

- Claude Code: plugin skills are namespaced, for example `/core-skills:plan`. Skills also load automatically when a task matches their description.
- Codex: mention a skill with `$`, for example `$plan`, or use `/skills`.

## Layout

Canonical skill definitions are in `plugin/skills/<name>/SKILL.md`; both the Claude plugin (`plugin/.claude-plugin/`) and the Codex plugin (`plugin/.codex-plugin/`) point at that one directory. Do not copy the definitions into platform-specific folders.

## Development

```text
python scripts/check.py                      # structural and packaging checks
python -m unittest discover -s tests         # tests for the checker
```

The checker does not launch Claude or Codex and cannot prove behavioral compatibility. Open work is tracked in [TODO.md](TODO.md); release gates are in [docs/RELEASE-CHECKLIST.md](docs/RELEASE-CHECKLIST.md).

## Provenance and status

The skills were migrated from `bassemZohdy/ai-skills` main and may since have been edited here; see [docs/PROVENANCE.md](docs/PROVENANCE.md). Cross-agent behavioral evaluation is still pending.

## License

Licensed under the Apache License 2.0 ([LICENSE](LICENSE)). Each `SKILL.md` declares `license: Apache-2.0`, and both plugin manifests carry the same identifier. Maintained by Bassem Zohdy (author in the plugin manifests).
