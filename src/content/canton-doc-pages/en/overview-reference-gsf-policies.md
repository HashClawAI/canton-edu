---
title: "GSF Policies"
slug: "overview-reference-gsf-policies"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/gsf-policies.md"
source_title: "GSF Policies"
tags:
  - overview
  - reference
  - gsf-policies
---

# GSF Policies

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# GSF Policies

> Global Synchronizer Foundation policies and governance framework

The [Global Synchronizer Foundation](https://canton.foundation) (GSF) is an independent non-profit organization created in partnership with the Linux Foundation. It governs the Global Synchronizer, the decentralized interoperability and synchronization infrastructure of the Canton Network.

## Purpose and role

The GSF provides transparent governance over the Global Synchronizer and works to grow the ecosystem around it. Its responsibilities include:

* Defining and maintaining the governance framework for the Global Synchronizer
* Providing transparency into Super Validator operations and governance votes
* Operating a Super Validator node and participating in governance on behalf of its members
* Coordinating upgrade schedules and network policies across the Super Validator set
* Supporting ecosystem development through outreach, developer programs, and a Protocol Development Fund

The GSF does not control the network unilaterally. Governance decisions require consensus among the Super Validators through on-chain voting mechanisms. The GSF participates in these votes as one Super Validator among many.

## Membership

The GSF offers three membership tiers:

* **Premier** (\$150,000/year) -- includes a seat on the Board of Directors, delegate positions on Board Committees, participation in Board strategy days, and premium placement in marketing materials
* **General** ($5,000--$30,000/year, scaled by organization size) -- includes participation in Member Committees and blog posting access
* **Associate** (no cost) -- restricted to government agencies, regulatory bodies, nonprofits, and academic institutions; requires Board approval

Any member can join the GSF's Member Committees. You can apply for membership through the [GSF membership page](https://canton.foundation/membership).

## Member Committees

The GSF organizes governance and operational work through six Member Committees:

* **Tech and Operations** -- technical direction and operational standards
* **Tokenomics** -- Canton Coin economics, fee calibration, and reward parameters
* **Accountability** -- oversight and compliance
* **Marketing** -- ecosystem outreach and communications
* **Legal** -- legal framework and regulatory matters
* **Audit and Finance** -- financial oversight

Premier members additionally have access to Board Committees and can appoint delegates to those committees.

## Governance framework

The Global Synchronizer is operated by independently acting organizations called Super Validators. These organizations run the core infrastructure -- sequencers, mediators, and SV application nodes -- and participate in governance through an on-chain governance application.

Governance actions are executed through the DSO (Decentralized Synchronizer Operations) party, a decentralized Daml party with a confirmation threshold of approximately 2/3 of onboarded Super Validators. No single entity, including the GSF, can make unilateral changes. For a detailed breakdown of the DSO party, confirmation protocols, and voting mechanics, see [SV Governance Reference](/docs/canton/overview-reference-sv-governance-reference).

The governance framework covers:

* **Network configuration** -- parameters such as traffic pricing, fee schedules, and tokenomics configuration
* **Super Validator membership** -- onboarding and offboarding of Super Validators
* **Software upgrades** -- coordination of Canton and Splice version upgrades
* **Daml package upgrades** -- managing upgrades to the on-chain governance and tokenomics packages
* **Canton Improvement Proposals (CIPs)** -- a structured process for proposing and ratifying changes to network rules and standards

## Network policies

### Validator onboarding

Validators must be approved before joining TestNet or MainNet. The process works as follows:

1. You submit a request through the [GSF validator request form](https://sync.global/validator-request/).
2. The Tokenomics Committee reviews and approves your application.
3. Your sponsoring Super Validator provides your egress IP to the allowlist maintained by the SV set. Only one IP per network is permitted, and it must be distinct across DevNet, TestNet, and MainNet.
4. Once a majority of Super Validators have adopted the updated allowlist (typically 2--7 days), you receive a one-time onboarding secret from your sponsoring SV. This secret expires after 48 hours.
5. You deploy your validator node using the onboarding secret.

DevNet is open to any validator without Tokenomics Committee approval, though your IP must still be added to the allowlist.

### Traffic and fee policies

Super Validators collectively set traffic pricing parameters through governance votes. The `extraTrafficPrice` parameter determines the cost of write traffic on the synchronizer, calibrated so that a standard Canton Coin transfer costs approximately 1 USD (per [CIP-0042](https://github.com/canton-foundation/cips/blob/main/cip-0042/cip-0042.pdf)). Super Validators are expected to periodically measure actual traffic costs and adjust parameters accordingly.

Fee parameters are updated through an on-chain median-based voting mechanism: each SV publishes their preferred value, and the system uses the median. This ensures no single SV can move the parameter by more than a small amount.

### Participation requirements

Super Validators must meet operational requirements to participate in the network:

* Run the required infrastructure components (sequencer, mediator, SV application)
* Maintain uptime and connectivity to support BFT consensus
* Participate in governance votes and upgrade coordination
* Comply with the CometBFT validator requirements for consensus participation

The CometBFT consensus protocol used by the Global Synchronizer requires more than 2/3 of Super Validators to be operational for the network to advance. Each Super Validator failure reduces the fault tolerance buffer.

### Reward policies

Super Validators earn rewards for operating infrastructure, configured through reward weight parameters. Changes to reward weights follow a governance vote process:

1. Super Validator owners agree on the updated weight.
2. A governance vote is initiated through the SV web UI.
3. The vote must be approved by a quorum of Super Validators.
4. The updated weight is reflected in the [GSF configs repository](https://github.com/global-synchronizer-foundation/configs) to ensure consistency across onboarding events.

## Upgrade coordination

Network upgrades -- whether Canton versions, Splice versions, or Daml package upgrades -- require coordination across all Super Validators. The GSF facilitates this by:

* Communicating upgrade timelines and requirements to all operators
* Tracking readiness across the Super Validator set
* Providing operational guidance for specific upgrade procedures (such as pausing triggers during Daml upgrades)

Super Validators that do not upgrade in time can cause operational issues. For example, during Daml package upgrades, validators running outdated versions may block reward expiry automation. The GSF coordinates workarounds for these situations and sets deadlines for compliance.

## CIP governance

Changes to network rules, standards, and protocols are proposed through Canton Improvement Proposals (CIPs). The CIP process provides a structured way for anyone in the ecosystem to propose changes, with final ratification by Super Validator vote.

For details on the CIP process, including how to propose one, see [CIP Reference](/docs/canton/overview-reference-what-are-cips). The full list of CIPs is maintained at [github.com/global-synchronizer-foundation/cips](https://github.com/global-synchronizer-foundation/cips).

## Communication channels

The GSF maintains several channels for validator operators and ecosystem participants:

* **Slack** -- `#validator-operations` for operational coordination, `#gsf-global-synchronizer-appdev` for application development, `#gsf-outreach` for ecosystem discussions
* **Mailing lists** at [lists.sync.global](https://lists.sync.global/) -- including `main` (general Canton Network announcements), `cip-announce` (new CIP notifications), `tokenomics-announce` (Tokenomics Committee decisions), and `validator-announce` (operator-targeted announcements)
* **Support** -- `da-support@digitalasset.com` for best-effort support, `support@digitalasset.com` for SLA-backed support

## Further resources

* [GSF website](https://canton.foundation) -- foundation information and membership
* [Canton Network](https://canton.network) -- network overview and entry point
* [GSF configs repository](https://github.com/global-synchronizer-foundation/configs) -- network configuration parameters
* [CIP repository](https://github.com/global-synchronizer-foundation/cips) -- Canton Improvement Proposals
* [SV Governance Reference](/docs/canton/overview-reference-sv-governance-reference) -- technical details on the DSO party and voting mechanics

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
