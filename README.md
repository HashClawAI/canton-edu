# Open Canton Edu — bilingual static site (EN / 中文)

Independent Canton Network education hub: **English** at `/`, **Chinese** at `/zh/`.

Built with [Astro](https://astro.build) · Deployed on [GitHub Pages](https://pages.github.com/) · Live at **[canton.tools](https://canton.tools/)** (project mirror: [hashclawai.github.io/canton-edu](https://hashclawai.github.io/canton-edu/))

## Site structure

| Page | EN path | Content |
|------|---------|---------|
| Home | `/` | Canton intro, live CC price, feature cards |
| Learn | `/learn` | 7-step learning path |
| Ecosystem | `/ecosystem` | Explorers, wallets, DeFi, naming, earn, institutional |
| CIPs | `/cips` | Key CIP summaries, SV onboarding, stats |
| News | `/news` | Event timeline, CIP watch |
| Videos | `/videos` | Interviews, Quadrillions podcast |
| Research | `/research` | Reports from Blockworks, Solus, Finadium, Coin Metrics, The Tie, DAIC |
| Community | `/community` | Discord, Telegram, forums, X accounts, governance |
| Resources | `/resources` | Official links, dev docs, chat, newsletters, GitHub, exchanges |

Chinese versions are mirrored at `/zh/learn`, `/zh/cips`, etc.

## Local development

```bash
npm install
npm run dev
```

Open the URL shown in the terminal (usually `http://127.0.0.1:4321`).

## Build

```bash
npm run build
npm run preview
```

For GitHub Pages project site (`https://<user>.github.io/<repo>/`):

```bash
BASE_PATH=/your-repo-name/ PUBLIC_SITE_URL=https://<user>.github.io/<repo> npm run build
```

## GitHub Pages deployment

1. **Settings → Pages → Source: GitHub Actions**
2. Push to `main` — the included workflow (`.github/workflows/deploy.yml`) builds and deploys automatically
3. `BASE_PATH` and `PUBLIC_SITE_URL` are set from the repo name in the workflow

## Editing content

All text lives in **one file**: `src/i18n/translations.ts`

| What to change | Where |
|----------------|-------|
| Page copy, data arrays | `src/i18n/translations.ts` — `en` and `zh` sections |
| Page layout / new sections | `src/pages/*.astro` (EN) + `src/pages/zh/*.astro` (ZH) |
| Styles | `src/styles/global.css` |
| Navigation | Auto-generated from `translations.nav` via `src/components/Nav.astro` |
| Live CC price + static implied sats/CC chart | `CoinPrice.astro` (browser: CoinGecko `simple/price` only). Chart SVG is **`npm run chart:build`** → `public/generated/cc-sats-chart-*.svg` before `astro build`. |

---

## AI-powered content updates (Cursor Skill)

This repo includes a **Cursor Agent Skill** that, on **each run**, fetches the latest Canton-related information from the web and **merges** it into the site **on top of the existing content** (additive updates, dedupe by URL/name, no mass deletion unless verified).

### What it does

The skill teaches any Cursor Agent to:

1. **Read** the current `translations.ts` (and related pages) for the sections being updated
2. **Scan** the web for new Canton news, CIPs, ecosystem projects, videos, reports, X accounts
3. **Classify** each finding and **merge** (prepend news, append lists, patch rows) — bilingual EN + ZH in lockstep
4. **Build** and verify all 18 pages compile
5. **Commit & push** — GitHub Actions deploys automatically

### How to use it

#### In Cursor IDE

1. Open this repo in [Cursor](https://cursor.com)
2. The skill at `.cursor/skills/canton-edu-updater/` is auto-detected
3. Ask the Agent:
   - *"Scan for Canton updates and refresh the site"*
   - *"Add recent Canton news to the News page"*
   - *"Check for new CIPs and update the CIPs page"*
   - *"Find new Canton ecosystem projects"*
4. The Agent reads the skill, compares against what is already published, searches the web, edits `translations.ts` incrementally, builds, and pushes

#### For contributors without Cursor

The skill files are plain Markdown — read `.cursor/skills/canton-edu-updater/SKILL.md` to understand the data format and workflow, then edit `translations.ts` manually following the same patterns.

### Skill files

```
.cursor/skills/canton-edu-updater/
├── SKILL.md       ← Main instructions (workflow, data formats, rules)
└── site-map.md    ← File tree, APIs, and search sources
```

### Data format cheat sheet

```typescript
// News item
{ date: '2026-04-01', tag: 'Ecosystem', title: '...', body: '...', url: '...' }

// Ecosystem entry
{ name: 'ProjectName', desc: 'Short desc', url: 'https://...' }

// X account
{ name: '@handle', desc: 'Role — followers', url: 'https://x.com/handle' }

// Video
{ title: '...', channel: '...', date: 'Mon YYYY', duration: 'NN min', summary: '...', youtubeId: '...' }

// Research report
{ source: 'Publisher', title: '...', date: 'Mon YYYY', desc: '...', url: '...' }
```

---

## Contributing

1. Fork the repo
2. Edit `src/i18n/translations.ts` — add to **both** `en` and `zh` sections
3. Run `npm run build` to verify
4. Open a PR

Or use Cursor with the built-in skill to automate the process.

## Disclaimer

This site is educational and **not** affiliated with Canton Foundation, Digital Asset, or network participants. Verify all technical claims against official documentation.
