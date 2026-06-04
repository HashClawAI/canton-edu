---
title: "Development Tools Overview"
slug: "appdev-tooling-development-tools-overview"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/development-tools-overview.md"
source_title: "Development Tools Overview"
tags:
  - appdev
  - tooling
  - development-tools-overview
---

# Development Tools Overview

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Development Tools Overview

> Overview of the Canton development toolchain: DPM, Daml Studio, Canton Console, Sandbox, LocalNet, and PQS

Canton application development involves several tools that handle different parts of the workflow -- from writing and compiling Daml contracts to testing locally and querying ledger state. This page summarizes each tool and when you use it.

## DPM (Daml Package Manager)

DPM is the primary command-line tool for Canton project management. It handles project initialization, dependency management, compilation, code generation, and testing.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm init                  # Create a new project
dpm build                 # Compile Daml contracts to DAR files
dpm test                  # Run Daml Script tests
dpm codegen-js .dar -o out  # Generate TypeScript bindings
dpm codegen-java .dar -o out # Generate Java bindings
dpm sandbox               # Start a local Sandbox node
dpm studio                # Launch Daml Studio (VS Code)
```

DPM replaces the older `daml` CLI and is the recommended entry point for all build and project tasks. See the [DPM reference](/sdks-tools/cli-tools/dpm) for the full command set.

## Daml Studio (VS Code Extension)

Daml Studio is a VS Code extension that provides an IDE experience for writing Daml smart contracts. It includes:

* Real-time type checking and error diagnostics as you type
* Go-to-definition and find-references navigation
* Script results visualization -- run Daml Scripts directly from the editor and inspect the resulting ledger state in a table view
* Code completion for templates, choices, and standard library functions

Install it by running `dpm studio` from a project directory, or search for "Daml" in the VS Code extensions marketplace. Requires VS Code 1.87 or later.

For full setup instructions, see [IDE Setup](/appdev/tooling/ide-setup).

## Canton Console

The Canton Console is an interactive Scala-based REPL for inspecting and managing Canton nodes. You can use it to:

* Query the active contract set (ACS) on a validator
* Inspect transaction trees and event details
* Upload DAR packages to validators
* Manage parties and their hosting
* Check node health and connectivity

The console connects to a running Canton node and provides direct access to administrative and diagnostic operations. It is particularly useful during development for verifying that transactions produced the expected state.

## Sandbox

The Sandbox is a lightweight, single-node Canton environment for rapid local testing. Start it with:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm sandbox
```

Sandbox gives you a local validator with an in-memory ledger. It is fast to start and suitable for running Daml Script tests, experimenting with contract logic, and iterating on Daml code without external dependencies.

Sandbox does not simulate multi-validator or multi-party-on-different-validator scenarios. For that, use LocalNet.

See [Sandbox](/sdks-tools/development-tools/sandbox) for configuration options.

## LocalNet

LocalNet is a Docker Compose-based local environment that simulates the Global Synchronizer with multiple validators. The [cn-quickstart](https://github.com/digital-asset/cn-quickstart) repository packages LocalNet as part of its development setup:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd cn-quickstart/quickstart
make setup
make build
make start
```

LocalNet provides a local synchronizer, multiple validator nodes, test Canton Coin with faucet access, and a Splice wallet. It is the right environment for integration testing, multi-party workflows, and end-to-end application testing before deploying to DevNet.

See [LocalNet](/sdks-tools/development-tools/localnet) for details.

## PQS (Participant Query Store)

PQS maintains a PostgreSQL database synchronized with your validator's ledger state. It projects ledger events (creates, archives, exercises) into SQL tables that you can query with standard SQL.

PQS is useful when you need:

* Complex queries across multiple contract types (joins, aggregations, filters)
* Reporting and analytics over historical ledger data
* Integration with BI tools or dashboards that speak SQL
* Full-text search or custom indexing on contract payloads

PQS respects the same privacy boundaries as the Ledger API -- it contains only the data your party is entitled to see.

See [PQS](/sdks-tools/development-tools/pqs) and the [PQS SQL Reference](/api-reference) for schema details and query examples.

## Choosing the Right Tool

* **Write and compile Daml contracts** -- DPM + Daml Studio
* **Run unit tests for contract logic** -- `dpm test` (Daml Script)
* **Quick local iteration on Daml code** -- Sandbox
* **Multi-validator integration testing** -- LocalNet
* **Inspect contract state interactively** -- Canton Console
* **Complex queries and reporting** -- PQS

## Next Steps

* [IDE Setup](/appdev/tooling/ide-setup) -- Configure your editor for Canton development
* [Debugging Tools](/appdev/tooling/debugging-tools) -- Troubleshoot transactions and contract state
* [The Canton Development Stack](/appdev/modules/m1-development-stack) -- How all the pieces fit together

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
