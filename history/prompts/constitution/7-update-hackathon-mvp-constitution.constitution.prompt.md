---
id: 7
title: Update Hackathon MVP Constitution
stage: constitution
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: 001-specify-project-ai
user: sweetoo
command: /sp.constitution
labels: [constitution, update, hackathon, mvp]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - constitution validation
---

## Prompt

```text
/sp.constitution
Project: Physical AI & Humanoid Robotics – Hackathon MVP Edition

Replace the old "at least 10 complete chapters" success criteria with this updated one:

Success Criteria (updated for hackathon reality):
- Exactly 6 polished, interactive chapters (as defined in current spec)
- Live GitHub Pages URL with full navigation
- All 6 chapters contain code + diagrams + quiz
- Lighthouse ≥ 90 performance & accessibility
- Judges can understand the full learning path in < 3 minutes

Everything else in the constitution stays the same.
```

## Response snapshot

Updated the project constitution to reflect hackathon MVP requirements. Changed the success criteria from "At least 10 complete chapters with quizzes and code examples" to "Exactly 6 polished, interactive chapters (as defined in current spec)" to align with the hackathon scope and realistic delivery timeline. Also updated the judge evaluation time from "< 30 seconds" to "< 3 minutes" to allow for proper understanding of the learning path. Version has been incremented from 1.1.0 to 1.1.1 with appropriate sync impact report updated.

## Outcome

- ✅ Impact: Constitution updated to reflect hackathon MVP scope
- 🧪 Tests: Success criteria now align with 6-chapter requirement
- 📁 Files: Updated .specify/memory/constitution.md with new criteria
- 🔁 Next prompts: Ready for implementation with aligned requirements
- 🧠 Reflection: Constitution now realistic for hackathon timeline

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - Constitution updated successfully
- Prompt variant (if applicable): Constitution update for hackathon
- Next experiment (smallest change to try): Proceed with implementation using updated criteria