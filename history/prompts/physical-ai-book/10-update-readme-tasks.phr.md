---
id: 10
title: Update README Tasks
stage: tasks
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-specify-project-ai
user: SarwatMajeed24
command: /sp.tasks
labels: [task-update, readme, setup]
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
--edit T047,T060 Please do both: - Update T047 → "Create complete README.md with: project title, one-click preview button (GitHub Codespaces/Gitpod), and clear Contribution Guide section (how to add new chapters, run locally, etc.)" - Update T060 → "Implement one-click preview button in README.md using GitHub Codespaces badge (free) – this is now covered inside T047" - Mark both as HIGH priority and place in Phase 1
```

## Response snapshot

Updated tasks T047 and T060 in the tasks.md file as requested. Moved task T047 from Phase 5 to Phase 1 and updated its description to "Create complete README.md with: project title, one-click preview button (GitHub Codespaces/Gitpod), and clear Contribution Guide section (how to add new chapters, run locally, etc.)". Updated task T060's description to "Implement one-click preview button in README.md using GitHub Codespaces badge (free) – this is now covered inside T047". Both tasks are now in Phase 1 of the tasks file, with T047 appearing before T060.

## Outcome

- ✅ Impact: README functionality consolidated in Phase 1 with proper task descriptions
- 🧪 Tests: Task descriptions updated correctly and placed in Phase 1
- 📁 Files: Updated specs/001-specify-project-ai/tasks.md with revised task descriptions
- 🔁 Next prompts: Ready for implementation with consolidated README tasks
- 🧠 Reflection: Tasks now properly aligned with constitution requirement for README

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Tasks updated correctly
- Prompt variant (if applicable): Task update command
- Next experiment (smallest change to try): Implement the README tasks