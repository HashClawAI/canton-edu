---
title: "Composing Multi-Party Workflows in Daml"
slug: "appdev-deep-dives-composition-multi-party"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/composition-multi-party.md"
source_title: "Composing Multi-Party Workflows in Daml"
tags:
  - appdev
  - deep-dives
  - composition-multi-party
---

# Composing Multi-Party Workflows in Daml

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Composing Multi-Party Workflows in Daml

> Advanced Daml patterns for propose-accept, delegation, authorization chains, and atomic multi-party composition

Real-world Daml applications involve multiple parties with different roles, permissions, and trust relationships. This deep dive covers the Daml design patterns that make complex multi-party workflows work — from simple two-party agreements to multi-step authorization chains spanning several organizations.

## The Propose-Accept Pattern

For the canonical walkthrough of propose-accept, see [Module 2: Multi-Party Workflows](/docs/canton/appdev-modules-m2-multi-party-workflows#the-propose-accept-pattern). This deep dive focuses on the additional composition patterns that build on that foundation.

## Delegation

Delegation lets one party grant another party the authority to act on their behalf within a defined scope. Unlike the propose-accept pattern (which creates a shared agreement), delegation creates a one-directional trust relationship.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template OperatorLicense
  with
    owner : Party
    operator : Party
    allowedOperations : [Text]
  where
    signatory owner
    observer operator

    choice Operate : ContractId OperationResult
      with
        operation : Text
      controller operator
      do assertMsg "Operation not allowed"
           (operation `elem` allowedOperations)
         create OperationResult with
           performer = operator
           onBehalfOf = owner
           operation
```

The owner grants specific operations to the operator. The operator can exercise the `Operate` choice, but only for allowed operations. The owner can revoke the delegation by archiving the `OperatorLicense`.

## Multi-Step Workflows

Many business processes require a sequence of actions by different parties. Model these as a chain of contracts, where each step's output becomes the next step's input:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template TradeRequest
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer
    observer seller

    choice ConfirmTrade : ContractId TradeSettlement
      controller seller
      do create TradeSettlement with
           buyer
           seller
           asset
           price

template TradeSettlement
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer, seller

    choice Settle : ()
      controller seller
      do pure ()
```

Each step in the workflow is a separate template. This makes the workflow state visible and auditable — you can query the ledger to see which step any given trade is at.

## Atomic Composition

Daml transactions are atomic: either all the creates and archives in a transaction succeed, or none of them do. Use this property to implement complex operations that must happen together:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice SwapAssets : (ContractId Asset, ContractId Asset)
  controller partyA
  do -- Both transfers happen atomically
     newAssetForB <- exercise assetFromA Transfer with newOwner = partyB
     newAssetForA <- exercise assetFromB Transfer with newOwner = partyA
     pure (newAssetForA, newAssetForB)
```

If either transfer fails (wrong controller, contract already archived, assertion failure), neither happens. This is the foundation of delivery-versus-payment (DvP) and other settlement patterns.

## Authorization Through Interfaces

Interfaces define abstract capabilities that templates can implement. Use them to create composable authorization patterns:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface Transferable where
  viewtype TransferView
  getOwner : Party
  transfer : Party -> Update (ContractId Transferable)

  choice TransferTo : ContractId Transferable
    with newOwner : Party
    controller getOwner this
    do transfer this newOwner
```

Any template that implements `Transferable` gets the `TransferTo` choice. Your backend can work with the interface without knowing the specific template type, enabling generic transfer logic across different asset types.

<Note>
  Place interface definitions in standalone packages that contain only interfaces and no templates. An interface's structure (methods and view type) cannot be modified after deployment. If changes are needed, introduce a new interface version in a new package.
</Note>

## Multi-Party Visibility Patterns

Canton's privacy model means each party sees only the contracts where they are a stakeholder (signatory or observer). For workflows that need broader visibility without giving parties the ability to act, use the observer pattern:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuditableTransaction
  with
    executor : Party
    counterparty : Party
    auditor : Party
    details : Text
  where
    signatory executor, counterparty
    observer auditor  -- auditor can see but not act
```

For regulatory or compliance scenarios where a third party needs visibility into transactions without being a participant, add them as observers. They can read the contract data through the Ledger API but cannot exercise choices on it.

## Design Considerations

When composing multi-party workflows:

* Keep the signatory set minimal — each additional signatory adds coordination overhead
* Use observers for read-only access rather than making parties signatories
* Design templates so that each party's choices are clear from the template declaration
* Avoid deep transaction trees (many nested exercises) as they increase transaction size and latency
* Consider whether a workflow step needs to be on-ledger or can happen off-ledger

## Next Steps

* [Decentralization](/docs/canton/appdev-deep-dives-decentralization) — Strategies for decentralizing at each layer
* [Multi-Hosting](/docs/canton/appdev-deep-dives-multi-hosting) — Distributing parties across validators for resilience

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
