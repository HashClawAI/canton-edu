---
title: "Canton Coin 预批准"
slug: "appdev-modules-m7-canton-coin-preapprovals"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-canton-coin-preapprovals.md"
source_title: "Canton Coin Preapprovals"
tags:
  - appdev
  - modules
  - m7-canton-coin-preapprovals
---

# Canton Coin 预批准

> TransferPreapproval 合约如何启用预批准的 Canton Coin 转账

与 Eth、Bitcoin 等资产不同，Canton Coin 要求 party 显式同意持有 Canton Coin，包括对每笔入账转账的显式同意。

愿意接受任意发送方转入 Canton Coin 的 party 可设置 `TransferPreapproval`，允许任何 party 向该 party 发送 Canton Coin。注意这仅适用于 Canton Coin 转账，不适用于其他资产；其他资产可能有各自的预批准机制，或需逐笔批准入账。

为避免 super validator 为不再活跃的 party 存储并提供 `TransferPreapproval`，并防止恶意 party 滥发，预批准有有效期，创建时须按有效期比例销毁费用。费用由 super validator 通过 `transferPreapprovalFee` 参数控制。当前值可在 CC Scan 查看（选择对应网络）：

* DevNet: [https://scan.sv-1.dev.global.canton.network.sync.global/dso](https://scan.sv-1.dev.global.canton.network.sync.global/dso)
* TestNet: [https://scan.sv-1.test.global.canton.network.sync.global/dso](https://scan.sv-1.test.global.canton.network.sync.global/dso)
* MainNet: [https://scan.sv-1.global.canton.network.sync.global/dso](https://scan.sv-1.global.canton.network.sync.global/dso)

当前默认约为每年 1 美元。

每个预批准有两个 party：`receiver` 批准入账，`provider` 负责付费并在临近到期时续期。作为回报，`provider` 将成为使用该预批准的所有入账转账的应用提供方并获得应用奖励。`provider` 不必与 `receiver` 托管在同一节点，但实践中常见如此。

## 设置预批准

未使用外部签名的 party 可在 splice 钱包 UI 中，通过登出按钮旁的按钮创建预批准：

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/preapproval_button.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=feabdf575485595c7c0aa26911e133dd" width="600" alt="Button to create preapproval" data-path="images/splice/preapproval_button.png" />

使用外部签名时，常见做法由 validator 运营方创建 `ExternalPartySetupProposal` 合约，外部 party 签署行使 `ExternalPartySetupProposal_Accept` 的交易。这会同时创建外部 party 的 validator 奖励铸造所需的 `ValidatorRight` 合约，以及 provider 设为 validator 运营方 party 的 `TransferPreapproval`。validator 暴露 `/v0/admin/external-party/setup-proposal` 创建提案，以及 `/v0/admin/external-party/setup-proposal/prepare-accept` 与 `submit-accept` 供外部 party 准备并提交签名接受。详见 API 文档。若 provider 需不同设置，可能需自建 Daml 设置合约并通过 Ledger API 创建，而非使用 validator API。

注意将 provider 设为 validator 运营方时的 party 数量限制。

validator API 创建的预批准到期日为未来 90 天。

## 到期与续期

如上，预批准总有到期日。到期且未续期则不能再用于转账，super validator 运行的自动化最终会归档该合约。

provider 为 validator 运营方 party 的预批准，在距到期不足 30 天时由 validator 应用自动化续期 90 天。

若 provider 为其他 party，需自行实现定期行使 `TransferPreapproval_Renew` 的续期自动化。

## 撤销预批准

`receiver` 与 `provider` 均可通过 `TransferPreapproval_Cancel` 撤销。

splice 钱包 UI 目前不支持；provider 为 validator 运营方时，运营方可对 `/v0/admin/transfer-preapprovals/by-party/{receiver-party}` 发 `DELETE`。详见 API 文档。

## 通过预批准转账

若收款方已设预批准，splice 钱包 UI 转账时会默认使用。

若通过 API（尤其外部 party），推荐用 Token Standard API，会在可能时使用预批准。用法见 [CIP](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 与 [token standard reference CLI](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/transfer.ts)。

亦可使用 validator 上非标准 Canton Coin 转账的遗留外部签名 API：`/v0/admin/external-party/transfer-preapproval/prepare-send` 与 `submit-send`。详见 API 文档。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
