import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { markdownPage, summarizeBody } from './lib/canton-doc-utils.mjs';
import {
  buildLegacyPathMap,
  buildSlugToSourceUrl,
  buildValidSlugSet,
  rewriteAllLinks,
} from './lib/canton-link-rewrite.mjs';

const ROOT = process.cwd();
const manifestPath = path.join(ROOT, 'docs/education/canton-dev/manifest.json');
const progressPath = path.join(ROOT, 'docs/education/canton-dev/translate-progress.json');
const indexPath = path.join(ROOT, 'src/content/canton-docs/index.json');
const KB_ZH = path.join(ROOT, 'docs/education/canton-dev/zh');
const PAGE_ZH = path.join(ROOT, 'src/content/canton-doc-pages/zh');

const batchArg = process.argv.find((arg) => arg.startsWith('--batch='));
const batchId = batchArg?.split('=')[1] ?? '1';

async function main() {
  const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  const progress = JSON.parse(await readFile(progressPath, 'utf8'));
  const batch = progress.batches?.[batchId];
  if (!batch) {
    throw new Error(`Unknown batch: ${batchId}`);
  }

  const index = JSON.parse(await readFile(indexPath, 'utf8'));
  const linkCtx = {
    base: '/',
    validSlugs: buildValidSlugSet(index.items),
    legacyPathMap: buildLegacyPathMap(index.items),
    slugToSourceUrl: buildSlugToSourceUrl(index.items),
  };
  const zhBySlug = new Map(index.items.filter((item) => item.locale === 'zh').map((item) => [item.slug, item]));
  const docBySlug = new Map(manifest.documents.map((doc) => [doc.slug, doc]));

  let applied = 0;
  for (const slug of batch.slugs) {
    const payloadPath = path.join(ROOT, 'docs/education/canton-dev/zh-cursor', `${slug}.json`);
    let payload;
    try {
      payload = JSON.parse(await readFile(payloadPath, 'utf8'));
    } catch {
      console.warn(`skip (no payload): ${slug}`);
      continue;
    }

    const doc = docBySlug.get(slug);
    if (!doc) {
      console.warn(`skip (not in manifest): ${slug}`);
      continue;
    }

    const record = {
      slug: doc.slug,
      title: doc.title,
      sourceUrl: doc.sourceUrl,
      sourcePath: doc.sourcePath,
      category: doc.category,
      tags: doc.tags,
    };
    const body = rewriteAllLinks(payload.body, { ...linkCtx, locale: 'zh', fromSlug: slug });
    const markdown = markdownPage({
      doc: record,
      locale: 'zh',
      body,
      zhTitle: payload.zhTitle,
    });

    await mkdir(KB_ZH, { recursive: true });
    await mkdir(PAGE_ZH, { recursive: true });
    await writeFile(path.join(KB_ZH, `${slug}.md`), markdown, 'utf8');
    await writeFile(path.join(PAGE_ZH, `${slug}.md`), markdown, 'utf8');

    zhBySlug.set(slug, {
      slug: doc.slug,
      locale: 'zh',
      title: payload.zhTitle,
      sourceTitle: doc.title,
      summary: payload.summary ?? summarizeBody(payload.body),
      category: doc.category,
      tags: doc.tags,
      sourceUrl: doc.sourceUrl,
      localPath: `docs/education/canton-dev/zh/${slug}.md`,
    });
    applied += 1;
    if (!progress.completed.includes(slug)) {
      progress.completed.push(slug);
    }
    console.log(`applied: ${slug}`);
  }

  const enItems = index.items.filter((item) => item.locale === 'en');
  index.items = [...enItems, ...zhBySlug.values()];
  index.generatedAt = new Date().toISOString();
  batch.status = batch.slugs.every((slug) => progress.completed.includes(slug)) ? 'done' : 'in_progress';
  progress.zhCount = progress.completed.length;

  await writeFile(indexPath, `${JSON.stringify(index, null, 2)}\n`, 'utf8');
  await writeFile(progressPath, `${JSON.stringify(progress, null, 2)}\n`, 'utf8');
  console.log(`Batch ${batchId}: applied ${applied}, total zh completed: ${progress.completed.length}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
