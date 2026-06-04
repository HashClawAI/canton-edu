---
title: "The Canton Development Stack"
slug: "appdev-modules-m1-development-stack"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m1-development-stack.md"
source_title: "The Canton Development Stack"
tags:
  - appdev
  - modules
  - m1-development-stack
---

# The Canton Development Stack

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# The Canton Development Stack

> Overview of tools and technologies for building on Canton Network

This page introduces the development stack you'll use to build Canton applications. Understanding these components helps you see how everything fits together.

## Stack Overview

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart TB
    subgraph App[Your Application]
        FE[Frontend<br>React, Vue, etc.]
        BE[Backend<br>TypeScript, Java, Python]
        SC[Smart Contracts<br>Daml]
    end

    subgraph Tools[Development Tools]
        SDK[Daml SDK]
        DPM[dpm<br>Package Manager]
        DAML[Daml Compiler]
        SCRIPT[Daml Script]
        VSC[VS Code Extension]
        SANDBOX[Sandbox]
    end

    subgraph Infra[Canton Infrastructure]
        LOCAL[LocalNet<br>Development]
        PART[Participant Node]
        PQS[PQS<br>Query Service]
    end

    SC --> DAML
    DAML --> SDK
    SDK --> LOCAL
    FE --> BE
    BE --> PART
    BE --> PQS
```

## Smart Contract Layer

### Daml

Daml is Canton's smart contract language—a functional language designed for multi-party workflows.

| Aspect          | Details                                  |
| --------------- | ---------------------------------------- |
| **Paradigm**    | Functional programming                   |
| **Type system** | Strongly typed with inference            |
| **Compiles to** | Daml-LF (ledger format)                  |
| **Primary use** | Define contracts, choices, authorization |

**Example:**

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Token
  with
    owner : Party
    issuer : Party
    amount : Decimal
  where
    signatory issuer
    observer owner

    choice Transfer : ContractId Token
      with newOwner : Party
      controller owner
      do create this with owner = newOwner
```

### Daml Compiler

The Daml compiler (`dpm build`) compiles Daml source code into DAR files (Daml Archives) that can be deployed to participant nodes.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Compile Daml code
dpm build

# Output: .dar file containing compiled contracts
```

## Application Layer

### Backend Integration

Your backend connects to Canton via the Ledger API.

| Option       | Protocol      | Best For                          |
| ------------ | ------------- | --------------------------------- |
| **gRPC API** | gRPC/Protobuf | High-performance, typed           |
| **JSON API** | HTTP/JSON     | Simpler integration, web-friendly |

**Language support:**

* TypeScript/JavaScript (code generation available via `dpm codegen-js`)
* Java (code generation available via `dpm codegen-java`)
* Any language via gRPC or JSON API

Community-supported bindings also exist for Python, Rust, and Go.

### Code Generation

Generate type-safe bindings from your Daml code:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate TypeScript bindings
dpm codegen-js .dar -o generated

# Generate Java bindings
dpm codegen-java .dar -o generated
```

Generated code provides:

* Type-safe contract representations
* Command submission helpers
* Event handling utilities

### Frontend

Use any web framework. Common choices:

| Framework   | Notes                           |
| ----------- | ------------------------------- |
| **React**   | Most common in Canton ecosystem |
| **Vue**     | Good alternative                |
| **Angular** | Enterprise preference           |

The frontend typically connects via your backend, which handles Ledger API communication.

## Development Tools

### Daml SDK

The Daml SDK bundles everything needed for Canton development:

| Component          | Purpose                              |
| ------------------ | ------------------------------------ |
| **Daml compiler**  | Compile smart contracts              |
| **Daml Script**    | Test and interact with contracts     |
| **Sandbox**        | Run a single Canton node for testing |
| **Canton runtime** | Run local participant nodes          |
| **Console**        | Interactive administration           |
| **Templates**      | Project scaffolding                  |

### dpm (Daml Package Manager)

Manage dependencies and build workflows:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Initialize project
dpm init

# Add dependency
dpm add package-name

# Build
dpm build
```

### VS Code Extension

The Daml VS Code extension (Daml Studio) provides:

* Syntax highlighting
* Type checking
* Error diagnostics
* Code navigation
* Integrated terminal

The extension is installed automatically with DPM. You need VS Code 1.87 or above. To launch Daml Studio, run `dpm studio` from your project directory.

## Infrastructure Components

### LocalNet

LocalNet is a local Global Synchronizer simulation for development:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Start LocalNet (via QuickStart)
make setup
make build
make start

# Or run a single Canton node via Daml SDK
dpm sandbox
```

LocalNet provides:

* Local synchronizer
* Local participant node(s)
* Test Canton Coin
* No external dependencies

### Participant Node

The participant node is the portion of the validator that hosts the Canton runtime which:

* Hosts your parties
* Stores contract data
* Executes Daml logic
* Exposes the Ledger API

In production, this runs as part of your validator.

### PQS (Participant Query Store)

PQS provides SQL-based querying for complex data access:

| Use Case             | Ledger API | PQS       |
| -------------------- | ---------- | --------- |
| Simple queries       | Good       | Good      |
| Complex aggregations | Limited    | Excellent |
| Reporting            | Difficult  | Easy      |
| Real-time updates    | Excellent  | Excellent |

PQS maintains a PostgreSQL database synchronized with ledger state.

## Development Workflow

### Typical Flow

```mermaid theme={"theme":{"light":"github-light","dark":"github-dark"}}
flowchart LR
    WRITE[Write Daml] --> COMPILE[Compile]
    COMPILE --> TEST[Test locally]
    TEST --> ITERATE[Iterate]
    ITERATE --> WRITE

    TEST --> DEPLOY[Deploy to DevNet]
    DEPLOY --> VALIDATE[Validate]
    VALIDATE --> PROMOTE[Promote to TestNet]
```

### Steps

1. **Write** Daml contracts defining your business logic
2. **Compile** with `daml build`
3. **Test** locally with Daml Script or LocalNet
4. **Build** backend integration
5. **Deploy** to DevNet for integration testing
6. **Promote** through TestNet to MainNet

## QuickStart Project

The [cn-quickstart](https://github.com/digital-asset/cn-quickstart) repository provides a complete example that includes build tooling:

| Component          | Technology              |
| ------------------ | ----------------------- |
| **Contracts**      | Daml                    |
| **Backend**        | TypeScript              |
| **Frontend**       | React                   |
| **Infrastructure** | Docker Compose LocalNet |

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Clone and run
git clone https://github.com/digital-asset/cn-quickstart
cd cn-quickstart
direnv allow
cd quickstart
make install-daml-sdk
make setup
make build
make start
```

## Tool Comparison with Other Platforms

| Purpose             | Ethereum             | Canton                   |
| ------------------- | -------------------- | ------------------------ |
| **Smart contracts** | Solidity             | Daml                     |
| **Build tool**      | Hardhat/Foundry      | daml build/dpm           |
| **IDE**             | Remix, VS Code       | VS Code + Daml extension |
| **Testing**         | Mocha, Foundry tests | Daml Script              |
| **Local network**   | Hardhat node, Anvil  | LocalNet, Canton Sandbox |
| **API**             | JSON-RPC             | Ledger API (gRPC/JSON)   |
| **Indexing**        | The Graph            | PQS                      |

## Next Steps

<CardGroup cols={2}>
  <Card title="QuickStart" icon="rocket" href="/docs/canton/appdev-quickstart-index">
    Run the example application.
  </Card>

  <Card title="Module 3: Daml" icon="code" href="/docs/canton/appdev-modules-m3-dev-environment">
    Start writing smart contracts.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
