# Canton Docs Knowledge Base Runbook

This runbook describes how maintainers and agents refresh and use the Canton developer knowledge base.

## Refresh Command

Run from the repository root:

```bash
npm run docs:sync-canton
```

The command fetches `https://docs.canton.network/llms.txt`, verifies the curated core pages still exist, and regenerates:

- `docs/education/canton-dev/en/*.md`
- `docs/education/canton-dev/zh/*.md`
- `docs/education/canton-dev/manifest.json`
- `docs/education/canton-dev/rag-index.jsonl`
- `src/content/canton-docs/index.json`

After a refresh, run:

```bash
npm run build
```

## Source Policy

- Official documentation source: https://docs.canton.network/
- LLM-friendly source index: https://docs.canton.network/llms.txt
- Local notes are unofficial and educational.
- Every local topic must retain the upstream `sourceUrl`.
- Do not copy large official pages into `translations.ts` or long UI strings.

## Agent and RAG Rules

Agents may use `docs/education/canton-dev/rag-index.jsonl` as the retrieval entry point.

Required behavior:

- Cite the official `source_url` for implementation-sensitive answers.
- Mention that CC Privacy Club is an unofficial learning hub when there is risk of confusion.
- Prefer the official page over local summaries for protocol, API, deployment, and security details.
- Keep EN and ZH slugs aligned.
- If a source URL disappears from `llms.txt`, stop and ask a maintainer before replacing it with an unrelated page.

## Human Review Checklist

- `manifest.json` includes the intended core documents.
- EN and ZH generated files have the same slug count.
- `rag-index.jsonl` has one EN and one ZH chunk for each manifest document.
- New website routes render locally.
- The PR summary links back to official Canton documentation and states that the knowledge base is unofficial.
