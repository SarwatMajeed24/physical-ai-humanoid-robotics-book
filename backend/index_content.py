#!/usr/bin/env python3
"""
Script to crawl, embed, and index the book content into Qdrant
"""
import asyncio
import sys
import os
from datetime import datetime

# Add the src directory to the path so we can import our modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '.'))

from src.services.crawler import SitemapCrawler
from src.services.cohere_embedding import CohereEmbeddingService
from src.services.vector_store import QdrantVectorStore
from src.models.embedding import BookContentChunk
from src.config.settings import settings

async def index_book_content():
    """Main function to crawl, embed, and index book content"""
    print("Starting book content indexing process...")

    if not settings.COHERE_API_KEY:
        print("Error: COHERE_API_KEY environment variable is not set")
        return False

    if not settings.QDRANT_URL:
        print("Error: QDRANT_URL environment variable is not set")
        return False

    try:
        # Initialize services
        crawler = SitemapCrawler()
        embedding_service = CohereEmbeddingService()
        vector_store = QdrantVectorStore()

        print("Crawling sitemap and extracting content...")
        pages_content = await crawler.fetch_all_pages_from_sitemap()

        if not pages_content:
            print("No content found to index")
            return False

        print(f"Found {len(pages_content)} pages to process")

        # Process each page and create content chunks
        all_chunks = []
        for url, title, content in pages_content:
            print(f"Processing: {url}")

            # Chunk the content
            chunks = crawler.chunk_content(title, content, url)

            # Generate embeddings for each chunk
            chunk_texts = [chunk.content for chunk in chunks]
            if chunk_texts:
                embeddings = await embedding_service.embed_content_chunks(chunk_texts)

                if embeddings:
                    for i, chunk in enumerate(chunks):
                        if i < len(embeddings):
                            chunk.embedding = embeddings[i]
                            all_chunks.append(chunk)
                    print(f"  Processed {len(chunks)} chunks with embeddings")
                else:
                    print(f"  Failed to generate embeddings for {url}")
            else:
                print(f"  No text content to embed from {url}")

        print(f"Total chunks ready for storage: {len(all_chunks)}")

        # Store all chunks in Qdrant
        print("Storing content in Qdrant vector store...")
        success = await vector_store.create_collection_and_store_chunks(all_chunks)

        if success:
            print(f"Successfully indexed {len(all_chunks)} content chunks into Qdrant collection '{settings.QDRANT_COLLECTION_NAME}'")

            # Print final status
            count = await vector_store.get_all_chunks_count()
            print(f"Total indexed chunks in collection: {count}")

            return True
        else:
            print("Failed to store content in Qdrant")
            return False

    except Exception as e:
        print(f"Error during indexing process: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = asyncio.run(index_book_content())
    sys.exit(0 if success else 1)