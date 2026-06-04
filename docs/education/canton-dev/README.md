# Canton Developer Knowledge Base

This is an unofficial, source-linked learning knowledge base for Canton Network developers.
It is designed to serve three uses:

- Human-readable bilingual Markdown notes.
- RAG-friendly JSONL chunks for agents.
- A generated website section in CC Privacy Club.

Primary upstream source:

- Canton Network Documentation: https://docs.canton.network/
- LLM-friendly index: https://docs.canton.network/llms.txt

## Layout

- `en/` contains English learning notes anchored to official Canton docs pages.
- `zh/` contains Chinese learning notes with the same slugs and source URLs.
- `manifest.json` records the selected core documents, upstream URLs, tags, and generation metadata.
- `rag-index.jsonl` contains retrieval chunks with stable IDs, local paths, titles, tags, and official source URLs.

## Attribution

Canton Network official documentation is maintained by its upstream authors and is linked here as the primary source.
This knowledge base does not claim official status, endorsement, or completeness. It summarizes and organizes selected
developer topics for learning and retrieval. Always verify implementation details against the upstream page linked in
each note.

## Refresh

Run from the repository root:

```bash
npm run docs:sync-canton
```

The script reads `https://docs.canton.network/llms.txt`, selects the curated core developer set, and regenerates:

- `docs/education/canton-dev/en/*.md`
- `docs/education/canton-dev/zh/*.md`
- `docs/education/canton-dev/manifest.json`
- `docs/education/canton-dev/rag-index.jsonl`
- `src/content/canton-docs/index.json`
