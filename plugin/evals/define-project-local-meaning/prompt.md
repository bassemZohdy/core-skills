---
max_turns: 6
allowed_tools: [Read, Glob, Grep, Skill]
---

Our design doc says: "A Task is a durable workflow execution: it is created when a user starts a workflow and persists until that workflow finishes. A Job is a single retryable unit of work inside a Task."

A teammate says "a Task is just a to-do item, like in Jira". Who is right for our project, and how does a Task differ from a Job?
