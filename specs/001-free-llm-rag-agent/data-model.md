# Data Model: Free LLM RAG Agent for Physical AI Book

## Entities

### ChatSession
- **session_id**: string (UUID) - Unique identifier for the conversation session
- **created_at**: datetime - Timestamp when the session was created
- **messages**: array of Message objects - List of all messages in the session
- **metadata**: object - Additional session information (user agent, etc.)

### Message
- **message_id**: string (UUID) - Unique identifier for the message
- **role**: string (enum: "user", "assistant") - The role of the message sender
- **content**: string - The text content of the message
- **timestamp**: datetime - When the message was created
- **selected_text**: string (optional) - Text selected by user when message was sent
- **sources**: array of SourceReference (assistant messages only) - Sources used in response

### SourceReference
- **url**: string - URL of the source document
- **title**: string - Title of the source document
- **snippet**: string - Excerpt from the source document

### Query
- **query**: string - The user's question or input text
- **selected_text**: string (optional) - Text selected on the page by the user
- **session_id**: string (optional) - Session identifier (generated if not provided)

### ChatResponse
- **response**: string - The generated response from the Gemini agent
- **session_id**: string - Session identifier for the conversation
- **sources**: array of SourceReference - Sources referenced in the response
- **timestamp**: datetime - When the response was generated

### DocumentChunk
- **chunk_id**: string (UUID) - Unique identifier for the document chunk
- **content**: string - The text content of the chunk
- **url**: string - URL of the original document
- **title**: string - Title of the original document
- **embedding**: array of float - Vector embedding of the content
- **metadata**: object - Additional metadata about the chunk (page number, section, etc.)

## Relationships

- ChatSession contains multiple Messages (1 to many)
- Message may reference multiple SourceReferences (1 to many) in assistant messages
- ChatResponse may include multiple SourceReferences (1 to many)
- Query is processed to generate a ChatResponse (1 to 1)

## State Transitions

### Message States
- `created` → `processing` → `completed` (for user messages)
- `received` → `generating` → `completed` (for assistant messages)

## Validation Rules

### ChatSession
- session_id must be a valid UUID
- created_at must be a valid datetime
- messages array must not exceed 1000 items

### Message
- message_id must be a valid UUID
- role must be either "user" or "assistant"
- content must not be empty
- timestamp must be a valid datetime

### Query
- query must not be empty or only whitespace
- selected_text (if provided) must not exceed 10000 characters

### DocumentChunk
- chunk_id must be a valid UUID
- content must not be empty
- embedding must be a valid vector array
- url must be a valid URL format