---
title: "Multi-Party Workflows"
slug: "appdev-modules-m2-multi-party-workflows"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-multi-party-workflows.md"
source_title: "Multi-Party Workflows"
tags:
  - appdev
  - modules
  - m2-multi-party-workflows
---

# Multi-Party Workflows

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Multi-Party Workflows

> How Canton handles multi-party workflows differently than Ethereum

Multi-party workflows are where Canton's architecture shines compared to Ethereum. This page covers the key patterns and how to think about them differently.

## The Core Difference

On Ethereum, multi-party agreement is a **pattern you implement**. On Canton, it's a **protocol guarantee**.

| Aspect                 | Ethereum                                      | Canton                                             |
| ---------------------- | --------------------------------------------- | -------------------------------------------------- |
| **Multi-sig creation** | Deploy contract, collect signatures over time | Collect signatures over time or submit all at once |
| **Authorization**      | Runtime mapping checks                        | Protocol-level enforcement                         |
| **Atomicity**          | Manual state machine                          | Built-in all-or-nothing                            |
| **Visibility**         | All parties see everything                    | Each party sees only their view                    |

## The Propose-Accept Pattern

Since Canton requires all signatories to authorize contract creation, you can't create a multi-party contract unilaterally. The standard pattern is **propose-accept**:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequenceDiagram
    participant Alice
    participant Bob
    participant Ledger

    Alice->>Ledger: Create Proposal (signatory: Alice, observer: Bob)
    Note over Ledger: Proposal exists<br/>Bob can see it
    Bob->>Ledger: Exercise Accept on Proposal
    Note over Ledger: Proposal archived<br/>Agreement created (signatory: Alice, Bob)
```

### In Daml

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Step 1: Alice creates a proposal
template TradeProposal
  with
    proposer : Party
    counterparty : Party
    asset : Text
    price : Decimal
  where
    signatory proposer
    observer counterparty  -- Counterparty can see the proposal

    choice Accept : ContractId Trade
      controller counterparty  -- Only counterparty can accept
      do
        create Trade with
          buyer = counterparty
          seller = proposer
          asset
          price

    choice Withdraw : ()
      controller proposer  -- Proposer can cancel
      do pure ()

-- Step 2: Acceptance creates the multi-party contract
template Trade
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer, seller  -- Both must have agreed
```

### Compare to Ethereum

```solidity theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Ethereum: Manual approval tracking
contract TradeEscrow {
    address public buyer;
    address public seller;
    bool public buyerApproved;
    bool public sellerApproved;

    function approve() public {
        if (msg.sender == buyer) buyerApproved = true;
        if (msg.sender == seller) sellerApproved = true;
    }

    function execute() public {
        require(buyerApproved && sellerApproved, "Not approved");
        // Execute trade...
    }
}
```

The Canton version:

* Authorization is enforced by the protocol, not by application-level checks
* State transitions are atomic, so partial or inconsistent states don't arise
* Visibility is automatically scoped to the involved parties

## Delegation Patterns

Canton supports sophisticated delegation where one party grants another the ability to act on their behalf.

### Controller Delegation

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Asset
  with
    owner : Party
    delegate : Optional Party  -- Optional delegate
  where
    signatory owner

    choice Transfer : ContractId Asset
      with newOwner : Party
      controller case delegate of
        Some d -> d        -- Delegate can act if set
        None -> owner      -- Otherwise owner acts
      do
        create this with owner = newOwner

    choice SetDelegate : ContractId Asset
      with newDelegate : Party
      controller owner
      do
        create this with delegate = Some newDelegate
```

### Delegation via Separate Contract

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Delegation authority as a separate contract
template DelegationAuthority
  with
    principal : Party    -- Who grants authority
    agent : Party        -- Who receives authority
    scope : [Text]       -- What actions are allowed
  where
    signatory principal
    observer agent

    nonconsuming choice ActOnBehalf : ()
      with action : Text
      controller agent
      do
        assertMsg "Action not in scope" (action `elem` scope)
        -- Perform delegated action...
        pure ()
```

## Multi-Step Workflows

For workflows requiring multiple parties in sequence:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph Step1[Step 1: Proposal]
        A[Alice proposes]
    end

    subgraph Step2[Step 2: Approval]
        B[Bob approves]
    end

    subgraph Step3[Step 3: Execution]
        C[Charlie settles]
    end

    Step1 --> Step2 --> Step3
```

### Workflow State Machine

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data WorkflowState
  = Proposed
  | Approved
  | Settled

template Workflow
  with
    initiator : Party
    approver : Party
    settler : Party
    state : WorkflowState
    payload : Text
  where
    signatory initiator
    observer approver, settler

    choice Approve : ContractId Workflow
      controller approver
      do
        assertMsg "Must be in Proposed state" (state == Proposed)
        create this with state = Approved

    choice Settle : ContractId Workflow
      controller settler
      do
        assertMsg "Must be in Approved state" (state == Approved)
        create this with state = Settled
```

## Atomic Multi-Contract Operations

Canton can atomically update multiple contracts in a single transaction:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice ExecuteSwap : ()
  with
    assetA : ContractId Asset
    assetB : ContractId Asset
  controller buyer, seller
  do
    -- Both happen atomically or neither does
    exercise assetA Transfer with newOwner = buyer
    exercise assetB Transfer with newOwner = seller
```

### Why This Matters

On Ethereum, atomic swaps require:

* Escrow contracts
* Time-locked phases
* Failure recovery logic
* Careful reentrancy protection

On Canton, atomicity is **guaranteed by the protocol**. If any part fails, nothing happens.

## Privacy in Multi-Party Workflows

Each party only sees their relevant portion:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph TX[Transaction]
        E1[Alice accepts Proposal from Bob]
        E1 --> E2[Create Trade between Alice and Bob]
        E2 --> E3[Transfer payment from Alice to Bob]
        E3 --> E4[Notify Alice's bank]
    end

    TX --> VA[Alice sees: all]
    TX --> VB[Bob sees: Trade, payment received]
    TX --> VK[Bank sees: notification only]
```

## Common Workflow Patterns

| Pattern                   | Use Case              | Key Feature                   |
| ------------------------- | --------------------- | ----------------------------- |
| **Propose-Accept**        | Two-party agreements  | Simple, clear consent         |
| **Propose-Accept-Settle** | Three-party workflows | Sequential authorization      |
| **Delegation**            | Acting on behalf      | Controlled authority transfer |
| **Escrow**                | Conditional execution | Atomic swap guarantee         |
| **Voting**                | Group decisions       | Threshold-based approval      |

### Voting Example

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Vote
  with
    proposal : Text
    voters : [Party]
    votes : [(Party, Bool)]
    threshold : Int
  where
    signatory (map fst votes)
    observer voters

    choice CastVote : ContractId Vote
      with
        voter : Party
        approve : Bool
      controller voter
      do
        assertMsg "Not a voter" (voter `elem` voters)
        assertMsg "Already voted" (voter `notElem` map fst votes)
        create this with votes = (voter, approve) :: votes

    choice TallyAndExecute : ()
      controller voters
      do
        let approvals = length [v | (_, v) <- votes, v]
        assertMsg "Threshold not met" (approvals >= threshold)
        -- Execute the proposal...
        pure ()
```

## Related Topics

<CardGroup cols={2}>
  <Card title="Migration Checklist" icon="list-check" href="/docs/canton/appdev-modules-m2-migration-checklist">
    Practical checklist for migrating from Ethereum.
  </Card>

  <Card title="Module 3: Daml" icon="code" href="/docs/canton/appdev-modules-m3-dev-environment">
    Start writing Daml smart contracts.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
