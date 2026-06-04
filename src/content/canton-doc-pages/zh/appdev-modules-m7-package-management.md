---
title: "包管理"
slug: "appdev-modules-m7-package-management"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-package-management.md"
source_title: "Package Management"
tags:
  - appdev
  - modules
  - m7-package-management
---

# 包管理

> 跨环境管理 DAR、版本固定、依赖管理与协调包分发

Daml 包（DAR）是链上逻辑的部署单元。跨环境与组织管理 DAR 比典型软件制品需更多监督，因参与工作流的每个 validator 都需要相同包。

## DAR 生命周期

DAR 经历若干阶段：

1. **构建** — `dpm build` 将 Daml 源码编译为 DAR。输出确定性：相同源码与 SDK 版本产生相同 DAR。
2. **测试** — 将 DAR 上传到 sandbox 或 LocalNet 并运行测试套件。
3. **存储** — 发布到制品库（Artifactory、Nexus、S3 或 CI 制品存储）。
4. **分发** — 与需在各自 validator 上部署的对手方共享 DAR。
5. **部署** — 上传到生产 validator 并 vet。
6. **废弃** — 成功升级周期后 unvet 旧包版本。

## 版本固定

在 `daml.yaml` 中固定 SDK 版本以防意外升级：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: 3.4.9
name: com-example-licensing
version: 1.2.0
```

运行 `dpm install package` 安装 `daml.yaml` 指定的 SDK。固定的 `sdk-version` 保证团队使用同一 SDK 构建。

## 依赖管理

多包项目用 `multi-package.yaml` 声明包间依赖。`dpm build` 按拓扑顺序解析并构建。

外部依赖（其他组织发布的包）以项目内 DAR 管理：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml.yaml
dependencies:
  - daml-prim
  - daml-stdlib
  - ./deps/com-acme-tokens-1.0.0.dar
```

将依赖 DAR 存入仓库，或用环境变量从共享制品库拉取：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
  - daml-prim
  - daml-stdlib
  - ${DEPS_DIR}/com-acme-tokens-1.0.0.dar
```

依赖发布新版本时，先针对新版本测试再更新固定版本。依赖更新可能改变你使用的 interface 与 choice 行为。

## 制品库

将生产 DAR 与版本元数据存入专用制品库。典型结构：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
artifacts/
├── com-example-licensing/
│   ├── 1.0.0/
│   │   ├── com-example-licensing-1.0.0.dar
│   │   └── metadata.json
│   └── 1.1.0/
│       ├── com-example-licensing-1.1.0.dar
│       └── metadata.json
```

DAR 体积小，小项目也可纳入版本控制。专用库的优势是将制品管理与源码分离，便于向对手方分发。

## 向对手方分发包

工作流涉及的所有 validator 须部署相同 DAR。Daml 代码定义跨 validator 同步的状态与工作流 API，类似向 gRPC 客户端开发者共享的 `.proto`。

建议将 Daml 代码与前后端代码分库，向应用用户组织提供 tarball 或只读访问，以便其审查并构建代码，对安装在其 validator 上的 DAR 行为有信心。

分发实践：

* 发布到对手方可访问的共享制品库
* 提供构建说明以便从源码编译并验证 DAR 一致
* 附变更日志说明版本间差异
* 沟通升级时间线（见 [Upgrade Deployment](/appdev/modules/m6-deployment)）

## 包模块化

* **按 stakeholder 划分模块** — 按 stakeholder 交互模块化工作流，简化升级并维护隐私。DAR 仅需分发给托管该工作流参与 party 的 validator。
* **公开与私有 API** — 最小化公开工作流，内部工作流放在独立 DAR 以灵活演进业务。将 interface 定义放在独立包便于工作流管理；用 interface 定义公开 API，使应用升级更容易。
* **测试代码分离** — 测试代码与生产代码分 DAR。测试 DAR 不应部署到生产 validator。

## 下一步

* [Security Best Practices](/appdev/modules/m7-security) — 保护包与部署流水线
* [Performance](/appdev/modules/m7-performance) — Canton 应用优化策略

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
