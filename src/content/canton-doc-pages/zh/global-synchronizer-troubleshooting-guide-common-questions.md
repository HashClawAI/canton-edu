---
title: "常见问题"
slug: "global-synchronizer-troubleshooting-guide-common-questions"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/common-questions.md"
source_title: "Common Questions"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - common-questions
---

# 常见问题

> 验证者搭建、运维与升级相关的常见问题解答。

## 设置

### 我如何加入测试网或主网？

加入测试网需要超级验证者 (SV) 赞助商。请联系与您合作的 SV，或通过 `#validator-operations-onboarding` Slack 渠道寻找赞助商。发起人提交投票以批准您的验证者。该过程通常需要 2-4 周。

主网上线遵循相同的模式，但要求更严格。您需要签署运营商协议，并且必须证明在测试网上成功运行。有关完整清单，请参阅[onboarding 流程](/zh/docs/canton/global-synchronizer-deployment-onboarding-process) 文档。

### 需要开放哪些端口？

您的验证者需要出站访问：

* **TCP 443** -- HTTPS/gRPC-TLS 到 synchronizer sequencer
* **TCP 5432** -- 到您的 PostgreSQL 数据库（如果托管在外部）
* **TCP 443** -- 发送至您的 OIDC 提供商（Auth0、Keycloak 等）

入站访问取决于您的设置：

* **TCP 443** -- 如果您向外部公开 Ledger API 或验证者钱包 UI
* **TCP 26656** -- 如果您运行 CometBFT 节点（对于 SV 运营商）

DevNet 还需要 VPN 连接。

### 运行验证者需要多少钱？

成本分为基础设施费用和网络费用。

**基础设施成本**取决于您的部署选择。云提供商上的最小 Kubernetes 部署运行费用约为每月 500-800 美元（计算、数据库、存储）。单个虚拟机上的 Docker Compose 可能更便宜，但不建议用于生产。

**网络费用**是通过流量支付的，流量是用Canton Coin（CC）购买的。金额取决于您的交易量。验证者获得的奖励可以抵消这些成本。在[Global Synchronizer Foundation](https://sync.global/)网站上查看当前奖励率。

## 操作

### 如何查看我的流量余额？

通过Canton Console：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res1: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

通过验证者 API:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost/api/validator/readyz | jq '.traffic'
```

如果余额不足，请购买更多流量或在`validator-values.yaml`中启用自动充值。

### 我应该多久修剪一次？

经常进行修剪以保持数据库易于管理。常见的计划是每 10 分钟一次，保留 90 天：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

如果您为应用程序运行 PQS（Participant Query Store（PQS）），则可以对参与者使用较短的保留期，因为 PQS 维护自己的查询数据存储。

### 网络重置期间会发生什么？

网络重置很少见，仅发生在 DevNet 和 TestNet 上。 重置期间：

* 所有账本状态都被擦除
* 验证者身份可能需要重新注册
* 您可以使用与初始设置相同的流程重新启动验证者

主网从未被重置，预计也不会被重置。网络升级过程（同步器迁移）保留跨版本更改的状态。

## 升级

### 能否跳过版本？

这取决于升级类型。对于同一 Splice 版本中的次要补丁版本，您通常可以跳过中间补丁。对于涉及同步器迁移的主要版本升级，您必须遵循发行说明中记录的特定升级路径。

如果在您的验证者离线时网络已经向前移动了多个版本，请直接升级到当前网络版本。运行旧版本会导致`You don't speak X.Y.Z`错误，因为网络拒绝不兼容的协议版本。

### 类型 1、类型 2 和类型 3 升级之间有什么区别？

这些类别描述了升级的范围和影响：* **类型 1（补丁）** -- 错误修复和细微改进。无需同步器迁移，预计不会出现停机。通过更新 Helm Chart 版本并运行 `helm upgrade` 来应用。
* **类型 2（次要）** -- 新功能或行为更改。可能需要配置更新。无需同步器迁移，但需要滚动重启。
* **类型 3（主要）** -- 涉及同步器迁移。网络移动到新的同步器 ID，验证者必须更新其数据库配置（例如，`participant_4` 变为 `participant_5`）。通过预定的迁移窗口在所有验证者之间进行协调。

检查每个版本的发行说明以确定其升级类型并遵循相应的过程。

### 如何验证我的验证者正在运行正确的版本？

升级完成后，确认运行版本：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Kubernetes
kubectl -n validator get deploy validator-app \
  -o "jsonpath={.spec.template.spec.containers[0].image}"

# Docker
docker inspect validator-app --format='{{.Config.Image}}'
```

您还可以检查网络的公共验证者状态页面，其中显示每个注册验证者的报告版本。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
