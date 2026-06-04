---
title: "错误处理"
slug: "appdev-modules-m7-error-handling"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-error-handling.md"
source_title: "Error Handling"
tags:
  - appdev
  - modules
  - m7-error-handling
---

# 错误处理

> Canton 应用的错误处理与恢复模式

Canton 应用面向分布式、多方账本。错误分不同类别，每类需不同恢复策略。本文涵盖常见错误类型及后端处理方式。

## 错误类别

### 命令拒绝

命令在到达 synchronizer 前被 Ledger API 拒绝。常见原因：

* **INVALID_ARGUMENT** — 载荷与模板或 choice 签名不匹配（字段类型错误、缺必填字段）
* **NOT_FOUND** — 引用的 contract ID 不存在或对提交 party 不可见
* **PERMISSION_DENIED** — 已认证 party 无权执行该操作

此类错误通常表示应用逻辑 bug 或陈旧数据。重试相同命令结果相同。应修复根因：更正载荷、重新查询有效 contract ID 或检查 party 授权。

### 争用（Contention）

两个或多个命令同时试图消费同一合约时发生争用。仅一个成功，其余收到 **FAILED_PRECONDITION**（或 `ABORTED`），表示合约已被归档。

多方应用中这很正常。两用户可能几乎同时对同一合约行使同一 choice。Canton 一致性模型保证仅一个成功。

### 超时

若 synchronizer 在配置截止时间内未处理命令，`StatusRuntimeException` 可能为 `DEADLINE_EXCEEDED`。网络拥塞或对手方 validator 响应慢时会出现。

超时**不**意味着命令失败。可能已成功但响应未及时返回。重试前请查完成流或 PQS 确认命令是否已应用。

### 流量不足

Validator 流量预算耗尽时，提交失败并提示流量不足。这不是瞬时错误——在预算补充（手动或自动充值）前重试无效。

流量额度管理见 [Canton Coin and Traffic](/zh/docs/canton/appdev-modules-m4-canton-coin)。

## 处理争用

消费型合约上的争用是 Canton 应用最常见错误模式。标准做法：

1. **捕获错误** — 在 gRPC 响应中识别 `FAILED_PRECONDITION` 或 `ABORTED`
2. **重读合约** — 用 PQS 查当前状态。目标合约可能已归档，竞争交易可能已创建新活跃合约
3. **用新 command ID 重提交** — 针对当前合约构建新命令并以新 command ID 提交

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
int maxRetries = 3;
for (int attempt = 0; attempt < maxRetries; attempt++) {
    try {
        var contract = damlRepository.findActiveAsset(assetId).join();
        if (contract.isEmpty()) {
            throw new NotFoundException("Asset no longer active");
        }
        ledger.exerciseAndGetResult(
            contract.get().contractId, choice, UUID.randomUUID().toString()
        ).join();
        return; // success
    } catch (CompletionException e) {
        if (isContention(e) && attempt < maxRetries - 1) {
            Thread.sleep((long) Math.pow(2, attempt) * 100); // exponential backoff
            continue;
        }
        throw e;
    }
}
```

重试间使用指数退避，否则竞争命令会持续碰撞。

### 何时不应重试

以下情况勿重试：

* **INVALID_ARGUMENT** — 命令本身错误
* **PERMISSION_DENIED** — 重试间授权不会变
* **流量不足** — 问题是流量预算而非命令

## 幂等命令提交

Ledger API 按 command ID 去重。相同 ID 的第二次提交视为重复并返回第一次结果。

据此使后端幂等：

* 根据操作输入生成确定性 command ID（如用户 ID、操作类型与前端 nonce 的哈希）
* 网络故障未收到响应时，用相同 command ID 重提交
* Ledger API 返回原结果而非执行两次

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
String commandId = "renew-license-" + licenseNum + "-" + requestNonce;
ledger.exerciseAndGetResult(contractId, renewChoice, commandId).join();
// Safe to retry with the same commandId if the response is lost
```

去重窗口可配置。默认对多数应用足够；若操作跨很长时间，确认窗口覆盖重试时间范围。

## 完成流监控

Ledger API 完成流报告每个已提交命令的最终状态。订阅它以可靠跟踪结果：

* **成功完成** 确认交易已提交
* **失败完成** 含错误码与详情
* **预期窗口内无完成** 暗示命令在到达 synchronizer 前丢失

cn-quickstart 中同步 `CommandService`（而非 `CommandSubmissionService`）在内部等待完成并单次往返返回结果。若用异步 `CommandSubmissionService`，需自行监控完成。

## 后端恢复模式

### 启动恢复

后端重启时可能有结果未知的在途命令。启动时：

1. 从最后已知 offset 读取完成流
2. 将在途命令与完成状态对账
3. 对从未提交的命令（无完成且 PQS 无匹配合约）重试

### 熔断器

Ledger API 不可用时（validator 重启、网络分区），用熔断器包装提交逻辑。连续失败达配置次数后停止提交并向调用方返回服务不可用。定期探测 Ledger API 以检测恢复。

### 死信处理

重试耗尽仍失败的命令应记录完整上下文（command ID、模板、choice、参数、错误）并送入死信队列或表，便于审计与人工处理边缘情况。

## 延伸阅读

* [Backend Development](/zh/docs/canton/appdev-modules-m4-backend-dev) — Ledger API 客户端与错误处理示例
* [Canton Coin and Traffic](/zh/docs/canton/appdev-modules-m4-canton-coin) — 避免提交流量失败
* [Observability](/zh/docs/canton/appdev-modules-m4-observability) — 错误追踪的日志与指标

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
