---
title: "Canton Network QuickStart"
slug: "appdev-quickstart-index"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/quickstart/index.md"
source_title: "Canton Network QuickStart"
tags:
  - appdev
  - quickstart
  - index
---

# Canton Network QuickStart

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Network QuickStart

> Get a complete Canton Network application running locally with the cn-quickstart project

The [Canton Network QuickStart](https://github.com/digital-asset/cn-quickstart) (cn-quickstart) is a reference application that gives you a working Canton Network setup on your local machine. It includes a Daml model, a Java backend service, a React frontend, a local Canton sandbox with simulated Global Synchronizer nodes, and developer tooling to build and test your own applications.

The QuickStart demonstrates a software licensing workflow where an App Provider creates licenses for App Users, who can request renewals and make payments using Canton Coin. This workflow covers the core patterns you'll use in production Canton Network applications: multi-party agreements, propose-accept flows, and token transfers.

## What you'll get

The QuickStart sets up a local environment (called LocalNet) with:

* **A simulated Canton Network** with a super-validator node, sequencer, and mediator
* **An App Provider node** running a participant node with the licensing application
* **An App User node** running a separate participant with a wallet
* **A React frontend** for both provider and user roles
* **A Java backend** service handling Ledger API interactions
* **Canton Coin wallets** for traffic purchase and payment flows
* **Log analysis** with [lnav](/appdev/quickstart/lnav) for debugging and troubleshooting

## Pages in this section

<CardGroup cols={2}>
  <Card title="Prerequisites and Installation" icon="download" href="/appdev/quickstart/prerequisites">
    System requirements, dependencies, and step-by-step installation
  </Card>

  <Card title="Project Structure" icon="folder-tree" href="/appdev/quickstart/project-structure">
    How the QuickStart project is organized and what each component does
  </Card>

  <Card title="Running the Demo" icon="play" href="/appdev/quickstart/running-the-demo">
    Start the application and walk through the licensing workflow
  </Card>
</CardGroup>

## Before you start

The QuickStart assumes familiarity with the concepts from Module 1 (understanding Canton) and ideally Module 3 (Daml smart contracts). You don't need to be a Daml expert to run the demo, but understanding templates, choices, and multi-party authorization will help you make sense of what the application is doing.

<Note>
  The QuickStart repository is the recommended starting point for building your own Canton Network application. After running the demo, you can modify the Daml model, backend, and frontend to implement your own business logic.
</Note>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
