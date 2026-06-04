---
title: "性能优化"
slug: "global-synchronizer-production-operations-performance-optimization"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/performance-optimization.md"
source_title: "Performance Optimization"
tags:
  - global-synchronizer
  - production-operations
  - performance-optimization
---

# 性能优化

> 验证者与 SV 节点的数据库、JVM 与 Canton 性能调优。

> 调整数据库、JVM 和 Canton 配置以提高验证者和 SV 节点性能

Canton 节点性能取决于数据库吞吐量、JVM 配置、Sequencer容量和修剪策略。本页面涵盖了验证者和 SV 节点运营商的关键调优领域。

## 数据库优化

PostgreSQL 是大多数 Canton 部署中的主要性能瓶颈。

### 连接池

Canton 使用 HikariCP 进行数据库连接池。默认池大小适用于轻量工作负载，但高吞吐量部署可从调整中受益：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.storage {
  type = "memory"

  config {
    # Maximum number of connections in the pool
    maxConnections = 30

```

根据您的 PostgreSQL `max_connections` 设置和共享数据库服务器的 Canton 进程数来设置 `maxConnections`。一个好的起点是`max_connections / number_of_canton_processes`，为监控和维护连接留出空间。

### PostgreSQL 调优

这些 PostgreSQL 参数对 Canton 工作负载影响最大：

* **`shared_buffers`** — 设置为可用 RAM 的 25%。对于 64 GB 数据库服务器，请使用 `16GB`。
* **`effective_cache_size`** — 设置为可用 RAM 的 50-75%。这告诉查询规划器有多少内存可用于缓存，包括操作系统缓存。
* **`work_mem`** — 控制排序操作和哈希表的内存。从 `64MB` 开始，如果您在查询计划中看到基于磁盘的排序，则增加。
* **`maintenance_work_mem`** — 用于 VACUUM 和索引操作的内存。对于大型数据库，设置为 `1GB` 或更高。
* **`max_wal_size`** — 控制检查点频率。增加到`4GB`或`8GB`以减少重写入负载下的检查点压力。
* **`random_page_cost`** — 如果您的数据库在 SSD 存储上运行，则设置为 `1.1`（默认为 `4.0`，针对旋转磁盘进行调整）。

`postgresql.conf` 添加示例：

```ini theme={"theme":{"light":"github-light","dark":"github-dark"}}
shared_buffers = 16GB
effective_cache_size = 48GB
work_mem = 64MB
maintenance_work_mem = 1GB
max_wal_size = 8GB
random_page_cost = 1.1
checkpoint_completion_target = 0.9
wal_buffers = 64MB
```

### 索引

Canton 在架构迁移期间创建必要的索引。请勿修改或删除 Canton 管理的索引。如果您在 PostgreSQL 日志中观察到缓慢的查询，请检查 autovacuum 是否正常运行 - 膨胀的表和过时的统计信息是查询计划降级的最常见原因。

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Check for tables that need vacuuming
SELECT schemaname, relname, n_dead_tup, last_autovacuum
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
```

## JVM 调优

Canton 在 JVM 上运行。默认 JVM 设置是保守的，生产部署受益于显式配置。

### 堆大小

根据节点类型和预期工作负载设置堆大小：* **验证者（参与者）** — 从 `-Xmx4g` 开始。对于高吞吐量工作负载或托管多方时，增加至 8-12 GB。
* **音序器** — 从 `-Xmx4g` 开始。Sequencer的内存需要根据消息吞吐量进行扩展。
* **调解员** — 从 `-Xmx2g` 开始。调解者比定序者或参与者具有更小的内存要求。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Helm values for JVM settings
participant:
  jvmOptions: "-Xms4g -Xmx4g -XX:+UseG1GC -XX:MaxGCPauseMillis=200"
```

### 垃圾收集

G1GC 是 Canton 推荐的垃圾收集器。它提供了良好的吞吐量和可预测的暂停时间。按键设置：

* **`-XX:+UseG1GC`** — 启用 G1 垃圾收集器
* **`-XX:MaxGCPauseMillis=200`** — 目标最大 GC 暂停时间。较低的值可减少延迟峰值，但可能会降低吞吐量。
* **`-XX:G1HeapRegionSize=16m`** — 对于 8 GB 以上的堆，增加区域大小可提高 G1 效率

使用 `-Xlog:gc*:file=/var/log/canton/gc.log:time,uptime,level,tags` 监视 GC 活动，并观察频繁的完整 GC 暂停，这表明堆太小。

## Sequencer吞吐量

Sequencer的吞吐量由其排序后端和数据库性能决定。对于集中式 (PostgreSQL) 订购后端（目前处于 Alpha 阶段）：

* 单一数据库是所有消息排序的序列化点
* 数据库服务器的垂直扩展（更快的CPU，更多的IOPS）直接提高吞吐量
* Sequencer进程与其数据库之间的网络延迟会影响每条消息

对于去中心化（BFT）排序后端，吞吐量取决于共识轮时间和Sequencer节点的数量。 BFT 共识增加了每条消息的延迟，但提供了容错能力。

## 交通管理

在全局同步器上，每笔交易都会消耗流量，流量是用Canton币支付的。降低流量成本：

* **批量操作** — 一起提交多个相关命令，而不是单独提交。 Canton 更高效地处理批处理命令。
* **合约设计** - 较小的合约和每笔交易创建/存档的合约较少，可减少流量消耗。
* **同步器分配** — 将高频双边工作流程移至不收取流量费用的专用同步器。

通过验证者的钱包或 Splice 管理 API 监控您的流量消耗，以避免在高峰时段耗尽流量平衡。

## 修剪

Canton 存储完整的交易历史记录和 ACS（活动合约集）快照。随着时间的推移，这些数据会不断积累，并会减慢查询速度。修剪会删除不再需要的历史数据。

### 对性能的影响

* 修剪可减少数据库大小，从而提高备份时间和查询性能
* 修剪过程本身是资源密集型的 - 将其安排在低流量时段
* 修剪后，在受影响的表上运行`VACUUM ANALYZE`以回收磁盘空间并更新查询统计信息

### 配置

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
    connectionTimeout = 30000
  }
}

```<Warning>
  修剪后的数据无法恢复。在启用积极修剪之前，请确保您有备份。一些监管环境要求在规定的时间内保留交易历史记录。
</Warning>

## 批量大小

Canton 在内部批量处理命令。默认批量大小平衡延迟和吞吐量。对于高吞吐量工作负载，您可以增加批量大小：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # Prune data older than this duration
  max-修剪-batch-size = 1000
}

canton.participants.participant.parameters {
```

较大的批次可以提高吞吐量，但代价是每个命令的延迟稍高。监视Sequencer和命令完成延迟指标以找到适当的平衡。

## 监控性能

跟踪这些指标以识别瓶颈：`canton_participant_command_completion_latency`（端到端命令时间）、`canton_sequencer_send_latency`（Sequencer吞吐量）、`canton_participant_db_query_latency`（数据库运行状况）、`hikaricp_connections_active`（连接池饱和度）和 JVM 堆/GC 指标。设置仪表板并在值超出基线时发出警报 - 性能下降通常是渐进的，早期检测可以防止中断。

记录如何在具有受支持存储的企业节点上启用复制（默认情况下处于打开状态）。记录运行状况检查配置和故障转移时间。记录用于处理多个副本的管理命令（查找活动副本），记录用于检查活动性的命令。对于参与者：gRPC Ledger API 前面的负载均衡器配置用于路由到活动实例。链接到有关 HA 架构的说明。

## 高可用性使用

本节将介绍一些已经提到的组件并提供有用的 Canton 命令。

### 参与者

参与者节点的高可用性是通过运行多个有权访问共享数据库的参与者节点副本来实现的。

参与者节点副本在 Canton 配置文件中配置为单独的参与者，每个参与者节点副本需要进行两处更改：

* 使用相同的存储配置来保证对共享数据库的访问。 HA 仅支持基于 PostgreSQL 和 Oracle 的存储。对于 Oracle 来说，参与者副本使用相同的用户名访问共享数据库至关重要。
* 为每个参与节点副本设置`replication.enabled = true`。

<Note>
  从 Canton 2.4.0 开始，使用支持的存储时默认启用参与者复制。
</Note>

#### 手动触发故障转移

当主动副本发生故障时，会自动完成从主动副本到被动副本的故障转移，但也可以使用以下命令启动正常故障转移：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
activeParticipantReplica.replication.set_passive()
```

如果至少有另一个被动副本接管当前主动副本，则该命令成功，否则主动副本保持主动状态。

#### 负载均衡器配置许多复制的参与者可以放置在适当复杂的负载均衡器后面，该负载均衡器将通过运行状况检查确定哪个参与者实例处于活动状态，并适当地向该实例发出直接分类帐和管理 API 请求。从管理逻辑参与者的 ledger-api 应用程序或 canton 控制台的角度来看，这使得参与者复制和故障转移变得透明，因为它们将简单地指向负载均衡器。

应将参与者配置为使用以下监控配置在我们的健康 HTTP 服务器上公开“IsActive”健康状态：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  monitoring {
    health {
      server {
        address = 0.0.0.0
        port = 8000
      }

      check.type = is-active
    }
  }
}
```

运行后，如果参与者当前是活动副本，则该服务器会向`/health`报告 http/1 GET 请求上的 HTTP 200 状态代码。否则，将返回错误。

要使用负载均衡器，它必须支持 http/1 运行状况检查，以便在单独的 http/2 (GRPC) 服务器上路由请求。这可以通过 [HAProxy](http://www.haproxy.org/) 使用以下示例配置来实现：

全球
记录标准输出格式原始 local0

默认值
记录全局
模式 http
选项 httplog

# 启用，以便在连接后立即记录长时间运行的连接

选项日志

# 将 admin-api 和 ledger-api 作为单独的服务器公开

前端管理 API
绑定：15001 原型 h2
默认\_backend admin-api

后端管理API

# 启用 HTTP 健康检查

选项 httpchk

# 需要创建一个单独的连接来查询负载均衡器。

# 这一点尤其重要，因为健康 HTTP 服务器不支持 h2

# 否则将是默认值。

http 检查连接

# 设置健康检查uri

http-check 发送 meth GET uri /health

# 列出所有参与者后端

服务器参与者1参与者1.lan:15001 proto h2检查端口8080
服务器participant2participant2.lan:15001 proto h2检查端口8080
服务器participant3participant3.lan:15001 proto h2检查端口8080

# 对 ledger-api 重复与上面类似的配置

前端账本 API
绑定：15000 原型 h2
默认\_backend ledger-api

后端账本API
选项 httpchk
http 检查连接
http-check 发送 meth GET uri /health

服务器参与者1参与者1.lan:15000 proto h2检查端口8080
服务器participant2participant2.lan:15000 proto h2检查端口8080
服务器participant3participant3.lan:15000 proto h2检查端口8080

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/optimize/storage.rst" hash="b2f96e3b" */}

添加查询成本日志记录。

## 优化存储

### 常规设置

#### 最大连接设置

可以使用以下附加设置进一步调整存储配置：

```
canton.participants.<service-name>.storage.parameters.max-connections = X
```这允许您设置 Canton 节点使用的最大数据库连接数。如果该值为 None 或非正数，则该值为处理器的数量。如果连接数已通过灵活选项（即 storage.config.numThreads）设置，则该设置无效。

如果您不确定如何调整连接池的大小，[本文](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing)可能是一个很好的起点。

通常，连接数最多应为数据库计算机上 CPU 数的两倍。

并行索引器连接的数量可以通过配置

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.<participant-name>.parameters.ledger-api-server-parameters.indexer.ingestion-parallelism = Y
```

独占Sequencer写入器组件使用的连接数`Z`是最终可以控制的参数。

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.sequencers.<sequencer-name>.sequencer.high-availability.exclusive-storage.max-connections = Z
```

Canton 参与者节点将与数据库建立最多 `X + Y + 2` 永久连接，而同步器最多将使用 `X` 永久连接，但具有 HA 设置的Sequencer将分配最多 `2X` 连接。在启动期间，节点将在数据库初始化期间使用一组额外的最多`X`临时连接。

数字`X`代表永久连接的上限，并根据实现的不同在内部划分用于不同的目的。因此，例如，写入连接池的实际大小可能会更小。一些分配的连接将由“读”池占用，一些将由“写”池占用，并且一个附加连接将保留给负责管理锁定机制的专用“主”连接。

下表总结了不同 Canton 节点中连接池的详细划分。 `R` 表示*读取* 池，`W` 表示*写入* 池，`A` 表示*Ledger API* 池，`I` 表示*索引器* 池，`RW` 表示组合的*读/写* 池，`M` 表示*主* 池。|节点类型|具有复制功能的企业版|企业版|社区版 |
| -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------ |
|参与者 | A = X / 2<br />R = X / 4<br />W = X / 4 - 1<br />M = 1<br />I = Y | A = X / 2<br />R = X / 4<br />W = X / 4 - 1<br />M = 1<br />I = Y | A = X / 2<br />RW = X / 2<br />I = Y |
|调解员| R = X / 2<br />W = X / 2 - 1<br />M = 1 |不适用 |不适用 |
|音序器| RW = X |不适用 |不适用 |
|音序器编写器 | R = X / 2<br />W = X / 2 - 1<br />M = 1 |不适用 |不适用 |
| Sequencer独家撰稿人| R = Z / 2<br />W = Z / 2 |不适用 |不适用 |
|同步器|不适用 | RW = X | RW = X |

除法的结果总是向下舍入，除非它们产生零。在这种情况下，确定最小池大小为 1。

从该公式获得的值可以使用 *Ledger API* `A`、*Read* `R`、*Write* `W` 池的显式配置设置来覆盖。

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-reads = R-overwrite
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-writes = W-overwrite
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-ledger-api = A-overwrite
```

其他坎顿节点类型也存在类似的参数：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.sequencers.sequencer.storage.parameters.connection-allocation...
    canton.mediators.mediator.storage.parameters.connection-allocation...
```

当节点操作组合的*读/写*连接池时，`R`和`W`覆盖的数量相加，以确定总池大小。

有效连接池大小由 Canton 节点在启动时报告。

信息 c.d.c.r.DbStorageMulti\$:participant=participant\_b - 创建存储，读取次数：5，写入次数：4

#### 队列大小Canton 可能会安排比数据库能够处理的更多的数据库查询。结果，这些查询将被放入数据库队列中。默认情况下，数据库队列的大小为 1000 个查询。达到排队限制将导致`DB_STORAGE_DEGRADATION`警告。此警告的影响是队列将溢出到异步执行上下文并缓慢降低处理性能，这将导致创建的数据库查询减少。然而，对于高性能设置，此类峰值可能会更频繁地发生。因此，为了避免降级警告出现得太频繁，可以使用以下方式配置队列大小：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.storage.config.queueSize = 10000

```

### Postgres

#### Postgres 配置

对于 Postgres，[PGTune 在线工具](https://pgtune.leopard.in.ua/) 是寻找合理参数的良好起点（使用在线事务处理系统），但您需要增加 `shared_buffers`、`checkpoint_timeout` 和 `max_wal_size` 的设置，如下所述。

除了初始配置之外，请注意 Canton 使用的大多数索引都是“基于哈希的”。因此，对这些索引的读写访问是均匀分布的。然而，Postgres 以 8kb 的页为单位读取和写入索引，而简单的索引可能只需要几次写入。因此，能够将索引保留在内存中并且只时不时地将更新写入磁盘是非常重要的；否则，32 字节的简单更改需要 8kb I/O 操作。

建议将 `shared_buffers` 设置配置为保留 60-70% 的主机内存，而不是默认建议的 25%，因为 Postgres 缓存似乎比基于主机的文件访问缓存更有效。

还要增加以下变量超出其默认值：增加`checkpoint_timeout`，以便刷新到磁盘包括多次写入，而不仅仅是每页一次，随着时间的推移累积，以及更高的`max_wal_size`，以确保系统在到达`checkpoint_timeout`之前不会过早刷新。在负载测试期间监视您的系统并根据您的用例调整参数。更改检查点参数的缺点是崩溃恢复需要更长的时间。

#### 尺寸和性能

请注意，您的 Postgres 数据库设置需要进行适当的调整才能达到所需的性能。广州的数据库非常密集。本节应该为您的调整工作提供一个起点。您可能需要查阅故障排除部分，了解如何分析数据库是否是限制因素。

本指南可以为您提供调整的起点。最终，每个用例都是不同的，并且无法预测确切的资源需求，但必须进行测量。

首先，确保您使用的数据库的大小适合您的用例。核心数量取决于您的吞吐量要求。经验法则是：

* 每 1 个参与者核心 1 个 db 核心。
* 1 个参与者核心每秒处理 30-100 个账本事件（取决于命令的复杂性）。内存要求取决于您的数据保留期限和要存储的数据大小。理想情况下，您可以监视数据库索引缓存命中/未命中率。如果您的实例需要继续从磁盘加载索引，性能就会受到影响。从 128GB 开始，运行长时间运行的规模和性能测试，并[监控缓存命中/未命中率](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STATIO-ALL-INDEXES-VIEW)可能是有意义的。

大多数 Canton 索引都是基于合约 ID 的，这意味着索引查找是随机分布的。为此，具有高吞吐量的固态驱动器比旋转磁盘的性能要好得多。

#### 共享环境的可预测性

Canton节点的吞吐量和延迟取决于数据库的性能。共享硬件或软件可以节省成本，更好地利用可用资源，但也有一些缺点：如果数据库运行在云等共享环境中，其他应用程序使用相同的数据库或运行在相同的硬件上，则由于共享资源的争用，Canton节点的性能会有所不同。这是共享环境的自然效应，无法完全避免。由于缺乏对其他应用程序和主机系统的可见性，作为共享环境的用户可能很难进行诊断。

如果您在共享环境中操作，则应该监视数据库的性能并预计延迟和吞吐量会有更大的变化。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
