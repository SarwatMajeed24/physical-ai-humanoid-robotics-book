# Data Model: RAG Chatbot for Physical AI Book

## Entity: BookContentChunk

**Description**: Represents a chunk of book content that has been processed and embedded for RAG retrieval

**Fields**:
- `id` (string): Unique identifier for the content chunk
- `url` (string): Original URL of the source page
- `title` (string): Title of the source content
- `content` (string): The actual text content of the chunk
- `embedding` (list[float]): Vector embedding of the content (1024 dimensions for Cohere)
- `section` (string): Book section identifier (e.g., "Chapter 1", "Module 3")
- `created_at` (datetime): Timestamp when the chunk was created
- `updated_at` (datetime): Timestamp when the chunk was last updated

**Relationships**:
- None (standalone entity stored in vector database)

**Validation Rules**:
- `url` must be a valid URL
- `content` must not be empty and less than 10,000 characters
- `embedding` must have exactly 1024 dimensions
- `id` must be unique

## Entity: ChatSession

**Description**: Represents a user's chat session with the RAG system

**Fields**:
- `session_id` (string): Unique identifier for the session
- `user_id` (string): Identifier for the user (optional, can be anonymous)
- `created_at` (datetime): Timestamp when session was created
- `updated_at` (datetime): Timestamp when session was last updated
- `messages` (list[Message]): List of messages in the session

**Relationships**:
- Contains multiple Message entities

**Validation Rules**:
- `session_id` must be unique
- `messages` array cannot exceed 100 messages

## Entity: Message

**Description**: Represents a single message in a chat session

**Fields**:
- `message_id` (string): Unique identifier for the message
- `session_id` (string): Reference to the parent ChatSession
- `role` (string): Either "user" or "assistant"
- `content` (string): The text content of the message
- `timestamp` (datetime): When the message was created
- `context_chunks` (list[string]): IDs of content chunks used to generate the response
- `selected_text` (string): Text that was selected by user when message was sent (optional)

**Relationships**:
- Belongs to one ChatSession
- References multiple BookContentChunk entities via context_chunks

**Validation Rules**:
- `role` must be either "user" or "assistant"
- `content` must not be empty
- `session_id` must reference an existing ChatSession

## Entity: CrawlRecord

**Description**: Represents a record of content crawling and processing

**Fields**:
- `crawl_id` (string): Unique identifier for the crawl operation
- `url` (string): URL that was crawled
- `status` (string): Status of the crawl ("success", "failed", "pending")
- `content_hash` (string): Hash of the content to detect changes
- `processed_at` (datetime): When the content was processed
- `chunk_count` (int): Number of chunks created from this URL

**Relationships**:
- None (standalone entity for tracking)

**Validation Rules**:
- `url` must be a valid URL
- `status` must be one of the allowed values
- `content_hash` must be a valid SHA-256 hash

## State Transitions

### ChatSession States
- `active` → When first created
- `active` → `inactive` → After 30 minutes of inactivity
- `inactive` → `archived` → After 30 days of inactivity

### CrawlRecord States
- `pending` → When crawl is initiated
- `pending` → `success` → When content is successfully processed
- `pending` → `failed` → When there's an error in crawling or processing