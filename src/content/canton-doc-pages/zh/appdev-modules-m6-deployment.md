---
title: "升级部署"
slug: "appdev-modules-m6-deployment"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-deployment.md"
source_title: "Upgrade Deployment"
tags:
  - appdev
  - modules
  - m6-deployment
---

# 升级部署

> 跨环境部署 Daml 包升级：协调、回滚与迁移策略

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
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — 通用环境推广策略

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
