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

This proposal requests **Canton Coin (CC)** to deepen **three technical tracks**—**(1) information aggregation** (allow-listed sources, dedup, **daily** scheduled rebuild/deploy within ToS/rate limits), **(2) Canton education content generation** (structured, **human-reviewed** drafts assisted by tooling/AI, **primary-source links**), and **(3) analysis using Canton-related on-chain or public-indexer data** (explorer/API-backed metrics, **reproducible** fetch or frozen snapshots at build time, **explicit methodology**—**not** official network statistics). Milestones also cover **multilingual** **`ja`/`ko`** i18n, a **production-grade launch** baseline, and **12 months** of **documented maintenance** plus quarterly public updates. **Developer-community event series are out of scope** (see §1.3). Deliverables are **objectively verifiable** in the public repository (including **manifests** in §1.5).

---

## 1. Objective and scope

### 1.1 Problem and ecosystem value

| Dimension | Problem | Ecosystem value |
|-----------|---------|-----------------|
| **Signal vs noise** | Official and community Canton signals are **scattered** (CIPs, forums, blogs, APIs); learners lack a **single neutral index** that still **points upstream**. | **Aggregation** with transparent sources reduces duplicate hunting and improves **CIP / doc literacy**. |
| **Education throughput** | Turning raw updates into **structured explainers** (EN/ZH, later JA/KO) is **labor-intensive**; quality drops without checklists. | A **repeatable generation + review** pipeline produces **consistent** educational snippets without posing as authoritative specs. |
| **Trust** | Unofficial summaries can read “official.” | **Disclaimers**, **verify-at-source** links, and **Development Fund** credit. |
| **Sustainability** | Aggregators rot when feeds break. | **12-month maintenance SLA**, **daily** automated rebuild where configured, monitoring, and documented runbooks. |
| **On-chain / indexer literacy** | Learners see headlines but not **how** to relate claims to **public explorer or API data**. | **Reproducible** on-chain or indexer-backed figures and **methodology** improve critical reading—**always** labelled as third-party index data, not Canton Foundation truth. |

### 1.2 In scope

- **M1 — Site launch & IA for aggregation:** Production readiness (§4): disclaimers, performance/accessibility smoke, deploy reliability, **information architecture** notes for which surfaces are **aggregated vs hand-authored**, **launch announcement** + baseline metrics.  
- **M2 — Multilingual:** **i18n helper** (docs + scripts) with **distinct `ja` and `ko`** checks (e.g. `i18n:check:ja` / `i18n:check:ko`), `docs/i18n.md` + `docs/i18n/ja.md` + `docs/i18n/ko.md`, **two** parity reports; **ship** `ja` + `ko` UI on home + nav + **Learn** entry (minimum) or documented **`gaps-ja.md` / `gaps-ko.md`**.  
- **M3 — Aggregation, daily refresh, education generation & on-chain analysis:** **Aggregation + daily site refresh:** `docs/aggregation/sources.md`, `docs/aggregation/runbook.md`, **`docs/operations/daily-update.md`** tying **≥1×/calendar-day** scheduled **GitHub Actions** full build + deploy to refresh allow-listed feeds and **on-chain snapshot** jobs (queue skew documented—aligned with existing **~20:00 CST (GMT+8)** cadence in-repo). **≥8** **aggregation integration PRs** counted only via **`docs/grants/m3-aggregation-prs.md`** (see §1.5). **Generation:** `docs/content-generation/workflow.md`, reviewer checklist, **`docs/grants/m3-generation-units.md`** listing **≥18** **education content units** (§1.5 definition), each with **≥1 canonical URL**; **≥4** of those **18** must **incorporate on-chain/indexer metrics** with **`docs/onchain/methodology.md`** + **`docs/onchain/sources.md`**. No narrative ship without **maintainer** approval per §1.5.  
- **M4 — Maintenance:** **12 months** from M1: **≥10** maintenance PRs (or batched equivalents), **≥4** quarterly public update posts, `docs/grants/maintenance-log.md` including **weekly** rollup of **daily** build success/failure (link to Actions), and `docs/grants/final-report.md` covering **aggregation**, **daily refresh reliability**, **generation quality**, and **on-chain analysis** outcomes.

### 1.3 Out of scope (explicit)

- **Not** protocol, node, or synchronizer engineering. **Not** custody, trading, or token sales.  
- **Not** implying Canton Foundation / Digital Asset / Canton Network **endorsement**.  
- **Not in this proposal:** **Developer-community event programs** (meetups, salons, conferences, travel budgets, RSVP campaigns, or **Canton Foundation–coordinated** physical/hybrid event series). Those may be a **separate** initiative if desired later.  
- **Not** fully automated “write production DAML” systems; generation stays **educational**, **source-linked**, and **human-gated**.  
- **Not** operating a **validator**, **not** using **non-public** chain or participant data; on-chain work uses **public explorer/API** endpoints only, per **`docs/onchain/sources.md`**.

### 1.4 Optional future phase (not in this funding ask)

In-person or hybrid **community events**, long-form video curricula, and **DAML AI-assist MVP** tooling may be proposed **separately**.

### 1.5 Definitions & counting rules (clarity for reviewers)

**Education content unit** (counts toward **≥18** only when listed in **`docs/grants/m3-generation-units.md`** *after* merge):  
- One coherent learning artifact: Learn-path blurb, glossary entry, news digest expansion, or short explainer **embedded in the shipped site** (typically `translations.ts` or an agreed `docs/education/` page).  
- **English body ≥90 characters** (excluding URLs) **or** equivalent substantive ZH copy in the same row.  
- **≥1 canonical primary-source URL** per shipped language (defer ZH in same milestone if documented in the manifest row).  
- **≥4** of the **18** units must **include at least one chart, table, or numeric call-out** derived from **allow-listed explorer/API** data defined in **`docs/onchain/sources.md`**, with interpretation tied to **`docs/onchain/methodology.md`** (indexer lag, reorgs disclaimer, non-official status).

**Aggregation integration PR** (counts toward **≥8** only when listed in **`docs/grants/m3-aggregation-prs.md`**): merged PR whose **primary diff** is confined to allow-listed globs in **`docs/aggregation/sources.md`** (e.g. `scripts/**`, `.github/workflows/**`, `docs/aggregation/**`, designated `public/generated/**` or `src/data/**`). **≤2** PRs may include **trivial** `translations.ts` label-only changes if flagged `aggregation+labels` in the manifest; they count toward **8**, **not** toward **18**, unless a **separate** generation-unit row is added.

**Double-count rule:** one merge line may not increment both counts unless it matches the **`aggregation+labels`** exception above and **adds** a distinct generation-unit row.

**Reviewer sign-off:** **`MAINTAINERS.md`** names **≥2** individuals with merge rights for **generation** PRs; **Champion** performs **≥4** spot-checks of merged generation PRs across the grant (short notes in the milestone PR thread or `docs/grants/champion-spotchecks.md`).

---

## 2. Technical approach

| Workstream | Approach | Verifiable outputs |
|------------|----------|---------------------|
| **Site** | Astro static site, `src/i18n/translations.ts`, GitHub Actions → Pages; open `LICENSE`. | Tag + CI green + live URL in milestone note. |
| **Launch (M1)** | Checklist + link sweep + **IA doc** `docs/grants/m1-aggregation-ia.md` listing which pages are **aggregated feeds** vs static narrative; stub **`docs/operations/daily-update.md`** pointing to Actions schedule. | Artifacts under `docs/grants/m1-launch/` + IA + daily-update stub on `main`. |
| **i18n (M2)** | Per-locale **`ja` / `ko`** checks; reports `i18n-report-ja.*`, `i18n-report-ko.*`. | Helper + routes + reports merged. |
| **Aggregation + daily refresh (M3a)** | Allow-listed HTTP/RSS/mail-public sources; rate limits; **daily** workflow refresh in CI; normalize to typed entries; fail-soft with **uploaded** CI logs on failure. | `docs/aggregation/runbook.md` + `docs/operations/daily-update.md` + **≥8** PRs listed in **`m3-aggregation-prs.md`**. |
| **Education generation (M3b)** | Templates + optional LLM/editor assist → PRs with checklist + **manifest** `m3-generation-units.md`. | `docs/content-generation/workflow.md` + **≥18** manifest rows. |
| **On-chain analysis (M3c)** | Read-only calls to **public** explorer/API endpoints in `docs/onchain/sources.md`; snapshot at build; disclaimers. | `docs/onchain/methodology.md` + **≥4** units among the 18 with on-chain/indexer sections + frozen artifact paths. |
| **Maintenance (M4)** | `MAINTAINERS.md`, `docs/sustainability.md`, `docs/grants/maintenance-log.md` with **weekly** digest of **daily** build health. | Log + quarterly links + final report. |

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

- **Deliverables:** `docs/grants/m1-launch/checklist.md`; Lighthouse or equivalent export; `m1-links.md`; **`docs/grants/m1-aggregation-ia.md`**; **`docs/operations/daily-update.md`** (stub linking Actions schedule for **daily** rebuild); public launch post URL; `docs/grants/m1-traffic.md` baseline.  
- **Verification:** Tag `milestone-m1` + paths on `main`.

### Milestone 2 — Multilingual support & i18n helper (`ja` + `ko`) (Week 18)

- **Deliverables:** `docs/i18n.md`, `docs/i18n/ja.md`, `docs/i18n/ko.md`; helper + **two** reports; shipped **`ja`/`ko`** routes (or gap files + plan); EN/ZH CI clean.  
- **Verification:** CI logs + URLs in milestone note.

### Milestone 3 — Aggregation, daily refresh, education generation & on-chain analysis (Week 32)

- **Aggregation + daily refresh:** `docs/aggregation/sources.md`, `docs/aggregation/runbook.md`, completed **`docs/operations/daily-update.md`** (cron, secrets policy **none** or GitHub-only, failure alerting path); **≥8** PRs recorded in **`docs/grants/m3-aggregation-prs.md`**; evidence of **≥30 consecutive calendar days** of scheduled runs with **≥95%** success (documented in milestone note—exclude GitHub-wide outages if noted).  
- **On-chain analysis:** `docs/onchain/sources.md` + **`docs/onchain/methodology.md`** (lag, definitions, “not official stats”); build-time or daily snapshot scripts producing **versioned** outputs under agreed paths.  
- **Generation:** `docs/content-generation/workflow.md` + checklist; **`docs/grants/m3-generation-units.md`** with **≥18** rows meeting §1.5; **≥4** rows flagged **`onchain:true`** with linked artifacts.  
- **Verification:** Manifest row counts; spot-check **3** random generation rows + **all 4** `onchain:true` rows for methodology + source URLs; Champion spot-check log **≥4** PRs referenced.

### Milestone 4 — Ongoing maintenance & annual close-out (Month 12 from M1)

- **Deliverables:** `docs/grants/maintenance-log.md` (**≥10** editorial/engineering cycles **plus** **≥48 weekly** one-line summaries of **daily** build health—**~1 per week** over the grant), **≥4** quarterly update links, `docs/grants/final-report.md` (**daily** refresh reliability, **aggregation** error budgets, **generation** throughput, **on-chain** section with lessons).  
- **Verification:** Merged files + links.

---

## 5. Acceptance criteria

1. **M1:** All §4 M1 artifacts on `main` (including **`docs/operations/daily-update.md`** stub); disclaimers accurate; **IA doc** lists aggregation boundaries.  
2. **M2:** Separate **`ja`/`ko` validation**; shipped routes or documented gaps + plan.  
3. **M3:** **`m3-aggregation-prs.md`** lists **≥8** qualifying PRs; **`m3-generation-units.md`** lists **≥18** rows meeting §1.5 with **≥4** `onchain:true`; **daily** workflow documented and **≥30** consecutive days **≥95%** green in note; **no** data source outside **`docs/aggregation/sources.md`** / **`docs/onchain/sources.md`** allow lists without Champion amendment; **Champion** **≥4** spot-checks recorded.  
4. **M4:** Maintenance log (including **weekly daily-build** rollup) + quarterly posts + final report.  
5. **No false authority** throughout.  
6. **Public good:** repo public; new prose defaults **CC-BY 4.0** where not otherwise constrained by third-party quotes.

---

## 6. Funding request and milestone breakdown

### 6.1 Is **120,000 CC** “usual”?

The [canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund) repository **does not publish** a typical approved grant size or median. **Amounts are Committee decisions.**

**120,000 CC** is an **ask**. It is **defensible** for **part-time engineering + editorial/fact-check**, **JA/KO review**, **aggregation + daily CI** infra, **public explorer/API** usage within ToS, **optional LLM/tooling costs** for **draft-only** generation under human review, **on-chain snapshot** compute, and **12 months** maintenance. **Re-price** with the Committee if scope shifts.

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
| Aggregation + **daily** CI engineering (scripts, workflows, monitoring) | 12,000–18,000 | Rate limits, retries, **per-day** job reliability |
| Human editorial + fact-check for generated units | 8,000–14,000 | **≥18** units × review depth |
| **On-chain / explorer API** usage & snapshot storage | 3,000–8,000 | Public indexers only; ToS-respecting quotas |
| Optional AI/tooling API (draft assist only) | 0–8,000 | **Zero** if Committee prefers no third-party LLM spend |
| Source hygiene / legal spot-check (quotes, logos) | 3,000–6,000 | Brand-kit compliance for on-site graphics |
| Contingency | remainder | Feed/API or upstream schema changes |

**Payment:** Per milestone **acceptance** against §5. **>6 months** → **6-month re-evaluation** for CC volatility.

---

## Adoption and distribution plan

| Channel | Action |
|---------|--------|
| **Site** | RSS/sitemap where applicable; **“Last refreshed”** on aggregated and **on-chain** sections; README badge or link to **Actions** daily workflow. |
| **Repository** | Runbooks + workflows reusable by forks. |
| **Public venues** | **≥4** quarterly posts (forum / X / Discord—**follow channel rules**) pointing **first** to official docs for normative claims; **≥1** post may highlight a **reproducible on-chain** chart with methodology link. |
| **Quantitative habit** | Maintenance log captures **weekly** **daily** build pass rate; final report states **median** days-to-recover from aggregation failure (if any). |
| **Foundation** | Co-marketing when offered; **no** event-series obligations in this grant. |

---

## Evidence of technical capability

- Shipped stack: [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu) — Astro, bilingual `translations.ts`, GitHub Actions.  
- **Live site** URL at submission.  
- **Precedent for scheduled refresh:** the repo already documents **daily ~20:00 CST (GMT+8)** full build + deploy and **build-time** jobs (e.g. chart generation from public market data)—see `src/i18n/translations.ts` **`home.buildSyncIntro`** / **`buildSyncItems`** and `npm run chart:build` / CI wiring; this grant **extends** that pattern to **allow-listed aggregation** and **on-chain snapshot** steps under the same **daily** gate.  
- Prior **incremental** `translations.ts` PRs show capacity to land **EN/ZH** parity at scale.

---

## Open-source and reusable outputs

| Output | License |
|--------|---------|
| Site + scripts | Repo `LICENSE` |
| Runbooks, workflow docs, templates, on-chain methodology | **CC-BY 4.0** (default) |
| i18n helper | Same as repo |

---

## Co-Marketing

- Milestone notes suitable for Foundation channels.  
- **Canton Development Fund** credit in contribute / about (wording per brand guidance).

---

## Rationale (summary)

- **Focused ask:** **Aggregation**, **daily** refresh, **on-chain/indexer-backed analysis**, **education generation**, **`ja`/`ko` i18n**, and **maintenance**—verification stays **manifest- and repo-centric** (no dev-event program in this tranche).  
- **Why CC:** Converts volunteer bandwidth into **measurable** public-good documentation infrastructure.

---

## References

- [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- **CIP-0082**, **CIP-0100**  
- **grants-discuss@lists.sync.global** · **dev-fund@canton.foundation**  
- [Canton brand & trademark use](https://www.canton.network/brand-kit-trademark-use)
