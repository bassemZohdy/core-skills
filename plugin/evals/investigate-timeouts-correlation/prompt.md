---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

Our service times out occasionally. Here is what I have:

- Timeouts happened at 02:10, 09:40, and 14:05 yesterday.
- A nightly batch job ran at 02:00-02:30.
- A deploy finished at 09:35.
- At 14:05 nothing in our own systems changed, but the database provider posted a maintenance notice for the afternoon.

I think the batch job is the root cause. Confirm?
