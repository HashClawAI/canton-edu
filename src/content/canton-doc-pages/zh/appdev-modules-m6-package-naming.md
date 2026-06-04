---
title: "包命名"
slug: "appdev-modules-m6-package-naming"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-package-naming.md"
source_title: "Package Naming"
tags:
  - appdev
  - modules
  - m6-package-naming
---

# 包命名

> Daml 智能合约升级的命名惯例与包结构

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

版本标记指**合约模型版本**，非构建版本。仅在做需新包的破坏性变更时递增（见 [升级限制](/zh/docs/canton/appdev-modules-m6-limitations)）。非破坏性升级（添加可选字段、新 choice）在同一包名内由 SCU 透明处理。

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

* [Upgrade Limitations](/zh/docs/canton/appdev-modules-m6-limitations) — 驱动包命名决策的约束
* [Upgrade Compatibility](/zh/docs/canton/appdev-modules-m6-upgrade-compatibility) — 破坏性 vs 非破坏性变更规则
* [Building and Packaging](/zh/docs/canton/appdev-modules-m3-building-packaging) — 用 `dpm build` 编译打包

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
