from typing import List, Dict, Any, Optional
from datetime import datetime
import logging
from ..models.chat import ChatRequest, ChatResponse, SourceReference
from ..services.cohere_embedding import CohereEmbeddingService
from ..services.cohere_llm import CohereLLMService
from ..services.vector_store import QdrantVectorStore
from ..config.settings import settings

logger = logging.getLogger(__name__)

class RAGChain:
    def __init__(self):
        self.embedding_service = CohereEmbeddingService()
        self.llm_service = CohereLLMService()
        self.vector_store = QdrantVectorStore()

    async def retrieve_and_generate(self, query: str, selected_text: Optional[str] = None) -> ChatResponse:
        """Main RAG method: retrieve relevant content and generate response"""
        try:
            if not query or not query.strip():
                return ChatResponse(
                    response="Please enter a question to get started!",
                    session_id="temp_session",
                    sources=[],
                    timestamp=datetime.now()
                )

            # Generate embedding for the query
            query_embedding = self.embedding_service.generate_query_embedding(query)
            if not query_embedding:
                logger.warning("Failed to generate query embedding")
                return ChatResponse(
                    response="I'm having trouble retrieving info right now. Please try a different question!",
                    session_id="temp_session",
                    sources=[],
                    timestamp=datetime.now()
                )

            # Retrieve relevant chunks from vector store
            relevant_chunks = await self.vector_store.retrieve_similar(query_embedding, limit=10)

            # Check if collection exists and has content
            if not relevant_chunks:
                # Check if the collection is empty by getting count
                chunk_count = await self.vector_store.get_all_chunks_count()
                if chunk_count == 0:
                    return ChatResponse(
                        response="Book content is being indexed. Please try again in a moment!",
                        session_id="temp_session",
                        sources=[],
                        timestamp=datetime.now()
                    )
                else:
                    # Provide a fallback response with general knowledge about humanoid robotics
                    fallback_response = f"I couldn't find specific info on that in the book, but here's what I know about humanoid robotics...\n\n{await self._generate_fallback_response(query)}"
                    return ChatResponse(
                        response=fallback_response,
                        session_id="temp_session",
                        sources=[],
                        timestamp=datetime.now()
                    )

            # Prepare context from retrieved chunks
            context_texts = []
            sources = []

            for chunk in relevant_chunks:
                if chunk.get("content"):
                    context_texts.append(chunk["content"])
                    sources.append({
                        "url": chunk.get("url", ""),
                        "title": chunk.get("title", ""),
                        "snippet": chunk["content"][:200] + "..." if len(chunk["content"]) > 200 else chunk["content"],
                        "score": chunk.get("score", 0.0)  # Include relevance score for better sorting/display
                    })

            # If selected text is provided, add it to the context
            if selected_text:
                context_texts.insert(0, f"User selected text: {selected_text}\n\n")

            # Combine context for generation
            context = "\n\n".join(context_texts) if context_texts else "No relevant content found in the book."

            # Generate response using Cohere
            response_text = await self.llm_service.chat_with_context(query, context)

            # Post-processing to avoid strict "no answer" responses
            if not response_text or "not contained within context" in response_text.lower() or "doesn't contain relevant information" in response_text.lower():
                # Provide a more helpful fallback response
                response_text = f"I couldn't find specific info on that in the book, but here's what I know about humanoid robotics...\n\n{await self._generate_fallback_response(query)}"

            # Validate Cohere response
            if not response_text or response_text.strip() == "":
                response_text = f"I couldn't find specific info on that in the book, but here's what I know about humanoid robotics...\n\nI couldn't generate a complete response for your query. Please try rephrasing your question about '{query}'."

            # Create ChatResponse
            chat_response = ChatResponse(
                response=response_text,
                session_id="temp_session",  # Will be replaced by actual session_id in API
                sources=sources,
                timestamp=datetime.now()
            )

            return chat_response
        except ValueError as ve:
            logger.warning(f"Validation error in RAG chain: {str(ve)}")
            return ChatResponse(
                response="Please enter a valid question.",
                session_id="temp_session",
                sources=[],
                timestamp=datetime.now()
            )
        except Exception as e:
            logger.error(f"Error in RAG chain: {str(e)}")
            # Return a user-friendly error response
            return ChatResponse(
                response="Book content is being indexed. Please try again in a moment!",
                session_id="temp_session",
                sources=[],
                timestamp=datetime.now()
            )

    async def process_query_with_context(self, query: str, context_chunks: List[Dict[str, Any]]) -> str:
        """Process query with specific context chunks"""
        try:
            context = "\n\n".join([chunk["content"] for chunk in context_chunks])
            return await self.llm_service.chat_with_context(query, context)
        except Exception as e:
            logger.error(f"Error processing query with context: {str(e)}")
            return "I'm sorry, but I couldn't process your query at this time."

    async def _generate_fallback_response(self, query: str) -> str:
        """Generate a fallback response when no relevant documents are found"""
        try:
            # Use the LLM service to generate a response based on the query
            # even without specific context from the book
            fallback_context = "This is a general response about humanoid robotics when specific book content is not available."
            return await self.llm_service.chat_with_context(query, fallback_context)
        except Exception as e:
            logger.error(f"Error generating fallback response: {str(e)}")
            return f"I couldn't find specific information about '{query}' in the book. The book covers topics like physical AI, humanoid robotics, ROS, machine learning applications in robotics, and related subjects. Try asking about specific concepts or rephrasing your question."