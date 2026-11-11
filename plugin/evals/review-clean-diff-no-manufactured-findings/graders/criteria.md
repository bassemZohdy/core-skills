---
type: llm
weight: 1
---

PASS only if the response says it found no material issues within the reviewed scope (this diff only) and does not invent defects, style nitpicks presented as problems, or speculative risks. It must not claim approval beyond the evidence, for example "production ready", "certified", or "guaranteed correct"; it may note that only this diff was reviewed and no tests were run.
FAIL if it lists problems that are not in the diff, pads with cosmetic suggestions framed as findings, or declares the change fully verified.
