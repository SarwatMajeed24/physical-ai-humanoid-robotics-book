# Tasks: Local Frontend-Backend Integration for RAG Chatbot

**Feature**: Local Frontend-Backend Integration for RAG Chatbot
**Branch**: `003-local-frontend-backend-integration`
**Generated**: 2025-12-16
**Input**: spec.md, plan.md, data-model.md, contracts/chat-api.yaml

## Implementation Strategy

This feature implements local connection between Docusaurus frontend and FastAPI backend for the RAG chatbot system. The integration enables bidirectional communication with proper CORS configuration, supporting both basic chat functionality and selected text context transmission. The system operates on localhost (frontend:3000 ↔ backend:8000) with JSON-based request/response format.

**MVP Scope**: User Story 1 (Basic Chat Message Exchange) provides the core functionality for an independently testable and deployable system.

## Dependencies

User stories completion order:
- User Story 1 (P1) - Basic Chat Message Exchange (Independent)
- User Story 2 (P2) - Selected Text Context Transmission (Depends on US1)
- User Story 3 (P1) - CORS Error Prevention (Independent)

Parallel execution opportunities:
- US2 can be developed in parallel with US1 after foundational setup
- Backend CORS configuration and frontend API calls can be developed in parallel after foundational setup

## Phase 1: Setup

- [ ] T001 [P] Create project structure per implementation plan
- [ ] T002 [P] Install required dependencies: fastapi, cors middleware, react components
- [ ] T003 [P] Set up environment configuration for local development

## Phase 2: Foundational

- [X] T004 Configure CORS middleware in FastAPI to allow localhost:3000
- [X] T005 Update backend /chat endpoint to accept JSON requests
- [X] T006 Implement basic request/response handling in backend

## Phase 3: User Story 1 - Basic Chat Message Exchange (Priority: P1)

**Goal**: Enable local developers to send messages from Docusaurus frontend chat widget to FastAPI backend and receive responses for end-to-end RAG chatbot functionality testing.

**Independent Test**: Can be fully tested by starting both services locally (frontend on port 3000, backend on port 8000), opening the chat widget, sending a message, and verifying that the backend processes it and returns a response to the frontend without CORS errors.

- [X] T007 [P] [US1] Add CORS middleware in FastAPI main.py (allow localhost:3000)
- [X] T008 [P] [US1] Update RagChat.js to use backend URL http://localhost:8000/api/v1/chat
- [X] T009 [US1] Modify frontend to send POST request with JSON body { "query": user_input }
- [X] T010 [US1] Implement backend response handling and display in widget
- [X] T011 [US1] Add error handling for failed requests in frontend
- [X] T012 [US1] Test basic communication with simple "hello" message
- [X] T013 [US1] Test with book-related question to verify RAG functionality
- [X] T014 [US1] Validate JSON request/response format compliance
- [X] T015 [US1] Test multiple sequential messages in single session

## Phase 4: User Story 2 - Selected Text Context Transmission (Priority: P2)

**Goal**: Enhance the core chat functionality by enabling the selected text feature that adds context to user queries, improving the relevance of responses.

**Independent Test**: Can be tested by selecting text on the frontend page, typing a question in the chat widget, sending the message, and verifying that both the query and selected text context are received by the backend and processed appropriately.

- [X] T016 [US2] Update frontend to capture selected text using window.getSelection()
- [X] T017 [US2] Modify POST request to include selected_text field in JSON body
- [X] T018 [US2] Update backend to handle selected_text parameter from frontend
- [X] T019 [US2] Test selected text functionality with sample selections
- [X] T020 [US2] Validate selected text context is properly integrated in RAG responses

## Phase 5: User Story 3 - CORS Error Prevention (Priority: P1)

**Goal**: Ensure CORS is properly configured between the frontend and backend to prevent cross-origin errors during local testing.

**Independent Test**: Can be tested by attempting to send requests from the frontend to backend and verifying that no CORS-related errors appear in browser console.

- [X] T021 [US3] Configure CORS middleware with proper origins (localhost:3000)
- [X] T022 [US3] Set appropriate CORS headers for POST requests
- [X] T023 [US3] Test CORS configuration with various request methods
- [X] T024 [US3] Verify no CORS errors in browser console during communication
- [X] T025 [US3] Test with different content types and headers

## Phase 6: Polish & Cross-Cutting Concerns

- [X] T026 Add proper loading states and user feedback during API calls
- [X] T027 Implement comprehensive error handling with user-friendly messages
- [X] T028 Add request/response logging for debugging purposes
- [X] T029 Create integration tests for frontend-backend communication
- [X] T030 Validate all API request/response formats against contracts
- [X] T031 Add input validation for query and selected text fields
- [X] T032 Optimize network requests and implement caching where appropriate
- [X] T033 Document the API integration for frontend developers
- [X] T034 Perform end-to-end testing of all functionality
- [X] T035 Deploy and test locally to ensure all requirements are met