---
title: "同步器运维"
slug: "global-synchronizer-extension-synchronizers-synchronizer-operations"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/synchronizer-operations.md"
source_title: "Synchronizer Operations"
tags:
  - global-synchronizer
  - extension-synchronizers
  - synchronizer-operations
---

# 同步器运维

> 引导、配置与运维 Canton 同步器节点。

> 引导、配置和操作 Canton 同步器节点。


本指南假定您熟悉一般同步器概念。请参阅Canton 概览了解更多信息。

## 设置集中同步器

在**集中式**同步器中，操作员可以访问所有 Sequencer 和 Mediator 节点。

集中式同步器的设置和管理是最简单的，但它假设一个完全受信任的实体拥有并操作同步器。

您可以通过指定单个所有者和 1 的 `synchronizerThreshold` 来引导集中式同步器。这分别意味着只有该所有者才能授权同步器上的拓扑更改，并且一个签名就足够了。

首先，确保节点是新鲜的并且尚未初始化：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.initialized()
    res1: Boolean = false
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.initialized()
    res2: Boolean = false
```

现在您可以按如下方式初始化集中同步器：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ bootstrap.synchronizer(
      synchronizerName = "mySynchronizer",
      sequencers = Seq(sequencer1),
      mediators = Seq(mediator1),
      synchronizerOwners = Seq(sequencer1),
      synchronizerThreshold = 1,
      staticSynchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer),
    )
    res3: PhysicalSynchronizerId = mySynchronizer::122032922613...::35-0
```

您可以自定义静态 同步器 参数，而不是使用默认值。有关可用静态同步器参数及其值的更多信息，请参阅参数配置部分。

现在，参与方节点可以通过Sequencer连接到同步器。检查参与方节点是否可以通过`ping`命令使用同步器：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1)
    res5: Duration = 4661 milliseconds
```

## 设置一个去中心化的同步器

本小节涵盖了最常见的情况，其中不同的操作员代表各自的所有者管理**去中心化**同步器节点。这也意味着它们是从单独的控制台环境进行管理的。

在这种情况下，引导过程必须在同步器节点之间同步协调，并通过安全通信通道进行数据的协调和交换。

总而言之，要使用单独的控制台、操作员引导去中心化同步器：

1. 修复初始参数。
2. 交换同步器身份。
3. 共同创建一个去中心化的命名空间（更多信息请参阅 Canton 概述）；每个操作员：
   1. 签署引导拓扑事务。
   2. 与其他运营商交换引导拓扑事务。
   3. 初始化其同步器节点。

本指南使用两个 Sequencer 节点和两个 Mediator 节点。Sequencer节点是同步器所有者，并由代表各自实体的不同操作员进行管理。

下图说明了操作员之间的信息交换：

<div style={{背景：“#ffffff”，填充：“1rem”，borderRadius：“0.5rem”，显示：“内联块”，宽度：“80%”}}>
  <图片src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/decentralized-同步器-bootstrap-data-exchange.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c56d172bd4ddb3e7441e84214215cd9e" alt="去中心化引导期间同步器算子之间信息交换的序列图" style={{width: "100%", display: "block"}} width="671" height="391" data-path="images/docs_website/decentralized-同步器-bootstrap-data-exchange.png" />
</div>

<Note>
  在继续之前，请确保去中心化同步器中的所有节点都已启动。
</Note>

所有同步器所有者必须事先就静态同步器参数达成一致。例如，您可以通过导出和共享包含其定义的文件来实现这一点：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Parameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer)
    同步器Parameters : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 同步器Parameters.writeToFile("tmp/同步器-bootstrapping-files/params.proto")
```

现在创建临时拓扑存储以在两个 Sequencer 控制台中引导同步器的拓扑：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Id = sequencer1.id
    sequencer1Id : SequencerId = SEQ::sequencer1::1220cb0a22fb...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1TempStore = sequencer1.拓扑.stores.create_temporary_拓扑_store("sequencer1-同步器-setup", 同步器Parameters.protocolVersion)
    sequencer1TempStore : 拓扑StoreId.Temporary = Temporary(name = String185(str = "sequencer1-同步器-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Id = sequencer2.id
    sequencer2Id : SequencerId = SEQ::sequencer2::12203a55a279...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2TempStore = sequencer2.拓扑.stores.create_temporary_拓扑_store("sequencer2-同步器-setup", 同步器Parameters.protocolVersion)
    sequencer2TempStore : 拓扑StoreId.Temporary = Temporary(name = String185(str = "sequencer2-同步器-setup"))
```

从两个 Sequencer 控制台导出 Sequencer 和 Mediator 身份：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/mediator1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator2.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/mediator2-identity.proto")
```

从相应的控制台将节点标识导入到相应的临时拓扑存储中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer1-identity.proto", sequencer2TempStore)
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer2-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator2-identity.proto", sequencer2TempStore)
```

使用第一个 Sequencer 的签名提出并导出去中心化命名空间声明：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq1DND = sequencer1.拓扑.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer1TempStore,
      )
    seq1DND : Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq1DND.writeToFile("tmp/同步器-bootstrapping-files/decentralized-namespace.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Id = 同步器Id(UniqueIdentifier.tryCreate("mySynchronizer", seq1DND.mapping.namespace.toProtoPrimitive))
    同步器Id : 同步器Id = mySynchronizer::12209266a807...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val physical同步器Id = PhysicalSynchronizerId(同步器Id, 同步器Parameters.toInternal)
    physical同步器Id : PhysicalSynchronizerId = mySynchronizer::12209266a807...::35-0
```

在第二个 Sequencer 的控制台上，加载第一个 Sequencer 的去中心化命名空间声明，对其进行签名，然后再次共享：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.load_single_from_file(
        "tmp/同步器-bootstrapping-files/decentralized-namespace.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq2DND = sequencer2.拓扑.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer2TempStore,
      )
    seq2DND : Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 12203a55a279...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq2DND.writeToFile("tmp/同步器-bootstrapping-files/decentralized-namespace.proto")
```

使用第二个Sequencer的签名生成同步器引导事务，并与第一个Sequencer共享它们：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Bootstrap =
        sequencer2.拓扑.同步器_bootstrap.download_genesis_拓扑(
          physical同步器Id,
          synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
          sequencers = Seq(sequencer1Id, sequencer2Id),
          mediators = Seq(mediator1.id, mediator2.id),
          outputFile = "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
          store = sequencer2TempStore,
        )
```

在第一个 Sequencer 的控制台上，加载第二个 Sequencer 的去中心化命名空间声明和 同步器 引导事务：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.load_single_from_file(
        "tmp/同步器-bootstrapping-files/decentralized-namespace.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.load_multiple_from_file(
        "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

仍然在第一个 Sequencer 的控制台上，生成并重新导出创世拓扑。这也合并了两个Sequencer的签名：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.同步器_bootstrap.download_genesis_拓扑(
        physical同步器Id,
        synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
        sequencers = Seq(sequencer1Id, sequencer2Id),
        mediators = Seq(mediator1.id, mediator2.id),
        outputFile = "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        store = sequencer1TempStore
      )
```

在第二个 Sequencer 的控制台上，加载第一个 Sequencer 的 同步器 引导事务，其中包含两个 Sequencer 的签名：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.load_multiple_from_file(
        "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

使用来自各自控制台的完全授权的初始拓扑快照引导两个Sequencer：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer1.拓扑.transactions.export_拓扑_snapshot(store = sequencer1TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@79ade368 size=6293 contents="\n\2201\n\303\002\n\f\b\215\317\354\317\006\020\220\347\220\344\001\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Params = StaticSynchronizerParameters.tryReadFromFile("tmp/同步器-bootstrapping-files/params.proto")
    同步器Params : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res33: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer2.拓扑.transactions.export_拓扑_snapshot(store = sequencer2TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@70a7b5d8 size=6289 contents="\n\2141\n\303\002\n\f\b\215\317\354\317\006\020\250\373\260\357\002\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Params = StaticSynchronizerParameters.tryReadFromFile("tmp/同步器-bootstrapping-files/params.proto")
    同步器Params : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res36: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

现在同步器已成功引导并且Sequencer已初始化，请删除临时拓扑存储：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.stores.drop_temporary_拓扑_store(sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.stores.drop_temporary_拓扑_store(sequencer2TempStore)
```

在两个 Sequencer 的控制台上，通过将每个 Mediator 连接到关联的 Sequencer 来初始化它们：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator1.setup.assign(
        physical同步器Id,
        SequencerConnections.single(sequencer1.sequencerConnection),
      )
      mediator1.health.wait_for_initialized()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator2.setup.assign(
        physical同步器Id,
        SequencerConnections.single(sequencer2.sequencerConnection),
      )
      mediator2.health.wait_for_initialized()
```

现在去中心化同步器已完全初始化，参与方节点可以通过其 Sequencer 连接在此同步器上进行操作：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.同步器s.connect_local(sequencer2, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res43: Duration = 2295 milliseconds
```

## 设置一个分散的同步器，其中一部分Sequencer作为所有者

上一小节描述了如何使用多个都是 同步器 所有者的 Sequencer 来引导去中心化 同步器。本小节介绍当只有一部分 Sequencer 是 同步器 所有者时，如何使用多个 Sequencer 引导去中心化 同步器。

与上一小节类似，不同的操作员可以从单独的控制台环境管理不同的同步器节点。引导过程必须在同步器节点之间同步协调，并通过安全通信通道进行数据的协调和交换。

本指南使用四个 Sequencer 节点和两个 Mediator 节点。只有**两个** Sequencer 节点（第一个和第二个）是 同步器 所有者，并且所有四个 Sequencer 节点均由不同的操作员管理。尽管本指南与前一小节共享许多共同的引导命令，但在显示所有者和非所有者 Sequencer 节点应分别执行的命令方面存在细微差别。

<Note>
  在继续之前，请确保去中心化同步器中的所有节点都已启动。
</Note>

所有同步器所有者必须事先就静态同步器参数达成一致。例如，您可以通过导出和共享包含其定义的文件来实现这一点：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Parameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer)
    同步器Parameters : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 同步器Parameters.writeToFile("tmp/同步器-bootstrapping-files/params.proto")
```

现在创建临时拓扑存储以在所有四个 Sequencer 节点的控制台中引导同步器的拓扑：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Id = sequencer1.id
    sequencer1Id : SequencerId = SEQ::sequencer1::1220cb0a22fb...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1TempStore = sequencer1.拓扑.stores.create_temporary_拓扑_store("sequencer1-同步器-setup", 同步器Parameters.protocolVersion)
    sequencer1TempStore : 拓扑StoreId.Temporary = Temporary(name = String185(str = "sequencer1-同步器-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Id = sequencer2.id
    sequencer2Id : SequencerId = SEQ::sequencer2::12203a55a279...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2TempStore = sequencer2.拓扑.stores.create_temporary_拓扑_store("sequencer2-同步器-setup", 同步器Parameters.protocolVersion)
    sequencer2TempStore : 拓扑StoreId.Temporary = Temporary(name = String185(str = "sequencer2-同步器-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Id = sequencer3.id
    sequencer3Id : SequencerId = SEQ::sequencer3::122076e8bfb8...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer4Id = sequencer4.id
    sequencer4Id : SequencerId = SEQ::sequencer4::1220990c49ca...
```

从所有四个 Sequencer 节点的控制台导出 Sequencer 和 Mediator 身份：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/mediator1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator2.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/mediator2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer3.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer3-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer4.拓扑.transactions.export_identity_transactions("tmp/同步器-bootstrapping-files/sequencer4-identity.proto")
```

从相应的控制台将节点标识导入到相应的临时拓扑存储中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer1-identity.proto", sequencer1TempStore)
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer3-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer4-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer2-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer3-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/sequencer4-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.import_拓扑_snapshot_from("tmp/同步器-bootstrapping-files/mediator2-identity.proto", sequencer2TempStore)
```

使用第一个 Sequencer 的签名提出并导出去中心化命名空间声明：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq1DND = sequencer1.拓扑.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer1TempStore,
      )
    seq1DND : Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq1DND.writeToFile("tmp/同步器-bootstrapping-files/decentralized-namespace.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Id = 同步器Id(UniqueIdentifier.tryCreate("mySynchronizer", seq1DND.mapping.namespace.toProtoPrimitive))
    同步器Id : 同步器Id = mySynchronizer::12209266a807...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val physical同步器Id = PhysicalSynchronizerId(同步器Id, 同步器Parameters.toInternal)
    physical同步器Id : PhysicalSynchronizerId = mySynchronizer::12209266a807...::35-0
```

在第二个 Sequencer 的控制台上，加载第一个 Sequencer 的去中心化命名空间声明，对其进行签名，然后再次共享：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.load_single_from_file(
        "tmp/同步器-bootstrapping-files/decentralized-namespace.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq2DND = sequencer2.拓扑.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer2TempStore,
      )
    seq2DND : Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 12203a55a279...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq2DND.writeToFile("tmp/同步器-bootstrapping-files/decentralized-namespace.proto")
```

使用第二个Sequencer的签名生成同步器引导事务，并与第一个Sequencer共享它们：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Bootstrap =
        sequencer2.拓扑.同步器_bootstrap.download_genesis_拓扑(
          physical同步器Id,
          synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
          sequencers = Seq(sequencer1Id, sequencer2Id, sequencer3Id, sequencer4Id),
          mediators = Seq(mediator1.id, mediator2.id),
          outputFile = "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
          store = sequencer2TempStore,
        )
```

在第一个 Sequencer 的控制台上，加载第二个 Sequencer 的去中心化命名空间声明和 同步器 引导事务：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.load_single_from_file(
        "tmp/同步器-bootstrapping-files/decentralized-namespace.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.transactions.load_multiple_from_file(
        "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

仍然在第一个 Sequencer 的控制台上，生成并重新导出创世拓扑。这也合并了两个Sequencer的签名：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.同步器_bootstrap.download_genesis_拓扑(
        physical同步器Id,
        synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
        sequencers = Seq(sequencer1Id, sequencer2Id, sequencer3Id, sequencer4Id),
        mediators = Seq(mediator1.id, mediator2.id),
        outputFile = "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        store = sequencer1TempStore
      )
```

在第二个 Sequencer 的控制台上，加载第一个 Sequencer 的 同步器 引导事务，其中包含两个 Sequencer 的签名：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.transactions.load_multiple_from_file(
        "tmp/同步器-bootstrapping-files/同步器-bootstrap.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

使用来自相应控制台的完全授权的初始拓扑快照引导所有Sequencer。对于作为 同步器 所有者的两个 Sequencer，初始快照已在 同步器 引导过程中本地存在于各自的临时存储中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer1.拓扑.transactions.export_拓扑_snapshot(store = sequencer1TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@784b7f29 size=8481 contents="\n\234B\n\301\002\n\v\b\263\317\354\317\006\020\330\315\317n\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220c...">
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.write_to_file(initialSnapshot, "tmp/同步器-bootstrapping-files/initial-snapshot.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Params = StaticSynchronizerParameters.tryReadFromFile("tmp/同步器-bootstrapping-files/params.proto")
    同步器Params : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res42: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer2.拓扑.transactions.export_拓扑_snapshot(store = sequencer2TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@8eac748 size=8483 contents="\n\236B\n\303\002\n\f\b\263\317\354\317\006\020\330\250\376\227\002\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Params = StaticSynchronizerParameters.tryReadFromFile("tmp/同步器-bootstrapping-files/params.proto")
    同步器Params : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res45: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

对于非所有者 Sequencer，外部共享初始拓扑快照以启用*从创世状态分配*命令。在此示例中，假设第一个 Sequencer 通过共享写入文件在外部与第三和第四个 Sequencer 共享初始拓扑快照：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = utils.read_byte_string_from_file("tmp/同步器-bootstrapping-files/initial-snapshot.proto")
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@4fb0684b size=8481 contents="\n\234B\n\301\002\n\v\b\263\317\354\317\006\020\330\315\317n\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220c...">
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Params = StaticSynchronizerParameters.tryReadFromFile("tmp/同步器-bootstrapping-files/params.proto")
    同步器Params : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      拓扑 change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer3.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res48: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer4.setup.assign_from_genesis_state(initialSnapshot, 同步器Params)
    res49: com.digitalasset.canton.同步器.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

现在同步器已成功引导并且Sequencer已初始化，请删除临时拓扑存储：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.stores.drop_temporary_拓扑_store(sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.拓扑.stores.drop_temporary_拓扑_store(sequencer2TempStore)
```

在两个 Sequencer 所有者的控制台上，通过将每个 Mediator 连接到关联的 Sequencer 来初始化它们：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator1.setup.assign(
        physical同步器Id,
        SequencerConnections.single(sequencer1.sequencerConnection),
      )
      mediator1.health.wait_for_initialized()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator2.setup.assign(
        physical同步器Id,
        SequencerConnections.single(sequencer2.sequencerConnection),
      )
      mediator2.health.wait_for_initialized()
```

现在去中心化同步器已完全初始化，参与方节点可以通过其 Sequencer 连接在此同步器上进行操作：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.同步器s.connect_local(sequencer2, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res56: Duration = 1972 milliseconds
```

## 引导一个许可的同步器

同步器 安全性的第一层是限制对 Sequencer 的公共 API 网络端点的访问。这可以使用标准网络工具（例如防火墙规则和虚拟专用网络）来完成。

单个同步器可以是**开放**，允许任何连接到Sequencer节点的参与者加入并参与网络，或者是**许可**，在这种情况下，同步器所有者需要显式授权参与者，然后才能注册同步器并使用它。

虽然 Canton 架构旨在抵御恶意参与方节点，但明确限制哪些参与方节点可以加入网络构成了有效的第二道防线。

本小节解释如何使去中心化同步器获得许可。为简单起见，它假设单个受信任的操作员从单个控制台环境访问所有节点。

首先，让所有同步器所有者将`入驻Restriction`动态同步器参数设置为`RestrictedOpen`：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Id = sequencer1.同步器_id
    同步器Id : 同步器Id = mySynchronizer::1220a82692ab...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.同步器_parameters.propose_update(同步器Id, _.update(入驻Restriction = 入驻Restriction.RestrictedOpen))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.同步器_parameters.propose_update(同步器Id, _.update(入驻Restriction = 入驻Restriction.RestrictedOpen))
```

现在，当参与方节点尝试加入同步器时，它会被拒绝，因为它是未知的：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.register(sequencer1, alias = synchronizerName, manualConnect = true)
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:同步器InstallationManual - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/INITIAL_ONBOARDING_ERROR(9,87b7eb17): Transport(Status{code=FAILED_PRECONDITION, description=Unable to register 入驻 拓扑 transactions, cause=null})
      Request: Register同步器(SynchronizerConnectionConfig(
      同步器 = 同步器 'mySynchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(sequencerAlias = Sequencer 'sequence ...
      DecodedCantonError(
      code = 'INITIAL_ONBOARDING_ERROR',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "Transport(Status{code=FAILED_PRECONDITION, description=Unable to register 入驻 拓扑 transactions, cause=null})",
      traceId = '87b7eb177d91ea704571712f223280ce',
      context = Seq('participant=>participant1', 'test=>同步器InstallationManual', '同步器=>mySynchronizer')
    )
      Command ParticipantAdministration$同步器s$.register invoked from cmd10000013.sc:1
```

要允许参与方节点加入同步器，必须获得同步器所有者的授权。

首先，将参与方节点的 ID 导出为字符串：

将参与方节点的 ID 提取为字符串：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val participantAsString = participant1.id.toProtoPrimitive
    participantAsString : String = "PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
```

将此字符串传达给同步器所有者，同步器所有者按如下方式导入它：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val participantIdFromString = ParticipantId.tryFromProtoPrimitive(participantAsString)
    participantIdFromString : ParticipantId = PAR::participant1::12201ff69b1d...
```

让所有同步器所有者对参与方节点进行授权：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.participant_同步器_permissions.propose(同步器Id, participantIdFromString, ParticipantPermission.Submission, store = Some(同步器Id))
    res6: Signed拓扑Transaction[拓扑ChangeOp, Participant同步器Permission] = Signed拓扑Transaction(
      拓扑Transaction(
        Participant同步器Permission(
          同步器Id = mySynchronizer::1220a82692ab...,
          participantId = PAR::participant1::12201ff69b1d...,
          permission = Submission
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:0f3f9883b343...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.participant_同步器_permissions.propose(同步器Id, participantIdFromString, ParticipantPermission.Submission, store = Some(同步器Id))
    res7: Signed拓扑Transaction[拓扑ChangeOp, Participant同步器Permission] = Signed拓扑Transaction(
      拓扑Transaction(
        Participant同步器Permission(
          同步器Id = mySynchronizer::1220a82692ab...,
          participantId = PAR::participant1::12201ff69b1d...,
          permission = Submission
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:0f3f9883b343...
      ),
      signatures = 122009299340...,
      proposal
    )
```检查参与方节点是否尚未激活：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.active(synchronizerName)
    res8: Boolean = false
```

当向给定参与方节点发出参与方节点同步器权限时，同步器所有者声明他们同意该参与方节点加入同步器。检查此声明：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.participant_同步器_permissions.list(同步器Id).map(_.item.permission)
    res9: Seq[ParticipantPermission] = Vector(Submission)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.participant_同步器_permissions.list(同步器Id).map(_.item.permission)
    res10: Seq[ParticipantPermission] = Vector(Submission)
```

<Note>
  传播和处理拓扑提案可能需要一些时间，因此您可能必须重试才能看到提交授权。
</Note>

要在同步器上激活参与方节点，请注册参与方节点的签名密钥和“同步器信任证书”（参与方节点自动生成此证书并在初始握手期间将其发送到同步器）。

通过让参与方节点重新连接到同步器来再次触发握手：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.reconnect_all()
```

现在，检查参与方节点是否处于活动状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.active(synchronizerName)
    res12: Boolean = true
```

您还可以通过以下方式确认参与方节点是否处于活动状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.participant_同步器_states.active(同步器Id, participantIdFromString)
    res13: Boolean = true
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.拓扑.participant_同步器_states.active(同步器Id, participantIdFromString)
    res14: Boolean = true
```

最后，检查参与方节点是否健康并且可以使用同步器：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1)
    res15: Duration = 1057 milliseconds
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/operate/new_nodes.rst" hash="9f3029cf" */}

# 添加新节点

## 添加一个新的 Sequencer 到分布式 同步器

您可以将 Sequencer 初始化为常规分布式同步器引导过程的一部分，也可以稍后动态添加新的 Sequencer，如本节所述。

相反的过程记录在Sequencer停用部分中。

### 数据库Sequencer

目前不支持数据库Sequencer。

### BFT Sequencer

1. 假设至少有一个现有 Sequencer 可以访问，请准备一个新的 Sequencer 并确保其正在运行。

2. 使用新 Sequencer、现有 Sequencer 和当前 同步器 所有者的实例引用运行以下 `bootstrap` 命令：

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > bootstrap
   >   .onboard_new_sequencer(
   >     同步器Id.logical,
   >     newSequencerReference,
   >     existingSequencerReference,
   >     synchronizerOwners,
   >     // Avoid issues if things are slow
   >     customCommandTimeout = Some(config.NonNegativeDuration.tryFromDuration(2.minutes)),
   >     isBftSequencer = true,
   >   )
   > ```

3. 使用以下命令为所有 Sequencer 在一个或两个方向上设置新连接：

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > newSequencerReference.bft.add_peer_endpoint(existingSequencerEndpoint)
   > // existingSequencerReference.bft.add_peer_endpoint(newSequencerEndpoint) // Optional, one direction is enough
   > ```
   >
   > 对于新加入的 Sequencer，可以将端点配置为初始网络的一部分。

4. 等待新的 Sequencer 初始化：

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > newSequencerReference.health.wait_for_initialized()
   > ```此时，其他节点应该能够连接到新的 Sequencer。为了避免出现问题，最佳实践是在将节点连接到新加入的 Sequencer 之前至少等待“最大决策持续时间”（`participant_response_timeout` 和 `mediator_reaction_timeout` 动态同步器参数的总和，每个参数默认为 30 秒）。

如果遇到问题，请参阅故障排除指南。

<div className="todo" />

有关必要管理命令的详细信息，请查看参考文档。

### 使用单独的控制台

与使用单独的控制台初始化分布式同步器类似，可以在单独的控制台中动态加载新的 Sequencer，如下所示：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Third sequencer's console:
// * write file with identity 拓扑 transactions
{
  sequencer3.拓扑.transactions.export_identity_transactionsV2(identityFile)
}

// Fist and second sequencers' (i.e., owners) console:
// * load third sequencer's identity transactions
// * add the third sequencer to the sequencer 同步器 state
// * write the 拓扑 snapshot, sequencer snapshot and static 同步器 parameters to files
{
  // Store the third sequencer's identity 拓扑 transactions on the 同步器
  sequencer1.拓扑.transactions
    .import_拓扑_snapshot_fromV2(identityFile, store = 同步器Id)
  sequencer2.拓扑.transactions
    .import_拓扑_snapshot_fromV2(identityFile, store = 同步器Id)

  // wait for the identity transactions to become effective
  sequencer1.拓扑.synchronisation.await_idle()
  sequencer2.拓扑.synchronisation.await_idle()

  // find the current sequencer 同步器 state
  val sequencer同步器State =
    sequencer1.拓扑.sequencers
      .list(store = 同步器Id)
      .headOption
      .getOrElse(sys.error("Did not find sequencer 同步器 state on the 同步器"))

  // add the third sequencer to the 同步器 state
  val threshold = sequencer同步器State.item.threshold
  val activeSequencers = sequencer同步器State.item.active :+ sequencer3.id
  val newSerial = Some(sequencer同步器State.context.serial.increment)
  sequencer1.拓扑.sequencers.propose(
    同步器Id,
    threshold,
    activeSequencers,
    serial = newSerial,
  )
  sequencer2.拓扑.sequencers.propose(
    同步器Id,
    threshold,
    activeSequencers,
    serial = newSerial,
  )
  // wait for the 拓扑 change to be observed by the sequencer
  utils.retry_until_true(commandTimeouts.bounded) {
    sequencer1.拓扑.sequencers
      .list(sequencer1.同步器_id)
      .headOption
      .map(_.item.allSequencers.forgetNE)
      .getOrElse(Seq.empty)
      .contains(sequencer3.id)
  }

  // fetch the 入驻 state and write it to a file
  val 入驻State = sequencer1.setup.入驻_state_for_sequencer(sequencer3.id)
  utils.write_to_file(入驻State, 入驻StateFile)
}

// Third sequencer's console:
// * read the 入驻 state from file
// * initialize the third sequencer with the 入驻 state
{
  val 入驻State = utils.read_byte_string_from_file(入驻StateFile)
  sequencer3.setup.assign_from_入驻_state(入驻State)

  sequencer3.health.initialized() shouldBe true
}
```

## 添加一个新的 Mediator 到分布式 同步器

您可以将中介器初始化为常规分布式同步器引导过程的一部分，也可以稍后动态添加新中介器（如本节中所述）。

1. 准备一个新的Mediator节点并确保其正在运行。

2. 保存新Mediator的身份并将其加载到相关的Sequencer中：

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > val mediator2Identity = mediator2.拓扑.transactions.identity_transactions()
   > sequencer1.拓扑.transactions.load(
   >   mediator2Identity,
   >   store = 同步器1Id,
   >   ForceFlag.AlienMember,
   > )
   > ```

3. 提出一个新的 Mediator 状态，其中包含活跃的 Mediator，包括新加入的 Mediator：

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > sequencer1.拓扑.mediators.propose(
   >   同步器1Id,
   >   threshold = PositiveInt.one,
   >   active = Seq(mediator1.id, mediator2.id),
   >   group = NonNegativeInt.zero,
   > )
   > ```

4. 初始化新的Mediator：> ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > mediator2.setup.assign(
   >   同步器1Id,
   >   SequencerConnections.single(sequencer1.sequencerConnection),
   > )
   > mediator2.health.wait_for_initialized()
   > ```

相反的过程记录在调解器停用部分中。

<div className="todo" />

有关必要管理命令的详细信息，请查看参考文档。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/operate/dynamic_params.rst" hash="e8c87fd8" */}

# 管理动态同步器参数

<div id="dynamic_同步器_parameters">
  除了在 同步器 引导期间指定的静态 同步器 参数之外，您还可以在运行时（当 同步器 运行时）更改一些参数；这些被称为`dynamic 同步器 parameters`。当同步器启动时，动态同步器参数将使用默认值。
</div>

## 获取动态同步器参数

您可以使用以下命令获取所连接的同步器的当前参数：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
myParticipant.拓扑.同步器_parameters.get_dynamic_同步器_parameters(
  同步器Id
)
```

## 更改动态同步器参数

<div id="change_dynamic_同步器_parameters">
  您可以同时设置多个动态参数：
</div>

<div className="todo" />

<div className="todo" />

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mySequencer.拓扑.同步器_parameters
  .propose_update(
    同步器Id,
    _.update(
      confirmationResponseTimeout = 40.seconds,
      mediatorDeduplicationTimeout = 2.minutes,
      preparationTimeRecordTimeTolerance = 1.minute,
      mediatorReactionTimeout = 20.seconds,
      assignmentExclusivityTimeout = 1.second,
      reconciliationInterval = 5.seconds,
      confirmationRequestsMaxRate = 100,
      maxRequestSize = 100000,
      sequencerAggregateSubmissionTimeout = 5.minutes,
      流量Control = Some(
        流量ControlParameters(
          maxBase流量Amount = NonNegativeLong.tryCreate(204800),
          readVsWriteScalingFactor = 200,
          maxBase流量AccumulationDuration = 12.minutes,
          setBalanceRequestSubmissionWindowSize = 10.minutes,
          enforceRateLimiting = false,
          baseEventCost = NonNegativeLong.zero,
        )
      ),
    ),
  )

// For ledger time record time tolerance, use the dedicated set method
mySequencer.拓扑.同步器_parameters
  .set_ledger_time_record_time_tolerance(同步器Id, 60.seconds)
```

<Note>
  当增加`max request size`时，需要重新启动Sequencer节点才能考虑新值。
</Note>

## 从太小的*最大请求大小*中恢复

`MaxRequestSize`是一个动态参数。此参数配置 Sequencer 节点上的 gRPC 通道大小以及允许 Sequencer 客户端传输的最大大小。

如果该参数设置为非常小的值（大致低于`30kb`），Canton 可能会崩溃，因为所有消息都会被Sequencer客户端或Sequencer节点拒绝。这无法通过在控制台中设置更高的值来纠正，因为此更改请求需要通过Sequencer发送，并且也会被拒绝。

要从此崩溃中恢复，您需要在 Sequencer 节点和所有 Sequencer 客户端上配置 `override-max-request-size`。

这意味着您需要修改同步器和参与方节点配置，如下所示：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    sequencer-client.override-max-request-size = 30000
  }
}
participants {
  participant1 {
    sequencer-client.override-max-request-size = 30000
  }
  participant2 {
    sequencer-client.override-max-request-size = 30000
  }
}
mediators {
  mediator1 {
    sequencer-client.override-max-request-size = 30000
  }
}
sequencers {
  sequencer1 {
    # overrides the maxRequestSize in bytes on the sequencer node
    public-api.override-max-request-size = 30000
  }
}
```

配置修改后，断开所有参与节点与同步器的连接，然后重新启动所有节点。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.all.同步器s.disconnect(daName)
nodes.local.stop()
```

然后执行重启：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
nodes.local.start()
participants.all.同步器s.reconnect_all()
```

Canton恢复后，使用admin命令设置`maxRequestSize`值，然后删除上一步添加的配置，最后再次重启。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/operate/流量.rst" hash="0308899a" */}

# Sequencer流量管理

<Note>
  目前，仅拜占庭容错 (BFT) 同步器支持流量管理。
</Note>

本页介绍如何在 同步器 上启用和配置流量管理，以及如何检查和管理其成员的流量平衡。

管理节点流量中讨论了从成员的角度（对于参与方节点和Mediator 节点）检查同步器成员有多少流量。

## 在 同步器 上启用流量管理

通过调整动态同步器参数，可以在现有同步器上启用或禁用流量管理。更多详细信息，请参阅更改动态同步器参数。

首先我们检查一下同步器当前的流量管理状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.同步器_parameters.get_dynamic_同步器_parameters(sequencer1.同步器_id)
    res1: Dynamic同步器Parameters = Dynamic同步器Parameters(
      confirmation response timeout = 30s,
      mediator reaction timeout = 30s,
      assignment exclusivity timeout = 1m,
      ledger time record time tolerance = 1m,
      mediator deduplication timeout = 48h,
      reconciliation interval = 1m,
      confirmation requests max rate = 1000000,
      max request size = 10485760,
      sequencer aggregate submission timeout = 6m,
      ACS commitment catchup = AcsCommitmentsCatchUpParameters(
        catch up interval skip = 5,
        number of intervals to trigger catch up = 2
      ),
      participant 同步器 limits = Participant同步器Limits(
        confirmation requests max rate = 1000000
      ),
      preparation time record time tolerance = 24h,
      入驻 restriction = UnrestrictedOpen
    )
```

如果类型`流量ControlParameters`的字段`流量Control`未设置（上面的输出中不存在）或将`enforceRateLimiting`设置为`false`，则流量管理处于非活动状态。

要启用流量管理，您可以更新动态同步器参数，使用 `enforceRateLimiting = true` 设置 `流量ControlParameters`，并为 `configuration class Scaladoc reference` 中记录的其他参数指定所需值。

<Note>
  如果您使用具有多个所有者的同步器，则需要确保至少由配置的所有者阈值提交启用流量管理的命令。
</Note>

假设`sequencer1`是唯一的同步器所有者，请运行以下命令以启用流量管理：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.canton.config.RequireTypes.{NonNegativeNumeric, PositiveNumeric}
  import com.digitalasset.canton.config.PositiveFiniteDuration
  import com.digitalasset.canton.admin.api.client.data.流量ControlParameters
  val 流量ControlParameters = 流量ControlParameters(
    enforceRateLimiting = true,
    maxBase流量Amount = NonNegativeNumeric.tryCreate(20000L),
    readVsWriteScalingFactor = PositiveNumeric.tryCreate(200),
    maxBase流量AccumulationDuration = PositiveFiniteDuration.ofSeconds(10L),
    setBalanceRequestSubmissionWindowSize = PositiveFiniteDuration.ofMinutes(5L),
    baseEventCost = NonNegativeNumeric.tryCreate(500L),
    freeConfirmationResponses = false,
  )
  sequencer1.拓扑.同步器_parameters.propose_update(
    同步器Id = sequencer1.同步器_id,
    _.update(流量Control = Some(流量ControlParameters)),
  )
```

让我们再次检查同步器参数来确认流量管理现已启用：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.拓扑.同步器_parameters
  .get_dynamic_同步器_parameters(sequencer1.同步器_id)
    res3: Dynamic同步器Parameters = Dynamic同步器Parameters(
      confirmation response timeout = 30s,
      mediator reaction timeout = 30s,
      assignment exclusivity timeout = 1m,
      ledger time record time tolerance = 1m,
      mediator deduplication timeout = 48h,
      reconciliation interval = 1m,
      confirmation requests max rate = 1000000,
      max request size = 10485760,
      sequencer aggregate submission timeout = 6m,
      流量 control = 流量ControlParameters(
        max base 流量 amount = 20000,
        read vs write scaling factor = 200,
        max base 流量 accumulation duration = 10s,
        set balance request submission window size = 5m,
        enforce rate limiting = true,
        base event cost = 500,
        free confirmation responses = false
      ),
      ACS commitment catchup = AcsCommitmentsCatchUpParameters(
        catch up interval skip = 5,
        number of intervals to trigger catch up = 2
      ),
      participant 同步器 limits = Participant同步器Limits(
        confirmation requests max rate = 1000000
      ),
      preparation time record time tolerance = 24h,
      入驻 restriction = UnrestrictedOpen
    )
```

请注意上面输出中的`流量 control`。

## 查看同步器成员最新流量余额

用户可以使用`sequencer.流量_control`下的Canton控制台命令以交互方式检查和修改同步器成员的流量平衡。

要检查 同步器 所有成员的流量平衡，可以使用以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val allMembers流量State = sequencer1.流量_control.流量_state_of_all_members()
  allMembers流量State
    allMembers流量State : com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status = Sequencer流量Status(
      流量StatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            available流量 = 20000
          )
        ),
        MED::mediator1::122009299340... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            available流量 = 20000
          )
        ),
        PAR::participant3::1220d6908163... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            available流量 = 20000
          )
        ),
        PAR::participant2::1220a4d7463b... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            available流量 = 20000
          )
        )
      )
    )
```

如果您只想查看特定成员的流量平衡，可以使用：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.流量_control.流量_state_of_members(Seq(participant1))
    res5: com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status = Sequencer流量Status(
      流量StatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            available流量 = 20000
          )
        )
      )
    )
```

## 为同步器成员充值流量余额<Note>
  成员的流量平衡权利由外部工作流程决定，并通过一个或多个 Sequencer 提交相同的流量平衡进行传达。
</Note>

<Note>
  充值必须由法定人数的Sequencer提交才能生效。这是通过`Sequencer同步器State`拓扑映射的`threshold`参数配置的。
</Note>

<div className="todo" />

我们为会员添加一些流量，例如`participant1`。首先我们需要知道当前的`serial`（每个会员单调递增的`PositiveInt`），它对应于该会员最后一次充值的流量余额。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val nextSerial = allMembers流量State.流量States(participant1).serial
  .getOrElse(PositiveNumeric.tryCreate(1))
  .increment
    nextSerial : PositiveNumeric[Int] = PositiveNumeric(value = 2)
```

现在我们可以提交命令将`participant1`的流量平衡增加`newBalance`：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.流量_control.set_流量_balance(
    member = participant1,
    serial =  nextSerial,
    newBalance = NonNegativeNumeric.tryCreate(1000000L),
  )
```

现在`participant1`的流量平衡已更新。您可以通过再次检查流量状态来验证这一点：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(
    sequencer1.流量_control.流量_state_of_members(Seq(participant1))
      .流量States(participant1)
      .serial
      .exists(_ >= nextSerial)
  )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 流量StateBeforePing = sequencer1.流量_control.流量_state_of_members(Seq(participant1))
  流量StateBeforePing
    流量StateBeforePing : com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status = Sequencer流量Status(
      流量StatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = 流量State(
            extra流量Limit = 1000000,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:38.785734Z,
            serial = 2,
            available流量 = 1020000
          )
        )
      )
    )
```

现在让我们在参与者之间运行`ping`并观察流量消耗：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res10: Duration = 4511 milliseconds
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.health.ping(participant3)
    res11: Duration = 2843 milliseconds
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.流量_control.流量_state_of_all_members()
    res12: com.digitalasset.canton.同步器.sequencer.流量.Sequencer流量Status = Sequencer流量Status(
      流量StatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = 流量State(
            extra流量Limit = 1000000,
            extra流量Consumed = 0,
            base流量Remainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            serial = 2,
            available流量 = 1020000
          )
        ),
        MED::mediator1::122009299340... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 19351,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            available流量 = 19351
          )
        ),
        PAR::participant3::1220d6908163... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 16139,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            available流量 = 16139
          )
        ),
        PAR::participant2::1220a4d7463b... -> Right(
          value = 流量State(
            extra流量Limit = 0,
            extra流量Consumed = 0,
            base流量Remainder = 18160,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            available流量 = 18160
          )
        )
      )
    )
```

观察参与者和中介者的流量平衡减少。

有关流量控制及其配置参数的更多信息，请阅读流量控制概述。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/operate/修剪.rst" hash="bb82d965" */}

# 同步器修剪

## 修剪调解器状态

您可以按照此处的说明为每个调解器设置计划的自动修剪。

您还可以通过调用以下命令来直接修剪中介器而不使用调度：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediator1.修剪.prune()
```

此操作根据配置的默认保留期修剪已处理的排序事件并最终确认响应聚合。

该值默认为 7 天；您可以按如下方式配置它：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
parameters {
  retention-period-defaults {
    mediator = "7 days"
  }
}
```

要选择其他值，您可以更改上面的配置，也可以使用命令`mediator.修剪.prune_with_retention_period`直接指定保留期，甚至使用`mediator.修剪.prune_at`指定要修剪的确切时间戳。

## 修剪 Sequencer 状态

您可以通过调用以下命令来修剪 Sequencer：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val result = sequencer1.修剪.prune()
```

此命令使用配置的 Sequencer 默认保留期来计算要修剪排序事件的时间戳，并返回所修剪内容的描述。

该值默认为 7 天；您可以按如下方式配置它：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
parameters {
  retention-period-defaults {
    sequencer = "7 days"
  }
}
```

或者，您可以使用命令 `sequencer.修剪.prune_with_retention_period` 直接指定保留期，甚至使用 `sequencer.修剪.prune_at` 指定要修剪的确切时间戳。

### 解除由于不活动的Sequencer成员而导致的修剪

所有 Sequencer 客户端（例如参与者或中介者）都会定期确认从 Sequencer 收到的最新事件的时间戳。所有Sequencer都可以看到这些确认，允许Sequencer计算所有客户端已达到的最高时间戳。该时间戳用作安全修剪点。

您可以按如下方式检查 Sequencer 修剪状态：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val status = sequencer1.修剪.status()
```状态包含所有活动客户端的最新确认时间戳，您可以通过调用`status.safe修剪Timestamp`检查计算出的安全剪枝点。 Sequencer 只能在该点之前执行修剪。否则，一个或多个客户端将无法继续操作。

如果 Sequencer 客户端在一段时间内处于非活动状态，则所有 Sequencer 都将被阻止修剪超过该客户端的最新确认时间戳。要解除阻止 Sequencer 在较新的时间戳进行修剪，客户端必须返回并确认较新的事件，或者您必须在 Sequencer 上禁用该客户端。

Sequencer具有强制修剪命令。这些命令与常规修剪命令之间的区别在于，force-prune 命令会禁用阻止在给定时间戳发生修剪的成员。

您可以在给定时间戳强制修剪，如下所示：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val result = sequencer1.修剪.force_prune_at(earliestAck, dryRun = false)
```

将 `dryRun` 设置为 `true` 会生成一个将被禁用的客户端列表（如果有），作为操作的一部分，而不实际执行修剪。要执行修剪操作，请在 `dryRun` 设置为 `false` 的情况下运行。

如果您发现了不需要服务的有问题的客户端，您可以通过调用修复命令`repair.disable_member(client)`直接禁用它。

请注意，当您在 Sequencer 上禁用客户端时，这是本地操作；客户端在未执行相同操作的其他 Sequencer 上仍然处于活动状态。

### BFT 排序者修剪

Sequencer 的 BFT Orderer 层是所有 Sequencer 节点之间就交易顺序达成分布式共识的地方。它有自己独立的一组数据库表以及有关修剪的不同注意事项。

BFT Orderer 将有序事件提供给 Sequencer 层，Sequencer 层存储这些事件并随后将它们提供给 Sequencer 客户端。 BFT Orderer 在将这些数据提供给 Sequencer 层后也需要保留这些数据，因为它可能需要协助其他落后的 BFT Orderer 节点迎头赶上。

您必须选择足够长的修剪保留期，以便 BFT Orderer 节点能够在崩溃和恢复后赶上。

请参阅下面如何使用管理命令手动修剪并检查状态。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer1.bft.修剪.prune(retention = 30.days, minBlocksToKeep = 100)
val status = sequencer1.bft.修剪.status()
```

您还可以使用下面显示的命令以及此处解释的命令为 BFT Orderer 设置计划自动修剪。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer1.bft.修剪.set_bft_schedule(
  cron = "0 0 8 ? * SAT",
  maxDuration = 8.hours,
  retention = 90.days,
  minBlocksToKeep = 50,
)
sequencer1.bft.修剪.set_min_blocks_to_keep(100)
val schedule = sequencer1.bft.修剪.get_bft_schedule()
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/operate/ha.rst" hash="711b141d" */}

# 同步器的高可用性

## 调解员

中介服务采用热备机制，具有任意数量的副本。在调解器故障转移期间，所有正在进行的请求都会被清除。因此，这些请求将在参与者处超时。应用程序需要重试底层命令。

### 运行独立Mediator 节点

同步器可以静态配置为具有单个嵌入式Mediator 节点，也可以配置为与外部中介一起工作。一旦同步器被初始化，就可以在运行时添加更多的中介器。

默认情况下，同步器将运行嵌入式Mediator 节点本身。这在所有同步器功能可以共同位于单个主机上的简单部署中非常有用。在同步器服务在多台计算机上运行的分布式设置中，您可以配置同步器管理器节点并使用外部运行的中介器引导同步器。

Mediator 节点可以按照与 Canton 参与者和同步器相同的方式定义。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    admin-api.port = 5017
  }
```当同步器启动时，它将自动提供有关同步器的嵌入式中介器信息。必须使用运行时管理来初始化外部中介器才能完成同步器初始化。

### 高可用性配置

HA 中介器支持仅在 Canton 的 Daml Enterprise 版本中可用，并且 HA 仅支持 PostgreSQL 和基于 Oracle 的存储。

Mediator 节点副本在 Canton 配置文件中配置为单独的独立Mediator 节点，每个Mediator 节点副本需要进行两处更改：

* 使用相同的存储配置来保证对共享数据库的访问。
* 为每个Mediator 节点副本设置`replication.enabled = true`。

<Note>
  从 canton 2.4.0 开始，使用支持的存储时默认启用中介复制。
</Note>

只有活动Mediator 节点副本必须通过同步器引导命令进行初始化。被动副本通过共享数据库观察初始化情况。

更多副本可以在运行时启动，无需任何额外的设置。它们保持被动状态，直到当前主动Mediator 节点副本出现故障。

## 音序器

基于数据库的Sequencer可以水平扩展并放置在负载均衡器后面，以提供高可用性和性能改进。

使用以下配置为同步器部署多个Sequencer节点：

> * 所有Sequencer节点共享相同的数据库，因此确保每个Sequencer的存储配置匹配。
> * 所有Sequencer节点必须配置`high-availability.enabled = true`。

<Note>
  从 Canton 2.4.0 开始，使用支持的存储时默认启用Sequencer高可用性。
</Note>

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    remote-sequencers {
      sequencer1 {
        # these details are provided to other nodes to use for how they should connect to the sequencer
        public-api {
          address = sequencer1.local
          port = 1235
          tls {
            enabled = true
            trust-collection-file = "community/app/src/test/resources/tls/some.pem"
          }
        }
        # the server used from running administration commands
        admin-api {
          address = sequencer1.local
          port = 1235
        }
      }
    }
  }

```

同步器节点仅支持嵌入式Sequencer，因此必须将使用同步器管理器节点的分布式设置配置为通过将其指向这些外部服务来使用这些Sequencer节点。

配置完成后，必须使用 bootstrap\_同步器 操作过程通过新的外部Sequencer引导同步器。这些Sequencer共享一个数据库，因此只需使用单个实例进行引导，一旦共享数据库具有足够的启动状态，副本就会上线。

由于这些节点可能在单独的进程中运行，因此您可以使用远程管理配置完全在外部运行此命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  remote-sequencers {
    sequencer1 {
      # these details are provided to other nodes to use for how they should connect to the sequencer
      public-api {
        address = sequencer1.local
        port = 1235
      }
      # the server used from running administration commands
      admin-api {
        address = sequencer1.local
        port = 1235
      }
    }
  }
}
```

有两种方法可用于向参与者公开水平缩放的Sequencer实例。

### 总节点数`sequencer.high-availability.total-node-count`参数用于在数据库Sequencer之间划分时间。一旦部署了一组Sequencer节点，就不应更改该参数。由于排序的每条消息必须具有唯一的时间戳，因此Sequencer节点将使用时间戳 `modulo` `total-node-count` 加上自己的索引来创建在并行数据库插入过程中对消息进行排序时不与其他Sequencer节点冲突的时间戳。 Canton 使用微秒，理论最大吞吐量为每个同步器每秒 100 万条消息。现在，这个理论吞吐量在所有Sequencer节点之间平均分配（`total-node-count`）。因此，如果将 `total-node-count` 设置得太高，则Sequencer可能无法以最大理论吞吐量运行。我们建议保留`10`的默认值，因为以上所有解释都只是理论上的，我们还没有看到可以处理理论吞吐量的数据库/硬盘。另请注意，一条消息可能包含多个事件，因此我们在这里讨论的是大量事件。

### 外部负载均衡器

当您有支持负载均衡器的 http2+grpc，并且不能/不想向客户端公开后端Sequencer的详细信息时，建议使用负载均衡器。高级部署还可以支持弹性扩展可用Sequencer的数量，并为此更新集动态重新配置负载均衡器。

用于在没有 TLS 的情况下公开 GRPC 服务的示例 [HAProxy]() 配置如下所示：

前端域\_frontend
绑定 1234 原型 h2
默认\_backend域\_backend

后端域\_backend
选项 httpchk
http 检查连接
http-check 发送 meth GET uri /health
平衡循环赛
服务器sequencer1sequencer1.local:1234 proto h2检查端口8080
服务器sequencer2sequencer2.local:1234 proto h2检查端口8080
服务器sequencer3sequencer3.local:1234 proto h2检查端口8080

请注意，为了快速故障转移，您还需要添加 HTTP 健康检查，否则，您必须等待 TCP 超时发生才能进行故障转移。Sequencer的公共 API 公开了标准 GRPC health [endpoints]()，但 HAProxy 目前不支持这些，因此您需要依靠 HTTP/health 端点。

### 客户端负载均衡

当外部负载均衡服务不可用（或缺乏 http2+grpc 支持）时，建议使用客户端负载均衡，并且Sequencer集是静态的，可以在客户端进行配置。

要简单地指定多个Sequencer，请在注册/连接到同步器时使用 `同步器s.connect_multi` 控制台命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
myparticipant.synchronizers.connect_multi(
  "my_同步器_alias",
  Seq("https://sequencer1.example.com", "https://sequencer2.example.com", "https://sequencer3.example.com")
)
```

有关如何在与其他同步器连接选项结合使用时添加多个Sequencer URL 的更多详细信息，请参阅Sequencer连接文档。同步器连接配置也可以在运行时更改，以添加或替换配置的Sequencer连接。请注意，必须在参与者处断开同步器并重新连接，才能使用更新的配置。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/configure/apis.rst" hash="a0993dd6" */}

# 配置同步器 API

同步器公开两个主要 API，管理 API 和公共 API，而参与方节点公开账本 API 和管理 API。在本节中，我们将解释 API 的用途以及如何配置它们。

有关如何配置端点及其地址、端口、保持活动等的详细信息，请参阅通用 API 文档。

## 配置 Sequencer 公共 API

Sequencer Public API 向其他节点提供服务，以与 同步器 进行连接、身份验证和交换消息。要了解有关 Sequencer 角色的更多信息，请访问 Sequencer 概述页面。

在 Sequencer 节点配置下配置公共 API `public-api`：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    storage.type = memory
    public-api.port = 5001
    admin-api.port = 5002
    sequencer.type = BFT
  }
}
```

<div className="todo" />所有 Sequencer 公共 API 配置参数都有默认值。例如，默认监听地址是`127.0.0.1`。要了解有关参数的更多信息，请查看参考文档。

## 配置 Sequencer 管理 API

Sequencer Admin API 可以在 Sequencer 节点配置下以标准方式进行配置（与公共 API 处于同一级别）。

## 配置调解器管理 API

可以在 Mediator 节点配置下以标准方式配置 Mediator Admin API：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    storage.type = memory
    admin-api.port = 5202
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/configure/sequencer_backend.rst" hash="f62eca63" */}

# 配置Sequencer后端

下页介绍了配置 Sequencer 后端的基础知识。有关更高级的配置，请参阅以下部分：

> * 高可用性
> * 修剪
> * 优化

## 数据库Sequencer

数据库Sequencer当前不受支持，不应配置。

## BFT Sequencer

### 最小 BFT Sequencer后端配置

要使用拜占庭容错 (BFT) Sequencer，请将`type`参数设置为\`sequencer\`下的`BFT`：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    sequencer.type = BFT
    public-api.port = 5001
    admin-api.port = 5002
  }
}
```

请注意，此配置适用于单节点网络；您无法添加对等点。对于多节点网络，请参阅下一节。

### 配置初始对等点（可选）

如果网络包含多个节点，请在`initial-network`下配置服务器端点。在那里，您还可以配置对等端点，或者稍后使用管理命令执行此操作。预配置对等端点可减少手动配置步骤的数量，从而节省时间、减少错误并加速部署过程。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
server-endpoint {
  address = "0.0.0.0"
  port = 31030
  external-address = "127.0.0.1"
  external-port = 31030
  external-tls-config.enabled = false
}
peer-endpoints = [
  {
    address = "127.0.0.1"
    port = 31031
    tls-config.enabled = false
  }
]
```

`server-endpoint`下的`address`和`port`对组成了BFT Sequencer的gRPC服务器侦听的端点。如果未指定`port`，操作系统会为您选择一个。 `external-address` 和 `external-port` 形成其他对等方可以连接的外部可用端点。通常，`external-address`是指向监听端点的反向代理的域名。必须正确配置外部端点，客户端才能成功对服务器进行身份验证。

默认情况下，为外部端点和对等端点启用传输层安全性 (TLS)。为简单起见，它在配置示例中被禁用。但是，建议以标准方式配置它：

> * `tls` 位于 `server-endpoint` 下，用于内部服务器端点
> * 外部端点的 `server-endpoint` 下的 `external-tls-config`
> * 对于对等端点，`tls-config` 在 `peer-endpoints` 下

<div className="todo" />

有关`initial-network`配置的更多详细信息，请查看参考文档。

### 配置身份验证（可选）

默认情况下启用身份验证。可以在`initial-network`下配置`endpoint-authentication`（与`server-endpoint`同级）：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
endpoint-authentication {
  auth-token = {}
}
```

有关身份验证的更多详细信息，请访问安全同步器页面。

### 配置专用存储（可选）

要使用专用存储，请在 `config` 下配置 `storage`，作为顶级 Sequencer 存储配置。

虽然 BFT Sequencer默认使用顶级Sequencer存储，但配置专用存储可提供更大的灵活性。它允许您：

> * 支持不同数据库后端和设置的不同数据读写模式
> * 单独备份

### 配置全网参数

如果更改默认值，请使以下参数在网络中保持同步：> * \`epoch-length\`：所有纪元的长度
> * \`max-requests-in-batch\`：批量中的最大请求数，运行时验证
> * \`max-batches-per-block-proposal\`：每个区块提案的最大批次数，在运行时验证

上述所有参数都位于`config`下，并且在所有 BFT Orderer 节点上必须相同。

相关概念详见BFT Orderer说明页面。

### 配置其他（本地）参数

`config` 下还有其他（本地）配置参数可以更改。

<div className="todo" />

有关详细信息，请查看参考文档。

## 外部音序器

要使用外部 Sequencer（例如 CometBFT），请在 `sequencer` 配置中的 `config` 下配置底层 Sequencer `type`：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer {
    config {
        cometbft-node-host = "127.0.0.1"
        cometbft-node-port = 26627
    }
    type = CometBFT
}
```

每个外部 Sequencer 都需要在类路径上有一个相应的 Sequencer 驱动程序。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/secure/apis.rst" hash="8b67f3f9" */}

# 安全同步器 API

## Sequencer公共 API

### 公共API

同步器配置需要与参与者相同的`Admin API`配置。在`Admin API`旁边，我们需要配置`Public API`，这是所有参与者连接的API。

#### TLS 加密

与管理 API 一样，网络流量可以（并且应该）使用 TLS 进行加密。这对于公共 API 尤为重要。

启用 TLS 加密和服务器端 TLS 身份验证的示例配置部分如下：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.同步器.acme.public-api {
  port = 5028
  address = localhost // defaults to 127.0.0.1
  tls {
    cert-chain-file = "./tls/public-api.crt"
    private-key-file = "./tls/public-api.pem"
    // minimum-server-protocol-version = TLSv1.3, optional argument
    // ciphers = null // use null to default to JVM ciphers
  }
}
```

如果在服务器端使用带有自签名证书的 TLS，我们需要在参与者的 connect 调用期间传递证书链。否则，将使用 Java 运行时的默认根证书。一个例子是：

<div className="todo">
  #22917：修复损坏的文字包括文字包括：：CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/Multi同步器IntegrationTests.scala start-after：architecture-handbook-entry-begin：TlsConnect end-before：architecture-handbook-entry-end：TlsConnect dedent：
</div>

#### 服务器身份验证

Canton 有两种方法来执行服务器身份验证以防止中间人攻击：TLS 和同步器 ID。

如果如上所述在公共 API 上使用 TLS，则 TLS 还负责服务器身份验证。这是TLS的核心功能之一。

服务器认证还可以通过同步器操作员将其同步器身份传递给参与节点操作员并检查该身份是否与同步器报告给参与节点的身份匹配来执行。与所有节点一样，同步器具有与其名称空间根密钥的指纹相对应的身份。它向连接的参与方节点报告其身份，并使用拓扑分类账上该命名空间根密钥授权的密钥对其所有消息进行签名。假设没有关键妥协，这可以保证参与者所报告的身份是真实的。可以使用控制台命令读取唯一连接的同步器的同步器 ID，例如：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.list_connected.last.同步器Id.filterString
```

#### 客户端身份验证

与账本或管理 API 不同，公共 API 使用 Canton 的加密和拓扑状态进行客户端身份验证，而不是相互 TLS (mTLS)。客户端需要分几个步骤连接到公共 API：1. 客户端调用`SequencerConnectService`进行Canton协议版本对齐并获取同步器id。
2. 在第一次连接期间，客户端通过将其最小拓扑状态（身份、密钥委托、公钥）发送到Sequencer来进行注册。
3. 客户端调用 `SequencerAuthenticationService` 使用质询-响应协议进行身份验证，并获取其他Sequencer服务的访问令牌。
4. 客户端使用 3 中的访问令牌连接到主`SequencerService`。

客户端在步骤 2 中提供的信息是可验证的，因为它是密钥的证书链。如果包含的命名空间根密钥指纹未经许可（请参阅`permissioned-同步器`）或者提供的拓扑状态无效，则同步器会拒绝此操作。

在步骤 3 中，客户端声明一个身份，该身份是名称空间根密钥的指纹。如果该身份已注册（如步骤 2 中所做的那样），Sequencer将响应一个质询，其中包含随机数和根据拓扑分类帐为该成员授权的签名密钥的所有指纹。如果通过使用与授权密钥之一匹配的密钥对随机数进行适当签名来成功满足质询，`SequencerAuthenticationService` 将使用一个限时令牌进行响应，该令牌可用于在其他公共 API 服务上以更便宜的方式进行身份验证。

这种针对受限服务的身份验证机制内置于公共Sequencer API 中。您无需执行任何操作即可进行设置；它是自动强制执行的并且无法关闭。

步骤2中生成的token有效期默认为1小时。节点在令牌过期之前会在后台自动更新令牌。令牌和随机数的生命周期可以使用重新配置

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.sequencers.sequencer1.public-api {
    max-token-expiration-interval = 60m
    nonce-expiration-interval = 1m
}
```

但是，我们建议保留默认值。

如上所述，颁发的令牌允许在调用期间提供该令牌的成员在公共Sequencer API 服务上进行身份验证。因此，这些代币属于敏感信息，不得泄露。如果操作员怀疑成员的身份验证令牌已泄露或以某种方式受到损害，他们应使用 `logout` 控制台命令立即撤销该成员的所有有效令牌并关闭Sequencer连接。合法成员通过上述挑战响应协议自动重新连接并获取新的令牌。

根据成员是参与者还是Mediator，命令略有不同，例如：

<div className="todo">
  替换为对命令的引用。第22919章
</div>

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.logout(mysynchronizerAlias)
mediator1.sequencer_connections.logout()
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/secure/limits.rst" hash="3828c946" */}

# 设置Sequencer资源限制

## 防止大请求

最大请求大小是一个动态 同步器 参数。当您更改动态同步器参数时，您会更新 `maxRequestSize` 字段。

## 通过速率限制保护 Sequencer

确认请求最大速率是一个动态同步器参数。当您更改动态同步器参数时，您会更新 `confirmationRequestsMaxRate` 字段。

## 保护拜占庭容错Sequencer免受大请求的影响

启动拜占庭容错 (BFT) 排序程序时，您可以为 `max-request-payload-bytes` 一笔交易可以处理的字节数和 `max-request-in-batch` 批量可以处理的交易数量提供限制。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    public-api.port = 5001
    admin-api.port = 5002
    sequencer {
      config {
        max-request-payload-bytes = 1000000
        max-requests-in-batch = 16
      }
      type = BFT
    }
  }
}
```

<Note>
  请注意，`max-requests-in-batch`是一个网络范围的参数，对于网络中的所有排序者应该是相同的。
</Note>

## 保护Sequencer免受过多的确认为了限制网络上的确认数量，Sequencer可以合并来自同一成员且时间上太接近的确认。您可以通过在 config.php 文件中设置以下值来配置窗口。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers.sequencer1.acknowledgements-conflate-window = "1 minute"
```

## 通过流量管理限制Sequencer提交

您可以通过启用流量管理来保护同步器免受来自其成员的过多流量的影响。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/decommission/index.rst" hash="13c55e5a" */}

# 停用 Canton 节点和 同步器 实体

本指南假设您总体熟悉 Canton，特别是 Canton 身份管理概念和 Canton 控制台的操作。

请注意，虽然始终可以加入新节点，但**已停用的节点或实体将被有效处置，并且无法重新加入同步器**。 **因此，退役是一项不可逆转的操作**。

此外，**退役程序目前处于实验阶段**；无论如何，**强烈建议在停用节点之前备份要停用的节点**。

## 停用Sequencer

Sequencer是同步器消息传递基础设施的一部分，不存储应用程序合约，因此只要采取预防措施避免中断同步服务，它们就是一次性的。具体来说，这意味着确保：

1. 没有活动参与者或活动中介器连接到要停用的Sequencer。
2. 所有活动参与者和调解者都连接到活动Sequencer。

之后，可以通过将Sequencer从同步器的拓扑中删除并最终进行处置来使其退役。

### 断开所有节点与要退役的Sequencer的连接

* 根据中介连接，将连接到要停用的Sequencer的中介器上的Sequencer连接更改为使用另一个活动Sequencer：

<div className="todo">
  #22917: 修复损坏的文字包括文字包括:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala 语言: scala start-after: user-manual-entry-begin: SequencerOffboardingSwitchAwayMediator end-before: user-manual-entry-end: SequencerOffboardingSwitchAwayMediator 缩进：
</div>

* 使用与另一个活动Sequencer的Sequencer连接，将参与者重新连接到同步器，如同步器连接中所述：

<div className="todo">
  #22917: 修复损坏的文字包括文字包括:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala 语言: scala start-after: user-manual-entry-begin: SequencerOffboardingSwitchAwayParticipant end-before: user-manual-entry-end: SequencerOffboardingSwitchAwayParticipant 缩进：
</div>

### 停止序列发生器

Sequencer是同步器的一部分，因为它们的节点 ID 等于同步器 id，这也意味着它们都具有相同的节点 ID。由于Sequencer的身份与同步器的身份相同，因此您应该保持身份和命名空间映射不变。

然而，Sequencer可以使用其自己的与其他Sequencer不同的加密材料。在这种情况下，必须删除其独占拥有的密钥的所有者到密钥的映射：

1. 使用keys.secret.list 命令查找要停用的Sequencer上的密钥。
2. 在这些键中，找到未被其他音序器共享的键。您可以通过对每个节点发出keys.secret.list命令来完成此操作：仅出现在要停用的Sequencer节点上的指纹对应于其独占拥有的密钥。

<div className="todo">
  #22917：修复损坏的参考号。使用 ref:拓扑.owner\_to\_key\_mappings.authorize 命令删除其独占密钥的映射。
</div>

<div className="todo">
  #22917: 修复损坏的文字包括文字包括:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala 语言: scala start-after: user-manual-entry-begin: SequencerOffboardingRemoveExclusiveKeys end-before: user-manual-entry-end: SequencerOffboardingRemoveExclusiveKeys 缩进：
</div>最后，还必须处置退役Sequencer专有的加密材料：

* 如果仅存储在已退役的Sequencer上，则必须与已退役的Sequencer节点一起处理。
* 但是，如果退役Sequencer的密码材料是通过KMS系统管理的，则必须通过KMS进行处置；请参阅您的 KMS 文档和内部程序来处理此问题。 KMS 管理的Sequencer节点的加密材料。

## 停用调解器

中介器也是同步器消息传递基础设施的一部分，并且不存储应用程序合约，因此只要采取预防措施避免中断同步服务，它们就是一次性的。这意味着确保至少有一个中介器保留在同步器上。

<div className="todo">
  #22917：修复损坏的 ref 如果同步器上存在其他调解器，则可以使用单个控制台命令 ref:setup.offboard\_mediator 停用调解器。
</div>

<div className="todo">
  #22917: 修复损坏的文字包括文字包括:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/MediatorOffboardingIntegrationTest.scala 语言: scala start-after: user-manual-entry-begin: OffboardMediator end-before: user-manual-entry-end: OffboardMediator dedent:
</div>

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/同步器/howtos/recover/index.rst" hash="4187dc6f" */}

# 备份与恢复

建议经常备份数据库，以便发生灾难时可以恢复数据。

在恢复的情况下，只要同步器的备份比参与者的备份更新，参与者就可以从同步器重放丢失的数据。

<div className="todo" />

## 备份顺序

重要的是，参与者的备份不能比Sequencer的备份更新，因为这将构成账本分叉。因此，如果您按顺序备份参与者、中介者和排序者数据库，则适用以下限制：

* 在Sequencer之前备份调解者和参与者；否则，他们可能无法重新连接到Sequencer (`ForkHappened`)。调解者和参与者的相对顺序并不重要。

如果您通过一步执行完整的系统备份（例如，使用云 RDS），请确保备份过程中没有任何组件写入数据库。

在从备份恢复同步器的情况下，如果参与者领先于同步器，则参与者将拒绝连接到同步器 (`ForkHappened`)，并且您必须：

* 将参与者的状态恢复到同步器发生灾难之前的备份，或者
* 推出新的同步器作为修复策略，以便从丢失的同步器中恢复

与参与者的 Ledger API 交互的应用程序的状态必须在参与者之前备份，否则必须重置应用程序状态。

## 恢复警告

从备份恢复 Canton 节点时，由于备份点和节点最新状态之间的数据丢失，以下注意事项适用。

### 不完整的命令重复数据删除状态

恢复后，参与者的正在进行的提交跟踪将与备份后参与者发送到Sequencer的内容不同步。如果应用程序重新提交重复的命令，即使参与者应已删除重复命令，它也可能会被接受。

在以下情况下，此跟踪将再次同步：

> * 参与者已处理来自Sequencer的所有事件，并且
> * Sequencer上的队列不包含可再次排序的恢复之前的传输/交易请求的任何提交请求

此类提交请求的最大排序时间为账本时间加上同步器的账本时间记录时间容差。从同步器观察时间戳应该足够了，该时间戳是在参与者在恢复之前停止的时间超过容差的时间之后的。一旦观察到这样的时间戳，正在进行的提交跟踪将再次同步，并且应用程序可以恢复提交具有完整命令重复数据删除保证的命令。

### 应用程序状态重置如果应用程序的状态比参与者的状态新，或者因为应用程序是在参与者之后备份的，或者因为应用程序由不同的组织运行并且没有从备份中恢复，则必须重置应用程序状态。否则，应用程序已经请求并处理了参与者由于备份时间和节点灾难发生时间之间的间隙而丢失的事务。

这包括作为参与者的 Ledger API 客户端的所有应用程序。

### 私钥

假设一个场景，节点需要轮换其加密私钥，该私钥当前存储在节点的数据库中。如果在执行备份之前已在系统中宣布密钥轮换，则新密钥在恢复时将不可用，但系统中的所有其他节点都希望使用新密钥。

为了避免这种情况，请按以下顺序执行关键轮换步骤：

1. 生成新的私钥并存储到数据库中
2、备份数据库
3. 备份完成后，撤销之前的密钥

## Postgres 示例

如果您使用 Postgres 保存参与方节点或同步器数据，您可以创建备份到文件并使用 Postgres 的实用命令 `pg_dump` 和 `pg_restore` 恢复它，如下所示：

将 Postgres 数据库备份到文件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
pg_dump -U <user> -h <host> -p <port> -w -F tar -f <fileName> <dbName>
```

从文件恢复 Postgres 数据库数据：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
pg_restore -U <user> -h <host> -p <port> -w -d <dbName> <fileName>
```

尽管上面显示的方法适用于小型部署，但不建议用于大型部署。为此，我们建议研究增量备份并参考以下资源：

* PostgreSQL 文档：备份和恢复
* 增量备份在 PostgreSQL 中如何工作

## 用于灾难恢复的数据库复制

### 同步复制

我们建议在生产中至少同步器应该使用异地同步复制来运行，以确保同步器的状态始终比参与者的状态更新。然而，为了避免与备份恢复类似的警告，参与者也应该使用同步复制，或者作为手动灾难恢复故障过程的一部分，必须解决这些警告。

数据库备份允许您将分类帐恢复到创建上次备份时的位置。但是，在发生灾难时，创建备份后接受的任何命令都可能会丢失。因此，恢复备份可能会导致数据丢失。

如果此类数据丢失是不可接受的，您需要针对复制数据库运行 Canton，该数据库将其状态复制到另一个站点。如果原始站点因灾难而关闭，Canton 可以根据数据库中的复制状态在另一个站点上启动。至关重要的是，原始站点中没有写入者留在数据库中，因为 Canton 中使用的数据库机制无法跨站点使用以避免多个写入器从而避免数据损坏。

有关如何设置复制数据库以及如何执行故障转移的详细说明，我们参考数据库系统文档，例如PostgreSQL 的高可用性文档。

**强烈建议将复制配置为同步。** 这意味着，只有在将数据库事务持久化到所有数据库副本后，数据库才应将其报告为已成功提交。在 PostgreSQL 中，这对应于设置`synchronous_commit = on`。如果您不遵循此建议，您可能会在数据库故障转移后发现数据丢失和/或损坏状态。启用同步复制可能会影响 Canton 的性能，具体取决于主数据库和异地数据库之间的网络延迟。

对于 PostgreSQL，Canton 努力验证数据库复制配置，如果检测到配置错误，则会失败并显示错误。然而，这种验证是尽力而为的；因此它可能无法检测到不正确的复制配置。对于 Oracle，不会尝试验证数据库配置。总的来说，您不应该依赖 Canton 来检测数据库配置中的错误。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
