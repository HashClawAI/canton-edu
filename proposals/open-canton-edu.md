## Development Fund Proposal

**Author:** Openclaw  
**Status:** Draft  
**Created:** 2026-04-11  
**Label:** daml-tooling  
*(Rationale: primary audience is builders learning DAML/Canton; closest single label in the template. Review process SIG alignment: **App Building and Developer Experience** — documentation, examples, training — per [Development Fund Proposal Review Process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).)*

**Champion:** Nguyan Vinh

---

## Abstract

**Open Canton Edu** is an independent, open-source, bilingual (English / Chinese) educational hub for the Canton Network: structured learning paths, CIP highlights, ecosystem directory, news and research indexes, and community entry points — with explicit disclaimers, primary-source linking, and transparent editor- and AI-assisted maintenance workflows (see [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)).

This proposal requests Development Fund support to **harden and scale** that public-good documentation surface: closer alignment with official docs and CIPs, measurable adoption and freshness metrics, accessibility and contributor onboarding, and a clear post-grant maintenance model — plus **(a)** an **i18n helper** and workflow to grow **multi-locale** coverage beyond EN/ZH, **(b)** a **refined, more general-purpose** AI agent / maintainer workflow (still human-in-the-loop) with clearer guardrails and reuse patterns, **(c)** **optional, feasibility-gated** **AI-assisted DAML development** tooling (scope fixed only after a documented spike; if infeasible, effort is reallocated per Committee guidance), and **(d)** **recorded, produced multilingual public tutorials** for Canton (video + captions/subtitles, chapter pages in-repo). The outcome is **reduced developer friction**, improved **discoverability**, and broader **global reach** without claiming official status.

---

## Specification

### 1. Objective

- **Problem:** Canton’s official documentation and ecosystem are broad and fast-moving; new developers and institutions lack a **neutral, bilingual, source-linked** on-ramp that stays current without duplicating authority of official channels.
- **Outcome:** A **CC-funded maintenance and expansion** phase that delivers verifiable improvements (content audit trails, milestone deliverables, adoption metrics, i18n infrastructure, tutorial assets, and gated DAML-assist R&D where justified) while preserving the site’s **non-official** stance and trademark-safe descriptive use of Canton marks.

### 2. Implementation Mechanics

- **Codebase:** Static site (Astro), translation module with EN/ZH parity today; GitHub Actions build/deploy; public repository under open license (per repo `LICENSE`).
- **i18n helper (planned):** Contributor-oriented tooling and docs to **add and validate locales** (e.g. key coverage checks, merge checklist, optional extraction/diff helpers — exact stack to be fixed in M2 design note) so the site can scale beyond two languages without silently drifting from source-of-truth strings.
- **Content workflow:** Human-in-the-loop updates; optional Cursor Skill / agent flows for incremental scans; build-time and client-side integrations documented (e.g. price chart generation, public mail-list reads where applicable).
- **General-purpose agent (planned):** Refactor and document maintainer **agent playbooks** so workflows are **less site-idiosyncratic** where safe (templates, guardrails, “do not claim official status” checks), without automating trademark or compliance judgments.
- **AI-assisted DAML tooling (conditional):** After a **time-boxed feasibility spike**, deliver an **MVP only if** complexity, safety, and maintenance burden meet thresholds agreed with the Champion/Committee (examples of MVP classes: documented editor integration patterns, snippet packs, or a thin CLI/MCP companion — **not** a substitute for official DAML/Canton docs). If the spike recommends **no-go**, publish the spike report and **reallocate** remaining budgeted effort to tutorials or i18n, as documented in the milestone note.
- **Multilingual public tutorials (planned):** Produce **openly licensed** lesson sets (e.g. screen recordings + edited chapters + **subtitles/captions** in at least EN and ZH, with a repeatable publishing pipeline on the static site).
- **Grant execution:** Milestone-gated deliverables merged to `main` with tagged releases or commit ranges referenced in each milestone report; public **milestone completion** summary in-repo (`docs/grants/` or proposal addendum).

### 3. Architectural Alignment

- Aligns with ecosystem priority **App Building and Developer Experience** (documentation, examples, training) per the [review process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).
- Reinforces **CIP literacy** (links to [canton-foundation/cips](https://github.com/canton-foundation/cips), discussion venues) without replacing official specs.
- Supports **open participation** and **transparent governance** narrative consistent with the [Canton Development Fund](https://github.com/canton-foundation/canton-dev-fund) program goals (public good, predictable process).

### 4. Backward Compatibility

*No backward compatibility impact on Canton protocol, nodes, or SDKs.* This work is a standalone static site and documentation layer.

---

## Milestones and Deliverables

### Milestone 1: Official-source alignment & learning-path hardening

- **Estimated Delivery:** Week 12 from grant start  
- **Focus:** Audit learning path and key pages against **primary official sources** (e.g. `canton.network`, DAML/Canton docs, whitepapers, forum links); fix stale links; add “verify at source” callouts where needed; EN/ZH parity for changed sections.  
- **Deliverables / Value Metrics:**  
  - Published **link audit report** (CSV or MD) with resolution status.  
  - ≥ [N] substantive content updates merged (set N before submit, e.g. 25).  
  - **Unique visitors** or **page-view** baseline + 8-week post-milestone report (privacy-respecting analytics; method documented).

### Milestone 2: Developer onboarding, ecosystem discoverability & i18n helper v1

- **Estimated Delivery:** Week 22 (10 weeks after M1)  
- **Focus:** Add or expand **“first steps for builders”** section: DevNet/TestNet entry, official SDK links, wallet/explorer map cross-checks, optional **copy-paste command blocks** that mirror official quickstarts (no substitute for official tutorials). Ship **i18n helper v1**: documented workflow + automation/scripts as needed so contributors can **add a new locale** with **key coverage / parity checks** against the canonical translation table.  
- **Deliverables / Value Metrics:**  
  - New or expanded **onboarding page(s)** shipped in EN+ZH.  
  - ≥ [M] new ecosystem or tooling entries validated with primary URLs (set M, e.g. 15).  
  - **i18n helper** merged (code + `docs/i18n.md` or equivalent) with a **pilot third locale** *or* a staged empty locale scaffold approved by Champion (choose one before grant start).  
  - **External inbound links** or **GitHub stars/forks** trend snapshot (quantitative where possible).

### Milestone 3: Sustainability, governance handoff, and quarterly refresh SLA

- **Estimated Delivery:** Week 28 (6 weeks after M2)  
- **Focus:** Document **post-grant ownership**: maintainer roster, review checklist for AI-assisted PRs, security disclosure path, and a **quarterly content refresh** runbook tied to CIP/news cadence. Include **tutorial production RACI** (roles, review steps, brand/disclaimer checklist).  
- **Deliverables / Value Metrics:**  
  - `MAINTAINERS.md` + `docs/sustainability.md` merged.  
  - One **public quarterly review** issue or discussion thread template executed once during the grant.  
  - **Interim grant narrative** (metrics + risks + planned M4–M6), *not* the final close-out (reserved for M6).

### Milestone 4: Multilingual public Canton tutorials

- **Estimated Delivery:** Week 38 (10 weeks after M3)  
- **Focus:** Record, edit, and publish a **multilingual public tutorial series** aligned with official sources (on-screen citations / description links). Minimum **EN + ZH** audio or subtitles; additional languages if i18n/locale pipeline supports without blocking release.  
- **Deliverables / Value Metrics:**  
  - ≥ [V] published lesson units (set V before submit, e.g. 6–10), each with: hosted video or embedded player decision documented, **subtitle/caption files** (e.g. SRT/VTT), and matching **static site chapter pages** in-repo.  
  - **Public license** statement for tutorial assets (e.g. CC-BY or project default — fixed before recording).  
  - **View counts or distribution metrics** methodology documented (privacy-respecting).

### Milestone 5: General-purpose maintainer Agent refinement

- **Estimated Delivery:** Week 44 (6 weeks after M4)  
- **Focus:** **Micro-tune** maintainer-facing agent flows for **generality and safety**: reusable templates, reduced hard-coded site trivia where inappropriate, explicit “verify official docs” steps, and lightweight regression guidance for common PR types.  
- **Deliverables / Value Metrics:**  
  - Updated Skill / agent docs merged; **before/after** maintainer checklist.  
  - Short **evaluation log** (e.g. N trial PR scenarios) showing failure modes and mitigations.

### Milestone 6: Feasibility-gated AI-assisted DAML tooling + final report

- **Estimated Delivery:** Week 50 (6 weeks after M5)  
- **Focus:** **Phase A — Spike (≤2 weeks within this milestone window):** document options for AI-assisted DAML development aids (editor patterns, snippets, MCP, etc.), security/review implications, and **go/no-go** recommendation. **Phase B — MVP only on go:** implement the agreed-narrow MVP; **on no-go:** execute **documented descope** and shift remaining hours to **tutorials or i18n** (per Champion + Committee note). **Final grant report** with full metrics, lessons, and maintenance handoff.  
- **Deliverables / Value Metrics:**  
  - `docs/daml-ai-assist-spike.md` with decision and, if MVP, link to repo paths and usage doc.  
  - Final **grant close-out report** for the Committee.

---

## Acceptance Criteria

The Tech & Ops Committee can verify completion by:

- Each milestone’s **listed artifacts** merged to the default branch and tagged or cited by commit SHA in a short milestone note.  
- **EN/ZH parity** for all user-visible strings touched in scope (or explicit documented exceptions); **additional locales** must meet the i18n helper’s documented completeness bar before ship.  
- **Tutorial acceptance:** for each lesson unit, subtitles/captions + in-repo chapter page + source-link policy satisfied.  
- **DAML-assist gate:** no MVP billing without spike **go** decision recorded; no-go path documented with substitute deliverables.  
- **No implied endorsement** language: site disclaimers remain accurate; no Canton Foundation / Digital Asset / Canton Network affiliation claims.  
- **Adoption-driven signals:** documented traffic or engagement metrics and at least one qualitative signal (e.g. maintainer or community feedback from Discord/forum thread).  
- **Public good:** repo remains open; no paywall on grant-funded materials.

---

## Funding

**Total Funding Request:** `[TOTAL] CC`  
*(Replace with a concrete CC amount consistent with scope and duration. Denomination and milestone-based release follow program norms in the [canton-dev-fund README](https://github.com/canton-foundation/canton-dev-fund).)*

### Payment Breakdown by Milestone

- Milestone 1 — Official-source alignment & learning-path hardening: `[M1] CC` upon committee acceptance  
- Milestone 2 — Developer onboarding, discoverability & i18n helper v1: `[M2] CC` upon committee acceptance  
- Milestone 3 — Sustainability, handoff & quarterly SLA: `[M3] CC` upon committee acceptance  
- Milestone 4 — Multilingual public Canton tutorials: `[M4] CC` upon committee acceptance  
- Milestone 5 — General-purpose maintainer Agent refinement: `[M5] CC` upon committee acceptance  
- Milestone 6 — DAML-assist spike/MVP (gated) + final report: `[M6] CC` upon final acceptance  

*(Replace placeholders; split may differ — e.g. heavier weight on M4 tutorials or M2 i18n — align with Committee guidance.)*

### Volatility Stipulation

Baseline schedule spans **more than six months** (~50 weeks). Per program norms, the grant is denominated in **fixed CC** and will require a **re-evaluation at the 6-month mark** (or as otherwise directed by the Committee) for any remaining milestones and for material CC/USD volatility, including possible **descope** of gated DAML-assist work in favor of tutorials/i18n.

---

## Co-Marketing

Upon milestone releases, the implementing team will:

- Coordinate timing with the Foundation for **announcement** or **developer newsletter** inclusion where appropriate.  
- Provide a **short technical summary** (blog-shaped) suitable for cross-posting: what changed, how to verify against official docs, how to contribute.  
- Credit the **Canton Development Fund** visibly in the site’s contribute / about section for the grant period (wording subject to Foundation brand guidance).

---

## Motivation

Canton adoption depends on **credible, navigable entry points** for developers and institutions worldwide. A **multilingual-capable**, **source-linked**, **open-source** hub — plus **public tutorials** and **maintainer tooling** (i18n helper, disciplined agent workflows, and **only-if-feasible** DAML assist) — reduces duplicate questions, surfaces CIPs and ecosystem projects, and complements official documentation without replacing it. Development Fund support converts volunteer bandwidth into **accountable deliverables**, **metrics**, and **sustainability** — consistent with the fund’s mission to strengthen the ecosystem through open development ([canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)).

---

## Rationale

- **Why this project:** The site already exists in public; funding **de-risks** focused editorial/engineering time for alignment, onboarding, **locale scale-out**, **tutorial production**, and **disciplined agent/tooling R&D** rather than starting from zero.  
- **Alternatives considered:** (1) Only informal wiki edits — lacks milestones and metrics; (2) Fully automated scraper site — risks accuracy and trademark sensitivity; (3) Commercial course paywall — conflicts with public-good requirement; (4) Unbounded “AI for DAML” scope — mitigated by **spike-gated MVP** and explicit no-go reallocation. The proposed path keeps **human review**, **official citations**, and **transparent AI assistance**.  
- **Why Development Fund:** Matches **common-good documentation and training**, milestone-based CC settlement, and transparent community-visible process as described in the program repository.

---

## References

- Program repository: [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- Governance context: **CIP-0082**, **CIP-0100** (cited in program README)  
- Community discussion (per program README): **grants-discuss@lists.sync.global**  
- Private submission questions: **dev-fund@canton.foundation**
