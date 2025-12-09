# Research Summary: Physical AI & Humanoid Robotics Course Book

## Decision: Docusaurus v3 with Classic Preset
**Rationale**: Docusaurus v3 is the latest stable version with excellent MDX support, built-in search, and GitHub Pages deployment capabilities. The classic preset provides a well-structured documentation site with sidebar navigation, which aligns with the requirement for hierarchical documentation structure.

**Alternatives considered**:
- Gatsby with MDX: More complex setup, requires more configuration
- VuePress: Different ecosystem, less familiar for React developers
- GitBook: Less customizable than Docusaurus

## Decision: MDX Format for All Chapters
**Rationale**: MDX allows combining Markdown with React components, enabling interactive elements like quizzes and custom diagrams while maintaining readability. It's well-supported in Docusaurus and allows for the required Mermaid diagrams and code examples.

**Alternatives considered**:
- Pure Markdown: Limited interactivity
- JSX files: More complex, less readable for content authors

## Decision: GitHub Actions for Deployment
**Rationale**: GitHub Actions provides seamless integration with GitHub Pages, automatic deployment on pushes to main branch, and is free for public repositories. It's the standard approach for Docusaurus sites.

**Alternatives considered**:
- Netlify: Would require additional setup and service
- Manual deployment: Error-prone and not automated

## Decision: Built-in Docusaurus Search vs Algolia
**Rationale**: Based on clarification session, built-in search is acceptable for MVP. This reduces complexity and setup time while still providing search functionality.

**Alternatives considered**:
- Algolia DocSearch: More powerful but requires application and configuration

## Decision: Chapter Template Structure
**Rationale**: The template includes all required elements from the specification: learning objectives, core concepts, diagrams, code snippets, real robot spotlights, and quizzes. This ensures consistency across all chapters while meeting the constitutional requirements.

**Template Elements**:
- Learning Objectives: Clear goals for each chapter
- Core Concepts & Theory: Educational content
- 2-4 Mermaid diagrams: Visual representations of concepts
- 5-15 line Python/ROS2 snippets: Runnable code examples
- Real Robot Spotlight: Real-world grounding with photos and specs
- Quick Quiz: Markdown checkboxes for self-assessment

## Decision: Repository Structure
**Rationale**: The structure follows Docusaurus conventions with docs/ for content, src/ for custom components, and static/ for assets. The sequential folder naming (01-intro, 02-module1, etc.) ensures proper ordering in the sidebar.

## Decision: Code Snippet Complexity
**Rationale**: 5-15 line code snippets provide educational value without excessive complexity, as clarified in the specification session. These will demonstrate key concepts without requiring complex setup.

## Decision: Quiz Format
**Rationale**: Markdown checkbox quizzes provide interactivity without requiring JavaScript, as clarified in the specification session. This keeps the implementation simple while still allowing for self-assessment.

## Decision: Performance Targets
**Rationale**: Lighthouse score ≥ 90 and < 4 second load time align with the constitutional requirements for mobile-first and fast performance. These targets ensure good user experience and accessibility.