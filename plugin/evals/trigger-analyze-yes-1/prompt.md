---
max_turns: 2
runs: 2
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Here are the p95 latency numbers before and after Tuesday's release: 180ms before, 360ms after, CPU flat, error rate flat, one extra DB call per request in the traces. Why did latency double?
