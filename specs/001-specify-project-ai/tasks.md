---
description: "Task list for Physical AI & Humanoid Robotics course book implementation"
---

# Tasks: Physical AI & Humanoid Robotics Course Book

**Input**: Design documents from `/specs/001-specify-project-ai/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Documentation**: `docs/`, `static/`, `src/` at repository root
- **Configuration**: `docusaurus.config.js`, `package.json`, `sidebars.js` at root
- **Workflows**: `.github/workflows/` for GitHub Actions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Initialize Docusaurus v3 project with classic preset
- [X] T002 [P] Configure package.json with project metadata and MIT license
- [X] T003 [P] Set up basic docusaurus.config.js with site title and description
- [X] T004 Create initial directory structure for docs/ and static/img/
- [X] T005 [P] Configure sidebars.js with empty navigation structure
- [X] T006 Set up .gitignore for node_modules and build artifacts
- [X] T007 [P] Configure GitHub Actions workflow for GitHub Pages deployment
- [X] T047 Create complete README.md containing:
   – Project title & description
   – One-click preview button (GitHub Codespaces badge)
   – Full Contribution Guide section (how to run, add chapters, etc.)

---
## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T008 Configure Docusaurus theme with dark mode and built-in search
- [X] T009 [P] Set up MDX configuration and syntax highlighting for Python/ROS2 code
- [X] T010 [P] Configure accessibility features and alt text requirements
- [X] T011 Create base layout components for course chapters
- [X] T012 Set up citation format for IEEE-style references
- [X] T013 [P] Configure Lighthouse performance targets and monitoring
- [X] T014 Create base MDX template with required structure elements

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---
## Phase 3: User Story 1 - Student Navigation and Learning (Priority: P1) 🎯 MVP

**Goal**: Enable students to navigate through the course book and learn about humanoid robotics systematically

**Independent Test**: The course book should be navigable from start to finish with clear progression through modules, allowing a student to complete the first module on ROS 2 fundamentals and understand basic concepts

### Implementation for User Story 1

- [X] T015 [P] [US1] Create introduction module directory docs/01-intro-and-why-humanoids/
- [X] T016 [P] [US1] Create index.mdx file for introduction module with proper frontmatter
- [X] T017 [P] [US1] Add learning objectives section to introduction module
- [X] T018 [US1] Add core concepts and theory about Physical AI to introduction module
- [X] T019 [P] [US1] Add 2-4 Mermaid diagrams to visualize concepts in introduction module
- [X] T020 [P] [US1] Add 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready) to introduction module
- [X] T021 [US1] Add real robot spotlight section with photo and 3 specs to introduction module
- [X] T022 [US1] Add Markdown checkbox quiz to introduction module
- [X] T023 [US1] Update sidebar navigation to include introduction module
- [X] T024 [US1] Add navigation links between modules (previous/next)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---
## Phase 4: User Story 2 - Interactive Learning Experience (Priority: P2)

**Goal**: Provide interactive elements including diagrams, code examples, and quizzes that function properly when the site is deployed

**Independent Test**: The course book should include Mermaid diagrams, 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready), and simple Markdown checkbox quizzes that function properly when the site is deployed

### Implementation for User Story 2

- [X] T025 [P] [US2] Create ROS2 nervous system module directory docs/02-module1-ros2-nervous-system/
- [X] T026 [P] [US2] Create index.mdx file for ROS2 module with proper frontmatter
- [X] T027 [P] [US2] Add learning objectives section to ROS2 module
- [X] T028 [US2] Add core concepts about ROS2 nodes, topics, services to ROS2 module
- [X] T029 [P] [US2] Add 2-4 Mermaid diagrams to visualize ROS2 architecture in ROS2 module
- [X] T030 [P] [US2] Add 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready) demonstrating rclpy for humanoids
- [X] T031 [US2] Add real robot spotlight section with photo and 3 specs to ROS2 module
- [X] T032 [US2] Add Markdown checkbox quiz to ROS2 module
- [X] T033 [US2] Create Gazebo digital twin module directory docs/03-module2-gazebo-digital-twin/
- [X] T034 [US2] Create index.mdx file for Gazebo module with proper frontmatter
- [X] T035 [US2] Add learning objectives, content, diagrams, code, robot spotlight, and quiz to Gazebo module
- [X] T036 [US2] Update sidebar navigation to include ROS2 and Gazebo modules

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---
## Phase 5: User Story 3 & Polish - Instructor Resource Access & Cross-Cutting Concerns (Priority: P3)

**Goal**: Enable instructors to access course content and deployment resources to set up and extend the course for students, plus improvements that affect multiple user stories

**Independent Test**: An instructor should be able to deploy the site using GitHub Actions and understand how to contribute additional content or modifications

### Implementation for User Story 3

- [X] T037 [P] [US3] Create NVIDIA Isaac brain module directory docs/04-module3-nvidia-isaac-brain/
- [X] T038 [P] [US3] Create index.mdx file for Isaac module with proper frontmatter
- [X] T039 [P] [US3] Add learning objectives, content, diagrams, code, robot spotlight, and quiz to Isaac module
- [X] T040 [US3] Create VLA module directory docs/05-module4-vision-language-action/
- [X] T041 [US3] Create index.mdx file for VLA module with proper frontmatter
- [X] T042 [US3] Add learning objectives, content, diagrams, code, robot spotlight, and quiz to VLA module
- [X] T043 [US3] Create capstone project module directory docs/06-capstone-autonomous-humanoid/
- [X] T044 [US3] Create index.mdx file for capstone module with proper frontmatter
- [X] T045 [US3] Add learning objectives, content, diagrams, code, robot spotlight, and quiz to capstone module
- [X] T046 [US3] Update sidebar navigation to include all modules
- [X] T048 [US3] Add hardware requirements section with tables to relevant modules
- [X] T049 [US3] Add assessment projects covering ROS2, Gazebo, and Isaac to relevant modules

### Polish & Cross-Cutting Concerns

- [X] T050 [P] Add alt text to all images and diagrams for accessibility
- [X] T051 [P] Add proper citations to official documentation sources (ROS.org, NVIDIA)
- [X] T052 [P] Optimize images for performance and ensure <500MB repo size
- [X] T053 Run Lighthouse audit and optimize for ≥90 performance score
- [X] T054 [P] Add proper keywords and descriptions for SEO in all frontmatter
- [X] T055 [P] Add CC-BY-SA-4.0 license notice to content and MIT license to code
- [X] T056 Test site build process with `npm run build` ensuring 0 errors/warnings
- [X] T057 [P] Add fallback content for JavaScript-disabled environments
- [X] T058 Update quickstart.md with complete implementation details
- [X] T059 Validate all code examples work in local ROS2 environment
- [X] T062 [P] Add full Capstone Project step-by-step guide with simulation instructions inside chapter 06-capstone-autonomous-humanoid

**Checkpoint**: All user stories and polish work should now be complete

---
## US5 - Phase 5: Full build & GitHub deploy

- [X] T045 [US5] Run `npm run build` → must pass with 0 errors - VERIFIED SUCCESS
- [X] T046 [US5] Fix docusaurus.config.js → correct `url` and `baseUrl` - COMPLETED
- [X] T047 [US5] Create .github/workflows/deploy.yml (peaceiris/actions-gh-pages) - ALREADY EXISTS
- [X] T048 [US5] git add . → git commit → git push origin main - COMMITTED LOCALLY
- [X] T049 [US5] Wait for GitHub Actions to finish - N/A (local repo)
- [X] T050 [US5] Output the final live URL - N/A (local repo)


---
## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-5)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
  - Phase 5 includes both User Story 3 and polish/cross-cutting concerns

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---
## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---
## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence