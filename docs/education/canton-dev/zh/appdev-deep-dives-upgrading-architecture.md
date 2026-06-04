---
title: "升级架构考量"
slug: "appdev-deep-dives-upgrading-architecture"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/upgrading-architecture.md"
source_title: "Architectural Considerations for Upgrading"
tags:
  - appdev
  - deep-dives
  - upgrading-architecture
---

# 升级架构考量

> 升级 Canton Network 应用时的架构考量

升级 Canton Network 应用即部署组件新版本以修改或引入工作流。升级须保证**数据连续性**：应用状态与进行中的多步工作流（指账本上已稳定、尚未完成的工作流，非单笔交易）在升级后仍可访问并继续推进。

本文提供：推荐升级路径概览、关键挑战、向后兼容方法、测试与回滚策略；并与技术解决方案架构师认证路径中的 *Upgrading Daml Applications* 课程交叉引用。

实践中前端、后端与 Daml 模型演进节奏不同，前后端常快于 Daml。前后端应声明兼容所需的 DAR 最低版本。下文用 v1 表示当前部署组件，v2 表示升级引入组件。

## 1. 推荐做法

### 异步 rollout + 同步切换

1. **异步 rollout**：提供方实现并测试 v2；向用户开放 v2；各方异步升级前后端并审计 DAR。前后端应同时支持 v1/v2 工作流，允许各方按自身节奏部署，预期存在混部直至全员切换。切到 v2 可能还需将账本合约从 v1 迁移到 v2。

2. **同步切换**：提供方公布用户完成升级并下线 v1 的目标日期；临近日期时各方协调将 v2 DAR 部署到 participant 节点，使新工作流自目标日起在账本上同步。

### 未协调切换的风险

未协调切换到 v2 会导致命令提交失败、工作流卡住，例如：某利益相关方 participant 缺少 v2 Daml 模型；显式披露使用 v2 合约但提交方 participant 未上传 v2 模型（即便披露合约各方已上传 v2）。

## 2. 挑战

* **异步 rollout** — 提供方与用户往往无法同时升级；须支持各方独立排期。
* **混部** — 异步 rollout 期间须临时跨组织支持 v1/v2 混部，前后端与旧版 DAR 工作流保持向后兼容。
* **零停机** — 部分工作流须 7×24 推进；结合推荐做法与智能合约升级（SCU）等措施。

升级应精心规划。短期工作流可先跑完再切换；新实例应一律用新版本启动。

## 3. 向后兼容

### Daml 模型的向后兼容变更（自 Daml 2.9 / SCU）

#### 添加 `Optional` 字段

可在合约、choice 参数与返回类型末尾添加 `Optional` 字段：

* **场景 1（读旧版）**：v2 客户端 fetch v1 创建的合约时，新 `Optional` 字段默认为 `None`（仅在 Daml 执行内，非 Ledger API/PQS/客户端库层）。

* **场景 2（防数据丢失）**：旧版 Daml 代码 fetch 新版合约时，仅当所有未知字段均为 `None` 才成功；否则失败，防止 archive-and-recreate 等流程静默丢字段。

#### Choice 返回类型用 Daml Record

为 choice 返回类型添加 `Optional` 时，返回类型须为 Daml record，而非标量或 tuple/list 等。

#### 为 Variant/Enum 添加构造子

可添加新构造子；在旧版中使用新构造子会失败，与带非 `None` 值的新 `Optional` 字段降级失败类似。

#### 添加新 Choice

各方 participant 上传 v2 DAR 后，v1 创建的活跃合约可使用 v2 新 choice。

#### 修改既有 Choice

可更新 controller、observer 与 choice 体；不能删除 choice，可用 `abort` 使其失效。

#### 更新 signatory、observer 与 `ensure`

可更新计算逻辑，但对既有合约，重算的 signatory/observer 须与原始一致，否则交易 abort；`ensure` 在 fetch/exercise 时也会重算。

#### 接口

接口定义部署后不可改，应放在仅含接口的独立包。可添加新接口实例，不能删除；可用 `error` 使 choice 不可用。

#### 添加与废弃模板

可添加新模板；不能删除旧模板，可通过移除引用、`ensure False` 废弃（注意会留下无法 archive 的合约，宜先 archive 再 `ensure False`）。

### 后端向后兼容

Ledger 读取使用符号化包引用 `#package-name:module:template`，以兼容 v1 创建的合约。SDK codegen 会将缺失的 `Optional` 字段设为 `None`。

### 管理不兼容变更

对既有 API 仅允许向后兼容变更；不兼容变更通过**新**模板与 choice 引入。可在旧模板上添加消费性 `Upgrade` choice：archive 旧合约并创建新模板实例；必要时由后端自动化迁移。

### 避免包名冲突

遵循 Java 生态惯例，包名加应用提供方反向 DNS 前缀，如 `com-acme-money-market-fund-issuance`。

## 4. 包 vetting、测试与回滚

### 包 Vetting

默认上传 DAR 后 participant 自动 vet 并在同步器公布；未 vet 的包不可用。

### 取消 Vetting

上传并 vet v2 后可 unvet v1；**须先**完成全部 v1 合约升级。

### 测试

* **类型级**：在全新 participant 上同时上传新旧 DAR。
* **工作流级**：v2 软件 + v1 DAR 启动核心工作流 → 上传 v2 DAR → 后端切 v2 → 验证可继续。

### 回滚

* **Unvet v2** — 未改既有模板/choice 类型时适用。
* **Roll-forward** — 已有合约使用新字段时，发布含 `Downgrade` choice 的新版本并由后端遍历 ACS。

## 5. 要点

保证数据连续性、最小化停机、分布式兼容；异步 rollout + 同步切换；遵循 Daml/后端向后兼容；充分测试并掌握 unvet 或 roll-forward 回滚。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
