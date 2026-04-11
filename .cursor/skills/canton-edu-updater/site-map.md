# Canton Tools — Site Map Reference

Quick reference for the agent when updating the repo **incrementally** (merge new findings into existing `translations.ts` and related files).

## File tree (high level)

```
canton-edu/
├── src/i18n/translations.ts     ← primary copy: all EN + ZH strings & lists
├── src/components/
│   ├── CoinPrice.astro          ← live CoinGecko price (client); sats/CC chart = build-time SVG (`npm run chart:build` → `public/generated/`)
│   ├── Nav.astro
│   └── LanguageSwitcher.astro
├── src/lib/
│   ├── fetchCipDiscussTopics.ts ← CIPs page: topics at build (Jina / optional Groups.io)
│   └── siteBuildTimestamp.ts    ← News pages “last updated” at build
├── src/pages/                   ← EN *.astro
├── src/pages/zh/                ← ZH mirrors
├── src/styles/global.css
├── .env.example                 ← optional GROUPSIO_* for CIP discuss API
├── .github/workflows/deploy.yml
└── .cursor/skills/canton-edu-updater/
```

## URLs

- **Live site**: `https://canton.tools/`
- **Repo**: `https://github.com/HashClawAI/canton-edu`
- **CIP discuss (topics)**: `https://lists.sync.global/g/cip-discuss/topics` (wired via build fetch in `fetchCipDiscussTopics.ts`)

## Scan sources (non-exhaustive)

| Source | URL | Typical updates |
|--------|-----|-----------------|
| Canton Foundation | https://canton.foundation/ | SV, fund, announcements |
| CIP repo | https://github.com/canton-foundation/cips | New / merged CIPs |
| Canton blog | https://www.canton.network/blog | Official posts |
| CommunityOne feed | communityone.io (Canton server) | Ecosystem / governance blurbs |
| CoinGecko | coingecko.com coin canton | Listings / labels in resources if needed |

## Agent reminder

**Each run:** read current `translations.ts` → web scan → add or patch rows → EN/ZH parity → `npm run build` → commit + push. Prefer **additive** edits; remove only when verified or requested.
