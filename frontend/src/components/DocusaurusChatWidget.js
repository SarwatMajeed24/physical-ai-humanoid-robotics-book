import React from 'react';
import { useColorMode } from '@docusaurus/theme-common';
import ChatWidget from './ChatWidget';
import './DocusaurusChatWidget.css';

const DocusaurusChatWidget = () => {
  const { colorMode } = useColorMode();

  // Apply theme-specific styles if needed
  const themeClass = `chat-widget-theme--${colorMode}`;

  return (
    <div className={`docusaurus-chat-widget ${themeClass}`}>
      <ChatWidget />
    </div>
  );
};

export default DocusaurusChatWidget;