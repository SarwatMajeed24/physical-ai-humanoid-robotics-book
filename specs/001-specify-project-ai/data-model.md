# Data Model: Physical AI & Humanoid Robotics Course Book

## Entities

### Course Module
- **Name**: String (required) - Module name (e.g., "ROS 2 Nervous System")
- **Description**: String (required) - Brief description of the module
- **Order**: Integer (required) - Sequential order (1-6) for navigation
- **LearningObjectives**: Array of String (required) - List of learning objectives
- **Content**: String (required) - Main content in MDX format
- **Diagrams**: Array of Diagram objects (optional) - Mermaid diagrams
- **CodeExamples**: Array of CodeExample objects (optional) - Python/ROS2 snippets
- **RealRobotSpotlight**: RealRobotSpotlight object (optional) - Real robot information
- **Quiz**: Quiz object (optional) - Chapter quiz with questions

### Diagram
- **Title**: String (required) - Diagram title
- **Description**: String (required) - Diagram description
- **MermaidCode**: String (required) - Mermaid syntax code
- **AltText**: String (required) - Accessibility text for the diagram

### CodeExample
- **Title**: String (required) - Code example title
- **Description**: String (required) - Description of what the code does
- **Code**: String (required) - The actual code (5-15 lines)
- **Language**: String (required) - Code language (python, bash, etc.)
- **FileName**: String (optional) - Suggested file name

### RealRobotSpotlight
- **Name**: String (required) - Robot name (e.g., "Atlas", "Tesla Bot")
- **Image**: String (required) - Path to image in static/img
- **Description**: String (required) - Brief description of the robot
- **Specifications**: Array of String (required) - Key specs (3 bullet points)
- **Link**: String (optional) - URL to more information

### Quiz
- **Title**: String (required) - Quiz title
- **Questions**: Array of Question objects (required) - List of quiz questions
- **Type**: String (required) - Quiz type ("checkbox", "multiple-choice")

### Question
- **QuestionText**: String (required) - The question text
- **Options**: Array of Option objects (required for multiple-choice)
- **Answer**: String (required) - The correct answer
- **Explanation**: String (optional) - Explanation of the answer

### Option
- **Text**: String (required) - Option text
- **IsCorrect**: Boolean (required) - Whether this option is correct

## Relationships

- CourseModule contains many Diagrams
- CourseModule contains many CodeExamples
- CourseModule has one RealRobotSpotlight
- CourseModule has one Quiz
- Quiz contains many Questions
- Question contains many Options (for multiple-choice)

## Validation Rules

1. **CourseModule**
   - Name must be 3-100 characters
   - Description must be 10-500 characters
   - Order must be between 1-6
   - LearningObjectives must have 1-10 items
   - Content must be valid MDX format

2. **Diagram**
   - Title must be 3-50 characters
   - Description must be 10-200 characters
   - MermaidCode must be valid Mermaid syntax
   - AltText must be 5-100 characters

3. **CodeExample**
   - Title must be 3-50 characters
   - Description must be 10-200 characters
   - Code must be 1-50 lines (5-15 lines preferred)
   - Language must be a valid programming language

4. **RealRobotSpotlight**
   - Name must be 2-50 characters
   - Image path must exist in static directory
   - Specifications must have exactly 3 items
   - Link must be a valid URL if provided

5. **Quiz**
   - Title must be 3-100 characters
   - Questions must have 1-20 items
   - Type must be either "checkbox" or "multiple-choice"

6. **Question**
   - QuestionText must be 5-500 characters
   - For multiple-choice: Options must have 2-6 items
   - Answer must match one of the options (for multiple-choice)

## State Transitions

- CourseModule: Draft → Review → Published
- Diagram: Created → Validated → Included
- CodeExample: Created → Tested → Included
- Quiz: Created → Validated → Active