---
title: "测试升级"
slug: "appdev-modules-m6-testing-upgrades"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m6-testing-upgrades.md"
source_title: "Testing Upgrades"
tags:
  - appdev
  - modules
  - m6-testing-upgrades
---

# 测试升级

> 验证升级兼容性、测试跨版本工作流及回归测试策略

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
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @artifacts/v1.dar

# Upload v2 DAR — if this succeeds, type-level compatibility is confirmed
curl -X POST "http://localhost:7575/v2/packages" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @artifacts/v2.dar

# Run your project's upgrade test suite here

kill $SANDBOX_PID
```

## 下一步

* [Deploying Upgrades](/zh/docs/canton/appdev-modules-m6-deployment) — 在多环境 rollout 已测试的升级
* [Upgrade Compatibility](/zh/docs/canton/appdev-modules-m6-upgrade-compatibility) — 允许变更的参考

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
