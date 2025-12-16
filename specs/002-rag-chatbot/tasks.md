# Implementation Tasks: RAG Chatbot for Physical AI Book

**Feature**: RAG Chatbot with Cohere embeddings and Qdrant Cloud
**Branch**: `002-rag-chatbot`
**Input**: Implementation plan and feature specification

## Phase 1: Setup and Project Initialization

- [X] T001 Create backend directory structure: `backend/`, `backend/src/`, `backend/src/models/`, `backend/src/services/`, `backend/src/api/`, `backend/src/config/`, `backend/tests/`, `backend/tests/unit/`, `backend/tests/integration/`
- [X] T002 Create frontend directory structure: `frontend/`, `frontend/src/`, `frontend/src/components/`, `frontend/src/services/`, `frontend/src/hooks/`, `frontend/tests/`, `frontend/tests/components/`
- [X] T003 Create backend requirements.txt with FastAPI, Cohere, qdrant-client, python-dotenv, beautifulsoup4, lxml dependencies
- [X] T004 Create frontend package.json with React, Docusaurus dependencies and basic configuration
- [X] T005 [P] Create backend main.py with basic FastAPI app initialization
- [X] T006 Create backend config/settings.py with environment variable loading for Cohere, Qdrant, and sitemap URL

## Phase 2: Foundational Components

- [X] T007 Create BookContentChunk model in backend/src/models/embedding.py with id, url, title, content, embedding, section, timestamps
- [X] T008 Create Chat and Message models in backend/src/models/chat.py with session_id, message_id, role, content, context_chunks, selected_text
- [X] T009 Create Qdrant vector store service in backend/src/services/vector_store.py with initialization and connection methods
- [X] T010 Create Cohere embedding service in backend/src/services/embedding.py with embed method and error handling
- [X] T011 Create sitemap crawler service in backend/src/services/crawler.py with sitemap parsing and content extraction methods
- [X] T012 Create health check API endpoints in backend/src/api/health.py with GET /health and GET /status

## Phase 3: User Story 1 - Basic Chat with Book Content (Priority: P1)

**Goal**: Enable users to ask questions about book content and receive accurate answers based on book material

**Independent Test**: Can be fully tested by asking questions about book content and verifying the chatbot provides accurate, contextually relevant answers based on the book material.

- [X] T013 [US1] Implement content crawling functionality in backend/src/services/crawler.py to fetch all pages from sitemap
- [X] T014 [P] [US1] Implement HTML/MDX content extraction in backend/src/services/crawler.py with BeautifulSoup
- [X] T015 [P] [US1] Implement content chunking (1000 tokens) in backend/src/services/crawler.py with RecursiveCharacterTextSplitter
- [X] T016 [US1] Implement Cohere embedding generation in backend/src/services/embedding.py for content chunks
- [X] T017 [US1] Implement Qdrant collection creation and storage of embedded chunks in backend/src/services/vector_store.py
- [X] T018 [US1] Create RAG chain service in backend/src/services/rag_chain.py with retrieve and generate methods
- [X] T019 [US1] Implement chat API endpoint POST /chat in backend/src/api/chat.py with query processing
- [X] T020 [P] [US1] Create chat service in frontend/src/services/chatService.js with API communication methods
- [X] T021 [US1] Create basic ChatWindow component in frontend/src/components/ChatWindow.jsx with message display
- [X] T022 [US1] Create FloatingIcon component in frontend/src/components/FloatingIcon.jsx with toggle functionality
- [X] T023 [US1] Create ChatWidget component in frontend/src/components/ChatWidget.jsx integrating all chat components
- [X] T024 [US1] Test basic chat functionality with sample book questions

## Phase 4: User Story 3 - Embedded Chat Widget (Priority: P1)

**Goal**: Provide a toggleable chat widget that doesn't interfere with reading experience but is accessible when needed

**Independent Test**: Can be fully tested by verifying the chat widget appears as a floating icon, can be toggled open/closed, and is responsive across different screen sizes.

- [X] T025 [US3] Enhance FloatingIcon component with proper CSS styling and positioning in frontend/src/components/FloatingIcon.jsx
- [X] T026 [US3] Add responsive design to ChatWidget component in frontend/src/components/ChatWidget.jsx for mobile/tablet
- [X] T027 [US3] Implement proper positioning and z-index management for the chat widget
- [X] T028 [US3] Add smooth open/close animations to the chat widget
- [X] T029 [US3] Implement conversation state management in ChatWidget component
- [X] T030 [US3] Create Message component in frontend/src/components/Message.jsx with proper styling
- [X] T031 [US3] Integrate ChatWidget with Docusaurus Layout in the main site
- [X] T032 [US3] Test widget responsiveness across different screen sizes and browsers

## Phase 5: User Story 2 - Selected Text Context (Priority: P2)

**Goal**: Enable users to select specific text on the page and ask questions about that text with it used as context

**Independent Test**: Can be fully tested by selecting text on a book page, opening the chat, and verifying that the selected text is used as context for the response.

- [X] T033 [US2] Create useSelectedText hook in frontend/src/hooks/useSelectedText.js with window.getSelection() implementation
- [X] T034 [US2] Integrate selected text capture with ChatWidget component in frontend/src/components/ChatWidget.jsx
- [X] T035 [US2] Modify POST /chat endpoint to accept and use selected_text parameter in backend/src/api/chat.py
- [X] T036 [US2] Update RAG chain to incorporate selected text as additional context in backend/src/services/rag_chain.py
- [X] T037 [US2] Test selected text functionality with various content selections and queries

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T038 Add proper error handling and validation throughout backend services
- [X] T039 Implement rate limiting and request validation for API endpoints
- [X] T040 Add logging and monitoring to backend services
- [ ] T041 Create comprehensive tests for all backend services and API endpoints
- [ ] T042 Create comprehensive tests for all frontend components
- [ ] T043 Add proper TypeScript definitions if converting from JavaScript
- [ ] T044 Optimize performance with embedding caching and efficient retrieval
- [X] T045 Update documentation and README with setup instructions
- [X] T046 Perform end-to-end testing with real book content and user scenarios
- [X] T047 Deploy backend service and integrate with Docusaurus frontend

## Dependencies

- **User Story 1 (P1)**: Foundational components must be completed first (T007-T012)
- **User Story 3 (P1)**: Depends on basic chat functionality (T019-T023 completed)
- **User Story 2 (P2)**: Depends on basic chat and widget functionality (T023 completed)

## Parallel Execution Examples

- **Within User Story 1**: T013-T015 (crawling, extraction, chunking) can run in parallel with T016-T017 (embedding, storage)
- **Within User Story 3**: T025-T027 (UI components) can run in parallel with T028-T030 (animations, state)
- **Cross-Story**: Backend API development (T019) can run in parallel with frontend components (T020-T023)

## Implementation Strategy

1. **MVP Scope**: Complete Phase 1, 2, and User Story 1 for basic chat functionality
2. **Incremental Delivery**: Add widget functionality (User Story 3), then selected text (User Story 2)
3. **Testing**: Implement basic functionality first, then add comprehensive tests and optimizations