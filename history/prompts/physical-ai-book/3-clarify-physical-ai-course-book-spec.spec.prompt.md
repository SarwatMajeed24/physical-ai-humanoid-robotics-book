---
id: 3
title: Clarify Physical AI Course Book Spec
stage: spec
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-physical-ai-book
user: sweetoo
command: /sp.clarify
labels: [clarification, specification, education, robotics]
links:
  spec: specs/001-specify-project-ai/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/spec.md
tests:
  - specification review
---

## Prompt

```text
/sp.clarify
My book specification is at specs/001-book-spec/spec.md (the one I just created for "Physical AI & Humanoid Robotics" Docusaurus course book).

Please analyze the entire spec and answer only the following questions:

1. AMBIGUOUS TERMS
   - What exactly counts as one "chapter"? (top-level sidebar item vs every .mdx file vs every weekly section?)
   - What depth is expected for "runnable Python/ROS 2 code block"? (5-line hello-world, or full working node with launch file?)
   - What does "interactive quiz" mean? (simple Markdown checkboxes, multiple-choice with no JS, or real React component with scoring?)

2. MISSING ASSUMPTIONS
   - Exact chapter/folder structure and file naming convention? (e.g. docs/01-intro/, docs/02-ros2-fundamentals/ or module-based?)
   - Should every chapter have frontmatter? If yes, which fields are mandatory (title, sidebar_label, sidebar_position, description, keywords)?
   - Should we use Docusaurus classic preset or a custom theme? Dark mode on by default?
   - Do we need versioned documentation (multiple versions) or just "latest"?

3. INCOMPLETE REQUIREMENTS
   - For the Hardware Guide chapter: do we need exact up-to-date prices (Dec 2025) and purchase links, or just approximate ranges?
   - For the Capstone chapter: should we include a complete ready-to-run GitHub repo link + Colab notebook, or only step-by-step instructions?
   - Search plugin: exactly Algolia DocSearch (free application needed) or built-in simple search is acceptable for MVP?
   - Do we need a custom 404 page, custom favicon, custom domain setup instructions?

4. SCOPE & TIME CONFLICTS (critical for hackathon)
   - Current spec asks for 15–18 chapters with 1500–3000 words each → impossible in a 48-hour hackathon. What is the real MVP scope (number of complete chapters) to still have a winning demo?
   - Which chapters are absolutely required for a believable, impressive demo if time runs out?
   - Can we reduce some chapters to short "stub" pages with diagrams + quiz only?

For each gap/question, clearly mark:
- CRITICAL → blocks planning or implementation
- HIGH → strongly affects quality or hackathon score
- NICE-TO-HAVE → can be decided later

List everything in numbered/bulleted form so I can answer quickly.
```

## Response snapshot

Completed clarification session for the Physical AI & Humanoid Robotics course book specification. Five critical questions were addressed:

1. **MVP Scope**: Reduced from 15-18 chapters to 5-6 core chapters (Overview + 4 modules) for the 48-hour hackathon constraint
2. **Code Example Depth**: Specified 5-10 line Python/ROS2 code snippets instead of full working nodes
3. **Interactive Quizzes**: Defined as simple Markdown checkboxes rather than complex React components
4. **Folder Structure**: Established sequential numbering with descriptive names (docs/01-intro/, docs/02-ros2-fundamentals/, etc.)
5. **Search Functionality**: Confirmed built-in simple search is acceptable for MVP rather than Algolia DocSearch

All clarifications were integrated directly into the specification document in the "Clarifications" section, with corresponding updates to functional requirements and user stories to ensure consistency. The specification now has clear, actionable requirements for the planning phase.

## Outcome

- ✅ Impact: Critical ambiguities resolved that would have blocked implementation
- 🧪 Tests: All clarifications result in testable, specific requirements
- 📁 Files: Updated specs/001-specify-project-ai/spec.md with clarifications
- 🔁 Next prompts: Ready to proceed to planning phase with clear requirements
- 🧠 Reflection: Clarifications significantly improve specification clarity and implementation feasibility

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All clarifications properly integrated
- Prompt variant (if applicable): Standard clarification workflow
- Next experiment (smallest change to try): Proceed to planning phase with clarified spec