## Development Fund Proposal

**Author:** Hashclaw.AI  
**Status:** Draft  
**Created:** 2026-04-11  
**Suggested SIG (for reviewers):** Application developers / developer-experience adjacent (documentation, examples, training)  
**Label:** daml-tooling  
*(Closest single label in the [proposal template](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md); this grant focuses on **open education**, **multilingual reach**, and **in-person or hybrid developer events** in Asia—not protocol changes.)*

**Champion:** Nguyan Vinh  
*(Add GitHub handle / affiliation in the PR thread if not already public.)*

---

## Abstract

**Open Canton Edu** ([HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) is an independent, open-source education hub for Canton Network (EN/ZH today), with explicit non-official positioning and links to official documentation.

This proposal requests **Canton Coin (CC)** to **grow an Asia-Pacific developer community** around that hub: **(1)** a **production-grade site launch** milestone, **(2)** **multilingual** support including an **i18n helper with separate pipelines for Japanese (`ja`) and Korean (`ko`)** (key coverage, CI/docs per locale—not a single blended “Asian” check), **(3)** **at least two (2) developer salons / side events** (边会-style: technical, educational, non-commercial) in the region, and **(4)** **documented ongoing maintenance** with public quarterly updates. Deliverables are **objectively verifiable** (merged repo artifacts, published event pages, recap docs).

---

## 1. Objective and scope

### 1.1 Problem and ecosystem value

| Dimension | Problem | Ecosystem value |
|-----------|---------|-----------------|
| **Asia-Pacific onboarding** | Time zones and languages differ from US/EU defaults; many builders first encounter Canton through **fragmented** English-only or ad-hoc chat. | A **neutral, open hub** plus **local-language surfaces** and **live events** lowers friction to **official docs** and **CIPs**. |
| **Trust** | Unofficial education can be mistaken for “official.” | Hardened **disclaimers**, **verify-at-source** patterns, and **transparent** funding credit. |
| **Sustainability** | Volunteer sites stall after launch. | A **12-month maintenance SLA** with measurable merge cadence keeps the hub **current**. |

### 1.2 In scope

- **M1 — Site launch:** Production readiness (see §4): disclaimers, performance/accessibility smoke, deploy reliability, **launch announcement** + baseline metrics.  
- **M2 — Multilingual:** **i18n helper** (docs + scripts) with **distinct support for Japanese (`ja`) and Korean (`ko`)**: separate commands or config targets (e.g. `i18n:check:ja` / `i18n:check:ko`), **locale-specific** contributor notes (typography, length, tone placeholders), and **independent** missing-key / parity reports per locale. **EN + ZH** remain canonical for parity checks. **Ship minimum viable UI** for **both** `ja` and `ko` on the **same agreed route set** (home + nav + **Learn** entry minimum); partial keys allowed only if listed in `docs/i18n/gaps-ja.md` and `docs/i18n/gaps-ko.md` with remediation plan.  
- **M3 — Events:** **≥2** **developer salons** (边会): technical/educational, **non-commercial**, agenda aligned with **official learning resources**; **APAC-friendly** timing; in-person **or** hybrid **or** fully online if travel constraints—**each** with public agenda + **CC-BY** recap in-repo.  
- **M4 — Maintenance:** **12 months** from M1 acceptance: documented **monthly** content/engineering cadence (min. **≥10** maintenance PRs merged **or** equivalent documented batch releases), **≥4** quarterly public update posts (forum/Discord rules respected), **`docs/grants/final-report.md`**.

### 1.3 Out of scope (explicit)

- **Not** protocol, node, or synchronizer engineering. **Not** custody, trading, or token sales.  
- **Not** implying Canton Foundation / Digital Asset / Canton Network **endorsement**.  
- **Not** paid “pay-to-attend” training; events are **community / educational** (sponsorship transparency in recap if any).

### 1.4 Optional future phase (not in this funding ask)

Video course series, DAML AI-assist MVP, and deep agent refactors may be proposed **separately** if this grant succeeds—keeps scope **auditable** against the four milestones below.

---

## 2. Technical approach

| Workstream | Approach | Verifiable outputs |
|------------|----------|---------------------|
| **Site** | Astro static site, `src/i18n/translations.ts`, GitHub Actions → Pages; open `LICENSE`. | Tag + CI green + live URL in milestone note. |
| **Launch (M1)** | Checklist: headers, disclaimer copy, broken-link sweep, Lighthouse or equivalent report archived in `docs/grants/m1-launch/`. | Checklist MD + report artifacts on `main`. |
| **i18n (M2)** | Canonical `en` (or `zh`) key set; **per-locale** checks for **`ja`** and **`ko`**; `docs/i18n.md` + `docs/i18n/ja.md` + `docs/i18n/ko.md`; CI jobs or npm scripts **invoked separately** per locale so Japanese and Korean do not share a single ambiguous report. | Helper merged + **both** `ja` and `ko` route bundles + **two** parity reports (`i18n-report-ja.*`, `i18n-report-ko.*`). |
| **Events (M3)** | Public RSVP link (Luma / Google Form / GitHub Discussion—**no PII in repo**); agenda `.md` under `docs/grants/events/<slug>/`; photos/slides only with **speaker consent**; recap CC-BY. | **2** event folders + 2 recap files + announcement URLs. |
| **Maintenance (M4)** | `MAINTAINERS.md`, `docs/sustainability.md`, monthly merge log `docs/grants/maintenance-log.md`. | Log + PR count + quarterly links. |

**i18n helper — Japanese (`ja`) vs Korean (`ko`) (explicit split)**

- **Japanese (`ja`):** Missing-key and **orphan-key** diffs against canonical; optional **line-length / wrapping** hints for UI strings; glossary hook for repeated Canton terms (documented, not normative translations).  
- **Korean (`ko`):** **Separate** script entrypoint and report file from `ja` (no shared “CJK” bucket); notes on **formal `요`/`습니다` baseline** for UI copy and **postposition length** sensitivity in narrow layouts.  
- **Shared:** Single source of truth for keys in repo; **fail-closed** CI (or documented manual gate) if either locale falls below agreed coverage threshold for shipped routes.

**Backward compatibility:** *No Canton protocol / node / SDK changes.*

---

## 3. Architectural alignment

- **Developer experience & training** — per [Development Fund Proposal Review Process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).  
- **CIP / official docs literacy** — site links to [canton-foundation/cips](https://github.com/canton-foundation/cips) and official docs; events **must** cite primary reading.  
- **Program fit** — [Canton Development Fund](https://github.com/canton-foundation/canton-dev-fund): public good, transparent milestones, CC-denominated reporting (**CIP-0082**, **CIP-0100** as context).

---

## 4. Milestones and deliverables

### Milestone 1 — Site launch & production readiness (Week 8)

- **Deliverables:** `docs/grants/m1-launch/checklist.md` (all items checked); `docs/grants/m1-launch/lighthouse.pdf` or HTML export; **link sweep** summary (`m1-links.md`); **public launch post** URL (forum / X / Discord announcement—**one** minimum); `docs/grants/m1-traffic.md` baseline methodology.  
- **Verification:** Git tag `milestone-m1` (or release) + merged paths on `main`.

### Milestone 2 — Multilingual support & i18n helper (`ja` + `ko`) (Week 18)

- **Deliverables:**  
  - `docs/i18n.md` plus **`docs/i18n/ja.md`** and **`docs/i18n/ko.md`** (contributor + reviewer guidance).  
  - **i18n helper** implementing **separate** checks for **Japanese** and **Korean** (distinct CLI flags or config keys; **two** generated reports on `main`).  
  - **Shipped UI** for **`ja`** and **`ko`** each on: home + nav + **Learn** entry (minimum); gaps documented in **`docs/i18n/gaps-ja.md`** / **`docs/i18n/gaps-ko.md`** if any keys deferred.  
  - EN/ZH regression-free per CI.  
- **Verification:** CI logs show **both** `ja` and `ko` checks executed; staging or production URLs for `/ja/...` and `/ko/...` routes **or** locale switch behavior documented in milestone note (exact URL pattern follows repo routing at ship time).

### Milestone 3 — Asia-Pacific developer salons (**≥2** events) (Week 30)

- **Deliverables:** **Two** directories `docs/grants/events/<event-slug>/` each containing: `agenda.md`, `announcement-url.txt`, `recap.md` (CC-BY), optional `slides/` only with license file if redistributable. **≥20** unique participants **combined** (RSVP aggregate documented in recap—**no PII in-repo**; optional screenshot/export kept **out of repo** if needed for verification).  
- **Verification:** Two recap URLs or paths; Champion attestation in PR thread acceptable.

### Milestone 4 — Ongoing maintenance & annual close-out (Month 12 from M1)

- **Deliverables:** `docs/grants/maintenance-log.md` with **≥10** documented maintenance cycles; **≥4** quarterly update links; `docs/grants/final-report.md` (metrics, events outcomes, lessons).  
- **Verification:** Merged files + link list.

---

## 5. Acceptance criteria

1. **M1:** All §4 M1 files on `main`; live site matches disclaimer requirements; launch URL valid.  
2. **M2:** i18n helper merged with **separate `ja` and `ko` validation**; **both** locales meet agreed route list (or documented gaps files with plan); EN/ZH CI passes.  
3. **M3:** **≥2** events; each has agenda + announcement + recap; **combined RSVP ≥20** documented **without** storing personal data in-repo.  
4. **M4:** Maintenance log + 4 quarterly posts + final report.  
5. **No false authority** throughout.  
6. **Public good:** repo public; event materials **CC-BY** unless speaker IP requires redaction (then recap text-only).

---

## 6. Funding request and milestone breakdown

### 6.1 Is **120,000 CC** “usual”?

The [canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund) repository **does not publish** a typical approved grant size or median. **Amounts are Committee decisions** and must be **justified by deliverables, risk, and comparables** (if the Committee shares benchmarks).

**120,000 CC** here is an **ask**, not a guarantee. It is **defensible** if line items reflect: **part-time maintainer/editor**, **translation + professional or community review** for **both Japanese and Korean** surfaces, **two quality events** (venue or A/V, travel within Asia, recordings, volunteer stipends **if allowed** under program rules), and **12 months** of documented maintenance. If the Committee prefers a **smaller first tranche**, the same milestones can be **re-priced** (e.g. fewer travel events → more online salons).

### 6.2 Requested CC (illustrative split — **sum = 120,000 CC**)

| Milestone | CC | Rationale (high level) |
|-----------|-----|-------------------------|
| M1 — Site launch | 18,000 | Launch QA, link sweep, analytics setup, announcement pack. |
| M2 — Multilingual + i18n (`ja` + `ko`) | 32,000 | i18n engineering + **separate `ja` / `ko` helper paths** + **review** for both locales’ shipped strings. |
| M3 — **≥2** developer events | 45,000 | APAC logistics (hybrid/in-person or high-quality online), A/V, recap editing, **no alcohol/marketing fluff**. |
| M4 — 12-month maintenance | 25,000 | Monthly cadence + quarterly posts + final report. |
| **Total** | **120,000** | |

**Payment:** Per milestone **acceptance** against §5 (Committee process per program README). **>6 months** → **6-month re-evaluation** for CC volatility and any **descope** (e.g. second event fully online to save travel).

---

## Adoption and distribution plan

| Channel | Action |
|---------|--------|
| **Asia-Pacific** | Events and site updates promoted in **English + Chinese + Japanese + Korean** (as shipped); times **APAC-evening** friendly. |
| **Official-adjacent** | Every event recap links **official docs first**; CIP links for technical claims. |
| **Repository** | Event materials + maintenance log = **reuse** for other chapters. |
| **Foundation** | Co-marketing when offered (newsletter / social). |

---

## Evidence of technical capability

- Shipped stack: [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu) — Astro, bilingual content, GitHub Actions.  
- **Live site** URL cited at submission.  
- Maintainer experience landing large `translations.ts` PRs with parity.

---

## Open-source and reusable outputs

| Output | License |
|--------|---------|
| Site | Repo `LICENSE` |
| Event agendas & recaps | **CC-BY 4.0** (default) |
| i18n scripts | Same as repo |

---

## Co-Marketing

- Milestone notes suitable for Foundation channels.  
- **Canton Development Fund** credit in contribute / about for grant period (wording per brand guidance).

---

## Rationale (summary)

- **Focused ask:** Launch + language + **real-world Asia dev community** touchpoints + **sustained maintenance** — all **easy to verify**.  
- **Why CC:** Converts volunteer time into **accountable** community infrastructure aligned with the fund’s **public-good** mission.

---

## References

- [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- **CIP-0082**, **CIP-0100**  
- **grants-discuss@lists.sync.global** · **dev-fund@canton.foundation**
