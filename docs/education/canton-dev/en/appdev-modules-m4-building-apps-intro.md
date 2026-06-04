---
title: "Building Applications"
slug: "appdev-modules-m4-building-apps-intro"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-building-apps-intro.md"
source_title: "Building Applications"
tags:
  - appdev
  - modules
  - m4-building-apps-intro
---

# Building Applications

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Building Applications

> Go from Daml smart contracts to full-stack Canton Network applications

Module 4 bridges the gap between writing Daml contracts and shipping a complete application. You will learn how Canton applications are structured, which SDKs and APIs are available, and how to build both backend and frontend components that interact with the ledger.

## Prerequisites

Before starting this module, you should have completed [Module 3: Daml Smart Contracts](/docs/canton/appdev-modules-m3-dev-environment). You need a working understanding of templates, choices, and authorization in Daml. Familiarity with Java or TypeScript is helpful but not required.

## What You Will Learn

* How Canton application architecture maps roles (App Provider, App User, End User) to infrastructure
* Which SDKs, APIs, and code generation tools are available for building against the ledger
* How to build a backend service that submits commands and reads transactions
* How to build a frontend that displays contract data and integrates with wallets
* How Canton Coin and traffic work from an application developer's perspective

## Module Pages

<CardGroup cols={2}>
  <Card title="Application Architecture" icon="sitemap" href="/docs/canton/appdev-modules-m4-app-architecture">
    Roles, layers, and how the pieces of a Canton application fit together.
  </Card>

  <Card title="SDKs and APIs" icon="plug" href="/docs/canton/appdev-modules-m4-sdks-apis">
    Code generation, Ledger API, JSON API, PQS, and the Wallet SDK.
  </Card>

  <Card title="Backend Development" icon="server" href="/docs/canton/appdev-modules-m4-backend-dev">
    Connect to the ledger, submit commands, read transactions, and query PQS.
  </Card>

  <Card title="Frontend Development" icon="browser" href="/docs/canton/appdev-modules-m4-frontend-dev">
    Build a React UI with generated TypeScript bindings and wallet integration.
  </Card>

  <Card title="Canton Coin and Traffic" icon="coins" href="/docs/canton/appdev-modules-m4-canton-coin">
    Understand how CC buys traffic and how to manage transaction costs.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
