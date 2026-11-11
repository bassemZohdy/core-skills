---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

Turn this into an ordered plan:

- Task A (deploy service) needs Task B (provision database) finished first.
- Task B (provision database) needs Task C (get network access approved) finished first.
- Task C (get network access approved) needs the service from Task A to be deployed, because security reviews the running service.

Give me the final sequence.
