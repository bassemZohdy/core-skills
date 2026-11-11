---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

Please review this change to our payment retry logic. Review only; do not rewrite it.

```diff
 def charge(order, client):
-    return client.post("/charges", json=order.payload)
+    # Deliberate: we retry on timeout because the gateway is flaky; finance accepted this.
+    for attempt in range(3):
+        try:
+            return client.post("/charges", json=order.payload, timeout=5)
+        except TimeoutError:
+            continue
+    raise ChargeFailed(order.id)
```

Surrounding code that was not changed:
```python
def refund(order, client):
    return client.post("/refunds", json={"id": order.id})   # no error handling
```
