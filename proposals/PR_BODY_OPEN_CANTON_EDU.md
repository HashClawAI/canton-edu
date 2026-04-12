<!-- Use this as the PR body when opening a PR on YOUR FORK of canton-dev-fund → base: canton-foundation/canton-dev-fund (not canton-edu). -->

## Development Fund Proposal Submission

**Proposal file (in this PR’s repo):** `proposals/open-canton-edu.md` — **target upstream:** [`canton-foundation/canton-dev-fund`](https://github.com/canton-foundation/canton-dev-fund).

---

## Summary

**Open Canton Edu** ([github.com/HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) requests **Canton Development Fund** support for **Agentic Education**—**maintainer-facing agents** (e.g. Cursor **Skills**, scripted flows) that **propose** aggregation refreshes, **draft** bilingual learning units, **preflight** i18n gaps, and **help interpret** public on-chain/indexer data—while **every merge to `main` stays human-reviewed** and **PR-based**.

Concrete deliverables include: **`docs/agentic-education/`** (`playbooks.md`, `guardrails.md`, **`eval-log.md` ≥10 scenarios**), **daily** Actions rebuild, **≥8** aggregation PRs (manifest), **≥18** generation units covering **news / 大事记**, **research**, **video** curation, and core Learn copy (**≥6** **`agentic: true`** + `playbook_id`, **≥4** **`onchain:true`**), **`ja`/`ko`** i18n, **12-month** maintenance (**weekly** daily-build rollups **+** routine **GitHub** upkeep per §1.5). **Developer events out of scope** (§1.3).

**Author:** Hashclaw.AI · **Champion:** Nguyan Vinh (**@v9n**) · **Label:** `daml-tooling` *(closed list [here](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md))*  

---

## Funding note (120,000 CC)

**120,000 CC** illustrative total; **§6.3** includes **agent playbook/eval** + optional **agent LLM/API** bands. **Committee calibration** applies.

---

## Checklist (PR template)

- [x] Proposal file under `/proposals/` (`open-canton-edu.md`)
- [x] Milestones and funding amounts defined
- [x] Acceptance criteria included
- [x] Alignment with Canton priorities described

---

## Mapping to “What makes a strong proposal”

| Item | Location in proposal |
|------|----------------------|
| Problem & ecosystem value | §1.1 |
| Objectively verifiable deliverables | §1.5 manifests, **`docs/agentic-education/eval-log.md`**, §4–§5 |
| Realistic timelines | §4 |
| Open-source outputs | **Open-source and reusable outputs** |
| Technical capability | **Evidence** (daily build + **`.cursor/skills/`** precedent) |
| Adoption / distribution | **Adoption and distribution plan** |

---

## Notes for Reviewers

- **Human gate:** **`guardrails.md`** + acceptance §5 — **no** unsupervised agent merge to `main`.  
- **M3:** **≥6** `agentic:true` + **≥4** `onchain:true` rows in **`m3-generation-units.md`**; **`eval-log.md` ≥10** scenarios.  
- **§1.5 unit shapes:** **news / 大事记**, **research guides** (link-out), **video cards** (curate + canonical URL), plus glossary/Learn blurbs; **GitHub routine maintenance** (deps, CI, triage) counts toward **M4 log only**, not the **8**/**18** manifests.  
- **Champion @v9n:** ≥4 spot-checks on **agent-assisted** generation PRs.
