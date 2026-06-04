#!/usr/bin/env node
import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';

const ROOT = process.cwd();
const bodiesDir = path.join(ROOT, 'docs/education/canton-dev/zh-cursor-bodies');
const outDir = path.join(ROOT, 'docs/education/canton-dev/zh-cursor');

const slugs = process.argv.slice(2);
if (!slugs.length) {
  console.error('Usage: node scripts/build-zh-cursor-json.mjs <slug> [meta.json path optional]');
  process.exit(1);
}

const metaPath = process.argv.find((a) => a.endsWith('.json') && a.includes('meta'));
const metaFile = metaPath ?? path.join(bodiesDir, '_meta.json');
const metaAll = JSON.parse(await readFile(metaFile, 'utf8'));

await mkdir(outDir, { recursive: true });

for (const slug of slugs.filter((s) => !s.endsWith('.json'))) {
  const meta = metaAll[slug];
  if (!meta) throw new Error(`Missing meta for ${slug}`);
  const body = await readFile(path.join(bodiesDir, `${slug}.md`), 'utf8');
  const payload = { zhTitle: meta.zhTitle, summary: meta.summary, body: body.trim() };
  const out = path.join(outDir, `${slug}.json`);
  await writeFile(out, `${JSON.stringify(payload, null, 2)}\n`, 'utf8');
  console.log(`wrote ${out} (${body.length} chars)`);
}
