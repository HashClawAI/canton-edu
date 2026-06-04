---
title: "升级兼容性"
slug: "appdev-modules-m6-upgrade-compatibility"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-upgrade-compatibility.md"
source_title: "Upgrade Compatibility"
tags:
  - appdev
  - modules
  - m6-upgrade-compatibility
---

# 升级兼容性

> Daml 智能合约升级中允许的变更、破坏性变更与兼容性规则

SCU 对 Daml 模型的哪些变更可向后兼容有严格规定。Daml 编译器在构建时强制执行——若 v2 相对 v1 引入破坏性变更，`dpm build` 会拒绝。

## 向后兼容的变更

### 添加 Optional 字段

可向合约、choice 参数及 choice 返回类型添加 `Optional` 字段。

当组件 fetch 由旧版创建的合约时，新引入的 `Optional` 字段默认为 `None`，保证模板演进后旧合约仍可读。

当引用旧版的 Daml 代码 fetch 新版创建的合约时，仅当所有未知字段均为 `None` 时 fetch 才成功。若有未知字段非 `None`，fetch 失败，防止 archive-and-recreate 等工作流意外丢数据。

<Note>
  向 choice 返回类型添加 `Optional` 字段时，返回类型必须是 Daml record（不能是标量、元组、列表、集合或映射）。设计初期就让 choice 使用 record 返回类型，便于日后扩展返回字段。
</Note>

### 向 variant 添加新构造子

可向 variant（含枚举）添加新构造子。在期望旧版的代码中使用新构造子会失败，与将新 `Optional` 设为非 `None` 时旧代码失败类似。

### 添加新 choice

要使 v2 的新 choice 在既有 v1 活跃合约上可用，该合约所有 stakeholder 的 validator 必须已上传并 vet v2 DAR。新 choice 须通过 mediator 共识层，要求所有 stakeholder validator 识别 v2 包。非 stakeholder 的 validator 是否上传 v2 不影响该合约 stakeholder 能否使用新 choice。

### 修改既有 choice

可更新 controller、observer 与 choice 体以修 bug 或处理新参数。不能删除既有 choice——编译器视为破坏性变更并拒绝，因既有代码可能引用这些 choice。要废弃 choice，将其体替换为 `abort "Deprecated."`。

### 更新 signatory、observer 与 ensure

可更新确定 signatory、observer 及 `ensure` 的代码，但有限制。对既有合约，计算出的 signatory 与 observer 必须不变。fetch 或 exercise 时 Daml 用最新代码重算并与原值比较；不匹配则交易 abort。

对既有合约 fetch 或 exercise 时，`ensure` 也会重算并重新求值。

### 添加 interface 定义与实例

可向模板添加新 interface 实例，但不能删除既有实例。已部署的 interface 定义不可更改——应将 interface 放在仅含 interface、不含模板的独立包中。

可通过让 interface choice 求值为 `error "No longer implemented."` 使其不可操作。

### 添加与废弃模板

可自由添加新模板。不能删除既有模板，但可通过：

* 从其他 Daml 代码中移除引用
* 添加 `ensure False` 使其不可操作（阻止新合约创建与 choice exercise，含隐式 `Archive`）

<Warning>
  添加 `ensure False` 会使账本上既有合约无法归档。仅在通过自动化或正常业务操作归档该模板创建的所有活跃合约后再添加 `ensure False`。
</Warning>

## 破坏性变更

以下变更**不**向后兼容，编译器会拒绝：

* 从模板或 choice 删除字段
* 更改既有字段类型
* 从模板删除 choice
* 完全删除模板
* 从 variant 删除构造子
* 从模板删除 interface 实例
* 更改 interface 定义

若必须做破坏性变更，用期望结构创建新模板，并在旧模板上添加 `Upgrade` choice，归档旧合约并创建新合约。详见 [SCU 兼容性规则](/zh/docs/canton/appdev-modules-m6-writing-first-upgrade#step-3-verify-compatibility)。

## 后端兼容性

必须使用符号包引用而非包 ID。账本读取形式为 `#package-name:module-name:template-id`，以获取 `package-name` 任意版本中 `module-name` 与 `template-id` 对应模板的所有合约实例。

较新版本可能引入早期版本不存在的 `Optional` 字段，后端须处理字段缺失。Daml SDK 代码生成会自动将缺失的 `Optional` 设为 `None`。

## 包命名

避免包名冲突，尤其不同应用提供方发布的包。遵循 Java 生态惯例，用提供方反向 DNS 作为包名前缀。例如 Acme Inc. 货币市场基金发行工作流推荐 `daml.yaml`：`name: com-acme-money-market-fund-issuance`。

## 编译器版本考量

Daml 编译器在构建时验证 v1 与 v2 的升级兼容性。若构建 v1 与创建 v2 之间编译器版本变化，编译器需要已编译的 v1 DAR 才能做兼容性检查。v2 通过 `daml.yaml` 的 `upgrades` 字段指向 v1 DAR。只要 v1 DAR 可用，较新编译器即可验证升级，即使 v1 源码已无法用当前编译器编译。

## 下一步

* [Writing Your First Upgrade](/zh/docs/canton/appdev-modules-m6-writing-first-upgrade) — 创建 v2 包的分步教程
* [Package Selection](/zh/docs/canton/appdev-modules-m6-package-selection) — 账本如何解析包版本

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
