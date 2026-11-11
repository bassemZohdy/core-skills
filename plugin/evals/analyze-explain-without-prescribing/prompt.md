---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

Analyze where the time goes in our CI pipeline. Timings from the last run:

- checkout: 20s
- dependency install: 4m 10s
- unit tests: 6m 30s (4 test files take 5m of that)
- build: 2m
- upload artifacts: 40s
Total: 13m 40s.

I only want to understand it for now. We have not decided to change anything.
