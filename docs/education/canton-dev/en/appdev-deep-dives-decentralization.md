---
title: "Decentralization"
slug: "appdev-deep-dives-decentralization"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/decentralization.md"
source_title: "Decentralization"
tags:
  - appdev
  - deep-dives
  - decentralization
---

# Decentralization

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Decentralization

> Decentralization strategies at each layer of the Canton stack, from single-validator to BFT synchronizers

Canton supports a spectrum of decentralization. You don't have to commit to full decentralization from day one — you can start with a simple single-validator setup and progressively decentralize as your application's trust requirements evolve.

## The Decentralization Spectrum

Canton's architecture has several layers where decentralization choices apply, each with different trust implications:

* **Application layer** — How many validators host the parties in your application (e.g., multi-hosted party or decentralized party)
* **Synchronizer layer** — Whether the synchronizer itself is operated by one entity or many
* **Network layer** — Whether your application uses the Global Synchronizer, a private synchronizer, or both

At each layer, more decentralization means less trust in any single entity, but also more operational complexity.

## Single Validator

The simplest deployment. All your application's parties are hosted on a single validator connected to the Global Synchronizer.

**Trust model:** You trust the validator operator (yourself or a third party) to process transactions honestly and keep data available. The Global Synchronizer's BFT properties still protect against synchronizer-level attacks, but your validator is a single point of failure for your application.

**When this is appropriate:**

* Early development and prototyping
* Applications where all parties belong to the same organization
* Scenarios where a single trusted operator is acceptable

## Multi-Validator

Different parties in your application are hosted on different validators, each operated independently. This is the standard deployment for cross-organizational applications on the Canton Network.

**Trust model:** Each organization operates its own validator and controls its own data. No single validator can see all transactions — Canton's privacy model ensures that each validator only sees the transactions involving its own parties. The synchronizer routes encrypted transaction views to the appropriate validators.  Each party trusts its own validator operator.

**When this is appropriate:**

* Cross-organizational workflows (trade, settlement, supply chain)
* Applications where parties don't want to trust a single operator with their data
* Production applications on the Canton Network

## Multi-Hosted Parties

A single party can be hosted on multiple validators simultaneously. If one validator goes down, the party's operations continue on the others. This provides resilience without changing the application's Daml logic.

**Trust model:** The party trusts at least one validator that hosts it.  This weakens the trust for validator operators since all validators hosting the party need to agree if the threshold for agreements is reached.
Transactions involving the party may be processed by any of its hosting validators if the threshold is one. This reduces single-point-of-failure risk but requires trust in multiple validators.

**When this is appropriate:**

* High-availability requirements where a single validator's downtime is unacceptable
* Organizations that want geographic redundancy
* Gradual migration between validators

See [Multi-Hosting](/docs/canton/appdev-deep-dives-multi-hosting) for implementation details.

## BFT Synchronizers

The Global Synchronizer itself is decentralized. It's operated by a set of Super Validators (SVs) using a Byzantine Fault Tolerant (BFT) consensus protocol (CometBFT). No single SV can censor transactions or manipulate the ordering.

**Trust model:** The Global Synchronizer tolerates up to one-third of SVs being faulty or malicious. As long as two-thirds of SVs are honest, the synchronizer operates correctly. This is the highest level of decentralization Canton provides at the infrastructure layer.

**When this is appropriate:**

* The Global Synchronizer is already BFT — all applications on it benefit automatically
* Private synchronizers can also be configured with BFT if multiple operators want to run one jointly

## Multi-Synchronizer

Canton supports connecting validators to multiple synchronizers simultaneously. A party can have contracts on the Global Synchronizer and on one or more private (extension) synchronizers, with the ability to reassign contracts
between them.

**Trust model:** Different workflows can have different trust properties. Sensitive bilateral transactions might use a private synchronizer operated by the two parties, while settlement against Canton Coin happens on the public
Global Synchronizer.

**When this is appropriate:**

* Applications with mixed privacy/performance requirements
* Workflows that benefit from both public settlement and private processing
* Organizations with regulatory requirements about where data is processed or have specific privacy needs

## Choosing Your Level

The right level of decentralization depends on your application's specific requirements:

* **Start simple** — Most applications begin with multi-validator deployment because cross-organizational workflows are Canton's primary use case
* **Add resilience** — Move to multi-hosting when your application needs high availability
* **BFT is built in** — Applications on the Global Synchronizer benefit from its BFT properties without additional application-level configuration
* **Add privacy** — Use multi-synchronizer deployment when some workflows need private processing

You don't need to design for the highest level of decentralization from the start. Canton's architecture lets you progressively decentralize by adding validators, hosting parties on additional nodes, or connecting to new synchronizers — all without changing your Daml code.

## Next Steps

* [Multi-Hosting](/docs/canton/appdev-deep-dives-multi-hosting) — Implementation details for distributing parties across validators
* [Composition and Multi-Party Workflows](/docs/canton/appdev-deep-dives-composition-multi-party) — Daml patterns for multi-party interactions

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
