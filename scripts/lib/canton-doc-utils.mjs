import { createHash } from 'node:crypto';

const SOURCE_INDEX_URL = 'https://docs.canton.network/llms.txt';

export { SOURCE_INDEX_URL };

export function parseLlmsIndex(markdown) {
  const docs = [];
  const linkPattern = /^- \[(?<title>[^\]]+)\]\((?<url>https:\/\/docs\.canton\.network(?<path>[^)]+))\)$/gm;
  for (const match of markdown.matchAll(linkPattern)) {
    docs.push({
      title: match.groups.title.trim(),
      sourceUrl: match.groups.url,
      sourcePath: match.groups.path,
    });
  }
  return docs;
}

export function pathToSlug(sourcePath) {
  const base = sourcePath.replace(/^\//, '').replace(/\.md$/i, '');
  const slug = base
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '');
  return slug || 'doc';
}

export function pathToCategory(sourcePath) {
  const segment = sourcePath.replace(/^\//, '').split('/').filter(Boolean)[0];
  return segment?.replace(/\.md$/i, '') ?? 'docs';
}

export function pathToTags(sourcePath) {
  const parts = sourcePath.replace(/^\//, '').split('/').filter(Boolean).map((p) => p.replace(/\.md$/i, ''));
  return [...new Set(parts.slice(0, 4))];
}

export function escapeYaml(value) {
  return String(value).replaceAll('"', '\\"');
}

export function stripFrontmatter(text) {
  if (!text.startsWith('---')) {
    return text.trim();
  }
  const end = text.indexOf('\n---', 3);
  if (end === -1) {
    return text.trim();
  }
  return text.slice(end + 4).trim();
}

export function hashText(text) {
  return createHash('sha256').update(text).digest('hex');
}

export function dedupeBySlug(entries) {
  const seen = new Map();
  for (const entry of entries) {
    let key = entry.slug;
    if (seen.has(key)) {
      entry.slug = `${key}-${hashText(entry.sourcePath).slice(0, 8)}`;
      key = entry.slug;
    }
    seen.set(key, entry);
  }
  return [...seen.values()];
}

export function extractPageBody(markdown) {
  let body = stripFrontmatter(markdown);
  body = body.replace(/^#\s.+\n+/, '');
  const cut = body.lastIndexOf('\n---\n');
  if (cut !== -1) {
    body = body.slice(0, cut).trim();
  }
  return body.trim();
}

export function buildDocRecord(upstream) {
  const slug = pathToSlug(upstream.sourcePath);
  return {
    slug,
    title: upstream.title,
    sourceUrl: upstream.sourceUrl,
    sourcePath: upstream.sourcePath,
    category: pathToCategory(upstream.sourcePath),
    tags: pathToTags(upstream.sourcePath),
  };
}

export function markdownPage({ doc, locale, body, zhTitle }) {
  const isZh = locale === 'zh';
  const title = isZh ? (zhTitle ?? doc.title) : doc.title;
  const attribution = isZh
    ? '本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。'
    : 'Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.';

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

${body}

---

> ${attribution}
`;
}

export function summarizeBody(body, max = 220) {
  const plain = body
    .replace(/```[\s\S]*?```/g, ' ')
    .replace(/[#>*\[\]()!`]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  if (plain.length <= max) {
    return plain;
  }
  return `${plain.slice(0, max).trim()}…`;
}
