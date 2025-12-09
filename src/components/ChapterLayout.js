import React from 'react';
import clsx from 'clsx';
import styles from './ChapterLayout.module.css';

// Define the props for the ChapterLayout component
const ChapterHeader = ({title, description, learningObjectives}) => {
  return (
    <header className={styles.chapterHeader}>
      <div className="container">
        <h1 className={styles.chapterTitle}>{title}</h1>
        {description && <p className={styles.chapterDescription}>{description}</p>}
        {learningObjectives && learningObjectives.length > 0 && (
          <div className={styles.learningObjectives}>
            <h3>Learning Objectives</h3>
            <ul>
              {learningObjectives.map((objective, index) => (
                <li key={index}>{objective}</li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </header>
  );
};

const ChapterSection = ({title, children, className}) => {
  return (
    <section className={clsx(styles.chapterSection, className)}>
      <div className="container">
        {title && <h2 className={styles.sectionTitle}>{title}</h2>}
        <div className={styles.sectionContent}>
          {children}
        </div>
      </div>
    </section>
  );
};

const RobotSpotlight = ({robotName, image, specs, description}) => {
  return (
    <div className={styles.robotSpotlight}>
      <h4>{robotName}</h4>
      {image && <img src={image} alt={`Photo of ${robotName}`} className={styles.robotImage} />}
      {description && <p>{description}</p>}
      {specs && Object.keys(specs).length > 0 && (
        <table className={styles.robotSpecsTable}>
          <tbody>
            {Object.entries(specs).map(([key, value]) => (
              <tr key={key}>
                <td><strong>{key}</strong></td>
                <td>{value}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
};

const QuizSection = ({question, options, correctAnswer}) => {
  const [selectedOption, setSelectedOption] = React.useState(null);
  const [submitted, setSubmitted] = React.useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSubmitted(true);
  };

  const isCorrect = selectedOption === correctAnswer;

  return (
    <div className={styles.quizSection}>
      <h4>Knowledge Check</h4>
      <form onSubmit={handleSubmit}>
        <p><strong>{question}</strong></p>
        {options.map((option, index) => (
          <label key={index} className={styles.quizOption}>
            <input
              type="checkbox"
              checked={selectedOption === index}
              onChange={() => setSelectedOption(index)}
              disabled={submitted}
            />
            <span>{option}</span>
          </label>
        ))}
        <button
          type="submit"
          className={styles.quizSubmitBtn}
          disabled={selectedOption === null || submitted}
        >
          {submitted ? (isCorrect ? '✓ Correct!' : '✗ Try Again') : 'Submit'}
        </button>
        {submitted && !isCorrect && (
          <p className={styles.quizFeedback}>Try again! Consider the concepts we just covered.</p>
        )}
      </form>
    </div>
  );
};

const ChapterLayout = ({title, description, learningObjectives, children}) => {
  return (
    <div className={styles.chapterLayout}>
      <ChapterHeader
        title={title}
        description={description}
        learningObjectives={learningObjectives}
      />
      <main className={styles.chapterMain}>
        {children}
      </main>
    </div>
  );
};

export {ChapterLayout, ChapterSection, RobotSpotlight, QuizSection};