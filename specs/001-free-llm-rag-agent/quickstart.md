# Quickstart: Free LLM RAG Agent for Physical AI Book

## Development Setup

### Prerequisites
- Python 3.11+
- Node.js 18+ (for Docusaurus integration)
- Google Gemini API key
- Qdrant Cloud API key and URL

### Environment Setup

1. Create a `.env` file in the backend directory:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
```

2. Install backend dependencies:
```bash
cd backend
pip install fastapi uvicorn python-dotenv google-generativeai qdrant-client Pydantic
```

3. Install frontend dependencies:
```bash
cd frontend  # or your Docusaurus project
npm install react react-dom
```

## Running the Application

### Backend (FastAPI)
```bash
cd backend
uvicorn src.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Frontend Integration
The RagChat component can be integrated into your Docusaurus site by importing it into your layout.

## API Endpoints

### POST /api/v1/chat
Process user queries using the RAG system:
```json
{
  "query": "Your question about the book content",
  "selected_text": "Optional text selected by user",
  "session_id": "Optional session ID (auto-generated if not provided)"
}
```

Response:
```json
{
  "response": "Generated response from Gemini",
  "session_id": "Current session ID",
  "sources": [
    {
      "url": "Source document URL",
      "title": "Source document title",
      "snippet": "Relevant snippet"
    }
  ],
  "timestamp": "ISO timestamp"
}
```

## Key Components

### RAG Chain (`src/services/rag_chain.py`)
- Handles the complete RAG flow: retrieve → generate
- Uses Google Gemini 1.5 Flash for response generation
- Integrates with Qdrant Cloud for document retrieval

### Embedding Service (`src/services/embedding.py`)
- Uses Google Gemini embedding-001 for text embeddings
- Handles query and document embedding generation

### Vector Store (`src/services/vector_store.py`)
- Qdrant Cloud integration for vector storage and retrieval
- Handles similarity search for relevant document chunks

### Chat API (`src/api/chat.py`)
- FastAPI endpoints for chat functionality
- Session management and message history