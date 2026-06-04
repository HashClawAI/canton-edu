---
title: "部署选项"
slug: "global-synchronizer-deployment-deployment-options"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/deployment-options.md"
source_title: "Deployment Options"
tags:
  - global-synchronizer
  - deployment
  - deployment-options
---

# 部署选项

> Canton Network 验证者部署：Docker Compose 与 Kubernetes 选型指南。

> 选择 Docker Compose 和 Kubernetes 来部署 Canton Network 验证器

Canton Network 验证器可以使用 Docker Compose 或带有 Helm 图表的 Kubernetes 进行部署。您的选择取决于目标环境、运营成熟度和规模要求。

## Docker 组合

Docker Compose 是运行验证器的最简单路径。它将所有组件打包到由 shell 脚本管理的单主机部署中。

**何时使用 Docker Compose：**

* LocalNet和DevNet开发
* 概念验证和集成测试
* 小规模部署，无高可用性要求
* 没有 Kubernetes 专业知识的团队

**你得到什么：**

* 单一`start.sh` / `stop.sh` 工作流程
* Splice 节点包中预配置的组合文件
* 用于 UI 路由的本地 Traefik 反向代理
* 用于流程管理的 Systemd 集成

**限制：**

* 在单个主机上运行 - 没有内置的高可用性
* 手动扩展和故障转移
* 不建议用于生产主网部署
* 数据库在容器内运行，除非您配置外部 PostgreSQL 实例

## 带有 Helm 的 Kubernetes

Kubernetes 是测试网和主网推荐的部署方法。 Helm 图表为所有验证器组件提供参数化配置。

**何时使用 Kubernetes：**

* 测试网和主网生产部署
* 需要高可用性和自动故障转移的环境
* 拥有现有 Kubernetes 基础设施的组织
* 需要托管数据库服务（RDS、Cloud SQL、Azure 数据库）的部署

**你得到什么：**

* 验证者、参与者、钱包 UI 和 CNS UI 的 Helm 图表
* 通过`helm upgrade`管理滚动升级
* 与云原生服务集成（托管数据库、KMS、监控）
* 入口控制器支持 TLS 终止和路由
* 跨环境可扩展和可复制

**要求：**

* Kubernetes 1.27 或更高版本
* Helm 3.11.1 或更高版本
* 入口控制器（NGINX、Traefik 或云原生）
* 外部 PostgreSQL（托管或自托管，不在生产容器内）

## 云提供商注意事项

所有三大云提供商都支持验证器部署。主要区别在于托管服务名称。

**AWS：**

* 用于 Kubernetes 的 EKS、用于 PostgreSQL 的 RDS 或 Aurora
* 静态出口 IP 的 NAT 网关
* 用于密钥管理的 AWS KMS（社区版）
* 用于存储的 gp3 EBS 卷

**谷歌云：**

* 适用于 Kubernetes 的 GKE、适用于 PostgreSQL 的 Cloud SQL
* 静态出口IP的云NAT
* 用于密钥管理的云KMS（社区版）
* SSD永久磁盘用于存储

**天蓝色：**

* 用于 Kubernetes 的 AKS、用于 PostgreSQL 的 Azure 数据库
* 静态出口 IP 的 NAT 网关
* 用于存储的高级 SSD

无论使用哪个云提供商，都请将托管数据库放置在与 Kubernetes 集群相同的区域和可用区中。数据库延迟直接影响验证器性能。

## 在选项之间进行选择

对于大多数团队来说，决定取决于环境和运营能力：

* **在 DevNet 上开始或测试** — 使用 Docker Compose。它可以让您在几分钟内以最少的基础设施运行。
* **转移到测试网** - 任一选项都有效。如果不需要高可用性，Docker Compose 是可以接受的。如果您想要在生产中使用相同的部署方法，那么 Kubernetes 是首选。
* **主网生产** — 使用 Kubernetes。对于必须保持高可用性的生产验证器来说，操作工具（滚动升级、运行状况检查、自动扩展）是必需的。

<注意>
  您可以从 DevNet 上的 Docker Compose 开始，然后迁移到 Kubernetes 以实现 TestNet/MainNet。验证器状态位于 PostgreSQL 中，只要您保留数据库，登录身份就会在部署中持续存在。
</注>

## 超级验证器部署

超级验证者必须使用 Kubernetes。其他组件（CometBFT 节点、排序器、中介器、SV 应用程序、扫描服务）需要编排，而 Docker Compose 在生产规模上不支持。请参阅 [Kubernetes 部署](/zh/docs/canton/global-synchronizer-deployment-kubernetes-deployment) 指南。

## 后续步骤

<卡组列={2}>
  <Card title="先决条件" icon="list-check" href="https://docs.canton.network/global-synchronizer/deployment/precessions">
    您选择的部署方法的系统要求。
  </卡><Card title="Docker Compose 验证器部署" icon="docker" href="/zh/docs/canton/global-synchronizer-deployment-validator-docker-compose">
    分步 Docker Compose 验证器部署。
  </卡>

  <Card title="Kubernetes 验证器部署" icon="dharmachakra" href="/zh/docs/canton/global-synchronizer-deployment-validator-kubernetes">
    使用 Helm 图表逐步部署 Kubernetes 验证器。
  </卡>
</卡组>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
