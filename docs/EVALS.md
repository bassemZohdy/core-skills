# Evals

Two kinds of case live in `plugin/evals/`, run with `claude plugin eval` (Claude Code 2.1.322).

- **Behavior cases** (16, two per skill; for example `review-clean-diff-no-manufactured-findings`): a realistic prompt aimed at something a default model may get wrong, an LLM-judged `criteria` grader, and a `skill-fired` grader.
- **Trigger cases** (48, `trigger-<skill>-yes-N` and `trigger-<skill>-no-N`; three of each per skill): a prompt that should (yes) or should not (no, a near miss that belongs to a sibling skill) load the named skill, graded only by whether the `Skill` tool was called for it.

## Running

```text
claude plugin eval ./plugin --trust-plugin -j 4 --max-cost-usd 9 --case '<glob>' --json out.json
```

Add `--ablation none` for a plugin-only run (skill-fired graders then count toward the score). Without it each case also runs a no-plugin baseline. Cases default to 3 runs (the trigger cases set 2). Output goes to `plugin/evals/results/` (ignored by git). On Windows, `--keep-temp` leaves scratch directories in `%TEMP%` that you must delete yourself.

## Results (2026-11-11)

Recorded to keep the claims below honest; the numbers are small and noisy.

**Behavior cases, with and without the plugin, 3 runs each, 16 cases, $7.01.** Criteria passed in 44 of 48 runs with the plugin and 38 of 48 without; mean delta +0.125.

| Skill | With | Without | Note |
| --- | --- | --- | --- |
| investigate | 6 / 6 | 3 / 6 | `investigate-vague-need` 3/3 vs 0/3: the clearest gain |
| analyze | 4 / 6 | 3 / 6 | failures in both arms are answers that add fix suggestions |
| evaluate | 6 / 6 | 5 / 6 | |
| review | 4 / 6 | 3 / 6 | `review-clean-diff-no-manufactured-findings` 1/3 vs 0/3 |
| define, plan, research, validate | all pass | all pass | ceiling: the default model already passes these cases, so they cannot show a gain |

**Trigger cases, plugin only, 2 runs each, 48 cases, about $9.4 over three runs of the suite.** All 24 near-miss cases passed (the skill did not fire when it should not). Of 24 should-fire cases, 21 fired in both runs; the other three never fired: `trigger-review-yes-1` (a bug review of a one-line function), `trigger-validate-yes-2` (a test result with one skipped test, asking whether a criterion can be marked validated), and `trigger-validate-yes-3` (a JSON document checked against two stated requirements). In each the model answered directly.

**Limits.** Three queries per case type per skill, not the roughly 20 recommended; two runs per case; judged by a model. A zero delta on a case does not mean a skill is useless, only that the case is too easy for the baseline.
