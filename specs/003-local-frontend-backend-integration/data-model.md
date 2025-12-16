# Data Model: Local Frontend-Backend Integration for RAG Chatbot

## Entities

### ChatMessage
- **message_id**: string (UUID) - Unique identifier for the message
- **sender**: string (enum: "user", "bot") - The sender of the message
- **text**: string - The text content of the message
- **timestamp**: datetime - When the message was created
- **selected_text**: string (optional) - Text selected by user when message was sent
- **sources**: array of SourceReference (optional) - Sources referenced in response

### SourceReference
- **url**: string - URL of the source document
- **title**: string - Title of the source document
- **snippet**: string - Excerpt from the source document

### ChatRequest
- **query**: string - The user's question or input text
- **selected_text**: string (optional) - Text selected on the page by the user
- **session_id**: string (optional) - Session identifier (auto-generated if not provided)

### ChatResponse
- **response**: string - The generated response from the backend
- **session_id**: string - Session identifier for the conversation
- **sources**: array of SourceReference - Sources referenced in the response
- **timestamp**: datetime - When the response was generated

## Relationships

- ChatMessage contains optional SourceReference (1 to many) in bot messages
- ChatRequest is processed to generate ChatResponse (1 to 1)
- ChatResponse may include multiple SourceReferences (1 to many)

## State Transitions

### Message States
- `sent` → `processing` → `delivered` (for user messages)
- `received` → `generating` → `delivered` (for bot responses)

## Validation Rules

### ChatMessage
- message_id must be a valid UUID
- sender must be either "user" or "bot"
- text must not be empty
- timestamp must be a valid datetime

### ChatRequest
- query must not be empty or only whitespace
- selected_text (if provided) must not exceed 10000 characters
- session_id (if provided) must be a valid identifier

### ChatResponse
- response must not be empty
- session_id must match the corresponding request
- sources array must contain valid SourceReference objects

## API Contract

### Request Format
```
{
  "query": "User's question",
  "selected_text": "Optional selected text context",
  "session_id": "Optional session identifier"
}
```

### Response Format
```
{
  "response": "Generated response",
  "session_id": "Session identifier",
  "sources": [
    {
      "url": "Source URL",
      "title": "Source title",
      "snippet": "Content snippet"
    }
  ],
  "timestamp": "ISO datetime string"
}
```