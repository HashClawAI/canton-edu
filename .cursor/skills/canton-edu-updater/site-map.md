# Canton Tools — Site Map Reference

Quick reference for the agent when it needs to understand the file layout.

## File tree

```
canton-edu/
├── src/
│   ├── i18n/translations.ts        ← ALL text content (EN + ZH)
│   ├── components/
│   │   ├── Nav.astro                ← navigation (auto from translations.nav)
│   │   ├── CoinPrice.astro          ← live CC price ticker (CoinGecko API)
│   │   └── LanguageSwitcher.astro
│   ├── layouts/BaseLayout.astro     ← shared HTML shell
│   ├── styles/global.css            ← all CSS
│   └── pages/
│       ├── index.astro              ← EN home
│       ├── learn.astro
│       ├── ecosystem.astro
│       ├── cips.astro
│       ├── news.astro
│       ├── videos.astro
│       ├── research.astro
│       ├── community.astro
│       ├── resources.astro
│       └── zh/                      ← ZH mirrors (same filenames)
├── .cursor/skills/canton-edu-updater/  ← this skill
├── public/favicon.svg
├── .github/workflows/deploy.yml     ← GitHub Actions → Pages
├── astro.config.mjs
├── package.json
└── README.md
```

## Key external APIs

- **CoinGecko** (client-side, no key): `canton-network` coin ID
- **GitHub Actions**: auto-deploys on push to `main`
- **Primary site URL**: `https://canton.tools/`
- **GitHub Pages project URL**: `https://hashclawai.github.io/canton-edu/`

## Useful search sources for updates

| Source | URL | What to look for |
|--------|-----|-------------------|
| Canton Foundation news | https://canton.foundation/ | SV additions, fund announcements |
| CIP repo | https://github.com/canton-foundation/cips | New/updated CIPs |
| Canton blog | https://www.canton.network/blog | Official articles |
| CommunityOne | https://communityone.io/servers/1379531004116471878/canton-network/ | Discord news feed |
| Canton Wiki | https://canton.wiki/ | Ecosystem updates |
| CoinGecko Canton | https://www.coingecko.com/en/coins/canton | Market data changes |
| X @CantonNetwork | https://x.com/CantonNetwork | Announcements |
| X @CantonFdn | https://x.com/CantonFdn | Foundation updates |
