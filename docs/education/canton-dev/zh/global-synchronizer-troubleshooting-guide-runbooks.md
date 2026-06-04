---
title: "运维手册"
slug: "global-synchronizer-troubleshooting-guide-runbooks"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/runbooks.md"
source_title: "Runbooks"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - runbooks
---

# 运维手册

> 常见验证者事件的检测、处置与验证运维手册。

> 常见验证者事件的运维手册以及分步程序

运维手册提供对已知事件类型的结构化响应。每个运维手册都遵循相同的阶段：检测、评估、行动、验证和记录。

## 事件响应模板

对于没有专用运维手册的任何事件，请使用此模板。

1. **检测** -- 识别症状。问题是如何发现的？ （警报、用户报告、例行检查。）
2. **评估**——确定范围和严重性。验证者是否离线？交易失败？数据有风险吗？
3. **行动** -- 执行适当的修复。请遵循下面的相关运维手册或[故障排除方法](/zh/docs/canton/global-synchronizer-troubleshooting-guide-troubleshooting-methodology)。
4. **验证** -- 确认修复。检查运行状况端点、提交测试交易、检查日志是否重复出现错误。
5. **文档** -- 记录发生的情况、原因、所做的操作以及任何后续操作。

***

## 运维手册：验证者离线

**检测：**健康端点返回非200，监控警报触发，或验证者从公共网络状态中消失。

**评估：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check pod/container status
kubectl get pods -n validator
# or
docker ps --filter "name=validator"
```

**行动：**

* 如果 pod 位于`CrashLoopBackOff`，请检查日志以查找根本原因：
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  kubectl logs -n validator deployment/validator-app --previous
  ```
* 如果pod没有被调度，请检查资源配额问题或节点可用性：
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  kubectl describe pod -n validator -l app=validator-app
  ```
* 如果容器以代码 137 退出，则它被 OOM 杀死。增加内存限制。
* 如果容器退出时代码为 1，请检查日志中是否存在配置或启动错误。

**验证：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost/api/validator/readyz
```

端点应返回 HTTP 200。

***

## 运行手册：流量耗尽

**检测：** 交易失败并显示 `PARTICIPANT_TRAFFIC_BELOW_LIMIT` 或 `MEDIATOR_SAYS_TX_TIMED_OUT`，其中您的验证者位于 `unresponsiveParties` 列表中。

**评估：**

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

若`availableTraffic`为0或流量已满，请购买流量或开启自动充值，交易才能正常进行。

**行动：**

1、立即购买流量：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
     -H "Authorization: Bearer $TOKEN"
   ```
2. 启用自动充值以防止再次发生：
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   # In validator-values.yaml
   topup:
     enabled: true
     targetThroughput: 100000
     minTopupInterval: 10m
   ```
3. 检查验证者是否有足够的 Canton Coin 余额用于购买流量。

**验证：** 提交测试交易并确认交易成功。

***

## 运维手册：数据库磁盘已满

**检测：** 包含 `No space left on device` 的 PostgreSQL 错误，或来自监控的磁盘使用警报。

**评估：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check disk usage
kubectl exec -n validator statefulset/postgres -- df -h /var/lib/postgresql/data
```

**行动：**1. **立即缓解** - 如果数据库完全满，您可能需要扩展 PVC 或可用空间，然后 PostgreSQL 才能再次接受写入。
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   # Resize PVC (if your StorageClass supports it)
   kubectl edit pvc postgres-data -n validator
   # Change spec.resources.requests.storage to a larger value
   ```
2. **启用或修复修剪：**
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   participantPruningSchedule:
     cron: "0 */10 * * * ?"
     maxDuration: 60m
     retention: 90d
   ```
3. **在 PostgreSQL 上运行手动 VACUUM** 以在修剪删除行后回收空间：
   ```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   VACUUM FULL;
   ```
   注意：`VACUUM FULL` 锁定表，并且需要与被清理的表大致相同数量的可用空间。在维护窗口期间安排。

**验证：** 确认磁盘使用率已下降并且验证者正在正常处理交易。

***

## 运维手册：升级回滚失败

**检测：** 在`helm upgrade`之后，验证者处于崩溃循环中或生成`UnrecoverableError`消息。

**评估：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check the current release state
helm history validator -n validator

# Check pod logs for the specific error
kubectl logs -n validator deployment/validator-app --tail=200
```

**行动：**

1. **不要**反复重启——这会加剧国家腐败。
2. 回滚到之前工作的 Helm 版本：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   helm rollback validator <previous-revision> -n validator
   ```
3. 如果回滚涉及同步器迁移（类型3升级），您可能还需要将数据库名称切换回来：
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   persistence:
     databaseName: participant_3  # Previous migration ID
   ```
4. 验证回滚是否恢复了之前的容器镜像：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   kubectl -n validator get deploy validator-app \
     -o "jsonpath={.spec.template.spec.containers[0].image}"
   ```
5. 稳定后，在重新尝试之前调查升级失败。常见原因：缺少迁移配置、数据库名称错误或值文件不兼容。

**验证：**健康端点返回200，验证者正在处理交易。

***

## 运维手册：CometBFT 共识停滞

**检测：** 这适用于运行 CometBFT 节点的超级验证者 (SV) 运营商。区块高度停止增长，或者 CometBFT 状态端点显示没有新区块。

**评估：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check CometBFT status
curl -s http://localhost:26657/status | jq '.result.sync_info'
```

如果`latest_block_height`在几分钟内没有变化并且`catching_up`是`false`，则共识已陷入停滞。

**行动：**

1. 检查连接对等点的数量：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -s http://localhost:26657/net_info | jq '.result.n_peers'
   ```
   如果节点数量低于共识阈值（验证者的 2/3），则无法生成区块。

2. 检查验证者签名问题：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -s http://localhost:26657/dump_consensus_state | jq '.result.round_state.votes'
   ```

3. 如果您自己的CometBFT节点未签名，请重新启动它：
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   kubectl rollout restart deployment/cometbft -n validator
   ```

4. 如果摊位是全网范围的（多个SV节点未签名），则通过`#验证者-operations` Slack通道与其他SV运营商协调。

**验证：** 区块高度正在推进，区块之间的间隔已恢复正常（通常为几秒）。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
