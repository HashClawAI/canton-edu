/**
 * Build-time GEO files for ccprivacy.club: llms.txt (+ robots.txt refresh).
 * Run before `astro build` (see package.json).
 */

import { readFileSync, writeFileSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, '..');
const publicDir = resolve(root, 'public');

const SITE_URL = (process.env.PUBLIC_SITE_URL || 'https://ccprivacy.club').replace(/\/$/, '');

const MAIN_PAGES = [
  { path: '/', label: '首页（中文默认）', desc: 'Canton Network 社区教育站入口' },
  { path: '/en/', label: 'Home (English)', desc: 'Canton Network education hub' },
  { path: '/learn', label: 'Learning path (EN)', desc: 'Structured Canton learning steps' },
  { path: '/zh/learn', label: '学习路径（中文）', desc: 'Canton 结构化学习路径' },
  { path: '/docs/canton', label: 'Developer docs (EN)', desc: 'Bilingual Canton docs mirror index' },
  { path: '/zh/docs/canton', label: '开发者文档（中文）', desc: 'Canton 官方文档中文镜像索引' },
  { path: '/ecosystem', label: 'Ecosystem (EN)', desc: 'Featured Canton apps and projects' },
  { path: '/zh/ecosystem', label: '生态（中文）', desc: 'Canton 生态项目精选' },
  { path: '/cips', label: 'CIPs (EN)', desc: 'Canton Improvement Proposals overview' },
  { path: '/zh/cips', label: 'CIPs（中文）', desc: 'Canton 改进提案概览' },
  { path: '/news', label: 'News (EN)', desc: 'Canton Network news and updates' },
  { path: '/zh/news', label: '动态（中文）', desc: 'Canton 新闻与动态' },
  { path: '/research', label: 'Research (EN)', desc: 'Reports and research links' },
  { path: '/zh/research', label: '研究报告（中文）', desc: 'Canton 研究报告与链接' },
  { path: '/community', label: 'Community (EN)', desc: 'Forums, Discord, governance' },
  { path: '/zh/community', label: '社区（中文）', desc: '论坛、Discord 与治理' },
  { path: '/resources', label: 'Resources (EN)', desc: 'Whitepapers, explorers, exchanges' },
  { path: '/zh/resources', label: '资源（中文）', desc: '白皮书、浏览器、交易所' },
  { path: '/videos', label: 'Videos (EN)', desc: 'Curated Canton video list' },
  { path: '/zh/videos', label: '视频（中文）', desc: 'Canton 视频精选' },
];

const CURATED_DOC_SLUGS = [
  'appdev-get-started-choose-your-path',
  'appdev-deep-dives-tokenomics',
  'appdev-modules-m1-mental-models',
  'appdev-modules-m1-understanding-canton',
  'appdev-troubleshooting-guide-common-questions',
  'appdev-app-rewards',
  'appdev-deep-dives-token-standard',
];

function loadDocIndex() {
  const raw = readFileSync(resolve(root, 'src/content/canton-docs/index.json'), 'utf8');
  return JSON.parse(raw).items ?? [];
}

function url(path) {
  return `${SITE_URL}${path}`;
}

function buildLlmsTxt() {
  const docs = loadDocIndex();
  const bySlug = new Map(docs.filter((d) => d.locale === 'en').map((d) => [d.slug, d]));

  const lines = [
    '# CC Privacy Club · Canton Network Education',
    '',
    '> 非官方 Canton Network 中英文教育站 · https://ccprivacy.club · 维护：HashClaw 社区',
    '',
    '## 站点',
    `- 首页: ${url('/')}`,
    `- English: ${url('/en/')}`,
    `- Sitemap: ${url('/sitemap-index.xml')}`,
    `- Robots: ${url('/robots.txt')}`,
    '',
    '## 主要栏目',
    '',
  ];

  for (const page of MAIN_PAGES) {
    lines.push(`- [${page.label}](${url(page.path)}) — ${page.desc}`);
  }

  lines.push('', '## 开发者文档精选（英文路径，站内提供中文版）', '');
  for (const slug of CURATED_DOC_SLUGS) {
    const doc = bySlug.get(slug);
    if (!doc) continue;
    const title = doc.title || slug;
    const summary = String(doc.summary || '')
      .replace(/\s+/g, ' ')
      .slice(0, 100);
    lines.push(`- [${title}](${url(`/docs/canton/${slug}`)}) — ${summary}…`);
    lines.push(`  - 中文: ${url(`/zh/docs/canton/${slug}`)}`);
  }

  lines.push(
    '',
    '## 官方参考',
    '- Canton Network: https://www.canton.network/',
    '- Official docs: https://docs.canton.network/',
    '- Official llms.txt: https://docs.canton.network/llms.txt',
    '',
    '## 维护',
    '- GitHub: https://github.com/HashClawAI/canton-edu',
    '',
    `Generated: ${new Date().toISOString()}`,
  );

  return `${lines.join('\n')}\n`;
}

function buildRobotsTxt() {
  return `User-agent: *
Allow: /

Sitemap: ${url('/sitemap-index.xml')}
LLMs: ${url('/llms.txt')}
`;
}

const llms = buildLlmsTxt();
writeFileSync(resolve(publicDir, 'llms.txt'), llms);
writeFileSync(resolve(publicDir, 'robots.txt'), buildRobotsTxt());

console.log(`GEO files written for ${SITE_URL}`);
console.log(`  public/llms.txt (${llms.length} bytes)`);
console.log(`  public/robots.txt`);
