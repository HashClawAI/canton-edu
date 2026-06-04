import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const cantonDocs = defineCollection({
  loader: glob({ pattern: '**/*.json', base: './src/content/canton-docs' }),
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

export const collections = {
  'canton-docs': cantonDocs,
};
