from typing import List, Dict, Any
from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from ..services.vector_store import QdrantVectorStore
from ..services.cohere_embedding import CohereEmbeddingService
import logging

logger = logging.getLogger(__name__)

class QdrantRetrievalInput(BaseModel):
    query: str = Field(description="The search query to find relevant documents from the book content")

class QdrantRetrievalTool(BaseTool):
    name: str = "qdrant_retrieval"
    description: str = "Retrieve relevant documents from Qdrant vector store based on the query"
    args_schema: type = QdrantRetrievalInput

    def __init__(self):
        super().__init__()

    @property
    def embedding_service(self):
        if not hasattr(self, '_embedding_service'):
            self._embedding_service = CohereEmbeddingService()
        return self._embedding_service

    @property
    def vector_store(self):
        if not hasattr(self, '_vector_store'):
            self._vector_store = QdrantVectorStore()
        return self._vector_store

    def _run(self, query: str) -> str:
        """Synchronous version of the tool - This should not be called when using async agents"""
        logger.warning("Sync _run method called for Qdrant tool. This should not happen when using async agents.")
        return f"Tool is designed for async usage. Query: {query[:100]}..."

    async def _arun(self, query: str) -> str:
        """Asynchronous version of the tool (primary implementation)"""
        try:
            # Generate embedding for the query
            query_embedding = self.embedding_service.generate_query_embedding(query)
            if not query_embedding:
                logger.warning(f"Failed to generate embedding for query: {query}")
                return "No relevant documents found."

            # Retrieve similar documents
            relevant_chunks = await self.vector_store.retrieve_similar(query_embedding, limit=10)

            if not relevant_chunks:
                return "No relevant documents found."

            # Format results
            results = []
            for chunk in relevant_chunks:
                results.append(f"Title: {chunk.get('title', 'N/A')}\nURL: {chunk.get('url', 'N/A')}\nContent: {chunk.get('content', '')[:500]}...")

            return "\n\n".join(results)

        except Exception as e:
            logger.error(f"Error in Qdrant retrieval tool: {str(e)}", exc_info=True)
            return f"Error retrieving documents: {str(e)}"

# Create an instance of the tool
qdrant_retrieval_tool = QdrantRetrievalTool()

def get_qdrant_retrieval_tool():
    """Get the Qdrant retrieval tool configured for Cohere"""
    return qdrant_retrieval_tool