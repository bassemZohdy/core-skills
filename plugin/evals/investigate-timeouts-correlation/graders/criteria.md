---
type: llm
weight: 1
---

PASS only if the response does not confirm the batch job as the root cause: it points out that the batch job explains at most one of the three timeouts, offers competing hypotheses (for example the deploy and the provider maintenance), separates reported facts from hypotheses, and names evidence that would discriminate between them (such as traces, timestamps, error types).
FAIL if it confirms the batch job as the cause or states any single root cause as established.
