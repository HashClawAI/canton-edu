import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import cantonDocsIndex from './src/content/canton-docs/index.json' with { type: 'json' };
import { buildLegacyRedirects } from './scripts/lib/canton-link-rewrite.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// GitHub Pages project site: set BASE_PATH in Actions, e.g. /repo-name/
const base = process.env.BASE_PATH || '/';
const site = process.env.PUBLIC_SITE_URL || 'https://ccprivacy.club';
const cantonLegacyRedirects = buildLegacyRedirects(cantonDocsIndex.items, base);

export default defineConfig({
  site,
  base,
  redirects: cantonLegacyRedirects,
  integrations: [
    sitemap({
      filter: (page) => !page.includes('/theme-demo') && !page.includes('/matrix-demo'),
    }),
  ],
  vite: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
  },
  i18n: {
    defaultLocale: 'zh',
    locales: ['zh', 'en'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
