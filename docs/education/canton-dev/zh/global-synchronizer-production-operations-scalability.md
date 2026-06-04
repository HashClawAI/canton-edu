---
title: "网络可扩展性"
slug: "global-synchronizer-production-operations-scalability"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/scalability.md"
source_title: "Network Scalability"
tags:
  - global-synchronizer
  - production-operations
  - scalability
---

# 网络可扩展性

> Canton Network 节点的扩展特性与调优指南。

> Canton Network节点的扩展特性和调优指南

## 每个验证者的参与方数量

虽然底层 Canton 参与者支持每个节点最多 100 万个 Party，但验证者应用的限制目前意味着在涉及验证者应用时最多仅支持 200 个 Party。预计未来 200 个参与方的限制将被取消，这将不再需要这些变通办法。

具体而言，200 个 Party 的限制适用于：

1. 不使用外部签名并通过验证者 API 加入的各方或已单独创建 `WalletAppInstall` 合约的任何其他方。
2. 使用外部签名的各方，已通过 `/v0/admin/external-party/setup-proposal` 设置了入职合同，或者已手动创建与设置为验证者运营方的 `validator` party的 `ValidatorRight` 合同。

它不适用于：

1. 不使用通过 Ledger API 或 Canton admin API 创建的外部签名且尚未通过验证者 API 加入或具有关联的 `WalletAppInstall` 合约的各方。
2. 使用外部签名的各方不存在对应的`ValidatorRight`，且`validator` party设置为验证者运营方。请注意，`/v0/admin/external-party/setup-proposal`确实设置了这样的`ValidatorRight`合约，因此必须避免使用此API。可以直接使用`ExternalPartySetupProposal`合约来设置预批准，但`validator` party必须设置为与验证者运营方不同的一方。这也意味着您需要编写自己的自动化程序以在预批准到期时续订预批准。请参阅文档了解更多详细信息。

### 绕过限制

绕过限制的首选方法是直接通过[用于外部签名的Canton API](/appdev/deep-dives/external-signing)或验证者 API上的`/v0/admin/external-party/topology/{generate,submit}`设置外部 Party，但*不*使用`/v0/admin/external-party/setup-proposal`下的端点。

如果您不需要预先批准，这就足够了。

如果您确实需要创建预先批准，则必须确保您不会创建将`validator` party设置为验证者操作员的`ValidatorRight`合同。最好的选择是使用`#splice-wallet:Splice.Wallet.TransferPreapproval:TransferPreapprovalProposal`从外部方和验证者运营商那里收集授权，验证者运营商创建`TransferPreapproval`但不创建`ValidatorRight`合约。只要生成的 `TransferPreapproval` 上的 `provider` 是验证者运营方，验证者中传输预批准的续订自动化仍将继续运行。如果您将其设置为不同的一方，则需要构建自己的续订自动化。

### 绕过限制的影响

请注意，绕过验证者限制确实意味着验证者应用不会处理该方的任何合约。最值得注意的是，这意味着该方没有运行奖励铸造自动化，包括为该方生成的 `ValidatorRewardCoupon` 活动记录无法由验证者运营商铸造，因为这依赖于 `ValidatorRight` 合约。如果需要铸造奖励，您有两种选择：

1. 使用铸币委派将奖励收集委托给验证者
2. 构建您自己的铸币自动化系统。

您也不能为此方使用 `/v0/admin/external-party/` 下的任何验证者端点，例如发起转账。相反，通过账本 API 上的代币标准与外部方进行交互。

## 拓扑批处理

默认情况下，拓扑批处理被禁用，这意味着每个拓扑事务都会作为自己的消息提交给同步器。这对于引导来说尤其必要，其中太大的批次可能会超出免费流量限制，从而阻止节点甚至无法达到可以购买流量的程度，唯一的选择是从现有节点为新节点购买流量。但是，引导完成后（验证者就绪探针报告已准备就绪并且您观察到收集的奖励），增加批量大小以增加节点可以提交的拓扑事务的吞吐量可能很有用。这对于托管许多不同最终用户方的钱包中的节点特别有用。

为此，请将以下环境变量添加到您的参与者配置中。您可以试验批量大小，但不建议批量大小超过 20，因为批量太大可能会导致问题。

```
- name: ADDITIONAL_CONFIG_TOPOLOGY_BATCH_SIZE
  value: |
    canton.participants.participant.topology.broadcast-batch-size = 20
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
