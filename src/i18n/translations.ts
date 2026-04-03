export type Locale = 'en' | 'zh';

export const translations = {
  en: {
    siteName: 'Canton Learn',
    nav: {
      home: 'Home',
      learn: 'Learn',
      resources: 'Resources',
    },
    home: {
      title: 'Learn Canton Network',
      subtitle:
        'Independent educational notes about Canton Network, DAML, and the ecosystem. Always verify against official documentation.',
      ctaLearn: 'Start learning',
      ctaResources: 'Official resources',
      cardWhatTitle: 'What is Canton?',
      cardWhatBody:
        'Canton is a privacy-enabled network designed for institutional finance and tokenized assets, built with DAML smart contracts.',
      cardWhoTitle: 'Who is this for?',
      cardWhoBody:
        'Developers, students, and teams who want a structured entry point before reading primary sources.',
      disclaimer:
        'This site is not affiliated with Canton Foundation, Digital Asset, or network participants. Content is for education only, not financial or legal advice.',
    },
    learn: {
      title: 'Learning path',
      intro:
        'Use the links below as a reading order. Replace or extend this page as your curriculum grows.',
      step1Title: 'Concepts',
      step1Body: 'Network model, parties, privacy, and Canton Coin (CC) at a high level.',
      step2Title: 'DAML',
      step2Body: 'Templates, choices, signatories, and the Ledger API.',
      step3Title: 'Token standards',
      step3Body: 'Holdings, instruments, and ecosystem APIs where documented publicly.',
    },
    resources: {
      title: 'Official resources',
      intro: 'Primary sources you should bookmark.',
      cantonSite: 'Canton Network',
      damlDocs: 'DAML / Daml documentation',
      foundation: 'Canton Foundation',
    },
    lang: {
      switch: '中文',
      label: 'Language',
    },
  },
  zh: {
    siteName: 'Canton 学习站',
    nav: {
      home: '首页',
      learn: '学习路径',
      resources: '官方资源',
    },
    home: {
      title: 'Canton Network 学习',
      subtitle:
        '关于 Canton Network、DAML 与生态的独立学习笔记。请务必以官方文档为准进行核对。',
      ctaLearn: '开始学习',
      ctaResources: '官方资源',
      cardWhatTitle: 'Canton 是什么？',
      cardWhatBody:
        'Canton 是面向机构金融与资产代币化的隐私增强型网络，智能合约基于 DAML。',
      cardWhoTitle: '适合谁？',
      cardWhoBody: '希望在阅读一手资料前，先建立结构认知的开发者、学生与团队。',
      disclaimer:
        '本站与 Canton Foundation、Digital Asset 及网络参与方无隶属关系。内容仅供学习，不构成投资或法律建议。',
    },
    learn: {
      title: '学习路径',
      intro: '以下可作为阅读顺序，你可随课程扩展替换或增删本页内容。',
      step1Title: '概念',
      step1Body: '网络模型、参与方、隐私与 Canton Coin（CC）等入门概念。',
      step2Title: 'DAML',
      step2Body: '模板（Template）、选择（Choice）、签字方与 Ledger API。',
      step3Title: '代币与标准',
      step3Body: 'Holding、Instrument 及公开文档中的生态 API。',
    },
    resources: {
      title: '官方资源',
      intro: '建议收藏的一手资料。',
      cantonSite: 'Canton Network 官网',
      damlDocs: 'DAML / Daml 文档',
      foundation: 'Canton Foundation',
    },
    lang: {
      switch: 'English',
      label: '语言',
    },
  },
} as const;

export function t(locale: Locale) {
  return translations[locale];
}
