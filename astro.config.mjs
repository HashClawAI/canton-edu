import { defineConfig } from 'astro/config';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

// GitHub Pages project site: set BASE_PATH in Actions, e.g. /repo-name/
const base = process.env.BASE_PATH || '/';

export default defineConfig({
  site: process.env.PUBLIC_SITE_URL || undefined,
  base,
  vite: {
    resolve: {
      alias: {
        '@': path.resolve(__dirname, 'src'),
      },
    },
  },
  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'zh'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
