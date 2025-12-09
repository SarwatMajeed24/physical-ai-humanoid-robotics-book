---
id: 11
title: Bulk Update Code Snippet Wording
stage: tasks
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-specify-project-ai
user: SarwatMajeed24
command: /sp.tasks
labels: [bulk-update, consistency, documentation]
links:
  spec: specs/001-specify-project-ai/spec.md
  plan: specs/001-specify-project-ai/plan.md
  tasks: specs/001-specify-project-ai/tasks.md
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/tasks.md
tests:
  - consistency check
---

## Prompt

```
--bulk-update
Search all tasks for the text "5-10 line" or "5–10 line" and replace with:
"5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)"
Do the same in any test descriptions or user stories.
Confirm when complete.
```

## Response snapshot

Completed bulk update of code snippet wording across tasks.md file. Updated three instances:
1. Task T020: Changed "Add 5-10 line Python/ROS2 code snippet" to "Add 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)"
2. Independent test description: Updated from "5-10 line Python/ROS2 code snippets" to "5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)"
3. Task T030: Changed "Add 5-10 line Python/ROS2 code snippet" to "Add 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)"

All instances in the main project files have been updated to maintain consistency with the standardized terminology.

## Outcome

- ✅ Impact: All code snippet references now use consistent terminology across tasks
- 🧪 Tests: Consistency check - all references updated to same wording
- 📁 Files: Updated specs/001-specify-project-ai/tasks.md with consistent wording
- 🔁 Next prompts: Ready for continued development with consistent specs
- 🧠 Reflection: Maintained consistency across all project documentation

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All instances updated consistently
- Prompt variant (if applicable): Bulk update command
- Next experiment (smallest change to try): Proceed with implementation using consistent specs