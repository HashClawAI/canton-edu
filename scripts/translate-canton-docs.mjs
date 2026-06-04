import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { extractPageBody, markdownPage, summarizeBody } from './lib/canton-doc-utils.mjs';
import { translateBodyToZh } from './lib/translate-zh.mjs';

const ROOT = process.cwd();
const PAGE_EN = path.join(ROOT, 'src/content/canton-doc-pages/en');
const KB_ZH = path.join(ROOT, 'docs/education/canton-dev/zh');
const PAGE_ZH = path.join(ROOT, 'src/content/canton-doc-pages/zh');
const manifestPath = path.join(ROOT, 'docs/education/canton-dev/manifest.json');
const indexPath = path.join(ROOT, 'src/content/canton-docs/index.json');

const limitArg = process.argv.find((arg) => arg.startsWith('--limit='));
const limit = limitArg ? Number(limitArg.split('=')[1]) : Infinity;
const slugArg = process.argv.find((arg) => arg.startsWith('--slug='));
const onlySlug = slugArg?.split('=')[1];

async function main() {
  const manifest = JSON.parse(await readFile(manifestPath, 'utf8'));
  let docs = manifest.documents ?? [];
  if (onlySlug) {
    docs = docs.filter((doc) => doc.slug === onlySlug);
  }
  docs = docs.slice(0, limit);

  const index = JSON.parse(await readFile(indexPath, 'utf8'));
  const items = index.items.filter((item) => item.locale !== 'zh');

  let done = 0;
  for (const doc of docs) {
    const enPath = path.join(PAGE_EN, `${doc.slug}.md`);
    const raw = await readFile(enPath, 'utf8');
    const body = extractPageBody(raw);
    const { zhTitle, zhBody, cached } = await translateBodyToZh({
      slug: doc.slug,
      title: doc.title,
      body,
    });
    const record = {
      slug: doc.slug,
      title: doc.title,
      sourceUrl: doc.sourceUrl,
      sourcePath: doc.sourcePath,
      category: doc.category,
      tags: doc.tags,
    };
    const markdown = markdownPage({ doc: record, locale: 'zh', body: zhBody, zhTitle });
    await mkdir(KB_ZH, { recursive: true });
    await mkdir(PAGE_ZH, { recursive: true });
    await writeFile(path.join(KB_ZH, `${doc.slug}.md`), markdown, 'utf8');
    await writeFile(path.join(PAGE_ZH, `${doc.slug}.md`), markdown, 'utf8');
    items.push({
      slug: doc.slug,
      locale: 'zh',
      title: zhTitle,
      sourceTitle: doc.title,
      summary: summarizeBody(zhBody),
      category: doc.category,
      tags: doc.tags,
      sourceUrl: doc.sourceUrl,
      localPath: `docs/education/canton-dev/zh/${doc.slug}.md`,
    });
    done += 1;
    console.log(`[${done}/${docs.length}] ${cached ? 'cache' : 'new'} ${doc.slug}`);
  }

  index.items = items;
  index.generatedAt = new Date().toISOString();
  await writeFile(indexPath, `${JSON.stringify(index, null, 2)}\n`, 'utf8');
  console.log(`Translated ${done} Chinese pages.`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
