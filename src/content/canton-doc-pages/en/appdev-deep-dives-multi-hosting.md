---
title: "Multi-Hosting and Resilience"
slug: "appdev-deep-dives-multi-hosting"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/multi-hosting.md"
source_title: "Multi-Hosting and Resilience"
tags:
  - appdev
  - deep-dives
  - multi-hosting
---

# Multi-Hosting and Resilience

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Hosting and Resilience

> Distributing parties across multiple validators for high availability, failover, and data resilience

Multi-hosting lets a single party be hosted on multiple validators simultaneously. If one validator goes down, the party's operations continue on the others — without changing any Daml logic. This deep dive covers how multi-hosting works, when to use it, and how to set it up.

## Why Multi-Host?

A party hosted on a single validator has a single point of failure. If that validator goes offline, the party can't submit transactions or receive updates until it recovers. Multi-hosting addresses this by distributing the party across multiple validators.

Common reasons to multi-host:

* **High availability** — Business-critical parties that can't tolerate downtime
* **Geographic redundancy** — Validators in different regions to survive regional outages
* **Validator migration** — Gradually shifting a party from one validator to another without downtime
* **Organizational resilience** — Separating operational risk across independently managed validators
* **Protect against a malicious operator** — Using a threshold value higher than one prevents a single malicious operator from invalid activity

## How Multi-Hosting Works

Multi-hosting is managed through Canton's topology system. A party-to-participant mapping declares which validators host a given party and what permission each validator has (Submission, Confirmation, or Observation).

When a local party is hosted on multiple validators with Submission permission, any of those validators can submit commands on behalf of the party. For external parties, submission happens on any validator where the party is hosted with Confirmation permission. The synchronizer delivers transaction views to all hosting validators, so each one maintains a consistent view of the party's contracts.

### Confirmation Thresholds

You can configure a confirmation threshold that determines how many hosting validators must confirm a transaction before it proceeds. With a threshold of 1 (the default when not specified), any single hosting validator can confirm. With a higher threshold, multiple validators must independently validate and confirm, providing stronger integrity guarantees at the cost of additional latency.  A threshold greater than 1 protects against a malicious validator.

### Permission Levels

Each hosting validator is assigned one of three permission levels:

* **Submission** — The validator can submit commands on behalf of the party. This permission is only available for local parties (parties whose keys are managed by the validator).
* **Confirmation** — The validator can confirm transactions for the party. This is the standard permission for active hosting.
* **Observation** — The validator receives transaction data for the party but cannot submit or confirm. Useful for read-only replicas, audit nodes, or pre-staging a migration target.

## Setting Up Multi-Hosting for New Parties

Multi-hosting requires a topology transaction that maps the party to multiple validators. All hosting validators must sign the mapping — it's a proposal that becomes active only when all parties agree.

<Note>
  The instructions below apply to **new external parties**. Adding hosting nodes to existing parties is called [party replication](/docs/canton/global-synchronizer-production-operations-party-management#simple-party-replication) and is a different, more involved workflow. For external parties, the external party must authorize (sign) the party to participant mapping with its own key. See the [external signing onboarding documentation](/docs/canton/appdev-deep-dives-external-signing-onboarding) for details.
</Note>

### Via the Ledger API

When onboarding an external party, include additional validators in the topology request:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "otherConfirmingParticipantUids": ["PAR::participant2::1220a4d7..."],
  "confirmationThreshold": 1
}
```

The generated topology transactions need to be uploaded to each hosting validator's Ledger API. When a party-to-participant mapping is uploaded through the allocate endpoint which mentions the local validator, it is automatically signed by the local validator and forwarded to the network. If the topology transaction is not fully authorized (some signatures are still missing), it is treated as a proposal.

If the proposal already exists on the network, the new signatures are merged into the proposal. Once enough signatures are present, the topology transaction is accepted and added to the state.

### Via the Canton Console

You can also set up multi-hosting directly through the Canton Console. This approach is useful for internal parties where you have console access to both validators.

Create a hosting proposal on the first validator:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.propose(partyId, newParticipants = Seq((participant1.id, ParticipantPermission.Confirmation), (participant2.id, ParticipantPermission.Confirmation)), store = synchronizerId)
    res1: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Confirmation,
            PAR::participant2::1220a4d7463b... -> Confirmation
          )
        ),
        serial = 2,
        operation = Replace,
        hash = SHA-256:f77e8ccd88df...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

On the second validator, list pending proposals and authorize:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val proposals = participant2.topology.party_to_participant_mappings.list_hosting_proposals(synchronizerId, participant2.id)
    proposals : Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMultiHostingProposal] = Vector(
      ListMultiHostingProposal(
        txHash = SHA-256:f77e8ccd88df...,
        party = Alice::12201ff69b1d...,
        permission = Confirmation$,
        others = PAR::participant1::12201ff69b1d... -> Confirmation$,
        threshold = 1
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ proposals.map { p => participant2.topology.transactions.authorize(synchronizerId, p.txHash); p.txHash}
    res3: Seq[TopologyTransaction.TxHash] = Vector(TxHash(hash = SHA-256:f77e8ccd88df...))
```

Once both validators have signed, the party appears as hosted on both nodes. You can verify with:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.hosted("Alice")
    res4: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = Alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = local::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

## Data Resilience Patterns

Multi-hosting addresses compute resilience (can I submit transactions?), but you also need data resilience (can I query my party's contract state?). The Participant Query Store (PQS) is the primary query layer for Canton applications, and its availability matters as much as the validator itself.

For PQS deployment patterns — including high availability across hosting validators and sharing the PQS database with application tables — see [PQS (Participant Query Store)](/sdks-tools/development-tools/pqs#high-availability-and-database-sharing).

## When to Use Multi-Hosting vs. Other Resilience Strategies

Multi-hosting is one of several resilience approaches. Choose based on your requirements:

* **Single validator with database backups** — Sufficient when some downtime is acceptable and you can restore from backup. Simplest to operate.
* **Multi-hosting (two or more validators)** — Good for parties that need continuous availability and need to protect against a malicious validator. Both validators independently maintain state, so failover is immediate.
* **Multi-hosting with observation nodes** — Add Observation-permission validators as read-only replicas for query scaling or audit purposes without increasing confirmation overhead.
* **Multi-hosting across synchronizers** — For workflows that span multiple synchronizers, each hosting validator can connect to different synchronizers, providing both resilience and multi-synchronizer access.

## Operational Considerations

* **Cost** — Each hosting validator with Confirmation permission independently processes and confirms transactions, which increases traffic consumption proportionally. The exact cost increase depends on the number of confirming validators and the confirmation threshold.
* **Consistency** — All hosting validators see the same transactions (the synchronizer ensures this), but PQS queries may need to take into account offsets being a little different.
* **Key management** — Each hosting validator holds its own signing keys. Compromising one validator's keys doesn't compromise the others, but the party's security depends on the threshold configuration.
* **Removing a host** — To stop hosting a party on a validator, submit a new topology transaction that removes that validator from the mapping. The party's contracts remain accessible on the other hosting validators.

## Next Steps

* [Decentralization](/docs/canton/appdev-deep-dives-decentralization) — How multi-hosting fits into Canton's decentralization spectrum
* [Composition and Multi-Party Workflows](/docs/canton/appdev-deep-dives-composition-multi-party) — Daml patterns for multi-party interactions

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
