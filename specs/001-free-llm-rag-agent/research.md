# Research: Free LLM RAG Agent for Physical AI Book

## Decision: Google Gemini 1.5 Flash for RAG Implementation

**Rationale**: Selected Google Gemini 1.5 Flash as the primary LLM for the RAG agent to meet the requirement of using only free LLM services. This model offers strong multimodal capabilities and good performance for question-answering tasks while being available in the free tier.

**Alternatives considered**:
1. OpenAI GPT models - Rejected due to paid service requirement
2. Anthropic Claude - Rejected due to paid service requirement
3. Open-source models (e.g., Llama 3) - Rejected due to infrastructure complexity and computational requirements
4. Google Gemini Pro - Rejected due to paid service requirement

## Decision: Qdrant Cloud for Vector Storage

**Rationale**: Chose Qdrant Cloud as the vector database for storing document embeddings due to its proven performance with RAG systems, ease of integration, and existing familiarity from previous RAG implementation.

**Alternatives considered**:
1. Pinecone - Good alternative but requires paid subscription
2. Weaviate - Open source option but more complex setup
3. ChromaDB - Local option but not suitable for production/cloud deployment
4. PostgreSQL with pgvector - Possible but less optimized for vector similarity search

## Decision: FastAPI Backend Framework

**Rationale**: Selected FastAPI for the backend due to its excellent support for async operations, automatic API documentation, and strong performance characteristics suitable for LLM API integration.

**Alternatives considered**:
1. Flask - Simpler but lacks async support and modern features
2. Django - More complex than needed for this API-only service
3. Express.js - Node.js alternative but Python preferred for LLM integration

## Decision: React-based Toggleable Chat Widget

**Rationale**: Implemented a React-based toggleable chat widget to provide a seamless user experience integrated with the Docusaurus documentation site while allowing users to ask questions about book content.

**Alternatives considered**:
1. Standalone chat application - Would require separate deployment and navigation
2. iframe integration - Would create isolation issues and styling challenges
3. Native Docusaurus plugin - Would be more complex to develop

## Technical Considerations for Gemini Integration

**API Limits**: Google Gemini has rate limits that need to be considered for concurrent users. The free tier has specific quotas that may require rate limiting implementation.

**Embedding Model**: Using Gemini embedding-001 for text embeddings to maintain consistency with the LLM choice and ensure compatibility with the free tier.

**Tool Use Capability**: Implementing Gemini's tool use functionality to allow the agent to interact with Qdrant Cloud for document retrieval operations.

## Selected Text Feature Implementation

**Approach**: Using JavaScript's Selection API to capture selected text on the page and pass it as additional context to the Gemini agent for more targeted responses.

**Technical Implementation**: The feature will capture selected text when the user submits a query and include it as additional context in the request to the backend.