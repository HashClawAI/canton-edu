# Canton Learn — bilingual static site (EN / 中文)

Independent Canton Network education starter: **English** at `/`, **Chinese** at `/zh/`. Built with [Astro](https://astro.build) for static output and [GitHub Pages](https://pages.github.com/).

## Local development

```bash
cd canton-edu
npm install
npm run dev
```

Open the URL shown in the terminal (usually `http://127.0.0.1:4321`).

## Build

```bash
npm run build
npm run preview
```

- **Root deploy** (custom domain or `username.github.io` repo with site at root): use default `BASE_PATH` `/`:

  ```bash
  npm run build
  ```

- **Project site** (`https://<user>.github.io/<repo>/`): match Astro `base` to the repo name:

  ```bash
  BASE_PATH=/your-repo-name/ PUBLIC_SITE_URL=https://<user>.github.io/<repo> npm run build
  ```

## GitHub Pages

1. Create a new repository and **push this folder as the repo root** (contents of `canton-edu/`, not the parent workspace).
2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
3. Ensure the default branch is **`main`** (or edit `.github/workflows/deploy.yml` to match your branch).
4. Push to `main`. The workflow sets `BASE_PATH` and `PUBLIC_SITE_URL` from the repository name automatically.

### User site (`username.github.io`)

If the repository name is exactly `username.github.io`, set in the workflow build step:

```yaml
env:
  BASE_PATH: /
  PUBLIC_SITE_URL: https://username.github.io
```

## Editing content

- **Strings (nav, copy):** `src/i18n/translations.ts`
- **Pages:** `src/pages/` (English) and `src/pages/zh/` (中文)
- **Styles:** `src/styles/global.css`
- **Language switch:** `src/components/LanguageSwitcher.astro`

## Disclaimer

This template is educational and **not** affiliated with Canton Foundation, Digital Asset, or network participants. Verify all technical claims against official documentation.
