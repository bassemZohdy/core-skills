# Provenance

The eight skills in `plugin/skills/` were migrated from [`bassemZohdy/ai-skills`](https://github.com/bassemZohdy/ai-skills) `main`.

## Upstream pin

| | |
| --- | --- |
| Upstream repository | `bassemZohdy/ai-skills` |
| Upstream commit compared | `851945057f97be8fc13fd3d7bc6467200f7dc8a2` (2026-11-10) |
| Comparison method | Git blob hashes of each `SKILL.md` (and `LICENSE`) against this repository at `7849588`; checked 2026-11-11 |
| Result at `7849588` | All eight skills and `LICENSE` identical to upstream |

The upstream repository has not been changed by this migration.

## Per-skill record

| Skill | Upstream blob (`SKILL.md`) | Status here |
| --- | --- | --- |
| analyze | `905e6b63f8e6cb81ca855164ed92756feb9da41e` | Edited here (TODO T06/T07): description rewritten as a trigger |
| define | `de569d6b65bcc02bad917eb3b140f7642b69ba35` | Edited here (TODO T06/T07/T08): description rewritten as an on-demand trigger |
| evaluate | `70b2912aac7c40366d23464308ad410f6a7ec426` | Edited here (TODO T01: removed upstream-only references; T06/T07: description) |
| investigate | `c0cfc157180736009a06ab10df1cd11417d08a2a` | Edited here (TODO T01: removed reference to a non-existent Interview skill; T06/T07: description) |
| plan | `0c4b632338d53118f3dfad8e07cbd63ccdb66446` | Edited here (TODO T06/T07): description rewritten as a trigger |
| research | `cc5bea16921dbd2b77bb2988dc77a9d8eb307d18` | Edited here (TODO T01: removed upstream-only references; T06/T07: description) |
| review | `51cbe0c3ccdce587630565e24a60f881ff049761` | Edited here (TODO T06/T07): description rewritten as a trigger |
| validate | `82817581c798104852f1a6d47c5d2de89d4c6268` | Edited here (TODO T06/T07): description rewritten as a trigger |

`LICENSE` (Apache-2.0) is identical to upstream: `d645695673349e3947e8e5ae42332d0ac3164cd7`.

From this point the skills in this repository may diverge from upstream. Update the "Status here" column whenever a skill is edited.

## Origin of each skill

- Analyze, Research, Evaluate, Plan and Investigate originated in merged upstream PRs #21–#24.
- Define, Review and Validate were already present on upstream `main`.

## Review status

Editorial and structural review was done upstream. Cross-agent behavioral evaluation has not been done; see `TODO.md` (T11–T14) and `docs/RELEASE-CHECKLIST.md`.
