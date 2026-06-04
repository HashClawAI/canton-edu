---
title: "逻辑同步器升级"
slug: "global-synchronizer-production-operations-logical-synchronizer-upgrade"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/logical-synchronizer-upgrade.md"
source_title: "Logical Synchronizer Upgrades"
tags:
  - global-synchronizer
  - production-operations
  - logical-synchronizer-upgrade
---

# 逻辑同步器升级

> 以极低停机通过 LSU 升级全局同步器协议版本。

> 通过逻辑同步器升级 (LSU) 升级全局同步器的协议版本，网络停机时间非常有限

</>;


<警告>
  逻辑同步器升级 (LSU) 仍在开发中，此处的说明旨在作为主要针对超级验证器的预览，但在完整发布之前可能会发生一些细微的变化。
</警告>

逻辑同步器升级 (LSU) 允许升级同步器的协议版本
**网络停机时间非常有限**，并且验证器操作员和应用程序开发人员在升级方面没有运营开销。
超级验证者仍然必须执行操作步骤来部署后续节点并安排升级，但这些都是在实际升级发生之前异步完成的。

## 高级概述

1. 具有更新协议版本的新 Canton 版本以及兼容的 Splice 版本现已推出。出于测试目的或在某些灾难恢复场景中，这也可以是相同的版本和/或协议版本。
   此版本同时支持新旧协议版本。

2. 验证器和超级验证器升级到新版本，但继续使用旧协议版本运行原始物理同步器。这是定期升级，可以异步完成
   但必须在实际升级时间之前完成。

3. 在SV UI 中创建投票，通过`DsoRulesConfig` 中的`nextScheduledLogical同步器Upgrade` 字段来调度LSU。
   时间表包括

   1. **拓扑冻结时间**：在此时间之后，在升级时间之前无法对任何拓扑事务进行排序，因此特别是不能添加任何参与方，也不能审查任何 Daml 包
   2. **升级时间**：此时原物理同步器上的Daml事务将超时，新的Daml事务将在新的物理同步器上运行
   3. **新物理同步器序列**：通常只是旧序列号加1
   4. **新协议版本**：后继同步器的协议版本

4. 所有 SV 都在其现有节点旁边部署*后继*同步器节点（排序器、中介器，如果不使用 DABFT，还可以选择 CometBFT）。注意：没有新的参与者，参与者被绑定到逻辑同步器，因此它不会在 LSU 上更改。作为其中的一部分，他们还在 SV 和扫描配置中[配置](#super-验证者-deployment-changes)后继同步器。
   此部署应在冻结时间之前完成。

5. 在预定的**拓扑冻结时间**，每个 SV 的 SV 应用程序自动化将拓扑状态传输到后继节点，并在拓扑状态下发布新定序器的定序器 URL（这是冻结时间后唯一可以发布的拓扑事务）。6. 拓扑冻结时间和升级时间之间，SV app
   自动化将定期发送特殊的健康检查事件
   新的物理同步器来验证其健康状况。  每个超
   验证者应该使用他们的指标来验证他们观察到的
   “LSU”中每个超级验证者至少有一个事件
   排序测试仪表板以及 BFT 对等点
   后继节点的连接（CometBFT 或 DABFT）是健康的。

   <div className="todo">添加更多详细信息</div>

7. 在预定的**升级时间**，参与者自动连接到后继同步器。
   SV 自动化将交通控制状态从当前定序器传输到后继定序器。
   后继物理同步器可以配置有较低的初始速率限制，该限制将是
   由 SV 应用程序在可配置的时间后引发，以避免新同步器上的初始流量激增。

   <div className="todo">添加更多详细信息。</div>

8. 后继物理同步器现已完全可用。超级验证器更新其[配置](#super-验证者-deployment-changes)以将原始同步器标记为遗留
   和后继者作为当前同步器。

9. 30 天后，超级验证者删除旧的物理同步器节点部署。超级验证器更新其[配置](#super-验证者-deployment-changes)以删除
   传统同步器配置。

### 路易斯安那州立大学取消

在拓扑冻结时间和升级时间之间，如果后继物理同步器被认为不健康，例如因为健康检查失败，则可以取消升级。
为此，超级验证器的阈值必须向 SV API 上的 `/v0/admin/同步器/lsu/cancel` 端点发送 `POST` 请求。

### 通过前滚 LSU 进行灾难恢复

如果发生灾难导致当前物理同步器不可用，LSU 可以用作前滚恢复机制。
该过程与常规 LSU 类似，但由于当前物理同步器不可用，无法通过投票和拓扑事务进行协调，而是验证者和超级验证者需要手动启动升级。

此过程还可用于从失败的 LSU 中恢复。有两个相关案例：1. LSU 在升级时间之前未取消，但在升级时间之后，无法在后继物理同步器上对任何 Daml 事务和拓扑事务进行排序。在这种情况下，原来的后继同步器可以扔掉并更换
   由一个新的后继同步器，其序列号增加 1（因此与原始非后继同步器相比为 2）。
2. LSU 继续进行，并且某些事务确实在后继物理同步器上进行了排序，但后继物理同步器随后变得不可用。在这种情况下，程序是相同的，但是
   SV 应保持原始同步器和损坏的后继同步器运行（假设它仍然可以服务事件，只是不对新消息进行排序），以允许节点首先赶上并在侧面启动新的后继同步器
   所以他们在一段时间内运行 3 个同步器节点。允许节点尽可能多地跟上，限制了需要通过 ACS 承诺不匹配进行手动解决的去同步的可能性。

具体流程如下：

1.旧的物理同步器被认为已损坏，并且最后排序的消息是在记录时间R。
2. 超级验证器将其配置为旧排序器上的最大排序时间，以保证在该时间之后不会意外排序。这是通过将以下环境变量应用于现有定序器来完成的：

```
- name: ADDITIONAL_CONFIG_SEQUENCER_LSU_MAX_SEQUENCING_TIME
  value: |
    canton.sequencers.sequencer.parameters.lsu-repair.global-max-sequencing-time-exclusive=MAX_SEQUENCING_TIME
```

2. 超级验证人部署后继节点。根据问题的不同，
   后继节点可以配置旧的映像和协议
   如果问题仅限于新版本。  继任者
   序列发生器必须配置两个时间戳：
   `lower-bound-sequencing-time-exclusive` 和
   `upgrade-time`。这些对应于拓扑冻结时间和
   常规 LSU 的升级时间。特别是之后
   `lower-bound-sequencing-time-exclusive` 排序测试消息
   可以在`LSU Sequencing Test`提交并观察
   仪表板。 `upgrade-time`之后所有Daml交易都可以
   已提交。实际的时间戳将通过与所有 SV 的协调来选择。
   时间戳通过后继定序器上的环境变量应用：

<Version title="LSU 排序边界配置" networkData={networkData}>
  <版本选项
    版本=“0.5.18”
    代码={`-名称：ADDITIONAL_CONFIG_SEQUENCER_LSU_SEQUENCE_BOUNDS
值：|
canton.sequencers.sequencer.parameters.parameters.lsu-repair.lsu-sequencing-bounds-override.lower-bound-sequencing-time-exclusive=LOWER_BOUND_SEQUENCING_TIME_EXCLUSIVE
canton.sequencers.sequencer.parameters.parameters.lsu-repair.lsu-sequencing-bounds-override.upgrade-time=UPGRADE_TIME`}
  /><版本选项
    版本=“0.6.3”
    代码={`-名称：ADDITIONAL_CONFIG_SEQUENCER_LSU_SEQUENCE_BOUNDS
值：|
canton.sequencers.sequencer.parameters.lsu-repair.lsu-sequencing-bounds-override.lower-bound-sequencing-time-exclusive=LOWER_BOUND_SEQUENCING_TIME_EXCLUSIVE
canton.sequencers.sequencer.parameters.lsu-repair.lsu-sequencing-bounds-override.upgrade-time=UPGRADE_TIME`}
  />
</版本>

3. 超级验证器等待摄取完成。

4. 超级验证器配置其 SV 应用程序，将拓扑和流量状态从旧的物理同步器传输到后继节点。
   为此，请将以下 helm 值添加到 SV 应用程序：

```
rollForwardLsu:
  newPhysical同步器Serial: NEW_PHYSICAL_SYNCHRONIZER_SERIAL # Must be agreed between SVs, usually existing (broken) 同步器 serial + 1
  newPhysical同步器ProtocolVersion: NEW_PHYSICAL_SYNCHRONIZER_PROTOCOL_VERSION # Must be agreed between SVs, usually existing (broken) 同步器 serial + 1
  exportTimes:
    拓扑ExportTime: TOPOLOGY_EXPORT_TIME # Must be agreed between SVs
    trafficExportTime: TRAFFIC_EXPORT_TIME # Must be agreed between SVs
    upgradeTime: UPGRADE_TIME # Must be agreed between SVs
```

5. 验证者自行启动“程序”。

#### 从失败的 LSU 中恢复，没有任何排序

对于 LSU 已宣布但未取消但
失败并且后继同步器上没有任何排序，那里
是一种无需手动检查摄取的变体
正在完成，并且不需要验证者的显式交互。

为此，请使用以下步骤：

1. 超级验证者在其扫描中配置手动 LSU。

```
rollForwardLsu:
   enabled: true
   upgradeTime: UPGRADE_TIME # Must be agreed between SVs, optional, if not specified it is taken from an existing LSU announcement which should usually be sufficient.
```

2. 验证器应用程序自动化获取该配置并启动手动前滚 LSU 到新同步器。

#### 解决 ACS 不匹配问题

请注意，根据旧同步器失败的具体情况，
如果某些验证器观察到了某个情况，验证器可能会不同步
之前的交易失败，而其他交易则没有。从中恢复
遵循*验证器*的说明。

## 超级验证器部署变更

<div className="todo">更新 helm 值并在此处链接</div>

LSU 需要更改超级验证器的部署。具体来说：1. 参与者现在作为 LSU 的一部分保留。因此，如果您之前假设参与者、定序器和中介器始终作为每个迁移 ID 的一个单元，那么您现在需要将参与者移出该单元。
2. sv app helm 图表上的 `domain` 值应替换为 `同步器s`。 `同步器s.current` 替换之前通过`domain` 配置的同步器。 `同步器s.successor`
   应在部署时配置到后继物理同步器。升级后，`同步器s.current`变为`同步器s.legacy`，`同步器s.successor`变为`同步器s.current`。 30 天后，旧配置应与旧物理同步器一起删除。如果您在 `legacy` 中已经有一个节点，并且尚未停用，请将其移动到 `additionalLegacy`，它接受同步器数组。
   CometBFT 配置也移动到`同步器s.(current|successor|legacy)`。
3. 扫描中的`sequencerAddress`和`mediatorAddress`值应替换为`同步器s.current.sequencer`和`同步器s.current.mediator`。 `同步器s.successor`下对应的值应与
   后续物理同步器的部署。升级后`successor`变为`current`且`current`被移除。
4. 当使用DABFT作为后继节点时，将需要进一步更改。最值得注意的是，当 DABFT 作为定序器 pod 的一部分运行时，cometbft 节点就会消失。音序器 Pod 和 SV 应用程序将需要一些额外的配置。稍后将添加详细信息。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
