---
title: "交易失败"
slug: "global-synchronizer-troubleshooting-guide-transaction-failures"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/transaction-failures.md"
source_title: "Transaction Failures"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - transaction-failures
---

# 交易失败

> 授权、包 vetting、超时与 ACS 承诺相关交易失败排查。

> 诊断授权错误、包 vetting失败和交易超时

全局synchronizer上的交易失败会产生指向根本原因的特定错误代码。此页面涵盖三个最常见的类别：授权错误、包 vetting问题和超时。

## 授权错误

当一方尝试执行其无权执行的操作时，就会出现授权失败。

### 缺少签名者

```
INVALID_ARGUMENT: DAML_AUTHORIZATION_ERROR: ... requires authorizers <party-id> but only <other-party-id> were given
```

这意味着该命令缺少必需的签名者。检查：

* Daml模型中模板的签名声明
* 提交方是否被列为合同签字方
* 如果使用多方提交，则所有必需方都包含在`actAs`列表中

### 错误的一方

如果您在加入后立即看到授权错误，请验证您的Party ID 是否与注册的 ID 匹配：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list()
    res1: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = participant1::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

将输出与应用程序配置中的Party ID 进行比较。Party ID 区分大小写，并包含指纹后缀（例如，`验证者::1220abcd...`）。

## 包 vetting问题

包 vetting可确保参与事务的所有验证者都同意正在执行的 Daml 代码。

### DAR 未上传

```
PACKAGE_NOT_FOUND: Could not find package <package-id>
```

将所需的 DAR 上传到您的验证者：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Via REST API
curl -X POST "http://localhost/api/validator/v0/admin/dars" \
  -H "Authorization: Bearer $TOKEN" \
  -F "dar=@path/to/your-app.dar"
```

或通过广东控制台：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res2: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

### DAR 未经对手方审查

即使你的验证者有该包，对方的验证者也必须上传并审核该包。如果您看到：

```
PACKAGE_SELECTION_FAILED: No package found for module <module-name>
```

联系对方的验证者运营商上传并审查相同的 DAR。交易双方都必须拥有可用的包裹。

### 检查审核状态

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list()
    res3: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:57:04.619144Z,
          validUntil = None,
          sequenced = 2026-05-04T17:57:04.369144Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:0508a1646517...),
          serial = PositiveNumeric(value = 2),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = VettedPackages(
          participantId = PAR::participant1::12201ff69b1d...,
          packages = VettedPackage(packageId = 6f8e6085f576..., unbounded),VettedPackage(packageId = 60c61c542207..., unbounded),VettedPackage(packageId = a1fa18133ae4..., unbounded),VettedPackage(packageId = cae345b5500e..., unbounded),VettedPackage(packageId = c3bb0c5d0479..., unbounded),... 29 more
        )
      )
    )
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.list().filter(_.packageId.toString.nonEmpty)
    res4: Seq[PackageDescription] = Vector(
      PackageDescription(
        packageId = 9e70a8b3510d...,
        name = ghc-stdlib-DA-Internal-Template,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 114
      ),
      PackageDescription(
        packageId = 0e4a572ab1fb...,
        name = daml-prim-DA-Internal-Erased,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 98
      ),
      PackageDescription(
        packageId = 5aee9b21b8e9...,
        name = daml-prim-DA-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 17554
      ),
      PackageDescription(
        packageId = 8287d565fd2f...,
        name = CantonExamples,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:57:07.314002Z,
        size = 221449
      ),
      PackageDescription(
        packageId = a1fa18133ae4...,
        name = daml-stdlib-DA-Action-State-Type,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 593
      ),
      PackageDescription(
        packageId = 60c61c542207...,
        name = daml-stdlib-DA-Stack-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 1194
      ),
      PackageDescription(
        packageId = d095a2ccf6dd...,
        name = daml-stdlib-DA-Semigroup-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 426
      ),
      PackageDescription(
        packageId = ee33fb70918e...,
        name = daml-prim-DA-Exception-ArithmeticError,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 286
      ),
      PackageDescription(
        packageId = c280cc3ef501...,
        name = daml-stdlib-DA-Internal-Interface-AnyView-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 826
      ),
      PackageDescription(
        packageId = de2cc2f90eb5...,
        name = canton-builtin-admin-workflow-ping,
        version = 3.4.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 148192
      ),
      PackageDescription(
        packageId = 22ffcbab726e...,
        name = daml-prim,
        version = 0.0.0,
        uploadedAt = 2026-05-04T17:57:07.314002Z,
        size = 286794
      ),
      PackageDescription(
        packageId = e5411f3d75f0...,
        name = daml-prim-DA-Internal-NatSyn,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 109
      ),
      PackageDescription(
        packageId = 7adc4c2d07fa...,
        name = daml-stdlib-DA-Internal-Fail-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 802
      ),
      PackageDescription(
        packageId = 86d888f34152...,
        name = daml-stdlib-DA-Internal-Down,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 258
      ),
    ...
```

## 超时问题

超时表示事务未在允许的窗口内完成。当确认到达太晚时，中介会拒绝交易。

### 流量耗尽

```
MEDIATOR_SAYS_TX_TIMED_OUT: Rejected transaction as the mediator did not receive
sufficient confirmations within the expected timeframe
```

超时的最常见原因是流量平衡耗尽。全球synchronizer上的每笔交易都会消耗流量，您可以用广东币购买流量。

**检查您的流量平衡：**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res5: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

如果余额为零或接近于零，交易将会失败，因为Sequencer不会接受来自验证者的消息。

**充值流量：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
  -H "Authorization: Bearer $TOKEN"
```**启用自动充值**以防止这种情况再次发生。在你的`validator-values.yaml`中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
topup:
  enabled: true
  targetThroughput: 100000
  minTopupInterval: 10m
```

### 缓慢的数据库查询

如果您的验证者有足够的流量，但事务仍然超时，则数据库可能是瓶颈。检查慢速查询：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active' AND (now() - pg_stat_activity.query_start) > interval '5 seconds';
```

未修剪的大型表会导致查询延迟随着时间的推移而增加。如果尚未启用修剪，请执行以下操作：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

### 交易对手无反应

超时错误包括列出 `unresponsiveParties` 的 `context` 字段。如果反应迟钝的一方不是您的，则问题出在交易对手方 - 他们的验证者可能已离线、流量资金不足或遇到自身问题。您无法直接修复此问题；联系对方运营商。

# ACS 承诺故障排除

参与者节点定期生成对活动合约集（ACS）的承诺，并与其相对参与者交换它们。这些承诺用于在参与者之间的公共 ACS 状态上建立不可否认性，这对于修剪参与者状态是必要的。有关承诺的更多信息，请参阅修剪概述部分。

## 错误代码

当参与者节点检测到与对方参与者的 ACS 的分叉、承诺计算缓慢或收到的承诺显示篡改证据时，它会记录警告消息。以下错误代码与故障排除承诺相关，在错误代码参考部分中有详细描述：

* `ACS_COMMITMENT_ALARM`：此警告表示恶意行为。当从对方参与者收到的 ACS 承诺具有无效签名时，以及当参与者从同一对方参与者收到覆盖相同时间间隔的两个正确签名但不同的承诺时，就会发生这种情况。
* `ACS_COMMITMENT_MISMATCH`：此警告表示参与者和一个或多个相对参与者的共同 ACS 状态出现分叉。请查阅运行手册以检查承诺不匹配情况。
* `ACS_MISMATCH_NO_SHARED_CONTRACTS`：此警告表示分叉的一种特殊情况，即对方参与者发送了一段时间的承诺，而该参与者认为在该时间段结束时不存在任何共享的活跃合约。对方参与者将记录一个`ACS_COMMITMENT_MISMATCH`。
* `ACS_COMMITMENT_DEGRADATION`：此警告表明参与节点在承诺计算中落后于某些对应参与者，可能是由于负载过重，并进入追赶模式。对方参与者可能会将该参与者列入黑名单，因为这会阻止他们进行修剪。
* `ACS_COMMITMENT_DEGRADATION_WITH_INEFFECTIVE_CONFIG`：该错误码表示承诺计算出现降级，并且启动了追赶模式，但追赶模式配置无效，不会提高性能。

## 检查工具

检查工具使操作员能够了解其参与者节点与其相对参与者在其 ACS 状态上达成一致的程度。这在两种情况下特别有用：

* 运营商怀疑协议比它可能或应该的要慢，例如，因为承诺监控会在发送或接收承诺时提醒运营商速度减慢。检查工具使操作员能够调查警报的原因：哪些相对参与者落后，落后多远，或者参与者本身是否落后。
* 参与者的 ACS 状态与一个或多个对应参与者的状态之间存在分叉。参与者节点操作员想要了解分叉的上下文，例如分叉是否是瞬态的，分叉是否跨越多个相对参与者还是仅一个，等等。

### 解决承诺缓慢的问题假设运营商通过承诺监控观察到参与者自己的承诺或对方参与者的承诺很慢，或者当运营商在日志中观察到`ACS_COMMITMENT_DEGRADATION`警告时。参与者操作员可以在管理控制台（或通过 gRPC）使用命令 `commitments.lookup_received_acs_commitments` 来了解哪个对方参与者领先于自己的参与者以及领先多远。如果有多个相对参与者领先，则操作员可以尝试将减速开始时相对参与者的承诺周期与参与者的负载、连接性等的任何变化关联起来。

解决 [#27011](https://github.com/DACH-NY/canton/issues/27011) 时进行细化

以下示例显示`participant1`的操作员如何检查synchronizer`synchronizerId`上特定时间段内从所有相对参与者收到的承诺，并通过缓冲承诺进行过滤，这意味着参与者已收到但尚未计算该时间段的承诺：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
import com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.{
  TimeRange,
  SynchronizerTimeRange,
}
participant1.commitments.lookup_received_acs_commitments(
  synchronizerTimeRanges = Seq(
    SynchronizerTimeRange(
      synchronizerId,
      Some(TimeRange(startTimestamp, endTimestamp)),
    )
  ),
  counterParticipants = Seq.empty,
  commitmentState = Seq(ReceivedCmtState.Buffered),
  verboseMode = true,
)
```

输出表明对方参与者`participant2`已在`1970-01-01T00:00:20Z to 1970-01-01T00:00:25Z`和`1970-01-01T00:00:25Z to 1970-01-01T00:00:30Z`期间发送承诺，显示收到的承诺哈希值，但不显示发送承诺，因为参与者尚未计算它们，以及这些承诺被缓冲的状态。

最好是从实际集成测试中生成命令的输出。我们的文档工具支持这一点（请参阅SphinxDocumentationGenerator 及其实现）。相应地转换工具集成测试可能是值得的。 [#27011](https://github.com/DACH-NY/canton/issues/27011)

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Map(synchronizer1::122025ee4d83... ->
  Vector(
    ReceivedAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:20Z, toInclusive = 1970-01-01T00:00:25Z),PAR::participant2::122080ac62a3...,Some(SHA-256:9a5a5575876d...),None,Buffered),
    ReceivedAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:25Z, toInclusive = 1970-01-01T00:00:30Z),PAR::participant2::122080ac62a3...,Some(SHA-256:ac9142943183...),None,Buffered)
  )
)
```

作为另一个示例，假设操作员在日志中观察到`ACS_COMMITMENT_MISMATCH`。操作员可以在管理控制台（或通过 gRPC）使用`commitments.lookup_sent_acs_commitments`作为检查不匹配的第一步。具体地，操作员可以使用该命令来了解参与者与哪些相对参与者不匹配以及不匹配的时间段。然后，操作员可以将不匹配的周期与参与者的潜在修复命令相关联，甚至发现行为不当的相对参与者。

解决 [#27011](https://github.com/DACH-NY/canton/issues/27011) 时进行细化

以下示例显示了`participant1`的操作员如何检查synchronizer`synchronizerId`上特定时间段发送给所有相对参与者的承诺，并通过不匹配的承诺进行过滤：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
import com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.{
  TimeRange,
  SynchronizerTimeRange,
}
participant1.commitments.lookup_sent_acs_commitments(
  synchronizerTimeRanges = Seq(
    SynchronizerTimeRange(
      synchronizerId,
      Some(TimeRange(startTimestamp, endTimestamp)),
    )
  ),
  counterParticipants = Seq.empty,
  commitmentState = Seq(SentCmtState.Mismatch),
  verboseMode = true,
)
```

输出表明参与者`participant1`已发送了`1970-01-01T00:00:40Z to 1970-01-01T00:00:45Z`到`participant2`期间的承诺，显示了发送和接收的承诺的承诺字节串，它们是不同的，因此是不匹配状态。```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Map(synchronizer1::1220087eeae4... ->
  Vector(
    SentAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:40Z, toInclusive = 1970-01-01T00:00:45Z),PAR::participant2::12208336b38e...,Some(SHA-256:1d7e803bed16...),Some(SHA-256:c72753e6adc6...),Mismatch)
  )
)
```

## 处理缓慢的对方参与者

如果参与者操作员观察到对方参与者发送承诺的速度很慢，则该操作员可以选择不等待来自多个synchronizer的特定计数器参与者的承诺。配置位置立即生效。即使参与者错过了这些对方参与者的承诺，或者它收到的承诺不匹配，修剪参与者也可以继续。尽管参与者并不期望来自这些对方参与者的承诺，但它仍然计算并向他们发送承诺，并且它确实处理潜在收到的承诺，例如，记录不匹配警告。

<Note>
  禁用等待承诺会忽略这些相对参与者。参与者被修剪时的不可否认性，但增加了对那些相对参与者和/或网络的故障和减速的修剪弹性。
</Note>

下面展示了`participant1`的算子如何在synchronizer`synchronizerId1`上标记为无等待对方参与者`participant2`。该命令以及本节中的命令也接受多个对方参与者和synchronizer。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.commitments.set_no_wait_commitments_from(Seq(participant2), Seq(synchronizerId1))
```

操作员还可以使用类似的命令为synchronizer `synchronizerId1` 上的对方参与者 `participant2` 重置无等待配置，即等待承诺：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.commitments.set_wait_commitments_from(Seq(participant2), Seq(synchronizerId1))
```

要检索synchronizer`synchronizerId1`以及synchronizer`synchronizerId1`上`participant1`已知的所有参与者的当前无等待配置，无论它们是否连接到`synchronizerId1`，操作员都可以使用以下命令。该命令允许按特定的对方参与者和/或synchronizer进行过滤。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val (participant1FilterNoWaitList, participant1FilterWaitList) =
  participant1.commitments.get_wait_commitments_config_from(Seq(synchronizer1Id), Seq.empty)
```

输出显示`participant2`在`synchronizerId1`上对于`participant1`被标记为不等待，并且`participant1`当前没有等待`synchronizerId1`承诺的参与者。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
(Vector
  (NoWaitCommitments
    (no-wait counter-participant = PAR::participant2::12206a279664..., synchronizers = synchronizer1::1220034cf0b0...)
  ),
Vector()
)
```

<Note>
  添加到无等待的参与者不会影响*默认*或*杰出*对应参与者延迟监控。
</Note>

## 处理缓慢的承诺计算

追赶模式是当参与者发现自己落后时自动触发的行为。synchronizer操作员可以在每个synchronizer的基础上配置追赶模式。

一旦参与者检测到自己落后了多个周期（`nrIntervalsToTriggerCatchUp`，默认值为 2），那么它就会激活跳过周期（`catchUpIntervalSkip`，默认值为 5），以执行更少的计算，从而赶上。这确实意味着其间的所有周期都不会受到分叉检测，并且只会比较间隔跳跃。如果在料斗处没有检测到分叉，则任何潜在的分叉都已自行解决。synchronizer中的另一种配置是`reconciliationInterval`（默认值一分钟），这决定了参与者与计数器参与者执行承诺交换的频率。较低的值意味着更频繁和更快的分叉检测。较高的值意味着较少的计算，但注意到分叉之前的时间较长。追赶模式直接受`reconciliationInterval`影响。使用默认值，一旦参与者发现自己落后了 10 分钟（`reconciliationInterval` \* `nrIntervalsToTriggerCatchUp` \* `catchUpIntervalSkip`），就会触发追赶。

要配置上述参数，请参阅管理动态synchronizer参数中的synchronizer管理部分。

### 分叉故障排除（承诺不匹配）

当操作员在日志中观察到`ACS_COMMITMENT_MISMATCH`时，表明参与者的ACS状态与对方参与者的状态存在偏差。换句话说，两个参与者并未就共享合同达成一致。在下面的示例中，`participant1` 在 `synchronizer1` 收到来自 `participant2` 的 `1970-01-01T00:01:35Z to 1970-01-01T00:01:40Z` 期间的承诺，但收到的承诺与该期间的本地承诺不匹配。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
ACS_COMMITMENT_MISMATCH(5,246a29fb): The local commitment does not match the remote commitment
err-context:
  {
    local=Vector((CommitmentPeriod(fromExclusive = 1970-01-01T00:01:35Z, toInclusive = 1970-01-01T00:01:40Z), SHA-256:cfd7fd917fb9...)),
    remote=AcsCommitment(
      synchronizerId = synchronizer1::1220b9dd1a9f199b898522ec31a8ce3ff098a7ce05b0cd3ce76e0a544959fe58c8e9::34-0,
      sender = PAR::participant2::1220b2063ef1...,
      counterParticipant = PAR::participant1::1220cc59a221...,
      period = CommitmentPeriod(fromExclusive = 1970-01-01T00:01:35Z, toInclusive = 1970-01-01T00:01:40Z),
      commitment = SHA-256:e2c0cf0361cb...
    ),
    synchronizerId=synchronizer1::1220b9dd1a9f...
  }
```

<Note>
  对不匹配进行故障排除需要两个参与操作员进行协作，以确定导致不匹配的原因。不匹配可能由于配置错误而发生，例如，通过维修服务、错误或恶意行为更改合约存储时。不可否认性部分提供了有关分叉的更多详细信息。例如，其中一个参与者可能不知道另一参与者声称在不匹配时间戳处共享的合约，或者它可能过去知道该合约但在不匹配时间戳之前将其停用，或者它可能使该合约处于活动状态但在不同的synchronizer上。因此，解决不匹配问题的结果给出了只有一个参与者认为它与另一参与者共享的每个合约的不匹配类型。
</Note>

如果参与者相互不信任，他们可能希望验证他们在故障排除过程中交换的数据。因此，根据信任级别，这些验证步骤是可选的。

我们按如下方式解决不匹配问题：

1. **检查本地共享合约元数据** 该数据代表`participant1`认为它在`synchronizer1`的时间戳`1970-01-01T00:01:40Z`与对方参与者`participant2`共享的合约集。 `participant1` 的操作者可以通过首先使用lookup\_sent\_acs\_commitments 获取它发送的承诺，然后使用管理控制台中的命令`commitments.open_commitment`（或通过gRPC）打开承诺，如下所示：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val sentCommitmentP1 = participant1.commitments
     .lookup_sent_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant2.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .sentCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val contractsAndReassignmentCountersP1 = participant1.commitments.open_commitment(
     commitment = sentCommitmentP1,
     physicalSynchronizerId = synchronizerId1,
     timestamp = mismatchTimestamp,
     counterParticipant = participant2,
     outputFile = Some(openCmtLocalFilename),
   )
   ```

   其中`mismatchTimestamp = 1970-01-01T00:01:40Z`。如果本地和远程承诺的期末不同，我们采用本地承诺的期末。

   当操作员使用控制台命令时，操作员可以选择将输出写入文件，在本例中为`openCmtLocalFilename`，这对于后续步骤很有用。 `openCmtLocalFilename` 文件中的输出包含本地共享合约 ID 及其重新分配计数器：

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {"cid":"00749df26491a08f246d4cd262307ea0c9676adde3861d6d2c80e081ddd8160430ca1112202942877d5c9e8d6f79d9167f9841fd4fd092ed2c97c47459c2c40f18a236b239","reassignmentCounter":"0"}
   {"cid":"008403c268ce244fda036c7916b1f33885df153e6a4b0f60e3c8724277100b4362ca111220f5a052b1c66024133c844a8e6f67dec9a1d3c6e0cd3cb0023843b10cdeff4126","reassignmentCounter":"0"}
   {"cid":"002e46d505d569ad80638831c5ad043d281960121f8b6a564e18937819cf1c8536ca111220985ed1546f8a45e39626290d80d0640c8663ed13d078f9761b0e1e2bd0c99ec5","reassignmentCounter":"0"}
   {"cid":"00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1","reassignmentCounter":"0"}
   {"cid":"00e577eb32be4082705edcccc231657551b83bef6076fafcd0f3a89f63f09645f3ca1112208604884e3c2d4711bae0ab6178238b36de6ba1e5f5913be6dce2016e6371725a","reassignmentCounter":"0"}
   {"cid":"002d6217d1ea6ff05ca0d089a8988465197e6c5518a9f83cb0dc69611cf0572acbca1112202329ef987c25375e0130580e289df681581dc9439737cd53f3223cb22e7c2ff9","reassignmentCounter":"0"}
   ```

   <Note>
     用于承诺不匹配检查的文件使用`.json`格式；对于某些文件，每一行都是一个 `JSON` 对象，而不是整个文件。尽管如此，我们建议使用提供的工具来读取/写入这些文件，因为文件的内容可能会发生变化。
   </Note>

2. **从对方参与者那里检查对方参与者的共享合约元数据** 该数据表示对方参与者认为它在`synchronizer1`的时间戳`1970-01-01T00:01:40Z`与参与者共享的合约集。 `participant1` 的操作员要求 `participant2` 的操作员运行 `commitments.open_commitment`，对方操作员可能无论如何都打算这样做，因为它还在日志中观察到不匹配警告。

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val sentCommitmentP2 = participant2.commitments
     .lookup_sent_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant1.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .sentCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val contractsAndReassignmentCountersP2 = participant2.commitments.open_commitment(
     commitment = sentCommitmentP2,
     physicalSynchronizerId = synchronizerId1,
     timestamp = mismatchTimestamp,
     counterParticipant = participant1,
     outputFile = Some(openCmtRemoteFilename),
   )
   ```这次`participant2`的操作者检索它在`mismatchTimestamp = 1970-01-01T00:01:40Z`发送给`participant1`的承诺。如果本地和远程承诺的期末不同，我们将采用远程承诺的期末。

   和之前一样，`openCmtRemoteFilename` 文件中的输出包含本地共享合约 ID 及其重新分配计数器：

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {"cid":"00749df26491a08f246d4cd262307ea0c9676adde3861d6d2c80e081ddd8160430ca1112202942877d5c9e8d6f79d9167f9841fd4fd092ed2c97c47459c2c40f18a236b239","reassignmentCounter":"0"}
   {"cid":"008403c268ce244fda036c7916b1f33885df153e6a4b0f60e3c8724277100b4362ca111220f5a052b1c66024133c844a8e6f67dec9a1d3c6e0cd3cb0023843b10cdeff4126","reassignmentCounter":"0"}
   {"cid":"002e46d505d569ad80638831c5ad043d281960121f8b6a564e18937819cf1c8536ca111220985ed1546f8a45e39626290d80d0640c8663ed13d078f9761b0e1e2bd0c99ec5","reassignmentCounter":"0"}
   {"cid":"00e577eb32be4082705edcccc231657551b83bef6076fafcd0f3a89f63f09645f3ca1112208604884e3c2d4711bae0ab6178238b36de6ba1e5f5913be6dce2016e6371725a","reassignmentCounter":"0"}
   {"cid":"002d6217d1ea6ff05ca0d089a8988465197e6c5518a9f83cb0dc69611cf0572acbca1112202329ef987c25375e0130580e289df681581dc9439737cd53f3223cb22e7c2ff9","reassignmentCounter":"0"}
   ```

   `participant2`的操作员可以将`openCmtRemoteFilename`文件发送给`participant1`的操作员。

3. **可选：验证对方参与者数据** `participant1`的运营者可以验证从`participant2`收到的合约元数据是否与从`participant2`收到的承诺相匹配：

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.integration.tests.util.CommitmentTestUtil.computeHashedCommitment
   import com.digitalasset.canton.participant.pruning.OpenCommitmentHelper
   val remoteContractsAndTransferCounters =
     OpenCommitmentHelper.readFromFile(openCmtRemoteFilename)
   val receivedCommitmentP1fromP2 = participant1.commitments
     .lookup_received_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant2.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .receivedCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val receivedOpenedCommitmentP1fromP2 =
     computeHashedCommitment(remoteContractsAndTransferCounters)
   if (receivedOpenedCommitmentP1fromP2 != receivedCommitmentP1fromP2)
     throw new InvalidRequestStateException(
       s"The commitment does not match the opened contract metadata!"
     )
   ```

   其中`openCmtRemoteFilename`是`participant1`的操作员在步骤2中从`participant2`的操作员收到的文件。

   如果此步骤失败，则对方参与者发送了错误的承诺或错误的合约元数据，或者可能两者都发送了。在这种情况下，`participant1`的操作员似乎无法可靠地识别不匹配原因，因为它无法信任`participant2`的操作员的输入，并且不应该继续执行以下故障排除步骤。

4. **识别不匹配的合约** `participant1`的运营者可以通过检查步骤1中的`openCmtLocalFilename`文件中自己的开放承诺输出与步骤2中收到的对方参与者在`openCmtRemoteFilename`文件中的开放承诺输出来识别不匹配的合约。

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.participant.pruning.CommitmentContractMetadata
   import com.digitalasset.canton.participant.pruning.OpenCommitmentHelper
   val contractsAndTransferCounters1 =
     OpenCommitmentHelper.readFromFile(openCmtLocalFilename)
   val contractsAndTransferCountersCounterParticipant1 =
     OpenCommitmentHelper.readFromFile(openCmtRemoteFilename)
   val mismatchingContracts = CommitmentContractMetadata.compare(
     contractsAndTransferCounters1,
     contractsAndTransferCountersCounterParticipant1,
   )
   mismatchingContracts.writeToFile(mismatchingContractsFilename)
   ```如代码摘录所示，操作员可以选择将输出写入文件中，在本例中为`mismatchingContractsFilename`，这对于下一步很有用。

   输出显示不匹配：只有 `participant1` 认为有一份合约处于活动状态。输出还将显示 `participant2` 是否有其认为活跃的合约，但 `participant1` 没有，以及是否存在双方参与者都认为活跃但具有不同重新分配计数器的合约。

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {
     "cidsOnlyLocal": [
       "00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1"
     ],
     "cidsOnlyRemote": [],
     "differentReassignmentCounters": []
   }
   ```

5. **检查不匹配原因** `participant1`的运营者可以通过检查合约`00e773decfb7f537880972943980da..`为何活跃来分析不匹配的根源。操作员可以选择将输出写入文件中，在本例中为`inspectContractsFilename`，如果需要修复 ACS 状态，可以与`participant2` 的操作员交换该输出。

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.participant.pruning.CommitmentInspectContract
   val mismatches = CompareCmtContracts.readFromFile(mismatchingContractsFilename)

   val inspectContracts = participant1.commitments.inspect_commitment_contracts(
     contracts = mismatches.cidsOnlyLocal ++ mismatches.differentReassignmentCounters,
     timestamp = mismatchTimestamp,
     expectedSynchronizerId = synchronizerId1,
     downloadPayload = true,
   )
   CommitmentInspectContract.writeToFile(inspectContractsFilename, inspectContracts)
   ```

   该命令返回参与者从每个synchronizer上从开始到当前时间已知的所有synchronizer上给定合约的合约状态（已创建、已分配、未分配、已存档、未知）。在这种情况下，`inspectContractsFilename`包含参与者知道的所有synchronizer上合约`00e773decfb7f537880972943980da..`的合约状态：

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {
     "cid":"00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1",
     "activeOnExpectedSynchronizer":true,
     "contract":"CgMyLjES4QQKRQDKmKJSNKcVjBs2yEfu9TDXuGxVS8/FDK3F3QxK8tOs58oREiA3S1IQ7INuTTYMHjMRm/fNx6VaEaI/t61bwhf5XN5NexIOQ2FudG9uRXhhbXBsZXMaTApAODIwYTA5MjEzYzgyYmRlNjdmZjUxODEyMWViMTFhYjdjYTUwNTA3MTAzNDIyMDMzNzEyN2UyNjhkMTVkZWI1NhIDSW91GgNJb3Ui3AFq2QEKVgpUOlJwYXJ0aWNpcGFudDE6OjEyMjA4OWRlZjczZGEzYTAzOTkzMDIxZmFjM2Q1NDY5ZDQ5YWJmMzc1NWFhNzJlNTFhNzc0MTEwNWJlMjFmOWVlZGJlClYKVDpScGFydGljaXBhbnQyOjoxMjIwYjdhMzBmMDYwODIxNzU1YzZmNDFlNTg2MDU3NDBiZGE0NWM0ZjM5ZmEzMTVjODAwOThkYTNhZjAwM2FhNzFjOAohCh9qHQoSChAyDjEwMC4wMDAwMDAwMDAwCgcKBUIDVVNECgQKAloAKlJwYXJ0aWNpcGFudDE6OjEyMjA4OWRlZjczZGEzYTAzOTkzMDIxZmFjM2Q1NDY5ZDQ5YWJmMzc1NWFhNzJlNTFhNzc0MTEwNWJlMjFmOWVlZGJlMlJwYXJ0aWNpcGFudDI6OjEyMjBiN2EzMGYwNjA4MjE3NTVjNmY0MWU1ODYwNTc0MGJkYTQ1YzRmMzlmYTMxNWM4MDA5OGRhM2FmMDAzYWE3MWM4OQEtMQEAAAAAQioKJgokCAESICk3eHUEqY8nX3bxxmkk5wkSkfDtDxlKUI52dC38tZU5EB4=",
     "state":[
       {
         "synchronizerId":"synchronizer1::12207195bde33b4c24dac3f1d7105873ff6c6724d9160491386d17d97e910f3155e3",
         "contractState":{"$type":"ContractCreated"}
       }
     ]
   }
   ```

   `participant2`操作员可以执行步骤4和步骤5中的命令检查其侧的不匹配原因，并与`participant1`操作员交换结果，共同识别不匹配的根本原因。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
