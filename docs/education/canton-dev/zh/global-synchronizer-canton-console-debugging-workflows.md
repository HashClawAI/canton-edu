---
title: "调试工作流"
slug: "global-synchronizer-canton-console-debugging-workflows"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/debugging-workflows.md"
source_title: "Debugging Workflows"
tags:
  - global-synchronizer
  - canton-console
  - debugging-workflows
---

# 调试工作流

> 常见 Canton 故障的 Console 逐步诊断流程。

> 使用控制台对常见 Canton 问题进行分步诊断程序

当事务失败、节点断开连接或系统出现异常时，Canton Console 提供诊断问题的工具。本页使用具体的控制台命令介绍常见的调试场景。

## 调试卡住的事务

当提交命令但没有完成事件到达时，事务会出现“卡住”。常见原因：利益相关者的参与者无法访问、所需的包未经过审查或同步器拒绝事务。

### 第 1 步：检查节点健康状况

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res1: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
    Uptime: 19.211042s
    Ports: 
    	ledger: 32794
    	admin: 32795
    	json: 32796
    Connected synchronizers: 
    	da::122032922613...::35-0
    Unhealthy synchronizers: None
    Active: true
    Components: 
    	memory_storage : Ok()
    	connected-synchronizer : Ok()
    	sync-ephemeral-state : Ok()
    	sequencer-client : Ok()
    	acs-commitment-processor : Ok()
    	sequencer-connection-pool : Ok()
    	sequencer-subscription-pool : Ok()
    	internal-sequencer-connection-sequencer1-0 : Ok()
    	subscription-sequencer-connection-sequencer1-0 : Ok()
    Version: 3.6.0-SNAPSHOT
    Supported protocol version(s): 35, dev
```

如果参与者不活跃或没有连接的同步器，则事务无法继续进行。

### 步骤 2：验证同步器连接

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected()
    res2: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'da',
        physicalSynchronizerId = da::122032922613...::35-0,
        healthy = true
      )
    )
```

如果同步器断开连接，请检查网络连接并尝试重新连接：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.reconnect(synchronizerAlias)
    res3: Boolean = true
```

### 第 3 步：检查包裹审查

如果利益相关者的参与者尚未审查所需的包，交易就会失败。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list()
    res4: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:50:08.491115Z,
          validUntil = None,
          sequenced = 2026-05-04T17:50:08.241115Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:8352cebba166...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = VettedPackages(
          participantId = PAR::participant1::12201ff69b1d...,
          packages = VettedPackage(packageId = 6f8e6085f576..., unbounded),VettedPackage(packageId = 60c61c542207..., unbounded),VettedPackage(packageId = a1fa18133ae4..., unbounded),VettedPackage(packageId = cae345b5500e..., unbounded),VettedPackage(packageId = c3bb0c5d0479..., unbounded),... 25 more
        )
      )
    )
```如果包未经审查，请上传并审查它：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list().filter(_.item.packages.exists(_.packageId.toString.contains(targetPackageId)))
    res5: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res6: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

### 第 4 步：检查派对主办情况

验证交易涉及的所有各方均已正确托管：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect("unreachable_synchronizer", "http://non-existent-sequencer.local:12345")
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...
      Request: ConnectSynchronizer(SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'unreachable_synchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(sequencerAlias = Sequ ...
      DecodedCantonError(
      code = 'SYNC_SERVICE_BAD_CONNECTIVITY',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...",
      traceId = 'e3186611ac49ae5f2f63d4b1c5d8f6cd',
      context = Seq(
        'participant=>participant1',
        'test=>DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest',
        'errors=>List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-existent-sequencer.local: nodename nor servname provided, or not known
        non-existent-sequencer.local: nodename nor servname provided, or not known)))'
      )
    )
      Command ParticipantAdministration$synchronizers$.connect invoked from cmd10000021.sc:1
```

如果一方未映射到任何活跃参与者，则同步器无法将事务视图传递给该方的利益相关者。

## 连接问题

### 同步器连接失败

当参与者无法连接到同步器时：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect("unreachable_synchronizer", "http://non-existent-sequencer.local:12345")
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...
      Request: ConnectSynchronizer(SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'unreachable_synchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(sequencerAlias = Sequ ...
      DecodedCantonError(
      code = 'SYNC_SERVICE_BAD_CONNECTIVITY',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...",
      traceId = 'e3186611ac49ae5f2f63d4b1c5d8f6cd',
      context = Seq(
        'participant=>participant1',
        'test=>DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest',
        'errors=>List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-existent-sequencer.local: nodename nor servname provided, or not known
        non-existent-sequencer.local: nodename nor servname provided, or not known)))'
      )
    )
      Command ParticipantAdministration$synchronizers$.connect invoked from cmd10000021.sc:1
```

常见原因：

* 网络防火墙阻止Sequencer端口
* TLS 证书不匹配
* 身份验证令牌已过期或无效
* 排序器端点无法访问

### 验证Sequencer连接（从Sequencer控制台）```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res7: NodeStatus[sequencer1.Status] = Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
    Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
    Uptime: 1m 17.038832s
    Ports: 
    	public: 32798
    	admin: 32799
    Connected participants: 
    	PAR::participant1::12201ff69b1d...
    Connected mediators: 
    	MED::mediator1::122009299340...
    Sequencer: SequencerHealthStatus(active = true)
    details-extra: None
    Components: 
    	memory_storage : Ok()
    	sequencer : Ok()
    Accepts admin changes: true
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

## 身份问题

### 未找到派对

如果参与方 ID 未返回结果：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list().filter(_.party.toProtoPrimitive.startsWith("Bob"))
    res8: Seq[ListPartiesResult] = Vector()
```

该聚会可能由不同的参与者托管，或者聚会到参与者的映射可能尚未传播。拓扑变化需要很短的时间才能分布在整个网络上。

### 多主机提案状态

如果多主机设置未生效：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list_hosting_proposals(synchronizerId, participant1.id)
    res9: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMultiHostingProposal] = Vector(
      ListMultiHostingProposal(
        txHash = SHA-256:f77e8ccd88df...,
        party = Alice::12201ff69b1d...,
        permission = Confirmation$,
        others = PAR::participant2::1220a4d7463b... -> Confirmation$,
        threshold = 1
      )
    )
```

待决提案意味着第二个参与者尚未签署。授权流程请参见[Multi-Hosting](/appdev/deep-dives/multi-hosting)。

## ACS 检验

当应用程序行为异常时，检查活动合约集以验证账本状态：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val contracts = participant1.testing.acs_search(synchronizerAlias, filterTemplate = "Iou:Iou")
    contracts : List[com.digitalasset.canton.protocol.package.ContractInstance] = List(
      ContractInstanceImpl(
        contractId = 185a4f643c67...ca1212207c34f33a...,
        metadata = ContractMetadata(
          signatories = Alice::12201ff69b1d...,
          stakeholders = Alice::12201ff69b1d...
        ),
        created at = 2026-05-04T17:51:39.410348Z
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ s"Found ${contracts.size} active contracts"
    res11: String = "Found 1 active contracts"
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ contracts.headOption.map { c => (c.contractId, c.toLf.arg) }
    res12: Option[(com.digitalasset.canton.protocol.package.LfContractId, com.digitalasset.daml.lf.value.package.Value)] = Some(
      value = (
        V1(
          discriminator = Hash(185a4f643c674e59891e9f4340060205cebdb9b9bee7046a9ea1728f54bd4a3d),
          suffix = Bytes(ca1212207c34f33a388c409c1b4f2bdd5e6cc46625cc8ff16865d5ff363ef1a9550f8c4f)
        ),
        Record(
          tycon = None,
          fields = ImmArray((None,Party(Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c)),(None,Party(Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c)),(None,Record(None,ImmArray((None,Numeric(100.0000000000)),(None,Text(EUR))))),(None,List(FrontStack())))
        )
      )
    )
```

### 比较参与者之间的 ACS

如果两个参与者看到同一方的不同状态，请比较特定模板的 ACS 计数。差异表明存在同步问题 - 检查两个参与者是否连接到同一个同步器并检查了相同的包。

## 诊断检查表

调查任何问题时，请按以下顺序进行操作：

1. **运行状况** — 节点是否正在运行？ `participant.health.status`
2. **连接** — 同步器是否已连接？ `participant.synchronizers.list_connected`
3. **包** — 是否上传并审查了所需的包？ `participant.topology.vetted_packages.list()`
4. **派对** — 派对是否正确举办？ `participant.parties.hosted()`
5. **拓扑** — 参与方到参与者的映射是否正确？ `participant.topology.party_to_participant_mappings.list(syncId)`
6. **ACS** — 账本状态是否符合预期？ `participant.testing.acs_search(...)`

## 后续步骤

* [基本命令](/global-synchronizer/canton-console/essential-commands) — 所有按键命令的快速参考
* [控制台概述](/global-synchronizer/canton-console/console-overview) — 如何在不同环境下访问控制台

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
