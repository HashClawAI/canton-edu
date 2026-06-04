---
title: "Splice 指标概览"
slug: "global-synchronizer-production-operations-splice-metrics-overview"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/splice-metrics-overview.md"
source_title: "Splice Metrics Overview"
tags:
  - global-synchronizer
  - production-operations
  - splice-metrics-overview
---

# Splice 指标概览

> Canton Network 组件的 Prometheus 指标与抓取说明。

> Canton Network 各组件暴露的 Prometheus 指标及抓取方式

每个节点在端口 10013、路径 `/metrics` 暴露指标，用于健康监控与故障诊断。

<Note>
  应用在端口 10013 的 `/metrics` 路径以 Prometheus 格式暴露指标。
</Note>

验证者节点上暴露指标的组件包括：

* 验证者应用
* 参与方（participant）

超级验证者节点 additionally 还包括：

* SV 应用
* Scan 应用

<div className="todo">
  link to network or component diagram to improve understanding
</div>

## 抓取指标

指标由 OpenTelemetry 构建，以 Prometheus 格式暴露，可由 Prometheus 抓取。完整指标列表见 metrics reference。

### 直方图

直方图以[指数直方图](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exponentialhistogram)暴露，并转换为 [Prometheus native histograms](https://prometheus.io/docs/specs/native_histograms/)。

<Note>
  须用 `-enable-feature=native-histograms` 启用 Prometheus 支持。

  Native histogram 仅支持 protobuf 格式，Prometheus 将改用 protobuf 采集格式。
</Note>

若需改回常规直方图，可为节点添加环境变量：`ADDITIONAL_CONFIG_DISABLE_NATIVE_HISTOGRAMS="canton.monitoring.metrics.histograms=\[\]"`

### 启用指标

#### 在 Helm 部署中启用指标

在 Helm values 中将 `metrics.enable` 设为 `true`（默认 `false`），会创建 `ServiceMonitor` 自定义资源（需集群已安装 Prometheus Operator）。

也可为 chart 添加抓取端口 10013 的 Prometheus scrape 注解。

#### 在 Docker Compose 部署中启用指标

<Note>
  仅适用于验证者节点
</Note>

Docker Compose 部署默认已启用指标：验证者应用为 `http://validator.localhost/metrics`，参与方为 `http://participant.localhost/metrics`。

#### 启用额外指标触发器

验证者应用可配置触发器轮询拓扑状态并导出汇总指标，前缀为 `splice.synchronizer-topology`。具体指标见 `validator-metrics-reference`。

默认关闭。按 Adding ad-hoc configuration 说明，添加环境变量 `ADDITIONAL_CONFIG_TOPOLOGY_METRICS_EXPORT=canton.validator-apps.validator_backend.automation.topology-metrics-polling-interval = 5m` 即可以 5 分钟间隔启用。

## Grafana 仪表板

发行包内含可导入 Grafana 的仪表板，面向 Kubernetes 部署并使用 Prometheus native histogram 查询。

目录位置因 Splice 版本而异：

* Splice `0.6.4` 及更早：使用 `grafana-dashboards/`。
* 自 Splice `0.6.5` 起，验证者运营方使用 `validator-grafana-dashboards/`，超级验证者运营方使用 `sv-grafana-dashboards/`。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
