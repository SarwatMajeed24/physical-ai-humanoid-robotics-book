import React, { useState, useRef, useEffect } from 'react';
import './RagChat.css';

const RagChat = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [useAgent, setUseAgent] = useState(false);
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const sendMessage = async (useAgent = false) => {
    if (!inputValue.trim() || isLoading) return;

    const userMessage = { id: Date.now(), text: inputValue, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      // Get selected text if any
      const selectedText = window.getSelection?.().toString()?.trim() || '';

      // Determine which endpoint to use based on the useAgent parameter
      const endpoint = useAgent ? 'https://physical-ai-humanoid-robotics-book-lovat.vercel.app/api/v1/agent/chat' : 'https://physical-ai-humanoid-robotics-book-lovat.vercel.app/api/v1/chat';

      const response = await fetch(endpoint, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: inputValue,
          selected_text: selectedText || undefined,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      const botMessage = {
        id: Date.now() + 1,
        text: data.response,
        sender: 'bot',
        sources: data.sources || [],
      };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      // The backend now returns user-friendly error messages, so we don't need to show the generic error
      // If there's still a network error, we'll show a more appropriate message
      const errorMessage = {
        id: Date.now() + 1,
        text: 'I\'m having trouble connecting right now. Please check your connection and try again.',
        sender: 'bot',
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage(useAgent);
    }
  };

  const toggleChat = () => {
    setIsOpen(!isOpen);
    if (!isOpen) {
      setTimeout(() => inputRef.current?.focus(), 100);
    }
  };

  const clearChat = () => {
    setMessages([]);
  };

  const closeChat = () => {
    setMessages([]);
    setIsOpen(false);
  };

  return (
    <>
      {/* Floating Chat Icon */}
      {!isOpen && (
        <div className="rag-chat-float" onClick={toggleChat}>
          <div className="rag-chat-icon">
            <svg width="40" height="40" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M12 2C13.5912 2 15.1174 2.63214 16.2426 3.75736C17.3679 4.88258 18 6.40883 18 8C18 9.59117 17.3679 11.1174 16.2426 12.2426C15.1174 13.3679 13.5912 14 12 14C10.4088 14 8.88258 13.3679 7.75736 12.2426L6 14V12.2426C4.88258 11.1174 4.24264 9.59117 4.24264 8C4.24264 6.40883 4.88258 4.88258 6 3.75736C7.11742 2.63214 8.64367 2 10.2348 2H12Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M9 10L11 12L13 10" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              <path d="M9 15H15" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </div>
        </div>
      )}

      {/* Chat Window */}
      {isOpen && (
        <div className="rag-chat-container">
          <div className="rag-chat-header">
            <div className="rag-chat-title">AI Assistant</div>
            <div className="rag-chat-controls">
              <button className="rag-chat-clear" onClick={clearChat} title="Clear Chat">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M19 7L18.1327 19.1425C18.0574 20.1891 17.1891 21.0574 16.1425 21.1327L5.85752 21.8673C4.81088 21.9426 4.05736 21.1891 3.94262 20.1327L3 7M10 11V17M14 11V17M15 7V4C15 3.44772 14.5523 3 14 3H10C9.44772 3 9 3.44772 9 4V7M4 7H20" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
              <div className="rag-chat-mode-toggle">
                <label className="rag-chat-mode-label">
                  <input
                    type="checkbox"
                    checked={useAgent}
                    onChange={(e) => setUseAgent(e.target.checked)}
                    className="rag-chat-mode-checkbox"
                  />
                  <span className="rag-chat-mode-text">Agent Mode</span>
                </label>
              </div>
              <button className="rag-chat-close" onClick={closeChat}>
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
              </button>
            </div>
          </div>

          <div className="rag-chat-messages">
            {messages.length === 0 ? (
              <div className="rag-chat-welcome">
                <h3>Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book.</h3>
                <p>Ask me anything about the content, and I'll help you find relevant information.</p>
                <p>You can select text on the page and ask questions about it!</p>
                <p>Toggle "Agent Mode" to use advanced tool-based responses.</p>
              </div>
            ) : (
              messages.map((message) => (
                <div key={message.id} className={`rag-chat-message rag-chat-message-${message.sender}`}>
                  <div className="rag-chat-message-content">
                    {message.text}
                  </div>
                  {message.sources && message.sources.length > 0 && (
                    <div className="rag-chat-sources">
                      <small>Sources:</small>
                      {message.sources.map((source, index) => (
                        <div key={index} className="rag-chat-source">
                          <a href={source.url} target="_blank" rel="noopener noreferrer">
                            {source.title}
                          </a>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              ))
            )}
            {isLoading && (
              <div className="rag-chat-message rag-chat-message-bot">
                <div className="rag-chat-typing-indicator">
                  <div className="rag-chat-typing-dot"></div>
                  <div className="rag-chat-typing-dot"></div>
                  <div className="rag-chat-typing-dot"></div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="rag-chat-input-container">
            <textarea
              ref={inputRef}
              className="rag-chat-input"
              value={inputValue}
              onChange={(e) => setInputValue(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Ask about the book content..."
              rows={1}
            />
            <button
              className="rag-chat-send"
              onClick={() => sendMessage(useAgent)}
              disabled={isLoading || !inputValue.trim()}
            >
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M22 2L11 13M22 2L15 22L11 13M11 13L2 9L22 2" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
              </svg>
            </button>
          </div>
        </div>
      )}
    </>
  );
};

export default RagChat;