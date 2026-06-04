---
title: "验证者备份"
slug: "global-synchronizer-production-operations-validator-backups"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/validator-backups.md"
source_title: "Validator Backups"
tags:
  - global-synchronizer
  - production-operations
  - validator-backups
---

# 验证者备份

> 验证者节点的备份流程。

> 验证者节点的备份流程

虽然系统各组件设计为可容忍崩溃故障，但仍可能出现无法立即恢复的故障（例如配置错误或缺陷）。此时需从仍可用的组件备份或转储中恢复单个组件或整个验证者节点。

节点运营方应**同时**做好节点身份备份与 Postgres 实例备份，以覆盖尽可能多的灾难场景。

## 节点身份备份

验证者节点完成上线与入驻后，请备份节点身份。**该信息高度敏感，包含参与方私钥**（除非验证者已配置外部 KMS），应存放在 Secret Manager 等安全位置；同时它对维持身份（例如访问 Canton Coin 持仓）至关重要，必须在集群外备份。

可通过以下端点获取身份：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl "https://wallet.validator.YOUR_HOSTNAME/api/validator/v0/admin/participant/identities" -H "authorization: Bearer <token>"
```

其中 `\<token\>` 为具备访问验证者应用所需声明的 OAuth2 Bearer Token。认证说明见相关文档。

docker-compose 部署请将 `https://wallet.validator.YOUR_HOSTNAME` 换为 `http://wallet.localhost`。无认证部署可用 `python get-token.py administrator` 生成 `curl` 所用令牌（需 [PyJWT](https://pypi.org/project/PyJWT/)）。

## Postgres 实例备份

建议至少每 4 小时备份验证者节点上的全部 Postgres 实例。**备份顺序有严格要求：验证者应用 Postgres 的备份时间点必须严格早于参与方。**请先完成应用库备份，再备份参与方。

集群内自管 Postgres 可用 `pg_dump` 或持久卷快照；云托管 Postgres 可用 `pg_dump` 或云厂商备份工具。

docker-compose 部署可执行：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker exec -i splice-validator-postgres-splice-1 pg_dump -U cnadmin validator > "${backup_dir}"/validator-"$(date -u +"%Y-%m-%dT%H:%M:%S%:z")".dump
active_participant_db=$(docker exec splice-validator-participant-1 bash -c 'echo $CANTON_PARTICIPANT_POSTGRES_DB')
docker exec -i splice-validator-postgres-splice-1 pg_dump -U cnadmin "${active_participant_db}" > "${backup_dir}"/"${active_participant_db}"-"$(date -u +"%Y-%m-%dT%H:%M:%S%:z")".dump
```

### 历史备份

若已启用参与方修剪但仍需长期保留数据（例如审计），应保留历史备份，且相邻备份间隔不超过修剪窗口（即两次历史备份的时间差小于参与方 `retention` 配置）。

逻辑同步器升级期间也应保留备份。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
