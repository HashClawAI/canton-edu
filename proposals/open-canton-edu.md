## Development Fund Proposal

**Author:** Openclaw  
**Status:** Draft  
**Created:** 2026-04-11  
**Suggested SIG (for reviewers):** Application developers / developer-experience adjacent (documentation, examples, training)  
**Label:** daml-tooling  
*(Closest single label in the [proposal template](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md); scope spans DAML/Canton learning surfaces, not core protocol changes.)*

**Champion:** Nguyan Vinh  
*(Add GitHub handle / affiliation in the PR thread if not already public.)*

---

## Abstract

**Open Canton Edu** ([HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) is an independent, open-source education hub (EN/ZH today) for Canton Network: learning paths, CIPs, ecosystem listings, news/research indexes, and explicit non-official / source-linked / AI-assisted maintenance disclosures.

This proposal requests **Canton Coin (CC)** funding for a **~50-week**, **six-milestone** program: documentation hardening, builder onboarding, **i18n helper v1**, sustainability runbooks, **multilingual public tutorials**, **maintainer-agent** refinement, and a **feasibility-gated** **AI-assisted DAML tooling** spike (MVP only on **go**). All outputs remain **open source** and **objectively verifiable** in the public repository.

---

## 1. Objective and scope

### 1.1 Problem and ecosystem value

| Dimension | Problem | Ecosystem value |
|-----------|---------|-----------------|
| **Discovery** | Official Canton and DAML material is extensive and fast-moving; newcomers lack a **single neutral on-ramp** that still **points to primary sources**. | Faster orientation → fewer duplicate basic questions in forums/Discord; higher **CIP and official-doc literacy**. |
| **Locale** | Many teams need **languages beyond EN/ZH**; ad-hoc translations drift from keys and disclaimers. | **i18n helper** + pilot locale lowers the cost of **correct, reviewable** translations. |
| **Trust** | Unofficial aggregators risk looking “official” or stale. | Hardened disclaimers, link audits, and **verify-at-source** patterns model **good citizenship** for the ecosystem. |
| **Builders** | DAML/Canton first deploy steps are easy to get wrong without a curated path. | Onboarding pages + **optional** gated dev aids reduce **time-to-first-successful-read** of official tutorials. |

### 1.2 In scope

- **Content:** Learning-path and high-traffic pages **audited** against official sources; stale links fixed; EN/ZH parity for touched UI strings.  
- **Onboarding:** “First steps for builders” expansion (DevNet/TestNet pointers, SDK links, wallet/explorer cross-checks).  
- **i18n:** Contributor **i18n helper v1** (scripts/docs) + **one pilot third locale** (partial nav + home acceptable if documented) **or** Champion-approved **empty locale scaffold**—choice **fixed at grant kickoff**.  
- **Operations:** `MAINTAINERS.md`, `docs/sustainability.md`, quarterly refresh runbook, tutorial **RACI**.  
- **Tutorials:** **Six (6)** published lesson units (see §4), EN+ZH subtitles minimum, in-repo chapter pages, **CC-BY 4.0** (or repo default if already compatible) for tutorial text/assets as documented before recording.  
- **Agent:** Maintainer Cursor Skill / agent docs **refined** for reuse + safety checklist + short **evaluation log**.  
- **DAML assist:** **Time-boxed spike** + **optional MVP** per go/no-go; **no-go** → documented descope + hours shifted to tutorials/i18n (per Champion note).

### 1.3 Out of scope (explicit)

- **Not** protocol changes, **not** synchronizer/Canton node patches, **not** custody or trading products.  
- **Not** claiming affiliation, endorsement, or trademark license from Canton Foundation, Digital Asset, or Canton Network participants.  
- **Not** replacing official docs; **not** hosting proprietary third-party content without permission.  
- **Not** shipping a broad “AI writes production DAML” product without spike approval—**M6 is gated**.

---

## 2. Technical approach

| Layer | Approach | Primary outputs (verifiable) |
|-------|----------|------------------------------|
| **Site** | Astro static site, content in `src/i18n/translations.ts`, GitHub Actions CI/build/deploy to GitHub Pages; public `LICENSE`. | Green CI on `main`, deploy artifacts, versioned commits per milestone. |
| **Quality** | Link crawler or manual audit → **published** `docs/grants/m1-link-audit.md` (or CSV) with resolution status; PRs reference official URLs. | Audit file + merged PR count. |
| **i18n** | Scripts (Node or similar) + `docs/i18n.md`: key coverage vs canonical locale, PR checklist; optional third-locale JSON/TS slice. | Helper merged + pilot locale or scaffold merged. |
| **Tutorials** | Script → edit → **SRT/VTT** (EN+ZH) → static chapter pages (Astro) → video hosted on neutral platform (e.g. YouTube **unlisted/public** per decision doc) with **description links** to official docs. | 6 lesson folders under `docs/tutorials/` or `src/pages/...` + caption files + `LICENSE` note for media. |
| **Agent** | `.cursor/skills/` docs: templates, “verify official” steps, reduced brittle copy-paste; optional eval scenarios in `docs/grants/agent-eval.md`. | Diff to Skill + eval log. |
| **DAML assist (M6)** | Spike doc: threat model (e.g. no exfiltration of private repos), UX scope, maintenance; MVP only if **go** (e.g. snippet pack + docs, **not** auto-deploy). | `docs/daml-ai-assist-spike.md` + optional `packages/…` or `tools/…` + README. |

**Backward compatibility:** *No impact on Canton protocol, nodes, or SDKs*—documentation and tooling in a separate repo only.

---

## 3. Architectural alignment

- **Ecosystem priority:** Aligns with **App Building and Developer Experience** — *documentation, examples, training* — per the [Development Fund Proposal Review Process](https://github.com/canton-foundation/canton-dev-fund/blob/main/Development%20Fund%20Proposal%20Review%20Process.md).  
- **CIP literacy:** Surfaces [canton-foundation/cips](https://github.com/canton-foundation/cips) and public discussion venues **by reference**; does not fork normative spec text.  
- **Governance narrative:** Supports **open participation** and **transparent process** consistent with [Canton Development Fund](https://github.com/canton-foundation/canton-dev-fund) goals (**CIP-0082**, **CIP-0100** as program context).  
- **Security posture:** Human review for substantive content; spike explicitly addresses **what the tool must not do** (e.g. no substitute for security review of user code).

---

## 4. Milestones and deliverables

**Quantified targets (replace only if Champion/Committee requests):** **≥20** substantive content PRs merged in M1 (each with official link justification in PR body or audit row); **≥12** new ecosystem/tooling rows with primary URLs in M2; **6** tutorial lesson units in M4.

### Milestone 1 — Official-source alignment & learning-path hardening (Week 12)

- **Deliverables:** `docs/grants/m1-link-audit.md` (or `.csv`) with **Resolved / Wontfix / Official change pending**; **≥20** merged content PRs meeting audit criteria; **baseline + 8-week** traffic methodology in `docs/grants/m1-traffic.md` (privacy-respecting, e.g. Pages analytics or self-hosted Plausible—**no** third-party PII sale).  
- **Objective verification:** File paths on `main` + PR list + optional git tag `milestone-m1`.

### Milestone 2 — Developer onboarding, discoverability & i18n helper v1 (Week 22)

- **Deliverables:** New/expanded **onboarding** routes EN+ZH; **≥12** ecosystem entries; **`docs/i18n.md` + helper scripts** merged; **pilot third locale** *or* **documented empty scaffold** (per §1.2 kickoff choice).  
- **Objective verification:** Lighthouse/Playwright optional smoke; i18n CI job if added; PR links.

### Milestone 3 — Sustainability, handoff & quarterly SLA (Week 28)

- **Deliverables:** `MAINTAINERS.md`, `docs/sustainability.md`, tutorial **RACI** appendix; **one** executed public quarterly review thread/issue template; `docs/grants/m3-interim-report.md`.  
- **Objective verification:** Merged files + link to GitHub Discussion or issue.

### Milestone 4 — Multilingual public Canton tutorials (Week 38)

- **Deliverables:** **6** lesson units: each includes **chapter page**, **EN + ZH** `.srt` or `.vtt`, **source citation** block, and **license** file or section; `docs/grants/m4-tutorial-hosting.md` (embed vs external).  
- **Objective verification:** Public URLs listed in milestone note; files on `main`.

### Milestone 5 — General-purpose maintainer Agent refinement (Week 44)

- **Deliverables:** Updated `.cursor/skills/**` + `docs/grants/agent-eval.md` with **≥5** scripted trial scenarios (input → expected guardrail).  
- **Objective verification:** Merged diff + eval doc.

### Milestone 6 — DAML-assist spike / optional MVP + final report (Week 50)

- **Deliverables:** `docs/daml-ai-assist-spike.md` (**go/no-go**); if **go**, narrow MVP + `README` usage; if **no-go**, `docs/grants/m6-descope.md` + substitute merges (tutorials/i18n) per Champion; **`docs/grants/final-report.md`**.  
- **Objective verification:** Spike doc mandatory; MVP paths only if **go**.

---

## 5. Acceptance criteria

The Tech & Ops Committee may treat milestone acceptance as **all** of:

1. **Artifacts on `main`:** Every deliverable in §4 exists at cited paths or PR numbers in `docs/grants/milestone-<n>-note.md`.  
2. **Parity:** EN/ZH for all **new** user-visible strings in scope; pilot locale meets **documented completeness bar** before marked “shipped.”  
3. **No false authority:** Footer / disclaimer strings remain accurate; no new implied endorsement.  
4. **Tutorials:** Each of 6 units has captions + chapter + license + official links.  
5. **DAML gate:** **No MVP payment claim** without a **go** decision recorded in spike doc; **no-go** has descope note + substitute merges.  
6. **Adoption signal:** At least **one** of: 8-week traffic delta vs M1 baseline, **≥1** inbound reference from a **public** ecosystem channel (forum/Discord/GitHub issue link), or **GitHub** star/fork delta documented—method in interim/final reports.  
7. **Public good:** Repo stays public; grant-funded tutorial assets remain under declared open license.

---

## 6. Funding request and milestone breakdown

**Total funding request (illustrative, Committee-calibrated):** **120,000 CC**

| Milestone | Payment (CC) | Trigger |
|-----------|--------------|---------|
| M1 — Alignment & audit | 15,000 | Committee acceptance of M1 note + §5 criteria |
| M2 — Onboarding & i18n v1 | 18,000 | Acceptance of M2 |
| M3 — Sustainability & SLA | 12,000 | Acceptance of M3 |
| M4 — Tutorials (6 units) | 35,000 | Acceptance of M4 |
| M5 — Agent refinement | 15,000 | Acceptance of M5 |
| M6 — DAML spike / optional MVP + final report | 25,000 | Final acceptance (spike always; MVP only if go) |

**Sum:** 120,000 CC. **Indicative only**—the proposer will adjust totals or per-milestone weights if the Committee benchmarks against comparable documentation grants.

**Volatility / duration:** Baseline **> 6 months**; per [program README](https://github.com/canton-foundation/canton-dev-fund), **re-evaluate at month 6** for remaining milestones and CC/USD volatility; **M6 DAML MVP** may be descoped in favor of M4/M2 work with written agreement.

---

## Adoption and distribution plan

| Channel | Action | Metric |
|---------|--------|--------|
| **Repository** | README + Releases/tags per milestone | Stars/forks, clone traffic (if available) |
| **Site** | “What’s new” or news row + contribute CTA | Pageviews methodology per M1 |
| **Community** | At least **quarterly** short post to a **public** venue (e.g. Canton Network Forum, relevant Discord **#dev** with mod rules respected) linking **official docs first** | Links captured in grant reports |
| **Foundation coordination** | Co-marketing § below | Newsletter / retweet when offered |
| **Tutorials** | Playlists + descriptions with **official links** | View counts as reported by host + documented caveats |

---

## Evidence of technical capability

- **Shipping history:** Public repo [HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu) with **Astro** static build, **bilingual** content module, and **GitHub Actions** deploy path.  
- **Live property:** Site deployed per repo README (e.g. custom domain / Pages—**verify live** at submission time).  
- **Automation already in use:** Build-time chart generation, documented **Cursor Skill** path under `.cursor/skills/`.  
- **Process:** Prior **incremental** content PRs demonstrate ability to land large `translations.ts` changes with EN/ZH parity.

*(If Champion provides a letter of support or org backing, attach in PR discussion.)*

---

## Open-source and reusable outputs

| Output | License / reuse |
|--------|-----------------|
| Site code | Repo `LICENSE` (unchanged unless upgraded with legal review) |
| Tutorial scripts / chapters | **CC-BY 4.0** text; screen recordings **CC-BY 4.0** unless B-roll requires otherwise (documented pre-M4) |
| i18n helper scripts | Same as repo; documented CLI for other Astro projects |
| Agent / Skill templates | Same as repo; intended fork reuse for **other** doc sites with disclaimer swap |

---

## Co-Marketing

- Coordinate **announcement** or developer **newsletter** with Canton Foundation when appropriate.  
- Publish **milestone technical notes** (what shipped, how to verify against official docs).  
- Credit **Canton Development Fund** in contribute/about section for the grant period (wording per Foundation brand guidance).

---

## Rationale (summary)

- **Why this team/repo:** Working codebase + deploy path **de-risks** execution vs. greenfield.  
- **Alternatives rejected:** Paywalled courses (not public good); fully automated scrapers (accuracy/trademark risk); **unbounded** DAML AI (mitigated by **M6 gate**).

---

## References

- Program: [github.com/canton-foundation/canton-dev-fund](https://github.com/canton-foundation/canton-dev-fund)  
- Governance: **CIP-0082**, **CIP-0100**  
- Community list: **grants-discuss@lists.sync.global**  
- Private: **dev-fund@canton.foundation**
