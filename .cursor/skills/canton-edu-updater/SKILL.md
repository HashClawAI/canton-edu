---
name: canton-edu-updater
description: >-
  On each run: fetch the latest Canton Network information from the web, merge
  updates into the existing canton-edu site (CC Privacy Club) without wiping prior
  content. Use when asked to update, refresh, or add content; scan for Canton news,
  CIPs, ecosystem, research, videos, or community sources.
---

# CC Privacy Club Site Updater

Automates **incremental** content updates for the Canton Network bilingual site (CC Privacy Club): **read what is already published → scan for what is new → apply changes on top of the old version** (append, prepend, or targeted edits). Do **not** replace whole sections unless the user explicitly asks for a rewrite.

## Site Architecture

- **Framework**: Astro 5 static site, GitHub Pages
- **Repo**: `https://github.com/HashClawAI/canton-edu`
- **Primary content file**: `src/i18n/translations.ts` (EN + ZH in one file, `as const`)
- **Pages**: `src/pages/*.astro` (EN) and `src/pages/zh/*.astro` (ZH)
- **Styles**: `src/styles/global.css`
- **Live / build-time data** (usually **no** `translations.ts` edit unless fixing copy):
  - `src/components/CoinPrice.astro` — CC/BTC prices + 24h implied sats/CC chart (CoinGecko in the browser)
  - `src/lib/fetchCipDiscussTopics.ts` — CIPs page topic list at **build** time (Jina reader; optional `GROUPSIO_API_KEY` for Groups.io API — see `.env.example`)
- **News “Last updated”** on the News pages comes from `src/lib/siteBuildTimestamp.ts` at build time; it advances when you deploy, not when you edit strings alone.
- For file tree and external links, see [site-map.md](site-map.md)

## Incremental update rules (every run)

1. **Read first** — Open `src/i18n/translations.ts` (and any `.astro` you might extend) and note current entries in the sections you will touch (lengths, latest dates, URLs).
2. **Fetch latest** — Use the web (and repo links below) with **current month/year** in queries; prefer primary sources (Foundation, GitHub CIPs, official blogs) over aggregators when possible.
3. **Merge, don’t reset** — Add new rows where lists grow; insert news at the **top** (reverse-chronological). **Do not remove** existing items unless they are **verified wrong** or the user asked to delete them.
4. **Dedupe** — Before adding: same `url` → skip; for news, same title + same week → skip; for ecosystem rows, same `name` or same canonical URL → skip or merge description if strictly better.
5. **Bilingual parity** — Every EN change needs the matching ZH structure **at the same array index** (or same object keys). Never leave one language half-updated.
6. **Types** — Keep TypeScript valid; preserve the file’s `as const` export pattern.
7. **Verify** — `npm run build` (expect **18** static routes). Fix errors before commit.
8. **Ship** — `git add`, `git commit`, `git push` so GitHub Actions deploys to **`https://ccprivacy.club/`**.

## Content sections (in `translations.ts`)

| Section key | Nav label | What belongs here |
|-------------|-----------|-------------------|
| `home` | Home | Hero, cards, contribute block; CoinPrice labels |
| `learn` | Learn | 7-step path (step titles + bodies) |
| `ecosystem` | Ecosystem | Explorers, wallets, DEX/DeFi, **Payment** (`payments`), infra, naming, earn, institutional |
| `cips` | CIPs | Highlights table, SV list, stats, **mailing-list copy** (topic list is build-fetched) |
| `news` | News | `items[]` timeline only (CIP discussion lives on **CIPs** page) |
| `videos` | Videos | Interviews (`youtubeId`), podcast links |
| `research` | Research | Reports by publisher |
| `community` | Community | Discord, Telegram, X, governance, dev fund, wiki |
| `resources` | Resources | Official links, dev docs, forums, newsletters, GitHub, markets, exchanges |

## Scan queries (examples — adjust dates)

Also run queries that surface **Digital Asset (company)**, **Yuval Rooz**, and **Canton Network** together — e.g. partnerships, MOUs, and institutional adoption:

```
Digital Asset Holdings Canton Network
Yuval Rooz Digital Asset Canton Network
Hanwha Digital Asset MOU Canton
Canton Network news April 2026
Canton CIP approved OR proposed 2026
site:github.com/canton-foundation/cips
Canton Network ecosystem new project 2026
Canton coin CC listing exchange 2026
Canton Network interview YouTube 2026
@CantonNetwork OR @CantonFdn site:x.com
```

## Classify → where to add

| Finding type | Target | How to merge |
|--------------|--------|----------------|
| New milestone / press | `news.items` | **Prepend** one object EN + one ZH |
| CIP in discussion | `cips.highlights` / mailing list (CIPs page); not duplicated on News | Update highlights or rely on build-fetched discuss list |
| New SV line in governance story | `cips.svList` | Append if not already listed |
| New app / infra | `ecosystem.*` | Append to best sub-array (`payments` for payment rails) |
| New CC pair | `resources.exchanges` | Append if new venue |
| New X / Telegram | `community.twitterAccounts` / `telegramGroups` | Append if not duplicate |
| New interview | `videos.interviews` | Append with valid `youtubeId` |
| New PDF / report | `research.*` | Append under matching publisher group |
| Official URL | `resources.official` or `resources.dev` | Append |

## Edit checklist

- [ ] Existing content in touched sections **reviewed** (not blindly overwritten)
- [ ] New items **deduped** by URL / name / obvious duplicate story
- [ ] EN + ZH **same shape and order**
- [ ] `npm run build` succeeds (**18** pages)
- [ ] Commit message states what was **added or corrected** (incremental)

## Data shapes (reminder)

See previous skill version for full examples: `news.items` use `{ date, tag, title, body, url }`; ecosystem `{ name, desc, url }` — **always set `url`** when a canonical link exists (e.g. `https://www.canton.network/ecosystem/...`, product site, or issuer homepage); X `{ name, desc, url }`; videos `{ title, channel, date, duration, summary, youtubeId }`; research `{ source, title, date, desc, url }`.

## When to touch `.astro` files

Only if you add a **new** subsection key that pages do not yet render, or fix layout/accessibility. Most updates are **`translations.ts` only**.
