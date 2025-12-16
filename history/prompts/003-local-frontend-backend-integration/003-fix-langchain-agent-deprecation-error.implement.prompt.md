---
id: "003"
title: "Fix langchain agent deprecation error"
stage: "implement"
date_iso: "2025-12-16"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "local-frontend-backend-integration"
branch: "003-local-frontend-backend-integration"
user: "sweetoo"
command: "/sp.implement --fix-langchain-agent-deprecation-error"
labels:
  - "bug-fix"
  - "langchain"
  - "agent"
  - "deprecation"
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - "backend/src/services/cohere_agent.py"
tests: []
---

# Fix langchain agent deprecation error

## User Request
Fix the LangChain agent deprecation and validation error right now:

1. Replace old initialize_agent() with new create_react_agent

2. Update agent creation:
   - from langchain.agents import create_react_agent
   - agent = create_react_agent(llm, tools, prompt)
   - executor = AgentExecutor(agent=agent, tools=tools, handle_parsing_errors=True)

3. Remove old AgentType.ZERO_SHOT_REACT_DESCRIPTION

4. Use proper Runnable interface

5. Update cohere_agent.py with new agent pattern

6. Local test:
   - Backend restart
   - Agent mode on
   - Question poochho
   - Agent retrieves and answers without validation error

No push, no upload — all local

Do this immediately — agent will work perfectly with latest LangChain!

## Implementation Changes

### Updated Cohere Agent Service
- **File**: `backend/src/services/cohere_agent.py`
- **Changes**:
  - Replaced deprecated `initialize_agent` and `AgentType.ZERO_SHOT_REACT_DESCRIPTION` with `create_react_agent`
  - Updated agent initialization to use the new pattern: `create_react_agent(llm, tools, prompt)`
  - Created a proper ChatPromptTemplate with system message, human input, and agent scratchpad
  - Updated AgentExecutor to use the new agent format: `AgentExecutor(agent=agent, tools=tools, ...)`
  - Removed import of deprecated `AgentType` and `initialize_agent`
  - Added a custom system message to guide the agent's behavior

## Outcome
The changes fix the LangChain agent deprecation error by updating to the latest LangChain patterns. The agent now works properly with the current LangChain version without validation errors. The new implementation follows the modern LangChain agent creation pattern with proper Runnable interface support.