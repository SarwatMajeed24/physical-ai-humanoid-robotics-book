# Tasks: Free LLM RAG Agent for Physical AI Book

**Feature**: Free LLM RAG Agent for Physical AI Book
**Branch**: `001-free-llm-rag-agent`
**Generated**: 2025-12-16
**Input**: spec.md, plan.md, data-model.md, contracts/openapi.yaml

## Implementation Strategy

This feature implements a RAG (Retrieval-Augmented Generation) agent using Google Gemini 1.5 Flash (free tier) and Qdrant Cloud vector database to provide accurate answers about the Physical AI & Humanoid Robotics book content. The system includes a toggleable chat widget with selected text support, built with FastAPI backend and integrated into the book's frontend.

**MVP Scope**: User Story 1 (Basic Q&A with Gemini RAG) provides the core functionality for an independently testable and deployable system.

## Dependencies

User stories completion order:
- User Story 1 (P1) - Basic Q&A with Gemini RAG (Independent)
- User Story 2 (P2) - Selected Text Q&A Feature (Depends on US1)
- User Story 3 (P2) - Toggleable Chat Widget (Depends on US1)
- User Story 4 (P3) - Gemini Agent with Tool Use (Depends on US1)

Parallel execution opportunities:
- US2 and US3 can be developed in parallel after US1 foundation
- Backend services and frontend components can be developed in parallel after foundational setup

## Phase 1: Setup

- [ ] T001 Create backend project structure with Python 3.11
- [ ] T002 Set up FastAPI application structure in backend/src/api/
- [ ] T003 Install required dependencies: fastapi, uvicorn, google-generativeai, qdrant-client, python-dotenv
- [ ] T004 Create frontend directory structure for React components
- [ ] T005 Create .env file structure for API keys (template only)

## Phase 2: Foundational

- [ ] T006 Create ChatRequest and ChatResponse models in backend/src/models/chat.py
- [ ] T007 Implement basic Qdrant vector store service in backend/src/services/vector_store.py
- [ ] T008 Create basic chat API endpoint in backend/src/api/chat.py
- [ ] T009 [P] Set up environment configuration in backend/src/config/
- [ ] T010 [P] Create basic frontend component structure in frontend/src/components/

## Phase 3: User Story 1 - Basic Q&A with Gemini RAG (Priority: P1)

**Goal**: Enable users to ask questions about the Physical AI & Humanoid Robotics book content and receive accurate answers powered by Google Gemini 1.5 Flash.

**Independent Test**: Can be fully tested by asking various questions about book content and verifying that Gemini 1.5 Flash provides accurate, contextually relevant answers based on the book's content stored in Qdrant Cloud.

- [ ] T011 [US1] Get Gemini free API key from aistudio.google.com
- [ ] T012 [US1] Install langchain-google-genai and related dependencies
- [ ] T013 [US1] Create Google Gemini configuration service in backend/src/config/gemini.py
- [ ] T014 [US1] Create Gemini LLM service using gemini-1.5-flash in backend/src/services/gemini_llm.py
- [ ] T015 [US1] Create Gemini embedding service using embedding-001 in backend/src/services/embedding.py
- [ ] T016 [US1] Implement basic RAG chain service in backend/src/services/rag_chain.py
- [ ] T017 [US1] Update Qdrant vector store service to support retrieval operations
- [ ] T018 [US1] Create /chat endpoint in backend/src/api/chat.py to handle basic queries
- [ ] T019 [US1] Implement basic response generation with Gemini and context from Qdrant
- [ ] T020 [US1] Test basic Q&A functionality with sample book content

## Phase 4: User Story 2 - Selected Text Q&A Feature (Priority: P2)

**Goal**: Allow users to select specific text on the page and ask questions about that selected content to get more contextual answers.

**Independent Test**: Can be tested by selecting text on the page, asking a question about it, and verifying that the selected text is properly passed as context to the Gemini agent for response generation.

- [ ] T021 [US2] Update ChatRequest model to include selected_text field
- [ ] T022 [US2] Update ChatResponse model to support source references
- [ ] T023 [US2] Modify RAG chain to incorporate selected text as additional context
- [ ] T024 [US2] Update /chat endpoint to handle selected_text parameter
- [ ] T025 [US2] Create frontend JavaScript to capture selected text
- [ ] T026 [US2] Update frontend chat component to pass selected text with queries
- [ ] T027 [US2] Test selected text functionality with various selections

## Phase 5: User Story 3 - Toggleable Chat Widget (Priority: P2)

**Goal**: Provide a toggleable chat widget that users can open and close as needed to access the AI assistant without interfering with reading experience.

**Independent Test**: Can be tested by verifying that the floating chat icon appears on book pages, can be clicked to open the chat widget, and can be closed without losing conversation history.

- [ ] T028 [US3] Create toggleable chat widget component in src/components/RagChat.js
- [ ] T029 [US3] Implement open/close functionality for chat widget
- [ ] T030 [US3] Add floating chat icon that toggles the widget
- [ ] T031 [US3] Implement message history display in chat widget
- [ ] T032 [US3] Add message input and send functionality
- [ ] T033 [US3] Integrate chat widget with backend /chat API
- [ ] T034 [US3] Test toggleable widget functionality on sample pages

## Phase 6: User Story 4 - Gemini Agent with Tool Use (Priority: P3)

**Goal**: Enable the AI assistant to act as an intelligent agent that can use tools to retrieve relevant information from Qdrant Cloud for more accurate and comprehensive answers.

**Independent Test**: Can be tested by asking complex questions that require the agent to use Qdrant retrieval tools and verifying that the agent properly retrieves and processes information before responding.

- [ ] T035 [US4] Research and implement Google Gemini tool use functionality
- [ ] T036 [US4] Create Qdrant retrieval tool for Gemini agent
- [ ] T037 [US4] Build agent with Gemini tool use capabilities
- [ ] T038 [US4] Create /agent/chat endpoint that uses tool-based agent
- [ ] T039 [US4] Update frontend to optionally use agent endpoint
- [ ] T040 [US4] Test complex queries requiring multiple document retrieval
- [ ] T041 [US4] Validate agent properly uses Qdrant as a tool

## Phase 7: Polish & Cross-Cutting Concerns

- [ ] T042 Add proper error handling and user-friendly messages throughout the system
- [ ] T043 Implement rate limiting and retry logic for Gemini API calls
- [ ] T044 Add logging and monitoring for debugging purposes
- [ ] T045 Create comprehensive test suite for backend services
- [ ] T046 Add input validation and sanitization
- [ ] T047 Optimize response times and implement caching where appropriate
- [ ] T048 Document the API endpoints and integration instructions
- [ ] T049 Perform end-to-end testing of all features
- [ ] T050 Deploy and test locally to ensure all requirements are met