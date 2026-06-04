import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const cantonDocsIndex = defineCollection({
  loader: glob({ pattern: 'index.json', base: './src/content/canton-docs' }),
  schema: z.object({
    generatedAt: z.string(),
    sourceIndexUrl: z.string().url(),
    items: z.array(
      z.object({
        slug: z.string(),
        locale: z.enum(['en', 'zh']),
        title: z.string(),
        sourceTitle: z.string(),
        summary: z.string(),
        category: z.string(),
        tags: z.array(z.string()),
        sourceUrl: z.string().url(),
        localPath: z.string(),
      }),
    ),
  }),
});

const cantonDocPages = defineCollection({
  loader: glob({
    pattern: '{en,zh}/*.md',
    base: './src/content/canton-doc-pages',
    generateId: ({ entry }) => entry.replace(/\.md$/, ''),
  }),
  schema: z.object({
    title: z.string(),
    slug: z.string(),
    locale: z.enum(['en', 'zh']),
    category: z.string(),
    source_url: z.string().url(),
    source_title: z.string(),
    tags: z.array(z.string()),
  }),
});

export const collections = {
  'canton-docs': cantonDocsIndex,
  'canton-doc-pages': cantonDocPages,
};
