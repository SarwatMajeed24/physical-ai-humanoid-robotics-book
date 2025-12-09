import React from 'react';
import BrowserOnly from '@docusaurus/BrowserOnly';

// Mermaid diagram component
const MermaidDiagram = ({ chart, altText, title }) => {
  const id = React.useMemo(() => `mermaid-${Math.random().toString(36).substr(2, 9)}`, []);

  return (
    <div className="mermaid-diagram-container">
      <div className="diagram-container">
        <BrowserOnly>
          {() => {
            const { mermaid } = require('mermaid');
            // Configure mermaid
            mermaid.initialize({
              startOnLoad: true,
              theme: 'default',
              securityLevel: 'loose',
              alt: altText,
            });

            return (
              <div
                id={id}
                className="mermaid"
                data-title={title}
                aria-label={altText}
                dangerouslySetInnerHTML={{ __html: chart }}
              />
            );
          }}
        </BrowserOnly>
      </div>
      <div className="mermaid-diagram-alt-text" style={{ display: 'none' }} aria-hidden="true">
        {altText}
      </div>
    </div>
  );
};

// Code snippet component with copy functionality
const CodeBlock = ({ children, language, title }) => {
  return (
    <div className="code-block-wrapper">
      {title && <h5 className="code-block-title">{title}</h5>}
      <div className="code-block-container">
        <pre>
          <code className={`language-${language}`}>
            {children}
          </code>
        </pre>
      </div>
    </div>
  );
};

// Citation component for IEEE-style references
const Citation = ({ id, authors, title, journal, year, volume, issue, pages, doi, link }) => {
  // Format authors in IEEE style (first initial. last name, first initial. last name, and first initial. last name)
  const formatAuthors = (authors) => {
    if (typeof authors === 'string') {
      return authors;
    }
    if (Array.isArray(authors)) {
      if (authors.length === 1) {
        return authors[0];
      } else if (authors.length === 2) {
        return `${authors[0]} and ${authors[1]}`;
      } else {
        return `${authors[0]}, et al.`;
      }
    }
    return authors || '';
  };

  const formattedAuthors = formatAuthors(authors);

  let citationText = `${formattedAuthors}, "${title}", ${journal}`;
  if (volume) citationText += `, vol. ${volume}`;
  if (issue) citationText += `, no. ${issue}`;
  if (pages) citationText += `, pp. ${pages}`;
  if (year) citationText += `, ${year}`;
  if (doi) citationText += `, doi: ${doi}`;

  return (
    <div className="citation" id={`cite-${id}`}>
      <p className="citation-text">
        <sup>[{id}]</sup> {citationText}.
        {link && <a href={link} target="_blank" rel="noopener noreferrer"> [Online]</a>}
      </p>
    </div>
  );
};

// Table of Contents component for chapters
const ChapterTOC = ({ items }) => {
  return (
    <nav className="chapter-toc">
      <h3>Chapter Contents</h3>
      <ul>
        {items.map((item, index) => (
          <li key={index}>
            <a href={item.href}>{item.title}</a>
          </li>
        ))}
      </ul>
    </nav>
  );
};

export { MermaidDiagram, CodeBlock, Citation, ChapterTOC };