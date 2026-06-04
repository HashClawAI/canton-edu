---
title: "运维问题"
slug: "appdev-troubleshooting-guide-operational-issues"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/operational-issues.md"
source_title: "Operational Issues"
tags:
  - appdev
  - troubleshooting-guide
  - operational-issues
---

# 运维问题

> 在 DevNet、TestNet 与 MainNet 上排查流量耗尽、升级问题与 PQS 故障

# 运维问题

本页涵盖应用对接线上网络（DevNet、TestNet 或 MainNet）时出现的问题。本地开发问题见 [开发问题](/zh/docs/canton/appdev-troubleshooting-guide-development-issues)。

## 流量耗尽

Canton Network 上每笔交易都会消耗 traffic，由 Canton Coin（CC）支付。验证者 traffic 用尽后，交易会被拒绝。

### 症状

```
FAILED_PRECONDITION: INSUFFICIENT_TRAFFIC - Not enough traffic remaining
```

或交易超时并返回 `MEDIATOR_SAYS_TX_TIMED_OUT`，且 `unresponsiveParties` 字段指向你的验证者。

### 查看余额

通过 Admin API 查询验证者的 traffic 状态：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost/api/validator/readyz
```

若验证者配置了钱包 UI，也可在钱包界面查看。

### 启用自动充值

配置自动购买 traffic，使验证者在耗尽前补充：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 在 .env 或 validator-values.yaml 中
TARGET_TRAFFIC_THROUGHPUT=20000
MIN_TRAFFIC_TOPUP_INTERVAL=1m
```

### DevNet 水龙头

在 DevNet 上可从水龙头领取免费测试 CC。打开钱包 UI 使用 **Tap**，或直接调用 tap 端点。测试 CC 无实际价值，仅用于开发测试。

<Note>
  在 MainNet 上，CC 具有真实价值。部署生产负载前请监控余额并配置自动充值。
</Note>

## 升级问题

### Daml 包版本不一致

当你部署 Daml 包的新版本并与旧版本并存时，处理你合约的所有验证者都必须上传并 vet 两个版本。若验证者 A 有 v2 而验证者 B 仅有 v1，涉及双方的交易会失败。

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <new-package-id>
```

**修复：** 在提交引用新包的交易前，在所有验证者间同步包部署。使用 SCU（智能合约升级）机制，使 v1 上的现有合约可用 v2 代码行使。

### 混合版本部署

若应用后端期望的 Daml 包版本高于验证者上已部署的版本，命令会在提交时失败。请保持应用版本与已部署 DAR 同步。

上传新 DAR 后，确认已通过 vetting：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 检查已上传的包
curl http://localhost:5002/v2/packages | jq '.package_ids'
```

### Splice 版本不匹配

网络升级（例如从 Splice 0.4.x 到 0.5.x）时，验证者须运行兼容版本。不兼容的验证者会记录类似错误：

```
You don't speak 0.5.x
```

在 [canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/) 查看当前网络版本，并直接升级到所需版本。不要逐级穿越中间版本。

## PQS 问题

Participant Query Store（PQS）将账本数据镜像到 PostgreSQL，以便高效查询。可能出现以下问题。

### 连接失败

若 PQS 无法连接 PostgreSQL 或验证者的 Ledger API，会记录错误并停止流式同步：

```
UNAVAILABLE: io exception - Connection refused to localhost:5001
```

**检查清单：**

* PostgreSQL 在配置的主机/端口上运行并接受连接
* PQS 数据库用户具备所需权限
* PQS 进程可访问 Ledger API（gRPC）端口
* 网络策略或防火墙未阻断连接

### 数据滞后

PQS 与 Ledger API 保持流式连接。连接断开时，PQS 可能落后。将 PQS offset 与 ledger end 对比：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# PQS 最新 offset（查询 PQS 数据库）
psql -h localhost -U pqs -d pqs -c "SELECT max(offset) FROM _pqs_offsets;"

# Ledger end offset
grpcurl -plaintext localhost:5001 \
  com.daml.ledger.api.v2.StateService/GetLedgerEnd
```

若 PQS 明显落后，重启 PQS。PQS 会从上次已提交的 offset 继续。

### Flyway 模式迁移

PQS 使用 Flyway 管理数据库模式。升级 PQS 时 Flyway 会自动运行迁移。若迁移失败：

```
FlywayException: Validate failed: Migration checksum mismatch
```

通常表示数据库被手动修改，或先前迁移未完整应用。恢复步骤：

1. 备份 PQS 数据库
2. 查看已应用的迁移：`SELECT * FROM flyway_schema_history;`
3. 若有迁移标记为失败，修复历史：`flyway repair`
4. 重新启动 PQS

<Warning>
  切勿手动编辑由 Flyway 管理的 PQS 表。模式变更应仅通过 PQS 升级引入。
</Warning>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
