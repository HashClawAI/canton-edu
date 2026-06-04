#!/usr/bin/env python3
"""Write batch 2 zh-cursor JSON translations."""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs/education/canton-dev/zh-cursor"

DOCS = {
    "appdev-deep-dives-composition-multi-party": {
        "zhTitle": "在 Daml 中组合多方工作流",
        "summary": "提议-接受、委托、授权链、原子组合与接口等高级多方 Daml 设计模式。",
        "body": """> 高级 Daml 模式：提议-接受、委托、授权链与原子多方组合。

真实世界的 Daml 应用涉及角色、权限与信任关系各不相同的多个参与方。本深度文章涵盖使复杂多方工作流得以运行的 Daml 设计模式——从简单的双方协议到跨多个组织的多步授权链。

## 提议-接受模式

提议-接受的规范讲解见 [模块 2：多方工作流](/appdev/modules/m2-multi-party-workflows#the-propose-accept-pattern)。本文侧重在该基础上的其他组合模式。

## 委托

委托允许一方在限定范围内授予另一方代表其行事的权限。与提议-接受（创建共享协议）不同，委托建立的是单向信任关系。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template OperatorLicense
  with
    owner : Party
    operator : Party
    allowedOperations : [Text]
  where
    signatory owner
    observer operator

    choice Operate : ContractId OperationResult
      with
        operation : Text
      controller operator
      do assertMsg "Operation not allowed"
           (operation `elem` allowedOperations)
         create OperationResult with
           performer = operator
           onBehalfOf = owner
           operation
```

所有者将特定操作授予运营方。运营方可行使 `Operate` choice，但仅限允许的操作。所有者可通过归档 `OperatorLicense` 撤销委托。

## 多步工作流

许多业务流程需要不同参与方按序执行动作。将其建模为合约链，每一步的输出成为下一步的输入：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template TradeRequest
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer
    observer seller

    choice ConfirmTrade : ContractId TradeSettlement
      controller seller
      do create TradeSettlement with
           buyer
           seller
           asset
           price

template TradeSettlement
  with
    buyer : Party
    seller : Party
    asset : Text
    price : Decimal
  where
    signatory buyer, seller

    choice Settle : ()
      controller seller
      do pure ()
```

工作流每一步对应独立模板，使状态可见、可审计——可查询账本以查看任意交易处于哪一步。

## 原子组合

Daml 交易是原子的：交易中所有创建与归档要么全部成功，要么全部失败。利用该性质实现必须同时发生的复杂操作：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice SwapAssets : (ContractId Asset, ContractId Asset)
  controller partyA
  do -- Both transfers happen atomically
     newAssetForB <- exercise assetFromA Transfer with newOwner = partyB
     newAssetForA <- exercise assetFromB Transfer with newOwner = partyA
     pure (newAssetForA, newAssetForB)
```

若任一转移失败（controller 错误、合约已归档、断言失败），则两者都不会发生。这是 DvP（券款对付）等结算模式的基础。

## 通过接口授权

接口定义模板可实现的抽象能力，用于构建可组合的授权模式：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface Transferable where
  viewtype TransferView
  getOwner : Party
  transfer : Party -> Update (ContractId Transferable)

  choice TransferTo : ContractId Transferable
    with newOwner : Party
    controller getOwner this
    do transfer this newOwner
```

任何实现 `Transferable` 的模板都获得 `TransferTo` choice。后端可针对接口编写通用转移逻辑，而无需知道具体模板类型。

<Note>
  将接口定义放在仅含接口、不含模板的独立包中。接口结构（方法与 view 类型）部署后不可修改；若需变更，应在新包中引入新版本接口。
</Note>

## 多方可见性模式

Canton 隐私模型下，各方仅能看到自己作为利益相关方（签字方或观察方）的合约。若工作流需要更广可见性但不授予操作权，可使用观察方模式：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuditableTransaction
  with
    executor : Party
    counterparty : Party
    auditor : Party
    details : Text
  where
    signatory executor, counterparty
    observer auditor  -- auditor can see but not act
```

监管或合规场景下，第三方需可见交易但非参与方时，将其加为 observer。其可通过 Ledger API 读取合约数据，但不能对其行使 choice。

## 设计考量

组合多方工作流时：

* 尽量保持签字方集合最小——每增加一名签字方都会增加协调开销
* 只读访问用 observer，而非将各方都设为签字方
* 设计模板使各方 choice 在声明中一目了然
* 避免过深的交易树（大量嵌套 exercise），以免增大交易体积与延迟
* 评估某步是否必须上链，或可链下完成

## 下一步

* [去中心化](/appdev/deep-dives/decentralization) — 各层去中心化策略
* [多方托管](/appdev/deep-dives/multi-hosting) — 跨验证者分布 Party 以提高韧性
""",
    },
    "appdev-deep-dives-decentralization": {
        "zhTitle": "去中心化",
        "summary": "Canton 栈各层去中心化策略：单验证者、多验证者、多方托管、BFT 同步器与多同步器。",
        "body": """> 从单验证者到 BFT 同步器，Canton 栈各层的去中心化策略。

Canton 支持从集中到完全去中心化的光谱。不必一开始就全力去中心化——可从简单单验证者部署起步，随应用信任需求演进逐步去中心化。

## 去中心化光谱

Canton 架构有多层可做去中心化选择，信任含义各不相同：

* **应用层** — 多少验证者托管应用中的 Party（如多方托管或去中心化 Party）
* **同步器层** — 同步器由单一还是多个实体运营
* **网络层** — 使用 Global Synchronizer、私有同步器或两者

每一层去中心化程度越高，对单一实体的信任越少，但运维复杂度也越高。

## 单验证者

最简单部署：应用所有 Party 托管在连接 Global Synchronizer 的单一验证者上。

**信任模型：** 你信任验证者运营方（自己或第三方）诚实处理交易并保持数据可用。Global Synchronizer 的 BFT 仍防范同步器层攻击，但验证者是应用在验证者层面的单点故障。

**适用场景：**

* 早期开发与原型
* 所有 Party 同属一个组织的应用
* 可接受单一可信运营方的场景

## 多验证者

应用中不同 Party 托管在不同、独立运营的验证者上。这是 Canton Network 上跨组织应用的标准部署。

**信任模型：** 各组织运营自己的验证者并控制自己的数据。没有单一验证者能看到全部交易——Canton 隐私模型保证每个验证者仅看到涉及其 Party 的交易。同步器将加密交易视图路由到相应验证者。每个 Party 信任自己的验证者运营方。

**适用场景：**

* 跨组织工作流（交易、结算、供应链）
* 各方不愿将数据托付给单一运营方的应用
* Canton Network 上的生产应用

## 多方托管 Party

单个 Party 可同时托管在多个验证者上。一个验证者宕机时，Party 可在其他节点继续操作，无需改动 Daml 逻辑即可提升韧性。

**信任模型：** Party 至少信任一个托管它的验证者。这会削弱对运营方的信任要求——托管该 Party 的所有验证者在达到共识阈值时需一致。若阈值为 1，涉及该 Party 的交易可能由任一托管验证者处理，降低单点故障风险，但需信任多个验证者。

**适用场景：**

* 不能接受单一验证者宕机的高可用需求
* 需要地理冗余的组织
* 在验证者之间逐步迁移

实现细节见 [多方托管](/appdev/deep-dives/multi-hosting)。

## BFT 同步器

Global Synchronizer 本身是去中心化的，由一组 Super Validator（SV）通过拜占庭容错（BFT）共识（CometBFT）运营。单个 SV 无法审查交易或操纵排序。

**信任模型：** Global Synchronizer 可容忍最多三分之一 SV 故障或恶意；只要三分之二 SV 诚实，同步器即正确运行。这是 Canton 在基础设施层提供的最高去中心化程度。

**适用场景：**

* Global Synchronizer 已是 BFT——其上所有应用自动受益
* 多运营方联合运行私有同步器时也可配置 BFT

## 多同步器

Canton 支持验证者同时连接多个同步器。Party 可在 Global Synchronizer 与一个或多个私有（扩展）同步器上拥有合约，并能在其间 **reassign** 合约。

**信任模型：** 不同工作流可有不同信任属性。敏感双边交易可用双方运营的私有同步器，而针对 Canton Coin 的结算发生在公共 Global Synchronizer。

**适用场景：**

* 隐私/性能需求混合的应用
* 既需公共结算又需私有处理的工作流
* 对数据处理位置有监管要求或特殊隐私需求的组织

## 如何选择

合适去中心化程度取决于应用具体需求：

* **从简开始** — 多数应用因跨组织工作流是 Canton 主场景，从多验证者部署起步
* **增加韧性** — 需要高可用时采用多方托管
* **BFT 内置** — 使用 Global Synchronizer 的应用无需额外应用层配置即享有 BFT
* **增强隐私** — 部分工作流需私有处理时使用多同步器

不必一开始就按最高去中心化设计。Canton 允许通过增加验证者、在更多节点托管 Party 或连接新同步器逐步去中心化——**无需修改 Daml 代码**。

## 下一步

* [多方托管](/appdev/deep-dives/multi-hosting) — 跨验证者分布 Party 的实现细节
* [组合与多方工作流](/appdev/deep-dives/composition-multi-party) — 多方交互的 Daml 模式
""",
    },
    "appdev-deep-dives-contracts-and-transactions-in-java": {
        "zhTitle": "Java 中的合约与交易",
        "summary": "通过 Java 客户端与 Daml Codegen 在 Java 应用中读写账本合约与交易。",
        "body": """> 通过 Java 客户端库处理 Daml 合约与交易。

用 Java 编写 Canton Network 应用时，宜使用与原始 Daml 代码相近、又贴近 Java 原生类型的模板与数据类型表示。使用 Daml Codegen for Java 根据 Daml 模型生成 Java 类型，再在读写账本时使用这些类型。

## 配置 Codegen

按 Daml Codegen for Java 文档运行并配置 Java 代码生成器，为项目生成 Java 类。

生成代码外观（内置与用户定义类型）另见 Generated code。

## 在项目中使用生成类

编译生成的 Java 类需在构建工具中加入 Java bindings 库依赖。

在 **Maven** 项目中添加：

```XML theme={"theme":{"light":"github-light","dark":"github-dark"}}
<dependency>
    <groupId>com.daml</groupId>
    <artifactId>bindings-java</artifactId>
    <version>YOUR_SDK_VERSION</version>
</dependency>
```

<Note>
  将 `YOUR_SDK_VERSION` 替换为你的 SDK 版本。
</Note>

可用版本见 Maven Central [Repository]()。

## 使用 Java bindings 访问 gRPC Ledger API

`bindings-java` 库预置生成的 gRPC stub，用于访问 Ledger API。

每个 Ledger API 服务都有对应名称的 Java 类，例如 `CommandSubmissionService` 的 gRPC 对应类为 `CommandSubmissionServiceGrpc`。

### 连接账本

使用 `NettyChannelBuilder.forAddress(..)` 静态方法创建 `ManagedChannel`，再调用各服务的工厂方法创建 stub，例如 `CommandSubmissionServiceGrpc.newFutureStub`。使用 `bindings-java` 提供的辅助类构造请求参数，转换为 proto 消息后调用服务方法。

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Create a managed channel object pointing to the Ledger API address.
ManagedChannel channel = NettyChannelBuilder.forAddress(host, port).usePlaintext().build();

// Create a stub connecting to the desired service on the ledger.
CommandSubmissionServiceFutureStub submissionService = CommandSubmissionServiceGrpc.newFutureStub(channel);

// Create an object representing the service call arguments
CommandsSubmission commandsSubmission = CommandsSubmission.create(...);

// Convert the command submission to a proto data structure
final var request = SubmitRequest.toProto(commandsSubmission);

// Issue the service call
final var response = submissionService.submit(request)
```

### 执行授权

部分账本强制授权，要求每个请求携带访问令牌。详见 Authorization 概述。

若对所有 Ledger API 请求使用同一令牌，可在服务 stub 上使用 `withCallCredentials`，参数为继承自 `CallCredentials` 的类，在 header 中提供令牌。

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class LedgerCallCredentials extends CallCredentials {

    private static Metadata.Key<String> header =
            Metadata.Key.of("Authorization", Metadata.ASCII_STRING_MARSHALLER);

    private final String token;

    public LedgerCallCredentials(String token) {
        super();
        this.token = token;
    }

    @Override
    public void applyRequestMetadata(
            RequestInfo requestInfo, Executor appExecutor, MetadataApplier applier) {
        Metadata metadata = new Metadata();
        metadata.put(LedgerCallCredentials.header, token.startsWith("Bearer ") ? token : "Bearer " + token);
        applier.apply(metadata);
    }
}
```

长期运行的应用若令牌会过期，应在需要时重新加载令牌并显式传入每次调用。

与需验证授权的账本通信时，务必保护通道以防令牌遭受中间人攻击。下一节说明如何启用 TLS。

### 安全连接

`NettyChannelBuilder.forAddress` 创建的 builder 默认使用 TLS，密钥来自配置的 Java Keystore。可通过传入 `SslContext` 调用 `sslContext` 覆盖。

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
NettyChannelBuilder.forAddress(host, port)
            .useTransportSecurity()
            .sslContext(sslContext)
            .build();
```

<Warning>
  也可调用 `usePlaintext()` 配置明文连接。**仅**在连接本地开发用账本时使用。
</Warning>

连接账本的安全通道须配置客户端认证证书，通常由账本运营方提供。

如何用手头证书配置用于客户端认证的 `SslContext`，请参阅 gRPC 关于 OpenSSL TLS 的文档及 `grpc-java` 项目的 HelloWorldClientTls 示例。

## 使用异步 stub

Ledger API gRPC 服务生成多种 stub：阻塞、基于 Future 与异步。**推荐**使用异步方式。上文 `CommandService` 示例中，它们分别称为 `CommandServiceBlockingStub`、`CommandServiceFutureStub` 与 `CommandServiceStub`。

从 Java 应用调用各 gRPC 端点时，创建实现 `onNext`、`onError`、`onComplete` 的 gRPC `StreamObserver`。编解码 gRPC 消息时使用 Java bindings 生成类的 `fromProto` 与 `toProto`。

### 使用 OpenAPI 定义

OpenAPI 定义描述各 Ledger API 服务，可通过 JSON Ledger API 访问。用这些定义将 gRPC 消息编解码为 JSON Ledger API 所需的 JSON 载荷。详见 Get started with Canton and the JSON Ledger API。
""",
    },
    "appdev-deep-dives-external-signing": {
        "zhTitle": "外部签名",
        "summary": "用外部密钥签署 Canton 交易：概述、Party 入网与提交流程。",
        "body": """> 使用外部加密密钥签署 Canton 交易——概述、入网与提交。

# 外部签名

## 你将学到什么

本系列教程介绍如何：

* 使用 Ledger API 以外部密钥入网 Party 并签署交易
* 使用 Ledger API 入网多方托管的外部 Party
* 使用外部签名创建合约
* 使用外部签名在合约上 exercise choice

进阶场景可参考 Admin API 管理 Party 或用外部签名提交更通用的拓扑交易：

* 使用 Admin API 入网外部 Party
* 构建、签署并提交拓扑交易

## 背景

Canton 账本状态由 **Party 拥有的合约** 定义。每份合约规定各方单方面变更共享账本的权利。从 Party 视角，关键活动是 **发起交易** 与 **验证交易**。

**Party** 是账本上的逻辑参与者，其链上表示与状态管理委托给一个或多个所选 **验证者**。因 Canton 隐私特性，只有这些验证者掌握 Party 拥有的全部合约，因而只有它们能权威地验证并确认影响该 Party 合约的交易。

交易只能涉及当前正被托管的 Party；引用无效 Party 的交易会被系统拒绝。

### 拓扑与身份

Party、验证者与同步器在 Canton 中的身份表示为 **唯一标识符**，每个标识符为名称与公钥指纹对 `<prefix>::<fingerprint>`，详见拓扑管理概述。公钥用于最终验证与身份相关的授权。

Party 如何设置由一组拓扑交易定义。这些交易须由所有受影响 Party 与验证者签署并提交到账本。全部拓扑交易之和定义 **拓扑状态**——各方对 Party、密钥、验证者与包的共享认知。

拓扑状态可演进。Party 不绑定初始配置；跨节点复制 Party 是验证者运营方之间的运维流程，不在本节讨论。

### 托管关系

设置 Party 须与一个或多个验证者建立 **托管关系**，通过名为 **party to participant mapping** 的拓扑交易表达，须由 Party 与相关验证者签署。托管关系中，Party 定义用于授权影响其合约的交易的私钥；该私钥可由用户管理，也可将签署委托给验证者。据此区分两类托管：

* **外部 Party**：授权私钥由 Party 用户（终端钱包或后端应用）持有并操作。
* **内部 Party**：验证者密钥代表 Party 授权交易，用户通过 Ledger API 上的 JWT 认证。

内部 Party 运维更简单，无需额外保管私钥，但最终需信任验证者不会滥用私钥授权交易。Party 与 participant 的托管关系通过三类验证者权限定义：

* **Submission**：验证者签名密钥用于授权交易
* **Confirmation**：验证者签名密钥仅用于确认交易
* **Observation**：验证者仅获知并验证状态，无需确认

授予 **Submission** 即该 Party 为内部 Party。若仅授予 **Confirmation** 或 **Observation**，则为外部 Party，须用额外拓扑交易 **party to key mapping** 定义授权密钥。

请继续下一教程了解如何用 Ledger API 入网外部 Party。内部 Party 见 party management 文档。

### 多方托管 Party

为降低对单一验证者的完全信任，Party 可配置托管关系，要求若干验证者批准交易后才视为有效。这又划分部署维度：

* **单托管 Party**：仅由一个验证者托管，最简单，适用于 Party 所有者完全信任该验证者。
* **多方托管 Party**：由多个验证者托管，通过分散信任提升安全与可用性。

请按教程学习如何用 Ledger API 设置多方托管 Party。

概括而言，Party 要使用账本须定义以下拓扑状态：

* Party 名称及其用于授权交易的签名密钥
* 哪些验证者以何种权限与阈值托管该 Party
* 验证拓扑交易签名所需的命名空间委托

托管选择对 Party 的安全与可用性影响重大，请参阅 party trust model 中的信任假设。

### 通过 Admin API 管理拓扑

拓扑系统灵活强大但也复杂。需多方独立签署时，构建、签署与提交流程可能繁琐。拓扑交易也可作为 **proposal** 通过账本分发——proposal 是尚未被所有必要参与者签署的拓扑交易。

与 Party 相关的 Admin API 拓扑管理任务见：

* 使用 Admin API 入网外部 Party
* 构建、签署并提交拓扑交易

### 交易提交

Party 设置完成后即可通过提交创建合约或 exercise choice 的交易使用账本。使用外部密钥授权的 Party，提交流程为：

* 向所选验证者节点提交命令以解释命令并生成结果交易；交易尚未发往账本，而是返回给用户。
* 用 Party 私钥验证并签署交易哈希（对整个结果交易——命令与结果——的承诺）。
* 将预计算交易与签名提交给验证者节点以提交到账本。
* 通过托管该 Party 的验证者节点观察交易结果。

更详细说明见 external signing overview。

注意：签名是对整个交易输出的承诺，而非仅命令。若解释器有误，验证者会拒绝交易。可通过任意节点提交，不限于托管该 Party 的节点。

如何用外部签名密钥提交命令见：创建合约、exercise choice 等教程。
""",
    },
}

def write_doc(slug, data):
    path = OUT / f"{slug}.json"
    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("wrote", path.name)

for slug, data in DOCS.items():
    write_doc(slug, data)

print("count", len(DOCS))
