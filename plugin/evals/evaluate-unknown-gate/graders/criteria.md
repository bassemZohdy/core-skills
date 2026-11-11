---
type: llm
weight: 1
---

PASS only if the response: (1) fails VendorB on the mandatory air-gap gate despite its top scores, and does not let a high weighted score compensate; (2) marks VendorC as UNKNOWN (or "unverified") on the gate, not as FAIL and not silently as PASS; (3) does not declare VendorC the winner outright and instead recommends VendorA conditionally or says the choice depends on verifying VendorC's offline support (VendorC scores higher, 4.0 against 3.0, only if the gate is confirmed).
FAIL if it picks VendorB, treats VendorC's missing information as failure, or treats it as passed.
