---
max_turns: 2
runs: 2
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Our acceptance criteria: the export returns CSV with headers, and handles 10,000 rows in under 5 seconds. All 14 tests passed but I never timed the 10,000-row case. Is it done?
