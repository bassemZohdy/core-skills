---
type: llm
weight: 1
---

PASS only if the response produces a usable sequenced plan (for example discovery, schema and data conversion, dual-run or validation, cutover, rollback) with acceptance criteria or checks for the important steps, flags the irreversible cutover step with a rollback or go/no-go criterion, and does not invent a team size, specific calendar dates, week-by-week durations presented as facts, or a budget. Any estimate must be labelled as an assumption, and missing inputs should be listed as open questions or assumptions.
FAIL if it states invented durations or dates as facts, assigns named people or headcount, or gives no rollback or verification.
