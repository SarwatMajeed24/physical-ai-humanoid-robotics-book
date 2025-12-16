# ADR-0001: RAG Chatbot Widget Integration with Docusaurus

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-16
- **Feature:** rag-chatbot
- **Context:** Need to integrate a RAG (Retrieval-Augmented Generation) chatbot widget into an existing Docusaurus documentation site for the Physical AI & Humanoid Robotics book. The widget must be accessible on all pages, provide seamless user experience, and maintain the educational value of the content while enabling interactive learning through AI-powered Q&A functionality.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

Integrate the RAG chatbot as a persistent floating widget in the Docusaurus site using theme component override approach:

- **Widget Placement**: Floating bottom-right icon with neon styling that appears on all pages
- **Component Architecture**: Custom React component (RagChat.js) with CSS styling and state management
- **Integration Method**: Override Docusaurus Layout theme component to inject widget globally
- **UI/UX Approach**: Toggleable interface with smooth animations, responsive design for mobile
- **Backend Connection**: Direct API calls to RAG service at http://localhost:8000/chat
- **Styling**: CSS with modern gradients, animations, and responsive breakpoints

## Consequences

### Positive

- **Global Accessibility**: Chatbot available on all pages without requiring individual page modifications
- **Non-intrusive Design**: Floating icon doesn't interfere with reading experience until activated
- **Consistent User Experience**: Same interface across all documentation pages
- **Performance**: Minimal impact on page load times (widget loads only when needed)
- **Maintainability**: Centralized component that can be updated globally
- **Educational Enhancement**: Enables interactive learning by allowing students to ask questions about content
- **Selected Text Integration**: Users can select text and ask questions about specific passages

### Negative

- **Additional Dependencies**: New CSS and React components increase bundle size
- **Potential Conflicts**: Theme override might conflict with future Docusaurus updates
- **Memory Usage**: Widget remains in memory on all pages (though minimized when closed)
- **Mobile Constraints**: Floating element might interfere with touch interactions on small screens
- **Backend Coupling**: Direct dependency on RAG service endpoint creates tight coupling

## Alternatives Considered

Alternative A: Page-specific integration approach
- Embed widget in individual MDX files using Docusaurus MDX components
- Why rejected: Requires manual addition to every page, harder to maintain, inconsistent across pages

Alternative B: Separate chat page approach
- Create dedicated chat page with full-screen interface
- Why rejected: Less accessible, breaks context of current content, reduces serendipitous interaction

Alternative C: Toolbar integration approach
- Add chat functionality to existing Docusaurus navbar or sidebar
- Why rejected: Would clutter existing navigation, limited space for rich chat interface

Alternative D: Native browser extension approach
- Implement as separate browser extension
- Why rejected: Higher barrier to entry, additional installation steps, harder distribution

## References

- Feature Spec: /specs/002-rag-chatbot/spec.md
- Implementation Plan: /specs/002-rag-chatbot/plan.md
- Related ADRs: None
- Evaluator Evidence: /history/prompts/002-rag-chatbot/001-embed-rag-chatbot-widget-in-frontend-permanently.green.prompt.md
