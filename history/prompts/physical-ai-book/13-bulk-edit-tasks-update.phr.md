---
id: 13
title: Bulk Edit Tasks Update
stage: tasks
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-specify-project-ai
user: SarwatMajeed24
command: /sp.tasks
labels: [bulk-edit, tasks-update, phase-standardization]
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
--bulk-edit
Do all of these at once:

• Change every folder reference from "docs/01-intro/" → "docs/01-intro-and-why-humanoids/"
  and apply the same pattern to all 6 chapters exactly as in the plan

• Update T047 to this exact wording:
  "Create complete README.md containing:
   – Project title & description
   – One-click preview button (GitHub Codespaces badge)
   – Full Contribution Guide section (how to run, add chapters, etc.)"

• Delete or merge T060 (now redundant)

• Standardise phase count everywhere to exactly 5 phases (remove any mention of 6 phases)
```

## Response snapshot

Completed all requested bulk edits to tasks.md:

1. Verified folder references were already using correct naming pattern (docs/01-intro-and-why-humanoids/, etc.)
2. Updated T047 with exact specified wording about README.md content
3. Removed redundant T060 task which was now covered by updated T047
4. Merged Phase 6 (Polish & Cross-Cutting Concerns) into Phase 5, standardizing to exactly 5 phases
5. Updated Dependencies section to reflect 5-phase structure instead of 6 phases

All changes maintain the integrity of the task structure while meeting the specified requirements.

## Outcome

- ✅ Impact: Tasks now follow 5-phase structure with updated README requirements
- 🧪 Tests: Task structure validated and consistent
- 📁 Files: Updated specs/001-specify-project-ai/tasks.md with all changes
- 🔁 Next prompts: Ready for continued development with standardized phases
- 🧠 Reflection: Successfully consolidated to 5 phases as requested

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All changes applied correctly
- Prompt variant (if applicable): Bulk edit command
- Next experiment (smallest change to try): Proceed with implementation using updated tasks