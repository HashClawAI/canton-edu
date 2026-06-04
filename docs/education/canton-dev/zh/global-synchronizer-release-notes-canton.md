---
title: "Canton 发布说明"
slug: "global-synchronizer-release-notes-canton"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/release-notes/canton.md"
source_title: "Canton"
tags:
  - global-synchronizer
  - release-notes
  - canton
---

# Canton 发布说明

> Canton 工具（含 PQS、Daml Shell、Daml 语言等）发布说明。

> Canton 工具的发行说明，包括 PQS、Daml Shell、Daml 语言等。

最新的 Canton 稳定版本是从上游发行说明中逐字复制的。有关完整的 Canton 发行历史记录（包括旧版本），请参阅 [数字资产博客上的 Canton 发行说明](https://blog.digitalasset.com/developers/release-notes/author/curtis-hrischuk)。

## Canton 3.4.11 发布

Canton 3.4.11 已于 2026 年 2 月 16 日发布。

### 总结

此版本改进了性能、可观察性和可靠性。

作为此补丁版本升级的一部分，需要进行数据库迁移，并且
由坎顿演奏。

### 新消息

#### 免费确认回复

添加了新的流量控制参数：`freeConfirmationResponses`。
当在启用流量控制的同步器上设置为 true 时，确认响应不会消耗流量。
默认为`false`。

#### 新的拓扑处理和客户端架构

拓扑处理已被显着重构。之前，它用于执行大量的顺序数据库
拓扑事务验证期间的查找。新的验证将批次的所有数据预取到
通过缓存写入，仅在批处理结束时保留数据。这意味着之前
一批 100 笔交易需要 200-300 db 往返才能处理，现在已减少到有效 2 db 操作
（一批读取，一批写入）。

此外，现在还利用相同的直写式缓存进行读取处理，其中构建拓扑状态
直接从缓存中获取，避免进一步的数据库往返。

新组件可以使用以下方式打开和控制

```
canton.<type>.<name>.拓扑 = {
       use-new-processor = true // can be used without new client
       use-new-client = true // can only be used with new processor
       // optional flags
       enable-拓扑-state-cache-consistency-checks = true // enable in the beginning for additional consistency checks for further validation
       拓扑-state-cache-eviction-threshold = 250 // what is the oversize threshold that must be reached before we start eviction
       max-拓扑-state-cache-items = 10000 // how many items to keep in cache (uid, transaction_type)
}
```

拓扑状态缓存还将使用标签“拓扑”公开适当的缓存指标。

#### 性能改进

* 修复了私有存储缓存，以防止过多的数据库读取。

* 为许多验证者订阅提供服务的Sequencer节点不再因从数据库读取任务而过载。
  并行度通过`sequencers.<sequencer>.parameters.batching.parallelism`配置。请注意，这
  配置设置不仅用于限制事件读取，还用于Sequencer中的其他位置。

* 重放 ACS 承诺处理器的 ACS 更改具有较小的内存开销：
  * 更改从数据库中批量加载
  * ACS 更改可能较小，因为我们删除了取消的激活和停用。
    这对于短期合约特别有用

* ACS 承诺表上的附加 DB 索引可提高承诺修剪的性能。这需要数据库迁移。

* 添加了Mediator异步处理事件的模式。默认情况下启用此功能。
  在新的异步模式中，同一请求id的事件是顺序处理的，但不同请求id的事件是并行处理的。
  可以使用`canton.mediators.<mediator-name>.mediator.asynchronous-processing = false`关闭异步模式。

* 调解器现在批量获取和存储最终响应。可以通过以下参数配置批处理行为：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.mediators.<mediator>.parameters.batching {
  mediator-fetch-finalized-responses-aggregator {
    maximum-in-flight = 2 // default
    maximum-batch-size = 500 // default
  }
  mediator-store-finalized-responses-aggregator {
    maximum-in-flight = 2 // default
    maximum-batch-size = 500 // default
  }
}
```* 新的参与者配置标志`canton.参与方s.<参与方>.parameters.commitment-asynchronous-initialization`启用ACS承诺处理器的异步初始化。如果参与者管理大量不同利益相关者群体的活动合约，这会加速同步器连接，但会增加内存和数据库负载。

* 由于性能原因，默认禁用最后错误日志。您可以通过将 `--log-last-errors=true` 传递给 canton 二进制文件来重新启用之前的行为。

#### 可观测性改进

* 附加Sequencer指标：
  * 更多 `daml.sequencer.block.stream-element-count` 指标值以及来自Sequencer读取器中 Pekko 流的 `flow` 标签
  * 新的`daml.sequencer.public-api.subscription-last-timestamp`指标以及通过会员订阅读取的最后时间戳，
    标记为`subscriber`
  * 2 个新指标用于监控事件缓冲区`daml.sequencer.head_timestamp` 和 `daml.sequencer.last_timestamp` 涵盖的时间间隔

* ACS 承诺处理器的其他指标：`daml.participant.sync.commitments.last-incoming-received`、`daml.participant.sync.commitments.last-incoming-processed`、`daml.participant.sync.commitments.last-locally-completed` 和 `daml.participant.sync.commitments.last-locally-checkpointed`。

* Sequencer中的日志记录改进（围绕事件信号器和Sequencer读取器）。

* Canton 启动日志记录：现在可以配置启动日志级别，该级别将在超时后重置，即：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.monitoring.logging.startup {
  log-level = "DEBUG"
  reset-after = "5 minutes"
}
```

* Sequencer进度监控器：现在可以为Sequencer节点在其自己的订阅上的进度启用监视器。
  * 与异步编写器相关的误报已修复
  * 添加了警告操作来终止Sequencer节点
  * 配置：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Future supervision has to be enabled
canton.monitoring.logging.log-slow-futures = true
canton.sequencers.<sequencer>.parameters.progress-supervisor {
  enabled = true
  warn-action = enable-debug-logging // set to "restart-sequencer" for sequencer node to exit when stuck
  // detection timetout has been bumped in defaults to
  // stuck-detection-timeout = 15 minutes
}
```

* 如果启用新的连接池，节点的健康状态将呈现以下新组件：
  * `sequencer-connection-pool`
  * `internal-sequencer-connection-<alias>`（每个定义的Sequencer连接一个）
  * `sequencer-subscription-pool`
  * `subscription-sequencer-connection-<alias>`（每个活跃订阅者一份）

* 确认指标`daml_sequencer_block_acknowledgments_micros`现在在重新启动时是单调的，并忽略迟到/延迟的成员的确认。

* 调解器指标`daml_mediator_requests`包括由于重用请求UUID而被拒绝的确认请求。此类请求在指标上标有`duplicate_request -> true`。

#### 其他小改进

* 在Sequencer的管理 API 上添加了 RPC 和相应的控制台命令
  为成员生成用于测试的身份验证令牌：`sequencer1.authentication.generate_authentication_token(参与方1)`。
  需要以下配置：`canton.features.enable-testing-commands = yes`。

* 添加了一个控制台命令，用于在Sequencer上使用其令牌注销成员：`sequencer1.authentication.logout(token)`* 添加了对 PostgreSQL 添加表设置的支持。可以在文件中使用可重复迁移（Flyway 功能）
  外部提供给Canton。
  * 使用`canton.<node_type>.<node>.storage.parameters`配置部分下的新配置`repeatable-migrations-paths`。
  * 配置采用必须放置可重复迁移文件的目录列表，路径必须以 `filesystem:` 为前缀，以便 Flyway 识别它们。
  * 示例：`canton.sequencers.sequencer1.storage.parameters.repeatable-migrations-paths = ["filesystem:community/common/src/test/resources/test_table_settings"]`。
  * 这些目​​录中只允许可重复迁移：名称以`R__`开头并以`.sql`结尾的文件。
  * 文件一旦添加就无法删除，但可以修改（与 `V__` 版本化架构迁移不同），并且如果修改，这些文件将在每次 Canton 启动时重新应用。
  * 文件按字典顺序应用。
  * 示例用例：向现有表添加 `autovacuum_*` 设置。
  * 仅在可重复迁移中添加幂等更改。

* 现在，当出现 HTTP/2 INTERNAL gRPC 异常时，会重试 KMS 操作。

* `参与方StoreConfig`中新增参数`safeToPruneCommitmentState`，可选择性指定
  在这种情况下，未发送匹配承诺的对方参与者不能阻止剪枝
  当前参与者。该参数影响所有修剪命令，包括计划修剪。

* 扩展了 ledger api 中用户 ID 中允许的字符集，以包含括号：`()`。
  这也使得这些字符被接受为 JWT 令牌中 `sub` 声明的一部分。

* 在 Postgres 连接上设置积极的 TCP keepalive 设置，以便在数据库连接卡住的情况下实现快速 HA 故障转移。

* 用于设置Sequencer动态聚合查询间隔的新配置值：`batching-config.in-flight-aggregation-query-interval`。

* 修复了`SequencerAggregator`无法及时关机的问题。

* 将充气城堡更新至 1.83，修复了 CVE-2024-29857 和 CVE-2024-34447

### 兼容性

支持以下 Canton 协议版本：

|依赖|版本 |
| ------------------------ | -------- |
|Canton协议版本 | 34 | 34

Canton 已针对其依赖项的以下版本进行了测试：

|依赖|版本 |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Java 运行时 | OpenJDK 64位服务器VM（构建21.0.5+1-nixos，混合模式，共享）|
| Postgres |推荐：PostgreSQL 17.8 (Debian 17.8-1.pgdg13+1) – 还测试了：PostgreSQL 14.21 (Debian 14.21-1.pgdg13+1)、PostgreSQL 15.16 (Debian 15.16-1.pgdg13+1)、PostgreSQL 16.12 (Debian 16.12-1.pgdg13+1) |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
