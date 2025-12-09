# Physical AI & Humanoid Robotics

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sweetoo/physical-ai-humanoid-robotics-book)

A comprehensive open-source course book on Physical AI and Humanoid Robotics, built with Docusaurus v3 and deployed on GitHub Pages.

## 🚀 Quick Start

### One-Click Preview (Free)
Click the button below to launch an instant development environment in GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/sweetoo/physical-ai-humanoid-robotics-book)

Once the codespace is ready, run these commands to get started:

```bash
npm install
npm start
```

### Local Development

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sweetoo/physical-ai-humanoid-robotics-book.git
   cd physical-ai-humanoid-robotics-book
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

## 📚 Course Structure

This course book is organized into 6 comprehensive chapters:

1. **Introduction & Why Humanoids Matter** - Foundations of Physical AI
2. **Module 1 – ROS 2: The Robotic Nervous System** - Core robotics framework
3. **Module 2 – Gazebo & Digital Twin Simulation** - Physics simulation and modeling
4. **Module 3 – NVIDIA Isaac: The AI Robot Brain** - AI and perception systems
5. **Module 4 – Vision-Language-Action (VLA) Models** - Advanced multimodal AI
6. **Capstone – Autonomous Simulated Humanoid** - Complete project integration

## 🤝 Contribution Guide

We welcome contributions to enhance this course book! Here's how you can contribute:

### Adding New Chapters
1. Create a new directory in the `docs/` folder following the naming convention:
   - `docs/07-new-topic-name/` (use sequential numbering)
2. Add an `index.mdx` file with proper frontmatter:
   ```md
   ---
   title: Your Chapter Title
   sidebar_position: 1
   ---

   # Your Chapter Title

   Content here...
   ```
3. Update `sidebars.js` to include your new chapter in the navigation

### Adding Content to Existing Chapters
1. Navigate to the appropriate chapter directory
2. Edit the `index.mdx` file or create new sub-sections
3. Follow the existing format with:
   - Learning objectives
   - Core concepts and theory
   - 2-4 Mermaid diagrams
   - 5–15 line runnable Python/ROS 2 code snippets (copy-paste ready)
   - Real Robot Spotlight section with photos/videos and specs
   - Markdown checkbox quiz

### Code of Conduct
- All content must be technically accurate and factually correct
- Include verifiable sources and citations (IEEE style)
- Ensure content is beginner-friendly but advances to complex topics
- Add meaningful alt text for diagrams and images (see accessibility guidelines)
- Maintain mobile-friendly and accessible content
- Follow WCAG 2.1 AA compliance standards

### Accessibility Guidelines
For detailed information on accessibility requirements, including alt text standards and WCAG compliance, see our [Accessibility Guidelines](./docs/accessibility-guidelines.mdx).

### Pull Request Process
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-chapter`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing new chapter'`)
5. Push to the branch (`git push origin feature/amazing-chapter`)
6. Open a Pull Request

## 🛠️ Tech Stack

- **Framework**: [Docusaurus v3](https://docusaurus.io/) with classic preset
- **Language**: JavaScript/TypeScript, Python for ROS 2 examples
- **Format**: MDX for interactive documentation
- **Deployment**: GitHub Pages via GitHub Actions
- **Styling**: Tailwind CSS with custom components

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Content (text, diagrams, images) is licensed under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

## 🏗️ Project Structure

```
physical-ai-humanoid-robotics-book/
├── docs/                     # Course content (MDX files)
│   ├── 01-intro-and-why-humanoids/
│   ├── 02-module1-ros2-nervous-system/
│   ├── 03-module2-gazebo-digital-twin/
│   ├── 04-module3-nvidia-isaac-brain/
│   ├── 05-module4-vision-language-action/
│   └── 06-capstone-autonomous-humanoid/
├── src/                      # Custom React components
├── static/                   # Static assets (images, etc.)
├── .github/workflows/        # GitHub Actions CI/CD
├── docusaurus.config.js      # Site configuration
├── sidebars.js               # Navigation structure
├── package.json              # Dependencies and scripts
└── README.md                 # This file
```

## 🚀 Building for Production

To build the website for production:

```bash
npm run build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

## 🧪 Running Tests

Currently, manual testing is used for documentation rendering and code snippet validation. Performance testing is done with Lighthouse.

---

Made with ❤️ using [Docusaurus](https://docusaurus.io/).