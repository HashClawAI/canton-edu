---
title: "编写你的第一个升级"
slug: "appdev-modules-m6-writing-first-upgrade"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-writing-first-upgrade.md"
source_title: "Writing Your First Upgrade"
tags:
  - appdev
  - modules
  - m6-writing-first-upgrade
---

# 编写你的第一个升级

> 创建含向后兼容变更的 v2 Daml 包的分步教程

本教程带你创建 Daml 包的 v2：从简单模板开始，添加可选字段与新 choice，验证升级可编译且既有合约与新代码协同工作。

## 前置条件

* 已安装可用的 `dpm` 与 Daml SDK
* 熟悉 Daml 模板与 choice（[模块 3](/appdev/modules/m3-contract-templates)）
* 文本编辑器或 Daml Studio

## 步骤 1：创建 v1 包

`dpm new` 可脚手架项目：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm new com-example-licensing
```

本教程为清晰起见手动建目录：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
mkdir -p daml/v1/daml
```

创建 `daml/v1/daml.yaml`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v1/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 1.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
```

创建 `daml/v1/daml/Main.daml`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v1/daml/Main.daml
module Main where

data LicenseInfo = LicenseInfo
  with
    holder : Party
    issuer : Party
    product : Text
  deriving (Eq, Show)

template License
  with
    info : LicenseInfo
  where
    signatory info.issuer
    observer info.holder

    choice Revoke : ()
      controller info.issuer
      do pure ()
```

构建并验证：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v1
dpm build
```

<Note>
  SDK 也可用 `dpm new upgrade-demo --template upgrades-example` 生成内置升级示例。详见[示例源码](https://github.com/digital-asset/daml/tree/main/sdk/docs/source/sdk/sdlc-howtos/smart-contracts/upgrade/example)。
</Note>

## 步骤 2：创建 v2 包

复制包（`cp -r v1 v2`）并提升版本。包名必须相同——Daml 据此识别为升级：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v2/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 2.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
upgrades: ../v1/.daml/dist/com-example-licensing-1.0.0.dar
```

`upgrades` 指向 v1 DAR，告知 `dpm build` 验证 v2 为 v1 的兼容升级。

进行向后兼容变更：向 record 添加 `Optional` 字段，向模板添加新 choice：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v2/daml/Main.daml
module Main where

data LicenseInfo = LicenseInfo
  with
    holder : Party
    issuer : Party
    product : Text
    expiryDate : Optional Time  -- NEW: optional expiry date
  deriving (Eq, Show)

template License
  with
    info : LicenseInfo
  where
    signatory info.issuer
    observer info.holder

    choice Revoke : ()
      controller info.issuer
      do pure ()

    -- NEW: choice to renew the license with an expiry date
    choice Renew : ContractId License
      with
        newExpiry : Time
      controller info.issuer
      do create this with
           info = info with expiryDate = Some newExpiry
```

变更符合 SCU 规则：

* `expiryDate` 为 `Optional`，v1 合约隐式默认为 `None`
* `Renew` 为新 choice（v1 不存在，无向后兼容问题）

## 步骤 3：验证兼容性

构建 v2：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v2
dpm build
```

构建成功即编译器已验证 v2 为 v1 的有效升级。`daml.yaml` 中的 `upgrades` 触发此检查——无该字段时 `dpm build` 孤立编译 v2，不做跨版本验证。编译器检查所有 SCU 规则：无删字段、无改类型、新字段为 `Optional` 等。

若引入破坏性变更，编译器会报告违反的规则。

## 步骤 4：测试近似跨版本行为

在 v2 包中添加测试脚本。先在 `daml/v2/daml.yaml` 加入 `daml-script` 依赖：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml/v2/daml.yaml
sdk-version: 3.4.9
name: com-example-licensing
version: 2.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
  - daml-script
upgrades: ../v1/.daml/dist/com-example-licensing-1.0.0.dar
```

创建测试脚本，模拟 v1 合约（`expiryDate = None`）并行使 v2 的 `Renew`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- daml/v2/daml/UpgradeTest.daml
module UpgradeTest where

import Main
import Daml.Script
import DA.Date (Month(..), datetime)

testUpgradePath : Script ()
testUpgradePath = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  -- Create a contract with no expiryDate (simulating a v1 contract)
  licenseCid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder
        issuer
        product = "Widget Pro"
        expiryDate = None

  -- Exercise the new v2 Renew choice
  newLicenseCid <- submit issuer do
    exerciseCmd licenseCid Renew with
      newExpiry = datetime 2026 Dec 31 0 0 0

  -- Verify the renewed license has the expiry set
  Some renewed <- queryContractId holder newLicenseCid
  assertMsg "Should have expiry"
    (renewed.info.expiryDate == Some (datetime 2026 Dec 31 0 0 0))
```

在 v2 目录运行：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd daml/v2
dpm test
```

<Note>
  此测试在单一包版本内运行，近似而非完全复现跨版本行为。真实账本上同时上传 v1、v2 DAR 时，运行时处理实际 v1 合约与 v2 代码间的版本解析。真实跨版本策略见 [Testing Upgrades](/appdev/modules/m6-testing-upgrades)。
</Note>

## 步骤 5：部署两个版本

真实部署中两个 DAR 可能都上传到 validator。顺序重要：先上传 v1（若尚未上传），再 v2。新 validator 若 v2 与 v1 SCU 兼容，可只上传 v2。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Upload v1 (if not already on the ledger)
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @daml/v1/.daml/dist/com-example-licensing-1.0.0.dar

# Upload v2
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @daml/v2/.daml/dist/com-example-licensing-2.0.0.dar
```

v2 在所有 stakeholder validator 上上传并 vet 后，新 choice 在既有 v1 合约上可用。

## 底层机制

validator 收到 v2 DAR 时：

1. 若启用自动 vetting，validator 与 v1 一并 vet 新包；否则须手动 vet。
2. 两包均保持活跃——v1 合约不受影响。
3. v2 代码 fetch v1 合约时，运行时将 `Optional` 填为 `None`。
4. v1 代码 fetch v2 合约且 `Optional` 均为 `None` 时，fetch 成功（字段被忽略）。
5. v1 代码 fetch 的 v2 合约中某 `Optional` 非 `None` 时，fetch 失败以防数据丢失。

该设计保证混合版本安全：无静默丢数据，不兼容交互显式失败而非破坏状态。

运行时版本解析见 [Package Selection](/appdev/modules/m6-package-selection)。

## 下一步

* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — 允许与禁止变更完整参考
* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — 全面升级测试策略
* [Deploying Upgrades](/appdev/modules/m6-deployment) — 跨环境 rollout 升级

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
