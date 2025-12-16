# Feature Specification: Free LLM RAG Agent for Physical AI Book

**Feature Branch**: `001-free-llm-rag-agent`
**Created**: 2025-12-16
**Status**: Draft
**Input**: User description: "Project: Free LLM RAG Agent for Physical AI Book

Target audience: Book readers

Focus: RAG agent with free LLM (Google Gemini 1.5 Flash)

Requirements:
- LLM: Google Gemini 1.5 Flash (free tier)
- Embedding: Gemini embedding-001 (free)
- Vector DB: Qdrant Cloud (given key)
- Backend: FastAPI
- Frontend: Toggleable chat widget
- Selected text support
- Agent: Gemini tool use for Qdrant retrieval
- No OpenAI, no paid LLM

Success criteria:
- Agent book content se accurate answers de
- Free LLM use kare
- Local mein perfect kaam kare

Constraints:
- Only free LLM (Gemini)
- No OpenAI
- No push/upload abhi
- Spec-Kit Plus se implement"

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.

  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Basic Q&A with Gemini RAG (Priority: P1)

As a book reader, I want to ask questions about the Physical AI & Humanoid Robotics book content and receive accurate answers powered by Google Gemini 1.5 Flash, so that I can quickly find information without manually searching through the book.

**Why this priority**: This is the core functionality of the RAG agent - enabling users to get accurate answers from the book content using free LLM technology.

**Independent Test**: Can be fully tested by asking various questions about book content and verifying that Gemini 1.5 Flash provides accurate, contextually relevant answers based on the book's content stored in Qdrant Cloud.

**Acceptance Scenarios**:

1. **Given** the RAG agent is connected to Qdrant Cloud with book content indexed, **When** a user asks a question about the book content, **Then** Gemini 1.5 Flash processes the query using RAG and returns an accurate answer based on the book content.

2. **Given** a user has entered a question, **When** the system processes the query through the Gemini RAG pipeline, **Then** the response should be generated using free Gemini 1.5 Flash model without incurring paid LLM costs.

---

### User Story 2 - Selected Text Q&A Feature (Priority: P2)

As a book reader, I want to select specific text on the page and ask questions about that selected content, so that I can get more contextual answers related to the specific text I'm reading.

**Why this priority**: This enhances user experience by allowing more targeted questions about specific content they're currently reading, making the interaction more intuitive and useful.

**Independent Test**: Can be tested by selecting text on the page, asking a question about it, and verifying that the selected text is properly passed as context to the Gemini agent for response generation.

**Acceptance Scenarios**:

1. **Given** a user has selected text on the book page, **When** they ask a question in the chat widget, **Then** the selected text should be included as context for the Gemini agent to provide more targeted answers.

---

### User Story 3 - Toggleable Chat Widget (Priority: P2)

As a book reader, I want to have a toggleable chat widget that I can open and close as needed, so that I can access the AI assistant without it interfering with my reading experience.

**Why this priority**: Essential for user experience - provides easy access to the AI assistant while allowing users to focus on reading when needed.

**Independent Test**: Can be tested by verifying that the floating chat icon appears on book pages, can be clicked to open the chat widget, and can be closed without losing conversation history.

**Acceptance Scenarios**:

1. **Given** the book page is loaded, **When** the user sees the floating chat icon, **Then** they can click it to open the chat widget and interact with the Gemini agent.

---

### User Story 4 - Gemini Agent with Tool Use (Priority: P3)

As a book reader, I want the AI assistant to act as an intelligent agent that can use tools to retrieve relevant information from Qdrant Cloud, so that I get more accurate and comprehensive answers by leveraging Gemini's tool use capabilities.

**Why this priority**: This represents the advanced agent functionality that leverages Gemini's tool use capabilities for better RAG performance and more sophisticated interactions.

**Independent Test**: Can be tested by asking complex questions that require the agent to use Qdrant retrieval tools and verifying that the agent properly retrieves and processes information before responding.

**Acceptance Scenarios**:

1. **Given** a complex question requiring multiple sources, **When** the Gemini agent processes the query, **Then** it should use Qdrant Cloud as a tool to retrieve relevant documents and synthesize a comprehensive answer.

---

### Edge Cases

- What happens when Qdrant Cloud is temporarily unavailable or rate-limited?
- How does the system handle very long user queries or selected text that exceeds Gemini's context limits?
- How does the system respond when the requested information is not available in the book content?
- What happens when Gemini API returns an error or is temporarily unavailable?
- How does the system handle concurrent users accessing the RAG agent simultaneously?
- What happens when the embedding service fails to generate embeddings for query or document chunks?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST use Google Gemini 1.5 Flash as the primary LLM for response generation (free tier only, no paid models)
- **FR-002**: System MUST use Google Gemini embedding-001 for generating text embeddings (free tier only)
- **FR-003**: System MUST integrate with Qdrant Cloud for vector storage and retrieval of book content
- **FR-004**: System MUST implement a toggleable chat widget that can be opened/closed by users
- **FR-005**: System MUST capture and utilize selected text on the page as additional context for queries
- **FR-006**: System MUST implement Gemini tool use functionality for Qdrant retrieval operations
- **FR-007**: System MUST be built with FastAPI backend framework for the API endpoints
- **FR-008**: System MUST handle user queries by retrieving relevant content from Qdrant and passing to Gemini for response generation
- **FR-009**: System MUST validate that no OpenAI APIs or paid LLM services are used in the implementation
- **FR-010**: System MUST provide accurate answers based on the Physical AI & Humanoid Robotics book content

*Example of marking unclear requirements:*

- **FR-011**: System MUST handle rate limiting from Gemini API [NEEDS CLARIFICATION: specific rate limits and retry strategy not specified]
- **FR-012**: System MUST manage conversation history [NEEDS CLARIFICATION: retention period and storage mechanism not specified]

### Key Entities

- **ChatSession**: Represents a user's conversation with the Gemini agent, including message history and metadata
- **Query**: Represents a user's question with optional selected text context
- **DocumentChunk**: Represents a piece of book content stored in Qdrant Cloud with embedding vector
- **ChatResponse**: Represents Gemini's response with sources and metadata

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Agent provides accurate answers to book-related questions with at least 85% relevance based on manual evaluation
- **SC-002**: System uses only free LLM services (Google Gemini 1.5 Flash) without incurring any paid LLM costs
- **SC-003**: Local testing confirms the system works perfectly with all features (toggleable widget, selected text, Qdrant integration) functioning as expected
- **SC-004**: Response time for queries is under 5 seconds for typical questions
- **SC-005**: Selected text functionality works reliably across different browsers and page layouts
- **SC-006**: Gemini agent successfully uses Qdrant Cloud as a tool to retrieve relevant information for complex queries
- **SC-007**: No OpenAI or other paid LLM services are integrated or called in the implementation
