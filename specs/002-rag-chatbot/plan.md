# Implementation Plan: RAG Chatbot for Physical AI Book

**Branch**: `002-rag-chatbot` | **Date**: 2025-12-16 | **Spec**: /specs/002-rag-chatbot/spec.md
**Input**: Feature specification from `/specs/002-rag-chatbot/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

Implementation of a RAG (Retrieval-Augmented Generation) chatbot for the Physical AI & Humanoid Robotics book. The system will crawl the book's sitemap, extract content from HTML/MDX pages, create embeddings using Cohere embed-english-v3.0, store them in Qdrant Cloud, and provide a FastAPI backend with a /chat endpoint. The frontend will be a React-based chat widget that integrates with the Docusaurus site, featuring a floating toggleable icon and selected text functionality.

## Technical Context

**Language/Version**: Python 3.11, JavaScript/TypeScript for frontend components
**Primary Dependencies**: FastAPI, Cohere Python SDK, Qdrant Python client, React 18, Docusaurus v3
**Storage**: Qdrant Cloud vector database (for embeddings), temporary local storage for processing
**Testing**: pytest for backend, Jest for frontend components, integration tests for RAG pipeline
**Target Platform**: Linux server (backend), Web browsers (frontend)
**Project Type**: Web (backend + frontend integration)
**Performance Goals**: <5 second response time for queries, handle 100 concurrent users
**Constraints**: <200ms p95 for API responses, must work without OpenAI (Cohere only), embeddable in Docusaurus
**Scale/Scope**: 1000+ book content chunks, 100+ concurrent users, 90% accuracy on book-related queries

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

**Technical Accuracy First**: ✅ The RAG system will provide accurate answers based on the book content, with proper retrieval-augmented generation ensuring responses are grounded in the source material.

**Learn-by-doing Pedagogy**: ✅ The chatbot will provide interactive learning opportunities, allowing students to ask questions and get immediate feedback about the book content.

**Beginner-to-Advanced Progression**: ✅ The chatbot enhances the learning experience by allowing users to ask questions at their level of understanding, supporting both beginners and advanced users.

**Open Source & Reproducible**: ⚠️ PARTIAL - The system uses Cohere (proprietary) and Qdrant Cloud (external service), but the codebase itself will be open source and the implementation will be reproducible with proper API keys.

**Real-World Grounding**: ✅ The system will work with real book content about humanoid robotics, providing practical answers based on actual course material.

**Future-Proof Content**: ✅ The architecture is designed to be maintainable and adaptable to future changes in the course content.

**GATE PASS**: The implementation plan aligns with most constitution principles, with awareness of the proprietary service dependencies that are required by the feature specification.

---

**Post-Design Review**: After Phase 1 design, the architecture maintains compliance with the constitution. The separation of backend and frontend allows for maintainable code that supports the educational goals while using the required technologies (Cohere, Qdrant Cloud) as specified in the feature requirements.

[Gates determined based on constitution file]

## Project Structure

### Documentation (this feature)

```text
specs/002-rag-chatbot/
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
├── main.py              # FastAPI application entry point
├── requirements.txt     # Python dependencies
├── src/
│   ├── models/
│   │   ├── embedding.py    # Embedding models and schemas
│   │   └── chat.py         # Chat models and schemas
│   ├── services/
│   │   ├── crawler.py      # Sitemap crawler and content extractor
│   │   ├── embedding.py    # Cohere embedding service
│   │   ├── vector_store.py # Qdrant vector store operations
│   │   └── rag_chain.py    # RAG chain implementation
│   ├── api/
│   │   ├── chat.py         # Chat endpoint implementation
│   │   └── health.py       # Health check endpoints
│   └── config/
│       └── settings.py     # Configuration and settings
└── tests/
    ├── unit/
    │   ├── test_crawler.py
    │   ├── test_embedding.py
    │   └── test_chat.py
    └── integration/
        └── test_rag_pipeline.py

frontend/
├── src/
│   ├── components/
│   │   ├── ChatWidget.jsx     # Main chat widget component
│   │   ├── ChatWindow.jsx     # Chat window UI
│   │   ├── FloatingIcon.jsx   # Floating chat icon
│   │   └── Message.jsx        # Individual message component
│   ├── services/
│   │   └── chatService.js     # API communication service
│   └── hooks/
│       └── useSelectedText.js # Hook for selected text functionality
└── tests/
    └── components/
        └── test_chatWidget.js
```

**Structure Decision**: Web application architecture selected with separate backend (FastAPI) and frontend (React components) to handle the RAG system requirements. The backend handles content crawling, embedding, and RAG processing, while the frontend provides the chat widget that integrates with the existing Docusaurus site.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Proprietary services (Cohere, Qdrant Cloud) | Feature specification requires these specific technologies | Open source alternatives would require significant additional development and may not meet performance requirements |
