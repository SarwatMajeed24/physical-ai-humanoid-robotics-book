<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 1.1.1
Modified principles: None
Added sections: None
Removed sections: None
Updated sections: Success Criteria (changed from "at least 10 complete chapters" to "exactly 6 polished, interactive chapters")
Templates requiring updates: None
Follow-up TODOs: None
-->

# Physical AI & Humanoid Robotics – A Complete Open-Source Course Book Constitution

## Core Principles

### Technical Accuracy First
Every concept, formula, code example, hardware spec, and research claim must be correct and verifiable. All content must be technically accurate and factually correct with verifiable sources and citations.

### Learn-by-doing Pedagogy
Every chapter must contain at least one runnable code example (Python/ROS2), one Mermaid diagram, and one short quiz/exercise. The learning experience must be hands-on with practical implementation opportunities.

### Beginner-to-Advanced Progression
Content must start from zero robotics background and end with the ability to design a simple humanoid subsystem. The progression must be clear and accessible to beginners while advancing to complex topics.

### Open Source & Reproducible
All code, datasets, CAD files, and simulation environments must be free and linkable. The entire course must be built on open-source tools and resources that students can access and reproduce.

### Real-World Grounding
Every major section must reference at least one real humanoid robot (Atlas, Tesla Bot, Figure 01, Ameca, Unitree H1, etc.) or open-source projects like Poppy, InMoov, OpenDynamic Robot Initiative. Theory must be grounded in real implementations.

### Future-Proof Content
Prefer up-to-date (2024–2025) sources, frameworks, and hardware trends. Content must remain current and relevant with the latest developments in humanoid robotics.

## Key Standards

Book title: "Physical AI & Humanoid Robotics"
Site built with Docusaurus v3 + classic preset + MDX v2/v3
All chapters written in .mdx inside /docs folder with proper frontmatter and sidebar ordering
Every chapter must include:
   • At least 2–3 Mermaid diagrams (kinematics, control loops, sensor fusion, etc.)
   • 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)
   • End-of-chapter interactive quiz (simple React component or Markdown checkboxes)
   • "Real Robot Spotlight" section with photos/videos and specs
Citation style: IEEE numeric style with clickable links (Docusaurus built-in support)
Images: all diagrams self-hosted in /static/img with meaningful alt text (accessibility)
Mobile-first & fast: Lighthouse score ≥ 90 on performance and accessibility
Full-text search enabled (DocSearch or built-in Algolia free tier)
Licensing: CC-BY-SA-4.0 for text, MIT for code

## Constraints

Entire site must build with npm run build and deploy automatically via GitHub Actions to GitHub Pages
No paid third-party services except free tiers (GitHub, Algolia DocSearch, etc.)
Total repository size < 500 MB (compress videos or embed YouTube/Vimeo)
All generated content must be committed to Git (no external blobs)

## Success Criteria

Live URL working on GitHub Pages with custom domain optional
Exactly 6 polished, interactive chapters (as defined in current spec)
npm run build succeeds with zero errors/warnings
All Mermaid diagrams render correctly
All code examples run in Colab or local ROS2 environment
Site passes mobile-friendly test and accessibility check
Judges can understand the full learning path in < 3 minutes
README contains one-click preview and contribution guide

## Governance

All development must align with the core principles and standards. Every contribution must verify compliance with technical accuracy, learn-by-doing pedagogy, and open-source reproducibility requirements. Content changes must be validated against real-world examples and maintain beginner-to-advanced progression. All PRs/reviews must verify compliance with Docusaurus v3 standards, code examples, diagrams, and accessibility requirements.

**Version**: 1.1.1 | **Ratified**: 2025-12-09 | **Last Amended**: 2025-12-09