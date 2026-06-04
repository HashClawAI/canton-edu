#!/usr/bin/env node
/**
 * Build zh-cursor/{slug}.json from en/{slug}.md + zh-cursor-bodies/{slug}.md
 * Usage: node scripts/write-zh-cursor-from-en.mjs <slug>...
 */
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const enDir = path.join(ROOT, 'docs/education/canton-dev/en');
const bodiesDir = path.join(ROOT, 'docs/education/canton-dev/zh-cursor-bodies');
const outDir = path.join(ROOT, 'docs/education/canton-dev/zh-cursor');
const metaPath = path.join(bodiesDir, '_meta-integrations.json');

const slugs = process.argv.slice(2);
if (!slugs.length) {
  console.error('Usage: node scripts/write-zh-cursor-from-en.mjs <slug>...');
  process.exit(1);
}

const metaAll = JSON.parse(await readFile(metaPath, 'utf8'));
await mkdir(outDir, { recursive: true });

let ok = 0;
for (const slug of slugs) {
  const meta = metaAll[slug];
  if (!meta) {
    console.error(`skip (no meta): ${slug}`);
    continue;
  }
  const bodyPath = path.join(bodiesDir, `${slug}.md`);
  let body;
  try {
    body = (await readFile(bodyPath, 'utf8')).trim();
  } catch {
    console.error(`skip (no body): ${slug}`);
    continue;
  }
  const out = path.join(outDir, `${slug}.json`);
  await writeFile(
    out,
    `${JSON.stringify({ zhTitle: meta.zhTitle, summary: meta.summary, body }, null, 2)}\n`,
    'utf8',
  );
  console.log(`wrote ${slug} (${body.length} chars)`);
  ok++;
}
console.log(`done: ${ok}/${slugs.length}`);
