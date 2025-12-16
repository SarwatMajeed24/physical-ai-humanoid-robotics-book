import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from typing import List, Dict, Tuple
from urllib.parse import urljoin, urlparse
import asyncio
import aiohttp
from datetime import datetime
import hashlib
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter
from ..models.embedding import BookContentChunk
from ..config.settings import settings

logger = logging.getLogger(__name__)

class SitemapCrawler:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'RAG-Chatbot-Crawler/1.0'
        })

        # Initialize text splitter for chunking content
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # 1000 tokens as specified
            chunk_overlap=200,
            length_function=len,
        )

    def parse_sitemap(self, sitemap_url: str) -> List[str]:
        """Parse sitemap and extract all URLs"""
        try:
            response = self.session.get(sitemap_url)
            response.raise_for_status()

            root = ET.fromstring(response.content)

            # Handle both regular sitemaps and sitemap indexes
            urls = []
            namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

            # First, check if this is a sitemap index
            sitemap_locs = root.findall('.//sitemap:sitemap/sitemap:loc', namespace)
            if sitemap_locs:
                # This is a sitemap index, need to fetch individual sitemaps
                for sitemap_loc in sitemap_locs:
                    sitemap_url = sitemap_loc.text.strip()
                    urls.extend(self._parse_individual_sitemap(sitemap_url))
            else:
                # This is a regular sitemap
                url_elements = root.findall('.//sitemap:url/sitemap:loc', namespace)
                urls = [elem.text.strip() for elem in url_elements]

            # Fix domain issue: replace incorrect domain with correct one
            corrected_urls = []
            for url in urls:
                # Replace the incorrect domain with the correct one
                if url.startswith('https://sweetoo.github.io/'):
                    corrected_url = url.replace('https://sweetoo.github.io/', 'https://physical-ai-humanoid-robotics-book-lovat.vercel.app/')
                    corrected_urls.append(corrected_url)
                else:
                    corrected_urls.append(url)

            return corrected_urls
        except Exception as e:
            logger.error(f"Error parsing sitemap {sitemap_url}: {str(e)}")
            return []

    def _parse_individual_sitemap(self, sitemap_url: str) -> List[str]:
        """Parse an individual sitemap URL"""
        try:
            response = self.session.get(sitemap_url)
            response.raise_for_status()

            root = ET.fromstring(response.content)
            namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

            url_elements = root.findall('.//sitemap:url/sitemap:loc', namespace)
            urls = [elem.text.strip() for elem in url_elements]

            # Fix domain issue: replace incorrect domain with correct one
            corrected_urls = []
            for url in urls:
                # Replace the incorrect domain with the correct one
                if url.startswith('https://sweetoo.github.io/'):
                    corrected_url = url.replace('https://sweetoo.github.io/', 'https://physical-ai-humanoid-robotics-book-lovat.vercel.app/')
                    corrected_urls.append(corrected_url)
                else:
                    corrected_urls.append(url)

            return corrected_urls
        except Exception as e:
            logger.error(f"Error parsing individual sitemap {sitemap_url}: {str(e)}")
            return []

    def extract_content_from_url(self, url: str) -> Tuple[str, str]:
        """Extract title and content from a URL"""
        try:
            if not url or not url.strip():
                logger.warning("Empty URL provided for content extraction")
                return "", ""

            response = self.session.get(url, timeout=30)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.decompose()

            # Extract title
            title_tag = soup.find('title')
            title = title_tag.get_text().strip() if title_tag else urlparse(url).path.split('/')[-1] or 'Untitled'

            # Extract main content - try to get the most relevant content
            # Look for main content areas first
            main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='main-content') or soup.find('div', class_='content') or soup

            if main_content:
                content = main_content.get_text(separator=' ', strip=True)
            else:
                content = soup.get_text(separator=' ', strip=True)

            # Clean up excessive whitespace
            content = ' '.join(content.split())

            return title, content
        except requests.exceptions.RequestException as re:
            logger.error(f"Network error extracting content from {url}: {str(re)}")
            return "", ""
        except Exception as e:
            logger.error(f"Error extracting content from {url}: {str(e)}")
            return "", ""

    def chunk_content(self, title: str, content: str, url: str) -> List[BookContentChunk]:
        """Chunk content into smaller pieces"""
        try:
            chunks = self.text_splitter.split_text(content)

            book_chunks = []
            for i, chunk_text in enumerate(chunks):
                chunk_id = hashlib.md5(f"{url}_{i}_{chunk_text[:50]}".encode()).hexdigest()

                book_chunk = BookContentChunk(
                    id=chunk_id,
                    url=url,
                    title=title,
                    content=chunk_text,
                    embedding=[],  # Will be filled later
                    section=url.split('/')[-2] if len(url.split('/')) > 2 else 'general',
                    created_at=datetime.now(),
                    updated_at=datetime.now()
                )

                book_chunks.append(book_chunk)

            return book_chunks
        except Exception as e:
            logger.error(f"Error chunking content from {url}: {str(e)}")
            return []

    async def crawl_and_extract_all(self) -> List[BookContentChunk]:
        """Crawl all pages from sitemap and extract content"""
        urls = self.parse_sitemap(settings.BOOK_SITEMAP_URL)
        logger.info(f"Found {len(urls)} URLs to crawl")

        all_chunks = []

        for url in urls:
            logger.info(f"Crawling: {url}")
            title, content = self.extract_content_from_url(url)

            if content:
                chunks = self.chunk_content(title, content, url)
                all_chunks.extend(chunks)
                logger.info(f"Extracted {len(chunks)} chunks from {url}")
            else:
                logger.warning(f"No content extracted from {url}")

        return all_chunks

    async def fetch_all_pages_from_sitemap(self) -> List[Tuple[str, str, str]]:  # Returns (url, title, content)
        """Fetch all pages from sitemap as specified in task T013"""
        urls = self.parse_sitemap(settings.BOOK_SITEMAP_URL)
        logger.info(f"Found {len(urls)} URLs to crawl from sitemap")

        pages_content = []
        for url in urls:
            logger.info(f"Fetching content from: {url}")
            title, content = self.extract_content_from_url(url)
            if content:
                pages_content.append((url, title, content))
            else:
                logger.warning(f"No content extracted from {url}")

        return pages_content

    def get_content_hash(self, content: str) -> str:
        """Generate a hash for content to detect changes"""
        return hashlib.sha256(content.encode()).hexdigest()