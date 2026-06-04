---
title: "Canton Network 应用架构设计"
slug: "appdev-deep-dives-app-architecture-design"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/app-architecture-design.md"
source_title: "Canton Network Application Architecture Design"
tags:
  - appdev
  - deep-dives
  - app-architecture-design
---

# Canton Network 应用架构设计

> Canton Network 应用组件、部署拓扑与后端设计考量。

# Canton Network 应用架构设计考量

构建并运营生产级 Canton Network 应用时，需对每个组件做审慎设计。本文介绍 Canton Network 应用的基本组件，侧重后端核心职责，并从应用提供方与应用用户双方视角讨论可行技术栈与架构选项的成本与收益，亦可对照技术解决方案架构师认证路径中的 *Daml Application Architecture* 与 *Daml Application Backend* 课程。

## Canton Network 应用组件

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/tsa-master-arch-with-user-backend.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=e2635b256b1531673b3cc57d536e9a3f" className="align-center" alt="Canton Network application architecture diagram as described below." width="1357" height="1084" data-path="images/docs_website/tsa-master-arch-with-user-backend.png" />

### 前端

前端让人类终端用户高效参与 Canton Network 应用的业务流程。纯系统间集成方案可能无需前端，其余应用通常需要。

为实现不可抵赖性，代表应用提供方或应用用户组织执行的终端用户操作，须通过该组织控制的、连接其 participant 节点的前端提交；否则组织可争议交易记录，声称其与终端用户实际操作不符。为获得尽可能强的不可抵赖保证，应用提供方与各应用用户应在其控制的 Web 服务器上托管前端。同理，各组织前端应通过本组织 IAM 登录；IAM 签发可用于向本组织 participant 提交命令的访问令牌。注意：前端不直接与账本通信，而是将命令发给后端，再由后端提交账本。

### Daml 模型

Daml 模型定义跨组织工作流，并作为与之交互组件的 API 定义。模型编译为 DAR（Daml 包），须上传至各应用用户的 Canton participant 节点。

### 后端

后端通过 Ledger API 直接管理对 participant 节点的访问，用 Daml Party 表示应用提供方与应用用户，用 Daml 合约表示组织间工作流状态。

Daml Party 在组织层面于账本行动并读取数据。后端不必是单一单体，可按团队偏好采用微服务等逻辑架构。

后端通常承担以下一项或多项：

* 提供更高层 API
* 自动化链上工作流
* 与链下系统集成

具体如下：

#### 提供更高层 API

participant 与 synchronizer 实时跨组织同步共享应用数据。当前端或其他系统需对此数据执行特定查询时，请求发往后端；后端通过具备适当访问控制与性能特征的应用专用 API 响应。

当应用需与账本通信时，若干共性考量可抽象为更高层 API，供后端其他逻辑组件、前端或外部应用/系统使用。读写路径考量不同。

##### 读

读路径最重要的是通过 Participant Query Store（PQS）读取账本数据。利用应用专用索引，使查询可随应用规模扩展。PQS 扩展并补充 Ledger API 能力。

* Ledger API 侧重暴露账本当前状态及变更，不做过滤。Canton Network 应用通常有应用专用查询需求，常包括检索单个合约。
* PQS 作为运营数据存储，在 participant 节点上为账本数据提供灵活高效查询；例如可通过 JDBC 用 SQL 检索，实现读路径可像普通 SQL 后端 Web 服务一样标准。

PQS 可摄取其配置与权限允许从 Private Contract Store（PCS）获取的全部数据，但不对 PQS 客户端额外实施访问控制。向上游展示数据时，API 服务须实施适当的终端用户认证与访问控制。将终端用户访问控制交给应用后端开发者（而非内置在 PQS），可在任意粒度实现，关键在于可基于组织内业务需求——使同组织不同用户访问不同数据集，而不局限于 Daml 模型编码的跨组织访问控制 schema。

PQS 支持在修剪窗口内访问 Active Contract Set（ACS）与账本历史。建议按业务需求与预期数据量选择修剪窗口。必要时 PQS 可作为过滤事件源用于分析或填充数仓，并存储合约及证明其创建与归档的 exercise 事件。

Daml 模型设计上，建议避免以活跃合约形式保存已完成工作流步骤信息，否则 ACS 无界增长；应使用 PQS 历史事件作为黄金源，例如应用专用交易日志或向终端用户推送已完成步骤通知。有时可用额外非 consuming exercise 事件表示应通知工作流相关方的特定事件。

PQS 提供适用于多种场景的通用可查询账本历史与状态视图，是自动化与集成组件访问账本数据的推荐路径。对某些专用大规模读场景，可能需要定制运营数据存储（ODS）方案。

##### 写

写路径实现更高层 API 时，最重要的是可靠性，包含两项相关要点：命令失败时的重试行为，以及命令提交的幂等性。

* **重试行为**：凡需向账本发送命令的组件都需重试失败提交，通常应将此能力封装为可复用模块。
* **幂等性**：因重试或崩溃可能重新计算并重新提交命令，须保证写账本幂等。简单做法是让发往账本的命令消耗部分输入，例如对触发该命令的合约 exercise consuming choice。另一做法是命令去重：participant 在 Ledger API 提供命令去重，存储 command ID 并对相同 ID 后续提交去重。机制详见 Ledger API 文档。

##### 提供参考数据合约

更高层 API 的特例是为应用用户提供提交 Daml 交易所需的参考数据合约。部分 Daml 模型在链上存储参考数据，例如 OTC 交易合格对手方目录，或 oracle Party 提供的股指收盘、外汇、利率定盘等。此类合约通常不对应用用户 Daml Party 可见——在链上为大量 Party 维护可见性成本高，且多 observer 合约影响性能。此时使用「显式披露」：合约利益相关方链下共享，提交方在交易中附带，从而在解释时访问这些合约，即使提交方非利益相关方亦可成功。详见显式合约披露文档。

#### 自动化链上工作流

无需人工干预的链上步骤由后端自动化。例如金融服务应用客户入网：后端监听链上入网请求，在链下 KYC 系统通过后自动推进。

Daml 代码无独立执行线程；账本合约是被动的同步数据与权利记录，工作流须由外部组件推进，任何账本操作须由外部发起。

建议将自动化模块化为可重试任务：定义明确、独立的 work unit，保证自动化最终完成，并可基于该结构有界并行处理。

* **外部事件触发**：链下消息、定时/计划事件等。
* **状态触发**：常表示后端需推进链上工作流；状态以 Daml 合约表示，由合约创建或后端启动后发现而触发（「状态触发自动化」）。触发自动化的合约应在处理命令中被消费，避免循环。技术上常通过定期查询 PQS 轮询实现；重试时应重新执行完整查询以反映最新账本状态；同一任务内多查询应使用一致 ledger offset。任务应对可重试错误自动重试至上限，且重试整个处理块（非仅账本提交），以便反映最新状态或发现任务已完成/失效。

#### 与链下系统集成

后端亦集成链下系统，例如 AML 检查、在处理链上金融交易时填充报表库，或从链下预交易分析发起链上交易。设计应用时须理解提供方与用户组织的集成需求并建设相应后端基础设施。

对此类功能无特殊 Canton 约束，按现有 IT 景观选用集成技术即可。

常见方式包括：

* 自动化工作流中查询链下系统（KYC 库、保证金计算、净额结算优化等）。
* 通过 API 或消费消息队列将链下数据推送到账本（如定价数据入库为参考数据合约）。
* 通过 webhook 或写消息队列将账本数据推到链下；亦可基于 offset 拉取（PQS 与 Ledger API 均支持），例如将链上登记复制到撮合服务、对接会计或报表库。
* 方式非穷尽；选用便于提供方与用户开发部署的技术。建议读写路径分离，经后端集成链下系统，而非让链下系统直接使用 Ledger API。

## 2. 选择后端技术栈

### 采用企业应用标准栈

* 与 Ledger API 交互：使用与 gRPC 交互的标准库。
* IAM：采用组织标准栈。
* 需后台处理以响应链上状态变化并将外部数据写入账本。
* 与账本的所有交互应通过幂等命令的重试实现崩溃容错。

### 任意语言实现后端

* 任意支持 HTTP 的语言可用 JSON Ledger API。
* 部分语言有更高层工具，如 Daml Codegen for Java。
* Codegen 尤其便于处理 Daml 合约载荷，生成 Daml 类型与目标语言的映射及 exercise 命令样板代码。

## 3. 架构选项

Canton Network 应用无单一最佳架构，存在连续谱，各选项有权衡，须结合业务需求，尤其从成本角度比较三种典型架构：

* 应用提供方运营后端
* 应用用户运营由提供方构建的后端
* 各组织自建并运营各自后端

### 应用提供方运营后端

组件最少：用户仅运营前端，提供方独家运营后端。用户前端通过 Ledger API 或 JSON API 写账本，读依赖提供方后端。部署最简单，仍可为双方保证不可抵赖与数据主权；但不支持用户链下集成，链上自动化受限——后端只能代表提供方 Party 提交，用户 Party 仅能通过前端提交。

### 应用用户运营由提供方构建的后端

除运营 participant 带来的不可抵赖与数据主权外，用户还获得：

* **数据查询主权**：可由用户自有后端基于本地应用数据副本提供查询（高赌注低信任或合规控制基础设施时可能需要）。
* **用户系统集成**：本地后端作为用户链下系统与应用的桥梁。
* **争用资源批处理**：多终端用户访问同一链上资源时，本地后端可批处理（如多交易员从公司链上账户划拨），单次 Daml 交易处理多请求，吞吐显著高于串行。
* **细粒度终端用户权限**：通过管理对用户 participant 与托管 Party 的访问实现细粒度读写控制。

劣势包括：用户运营成本、多版本并存导致工作流变更与升级测试复杂、提供方须承担本地软件供应商角色（支持团队、发布管理等）。

### 各组织自建并运营各自后端

各方自建前端与后端，自动化与链下集成灵活性最大，但成本最高。用户可定制集成与访问控制，降低供应链风险。

劣势：用户开发成本高、缩小可触达市场、跨组织协调与 Daml 虽能规范跨组织 API 但软件协作仍复杂、应用演进时用户可能无力改代码导致工作流难以变更或下线。

### 属性摘要

#### 架构属性

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/properties-of-arch.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=013cdc6ae8a0c3b18e1a3646c06169e9" className="align-center" alt="Properties of the architectures as described below." width="2286" height="1138" data-path="images/docs_website/properties-of-arch.png" />

下表汇总三种架构属性。实际可在其间连续选择，架构亦可随时间演进。建议从满足最低需求的最简架构起步，随业务演进再增加复杂度。

#### 成本视角下的架构属性

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/docs_website/properties-of-arch-from-cost-perspective.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=3619d3f880097e76764f30ad1ad20223" className="align-center" alt="Properties of the architectures from a cost perspective as described below." width="2288" height="1028" data-path="images/docs_website/properties-of-arch-from-cost-perspective.png" />

下表从成本与软件工程角度汇总同一三种架构。建议在满足需求前提下尽量降低用户的工程与运维负担。「X」表示存在问题，「XX」表示更严重；例如各方自建后端时跨组织协调问题显著加剧。

## 4. 要点

1. Canton Network 应用通常包含前端、Daml 模型与后端；Daml 模型须部署在提供方与各用户的 participant 节点。
2. 后端主要用途：提供与账本通信的更高层 API、自动化链上工作流、集成链下系统。
3. 更高层 API 读路径用 PQS；写路径最重要的是可靠性（重试与幂等）。
4. 后端职责并不特殊，技术栈为标准企业应用栈即可。
5. 前后端开发与运营有多种选项，架构可演进；建议初期优先最小化用户工程与运维负担的架构，以降低交付风险并扩大可触达市场。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
