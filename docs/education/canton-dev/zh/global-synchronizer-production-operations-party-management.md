---
title: "Party 管理"
slug: "global-synchronizer-production-operations-party-management"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/party-management.md"
source_title: "Party Management"
tags:
  - global-synchronizer
  - production-operations
  - party-management
---

# Party 管理

> 在 Canton 节点上管理 Party 的分配、复制与去中心化设置。

> 管理 Canton 节点上的Party - 分配、复制和去中心化Party设置


Party是与 Daml 账本交互的实体，代表用户或组织。他们可以加入参与者节点，这允许他们提交交易并访问账本。

以下部分介绍如何加入（本地）Party。请参阅以下有关其他类型Party的入职指南：

* 对于去中心化Party，请参阅去中心化方概述文档。
* 对于外部方，请参阅 Onboard 外部方教程。
* 对于已在参与者上托管的Party，请参阅Party 复制文档。

## 通过账本 API 加入新方

如果您有权访问账本 API，则可以使用 `parties` 命令加入新方。该命令只是底层 Ledger API 端点的包器。有关更多信息，请参阅 Ledger API 文档。

1. 定义Party的名称。您可以自由选择名称，但必须符合以下格式：`\[a-zA-Z0-9:-\_ \]`，不得超过 185 个字符，不得使用两个连续的冒号，并且在命名空间中必须唯一。

例如，我们想创建 Party`bob`。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bob = "bob"
    bob : String = "bob"
```

2. 指定应将Party分配到的可选同步器 ID。参与者必须连接到此同步器。如果参与者仅连接到一个同步器，则可以省略此参数，否则需要在每个同步器上显式启用该参与者。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of("my-synchronizer")
    synchronizerId : synchronizerId = da::122032922613...
```

3. 定义可选注释。这些是与此方关联的键值对，并本地存储在此 Ledger API 服务器上。注释对于维护有关分配方的元数据很有用。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3")
    annotations : Map[String, String] = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3")
```

4. 定义可选的身份提供商 ID。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val idpId = "idp-id-" + java.util.UUID.randomUUID().toString
    idpId : String = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.identity_provider_config.create(identityProviderId = idpId, jwksUrl = "https://jwks:900", issuer = java.util.UUID.randomUUID().toString, audience = Option("someAudience"))
    res5: com.digitalasset.canton.ledger.api.IdentityProviderConfig = IdentityProviderConfig(
      identityProviderId = Id(value = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"),
      isDeactivated = false,
      jwksUrl = JwksUrl(value = "https://jwks:900"),
      issuer = "a8f1e514-a622-4a16-bb4c-85bfa83d2545",
      audience = Some(value = "someAudience")
    )
```5. 在“my-synchronizer”上启用该参与者的Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.allocate(bob, annotations = annotations, identityProviderId = idpId, synchronizerId = Some(synchronizerId))
    res6: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

6. 如果您想在第二个同步器上加入队伍，可以通过使用不同的同步器 ID 再次运行 `allocate` 命令来实现。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.allocate(bob, annotations = annotations, identityProviderId = idpId, synchronizerId = Some(synchronizerId))
    res6: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

### 更新派对

1.可以更新一方的注释。为此，请使用 `update` 命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.update(bobPartyId, modifier = _.copy(annotations = Map("foo" -> "bar")), identityProviderId = idpId)
    res9: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("foo" -> "bar"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

2. 您还可以更新一方的身份提供者。为此，请使用 `update_idp` 命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.update_idp(bobPartyId, sourceIdentityProviderId = idpId, targetIdentityProviderId = "")
```

### 寻找派对

要寻找队伍，您可以使用`list`命令。

1. 您可以按身份提供商过滤Party。否则，该参与者托管的所有Party都将被退回。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.list(idpId)
    res11: Seq[parties.PartyDetails] = Vector(
      PartyDetails(
        party = bob::12201ff69b1d...,
        isLocal = false,
        annotations = Map(),
        identityProviderId = ""
      ),
      PartyDetails(
        party = participant1::12201ff69b1d...,
        isLocal = false,
        annotations = Map(),
        identityProviderId = ""
      )
    )
```

## 通过管理 API 加入新队伍

如果您在分配队伍时需要更精细的控制，请使用管理 API。要将新方加入参与者节点，请按照以下步骤操作：

1. 定义Party的名称（与上述规则相同）。例如，我们想创建 Party`alice`。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = "alice"
    alice : String = "alice"
```2. 定义可选的命名空间。默认情况下，Alice 将使用您提交命令的参与者的名称空间。

有关命名空间的更多信息，请参阅命名空间文档。

3. 指定应将Party分配到的可选同步器别名。参与者必须连接到此同步器。如果参与者仅连接到一个同步器，则可以省略此参数，否则需要在每个同步器上显式启用该参与者。

4. 在此参与者上启用Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.enable(alice, 同步器 = Some("my-synchronizer"))
    res13: PartyId = alice::12201ff69b1d...
```

5. 验证该方已加入。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice", filterParticipant = participant1.filterString)
    res14: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
        participants = Vector(
          Participantsynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              同步器Permission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

6. 如果您想在第二个同步器上加入队伍，可以通过使用不同的同步器别名再次运行 `enable` 命令来实现。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.enable("alice", 同步器 = Some("my-second-同步器"))
    res15: PartyId = alice::12201ff69b1d...
```

### 寻找派对

要寻找队伍，您可以使用`list`命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice")
    res16: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
        participants = Vector(
          Participantsynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              同步器Permission(synchronizerId = da::122032922613..., permission = Submission),
              同步器Permission(synchronizerId = acme::122054fe9ea4..., permission = Submission)
            )
          )
        )
      )
    )
```

您还可以按参与者节点和同步器进行过滤。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of("my-synchronizer")
    synchronizerId : synchronizerId = da::122032922613...
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice", filterParticipant = participant1.filterString, synchronizerIds = Set(synchronizerId))
    res18: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
        participants = Vector(
          Participantsynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              同步器Permission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

### 禁用派对

<Warning>
  目前不支持禁用一方，并且被认为是危险的操作。
</Warning>

如果您确定自己在做什么，则可以使用以下命令禁用特定同步器上的一方：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.disable(alicePartyId, 同步器 = Some("my-synchronizer"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.disable(alicePartyId, 同步器 = Some("my-second-同步器"))
```

## 多方主办派对

*多方主办Party*是由多名参与者主办的Party。这就提出了一个问题，如何将Party从一个参与者复制到另一个参与者？

多托管一方的最简单、最安全的方法仅适用于您且该方未参与任何 Daml 交易的情况。否则，您必须执行离线方复制过程。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/operate/parties/party_replication.rst" hash="3d2e1e44" */}

# Party复制

*Party复制*是将现有Party复制到单个同步器**内的其他参与者的过程。在此过程中，已经主持Party的参与者称为“源”参与者，而新参与者称为“目标”参与者。

根据您复制的一方是否已经参与任何 Daml 交易，操作过程的复杂性和风险有很大不同。

因此，在参与者上加入您的派对，并**在使用该派对之前**按照简单的派对复制步骤将其复制到其他参与者。

否则，您必须应用离线方复制过程。

<Note>
  **方复制**与**方迁移**不同。Party迁移包括一个额外的最后步骤，即将Party从其原始参与者中删除（或*脱离*）。

  目前不支持Party退出以及Party迁移。
</Note>

## Party复制授权

### 授权如何运作

Party和新的托管参与者都必须通过发布Party到参与者映射拓扑交易来表示同意。这确保了Party复制的相互协议。

### 外部Party对于外部方，对该方拓扑的更改必须使用外部方的名称空间密钥的签名进行显式授权。每当在操作方法中需要来自一方的授权时，就会在*本地*和*外部*方之间进行区分。外部Party的程序将引用一个抽象函数，该函数授权更新该方的Party到参与者映射：

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
class HostingParticipant:
    participant_uid: str
    permission: Enums.ParticipantPermission

def update_external_party_hosting(
    party_id: str,
    同步器_id: str,
    confirming_threshold: int,
    hosting_participants_add_or_update: [HostingParticipant]
)
```

外部方入职文档中给出了此功能的示例实现。该实现还需要该方命名空间的私钥以及连接到该方确认节点之一的管理 API 的 gRPC 通道。为了简洁起见，上面声明的函数中省略了这些内容。

当`source`参与者在本指南中用于授权拓扑更改以外的操作时，必须使用外部方的现有确认参与者之一。

### 拥有多个所有者的Party

当一方由去中心化命名空间中的一组成员拥有时，这些所有者的最低数量（定义的阈值）必须批准新的托管安排。一旦有足够多的个体所有者各自发出自己的Party到参与者映射拓扑交易，就满足该阈值。

### 激活

完成相互授权过程*激活*目标参与者上的一方。

## 简单的Party 复制

复制一方最简单、最安全的方法是在它成为任何合同中的利益相关者之前**这样做。

<Warning>
  如果一方已参与任何 Daml 交易，则必须改用离线方复制。
</Warning>

简单方复制由以下步骤组成，请按照它们所列出的顺序**执行：

1. 在参与者的命名空间或专用命名空间中创建Party。
2. 兽医包。
3. 授权一名或多名其他参与者主持Party。
4.使用Party。

下面使用两个参与者演示了这些步骤：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val source = participant1
    source : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant1'
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val target = participant2
    target : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant2'
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = source.synchronizers.id_of("my同步器")
    synchronizerId : synchronizerId = da::1220a82692ab...
```

### 1. 创建派对

创建一个派对爱丽丝：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = source.parties.enable("Alice", 同步器 = Some("my同步器"))
    alice : PartyId = Alice::12201ff69b1d...
```

<Note>
  在此示例中，**本地方 Alice** 由 `source` 参与者拥有，这是一种简化。这意味着 Alice 已在参与者的命名空间中注册，但这不是必需的。

  或者，您可以在其自己的专用命名空间中创建Party，或创建外部Party。
</Note>

### 2. 兽医套餐

**在**继续之前审查目标参与者的包裹。

<Note>
  如果您不熟悉此过程，请阅读包审查的一般说明。
</Note>

### 3.多主机Party

派对 Alice 需要同意托管在目标参与者上。

由于源参与者拥有一方Alice，因此您需要在`source`参与者上发出方到参与者映射拓扑交易。

#### 授权源参与者的托管更新

当地Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
        @ source.拓扑.party_to_participant_mappings
            .propose_delta(
              party = alice,
              adds = Seq(target.id -> ParticipantPermission.Submission),
              store = synchronizerId,
            )
            res5: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
              拓扑Transaction(
                PartyToParticipant(
                  partyId = Alice::12201ff69b1d...,
                  participants = Map(
                    PAR::participant1::12201ff69b1d... -> Submission,
                    PAR::participant2::1220a4d7463b... -> Submission
                  )
                ),
                serial = 2,
                operation = Replace,
                hash = SHA-256:20eef8c6481f...
              ),
              signatures = 12201ff69b1d...,
              proposal
            )
```

参与者可以举办具有不同权限的Party。在这个例子中，目标参与者将托管具有提交权限的Alice，即Alice可以在其上提交Daml交易。

外部当事人

外部Party的入职流程演示了如何在创建Party时声明Party的托管关系，包括在多个节点上托管（多托管外部Party）。与始终首先在单个节点上托管的本地Party不同，因此在成为多托管之后始终需要修改其Party到参与者的映射，而外部Party可以在加入过程中一步完成此操作。有关更多详细信息，请参阅入职流程。

#### 授权目标参与者的托管更新

要完成该过程，目标参与者还需要同意新主持爱丽丝。因此，您需要在`target`参与者上发出**相同的**方到参与者映射拓扑交易：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.拓扑.party_to_participant_mappings
    .propose_delta(
      party = alice,
      adds = Seq(target.id -> ParticipantPermission.Submission),
      store = synchronizerId,
    )
    res6: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Submission,
            PAR::participant2::1220a4d7463b... -> Submission
          )
        ),
        serial = 2,
        operation = Replace,
        hash = SHA-256:20eef8c6481f...
      ),
      signatures = 1220a4d7463b...,
      proposal
    )
```

<Note>
  这里的参与者权限必须与上一步中的相同。特别是对于外部Party，这必须是 `Confirmation` 或 `Observation`。
</Note>

一旦Party到参与者的映射生效，复制就完成了。这导致 Alice 方在 `source` 和 `target` 参与者上进行多托管。

要将 Alice 复制给更多参与者，请首先在 `newTarget` 参与者上审查包，然后重复此过程。然后，使用原始`source`和`newTarget`参与者再次执行复制。

### 3.a 复制方同时更改确认阈值（变体为 3）

<Note>
  对于**外部Party**，阈值已在入职流程中定义，因此本节与他们无关。
</Note>

要更改Party的确认阈值，您必须使用与之前所示不同的过程来提议Party到参与者的映射。

此替代方法允许您在单个操作中执行复制和更新阈值。

下面的示例继续上一个示例，演示如何将Party Alice 从`source` 参与者复制到`newTarget` 参与者，同时将确认阈值设置为 3。此操作还将参与者权限设置为将托管 Alice 的所有三个参与者进行确认。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newTarget = participant3
    newTarget : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant3'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val hostingParticipants = Seq(source, target, newTarget)
    hostingParticipants : Seq[com.digitalasset.canton.console.LocalParticipantReference] = List(Participant 'participant1', Participant 'participant2', Participant 'participant3')
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.拓扑.party_to_participant_mappings
    .propose(
      alice,
      newParticipants = hostingParticipants.map(_.id -> ParticipantPermission.Confirmation),
      threshold = PositiveInt.three,
      store = synchronizerId,
    )
    res9: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          threshold = 3,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Confirmation,
            PAR::participant2::1220a4d7463b... -> Confirmation,
            PAR::participant3::1220d6908163... -> Confirmation
          )
        ),
        serial = 3,
        operation = Replace,
        hash = SHA-256:7249f1511e32...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ newTarget.拓扑.party_to_participant_mappings
    .propose(
      alice,
      newParticipants = hostingParticipants.map(_.id -> ParticipantPermission.Confirmation),
      threshold = PositiveInt.three,
      store = synchronizerId,
    )
    res10: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          threshold = 3,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Confirmation,
            PAR::participant2::1220a4d7463b... -> Confirmation,
            PAR::participant3::1220d6908163... -> Confirmation
          )
        ),
        serial = 3,
        operation = Replace,
        hash = SHA-256:7249f1511e32...
      ),
      signatures = 1220d6908163...,
      proposal
    )
```

## 离线方复制

离线方复制是一个多步骤的手动过程。

在开始复制之前，目标参与者和Party本身都必须明确同意新的托管安排。

然后，复制包括从源参与者导出该方的活动合同集 (ACS)，并将其导入到目标参与者。

<Note>
  * 将单个 Canton 控制台连接到源参与者和目标参与者，以使用单个物理机器或环境导出和导入该方的 ACS 文件。否则，您需要将 ACS 导出文件安全地传输到将其导入到目标参与者的位置。
  * 离线Party复制要求您在导入Party的 ACS 之前断开目标参与者与所有同步器的连接。因此，名称为“离线”方复制。
  * 当您在目标参与者上加入Party时，您可能会检测到 ACS 承诺不匹配。这是预料之中的，并且会及时自行解决；在Party复制过程中忽略此类错误。
</Note>

<Warning>
  **请注意：在开始 ACS 导入之前，您必须备份目标参与者！**如果 ACS 导入中断（崩溃、节点意外重启等），或者您无法按照此手动操作步骤完成操作，这可确保您拥有一个干净的恢复点。有了此备份，您就可以安全地重置目标参与者，并**仍然完成正在进行的离线方复制**。
</Warning>

## 离线方复制步骤

这些是您必须按照所列出的**确切顺序**执行的步骤：

1. **目标：包裹审查** – 确保目标参与者审查所有必需的包裹。
2. **来源：数据保留** - 确保源参与者保留数据足够长的时间以便导出。
3. **目标：授权** - 目标参与者授权设置了入职标志的新托管。
4. **目标：隔离** - 断开与所有同步器的连接并禁用重新启动时的自动重新连接。
5. **来源：Party授权** - Party授权设置了加入标志的复制。
6. **来源：ACS 导出** - 当前主持Party的参与者导出 ACS。
7. **目标：备份** - 在开始 ACS 导入之前备份目标参与者。
8. **目标：ACS 导入** - 目标参与者导入 ACS。
9. **目标：重新连接** - 目标参与者重新连接到同步器。
10. **目标：入职标志许可** - 目标参与者发出入职标志许可。

<Warning>
  离线方复制必须小心执行，严格遵循记录的**顺序步骤**。不遵循概述的操作流程将导致可能需要大量手动更正的错误。

  本文档提供了指南。您的环境可能需要调整。在生产使用之前在测试环境中进行彻底测试。
</Warning>

### 场景描述

以下步骤显示如何将Party `alice` 从 `source` 参与者复制到同步器 `my同步器` 上的新 `target` 参与者。 `source` 可以是任何已经主持Party的参与者。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val source = participant1
    source : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant1'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val target = participant2
    target : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant2'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = source.parties.enable("Alice", 同步器 = Some("my同步器")) // This command creates a local party. For external parties see the external party 入驻 documentation (link found above in this page)
    alice : PartyId = Alice::12201ff69b1d...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = source.synchronizers.id_of("my同步器")
    synchronizerId : synchronizerId = da::1220a82692ab...
```

### 1. 兽医套餐

确保目标参与者审查与该方作为利益相关者的合同相关的所有包。`alice` 方使用了`CantonExamples` 包，该包已在 `source` 参与者上进行了审查，但尚未在 `target` 参与者上进行了审查。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mainPackageId = source.dars.list(filterName = "CantonExamples").head.mainPackageId
    mainPackageId : String = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.拓扑.vetted_packages.list()
    .filter(_.item.packages.exists(_.packageId == mainPackageId))
    .map(r => (r.context.storeId, r.item.participantId))
    res6: Seq[(拓扑StoreId, ParticipantId)] = Vector(
      (同步器(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant1::12201ff69b1d...)
    )
```

因此，将缺少的 DAR 包上传到`target` 参与者。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.dars.upload("dars/CantonExamples.dar")
    res7: String = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.拓扑.vetted_packages.list()
    .filter(_.item.packages.exists(_.packageId == mainPackageId))
    .map(r => (r.context.storeId, r.item.participantId))
    res8: Seq[(拓扑StoreId, ParticipantId)] = Vector(
      (同步器(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant1::12201ff69b1d...),
      (同步器(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant2::1220a4d7463b...)
    )
```

### 2. 数据保留

确保源参与者上的保留期足够长，足以覆盖以下两个事件之间的整个持续时间：

1. Party映射拓扑交易生效。
2. 完成源参与者的ACS导出。

如果您不确定当前的保留期是否足够，或者作为额外的预防措施，您应该暂时禁用源参与者的自动修剪。

检索当前的自动修剪计划。如果未设置计划，此命令将返回`None`。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val 修剪Schedule = source.修剪.get_schedule()
    修剪Schedule : Option[修剪Schedule] = Some(value = 修剪Schedule(cron = "0 0 20 * * ?", maxDuration = 2h, retention = 720h))
```

清除修剪计划，禁用`source`节点上的自动修剪。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.修剪.clear_schedule()
```

<Warning>
  无法在 `source` 参与者上以编程方式禁用手动修剪。与其他操作员密切协调，确保在 ACS 导出完成之前没有外部自动化触发修剪。
</Warning>

### 3. 授权目标参与者进行新托管

首先，让 `target` 参与者同意以所需的参与者权限（本例中为*观察*）来接待 Alice。

<Warning>
  请确保入职标志设置为`requiresPartyToBeOnboarded = true`。
</Warning>```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val proposal = target.拓扑.party_to_participant_mappings
    .propose_delta(
      party = alice,
      adds = Seq((target.id, ParticipantPermission.Observation)),
      store = synchronizerId,
      requiresPartyToBeOnboarded = true
    )
    proposal : Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Submission,
            PAR::participant2::1220a4d7463b... -> Observation(入驻)
          )
        ),
        serial = 2,
        operation = Replace,
        hash = SHA-256:4fc27cf93b27...
      ),
      signatures = 1220a4d7463b...,
      proposal
    )
```

### 4. 断开目标参与者与所有同步器的连接

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.disconnect_all()
```

### 5. 禁用目标参与者的自动重新连接

确保目标参与者在重新启动时不会自动重新连接到同步器。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.config("my同步器")
    res13: Option[同步器ConnectionConfig] = Some(
      value = 同步器ConnectionConfig(
        同步器 = 同步器 'my同步器',
        sequencerConnections = SequencerConnections(
          connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
            sequencerAlias = Sequencer 'sequencer1',
            sequencerId = SEQ::sequencer1::1220cb0a22fb...,
            endpoints = http://127.0.0.1:30197
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
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.modify("my同步器", _.copy(manualConnect=true))
``````scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.config("my同步器")
    res15: Option[同步器ConnectionConfig] = Some(
      value = 同步器ConnectionConfig(
        同步器 = 同步器 'my同步器',
        sequencerConnections = SequencerConnections(
          connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
            sequencerAlias = Sequencer 'sequencer1',
            sequencerId = SEQ::sequencer1::1220cb0a22fb...,
            endpoints = http://127.0.0.1:30197
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
        manualConnect = true
      )
    )
```

### 6. 授权举办新的Party

为了稍后*查找*授权新托管安排的拓扑交易的账本偏移量，请以 `source` 参与者的当前账本结束偏移量为起点：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val beforeActivationOffset = source.ledger_api.state.end()
    beforeActivationOffset : Long = 23L
```

**仅在**目标参与者与所有同步器断开连接后，方 Alice 同意托管在其上。

<Warning>
  再次，请确保本地方的入职标志设置为 `requiresPartyToBeOnboarded = true`，外部方的入职标志设置为 `入驻 = HostingParticipant.入驻()`。
</Warning>

当地Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
        @ source.拓扑.party_to_participant_mappings
            .propose_delta(
              party = alice,
              adds = Seq((target.id, ParticipantPermission.Observation)),
              store = synchronizerId,
              requiresPartyToBeOnboarded = true
            )
            res17: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
              拓扑Transaction(
                PartyToParticipant(
                  partyId = Alice::12201ff69b1d...,
                  participants = Map(
                    PAR::participant1::12201ff69b1d... -> Submission,
                    PAR::participant2::1220a4d7463b... -> Observation(入驻)
                  )
                ),
                serial = 2,
                operation = Replace,
                hash = SHA-256:4fc27cf93b27...
              ),
              signatures = 12201ff69b1d...,
              proposal
            )
```

外部当事人```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
update_external_party_hosting(
    party_id = alice,
    同步器_id = synchronizerId,
    confirming_threshold = None, # Keep current threshold
    hosting_participants_add_or_update: [
        HostingParticipant(participant_uid = target.id, ParticipantPermission.Observation, 入驻 = HostingParticipant.入驻())
    ]
)
```

### 7. 导出 ACS

从 `source` 参与者导出 Alice 的 ACS。

以下命令在内部查找 `target` 参与者上激活 Alice 的账本偏移量，从 `beginOffsetExclusive` 开始搜索。

然后，它从 `source` 参与者以该精确偏移量导出 Alice 的 ACS，并将其存储在名为 `party_replication.alice.acs.gz` 的导出文件中。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.parties
    .export_party_acs(
      party = alice,
      synchronizerId = synchronizerId,
      targetParticipantId = target.id,
      beginOffsetExclusive = beforeActivationOffset,
      exportFilePath = "party_replication.alice.acs.gz",
    )
```

### 8.可选：重新启用自动修剪

如果您之前按照数据保留步骤在 `source` 参与者上禁用了自动修剪，现在可以重新启用它。

使用禁用计划之前记录的原始配置参数运行以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.修剪.set_schedule("0 0 20 * * ?", 2.hours, 30.days)
```

### 9. 备份目标参与者

<Warning>
  **导入ACS前请先备份目标参与者！**
</Warning>

### 10.导入 ACS

在`target`参与者中导入Alice的ACS：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.parties.import_party_acs("party_replication.alice.acs.gz")
```

### 11. 将目标参与者重新连接到同步器

为了稍后*查找*拓扑交易的账本偏移量（其中`target`参与者上的新托管安排已被授权），请采用当前账本结束偏移量：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val targetLedgerEnd = target.ledger_api.state.end()
    targetLedgerEnd : Long = 17L
```

现在，将 `target` 参与者重新连接到同步器。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.reconnect_local("my同步器")
    res22: Boolean = true
```

### 12.可选：重新启用目标参与者的自动重新连接

如果您之前按照前面的步骤禁用了自动重新连接，现在可以重新启用它。仅当目标参与者最初配置为重新启动时自动重新连接时，才需要执行此操作。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.modify("my同步器", _.copy(manualConnect=false))
```

### 13.清除参与者的加入标志`target` 参与者完成 ACS 导入并重新连接到同步器后，您必须清除加入标志。这表明参与者已完全准备好举办Party。

有一个专门的命令来完成登机旗的清除。它会发出拓扑事务来为您清除标志，但前提是这样做是安全的。

以下命令以上一步捕获的`targetLedgerEnd`为起点，在内部定位在`target`参与者上激活了`alice`的有效方到参与者映射交易。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val (onboarded, minimalSafeClearingTs) = target.parties
    .clear_party_入驻_flag(alice, synchronizerId, targetLedgerEnd)
    (onboarded, minimalSafeClearingTs) : (Boolean, Option[com.digitalasset.canton.data.CantonTimestamp]) = (false, Some(value = 2026-01-26T22:32:51.738792Z))
```

该命令返回一个指示状态的元组：

* `(true, None)`：清除入职标志。继续下一步。
* `(false, Some(CantonTimestamp))`：入职标志仍然设置。只有在指定的时间戳之后，删除才是安全的。

如果入职标志仍然设置，您必须至少等待指定的时间戳（`minimalSafeClearingTs`）。只有这样，调用此命令才会真正导致拓扑事务以清除载入标志，该标志随后生效。

由于该命令是幂等的，因此可以重复调用它。因此，您还可以轮询此命令，直到确认载入标志已被清除。以下代码片段演示了如何轮询该命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(timeout = 2.minutes, maxWaitPeriod = 30.seconds) {
      val (onboarded, _) = target.parties
        .clear_party_入驻_flag(alice, synchronizerId, targetLedgerEnd)
      onboarded
    }
```

<Note>
  `timeout` 基于默认的“决策超时”1 分钟。
</Note>

### 总结

您已成功在 `source` 和 `target` 参与者上多重托管 Alice。

{/* 已复制_END */}

# 去中心化Party概述

去中心化Party结合了三个不同的特征：* Party拓扑管理的去中心化：`decentralized namespace` 确保该方的任何拓扑交易都需要密钥阈值的签名。
* 交易确认方的去中心化：`party to participant mapping`包含多个确认参与者和一个阈值，以确保需要该方确认的交易也需要来自一定阈值的参与者节点的确认。
* Party交易提交的去中心化：可选地，`party to key mapping`支持提交需要外部方直接授权的交易，例如通过使用密钥阈值签署准备好的交易来创建该方作为签署人的合同。如果没有定义Party到密钥的映射，则需要在`party to participant`阈值为1时创建初始合约（如果曾经是这种情况），并且节点拥有提交权，而不仅仅是确认权。

## 建立一个去中心化Party

虽然去中心化命名空间、Party到参与者映射以及Party到密钥映射可以完全独立配置，但常见的情况是一组实体共同控制所有三个，即所有三个实体具有相同数量的成员和相同的阈值。这里的说明描述了三个成员的设置，即`alice`、`bob`和`charlie`，他们分别使用`participant1`、`participant2`和`participant3`。

首先生成用于去中心化命名空间的密钥：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceNamespaceKey = participant1.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    aliceNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 1220adfbf95c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobNamespaceKey = participant2.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    bobNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 122002ef937c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieNamespaceKey = participant3.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    charlieNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 1220d99d5e7c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceNamespace = Namespace(aliceNamespaceKey.fingerprint)
    aliceNamespace : Namespace = 1220adfbf95c...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobNamespace = Namespace(bobNamespaceKey.fingerprint)
    bobNamespace : Namespace = 122002ef937c...
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieNamespace = Namespace(charlieNamespaceKey.fingerprint)
    charlieNamespace : Namespace = 1220d99d5e7c...
```

接下来，每个节点将该密钥的命名空间委托发布给同步器。这使得连接到同步器的所有节点都知道该密钥，并允许在以后的事务中使用它：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of(com.digitalasset.canton.同步器Alias.tryCreate("global"))
    synchronizerId : synchronizerId = global::1220f622b718...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.namespace_delegations.propose_delegation(aliceNamespace, aliceNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res8: Signed拓扑Transaction[拓扑ChangeOp, NamespaceDelegation] = Signed拓扑Transaction(
      拓扑Transaction(
        NamespaceDelegation(
          1220adfbf95c...,
          SigningPublicKey(
            id = 1220adfbf95c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:62b8ebbd68b9...
      ),
      signatures = 1220adfbf95c...
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.拓扑.namespace_delegations.propose_delegation(bobNamespace, bobNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res9: Signed拓扑Transaction[拓扑ChangeOp, NamespaceDelegation] = Signed拓扑Transaction(
      拓扑Transaction(
        NamespaceDelegation(
          122002ef937c...,
          SigningPublicKey(
            id = 122002ef937c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:5ab6abc4efc3...
      ),
      signatures = 122002ef937c...
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.拓扑.namespace_delegations.propose_delegation(charlieNamespace, charlieNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res10: Signed拓扑Transaction[拓扑ChangeOp, NamespaceDelegation] = Signed拓扑Transaction(
      拓扑Transaction(
        NamespaceDelegation(
          1220d99d5e7c...,
          SigningPublicKey(
            id = 1220d99d5e7c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c2668b45ce0b...
      ),
      signatures = 1220d99d5e7c...
    )
```发布命名空​​间委托后，您可以创建去中心化命名空间定义。为此，每个节点需要签署相同的拓扑事务并将其发布到同步器。他们还需要选择一个阈值，该阈值确定需要多少个去中心化命名空间所有者的签名才能代表去中心化命名空间授权拓扑交易。此示例使用阈值 2。请注意，该阈值不适用于建立去中心化命名空间的初始交易。为此，需要所有所有者的签名，而不仅仅是门槛。一旦所有节点发布其签名的交易，去中心化命名空间交易就会显示在 `list` 命令中：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val namespaceDef = DecentralizedNamespaceDefinition.tryCreate(DecentralizedNamespaceDefinition.computeNamespace(Set(aliceNamespace, bobNamespace, charlieNamespace)), PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Set, aliceNamespace, bobNamespace, charlieNamespace))
    namespaceDef : DecentralizedNamespaceDefinition = DecentralizedNamespaceDefinition(
      12204768b31e...,
      PositiveNumeric(2),
      Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res12: Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 1220adfbf95c...,
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.拓扑.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res13: Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 122002ef937c...,
      proposal
    )
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.拓扑.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res14: Signed拓扑Transaction[拓扑ChangeOp, DecentralizedNamespaceDefinition] = Signed拓扑Transaction(
      拓扑Transaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 1220d99d5e7c...,
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant1.拓扑.decentralized_namespaces.list(synchronizerId, filterNamespace = namespaceDef.namespace.filterString).nonEmpty)
```

下一步是设置 `PartyToParticipant` 映射。为此，您需要为该方选择一个前缀。完整的队伍 ID 为 `prefix::namespace`。此示例使用 `decentralized-party` 作为前缀。您还需要指定应主办该方的参与者列表、权限（对于参与该方共识的所有节点，这应该是`Confirmation`，但您可能有其他具有`Observation`权限的只读节点）和阈值。该阈值决定了去中心化方需要多少次确认。此示例使用与分散命名空间相同的两个阈值。对于去中心化命名空间，每个节点独立发布交易；一旦他们所有人都发布了他们的交易，它就会变得有效并显示在`list`中：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val partyId = PartyId(UniqueIdentifier.tryCreate("decentralized-party", namespaceDef.namespace))
    partyId : PartyId = decentralized-party::12204768b31e...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res17: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(12201ff69b1d..., 1220adfbf95c...),
      proposal
    )
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.拓扑.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res18: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(122002ef937c..., 1220a4d7463b...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.拓扑.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res19: Signed拓扑Transaction[拓扑ChangeOp, PartyToParticipant] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(1220d6908163..., 1220d99d5e7c...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant3.拓扑.party_to_participant_mappings.list(synchronizerId, filterParty = partyId.filterString).nonEmpty)
```

最后（可选）步骤是设置Party到键的映射。这允许通过离线聚合签名作为去中心化方直接提交交易。可以在此处重用用于分散命名空间的相同密钥（前提是您将 SigningKeyUsage 更改为限制性较小），但我们在此处使用单独的密钥：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceDamlKey = participant1.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    aliceDamlKey : SigningPublicKey = SigningPublicKey(
      id = 12204d33ee39...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobDamlKey = participant2.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    bobDamlKey : SigningPublicKey = SigningPublicKey(
      id = 1220565ad7f7...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieDamlKey = participant3.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    charlieDamlKey : SigningPublicKey = SigningPublicKey(
      id = 1220f4dd56cb...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

设置密钥后，您现在可以创建 `PartyToKey` 拓扑事务。再次使用两个签名的阈值：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res24: Signed拓扑Transaction[拓扑ChangeOp, PartyToKeyMapping] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(12204d33ee39..., 1220adfbf95c...),
      proposal
    )
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.拓扑.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res25: Signed拓扑Transaction[拓扑ChangeOp, PartyToKeyMapping] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(122002ef937c..., 1220565ad7f7...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.拓扑.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res26: Signed拓扑Transaction[拓扑ChangeOp, PartyToKeyMapping] = Signed拓扑Transaction(
      拓扑Transaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(1220d99d5e7c..., 1220f4dd56cb...),
      proposal
    )
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant3.拓扑.party_to_key_mappings.list(store = synchronizerId, filterParty = partyId.filterString).nonEmpty)
```

至此，该派对已完全建立并可以使用。

## 更改成员集

要添加和删除成员，步骤是相同的：现有成员有一个阈值，任何新成员都必须提交三个拓扑事务。也可以仅将它们添加到三个映射中的某些（但不是全部）中，但通常保持三个映射同步是有意义的。

请注意，向 `PartyToParticipant` 添加成员不仅需要拓扑事务，还需要完整的Party迁移，包括 ACS 导出和导入。有关详细信息超出了本主题的范围。

## 后续步骤

有关如何提交由`PartyToKey`映射启用的外部签名Daml交易的详细信息，请参阅外部提交文档。

在本教程中，命名空间和协议密钥均由参与者本身持有。也可以将它们放在参与者之外。实际流程保持不变，但拓扑事务的每次提交都必须进行外部签名。有关如何执行此操作的详细信息，请参阅外部拓扑签名文档。

## 去中心化命名空间计算

在上面的例子中，我们使用`DecentralizedNamespaceDefinition.computeNamespace(Set(aliceNamespace, bobNamespace, charlieNamespace))`从初始所有者的命名空间计算去中心化命名空间。请注意，这里只有初始所有者很重要，分散的命名空间不会随着所有者的添加或删除而改变。

但是，在某些情况下，您可能无法从 Canton 控制台运行此命令（例如，因为您直接针对拓扑 gRPC API 进行工作），或者由于其他原因需要自行计算命名空间。对于这些情况，我们在这里记录了如何用 Python 计算它：

命名空间的字典顺序：

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def compute_decentralized_namespace(owners):
    builder = hashlib.sha256()
    # hash purpose prefix
    builder.update((37).to_bytes(4))
    for owner in sorted(owners):
        # namespace length
        builder.update(len(owner).to_bytes(4))
        builder.update(owner.encode("utf-8"))
    # 1220 is the Canton prefix for sha256 hashes
    return f"1220{builder.hexdigest()}"
```

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
