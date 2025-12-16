# Quickstart Guide: RAG Chatbot for Physical AI Book

## Prerequisites

- Python 3.11+
- Node.js 18+ (for Docusaurus integration)
- Cohere API key
- Qdrant Cloud URL and API key
- Access to the book sitemap at https://physical-ai-humanoid-robotics-book-lovat.vercel.app/sitemap.xml

## Setup Backend

1. **Install Python dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Set environment variables:**
   ```bash
   export COHERE_API_KEY="your-cohere-api-key"
   export QDRANT_URL="your-qdrant-cloud-url"
   export QDRANT_API_KEY="your-qdrant-api-key"
   export BOOK_SITEMAP_URL="https://physical-ai-humanoid-robotics-book-lovat.vercel.app/sitemap.xml"
   ```

3. **Initialize the vector database:**
   ```bash
   python -m src.services.crawler --init-db
   ```

4. **Run the backend:**
   ```bash
   uvicorn main:app --reload
   ```

## Index Book Content

1. **Crawl and index the book content:**
   ```bash
   python -m src.services.crawler --crawl
   ```

2. **Verify content is indexed:**
   ```bash
   curl http://localhost:8000/api/health
   ```

## Integrate Frontend Widget

1. **Install frontend dependencies:**
   ```bash
   cd frontend
   npm install
   ```

2. **Build the widget:**
   ```bash
   npm run build
   ```

3. **Integrate with Docusaurus:**
   - Add the ChatWidget component to your Docusaurus layout
   - Configure the backend API endpoint in the widget settings

## Environment Configuration

Create a `.env` file in the backend directory:

```env
COHERE_API_KEY=your_api_key_here
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
BOOK_SITEMAP_URL=https://physical-ai-humanoid-robotics-book-lovat.vercel.app/sitemap.xml
BACKEND_API_URL=http://localhost:8000
```

## API Endpoints

- `POST /chat` - Process user queries and return RAG responses
- `GET /health` - Check service health
- `GET /status` - Get indexing status

## Testing

1. **Run backend tests:**
   ```bash
   pytest tests/
   ```

2. **Run frontend tests:**
   ```bash
   npm test
   ```

## Deployment

1. **Deploy backend to cloud service** (e.g., Google Cloud Run, AWS Fargate)
2. **Integrate frontend widget** with the existing Docusaurus site
3. **Configure Vercel deployment** for the overall site