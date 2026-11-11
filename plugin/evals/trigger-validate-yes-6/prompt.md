---
max_turns: 1
runs: 3
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Acceptance criterion: the API must reject uploads over 10 MB. I tried a 12 MB file and got a 413. Does that validate the criterion?
