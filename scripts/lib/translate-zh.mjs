import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { hashText } from './canton-doc-utils.mjs';

const CACHE_DIR = path.join(process.cwd(), 'docs/education/canton-dev/.translate-cache');

const CODE_FENCE = /```[\s\S]*?```/g;
const INLINE_CODE = /`[^`\n]+`/g;

function maskProtected(text) {
  const tokens = [];
  let masked = text;
  const protect = (regex) => {
    masked = masked.replace(regex, (match) => {
      const token = `⟦P${tokens.length}⟧`;
      tokens.push(match);
      return token;
    });
  };
  protect(CODE_FENCE);
  protect(INLINE_CODE);
  return { masked, tokens };
}

function unmaskProtected(text, tokens) {
  let restored = text;
  tokens.forEach((value, index) => {
    restored = restored.replaceAll(`⟦P${index}⟧`, value);
  });
  return restored;
}

function chunkText(text, maxLen = 3500) {
  const paragraphs = text.split(/\n{2,}/);
  const chunks = [];
  let current = '';
  for (const paragraph of paragraphs) {
    const next = current ? `${current}\n\n${paragraph}` : paragraph;
    if (next.length > maxLen && current) {
      chunks.push(current);
      current = paragraph;
    } else {
      current = next;
    }
  }
  if (current) {
    chunks.push(current);
  }
  return chunks.length ? chunks : [text];
}

async function readCache(slug, sourceHash) {
  const file = path.join(CACHE_DIR, `${slug}.json`);
  try {
    const raw = JSON.parse(await readFile(file, 'utf8'));
    if (raw.sourceHash === sourceHash && raw.zhTitle && raw.zhBody) {
      return raw;
    }
  } catch {
    // miss
  }
  return null;
}

async function writeCache(slug, payload) {
  await mkdir(CACHE_DIR, { recursive: true });
  await writeFile(path.join(CACHE_DIR, `${slug}.json`), `${JSON.stringify(payload, null, 2)}\n`, 'utf8');
}

async function callTranslator(prompt) {
  const apiKey = process.env.DOCS_TRANSLATE_API_KEY ?? process.env.OPENAI_API_KEY;
  const baseUrl = (process.env.DOCS_TRANSLATE_API_BASE ?? 'https://api.openai.com/v1').replace(/\/$/, '');
  const model = process.env.DOCS_TRANSLATE_MODEL ?? 'gpt-4o-mini';

  if (!apiKey) {
    throw new Error(
      'Missing DOCS_TRANSLATE_API_KEY or OPENAI_API_KEY. Set one to generate Chinese documentation bodies.',
    );
  }

  const response = await fetch(`${baseUrl}/chat/completions`, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      model,
      temperature: 0.2,
      messages: [
        {
          role: 'system',
          content:
            'You translate technical documentation into Simplified Chinese. Preserve Markdown structure, headings, lists, links, and ALL placeholder tokens like ⟦P0⟧ exactly. Do not add commentary.',
        },
        { role: 'user', content: prompt },
      ],
    }),
  });

  if (!response.ok) {
    const detail = await response.text();
    throw new Error(`Translation API failed (${response.status}): ${detail.slice(0, 400)}`);
  }

  const json = await response.json();
  const content = json.choices?.[0]?.message?.content?.trim();
  if (!content) {
    throw new Error('Translation API returned empty content');
  }
  return content;
}

export async function translateTitle(title) {
  const { masked, tokens } = maskProtected(title);
  const translated = await callTranslator(
    `Translate this documentation title to Simplified Chinese. Return title only.\n\n${masked}`,
  );
  return unmaskProtected(translated, tokens).replace(/^["'“”]+|["'“”]+$/g, '');
}

export async function translateBodyToZh({ slug, title, body }) {
  const sourceHash = hashText(body);
  const cached = await readCache(slug, sourceHash);
  if (cached) {
    return { zhTitle: cached.zhTitle, zhBody: cached.zhBody, cached: true };
  }

  const chunks = chunkText(body);
  const translatedChunks = [];

  for (const chunk of chunks) {
    const { masked, tokens } = maskProtected(chunk);
    const translated = await callTranslator(
      `Translate the following Canton Network documentation excerpt to Simplified Chinese. Keep Markdown formatting and placeholders intact.\n\n${masked}`,
    );
    translatedChunks.push(unmaskProtected(translated, tokens));
    await new Promise((resolve) => setTimeout(resolve, 250));
  }

  const zhBody = translatedChunks.join('\n\n');
  const zhTitle = await translateTitle(title);
  await writeCache(slug, { sourceHash, zhTitle, zhBody, translatedAt: new Date().toISOString() });
  return { zhTitle, zhBody, cached: false };
}
