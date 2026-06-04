---
title: "Integrations Overview"
slug: "integrations-overview"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/overview.md"
source_title: "Integrations Overview"
tags:
  - integrations
  - overview
---

# Integrations Overview

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrations Overview

> Integrate wallets, exchanges, and applications with the Canton Network ecosystem

Integrations connect your applications to Canton Network's ecosystem of wallets, exchanges, tokens, and other services. They provide ready-to-use functionality that application developers can build on and that end users interact with directly.

## Integration Categories

Canton Network provides several categories of integrations:

* **Wallets** — Canton Coin management for users and applications
* **Exchange integration** — Liquidity bridges and fiat on/off ramps
* **Token standards** — Interoperable tokens following [CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)
* **Application integration** — Third-party app connectivity

## For Different Audiences

### For End Users

<CardGroup cols={2}>
  <Card title="Find a Wallet" icon="wallet" href="/docs/canton/integrations-wallets-for-users">
    Discover wallet options for managing your Canton Coin.
  </Card>

  <Card title="Find Apps" icon="grid-2" href="/docs/canton/integrations-apps-finding-apps">
    Explore applications built on Canton Network.
  </Card>
</CardGroup>

### For Developers

<CardGroup cols={2}>
  <Card title="Wallet Integration" icon="code" href="/docs/canton/integrations-wallet-guidance">
    Add wallet functionality to your application using the Wallet SDK.
  </Card>

  <Card title="Exchange Integration" icon="building-columns" href="/docs/canton/integrations-exchanges-guidance">
    Connect exchanges and liquidity providers.
  </Card>
</CardGroup>

## How Canton Integrations Differ from Other Ecosystems

Canton's privacy model changes how integrations work compared to public blockchains.

* **Balances are private** — wallets show holdings only to entitled parties, not the public
* **Transactions are private** — transfers are visible only to participants, not to block explorers
* **Tokens are private** — token balances are visible only to holders
* **Explorers are personal** — Canton explorers show only your transactions, not network-wide activity

<Note>
  Unlike blockchain explorers on Ethereum that show all transactions, Canton explorers show only transactions where you are a stakeholder. This is by design.
</Note>

## Next Steps

<CardGroup cols={2}>
  <Card title="Integration Patterns" icon="puzzle-piece" href="/docs/canton/integrations-integration-patterns">
    Common patterns for building integrations.
  </Card>

  <Card title="Canton Ecosystem" icon="globe" href="/docs/canton/integrations-ecosystem">
    Explore the broader Canton Network ecosystem.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
