---
title: "可观测性"
slug: "appdev-modules-m4-observability"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-observability.md"
source_title: "Observability"
tags:
  - appdev
  - modules
  - m4-observability
---

# 可观测性

> 为 Canton 应用配置日志、指标与仪表盘

在生产环境运行 Canton 应用，需要了解后端与底层 Canton 节点的行为。本节从应用开发者视角介绍日志、指标与仪表盘。

## 日志

### 使用 Logback 的结构化日志

Canton 节点与 cn-quickstart 均使用 [Logback](https://logback.qos.ch/) 记录日志。默认配置向控制台输出人类可读日志；生产环境应切换为结构化 JSON 输出，便于 ELK 栈或 Grafana Loki 等日志聚合系统摄取。

典型的 JSON 输出 `logback.xml` 配置：

```xml theme={"theme":{"light":"github-light","dark":"github-dark"}}
<configuration>
  <appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="net.logstash.logback.encoder.LogstashEncoder">
      <includeMdcKeyName>command-id</includeMdcKeyName>
      <includeMdcKeyName>party</includeMdcKeyName>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="JSON" />
  </root>
</configuration>
```

在 MDC（Mapped Diagnostic Context）中包含 `command-id`，可将单条 Ledger API 命令在后端日志中追踪，并与处理该命令的 Canton 节点日志关联。

### 应记录什么

应用日志应聚焦：

* **命令提交** — 每次 Ledger API 调用前记录 command ID、template 或 choice 名称、提交 party
* **命令完成** — 记录成功或失败，失败时含错误码
* **PQS 查询性能** — 记录慢查询（超过自定义阈值）及 SQL 与耗时
* **认证事件** — 记录 token 验证失败与 party 解析

生产环境避免记录合约 payload，可能含不应离开 validator 边界的私密数据。

## 指标

### Prometheus 端点

Canton 节点暴露 Prometheus 兼容指标端点。本地运行 cn-quickstart 时，validator 指标默认在 `http://localhost:10013/metrics`。

从应用视角应监控的关键指标：

* `daml_commands_submissions_total` — 提交的命令总数，按状态（成功、失败）细分
* `daml_commands_completions_total` — 已完成命令及其结果状态
* `daml_commands_delayed_submissions` — 因背压延迟的命令
* `daml_execution_total` — Daml 解释次数与耗时
* `canton_sequencer_client_submissions_sequencing_time` — 从提交到排序的时间，反映 synchronizer 延迟

### 应用层指标

cn-quickstart 通过服务方法上的 `@WithSpan` 注解集成 OpenTelemetry 追踪，可将 span 导出到 Jaeger、Zipkin、Grafana Tempo 等 OpenTelemetry 兼容后端。

后端自定义指标可用 Micrometer（Spring Boot 内置）或 OpenTelemetry 指标 API：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@WithSpan
public CompletableFuture<ResponseEntity<List<License>>> listLicenses() {
    // @WithSpan 注解自动创建 trace span
    return damlRepository.findActiveLicenses()
        .thenApply(licenses -> ResponseEntity.ok(licenses));
}
```

## 仪表盘

### cn-quickstart 中的 Grafana

cn-quickstart 在 `ops/` 目录提供预配置的 Grafana 仪表盘。运行 `make start` 后，Grafana 在 `http://localhost:3000` 可用。

内置仪表盘涵盖：

* **Ledger API 概览** — 命令提交速率、延迟与错误率
* **Canton 节点健康** — JVM 内存、gRPC 连接状态、sequencer 连通性
* **PQS 索引** — 账本 head 与 PQS 投影 offset 之间的滞后

### 构建自定义仪表盘

若添加应用专属指标，可创建结合 Canton 节点指标与后端指标的 Grafana 仪表盘。实用起始布局：

* **顶行** — 命令提交速率与错误率（来自 Canton 节点 Prometheus 端点）
* **中间行** — 应用 REST 端点延迟（来自 Spring Boot Actuator 或 OpenTelemetry）
* **底行** — PQS 查询延迟与关键 template 的活跃合约数量

### 告警

为影响应用可靠性的条件设置告警：

* 命令错误率超过阈值（如超过 5% 提交失败）
* PQS 索引滞后超过数秒（查询返回陈旧数据）
* Traffic 预算低于 auto-top-up 阈值（交易将开始失败）
* Validator 上 JVM 堆使用率持续高于 80%

## 延伸阅读

* [后端开发](/zh/docs/canton/appdev-modules-m4-backend-dev) — 与可观测性配套的错误处理模式
* [Canton Coin 与 Traffic](/zh/docs/canton/appdev-modules-m4-canton-coin) — 监控 traffic 预算
* [cn-quickstart 仓库](https://github.com/digital-asset/cn-quickstart) — 预配置的可观测性栈

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
