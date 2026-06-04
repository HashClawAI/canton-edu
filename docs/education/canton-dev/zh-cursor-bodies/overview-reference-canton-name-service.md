> 在 Canton Network 上将人类可读名称映射到 Party 标识符

Canton Name Service (CNS) 将人类可读名称映射到 Canton Network 上的 Party 标识符，功能类似互联网的 DNS：无需分享冗长不透明 Party ID（如 `auth0_007c675a429eaf831f0991308d85::12201abe669f...`），可分享 `alice.unverified.cns` 这类名称。

CNS 实现为 Global Synchronizer 上的一组 Daml 合约，由 DSO party 治理。[Splice](https://github.com/canton-network/splice) 代码库中底层实现称为 Amulet Name Service (ANS)。

## 名称格式

CNS 条目名称遵循 `<chosen-name>.unverified.cns`。后缀 `.unverified.cns` 附加于所有用户注册名。`unverified` 表示未对注册人做身份验证——任何有钱包且持有足够 Canton Coin 者均可注册。

DSO 自身持有特殊条目 `dso.cns`，无过期且无 contract ID（由 DSO 直接提供，非标准注册流程）。

## 注册流程

注册 CNS 条目是基于 Daml 订阅支付模型的多步流程：

1. 用户调用 Validator App ANS API 的 **POST** `/v0/entry/create`，提供 `name`、`url`、`description`。
2. Validator App exercise `AnsRules_RequestEntry` choice，创建 `AnsEntryContext` 与 `SubscriptionRequest` 合约。
3. 用户通过钱包接受订阅请求，触发以 Canton Coin 支付的首期款项。
4. DSO 自动化执行 `AnsEntryContext_CollectInitialEntryPayment`，销毁转给 DSO 的 Canton Coin，并创建 `AnsEntry` 合约。

条目费用与生命周期配置在 `AnsRules` 合约的 `AnsRulesConfig` 中。款项付给 DSO party 并被销毁——不再分配。

## 续费

CNS 条目会过期。每条目有 `expiresAt`，所有者须在到期前续费以保留名称。

续费使用相同订阅支付机制。续费到期时，若用户有足够 Canton Coin 且启用自动续费，钱包自动化可处理。DSO 自动化 exercise `AnsEntryContext_CollectEntryRenewalPayment`，销毁款项并将 `expiresAt` 延长配置的 `entryLifetime`。

若到期未续费，任一 signatory 可 exercise `AnsEntry_Expire` 归档条目。

## 名称解析

CNS 支持双向解析——名称到 Party、Party 到名称（类似正向与反向 DNS）。

Scan API 提供三个公共查询端点：

* **GET** `/v0/ans-entries/by-name/{name}` — 精确名称解析到条目（含所有者 Party ID）
* **GET** `/v0/ans-entries/by-party/{party}` — Party ID 解析到 CNS 条目
* **GET** `/v0/ans-entries?name_prefix=<prefix>&page_size=<n>` — 按名称前缀搜索

钱包等应用用这些端点显示人类可读名称而非原始 Party ID。例如发送 Canton Coin 时可输入 `alice.unverified.cns` 而非完整 Party ID。

Validator App 的 Scan Proxy API（`/v0/scan-proxy/ans-entries/*`）亦提供相同端点，通过查询多个 Super Validator 节点并返回共识结果实现 BFT 验证。

## 在 Global Synchronizer 上的存储

CNS 状态完全在 Global Synchronizer 上，为 `splice-amulet-name-service` 包中的 Daml 合约。关键合约类型：

* **`AnsRules`** — 单例合约，持有配置（条目费用、生命周期、续费时长）。由 DSO party 签署。
* **`AnsEntryContext`** — 跟踪 CNS 条目与其订阅关系。由 DSO 与条目所有者共同签署。
* **`AnsEntry`** — 实际名称记录，含名称、所有者 Party、URL、描述与过期时间。由 DSO 与条目所有者共同签署。

因遵循标准 Daml 授权规则，条目所有者与 DSO 均须同意创建、续费与过期。

## API 参考

CNS 功能分布在 Validator App 暴露的两套 API：

**ANS API**（条目管理）— 见 [ans-external.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/validator/src/main/openapi/ans-external.yaml) OpenAPI 规范：

* **POST** `/v0/entry/create` — 请求创建新条目
* **GET** `/v0/entry/all` — 列出认证用户拥有的全部条目

**Scan API**（名称解析）— 见 [scan.yaml](https://raw.githubusercontent.com/canton-network/splice/refs/heads/main/apps/scan/src/main/openapi/scan.yaml) OpenAPI 规范：

* **GET** `/v0/ans-entries` — 按名称前缀列出条目
* **GET** `/v0/ans-entries/by-name/{name}` — 按精确名称查找
* **GET** `/v0/ans-entries/by-party/{party}` — 按 Party ID 查找
* **POST** `/v0/ans-rules` — 获取当前 ANS 规则配置

ANS API 要求 JWT 认证，token subject 须与请求/列出条目的用户一致。Scan API 端点为公共。
