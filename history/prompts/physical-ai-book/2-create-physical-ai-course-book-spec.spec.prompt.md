---
id: 2
title: Create Physical AI Course Book Spec
stage: spec
date: 2025-12-09
surface: agent
model: Claude Sonnet 4.5
feature: physical-ai-book
branch: 001-physical-ai-book
user: sweetoo
command: /sp.specify
labels: [specification, education, robotics, docusaurus]
links:
  spec: specs/001-specify-project-ai/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-specify-project-ai/spec.md
  - specs/001-specify-project-ai/checklists/requirements.md
tests:
  - specification review
---

## Prompt

```text
/sp.specify
Project: AI/Spec-Driven Book Creation for "Physical AI & Humanoid Robotics" – A Comprehensive Open-Source Course Book
Built with Docusaurus v3 + MDX, deployed on GitHub Pages using Spec-Kit Plus + Qwen CLI + Claude Code integration

Target Audience: Engineering students, AI enthusiasts, and robotics hobbyists with basic Python knowledge, aiming to bridge digital AI skills to physical embodied intelligence; suitable for capstone courses or self-study.

Focus: Embodied AI systems in the physical world, emphasizing humanoid robotics through simulation and deployment; cover principles, tools (ROS 2, Gazebo, Unity, NVIDIA Isaac), and integration of LLMs for vision-language-action (VLA) workflows.

Book Structure and Content Requirements:
- Title: "Physical AI & Humanoid Robotics"
- Overview Section: Introduce Physical AI, embodied intelligence, and the shift from digital to physical AI; include "Why Physical AI Matters" with real-world humanoid examples (e.g., Atlas, Tesla Bot, Unitree H1).
- Modules as Main Chapters (4 primary modules, expanded via weekly breakdown):
  - Module 1: The Robotic Nervous System (ROS 2) – Cover nodes, topics, services, rclpy integration, URDF for humanoids.
  - Module 2: The Digital Twin (Gazebo & Unity) – Physics simulation, sensor modeling (LiDAR, IMUs), high-fidelity rendering.
  - Module 3: The AI-Robot Brain (NVIDIA Isaac™) – Isaac Sim for synthetic data, Isaac ROS for VSLAM, Nav2 for bipedal navigation.
  - Module 4: Vision-Language-Action (VLA) – LLM-robotics convergence, voice-to-action with OpenAI Whisper, cognitive planning for natural language tasks.
- Weekly Breakdown as Sub-Chapters or Sections:
  - Weeks 1-2: Foundations of Physical AI, sensor systems.
  - Weeks 3-5: ROS 2 fundamentals, package building.
  - Weeks 6-7: Gazebo setup, URDF/SDF, Unity integration.
  - Weeks 8-10: NVIDIA Isaac SDK, reinforcement learning, sim-to-real.
  - Weeks 11-12: Humanoid kinematics, bipedal locomotion, manipulation.
  - Week 13: Conversational robotics with GPT integration, multi-modal interactions.
- Capstone Project Section: Guide for building an autonomous humanoid simulation (voice command, path planning, object manipulation).
- Assessments Section: Detail projects like ROS 2 package dev, Gazebo sim, Isaac perception pipeline, and capstone sim.
- Hardware Requirements Section: Cover "Digital Twin" Workstation (RTX GPU, Ubuntu), Edge Kits (Jetson Orin), Robot Options (Unitree Go2/G1, Hiwonder), and Cloud Alternatives (AWS g5 instances); include tables for components, prices, and architecture summary.
- Learning Outcomes: List key skills like mastering ROS 2, simulating in Gazebo/Unity, developing with Isaac, integrating LLMs.

Docusaurus Site Features:
- Hierarchical docs structure: /docs/overview.mdx, /docs/module1/ros2.mdx, etc., with sidebar navigation and versioned docs.
- Interactive Elements: Embed Mermaid diagrams for kinematics/control loops, code blocks with Prism highlighting (Python/ROS2 snippets), quizzes via MDX React components or checkboxes, embedded videos/YouTube for robot demos.
- Additional Pages: Blog for updates, search plugin (Algolia free tier), custom theme for accessibility (WCAG-compliant).
- User Stories:
  - As a student, I can navigate modules sequentially and run code examples in-browser (e.g., via Colab embeds).
  - As a learner, I can visualize simulations with diagrams and understand hardware needs through tables.
  - As an instructor, I can deploy the site and extend it with GitHub contributions.

Success Criteria:
- At least 15 chapters/sections covering all modules, weeks, and hardware details.
- Site deploys successfully to GitHub Pages with GitHub Actions workflow.
- All content verifiable with citations (IEEE style) to official docs (ROS.org, NVIDIA developer sites).
- Interactive elements functional: Diagrams render, code copyable, quizzes interactive.
- Meets educational goals: Readers can set up a basic ROS 2 humanoid sim after completion.
- Lighthouse score ≥90 for performance, accessibility, and SEO.

Constraints:
- Tech Stack: Docusaurus v3, MDX for content, no external paid services beyond free tiers.
- Content Length: Each chapter 1500-3000 words, total site optimized for fast load (<2s per page).
- Sources: Official documentation, open-source repos (e.g., ROS 2 tutorials, Isaac examples), recent (2023+) research on embodied AI.
- Timeline: MVP complete within hackathon timeframe (e.g., 48 hours), iterable via Spec-Kit commands.
- Open-Source: MIT license for code, CC-BY-SA for text; repo size <500MB.

Not Building:
- Actual hardware setups or physical robots (focus on simulations and descriptions).
- Comprehensive code repositories (provide snippets, not full repos).
- Vendor-specific comparisons beyond course-recommended options.
- Ethical discussions on AI robotics (separate resource).
- Live cloud integrations (describe, don't implement).
```

## Response snapshot

Created comprehensive feature specification for the "Physical AI & Humanoid Robotics" course book. The specification includes:

- Three prioritized user stories covering student learning, interactive experience, and instructor access
- Ten functional requirements covering course content, navigation, interactive elements, deployment, citations, accessibility, hardware requirements, and assessments
- Five key entities (Course Module, Chapter, Interactive Element, Assessment, Hardware Requirement)
- Eight measurable success criteria including chapter count, deployment success, interactive functionality, learning outcomes, performance metrics, and verification standards

The specification adheres to the constitutional principles of technical accuracy, learn-by-doing pedagogy, and real-world grounding, with clear measurable outcomes and testable requirements.

## Outcome

- ✅ Impact: Comprehensive course book specification established with clear user journeys and measurable outcomes
- 🧪 Tests: All functional requirements include testable acceptance scenarios
- 📁 Files: Created spec.md and requirements checklist in specs/001-specify-project-ai/
- 🔁 Next prompts: Ready for planning phase with clear requirements and success criteria
- 🧠 Reflection: Specification balances comprehensive coverage with clear, testable requirements

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS - All requirements are specific, testable, and measurable
- Prompt variant (if applicable): Standard feature specification
- Next experiment (smallest change to try): Proceed to planning phase with current spec