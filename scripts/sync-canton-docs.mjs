import { mkdir, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import {
  SOURCE_INDEX_URL,
  buildDocRecord,
  dedupeBySlug,
  markdownPage,
  parseLlmsIndex,
  stripFrontmatter,
  summarizeBody,
} from './lib/canton-doc-utils.mjs';
import { translateBodyToZh } from './lib/translate-zh.mjs';
import { buildValidSlugSet, rewriteInternalLinks } from './lib/canton-link-rewrite.mjs';

const ROOT = process.cwd();
const KB_DIR = path.join(ROOT, 'docs/education/canton-dev');
const CONTENT_DIR = path.join(ROOT, 'src/content/canton-docs');
const PAGE_CONTENT_DIR = path.join(ROOT, 'src/content/canton-doc-pages');

const args = new Set(process.argv.slice(2));
const limitArg = process.argv.find((arg) => arg.startsWith('--limit='));
const limit = limitArg ? Number(limitArg.split('=')[1]) : Infinity;
const skipTranslate = args.has('--skip-translate');
const fetchDelayMs = Number(process.env.CANTON_DOCS_FETCH_DELAY_MS ?? 80);

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function fetchOfficialMarkdown(url) {
  try {
    const response = await fetch(url, {
      headers: { Accept: 'text/markdown, text/plain, */*' },
    });
    if (!response.ok) {
      return null;
    }
    return stripFrontmatter(await response.text());
  } catch {
    return null;
  }
}

async function cleanLocaleDir(localeDir, keepSlugs) {
  const keep = new Set(keepSlugs.map((slug) => `${slug}.md`));
  let files = [];
  try {
    files = await readdir(localeDir);
  } catch {
    return;
  }
  await Promise.all(
    files
      .filter((file) => file.endsWith('.md') && !keep.has(file))
      .map((file) => rm(path.join(localeDir, file))),
  );
}

async function writeLocaleFile(locale, doc, body, zhTitle, validSlugs) {
  const rewritten = rewriteInternalLinks(body, { locale, base: '/', validSlugs });
  const markdown = markdownPage({ doc, locale, body: rewritten, zhTitle });
  const kbPath = path.join(KB_DIR, locale, `${doc.slug}.md`);
  const pagePath = path.join(PAGE_CONTENT_DIR, locale, `${doc.slug}.md`);
  await writeFile(kbPath, markdown, 'utf8');
  await writeFile(pagePath, markdown, 'utf8');
  return {
    localPath: `docs/education/canton-dev/${locale}/${doc.slug}.md`,
    summary: summarizeBody(body),
  };
}

async function main() {
  const hasTranslateKey = Boolean(process.env.DOCS_TRANSLATE_API_KEY ?? process.env.OPENAI_API_KEY);
  const shouldTranslate = !skipTranslate && hasTranslateKey;

  if (!skipTranslate && !hasTranslateKey) {
    console.warn(
      'No DOCS_TRANSLATE_API_KEY / OPENAI_API_KEY — syncing English only. Run `npm run docs:translate-canton` after setting a key.',
    );
  }

  const response = await fetch(SOURCE_INDEX_URL);
  if (!response.ok) {
    throw new Error(`Failed to fetch ${SOURCE_INDEX_URL}: ${response.status} ${response.statusText}`);
  }

  const llmsText = await response.text();
  const indexedDocs = parseLlmsIndex(llmsText);
  const selected = dedupeBySlug(indexedDocs.map(buildDocRecord)).slice(0, limit);
  const validSlugs = new Set(selected.map((doc) => doc.slug));
  const generatedAt = new Date().toISOString();

  await mkdir(path.join(KB_DIR, 'en'), { recursive: true });
  await mkdir(path.join(KB_DIR, 'zh'), { recursive: true });
  await mkdir(CONTENT_DIR, { recursive: true });
  await mkdir(path.join(PAGE_CONTENT_DIR, 'en'), { recursive: true });
  await mkdir(path.join(PAGE_CONTENT_DIR, 'zh'), { recursive: true });

  const ragChunks = [];
  const contentItems = [];
  let fetched = 0;
  let translated = 0;
  let failed = 0;

  for (const [index, doc] of selected.entries()) {
    const officialBody = await fetchOfficialMarkdown(doc.sourceUrl);
    await sleep(fetchDelayMs);
    fetched += 1;

    if (!officialBody) {
      failed += 1;
      console.warn(`[${index + 1}/${selected.length}] missing body: ${doc.sourcePath}`);
      continue;
    }

    if ((index + 1) % 25 === 0 || index === 0) {
      console.log(`[${index + 1}/${selected.length}] syncing ${doc.slug}`);
    }

    {
      const enMeta = await writeLocaleFile('en', doc, officialBody, undefined, validSlugs);
      contentItems.push({
        slug: doc.slug,
        locale: 'en',
        title: doc.title,
        sourceTitle: doc.title,
        summary: enMeta.summary,
        category: doc.category,
        tags: doc.tags,
        sourceUrl: doc.sourceUrl,
        localPath: enMeta.localPath,
      });
      ragChunks.push({
        id: `canton-dev:en:${doc.slug}`,
        locale: 'en',
        title: doc.title,
        slug: doc.slug,
        category: doc.category,
        tags: doc.tags,
        source_url: doc.sourceUrl,
        local_path: enMeta.localPath,
        text: `${doc.title}\n${enMeta.summary}\n${officialBody.slice(0, 2500)}`,
      });
    }

    if (shouldTranslate) {
      try {
        const { zhTitle, zhBody, cached } = await translateBodyToZh({
          slug: doc.slug,
          title: doc.title,
          body: officialBody,
        });
        const zhMeta = await writeLocaleFile('zh', doc, zhBody, zhTitle, validSlugs);
        translated += cached ? 0 : 1;
        contentItems.push({
          slug: doc.slug,
          locale: 'zh',
          title: zhTitle,
          sourceTitle: doc.title,
          summary: zhMeta.summary,
          category: doc.category,
          tags: doc.tags,
          sourceUrl: doc.sourceUrl,
          localPath: zhMeta.localPath,
        });
        ragChunks.push({
          id: `canton-dev:zh:${doc.slug}`,
          locale: 'zh',
          title: zhTitle,
          slug: doc.slug,
          category: doc.category,
          tags: doc.tags,
          source_url: doc.sourceUrl,
          local_path: zhMeta.localPath,
          text: `${zhTitle}\n${zhMeta.summary}\n${zhBody.slice(0, 2500)}`,
        });
        console.log(`[${index + 1}/${selected.length}] zh ${cached ? '(cache)' : ''} ${doc.slug}`);
      } catch (error) {
        failed += 1;
        console.warn(`[${index + 1}/${selected.length}] translate failed ${doc.slug}: ${error.message}`);
      }
    }
  }

  const slugList = selected.map((doc) => doc.slug);
  await cleanLocaleDir(path.join(KB_DIR, 'en'), slugList);
  await cleanLocaleDir(path.join(KB_DIR, 'zh'), slugList);
  await cleanLocaleDir(path.join(PAGE_CONTENT_DIR, 'en'), slugList);
  await cleanLocaleDir(path.join(PAGE_CONTENT_DIR, 'zh'), slugList);

  const manifest = {
    name: 'Canton Developer Knowledge Base',
    unofficial: true,
    generatedAt,
    sourceIndexUrl: SOURCE_INDEX_URL,
    upstreamDocumentation: 'https://docs.canton.network/',
    totalInIndex: indexedDocs.length,
    syncedCount: selected.length,
    enCount: contentItems.filter((item) => item.locale === 'en').length,
    zhCount: contentItems.filter((item) => item.locale === 'zh').length,
    translateEnabled: shouldTranslate,
    documents: selected.map((doc) => ({
      slug: doc.slug,
      title: doc.title,
      category: doc.category,
      tags: doc.tags,
      sourceUrl: doc.sourceUrl,
      sourcePath: doc.sourcePath,
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

  console.log(
    `Done: index=${indexedDocs.length}, selected=${selected.length}, fetched=${fetched}, translated=${translated}, failed=${failed}, en=${manifest.enCount}, zh=${manifest.zhCount}`,
  );
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
