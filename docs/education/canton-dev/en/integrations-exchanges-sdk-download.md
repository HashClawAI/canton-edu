---
title: "Exchange SDK Download"
slug: "integrations-exchanges-sdk-download"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/exchanges/sdk-download.md"
source_title: "Exchange SDK Download"
tags:
  - integrations
  - exchanges
  - sdk-download
---

# Exchange SDK Download

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Exchange SDK Download

> Download tools and sample code for integrating exchanges with Canton Network

Exchange integrations use the Wallet SDK, the Canton Network Token Standard, and the Ledger API to implement deposit and withdrawal workflows for Canton Coin and other CN tokens.

## Integration Support Code

Use the following support code to simplify your integration development:

* **JavaScript/TypeScript** — Use the functions from the [Wallet SDK](https://github.com/canton-network/wallet-gateway) to simplify building your integration
* **Java/JVM** — Use the sample code from the [ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings) repository as a starting point
* **Other languages** — Use the Wallet SDK or Java sample code as a blueprint

## Wallet SDK (TypeScript)

The primary integration library. Install via npm:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm install @canton-network/wallet-sdk
```

The SDK provides:

* Token Standard transaction preparation and parsing
* Transfer preapproval management
* Transaction history ingestion helpers
* Scan API client for reading Canton Coin registry data

## Java Sample Code

The Java sample repository demonstrates how to interact with the JSON Ledger API from JVM languages:

* **Repository:** [digital-asset/ex-java-json-api-bindings](https://github.com/digital-asset/ex-java-json-api-bindings)

## Integration Milestones

The exchange integration guide is structured as incremental milestones:

1. **Canton Coin (CC) with 1-step withdrawal** — Deposit and withdrawal of CC using TransferPreapprovals. Includes earning app rewards for CC deposits.

2. **All CN Tokens** — Support for all Canton Network tokens (not just CC). Adds multi-step transfers that give receivers the choice to reject incoming transfers and enable asynchronous checks (KYC/AML).

3. **App rewards for all CN tokens** — Earn application rewards on both withdrawals and deposits of all CN tokens, with optional reward sharing with customers.

## Next Steps

* [Exchange Integration Guidance](/integrations/exchanges/guidance) — Workflows, architecture, and deployment

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
