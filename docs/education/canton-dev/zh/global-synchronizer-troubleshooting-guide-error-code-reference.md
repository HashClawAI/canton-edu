---
title: "常见错误码"
slug: "global-synchronizer-troubleshooting-guide-error-code-reference"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/error-code-reference.md"
source_title: "Common Error Codes"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - error-code-reference
---

# 常见错误码

> 验证者运维常见 Canton/Splice 错误码与处理步骤。

Canton 和 Splice 错误代码遵循结构化格式：`CATEGORY_ERROR_NAME(severity, retryability)`。严重性范围从 0（信息性）到 9（严重）。 `0` 的可重试性意味着错误不可重试；其他值指示重试逻辑的错误类别。

此页面列出了验证者操作员最常遇到的错误代码。

## 参与者错误

### PARTICIPANT_TOPOLOGY_UNKNOWN_PARTIES

* **消息：** `Parties not known on synchronizer`
* **原因：** 命令中引用的一方尚未在synchronizer上注册。当本地创建一方但拓扑事务尚未传播时，就会发生这种情况。
* **解决方案：** 等待几秒钟以进行拓扑传播。如果错误仍然存​​在，请使用 Canton Console 中的 `participant.parties.list()` 验证您的验证者上是否已启用该方。

### PARTICIPANT_PRUNING\_NOT\_SUPPORTED\_IN\_COMMUNITY

* **消息：** `Pruning is not supported in the community edition`
* **原因：** 您正在运行Canton Community Edition，它不支持修剪。
* **解决方案：** 升级到 Canton Enterprise，这是 全局synchronizer 验证者所必需的。

### PARTICIPANT_TRAFFIC_BELOW_LIMIT

* **消息：** `Insufficient traffic for submission`
* **原因：** 您的验证者的流量余额太低，无法将交易提交给Sequencer。
* **解决方案：** 通过验证者 API 购买额外流量或启用自动充值。有关详细信息，请参阅[交易失败](/zh/docs/canton/global-synchronizer-troubleshooting-guide-transaction-failures)。

## Sequencer错误

### SEQUENCER_请求\_拒绝

* **消息：** `The sequencer refused to sequence the send request`
* **原因：** Sequencer拒绝该消息。常见原因：发送方未注册、消息超过最大大小、或发送方流量余额不足。
* **解决方案：** 检查您的验证者是否已正确启动并且具有足够的流量。如果消息很大，请考虑将其拆分为较小的事务。

### Sequencer\_订阅\_丢失

* **消息：** `Lost subscription to sequencer`
* **原因：** 到Sequencer的 gRPC 流被中断。网络不稳定、Sequencer重新启动或负载平衡器超时可能会导致此问题。
* **解决方案：** 验证者自动重新连接。如果没有，请检查与Sequencer的网络连接并重新启动验证者。

### SEQUENCER_墓碑\_成员

* **消息：** `Member has been tombstoned`
* **原因：** 您的验证者被从synchronizer中逐出，通常是由于长时间不活动或治理决策。
* **解决方案：** 联系您的 SV 赞助商，了解驱逐发生的原因以及是否可以重新加入。

## 中介错误

### 调解员\_说\_TX\_超时\_OUT

* **消息：** `Rejected transaction as the mediator did not receive sufficient confirmations within the expected timeframe`
* **原因：** 一方或多方未能及时确认交易。错误上下文中的`unresponsiveParties`字段标识哪些方没有响应。
* **解决方案：** 如果无响应的一方是您，请检查验证者的运行状况、流量平衡和数据库性能。如果是交易对手，请联系其运营商。

### 中介\_INVALID\_MESSAGE

* **消息：** `The mediator received an invalid message`
* **原因：** 协议级错误，通常是由发送方和中介者之间的版本不匹配引起的。
* **解决方案：** 验证您的验证者正在运行与网络相同的协议版本。如果落后就升级。

## ACS 承诺错误

### ACS\_COMMITMENT\_MISMATCH

* **消息：** `ACS commitment mismatch detected`
* **原因：** 您的验证者的活动合约集 (ACS) 状态与预期承诺不匹配。这是一个严重的一致性问题。
* **解决方案：** 此错误需要调查。检查数据库是否损坏或同步器迁移不完整。捕获完整日志并联系 [da-support@digitalasset.com](mailto:da-support@digitalasset.com) 提供详细信息。

### ACS\_承诺\_降级

* **消息：** `ACS commitment computation is degraded`
* **原因：** 承诺计算无法及时完成，通常是因为数据库过载。
* **解决方案：** 检查数据库性能。确保修剪已启用并正在运行。如有必要，增加数据库 IOPS。

## 一般错误### 通用\_配置\_错误

* **消息：** `Cannot convert configuration`
* **原因：** 配置值缺失、为空或类型错误。错误信息包含具体的配置路径。
* **解决方案：** 根据您的配置文件和环境变量检查错误中提到的路径。请参阅[配置问题](/zh/docs/canton/global-synchronizer-troubleshooting-guide-configuration-problems)。

### 数据库存储降级

* **消息：** `Database storage is degraded`
* **原因：** 数据库查询花费的时间比预期的要长。连接池可能已饱和。
* **解决方案：** 检查数据库磁盘空间、IOPS 和活动查询计数。如果表大小较大，则启用修剪。

### 包\_选择\_失败

* **消息：** `No package found for module`
* **原因：** 所需的 Daml 包未上传或未在所涉及的验证者之一上进行审查。
* **解决方案：** 在验证者上上传并审查 DAR 文件。与交易对手协调，对其进行同样的操作。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
