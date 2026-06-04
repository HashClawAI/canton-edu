---
title: "CI/CD 集成"
slug: "appdev-modules-m5-ci-cd-integration"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-ci-cd-integration.md"
source_title: "CI/CD Integration"
tags:
  - appdev
  - modules
  - m5-ci-cd-integration
---

# CI/CD 集成

> 使用 dpm build、test 与部署自动化构建 Canton 应用的 CI/CD 流水线

Canton 应用的 CI/CD 流水线与其他软件项目结构相同：构建、打包、测试、部署。Canton 特有部分是用于编译 Daml、运行 Script 测试与管理 DAR 制品的 `dpm` 命令。

## 流水线结构

典型流水线有四个阶段：

1. **构建** — 编译 Daml 代码并生成客户端绑定
2. **打包** — 产出可部署制品（DAR、容器镜像）
3. **测试** — 运行 Daml Script 单元测试与后端集成测试
4. **部署** — 上传 DAR 并将链下服务部署到目标环境

## 构建阶段

构建阶段编译 Daml 包并为后端与前端生成代码绑定。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 从 daml.yaml 安装 SDK 版本
`dpm install` <<version>>

# 编译 Daml 为 DAR
dpm build

# 生成 Java 绑定
dpm codegen-java .daml/dist/<<your-project.dar>> -o <<output-directory>>

# 生成 TypeScript 绑定（如需要）
dpm codegen-js .daml/dist/<<your-project.dar>> -o <<output directory>>
```

多包项目中，根目录存在 `multi-package.yaml` 时，`dpm build` 按依赖顺序构建所有包。

### 构建缓存

DAR 编译是确定性的：相同源码与 SDK 版本产生相同 DAR。在 CI 运行间缓存 `.daml/dist/` 目录，Daml 源码未变时可跳过重编译。多数 CI 系统（GitHub Actions、GitLab CI、Jenkins）支持按文件哈希缓存。

## 测试阶段

### Daml Script 测试

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm test
```

在 Sandbox 上运行测试包中所有 `Script ()` 声明。任一断言失败时 `dpm test` 以非零码退出，流水线失败。

有独立测试包的项目，可在各测试包目录运行 `dpm test`，或使用包含测试包的 `multi-package.yaml`。

### 后端集成测试

Daml 测试通过后，针对 sandbox 运行后端集成测试：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 后台启动 sandbox
dpm sandbox &
SANDBOX_PID=$!

# 等待 sandbox 就绪
sleep 30  # 或使用健康检查循环

# 运行后端测试，例如 Java 后端
cd backend && ./gradlew test

# 清理
kill $SANDBOX_PID
```

需要完整多 validator 设置的测试，用 Docker Compose 启动 [LocalNet](/appdev/modules/m5-localnet-development) 而非 sandbox。更重但覆盖跨 validator 场景。

## 打包阶段

### DAR 制品

`dpm build` 产出的 `.dar` 文件是主要 Daml 制品。存入 CI 制品仓库（Artifactory、Nexus、S3 或 CI 内置存储）并附带版本元数据。

含版本的命名约定便于追踪：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
your-app-1.0.0.dar
your-app-1.1.0.dar
```

DAR 中的版本来自 `daml.yaml` 的 `version` 字段。可用环境变量插值从 CI 流水线设置：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml.yaml
version: ${PROJECT_VERSION}
```

### 容器镜像

若后端与前端容器化，在此阶段构建并打标签镜像。将 DAR 嵌入制品或在部署时挂载。

## 部署阶段

部署到各环境涉及两部分：向 validator 上传 DAR，部署链下服务（后端、前端、PQS）。

### DAR 上传

通过 participant 的 HTTP Ledger API 向目标 validator 上传 DAR：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://${LEDGER_HOST}:${LEDGER_HTTP_PORT}/v2/packages" \
  -H "Authorization: Bearer ${AUTH_TOKEN}" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @.daml/dist/your-project.dar
```

验证上传：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s "https://${LEDGER_HOST}:${LEDGER_HTTP_PORT}/v2/packages" \
  -H "Authorization: Bearer ${AUTH_TOKEN}"
```

### 环境晋升

使用 CI 系统的环境或 stage 抽象控制晋升。常见模式：

* 推送到 `main` 自动部署到 DevNet
* 手动审批门从 DevNet 晋升到 TestNet
* 另一手动门从 TestNet 晋升到 MainNet

每次晋升以不同环境配置运行相同部署步骤（见 [环境配置](/appdev/modules/m5-environment-configuration)）。

## 示例：GitHub Actions

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install DPM
        run: curl https://get.digitalasset.com/install/install.sh | sh

      - name: Install SDK
        run: dpm install package

      - name: Build Daml
        run: dpm build

      - name: Run Daml tests
        run: dpm test

      - name: Generate Java bindings
        run: dpm codegen-java .daml/dist/your-project.dar -o generated-java

      - name: Build backend
        run: cd backend && ./gradlew build

      - name: Upload DAR artifact
        uses: actions/upload-artifact@v4
        with:
          name: dar-${{ github.sha }}
          path: .daml/dist/*.dar
```

## 监控 CI 健康

开发测试期间定期审查日志，如在 CI 运行中捕获日志用于调试失败。为测试开发环境设置指标告警以监控应用健康，确保运维复用并集成到长期测试实例。开发阶段调优的告警可在运维中复用以检测系统健康问题。

## 下一步

* [测试策略](/appdev/modules/m5-testing-strategies) — 测试金字塔与方法细节
* [环境配置](/appdev/modules/m5-environment-configuration) — 各环境配置管理
* [部署进阶](/appdev/modules/m5-deployment-progression) — 各晋升阶段应验证的内容

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
