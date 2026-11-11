---
type: llm
weight: 1
---

PASS only if the response notices that A needs B, B needs C, and C needs A form a cycle, so no valid ordering exists as stated, and flags it rather than presenting a clean sequence; it should suggest ways to break the cycle (for example reviewing a staging or pre-production deployment, or splitting the approval) as options for the user to decide.
FAIL if it outputs a linear A-B-C ordering as valid without flagging the cycle.
