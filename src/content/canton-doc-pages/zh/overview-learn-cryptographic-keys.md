---
title: "Canton 中的密码学密钥"
slug: "overview-learn-cryptographic-keys"
locale: "zh"
category: "overview"
source_url: "https://docs.canton.network/overview/learn/cryptographic-keys.md"
source_title: "Cryptographic keys in Canton"
tags:
  - overview
  - learn
  - cryptographic-keys
---

# Canton 中的密码学密钥

> Canton 中密钥的存储方式、密钥类型与密钥管理：涵盖离线、内存、KMS 信封加密与完整 KMS 等选项。

本节介绍 Canton 中的密码学密钥。首先概述在 Canton 中存储机密的一般选项，然后概览各类密码学密钥及其在 Canton 中的用途与存储方式。

## 机密存储

本节概述在 Canton 中存储机密的一般选项。

### 明文存储选项

为便于使用，Canton 提供以下无需加密的选项：

* **数据库：** Canton 节点以明文将机密存入数据库。
* **文件：** Canton 节点以明文将机密存入文件。

### 无持久化选项

为更好保护机密，Canton 还提供不持久化的选项：

<div id="storage-option-offline">
  * **离线：** 对部分机密，Canton 允许完全不存储。因此使用机密（如签名、解密）须在 Canton 外部进行。
  * **内存：** Canton 以明文将机密保存在内存中，不写入文件或数据库。
</div>

### 使用密钥管理服务（KMS）的选项

对 Canton 需要持久化的机密，可使用密钥管理服务（KMS）：

* **KMS 信封加密：** Canton 以加密形式在数据库中存储机密，在内存中保持明文。需要解密时，将密文发给 KMS，KMS 解密后将明文返回 Canton。
* **完整 KMS：** KMS 生成并存储机密（通常为私有签名或加密密钥），不向任何人暴露机密。Canton 需要签名时，将数据发给 KMS，KMS 生成数字签名后返回；需要解密时，将密文发给 KMS，KMS 解密后返回明文。

### 带会话签名密钥的 KMS

由于「完整 KMS」延迟较高，Canton 提供以略弱私钥保护换取更低签名延迟的选项。节点将长期私有签名密钥存放在 KMS 中；签名时使用会话签名密钥而非 KMS 中的长期密钥。除签名外，还须附带：(1) 与会话私有签名密钥对应的公钥；(2) 证明会话密钥在限定时段内合法替代长期密钥的证书。长期密钥须签署该证书。

该方式限制 KMS 调用开销——节点仅在轮换会话密钥时访问 KMS（而非每次签名）。

节点在可配置生命周期内以明文将会话签名密钥保存在内存中，不写入磁盘或数据库。为限制密钥泄露影响，节点不接受证书定义时段之外的会话签名密钥签名。

### 会话加密密钥

为降低非对称加解密负载，Canton 改用对称加密，从而大幅减少非对称加密使用。

每个节点有长期非对称加密密钥，存放在数据库或 KMS 中。此外，各节点生成会话对称加密密钥，用于加密需保护的数据。随密文一并发送的是：用接收方长期加密密钥非对称加密后的对应会话加密密钥。

通常数据远大于会话密钥，且节点常需将数据发给多个接收方。在此假设下，会话加密密钥可降低加解密负载，原因包括：

* Canton 只需加密数据一次（而非每个接收方一次），且只发送一份数据密文。
* 对较大数据使用更便宜的对称加密，对较小会话密钥使用更贵的非对称加密。
* 节点可用同一会话密钥加密多段数据；此时接收方仅在首次收到时需解密会话密钥。

Canton 节点在可配置生命周期内、与会话无关地将会话加密密钥以明文保存在内存中，不将明文写入磁盘或数据库。可将会话密钥以加密形式存入数据库。为限制泄露影响，节点在可配置生命周期结束后不再使用会话加密密钥。仅当 d1 与 d2 的 intended recipients 相同，且其间公钥未轮换时，节点才复用同一会话密钥加密 d1 与 d2。

## Canton 密码学密钥概览

本节概述 Canton 如何使用各类密码学密钥。

### TLS 密钥

Canton 节点提供多种 gRPC 与 HTTP API，供客户端与节点交互，例如：

* Participant 节点的 ledger API（提交 ledger 命令、接收 ledger 更新），
* 各类节点的 admin API（管理用途），
* Sequencer 的 API（多播消息），
* Sequencer 间 ordering API（内部通信），
* 健康检查 API。

用户可将节点 API 配置为服务端 TLS，部分情况下还可配置双向 TLS。Canton 在启动时从一个或多个文件读取 TLS 所用密钥；这些文件中的 TLS 密钥为明文。

### 命名空间签名密钥

每个拓扑命名空间有一个公钥签名密钥，称为 `namespace root key`。命名空间即其根密钥的哈希。运营方用与根密钥对应的私钥签署并授权该命名空间的拓扑交易。命名空间可有更多签名密钥，运营方亦可用其授权拓扑交易。

命名空间密钥（根密钥或其他）可授权的拓扑交易示例包括：

* NamespaceDelegation：授权更多密钥管理该命名空间相关拓扑交易，
* OwnerToKeyMapping：将密钥与 Canton 节点关联，
* PartyToParticipant：将 Party 与 participant 关联。

Canton 支持以下私有命名空间密钥存储选项：

* database（默认），
* offline，
* KMS envelope encryption，
* full KMS。

### 节点签名密钥

节点有一个或多个签名密钥，用于：

* Sequencer 客户端认证：与 Sequencer 公共 API 交互时，客户端须提供有效认证令牌。客户端在 challenge-response 协议中签署 Sequencer 生成的 nonce 以获得令牌。

  此外，若请求可能改变 Sequencer 状态，请求须包含发送方签名。

* Sequencer 服务端认证：Sequencer 对其向客户端发出的每个事件签名。

* 处理 Ledger API 命令时，Participant 用其签名密钥签署并认证交易与重新指派协议中的消息，包括 Daml 交易与 reassignments。

* Sequencer 在 ordering 协议中交换消息，用签名密钥认证发送方。

* Participant 用签名密钥签署 ACS commitments。

Canton 支持以下节点签名密钥存储选项：

* database（默认），
* 所有在 KMS 中存储密钥的选项。例外：Canton 不支持对 sequencer 客户端认证使用带会话签名密钥的 KMS。

### 外部 Party 签名密钥

默认情况下，Participant 签署并授权 Daml 交易执行。Alternatively，提交方（external party）可直接签署并授权其拟加入账本的 Daml Transaction，即提交方签署而非提交 Participant。为此，external party 拥有自有签名密钥。

推荐将 external party 签名密钥存为「offline」。其他选项（如 database）技术上可能可行，但不推荐。

### 加密密钥

Participant 提议交易时，将交易分解为 transaction views，并仅向有权查看内容的 Participant 发送各 view。分解对实现子交易隐私至关重要。

Participant 有一个或多个非对称加密密钥。向其他 Participant 发送 view 时须加密，以免 Sequencer 看到 view 内容。Participant 不直接用非对称密钥加密 view，而使用会话加密密钥以提升性能。

除 Participant 外，其他节点（如 Sequencer）也可有加密密钥，但 Canton 目前不使用此类节点的加密密钥。

### 认证与授权令牌

部分 API 要求客户端在每个请求中包含令牌以作认证或授权。Canton 将此类令牌保存在内存中。若令牌已过期或不能证明客户端有权发送请求，节点将拒绝请求。

在接收令牌的 API 上启用 TLS 至关重要，否则攻击者可通过嗅探网络流量获取认证令牌。

Canton 在以下 API 使用令牌：

* Sequencer 公共 API 要求每个请求使用令牌。
* 运营方可为 Participant 在 Ledger API 启用授权；启用后，Ledger API 客户端须在每请求中包含 [JWT](https://jwt.io) 令牌。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
