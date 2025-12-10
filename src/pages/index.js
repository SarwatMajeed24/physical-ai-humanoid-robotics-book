import React from 'react';
import Layout from '@theme/Layout';
import Hero from '@site/src/components/Hero';
import ModuleGrid from '@site/src/components/ModuleGrid';
import Link from '@docusaurus/Link';

export default function Home() {
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics`}
      description="A Comprehensive Open-Source Course Book on Embodied AI and Humanoid Systems">
      <Hero />
      <div style={{ textAlign: 'center', padding: '1rem 0', marginTop: '-2rem', marginBottom: '2rem' }}>
        <span style={{ fontSize: '1.1rem', color: '#4a5568', fontFamily: 'inherit' }}>
          Created by Sarwat Majeed
        </span>
        <Link
          to="https://github.com/SarwatMajeed24"
          style={{
            marginLeft: '0.5rem',
            fontSize: '1.1rem',
            color: '#4a5568',
            textDecoration: 'none'
          }}
        >
          @SarwatMajeed24
        </Link>
      </div>
      <ModuleGrid />
    </Layout>
  );
}