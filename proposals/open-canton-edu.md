## Development Fund Proposal

**Author:** Hashclaw.AI  
**Status:** Draft  
**Created:** 2026-04-11  
**Suggested SIG (for reviewers):** Application developers / developer-experience adjacent (documentation, examples, training)  
**Label:** daml-tooling  

*(The [proposal template](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md) requires **exactly one** label from a **closed list**. There is **no** `education`, `documentation`, or `community` label—those themes must be described in the body and SIG alignment instead.)*

**Full label enum (pick only one):** `dapp-integration`, `wallet-apps`, `attestor-pools-daos-multisig`, `defi-liquidity`, `party-portability-data-resilience`, `token-asset-standards`, `tokenomics`, `onchain-governance`, `daml-tooling`, `dar-app-management`, `canton-protocol-multi-synchronizer`, `canton-apis`, `node-deployment-operations`, `global-synchronizer-scaling`, `financial-workflows-composability`, `regulatory-compliance`.

**Reasonable alternatives to `daml-tooling` for this project (if you retune one paragraph of the narrative):**

| Label | When it fits Open Canton Edu |
|-------|------------------------------|
| **`dapp-integration`** | You foreground **ecosystem app surfaces**—wallets, explorers, DEXes—and the site as an **integration map** fed by aggregation pipelines. |
| **`canton-apis`** | You foreground **Ledger API / JSON API** examples and troubleshooting as **generated** learning aids alongside official docs. |
| **`dar-app-management`** | Usually **weak fit** unless milestones emphasize **DAR** packaging and distribution. |

**Recommendation:** keep **`daml-tooling`** for **Canton / DAML learning surfaces**, i18n for builder-facing UI, and **tooling for aggregation + educational content generation**; cite **SIG / Review Process** alignment (*App Building and Developer Experience — documentation, examples, training*) in the PR thread.

**Champion:** Nguyan Vinh  
*(Add GitHub handle / affiliation in the PR thread if not already public.)*

---

## Abstract

**Open Canton Edu** ([HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) is an independent, open-source hub for **Canton Network** learning material (EN/ZH today), with explicit **non-official** positioning and links to **official** documentation.

This proposal requests **Canton Coin (CC)** to deepen **two tracks**—**(1) information aggregation** (documented sources, dedup, build-time or scheduled refresh within ToS/rate limits) and **(2) Canton education content generation** (structured, **human-reviewed** drafts assisted by tooling/AI, every substantive block traceable to **primary sources**). Milestones also cover **(3)** **multilingual** delivery via an **i18n helper** with **separate `ja` and `ko` pipelines**, **(4)** a **production-grade launch** baseline, and **(5)** **12 months** of **documented maintenance** with quarterly public updates. **Developer-community event series, meetups, and Foundation-coordinated salons are explicitly out of scope** for this grant (see §1.3). Deliverables are **objectively verifiable** in the public repository.

---

## 1. Objective and scope

### 1.1 Problem and ecosystem value

| Dimension | Problem | Ecosystem value |
|-----------|---------|-----------------|
| **Signal vs noise** | Official and community Canton signals are **scattered** (CIPs, forums, blogs, APIs); learners lack a **single neutral index** that still **points upstream**. | **Aggregation** with transparent sources reduces duplicate hunting and improves **CIP / doc literacy**. |
| **Education throughput** | Turning raw updates into **structured explainers** (EN/ZH, later JA/KO) is **labor-intensive**; quality drops without checklists. | A **repeatable generation + review** pipeline produces **consistent** educational snippets without posing as authoritative specs. |
| **Trust** | Unofficial summaries can read “official.” | **Disclaimers**, **verify-at-source** links, and **Development Fund** credit. |
| **Sustainability** | Aggregators rot when feeds break. | **12-month maintenance SLA**, monitoring, and documented runbooks. |

### 1.2 In scope

- **M1 — Site launch & IA for aggregation:** Production readiness (§4): disclaimers, performance/accessibility smoke, deploy reliability, **information architecture** notes for which surfaces are **aggregated vs hand-authored**, **launch announcement** + baseline metrics.  
- **M2 — Multilingual:** **i18n helper** (docs + scripts) with **distinct `ja` and `ko`** checks (e.g. `i18n:check:ja` / `i18n:check:ko`), `docs/i18n.md` + `docs/i18n/ja.md` + `docs/i18n/ko.md`, **two** parity reports; **ship** `ja` + `ko` UI on home + nav + **Learn** entry (minimum) or documented **`gaps-ja.md` / `gaps-ko.md`**.  
- **M3 — Aggregation pipeline & education content generation:** **Aggregation:** documented **allow-list sources**, fetch/transform scripts (or CI steps), dedup/idempotency rules, `docs/aggregation/runbook.md`, and **≥8** merged integration PRs refreshing agreed surfaces (e.g. news/CIP-watch/ecosystem indices—exact list fixed at kickoff). **Generation:** `docs/content-generation/workflow.md` (human-in-the-loop, AI where appropriate), quality checklist, and **≥18** merged **education content units** (e.g. new/expanded learn blurbs, glossary entries, digest rows—each PR lists **≥1 canonical URL** per unit); no ship without reviewer sign-off in PR template.  
- **M4 — Maintenance:** **12 months** from M1: **≥10** maintenance PRs (or batched equivalents), **≥4** quarterly public update posts, `docs/grants/final-report.md` covering **aggregation reliability** and **generation quality** metrics.

### 1.3 Out of scope (explicit)

- **Not** protocol, node, or synchronizer engineering. **Not** custody, trading, or token sales.  
- **Not** implying Canton Foundation / Digital Asset / Canton Network **endorsement**.  
- **Not in this proposal:** **Developer-community event programs** (meetups, salons, conferences, travel budgets, RSVP campaigns, or **Canton Foundation–coordinated** physical/hybrid event series). Those may be a **separate** initiative if desired later.  
- **Not** fully automated “write production DAML” systems; generation stays **educational**, **source-linked**, and **human-gated**.

### 1.4 Optional future phase (not in this funding ask)

In-person or hybrid **community events**, long-form video curricula, and **DAML AI-assist MVP** tooling may be proposed **separately**.

---

## 2. Technical approach

| Workstream | Approach | Verifiable outputs |
|------------|----------|---------------------|
| **Site** | Astro static site, `src/i18n/translations.ts`, GitHub Actions → Pages; open `LICENSE`. | Tag + CI green + live URL in milestone note. |
| **Launch (M1)** | Checklist + link sweep + **IA doc** `docs/grants/m1-aggregation-ia.md` listing which pages are **aggregated feeds** vs static narrative. | Artifacts under `docs/grants/m1-launch/` + IA doc on `main`. |
| **i18n (M2)** | Per-locale **`ja` / `ko`** checks; reports `i18n-report-ja.*`, `i18n-report-ko.*`. | Helper + routes + reports merged. |
| **Aggregation (M3a)** | Allow-listed HTTP/RSS/mail-public sources; rate limits; normalize to typed entries; fail-soft with logged errors in CI artifact. | `docs/aggregation/runbook.md` + scripts + **≥8** merge PRs touching agreed data paths. |
| **Education generation (M3b)** | Templates + optional LLM/editor assist → **PR per batch** with reviewer checklist + **primary-source URL list**; EN/ZH parity for generated UI strings where applicable. | `docs/content-generation/workflow.md` + **≥18** merged units (counted in milestone note). |
| **Maintenance (M4)** | `MAINTAINERS.md`, `docs/sustainability.md`, `docs/grants/maintenance-log.md`. | Log + quarterly links + final report. |

**i18n helper — Japanese (`ja`) vs Korean (`ko`) (explicit split)**

- **Japanese (`ja`):** Missing-key / orphan-key diffs; optional line-length hints.  
- **Korean (`ko`):** **Separate** entrypoint and report from `ja`; formal-register UI baseline notes.  
- **Shared:** Fail-closed or documented manual gate under agreed coverage thresholds.

**Backward compatibility:** *No Canton protocol / node / SDK changes.*

---

## 3. Architectural alignment

- **Developer experience & training** — per [Development Fund Proposal Review Process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).  
- **CIP / official docs literacy** — [canton-foundation/cips](https://github.com/canton-foundation/cips) and official docs are **cited**, not replaced.  
- **Program fit** — [Canton Development Fund](https://github.com/canton-foundation/canton-dev-fund): public good, transparent milestones, CC reporting (**CIP-0082**, **CIP-0100** as context).

---

## 4. Milestones and deliverables

### Milestone 1 — Site launch, IA & production readiness (Week 8)

- **Deliverables:** `docs/grants/m1-launch/checklist.md`; Lighthouse or equivalent export; `m1-links.md`; **`docs/grants/m1-aggregation-ia.md`**; public launch post URL; `docs/grants/m1-traffic.md` baseline.  
- **Verification:** Tag `milestone-m1` + paths on `main`.

### Milestone 2 — Multilingual support & i18n helper (`ja` + `ko`) (Week 18)

- **Deliverables:** `docs/i18n.md`, `docs/i18n/ja.md`, `docs/i18n/ko.md`; helper + **two** reports; shipped **`ja`/`ko`** routes (or gap files + plan); EN/ZH CI clean.  
- **Verification:** CI logs + URLs in milestone note.

### Milestone 3 — Aggregation pipeline & education content generation (Week 32)

- **Aggregation deliverables:** `docs/aggregation/sources.md` (allow list), `docs/aggregation/runbook.md`, scripts/CI as designed, **≥8** merged PRs updating agreed aggregated surfaces.  
- **Generation deliverables:** `docs/content-generation/workflow.md` + checklist; **≥18** merged **education content units** with **primary-source URLs** recorded in PR bodies or `sources.md` sidecars.  
- **Verification:** Milestone note links PR numbers + counts; spot-check **3** random units for source links.

### Milestone 4 — Ongoing maintenance & annual close-out (Month 12 from M1)

- **Deliverables:** `docs/grants/maintenance-log.md` (**≥10** cycles), **≥4** quarterly update links, `docs/grants/final-report.md` (**aggregation uptime / error budgets**, **generation throughput**, lessons).  
- **Verification:** Merged files + links.

---

## 5. Acceptance criteria

1. **M1:** All §4 M1 artifacts on `main`; disclaimers accurate; **IA doc** lists aggregation boundaries.  
2. **M2:** Separate **`ja`/`ko` validation**; shipped routes or documented gaps + plan.  
3. **M3:** **≥8** aggregation PRs + **≥18** generation units merged; **every** generation PR lists **canonical sources**; **no** aggregation source outside **`sources.md` allow list** without Champion-approved amendment note.  
4. **M4:** Maintenance log + quarterly posts + final report.  
5. **No false authority** throughout.  
6. **Public good:** repo public; new prose defaults **CC-BY 4.0** where not otherwise constrained by third-party quotes.

---

## 6. Funding request and milestone breakdown

### 6.1 Is **120,000 CC** “usual”?

The [canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund) repository **does not publish** a typical approved grant size or median. **Amounts are Committee decisions.**

**120,000 CC** is an **ask**. It is **defensible** for **part-time engineering + editorial/fact-check**, **JA/KO review**, **aggregation infra** (APIs within vendor ToS), **optional LLM/tooling costs** for **draft-only** generation under human review, and **12 months** maintenance. **Re-price** with the Committee if scope shifts.

### 6.2 Requested CC (illustrative split — **sum = 120,000 CC**)

| Milestone | CC | Rationale (high level) |
|-----------|-----|-------------------------|
| M1 — Launch + aggregation IA | 18,000 | Hardening, IA, analytics baseline. |
| M2 — Multilingual + i18n (`ja` + `ko`) | 32,000 | Helper + **separate locale QA** + review. |
| M3 — Aggregation + education generation | 45,000 | Pipelines, scripts, **editorial time**, optional **tooling/API** spend (see §6.3). |
| M4 — 12-month maintenance | 25,000 | Ops, quarterly posts, final report. |
| **Total** | **120,000** | |

### 6.3 M3 budget — illustrative mapping (**aggregation + generation**)

*Illustrative only; **not binding** until kickoff sourcing plan is fixed.*

| Sub-item | CC (example band) | Notes |
|----------|-------------------|--------|
| Aggregation engineering (scripts, CI, monitoring) | 12,000–18,000 | Rate limits, retries, structured logs |
| Human editorial + fact-check for generated units | 10,000–18,000 | **≥18** units × review depth |
| Optional AI/tooling API (draft assist only) | 0–8,000 | **Zero** if Committee prefers no third-party LLM spend |
| Source hygiene / legal spot-check (quotes, logos) | 3,000–6,000 | Brand-kit compliance for on-site graphics |
| Contingency | remainder | Feed/API changes |

**Payment:** Per milestone **acceptance** against §5. **>6 months** → **6-month re-evaluation** for CC volatility.

---

## Adoption and distribution plan

| Channel | Action |
|---------|--------|
| **Site** | RSS/sitemap where applicable; clear **“last refreshed”** on aggregated sections. |
| **Repository** | Runbooks + workflows reusable by forks. |
| **Public venues** | **≥4** quarterly posts (forum / X / Discord—**follow channel rules**) pointing **first** to official docs for normative claims. |
| **Foundation** | Co-marketing when offered; **no** event-series obligations in this grant. |

---

## Evidence of technical capability

- Shipped stack: [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu) — Astro, bilingual `translations.ts`, GitHub Actions.  
- **Live site** URL at submission.  
- Prior **incremental** content and automation patterns (e.g. build-time charts, optional feed-based pages) demonstrate ability to extend **aggregation** safely.

---

## Open-source and reusable outputs

| Output | License |
|--------|---------|
| Site + scripts | Repo `LICENSE` |
| Runbooks, workflow docs, templates | **CC-BY 4.0** (default) |
| i18n helper | Same as repo |

---

## Co-Marketing

- Milestone notes suitable for Foundation channels.  
- **Canton Development Fund** credit in contribute / about (wording per brand guidance).

---

## Rationale (summary)

- **Focused ask:** **Aggregation + education generation + multilingual reach + maintenance**—no parallel **dev-community event** program in this tranche, reducing operational risk and keeping verification **repo-centric**.  
- **Why CC:** Converts volunteer bandwidth into **measurable** public-good documentation infrastructure.

---

## References

- [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- **CIP-0082**, **CIP-0100**  
- **grants-discuss@lists.sync.global** · **dev-fund@canton.foundation**  
- [Canton brand & trademark use](https://www.canton.network/brand-kit-trademark-use)
