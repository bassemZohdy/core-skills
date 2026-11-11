---
max_turns: 1
runs: 3
allowed_tools: [Read, Glob, Grep, Skill]
tags: [trigger]
---

Explain how our own retry middleware handles timeouts; the code is pasted below: def call(): for i in range(3): try: return send() except Timeout: sleep(2**i)
