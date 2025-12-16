import React from 'react';
import './FloatingIcon.css';

const FloatingIcon = ({ onClick, isOpen, notificationCount = 0 }) => {
  return (
    <div className="floating-icon-container">
      <button
        className={`floating-icon ${isOpen ? 'open' : ''}`}
        onClick={onClick}
        aria-label={isOpen ? "Close chat" : "Open chat"}
        title={isOpen ? "Close chat" : "Open chat - Ask about Physical AI & Robotics"}
      >
        {notificationCount > 0 && (
          <span className="notification-badge">{notificationCount}</span>
        )}
        <div className="icon-content">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M21 15C21 15.5304 20.7893 16.0391 20.4142 16.4142C20.0391 16.7893 19.5304 17 19 17H16.5L14.03 19.56C13.8 19.82 13.49 19.99 13.16 20.02C12.83 20.05 12.5 19.94 12.25 19.7C12.0846 19.5588 11.9509 19.3838 11.8575 19.1877C11.7642 18.9916 11.7129 18.7791 11.7067 18.56L11.5 17H5C4.46957 17 3.96086 16.7893 3.58579 16.4142C3.21071 16.0391 3 15.5304 3 15V6C3 5.46957 3.21071 4.96086 3.58579 4.58579C3.96086 4.21071 4.46957 4 5 4H19C19.5304 4 20.0391 4.21071 20.4142 4.58579C20.7893 4.96086 21 5.46957 21 6V15Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
        </div>
      </button>
    </div>
  );
};

export default FloatingIcon;