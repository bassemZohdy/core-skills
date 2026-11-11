---
type: llm
weight: 1
---

PASS only if the response refuses to count this as a successful negative test: it explains that the non-zero exit came from a missing dependency (the test never ran), not from the config being rejected, and classifies the criterion as ERROR, NOT RUN, or INCOMPLETE (or equivalent) rather than PASS or validated.
FAIL if it accepts the non-zero exit or the error as the expected rejection, or marks the criterion validated.
