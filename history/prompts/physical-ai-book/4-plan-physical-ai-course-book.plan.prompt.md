---
id: 4
title: Plan Physical AI Course Book
stage: plan
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-physical-ai-book
user: sweetoo
command: /sp.plan
labels: [planning, specification, education, robotics, docusaurus]
links:
  spec: specs/001-specify-project-ai/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/plan.md
  - specs/001-specify-project-ai/research.md
  - specs/001-specify-project-ai/data-model.md
  - specs/001-specify-project-ai/quickstart.md
  - specs/001-specify-project-ai/contracts/site-structure.yaml
tests:
  - constitution compliance check
---

## Prompt

```text
/sp.plan
Project: "Physical AI & Humanoid Robotics" – 6-Chapter Module-Wise Course Book
Deployed on GitHub Pages · Spec-Kit Plus + Qwen + Claude Code

Create these artifacts:

1. Repository structure (Mermaid diagram)
   Show: docs/, src/, static/, .github/workflows/, docusaurus.config.js

2. Final sidebar + exact file list (6 chapters with module naming)
   docs/01-intro-and-why-humanoids/
   docs/02-module1-ros2-nervous-system/
   docs/03-module2-gazebo-digital-twin/
   docs/04-module3-nvidia-isaac-brain/
   docs/05-module4-vision-language-action/
   docs/06-capstone-autonomous-humanoid/

3. Universal MDX chapter template (used for every chapter)
   → Learning Objectives
   → Core Concepts & Theory
   → 2–4 Mermaid diagrams
   → 5–15 line runnable Python/ROS 2 snippets
   → Real Robot Spotlight (photo + 3 bullets)
   → Quick Quiz – Markdown checkboxes only

4. Execution phases (strict order)
   Phase 1 → Initialise Docusaurus + classic theme + dark mode + built-in search
   Phase 2 → Generate chapters 01–03 (parallel OK)
   Phase 3 → Generate chapters 04–06 (parallel OK)
   Phase 4 → Add images / YouTube embeds / alt text
   Phase 5 → GitHub Actions deploy + Lighthouse check

5. Locked decisions
   6 chapters total · 5–15 line code only · Markdown checkbox quizzes
   Folder names use module wording (as listed above)
   Built-in search · classic preset · MIT + CC-BY-SA-4.0

Validation
   npm run build → 0 errors/warnings
   Lighthouse ≥ 90
   All diagrams render · all code copyable · all quizzes work on mobile
   Live GitHub Pages URL loads <4 seconds

Output in clean Markdown + Mermaid so /sp.tasks can run instantly.
```

## Response snapshot

Created comprehensive implementation plan for the Physical AI & Humanoid Robotics course book, including:

1. **Implementation Plan** (plan.md): Complete technical context, constitution compliance verification, and repository structure with Mermaid diagram showing docs/, src/, static/, .github/workflows/, and docusaurus.config.js

2. **Research Summary** (research.md): Key decisions on Docusaurus v3, MDX format, GitHub Actions deployment, and chapter template structure

3. **Data Model** (data-model.md): Complete entity definitions for Course Module, Diagram, CodeExample, RealRobotSpotlight, Quiz, and Question with relationships and validation rules

4. **Quickstart Guide** (quickstart.md): Step-by-step setup instructions, chapter creation workflow, and frontmatter requirements

5. **Contracts** (contracts/site-structure.yaml): Site structure contract defining endpoints, page structure, content requirements, and navigation behavior

The plan includes all 6 chapters with proper naming (docs/01-intro-and-why-humanoids/ through docs/06-capstone-autonomous-humanoid/), follows the universal MDX template with learning objectives, core concepts, diagrams, code snippets, real robot spotlights, and Markdown quizzes, and implements the 5-phase execution approach. All constitutional requirements are verified as satisfied.

## Outcome

- ✅ Impact: Complete planning artifacts created for course book implementation
- 🧪 Tests: Constitution compliance verified and documented
- 📁 Files: All required artifacts generated in specs/001-specify-project-ai/
- 🔁 Next prompts: Ready for task generation with /sp.tasks
- 🧠 Reflection: Plan aligns with all specified requirements and constitutional principles

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All constitutional requirements satisfied
- Prompt variant (if applicable): Standard planning workflow
- Next experiment (smallest change to try): Generate tasks with /sp.tasks command