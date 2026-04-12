## Development Fund Proposal

**Author:** [GitHub handle / legal name — replace before submit]  
**Status:** Draft  
**Created:** 2026-04-11  
**Label:** daml-tooling  
*(Rationale: primary audience is builders learning DAML/Canton; closest single label in the template. Review process SIG alignment: **App Building and Developer Experience** — documentation, examples, training — per [Development Fund Proposal Review Process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).)*

**Champion:** Needs Champion  
*(External teams require a Champion per [canton-dev-fund README](https://github.com/canton-foundation/canton-dev-fund). Identify a Foundation member, contributor org, or community champion before or immediately after opening the PR.)*

---

## Abstract

**Open Canton Edu** is an independent, open-source, bilingual (English / Chinese) educational hub for the Canton Network: structured learning paths, CIP highlights, ecosystem directory, news and research indexes, and community entry points — with explicit disclaimers, primary-source linking, and transparent editor- and AI-assisted maintenance workflows (see [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)).

This proposal requests Development Fund support to **harden and scale** that public-good documentation surface: closer alignment with official docs and CIPs, measurable adoption and freshness metrics, accessibility and contributor onboarding, and a clear post-grant maintenance model. The outcome is **reduced developer friction** and improved **discoverability** of accurate Canton materials for global audiences.

---

## Specification

### 1. Objective

- **Problem:** Canton’s official documentation and ecosystem are broad and fast-moving; new developers and institutions lack a **neutral, bilingual, source-linked** on-ramp that stays current without duplicating authority of official channels.
- **Outcome:** A **CC-funded maintenance and expansion** phase that delivers verifiable improvements (content audit trails, milestone deliverables, adoption metrics) while preserving the site’s **non-official** stance and trademark-safe descriptive use of Canton marks.

### 2. Implementation Mechanics

- **Codebase:** Static site (Astro), single translation module for EN/ZH parity, GitHub Actions build/deploy, public repository under open license (per repo `LICENSE`).
- **Content workflow:** Human-in-the-loop updates; optional Cursor Skill for incremental scans; build-time and client-side integrations documented (e.g. price chart generation, public mail-list reads where applicable).
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

### Milestone 2: Developer onboarding & ecosystem discoverability

- **Estimated Delivery:** Week 20 (8 weeks after M1)  
- **Focus:** Add or expand **“first steps for builders”** section: DevNet/TestNet entry, official SDK links, wallet/explorer map cross-checks, optional **copy-paste command blocks** that mirror official quickstarts (no substitute for official tutorials).  
- **Deliverables / Value Metrics:**  
  - New or expanded **onboarding page(s)** shipped in EN+ZH.  
  - ≥ [M] new ecosystem or tooling entries validated with primary URLs (set M, e.g. 15).  
  - **External inbound links** or **GitHub stars/forks** trend snapshot (quantitative where possible).

### Milestone 3: Sustainability, governance handoff, and quarterly refresh SLA

- **Estimated Delivery:** Week 24  
- **Focus:** Document **post-grant ownership**: maintainer roster, review checklist for AI-assisted PRs, security disclosure path, and a **quarterly content refresh** runbook tied to CIP/news cadence.  
- **Deliverables / Value Metrics:**  
  - `MAINTAINERS.md` + `docs/sustainability.md` merged.  
  - One **public quarterly review** issue or discussion thread template executed once during the grant.  
  - Final **grant report** summarizing metrics, lessons, and recommended follow-up for the Committee.

---

## Acceptance Criteria

The Tech & Ops Committee can verify completion by:

- Each milestone’s **listed artifacts** merged to the default branch and tagged or cited by commit SHA in a short milestone note.  
- **EN/ZH parity** for all user-visible strings touched in scope (or explicit documented exceptions).  
- **No implied endorsement** language: site disclaimers remain accurate; no Canton Foundation / Digital Asset / Canton Network affiliation claims.  
- **Adoption-driven signals:** documented traffic or engagement metrics and at least one qualitative signal (e.g. maintainer or community feedback from Discord/forum thread).  
- **Public good:** repo remains open; no paywall on grant-funded materials.

---

## Funding

**Total Funding Request:** `[TOTAL] CC`  
*(Replace with a concrete CC amount consistent with scope and duration. Denomination and milestone-based release follow program norms in the [canton-dev-fund README](https://github.com/canton-foundation/canton-dev-fund).)*

### Payment Breakdown by Milestone

- Milestone 1 — Official-source alignment & learning-path hardening: `[M1] CC` upon committee acceptance  
- Milestone 2 — Developer onboarding & discoverability: `[M2] CC` upon committee acceptance  
- Milestone 3 — Sustainability & handoff: `[M3] CC` upon final acceptance  

*(Example structure only: e.g. 40% / 40% / 20% of total — adjust to Committee guidance.)*

### Volatility Stipulation

Project duration is **under 6 months** for the baseline plan above. If the Committee extends scope beyond six months, remaining milestones will be renegotiated per program rules for CC/USD volatility.

---

## Co-Marketing

Upon milestone releases, the implementing team will:

- Coordinate timing with the Foundation for **announcement** or **developer newsletter** inclusion where appropriate.  
- Provide a **short technical summary** (blog-shaped) suitable for cross-posting: what changed, how to verify against official docs, how to contribute.  
- Credit the **Canton Development Fund** visibly in the site’s contribute / about section for the grant period (wording subject to Foundation brand guidance).

---

## Motivation

Canton adoption depends on **credible, navigable entry points** for developers and institutions worldwide. A **bilingual**, **source-linked**, **open-source** hub reduces duplicate questions, surfaces CIPs and ecosystem projects, and complements official documentation without replacing it. Development Fund support converts volunteer bandwidth into **accountable deliverables**, **metrics**, and **sustainability** — consistent with the fund’s mission to strengthen the ecosystem through open development ([canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)).

---

## Rationale

- **Why this project:** The site already exists in public; funding **de-risks** focused editorial/engineering time for alignment and onboarding rather than starting from zero.  
- **Alternatives considered:** (1) Only informal wiki edits — lacks milestones and metrics; (2) Fully automated scraper site — risks accuracy and trademark sensitivity; (3) Commercial course paywall — conflicts with public-good requirement. The proposed path keeps **human review**, **official citations**, and **transparent AI assistance**.  
- **Why Development Fund:** Matches **common-good documentation and training**, milestone-based CC settlement, and transparent community-visible process as described in the program repository.

---

## References

- Program repository: [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- Governance context: **CIP-0082**, **CIP-0100** (cited in program README)  
- Community discussion (per program README): **grants-discuss@lists.sync.global**  
- Private submission questions: **dev-fund@canton.foundation**
