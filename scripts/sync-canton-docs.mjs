import { mkdir, writeFile } from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const SOURCE_INDEX_URL = 'https://docs.canton.network/llms.txt';
const KB_DIR = path.join(ROOT, 'docs/education/canton-dev');
const CONTENT_DIR = path.join(ROOT, 'src/content/canton-docs');

const coreDocs = [
  {
    sourcePath: '/appdev/get-started/choose-your-path.md',
    slug: 'choose-your-path',
    category: 'getting-started',
    tags: ['onboarding', 'learning-path'],
    summary:
      'A starting point for choosing the right Canton developer path before diving into Daml, APIs, app rewards, or deployment topics.',
    zhSummary:
      '帮助开发者先判断自己该走哪条 Canton 学习路径：Daml 合约、Ledger/API 集成、应用奖励还是部署运维，避免一开始就迷失在完整文档树里。',
  },
  {
    sourcePath: '/appdev/modules/m1-development-stack.md',
    slug: 'development-stack',
    category: 'foundations',
    tags: ['stack', 'daml', 'sdk'],
    summary:
      'Introduces the Canton development stack, including Daml, participant nodes, APIs, package tooling, and application integration surfaces.',
    zhSummary:
      '概览 Canton 开发栈：Daml、Participant Node、Ledger API、包管理和应用集成边界，是搭建开发环境前最重要的地图。',
  },
  {
    sourcePath: '/appdev/modules/m1-mental-models.md',
    slug: 'mental-models',
    category: 'foundations',
    tags: ['mental-models', 'architecture'],
    summary:
      'Frames Canton with the core mental models developers need: parties, contracts, privacy, synchronization, and multi-party workflows.',
    zhSummary:
      '用开发者能理解的模型解释 Canton：Party、合约、隐私、同步层和多方工作流，适合作为后续技术细节的认知底座。',
  },
  {
    sourcePath: '/appdev/modules/m2-concept-translation.md',
    slug: 'concept-translation',
    category: 'migration',
    tags: ['ethereum', 'migration', 'concepts'],
    summary:
      'Maps familiar blockchain and application concepts into Canton and Daml terminology so teams can migrate their mental model safely.',
    zhSummary:
      '把以太坊或传统应用开发者熟悉的概念翻译到 Canton/Daml 语境中，帮助团队迁移认知，而不是生搬硬套旧链模型。',
  },
  {
    sourcePath: '/appdev/modules/m3-dev-environment.md',
    slug: 'dev-environment',
    category: 'daml',
    tags: ['setup', 'sdk', 'local-dev'],
    summary:
      'Covers local development environment setup and the tooling needed before writing, building, and testing Daml applications.',
    zhSummary:
      '说明本地开发环境和 SDK 工具链准备，是写 Daml、构建包和跑测试之前的操作入口。',
  },
  {
    sourcePath: '/appdev/modules/m3-language-fundamentals.md',
    slug: 'language-fundamentals',
    category: 'daml',
    tags: ['daml', 'language'],
    summary:
      'Explains the core Daml language concepts required to model agreements and reason about contract-led workflows.',
    zhSummary:
      '解释 Daml 语言基础，重点是如何用类型和合约表达多方协议，而不只是把它当作另一种智能合约语法。',
  },
  {
    sourcePath: '/appdev/modules/m3-contract-templates.md',
    slug: 'contract-templates',
    category: 'daml',
    tags: ['templates', 'contracts'],
    summary:
      'Describes contract templates, signatories, observers, and data fields as the building blocks of Daml applications.',
    zhSummary:
      '说明 Template、Signatory、Observer 和字段如何组成 Daml 合约，是理解 Canton 应用状态模型的核心页面。',
  },
  {
    sourcePath: '/appdev/modules/m3-choices.md',
    slug: 'choices',
    category: 'daml',
    tags: ['choices', 'authorization'],
    summary:
      'Explains choices as authorized contract actions and how they encode who may exercise workflow transitions.',
    zhSummary:
      '解释 Choice 如何表达“谁有权执行什么动作”，是理解 Daml 授权模型和业务流程迁移的关键。',
  },
  {
    sourcePath: '/appdev/modules/m3-testing.md',
    slug: 'testing-daml-contracts',
    category: 'daml',
    tags: ['testing', 'daml'],
    summary:
      'Introduces testing practices for Daml contracts so developers can verify authorization, visibility, and workflow behavior early.',
    zhSummary:
      '介绍 Daml 合约测试方式，帮助开发者尽早验证授权、可见性和业务流程行为，降低上线后调试成本。',
  },
  {
    sourcePath: '/appdev/modules/m4-app-architecture.md',
    slug: 'app-architecture',
    category: 'application',
    tags: ['architecture', 'backend', 'frontend'],
    summary:
      'Outlines how Canton applications are structured across smart contracts, backends, frontends, APIs, and network integration.',
    zhSummary:
      '梳理 Canton 应用的整体架构：合约、后端、前端、API 与网络集成如何分层协作。',
  },
  {
    sourcePath: '/appdev/modules/m4-backend-dev.md',
    slug: 'backend-development',
    category: 'application',
    tags: ['backend', 'ledger-api'],
    summary:
      'Focuses on backend services that submit commands, read ledger state, and coordinate application workflows around Canton.',
    zhSummary:
      '聚焦后端服务如何提交命令、读取账本状态，并围绕 Canton 协调应用工作流。',
  },
  {
    sourcePath: '/appdev/modules/m4-frontend-dev.md',
    slug: 'frontend-development',
    category: 'application',
    tags: ['frontend', 'user-experience'],
    summary:
      'Explains frontend responsibilities when presenting Canton application state and actions to end users.',
    zhSummary:
      '说明前端在 Canton 应用中的职责：如何展示合约状态、用户可执行动作和多方流程进度。',
  },
  {
    sourcePath: '/appdev/modules/m4-json-api-tutorial.md',
    slug: 'json-ledger-api',
    category: 'api',
    tags: ['json-api', 'ledger-api'],
    summary:
      'Guides developers through using the JSON Ledger API to interact with Canton applications from familiar web stacks.',
    zhSummary:
      '指导开发者通过 JSON Ledger API 从常见 Web 技术栈接入 Canton 应用，是前后端集成的实用入口。',
  },
  {
    sourcePath: '/appdev/modules/m4-query-with-pqs.md',
    slug: 'query-with-pqs',
    category: 'api',
    tags: ['pqs', 'query', 'ledger-api'],
    summary:
      'Covers querying contracts and transactions with PQS, useful for read models, reporting, and application state views.',
    zhSummary:
      '介绍用 PQS 查询合约和交易，适合构建 read model、报表和应用状态视图。',
  },
  {
    sourcePath: '/appdev/modules/m4-sdks-apis.md',
    slug: 'sdks-and-apis',
    category: 'api',
    tags: ['sdk', 'api'],
    summary:
      'Surveys Canton SDKs and APIs so teams can choose the right integration layer for their application architecture.',
    zhSummary:
      '概览 Canton SDK 与 API，帮助团队按应用架构选择合适的集成层。',
  },
  {
    sourcePath: '/appdev/deep-dives/privacy-model.md',
    slug: 'privacy-model',
    category: 'deep-dive',
    tags: ['privacy', 'visibility'],
    summary:
      'Explains the privacy model for app developers, including how Canton limits transaction visibility to authorized stakeholders.',
    zhSummary:
      '从应用开发者视角解释 Canton 隐私模型：交易细节如何只对被授权的相关方可见。',
  },
  {
    sourcePath: '/appdev/deep-dives/authorization.md',
    slug: 'authorization',
    category: 'deep-dive',
    tags: ['authorization', 'parties'],
    summary:
      'Details authorization concepts and how Daml and Canton ensure that only the right parties can approve or exercise actions.',
    zhSummary:
      '深入说明授权概念，以及 Daml/Canton 如何保证只有正确的 Party 能批准或执行特定动作。',
  },
  {
    sourcePath: '/appdev/deep-dives/token-standard.md',
    slug: 'token-standard',
    category: 'deep-dive',
    tags: ['token-standard', 'cip-0056'],
    summary:
      'Introduces the Canton token standard and the contract/interface patterns used for tokenized assets.',
    zhSummary:
      '介绍 Canton Token Standard 及其合约/接口模式，是理解 CIP-0056 和代币化资产实现的入口。',
  },
  {
    sourcePath: '/appdev/app-rewards.md',
    slug: 'app-rewards',
    category: 'economics',
    tags: ['app-rewards', 'traffic', 'canton-coin'],
    summary:
      'Summarizes app rewards and why application activity, traffic, and reward mechanics matter for Canton builders.',
    zhSummary:
      '概述应用奖励机制，以及应用活跃度、Traffic 与奖励规则为什么会影响 Canton 开发者的产品设计。',
  },
  {
    sourcePath: '/appdev/modules/m4-observability.md',
    slug: 'observability',
    category: 'operations',
    tags: ['observability', 'operations'],
    summary:
      'Introduces observability concerns for Canton applications, including what teams should monitor once apps move beyond local development.',
    zhSummary:
      '介绍 Canton 应用的可观测性关注点，帮助团队从本地开发过渡到可运行、可排障的服务。',
  },
  {
    sourcePath: '/appdev/modules/m5-localnet-development.md',
    slug: 'localnet-development',
    category: 'deployment',
    tags: ['localnet', 'deployment'],
    summary:
      'Covers LocalNet development as a stepping stone between local coding and deployment into shared Canton environments.',
    zhSummary:
      '说明 LocalNet 开发如何连接本地编码和共享网络部署，是上链前验证应用行为的重要阶段。',
  },
  {
    sourcePath: '/appdev/modules/m5-deployment-progression.md',
    slug: 'deployment-progression',
    category: 'deployment',
    tags: ['deployment', 'environments'],
    summary:
      'Explains how teams should progress deployments across environments and reduce risk before production use.',
    zhSummary:
      '解释团队如何逐步推进不同环境的部署，在生产使用前降低集成和运维风险。',
  },
  {
    sourcePath: '/appdev/modules/m6-overview.md',
    slug: 'smart-contract-upgrades',
    category: 'upgrades',
    tags: ['upgrades', 'scu'],
    summary:
      'Introduces smart contract upgrades and the key constraints Canton developers must plan for before changing deployed packages.',
    zhSummary:
      '介绍智能合约升级的整体思路，以及开发者在修改已部署包之前必须考虑的约束。',
  },
  {
    sourcePath: '/appdev/faq.md',
    slug: 'common-issues-faq',
    category: 'reference',
    tags: ['faq', 'troubleshooting'],
    summary:
      'Collects common application-development issues and troubleshooting pointers for developers working through the Canton stack.',
    zhSummary:
      '汇总应用开发中的常见问题和排障入口，适合在学习或集成卡住时快速定位方向。',
  },
];

function parseLlmsIndex(markdown) {
  const docs = new Map();
  const linkPattern = /^- \[(?<title>[^\]]+)\]\((?<url>https:\/\/docs\.canton\.network(?<path>[^)]+))\)$/gm;
  for (const match of markdown.matchAll(linkPattern)) {
    docs.set(match.groups.path, {
      title: match.groups.title,
      sourceUrl: match.groups.url,
      sourcePath: match.groups.path,
    });
  }
  return docs;
}

function escapeYaml(value) {
  return String(value).replaceAll('"', '\\"');
}

function markdownFor({ doc, locale }) {
  const isZh = locale === 'zh';
  const title = isZh ? `${doc.title}（中文学习笔记）` : doc.title;
  const summary = isZh ? doc.zhSummary : doc.summary;
  const sourceLabel = isZh ? '官方原文' : 'Official source';
  const verifyLabel = isZh ? '使用规则' : 'Usage note';
  const questions = isZh
    ? [
        '这页解决哪个开发者问题？',
        '它依赖哪些 Canton/Daml 核心概念？',
        '实现前还需要回到哪些官方页面核对细节？',
      ]
    : [
        'What developer problem does this page answer?',
        'Which Canton or Daml concepts does it depend on?',
        'Which upstream details should be verified before implementation?',
      ];

  return `---
title: "${escapeYaml(title)}"
slug: "${doc.slug}"
locale: "${locale}"
category: "${doc.category}"
source_url: "${doc.sourceUrl}"
source_title: "${escapeYaml(doc.title)}"
tags:
${doc.tags.map((tag) => `  - ${tag}`).join('\n')}
---

# ${title}

${summary}

## ${sourceLabel}

- ${doc.sourceUrl}

## ${verifyLabel}

${isZh
  ? '这是一份非官方学习笔记，只用于导航、摘要和检索。实现协议、合约或 API 集成前，请以官方页面为准。'
  : 'This is an unofficial learning note for navigation, summarization, and retrieval. Verify protocol, contract, and API implementation details against the official page before building.'}

## ${isZh ? '检索问题' : 'Retrieval Questions'}

${questions.map((question) => `- ${question}`).join('\n')}
`;
}

function chunkText(doc, locale) {
  const summary = locale === 'zh' ? doc.zhSummary : doc.summary;
  const note =
    locale === 'zh'
      ? '非官方中文学习笔记。回答时必须引用官方来源，并提醒用户核对上游文档。'
      : 'Unofficial English learning note. Answers must cite the official source and ask readers to verify upstream docs.';
  return `${doc.title}\n${summary}\n${note}`;
}

async function main() {
  const response = await fetch(SOURCE_INDEX_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${SOURCE_INDEX_URL}: ${response.status} ${response.statusText}`);
  }

  const llmsText = await response.text();
  const indexedDocs = parseLlmsIndex(llmsText);
  const generatedAt = new Date().toISOString();
  const selected = coreDocs.map((entry) => {
    const upstream = indexedDocs.get(entry.sourcePath);
    if (!upstream) {
      throw new Error(`Core doc not found in llms.txt: ${entry.sourcePath}`);
    }
    return {
      ...entry,
      title: upstream.title,
      sourceUrl: upstream.sourceUrl,
    };
  });

  await mkdir(path.join(KB_DIR, 'en'), { recursive: true });
  await mkdir(path.join(KB_DIR, 'zh'), { recursive: true });
  await mkdir(CONTENT_DIR, { recursive: true });

  const ragChunks = [];
  const contentItems = [];

  for (const doc of selected) {
    for (const locale of ['en', 'zh']) {
      const localPath = `docs/education/canton-dev/${locale}/${doc.slug}.md`;
      await writeFile(path.join(ROOT, localPath), markdownFor({ doc, locale }), 'utf8');

      ragChunks.push({
        id: `canton-dev:${locale}:${doc.slug}:summary`,
        locale,
        title: locale === 'zh' ? `${doc.title}（中文学习笔记）` : doc.title,
        slug: doc.slug,
        category: doc.category,
        tags: doc.tags,
        source_url: doc.sourceUrl,
        local_path: localPath,
        text: chunkText(doc, locale),
      });

      contentItems.push({
        slug: doc.slug,
        locale,
        title: locale === 'zh' ? `${doc.title}（中文学习笔记）` : doc.title,
        sourceTitle: doc.title,
        summary: locale === 'zh' ? doc.zhSummary : doc.summary,
        category: doc.category,
        tags: doc.tags,
        sourceUrl: doc.sourceUrl,
        localPath,
      });
    }
  }

  const manifest = {
    name: 'Canton Developer Knowledge Base',
    unofficial: true,
    generatedAt,
    sourceIndexUrl: SOURCE_INDEX_URL,
    upstreamDocumentation: 'https://docs.canton.network/',
    attribution:
      'Summaries and organization are maintained by CC Privacy Club. Official Canton Network documentation remains the canonical source.',
    licenseNote:
      'The upstream documentation site states Documentation License (CC-BY-4.0). Preserve source URLs and attribution when reusing notes.',
    coreSetSize: selected.length,
    documents: selected.map((doc) => ({
      slug: doc.slug,
      title: doc.title,
      category: doc.category,
      tags: doc.tags,
      sourceUrl: doc.sourceUrl,
      sourcePath: doc.sourcePath,
      includedInCoreSet: true,
      local: {
        en: `docs/education/canton-dev/en/${doc.slug}.md`,
        zh: `docs/education/canton-dev/zh/${doc.slug}.md`,
      },
    })),
  };

  await writeFile(path.join(KB_DIR, 'manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
  await writeFile(
    path.join(KB_DIR, 'rag-index.jsonl'),
    `${ragChunks.map((chunk) => JSON.stringify(chunk)).join('\n')}\n`,
    'utf8',
  );
  await writeFile(
    path.join(CONTENT_DIR, 'index.json'),
    `${JSON.stringify({ generatedAt, sourceIndexUrl: SOURCE_INDEX_URL, items: contentItems }, null, 2)}\n`,
    'utf8',
  );

  console.log(`Generated ${selected.length} Canton docs in EN/ZH and ${ragChunks.length} RAG chunks.`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
