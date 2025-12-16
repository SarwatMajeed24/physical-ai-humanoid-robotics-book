import React, { useState, useEffect } from 'react';
import ChatWindow from './ChatWindow';
import FloatingIcon from './FloatingIcon';
import chatService from '../services/chatService';
import useSelectedText from '../hooks/useSelectedText';
import './ChatWidget.css';

const ChatWidget = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [sessionId, setSessionId] = useState(null);
  const [error, setError] = useState(null);

  // Use the selected text hook
  const { selectedText } = useSelectedText();

  // Initialize session on component mount
  useEffect(() => {
    const savedSessionId = localStorage.getItem('chatbot-session-id');
    if (savedSessionId) {
      setSessionId(savedSessionId);
    }
  }, []);

  const toggleChat = () => {
    setIsOpen(!isOpen);
  };

  const closeChat = () => {
    setIsOpen(false);
  };

  const handleSendMessage = async (query, providedSelectedText = null) => {
    try {
      setIsLoading(true);
      setError(null);

      // Use provided selected text or fall back to hook's selected text
      const textToUse = providedSelectedText || selectedText;

      // Add user message to UI immediately
      const userMessage = {
        id: Date.now(),
        role: 'user',
        content: query,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, userMessage]);

      // Send message to backend with selected text context
      const response = await chatService.sendMessage(query, sessionId, textToUse);

      // Update session ID if new one was provided
      if (response.session_id && !sessionId) {
        setSessionId(response.session_id);
        localStorage.setItem('chatbot-session-id', response.session_id);
      }

      // Add bot response to messages
      const botMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: response.response,
        sources: response.sources || [],
        timestamp: new Date()
      };

      setMessages(prev => [...prev, botMessage]);

    } catch (err) {
      setError('Failed to send message. Please try again.');
      console.error('Chat error:', err);

      // Add error message to UI
      const errorMessage = {
        id: Date.now(),
        role: 'assistant',
        content: 'Sorry, I encountered an error. Please try again.',
        timestamp: new Date()
      };

      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chat-widget">
      {isOpen ? (
        <div className="chat-popup">
          <ChatWindow
            messages={messages}
            onSendMessage={handleSendMessage}
            isLoading={isLoading}
            onClose={closeChat}
            title="Physical AI Assistant"
          />
        </div>
      ) : null}

      <FloatingIcon
        onClick={toggleChat}
        isOpen={isOpen}
        notificationCount={0} // Could implement unread message count
      />

      {error && (
        <div className="chat-error">
          {error}
        </div>
      )}
    </div>
  );
};

export default ChatWidget;