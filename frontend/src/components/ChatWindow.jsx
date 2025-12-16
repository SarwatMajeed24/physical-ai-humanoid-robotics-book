import React, { useState, useRef, useEffect } from 'react';
import Message from './Message';
import './ChatWindow.css';

const ChatWindow = ({
  messages = [],
  onSendMessage,
  isLoading = false,
  onClose,
  title = "AI Assistant"
}) => {
  const [inputValue, setInputValue] = useState('');
  const [selectedText, setSelectedText] = useState('');
  const messagesEndRef = useRef(null);
  const inputRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (inputValue.trim() && onSendMessage) {
      onSendMessage(inputValue, selectedText);
      setInputValue('');
    }
  };

  // Capture selected text when user types
  useEffect(() => {
    const handleSelection = () => {
      const selectedText = window.getSelection().toString().trim();
      if (selectedText) {
        setSelectedText(selectedText);
      }
    };

    document.addEventListener('mouseup', handleSelection);
    return () => {
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  return (
    <div className="chat-window">
      <div className="chat-header">
        <div className="chat-title">{title}</div>
        <button className="close-button" onClick={onClose}>×</button>
      </div>

      <div className="chat-messages">
        {messages.length === 0 ? (
          <div className="welcome-message">
            <p>Hello! I'm your AI assistant for the Physical AI & Humanoid Robotics book.</p>
            <p>Ask me anything about the content, or select text on the page for context-aware answers.</p>
          </div>
        ) : (
          messages.map((msg, index) => (
            <Message
              key={index}
              message={msg.content}
              isUser={msg.role === 'user'}
            />
          ))
        )}
        {isLoading && (
          <div className="message bot-message">
            <div className="message-content">
              <div className="typing-indicator">
                <span></span>
                <span></span>
                <span></span>
              </div>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="chat-input-form" onSubmit={handleSubmit}>
        <input
          ref={inputRef}
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Ask about the book content..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading || !inputValue.trim()}>
          {isLoading ? 'Sending...' : '→'}
        </button>
      </form>
    </div>
  );
};

export default ChatWindow;