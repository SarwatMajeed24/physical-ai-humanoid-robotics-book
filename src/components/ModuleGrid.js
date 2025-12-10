import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './ModuleGrid.module.css';

const ModuleCards = [
  {
    title: 'ROS 2: The Nervous System',
    icon: '/img/robot-arm-icon.jpg',
    description: 'Learn the Robot Operating System fundamentals that serve as the backbone for humanoid robotics communication and control.',
    link: '/docs/module1-ros2-nervous-system',
    buttonText: 'Explore',
  },
  {
    title: 'Gazebo: Digital Twin Simulation',
    icon: '/img/globe-icon.jpg',
    description: 'Master simulation environments for testing humanoid robot behaviors in safe, virtual worlds before real-world deployment.',
    link: '/docs/module2-gazebo-digital-twin',
    buttonText: 'Explore',
  },
  {
    title: 'NVIDIA Isaac: AI Robot Brain',
    icon: '/img/brain-icon.jpg',
    description: 'Explore NVIDIA Isaac platform for developing intelligent control systems that power autonomous humanoid behaviors.',
    link: '/docs/module3-nvidia-isaac-brain',
    buttonText: 'Explore',
  },
  {
    title: 'Vision-Language-Action (VLA)',
    icon: '/img/eye-icon.jpg',
    description: 'Understand how modern AI models integrate perception, reasoning, and action for embodied intelligence in humanoid robots.',
    link: '/docs/module4-vision-language-action',
    buttonText: 'Explore',
  },
  {
    title: 'Hardware Integration',
    icon: '/img/gear-icon.jpg',
    description: 'Connect software systems to real hardware components, sensors, and actuators for physical humanoid robot control.',
    link: '/docs/capstone-autonomous-humanoid',
    buttonText: 'Explore',
  },
  {
    title: 'Capstone: Autonomous Humanoid',
    icon: '/img/trophy-icon.jpg',
    description: 'Apply all learned concepts to build an autonomous humanoid robot capable of complex tasks and navigation.',
    link: '/docs/capstone-autonomous-humanoid',
    buttonText: 'Explore',
  },
];

function ModuleGrid() {
  return (
    <section className={styles.moduleGrid}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Course Modules</h2>
        <div className={styles.grid}>
          {ModuleCards.map((card, index) => (
            <div key={index} className={styles.card}>
              <div className={styles.cardContent}>
                <img src={card.icon} alt={card.title} className={styles.cardIcon} />
                <h3 className={styles.cardTitle}>{card.title}</h3>
                <p className={styles.cardDescription}>{card.description}</p>
                <Link className={styles.cardButton} to={card.link}>
                  {card.buttonText}
                </Link>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default ModuleGrid;