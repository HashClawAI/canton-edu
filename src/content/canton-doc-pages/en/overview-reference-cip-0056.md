---
title: "CIP-0056: Canton Network Token Standard"
slug: "overview-reference-cip-0056"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/reference/cip-0056.md"
source_title: "CIP-0056: Canton Network Token Standard"
tags:
  - overview
  - reference
  - cip-0056
---

# CIP-0056: Canton Network Token Standard

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# CIP-0056: Canton Network Token Standard

> Reference for CIP-0056, the standard Daml interfaces for token holdings, transfers, and allocations on Canton Network

[CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) defines the Canton Network Token Standard -- a set of Daml interfaces and off-ledger APIs that allow wallets and applications to interact with tokenized assets across registries in a uniform way. Any registry that implements CIP-0056 can be served by any compliant wallet, and any application can orchestrate transfers and settlements without depending on registry-specific code.

The Splice wallet implements CIP-0056 for Canton Coin (CC), where the underlying Daml template is called `Amulet`. Other asset registries on Canton Network can implement the same interfaces for their own instruments.

## What CIP-0056 Standardizes

The standard covers three categories of functionality:

* **Portfolio view** -- Display a party's current holdings, transaction history, and instrument metadata across multiple registries.
* **Direct peer-to-peer (FOP) transfers** -- Move assets from one party to another, either in a single step or through a two-step offer/accept flow.
* **Delivery-versus-payment (DvP) settlements** -- Lock assets into allocations so that a multi-leg settlement can execute atomically.

Six on-ledger Daml APIs and their corresponding off-ledger (HTTP) registry APIs support these capabilities:

* **Token Metadata** -- instrument symbol, name, total supply, and registry UI URLs
* **Holding** -- portfolio view and transaction history
* **Transfer Instruction** -- direct FOP transfers
* **Allocation** -- asset reservations for DvP
* **Allocation Request** -- standardized app-to-wallet allocation requests
* **Allocation Instruction** -- standardized wallet-to-registry allocation creation

## Core Interfaces

### Token Metadata

The Token Metadata API lets wallets retrieve descriptive information about an instrument without knowing the registry's internal data model. The registry exposes metadata such as the instrument's display name, symbol, total supply, and URLs for the registry's UI. Wallets query this through the registry's off-ledger HTTP endpoint.

### Holding

The `Holding` interface represents a single token holding -- one entry in a party's portfolio. Its view exposes:

* `owner` -- the party that owns the holding
* `instrumentId` -- a globally unique identifier combining an `admin` party (the registry) and an `id` text string
* `amount` -- the size of the holding as a `Decimal`
* `lock` -- an optional `Lock` with holder parties, expiry times, and a human-readable context string
* `meta` -- key-value metadata following Kubernetes annotation conventions

Each `Holding` contract is an individual UTXO on the ledger. You query holdings through the Ledger API's active-contracts endpoint, filtering by the `Holding` interface ID (e.g., `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding`).

### TransferFactory and TransferInstruction

`TransferFactory` is a non-consuming factory contract maintained by the registry. Your wallet fetches it from the registry's off-ledger API and exercises its `TransferFactory_Transfer` choice to initiate a transfer. The choice takes a `Transfer` record specifying the sender, receiver, amount, instrument, input holdings, and a deadline (`executeBefore`).

Depending on the registry's implementation, the result is either:

* **Completed** -- the transfer settled immediately, and the receiver's new holdings are returned.
* **Pending** -- a `TransferInstruction` contract was created, requiring further action.
* **Failed** -- the transfer could not be completed and input holdings (minus any fees) were returned to the sender.

When a `TransferInstruction` is created, it tracks the state of an in-progress transfer. The receiver can exercise `TransferInstruction_Accept` or `TransferInstruction_Reject`; the sender can exercise `TransferInstruction_Withdraw`. The registry can advance internal workflow steps through `TransferInstruction_Update`.

### Allocation and AllocationFactory

Allocations support multi-leg settlements (DvP). An `Allocation` contract represents a reservation of assets to a specific leg of a settlement, backed by locked holdings.

The `AllocationView` contains:

* `allocation` -- an `AllocationSpecification` that references the settlement info, a transfer leg ID, and the transfer leg itself (sender, receiver, amount, instrument)
* `holdingCids` -- the holdings backing this allocation
* `meta` -- extensibility metadata

You create allocations by fetching an `AllocationFactory` from the registry and exercising `AllocationFactory_Allocate`. Use the [Token Standard API](/overview/reference/splice-wallet-reference#wallet-api-endpoints) to discover and interact with allocation contracts. The settlement's `executor` party, along with the sender and receiver, jointly control the allocation. Three choices govern its lifecycle:

* `Allocation_ExecuteTransfer` -- execute the transfer of allocated assets (the settlement step)
* `Allocation_Cancel` -- release the allocation early, controlled jointly by sender, receiver, and executor
* `Allocation_Withdraw` -- the sender reclaims the assets before the `allocateBefore` deadline

The `AllocationInstruction` interface tracks multi-step allocation creation, similar to how `TransferInstruction` tracks multi-step transfers.

### Allocation Request

The `AllocationRequest` interface standardizes how an application asks a wallet to allocate assets. An app creates an allocation request specifying the settlement details and transfer leg; the user's wallet then funds it by exercising the appropriate `AllocationFactory` choice. This decouples the app's settlement logic from the wallet's holding management.

## Transfer Models

### One-Step Transfers

A one-step transfer completes within a single Daml transaction. When you exercise `TransferFactory_Transfer` and the registry can settle immediately, the result is `TransferInstructionResult_Completed` with the receiver's new holdings.

For Canton Coin, one-step transfers work when the receiver has set up a `TransferPreapproval` contract. The preapproval signals that the receiver agrees to accept incoming CC from any sender without per-transfer consent. Each preapproval has a `receiver` party and a `provider` party; the provider pays a fee proportional to the preapproval's lifetime and earns app rewards on incoming transfers that use it. Preapprovals expire and must be renewed periodically -- the validator app handles this automatically when the provider is the validator operator.

The Splice wallet and Token Standard registry APIs detect existing preapprovals and route transfers through them automatically. Other registries may implement their own one-step transfer mechanisms or always require two-step flows.

### Two-Step Transfers

When the receiver has no preapproval, or when the registry requires additional authorization, a transfer goes through two steps:

1. **Instruct** -- The sender exercises `TransferFactory_Transfer`. The registry creates a `TransferInstruction` contract in `TransferPendingReceiverAcceptance` status. The sender's input holdings are consumed, and the funds are held by the registry.
2. **Accept** -- The receiver exercises `TransferInstruction_Accept` on the pending instruction. The registry completes the transfer and creates holdings for the receiver.

The receiver can also reject the instruction (`TransferInstruction_Reject`), which returns the funds to the sender. The sender can withdraw before acceptance (`TransferInstruction_Withdraw`). Both paths are designed so that wallets can parse the transaction history and determine whether any given instruction succeeded or failed.

Two-step transfers do not require sender-side automation after the initial instruction, making them well suited for external parties that sign transactions with keys they control. Since [CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md), two-step CC transfers incur no fees.

### DvP Settlements Using Allocations

When a settlement involves multiple legs across different instruments or registries, each sender allocates their assets independently:

1. An application creates a settlement specification with an `executor` party, a deadline (`allocateBefore`), and a settlement deadline (`settleBefore`).
2. Each sender's wallet exercises `AllocationFactory_Allocate` to lock holdings into an `Allocation` contract for their respective transfer leg.
3. Once all legs are allocated, the executor exercises `Allocation_ExecuteTransfer` on each allocation to complete the settlement atomically.

If a sender fails to allocate before the deadline, the executor can cancel the remaining allocations. Senders can also withdraw their allocations before the `allocateBefore` time to reclaim their holdings.

## UTXO Management

Analogous to Bitcoin, Canton uses a UTXO model, where the UTXOs are all the active contracts that implement the `Holding` interface.

Active `Holding` contracts incur both storage and compute cost on the validator nodes hosting users that own `Holding` contracts and the validator nodes hosting the token administrator. To make efficient use of the network's resources, wallet providers should aim to keep the number of UTXOs per user low -- below roughly 10 UTXOs per user on average.

This also optimizes traffic costs, as each UTXO input to a transfer costs extra traffic. Furthermore, this recommendation aligns with the incentives put in place by tokens like Canton Coin, which:

* allows at most 100 input contracts for a single transfer, and thus discourages excessive splitting of holdings
* expires coin UTXOs whose initial amount is lower than the accrued holding fee, and thus discourages the creation of dust UTXOs

Wallet providers should prefer selecting small-amount `Holding` UTXOs as inputs to transfers, and set up `MergeDelegation` contracts during user onboarding so that the wallet can automatically merge small UTXOs on the user's behalf. The Splice `splice-util-token-standard-wallet.dar` package provides `MergeDelegation` and `BatchMergeUtility` templates for this purpose.

## Registry and Discovery

Each token instrument is administered by a registry -- an application that maintains ownership records and exposes both on-ledger Daml interfaces and off-ledger HTTP APIs. The registry's `admin` party appears in every `InstrumentId` and every factory contract's view.

To execute a factory choice, you first query the registry's off-ledger API to obtain:

* The `factoryId` (the contract ID of the factory)
* `disclosedContracts` (required for the exercise to succeed)
* `choiceContextData` (passed as `context` in the choice argument)

Registry URLs for a given instrument are currently maintained by wallets themselves. A generic discovery mechanism based on the [Canton Name Service](/overview/reference/canton-name-service) is planned, where registry URLs would be stored in CNS entry metadata and retrievable through the Scan API.

The off-ledger APIs do not require authentication. Instead, the security model relies on the unguessability of contract IDs and Canton's need-to-know data distribution -- only parties entitled to see a contract receive it.

## Metadata Conventions

All CIP-0056 interfaces include `Metadata` fields -- key-value text maps for extensibility. Keys follow Kubernetes annotation conventions and should be prefixed with the DNS name of the organization defining the key. For example, the Splice implementation uses keys prefixed with `splice.lfdecentralizedtrust.org/`.

Standard metadata keys used in transaction parsing include:

* `splice.lfdecentralizedtrust.org/tx-kind` -- the operation type (e.g., `transfer`, `merge-split`, `burn`, `mint`, `unlock`, `expire-dust`)
* `splice.lfdecentralizedtrust.org/sender` -- the sending party
* `splice.lfdecentralizedtrust.org/reason` -- a human-readable reason for the operation
* `splice.lfdecentralizedtrust.org/burned` -- the amount of a holding that was burned

The `ExtraArgs` type bundles two structures passed to most choices: a `ChoiceContext` (opaque data from the registry's off-ledger API) and a `Metadata` (caller-provided annotations). The choice context passes registry-internal data into the on-ledger execution; the metadata allows callers and registries to agree on additional semantics.

## Wallet Integration

The [Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk) packages these integration patterns into a reusable library for wallet developers. If you are building a wallet from scratch, the five integration patterns are:

* Reading contracts that implement a Token Standard interface (via the active-contracts endpoint)
* Reading and parsing transaction history involving Token Standard contracts
* Executing a factory choice (fetching the factory from the registry, then submitting to the Ledger API)
* Executing a non-factory choice on an existing contract (e.g., accepting a transfer instruction)
* Calling Token Standard choices from custom Daml code (for bulk operations, merges, or app-specific workflows)

The [Token Standard CLI](https://github.com/canton-network/splice/tree/main/token-standard#cli) demonstrates each of these patterns as executable code and serves as both a testing tool and a reference implementation.

## Further Reading

* [Full CIP-0056 text](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)
* [Token standard source code](https://github.com/canton-network/splice/tree/main/token-standard)
* [Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk)
* [Canton Coin Tokenomics](/overview/reference/canton-coin-tokenomics) -- fee structure and UTXO dust expiry for CC specifically

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
