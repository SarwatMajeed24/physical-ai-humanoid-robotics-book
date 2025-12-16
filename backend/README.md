# RAG Chatbot Backend

Backend API for the RAG Chatbot for Physical AI Book using Cohere and Qdrant Cloud.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Copy the environment file and add your API keys:
```bash
cp .env.example .env
# Edit .env with your Cohere API key and Qdrant credentials
```

3. Run the server:
```bash
python start_server.py
# Or with uvicorn directly:
uvicorn main:app --reload --port 8001
```

## API Endpoints

- `POST /api/v1/chat` - Basic RAG chat endpoint
- `POST /api/v1/agent/chat` - Agent-based chat with tool use
- `GET /api/v1/sessions/{session_id}` - Get session info
- `DELETE /api/v1/sessions/{session_id}` - Delete session

## Features

- **Cohere LLM**: Uses Cohere command-r-08-2024 (free tier)
- **Embeddings**: Uses Cohere embed-english-v3.0 (free tier)
- **Vector Storage**: Qdrant Cloud for document storage and retrieval
- **Agent Tool Use**: Advanced agent with Qdrant retrieval capabilities
- **Selected Text**: Support for context from selected page text
- **Toggleable UI**: React-based chat widget integrated with Docusaurus