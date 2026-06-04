---
title: "将验证者连接到多个同步器"
slug: "global-synchronizer-extension-synchronizers-linking-validator-multi-sync"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/linking-validator-multi-sync.md"
source_title: "Connecting a Validator to Multiple Synchronizers"
tags:
  - global-synchronizer
  - extension-synchronizers
  - linking-validator-multi-sync
---

# 将验证者连接到多个同步器

> 将验证者节点连接到多个同步器的操作指南。

> 如何将单个验证者同时连接到全局同步器和私有同步器

Canton 验证者可以同时连接到多个同步器。这是混合部署的基础 - 您的验证者参与全局同步器以实现网络范围的互操作性，同时还连接到一个或多个私有同步器以实现专门的工作流程。

## 多同步器连接如何工作

每个同步器连接都是独立的。您的验证者维护与每个同步器的Sequencer的单独通信通道，并且合约被分配给特定的同步器。当您创建合约时，它会被分配给一个同步器。您稍后可以使用取消分配/重新分配协议将其移动到另一个同步器。

验证者跟踪每个合约所属的同步器并相应地路由交易。如果一笔交易涉及不同同步器上的合约，Canton 会在两者之间同步交易——尽管与单同步器交易相比，这会增加延迟。

## 添加同步器连接

### 通过Canton Console

如果您的验证者已经在运行并连接到全局同步器，您可以在运行时添加私有同步器连接：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ bootstrap.synchronizer(synchronizerName = "private-sync", sequencers = Seq(sequencer1), mediators = Seq(mediator1), synchronizerOwners = Seq(sequencer1), synchronizerThreshold = PositiveInt.one, staticSynchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer))
    res1: PhysicalSynchronizerId = private-sync::122032922613...::35-0
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.connect_local(sequencer1, "private-sync")
```

`alias` 是您选择用于标识同步器的本地名称。它不需要匹配任何网络级名称 - 它仅在本地配置和 API 调用中使用。

要验证连接：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_connected()
    res3: Seq[ListConnected同步器sResult] = Vector(
      ListConnected同步器sResult(
        同步器Alias = 同步器 'private-sync',
        physical同步器Id = private-sync::122032922613...::35-0,
        healthy = true
      )
    )
```

这将返回所有已连接同步器的列表及其状态和同步器 ID。

### 通过管理 API

您还可以通过管理 API 的 gRPC 接口注册新的同步器连接。相关服务是`同步器ConnectivityService`，带有`Connect同步器` RPC：

```protobuf theme={"theme":{"light":"github-light","dark":"github-dark"}}
message Connect同步器Request {
  string 同步器_alias = 1;
  同步器ConnectionConfig config = 2;
}
```

`同步器ConnectionConfig` 包括Sequencer连接 URL 和任何 TLS 设置。

### 通过 Helm 值

对于使用 Helm 部署的验证者，您可以在值文件中声明其他同步器连接，以便在启动时建立它们：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant:
  additional同步器Connections:
    - alias: "private-sync"
      sequencerConnection: "https://sequencer.private-sync.example.com"
    - alias: "consortium-sync"
      sequencerConnection: "https://sequencer.consortium.example.com"
```

## 管理同步器连接

### 列出连接

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_connected()
    res4: Seq[ListConnected同步器sResult] = Vector(
      ListConnected同步器sResult(
        同步器Alias = 同步器 'private-sync',
        physical同步器Id = private-sync::122032922613...::35-0,
        healthy = true
      )
    )
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_registered()
    res5: Seq[(同步器ConnectionConfig, ConfiguredPhysicalSynchronizerId, Boolean)] = Vector(
      (
        同步器ConnectionConfig(
          同步器 = 同步器 'private-sync',
          sequencerConnections = SequencerConnections(
            connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://127.0.0.1:32670
            ),
            sequencer trust threshold = 1,
            sequencer liveness margin = 0,
            submission request amplification = SubmissionRequestAmplification(factor = 1, patience = 0s),
            sequencer connection pool delays = SequencerConnectionPoolDelays(
              minRestartDelay = 0.01s,
              maxRestartDelay = 10s,
              warnValidationDelay = 20s,
              subscriptionRequestDelay = 1s
            )
          ),
          manualConnect = false
        ),
        private-sync::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0,
        true
      )
    )
```

### 与同步器断开连接

您可以断开与同步器的连接而不会丢失合约数据：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.disconnect("private-sync")
```

分配给该同步器的合约保留在您的本地存储中，但在您重新连接之前无法在事务中使用。断开连接并不会取消分配合约——它们仍然与该同步器相关联。

### 重新连接

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.reconnect("private-sync")
    res7: Boolean = true
```

验证者恢复从同步器接收更新，并可以对分配给它的合约进行交易。

## 合同分配和重新分配

当合约创建时，它会被分配给执行创建交易的同步器。您可以通过适当的同步器连接提交命令来控制这一点。

要将合约移动到不同的同步器：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Unassign from current 同步器
val unassignId = participant.ledger_api.commands.重分配.unassign(
  contractId = contractId,
  source = source同步器Id,
  target = 同步器Id
)

// Reassign to target 同步器
participant.ledger_api.commands.重分配.assign(
  unassignId = unassignId,
  source = source同步器Id,
  target = 同步器Id
)
```

合同在取消分配和重新分配之间短暂不可用。源同步器和目标同步器都必须连接到您的验证者，并且合约的所有利益相关者都必须将验证者连接到目标同步器。

## 为合约选择正确的同步器

在决定将合同分配给何处时，请考虑以下因素：

* **谁需要看到它？** 托管合约利益相关者的所有验证者必须连接到合约的同步器。将全局同步器用于涉及外部各方的合同。
* **交易频率** — 高频双边工作流程在私有同步器上运行更高效，您可以在其中控制容量并避免流量费用。
* **结算需求** - 如果合约最终将与 Canton Coin 或 全局同步器 合约交互，请计划重新分配步骤。
* **隐私要求** — 私有同步器上的合约仅由您控制的基础设施处理。在全局同步器上，Sequencer和中介器由超级验证者操作。

## 故障排除

**连接被拒绝或超时：**

* 验证Sequencer URL 是否正确并且可以从验证者的网络访问
* 检查 TLS 证书是否有效且可信
* 确认任何防火墙或网络策略允许到Sequencer端口的出站连接

**连接后未列出同步器：**

* 检查验证者日志是否有连接错误
* 验证同步器是否已初始化且Sequencer是否正常
* 确保验证者的身份在目标同步器上得到授权

**合同重新分配失败：*** 确认您的验证者已连接到源同步器和目标同步器
* 验证所有合约利益相关者都有连接到目标同步器的验证者
* 检查该合约当前没有在另一笔交易中被执行

# 同步器连接

参与者节点通过连接到该同步器的一个或多个Sequencer来连接到该同步器。

一个参与者节点可以同时连接到多个同步器。同步器连接命令允许参与者节点的管理员管理与同步器的连接。

以下部分说明如何管理参与者节点的此类Sequencer连接。

## 连接

### 通过引用连接到Sequencer

要通过引用（本地或远程引用）将参与者节点连接到Sequencer，请按照以下步骤操作。

1. 定义同步器别名。别名是参与者的操作员选择的用于管理连接的名称。例如：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 同步器Alias = "my同步器"
    同步器Alias : String = "my同步器"
```

2. 设置可选的Sequencer连接验证。此参数确定所提供的 Sequencer 连接在持久化之前验证的彻底程度。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerConnectionValidation = com.digitalasset.canton.sequencing.SequencerConnectionValidation.Active
    sequencerConnectionValidation : Active.type = com.digitalasset.canton.sequencing.SequencerConnectionValidation$Active$@e82f02d
```

3.执行`connect_local`命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.connect_local(sequencerReference, 同步器Alias, validation = sequencerConnectionValidation)
```

4. 列出已连接的同步器以验证该连接是否已列出。请参阅检查连接。

### 通过 URL 连接到Sequencer

要连接到远程Sequencer：

1. 从 同步器 Operator 获取Sequencer地址和端口。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerUrl = s"https://${sequencerAddress}:${port}"
    sequencerUrl : String = "https://127.0.0.1:30147"
```

2. 提供定制证书（如有必要）。如果 Sequencer 使用无法使用 JVM 的信任存储自动验证的 TLS 证书（例如自签名证书），则您必须提供自定义证书，以便客户端可以验证 Sequencer 的公共 API TLS 证书。该操作必须信任自定义根 CA。我们假设该根证书由以下方式给出：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val certificatesPath = "tls/root-ca.crt"
    certificatesPath : String = "tls/root-ca.crt"
```

3. 使用 `connect` 控制台命令将参与者连接到序列器。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.connect("my同步器", connection = sequencerUrl, certificatesPath = certificatesPath)
    res6: 同步器ConnectionConfig = 同步器ConnectionConfig(
      同步器 = 同步器 'my同步器',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(
          sequencerAlias = Sequencer 'DefaultSequencer',
          endpoints = https://127.0.0.1:32814,
          transportSecurity,
          customTrustCertificates
        ),
        sequencer trust threshold = 1,
        sequencer liveness margin = 0,
        submission request amplification = SubmissionRequestAmplification(factor = 1, patience = 0s),
        sequencer connection pool delays = SequencerConnectionPoolDelays(
          minRestartDelay = 0.01s,
          maxRestartDelay = 10s,
          warnValidationDelay = 20s,
          subscriptionRequestDelay = 1s
        )
      ),
      manualConnect = false
    )
```

4. 列出已连接的同步器以验证该连接是否已列出。请参阅检查连接。

### 连接到分散的Sequencer

为了增强可靠性和安全性，您可以使用`connect_bft`命令连接到同一同步器的多个Sequencer。

1. 通过引用其公共 API 地址和端口为每个 Sequencer 创建 URL。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Url = s"http://${sequencer1Address}:${sequencer1Port}"
    sequencer1Url : String = "http://0.0.0.0:30143"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Url = s"http://${sequencer2Address}:${sequencer2Port}"
    sequencer2Url : String = "http://127.0.0.1:30145"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Url = s"https://${sequencer3Address}:${sequencer3Port}"
    sequencer3Url : String = "https://127.0.0.1:30147"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Certificate = com.digitalasset.canton.util.BinaryFileUtil.tryReadByteStringFromFile(certificatesPath)
    sequencer3Certificate : com.google.protobuf.ByteString = <ByteString@3fc760d size=1960 contents="-----BEGIN CERTIFICATE-----\nMIIFeTCCA2GgAwIBAgI...">
```

2. 创建Sequencer连接。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val connections = Seq(
     GrpcSequencerConnection.tryCreate(sequencer1Url, sequencerAlias = "sequencer1"),
     GrpcSequencerConnection.tryCreate(sequencer2Url, sequencerAlias = "sequencer2"),
     GrpcSequencerConnection.tryCreate(sequencer3Url, sequencerAlias = "sequencer3", customTrustCertificates = Some(sequencer3Certificate)),
   )
    connections : Seq[GrpcSequencerConnection] = List(
      GrpcSequencerConnection(sequencerAlias = Sequencer 'sequencer1', endpoints = http://0.0.0.0:32810),
      GrpcSequencerConnection(
        sequencerAlias = Sequencer 'sequencer2',
        endpoints = http://127.0.0.1:32812
      ),
      GrpcSequencerConnection(
        sequencerAlias = Sequencer 'sequencer3',
        endpoints = https://127.0.0.1:32814,
        transportSecurity,
        customTrustCertificates
      )
    )
```

3. 通过设置在消息被视为有效之前必须同意的最小Sequencer数量来配置Sequencer信任阈值。

* 默认值：1
* 最大：连接数

例如，将阈值设置为2：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerTrustThreshold = 2
    sequencerTrustThreshold : Int = 2
```

4、【针对连接池】配置Sequencer liveness margin；除了 `sequencerTrustThreshold`-many 之外，这还设置了我们尝试从中读取消息的 Sequencer 连接数。

* 默认值：0
* 较高的值会增加对Sequencer延迟或故障的恢复能力，但 (`sequencerTrustThreshold` + `sequencerLivenessMargin` > 连接数) 没有任何好处。

例如，将活跃度设置为 1：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerLivenessMargin = 1
    sequencerLivenessMargin : Int = 1
```

5. 配置提交请求放大：定义客户端应尝试发送符合重复数据删除条件的提交请求的频率。

* 较高的值会增加系统接受提交请求的机会，但也会增加Sequencer的负载。
* 默认：`SubmissionRequestAmplification.NoAmplification`

在此示例中，我想确保提交请求发送到两个 Sequencer。因此，我将放大系数设置为2，耐心设置为0秒。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val submissionRequestAmplification = SubmissionRequestAmplification(factor = 2, patience = 0.seconds)
    submissionRequestAmplification : SubmissionRequestAmplification = SubmissionRequestAmplification(factor = 2, patience = 0s)
```

6. 使用`connect_bft`命令进行连接。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.connect_bft(
     connections,
     同步器Alias,
     sequencerTrustThreshold = sequencerTrustThreshold,
     sequencerLivenessMargin = sequencerLivenessMargin,
     submissionRequestAmplification = submissionRequestAmplification,
   )
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.list_registered()
    res16: Seq[(同步器ConnectionConfig, ConfiguredPhysicalSynchronizerId, Boolean)] = Vector(
      (
        同步器ConnectionConfig(
          同步器 = 同步器 'my同步器',
          sequencerConnections = SequencerConnections(
            connections = Map(
              Sequencer 'sequencer1' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer1',
                sequencerId = SEQ::sequencer1::1220cb0a22fb...,
                endpoints = http://0.0.0.0:30143
              ),
              Sequencer 'sequencer2' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer2',
                sequencerId = SEQ::sequencer2::12203a55a279...,
                endpoints = http://127.0.0.1:30145
              ),
              Sequencer 'sequencer3' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer3',
                endpoints = https://127.0.0.1:30147,
                transportSecurity,
                customTrustCertificates
              )
            ),
            sequencer trust threshold = 2,
            sequencer liveness margin = 1,
            submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
            sequencer connection pool delays = SequencerConnectionPoolDelays(
              minRestartDelay = 0.01s,
              maxRestartDelay = 10s,
              warnValidationDelay = 20s,
              subscriptionRequestDelay = 1s
            )
          ),
          manualConnect = false
        ),
        da::1220222f081c6c7d7dd4cba1612b1c80e12e0a7c1eef2139be2d928d903fccf9f090::34-0,
        true
      )
    )
```

7. 列出已连接的同步器以验证该连接是否已列出。请参阅检查连接。

## 检查连接

您可以检查已连接的 同步器 连接以及特定连接的配置。

1. 列出已连接的同步器连接。您可以获得所有连接的同步器的同步器别名和同步器 ID：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.list_connected()
    res17: Seq[ListConnected同步器sResult] = Vector(
      ListConnected同步器sResult(
        同步器Alias = 同步器 'my同步器',
        physical同步器Id = da::1220222f081c...::35-0,
        healthy = true
      )
    )
```

您可以使用以下命令检查特定 同步器 连接的配置：

2. 检查特定连接的配置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.config("my同步器")
    res20: Option[同步器ConnectionConfig] = Some(
      value = 同步器ConnectionConfig(
        同步器 = 同步器 'my同步器',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:32810
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:32812
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              sequencerId = SEQ::sequencer3::122076e8bfb8...,
              endpoints = https://127.0.0.1:32814,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 1,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
          sequencer connection pool delays = SequencerConnectionPoolDelays(
            minRestartDelay = 0.01s,
            maxRestartDelay = 10s,
            warnValidationDelay = 20s,
            subscriptionRequestDelay = 1s
          )
        ),
        manualConnect = false
      )
    )
```

## 修改

### 更新 Sequencer 信任阈值您可以修改 Sequencer 信任阈值来控制在消息被视为有效之前必须有多少 Sequencer 同意。

1. 定义有效阈值。将阈值设置在 1 和连接的 Sequencer 数量之间。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.modify("my同步器", _.tryWithSequencerTrustThreshold(1))
```

2. 使用以下命令验证更新的配置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.config("my同步器")
    res22: Option[同步器ConnectionConfig] = Some(
      value = 同步器ConnectionConfig(
        同步器 = 同步器 'my同步器',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:32810
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:32812
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              sequencerId = SEQ::sequencer3::122076e8bfb8...,
              endpoints = https://127.0.0.1:32814,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
          sequencer connection pool delays = SequencerConnectionPoolDelays(
            minRestartDelay = 0.01s,
            maxRestartDelay = 10s,
            warnValidationDelay = 20s,
            subscriptionRequestDelay = 1s
          )
        ),
        manualConnect = false
      )
    )
```

### \[特定于连接池]更新Sequencer liveness margin

您可以修改 Sequencer liveness margin 以控制对故障 Sequencer 的恢复能力。

1. 使用新的活跃度更新配置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.modify("my同步器", _.withSequencerLivenessMargin(0))
```

2. 使用以下命令验证更新的配置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.config("my同步器")
    res22: Option[同步器ConnectionConfig] = Some(
      value = 同步器ConnectionConfig(
        同步器 = 同步器 'my同步器',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:30143
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:30145
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              endpoints = https://127.0.0.1:30147,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
          sequencer connection pool delays = SequencerConnectionPoolDelays(
            minRestartDelay = 0.01s,
            maxRestartDelay = 10s,
            warnValidationDelay = 20s,
            subscriptionRequestDelay = 1s
          )
        ),
        manualConnect = false
      )
    )
```

### 更新请求放大

1.配置提交请求放大。放大使 Sequencer 客户端向多个 Sequencer 发送符合条件的提交请求，以克服故障 Sequencer 中的消息丢失问题。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.modify("my同步器", _.withSubmissionRequestAmplification(SubmissionRequestAmplification.NoAmplification))
```

2. 与上面相同，使用`config`命令验证更新的配置。

### 同步器优先级

当连接多个 同步器 时，交易路由会选择优先级最高的 同步器 提交交易。您可以调整同步器的优先级来控制优先提交的同步器。有关更多详细信息，请参阅多个同步器文档

1. 更新同步器连接的优先级。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.modify("my同步器", _.withPriority(0))
```

2. 同上，使用`config`命令验证更新后的配置。

### 更新自定义 TLS 信任证书

每当信任根发生变化时，客户端都需要相应地更新自定义根证书。要更新自定义 TLS 信任证书，特别是在使用自签名证书作为 TLS Sequencer 连接的信任根时，请执行以下步骤：

1. 从文件加载根证书：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val certificate = com.digitalasset.canton.util.BinaryFileUtil.tryReadByteStringFromFile("tls/root-ca.crt")
    certificate : com.google.protobuf.ByteString = <ByteString@7e88e992 size=1960 contents="-----BEGIN CERTIFICATE-----\nMIIFeTCCA2GgAwIBAgI...">
```

2. 创建一个新的连接实例并将证书传递到该新连接中。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val connection = com.digitalasset.canton.sequencing.GrpcSequencerConnection.tryCreate(sequencerUrl, customTrustCertificates = Some(certificate))
    connection : GrpcSequencerConnection = GrpcSequencerConnection(
      sequencerAlias = Sequencer 'DefaultSequencer',
      endpoints = https://127.0.0.1:30147,
      transportSecurity,
      customTrustCertificates
    )
```

3. 更新参与者节点上的 Sequencer 连接设置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.modify("my同步器", _.copy(sequencerConnections=SequencerConnections.single(connection)))
```

对于调解器，使用类似的方法更新证书设置。

## 断开连接并重新连接

1. 使用带有 同步器 别名的 `disconnect` 命令断开与 同步器 的连接：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.disconnect("my同步器")
```

2. 验证断线情况：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.list_connected().isEmpty
    res29: Boolean = true
```

3. 使用 `reconnect` 命令和 同步器 别名重新连接到特定 同步器：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.reconnect("my同步器")
    res30: Boolean = true
```

4. 要重新连接所有未配置为需要手动连接的同步器，请使用以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.同步器s.reconnect_all()
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
