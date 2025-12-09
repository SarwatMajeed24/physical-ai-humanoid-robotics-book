import React from 'react';
import { ChapterLayout, ChapterSection, RobotSpotlight, QuizSection } from './ChapterLayout';
import { MermaidDiagram, CodeBlock, Citation, ChapterTOC } from './EducationalComponents';

// Main course chapter layout that combines all educational components
const CourseChapter = ({
  title,
  description,
  learningObjectives,
  children,
  robotSpotlights = [],
  quizzes = [],
  diagrams = [],
  citations = [],
  tocItems = []
}) => {
  return (
    <ChapterLayout
      title={title}
      description={description}
      learningObjectives={learningObjectives}
    >
      {tocItems.length > 0 && <ChapterTOC items={tocItems} />}

      <div className="course-chapter-content">
        {children}
      </div>

      {diagrams.length > 0 && (
        <ChapterSection title="Diagrams & Visualizations">
          {diagrams.map((diagram, index) => (
            <MermaidDiagram
              key={index}
              chart={diagram.chart}
              altText={diagram.altText}
              title={diagram.title}
            />
          ))}
        </ChapterSection>
      )}

      {robotSpotlights.length > 0 && (
        <ChapterSection title="Robot Spotlights">
          {robotSpotlights.map((robot, index) => (
            <RobotSpotlight
              key={index}
              robotName={robot.name}
              image={robot.image}
              specs={robot.specs}
              description={robot.description}
            />
          ))}
        </ChapterSection>
      )}

      {quizzes.length > 0 && (
        <ChapterSection title="Knowledge Checks">
          {quizzes.map((quiz, index) => (
            <QuizSection
              key={index}
              question={quiz.question}
              options={quiz.options}
              correctAnswer={quiz.correctAnswer}
            />
          ))}
        </ChapterSection>
      )}

      {citations.length > 0 && (
        <ChapterSection title="References">
          {citations.map((citation, index) => (
            <Citation
              key={index}
              id={citation.id}
              title={citation.title}
              authors={citation.authors}
              journal={citation.journal}
              year={citation.year}
              link={citation.link}
            />
          ))}
        </ChapterSection>
      )}
    </ChapterLayout>
  );
};

// Specialized components for specific content types
const PythonCodeBlock = ({ children, title = "Python Code Example" }) => {
  return <CodeBlock language="python" title={title}>{children}</CodeBlock>;
};

const ROS2CodeBlock = ({ children, title = "ROS 2 Code Example" }) => {
  return <CodeBlock language="cpp" title={title}>{children}</CodeBlock>;
};

const BashCodeBlock = ({ children, title = "Bash Command" }) => {
  return <CodeBlock language="bash" title={title}>{children}</CodeBlock>;
};

export {
  CourseChapter,
  PythonCodeBlock,
  ROS2CodeBlock,
  BashCodeBlock,
  ChapterLayout,
  ChapterSection,
  RobotSpotlight,
  QuizSection,
  MermaidDiagram,
  CodeBlock,
  Citation,
  ChapterTOC
};