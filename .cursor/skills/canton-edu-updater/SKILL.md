---
name: canton-edu-updater
description: >-
  Scan the web for Canton Network updates and add them to the canton-edu site
  (Canton Tools). Use when asked to update, refresh, or add new content to the
  Canton Tools / Canton education site, or when asked to scan for Canton news, CIPs, ecosystem projects,
  research reports, videos, or community accounts.
---

# Canton Tools Site Updater

Automates content updates for the Canton Network bilingual site (Canton Tools).

## Site Architecture

- **Framework**: Astro 5 static site, GitHub Pages
- **Repo**: `https://github.com/HashClawAI/canton-edu`
- **All text content** lives in ONE file: `src/i18n/translations.ts`
- **Pages** are in `src/pages/*.astro` (EN) and `src/pages/zh/*.astro` (ZH)
- **Styles**: `src/styles/global.css`
- **Both EN and ZH** must always be updated together (same structure, translated content)
- For full file tree and external APIs, see [site-map.md](site-map.md)

## Content Sections (in `translations.ts`)

| Section key | Nav label | What belongs here |
|-------------|-----------|-------------------|
| `home` | Home | Hero text, 4 feature cards, CoinPrice component |
| `learn` | Learn | 7-step learning path (step1–step7) |
| `ecosystem` | Ecosystem | Explorers, wallets, DEX/DeFi/lending, infra, naming, earn, institutional |
| `cips` | CIPs | Key CIP highlights table, SV onboarding list, stats |
| `news` | News | Timeline of major events (date/tag/title/body/url), CIP watch items |
| `videos` | Videos | Interview cards (youtubeId), Quadrillions podcast episodes |
| `research` | Research | Reports from Blockworks/Solus/Finadium/CoinMetrics/TheTie/DAIC/official |
| `community` | Community | Discord, Telegram, forums, X accounts, governance, dev fund, wiki links |
| `resources` | Resources | Official links, dev docs, forums, chat, newsletters, podcasts, GitHub, market data, exchanges |

## Update Workflow

### Step 1 — Scan

Search the web for new Canton content. Useful queries:

```
Canton Network news [current month] [current year]
Canton CIP approved proposed [current year]
Canton Network ecosystem new app project
Canton coin CC exchange listing [current year]
Canton Network interview video YouTube [current year]
Canton Network research report analysis
@CantonNetwork OR @CantonFdn site:x.com
site:github.com/canton-foundation/cips
```

### Step 2 — Classify

Map each finding to the correct section:

| Finding type | Target section | Key to add to |
|---|---|---|
| New event/milestone | `news.items` | Insert at top (array is reverse-chronological) |
| CIP approved/proposed | `news.cipWatchItems` or `cips.highlights` | Watch = in-discussion; highlights = important final/approved |
| New SV onboarded | `cips.svList` | Append |
| New DeFi/wallet/explorer/app | `ecosystem.*` | Match sub-section |
| New exchange listing | `resources.exchanges` | Append with pairs |
| New X account (5K+ followers) | `community.twitterAccounts` | Append with url |
| New Telegram group | `community.telegramGroups` | Append |
| New YouTube interview | `videos.interviews` | Append; needs `youtubeId` |
| New research report | `research.*` | Match sub-section by source |
| New official doc/link | `resources.official` or `resources.dev` | Append |

### Step 3 — Edit `translations.ts`

1. Read `src/i18n/translations.ts`
2. Add items to the EN section
3. Add corresponding translated items to the ZH section (same array index, same structure)
4. For news items: `{ date: 'YYYY-MM-DD', tag: 'Ecosystem|Governance|CIP|Institutional', title: '...', body: '...', url: '...' }`
5. For X accounts: `{ name: '@handle', desc: '...', url: 'https://x.com/handle' }`

**Rules:**
- Never remove existing entries unless they are confirmed wrong
- Keep arrays in their expected order (news = reverse-chronological, others = logical grouping)
- Every EN entry must have a ZH counterpart at the same position
- Preserve all TypeScript types and `as const` assertion

### Step 4 — Update page templates (only if new section types added)

If a new ecosystem sub-section or new page section is added, update the corresponding `.astro` page files (both EN and ZH) to render it. Existing sections auto-render from data.

### Step 5 — Build & verify

```bash
npm run build
```

All pages must build without errors. Check the page count in output matches expected (currently 18 pages = 9 pages × 2 languages).

### Step 6 — Commit & push

```bash
git add .
git commit -m "Update: [brief description of what was added]"
git push
```

GitHub Actions will auto-deploy to **`https://canton.tools/`** (GitHub project URL: `https://hashclawai.github.io/canton-edu/`).

## Data Format Reference

### News item

```typescript
{ date: '2026-04-01', tag: 'Ecosystem', title: 'Example title', body: 'One-sentence description.', url: 'https://...' }
```

### Ecosystem entry

```typescript
{ name: 'ProjectName', desc: 'Short description', url: 'https://...' }
```

### X account

```typescript
{ name: '@handle', desc: 'Role — follower count if notable', url: 'https://x.com/handle' }
```

### Video interview

```typescript
{ title: 'Video title', channel: 'Channel', date: 'Mon YYYY', duration: 'NN min', summary: 'Brief summary.', youtubeId: 'xxxxxxxxxxx' }
```

### Research report

```typescript
{ source: 'Publisher', title: 'Report title', date: 'Mon YYYY', desc: 'Key findings summary.', url: 'https://...' }
```

### CIP watch item

```typescript
{ id: 'CIP-NNNN', title: 'Short title', status: 'Proposed|Approved — implementing', summary: 'What it does.' }
```

## Checklist Before Finishing

- [ ] EN and ZH have identical array lengths for every section touched
- [ ] `npm run build` succeeds with expected page count
- [ ] News items are in reverse chronological order
- [ ] No duplicate entries (check by URL or name)
- [ ] Commit message describes what was added
- [ ] `git push` succeeded
