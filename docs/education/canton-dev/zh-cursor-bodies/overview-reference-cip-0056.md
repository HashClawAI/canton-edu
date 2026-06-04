> CIP-0056 参考：Canton Network 上代币持仓、转账与分配的标准 Daml 接口

[CIP-0056](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md) 定义 Canton Network Token Standard——一组 Daml 接口与链下 API，使钱包与应用能以统一方式跨 registry 与代币化资产交互。实现 CIP-0056 的 registry 可由任何合规钱包服务，任何应用可编排转账与结算而无需依赖 registry 专用代码。

Splice 钱包为 Canton Coin (CC) 实现 CIP-0056，底层 Daml template 为 `Amulet`。Canton Network 上其他资产 registry 可为自有工具实现相同接口。

## CIP-0056 标准化内容

标准涵盖三类功能：

* **Portfolio view** — 跨多个 registry 展示 Party 当前持仓、交易历史与工具元数据。
* **Direct peer-to-peer (FOP) transfers** — 在 Party 间转移资产，单步或两步 offer/accept。
* **Delivery-versus-payment (DvP) settlements** — 将资产锁定为 allocation，以原子执行多 leg 结算。

六套链上 Daml API 及对应链下（HTTP）registry API 支持上述能力：

* **Token Metadata** — 工具 symbol、名称、总供应、registry UI URL
* **Holding** — 投资组合视图与交易历史
* **Transfer Instruction** — 直接 FOP 转账
* **Allocation** — 为 DvP 预留资产
* **Allocation Request** — 标准化的应用→钱包 allocation 请求
* **Allocation Instruction** — 标准化的钱包→registry allocation 创建

## 核心接口

### Token Metadata

Token Metadata API 使钱包无需了解 registry 内部数据模型即可获取工具描述信息。Registry 暴露显示名称、symbol、总供应、registry UI URL 等。钱包经 registry 链下 HTTP 端点查询。

### Holding

`Holding` 接口表示单一代币持仓——投资组合中的一项。其 view 暴露：

* `owner` — 持仓所有者 Party
* `instrumentId` — 全局唯一标识，含 `admin` Party（registry）与 `id` 文本
* `amount` — 持仓规模（`Decimal`）
* `lock` — 可选 `Lock`，含 holder Party、过期时间与可读 context
* `meta` — 遵循 Kubernetes annotation 约定的键值元数据

每个 `Holding` 合约为账本上独立 UTXO。通过 Ledger API active-contracts 端点查询，按 `Holding` 接口 ID 过滤（如 `#splice-api-token-holding-v1:Splice.Api.Token.HoldingV1:Holding`）。

### TransferFactory 与 TransferInstruction

`TransferFactory` 为 registry 维护的 non-consuming 工厂合约。钱包从 registry 链下 API 获取并 exercise `TransferFactory_Transfer` 发起转账。choice 接受 `Transfer` 记录：发送方、接收方、金额、工具、输入持仓与截止时间（`executeBefore`）。

依 registry 实现，结果可为：

* **Completed** — 立即结算，返回接收方新持仓。
* **Pending** — 创建 `TransferInstruction`，需进一步操作。
* **Failed** — 无法完成，输入持仓（扣除费用后）退回发送方。

创建 `TransferInstruction` 时跟踪进行中转账状态。接收方可 exercise `TransferInstruction_Accept` 或 `TransferInstruction_Reject`；发送方可 `TransferInstruction_Withdraw`。Registry 可通过 `TransferInstruction_Update` 推进内部工作流。

### Allocation 与 AllocationFactory

Allocation 支持多 leg 结算（DvP）。`Allocation` 表示为结算特定 leg 预留的资产，由锁定持仓支撑。

`AllocationView` 含：

* `allocation` — `AllocationSpecification`，引用 settlement info、transfer leg ID 与 transfer leg 本身（发送方、接收方、金额、工具）
* `holdingCids` — 支撑该 allocation 的持仓
* `meta` — 扩展元数据

通过从 registry 获取 `AllocationFactory` 并 exercise `AllocationFactory_Allocate` 创建 allocation。用 [Token Standard API](/overview/reference/splice-wallet-reference#wallet-api-endpoints) 发现与交互 allocation 合约。Settlement 的 `executor` Party 与发送方、接收方共同控制 allocation。生命周期三 choice：

* `Allocation_ExecuteTransfer` — 执行已分配资产转账（结算步骤）
* `Allocation_Cancel` — 提前释放 allocation，由发送方、接收方与 executor 共同控制
* `Allocation_Withdraw` — 发送方在 `allocateBefore` 截止前取回资产

`AllocationInstruction` 接口跟踪多步 allocation 创建，类似 `TransferInstruction` 跟踪多步转账。

### Allocation Request

`AllocationRequest` 标准化应用请求钱包分配资产的方式：应用创建含 settlement 详情与 transfer leg 的 allocation request；用户钱包 exercise 相应 `AllocationFactory` choice 为其注资。这使应用结算逻辑与钱包持仓管理解耦。

## 转账模型

### 一步转账

一步转账在单笔 Daml 交易内完成。exercise `TransferFactory_Transfer` 且 registry 可立即结算时，结果为 `TransferInstructionResult_Completed` 及接收方新持仓。

对 Canton Coin，接收方已设置 `TransferPreapproval` 合约时可用一步转账。preapproval 表示接收方同意无需逐笔同意即可从任何发送方接收 CC。每个 preapproval 有 `receiver` 与 `provider` Party；provider 支付与 preapproval 生命周期成比例的费用，并在经其 preapproval 的入账转账上获得 app rewards。preapproval 会过期须定期续期——provider 为验证者运营方时由验证者应用自动处理。

Splice 钱包与 Token Standard registry API 检测现有 preapproval 并自动路由。其他 registry 可自有的一步机制或始终要求两步。

### 两步转账

无 preapproval 或 registry 需额外授权时，转账分两步：

1. **Instruct** — 发送方 exercise `TransferFactory_Transfer`。Registry 创建 `TransferPendingReceiverAcceptance` 状态的 `TransferInstruction`。消费发送方输入持仓，资金由 registry 持有。
2. **Accept** — 接收方 exercise `TransferInstruction_Accept`。Registry 完成转账并为接收方创建持仓。

接收方亦可 `TransferInstruction_Reject` 退回资金；发送方可在接受前 `TransferInstruction_Withdraw`。路径设计使钱包可解析交易历史判断各 instruction 成败。

两步转账初始 instruct 后无需发送方自动化，适合用自管密钥签署的外部 Party。[CIP-0078](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0078/cip-0078.md) 后两步 CC 转账无费用。

### 使用 Allocation 的 DvP 结算

结算跨不同工具或 registry 的多 leg 时，各发送方独立分配资产：

1. 应用创建 settlement specification，含 `executor` Party、截止 `allocateBefore` 与 settlement 截止 `settleBefore`。
2. 各发送方钱包 exercise `AllocationFactory_Allocate`，将持仓锁定为各自 transfer leg 的 `Allocation`。
3. 全部 leg 分配后，executor 对各 allocation exercise `Allocation_ExecuteTransfer` 原子完成结算。

若发送方在截止前未分配，executor 可取消剩余 allocation。发送方亦可在 `allocateBefore` 前 `Allocation_Withdraw` 取回持仓。

## UTXO 管理

类似 Bitcoin，Canton 使用 UTXO 模型，UTXO 为实现 `Holding` 接口的全部活跃合约。

活跃 `Holding` 合约在托管用户与托管 token administrator 的验证者上产生存储与计算成本。为高效利用网络资源，钱包提供方应力求每用户 UTXO 数量较低——平均约 10 个以下。

这也优化流量成本——转账每个 UTXO 输入额外消耗流量。该建议与 Canton Coin 等代币激励一致：

* 单笔转账最多 100 个输入合约，抑制过度拆分持仓
* 过期初始金额低于累计持有费的 coin UTXO，抑制粉尘 UTXO

钱包提供方应优先选小额 `Holding` UTXO 作转账输入，并在用户入驻时设置 `MergeDelegation` 以便钱包自动合并小额 UTXO。Splice `splice-util-token-standard-wallet.dar` 提供 `MergeDelegation` 与 `BatchMergeUtility` template。

## Registry 与发现

每个代币工具由 **registry** 管理——维护所有权记录并暴露链上 Daml 接口与链下 HTTP API 的应用。Registry 的 `admin` Party 出现在每个 `InstrumentId` 与每个工厂合约 view 中。

执行 factory choice 前须查询 registry 链下 API 获取：

* `factoryId`（工厂 contract ID）
* `disclosedContracts`（exercise 成功所需）
* `choiceContextData`（作为 choice 参数中的 `context` 传入）

给定工具的 registry URL 目前由钱包自行维护。计划基于 [Canton Name Service](/overview/reference/canton-name-service) 的通用发现机制，将 registry URL 存入 CNS 条目元数据并经 Scan API 获取。

链下 API 无需认证。安全模型依赖 contract ID 不可猜测性与 Canton 按需分发——仅有权 Party 收到合约。

## 元数据约定

所有 CIP-0056 接口含 `Metadata` 字段——可扩展键值文本映射。键遵循 Kubernetes annotation 约定，应以定义组织的 DNS 名为前缀。例如 Splice 实现使用 `splice.lfdecentralizedtrust.org/` 前缀。

交易解析常用标准键：

* `splice.lfdecentralizedtrust.org/tx-kind` — 操作类型（如 `transfer`、`merge-split`、`burn`、`mint`、`unlock`、`expire-dust`）
* `splice.lfdecentralizedtrust.org/sender` — 发送方 Party
* `splice.lfdecentralizedtrust.org/reason` — 操作可读原因
* `splice.lfdecentralizedtrust.org/burned` — 销毁持仓金额

`ExtraArgs` 类型将传给多数 choice 的两结构打包：`ChoiceContext`（registry 链下 API 的不透明数据）与 `Metadata`（调用方注解）。choice context 将 registry 内部数据传入链上执行；metadata 使调用方与 registry 就额外语义达成一致。

## 钱包集成

[Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk) 将集成模式打包为可复用库。从零构建钱包的五种模式：

* 读取实现 Token Standard 接口的合约（active-contracts 端点）
* 读取并解析涉及 Token Standard 合约的交易历史
* 执行 factory choice（从 registry 获取工厂，再提交 Ledger API）
* 对现有合约执行 non-factory choice（如接受 transfer instruction）
* 从自定义 Daml 代码调用 Token Standard choice（批量操作、合并或应用专用工作流）

[Token Standard CLI](https://github.com/canton-network/splice/tree/main/token-standard#cli) 将各模式实现为可执行代码，兼作测试工具与参考实现。

## 延伸阅读

* [Full CIP-0056 text](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md)
* [Token standard source code](https://github.com/canton-network/splice/tree/main/token-standard)
* [Wallet SDK](https://github.com/canton-network/wallet-gateway/tree/main/sdk/wallet-sdk)
* [Canton Coin Tokenomics](/overview/reference/canton-coin-tokenomics) — CC 费用结构与 UTXO 粉尘过期
