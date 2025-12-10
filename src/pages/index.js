import React from 'react';
import Layout from '@theme/Layout';
import Hero from '@site/src/components/Hero';
import ModuleGrid from '@site/src/components/ModuleGrid';

export default function Home() {
  return (
    <Layout
      title={`Physical AI & Humanoid Robotics`}
      description="A Comprehensive Open-Source Course Book on Embodied AI and Humanoid Systems">
      <Hero />
      <ModuleGrid />
    </Layout>
  );
}