---
max_turns: 2
runs: 2
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Check whether every step in this rollout plan is complete: 1. migrate schema (done) 2. deploy (done) 3. smoke test (not run).
