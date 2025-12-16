# Research Summary: RAG Chatbot for Physical AI Book

## Decision: Architecture Pattern
**Rationale**: Selected microservices architecture with separate backend and frontend to handle the RAG system requirements effectively. The backend handles content crawling, embedding, and RAG processing, while the frontend provides the chat widget that integrates with the existing Docusaurus site.

## Decision: Technology Stack
**Rationale**:
- **Backend**: FastAPI chosen for its async support, excellent documentation, and Pydantic integration which is ideal for API development and data validation
- **Embeddings**: Cohere embed-english-v3.0 as specified in requirements (high quality embeddings, good for technical content)
- **Vector DB**: Qdrant Cloud as specified in requirements (robust vector database with cloud hosting)
- **Frontend**: React components for the chat widget to integrate seamlessly with Docusaurus (which uses React)

## Decision: Content Processing Pipeline
**Rationale**:
- **Crawling**: Use requests/sitemap parsing to extract all pages from the sitemap
- **Extraction**: Use BeautifulSoup or similar to extract clean text from HTML/MDX content
- **Chunking**: RecursiveCharacterTextSplitter to break content into appropriate-sized chunks for embedding
- **Storage**: Qdrant Cloud collection "physical_ai_book" with proper indexing for efficient similarity search

## Decision: Selected Text Integration
**Rationale**:
- Use JavaScript selection API to capture user-selected text
- Pass selected text as additional context to the RAG chain
- Implement this as a React hook for clean integration with the chat component

## Decision: Deployment Strategy
**Rationale**:
- Backend: Deploy as separate service (possibly using Docker/Cloud Run)
- Frontend: Embed as React component in Docusaurus site
- Vercel deployment for the overall site as specified in requirements

## Alternatives Considered

### Alternative 1: OpenAI vs Cohere
- **Considered**: Using OpenAI embeddings/models
- **Rejected**: Requirement explicitly states "No OpenAI", must use Cohere as specified

### Alternative 2: Vector Database Options
- **Considered**: Pinecone, Weaviate, Chroma, Supabase Vector
- **Rejected**: Requirement specifies Qdrant Cloud, which offers good performance and managed service

### Alternative 3: Monolithic vs Microservices
- **Considered**: Single application handling both frontend and backend
- **Rejected**: Separation of concerns is better for maintenance and scalability

### Alternative 4: Different Frontend Approaches
- **Considered**: Standalone widget, iframe integration
- **Rejected**: React component integration provides better performance and user experience with Docusaurus

## Technical Research Findings

### Sitemap Crawling
- Use `xml.etree.ElementTree` to parse sitemap.xml
- Follow links recursively to capture all pages
- Handle both sitemap index files and individual sitemap entries

### Content Extraction from MDX/HTML
- Use BeautifulSoup4 for HTML parsing
- For MDX content, consider using libraries that can handle JSX syntax
- Extract text content while preserving document structure

### Cohere Embedding Best Practices
- Batch requests for efficiency (up to 96 texts per request)
- Use embed-english-v3.0 for best performance on technical content
- Handle rate limits and errors appropriately

### Qdrant Vector Operations
- Create collection with appropriate vector dimensions (likely 1024 for Cohere embeddings)
- Use payload filtering to store metadata (URL, section info)
- Implement efficient similarity search with filtering

### FastAPI RAG Implementation
- Use async functions for better performance
- Implement proper error handling and validation
- Add middleware for logging and monitoring

### React Chat Widget
- Use floating UI library for proper positioning
- Implement message history and context management
- Add loading states and error handling