---
title: "CIP Reference"
slug: "overview-reference-what-are-cips"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/what-are-cips.md"
source_title: "CIP Reference"
tags:
  - overview
  - reference
  - what-are-cips
---

# CIP Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# CIP Reference

> Formal structure, lifecycle, and governance mechanics of Canton Improvement Proposals (CIPs)

Canton Improvement Proposals (CIPs) are formal design documents that describe standards, protocol changes, governance procedures, and guidelines for Canton Network. They serve as the primary mechanism through which the community proposes and ratifies changes to the network.

The CIP process is modeled on established improvement proposal frameworks (such as Ethereum's EIPs and Python's PEPs) and is formally defined in [CIP-0000](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0000/cip-0000.md). All CIPs are maintained in a [public GitHub repository](https://github.com/global-synchronizer-foundation/cips) managed by the Global Synchronizer Foundation.

For an introductory overview of CIPs and why they matter, see the [CIPs introduction](/docs/canton/overview-understand-cips-introduction).

## CIP types

Each CIP belongs to one of five categories:

* **Standards Track** — Technical specifications and protocol changes that affect Global Synchronizer implementations. These require a design document and a reference implementation before reaching Final status.
* **Governance** — Proposals that define or modify Super Validator rights, voting weights, or foundational governance rules, including on-chain voting processes.
* **Tokenomics** — Changes to reward structures, Canton Coin fees, or synchronizer traffic pricing.
* **Process** — Adjustments to workflows, tooling, or meta-CIPs about the CIP process itself. Community consensus typically applies.
* **Informational** — General design guidelines or recommendations. Informational CIPs do not require adoption and carry no binding effect.

## CIP lifecycle

A CIP progresses through a defined set of stages:

* **Draft** — The author develops the proposal and gathers feedback on the `cip-discuss` mailing list. At this stage, the CIP does not yet have an official number.
* **Proposed** — After securing sponsorship from two Super Validators, the author submits the CIP to the `cip-vote` mailing list for formal consideration. A CIP editor assigns the official number at this point.
* **Approved** — The CIP receives a two-thirds majority vote from Super Validator rights holders during a 10-day voting window.
* **Active** — For approved CIPs that require no on-chain implementation (such as Process or Informational CIPs), the proposal takes effect immediately upon approval.
* **Final** — For approved CIPs that require on-chain adoption (typically Standards Track, Governance, or Tokenomics CIPs), the proposal reaches Final once two-thirds of Super Validators have implemented the change on-chain.

A CIP may also reach one of three terminal states outside the normal progression: **Withdrawn** (the author pulls the proposal), **Deferred** (postponed for future consideration), or **Rejected** (failed to achieve the two-thirds vote threshold). A CIP that has been superseded by a later proposal is marked **Replaced** — for example, CIP-0073 was replaced by CIP-0096.

## Numbering convention

Authors do not self-assign CIP numbers. During the draft phase, you use a descriptive alias (for example, `CIP-johndoe-token-lockup`). A CIP editor assigns the official sequential number once the proposal passes editorial review. Numbers use a four-digit zero-padded format: CIP-0000, CIP-0056, CIP-0103, and so on. The numbering is strictly sequential and does not encode type or category information — you determine a CIP's type from its preamble metadata, not its number.

## Who can propose a CIP

Any member of the public can author a CIP. You join the `cip-discuss` mailing list at [lists.sync.global](https://lists.sync.global/) and begin the discussion there. In practice, CIP authors include Super Validator operators, application developers, and ecosystem contributors.

Not every change requires a CIP. Small enhancements to a specific software project proceed through that project's own development workflow. You need a CIP when the change affects interoperability across validators, modifies governance rules, alters tokenomics parameters, or establishes a network-wide standard that multiple parties must implement. If in doubt, start a discussion on the `cip-discuss` list — the community and editors will advise whether a formal CIP is warranted.

To move from discussion to a formal vote, you need sponsorship from two Super Validators. Sponsorship signals that at least two SV operators consider the proposal worth putting to a network-wide vote. It does not imply endorsement of the proposal's content.

## Review and approval

CIP editors manage the review process. Their responsibilities include verifying technical soundness, confirming that community discussion has taken place on the mailing list, validating format compliance, and assigning the official CIP number and category. Editors can make editorial corrections independently but do not rule on whether a CIP should be approved — that decision belongs to the Super Validator vote. The current editorial team is listed in [CIP-0000](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0000/cip-0000.md).

Before a CIP can move to a vote, minimum discussion periods apply on the `cip-discuss` mailing list:

* Standards Track: 3 months
* Governance and Tokenomics: 1 month each
* Process: 1 month
* Informational: 2 weeks

These minimums exist to ensure that proposals receive adequate scrutiny relative to their impact. A Standards Track CIP changing protocol behavior warrants longer discussion than an Informational guideline.

Once the discussion period has elapsed and two Super Validators have agreed to sponsor the proposal, voting proceeds on the `cip-vote` list using GitHub Team Voting. The voting window lasts 10 days. Approval requires a two-thirds majority of Super Validator rights holders voting in favor.

## Relationship to on-chain governance

CIP approval through the vote process is not the final step for proposals that require on-chain changes. Once a CIP is approved, Super Validators must adopt it through an on-chain governance action — the same BFT voting mechanism described in the [SV governance reference](/docs/canton/overview-reference-sv-governance-reference). A CIP reaches Final status only after two-thirds of Super Validators have implemented the change on-chain.

This two-phase structure separates the design consensus (off-chain CIP vote) from the operational commitment (on-chain adoption), ensuring that approved proposals are actually deployed before becoming authoritative. On-chain implementation results are visible through the Canton Coin Scan APIs, so you can verify whether a given CIP has reached Final status by checking adoption across Super Validators.

## CIP document structure

CIPs follow a consistent format so that reviewers can evaluate proposals efficiently and implementers can find the information they need. Every CIP must include these sections:

* **Preamble** — Metadata headers: CIP number, title, authors, status, type, dates, and license
* **Abstract** — A roughly 200-word summary of the problem and proposed solution
* **Specification** — The detailed technical or governance change, written precisely enough for Super Validators to verify compliance
* **Motivation** — Why the current state is inadequate and what the proposal addresses
* **Rationale** — Design decisions, trade-offs considered, and alternatives rejected
* **Backwards Compatibility** — Any breaking changes and migration paths (where applicable)
* **Reference Implementation** — Required before a Standards Track CIP can reach Final status
* **Copyright** — Licensing terms under an approved license

The CIP repository contains a template you can use as a starting point. For the step-by-step process of authoring and submitting a CIP, see [How to propose a CIP](#how-to-propose-a-cip) below.

## Notable CIPs

The following CIPs illustrate the range of topics the process covers.

**[CIP-0056: Canton Network Token Standard](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)** (Standards Track, Final) — Defines six standardized APIs for token operations on Canton Network, covering metadata, holdings, peer-to-peer transfers, and delivery-versus-payment settlement. Canton Coin implements all standard APIs. CIP-0056 draws on ideas from ERC-20 but is adapted for Canton's UTXO model and privacy architecture. If you are building a token on Canton Network, this is the standard you need to implement.

**[CIP-0078: Canton Coin Fee Removal](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md)** (Tokenomics, Final) — Eliminates transaction fees on Canton Coin transfers. Holding fees remain only on coin expiry to prevent accumulation of economically unviable dust coins. This change simplifies developer workflows that previously required fee-funding logic, and was viable because approximately 95% of MainNet burn already derived from traffic purchases rather than transfer fees.

**[CIP-0073: Weighted Validator Liveness Rewards](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0073/cip-0073.md)** (Tokenomics, Replaced by CIP-0096) — Extended validator liveness rewards to any party and introduced governance-adjustable reward weight multipliers. This CIP was later superseded by CIP-0096, which refined the reward model.

**[CIP-0103: dApp Standard](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0103/cip-0103.md)** (Standards Track, Approved) — Specifies a vendor-neutral dApp API that decouples network connectivity and key management from application logic. The standard supports both synchronous and asynchronous operation models, allowing any dApp to work with any wallet implementation.

## Resources

* [CIP repository on GitHub](https://github.com/global-synchronizer-foundation/cips) — All CIP documents and the canonical CIP-0000 process definition
* [CIP-0000: CIP Process](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0000/cip-0000.md) — The authoritative specification of the CIP process, including editorial team, voting rules, and format requirements
* [GSF mailing lists](https://lists.sync.global/) — The `cip-discuss` and `cip-vote` lists where CIP discussion and voting take place
* [SV governance reference](/docs/canton/overview-reference-sv-governance-reference) — On-chain governance mechanics that CIPs feed into after approval

## How to propose a CIP

Anyone can author a CIP. The process moves through several stages before a proposal becomes an accepted part of the Canton Network standards:

1. **Draft** -- the author writes the proposal and submits it for community review
2. **Discussion** -- the community reviews, debates, and suggests changes
3. **Review** -- the proposal is refined based on feedback and formally reviewed
4. **Acceptance** -- Super Validators vote on the proposal through on-chain governance
5. **Implementation** -- the accepted changes are built and deployed

Not every CIP reaches acceptance. Proposals can be withdrawn by the author, deferred for future consideration, or rejected by the Super Validator vote.

### Writing a CIP

CIPs are submitted as pull requests to the [CIP repository on GitHub](https://github.com/global-synchronizer-foundation/cips). Each CIP lives in its own directory (e.g., `cip-0056/cip-0056.md`).

A CIP document should include the following sections:

* **Preamble** -- CIP number, title, author(s), status, type, and creation date
* **Abstract** -- a short (200 words or fewer) description of the proposal
* **Motivation** -- why this change is needed, what problem it solves, and who benefits
* **Specification** -- the precise technical details of the proposed change, written clearly enough for implementers to work from
* **Rationale** -- why the specification is designed the way it is, including alternatives that were considered and rejected
* **Backwards compatibility** -- how the change affects existing deployments, contracts, or integrations
* **Reference implementation** -- if applicable, a link to or description of a working implementation
* **Security considerations** -- any security implications of the proposal

The specification section is the most important. It should be unambiguous and complete enough that two independent teams could implement it and arrive at compatible results.

### CIP types

CIPs generally fall into one of these categories:

* **Standards track** -- changes to network protocols, Daml packages, APIs, or other specifications that affect interoperability
* **Process** -- changes to the CIP process itself or to governance procedures
* **Informational** -- guidelines, recommendations, or design rationale that do not require a governance vote

### The discussion phase

After submitting a pull request, the proposal enters community discussion. This happens through:

* Comments on the GitHub pull request
* Threads on the [CIP discussion mailing list](https://lists.sync.global/g/cip-discuss)
* Conversations in relevant Slack channels (#gsf-global-synchronizer-appdev, #gsf-outreach)

Authors should expect feedback and be prepared to revise the proposal. Common feedback includes requests for more precise specification language, questions about backwards compatibility, and suggestions for additional security analysis.

The discussion period has no fixed duration. A CIP is ready for formal review when the author and community reach rough consensus that the proposal is well-specified and the open questions have been addressed.

### Formal review and acceptance

Once a CIP is considered mature, it moves to formal review. At this stage:

1. The CIP is marked as "Review" status in the repository.
2. Super Validators evaluate the proposal against their own operational and business requirements.
3. A governance vote is initiated through the SV web UI. Acceptance requires approval from a quorum of Super Validators (approximately 2/3 of onboarded SVs).

If the vote passes, the CIP status is updated to "Accepted" and implementation can proceed. If the vote fails, the author can revise the proposal and resubmit, or withdraw it.

### After acceptance

An accepted CIP becomes part of the Canton Network standards. Implementation may involve:

* Changes to the Splice codebase ([github.com/canton-network/splice](https://github.com/canton-network/splice))
* Updates to Canton or Daml SDK components
* Configuration changes coordinated across the Super Validator set
* New Daml packages deployed through the standard upgrade process

The CIP repository tracks the implementation status of each accepted proposal.

### Tips for effective proposals

* Start by searching the [existing CIPs](https://github.com/global-synchronizer-foundation/cips) and discussion archives to make sure your idea has not already been proposed or addressed.
* Talk to the community early. Floating an idea in the discussion channels before writing a full CIP can save time and improve the proposal.
* Be specific in the specification section. Vague language leads to extended discussion and delays.
* Address backwards compatibility explicitly, even if you believe the change is fully backwards-compatible. Reviewers will ask about it.
* Consider writing a reference implementation alongside the CIP. Proposals with working code tend to move through review faster.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
