---
title: "同步器监控"
slug: "global-synchronizer-extension-synchronizers-synchronizer-monitoring"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/synchronizer-monitoring.md"
source_title: "Synchronizer Monitoring"
tags:
  - global-synchronizer
  - extension-synchronizers
  - synchronizer-monitoring
---

# 同步器监控

> Sequencer 与 Mediator 节点健康监控与检查。

> 监控Sequencer和中介器的运行状况、检查中介器状态并解决同步器问题


本页介绍如何检查和了解 Sequencer 节点的当前状态，以及如何使用运行状况检查持续监控它。

另请参阅有关如何检查节点状态并监控其运行状况的通用指南。

## 交互式检查节点状态

Canton 控制台可用于交互式检查状态并获取有关正在运行的 Sequencer 节点的信息。针对感兴趣的 `sequencer` 参考执行以下命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer.health.status
```

对于从未连接到同步器的Sequencer节点，输出如下所示：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res1: NodeStatus[sequencer1.Status] = NotInitialized(active = true, waitingFor = Initialization)
```

对于健康状态，希望Sequencer节点报告类似于以下内容的状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res2: NodeStatus[sequencer1.Status] = Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
    同步器 id: da::1220222f081c6c7d7dd4cba1612b1c80e12e0a7c1eef2139be2d928d903fccf9f090::35-0
    Uptime: 7.080586s
    Ports: 
    	public: 33028
    	admin: 33029
    Connected participants: 
    	PAR::participant2::1220a4d7463b...
    	PAR::participant1::12201ff69b1d...
    	PAR::participant3::1220d6908163...
    Connected mediators: None
    Sequencer: SequencerHealthStatus(active = true)
    details-extra: None
    Components: 
    	db-storage : Ok()
    	sequencer : Ok()
    Accepts admin changes: true
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

组件状态包括Sequencer节点本身的`sequencer`和`db-storage`。后者不是 `Ok()` 表明数据库存储后端或其连接存在问题。

该状态还显示连接到Sequencer节点的同步器成员。这些成员对 Sequencer 节点具有活跃订阅。他们可以将新提交发送到同步器，并从同步器读取有序事务。

## BFT Orderer 对等网络状态

对于 BFT（拜占庭容错）Sequencer节点，您可以检查与其 BFT 对等网络的其他对等点的连接状态。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.bft.get_peer_network_status()
    res3: com.digitalasset.canton.同步器.sequencer.block.bftordering.admin.SequencerBftAdminData.PeerNetworkStatus = PeerNetworkStatus(
      endpoint statuses = Seq(
        PeerEndpointStatus(
          p2pEndpointId = Id(url = "http://localhost:33030", tls = false),
          health = PeerEndpointHealth(status = Authenticated(sequencerId = SEQ::sequencer3::122076e8bfb8...))
        ),
        PeerEndpointStatus(
          p2pEndpointId = Id(url = "http://localhost:33031", tls = false),
          health = PeerEndpointHealth(status = Authenticated(sequencerId = SEQ::sequencer2::12203a55a279...))
        )
      )
    )
```

## 健康检查端点

要使用外部工具监控 Sequencer 节点的运行状况，请使用 Canton 节点运行状况检查端点。

如何检查节点状态并监控其运行状况的通用指南中描述了启用端点。

Sequencer Node 公开一对健康检查端点：`readiness`（接受流量）和`liveness`（不需要重新启动），分别用于使用 Kubernetes 等工具进行负载平衡和编排。

`readiness`端点对应于`sequencer`（包括BFT Orderer）的健康状况，`liveness`端点对应于上述状态命令输出中`db-storage`组件的健康状况。这意味着数据库连接的致命故障会导致 Sequencer 节点重新启动。

## 活跃度看门狗

可以将 Sequencer 节点配置为在变得不健康时自动退出。以下配置启用内部看门狗服务，该服务每隔 `check-interval` 秒检查 Sequencer 节点的运行状况，并在 `liveness` 报告节点运行状况不佳后 `kill-delay` 秒后终止进程。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
watchdog {
  enabled = true
  check-interval = 15s
  kill-delay = 30s
}
```将以上内容放在 Sequencer 节点配置文件中的`canton.sequencers.sequencer.parameters`下。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/observe/mediator_health.rst" hash="572f2273" */}

# 检查并监控Mediator 节点的健康状况

本页介绍如何检查和了解Mediator 节点的当前状态，以及如何使用运行状况检查持续监控它。

另请参阅有关如何检查节点状态并监控其运行状况的通用指南。

## 交互式检查节点状态

Canton 控制台可用于交互式检查状态并获取有关正在运行的Mediator 节点的信息。针对感兴趣的 `mediator` 参考执行以下命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediator.health.status
```

对于从未连接到同步器的Mediator 节点，输出如下所示：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.status
    res1: NodeStatus[mediator1.Status] = NotInitialized(active = true, waitingFor = Initialization)
```

对于健康状态，期望Mediator 节点报告类似于以下内容的状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.status
    res2: NodeStatus[mediator1.Status] = Node uid: mediator1::12200929934059da3e012af672ee8a5d26a7e4b3e5084920be298f791f7619843c78
    同步器 id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
    Uptime: 0.398993s
    Ports: 
    	admin: 32784
    Active: true
    Components: 
    	db-storage : Ok()
    	sequencer-client : Ok()
    	sequencer-connection-pool : Ok()
    	sequencer-subscription-pool : Ok()
    	internal-sequencer-connection-sequencer1-0 : Ok()
    	subscription-sequencer-connection-sequencer1-0 : Ok()
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

组件状态包括数据库存储后端的`db-storage`和`sequencer-client`。后者不是 `Ok()` 表明同步器连接存在问题。

该状态还显示Mediator 节点的 `Active: true` 或 `Active: false`，这在高可用性 (HA) 配置中指示此Mediator 节点是否是活动 HA 副本。

## 健康检查端点

要使用外部工具监控Mediator 节点的运行状况，请使用 Canton 节点运行状况检查端点。

如何检查节点状态并监控其运行状况的通用指南中描述了启用端点。

Mediator 节点公开一对健康检查端点：`readiness`（接受流量）和`liveness`（不需要重新启动），分别用于使用 Kubernetes 等工具进行负载平衡和编排。

`readiness`端点对应Mediator存储后端的健康状况，`liveness`端点对应上述状态命令输出中`sequencer-client`组件的健康状况。这意味着Mediator 节点的 Sequencer 连接发生致命故障，需要重新启动Mediator 节点。

## 活跃度看门狗

Mediator 节点可以配置为在变得不健康时自动退出。以下配置启用内部看门狗服务，该服务每`check-interval`秒检查Mediator 节点的运行状况，并在`liveness`报告节点不健康后的`kill-delay`秒后终止该进程。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
watchdog {
  enabled = true
  check-interval = 15s
  kill-delay = 30s
}
```

将以上内容放在Mediator节点配置文件中的`canton.mediators.mediator.parameters`下。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/observe/mediator_inspection.rst" hash="addb7204" */}

# 中介者检查

调解器检查提供对与最终交易相关的元数据（也称为判决）的访问，以深入了解同步器上完成的交易。本页介绍如何从管理控制台获取判决。

## 从调解员处获取裁决

使用 `裁决s` admin 命令检查判决：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.canton.data.CantonTimestamp
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.inspection.裁决s(fromRecordTimeOfRequestExclusive = CantonTimestamp.MinValue, maxItems = 1)
    res2: Seq[com.digitalasset.canton.mediator.admin.v30.裁决] = List(
      裁决(
        submittingParties = Vector(
          "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
        ),
        submittingParticipantUid = "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c",
        裁决 = VERDICT_RESULT_ACCEPTED,
        finalizationTime = Some(
          value = Timestamp(
            seconds = 1777916965L,
            nanos = 327154000,
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        recordTime = Some(
          value = Timestamp(
            seconds = 1777916964L,
            nanos = 63195000,
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        mediatorGroup = 0,
        views = TransactionViews(
          value = TransactionViews(
            views = Map(
              0 -> TransactionView(
                informees = Vector(
                  "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                confirmingParties = Vector(
                  Quorum(
                    parties = Vector(
                      "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                    ),
                    threshold = 1
                  )
                ),
                subViews = Vector(),
                viewHash = <ByteString@2c4c9a07 size=34 contents="\022 \312\320Fj\310\233\372\000\b\314\036\034C\300\006\311\215\363\227\343j\210\317\350\254}6\"\2639\362\300">
              )
            ),
            rootViews = Vector(0)
          )
        ),
        updateId = "12200320c85e320ef71daaca64b8ee8c00e79b0a2a0278f9fe5c5737df35af511cba"
      )
    )
```

该命令需要起始记录时间（不包括）和要列出的最大判定数。 `CantonTimestamp.MinValue`可以用来获取从头开始的所有判决。

输出是判决列表。每个判决包含其结果（接受、拒绝、未指定）、提交参与者、提交方、最终确定时间、相应确认请求的记录时间以及交易视图的元数据等。

{/* TODO：管理 API Protobuf 参考文档可用后立即链接。 https://github.com/DACH-NY/canton/issues/26126 */}

有关 `裁决s` admin 命令的更多详细信息，请查看参考文档。

要了解有关相关概念的更多信息，请参阅中介器概述。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/troubleshoot/index.rst" hash="44a81d5c" */}

链接到参与者文档以获取一般故障排除指南。

# 同步器故障排除

## 对于新加入的Sequencer，Sequencer订阅失败

新加入的 Sequencer 仅提供比加入期间拍摄的“加入快照”更新的事件。此外，某些事件可能属于在 Sequencer 加入之前发起的交易，但 Sequencer 无法签署此类事件并用“墓碑”替换它们。如果参与者（或中介者）过早连接到新加入的 Sequencer，并且订阅遇到逻辑删除，则 Sequencer 订阅将中止，并出现指定 `InvalidCounter` 或 `SEQUENCER_TOMBSTONE_ENCOUNTERED` 的 `FAILED_PRECONDITION` 错误。如果发生这种情况，参与者或调解者应在切换到新加入的 Sequencer 之前连接到具有较长序列事件历史记录的另一个 Sequencer。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
