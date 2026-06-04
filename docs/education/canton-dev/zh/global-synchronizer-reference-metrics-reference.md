---
title: "Splice 指标参考"
slug: "global-synchronizer-reference-metrics-reference"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/metrics-reference.md"
source_title: "Splice Metrics Reference"
tags:
  - global-synchronizer
  - reference
  - metrics-reference
---

# Splice 指标参考

> Canton Network 验证者与超级验证者节点监控指标参考。

> Canton Network验证人和超级验证者节点暴露的监控指标参考

您可以使用就绪端点检查验证者的运行状况。所有 CN 应用程序都提供 `/readyz` 和 `/livez` 端点，用于就绪性和活性探测。

* **检查准备情况**

  * 在 Kubernetes 中：已配置就绪和活跃探针。

    您还可以使用以下命令手动检查验证者准备情况：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl exec &lt;pod-name&gt; -n <namespace> -- curl -v http://localhost:5003/api/验证者/readyz
    ```

  * 在 Docker 中：例如运行以下命令来检查容器内验证者的活跃度：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker exec &lt;container-name&gt; -- curl -v http://localhost:5003/api/验证者/livez
    ```

  如果验证者已准备就绪并处于活动状态，则在这两种情况下，您都应该期望 HTTP 状态代码 200。

* **使用指标**

  `splice_store_last_ingested_record_time_ms` 指标表示每个验证者存储中最后摄取的记录时间。它可用于跟踪节点的一般活动：

  * 如果该值随着时间的推移继续增加，则您的节点处于活动状态并与网络保持同步。请注意，只有当您的节点实际接收新交易时，它才会前进。对于收集验证者活跃度奖励的验证者来说，这种情况每轮都会发生，因此你应该期望你的延迟永远不会超过 20 分钟。
  * 如果保持不变，可能需要进一步调查。

  有关更多详细信息以及要在其专用仪表板`Splice Store Last Ingested Record Time`上可视化此指标，请参阅有关指标的文档。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
