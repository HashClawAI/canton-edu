---
title: "The Ledger Model"
slug: "overview-learn-ledger-model"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/learn/ledger-model.md"
source_title: "The Ledger Model"
tags:
  - overview
  - learn
  - ledger-model
---

# The Ledger Model

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# The Ledger Model

> Understanding Canton's UTXO-based ledger model with contracts, stakeholders, and transactions

Canton uses an **extended UTXO (eUTXO)** ledger model where contracts are discrete objects that are created and archived, rather than mutable account balances. This model is fundamental to how Canton achieves privacy and composability.

## Contracts as UTXOs

In Canton, the ledger is a collection of **active contracts**. Each contract:

* Is created by a transaction
* Exists until archived by another transaction
* Is immutable
* Has a unique contract ID

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    subgraph T1[Transaction 1]
        C1[Create Contract A]
    end

    subgraph T2[Transaction 2]
        A1[Archive Contract A]
        C2[Create Contract B]
    end

    subgraph T3[Transaction 3]
        A2[Archive Contract B]
        C3[Create Contract C]
        C4[Create Contract D]
    end

    T1 --> T2 --> T3
```

### Why UTXO?

| Property                    | UTXO Model                                      | Account Model                |
| --------------------------- | ----------------------------------------------- | ---------------------------- |
| **Parallelism**             | High—independent contracts process in parallel  | Low—account locks needed     |
| **Privacy**                 | Natural—each contract has specific stakeholders | Hard—accounts aggregate data |
| **Composability**           | Built-in—contracts reference each other         | Requires careful design      |
| **Double-spend prevention** | Structural—contract archived once               | Requires sequence numbers    |

### Contract Lifecycle

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
stateDiagram-v2
    [*] --> Active: Create
    Active --> Archived: Archive/Exercise
    Archived --> [*]

    note right of Active
        Contract is visible
        to stakeholders and
        can be exercised
    end note

    note right of Archived
        Contract no longer
        exists on ledger
        (historical only)
    end note
```

## Stakeholder Roles

Every contract has **stakeholders**—parties with specific relationships to that contract. Stakeholder roles determine visibility and authorization.

### Signatories

Signatories are the primary authorities on a contract.

**Properties:**

* Must authorize contract creation
* May authorize contract archival (if controller on a consuming choice)
* Always see the contract and all actions on it
* Defined in the template with `signatory` keyword

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Asset
  with
    issuer : Party
    owner : Party
  where
    signatory issuer, owner  -- Both must agree to create/archive
```

**When to use:** When a party's agreement is essential to the contract's existence.

### Observers

Observers can see the contract but cannot act on it unilaterally.

**Properties:**

* See the contract and actions on it
* Cannot archive or exercise choices (unless also a controller)
* Defined with `observer` keyword

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template RegulatedAsset
  with
    owner : Party
    regulator : Party
  where
    signatory owner
    observer regulator  -- Regulator can see but not act
```

**When to use:** When a party needs visibility for compliance, audit, or information.

### Controllers

Controllers can exercise specific choices on a contract.

**Properties:**

* Can exercise choices they control
* See the choice and its consequences
* Defined per-choice with `controller` keyword

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Proposal
  with
    proposer : Party
    accepter : Party
  where
    signatory proposer
    observer accepter

    choice Accept : ContractId Agreement
      controller accepter  -- Only accepter can exercise
      do
        create Agreement with party1 = proposer, party2 = accepter
```

**When to use:** When a party should be able to trigger specific actions.

### Actors

Actors are the parties submitting or authorizing a transaction.

### Role Comparison

| Role           | Can Create?  | Can See?              | Can Exercise?       | Can Archive?         |
| -------------- | ------------ | --------------------- | ------------------- | -------------------- |
| **Signatory**  | Yes          | Always                | If controller       | Must authorize       |
| **Observer**   | No           | Always                | If controller       | No                   |
| **Controller** | No           | Choice + consequences | Yes (their choices) | Via consuming choice |
| **Actor**      | If signatory | If stakeholder        | If controller       | If signatory         |

## Transaction Structure

Transactions in Canton are trees of **actions**. Each action creates, exercises, or fetches contracts. (*Note that fetches are not typically returned in the transaction stream.*)

### Action Types

* **Create** adds a new contract to the ledger and returns a contract ID.
* **Exercise** executes a choice on a contract (which may archive it) and returns the choice result along with any consequences.
* **Fetch** reads a contract without changing state, returning the contract data.

### Transaction Tree

A transaction tree records all creates, exercises, fetches, and archives that occur within a single transaction:

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph TX[Transaction]
        E1[Exercise Transfer on Asset #1]
        E1 --> C1[Create Asset #2]
        E1 --> E2[Exercise Notify on Registry]
        E2 --> C2[Create Notification]
    end
```

### Consuming vs Non-Consuming Choices

A **consuming** choice (the default) archives the contract when exercised. Use these for state transitions and transfers. A **non-consuming** choice leaves the contract active, which is useful for queries, notifications, and reads.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Consuming: archives the contract
choice Transfer : ContractId Asset
  controller owner
  do
    create this with owner = newOwner

-- Non-consuming: contract remains
nonconsuming choice GetBalance : Decimal
  controller owner
  do
    return balance
```

## Views

Each stakeholder sees a **view** of the transaction: only the parts they're entitled to.

### View Composition

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph Full[Full Transaction]
        A[Alice pays Bob 100]
        B[Bob pays Charlie 50]
    end

    Full --> VA[Alice's View]
    Full --> VB[Bob's View]
    Full --> VC[Charlie's View]

    subgraph VA[Alice's View]
        A1[Alice pays Bob 100]
        A2[Hidden from Alice]
    end

    subgraph VB[Bob's View]
        B1[Alice pays Bob 100]
        B2[Bob pays Charlie 50]
    end

    subgraph VC[Charlie's View]
        C1[Hidden from Charlie]
        C2[Bob pays Charlie 50]
    end
```

### Visibility Rules

1. **Signatories see the contract**, consuming, and non-consuming choices exercised on it
2. **Observers see the contract** and consuming choices exercised on it
3. **Controllers see choices** they can exercise and their consequences

## Contract Keys

<Note>
  Contract keys are under development and planned for Canton 3.5.
</Note>

Contracts can have **keys**—identifiers that allow lookup without knowing the contract ID.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Account
  with
    bank : Party
    owner : Party
    accountNumber : Text
  where
    signatory bank
    observer owner

    key (bank, accountNumber) : (Party, Text)
    maintainer key._1  -- bank maintains the key
```

They support **lookup** so you can find a contract by its key without knowing the contract ID. Every key has a **maintainer**, the party responsible for the key.

<Warning>
  Keys are global within a synchronizer. Design keys carefully to avoid leaking information about contract existence.
</Warning>

## Ledger Time

Canton uses **ledger time** for contract operations. Time is:

* Assigned by the synchronizer
* Monotonically increasing per synchronizer
* Used for time-based contract logic

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice ClaimAfterDeadline : ()
  controller beneficiary
  do
    assertDeadlineExceeded "claim-after-deadline" deadline
    -- ... claim logic
```

See [Working with Time](/docs/canton/appdev-modules-m3-working-with-time) for the full set of time primitives available in Canton 3.x.

## Composability

The UTXO model enables **atomic composition**—multiple contracts can be affected in a single transaction, all-or-nothing.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Atomic swap: both transfers happen or neither does
choice ExecuteSwap : ()
  controller buyer
  do
    exercise assetId Transfer with newOwner = buyer
    exercise paymentId Transfer with newOwner = seller
```

The ledger enforces this atomicity — either the entire swap commits or none of it does.

## Related Topics

* [Contract Templates](/docs/canton/appdev-modules-m3-contract-templates) — write your first Daml contracts
* [Choices](/docs/canton/appdev-modules-m3-choices) — add behavior to contracts
* [Privacy Model](/docs/canton/overview-learn-privacy-model) — how views enable privacy

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
