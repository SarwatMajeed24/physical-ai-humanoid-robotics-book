# Feature Specification: RAG Chatbot for Physical AI Book

**Feature Branch**: `002-rag-chatbot`
**Created**: 2025-12-16
**Status**: Draft
**Input**: User description: "Project: RAG Chatbot for Physical AI Book (Vercel Live)

Target audience: Book readers

Focus: RAG using Cohere embeddings + Qdrant Cloud

Requirements:
- Crawl content from sitemap: https://physical-ai-humanoid-robotics-book-lovat.vercel.app/sitemap.xml
- Extract text from all pages
- Chunk content
- Embeddings: Cohere embed-english-v3.0 (given key)
- Vector DB: Qdrant Cloud (given URL and key)
- Backend: FastAPI with /chat endpoint
- Frontend: Docusaurus embedded toggleable chat widget (floating icon)
- Selected text support: User select kare text → chatbot us context se answer de
- No OpenAI

Success criteria:
- Chatbot book content pe accurate answers de
- Selected text feature kaam kare
- Widget book mein embedded aur responsive
- Pipeline test: crawl → embed → retrieve → answer

Constraints:
- Use given Cohere and Qdrant keys
- Local test first, then Vercel deploy ready
- Spec-Kit Plus se implement"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Basic Chat with Book Content (Priority: P1)

As a book reader, I want to ask questions about the Physical AI and Humanoid Robotics content so that I can get accurate answers based on the book material without having to search through pages.

**Why this priority**: This is the core functionality that delivers immediate value - users can interact with the book content through natural language queries.

**Independent Test**: Can be fully tested by asking questions about book content and verifying the chatbot provides accurate, contextually relevant answers based on the book material.

**Acceptance Scenarios**:

1. **Given** a user is reading the book website, **When** they open the chat widget and ask a question about book content, **Then** the chatbot provides an accurate answer based on the book material
2. **Given** a user asks a question about humanoid robotics concepts, **When** they submit the query, **Then** the response contains information directly from the book's content

---

### User Story 2 - Selected Text Context (Priority: P2)

As a book reader, I want to select specific text on the page and ask questions about that text so that I can get detailed explanations or clarifications about specific concepts.

**Why this priority**: This enhances the user experience by allowing contextual questions about specific content they're reading.

**Independent Test**: Can be fully tested by selecting text on a book page, opening the chat, and verifying that the selected text is used as context for the response.

**Acceptance Scenarios**:

1. **Given** a user has selected text on a book page, **When** they use the chat widget to ask a question, **Then** the selected text is automatically included as context for the response
2. **Given** a user selects text containing technical terminology, **When** they ask for clarification, **Then** the response explains the selected terms using book content as reference

---

### User Story 3 - Embedded Chat Widget (Priority: P1)

As a book reader, I want to access the chatbot through a toggleable widget that doesn't interfere with reading so that I can get help when needed without disrupting my learning experience.

**Why this priority**: Essential for user adoption - the widget must be accessible but not intrusive.

**Independent Test**: Can be fully tested by verifying the chat widget appears as a floating icon, can be toggled open/closed, and is responsive across different screen sizes.

**Acceptance Scenarios**:

1. **Given** a user is viewing any page of the book, **When** they see the floating chat icon, **Then** they can click it to open the chat interface
2. **Given** the chat widget is open, **When** the user clicks outside or closes it, **Then** the widget minimizes to the floating icon without losing conversation state

---

## Edge Cases

- What happens when the book content is updated and embeddings need regeneration?
- How does the system handle very long text selections?
- What occurs when the Qdrant Cloud service is temporarily unavailable?
- How does the system respond to queries completely unrelated to book content?
- What happens when a user submits extremely long queries?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST crawl content from the provided sitemap URL to index book content
- **FR-002**: System MUST extract text from all pages retrieved from the sitemap
- **FR-003**: System MUST chunk content into manageable segments for embedding
- **FR-004**: System MUST use Cohere embed-english-v3.0 for generating text embeddings
- **FR-005**: System MUST store embeddings in Qdrant Cloud vector database
- **FR-006**: System MUST provide a FastAPI backend with a /chat endpoint for processing queries
- **FR-007**: System MUST include a Docusaurus-compatible chat widget with a floating toggleable icon
- **FR-008**: System MUST capture selected text from the current page and use it as context for queries
- **FR-009**: System MUST return accurate answers based on the book's content, citing relevant sources when possible
- **FR-010**: System MUST handle concurrent users without performance degradation
- **FR-011**: System MUST support a complete pipeline test: crawl → embed → retrieve → answer
- **FR-012**: System MUST be responsive and work on mobile, tablet, and desktop devices

### Key Entities

- **Book Content**: The HTML/MDX content from the book website that gets indexed and used for RAG responses
- **Embeddings**: Vector representations of book content chunks stored in Qdrant Cloud for similarity search
- **User Query**: Text input from users seeking information about book content
- **Chat Session**: Conversation context between user and chatbot for maintaining context across multiple exchanges
- **Selected Text**: Portion of text on the current page that user has highlighted for contextual queries

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can ask questions about book content and receive accurate answers within 5 seconds
- **SC-002**: 90% of user queries about book content receive relevant responses based on actual book material
- **SC-003**: The selected text feature works correctly in 95% of attempts, incorporating context into responses
- **SC-004**: The chat interface is accessible and responsive on 100% of major browsers and screen sizes
- **SC-005**: The system handles at least 100 concurrent users without significant performance degradation
- **SC-006**: 85% of users find the information retrieval helpful for understanding book content based on user satisfaction metrics
- **SC-007**: The complete pipeline (crawl → embed → retrieve → answer) functions correctly and can be verified through testing
