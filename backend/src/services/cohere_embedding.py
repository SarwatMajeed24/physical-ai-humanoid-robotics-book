import cohere
from typing import List, Optional
from ..config.settings import settings
import logging

logger = logging.getLogger(__name__)

class CohereEmbeddingService:
    def __init__(self, model_name: str = "embed-english-v3.0"):
        if not settings.COHERE_API_KEY:
            raise ValueError("COHERE_API_KEY environment variable is not set")

        self.client = cohere.Client(settings.COHERE_API_KEY)
        self.model_name = model_name

    def generate_embedding(self, text: str) -> Optional[List[float]]:
        """Generate a single embedding for the given text"""
        try:
            if not text or not text.strip():
                logger.warning("Empty text provided for embedding generation")
                return None

            response = self.client.embed(
                texts=[text],
                model=self.model_name,
                input_type="search_document"
            )
            return response.embeddings[0]  # Return the first (and only) embedding
        except Exception as e:
            logger.error(f"Error generating embedding for text: {str(e)}")
            return None

    def generate_embeddings(self, texts: List[str]) -> Optional[List[List[float]]]:
        """Generate embeddings for multiple texts"""
        try:
            # Filter out empty texts but keep track of positions for proper alignment
            non_empty_texts = [text for text in texts if text and text.strip()]

            if not non_empty_texts:
                # Return empty embeddings for all input texts
                return [[] for _ in texts]

            response = self.client.embed(
                texts=non_empty_texts,
                model=self.model_name,
                input_type="search_document"
            )

            # Align embeddings back to original positions
            embeddings = response.embeddings
            result = []
            text_idx = 0
            for text in texts:
                if text and text.strip():
                    result.append(embeddings[text_idx])
                    text_idx += 1
                else:
                    result.append([])  # Empty embedding for empty text

            return result
        except Exception as e:
            logger.error(f"Error generating embeddings for {len(texts)} texts: {str(e)}")
            return None

    def generate_query_embedding(self, query: str) -> Optional[List[float]]:
        """Generate an embedding for a query (using search_query input type)"""
        try:
            if not query or not query.strip():
                logger.warning("Empty query provided for embedding generation")
                return None

            response = self.client.embed(
                texts=[query],
                model=self.model_name,
                input_type="search_query"
            )
            return response.embeddings[0]  # Return the first (and only) embedding
        except Exception as e:
            logger.error(f"Error generating query embedding: {str(e)}")
            return None

    def generate_document_embedding(self, document: str) -> Optional[List[float]]:
        """Generate an embedding for a document chunk (using search_document input type)"""
        try:
            if not document or not document.strip():
                logger.warning("Empty document provided for embedding generation")
                return None

            response = self.client.embed(
                texts=[document],
                model=self.model_name,
                input_type="search_document"
            )
            return response.embeddings[0]  # Return the first (and only) embedding
        except Exception as e:
            logger.error(f"Error generating document embedding: {str(e)}")
            return None

    async def embed_content_chunks(self, chunks: List[str]) -> Optional[List[List[float]]]:
        """Generate embeddings for content chunks (for T016)"""
        try:
            if not chunks:
                logger.warning("Empty chunks list provided for embedding generation")
                return None

            # Filter out empty chunks
            filtered_chunks = [chunk for chunk in chunks if chunk and chunk.strip()]
            if not filtered_chunks:
                logger.warning("No valid chunks to embed after filtering")
                return None

            response = self.client.embed(
                texts=filtered_chunks,
                model=self.model_name,
                input_type="search_document"
            )

            # Align embeddings back to original positions
            embeddings = response.embeddings
            result = []
            chunk_idx = 0
            for chunk in chunks:
                if chunk and chunk.strip():
                    result.append(embeddings[chunk_idx])
                    chunk_idx += 1
                else:
                    result.append([])  # Empty embedding for empty chunk

            return result
        except Exception as e:
            logger.error(f"Error generating embeddings for content chunks: {str(e)}")
            return None