import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './ModuleGrid.module.css';

const ModuleCards = [
  {
    title: 'Module 1 – ROS 2: The Nervous System',
    icon: 'https://ros.org/img/ros_logo_black.png',
    description: 'Learn the Robot Operating System fundamentals that serve as the backbone for humanoid robotics communication and control.',
    link: '/docs/module1-ros2-nervous-system',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 2 – Gazebo: Digital Twin Simulation',
    icon: 'https://gazebosim.org/assets/images/gazebo_logo.svg',
    description: 'Master simulation environments for testing humanoid robot behaviors in safe, virtual worlds before real-world deployment.',
    link: '/docs/module2-gazebo-digital-twin',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 3 – NVIDIA Isaac: AI Robot Brain',
    icon: 'https://developer.nvidia.com/sites/default/files/akamai/embedded/isaac-sim/IsaacSim_Logo.png',
    description: 'Explore NVIDIA Isaac platform for developing intelligent control systems that power autonomous humanoid behaviors.',
    link: '/docs/module3-nvidia-isaac-brain',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 4 – Vision-Language-Action (VLA)',
    icon: 'https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/hf-logo-with-title.png',
    description: 'Understand how modern AI models integrate perception, reasoning, and action for embodied intelligence in humanoid robots.',
    link: '/docs/module4-vision-language-action',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 5 – Humanoid Robot',
    icon: 'https://upload.wikimedia.org/wikipedia/commons/7/7e/Atlas_robot_%281%29.jpg',
    description: 'Real robot spotlight and hardware integration for physical humanoid robot control and deployment.',
    link: '/docs/capstone-autonomous-humanoid',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 6 – Capstone Project',
    icon: 'https://img.icons8.com/color/96/rocket.png',
    description: 'Apply all learned concepts to build an autonomous humanoid robot capable of complex tasks and navigation.',
    link: '/docs/capstone-autonomous-humanoid',
    buttonText: 'Explore →',
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