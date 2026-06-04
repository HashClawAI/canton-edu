#!/usr/bin/env node
/**
 * Audit internal links in Canton doc markdown for likely broken targets on ccprivacy.club.
 */
import { readFile, readdir } from 'node:fs/promises';
import path from 'node:path';
import { legacyPathToSlug, buildValidSlugSet } from './lib/canton-link-rewrite.mjs';
import { pathToSlug } from './lib/canton-doc-utils.mjs';

const ROOT = process.cwd();
const INDEX_PATH = path.join(ROOT, 'src/content/canton-docs/index.json');
const PAGE_DIR = path.join(ROOT, 'src/content/canton-doc-pages');

const INTERNAL_ROOTS =
  /^\/?(overview|appdev|global-synchronizer|integrations|reference|api-reference)(\/|$)/;

const MD_LINK = /\]\(([^)\s]+)\)/g;
const HREF_DQ = /href="([^"]+)"/g;
const HREF_SQ = /href='([^']+)'/g;

function extractLinks(text) {
  const links = [];
  for (const re of [MD_LINK, HREF_DQ, HREF_SQ]) {
    re.lastIndex = 0;
    for (const m of text.matchAll(re)) {
      links.push(m[1]);
    }
  }
  return links;
}

function classifyHref(href) {
  if (!href || href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:')) {
    return 'skip';
  }
  if (href.startsWith('http://') || href.startsWith('https://')) {
    if (href.includes('docs.canton.network')) return 'external-official';
    return 'external';
  }
  if (href.startsWith('/docs/canton/') || href.startsWith('/zh/docs/canton/')) {
    return 'site-doc';
  }
  if (href.startsWith('/') && INTERNAL_ROOTS.test(href.slice(1))) {
    return 'legacy-official';
  }
  if (href.startsWith('/') && /[\u4e00-\u9fff]/.test(href)) {
    return 'legacy-non-ascii';
  }
  if (href.startsWith('/')) {
    return 'other-root';
  }
  if (!href.includes('://') && !href.startsWith('#')) {
    return 'relative';
  }
  return 'other';
}

function siteDocSlug(href, locale) {
  const prefix = locale === 'zh' ? '/zh/docs/canton/' : '/docs/canton/';
  if (!href.startsWith(prefix)) return null;
  const rest = href.slice(prefix.length).split('#')[0].split('?')[0].replace(/\/$/, '');
  return rest || null;
}

async function loadAllMd(locale) {
  const dir = path.join(PAGE_DIR, locale);
  const files = await readdir(dir);
  const out = [];
  for (const file of files) {
    if (!file.endsWith('.md')) continue;
    const content = await readFile(path.join(dir, file), 'utf8');
    out.push({ file, slug: file.replace(/\.md$/, ''), content });
  }
  return out;
}

async function main() {
  const index = JSON.parse(await readFile(INDEX_PATH, 'utf8'));
  const validSlugs = buildValidSlugSet(index.items);
  const slugByLocale = {
    en: new Set(index.items.filter((i) => i.locale === 'en').map((i) => i.slug)),
    zh: new Set(index.items.filter((i) => i.locale === 'zh').map((i) => i.slug)),
  };

  const issues = {
    legacyOfficial: new Map(),
    legacyNonAscii: new Map(),
    siteDocMissing: new Map(),
    otherRoot: new Map(),
    relativeUnresolved: new Map(),
    legacyNoSlug: new Map(),
  };

  for (const locale of ['en', 'zh']) {
    const pages = await loadAllMd(locale);
    for (const { file, slug: fromSlug, content } of pages) {
      const links = extractLinks(content);
      for (const href of links) {
        const kind = classifyHref(href);
        const key = `${locale}:${fromSlug}`;

        if (kind === 'legacy-official') {
          const computed = legacyPathToSlug(href);
          const ok = computed && validSlugs.has(computed);
          const bucket = issues.legacyOfficial;
          if (!bucket.has(href)) bucket.set(href, { count: 0, ok, computed, examples: [] });
          const e = bucket.get(href);
          e.count += 1;
          if (e.examples.length < 3 && !e.examples.includes(key)) e.examples.push(key);
          if (!ok) {
            const ns = issues.legacyNoSlug;
            if (!ns.has(href)) ns.set(href, { computed, count: 0, examples: [] });
            const n = ns.get(href);
            n.count += 1;
            if (n.examples.length < 3 && !n.examples.includes(key)) n.examples.push(key);
          }
        } else if (kind === 'legacy-non-ascii') {
          const bucket = issues.legacyNonAscii;
          if (!bucket.has(href)) bucket.set(href, { count: 0, examples: [] });
          const e = bucket.get(href);
          e.count += 1;
          if (e.examples.length < 3 && !e.examples.includes(key)) e.examples.push(key);
        } else if (kind === 'site-doc') {
          const target = siteDocSlug(href, locale);
          const ok = target && slugByLocale[locale].has(target);
          if (!ok) {
            const bucket = issues.siteDocMissing;
            const id = href;
            if (!bucket.has(id)) bucket.set(id, { count: 0, examples: [] });
            const e = bucket.get(id);
            e.count += 1;
            if (e.examples.length < 3 && !e.examples.includes(key)) e.examples.push(key);
          }
        } else if (kind === 'other-root') {
          const bucket = issues.otherRoot;
          if (!bucket.has(href)) bucket.set(href, { count: 0, examples: [] });
          const e = bucket.get(href);
          e.count += 1;
          if (e.examples.length < 3 && !e.examples.includes(key)) e.examples.push(key);
        } else if (kind === 'relative') {
          const bucket = issues.relativeUnresolved;
          if (!bucket.has(href)) bucket.set(href, { count: 0, examples: [] });
          const e = bucket.get(href);
          e.count += 1;
          if (e.examples.length < 3 && !e.examples.includes(key)) e.examples.push(key);
        }
      }
    }
  }

  const sortByCount = (map) =>
    [...map.entries()].sort((a, b) => b[1].count - a[1].count);

  console.log('=== Canton doc link audit ===\n');
  console.log(`Valid EN slugs: ${slugByLocale.en.size}, ZH slugs: ${slugByLocale.zh.size}\n`);

  const legacy = sortByCount(issues.legacyOfficial);
  const stillLegacy = legacy.filter(([, v]) => !v.ok);
  console.log(`1) Unrewritten legacy paths (/overview|appdev|...): ${stillLegacy.length} unique (${stillLegacy.reduce((s, [, v]) => s + v.count, 0)} occurrences)`);
  for (const [href, v] of stillLegacy.slice(0, 25)) {
    console.log(`   ${v.count}x ${href}  → slug: ${v.computed ?? 'NONE'}`);
  }
  if (stillLegacy.length > 25) console.log(`   ... +${stillLegacy.length - 25} more`);

  const noSlug = sortByCount(issues.legacyNoSlug);
  console.log(`\n2) Legacy paths with no matching slug: ${noSlug.length} unique`);
  for (const [href, v] of noSlug.slice(0, 20)) {
    console.log(`   ${v.count}x ${href}  (computed: ${v.computed ?? 'null'})`);
  }

  const nonAscii = sortByCount(issues.legacyNonAscii);
  console.log(`\n3) Non-ASCII / translated wrong paths: ${nonAscii.length} unique (${nonAscii.reduce((s, [, v]) => s + v.count, 0)} occurrences)`);
  for (const [href, v] of nonAscii.slice(0, 30)) {
    console.log(`   ${v.count}x ${href}`);
    console.log(`      e.g. ${v.examples.join(', ')}`);
  }

  const missing = sortByCount(issues.siteDocMissing);
  console.log(`\n4) /docs/canton/... pointing to missing slug: ${missing.length} unique`);
  for (const [href, v] of missing.slice(0, 20)) {
    console.log(`   ${v.count}x ${href}`);
  }

  const otherRoot = sortByCount(issues.otherRoot);
  console.log(`\n5) Other root-relative paths (not docs.canton categories): ${otherRoot.length} unique`);
  for (const [href, v] of otherRoot.slice(0, 25)) {
    console.log(`   ${v.count}x ${href}`);
  }

  const rel = sortByCount(issues.relativeUnresolved);
  const relFiltered = rel.filter(([h]) => !h.startsWith('./') && !h.endsWith('.md'));
  console.log(`\n6) Suspicious relative links (sample, non-./file.md): ${relFiltered.length} unique (top 20)`);
  for (const [href, v] of relFiltered.slice(0, 20)) {
    console.log(`   ${v.count}x ${href}  (${v.examples[0]})`);
  }

  const reportPath = path.join(ROOT, 'docs/education/canton-dev/link-audit-report.json');
  const report = {
    generatedAt: new Date().toISOString(),
    summary: {
      unrewrittenLegacy: stillLegacy.length,
      legacyNoSlug: noSlug.length,
      nonAsciiPaths: nonAscii.length,
      siteDocMissing: missing.length,
      otherRoot: otherRoot.length,
    },
    unrewrittenLegacy: stillLegacy.map(([href, v]) => ({ href, ...v })),
    legacyNoSlug: noSlug.map(([href, v]) => ({ href, ...v })),
    nonAsciiPaths: nonAscii.map(([href, v]) => ({ href, ...v })),
    siteDocMissing: missing.map(([href, v]) => ({ href, ...v })),
    otherRoot: otherRoot.slice(0, 100).map(([href, v]) => ({ href, ...v })),
  };
  await import('node:fs/promises').then(({ writeFile }) =>
    writeFile(reportPath, `${JSON.stringify(report, null, 2)}\n`, 'utf8'),
  );
  console.log(`\nFull report: ${reportPath}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
