> Release notes for the Canton Network dApp SDK

发布说明逐字摘自 from the [`@canton-网络/dapp-sdk` GitHub releases](https://github.com/hyperledger-labs/splice-wallet-kernel/releases?q=dapp-sdk).

## 1.1.0 — 2026-04-24

### 🚀 新功能

* sdk discovery improvements ([#1667](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1667))
* 钱包 connect 集成 ([#1595](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1595))

### 🩹 修复

* **dapp-sdk:** empty adapter list ([#1653](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1653))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 1.1.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 1.1.0
* Updated @canton-网络/core-钱包-ui-组件 to 1.1.0
* Updated @canton-网络/core-钱包-discovery to 1.1.0
* Updated @canton-网络/core-splice-提供方 to 1.1.0
* Updated @canton-网络/core-提供方-dapp to 1.1.0
* Updated @canton-网络/core-rpc-transport to 1.1.0
* Updated @canton-网络/core-types to 1.1.0

### ❤️ 致谢

* Gancho Radkov @ganchoradkov
* Marc Juchli @mjuchli-da

## 0.26.0 — 2026-04-16

### 🚀 新功能

* **core-钱包-ui-组件:** increased robustness of 钱包 picker ([#1624](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1624))
* add CIP-0103 connected and isConnected ([#1609](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1609))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.27.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.33.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.33.0
* Updated @canton-网络/core-钱包-discovery to 0.10.0
* Updated @canton-网络/core-splice-提供方 to 0.34.0
* Updated @canton-网络/core-提供方-dapp to 0.10.0
* Updated @canton-网络/core-rpc-transport to 0.12.0
* Updated @canton-网络/core-types to 0.26.0

### ❤️ 致谢

* pawelstepien-da
* Phillip Olesen @PHOL-DA

## 0.25.0 — 2026-04-02

### 🚀 新功能

* global popup ([#1561](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1561), [#1560](https://github.com/hyperledger-labs/splice-wallet-kernel/issues/1560))
* expose connected 提供方 ([#1549](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1549))
* multi 提供方 support ([#1522](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1522))
* update dapp lapi schema ([#1339](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1339))

### 🩹 修复

* missing sdk controller 方法 ([#1558](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1558))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.25.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.31.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.31.0
* Updated @canton-网络/core-钱包-discovery to 0.8.0
* Updated @canton-网络/core-splice-提供方 to 0.32.0
* Updated @canton-网络/core-提供方-dapp to 0.8.0
* Updated @canton-网络/core-rpc-transport to 0.11.0
* Updated @canton-网络/core-types to 0.25.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da

## 0.24.0 — 2026-03-14

### 🚀 新功能

* 钱包 reallocation in sync ([#1381](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1381))

### 🩹 修复

* bump default timeout for prepareExecuteAndWait ([#1451](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1451))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.21.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.27.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.27.0
* Updated @canton-网络/core-钱包-discovery to 0.4.0
* Updated @canton-网络/core-splice-提供方 to 0.28.0
* Updated @canton-网络/core-提供方-dapp to 0.4.0
* Updated @canton-网络/core-types to 0.22.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* pawelstepien-da

## 0.23.1 — 2026-03-11

### 🩹 修复

* **core-splice-提供方,core-提供方-dapp:** allow multiple listeners ([#1438](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1438))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-discovery to 0.3.1
* Updated @canton-网络/core-splice-提供方 to 0.27.1
* Updated @canton-网络/core-提供方-dapp to 0.3.1

### ❤️ 致谢

* Phillip Olesen @PHOL-DA

## 0.23.0 — 2026-03-10

### 🚀 新功能

* improve discovery UI ([#1427](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1427))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.20.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.26.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.26.0
* Updated @canton-网络/core-钱包-discovery to 0.3.0
* Updated @canton-网络/core-splice-提供方 to 0.27.0
* Updated @canton-网络/core-提供方-dapp to 0.3.0
* Updated @canton-网络/core-types to 0.21.0

### ❤️ 致谢

* Fayi @fayi-da

## 0.22.0 — 2026-03-02

### 🚀 新功能

* new discovery ([#1337](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1337))
* **dapp-sdk:** improved 提供方 interfaces ([#1247](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1247))
* dapp 方法 renaming (CIP-103) ([#1239](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1239))

### 🩹 修复

* disable additionalProperties in OpenRPC specs (dapp, dapp-remote, 用户, & signing) ([#1259](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1259), [#1260](https://github.com/hyperledger-labs/splice-wallet-kernel/issues/1260))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.19.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.25.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.25.0
* Updated @canton-网络/core-钱包-discovery to 0.2.0
* Updated @canton-网络/core-splice-提供方 to 0.26.0
* Updated @canton-网络/core-提供方-dapp to 0.2.0
* Updated @canton-网络/core-types to 0.20.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da

## 0.21.1 — 2026-02-03

### 🩹 修复

* **钱包-gateway-remote:** dApp ui in pop-up window ([#1224](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1224))

### ❤️ 致谢

* Phillip Olesen @PHOL-DA

## 0.20.0 — 2026-01-22

### 🩹 修复

* **dapp-sdk:** prepareExecuteAndWait to dapp 提供方 ([#1156](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1156))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.14.2
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.20.2
* Updated @canton-网络/core-钱包-ui-组件 to 0.21.0
* Updated @canton-网络/core-splice-提供方 to 0.21.0
* Updated @canton-网络/core-types to 0.16.3

### ❤️ 致谢

* Jasper Van der Jeugt

## 0.19.0 — 2026-01-15

### 🚀 新功能

* **dapp-sdk:** return null for prepareExecute ([#1152](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1152))
* store disabled wallets on sync 错误 ([#1112](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1112))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.14.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.20.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.20.0
* Updated @canton-网络/core-splice-提供方 to 0.20.0
* Updated @canton-网络/core-types to 0.16.1

### ❤️ 致谢

* Alex Matson @alexmatson-da
* pawelstepien-da

## 0.18.0 — 2026-01-08

### 🩹 修复

* **dapp-sdk:** more reliable verified gateways ([#1102](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1102))
* update copyright headers to 2026 ([#1077](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1077))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.12.1
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.18.1
* Updated @canton-网络/core-钱包-ui-组件 to 0.18.1
* Updated @canton-网络/core-splice-提供方 to 0.18.1
* Updated @canton-网络/core-types to 0.15.1

### ❤️ 致谢

* Alex Matson @alexmatson-da
* Jasper Van der Jeugt

## 0.17.2 — 2025-12-19

### 🩹 修复

* add timeout for prepareExecute 方法 ([#1059](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1059))

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.17.1 — 2025-12-18

### 🩹 修复

* stop double popup for prepareExecute ([#1049](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1049))

### 🧱 依赖更新

* Updated @canton-网络/core-splice-提供方 to 0.17.1

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.17.0 — 2025-12-17

### 🩹 修复

* **钱包-gateway-remote:** isolate socket connections per-会话 ([#1035](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1035))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.11.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.17.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.17.0
* Updated @canton-网络/core-splice-提供方 to 0.17.0
* Updated @canton-网络/core-types to 0.14.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da

## 0.16.0 — 2025-12-12

### 🚀 新功能

* extend StatusEvent props ([#977](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/977))

### 🩹 修复

* **dapp-sdk:** improve switching between different gateways ([#1020](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1020))
* **dapp-sdk:** prevent duplicated socket 事件 ([#1015](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1015))
* consolidate specs and fix open() ([#1010](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1010))
* **dapp-sdk,core-splice-提供方:** minor code cleanup ([#1007](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/1007))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.10.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.16.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.16.0
* Updated @canton-网络/core-splice-提供方 to 0.16.0
* Updated @canton-网络/core-types to 0.13.4

### ❤️ 致谢

* Alex Matson @alexmatson-da
* Marc Juchli @mjuchli-da
* pawelstepien-da

## 0.15.0 — 2025-12-01

### 🩹 修复

* **dapp-sdk:** conditionally add status listener ([#931](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/931))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.9.1
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.15.1
* Updated @canton-网络/core-钱包-ui-组件 to 0.14.0
* Updated @canton-网络/core-splice-提供方 to 0.14.0
* Updated @canton-网络/core-types to 0.13.1

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.14.0 — 2025-11-26

### 🚀 新功能

* extend arguments for prepareExecute ([#904](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/904))
* emit on 用户 logout ([#902](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/902))
* expose remove listener per 事件 ([#900](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/900))
* merge utxos ([#864](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/864))

### 🩹 修复

* **钱包-gateway-remote:** handle discovery close ([#896](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/896))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.9.0
* Updated @canton-网络/core-splice-提供方 to 0.13.0

### ❤️ 致谢

* Marc Juchli @mjuchli-da
* Phillip Olesen @PHOL-DA
* rukmini-basu-da @rukmini-basu-da

## 0.13.0 — 2025-11-17

### 🚀 新功能

* differentiate between authenticated and connected ([#850](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/850))

### 🩹 修复

* **dapp-sdk:** always getting timeout when prepareExecute ([#870](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/870))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.8.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.13.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.11.1
* Updated @canton-网络/core-splice-提供方 to 0.12.0
* Updated @canton-网络/core-types to 0.11.1

### ❤️ 致谢

* Marc Juchli @mjuchli-da
* Phillip Olesen @PHOL-DA

## 0.12.0 — 2025-11-14

### 🚀 新功能

* implement creation 钱包 with fireblocks ([#824](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/824))
* **钱包-gateway-remote:** rename chainId to networkId ([#814](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/814))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.7.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.12.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.11.0
* Updated @canton-网络/core-splice-提供方 to 0.11.0
* Updated @canton-网络/core-types to 0.11.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* PixelPlex Dev team @pixelplex

## 0.11.0 — 2025-10-29

### 🚀 新功能

* cjs builds ([#772](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/772))
* **dapp-sdk, 钱包-gateway-remote:** add status changed 事件 and disconnect 方法 ([#767](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/767))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.6.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.11.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.10.0
* Updated @canton-网络/core-splice-提供方 to 0.10.0
* Updated @canton-网络/core-types to 0.10.0

### ❤️ 致谢

* Alex Matson @alexmatson-da
* pawelstepien-da

## 0.10.0 — 2025-10-22

### 🚀 新功能

* run 钱包-gateway on a single port ([#753](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/753))

### 🩹 修复

* workspace dependency specifiers ([#764](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/764))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.5.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.10.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.9.0
* Updated @canton-网络/core-splice-提供方 to 0.9.0
* Updated @canton-网络/core-types to 0.9.0

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.9.0 — 2025-10-22

### 🚀 新功能

* **dapp-sdk:** ledger api 方法 impl ([#720](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/720))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.9.0

### ❤️ 致谢

* Marc Juchli @mjuchli-da

## 0.8.0 — 2025-10-21

### 🚀 新功能

* **dapp-sdk:** 方法 wrappers ([#684](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/684))

### 🩹 修复

* styles for discovery & config file ([#649](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/649))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.4.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.8.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.8.0
* Updated @canton-网络/core-splice-提供方 to 0.8.0
* Updated @canton-网络/core-types to 0.8.0

### ❤️ 致谢

* Marc Juchli @mjuchli-da
* PixelPlex Dev team @pixelplex

## 0.6.0 — 2025-10-10

### 🩹 修复

* **dapp-sdk,core-splice-提供方:** fix 提供方 export ([#604](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/604))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.3.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.7.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.6.0
* Updated @canton-网络/core-splice-提供方 to 0.6.0
* Updated @canton-网络/core-types to 0.6.0

### ❤️ 致谢

* Marc Juchli @mjuchli-da

## 0.5.0 — 2025-10-02

### 🚀 新功能

* dapp-api rework ([#535](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/535))

### 🩹 修复

* return 用户 url as part of kernel info ([#581](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/581))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-remote-rpc-client to 0.2.0
* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.6.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.5.0
* Updated @canton-网络/core-splice-提供方 to 0.5.0
* Updated @canton-网络/core-types to 0.5.0

### ❤️ 致谢

* Marc Juchli @mjuchli-da

## 0.4.0 — 2025-09-26

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.5.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.4.0
* Updated @canton-网络/core-splice-提供方 to 0.4.0
* Updated @canton-网络/core-types to 0.4.0

## 0.3.3 — 2025-09-24

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.4.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.3.3
* Updated @canton-网络/core-splice-提供方 to 0.3.3
* Updated @canton-网络/core-types to 0.3.3

## 0.3.2 — 2025-09-18

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.3.2
* Updated @canton-网络/core-钱包-ui-组件 to 0.3.2
* Updated @canton-网络/core-splice-提供方 to 0.3.2
* Updated @canton-网络/core-types to 0.3.2

## 0.3.1 — 2025-09-16

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.3.1
* Updated @canton-网络/core-钱包-ui-组件 to 0.3.1
* Updated @canton-网络/core-splice-提供方 to 0.3.1
* Updated @canton-网络/core-types to 0.3.1

## 0.1.2 — 2025-09-03

### 🩹 修复

* ensure package json publishes everything in dist/ recursively ([#363](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/363))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.1.2
* Updated @canton-网络/core-钱包-ui-组件 to 0.1.1
* Updated @canton-网络/core-splice-提供方 to 0.1.1
* Updated @canton-网络/core-types to 0.1.1

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.1.1 — 2025-09-02

### 🩹 修复

* **钱包-sdk,dapp-sdk:** fill out package readmes for the SDKs ([#317](https://github.com/hyperledger-labs/splice-wallet-kernel/pull/317))

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 0.1.1

### ❤️ 致谢

* Alex Matson @alexmatson-da

## 0.2.0 — 2025-08-28

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 1.2.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.2.0
* Updated @canton-网络/core-splice-提供方 to 0.2.0
* Updated @canton-网络/core-types to 0.2.0

## 0.1.0 — 2025-08-28

### 🧱 依赖更新

* Updated @canton-网络/core-钱包-dapp-rpc-client to 1.1.0
* Updated @canton-网络/core-钱包-ui-组件 to 0.1.0
* Updated @canton-网络/core-splice-提供方 to 0.1.0
* Updated @canton-网络/core-types to 0.1.0

