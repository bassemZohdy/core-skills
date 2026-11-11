# Contributor notes

Instructions for humans and coding agents working in this repository.

- **Skills live only in `plugin/skills/<name>/SKILL.md`.** Both the Claude plugin and the Codex plugin point at that directory. Never copy definitions into platform folders.
- **Before committing, run** `python scripts/check.py` and `python -m unittest discover -s tests`. For manifest or marketplace changes also run `claude plugin validate .` and `claude plugin validate ./plugin`.
- **Editing a skill:** update its row in `docs/PROVENANCE.md` ("Status here"); the skills no longer match upstream byte for byte once edited. Frontmatter must stay flat `key: value` lines; quote a value that contains `: ` or ` #`. Keep `SKILL.md` under 500 lines and descriptions under 1024 characters (enforced by the checker).
- **Skill outline:** every skill ends with `## Outcomes` (where it has outcome states), `## Output`, `## Relationship to other skills`, and `## Examples`, using exactly those names (checked). The middle is skill-specific: `## Inputs`, `## Principles`, and a numbered `## Workflow` where the task is a sequence; define, review, and validate keep topic headings because they are not sequential.
- **Versioning:** the Claude manifest intentionally has no `version`, so installs follow the source commit (verified 2026-11-11: the installed version is the commit's short SHA). The Codex manifest requires one; keep the two consistent if the Claude one is ever added. See decision D2 in `TODO.md`.
- **Leave `LICENSE` as is** (identical to upstream) unless the maintainer decides on a copyright notice. Do not invent a year or owner.
- **Line endings are LF** (`.gitattributes`). Do not commit CRLF.
- **Do not claim** marketplace approval, install success, or behavioral quality that has not been tested. Record what was run and on which host version.
- **Open work** is tracked in `TODO.md`. Tick a task only after its stated check passes; leave partly done tasks unticked with a note. `python scripts/progress.py TODO.md` prints the progress bar and refreshes the `**Progress:**` line.
