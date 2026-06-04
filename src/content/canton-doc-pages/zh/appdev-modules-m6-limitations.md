---
title: "升级限制"
slug: "appdev-modules-m6-limitations"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-limitations.md"
source_title: "Upgrade Limitations"
tags:
  - appdev
  - modules
  - m6-limitations
---

# 升级限制

> Daml 智能合约升级的已知限制与约束

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

* [Upgrade Compatibility](/zh/docs/canton/appdev-modules-m6-upgrade-compatibility) — SCU 完整兼容规则
* [Package Naming](/zh/docs/canton/appdev-modules-m6-package-naming) — 考虑破坏性变更的命名惯例
* [Smart Contract Upgrades in Production](/zh/docs/canton/appdev-modules-m7-smart-contract-upgrades) — 推广运维考量

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
