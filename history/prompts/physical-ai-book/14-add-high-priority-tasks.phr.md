---
id: 14
title: Add High Priority Tasks
stage: tasks
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-specify-project-ai
user: SarwatMajeed24
command: /sp.tasks
labels: [task-addition, high-priority, content]
links:
  spec: specs/001-specify-project-ai/spec.md
  plan: specs/001-specify-project-ai/plan.md
  tasks: specs/001-specify-project-ai/tasks.md
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/tasks.md
tests:
  - task validation
---

## Prompt

```
--add
Add these three new HIGH-priority tasks at the end:

T061 – Add Hardware Requirements & Lab Setup Options section with tables (in chapter 06 or separate page)
T062 – Write complete Capstone Project step-by-step guide with simulation instructions
T063 – Add Assessments & Grading Rubric section (ROS project, Gazebo sim, final capstone)

Mark all three as belonging to chapter 06 or a new "Extras" chapter if preferred.
```

## Response snapshot

Added three new HIGH-priority tasks to the tasks.md file:
- T061: Add Hardware Requirements & Lab Setup Options section with tables
- T062: Write complete Capstone Project step-by-step guide with simulation instructions
- T063: Add Assessments & Grading Rubric section (ROS project, Gazebo sim, final capstone)

All tasks were added to the "Polish & Cross-Cutting Concerns" section of Phase 5 with [P] parallel markers, positioned after the existing T059 task. The tasks address content requirements that were mentioned in the spec but not fully detailed in previous tasks.

## Outcome

- ✅ Impact: Three new high-priority content tasks added to complete the course book
- 🧪 Tests: Tasks follow proper format and placement criteria
- 📁 Files: Updated specs/001-specify-project-ai/tasks.md with new tasks
- 🔁 Next prompts: Ready for implementation with additional content tasks
- 🧠 Reflection: Tasks address hardware, capstone, and assessment requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Tasks added correctly
- Prompt variant (if applicable): Task addition command
- Next experiment (smallest change to try): Implement the new content tasks