// @ts-check

/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  tutorialSidebar: [
    {
      type: 'category',
      label: '🤖 Introduction & Why Humanoids Matter',
      items: ['intro-and-why-humanoids/index'],
    },
    {
      type: 'category',
      label: '🔗 Module 1 – ROS 2: The Robotic Nervous System',
      items: ['module1-ros2-nervous-system/index'],
    },
    {
      type: 'category',
      label: '🔄 Module 2 – Gazebo & Digital Twin Simulation',
      items: ['module2-gazebo-digital-twin/index'],
    },
    {
      type: 'category',
      label: '🧠 Module 3 – NVIDIA Isaac: The AI Robot Brain',
      items: ['module3-nvidia-isaac-brain/index'],
    },
    {
      type: 'category',
      label: '👁️ Module 4 – Vision-Language-Action (VLA) Models',
      items: ['module4-vision-language-action/index'],
    },
    {
      type: 'category',
      label: '🏆 Capstone – Autonomous Simulated Humanoid',
      items: ['capstone-autonomous-humanoid/index'],
    },
    {
      type: 'category',
      label: '📚 Resources',
      items: ['accessibility-guidelines', 'citation-format', 'performance-monitoring', 'base-chapter-template'],
    },
  ],
};

export default sidebars;