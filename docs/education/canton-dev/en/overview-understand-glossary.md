---
title: "Glossary"
slug: "overview-understand-glossary"
locale: "en"
category: "overview"
source_url: "https://docs.canton.network/overview/understand/glossary.md"
source_title: "Glossary"
tags:
  - overview
  - understand
  - glossary
---

# Glossary

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Glossary

> Authoritative terminology reference for Canton Network concepts

## A

### Active Contract Set (ACS)

The set of contracts currently active (not archived) on a participant node for its hosted parties. The ACS represents the current state from that participant's perspective.

**Related**: Contract, Archive, Participant Node

### Admin API

The administrative API exposed by Canton nodes for operational tasks like party management, package uploads, and node configuration. Separate from the Ledger API used by applications.

**Related**: Ledger API, Participant Node

### Archive

The action of consuming/deleting a contract. Archived contracts can no longer be acted upon. In Daml, exercising a consuming choice archives the contract.

**Related**: Contract, Choice, Active Contract Set

## C

### Canton

The blockchain protocol and software implementing privacy-preserving distributed ledger technology. Canton is the underlying technology; Canton Network is the public network running it.

**Related**: Canton Network, Synchronizer, Participant Node

### Canton Coin (CC)

The native utility token of the Global Synchronizer, used for transaction fees (traffic) and validator rewards. Formerly referred to as "Amulet" in some contexts.

**Related**: Traffic, Global Synchronizer, Splice

### Canton Console

Interactive command-line interface for administering Canton nodes. Provides Scala-based scripting for operational tasks like party management, package deployment, and debugging.

**Related**: Admin API, Participant Node

### Canton Network

The public blockchain network running on Canton protocol, coordinated by the Global Synchronizer and operated by Super Validators.

**Related**: Canton, Global Synchronizer, Super Validator

### Choice

An action that can be exercised on a Daml contract. Choices are controlled by specific parties and can be:

* **Consuming**: Archives the contract when exercised
* **Non-consuming**: Leaves the contract active

**Related**: Contract, Template, Controller

### Confirming Participant Node (CPN)

A participant node with permission to confirm transactions on behalf of a party it hosts. Part of the transaction confirmation protocol.

**Related**: Participant Node, Transaction

### Contract

An instance of a template on the ledger. Contracts are immutable—changes create new contracts and archive old ones. Each contract has a unique contract ID.

**Related**: Template, Archive, Contract ID

### Contract ID

A unique identifier for a contract instance on the ledger. Used to reference specific contracts in choices and transactions.

**Related**: Contract, Contract Key

### Contract Key

A unique identifier for looking up contracts without knowing their contract ID. Keys must be unique within their template scope and have privacy implications—key structures can reveal information.

**Related**: Contract, Contract ID, Privacy

### Controller

A party authorized to exercise a specific choice on a contract. Declared in the template definition using the `controller` keyword.

**Related**: Choice, Signatory, Observer

## D

### Daml

The smart contract language used on Canton. A functional programming language designed for multi-party workflows with built-in authorization and privacy. Compiles to Daml-LF.

**Related**: Template, Choice, Daml-LF

### Daml-LF

Daml Ledger Format—the compiled bytecode format for Daml contracts. The intermediate representation that runs on Canton participant nodes.

**Related**: Daml, DAR

### DAR (Daml Archive)

A compiled package of Daml code (templates, data types, etc.) ready for deployment to a participant node. Created by `daml build`.

**Related**: Daml, Daml-LF, Package

### DevNet

The development/testing environment for Canton Network. Requires VPN access and Super Validator sponsorship. Uses test Canton Coin from faucet.

**Related**: TestNet, MainNet, LocalNet

### Divulgence

The automatic disclosure of contract information to parties who weren't original stakeholders but became involved through transaction composition. Happens when contracts are fetched in transactions.

**Related**: Privacy, Observer, Sub-transaction Privacy

### DSO (Decentralized Synchronizer Operator)

The collective of Super Validators actively operating nodes in a decentralized synchronizer. Makes governance decisions and operates infrastructure.

**Related**: Super Validator, Global Synchronizer

### DSO Party

A special party construct used to collect signatures for joint actions and maintain synchronization infrastructure for the DSO.

**Related**: DSO, Party

## E

### External Party

A party that holds its own signing keys externally to the participant node, requiring explicit signatures for transactions. Analogous to an externally owned account (EOA) in Ethereum. Provides more control but requires external signing flow.

**Related**: Local Party, Party

## G

### Global Synchronizer

The public, decentralized synchronizer operated by Super Validators, serving as the backbone of Canton Network. Governed by the Global Synchronizer Foundation.

**Related**: Synchronizer, Super Validator, Global Synchronizer Foundation

### Global Synchronizer Foundation (GSF)

The independent, non-profit body under Linux Foundation that governs the Global Synchronizer. Sets network policies, coordinates upgrades, and oversees Super Validator participation.

**Related**: Global Synchronizer, Super Validator

### gRPC

The primary protocol for the Ledger API, using Protocol Buffers for serialization. Higher performance than JSON API.

**Related**: Ledger API, JSON Ledger API

## H

### Hosting

The relationship between a participant node and the parties it hosts. A participant stores data for and acts on behalf of its hosted parties.

**Related**: Participant Node, Party

## I

### Interface

A Daml construct that defines a set of choices that multiple templates can implement. Enables polymorphic contract handling.

**Related**: Template, Choice

## J

### JSON Ledger API

HTTP/JSON variant of the Ledger API. Simpler to use than gRPC but with some performance overhead. Often used for browser-based applications.

**Related**: Ledger API, gRPC

### JWT (JSON Web Token)

The authentication mechanism used by Canton APIs. Tokens encode party identity and permissions.

**Related**: Ledger API, Admin API

## L

### Ledger API

The primary API exposed by participant nodes for submitting commands and reading ledger data. Available in gRPC and JSON formats. Used by applications to interact with the ledger.

**Related**: gRPC, JSON Ledger API, Admin API

### Local Party

A party whose keys are held by the hosting participant node, allowing the node to sign on the party's behalf. Simpler than external parties but gives validator full control.

**Related**: External Party, Party, Participant Node

### LocalNet

A local development environment running Canton components on your machine. No external network required; uses simulated Canton Coin.

**Related**: DevNet, TestNet, MainNet

## M

### MainNet

The production environment for Canton Network. Uses real Canton Coin with economic value. Requires full onboarding process.

**Related**: DevNet, TestNet, LocalNet

### Mediator

A synchronizer component that facilitates the transaction confirmation protocol by collecting confirmations from participants and declaring transaction outcomes (committed or rejected).

**Related**: Synchronizer, Sequencer, Transaction

## N

### Namespace

The cryptographic scope defined by a key fingerprint. Parties and other topology entities exist within namespaces. Controls who can modify topology for entities in that namespace.

**Related**: Party, Topology Transaction

## O

### Observer

A party that can see a contract but cannot exercise choices on it (unless also declared as controller). Declared explicitly in templates using the `observer` keyword.

**Related**: Signatory, Controller, Privacy

### Offset

A position in the ledger's transaction stream. Used for pagination and resumption when reading from the Ledger API.

**Related**: Ledger API, Transaction

## P

### Package

A collection of compiled Daml modules (templates, data types) deployed to participant nodes. Packaged as DAR files.

**Related**: DAR, Template, Vetting

### Participant Node

A node that hosts parties, stores their contract data, validates transactions, and participates in the Canton protocol. Also called "validator node" in Canton Network context.

**Related**: Validator Node, Party, Hosting

### Party

An on-ledger identity in Canton, analogous to an address or account. Formatted as `name::fingerprint` where fingerprint is derived from the party's public key.

**Related**: Local Party, External Party, Signatory

### PQS (Participant Query Store)

An optional component providing SQL-based querying of ledger data for performance-intensive applications. Maintains a PostgreSQL database synchronized with ledger state.

**Related**: Ledger API, Active Contract Set

### Pruning

The process of removing old, no longer needed data from a participant's storage to manage growth. Pruned data is no longer queryable but the ledger remains valid.

**Related**: Participant Node, Active Contract Set

## S

### Sequencer

A synchronizer component that orders messages from participants and distributes them to recipients. Provides total ordering without seeing decrypted message content.

**Related**: Synchronizer, Mediator

### Signatory

A party that must authorize contract creation and is liable for contract obligations. Signatories always see the contract and any actions on it.

**Related**: Observer, Controller, Template

### Splice

The open-source project (under Hyperledger Labs) providing infrastructure for operating, funding, and governing decentralized Canton synchronizers. Implements Canton Coin and related applications.

**Related**: Canton Coin, Global Synchronizer, DSO

### Stakeholder

A party with a stake in a contract—either as signatory or observer. Stakeholders receive transaction views for contracts they have stake in.

**Related**: Signatory, Observer, View

### Sub-transaction Privacy

Canton's core privacy feature—decomposing transactions into views where each party sees only their relevant portion. Participants see neither content nor metadata for views they're not entitled to.

**Related**: View, Privacy, Transaction

### Super Validator (SV)

An entity operating nodes in the Global Synchronizer's decentralized infrastructure. Super Validators run sequencer/mediator nodes, participate in governance, and sponsor new validators.

**Related**: Global Synchronizer, DSO, Validator Node

### Synchronizer

The coordination layer that orders transactions and facilitates consensus between participant nodes. Consists of sequencer(s) and mediator(s). Does not store transaction content.

**Related**: Sequencer, Mediator, Global Synchronizer

## T

### Template

A Daml definition specifying contract data, signatories, observers, and choices. Contracts are instances of templates. Analogous to a class in object-oriented programming.

**Related**: Contract, Choice, Daml

### TestNet

The staging environment for Canton Network, used for final validation before MainNet deployment. Uses test Canton Coin from faucet.

**Related**: DevNet, MainNet, LocalNet

### Topology Transaction

Transactions that modify network topology—party hosting relationships, key authorizations, synchronizer connections, etc. Managed through the Admin API and Canton Console.

**Related**: Namespace, Party, Admin API

### Traffic

Canton Network's term for transaction fees, paid in Canton Coin. Traffic costs depend on transaction size and complexity.

**Related**: Canton Coin, Transaction

### Transaction

A ledger update consisting of one or more actions (creates, archives, exercises). Transactions are atomic—all actions succeed or all fail.

**Related**: View, Sub-transaction Privacy

### Transaction ID

A unique identifier for a transaction on the ledger. Used for tracking and auditing.

**Related**: Transaction, Contract ID

## U

### Update

A Daml monad representing ledger operations (create, exercise, fetch). The core building block of Daml transaction logic.

**Related**: Daml, Transaction

### User

An identity in the authentication layer (JWT) that maps to one or more parties. Users authenticate to the Ledger API and act as their associated parties.

**Related**: Party, JWT, Ledger API

## V

### Validator Node

A node that hosts parties, stores their contract data, validates transactions, and participates in the Canton protocol. Used interchangeably with "participant node" in Canton Network context.

**Related**: Participant Node, Super Validator

### Vetting

The process of approving a package for use on a participant. Packages must be vetted before contracts from that package can be created. Provides security control over deployed code.

**Related**: Package, DAR, Participant Node

### View

A portion of a transaction visible to a specific party or set of parties. Sub-transaction privacy is implemented through views—each participant receives only the views they're entitled to.

**Related**: Sub-transaction Privacy, Transaction, Stakeholder

## W

### Wallet

A user-facing application for managing Canton Coin and interacting with Canton Network. The Splice project provides reference wallet implementations.

**Related**: Canton Coin, Splice, Wallet SDK

### Wallet SDK

SDK for integrating wallet functionality into applications. Provides APIs for balance queries, transfers, and user management.

**Related**: Wallet, Splice, Ledger API

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
