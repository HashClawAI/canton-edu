<!-- Copy everything below into the Pull Request description when opening a PR against canton-foundation/canton-dev-fund -->

## Development Fund Proposal Submission

**Proposal file:** `/proposals/open-canton-edu.md`

---

## Summary

**Open Canton Edu** ([github.com/HashClawAI/canton-edu](https://github.com/HashClawAI/canton-edu)) requests **Canton Development Fund** support for: **(1)** **information aggregation** with **allow-listed sources** and **≥1×/calendar-day** scheduled rebuild/deploy; **(2)** **Canton education content generation** (**≥18** manifest-listed **units**, §1.5 definition, human-reviewed, mandatory primary URLs); **(3)** **analysis using public Canton-related on-chain / explorer-indexer data** (**≥4** units flagged `onchain:true`, **`docs/onchain/methodology.md`**); **(4)** **`ja`/`ko` i18n** with separate validation pipelines; **(5)** **production launch + IA**; **(6)** **12 months** maintenance with **weekly daily-build** rollups in the log.

**Counting:** **`docs/grants/m3-aggregation-prs.md`** (≥8) vs **`docs/grants/m3-generation-units.md`** (≥18)—see **§1.5** to avoid double-count. **Developer events remain out of scope** (§1.3).

The proposal maps to the program README structure plus **Definitions (§1.5)**, **Evidence** (existing daily build + chart precedent), and **quantitative** daily-job success criteria for M3.

**Author:** Hashclaw.AI · **Champion:** Nguyan Vinh · **Label:** `daml-tooling` *(closed list [here](https://github.com/canton-foundation/canton-dev-fund/blob/main/proposals/_template.md))*  

---

## Funding note (120,000 CC)

**120,000 CC** illustrative total; **§6.3** includes **explorer/API** and **daily CI** bands. **Committee calibration** applies.

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
| Objectively verifiable deliverables | §1.5 manifests, §4, §5 |
| Realistic timelines | §4 |
| Open-source outputs | **Open-source and reusable outputs** |
| Technical capability | **Evidence of technical capability** (daily build + chart precedent) |
| Adoption / distribution | **Adoption and distribution plan** (+ quantitative daily-build habit) |

---

## Notes for Reviewers

- **M3:** **≥30** consecutive calendar days of **daily** workflow **≥95%** green (documented); **≥4** `onchain:true` generation rows; manifests **`m3-aggregation-prs.md`** / **`m3-generation-units.md`**.  
- **On-chain:** **Public** explorer/API only; **not** validator or private participant data.  
- **Champion:** **≥4** spot-checks of generation PRs; **≥2** named merge approvers in `MAINTAINERS.md` (per §1.5).
