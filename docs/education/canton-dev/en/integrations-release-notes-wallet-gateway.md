---
title: "Wallet Gateway"
slug: "integrations-release-notes-wallet-gateway"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/release-notes/wallet-gateway.md"
source_title: "Wallet Gateway"
tags:
  - integrations
  - release-notes
  - wallet-gateway
---

# Wallet Gateway

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Wallet Gateway

> Release notes for the Canton Network Wallet Gateway

Release notes are reproduced verbatim from the [`@canton-network/wallet-gateway-remote` GitHub releases](https://github.com/hyperledger-labs/splice-wallet-kernel/releases?q=wallet-gateway-remote).

## 1.3.0 — 2026-05-13

### 🧱 Updated Dependencies

* Updated @canton-network/core-signing-dfns to 0.3.0

## 1.2.1 — 2026-05-08

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 1.2.1
* Updated @canton-network/core-wallet-user-rpc-client to 1.2.1
* Updated @canton-network/core-wallet-store-inmemory to 1.2.1
* Updated @canton-network/core-wallet-ui-components to 1.2.1
* Updated @canton-network/core-signing-blockdaemon to 1.2.1
* Updated @canton-network/core-signing-participant to 1.2.1
* Updated @canton-network/core-signing-fireblocks to 1.2.1
* Updated @canton-network/core-signing-store-sql to 1.2.1
* Updated @canton-network/core-signing-internal to 1.2.1
* Updated @canton-network/core-wallet-store-sql to 1.2.1
* Updated @canton-network/core-ledger-client to 1.2.1
* Updated @canton-network/core-rpc-transport to 1.2.1
* Updated @canton-network/core-tx-visualizer to 1.2.1
* Updated @canton-network/core-signing-dfns to 0.2.1
* Updated @canton-network/core-wallet-store to 1.2.1
* Updated @canton-network/core-signing-lib to 1.2.1
* Updated @canton-network/core-wallet-auth to 1.2.1
* Updated @canton-network/core-rpc-errors to 1.2.1
* Updated @canton-network/core-types to 1.2.1

## 1.2.0 — 2026-05-05

### 🚀 Features

* add dfns signing driver ([#1682](https://github.com/canton-network/wallet-gateway/pull/1682))

### 🩹 Fixes

* **wallet-gateway-remote:** support scp scoping in jwt ([#1702](https://github.com/canton-network/wallet-gateway/pull/1702))
* **wallet-gateway-remote:** updates to creating a party in the wallet gateway ([#1676](https://github.com/canton-network/wallet-gateway/pull/1676))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 1.2.0
* Updated @canton-network/core-wallet-user-rpc-client to 1.2.0
* Updated @canton-network/core-wallet-store-inmemory to 1.2.0
* Updated @canton-network/core-wallet-ui-components to 1.2.0
* Updated @canton-network/core-signing-blockdaemon to 1.2.0
* Updated @canton-network/core-signing-participant to 1.2.0
* Updated @canton-network/core-signing-fireblocks to 1.2.0
* Updated @canton-network/core-signing-store-sql to 1.2.0
* Updated @canton-network/core-signing-internal to 1.2.0
* Updated @canton-network/core-wallet-store-sql to 1.2.0
* Updated @canton-network/core-ledger-client to 1.2.0
* Updated @canton-network/core-rpc-transport to 1.2.0
* Updated @canton-network/core-tx-visualizer to 1.2.0
* Updated @canton-network/core-signing-dfns to 0.2.0
* Updated @canton-network/core-wallet-store to 1.2.0
* Updated @canton-network/core-signing-lib to 1.2.0
* Updated @canton-network/core-wallet-auth to 1.2.0
* Updated @canton-network/core-rpc-errors to 1.2.0
* Updated @canton-network/core-types to 1.2.0

### ❤️ Thank You

* Copilot Autofix powered by AI @github-code-quality\[bot]
* Fayi @fayi-da
* Noah
* Phillip Olesen @PHOL-DA

## 1.1.0 — 2026-04-28

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 1.1.1
* Updated @canton-network/core-wallet-user-rpc-client to 1.1.1
* Updated @canton-network/core-wallet-store-inmemory to 1.1.1
* Updated @canton-network/core-wallet-ui-components to 1.1.1
* Updated @canton-network/core-signing-blockdaemon to 1.1.1
* Updated @canton-network/core-signing-participant to 1.1.1
* Updated @canton-network/core-signing-fireblocks to 1.1.1
* Updated @canton-network/core-signing-store-sql to 1.1.1
* Updated @canton-network/core-signing-internal to 1.1.1
* Updated @canton-network/core-wallet-store-sql to 1.1.1
* Updated @canton-network/core-ledger-client to 1.1.1
* Updated @canton-network/core-rpc-transport to 1.1.1
* Updated @canton-network/core-tx-visualizer to 1.1.1
* Updated @canton-network/core-wallet-store to 1.1.1
* Updated @canton-network/core-signing-lib to 1.1.1
* Updated @canton-network/core-wallet-auth to 1.1.1
* Updated @canton-network/core-rpc-errors to 1.1.1
* Updated @canton-network/core-types to 1.1.1

## 0.27.0 — 2026-04-16

### 🚀 Features

* **core-wallet-ui-components:** increased robustness of wallet picker ([#1624](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1624))
* **core-wallet-store:** changed transaction to have unique id ([#1628](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1628))

### 🩹 Fixes

* **wallet-gateway-remote:** missing payload for external signed transaction ([#1632](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1632))
* a few minor fixes ([#1618](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1618))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.33.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.32.0
* Updated @canton-network/core-wallet-store-inmemory to 0.32.0
* Updated @canton-network/core-wallet-ui-components to 0.33.0
* Updated @canton-network/core-signing-blockdaemon to 0.28.0
* Updated @canton-network/core-signing-participant to 0.31.0
* Updated @canton-network/core-signing-fireblocks to 0.28.0
* Updated @canton-network/core-signing-store-sql to 0.32.0
* Updated @canton-network/core-signing-internal to 0.31.0
* Updated @canton-network/core-wallet-store-sql to 0.31.0
* Updated @canton-network/core-ledger-client to 0.36.0
* Updated @canton-network/core-rpc-transport to 0.12.0
* Updated @canton-network/core-tx-visualizer to 0.26.0
* Updated @canton-network/core-wallet-store to 0.31.0
* Updated @canton-network/core-signing-lib to 0.30.0
* Updated @canton-network/core-wallet-auth to 0.27.0
* Updated @canton-network/core-rpc-errors to 0.22.0
* Updated @canton-network/core-types to 0.26.0

### ❤️ Thank You

* Phillip Olesen @PHOL-DA

## 0.26.0 — 2026-04-13

### 🚀 Features

* add CIP-0103 connected and isConnected ([#1609](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1609))
* add externalId if available to activities ([#1588](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1588))

### 🩹 Fixes

* blockdaemon caip2 ([#1611](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1611))
* **wallet-gateway-remote:** rate limit based on key ([#1590](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1590))
* error log serialize object ([#1597](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1597))
* **core-wallet-store:** prevent overwrites of transactions ([#1592](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1592))
* **wallet-gateway-remote:** validate sub against networkidp ([#1589](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1589))
* restore party allocation toasts ([#1594](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1594))
* fix error in blockdaemon allocation ([#1586](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1586))
* remove tx details for signing ([#1572](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1572))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.32.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.31.1
* Updated @canton-network/core-wallet-store-inmemory to 0.31.1
* Updated @canton-network/core-wallet-ui-components to 0.32.0
* Updated @canton-network/core-signing-blockdaemon to 0.27.1
* Updated @canton-network/core-signing-participant to 0.30.1
* Updated @canton-network/core-signing-fireblocks to 0.27.1
* Updated @canton-network/core-signing-store-sql to 0.31.1
* Updated @canton-network/core-signing-internal to 0.30.1
* Updated @canton-network/core-wallet-store-sql to 0.30.1
* Updated @canton-network/core-ledger-client to 0.35.1
* Updated @canton-network/core-rpc-transport to 0.11.1
* Updated @canton-network/core-tx-visualizer to 0.25.1
* Updated @canton-network/core-wallet-store to 0.30.1
* Updated @canton-network/core-signing-lib to 0.29.1
* Updated @canton-network/core-wallet-auth to 0.26.1
* Updated @canton-network/core-rpc-errors to 0.21.1
* Updated @canton-network/core-types to 0.25.1

### ❤️ Thank You

* Chien-An Lin
* Marc Juchli @mjuchli-da
* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.25.0 — 2026-04-02

### 🚀 Features

* configurable log level ([#1559](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1559))
* implement new wallet-gateway ui designs ([#1520](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1520))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.31.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.31.0
* Updated @canton-network/core-wallet-store-inmemory to 0.31.0
* Updated @canton-network/core-wallet-ui-components to 0.31.0
* Updated @canton-network/core-signing-blockdaemon to 0.27.0
* Updated @canton-network/core-signing-participant to 0.30.0
* Updated @canton-network/core-signing-fireblocks to 0.27.0
* Updated @canton-network/core-signing-store-sql to 0.31.0
* Updated @canton-network/core-signing-internal to 0.30.0
* Updated @canton-network/core-wallet-store-sql to 0.30.0
* Updated @canton-network/core-ledger-client to 0.35.0
* Updated @canton-network/core-rpc-transport to 0.11.0
* Updated @canton-network/core-tx-visualizer to 0.25.0
* Updated @canton-network/core-wallet-store to 0.30.0
* Updated @canton-network/core-signing-lib to 0.29.0
* Updated @canton-network/core-wallet-auth to 0.26.0
* Updated @canton-network/core-rpc-errors to 0.21.0
* Updated @canton-network/core-types to 0.25.0

### ❤️ Thank You

* Fayi @fayi-da
* Marc Juchli @mjuchli-da

## 0.24.0 — 2026-03-30

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.30.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.30.0
* Updated @canton-network/core-wallet-store-inmemory to 0.30.0
* Updated @canton-network/core-wallet-ui-components to 0.30.0
* Updated @canton-network/core-signing-blockdaemon to 0.26.0
* Updated @canton-network/core-signing-participant to 0.29.0
* Updated @canton-network/core-signing-fireblocks to 0.26.0
* Updated @canton-network/core-signing-store-sql to 0.30.0
* Updated @canton-network/core-signing-internal to 0.29.0
* Updated @canton-network/core-wallet-store-sql to 0.29.0
* Updated @canton-network/core-ledger-client to 0.34.0
* Updated @canton-network/core-rpc-transport to 0.10.0
* Updated @canton-network/core-tx-visualizer to 0.24.0
* Updated @canton-network/core-wallet-store to 0.29.0
* Updated @canton-network/core-signing-lib to 0.28.0
* Updated @canton-network/core-wallet-auth to 0.25.0
* Updated @canton-network/core-rpc-errors to 0.20.0
* Updated @canton-network/core-types to 0.24.0

## 0.23.1 — 2026-03-27

### 🩹 Fixes

* **core-signing-blockdaemon:** follow up fix with endpoint changes ([#1525](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1525))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.29.1
* Updated @canton-network/core-wallet-user-rpc-client to 0.29.1
* Updated @canton-network/core-wallet-store-inmemory to 0.29.1
* Updated @canton-network/core-wallet-ui-components to 0.29.1
* Updated @canton-network/core-signing-blockdaemon to 0.25.2
* Updated @canton-network/core-signing-participant to 0.28.1
* Updated @canton-network/core-signing-fireblocks to 0.25.2
* Updated @canton-network/core-signing-store-sql to 0.29.1
* Updated @canton-network/core-signing-internal to 0.28.1
* Updated @canton-network/core-wallet-store-sql to 0.28.1
* Updated @canton-network/core-ledger-client to 0.33.1
* Updated @canton-network/core-rpc-transport to 0.9.2
* Updated @canton-network/core-tx-visualizer to 0.23.2
* Updated @canton-network/core-wallet-store to 0.28.1
* Updated @canton-network/core-signing-lib to 0.27.2
* Updated @canton-network/core-wallet-auth to 0.24.2
* Updated @canton-network/core-rpc-errors to 0.19.2
* Updated @canton-network/core-types to 0.23.2

### ❤️ Thank You

* Phillip Olesen @PHOL-DA

## 0.23.0 — 2026-03-26

### 🚀 Features

* update dapp lapi schema ([#1339](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1339))
* user party rights ([#1492](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1492))

### 🩹 Fixes

* **core-wallet-auth:** use email for blockdaemon ([#1517](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1517))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.29.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.29.0
* Updated @canton-network/core-wallet-store-inmemory to 0.29.0
* Updated @canton-network/core-wallet-ui-components to 0.29.0
* Updated @canton-network/core-signing-blockdaemon to 0.25.1
* Updated @canton-network/core-signing-participant to 0.28.0
* Updated @canton-network/core-signing-fireblocks to 0.25.1
* Updated @canton-network/core-signing-store-sql to 0.29.0
* Updated @canton-network/core-signing-internal to 0.28.0
* Updated @canton-network/core-wallet-store-sql to 0.28.0
* Updated @canton-network/core-ledger-client to 0.33.0
* Updated @canton-network/core-rpc-transport to 0.9.1
* Updated @canton-network/core-tx-visualizer to 0.23.1
* Updated @canton-network/core-wallet-store to 0.28.0
* Updated @canton-network/core-signing-lib to 0.27.1
* Updated @canton-network/core-wallet-auth to 0.24.1
* Updated @canton-network/core-rpc-errors to 0.19.1
* Updated @canton-network/core-types to 0.23.1

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* Phillip Olesen @PHOL-DA

## 0.22.0 — 2026-03-19

### 🚀 Features

* **wallet-gateway-remote:** read client secrets from env ([#1446](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1446))
* async tx approval and fireblocks sign/execute ([#1462](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1462))
* remove canton 3.3 support ([#1461](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1461))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.28.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.28.0
* Updated @canton-network/core-wallet-store-inmemory to 0.28.0
* Updated @canton-network/core-wallet-ui-components to 0.28.0
* Updated @canton-network/core-signing-blockdaemon to 0.25.0
* Updated @canton-network/core-signing-participant to 0.27.0
* Updated @canton-network/core-signing-fireblocks to 0.25.0
* Updated @canton-network/core-signing-store-sql to 0.28.0
* Updated @canton-network/core-signing-internal to 0.27.0
* Updated @canton-network/core-wallet-store-sql to 0.27.0
* Updated @canton-network/core-ledger-client to 0.32.0
* Updated @canton-network/core-rpc-transport to 0.9.0
* Updated @canton-network/core-tx-visualizer to 0.23.0
* Updated @canton-network/core-wallet-store to 0.27.0
* Updated @canton-network/core-signing-lib to 0.27.0
* Updated @canton-network/core-wallet-auth to 0.24.0
* Updated @canton-network/core-rpc-errors to 0.19.0
* Updated @canton-network/core-types to 0.23.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.21.0 — 2026-03-16

### 🚀 Features

* **core-wallet-auth:** refactor AuthTokenProvider ([#1445](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1445))
* wallet reallocation in sync ([#1381](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1381))

### 🩹 Fixes

* **wallet-gateway-remote:** support pcke in auth flow ([#1453](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1453))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.27.1
* Updated @canton-network/core-wallet-user-rpc-client to 0.27.1
* Updated @canton-network/core-wallet-store-inmemory to 0.27.1
* Updated @canton-network/core-wallet-ui-components to 0.27.1
* Updated @canton-network/core-signing-blockdaemon to 0.24.1
* Updated @canton-network/core-signing-participant to 0.26.1
* Updated @canton-network/core-signing-fireblocks to 0.24.1
* Updated @canton-network/core-signing-store-sql to 0.27.1
* Updated @canton-network/core-signing-internal to 0.26.1
* Updated @canton-network/core-wallet-store-sql to 0.26.1
* Updated @canton-network/core-ledger-client to 0.31.1
* Updated @canton-network/core-rpc-transport to 0.8.1
* Updated @canton-network/core-tx-visualizer to 0.22.2
* Updated @canton-network/core-wallet-store to 0.26.1
* Updated @canton-network/core-signing-lib to 0.26.1
* Updated @canton-network/core-wallet-auth to 0.23.1
* Updated @canton-network/core-rpc-errors to 0.18.2
* Updated @canton-network/core-types to 0.22.1

### ❤️ Thank You

* Alex Matson @alexmatson-da
* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.20.0 — 2026-03-10

### 🚀 Features

* implement getActiveNetwork ([#1410](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1410))

### 🩹 Fixes

* explicitly set additionalProperties for all OpenRPC schemas ([#1032](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1032))
* **wallet-ui-components:** move routing to core ([#1404](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1404))
* **wallet-gateway-remote:** consistent relative pathing ([#1398](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1398))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.26.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.26.0
* Updated @canton-network/core-wallet-store-inmemory to 0.26.0
* Updated @canton-network/core-wallet-ui-components to 0.26.0
* Updated @canton-network/core-signing-blockdaemon to 0.23.0
* Updated @canton-network/core-signing-participant to 0.25.0
* Updated @canton-network/core-signing-fireblocks to 0.23.0
* Updated @canton-network/core-signing-store-sql to 0.26.0
* Updated @canton-network/core-signing-internal to 0.25.0
* Updated @canton-network/core-wallet-store-sql to 0.25.0
* Updated @canton-network/core-ledger-client to 0.30.0
* Updated @canton-network/core-rpc-transport to 0.7.0
* Updated @canton-network/core-tx-visualizer to 0.22.0
* Updated @canton-network/core-wallet-store to 0.25.0
* Updated @canton-network/core-signing-lib to 0.25.0
* Updated @canton-network/core-wallet-auth to 0.22.0
* Updated @canton-network/core-rpc-errors to 0.18.0
* Updated @canton-network/core-types to 0.21.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* Phillip Olesen @PHOL-DA

## 0.17.5 — 2026-03-03

### 🩹 Fixes

* backport ([#1405](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1405))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-ui-components to 0.21.2

### ❤️ Thank You

* Alex Matson @alexmatson-da

## 0.17.4 — 2026-03-03

### 🩹 Fixes

* **wallet-gateway-remote:** added comment to torelhref ([#1402](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1402))

### ❤️ Thank You

* Phillip Olesen @PHOL-DA

## 0.19.0 — 2026-03-02

### 🚀 Features

* new discovery ([#1337](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1337))
* **wallet-gateway-remote:** deleting transactions ([#1296](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1296))
* admin role to modfiy settings ([#1295](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1295))
* separate bootstrap from static config ([#1275](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1275))
* **dapp-sdk:** improved Provider interfaces ([#1247](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1247))
* dapp method renaming (CIP-103) ([#1239](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1239))

### 🩹 Fixes

* **wallet-gateway-remote:** vite serve not supporting relative base ([#1391](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1391))
* **wallet-gateway-remote:** build relative paths for vite assets ([#1385](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1385))
* **wallet-gateway-remote:** added cost estimation logging ([#1363](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1363))
* **wallet-gateway-remote:** added relative pathing for files ([#1365](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1365))
* disable additionalProperties in OpenRPC specs (dapp, dapp-remote, user, & signing) ([#1259](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1259), [#1260](https://github.com/hyperledger-labs/splice-wallet-kernel/issues/1260))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.25.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.25.0
* Updated @canton-network/core-wallet-store-inmemory to 0.25.0
* Updated @canton-network/core-wallet-ui-components to 0.25.0
* Updated @canton-network/core-signing-blockdaemon to 0.22.0
* Updated @canton-network/core-signing-participant to 0.24.0
* Updated @canton-network/core-signing-fireblocks to 0.22.0
* Updated @canton-network/core-signing-store-sql to 0.25.0
* Updated @canton-network/core-signing-internal to 0.24.0
* Updated @canton-network/core-wallet-store-sql to 0.24.0
* Updated @canton-network/core-ledger-client to 0.29.0
* Updated @canton-network/core-rpc-transport to 0.6.0
* Updated @canton-network/core-tx-visualizer to 0.21.0
* Updated @canton-network/core-wallet-store to 0.24.0
* Updated @canton-network/core-signing-lib to 0.24.0
* Updated @canton-network/core-wallet-auth to 0.21.0
* Updated @canton-network/core-rpc-errors to 0.17.0
* Updated @canton-network/core-types to 0.20.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.17.3 — 2026-03-02

### 🩹 Fixes

* bump wg version ([#1393](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1393))

### ❤️ Thank You

* Alex Matson @alexmatson-da

## 0.17.2 — 2026-02-27

### 🩹 Fixes

* **wallet-gateway-remote:** build relative paths for vite assets ([#1385](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1385), [#1388](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1388))

### ❤️ Thank You

* Alex Matson @alexmatson-da

## 0.17.1 — 2026-02-26

### 🩹 Fixes

* **wallet-gateway-remote:** added relative pathing for files ([#1365](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1365), [#1375](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1375))
* backport ([#1363](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1363), [#1374](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1374))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.20.3
* Updated @canton-network/core-wallet-user-rpc-client to 0.21.1
* Updated @canton-network/core-wallet-store-inmemory to 0.21.3
* Updated @canton-network/core-wallet-ui-components to 0.21.1
* Updated @canton-network/core-signing-blockdaemon to 0.18.1
* Updated @canton-network/core-signing-participant to 0.20.3
* Updated @canton-network/core-signing-fireblocks to 0.18.4
* Updated @canton-network/core-signing-store-sql to 0.21.3
* Updated @canton-network/core-signing-internal to 0.20.3
* Updated @canton-network/core-wallet-store-sql to 0.20.3
* Updated @canton-network/core-ledger-client to 0.25.3
* Updated @canton-network/core-rpc-transport to 0.2.5
* Updated @canton-network/core-tx-visualizer to 0.17.4
* Updated @canton-network/core-wallet-store to 0.20.3
* Updated @canton-network/core-signing-lib to 0.20.4
* Updated @canton-network/core-wallet-auth to 0.17.4
* Updated @canton-network/core-rpc-errors to 0.13.4
* Updated @canton-network/core-types to 0.16.4

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Phillip Olesen @PHOL-DA

## 0.17.0 — 2026-01-23

### 🧱 Updated Dependencies

* Updated @canton-network/core-signing-blockdaemon to 0.18.0

## 0.16.0 — 2026-01-22

### 🚀 Features

* determine wallet sync need ([#1138](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1138))

### 🩹 Fixes

* **wallet-gateway-remote:** improved wallet sync flow ([#1171](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1171))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.20.2
* Updated @canton-network/core-wallet-user-rpc-client to 0.21.0
* Updated @canton-network/core-wallet-store-inmemory to 0.21.2
* Updated @canton-network/core-wallet-ui-components to 0.21.0
* Updated @canton-network/core-signing-blockdaemon to 0.17.3
* Updated @canton-network/core-signing-participant to 0.20.2
* Updated @canton-network/core-signing-fireblocks to 0.18.3
* Updated @canton-network/core-signing-store-sql to 0.21.2
* Updated @canton-network/core-signing-internal to 0.20.2
* Updated @canton-network/core-wallet-store-sql to 0.20.2
* Updated @canton-network/core-ledger-client to 0.25.2
* Updated @canton-network/core-rpc-transport to 0.2.4
* Updated @canton-network/core-tx-visualizer to 0.17.3
* Updated @canton-network/core-wallet-store to 0.20.2
* Updated @canton-network/core-signing-lib to 0.20.3
* Updated @canton-network/core-wallet-auth to 0.17.3
* Updated @canton-network/core-rpc-errors to 0.13.3
* Updated @canton-network/core-types to 0.16.3

### ❤️ Thank You

* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.15.0 — 2026-01-15

### 🚀 Features

* **wallet-gateway-remote:** make API rate limit configurable ([#1141](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1141))
* remove need for network selection during wallet creation ([#1128](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1128), [#686](https://github.com/hyperledger-labs/splice-wallet-kernel/issues/686))
* store disabled wallets on sync error ([#1112](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1112))

### 🩹 Fixes

* **core-signing-blockdaemon,wallet-gateway-remote:** enable blockdaemon signing driver ([#1137](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1137))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.20.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.20.0
* Updated @canton-network/core-wallet-store-inmemory to 0.21.0
* Updated @canton-network/core-wallet-ui-components to 0.20.0
* Updated @canton-network/core-signing-blockdaemon to 0.17.1
* Updated @canton-network/core-signing-participant to 0.20.0
* Updated @canton-network/core-signing-fireblocks to 0.18.1
* Updated @canton-network/core-signing-store-sql to 0.21.0
* Updated @canton-network/core-signing-internal to 0.20.0
* Updated @canton-network/core-wallet-store-sql to 0.20.0
* Updated @canton-network/core-ledger-client to 0.25.0
* Updated @canton-network/core-rpc-transport to 0.2.2
* Updated @canton-network/core-tx-visualizer to 0.17.1
* Updated @canton-network/core-wallet-store to 0.20.0
* Updated @canton-network/core-signing-lib to 0.20.1
* Updated @canton-network/core-wallet-auth to 0.17.1
* Updated @canton-network/core-rpc-errors to 0.13.1
* Updated @canton-network/core-types to 0.16.1

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.14.1 — 2026-01-13

### 🚀 Features

* **wallet-gateway-remote:** enable configurable max payload size ([#1121](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1121))
* **wallet-gateway-remote:** added copy button for hash and decoded tx ([#1122](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1122))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.19.1
* Updated @canton-network/core-wallet-user-rpc-client to 0.19.1
* Updated @canton-network/core-wallet-ui-components to 0.19.1
* Updated @canton-network/core-rpc-transport to 0.2.1

### ❤️ Thank You

* Phillip Olesen @PHOL-DA

## 0.13.0 — 2026-01-08

### 🚀 Features

* **wallet-gateway-remote:** add public URL config option, deprecate host/tls options ([#1101](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1101))
* signing public key or id ([#1067](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1067))
* **wallet-gateway-remote:** expired token handling ([#1034](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1034))

### 🩹 Fixes

* user url ([#1105](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1105))
* update copyright headers to 2026 ([#1077](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1077))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.18.1
* Updated @canton-network/core-wallet-user-rpc-client to 0.18.1
* Updated @canton-network/core-wallet-store-inmemory to 0.19.1
* Updated @canton-network/core-wallet-ui-components to 0.18.1
* Updated @canton-network/core-signing-blockdaemon to 0.16.0
* Updated @canton-network/core-signing-participant to 0.18.0
* Updated @canton-network/core-signing-fireblocks to 0.17.0
* Updated @canton-network/core-signing-store-sql to 0.19.0
* Updated @canton-network/core-signing-internal to 0.18.0
* Updated @canton-network/core-wallet-store-sql to 0.18.1
* Updated @canton-network/core-ledger-client to 0.23.1
* Updated @canton-network/core-tx-visualizer to 0.16.1
* Updated @canton-network/core-wallet-store to 0.18.1
* Updated @canton-network/core-signing-lib to 0.19.0
* Updated @canton-network/core-wallet-auth to 0.16.1
* Updated @canton-network/core-rpc-errors to 0.12.1
* Updated @canton-network/core-types to 0.15.1

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Jasper Van der Jeugt
* pawelstepien-da

## 0.12.0 — 2025-12-31

### 🚀 Features

* implement signing api using blockdaemon ([#1041](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1041))

### 🩹 Fixes

* **wallet-gateway:** always bind http server to local interfaces ([#1074](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1074))

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Lim, Kian-An

## 0.11.3 — 2025-12-18

### 🩹 Fixes

* update transaction after execute with internal party ([#1055](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1055))

### ❤️ Thank You

* Marc Juchli @mjuchli-da

## 0.11.2 — 2025-12-18

### 🩹 Fixes

* include transactions page in build ([#1045](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1045))
* user token provider when wallet sync ([#1043](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1043))

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da

## 0.11.1 — 2025-12-17

### 🩹 Fixes

* use admin client for wallet syncing ([#1039](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1039))

### ❤️ Thank You

* Alex Matson @alexmatson-da

## 0.11.0 — 2025-12-17

### 🩹 Fixes

* **wallet-gateway-remote:** isolate socket connections per-session ([#1035](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1035))
* disconnect not ending a session ([#1031](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1031))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.17.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.17.0
* Updated @canton-network/core-wallet-store-inmemory to 0.18.0
* Updated @canton-network/core-wallet-ui-components to 0.17.0
* Updated @canton-network/core-signing-participant to 0.16.0
* Updated @canton-network/core-signing-fireblocks to 0.15.0
* Updated @canton-network/core-signing-store-sql to 0.17.0
* Updated @canton-network/core-signing-internal to 0.16.0
* Updated @canton-network/core-wallet-store-sql to 0.17.0
* Updated @canton-network/core-ledger-client to 0.22.0
* Updated @canton-network/core-tx-visualizer to 0.15.0
* Updated @canton-network/core-wallet-store to 0.17.0
* Updated @canton-network/core-signing-lib to 0.17.0
* Updated @canton-network/core-wallet-auth to 0.15.0
* Updated @canton-network/core-rpc-errors to 0.11.0
* Updated @canton-network/core-types to 0.14.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da

## 0.10.0 — 2025-12-12

### 🚀 Features

* **wallet-gateway-remote:** determine signing provider on wallet sync ([#1016](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1016))
* tx origin ([#999](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/999))
* extend StatusEvent props ([#977](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/977))

### 🩹 Fixes

* **wallet-gateway-remote:** improve JsCantonError handling ([#1014](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1014))
* consolidate specs and fix open() ([#1010](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1010))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.16.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.16.0
* Updated @canton-network/core-wallet-store-inmemory to 0.17.0
* Updated @canton-network/core-wallet-ui-components to 0.16.0
* Updated @canton-network/core-signing-participant to 0.15.0
* Updated @canton-network/core-signing-fireblocks to 0.14.2
* Updated @canton-network/core-signing-store-sql to 0.16.0
* Updated @canton-network/core-signing-internal to 0.15.0
* Updated @canton-network/core-wallet-store-sql to 0.16.0
* Updated @canton-network/core-ledger-client to 0.21.0
* Updated @canton-network/core-tx-visualizer to 0.14.3
* Updated @canton-network/core-wallet-store to 0.16.0
* Updated @canton-network/core-signing-lib to 0.16.2
* Updated @canton-network/core-wallet-auth to 0.14.4
* Updated @canton-network/core-rpc-errors to 0.10.4
* Updated @canton-network/core-types to 0.13.4

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* pawelstepien-da

## 0.9.2 — 2025-12-05

### 🩹 Fixes

* **wallet-gateway-remote:** display gateway version in startup logs + UI ([#992](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/992))
* **wallet-gateway-remote:** defaults for server config ([#990](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/990))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.15.3
* Updated @canton-network/core-wallet-user-rpc-client to 0.15.3
* Updated @canton-network/core-wallet-store-inmemory to 0.16.2
* Updated @canton-network/core-wallet-ui-components to 0.15.2
* Updated @canton-network/core-signing-participant to 0.14.2
* Updated @canton-network/core-signing-fireblocks to 0.14.1
* Updated @canton-network/core-signing-store-sql to 0.15.2
* Updated @canton-network/core-signing-internal to 0.14.2
* Updated @canton-network/core-wallet-store-sql to 0.15.2
* Updated @canton-network/core-ledger-client to 0.20.3
* Updated @canton-network/core-tx-visualizer to 0.14.2
* Updated @canton-network/core-wallet-store to 0.15.1
* Updated @canton-network/core-signing-lib to 0.16.1
* Updated @canton-network/core-wallet-auth to 0.14.3
* Updated @canton-network/core-rpc-errors to 0.10.3
* Updated @canton-network/core-types to 0.13.3

### ❤️ Thank You

* Alex Matson @alexmatson-da
* pawelstepien-da

## 0.9.1 — 2025-12-04

### 🚀 Features

* **wallet-gateway-remote:** added support for custom client id ([#985](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/985))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-user-rpc-client to 0.15.2
* Updated @canton-network/core-wallet-store-inmemory to 0.16.1
* Updated @canton-network/core-wallet-ui-components to 0.15.1
* Updated @canton-network/core-signing-participant to 0.14.1
* Updated @canton-network/core-signing-store-sql to 0.15.1
* Updated @canton-network/core-signing-internal to 0.14.1
* Updated @canton-network/core-wallet-store-sql to 0.15.1
* Updated @canton-network/core-ledger-client to 0.20.2

### ❤️ Thank You

* Phillip Olesen @PHOL-DA

## 0.9.0 — 2025-12-03

### 🚀 Features

* tx signedAt and createdAt ([#948](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/948))
* **wallet-gateway-remote:** userUrl and cors from configs ([#937](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/937))
* transactions view ([#938](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/938))
* transactions listing ([#935](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/935))
* **core-ledger-client:** add fetch option, refactor to named params ([#921](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/921))
* **core-ledger-client:** browser support ([#919](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/919))

### 🩹 Fixes

* **wallet-gateway-remote:** store all tx params ([#942](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/942))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.15.2
* Updated @canton-network/core-wallet-user-rpc-client to 0.15.1
* Updated @canton-network/core-wallet-store-inmemory to 0.16.0
* Updated @canton-network/core-wallet-ui-components to 0.15.0
* Updated @canton-network/core-signing-participant to 0.14.0
* Updated @canton-network/core-signing-fireblocks to 0.14.0
* Updated @canton-network/core-signing-store-sql to 0.15.0
* Updated @canton-network/core-signing-internal to 0.14.0
* Updated @canton-network/core-wallet-store-sql to 0.15.0
* Updated @canton-network/core-ledger-client to 0.20.1
* Updated @canton-network/core-tx-visualizer to 0.14.1
* Updated @canton-network/core-wallet-store to 0.15.0
* Updated @canton-network/core-signing-lib to 0.16.0
* Updated @canton-network/core-wallet-auth to 0.14.2
* Updated @canton-network/core-rpc-errors to 0.10.2
* Updated @canton-network/core-types to 0.13.2

### ❤️ Thank You

* Jasper Van der Jeugt
* Marc Juchli @mjuchli-da
* pawelstepien-da

## 0.8.1 — 2025-11-26

### 🩹 Fixes

* missing sessino on connect ([#923](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/923))

### ❤️ Thank You

* Marc Juchli @mjuchli-da

## 0.8.0 — 2025-11-24

### 🚀 Features

* extend arguments for prepareExecute ([#904](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/904))
* **wallet-gateway-remote:** add CLI flags to print config schema or example ([#905](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/905))
* connect to LocalNet (easily) ([#895](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/895))
* emit on user logout ([#902](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/902))
* emit accountsChanged on syncWallets ([#899](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/899))

### 🩹 Fixes

* avoid tx data as url param for approve view ([#911](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/911))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.15.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.14.0
* Updated @canton-network/core-wallet-store-inmemory to 0.15.0
* Updated @canton-network/core-wallet-ui-components to 0.13.0
* Updated @canton-network/core-signing-participant to 0.13.0
* Updated @canton-network/core-signing-fireblocks to 0.13.0
* Updated @canton-network/core-signing-store-sql to 0.14.0
* Updated @canton-network/core-signing-internal to 0.13.0
* Updated @canton-network/core-wallet-store-sql to 0.14.0
* Updated @canton-network/core-ledger-client to 0.20.0
* Updated @canton-network/core-tx-visualizer to 0.14.0
* Updated @canton-network/core-wallet-store to 0.13.0
* Updated @canton-network/core-signing-lib to 0.15.0
* Updated @canton-network/core-wallet-auth to 0.14.0
* Updated @canton-network/core-rpc-errors to 0.10.0
* Updated @canton-network/core-types to 0.13.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Jasper Van der Jeugt
* Marc Juchli @mjuchli-da

## 0.6.0 — 2025-11-14

### 🚀 Features

* signing provider store support ([#841](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/841), [#562](https://github.com/hyperledger-labs/splice-wallet-kernel/issues/562))
* implement creation wallet with fireblocks ([#824](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/824))
* **wallet-gateway-remote:** separate IDP config from Networks ([#813](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/813))
* **wallet-gateway-remote:** rename chainId to networkId ([#814](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/814))

### 🩹 Fixes

* **wallet-gateway:** await setting primary party ([#860](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/860))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.12.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.12.0
* Updated @canton-network/core-wallet-store-inmemory to 0.13.0
* Updated @canton-network/core-wallet-ui-components to 0.11.0
* Updated @canton-network/core-signing-participant to 0.11.0
* Updated @canton-network/core-signing-fireblocks to 0.11.0
* Updated @canton-network/core-signing-store-sql to 0.12.0
* Updated @canton-network/core-signing-internal to 0.11.0
* Updated @canton-network/core-wallet-store-sql to 0.12.0
* Updated @canton-network/core-ledger-client to 0.18.0
* Updated @canton-network/core-tx-visualizer to 0.12.0
* Updated @canton-network/core-wallet-store to 0.11.0
* Updated @canton-network/core-signing-lib to 0.13.0
* Updated @canton-network/core-wallet-auth to 0.12.0
* Updated @canton-network/core-rpc-errors to 0.8.0
* Updated @canton-network/core-types to 0.11.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* PixelPlex Dev team @pixelplex

## 0.5.0 — 2025-10-29

### 🚀 Features

* support self-signed auth token ([#778](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/778))
* cjs builds ([#772](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/772))
* **wallet-gateway-remote:** add health, readiness endpoints ([#783](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/783))
* **dapp-sdk, wallet-gateway-remote:** add status changed event and disconnect method ([#767](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/767))
* logout ux ([#721](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/721))
* **wallet-sdk:** cache access token ([#723](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/723))

### 🩹 Fixes

* network edit form ([#805](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/805))
* **core-ledger-client, wallet-sdk:** refactor grant user rights ([#784](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/784))
* **wallet-gateway-remote:** idempotent database startup ([#781](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/781))
* add missing admin field ([#780](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/780))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.11.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.11.0
* Updated @canton-network/core-wallet-store-inmemory to 0.12.0
* Updated @canton-network/core-wallet-ui-components to 0.10.0
* Updated @canton-network/core-signing-participant to 0.10.0
* Updated @canton-network/core-signing-internal to 0.10.0
* Updated @canton-network/core-wallet-store-sql to 0.11.0
* Updated @canton-network/core-ledger-client to 0.16.0
* Updated @canton-network/core-tx-visualizer to 0.10.0
* Updated @canton-network/core-wallet-store to 0.10.0
* Updated @canton-network/core-signing-lib to 0.12.0
* Updated @canton-network/core-wallet-auth to 0.11.0
* Updated @canton-network/core-rpc-errors to 0.7.0
* Updated @canton-network/core-types to 0.10.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* pawelstepien-da
* PixelPlex Dev team @pixelplex
* rukmini-basu-da @rukmini-basu-da

## 0.4.0 — 2025-10-22

### 🚀 Features

* run wallet-gateway on a single port ([#753](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/753))

### 🩹 Fixes

* workspace dependency specifiers ([#764](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/764))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.10.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.10.0
* Updated @canton-network/core-wallet-store-inmemory to 0.11.0
* Updated @canton-network/core-wallet-ui-components to 0.9.0
* Updated @canton-network/core-signing-participant to 0.9.0
* Updated @canton-network/core-signing-internal to 0.9.0
* Updated @canton-network/core-wallet-store-sql to 0.10.0
* Updated @canton-network/core-ledger-client to 0.15.0
* Updated @canton-network/core-tx-visualizer to 0.9.0
* Updated @canton-network/core-wallet-store to 0.9.0
* Updated @canton-network/core-signing-lib to 0.11.0
* Updated @canton-network/core-wallet-auth to 0.10.0
* Updated @canton-network/core-rpc-errors to 0.6.0
* Updated @canton-network/core-types to 0.9.0

### ❤️ Thank You

* Alex Matson @alexmatson-da

## 0.3.0 — 2025-10-22

### 🚀 Features

* **dapp-sdk:** ledger api method impl ([#720](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/720))

### 🩹 Fixes

* error in dapp api controller ([#758](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/758))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.9.0
* Updated @canton-network/core-wallet-store-inmemory to 0.10.0
* Updated @canton-network/core-signing-participant to 0.8.1
* Updated @canton-network/core-signing-internal to 0.8.1
* Updated @canton-network/core-wallet-store-sql to 0.9.0
* Updated @canton-network/core-ledger-client to 0.14.0
* Updated @canton-network/core-tx-visualizer to 0.8.1
* Updated @canton-network/core-signing-lib to 0.10.1
* Updated @canton-network/core-wallet-auth to 0.9.0

### ❤️ Thank You

* Marc Juchli @mjuchli-da
* Phillip Olesen @PHOL-DA

## 0.2.0 — 2025-10-21

### 🚀 Features

* **core-ledger-client:** added retry logic and stress testing ([#719](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/719))

### 🩹 Fixes

* some npx improvements, --version, docs ([#740](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/740))

### 🧱 Updated Dependencies

* Updated @canton-network/core-wallet-dapp-rpc-client to 0.8.0
* Updated @canton-network/core-wallet-user-rpc-client to 0.9.0
* Updated @canton-network/core-wallet-store-inmemory to 0.9.0
* Updated @canton-network/core-wallet-ui-components to 0.8.0
* Updated @canton-network/core-signing-participant to 0.8.0
* Updated @canton-network/core-signing-internal to 0.8.0
* Updated @canton-network/core-wallet-store-sql to 0.8.0
* Updated @canton-network/core-ledger-client to 0.13.0
* Updated @canton-network/core-tx-visualizer to 0.8.0
* Updated @canton-network/core-wallet-store to 0.8.0
* Updated @canton-network/core-signing-lib to 0.10.0
* Updated @canton-network/core-wallet-auth to 0.8.0
* Updated @canton-network/core-rpc-errors to 0.5.0
* Updated @canton-network/core-types to 0.8.0

### ❤️ Thank You

* Alex Matson @alexmatson-da
* Phillip Olesen @PHOL-DA

## 0.1.0 — 2025-10-17

This was a version bump only for @canton-network/wallet-gateway-remote to align it with other projects, there were no code changes.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
