---
title: "环境配置"
slug: "appdev-modules-m5-environment-configuration"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-environment-configuration.md"
source_title: "Environment Configuration"
tags:
  - appdev
  - modules
  - m5-environment-configuration
---

# 环境配置

> 为不同 Canton Network 环境配置 DPM、项目设置与认证

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

用反斜杠前缀转义：\${NOT_INTERPOLATED}。

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
curl -X POST "http://localhost:8080/realms/canton/protocol/openid-connect/token"   -d "grant_type=client_credentials"   -d "client_id=your-app"   -d "client_secret=your-secret"
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
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 在自动化流水线中使用环境配置

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
