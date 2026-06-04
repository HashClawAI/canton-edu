---
title: "SDKs and APIs"
slug: "appdev-modules-m4-sdks-apis"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-sdks-apis.md"
source_title: "SDKs and APIs"
tags:
  - appdev
  - modules
  - m4-sdks-apis
---

# SDKs and APIs

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SDKs and APIs

> Overview of the Canton SDK, code generation, Ledger API, JSON API, PQS, and Wallet SDK

Canton provides a set of tools and APIs for building applications against the ledger. This page covers what each component does and when to use it.

## Canton SDK

The Daml SDK bundles the compiler, code generators, sandbox, and supporting tools you need to develop Canton applications. The main entry point is the `dpm` command-line tool.

Key capabilities of `dpm`:

* `dpm build` -- Compile Daml source code into a DAR file (Daml Archive)
* `dpm codegen-java` -- Generate Java bindings from a compiled DAR
* `dpm codegen-js` -- Generate TypeScript/JavaScript bindings from a compiled DAR
* `dpm sandbox` -- Start a local Canton sandbox node for testing
* `dpm test` -- Run Daml Script tests
* `dpm new` -- Scaffold a new project from a template

`dpm` has additional functionality which can be explored by adding the `--help` option, such as `dpm inspect-dar --help` or `dpm test --help`

The SDK also includes the Daml Studio VS Code extension for syntax highlighting, type checking, and error diagnostics.

## Code Generation

Code generation produces type-safe client bindings from your Daml model. Instead of constructing raw gRPC messages or JSON payloads by hand, you work with generated classes that mirror your templates and choices.

### Java Bindings

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-java .daml/dist/<project>.dar -o generated-java
```

The generated Java classes integrate with the gRPC Ledger API client. Each Daml template becomes a Java class with methods for creating contracts and exercising choices. The cn-quickstart backend uses these bindings through the codegen capabilities.

### TypeScript Bindings

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm codegen-js .daml/dist/<project>.dar -o generated-ts
```

The generated TypeScript types can be used in a Node.js backend or in a frontend that submits commands directly to the Ledger API. In a fully mediated architecture (like cn-quickstart), the frontend instead uses the backend's REST API and doesn't need these bindings directly.

## Ledger API (gRPC)

The Ledger API is the primary interface for submitting commands and reading transactions. It is accessible via the gRPC or JSON API transport exposed by the validator's participant node.

The Ledger API provides:

* **Command submission** -- Create contracts and exercise choices. Commands are submitted as a party acting on the ledger, and the validator processes them through the synchronizer.
* **Transaction stream** -- Subscribe to a stream of committed transactions for one or more parties. Your backend processes these events to keep its state up to date.
* **Active contract set** -- Query the currently active contracts visible to a party.
* **Package management** -- Upload DAR files to a validator.
* **User and party management** -- Create and admin parties on the validator.

The Ledger API uses TLS and token-based authentication in production environments. On LocalNet, authentication can be configured through Keycloak or disabled entirely for faster experimentation.

## JSON API

In Canton 3.x, the JSON API is integrated into the validator. It provides an HTTP/JSON interface to the Ledger API. Architecturally, the JSON API LAPI endpoint translates all of its calls to flow through the gRPC LAPI endpoint.

Use the JSON API when:

* You want simpler HTTP integration without a gRPC client
* You are prototyping and want to test commands with `curl`
* Your language or platform has limited gRPC support

The JSON API supports the same operations as the Ledger API (command submission, active contracts, transaction stream) but through HTTP endpoints and JSON payloads. In cn-quickstart, the JSON API is available on port `x975` for each validator (e.g., `2975` for the App User validator).

For production backends that need very high throughput, the gRPC Ledger API is the better choice because it avoids the serialization overhead of the JSON translation layer.

## Participant Query Store (PQS)

PQS is a service that subscribes to a validator's transaction stream and projects contract data into a PostgreSQL database. Your backend queries this database with standard SQL.

PQS is the right choice when you need:

* Filtered queries across many contracts (e.g., "all licenses expiring this month")
* Aggregations and reporting
* Full-text search or complex joins
* A read path that doesn't load the Ledger API

PQS keeps its PostgreSQL tables synchronized with the ledger. As contracts are created and archived on the ledger, PQS updates the corresponding rows. Your SQL queries always reflect the current ledger state (with a small propagation delay).

In the cn-quickstart project, the backend's `repository/` and `pqs/` modules demonstrate how to query PQS tables for contract data.

## Wallet SDK

The Wallet SDK provides integration with Canton Coin (CC) wallets for applications that need to handle payments or traffic management. Through the wallet integration, your application can:

* Initiate CC transfers between parties
* Create payment requests tied to application workflows (e.g., license renewals)
* Check wallet balances

In cn-quickstart, the licensing application uses wallet integration for license renewal payments. The `LicenseRenewalRequest` contract implements the Splice `AllocationRequest` interface, which the wallet system detects and processes as a payment.

For more on how CC and traffic work, see [Canton Coin and Traffic](/appdev/modules/m4-canton-coin).

## Working Examples

The [cn-quickstart](https://github.com/digital-asset/cn-quickstart) repository demonstrates all of these components working together:

* Daml contracts in `daml/` compiled with `dpm build`
* Java backend in `backend/` using generated bindings and PQS
* React frontend in `frontend/` consuming the backend's REST API
* LocalNet with validators, PQS, JSON API, and wallet services running via Docker Compose

Clone the repository and run `cd quickstart && make setup && make build && make start` to see the full stack in action.

## Next Steps

* [Backend Development](/appdev/modules/m4-backend-dev) -- Patterns for using the Ledger API and PQS in a Java backend
* [Frontend Development](/appdev/modules/m4-frontend-dev) -- Building a React frontend against the backend API

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
