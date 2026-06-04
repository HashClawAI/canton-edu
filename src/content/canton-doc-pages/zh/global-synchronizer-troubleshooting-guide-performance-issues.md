---
title: "性能问题"
slug: "global-synchronizer-troubleshooting-guide-performance-issues"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/performance-issues.md"
source_title: "Performance Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - performance-issues
---

# 性能问题

> 慢交易、资源耗尽与数据库瓶颈的性能排查。

> 解决交易缓慢、资源耗尽和数据库瓶颈

性能逐渐下降，因此通常不会被注意到，直到事务开始超时或验证者在事件处理上落后。本页涵盖最常见的性能问题及其解决方案。

## 交易缓慢

如果交易延迟增加，请按顺序检查这些区域。

### 流量平衡

低流量平衡会导致Sequencer限制验证者的消息。检查一下：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res1: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

如果`availableTraffic`接近于零（或流量限制已用完），请立即充值并启用自动充值以防止再次发生。

### 数据库性能

查询数据库中活动的慢查询：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT pid, now() - query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY duration DESC
LIMIT 10;
```

如果您看到查询运行超过几秒钟，则数据库可能是瓶颈。常见原因：

* **表变得太大。** 启用修剪（见下文）。
* **缺少索引。** 版本或协议升级后，在参与者数据库上运行`ANALYZE`以更新查询规划器统计信息。
* **IOPS 不足。** 如果在云基础设施上运行，请升级您的存储类别（例如，在 AWS 上从 gp2 切换到 gp3 并增加预配置的 IOPS）。

### JVM 堆压力

如果验证者进程在垃圾收集上花费大量时间，则交易处理速度会减慢。检查日志中的 GC 压力：

```
GC overhead limit exceeded
```

或频繁的`Full GC`条目。增加堆分配：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# In Docker Compose, set JAVA_OPTS
JAVA_OPTS="-Xmx4g -Xms4g"

# In Kubernetes, set in the values file
jvmOptions: "-Xmx4g -Xms4g"
```

通过 JMX 或使用 `-Xlog:gc*` 启用 GC 日志记录来监视堆使用情况。

## 资源耗尽

### 磁盘空间

随着新交易的处理，参与者数据库不断增长。如果不进行修剪，它最终会耗尽磁盘空间。

**症状：**

* PostgreSQL 错误：`could not extend file ... No space left on device`
* 由于临时存储限制，Kubernetes 中的 Pod 被驱逐

**检查磁盘使用情况：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# On the database host
df -h /var/lib/postgresql/data

# In Kubernetes
kubectl exec -n validator statefulset/postgres -- df -h /var/lib/postgresql/data
```

**启用修剪**以回收空间：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

启用修剪后，第一次运行可能比后续运行花费更长的时间。为初始修剪（60 分钟或更长时间）充分设置 `maxDuration`。

### 内存

如果验证者 Pod 被 OOM Killer 杀死（退出代码 137），请增加内存限制：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# In Kubernetes values
resources:
  limits:
    memory: "8Gi"
  requests:
    memory: "4Gi"
```

对于 Docker Compose，将 Docker 的总内存分配增加到至少 8 GB。

###CPU

高 CPU 使用率通常是由失控的自动化（在紧密循环中重试的脚本）或繁重的 ACS（活动合约集）处理引起的。

**查明原因：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check which threads are consuming CPU
jcmd <pid> Thread.print | grep -A2 "java.lang.Thread.State: RUNNABLE"
```

如果您的应用程序包含重试失败命令的自动化，请确认它使用指数退避而不是固定间隔重试循环。

## 数据库查询优化

### 缺失索引

升级或迁移后，可能尚未为新列创建索引。检查大表上的顺序扫描：```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT relname, seq_scan, idx_scan
FROM pg_stat_user_tables
WHERE seq_scan > 1000
ORDER BY seq_scan DESC;
```

具有高 `seq_scan` 计数和低 `idx_scan` 计数的表是缺失索引的候选者。有关任何所需的索引添加，请参阅 Canton 发行说明。

### 连接池耗尽

如果您看到类似以下错误：

```
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

数据库连接池得到充分利用。原因包括：

* 长时间运行的查询保持连接
* 对于配置的池大小来说，并发操作过多
* 达到数据库端连接限制

增加 Canton 配置中的池大小：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.storage.parameters {
  max-connections = 32
}
```

另请检查 PostgreSQL `max_connections` 设置，以确认它适应部署中的所有连接池。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
