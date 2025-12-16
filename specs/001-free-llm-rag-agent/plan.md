# Implementation Plan: Free LLM RAG Agent for Physical AI Book

**Branch**: `001-free-llm-rag-agent` | **Date**: 2025-12-16 | **Spec**: [Free LLM RAG Agent Spec](/specs/001-free-llm-rag-agent/spec.md)
**Input**: Feature specification from `/specs/001-free-llm-rag-agent/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a RAG (Retrieval-Augmented Generation) agent using Google Gemini 1.5 Flash (free tier) and Qdrant Cloud vector database to provide accurate answers about the Physical AI & Humanoid Robotics book content. The system includes a toggleable chat widget with selected text support, built with FastAPI backend and integrated into the book's frontend.

## Technical Context

**Language/Version**: Python 3.11, JavaScript/TypeScript for frontend components
**Primary Dependencies**: FastAPI, Google Gemini SDK, Qdrant Python client, React 18, Docusaurus v3
**Storage**: Qdrant Cloud vector database for document embeddings, in-memory session storage
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application (Docusaurus-based documentation site)
**Project Type**: Web application (frontend + backend)
**Performance Goals**: <5 seconds response time for typical queries, support concurrent users
**Constraints**: Must use only free LLM services (Google Gemini 1.5 Flash), no OpenAI APIs, local testing compatibility
**Scale/Scope**: Single book content, multiple concurrent users accessing RAG agent

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

The implementation aligns with the project constitution:
- Uses open-source technologies where possible
- Maintains clean architecture with separation of concerns
- Follows security best practices
- Implements proper error handling
- Uses only free LLM services as required

## Project Structure

### Documentation (this feature)

```text
specs/001-free-llm-rag-agent/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── models/
│   │   └── chat.py      # Chat request/response models
│   ├── services/
│   │   ├── rag_chain.py # Gemini-based RAG implementation
│   │   ├── embedding.py # Gemini embedding service
│   │   └── vector_store.py # Qdrant integration
│   └── api/
│       └── chat.py      # Chat API endpoints
└── tests/
    └── unit/

frontend/
├── src/
│   └── components/
│       └── RagChat.js   # Toggleable chat widget component
└── tests/
    └── unit/

src/
└── components/
    └── RagChat.js       # Legacy path for Docusaurus integration
```

**Structure Decision**: Web application structure with separate backend (FastAPI) and frontend (React component) to handle RAG processing and user interface respectively. The backend handles Gemini API calls and Qdrant integration, while the frontend provides the toggleable chat widget integrated into the Docusaurus documentation site.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
