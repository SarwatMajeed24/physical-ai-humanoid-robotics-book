import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './ModuleGrid.module.css';

const ModuleCards = [
  {
    title: 'Module 1 – ROS 2: The Nervous System',
    icon: '/static/img/modules/module1.png',
    description: 'Learn the Robot Operating System fundamentals that serve as the backbone for humanoid robotics communication and control.',
    link: '/docs/module1-ros2-nervous-system',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 2 – Gazebo: Digital Twin Simulation',
    icon: '/static/img/modules/module2.png',
    description: 'Master simulation environments for testing humanoid robot behaviors in safe, virtual worlds before real-world deployment.',
    link: '/docs/module2-gazebo-digital-twin',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 3 – NVIDIA Isaac: AI Robot Brain',
    icon: '/static/img/modules/module3.png',
    description: 'Explore NVIDIA Isaac platform for developing intelligent control systems that power autonomous humanoid behaviors.',
    link: '/docs/module3-nvidia-isaac-brain',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 4 – Vision-Language-Action (VLA)',
    icon: '/static/img/modules/module4.png',
    description: 'Understand how modern AI models integrate perception, reasoning, and action for embodied intelligence in humanoid robots.',
    link: '/docs/module4-vision-language-action',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 5 – Humanoid Robot',
    icon: '/static/img/modules/module5.png',
    description: 'Real robot spotlight and hardware integration for physical humanoid robot control and deployment.',
    link: '/docs/capstone-autonomous-humanoid',
    buttonText: 'Explore →',
  },
  {
    title: 'Module 6 – Capstone Project',
    icon: '/static/img/modules/module6.png',
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
                <div
                  style={{
                    fontSize: '80px',
                    textAlign: 'center',
                    margin: '0 auto 16px',
                    display: 'block',
                    lineHeight: '1'
                  }}
                >
                  {index === 0 && '🧠'}  {/* Module 1 → 🧠 */}
                  {index === 1 && '🌐'}  {/* Module 2 → 🌐 */}
                  {index === 2 && '⚡'}  {/* Module 3 → ⚡ */}
                  {index === 3 && '👁️'}  {/* Module 4 → 👁️ */}
                  {index === 4 && '🤖'}  {/* Module 5 → 🤖 */}
                  {index === 5 && '🚀'}  {/* Module 6 → 🚀 */}
                </div>
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