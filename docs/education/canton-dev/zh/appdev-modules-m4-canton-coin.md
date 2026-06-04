---
title: "Canton Coin 与 Traffic"
slug: "appdev-modules-m4-canton-coin"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-canton-coin.md"
source_title: "Canton Coin and Traffic"
tags:
  - appdev
  - modules
  - m4-canton-coin
---

# Canton Coin 与 Traffic

> 应用开发者需了解的 Canton Coin 购买 traffic 额度与交易成本

Global Synchronizer 上的每笔交易都需要 traffic。Canton Coin（CC）是购买 traffic 额度的原生货币。作为应用开发者，你需要理解这一关系，以免用户交易因额度不足而中断。

## Canton Coin

Canton Coin 是 Global Synchronizer 的原生实用代币，通过 [Splice](https://github.com/canton-network/splice)（去中心化 Canton synchronizer 的开源基础设施层）实现。

CC 在网络上的主要用途：

* **购买 traffic** — 将 CC 兑换为 traffic 额度，供 validator 提交交易
* **Validator 奖励** — Validator 因运营基础设施与处理交易而获得 CC
* **应用奖励** — 应用提供方因应用为 Canton Network 创造价值而获得 CC
* **治理** — Super Validator 质押 CC 参与 synchronizer 治理

与多数区块链代币不同，CC 余额是私密的。只有你和明确授权方可见你的持仓，没有公开的余额或转账账本。

## Traffic：交易费如何运作

Traffic 是 Canton 对交易费的称呼。提交交易时并不直接支付 CC，而是由 validator 维护以 traffic 额度计量的 **traffic 预算**。每笔交易按大小与复杂度从预算中扣除额度。

两步流程：

1. **充值** — 将 CC 兑换为 traffic 额度，加入 validator 的 traffic 预算
2. **消耗** — validator 提交交易时，从预算中扣除 traffic 额度

Traffic 额度不可转让。CC 一旦兑换为 traffic，这些额度只能在该 validator 上用于交易费。

### 影响 Traffic 成本的因素

给定交易的 traffic 成本取决于：

* **交易大小** — 载荷越大（更多合约数据、更多 party）消耗越多
* **网络状况** — 负载高时成本可能变化

## 自动充值功能

Validator 可启用 **auto-top-up**，在预算低于配置阈值时自动购买 traffic 额度，无需人工干预。

这是应用提供方的推荐做法。若无自动充值，需监控 traffic 预算并在耗尽前手动充值；预算用尽后 validator 的交易将失败，直到补充额度。

<Note>
  自动充值要求 validator 钱包持有足够 CC。余额过低无法购买 traffic 时，自动充值无法执行，交易将开始失败。
</Note>

## 作为应用提供方管理 Traffic

作为应用提供方，你的 validator 代表应用 party 提交交易。你需确保 validator 有足够 traffic 额度应对应用产生的交易量。

实践要点：

* **估算 traffic 用量** — 了解应用每日交易数量与大小。在 DevNet 或 TestNet 测量实际消耗。为外部 party 准备交易时，可提供该交易的 traffic 估算。
* **启用 auto-top-up** — 配置 validator 自动补充 traffic 额度，阈值应足够吸收流量峰值。
* **监控钱包余额** — 自动充值从钱包 CC 余额扣款，保持充足资金。
* **处理 traffic 不足错误** — 若因 traffic 不足导致交易失败，后端应返回明确错误而非静默重试。修复方式是充值 traffic 预算，而非重试命令。

## 获取 Canton Coin

获取 CC 的方式因环境而异：

* **LocalNet** — 自动提供测试 CC，无需操作。
* **DevNet** — 通过 faucet（tap）领取免费测试 CC，有速率限制，无真实价值。
* **TestNet** — 与 DevNet 相同的 faucet 机制，仅测试 CC。
* **MainNet** — 从支持的交易所购买、通过 validator 运营赚取，或从其他 party 直接转账接收。

## 应用中的钱包集成

若应用涉及 party 之间的 CC 支付（如用户购买许可证），需集成 Splice 钱包系统。在 cn-quickstart 中，许可证续期流程演示如下：

1. [`License_Renew`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml) choice 创建实现 Splice `AllocationRequest` 接口的 `LicenseRenewalRequest` 合约
2. Splice 钱包检测到分配请求，创建 `AppPaymentRequest`，将 CC 从用户转给提供方
3. 支付结算后，提供方行使 [`LicenseRenewalRequest_CompleteRenewal`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml) 创建续期后的许可证

后端实现见 [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java)。

钱包处理 CC 转账、余额查询与支付确认。你的 Daml 模型定义钱包系统可理解的支付请求合约。

## Traffic 与 CC：小结

* **Canton Coin（CC）** 是货币。你持有于钱包、在 party 间转账，并用于购买 traffic。
* **Traffic 额度** 是 validator 提交交易时消耗的资源，存在于 validator 的 traffic 预算中，而非钱包。
* 通过充值（手动或自动）将 CC 兑换为 traffic 额度；不可逆 — traffic 额度无法换回 CC。

## 延伸阅读

* [Canton Coin 概述](/zh/docs/canton/overview-understand-canton-coin) — CC 代币经济学、validator 奖励与治理
* [后端开发](/zh/docs/canton/appdev-modules-m4-backend-dev) — 含 traffic 不足失败在内的交易错误处理
* [cn-quickstart](https://github.com/digital-asset/cn-quickstart) — Canton 应用中钱包集成的可运行示例

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
