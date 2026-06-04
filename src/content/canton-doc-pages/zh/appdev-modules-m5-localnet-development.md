---
title: "LocalNet 开发"
slug: "appdev-modules-m5-localnet-development"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-localnet-development.md"
source_title: "LocalNet Development"
tags:
  - appdev
  - modules
  - m5-localnet-development
---

# LocalNet 开发

> 将 cn-quickstart 的 LocalNet 作为主要开发与测试环境

LocalNet 是基于 Docker Compose 的本地网络，在开发机上复现 Canton Network 拓扑。提供多个 validator、钱包服务、PQS 与完整 Splice 应用——无需连接共享网络即可构建并测试多方应用。

## LocalNet 提供什么

LocalNet 拓扑包含三个 participant、三个 validator、PostgreSQL 数据库，以及经 NGINX 网关的多个 Web 应用（wallet、SV、scan）。各 validator 在 Splice 生态中扮演不同角色：

* **app-provider** — 运营应用的一方
* **app-user** — 从应用提供方使用应用的用户
* **sv** — 超级验证者，提供 Global Synchronizer 并处理自动做市（AMT）

LocalNet 面向开发与测试，不用于生产。

## 开发生命周期

多数团队与 cn-quickstart 经历五个阶段：

### 学习阶段（1–2 天）

首次接触 cn-quickstart：跑通环境、探索示例应用、理解架构。从 main 拉取保持最新：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git clone https://github.com/digital-asset/cn-quickstart.git
cd cn-quickstart

# 学习期间定期更新
git pull origin main
```

### 实验阶段（1–2 周）

开始改配置、探索 API、改 Daml 代码测试集成模式。配置 upstream 以便选择性合并变更：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git remote add upstream https://github.com/digital-asset/cn-quickstart.git
git checkout -b experiments
git fetch upstream
git merge upstream/main
```

### 开发阶段（2–3 周）

在示例旁构建自有应用。许多开发者在并行目录写代码：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
cn-quickstart/
├── quickstart/    # 原始示例
│   ├── daml/
│   ├── backend/
│   └── frontend/
└── myapp/         # 你的应用
    ├── daml/
    ├── backend/
    └── frontend/
```

更新 `settings.gradle.kts` 包含两套结构。用 `.envrc.private` 做本地环境覆盖。创建扩展 cn-quickstart 的自定义 Docker Compose 文件。

### 分离阶段

当应用复杂度超过 cn-quickstart 示例，可移除对原代码的依赖：删除示例目录、更新构建文件、移除 upstream remote：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git remote remove upstream
rm -rf quickstart/
# 更新 settings.gradle.kts、build.gradle.kts 等
```

### 持续更新

分离后定期查看 cn-quickstart 变更日志，采纳工具改进与新版本。cn-quickstart 变为参考而非依赖。

## 启停 LocalNet

使用 cn-quickstart 时，Makefile 封装 Docker Compose：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd quickstart
make setup    # 首次设置
make build    # 构建 Daml 与后端
make start    # 启动 LocalNet
make stop     # 停止 LocalNet
```

直接控制 Docker Compose 时，设置 `LOCALNET_DIR`（LocalNet 目录路径）与 `IMAGE_TAG`（Splice 版本），然后：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 启动全部节点
docker compose --env-file $LOCALNET_DIR/compose.env                --env-file $LOCALNET_DIR/env/common.env                -f $LOCALNET_DIR/compose.yaml                -f $LOCALNET_DIR/resource-constraints.yaml                --profile sv                --profile app-provider                --profile app-user up -d

# 停止全部节点
docker compose --env-file $LOCALNET_DIR/compose.env                --env-file $LOCALNET_DIR/env/common.env                -f $LOCALNET_DIR/compose.yaml                -f $LOCALNET_DIR/resource-constraints.yaml                --profile sv                --profile app-provider                --profile app-user down -v
```

可用 Docker Compose profile（`--profile app-provider` 等）与环境变量（`APP_PROVIDER_PROFILE=on/off`）禁用特定 validator 以降低资源占用。

## 端口与服务

端口按 validator 角色有规律：

* **SV**：`4${PORT_SUFFIX}`（如 Ledger API `4901`）
* **App Provider**：`3${PORT_SUFFIX}`（如 `3901`）
* **App User**：`2${PORT_SUFFIX}`（如 `2901`）

关键后缀：

* `901` — Participant Ledger API（gRPC）
* `902` — Participant Admin API
* `975` — JSON API（HTTP）
* `903` — Validator Admin API
* `900` — Canton HTTP 健康检查
* `961` — Canton gRPC 健康检查

Web UI：

* App User Wallet：`http://wallet.localhost:2000`
* App Provider Wallet：`http://wallet.localhost:3000`
* SV UI：`http://sv.localhost:4000`
* Scan UI：`http://scan.localhost:4000`

<Note>
  若 `*.localhost` 无法解析，在 `/etc/hosts` 添加：

  ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  127.0.0.1   scan.localhost
  127.0.0.1   wallet.localhost
  127.0.0.1   sv.localhost
  ```
</Note>

## 用 LocalNet 调试

### 捕获与查看日志

最快方式是一次捕获全部日志：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make capture-logs
```

用 [lnav](https://lnav.org/) 分析日志文件——支持多格式，可过滤、搜索并关联跨服务事件。

### 查看实时日志

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 全部容器
docker compose -f $LOCALNET_DIR/compose.yaml logs -f

# 指定服务
docker compose -f $LOCALNET_DIR/compose.yaml logs -f app-provider-participant

# 过滤错误
docker compose -f $LOCALNET_DIR/compose.yaml logs -f 2>&1 | grep -i error
```

### 访问 Canton Console

Canton Console 可直接检查并修改 participant、sequencer、mediator：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env                --env-file $LOCALNET_DIR/env/common.env                -f $LOCALNET_DIR/compose.yaml                -f $LOCALNET_DIR/resource-constraints.yaml                run --rm console
```

cn-quickstart：`make canton-console`。

### 常见问题

* **容器无法启动** — 检查内存。三 validator 全开占用较大，可禁用未用 profile 减负。
* **Scan UI 无 round** — 启动后数分钟才出现数据，初始引导期间属正常。
* **数据库连接错误** — 单一 PostgreSQL 服务所有组件，确认其先于其他服务成功启动。

## 下一步

* [Testing Strategies](/appdev/modules/m5-testing-strategies) — Canton 应用测试金字塔
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — 从 LocalNet 到 DevNet、TestNet、MainNet

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
