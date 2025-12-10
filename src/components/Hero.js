import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './Hero.module.css';

function Hero() {
  const {siteConfig} = useDocusaurusContext();

  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <div className={styles.heroContent}>
          <h1 className="hero__title">{siteConfig.title}</h1>
          <p className="hero__subtitle">{siteConfig.tagline}</p>
          <p className="hero__tagline">
            Master Embodied AI: From Digital Brains to Humanoid Bodies
          </p>
          <p className="hero__subtitle">
            Open-source course with ROS 2, Gazebo, NVIDIA Isaac, and VLA models
          </p>
          <div className={styles.buttons}>
            <Link
              className="button button--secondary button--lg"
              to="/docs/intro-and-why-humanoids">
              Start with Module 1
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Hero;