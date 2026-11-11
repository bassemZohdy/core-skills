---
max_turns: 2
runs: 2
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Audit this SQL for problems: SELECT * FROM orders WHERE customer_id = '' + id + '';
