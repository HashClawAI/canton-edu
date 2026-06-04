#!/usr/bin/env node
/**
 * Rewrite official-docs paths (/overview/..., /appdev/...) to on-site /docs/canton/{slug}.
 */
import { readFile, readdir, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { rewriteInternalLinks, buildValidSlugSet } from './lib/canton-link-rewrite.mjs';

const ROOT = process.cwd();
const INDEX_PATH = path.join(ROOT, 'src/content/canton-docs/index.json');
const PAGE_DIR = path.join(ROOT, 'src/content/canton-doc-pages');
const KB_DIR = path.join(ROOT, 'docs/education/canton-dev');

async function rewriteDir(dir, locale, validSlugs) {
  let changed = 0;
  let files = 0;
  const entries = await readdir(dir);
  for (const file of entries) {
    if (!file.endsWith('.md')) {
      continue;
    }
    files += 1;
    const filePath = path.join(dir, file);
    const raw = await readFile(filePath, 'utf8');
    const next = rewriteInternalLinks(raw, { locale, base: '/', validSlugs });
    if (next !== raw) {
      await writeFile(filePath, next, 'utf8');
      changed += 1;
    }
  }
  return { files, changed };
}

async function main() {
  const index = JSON.parse(await readFile(INDEX_PATH, 'utf8'));
  const validSlugs = buildValidSlugSet(index.items);

  const enPages = await rewriteDir(path.join(PAGE_DIR, 'en'), 'en', validSlugs);
  const zhPages = await rewriteDir(path.join(PAGE_DIR, 'zh'), 'zh', validSlugs);
  const enKb = await rewriteDir(path.join(KB_DIR, 'en'), 'en', validSlugs);
  const zhKb = await rewriteDir(path.join(KB_DIR, 'zh'), 'zh', validSlugs);

  console.log(
    `pages en: ${enPages.changed}/${enPages.files}, zh: ${zhPages.changed}/${zhPages.files}`,
  );
  console.log(`kb   en: ${enKb.changed}/${enKb.files}, zh: ${zhKb.changed}/${zhKb.files}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
