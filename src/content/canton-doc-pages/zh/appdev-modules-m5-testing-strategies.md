---
title: "测试策略"
slug: "appdev-modules-m5-testing-strategies"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-testing-strategies.md"
source_title: "Testing Strategies"
tags:
  - appdev
  - modules
  - m5-testing-strategies
---

# 测试策略

> Canton 应用测试金字塔：从 Daml Script 单元测试到集成与端到端测试

测试 Canton 应用与任何分布式系统原则相同：尽量自动化，在能捕获缺陷的最低层测试。差异在于各层工具及多方、隐私账本带来的特有挑战。

## 测试金字塔

Canton 应用采用三层测试，各层捕获不同类别问题：

* **单元测试** — Daml Script 隔离验证智能合约逻辑，在内存账本（Sandbox）上运行，无网络开销。
* **集成测试** — 针对运行中的 Canton sandbox 或 LocalNet 测试后端与 API，验证链下代码与账本正确交互。
* **端到端测试** — 跨多个 validator、后端与前端的完整工作流，验证用户实际体验的系统行为。

## 用 Daml Script 做单元测试

Daml Script 是单元测试智能合约逻辑的主要工具。将测试 script 写为 `Script ()` 类型的顶层值，`dpm test` 在 Sandbox 上运行。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm test
```

Daml Script 可在 Sandbox 上运行，执行通常只需数秒。

单元测试创建 party、提交命令并断言结果：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
testTokenTransfer : Script ()
testTokenTransfer = do
  alice <- allocateParty "Alice"
  bob <- allocateParty "Bob"

  -- Alice creates a token
  tokenCid <- submit alice do
    createCmd Token with
      owner = alice
      issuer = alice
      amount = 100.0

  -- Alice transfers to Bob
  submit alice do
    exerciseCmd tokenCid Transfer with
      newOwner = bob
      transferAmount = 50.0

  -- Verify Bob received the token
  bobTokens <- query @Token bob
  assertMsg "Bob should have one token contract" (length bobTokens == 1)
```

查看 `dpm test` 输出确认各 script 通过或失败。

### 单元层应测什么

聚焦 Daml 模型特有行为：

* 有效与无效参数的模板创建
* Choice 授权（正确 controller 可行使，他人不可）
* Choice 内业务逻辑（计算、状态转移）
* 边界与错误条件（应失败的断言）
* 多方授权模式（提议-接受工作流）

### 测试代码与生产代码分离

Daml 工作流单元测试编译进 DAR，这些 DAR 仅用于测试，不应部署到 validator。将测试放在独立包，与生产代码分离：

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
daml/
├── main/           # 生产 Daml → main.dar
│   └── daml.yaml
└── test/           # 测试 script → test.dar（依赖 main.dar）
    └── daml.yaml
```

## 集成测试

集成测试验证链下代码——后端服务、API 处理器、数据库查询——与 live ledger 正确协作。有两种工具：

* **`dpm sandbox`** — 单进程启动本地 Canton sandbox，适合单后端对 Ledger API 测试，无需完整网络开销。
* **LocalNet** — Docker Compose 多 validator 网络。测试需要多方在不同 validator、钱包集成或 PQS 时使用。

### 后端集成测试

对连接 Ledger API 的后端，测试应：

1. 启动 sandbox 或连接运行中的 LocalNet
2. 创建测试 party 并上传 DAR
3. 经后端 API 层提交命令
4. 断言账本状态或 API 响应

Java 集成测试经 gRPC 连接 Ledger API 并提交命令：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Set up a gRPC channel to the participant's Ledger API
Channel channel = ManagedChannelBuilder
    .forAddress(ledgerhost, ledgerport)
    .usePlaintext()
    .build();

// Create a blocking stub for command submission
CommandServiceGrpc.CommandServiceBlockingStub commandService =
    CommandServiceGrpc.newBlockingStub(channel);

// Submit a contract creation and wait for the transaction result
var updateSubmission = UpdateSubmission
    .create(APP_ID, randomUUID().toString(), update)
    .withActAs(party);
var request = new SubmitAndWaitForTransactionRequest(
    updateSubmission.toCommandsSubmission());
var response = commandService.submitAndWaitForTransaction(request.toProto());
```

查询活跃合约使用 `StateService`：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
StateServiceGrpc.StateServiceBlockingStub stateService =
    StateServiceGrpc.newBlockingStub(channel);
long ledgerEnd = stateService
    .getLedgerEnd(GetLedgerEndRequest.newBuilder().build())
    .getOffset();

var request = new GetActiveContractsRequest(eventFormat, ledgerEnd);
Iterator<GetActiveContractsResponse> activeContracts =
    stateService.getActiveContracts(request.toProto());
```

### 测试隔离

优化做法是长期运行 Canton 实例，避免反复初始化。用每次测试唯一的 participant 用户与 party 隔离测试；可在测试 harness 中为 party 与用户名追加测试运行 ID 后缀。

这样可在同一 Canton 实例上并行运行测试而不互相干扰。

## 端到端测试

端到端测试跨多个 validator、后端与前端，演练终端用户与系统间的工作流。

### 浏览器自动化

涉及前端的测试可用 [Selenium](https://www.selenium.dev/) 或 [Playwright](https://playwright.dev/) 驱动浏览器：登录、经 UI 创建合约、验证对手方看到预期结果。

### 时间相关工作流

时间敏感工作流可在 Daml 中用 `passTime`，并为 CI 配置更短等待时间。含日历或时间函数的流程（如带息票支付的债券生命周期）可用 `passTime` 推进时间；端到端测试可将工作流推进间隔设为毫秒以缩短 CI。在测试 harness 中暂停/恢复自动化以避免竞态。

## 处理 Flaky 测试

分布式系统存在数据传播延迟与并发执行，可能导致测试不稳定，削弱开发者信任并拖慢迭代。

Canton 测试中 flaky 常见来源：

* **传播延迟** — 命令成功但交易尚未出现在读取方 validator。用带超时的轮询而非固定 sleep。
* **Party 可见性** — 在所有相关 validator 分配 party 之前就查询合约。
* **并发行使** — 两个测试同时行使同一合约，一个成功另一个发现合约已归档。

消除 flaky 的投入回报很快。可靠的测试套件意味着更快反馈与更有信心的部署。

## 性能测试

尽早并持续做性能测试。为各相关工作流单独建性能测试；用接近生产特征的合成数据做规模测试；测量性能指标并在运行间重置以发现回归；长时间 soak 测试发现瓶颈；配置告警监控系统故障，随时间调优可观测性。

Canton 应用性能测试需区分链上与链下操作。账本操作有随交易复杂度与参与方数量变化的同步开销；链下操作（PQS 查询、后端逻辑）按常规定位分析。

## 下一步

* [LocalNet Development](/appdev/modules/m5-localnet-development) — 搭建并使用 cn-quickstart LocalNet
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — 自动化测试流水线

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
