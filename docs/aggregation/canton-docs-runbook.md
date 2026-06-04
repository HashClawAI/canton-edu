# Canton Docs Knowledge Base Runbook

## Cursor batch translation (no API key)

1. Agent writes payloads to `docs/education/canton-dev/zh-cursor/{slug}.json`.
2. Apply a batch:

```bash
npm run docs:apply-cursor-zh -- --batch=1
```

Progress is tracked in `docs/education/canton-dev/translate-progress.json`. Add new batches under `batches` in that file, then repeat.

## Full sync (English + optional Chinese)

```bash
# 1) Mirror all pages from docs.canton.network (English)
npm run docs:sync-canton -- --skip-translate

# 2) Translate to Chinese (requires API key, resumable cache)
export OPENAI_API_KEY=sk-...
npm run docs:translate-canton

# Or sync + translate in one pass when the key is set:
npm run docs:sync-canton
```

### Flags

| Command | Meaning |
|---------|---------|
| `npm run docs:sync-canton -- --limit=20` | Process first N pages only (smoke test) |
| `npm run docs:sync-canton -- --skip-translate` | English mirror only |
| `npm run docs:translate-canton -- --limit=50` | Translate first N Chinese pages |
| `npm run docs:translate-canton -- --slug=appdev-modules-m6-overview` | Translate one page |

### Translation environment

| Variable | Default |
|----------|---------|
| `OPENAI_API_KEY` or `DOCS_TRANSLATE_API_KEY` | required for Chinese |
| `DOCS_TRANSLATE_API_BASE` | `https://api.openai.com/v1` |
| `DOCS_TRANSLATE_MODEL` | `gpt-4o-mini` |
| `CANTON_DOCS_FETCH_DELAY_MS` | `80` |

Chinese translations are cached under `docs/education/canton-dev/.translate-cache/`.

## Build

```bash
npm run build
```

## Policy

- Site pages are self-contained; users read EN/ZH on CC Privacy Club.
- Official attribution appears at the bottom of each article (CC-BY-4.0).
- Re-run sync when `https://docs.canton.network/llms.txt` changes.
