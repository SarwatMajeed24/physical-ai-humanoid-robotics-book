# ADR-0002: RAG Architecture with Google Gemini and Qdrant

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-16
- **Feature:** Free LLM RAG Agent for Physical AI Book
- **Context:** Need to implement a RAG (Retrieval-Augmented Generation) system for the Physical AI & Humanoid Robotics book that uses only free LLM services, as required by the project constraints. The system must provide accurate answers based on book content while maintaining good performance and user experience.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

- **LLM**: Google Gemini 1.5 Flash (free tier) for response generation
- **Embedding Model**: Google Gemini embedding-001 (free tier) for text embeddings
- **Vector Database**: Qdrant Cloud for document storage and retrieval
- **Backend Framework**: FastAPI for API endpoints and RAG processing
- **Frontend Integration**: React-based toggleable chat widget for Docusaurus site
- **Tool Use**: Gemini's tool use capability for Qdrant retrieval operations

## Consequences

### Positive

- Leverages free tier of Google's advanced LLM without incurring costs
- Qdrant Cloud provides optimized vector similarity search for RAG operations
- FastAPI offers excellent performance for async LLM API calls
- Seamless integration with existing Docusaurus documentation site
- Tool use capability allows sophisticated retrieval-augmented interactions
- Google's Gemini models provide strong multimodal capabilities for complex queries

### Negative

- Dependency on Google Cloud services and potential rate limits
- Limited control over LLM behavior compared to open-source alternatives
- Potential vendor lock-in to Google's ecosystem
- Rate limits on free tier may impact concurrent user experience
- Less customization options compared to self-hosted LLMs
- Potential latency from external API calls to Google services

## Alternatives Considered

Alternative Stack A: OpenAI GPT + Pinecone + FastAPI
- Why rejected: Violates requirement to use only free LLM services

Alternative Stack B: Anthropic Claude + Weaviate + FastAPI
- Why rejected: Violates requirement to use only free LLM services

Alternative Stack C: Open-source models (e.g., Llama 3) + ChromaDB + FastAPI
- Why rejected: Requires significant computational resources and infrastructure complexity that exceeds project scope

Alternative Stack D: Self-hosted solution with local embeddings
- Why rejected: Would require more infrastructure and maintenance than the cloud-based approach

## References

- Feature Spec: /specs/001-free-llm-rag-agent/spec.md
- Implementation Plan: /specs/001-free-llm-rag-agent/plan.md
- Related ADRs: None
- Evaluator Evidence: /specs/001-free-llm-rag-agent/research.md
