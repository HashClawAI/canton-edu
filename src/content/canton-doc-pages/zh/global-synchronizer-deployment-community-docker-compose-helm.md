---
title: "社区 Docker Compose 部署"
slug: "global-synchronizer-deployment-community-docker-compose-helm"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/community-docker-compose-helm.md"
source_title: "Alternative Docker Compose Deployment (Community)"
tags:
  - global-synchronizer
  - deployment
  - community-docker-compose-helm
---

# 社区 Docker Compose 部署

> 社区 Docker Compose 验证者部署方案（非官方）。

> 社区贡献的基于Helm图表的Docker Compose部署

<Warning>
  This section features solutions shared by community members. While they haven’t been formally tested by the Splice maintainers, users are encouraged to verify the information independently. Contributions to enhance accuracy and completeness are always welcome.
</Warning>

本指南介绍了社区贡献的 Docker Compose 解决方案，用于部署 Canton 验证器节点和支持基础设施，遵循 Mario Delgado 团队用于加入区块链的 `x-docker` 标准。请注意，虽然它是在 DevNet 上的计划升级期间进行测试的，但这需要使用迁移 ID 更新 `.env` 文件，重命名数据库（计划更改为使用`participant_${MIGRATION_ID}` 和 `validator_${MIGRATION_ID}` 等标准化名称），并将 `validator-migration.yaml` 作为迁移设置的一部分。欲了解更多信息，请联系该贡献的作者。该解决方案强调可扩展性、操作灵活性以及与更广泛的基础设施的集成。官方支持的docker-compose部署请参考基于Docker Compose的Validator节点部署。

感谢 Mario Delgado 在社区讨论中分享此解决方案。有关更多详细信息和未来更新，请参阅 [CryptoManufaktur-io/canton-docker](https://github.com/CryptoManufaktur-io/canton-docker) 存储库。

## 解决方案的主要特点

* 为 Canton 定制 Docker Compose 设置，符合 `x-docker` 标准。
* 通过`validator-migration.yaml` 支持验证器迁移以进行升级。
* 用于设置和维护的自动安装和更新脚本。
* 支持自定义覆盖（`custom.yml`）和环境变量，无需修改基础文件即可实现高级配置。
* 通过 `central-proxy-docker` 和 `:ext-network.yml` 集成 Traefik（代理）和 Prometheus（监控）指南。
* Kubernetes 环境的实验 Helm 图表（截至 2025 年 6 月正在进行中）。
* 灾难恢复功能（截至 2025 年 6 月正在进行中）。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
