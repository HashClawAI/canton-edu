<!-- PR body for: fork canton-dev-fund → base canton-foundation/canton-dev-fund. -->

## Development Fund Proposal Submission

**Proposal:** `proposals/open-canton-edu.md` · **Upstream:** [canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)

---

## Summary

**Open Canton Edu** ([github.com/HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) requests **Canton Development Fund** support for **Agentic Education**: maintainer-facing **agents** (e.g. Cursor **Skills**, scripted flows) that **open draft PRs** for aggregation refreshes, bilingual **generation units**, i18n preflight, and on-chain/indexer explainers—**all merges to `main` remain human-reviewed**.

**Deliverables:** **`docs/agentic-education/`** (`playbooks.md`, `guardrails.md`, **`eval-log.md` ≥10 scenarios**), **daily** Actions rebuild, **≥8** aggregation PRs (manifest), **≥18** generation units (**news / 大事记**, research, video, Learn copy; **≥6** `agentic: true` + `playbook_id`; **≥4** `onchain:true`), **`ja`/`ko` i18n**, **12-month** maintenance (weekly daily-build rollup + GitHub upkeep per §1.5). **Developer events out of scope** (§1.3).

**Author:** Hashclaw.AI · **Champion:** Nguyan Vinh (**@v9n**) · **Label:** `daml-tooling` ([closed list](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md))

**Funding:** **200,000 CC** total — **M1 30,000 · M2 20,000 · M3 30,000 · M4 120,000** (M4 = **12 × 10,000 CC**; **CC release** **60,000 + 60,000** after maintenance **month 1** and **month 6** acceptance per §6.2). **M3** sub-bands: §6.3.

---

## Checklist (PR template)

- [x] Proposal file under `/proposals/` (`open-canton-edu.md`)
- [x] Milestones and funding amounts defined
- [x] Acceptance criteria included
- [x] Alignment with Canton priorities described

---

## Proposal cross-reference

| Topic | Section |
|------|---------|
| Problem & ecosystem value | §1.1 |
| Verifiable deliverables | §1.5, **`eval-log.md`**, §4–§5 |
| Timelines | §4 |
| Open-source outputs | **Open-source and reusable outputs** |
| Technical capability | **Evidence** |
| Adoption | **Adoption and distribution plan** |

---

## Notes for reviewers

- **Human gate:** `guardrails.md` + §5 — no unsupervised agent merge to `main`.
- **M3:** **≥6** `agentic:true` + **≥4** `onchain:true` in **`m3-generation-units.md`**; **`eval-log.md` ≥10** scenarios.
- **§1.5:** Unit shapes (news, research, video, glossary/Learn); GitHub routine maintenance → **M4 log only**, not **8**/**18** manifests.
- **Champion @v9n:** **≥4** spot-checks on agent-assisted generation PRs.
