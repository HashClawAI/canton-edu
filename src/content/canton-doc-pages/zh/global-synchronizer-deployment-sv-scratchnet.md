---
title: "如何引导网络"
slug: "global-synchronizer-deployment-sv-scratchnet"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/sv-scratchnet.md"
source_title: "How to Bootstrap a Network"
tags:
  - global-synchronizer
  - deployment
  - sv-scratchnet
---

# 如何引导网络

> 以超级验证者身份从零引导新 Canton Network。

> 作为超级验证者从头开始启动新的 Canton 网络

<div className="todo">
  调整下面的写作风格以适应文档的其余部分
</div>

## cometbft Helm 值

1. 禁用 state sync

stateSync:

* enable: true
* rpcServers：“...”

- enable: false

2. 对于单个 SV 配置，您现在正在引导单个 sv，因此请将您自己的密钥放入：

sv1:

* keyAddress：“...”
* nodeId：“...”
* publicKey：“...”

## scan Helm 值

添加 1 个值：

* isFirstSv: true

## sv Helm 值

1.删除joinWithKeyOnboarding

* joinWithKeyOnboarding：
*sponsorApiUrl：[https://sv.sv-2.whatever.global.canton.network.digitalasset.com](https://sv.sv-2.whatever.global.canton.network.digitalasset.com)

2. 添加初始Helm 值 您可以使用这些数值或选择其他数值

* isDevNet: true
* onboardingType: found-dso
*
* // 请参阅下面关于其余部分的注释：
* initialSynchronizerFeesConfig：
* baseRateBurstAmount：400000
* baseRateBurstWindowMins：20
* extraTrafficPrice：16.670000000000002
* minTopupAmount：200000
* readVsWriteScalingFactor：4
* onboardingFoundingSvRewardWeightBps：10000

3. 从 `sv-values.yaml` 中删除 `decentralizedSynchronizerUrl` 配置。它仅用于在初始 SV 之后加入的节点。

## 您可能需要考虑的其他 helm 值

* 在所有使用 TARGET\_CLUSTER / TARGET\_HOSTNAME 的地方，您需要指向网络的基本域
  * 例如，我们的网络基于 hub-scratch.global.canton.network.digitalasset.com，因此我们设置：
    * 目标集群 = hub-scratch
    * targetHostname = hub-scratch.global.canton.network.digitalasset.com
* 如果您使用 walletSweep，您可能不会在这个临时环境中使用它，除非您还计划部署验证者

## 您可能需要考虑的底层事物

* 配置 IP 允许列表，将集群暴露给内部 VPN 或您控制的类似网络。目前不建议将其公开到公共互联网。
* 批准的 SV 身份（进入 sv helm 值）：如果您正在部署单个引导节点，则可以将其设置为 \[]

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
