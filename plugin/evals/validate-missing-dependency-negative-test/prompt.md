---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

We have a negative test that checks our config loader rejects an invalid config. I ran it and want to know if the "invalid config is rejected" criterion is validated.

Command: `pytest tests/test_config_rejects_invalid.py -q`
Output:
```
E   ModuleNotFoundError: No module named 'yaml'
1 error in 0.12s
```
It exited non-zero, and the test is supposed to expect a non-zero exit when the config is invalid, so that is the rejection we wanted. Can I mark it validated?
