---
title: "部署晋级路径"
slug: "appdev-modules-m5-deployment-progression"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-deployment-progression.md"
source_title: "Deployment Progression"
tags:
  - appdev
  - modules
  - m5-deployment-progression
---

# 部署晋级路径

> 将 Canton 应用从 LocalNet 经 DevNet、TestNet 推进至 MainNet 生产环境

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
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 自动化晋级流水线

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
