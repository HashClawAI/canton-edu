---
title: "修剪"
slug: "global-synchronizer-production-operations-pruning"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/pruning.md"
source_title: "Pruning"
tags:
  - global-synchronizer
  - production-operations
  - pruning
---

# 修剪

> Party、Sequencer与 CometBFT 的修剪配置说明。

> 全局同步器节点的 Sequencer 和 CometBFT 修剪配置

本页面介绍了参与者节点的 Canton 端剪枝和自动剪枝配置。

有关序列器和 CometBFT 层的超级验证者剪枝，请参阅 [SV 剪枝](/zh/docs/canton/global-synchronizer-production-operations-sv-pruning)。

## 参与者节点剪枝

修剪有助于限制数据库存储的大小。参与者节点剪枝是指选择性删除存档合约和旧交易。选择两个选项之一，在易用性和控制之间进行选择：

1. 自动剪枝指示参与节点按照定期的时间表和保留期限进行剪枝。
2. 手动修剪提供了对要修剪的账本偏移量的明确控制。此外，手动修剪允许将修剪与数据库备份和碎片整理等操作过程集成。

作为修剪的先决条件，请放置备份并确保每次修剪参与者节点时都进行备份。具体参见备份与恢复。

### 启用自动修剪

通过指定由以下内容组成的修剪计划来启用自动修剪：

* 指定定期修剪开始时间的 cron 表达式。
* 指定相对于 cron 表达式开始时间的修剪结束时间的最大持续时间。
* 保留期，用于指定相对于当前时间的修剪程度。
* 可选指示是否仅修剪内部存储，或者默认情况下也修剪 Ledger API 可见的存档合约和更新。

例如，要在每周六上午 8 点到下午 4 点（均为 UTC 时间）运行修剪：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant.pruning.set_participant_schedule(
  cron = "0 0 8 ? * SAT",
  maxDuration = 8.hours,
  retention = 90.days,
  pruneInternallyOnly = false,
)
```

在配置为共享公共数据库的高可用性的参与者节点上，必须在活动参与者节点副本上调用修改修剪计划的方法。

有关其他可用自动修剪方法的参考，请参阅自动修剪。

### 执行手动修剪

手动修剪参与者节点允许将修剪与数据库维护操作结合起来，但需要识别明确的分类帐偏移量，直到该分类帐应被修剪。

1. 通过指定要修剪的时间来确定要修剪分类帐的数字分类帐偏移量：

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val offsetToPruneUpTo = participant.pruning.find_safe_offset(timeToPruneUpTo.toInstant)
   ```

   如果没有偏移量对应于指定时间，则`find_safe_offset`方法返回`None`。

2. 在参与者节点上调用手动修剪。

   在几乎所有情况下，选择综合的 `prune` 方法，可以释放最多的存储空间，同时也减少通过 Ledger API 可见的账本部分。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   // The prune() method prunes more comprehensively and should be used in most cases.
   participant.pruning.prune(offsetToPruneUpTo)
   ```

   在某些情况下，除了 `prune` 方法之外，您还可能选择使用 `prune_internally` 方法。通常，您可以在 `prune` 方法之后调用 `prune_internally` 方法，并使用较大的偏移量。例如，通过这种方式，您可以保留三个月的 Ledger API 历史记录，但将内部存储最多删除一个月。

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   // The prune() method prunes more comprehensively and should be used in most cases.
   participant.pruning.prune_internally(offsetToPruneUpTo, None)
   ```

   在配置为高可用性并共享公共数据库的参与者节点上，必须在活动参与者节点副本上调用修剪方法。

`prune` 和 `prune_internally` 方法可能看起来挂起，除非账本偏移量以足够小的增量迭代增加，以便通过多个方法调用进行分段修剪。此外，这些手动方法没有内置机制可以在高可用性故障转移后在另一个节点上恢复。

### 对数据库进行碎片整理

修剪后对数据库进行碎片整理。修剪会从数据库中删除数据，释放空间，但不会调整表的大小。有关如何以最佳方式回收通过修剪释放的空间的更多信息，请参阅有关 `VACUUM` 和 `VACUUM FULL` 的 PostgreSQL 文档。

### 监控修剪进度

监视修剪状态以确定修剪计划是否允许修剪跟上分类帐的增长，并且自动修剪不会由于下面描述的修剪限制原因之一而被卡住。

监控描述“最旧的、未修剪”事件的年龄（以小时为单位）的`daml_修剪_max_event_age`指标。 `max-event-age` 指标不应超过修剪计划`retention` 的值加上间隔长度。例如，如果您的计划指定保留 30 天，并且 cron 要求每周修剪，则 `max-event-age` 必须保持在 37 天以下。如果对于任何节点，`max-event-age`指标超过此上限，请考虑通过减少修剪窗口之间的间隔或增加`maximum duration`修剪计划设置来分配更多时间进行修剪。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/reference/automatic_修剪.rst" hash="6e2b1915" */}

### 自动修剪参考

以下功能可用于设置、修改和读取修剪计划：

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
// 设置具有持续时间和保留期的修剪计划。
修剪.set_schedule("0 0 8 ? * SAT", 8.小时, 90.天)

// 检索当前修剪计划，如果未设置计划，则返回`None`。
val 修剪Schedule = 修剪.get_schedule()

// 设置各个字段来修改现有的修剪计划。
修剪.set_cron("0 /5 * * * ?")
修剪.set_retention(30.days)
修剪.set_max_duration(2.小时)// 清除修剪计划，禁用特定节点上的自动修剪。
修剪.clear_schedule()
```

Refer to the cron specification to customize the 修剪 schedule. Here are a few examples:

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
// 每天晚上 8 点 GMT 修剪两个小时
set_schedule("0 0 20 * * ?", 2.小时, 保留时间)

// 每 5 分钟修剪一次，持续一分钟
set_schedule("0 /5 * * * ?", 1.分钟, 保留)

// 针对某一特定日期进行修剪
set_schedule("0 0 0 31 12 ? 2025", 1.day, 保留)
````

为了指定可靠的修剪窗口结束时间的最大持续时间，cron 表达式的前导字段不能是通配符 (`\*`)，如前面的示例所示。如果小时字段是固定的，那么分钟和秒的字段也必须是固定的。

#### 时间表格式

Cron 表达式的格式为七个空格分隔的字段：

|领域|类型和有效值\* |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
|秒|从 `0` 到 `59` 的编号 |
|分钟|从 `0` 到 `59` 的编号 |
|小时 |从 `0` 到 `23` 的编号 |
|每月的哪一天 |从 `1` 到 `31` 的编号 |
|月 |从 `0` 到 `11` 的数字（`0` = 一月） **或** 月份名称的前三个字母（`JAN`、`FEB`、`MAR` 等）|
|一周中的哪一天 |从`1`到`7`的数字（`1`=星期日）**或**当天名称的前三个字母（`SUN`、`MON`、`TUE`等）|
|年份（可选）|编号从 `1900` 到 `2099` |

*\*用“从 .. 到 ..”指定的范围包括两个端点。*

请注意，尽管根据前面的定义，日期值可能有效，但它可能与某些月份中的实际日期（例如 11 月 31 日）不对应。如果您安排在该月的三十一日进行修剪，则将跳过少于 31 天的每个月。

#### 高级计划格式* 您可以构建值的**列表和范围**。例如，一周中的某一天可以是一个范围，例如 `MON-FRI` 表示星期一到星期五，或者 `TUE,FRI` 专门表示星期二和星期五。或者您可以混合使用两者，例如，`MON,WED-FRI`，意思是“星期一，以及星期三到星期五”。
* 使用**星号** (`*`) 作为通配符，表示“所有可能的值”。
* 使用 **问号** (`?`) 作为通配符，在月份和星期几字段中表示“任何值”。例如，要指定“每周一中午”，请使用 `?` 字符来指示该月中的任意一天有效：`0 0 12 ? * MON`
* 要将**增量**应用于数值，请使用斜杠字符 (`/`)。例如，小时字段中的值`1/2`表示“从凌晨 1 点开始每两小时一次”（凌晨 1 点、凌晨 3 点、上午 5 点等）。

以下是一些有效时间表的示例：

* `0 30 * * * *` 每小时半点
* `0 5/15 12,18-20 * * *` 每十五分钟一班，从五点开始、中午、下午 6 点至 8 点
* `0 5/15 12,18-20 ? * MON,THU` 同上，但仅限周一和周四
* `0 0 22 1 * ?` 每个月的第一天晚上 10 点

有关 cron 表达式的更多信息，请参阅 [Apache Log4j API 文档](https://logging.apache.org/log4j/2.x/javadoc/log4j-core/org/apache/logging/log4j/core/util/CronExpression.html)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
