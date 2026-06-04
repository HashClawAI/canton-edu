#!/usr/bin/env python3
"""Write batch 7 zh-cursor JSON files."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs/education/canton-dev/zh-cursor"

PAYLOADS = {
    "appdev-modules-m5-deployment-progression": {
        "zhTitle": "部署晋级路径",
        "summary": "LocalNet→DevNet→TestNet→MainNet 四环境差异、Global Synchronizer 三类升级与晋级检查清单。",
        "body": """> 将 Canton 应用从 LocalNet 经 DevNet、TestNet 推进至 MainNet 生产环境

Canton 应用开发跨越四个环境，各对应开发与部署生命周期的不同阶段。应用按序推进：LocalNet 开发、DevNet 早期集成、TestNet 预生产验证、MainNet 生产。

## 环境概览

* **LocalNet** — 通过 Docker Compose 完全在本地运行。你控制全部 validator 与 synchronizer。无外部依赖、无成本。
* **DevNet** — 由 Global Synchronizer Foundation 运营的共享开发网。用于与真实 Global Synchronizer 基础设施的早期集成测试。会定期重置，更新频繁，可能有破坏性变更。
* **TestNet** — 预生产网络，配置与升级节奏与 MainNet 一致。用于生产部署前的最终验证。
* **MainNet** — Canton Network 生产环境。真实 Canton Coin（CC）、真实 traffic 成本、真实用户。

## 环境间变化

四层环境的核心架构相同：应用经 Ledger API 连接 validator 的 participant 节点。变化的是周边基础设施。

| 类别 | LocalNet | 共享网络（DevNet / TestNet / MainNet） |
| ----------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **身份与认证** | 预配置 Keycloak 与默认用户 | 需完成 validator 入网 + validator 认证提供方签发的有效 JWT |
| **网络连接** | 运行于 localhost | Validator 须连接 Global Synchronizer sequencer 节点 |
| **Canton Coin 与 Traffic** | 模拟 CC 与 traffic | 需真实 CC 购买 traffic（可配置自动充值）。DevNet 可用 `Tap`。 |
| **DAR 部署** | 直接上传到本地 validator | 经 validator participant 上传；可能与对手方协调同步 |

## Global Synchronizer 上的升级类型

<Note>
  详细升级流程见 [Validator Upgrades](/global-synchronizer/production-operations/validator-upgrades)。
</Note>

超级验证者（SV）会定期对 Global Synchronizer 实施升级以改进功能、修复问题并引入新特性。作为节点运营方或应用提供方，应了解可能发生的三类升级。

### 类型 1：向后兼容变更

类型 1 升级涉及 Splice 应用及 Canton 同步层行为的向后兼容变更。这些非破坏性变更每周一进行。

Validator 落后一两个 Splice 版本通常仍可运行，但 SV 建议保持与每周升级同步。「跳版本升级」（一次跨多个版本）未经 SV 官方测试，虽通常可用但风险更高。

### 类型 2：Daml 模型变更

类型 2 升级修改 Splice 应用底层的 Daml 模型，会在应用链上产生分叉，每隔数月发生。

流程先通过类型 1 升级分发新 Daml 模型，再经离线 Canton Improvement Proposal（CIP）由 SV 节点所有者批准，随后 SV 链上投票确定新模型生效的具体日期时间。截止后仅运行最新 Splice 版本的 validator 可参与使用新模型的交易；未采用最新版本的 validator 无法参与。

### 类型 3：不兼容协议变更

类型 3 升级涉及 Canton 同步协议的根本变更，需停机（有时称 Hard Migrations），每三至四个月一次。

实施需经离线投票批准的 CIP，再由 SV 链上投票排期。迁移影响所有 SV 与 validator，需从旧协议协调过渡到新协议。目前 Canton 要求此类升级时所有节点一起迁移。

## 晋级检查清单

将应用晋级到下一环境前，请确认：

### LocalNet → DevNet

* 全部 Daml Script 单元测试通过（`dpm test`）
* 针对 LocalNet 的后端集成测试通过
* DAR 干净编译（`dpm build`）
* Validator 已完成 DevNet 入网
* 已配置 DevNet 认证（不再使用默认 Keycloak 用户）

### DevNet → TestNet

* DevNet 上真实多方工作流的端到端测试通过
* 应用能应对类型 1 升级（每周 Splice 更新）而不中断
* 预期负载下性能可接受
* DAR 部署流程已文档化并测试
* 已配置监控与告警

### TestNet → MainNet

* TestNet 上完整回归套件通过
* 已在 TestNet 至少经历一个类型 1 升级周期
* 存在事件响应运维手册
* 已配置 CC 与 traffic 管理（自动充值、预算监控）
* 组织已审查与对手方的 DAR 部署协调流程

应用提供方应在 DevNet、TestNet、MainNet 维护节点，以保证升级期间运营顺畅。在三套环境均维护节点可大幅提高 MainNet 升级不中断服务或客户体验的概率。

## 下一步

* [Environment Configuration](/appdev/modules/m5-environment-configuration) — 各环境的 DPM 配置
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 自动化晋级流水线""",
    },
    "appdev-modules-m5-environment-configuration": {
        "zhTitle": "环境配置",
        "summary": "DPM 全局与项目配置、daml.yaml 环境变量插值，以及 LocalNet 与共享网络的认证设置。",
        "body": """> 为不同 Canton Network 环境配置 DPM、项目设置与认证

Canton 应用在各环境（LocalNet、DevNet、TestNet、MainNet）需要不同配置。本节涵盖配置层次：DPM 全局设置、项目级 `daml.yaml`、环境变量与认证。

## DPM 配置

DPM 是 Daml 的包管理器。

`dpm` 可同时通过配置文件与环境变量配置，环境变量优先于配置文件。

### 配置文件

配置文件位于 `${DPM_HOME}/dpm-config.yaml`：

* `registry` — 覆盖 `dpm` 拉取 SDK 与组件的默认位置。稳定版默认为 `europe-docker.pkg.dev/da-images/public`；不稳定版用 `europe-docker.pkg.dev/da-images/public-unstable`。
* `registry-auth-path` — 覆盖 registry 的默认认证文件。
* `insecure` — 允许 `dpm` 从不安全（HTTP）registry 拉取。

### 环境变量

以下会覆盖对应配置文件项：

* `DPM_REGISTRY` — SDK 拉取的 registry 地址
* `DPM_REGISTRY_AUTH` — registry 访问认证文件
* `DPM_INSECURE_REGISTRY` — 允许不安全 registry 连接
* `DPM_LOG_LEVEL` — `dpm install`、`dpm version` 等命令的日志级别（`debug`、`info`、`error`、`warn`）
* `DAML_PACKAGE` — 不在包目录也可在包上下文中运行 `dpm`（如 `DAML_PACKAGE=/path/to/package`）
* `DPM_SDK_VERSION` — 全局覆盖 SDK 版本（覆盖所有 `daml.yaml` 的 `sdk-version`，不影响 `dpm install`）

## 项目配置

### daml.yaml

每个 Daml 包有 `daml.yaml`，指定 SDK 版本、包名、源码位置与依赖。`dpm build` 用此文件解析依赖并编译。

### multi-package.yaml

多包项目用 `multi-package.yaml` 告诉 `dpm` 如何查找并构建：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  packages:
    - ./path/to/package/a
    - ./path/to/package/b

```

`dpm` 按依赖拓扑顺序构建这些包。

### 环境变量插值

`daml.yaml` 与 `multi-package.yaml` 的所有字符串字段支持 `${MY_VARIABLE}` 插值：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: ${SDK_VERSION}
name: ${PROJECT_NAME}_test
source: daml
version: ${PROJECT_VERSION}
dependencies:
  - ${DEPENDENCY_DIRECTORY}/my-dependency-1.0.0.dar
```

用反斜杠前缀转义：\\${NOT_INTERPOLATED}。

便于将 SDK 版本、包版本等抽到 `.envrc` 或构建系统变量；也可通过环境变量传入依赖 DAR，适合构建系统在缓存中管理 DAR 产物。

## 分环境设置

各环境通常只需为少量配置点设不同值。可用如下模式管理。

### LocalNet

LocalNet 自包含。cn-quickstart 的 Makefile 与 Docker Compose 处理大部分设置：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# .envrc（或 .envrc.private 覆盖）
export PARTY_HINT="your-company"
export DAML_SDK_VERSION="3.4.9"
```

认证使用捆绑的 Keycloak 与默认用户（`app-user`、`app-provider`、`sv`）。

### DevNet / TestNet / MainNet

共享网络需配置连接详情与认证：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 环境专用设置
export LEDGER_HOST="your-validator.example.com"
export LEDGER_GRPC_PORT="5001"    # gRPC Ledger API 端口（依 validator 配置）
export LEDGER_HTTP_PORT="7575"    # HTTP JSON API 端口（依 validator 配置）
export AUTH_URL="https://auth.your-validator.example.com"
export AUTH_CLIENT_ID="your-app-client-id"
```

Ledger API 端点、认证 URL 与 party 标识因环境而异。可放在 `.envrc.devnet`、`.envrc.testnet`、`.envrc.mainnet` 并按需加载。

## 认证配置

Canton validator 用基于 JWT 的认证保护 Ledger API。应用需有效 token 才能提交命令与读取交易。

### LocalNet 与 Keycloak

cn-quickstart LocalNet 含预配置 Keycloak。经 Keycloak token 端点获取 token：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "http://localhost:8080/realms/canton/protocol/openid-connect/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=your-app" \
  -d "client_secret=your-secret"
```

### 生产环境

DevNet、TestNet、MainNet 上由 validator 的认证提供方签发 token。具体机制取决于 validator 的 IAM，流程相同：应用获取 JWT 并在 Ledger API 请求中以 Bearer token 携带。

gRPC 客户端将 token 设为 call credential；HTTP/JSON 请求放在 `Authorization` 头。

## 覆盖 SDK 组件（高级）

<Warning>
  此为高级主题。仅在支持指导下、针对特定事件或兼容性问题时覆盖 SDK 组件。
</Warning>

`dpm` 支持为单包或整个 multi-package 项目覆盖个别 SDK 组件。在 `daml.yaml` 中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: 3.4.9
override-components:
  damlc:
    version: 3.4.0-snapshot.20251007.14274.0.ve2024cd6
```

`multi-package.yaml` 中相同 `override-components` 块作用于所有包。两文件均指定时，`dpm` 先应用 `multi-package.yaml` 覆盖，再应用 `daml.yaml`（`daml.yaml` 优先级最高）。

安装覆盖组件：

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    dpm install package

```

## 下一步

* [Deployment Progression](/appdev/modules/m5-deployment-progression) — 环境差异与晋级清单
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 在自动化流水线中使用环境配置""",
    },
    "appdev-modules-m5-localnet-development": {
        "zhTitle": "LocalNet 开发",
        "summary": "cn-quickstart LocalNet 拓扑、开发五阶段、启停与端口规律，以及日志与 Canton Console 调试。",
        "body": """> 将 cn-quickstart 的 LocalNet 作为主要开发与测试环境

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
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user up -d

# 停止全部节点
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user down -v
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
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               run --rm console
```

cn-quickstart：`make canton-console`。

### 常见问题

* **容器无法启动** — 检查内存。三 validator 全开占用较大，可禁用未用 profile 减负。
* **Scan UI 无 round** — 启动后数分钟才出现数据，初始引导期间属正常。
* **数据库连接错误** — 单一 PostgreSQL 服务所有组件，确认其先于其他服务成功启动。

## 下一步

* [Testing Strategies](/appdev/modules/m5-testing-strategies) — Canton 应用测试金字塔
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — 从 LocalNet 到 DevNet、TestNet、MainNet""",
    },
    "appdev-modules-m5-manage-daml-packages": {
        "zhTitle": "如何上传与查询 Daml 包",
        "summary": "经 JSON Ledger API 上传 DAR、用 damlc 提取包 ID，并查询 participant 上已注册包状态。",
        "body": """> 向 participant 上传 DAR 并在运行时查询可用 Daml 包。

Canton Participant Node 暴露包管理服务，支持上传与发现 Daml 包。本指南说明如何用 JSON Ledger API（OpenAPI 描述）以编程方式操作包。

要了解 Daml 包概念，请参阅关键概念中的 DAR 文件与 Daml 包（官方文档）。

运维指南中的包管理章节介绍如何用 Canton console 上传并检查包。

## 前置条件

确保 Canton Participant Node 开放 JSON Ledger API HTTP 端口。参见教程：Get started with Canton and the JSON Ledger API。

确保可使用 Daml 工具（Assistant `daml`、Compiler `damlc`）。

安装 `curl` 或类似 HTTP 工具。

若需格式化、过滤 `curl` 的 JSON 响应，安装 `jq` 或类似工具。

任何账本交互前，先将模型构建为 `.dar` 文件。

## 如何上传 DAR 归档文件

假设你在开发名为 `MyModel` 的 Daml 模型，要基于此模型开始链上交互。第一步是上传其包，并确保在所有交互的 Participant Node 上完成 vetting。

JSON Ledger API 提供端点，可在上传过程中将包 vet 到 Participant Node。

多数交互基于 package ID，用 damlc 检查生成的 DAR 并提取主包 ID：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml damlc inspect-dar --json .daml/dist/mymodel-1.0.0.dar | jq '.main_package_id'
```

damlc 返回包 ID：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed"
```

上传包时对 `v2/packages` 发起 POST：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl --data-binary @.daml/dist/mymodel-1.0.0.dar http://localhost:7575/v2/packages
```

可验证包已在账本上注册：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages/47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed/status
```

账本返回包状态：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageStatus": "PACKAGE_STATUS_REGISTERED"
}
```

## 如何查询已有包

列出 Participant Node 已知全部包，对 `v2/packages` 发起 GET：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages
```

Participant 返回包含全部已知包 ID 的消息：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "packageIds": [
    "9e70a8b3510d617f8a136213f33d6a903a10ca0eeec76bb06ba55d1ed9680f69",
    "47fc5f9bf30bdc147465d7b5fe170a0bc26b3677b45b005573130d951fdaebed",
    "bfda48f9aa2c89c895cde538ec4b4946c7085959e031ad61bde616b9849155d7"
  ]
}
```

列表较长时，用 `jq` 过滤并确认期望的包 ID 是否存在：

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost:7575/v2/packages | jq '.packageIds | .[] | select(startswith("47"))'
```""",
    },
    "appdev-modules-m5-networks-and-use-cases": {
        "zhTitle": "SV 运营网络与用例",
        "summary": "DevNet/TestNet/MainNet 定位、应用运营商测试指南，以及 Daml Script、CI 集成与 TestNet 部署三层测试。",
        "body": """> DevNet、TestNet、MainNet 的用途及面向应用开发者的测试指南

超级验证者运营三个网络：

1. DevNet
2. TestNet
3. MainNet

## DevNet

该网络作为 TestNet 的预演场，配置便于探索：自 featured 应用、CC tapping、validator 自助入网。SV 以高可用承诺、尽力而为方式管理 DevNet，及时验证升级，并用于负载测试；约每三个月定期重置，避免达到无法代表 MainNet 的可扩展性瓶颈。特殊情况下若问题修复成本过高，SV 可能进行计划外重置。

DevNet 让应用运营商测试需要全新 validator 节点的入网工作流。

<Note>
  请公平使用网络，避免过量负载。只要运维开销可控，网络预期保持开放。
</Note>

## TestNet

TestNet 是 SV、Validator 与应用运营商的预生产环境，用于在部署到 MainNet 前测试即将发布的 SV 与 Validator 节点软件升级。该环境与 MainNet 配置完全一致。应用运营商在 TestNet 维护应用长期测试实例，主要作用：

在保障应用代码数据连续性的前提下测试升级；让其他应用运营商测试与其应用的集成。

<Note>
  应用运营商应通过活跃度奖励、featured app 奖励及友好 SV 协作获得覆盖 traffic 费用所需的 TestNet-CC。
</Note>

## MainNet

该网络是 SV、Validator 与应用运营商的生产环境，用于将应用部署到网络。

## 测试指南

我们建议应用运营商按以下方式测试应用：

1. **用 Daml Script 做单元测试：** 先用 Daml Script 充分测试 Daml 代码，覆盖应用内全部工作流及依赖，验证逻辑与数据模型正确性。
2. **在 CI 中做集成测试：** 在持续集成流水线中实现集成测试，使用 mock 依赖，针对连接独立 Canton synchronizer（domain）的独立 Canton participant 运行，确保组件在受控环境中正确协作。
3. **TestNet 部署：** 在 TestNet 部署应用测试实例，并与支持以下关键用例的其他应用测试实例集成：
   1. 基础设施升级
   2. 应用版本升级
   3. 消费依赖方的应用升级""",
    },
    "appdev-modules-m5-testing-strategies": {
        "zhTitle": "测试策略",
        "summary": "Canton 应用测试金字塔：Daml Script 单元测试、后端集成、E2E、性能测试及 flaky 测试处理。",
        "body": """> Canton 应用测试金字塔：从 Daml Script 单元测试到集成与端到端测试

测试 Canton 应用与任何分布式系统原则相同：尽量自动化，在能捕获缺陷的最低层测试。差异在于各层工具及多方、隐私账本带来的特有挑战。

## 测试金字塔

Canton 应用采用三层测试，各层捕获不同类别问题：

* **单元测试** — Daml Script 隔离验证智能合约逻辑，在内存账本（Sandbox）上运行，无网络开销。
* **集成测试** — 针对运行中的 Canton sandbox 或 LocalNet 测试后端与 API，验证链下代码与账本正确交互。
* **端到端测试** — 跨多个 validator、后端与前端的完整工作流，验证用户实际体验的系统行为。

## 用 Daml Script 做单元测试

Daml Script 是单元测试智能合约逻辑的主要工具。将测试 script 写为 `Script ()` 类型的顶层值，`dpm test` 在 Sandbox 上运行。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm test
```

Daml Script 可在 Sandbox 上运行，执行通常只需数秒。

单元测试创建 party、提交命令并断言结果：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testTokenTransfer : Script ()
testTokenTransfer = do
  alice <- allocateParty "Alice"
  bob <- allocateParty "Bob"

  -- Alice creates a token
  tokenCid <- submit alice do
    createCmd Token with
      owner = alice
      issuer = alice
      amount = 100.0

  -- Alice transfers to Bob
  submit alice do
    exerciseCmd tokenCid Transfer with
      newOwner = bob
      transferAmount = 50.0

  -- Verify Bob received the token
  bobTokens <- query @Token bob
  assertMsg "Bob should have one token contract" (length bobTokens == 1)
```

查看 `dpm test` 输出确认各 script 通过或失败。

### 单元层应测什么

聚焦 Daml 模型特有行为：

* 有效与无效参数的模板创建
* Choice 授权（正确 controller 可行使，他人不可）
* Choice 内业务逻辑（计算、状态转移）
* 边界与错误条件（应失败的断言）
* 多方授权模式（提议-接受工作流）

### 测试代码与生产代码分离

Daml 工作流单元测试编译进 DAR，这些 DAR 仅用于测试，不应部署到 validator。将测试放在独立包，与生产代码分离：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml/
├── main/           # 生产 Daml → main.dar
│   └── daml.yaml
└── test/           # 测试 script → test.dar（依赖 main.dar）
    └── daml.yaml
```

## 集成测试

集成测试验证链下代码——后端服务、API 处理器、数据库查询——与 live ledger 正确协作。有两种工具：

* **`dpm sandbox`** — 单进程启动本地 Canton sandbox，适合单后端对 Ledger API 测试，无需完整网络开销。
* **LocalNet** — Docker Compose 多 validator 网络。测试需要多方在不同 validator、钱包集成或 PQS 时使用。

### 后端集成测试

对连接 Ledger API 的后端，测试应：

1. 启动 sandbox 或连接运行中的 LocalNet
2. 创建测试 party 并上传 DAR
3. 经后端 API 层提交命令
4. 断言账本状态或 API 响应

Java 集成测试经 gRPC 连接 Ledger API 并提交命令：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Set up a gRPC channel to the participant's Ledger API
Channel channel = ManagedChannelBuilder
    .forAddress(ledgerhost, ledgerport)
    .usePlaintext()
    .build();

// Create a blocking stub for command submission
CommandServiceGrpc.CommandServiceBlockingStub commandService =
    CommandServiceGrpc.newBlockingStub(channel);

// Submit a contract creation and wait for the transaction result
var updateSubmission = UpdateSubmission
    .create(APP_ID, randomUUID().toString(), update)
    .withActAs(party);
var request = new SubmitAndWaitForTransactionRequest(
    updateSubmission.toCommandsSubmission());
var response = commandService.submitAndWaitForTransaction(request.toProto());
```

查询活跃合约使用 `StateService`：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
StateServiceGrpc.StateServiceBlockingStub stateService =
    StateServiceGrpc.newBlockingStub(channel);
long ledgerEnd = stateService
    .getLedgerEnd(GetLedgerEndRequest.newBuilder().build())
    .getOffset();

var request = new GetActiveContractsRequest(eventFormat, ledgerEnd);
Iterator<GetActiveContractsResponse> activeContracts =
    stateService.getActiveContracts(request.toProto());
```

### 测试隔离

优化做法是长期运行 Canton 实例，避免反复初始化。用每次测试唯一的 participant 用户与 party 隔离测试；可在测试 harness 中为 party 与用户名追加测试运行 ID 后缀。

这样可在同一 Canton 实例上并行运行测试而不互相干扰。

## 端到端测试

端到端测试跨多个 validator、后端与前端，演练终端用户与系统间的工作流。

### 浏览器自动化

涉及前端的测试可用 [Selenium](https://www.selenium.dev/) 或 [Playwright](https://playwright.dev/) 驱动浏览器：登录、经 UI 创建合约、验证对手方看到预期结果。

### 时间相关工作流

时间敏感工作流可在 Daml 中用 `passTime`，并为 CI 配置更短等待时间。含日历或时间函数的流程（如带息票支付的债券生命周期）可用 `passTime` 推进时间；端到端测试可将工作流推进间隔设为毫秒以缩短 CI。在测试 harness 中暂停/恢复自动化以避免竞态。

## 处理 Flaky 测试

分布式系统存在数据传播延迟与并发执行，可能导致测试不稳定，削弱开发者信任并拖慢迭代。

Canton 测试中 flaky 常见来源：

* **传播延迟** — 命令成功但交易尚未出现在读取方 validator。用带超时的轮询而非固定 sleep。
* **Party 可见性** — 在所有相关 validator 分配 party 之前就查询合约。
* **并发行使** — 两个测试同时行使同一合约，一个成功另一个发现合约已归档。

消除 flaky 的投入回报很快。可靠的测试套件意味着更快反馈与更有信心的部署。

## 性能测试

尽早并持续做性能测试。为各相关工作流单独建性能测试；用接近生产特征的合成数据做规模测试；测量性能指标并在运行间重置以发现回归；长时间 soak 测试发现瓶颈；配置告警监控系统故障，随时间调优可观测性。

Canton 应用性能测试需区分链上与链下操作。账本操作有随交易复杂度与参与方数量变化的同步开销；链下操作（PQS 查询、后端逻辑）按常规定位分析。

## 下一步

* [LocalNet Development](/appdev/modules/m5-localnet-development) — 搭建并使用 cn-quickstart LocalNet
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 自动化测试流水线""",
    },
    "appdev-modules-m6-deployment": {
        "zhTitle": "升级部署",
        "summary": "v1→v2 部署序列、对手方协调、合约迁移策略、回滚方式及按环境分阶段推广。",
        "body": """> 跨环境部署 Daml 包升级：协调、回滚与迁移策略

部署升级意味着将新版本包放到所有相关 validator 上，并将工作流从当前版本过渡到新版本。Canton 的分布式特性意味着不能简单「拨开关」——需在保持现有工作流运行的同时跨组织协调。

下文讨论中，当前版本为 `v1`，新版本为 `v2`。

## 部署序列

部署遵循 [概览](/appdev/modules/m6-overview) 中的异步 rollout 模型：

1. **将 v2 DAR 上传到你自己的 validator** — 在你的 participant 上传 v2 包，此时尚不影响其他组织。

2. **向对手方分发 v2 DAR** — 将 v2 DAR 文件分享给应用用户与其他组织。他们须先上传到各自 validator，跨组织的 v2 工作流才能进行。

3. **更新后端使用 v2** — 将后端 Ledger API 客户端指向 v2 包。新合约用 v2 创建，既有 v1 合约仍可用。注意后端可能需同时支持 v1 与 v2 包以尽量减少停机。

4. **迁移既有合约（如需要）** — 需要 v2 数据的合约，运行迁移自动化，行使升级 choice 归档 v1 并创建 v2 替代。

5. **设定切换日期** — 公布各方完成过渡的目标日期。此后可通过 unvet v1 包下线 v1 工作流。

6. **Vet 新包** — 在目标日期，各方完成过渡并 vet v2 包。此后可通过 unvet v1 下线 v1 工作流。

7. **Unvet v1（可选）** — 全部 v1 合约已归档或迁移后，unvet v1 包以完成升级。

## 与对手方协调

未协调就切换到 v2 工作流可能导致命令提交失败、工作流卡住。常见场景：

* **Daml 模型版本不匹配** — 若某利益相关方 participant 缺少所需 v2 包或未 vet v2，引用 v2 工作流的命令会失败；若 v1 仍 vet，则使用 v1。
* **显式披露** — v2 合约用于显式披露时，若提交方 participant 缺少 v2 包，引用该合约的命令会失败，即使披露合约的全部利益相关方已上传 v2。

为避免问题，清晰沟通升级时间线：

* 在切换日期前充分分发 v2 DAR
* 提供上传与 vet DAR 的说明
* 给各组织足够时间用 v2 测试自有后端
* 在行使仅 v2 工作流前确认就绪

## 合约迁移策略

并非所有合约都需显式迁移。Daml 中合约归档可通过多种路径：

* **自然生命周期结束** — 合约代表的业务实体自然结束（如贷款全额偿还）。
* **状态不再成立** — 合约所证明的状态已无效。
* **底层实体修改** — 实体仍相关，但 Daml 合约不可变，更新需归档旧合约；若用 v2 创建更新合约，则自然、渐进地从 v1 迁离。
* **显式升级** — 作为升级流程的一部分归档合约，理想情况由 upgrade runner 自动化。

首选在 Daml 内直接处理版本与升级，而非依赖外部自动化。但在某些情况下，有效 v2 只能结合链下系统或 ACS/PQS 查询从 v1 生成。

对需将旧 v1 合约升级到 v2 模板的不向后兼容变更：

1. 在 v1 模板上增加 consuming 的 `Upgrade` choice，归档旧合约并创建新模板实例
2. 必要时通过额外 choice 参数为 `Upgrade` 提供参考数据（如默认值）
3. 用后端自动化遍历 ACS 并对每个合约行使 `Upgrade` choice

## 回滚策略

### 通过 unvet 回滚

对未修改既有模板与 choice 类型的升级，通过 unvet v2 DAR 包回滚。仅当尚未用 v2 创建任何合约时适用。

### 通过向前滚动回滚

对给既有模板增加新字段的升级，回滚更复杂：若至少有一个合约使用了新字段，旧版 Daml 代码无法读取这些合约。此时：

1. 发布忽略新字段的新版 DAR。
2. 引入 `Downgrade` choice，将新字段重置为 `None`。
3. 用后端自动化遍历 ACS 并调用 `Downgrade` choice。

为避免复杂的向前滚动回滚，可将升级拆为两步：

1. 增加新字段但暂不使用——因未改 choice，此步无需回滚。
2. 单独升级修改 choice 实现以使用新字段——出问题可通过 unvet 回滚。

## 分环境推广

遵循 [部署晋级路径](/appdev/modules/m5-deployment-progression) 的标准推广路径：

* **LocalNet** — 本地测试完整升级周期：上传 v1、创建合约、上传 v2、验证跨版本行为、运行迁移自动化。
* **DevNet** — 与真实对手方部署升级，验证 DAR 分发与混合版本跨 validator 运行。
* **TestNet** — 走完含协调切换日期的完整升级流程，在 MainNet 前发现协调问题。
* **MainNet** — 与真实对手方和真实合约执行升级计划。

## 下一步

* [Smart Contract Upgrades Overview](/appdev/modules/m6-overview) — 返回模块概览
* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — 部署前验证升级路径
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — 通用环境推广策略""",
    },
    "appdev-modules-m6-limitations": {
        "zhTitle": "升级限制",
        "summary": "SCU 硬性边界：包不可删除、模板不可移除、字段/choice/变体构造器不可删及规划兼容变更。",
        "body": """> Daml 智能合约升级的已知限制与约束

Daml 智能合约升级（SCU）功能强大但有明确边界。提前理解这些限制可避免开发与生产推广中的意外。

## 包无法删除

DAR 包上传到 validator 后会永久保留，无法删除或注销。这意味着：

* 曾上传的每个版本仍可用
* Validator 包存储随时间增长
* 无法撤销包上传

请谨慎规划包上传，尤其在 MainNet 上每个包都会永久存在。

## 无法移除模板

无法在后续版本中从包中移除模板。若版本 1 定义 `Asset` 与 `LegacyAsset`，版本 2 仍须包含两者。

### 弃用模板

### 新增与弃用模板

可新增模板。既有模板不可移除，但可通过以下方式弃用：

* 从其他 Daml 代码中移除对它们的引用。
* 添加 `ensure False` 使其不可操作——阻止用该模板创建新合约及行使 choice（包括对既有合约的隐式 `Archive` choice）。

注意后者可能导致账本上大量无法归档的活跃合约，除非再部署更新将 `ensure` 求值为 `True`。要在不留下无法归档合约的情况下弃用模板，应在通过自动化或其他方式归档全部由该模板创建的活跃合约之后，再对模板添加 `ensure False`。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template LegacyAsset
  with
    owner : Party
    value : Decimal
  where
    signatory owner
    ensure False  -- 无法创建新合约
```

## 不允许移除字段、Choice 或变体构造器

SCU 兼容规则禁止移除：

* **模板字段** — 可添加带默认值的可选字段，不可移除既有字段
* **模板 Choice** — 一旦存在，所有未来版本必须保留
* **变体类型的构造器** — 可增加新构造器，不可移除既有构造器

这些规则确保旧包版本创建的合约在新版本下仍有效且可行使。若 validator 仍持有版本 1 的合约，版本 2 包必须能解释它们。

## 字段类型变更受限

不能更改既有字段类型。若版本 1 中 `amount` 为 `Decimal`，版本 2 仍须为 `Decimal`。类型变更属于破坏性修改，会使既有合约不可读。

## 允许的操作

对比之下，以下修改在包版本间允许：

* 添加新模板
* 给既有模板添加带默认值的新可选字段
* 给既有模板添加新 Choice
* 添加新变体构造器
* 添加新接口实现（仅在新模板上）
* 更改 Choice 体（实现逻辑）

## 围绕限制做规划

### 管理不向后兼容的变更

并非所有变更都能保持向后兼容。更新 Daml 模型的策略类似面向服务架构中 API 的演进。

仅允许对现有 API（即当前 Daml 代码）做向后兼容变更。通过创建变更后的 API 引入不兼容变更，例如在 choice 中移除参数。实现不向后兼容升级：

* 引入带 consuming `Upgrade` choice 的新模板，归档旧合约并创建新模板实例，确保升级路径向后兼容。
* 必要时通过额外 choice 参数为 `Upgrade` 提供参考数据（如默认值）。
* 用后端自动化将旧合约迁移到新合约；在自动化完成转换前，部分工作流可能停机。

此方式显式且需要合约利益相关方主动配合——利益相关方始终对影响其合约的变更表示同意，这是特性而非缺陷。

## 延伸阅读

* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — SCU 完整兼容规则
* [Package Naming](/appdev/modules/m6-package-naming) — 考虑破坏性变更的命名惯例
* [Smart Contract Upgrades in Production](/appdev/modules/m7-smart-contract-upgrades) — 推广运维考量""",
    },
    "appdev-modules-m6-package-naming": {
        "zhTitle": "包命名",
        "summary": "反向 DNS、合约模型版本标记、接口与模板分包，以及破坏性变更时的新包命名。",
        "body": """> Daml 智能合约升级的命名惯例与包结构

良好的包命名可在应用经多版本演进时避免混淆。清晰的命名方案可一眼看出归属、用途与版本。

## 反向 DNS 惯例

避免包名冲突，尤其不同应用提供方发布的包。遵循 Java 生态惯例：用提供方反向 DNS 作为包名前缀。例如 Acme Inc. 货币市场基金发行工作流，推荐 `daml.yaml` 配置：`name: com-acme-money-market-fund-issuance`。

Daml 包名用连字符分隔（非点）。反向 DNS 前缀确立组织归属，其余段描述包用途。

```
com-acme-money-market-fund-issuance
com-acme-money-market-fund-trading
org-example-token-registry
```

## 包名中的版本标记

若预期应用生命周期中有破坏性变更，在包名中包含版本标记，明确合约模型的主要版本：

```
com-acme-asset-main-v1
com-acme-asset-main-v2
com-acme-asset-interfaces-v1
```

版本标记指**合约模型版本**，非构建版本。仅在做需新包的破坏性变更时递增（见 [升级限制](/appdev/modules/m6-limitations)）。非破坏性升级（添加可选字段、新 choice）在同一包名内由 SCU 透明处理。

不要在模板名中包含版本号。

## 接口与模板分离

将 Daml 代码至少拆为两个包：

* **接口包** — 构成对外 API 的接口定义。其他应用依赖此包与你的合约交互。
* **模板包** — 实现接口的模板定义，为私有实现。

```
com-acme-asset-interfaces-v1    -- 仅接口
com-acme-asset-main-v1          -- 实现上述接口的模板
```

分离的意义：

* 接口不可升级。独立接口包意味着模板包可独立演进（加字段、choice、新模板）而不动接口包。
* 依赖你接口的其他应用只需导入接口包，不依赖实现细节。
* 不可避免的不兼容接口变更时，发布 `com-acme-asset-interfaces-v2` 与 `v1` 并存，消费者可按己 pace 迁移。

## 通过新包名处理破坏性变更

当 SCU 规则阻止原地升级（如须改字段类型或移除模板）时，创建带递增版本标记的新包：

```
com-acme-asset-main-v1   -- 原始版本
com-acme-asset-main-v2   -- 破坏性变更
```

两包在 validator 上共存。`v1` 下既有合约仍有效。你提供迁移路径——通常是 `v1` 模板上的 choice，归档旧合约并创建 `v2` 替代。利益相关方行使该 choice 迁移合约。

此方式使升级显式。行使 choice 需要其作为 signatory 的授权，利益相关方须同意迁移。

## 命名检查清单

为新包命名时确认：

* 名称以组织反向 DNS 前缀开头
* 名称含清晰功能描述（非仅 "main" 或 "core"）
* 接口包与模板包分开命名
* 若可预见破坏性变更，包含版本标记
* 与现有包命名一致（相同前缀风格、相同分隔符）

## 示例：多包应用

真实应用可能包含：

```
com-acme-lending-interfaces-v1       -- 贷款合约对外接口
com-acme-lending-main-v1             -- 贷款模板、choice、工作流
com-acme-lending-reporting-v1        -- 报表专用模板
com-acme-lending-test-fixtures-v1    -- 测试数据生成器（不部署生产）
```

各包可独立版本化。接口包变更少；主包随每次功能发布变更（非破坏性变更经 SCU）；报表包可能滞后；测试 fixture 永不离开开发环境。

## 延伸阅读

* [Upgrade Limitations](/appdev/modules/m6-limitations) — 驱动包命名决策的约束
* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — 破坏性 vs 非破坏性变更规则
* [Building and Packaging](/appdev/modules/m3-building-packaging) — 用 `dpm build` 编译打包""",
    },
    "appdev-modules-m6-package-selection": {
        "zhTitle": "包选择",
        "summary": "多版本共存时的运行时解析、符号化包引用、vetting/unvetting 及跨版本 fetch 的安全失败规则。",
        "body": """> 多版本包共存时 Canton 账本如何解析使用哪个包版本

多个包版本上传到 validator 后，需要规则决定执行哪个版本。包选择决定这一点——当 v1 与 v2 均可用时，Daml 运行时如何解析模板与 choice。

## 版本解析如何工作

账本上每个合约关联创建它的包版本。获取或行使合约时，运行时使用你代码引用的包版本，不一定是创建合约的版本。

解析遵循：

* **创建合约** — 运行时使用你代码引用的包版本。若后端导入 v2，新合约用 v2 创建。
* **获取合约** — 运行时用你代码引用的版本评估合约数据。fetch 是否成功由 SCU 与 vetting 规则决定（见 [升级兼容性](/appdev/modules/m6-upgrade-compatibility)）。
* **行使 Choice** — 执行你代码引用版本的 choice 体，而非创建合约的版本。即 v2 choice 中的 bug 修复适用于 v1 合约。

## 符号化包引用

不要在后端硬编码具体包版本。在 Ledger API 查询中使用符号化包引用。不指定具体 package ID，而按包名引用：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
#com-example-licensing:Main:License
```

这告诉 Ledger API 匹配 `com-example-licensing` 包任意版本中包含 `Main.License` 模板的合约。后端可同时收到 v1 与 v2 合约，无需为每版写单独查询逻辑。

若无符号引用，每次上传新包版本都需更新后端查询过滤器——违背无缝升级的目的。

## 多版本共存

上传 v2 后 v1 与 v2 在账本上均保持活跃：

* v1 创建的合约仍存在，可 fetch、行使、归档
* 可按代码引用用 v1 或 v2 创建新合约
* 推广期间不同组织可同时使用不同版本

账本不会自动将 v1 合约迁移到 v2。v1 合约保持 v1，直到归档。若合约需要 v2 数据（如新增 `Optional` 字段为非 `None`），须归档 v1 并创建 v2 合约——通过正常业务操作或显式升级 choice。

## 包 Vetting

Vetting 包让其他 participant 节点判断该 participant 上的 party 可参与哪些工作流。包须 vet 后才能使用，为部署增加验证步骤。默认上传 Daml 包时 participant 自动标记为 vet 并在 synchronizer 上发布 vetting 状态。

也可 unvet。例如上传并 vet v2 后 unvet v1，表示 participant 不再参与 v1 工作流，完成升级收尾。

Participant 须在 unvet v1 前完成全部 v1 合约升级，以避免问题。在 v1 已 unvet 但 v2 已 vet 的情况下，用 v1 模板创建的合约仍可用 v2 使用/升级。

## 跨版本 Fetch 行为

运行时使用你代码引用的包版本，不会自动「偏好」较新版本——取决于代码编译所依包。跨版本行为：

* 用 v2 代码 fetch `License`，合约由 v1 创建时，运行时应用 v2 逻辑（新 `Optional` 字段填 `None`）
* 用 v1 代码 fetch，合约由 v2 创建且新字段为 `None` 时，运行时应用 v1 逻辑（忽略未知字段）
* 用 v1 代码 fetch，合约由 v2 创建且新字段非 `None` 时，fetch 失败以防数据丢失

版本不兼容时系统安全失败，而非静默丢弃数据。

## 下一步

* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — 验证升级的版本解析是否正确
* [Deploying Upgrades](/appdev/modules/m6-deployment) — 跨 validator 协调包上传""",
    },
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    written = 0
    for slug, payload in PAYLOADS.items():
        path = OUT / f"{slug}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        written += 1
        print(f"wrote: {slug}")
    print(f"count: {written}")


if __name__ == "__main__":
    main()
