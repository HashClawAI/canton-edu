---
title: "包选择"
slug: "appdev-modules-m6-package-selection"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-package-selection.md"
source_title: "Package Selection"
tags:
  - appdev
  - modules
  - m6-package-selection
---

# 包选择

> 多版本包共存时 Canton 账本如何解析使用哪个包版本

多个包版本上传到 validator 后，需要规则决定执行哪个版本。包选择决定这一点——当 v1 与 v2 均可用时，Daml 运行时如何解析模板与 choice。

## 版本解析如何工作

账本上每个合约关联创建它的包版本。获取或行使合约时，运行时使用你代码引用的包版本，不一定是创建合约的版本。

解析遵循：

* **创建合约** — 运行时使用你代码引用的包版本。若后端导入 v2，新合约用 v2 创建。
* **获取合约** — 运行时用你代码引用的版本评估合约数据。fetch 是否成功由 SCU 与 vetting 规则决定（见 [升级兼容性](/zh/docs/canton/appdev-modules-m6-upgrade-compatibility)）。
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

* [Testing Upgrades](/zh/docs/canton/appdev-modules-m6-testing-upgrades) — 验证升级的版本解析是否正确
* [Deploying Upgrades](/zh/docs/canton/appdev-modules-m6-deployment) — 跨 validator 协调包上传

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
