---
id: 15
title: Update Folder Structure Spec
stage: spec
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-specify-project-ai
user: SarwatMajeed24
command: /sp.specify
labels: [spec-update, folder-structure, consistency]
links:
  spec: specs/001-specify-project-ai/spec.md
  plan: specs/001-specify-project-ai/plan.md
  tasks: specs/001-specify-project-ai/tasks.md
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/spec.md
tests:
  - specification consistency
---

## Prompt

```
Project: "Physical AI & Humanoid Robotics" – Final Hackathon MVP

Update the folder naming section to exactly this (replace any old version):

Locked folder structure (must match plan & tasks 100%):
docs/01-intro-and-why-humanoids/
docs/02-module1-ros2-nervous-system/
docs/03-module2-gazebo-digital-twin/
docs/04-module3-nvidia-isaac-brain/
docs/05-module4-vision-language-action/
docs/06-capstone-autonomous-humanoid/

Everything else in the spec stays unchanged.
```

## Response snapshot

Updated the folder naming convention in the specification to ensure 100% consistency with plan and tasks. Changed FR-005 in the Functional Requirements section from the old naming convention (docs/01-intro/, docs/02-ros2-fundamentals/, etc.) to the exact locked folder structure: docs/01-intro-and-why-humanoids/, docs/02-module1-ros2-nervous-system/, docs/03-module2-gazebo-digital-twin/, docs/04-module3-nvidia-isaac-brain/, docs/05-module4-vision-language-action/, docs/06-capstone-autonomous-humanoid/. This aligns the specification with the implementation plan and tasks.

## Outcome

- ✅ Impact: Specification now has consistent folder structure with plan and tasks
- 🧪 Tests: All documents now use matching folder naming convention
- 📁 Files: Updated specs/001-specify-project-ai/spec.md with correct structure
- 🔁 Next prompts: Ready for continued development with aligned specifications
- 🧠 Reflection: Documents now fully aligned after previous analysis findings

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Structure updated consistently
- Prompt variant (if applicable): Specification alignment command
- Next experiment (smallest change to try): Proceed with implementation using aligned specs