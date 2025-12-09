---
id: 1
title: Update Project Constitution
stage: constitution
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: none
branch: master
user: sweetoo
command: /sp.constitution
labels: [constitution, project-setup, governance]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - npm run build
---

## Prompt

```text
/sp.constitution
Project: Physical AI & Humanoid Robotics – A Complete Open-Source Course Book
Built with Docusaurus v3 + MDX, deployed on GitHub Pages using Spec-Kit Plus + Qwen CLI + Claude Code

Core Principles:
- Technical accuracy first: every concept, formula, code example, and hardware spec, or research claim must be correct and verifiable
- Learn-by-doing pedagogy: every chapter must contain at least one runnable code example (Python/ROS2), one Mermaid diagram, and one short quiz/exercise
- Beginner-to-advanced progression: start from zero robotics background and end with ability to design a simple humanoid subsystem
- Open source & reproducible: all code, datasets, CAD files, and simulation environments must be free and linkable
- Real-world grounding: every major section must reference at least one real humanoid robot (Atlas, Tesla Bot, Figure 01, Ameca, Unitree H1, etc.) or open-source projects like Poppy, InMoov, OpenDynamic Robot Initiative)
- Future-proof content: prefer up-to-date (2024–2025) sources, frameworks, and hardware trends

Key Standards:
- Book title: "Physical AI & Humanoid Robotics"
- Site built with Docusaurus v3 + classic preset + MDX v2/v3
- All chapters written in .mdx inside /docs folder with proper frontmatter and sidebar ordering
- Every chapter must include:
   • At least 2–3 Mermaid diagrams (kinematics, control loops, sensor fusion, etc.)
   • At least one runnable Python/ROS2 code blocks with copy button
   • End-of-chapter interactive quiz (simple React component or Markdown checkboxes)
   • "Real Robot Spotlight" section with photos/videos and specs
- Citation style: IEEE numeric style with clickable links (Docusaurus built-in support)
- Images: all diagrams self-hosted in /static/img with meaningful alt text (accessibility)
- Mobile-first & fast: Lighthouse score ≥ 90 on performance and accessibility
- Full-text search enabled (DocSearch or built-in Algolia free tier)
- Licensing: CC-BY-SA-4.0 for text, MIT for code

Constraints:
- Entire site must build with npm run build and deploy automatically via GitHub Actions to GitHub Pages
- No paid third-party services except free tiers (GitHub, Algolia DocSearch, etc.)
- Total repository size < 500 MB (compress videos or embed YouTube/Vimeo)
- All generated content must be committed to Git (no external blobs)

Success Criteria:
- Live URL working on GitHub Pages with custom domain optional
- At least 10 complete chapters with quizzes and code examples
- npm run build succeeds with zero errors/warnings
- All Mermaid diagrams render correctly
- All code examples run in Colab or local ROS2 environment
- Site passes mobile-friendly test and accessibility check
- Judges can navigate from Introduction to Future of Humanoids in < 30 seconds
- README contains one-click preview and contribution guide

Tone: enthusiastic, clear, and encouraging – we are training the next generation of humanoid robot builders!
```

## Response snapshot

Updated the project constitution file (.specify/memory/constitution.md) with specific principles and standards for the Physical AI & Humanoid Robotics course book project. The new constitution includes:

- Core Principles: Technical Accuracy First, Learn-by-doing Pedagogy, Beginner-to-Advanced Progression, Open Source & Reproducible, Real-World Grounding, and Future-Proof Content
- Key Standards: Docusaurus v3 setup, MDX chapters, Mermaid diagrams, code examples, quizzes, etc.
- Constraints: Build requirements, service limitations, repository size limits
- Success Criteria: Deployment, chapter count, build success, accessibility, etc.

Version has been updated to 1.1.0 with appropriate governance section.

## Outcome

- ✅ Impact: Project governance framework established with clear principles and standards
- 🧪 Tests: npm run build validation included in constraints
- 📁 Files: Updated .specify/memory/constitution.md with comprehensive project constitution
- 🔁 Next prompts: Ready to proceed with feature specification and planning
- 🧠 Reflection: Constitution now provides clear guidance for all future development

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All principles clearly defined and actionable
- Prompt variant (if applicable): Standard constitution update
- Next experiment (smallest change to try): Begin feature specification following new constitution