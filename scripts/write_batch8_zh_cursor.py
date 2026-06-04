#!/usr/bin/env python3
"""Write batch 8 zh-cursor JSON payloads."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs/education/canton-dev/zh-cursor"

PAYLOADS = {
    "appdev-modules-m6-testing-upgrades": {
        "zhTitle": "测试升级",
        "summary": "验证升级兼容性、跨版本工作流测试与回归策略；含类型级/工作流级测试、Daml Script 模式与 CI 集成。",
        "body": """> 验证升级兼容性、测试跨版本工作流及回归测试策略

在分布式网络上升级 Daml 包容不得猜测。你需要同时验证编译器接受该升级，以及混合包版本下工作流仍能正常运行。

## 类型级兼容性测试

类型级兼容性测试检查同名包的旧版与新版能否共存而不破坏结构。开发期最简便的方式是使用 `dpm upgrade-check`。

也建议在 CI 中执行：将生产将使用的旧版与新版 DAR 上传到全新的 participant 节点。理想情况下 DAR 存放在专用制品库；因其体积通常小于 1 MB，也可纳入源码管理。

实践中 CI 流水线应：

1. 用 `dpm build` 构建 v2 DAR
2. 用 `dpm sandbox` 启动 sandbox
3. 上传生产 v1 DAR
4. 上传 v2 DAR
5. 若两次上传均无错误，则类型级兼容性成立

## 工作流级兼容性测试

工作流级兼容性测试验证升级后核心业务流程仍正确。基础集成测试步骤：

1. 以 v2 软件启动应用，但仅上传 v1 DAR，测试向后兼容。
2. 初始化应用并启动每个核心工作流的一次实例。
3. 上传 v2 DAR。
4. 更新配置，指示后端开始使用 v2 DAR。
5. 验证工作流仍处于正确状态且可继续无问题运行。

更复杂的升级可能需要额外测试。

## Daml Script 升级测试

编写显式测试跨版本场景的 Daml Script。应覆盖的关键模式：

### 用 v1 创建合约，用 v2 读取

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testV1ContractWithV2Code : Script ()
testV1ContractWithV2Code = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  -- Create with v1 fields only
  cid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder; issuer
        product = "Widget"
        expiryDate = None  -- v2 field, set to None

  -- Fetch and verify v2 fields default correctly
  Some license <- queryContractId issuer cid
  assertMsg "expiryDate should be None" (license.info.expiryDate == None)
```

### 在既有合约上行使 v2 choice

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testNewChoiceOnExistingContract : Script ()
testNewChoiceOnExistingContract = do
  issuer <- allocateParty "Issuer"
  holder <- allocateParty "Holder"

  cid <- submit issuer do
    createCmd License with
      info = LicenseInfo with
        holder; issuer
        product = "Widget"
        expiryDate = None

  -- Exercise the new v2 choice
  newCid <- submit issuer do
    exerciseCmd cid Renew with
      newExpiry = datetime 2026 Dec 31 0 0 0

  -- Verify result
  Some renewed <- queryContractId issuer newCid
  assertMsg "Should have expiry set"
    (renewed.info.expiryDate == Some (datetime 2026 Dec 31 0 0 0))
```

### 测试不兼容的降级

真正的跨版本降级测试需在 sandbox 上传 v1 与 v2 两个 DAR，并在版本边界上操作合约。单个 Daml Script 测试无法完成，因为 Daml Script 在单一包版本内运行。请采用上文工作流级方法：在 sandbox 上传两个 DAR，用 v2 数据创建合约（非 `None` 的可选字段），再验证 v1 代码按预期无法 fetch。

## 回归测试

每次升级都应对新包版本运行完整既有测试套件。v1 测试在 v2 上应原样通过——否则存在向后兼容问题。

将测试包结构化为回归测试与升级专项测试分离：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml/
├── v1/              # Production v1
├── v2/              # Production v2
└── test/
    ├── regression/  # Existing tests, run against v2
    └── upgrade/     # New tests for cross-version scenarios
```

## CI 集成

在标准构建与测试之后，将升级测试作为独立 CI 阶段：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Standard build and test
dpm build
dpm test

# Upgrade compatibility
dpm sandbox &
SANDBOX_PID=$!

# Wait for sandbox to be ready (use a health check loop in production CI)
sleep 30

# Upload production v1 DAR
curl -X POST "http://localhost:7575/v2/packages" \\
  -H "Content-Type: application/octet-stream" \\
  --data-binary @artifacts/v1.dar

# Upload v2 DAR — if this succeeds, type-level compatibility is confirmed
curl -X POST "http://localhost:7575/v2/packages" \\
  -H "Content-Type: application/octet-stream" \\
  --data-binary @artifacts/v2.dar

# Run your project's upgrade test suite here

kill $SANDBOX_PID
```

## 下一步

* [Deploying Upgrades](/appdev/modules/m6-deployment) — 在多环境 rollout 已测试的升级
* [Upgrade Compatibility](/appdev/modules/m6-upgrade-compatibility) — 允许变更的参考""",
    },
    "appdev-modules-m6-upgrade-compatibility": {
        "zhTitle": "升级兼容性",
        "summary": "SCU 允许的向后兼容变更、破坏性变更规则，以及后端符号包引用与包命名约定。",
        "body": """> Daml 智能合约升级中允许的变更、破坏性变更与兼容性规则

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

若必须做破坏性变更，用期望结构创建新模板，并在旧模板上添加 `Upgrade` choice，归档旧合约并创建新合约。详见 [SCU 兼容性规则](/appdev/modules/m6-writing-first-upgrade#step-3-verify-compatibility)。

## 后端兼容性

必须使用符号包引用而非包 ID。账本读取形式为 `#package-name:module-name:template-id`，以获取 `package-name` 任意版本中 `module-name` 与 `template-id` 对应模板的所有合约实例。

较新版本可能引入早期版本不存在的 `Optional` 字段，后端须处理字段缺失。Daml SDK 代码生成会自动将缺失的 `Optional` 设为 `None`。

## 包命名

避免包名冲突，尤其不同应用提供方发布的包。遵循 Java 生态惯例，用提供方反向 DNS 作为包名前缀。例如 Acme Inc. 货币市场基金发行工作流推荐 `daml.yaml`：`name: com-acme-money-market-fund-issuance`。

## 编译器版本考量

Daml 编译器在构建时验证 v1 与 v2 的升级兼容性。若构建 v1 与创建 v2 之间编译器版本变化，编译器需要已编译的 v1 DAR 才能做兼容性检查。v2 通过 `daml.yaml` 的 `upgrades` 字段指向 v1 DAR。只要 v1 DAR 可用，较新编译器即可验证升级，即使 v1 源码已无法用当前编译器编译。

## 下一步

* [Writing Your First Upgrade](/appdev/modules/m6-writing-first-upgrade) — 创建 v2 包的分步教程
* [Package Selection](/appdev/modules/m6-package-selection) — 账本如何解析包版本""",
    },
    "appdev-modules-m6-writing-first-upgrade": {
        "zhTitle": "编写你的第一个升级",
        "summary": "分步教程：从 v1 许可模板出发，添加 Optional 字段与新 choice，验证 SCU 兼容并模拟跨版本行为。",
        "body": """> 创建含向后兼容变更的 v2 Daml 包的分步教程

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
curl -X POST "http://localhost:7575/v2/packages" \\
  -H "Content-Type: application/octet-stream" \\
  --data-binary @daml/v1/.daml/dist/com-example-licensing-1.0.0.dar

# Upload v2
curl -X POST "http://localhost:7575/v2/packages" \\
  -H "Content-Type: application/octet-stream" \\
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
* [Deploying Upgrades](/appdev/modules/m6-deployment) — 跨环境 rollout 升级""",
    },
    "appdev-modules-m7-canton-coin-preapprovals": {
        "zhTitle": "Canton Coin 预批准",
        "summary": "TransferPreapproval 如何启用预批准的 Canton Coin 转入、费用与有效期、设置/续期/撤销及通过预批准转账。",
        "body": """> TransferPreapproval 合约如何启用预批准的 Canton Coin 转账

与 Eth、Bitcoin 等资产不同，Canton Coin 要求 party 显式同意持有 Canton Coin，包括对每笔入账转账的显式同意。

愿意接受任意发送方转入 Canton Coin 的 party 可设置 `TransferPreapproval`，允许任何 party 向该 party 发送 Canton Coin。注意这仅适用于 Canton Coin 转账，不适用于其他资产；其他资产可能有各自的预批准机制，或需逐笔批准入账。

为避免 super validator 为不再活跃的 party 存储并提供 `TransferPreapproval`，并防止恶意 party 滥发，预批准有有效期，创建时须按有效期比例销毁费用。费用由 super validator 通过 `transferPreapprovalFee` 参数控制。当前值可在 CC Scan 查看（选择对应网络）：

* DevNet: [https://scan.sv-1.dev.global.canton.network.sync.global/dso](https://scan.sv-1.dev.global.canton.network.sync.global/dso)
* TestNet: [https://scan.sv-1.test.global.canton.network.sync.global/dso](https://scan.sv-1.test.global.canton.network.sync.global/dso)
* MainNet: [https://scan.sv-1.global.canton.network.sync.global/dso](https://scan.sv-1.global.canton.network.sync.global/dso)

当前默认约为每年 1 美元。

每个预批准有两个 party：`receiver` 批准入账，`provider` 负责付费并在临近到期时续期。作为回报，`provider` 将成为使用该预批准的所有入账转账的应用提供方并获得应用奖励。`provider` 不必与 `receiver` 托管在同一节点，但实践中常见如此。

## 设置预批准

未使用外部签名的 party 可在 splice 钱包 UI 中，通过登出按钮旁的按钮创建预批准：

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/preapproval_button.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=feabdf575485595c7c0aa26911e133dd" width="600" alt="Button to create preapproval" data-path="images/splice/preapproval_button.png" />

使用外部签名时，常见做法由 validator 运营方创建 `ExternalPartySetupProposal` 合约，外部 party 签署行使 `ExternalPartySetupProposal_Accept` 的交易。这会同时创建外部 party 的 validator 奖励铸造所需的 `ValidatorRight` 合约，以及 provider 设为 validator 运营方 party 的 `TransferPreapproval`。validator 暴露 `/v0/admin/external-party/setup-proposal` 创建提案，以及 `/v0/admin/external-party/setup-proposal/prepare-accept` 与 `submit-accept` 供外部 party 准备并提交签名接受。详见 API 文档。若 provider 需不同设置，可能需自建 Daml 设置合约并通过 Ledger API 创建，而非使用 validator API。

注意将 provider 设为 validator 运营方时的 party 数量限制。

validator API 创建的预批准到期日为未来 90 天。

## 到期与续期

如上，预批准总有到期日。到期且未续期则不能再用于转账，super validator 运行的自动化最终会归档该合约。

provider 为 validator 运营方 party 的预批准，在距到期不足 30 天时由 validator 应用自动化续期 90 天。

若 provider 为其他 party，需自行实现定期行使 `TransferPreapproval_Renew` 的续期自动化。

## 撤销预批准

`receiver` 与 `provider` 均可通过 `TransferPreapproval_Cancel` 撤销。

splice 钱包 UI 目前不支持；provider 为 validator 运营方时，运营方可对 `/v0/admin/transfer-preapprovals/by-party/{receiver-party}` 发 `DELETE`。详见 API 文档。

## 通过预批准转账

若收款方已设预批准，splice 钱包 UI 转账时会默认使用。

若通过 API（尤其外部 party），推荐用 Token Standard API，会在可能时使用预批准。用法见 [CIP](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 与 [token standard reference CLI](https://github.com/canton-network/splice/blob/main/token-standard/cli/src/commands/transfer.ts)。

亦可使用 validator 上非标准 Canton Coin 转账的遗留外部签名 API：`/v0/admin/external-party/transfer-preapproval/prepare-send` 与 `submit-send`。详见 API 文档。""",
    },
    "appdev-modules-m7-compliance": {
        "zhTitle": "合规考量",
        "summary": "Canton 应用的隐私、审计与监管相关技术特性：子交易隐私、PQS 审计、数据驻留、不可变账本与 GDPR 等设计指引。",
        "body": """> Canton 应用的隐私、审计与监管相关考量

Canton 架构在隐私与审计方面与公链有本质差异。本文汇总在 Canton Network 上构建应用时需了解的合规相关技术特性。

<Warning>
  本文提供 Canton 能力的技术事实，不构成法律意见。请就所在司法辖区的监管合规咨询合格法律顾问。
</Warning>

## 隐私特性

### 子交易隐私

Canton 不会向所有 validator 广播完整交易。每笔交易分解为**视图**，各 validator 仅接收与其托管 party 相关的视图。非某部分 stakeholder 的 validator 看不到该部分——无载荷、无参与 party，甚至不知其存在。

因此：

* 合约数据仅对 Daml 模板定义的 signatory、observer 与 controller 可见
* Synchronizer（sequencer 与 mediator）处理加密消息，不见明文交易数据
* Validator 仅存储涉及其托管 party 的合约与交易

可见性规则详见 [Privacy Model Explained](/overview/learn/privacy-model)。

### 无全局状态可见性

与任何参与者可读全账本不同，Canton validator 维护私有本地账本分片。无共享的全合约数据库。Party 无法查询无权查看的合约，validator 也无法访问未托管 party 的数据。

## 审计能力

### Ledger API 交易历史

各 validator 维护其托管 party 相关交易的完整只追加历史。应用可通过 Ledger API 更新流读取按时间顺序的合约创建、choice exercise 与归档记录。

### PQS 历史查询

Participant Query Store（PQS）维护镜像账本状态的 PostgreSQL 数据库，保存当前活跃合约集与完整合约事件历史，适合审计查询：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Find all archived contracts of a given template, with timestamps
SELECT contract_id, payload, created_at, archived_at
FROM contracts('your-module:YourTemplate')
WHERE archived_at IS NOT NULL
ORDER BY archived_at DESC;
```

PQS 数据保留取决于底层 PostgreSQL 维护策略，由你控制保留策略。

### Daml 中的审计方模式

可在智能合约层将审计 party 加为 observer，审计方可见合约及影响它的所有事件但不可修改。代码示例见 [Privacy Model](/overview/learn/privacy-model)。

## 数据驻留

### 私有 Synchronizer

若监管要求数据留在特定地理区域，可在你选择的司法辖区内运营**私有 synchronizer**。连接私有 synchronizer 的 validator 仅通过你控制的该基础设施通信。

Validator 可同时连接 Global Synchronizer（跨网络互操作）与一个或多个私有 synchronizer（辖区专属工作流）。多 synchronizer 架构可在不为此每种工作流单独建全套基础设施的情况下，将受监管工作流与公开工作流分离。

### Validator 级数据控制

Validator 仅存储托管 party 的数据，组织数据位于自有 validator 基础设施。你可选择部署位置——本地、特定云区域或多地。除非另一 validator 托管共享合约的 stakeholder party，否则其他 validator 不持有你的数据副本。

## 不可变账本与数据修改请求

Canton 账本只追加。合约就地修改，而是归档并替换。交易历史不可重写。

对要求修改或删除数据的法规（如 GDPR 删除权），可考虑：

* **合约设计** — 将个人身份信息（PII）存于链下，账本上仅保留不透明 ID 引用。删除链下数据可使链上引用失效。
* **PQS 数据管理** — PQS 是你控制的投影，可在不影响账本的情况下清除或匿名化 PQS 记录。
* **修剪（Pruning）** — Canton 支持账本修剪，在可配置保留期后从 validator 本地存储删除旧交易数据，修剪后无法通过 Ledger API 访问。

以上为技术机制。是否满足具体监管要求取决于法规与法律顾问解释。

## 应用设计指南

* 在合约层用 Daml signatory/observer 强制执行可见性，而非仅在应用层
* 需审计轨迹的合约将审计 party 加为 observer
* 敏感 PII 存链下，账本上仅 ID 引用
* 严格数据驻留要求的工作流使用私有 synchronizer
* 按监管义务配置账本修剪保留期

## 延伸阅读

* [Privacy Model Explained](/overview/learn/privacy-model) — 子交易隐私详情
* [Security Best Practices](/appdev/modules/m7-security) — 保护 Canton 应用
* [Architecture Overview](/overview/learn/architecture) — Validator 与 synchronizer 关系""",
    },
    "appdev-modules-m7-error-handling": {
        "zhTitle": "错误处理",
        "summary": "Canton 应用中的命令拒绝、争用、超时、流量不足及幂等提交、完成流监控与后端恢复模式。",
        "body": """> Canton 应用的错误处理与恢复模式

Canton 应用面向分布式、多方账本。错误分不同类别，每类需不同恢复策略。本文涵盖常见错误类型及后端处理方式。

## 错误类别

### 命令拒绝

命令在到达 synchronizer 前被 Ledger API 拒绝。常见原因：

* **INVALID_ARGUMENT** — 载荷与模板或 choice 签名不匹配（字段类型错误、缺必填字段）
* **NOT_FOUND** — 引用的 contract ID 不存在或对提交 party 不可见
* **PERMISSION_DENIED** — 已认证 party 无权执行该操作

此类错误通常表示应用逻辑 bug 或陈旧数据。重试相同命令结果相同。应修复根因：更正载荷、重新查询有效 contract ID 或检查 party 授权。

### 争用（Contention）

两个或多个命令同时试图消费同一合约时发生争用。仅一个成功，其余收到 **FAILED_PRECONDITION**（或 `ABORTED`），表示合约已被归档。

多方应用中这很正常。两用户可能几乎同时对同一合约行使同一 choice。Canton 一致性模型保证仅一个成功。

### 超时

若 synchronizer 在配置截止时间内未处理命令，`StatusRuntimeException` 可能为 `DEADLINE_EXCEEDED`。网络拥塞或对手方 validator 响应慢时会出现。

超时**不**意味着命令失败。可能已成功但响应未及时返回。重试前请查完成流或 PQS 确认命令是否已应用。

### 流量不足

Validator 流量预算耗尽时，提交失败并提示流量不足。这不是瞬时错误——在预算补充（手动或自动充值）前重试无效。

流量额度管理见 [Canton Coin and Traffic](/appdev/modules/m4-canton-coin)。

## 处理争用

消费型合约上的争用是 Canton 应用最常见错误模式。标准做法：

1. **捕获错误** — 在 gRPC 响应中识别 `FAILED_PRECONDITION` 或 `ABORTED`
2. **重读合约** — 用 PQS 查当前状态。目标合约可能已归档，竞争交易可能已创建新活跃合约
3. **用新 command ID 重提交** — 针对当前合约构建新命令并以新 command ID 提交

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
int maxRetries = 3;
for (int attempt = 0; attempt < maxRetries; attempt++) {
    try {
        var contract = damlRepository.findActiveAsset(assetId).join();
        if (contract.isEmpty()) {
            throw new NotFoundException("Asset no longer active");
        }
        ledger.exerciseAndGetResult(
            contract.get().contractId, choice, UUID.randomUUID().toString()
        ).join();
        return; // success
    } catch (CompletionException e) {
        if (isContention(e) && attempt < maxRetries - 1) {
            Thread.sleep((long) Math.pow(2, attempt) * 100); // exponential backoff
            continue;
        }
        throw e;
    }
}
```

重试间使用指数退避，否则竞争命令会持续碰撞。

### 何时不应重试

以下情况勿重试：

* **INVALID_ARGUMENT** — 命令本身错误
* **PERMISSION_DENIED** — 重试间授权不会变
* **流量不足** — 问题是流量预算而非命令

## 幂等命令提交

Ledger API 按 command ID 去重。相同 ID 的第二次提交视为重复并返回第一次结果。

据此使后端幂等：

* 根据操作输入生成确定性 command ID（如用户 ID、操作类型与前端 nonce 的哈希）
* 网络故障未收到响应时，用相同 command ID 重提交
* Ledger API 返回原结果而非执行两次

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
String commandId = "renew-license-" + licenseNum + "-" + requestNonce;
ledger.exerciseAndGetResult(contractId, renewChoice, commandId).join();
// Safe to retry with the same commandId if the response is lost
```

去重窗口可配置。默认对多数应用足够；若操作跨很长时间，确认窗口覆盖重试时间范围。

## 完成流监控

Ledger API 完成流报告每个已提交命令的最终状态。订阅它以可靠跟踪结果：

* **成功完成** 确认交易已提交
* **失败完成** 含错误码与详情
* **预期窗口内无完成** 暗示命令在到达 synchronizer 前丢失

cn-quickstart 中同步 `CommandService`（而非 `CommandSubmissionService`）在内部等待完成并单次往返返回结果。若用异步 `CommandSubmissionService`，需自行监控完成。

## 后端恢复模式

### 启动恢复

后端重启时可能有结果未知的在途命令。启动时：

1. 从最后已知 offset 读取完成流
2. 将在途命令与完成状态对账
3. 对从未提交的命令（无完成且 PQS 无匹配合约）重试

### 熔断器

Ledger API 不可用时（validator 重启、网络分区），用熔断器包装提交逻辑。连续失败达配置次数后停止提交并向调用方返回服务不可用。定期探测 Ledger API 以检测恢复。

### 死信处理

重试耗尽仍失败的命令应记录完整上下文（command ID、模板、choice、参数、错误）并送入死信队列或表，便于审计与人工处理边缘情况。

## 延伸阅读

* [Backend Development](/appdev/modules/m4-backend-dev) — Ledger API 客户端与错误处理示例
* [Canton Coin and Traffic](/appdev/modules/m4-canton-coin) — 避免提交流量失败
* [Observability](/appdev/modules/m4-observability) — 错误追踪的日志与指标""",
    },
    "appdev-modules-m7-package-management": {
        "zhTitle": "包管理",
        "summary": "跨环境 DAR 生命周期、SDK 版本固定、依赖与制品库、向对手方分发及按 stakeholder 模块化包。",
        "body": """> 跨环境管理 DAR、版本固定、依赖管理与协调包分发

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
* [Performance](/appdev/modules/m7-performance) — Canton 应用优化策略""",
    },
    "appdev-modules-m7-performance": {
        "zhTitle": "性能最佳实践",
        "summary": "Canton 应用性能指南已整合至 Performance Optimization 深度专题；含排障链接。",
        "body": """> Canton 应用性能指南所在位置 — 已迁至统一的 Performance Optimization 深度专题

详细性能指导——链上与链下权衡、为性能设计合约、PQS 查询优化、并行命令提交、流量管理及降低争用的示例——现与其余性能材料一并位于 [Performance Optimization](/appdev/deep-dives/performance-optimization)。

诊断运行中 validator 的性能问题另见：

* 排障速查中的 [Performance Issues](/appdev/troubleshooting#performance-issues-2) 与 [Contention](/appdev/troubleshooting#contention)。

## 下一步

* [Security Best Practices](/appdev/modules/m7-security) — 授权与安全配置
* [Package Management](/appdev/modules/m7-package-management) — 高效 DAR 管理""",
    },
    "appdev-modules-m7-security": {
        "zhTitle": "安全最佳实践",
        "summary": "链上授权、Ledger API 认证与 TLS、密钥管理、安全配置及 Open Tracing、Authorization 深度专题链接。",
        "body": """> Canton 应用的授权模式、API 认证、密钥管理与安全配置

Canton 在协议层提供结构性安全保证——授权在 Daml 中声明，隐私由 synchronizer 强制执行，账本保证不可抵赖。应用开发者的任务是在链下层次不引入缺口地构建于此之上。

## 链上安全

### Signatory 与 controller 声明

Daml 授权模型是第一道防线。每个模板声明 signatory（谁须授权创建），每个 choice 声明 controller（谁可行使）。协议强制执行——API 操纵无法绕过。

设计原则：

* 为每个模板声明最少 signatory 集合
* 用 `observer` 控制谁可见合约而不赋予操作权
* 多方协议优先 propose-accept，避免一方单方面为他人创建义务
* 在创建时及每次 fetch/exercise 运行的 `ensure` 中验证业务逻辑

### 授权链

复杂工作流用委托模式而非宽泛权限。Party 可通过独立授权合约委托特定操作：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuthorizedAgent
  with
    principal : Party
    agent : Party
    scope : Text
  where
    signatory principal
    observer agent

    choice ActOnBehalf : ()
      controller agent
      do assertMsg "Action not in scope"
           (scope == "transfer")
         pure ()
```

授权显式且可审计。principal 可通过归档 `AuthorizedAgent` 撤销委托。

## Ledger API 认证

Canton validator 用基于 token 的认证（JWT）保护 Ledger API。应用须获取有效 token 并在每次 API 调用中携带。

### 后端 token 管理

* 安全存储 token——勿放在客户端代码、会出现在日志的环境变量或版本库中
* 在过期前刷新 token，避免命令失败
* 为不同组件（后端、自动化、管理工具）使用独立服务账号，限制 token 泄露影响面
* gRPC 客户端用 call credentials 配置 token；HTTP/JSON 在 participant 集成 JSON API 上使用 `Authorization: Bearer <token>` 头

### TLS 配置

生产部署须对所有 Ledger API 连接使用 TLS。用 validator CA 证书配置 gRPC 客户端：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
ManagedChannel channel = NettyChannelBuilder
    .forAddress(host, port)
    .sslContext(GrpcSslContexts.forClient()
        .trustManager(new File("ca-cert.pem"))
        .build())
    .build();
```

LocalNet 开发默认禁用 TLS。勿将此类配置带入生产。

## 密钥管理

Canton 使用加密密钥标识 party、节点身份并签署交易。按敏感度保护密钥。

### 开发 vs 生产

LocalNet 上密钥本地生成存储，适合开发。生产中：

* 对私钥使用 [HSM 或云 KMS](/global-synchronizer/production-operations/kms-operations)
* 勿将生产密钥放在开发机或 CI
* 按组织安全策略轮换密钥
* 安全备份密钥材料——丢失密钥意味着失去 party 身份访问

### Validator 密钥保护

若运营自有 validator，其签名密钥是最关键机密。拥有这些密钥者可代表你的 party 提交交易。须存放在 HSM/KMS 并限制仅 validator 运行时环境可访问。

## 安全配置

### 密钥管理

* 用密钥管理器（Vault、AWS Secrets Manager、GCP Secret Manager）存数据库凭据、API 密钥与 auth token
* 勿通过可能出现在进程列表或容器检查中的环境变量传递密钥
* 定期轮换凭据并确保应用可无停机应对轮换

### 网络隔离

* 将 validator 置于私有网段
* 仅向应用服务器暴露 Ledger API 端口
* 用防火墙或安全组限制可访问 validator Admin API 的系统
* Admin API 提供特权操作（party 管理、包上传），不应暴露给应用代码

### 系统边界输入验证

数据到达 Ledger API 前验证所有用户输入。Daml 类型与授权可防多类攻击，后端仍应：

* 验证请求中的 party 标识与已认证用户一致
* 纳入合约载荷前清理文本字段
* 限制请求载荷大小
* 对 API 端点限流防滥用

## 下一步

* [Package Management](/appdev/modules/m7-package-management) — 保护 DAR 分发与部署
* [Performance](/appdev/modules/m7-performance) — Canton 应用优化

## 高级主题

* [Open Tracing in Ledger API Client Applications](/appdev/deep-dives/open-tracing) — 为使用 Ledger API 的应用添加基于 OpenTelemetry 的分布式追踪。
* [Authorization](/appdev/deep-dives/authorization) — Ledger API 的访问 token、身份提供方、scope 与 rights。""",
    },
    "appdev-modules-m7-smart-contract-upgrades": {
        "zhTitle": "生产环境中的智能合约升级",
        "summary": "生产 SCU rollout 的运营清单：升级前检查、对手方沟通、混合版本部署、监控与回滚程序。",
        "body": """> 在生产环境 rollout 智能合约升级的运营考量

在运行中的生产环境升级智能合约不同于开发期升级。合约在多方间共享，常跨组织边界；在你 validator 上有效的升级在对手方混跑版本时可能表现不同。本文涵盖生产 SCU rollout 的运营侧。

## 升级之前

### 升级前检查清单

向生产上传新包版本前：

* 确认升级在 CI 中通过 `dpm build` 与 `dpm test`
* 确认新包与当前版本 SCU 兼容（本地或 CI 运行兼容性检查）
* 对照[升级限制](/appdev/modules/m6-limitations)审查变更列表，确保无破坏性修改
* 在 DevNet 或 TestNet 用接近真实数据量测试
* 提前与持有受影响合约的对手方沟通（见下）
* 开始前记录回滚程序

### 与对手方沟通

在 Canton Network 上，你的合约可能在其他 validator 上托管 signatory 或 observer。上传新包版本后，那些 validator 也需新包才能正确解释升级后合约。

步骤：

1. **提前通知对手方**，共享新 DAR 与变更摘要。
2. **商定 rollout 窗口**。托管受影响合约 party 的所有 validator 应在约定时段内上传新包。
3. **验证包可用性**。上传后确认所有相关 validator 识别新 package ID。

若对手方尚未上传新包而你的应用在新版本下创建合约，其 validator 无法处理，该对手方交易会失败。

## 升级期间

### 上传包

用 Admin API 或部署工具向 validator 上传新 DAR：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm deploy --target <validator-url> <dar-file>
```

上传非破坏性。旧包版本仍可用，旧版本下创建的既有合约继续工作。无需停机。

### 混合版本部署

上传新包后系统进入**混合版本状态**：部分活跃合约在旧版创建，新合约将在新版创建。

Canton 处理方式：

* **既有合约** 仍关联创建时的包版本
* **新合约** 在最新上传版本下创建
* 对旧版合约 **行使 choice** 时，若模板 SCU 兼容，使用新包的 choice 体；合约载荷按新版类型定义解释
* 新版 **新增的 Optional 字段** 在读取旧合约时使用默认值

该混合状态持续到所有旧版合约被归档（消费或显式迁移）。无自动批量迁移。

### 监控 rollout

升级期间及之后关注：

* **命令错误率** — 关注 `FAILED_PRECONDITION` 或 `INVALID_ARGUMENT` 激增，可能表示兼容性问题
* **合约版本分布** — 用 PQS 查询仍有多少活跃合约在旧版 vs 新版
* **对手方就绪** — 监控涉及对手方的交易是否因缺包失败

检查合约版本分布的 PQS 查询：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT package_id, count(*) AS active_count
FROM active('your-module:YourTemplate')
GROUP BY package_id;
```

## 回滚程序

SCU 无内置回滚。包上传后无法删除，「回滚」指管理局面而非撤销上传。

若新版本出问题：

1. **停止** 用有问题版本创建新合约。若工具支持，更新后端在创建时显式引用旧包版本。
2. **调查并修复** 新包问题，再上传修正版（ effectively v3）。
3. **与对手方沟通**，使其知晓问题并调整系统。

旧包仍在，其下创建的合约可继续运行。风险主要在新建合约或行使仅新版才有的逻辑。

### 回滚不够时

若新版本引入测试中未发现的破坏性变更（兼容性检查应防此情况，但错误仍可能发生），可能需要：

* 上传修正包版本
* 用显式迁移 choice 迁移受影响合约
* 与持有受影响合约的所有对手方对齐迁移

这是最扰动场景，强调在 DevNet/TestNet 充分测试后再上生产。

## 运营检查清单

每次生产升级使用：

* [ ] 新 DAR 通过 `dpm build` 与 `dpm test`
* [ ] 与当前生产包的兼容性检查通过
* [ ] 在 DevNet 或 TestNet 用真实数据测试升级
* [ ] 已通知对手方并商定 rollout 窗口
* [ ] 已记录回滚程序
* [ ] 监控面板已更新以跟踪版本相关指标
* [ ] DAR 已上传到生产 validator
* [ ] 对手方确认已上传
* [ ] 升级后 24–48 小时监控错误率
* [ ] 已制定旧版合约迁移计划（如适用）

## 延伸阅读

* [Upgrade Limitations](/appdev/modules/m6-limitations) — 影响生产 rollout 的约束
* [Testing Upgrades](/appdev/modules/m6-testing-upgrades) — 上线前测试策略
* [Error Handling](/appdev/modules/m7-error-handling) — 混合版本部署中的错误处理
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — DevNet → TestNet → MainNet 路径
* [Smart Contract Upgrading Reference](/appdev/deep-dives/smart-contract-upgrading-reference) — 包验证与运行时升级规则详情
* [Values in the Ledger API](/appdev/deep-dives/values-in-the-ledger-api) — Ledger API 在命令提交与查询时如何验证与规范化值""",
    },
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for slug, payload in PAYLOADS.items():
        path = OUT / f"{slug}.json"
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        count += 1
        print(slug)
    print(f"count={count}")


if __name__ == "__main__":
    main()
