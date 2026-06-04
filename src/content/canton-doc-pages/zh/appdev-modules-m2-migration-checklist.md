---
title: "迁移清单"
slug: "appdev-modules-m2-migration-checklist"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m2-migration-checklist.md"
source_title: "Migration Checklist"
tags:
  - appdev
  - modules
  - m2-migration-checklist
---

# 迁移清单

> 以太坊开发者迁移到 Canton 的实用清单

规划与执行迁移时，按下列章节逐项核对。

## 开始前

<AccordionGroup>
  <Accordion title="评估应用架构">
    * [ ] **状态模型依赖**：是否依赖全局状态查询？
    * [ ] **多方关系**：合约中有哪些 Party？
    * [ ] **隐私需求**：是否需要子交易级隐私？
    * [ ] **集成点**：哪些系统连接智能合约？

    若严重依赖「展示所有 NFT」类全局查询，需用 Party 作用域查询或链下索引重新设计。
  </Accordion>

  <Accordion title="理解范式转变">
    | 领域 | 以太坊假设 | Canton 现实 |
    | ------------- | -------------------- | ---------------------------- |
    | 状态 | 全局可查询 | 分布式、按 Party 作用域 |
    | 合约 | 可变 | 不可变（归档 + 创建） |
    | 授权 | 运行时 `msg.sender` | 编译期 signatory |
    | 隐私 | 默认公开 | 默认私有 |
    | 身份 | 匿名地址 | 具名 Party |
  </Accordion>

  <Accordion title="搭建开发环境">
    * [ ] 安装 [Daml SDK](/sdks-tools/sdks/daml-sdk)
    * [ ] VS Code + [Daml 扩展](https://marketplace.visualstudio.com/items?itemName=DigitalAssetHoldingsLLC.daml)
    * [ ] 克隆 [CN Quickstart](/sdks-tools/reference-projects/cn-quickstart)
    * [ ] 运行 `make setup && make build && make start` 验证环境
  </Accordion>
</AccordionGroup>

## 智能合约迁移

### 阶段 1：建模 Party

<Steps>
  <Step title="识别所有参与者">
    列出与合约交互的各方并映射为 Canton Party：

    * **合约所有者** → `admin : Party`（管理类合约的 signatory）
    * **用户** → `user : Party`（每用户独立 Party）
    * **运营方** → `operator : Party`（可为 signatory 或 controller）
  </Step>

  <Step title="定义 Party 关系">
    对每个合约确定：

    * **谁必须同意创建？** → Signatories
    * **谁应可见？** → Observers
    * **谁能执行动作？** → Controllers（按 Choice）
  </Step>

  <Step title="规划 Party 托管">
    * **用户 Party**：常在应用提供方验证者
    * **管理 Party**：在本组织验证者
    * **外部 Party**：在其自有验证者
  </Step>
</Steps>

### 阶段 2：翻译合约

将 Solidity struct → Daml data type；`mapping` → 每持仓一份合约；函数 → Choice；`onlyOwner` → `controller admin`（协议强制，无需 modifier）。

### 阶段 3：不同方式处理状态

* [ ] **替换全局查询**：设计 Party 作用域查询
* [ ] **使用 contract keys**：用 key 查找而非地址
* [ ] **接受 Contract ID 变化**：每次更新 ID 会变；用 key 作稳定引用

<Warning>
  Canton 没有跨所有合约的 `eth_getLogs` 式事件过滤。尽早规划索引策略。
</Warning>

## 集成迁移

### API 变更

| 以太坊 | Canton | 说明 |
| ------------------- | ------------------------------------------------------------- | --------------------------------- |
| JSON-RPC | Ledger API (gRPC 或 JSON API) | 不同协议 |
| Web3.js / ethers.js | Ledger API 客户端或 [dApp SDK](/zh/docs/canton/appdev-modules-m4-sdks-apis) | 语言相关客户端 |
| Event logs | Transaction streams | 订阅 Party 交易 |
| `eth_call` | Exercise non-consuming choice | 只读操作 |

### 认证变更

以太坊用私钥签名并从 `msg.sender` 派生身份；Canton 用 Party 认证与 JWT。公开函数「任何人可调用」在 Canton 中变为仅已认证 Party 可访问。

### 索引策略

无全局状态查询时：

* [ ] 使用 **PQS** 做 SQL 查询
* [ ] **流式交易** 写入自有数据库
* [ ] **合约设计** 便于查询的 key

## 测试迁移

* [ ] Hardhat/Foundry → Daml Script
* [ ] 测试授权规则与多方 propose-accept

### 集成测试

* [ ] 对 LocalNet 测试（CN Quickstart）
* [ ] 验证 API 集成与错误/回滚场景

## 部署迁移

**网络**：LocalNet → DevNet → TestNet → MainNet

* [ ] `dpm build` 打包 Daml
* [ ] 经 admin/LAPI 上传到验证者
* [ ] 分配 Party、初始化合约、配置应用指向 Ledger API

## 运维变更

监控：区块浏览器 → 验证者日志与指标；gas → traffic 单位。密钥：EOA → Party 密钥（验证者或外部）；多签 → 多 signatory 合约。

## 常见迁移陷阱

| 陷阱 | 原因 | 避免 |
| ------------------------------- | -------------------------------------- | ----------------------------------------------- |
| 构建全局状态视图 | 习惯以太坊查询 | 从一开始就按 Party 作用域设计 |
| 过度使用 Party | 把 Party 当免费地址 | Party 有托管成本，审慎设计 |
| 忽略 propose-accept | 期望单方面创建多方合约 | 多方需工作流 |
| 期望 event logs | 以太坊事件模式 | 用交易流与索引 |
| 把 Contract ID 当地址 | ID 每次更新都变 | 用 contract keys |

## 迁移阶段

| 阶段 | 重点 | 完成标准 |
| ------------------ | ------------------------- | ---------------------------------- |
| **1. 学习** | 理解 Canton 模型 | 团队掌握 Daml 基础 |
| **2. 设计** | 为 Canton 重设计 | Party 模型与合约设计完成 |
| **3. 开发** | Daml 实现 | 合约与测试完成 |
| **4. 集成** | 连接应用 | LocalNet API 可用 |
| **5. 测试** | 测试网验证 | DevNet/TestNet 通过 |
| **6. 部署** | 上线 | MainNet 运行 |

## 下一步

<CardGroup cols={2}>
  <Card title="模块 3：Daml 开发" icon="code" href="/zh/docs/canton/appdev-modules-m3-dev-environment">
    开始用 Daml 构建。
  </Card>

  <Card title="CN Quickstart" icon="rocket" href="/sdks-tools/reference-projects/cn-quickstart">
    动手跑通示例。
  </Card>
</CardGroup>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
