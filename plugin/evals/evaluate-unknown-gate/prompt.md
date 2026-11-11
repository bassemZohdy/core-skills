---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

We must choose a log platform. Mandatory requirement: it must support fully air-gapped (offline) deployment. Weighted criteria: query speed 50%, cost 30%, ease of use 20%.

- VendorA: docs state offline deployment is supported. Scores (1-5): speed 3, cost 3, ease 3.
- VendorB: docs state it requires a cloud connection at all times. Scores: speed 5, cost 5, ease 5.
- VendorC: docs say nothing about offline deployment either way. Scores: speed 4, cost 4, ease 4.

Which one should we pick?
