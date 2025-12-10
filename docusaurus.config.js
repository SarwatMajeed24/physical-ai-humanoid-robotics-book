// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to configure your website.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A Comprehensive Open-Source Course Book on Embodied AI and Humanoid Systems',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://sweetoo.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub Pages user sites, it is often '/<username>.github.io/<repo-name>/'
  baseUrl: '/physical-ai-humanoid-robotics-book/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'sweetoo', // Usually your GitHub org/user name.
  projectName: 'physical-ai-humanoid-robotics-book', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/sweetoo/physical-ai-humanoid-robotics-book/tree/main/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
        },
        blog: false, // Disable blog for now
        theme: {
          customCss: './src/css/custom.css',
        },
        gtag: {
          trackingID: 'G-XXXXXXXXXX',
          anonymizeIP: true,
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/docusaurus-social-card.jpg',
      // Accessibility settings
      metadata: [
        {
          name: 'keywords',
          content: 'physical ai, humanoid robotics, ros2, gazebo, nvidia isaac, vision language action, vla, robotics education, embodied ai'
        },
        {
          name: 'theme-color',
          content: '#0A2540'
        }
      ],
      navbar: {
        title: 'Physical AI & Humanoid Robotics',
        logo: {
          alt: 'Physical AI & Humanoid Robotics Logo',
          src: 'img/logo.svg',
        },
        style: 'dark',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Course Book',
          },
          {
            type: 'dropdown',
            position: 'left',
            label: 'Modules',
            items: [
              {
                label: 'Introduction & Why Humanoids',
                to: '/docs/intro-and-why-humanoids',
              },
              {
                label: 'ROS 2: The Nervous System',
                to: '/docs/module1-ros2-nervous-system',
              },
              {
                label: 'Gazebo: Digital Twin Simulation',
                to: '/docs/module2-gazebo-digital-twin',
              },
              {
                label: 'NVIDIA Isaac: AI Robot Brain',
                to: '/docs/module3-nvidia-isaac-brain',
              },
              {
                label: 'Vision-Language-Action Models',
                to: '/docs/module4-vision-language-action',
              },
              {
                label: 'Capstone: Autonomous Humanoid',
                to: '/docs/capstone-autonomous-humanoid',
              },
            ],
          },
          {
            href: 'https://github.com/SarwatMajeed24/physical-ai-humanoid-robotics-book',
            className: 'header-github-link',
            'aria-label': 'GitHub repository',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Course Modules',
            items: [
              {
                label: 'Introduction',
                to: '/docs/intro-and-why-humanoids',
              },
              {
                label: 'ROS 2 Nervous System',
                to: '/docs/module1-ros2-nervous-system',
              },
              {
                label: 'Gazebo Digital Twin',
                to: '/docs/module2-gazebo-digital-twin',
              },
              {
                label: 'NVIDIA Isaac Brain',
                to: '/docs/module3-nvidia-isaac-brain',
              },
            ],
          },
          {
            title: 'Resources',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/sweetoo/physical-ai-humanoid-robotics-book',
              },
              {
                label: 'Docusaurus',
                href: 'https://docusaurus.io',
              },
              {
                label: 'ROS.org',
                href: 'https://ros.org',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'NVIDIA Isaac',
                href: 'https://nvidia.com/isaac',
              },
              {
                label: 'Gazebo Simulation',
                href: 'https://gazebosim.org',
              },
              {
                label: 'Humanoid Robotics',
                href: 'https://www.ieee-ras.org',
              },
            ],
          },
        ],
        copyright: `Created by <a href="https://github.com/SarwatMajeed24" style="color: #a0aec0;">Sarwat Majeed</a> | This work is licensed under a <a href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>. Built for Hackathons. Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics Course Book. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
      // Enable dark mode
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      // Enable search (using Algolia DocSearch)
      algolia: {
        // The application ID provided by Algolia
        appId: 'YOUR_APP_ID',
        // Public API key: it is safe to commit it
        apiKey: 'YOUR_SEARCH_API_KEY',
        indexName: 'physical-ai-humanoid-robotics-book',
        contextualSearch: true,
        searchPagePath: 'search',
      },
    }),
};

export default config;