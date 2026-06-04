---
title: "高级运维操作"
slug: "global-synchronizer-canton-console-advanced-operations"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/advanced-operations.md"
source_title: "Advanced Operations"
tags:
  - global-synchronizer
  - canton-console
  - advanced-operations
---

# 高级运维操作

> 面向资深运维的 Canton Console 高级操作：拓扑、密钥与修复。

> 适合经验丰富的操作员的高级 Canton 控制台操作

本页面涵盖高级控制台操作：拓扑管理、密钥轮换和修复过程。这些行动超出了日常管理的范围，通常需要对Canton 内部状态有更深入的了解。

## 拓扑管理

Canton 使用拓扑状态来跟踪各方、参与者、同步器和加密密钥之间的映射。您可以通过控制台检查和修改此状态。

### 检查拓扑状态

列出参与者当前的拓扑事务：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.transactions.list()
    res1: com.digitalasset.canton.topology.store.StoredTopologyTransactions[TopologyChangeOp, TopologyMapping] = Seq(
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            NamespaceDelegation(
              namespace = 12201ff69b1d...,
              target = SigningPublicKey(
                id = 12201ff69b1d...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = namespace
              ),
              restriction = none
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:252f433640a0...
          ),
          signatures = 12201ff69b1d...
        ),
        sequenced = 2026-05-04T17:56:08.399704Z,
        validFrom = 2026-05-04T17:56:08.399704Z
      ),
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            OwnerToKeyMapping(
              member = PAR::participant1::12201ff69b1d...,
              signingKeys = Seq(12202ac7545b..., 122044fb1b35...),
              encryptionKeys = 1220f78c3e7e...
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:5486c1b52e15...
          ),
          signatures = Seq(12201ff69b1d..., 12202ac7545b..., 122044fb1b35...)
        ),
        sequenced = 2026-05-04T17:56:08.409867Z,
        validFrom = 2026-05-04T17:56:08.409867Z
      ),
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            SynchronizerTrustCertificate(
              participantId = PAR::participant1::12201ff69b1d...,
              synchronizerId = da::122032922613...
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:b82608aa35af...
          ),
          signatures = 12201ff69b1d...
        ),
        sequenced = 2026-05-04T17:56:13.194363Z,
        validFrom = 2026-05-04T17:56:13.194363Z
      )
    )
```

要过滤特定类型的拓扑映射：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list(synchronizerId)
    res2: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult] = Vector(
      ListPartyToParticipantResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:56:24.441742Z,
          validUntil = None,
          sequenced = 2026-05-04T17:56:24.191742Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:6882f6f9ceea...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant1::12201ff69b1d... -> Submission
        )
      )
    )
```

这显示了哪些参与方托管在哪些参与者上，以及他们的权限级别（观察、确认或提交）。

### 政党到参与者的映射

每一方通过一方到参与者的映射与一个或多个参与者相关联。您可以检查这些映射来验证托管配置：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list(synchronizerId = synchronizerId, filterParty = "Alice")
    res3: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult] = Vector(
      ListPartyToParticipantResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:56:24.441742Z,
          validUntil = None,
          sequenced = 2026-05-04T17:56:24.191742Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:6882f6f9ceea...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant1::12201ff69b1d... -> Submission
        )
      )
    )
```

输出包括授予该聚会的每个参与者的权限。三个权限级别是：

* **观察** -- 涉及该方的合同的只读可见性
* **确认** -- 参与者可以代表当事人确认交易
* **提交** -- 参与者可以为队伍提交命令（仅限本地队伍）

<Note>
  The term "domain" appears in some older console commands and configuration keys. Canton has deprecated "domain" in favor of "synchronizer." If you encounter `domain` in command names or output, treat it as equivalent to `synchronizer`.
</Note>

### 修改拓扑状态

向参与者添加新方：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceParty = participant1.parties.enable("Alice")
    aliceParty : PartyId = Alice::12201ff69b1d...
```

对于更复杂的拓扑更改（例如调整确认阈值或添加托管参与者），您可以使用拓扑管理命令：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.propose(party = aliceParty, newParticipants = Seq((participant2.id, ParticipantPermission.Observation)))
    res5: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant2::1220a4d7463b... -> Observation
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:9360f5c90483...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

拓扑更改通过同步器的拓扑协议传播。从提出拓扑更改到生效之间存在固有的延迟。此延迟可在同步器级别进行配置，其存在是为了防止快速、潜在有害的更改。

## 密钥管理和轮换

Canton节点使用密钥进行签名和加密。随着时间的推移，您可能需要轮换密钥以确保安全或应对可疑的泄露。

### 列出键

查看参与者当前注册的密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.secret.list()
    res6: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12201ff69b1d...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          name = Some(KeyName(participant1-namespace))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 122044fb1b35...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(signing, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-signing))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12202ac7545b...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-sequencer-auth))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = EncryptionPublicKeyWithName(
          publicKey = EncryptionPublicKey(
            id = 1220f78c3e7e...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-P256
          ),
          name = Some(KeyName(participant1-encryption))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      )
    )
```

这显示了密钥指纹、用途（签名或加密）和密钥方案。

### 生成新密钥

生成新的签名密钥：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newKey = participant1.keys.secret.generate_signing_key(name = "new-signing-key", usage = SigningKeyUsage.All)
    newKey : SigningPublicKey = SigningPublicKey(
      id = 122006262a3e...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(namespace, sequencer-auth, signing, proof-of-ownership)
    )
```

生成新的加密密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newEncKey = participant1.keys.secret.generate_encryption_key(name = "new-encryption-key")
    newEncKey : EncryptionPublicKey = EncryptionPublicKey(
      id = 12209242c045...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-P256
    )
```

### 密钥轮换

轮换密钥涉及生成新密钥、通过拓扑事务对其进行授权，然后撤销旧密钥。具体步骤取决于密钥的用途：

1. 生成新密钥（见上文）。
2. 通过提议更新的映射来授权拓扑状态中的新密钥。
3. 等待拓扑更改生效。
4. 验证节点是否使用新密钥正常运行。
5. 确认新密钥有效后，才能撤销旧密钥。

<Warning>
  Do not revoke the old key before the new key is fully propagated and operational. Premature revocation can lock you out of your node.
</Warning>

### 导出和导入密钥

出于备份或迁移目的：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Export secret keys to a directory
participant1.keys.secret.download("backup/keys/")

// Import keys from a backup
participant1.keys.secret.upload("backup/keys/my-key.bin")
```

如果您的部署使用外部密钥管理服务 (KMS)，则密钥材料通过 KMS 而不是通过本地导出/导入进行管理。 GCP 和 AWS KMS 驱动程序均在社区版中提供。

## 修复操作

<Warning>
  Repair operations are powerful but dangerous. They can cause permanent data corruption if used incorrectly. You should only use repair commands with guidance from Digital Asset technical support.

  These commands are documented here for completeness, but they are not intended for unsupervised use.
</Warning>

### 启用修复命令

默认情况下禁用修复命令。要启用它们，请将以下内容添加到您的配置中：

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.features.enable-preview-commands = yes
canton.features.enable-repair-commands = yes
```

进行此更改后重新启动节点。修复完成后，删除这些设置并重新启动，以防止意外误操作。

### 需要维修时

Canton旨在自我修复。通过重试和重新连接自动处理数据库中断、网络中断和类似的基础设施问题。手动修复是自动恢复无法解决问题（通常是活动合同集 (ACS) 损坏或无法处理顺序事件）的情况下的最后手段。

修复场景的一般类别有：* **共享合约的参与者之间的 ACS 不一致**，由导致状态不同的基础设施故障引起
* **同步器连接被阻止**，参与者无法处理来自同步器的事件并在重新连接时崩溃
* **丢失同步器恢复**，其中同步器永久不可用并且需要迁移合约

### 修复工具箱

可用的修复操作包括：

* **从 ACS 添加或清除合约**，以修复参与者之间的不一致问题
* **忽略错误事件** 以解锁因处理损坏事件而卡住的参与者
* **将合约从丢失的同步器迁移到新同步器
* **导出和导入**身份状态、拓扑事务和 DAR 以实现全节点补水

### 修复宏

<Note>
  Repair macros are an advanced topic. They combine multiple repair commands into a single operation and are designed for use under the direction of technical support during incident recovery.
</Note>

一些修复操作被打包为宏——单个修复命令的序列组合成单个控制台调用。这些宏处理常见的恢复场景，例如克隆节点的身份状态以进行补充。

例如，身份下载/上传宏将参与者的拓扑状态、身份和（如果不使用 KMS）密钥导出到磁盘，从而允许您从干净的数据库恢复参与者：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Download identity state
repair.identity.download(participant1, "backup/identity/")

// After database reset, upload identity state
repair.identity.upload(participant1, "backup/identity/")
```

### 协调多方参与修复

当 ACS 不一致影响多个参与者时，所有受影响参与者的运营商需要就添加或删除哪些合约达成一致。这种协调至关重要——一个操作员的单方面更改可能会使不一致情况变得更糟。

典型的流程是：

1. 通过检查日志中的 ACS 承诺不匹配来识别不一致（查找 `ACS_COMMITMENT_MISMATCH` 错误）。
2. 与其他受影响的运营商就目标状态达成一致。
3. 对每个参与者应用商定的添加和删除。
4. 验证修复后 ACS 承诺是否匹配。

Canton 操作文档中提供了特定维修方案的详细程序。在所有情况下，请与技术支持人员合作，而不是尝试独立修复。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
