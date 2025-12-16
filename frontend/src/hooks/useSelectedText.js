import { useState, useEffect } from 'react';

const useSelectedText = () => {
  const [selectedText, setSelectedText] = useState('');

  useEffect(() => {
    const handleSelection = () => {
      const text = window.getSelection().toString().trim();
      setSelectedText(text);
    };

    // Listen for selection changes
    document.addEventListener('selectionchange', handleSelection);
    document.addEventListener('mouseup', handleSelection);

    // Cleanup event listeners on unmount
    return () => {
      document.removeEventListener('selectionchange', handleSelection);
      document.removeEventListener('mouseup', handleSelection);
    };
  }, []);

  return { selectedText, clearSelectedText: () => setSelectedText('') };
};

export default useSelectedText;