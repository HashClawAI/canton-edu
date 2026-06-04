---
title: "密钥管理"
slug: "global-synchronizer-production-operations-key-management"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/key-management.md"
source_title: "Key Management"
tags:
  - global-synchronizer
  - production-operations
  - key-management
---

# 密钥管理

> Canton 节点加密密钥的管理与限制。

> 管理 Canton 节点的加密密钥 - 列表、轮换、生成和限制

## 加密密钥管理

本页介绍如何列出、轮换、生成、停用和删除 Canton 节点的密钥。它还解释了如何配置节点支持的加密方案。

有一个单独的部分介绍命名空间键的管理。

### 列出键

使用以下命令枚举节点 `myNode` 存储在其保管库中的公钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.public.list()
    res1: Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 12207872a327...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(sequencer-auth, proof-of-ownership)
        ),
        name = Some(KeyName(mediator1-sequencer-auth))
      ),
    ..
```

这将显示一个非空的键序列，假设 `myNode` 正在运行并在启动期间创建了键，这是默认行为。

同样，用户可以枚举`myNode`的私钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.list()
    res2: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12207872a327...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(mediator1-sequencer-auth))
    ..
```

用户可以列出节点已授权在同步器上使用的密钥，如下所示：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.owner_to_key_mappings
                                .list(store = mySynchronizerId, filterKeyOwnerUid = myNode.id.filterString)
                                .flatMap(_.item.keys)
    res3: Seq[PublicKey] = Vector(
      SigningPublicKey(
        id = 12207872a327...,
        format = DER-encoded X.509 SubjectPublicKeyInfo,
        keySpec = EC-Curve25519,
        usage = Set(sequencer-auth, proof-of-ownership)
      ),
      SigningPublicKey(
        id = 1220db0eb017...,
        format = DER-encoded X.509 SubjectPublicKeyInfo,
    ..
```

### 轮换钥匙

Canton 支持使用单个命令轮换节点 `myNode` 的密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.rotate_node_keys()
```

为了确保连续操作，该命令首先激活新密钥，然后才停用旧密钥。该命令旋转`myNode`的**所有**键。但该命令不会轮换命名空间键。节点停用所有同步器上的旧密钥，但它们仍保留在`myNode`的保管库中。

以下命令轮换`myNode`的单个密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.rotate_node_key(oldKeyFingerprint, "newKeyName")
    res5: PublicKey = SigningPublicKey(
      id = 1220ad959eff...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(sequencer-auth, proof-of-ownership)
    )
```

<Note>
  密钥轮换应与备份交替进行。
</Note>

### 生成并激活密钥

Canton 为所有节点创建具有默认参数的密钥。要具有不同的密钥参数，请手动生成密钥。

要为 `myNode` 生成并激活新的签名密钥，请运行以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = myNode.keys.secret.generate_signing_key(
      "mySigningKeyName",
      SigningKeyUsage.ProtocolOnly,
      Some(SigningKeySpec.EcCurve25519)
    )
    key : SigningPublicKey = SigningPublicKey(
      id = 1220b8113819...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.owner_to_key_mappings.add_key(key.fingerprint, key.purpose)
```

同样，以下命令生成并激活新的加密密钥：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = myNode.keys.secret.generate_encryption_key(
      "myEncryptionKeyName",
      Some(EncryptionKeySpec.EcP256)
    )
    key : EncryptionPublicKey = EncryptionPublicKey(
      id = 1220c6f1c9da...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-P256
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.owner_to_key_mappings.add_key(key.fingerprint, key.purpose)
```

有关`SigningKeyUsage`的更多信息，请参阅主要限制页面。密钥是根据特定的加密密钥格式生成的。请参阅下表，了解有关坎顿的预期密钥格式的更多信息。

### 停用按键

要停用所有同步器上的某个键，请运行以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.owner_to_key_mappings.remove_key(key.fingerprint, key.purpose)
```

节点操作员通常不需要停用密钥，因为节点在滚动密钥时会停用旧密钥。当改变到不同的方案时，操作员可能需要明确地停用密钥。

### 删除键

轮换或停用密钥后，它仍保留在节点的保管库中。要从保管库中永久删除密钥，请使用以下控制台命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.delete(key.fingerprint, force = true)
```

<Warning>
  删除私钥时请务必小心。确保该密钥不再使用，并且不需要为旧消息解密或创建签名。因此，只有在停用密钥并修剪节点晚于停用的时间戳后才能删除该密钥。这对于开放网络中的Sequencer尤其重要。例如，如果参与者在检索排序事件方面滞后，并且Sequencer的操作员滚动了Sequencer的签名密钥，则旧签名密钥必须保持可访问状态，以便在落后参与者的密钥滚动之前对事件进行签名。否则，过早删除密钥可能会给这些参与者带来不可逆转的问题。
</Warning>

### 配置加密方案

Canton 支持多种加密方案。默认情况下，节点允许使用 Canton 支持的所有加密方案。

要配置节点的默认和允许的方案，请在 Canton 配置中包含如下代码片段：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    participants.participant1 {
       crypto {
         provider = jce

         # signing
         signing.algorithms {
           default = ed-25519
           allowed = [ed-25519, ec-dsa-sha-256, ec-dsa-sha-384]
         }
         signing.keys {
           default = ec-curve-25519
           allowed = [ec-curve-25519, ec-p-256, ec-p-384, ec-secp-256k-1]
         }

         # asymmetric encryption
         encryption.algorithms {
           default = ecies-hkdf-hmac-sha-256-aes-128-cbc
           allowed = [ecies-hkdf-hmac-sha-256-aes-128-cbc, rsa-oaep-sha-256]
         }
         encryption.keys {
           default = ec-p-256
           allowed = [ec-p-256, rsa-2048]
         }
      }
    }
  }

```

<Note>
  每个同步器都强制规定其成员必须支持的最小加密方案集。如果节点不支持此最小方案集，则无法连接到同步器。
</Note>

### 禁用会话密钥

有关会话密钥的用途和安全含义的说明，请参阅 [Canton 的加密密钥](/overview/learn/cryptographic-keys)。

虽然会话密钥可以提高性能，但它们也会带来安全风险，因为密钥存储在内存中，即使只存储很短的时间。如果您希望禁用会话密钥并接受由此导致的性能下降，可以通过设置以下配置来实现。

要禁用**会话加密密钥**：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant3.caching.session-encryption-key-cache.enabled = false
```

要禁用**会话签名密钥**：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant3.crypto.kms.session-signing-keys.enabled = false
```请注意，**会话签名密钥**仅与外部 KMS（密钥管理服务）提供商一起使用。

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/keys/key_restrictions.rst" hash="52807875" */}

## 限制密钥使用

本页介绍了如何将 Canton 节点的加密密钥的使用限制为特定目的，作为遏制潜在受损密钥损坏的最佳实践。

### 签名密钥使用

Canton 定义了以下签名密钥的密钥用法：

* `Namespace`：定义节点身份并签署拓扑请求的密钥（参见命名空间密钥管理）
* `SequencerAuthentication`：向Sequencer验证网络成员身份的密钥
* `Protocol`：作为同步协议执行一部分对各种结构进行签名的密钥

#### 限制签名密钥的使用

生成新密钥时，根据所需用途设置 `usage` 参数。

例如，使用以下命令生成仅限 `Protocol` 使用的签名密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val myKey = myNode.keys.secret.generate_signing_key(
      name = "mySigningKey",
      usage = SigningKeyUsage.ProtocolOnly,
    )
    myKey : SigningPublicKey = SigningPublicKey(
      id = 1220a5fb14f5...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

一些预定义集可用于常见用途：`NamespaceOnly`、`SequencerAuthenticationOnly`、`ProtocolOnly`、`All`。单独的用途可以组合在`Set`中，但不建议这样做，以避免密钥用于多种用途。

<Note>
  一旦在密钥生成期间指定，该组用法就是固定的，并且在该密钥的生命周期内无法修改。相反，必须生成并激活新密钥，并停用旧密钥。有关密钥管理命令的更多信息，请参阅密钥管理。
</Note>

如果您使用密钥管理服务 (KMS) 以外部密钥存储模式处理 Canton 的密钥，并且想要使用已存储在 KMS 中的手动生成的密钥，请在向 Canton 注册密钥时设置 `usage` 参数以获取所需的用途：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
node.keys.secret.register_kms_signing_key(
  kmsKeyId,
  usage = SigningKeyUsage.ProtocolOnly,
  name = s"${node.name}-signing-new",
)
```

返回的密钥可用于其他密钥管理命令。

#### 确定现有签名密钥的使用

要查找签名密钥已分配的用途，请使用以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.public.list(
      filterFingerprint = myKey.id.unwrap,
    )
    intermediateKey : Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220a5fb14f5...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mySigningKey))
      )
    )
```

如果省略 `filterFingerprint` 参数，则将返回所有现有密钥。

#### 确定具有给定用途的现有密钥

要查找已分配给定用途的所有签名密钥，请使用以下命令：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.public.list(
      filterUsage = SigningKeyUsage.ProtocolOnly,
    )
    intermediateKey : Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220033a8e3d...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mediator1-signing))
      ),
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220a5fb14f5...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mySigningKey))
      )
    )
```

将返回所有已分配至少一种`filterUsage`中指定用途的键。### 命名空间密钥委托限制

正如身份管理页面中所述，Canton 使用拓扑交易来管理身份，这些交易由具有`Namespace`用途的密钥进行签名。命名空间密钥管理表明您可以创建中间密钥来签署拓扑事务，从而限制根命名空间密钥的暴露。这些中间密钥可以使用细粒度的委托限制来进一步限制它们可以签署哪种类型的拓扑事务。

Canton 为命名空间键定义了以下限制：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// the key can sign all currently known mappings and all mappings that will be added in future releases
message CanSignAllMappings {}
// the key can sign all currently known mappings and all mappings that will be added in future releases, except for
// namespace delegations
message CanSignAllButNamespaceDelegations {}
// the key can only sign the explicitly specified mappings
message CanSignSpecificMappings {
  repeated Enums.拓扑MappingCode mappings = 1;
}
```

#### 限制密钥可以签名的映射类型

您必须首先创建一个至少具有 `Namespace` 使用率的新密钥，然后将命名空间的签名权限委托给该密钥，并在 `delegationRestriction` 参数中指定所需的限制。

例如，在下面的例子中，第一个命令为根命名空间创建一个中间密钥，然后第二个命令将签名权限委托给它，允许它签署除命名空间委托本身之外的所有类型的拓扑映射：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.secret.generate_signing_key(
      name = "intermediate-key",
      usage = SigningKeyUsage.NamespaceOnly,
    )
    intermediateKey : SigningPublicKey = SigningPublicKey(
      id = 1220481ada67...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.namespace_delegations.propose_delegation(
      namespace = myNode.namespace,
      targetKey = intermediateKey,
      delegationRestriction = CanSignAllButNamespaceDelegations,
    )
    res5: Signed拓扑Transaction[拓扑ChangeOp, NamespaceDelegation] = Signed拓扑Transaction(
      拓扑Transaction(
        NamespaceDelegation(
          namespace = 122009299340...,
          target = SigningPublicKey(
            id = 1220481ada67...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = not-nsd
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:b9b6a4bf20d3...
      ),
      signatures = 122009299340...
    )
```

与所有拓扑映射一样，命名空间键上的委派限制可以更新。为此，请发出具有更新的委派限制的新 `propose_delegation` 命令。

<Warning>
  如果您定义具有受限委托的中间命名空间密钥，则必须确保覆盖所有授权，并且通过将多个命名空间密钥组合在一起，它们可以授权所有拓扑事务。否则，某些操作过程可能会失败。例如，如果没有至少一个命名空间密钥可以授权 `OwnerToKey` 映射，则旋转密钥将会失败。

  在这种情况下，操作将失败，并显示“无法找到适当的签名密钥来发出拓扑交易”错误消息和代码`TOPOLOGY_NO_APPROPRIATE_SIGNING_KEY_IN_STORE`。
</Warning>

#### 确定现有命名空间键的限制

要查找命名空间密钥上定义的签名限制，请使用以下命令：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.拓扑.namespace_delegations.list(
      store = 拓扑StoreId.Authorized,
      filterTargetKey = Some(intermediateKey.id),
    )
    res6: Seq[com.digitalasset.canton.admin.api.client.data.拓扑.ListNamespaceDelegationResult] = Vector(
      ListNamespaceDelegationResult(
        context = BaseResult(
          storeId = Authorized,
          validFrom = 2026-05-04T17:53:53.944669Z,
          validUntil = None,
          sequenced = 2026-05-04T17:53:53.944669Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:b9b6a4bf20d3...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(122009299340...)
        ),
        item = NamespaceDelegation(
          namespace = 122009299340...,
          target = SigningPublicKey(
            id = 1220481ada67...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = not-nsd
        )
      )
    )
```

如果省略 `filterTargetKey` 参数，将返回所有现有的命名空间委托。

{/* 已复制_END */}

本文档是一项正在进行的工作。该功能将在未来按照文档中描述的流程进行开发和发布。

## 命名空间密钥管理

### 在线根命名空间密钥

默认情况下，Canton 节点在节点初始化期间创建根命名空间密钥。操作者可以在节点上手动创建中间密钥来授权拓扑交易。只能更改中间密钥。因此，保证根密钥的安全非常重要。

如果 Canton 节点配置为使用 KMS 系统，则可以使用 KMS 管理控件来管理隔离根密钥，以删除节点对根密钥的访问权限。由于仅在授权新的中间密钥或撤销现有授权时才需要根密钥，因此仅在执行此类操作时选择性地允许节点访问密钥就足够了。

只能隔离根密钥。所有其他键对于 Canton 的正确操作都是必不可少的。或者，中间密钥也可以被隔离，但必须在管理操作（例如上传 DAR 或添加参与方）期间根据需要打开和关闭。

### 离线根命名空间密钥

管理根命名空间密钥的更安全方法是使用脱机根命名空间密钥。在这种情况下，根名称空间密钥存储在安全的、可能有气隙的位置，无法从 Canton 节点访问。

根密钥的存储位置取决于您组织的安全要求。对于本指南的其余部分，假设有两个站点：具有中间密钥的节点的在线站点和根密钥的离线站点。离线根密钥用于签署对节点中间密钥的委托，然后使用该委托来授权拓扑事务。

离线根密钥过程由一组实用脚本支持，可以在 Canton `scripts` 目录 (`scripts/offline-root-key`) 中找到。

#### 密钥交换通道

必须有一个通道或方法允许在在线和离线站点之间交换公共中间密钥和签名的中间命名空间委托。该通道必须在真实性方面受到信任，但在机密性方面则不然，因为不会交换任何秘密信息。这意味着您需要确保数据在传输过程中不被篡改，但数据本身不需要加密。

这可以使用多种方法来完成，具体取决于站点是气隙站点还是通过网络连接。可能的示例有：安全文件传输、QR 码、物理存储介质。

假设存在这样的可信通道，则需要执行以下步骤来设置离线根命名空间密钥：

#### 1. 配置节点以期望外部根密钥

首次启动前，必须将Canton节点配置为不自动初始化。这是通过设置完成的

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.init.identity.type = manual
```

然后可以使用此配置启动节点。它启动管理 API，但停止启动过程并等待节点身份的初始化以及必要的拓扑事务。#### 2.导出节点公钥

假设您有权访问节点的远程控制台，请创建一个新的签名密钥用作中间密钥：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = participant1.keys.secret.generate_signing_key(name = "NamespaceDelegation", usage = com.digitalasset.canton.crypto.SigningKeyUsage.NamespaceOnly)
    key : SigningPublicKey = SigningPublicKey(
      id = 122080b595e9...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKeyPath = better.files.File.newTemporaryFile(prefix = "intermediate-key.pub").pathAsString
    intermediateKeyPath : String = "/tmp/intermediate-key.pub3520580670384386470"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.public.download_to(key.id, intermediateKeyPath)
```

这将创建一个包含中间密钥的公钥的文件。

以下 protobuf 定义列出了支持的关键规范：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
enum SigningKeySpec {
  SIGNING_KEY_SPEC_UNSPECIFIED = 0;

  // Elliptic Curve Key from Curve25519
  // as defined in http://ed25519.cr.yp.to/
  SIGNING_KEY_SPEC_EC_CURVE25519 = 1;

  // Elliptic Curve Key from the NIST P-256 curve (aka secp256r1)
  // as defined in https://doi.org/10.6028/NIST.FIPS.186-4
  SIGNING_KEY_SPEC_EC_P256 = 2;

  // Elliptic Curve Key from the NIST P-384 curve (aka secp384r1)
  // as defined in https://doi.org/10.6028/NIST.FIPS.186-4
  SIGNING_KEY_SPEC_EC_P384 = 3;

  // Elliptic Curve Key from SECG P256k1 curve (aka secp256k1)
  // commonly used in bitcoin and ethereum
  // as defined in https://www.secg.org/sec2-v2.pdf
  SIGNING_KEY_SPEC_EC_SECP256K1 = 4;
}
```

参与方节点打算连接的同步器可能会进一步限制支持的关键规范列表。要直接从同步器获取此信息，请在同步器公共 API 上运行以下命令。

```
grpcurl -d '{}' <sequencer_endpoint> com.digitalasset.canton.sequencer.api.v30.SequencerConnectService/Get同步器Parameters
```

如果无法访问控制台，您可以使用引导脚本或 `grpccurl` 针对管理 API 来调用命令。

#### 3. 与离线站点共享节点公钥

接下来，必须将中间公钥传输到离线站点，如上所述。确保公钥在运输过程中不被篡改。

#### 4. 生成根密钥和根证书

##### 使用 OpenSSL

确保安全站点上提供必要的脚本。这些脚本包含在 `scripts/offline-root-key` 的 Canton 发行包中。 `examples/10-offline-root-namespace-init` 提供了演示如何使用这些脚本使用 `openssl` 生成密钥和签署证书的示例。从 `examples/10-offline-root-namespace-init` 目录运行下一组命令。

首先初始化下面代码片段中使用的变量

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Points to the location of the offline root key scripts under the scripts/offline-root-key directory in the release artifact
SCRIPTS_ROOT="$(dirname "$0")/../../scripts/offline-root-key"
PRIVATE_KEY="$OUTPUT_DIR/root_private_key.der"
PUBLIC_KEY="$OUTPUT_DIR/root_public_key.der"
ROOT_NAMESPACE_PREFIX="$OUTPUT_DIR/root_namespace"
INTERMEDIATE_NAMESPACE_PREFIX="$OUTPUT_DIR/intermediate_namespace"
```

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
mkdir -p tmp/certs
OUTPUT_DIR="tmp/certs"
CANTON_NAMESPACE_DELEGATION_PUB_KEY=<Path to the intermediate key downloaded from Canton. ``intermediateKeyPath`` in this example>
```

以及设置包含生成证书所需的 protobuf 定义的 protobuf 图像的路径。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)
export BUF_PROTO_IMAGE="$CURRENT_DIR/../../scripts/offline-root-key/root_namespace_buf_image.json.gz"
source "$CURRENT_DIR/../../scripts/offline-root-key/utils.sh"
```

然后，在安全环境中生成根密钥并提取公钥：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl ecparam -name prime256v1 -genkey -noout -outform DER -out "$PRIVATE_KEY"
openssl ec -inform der -in "$PRIVATE_KEY" -pubout -outform der -out "$PUBLIC_KEY" 2> /dev/null
```

然后，创建自签名根命名空间委托，它实际上是用作给定命名空间的信任锚的自签名证书：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/prepare-certs.sh" --root-delegation --root-pub-key "$PUBLIC_KEY" --target-pub-key "$PUBLIC_KEY" --output "$ROOT_NAMESPACE_PREFIX"
```

请注意，根公钥必须采用`x509 SPKI DER`格式。有关 Canton 支持的密钥格式的更多信息，请参阅下表。这会生成两个文件，`root-delegation.prep`和`root-delegation.hash`。 `.prep` 文件包含序列化为字节的未签名拓扑事务。如果您确实想确定您正在签名的内容，请检查 `prepare-certs.sh` 脚本以了解它如何生成拓扑交易以及如何计算哈希。接下来，需要对哈希进行签名。

如果您使用 openssl，则可以使用以下命令对哈希进行签名：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "$PRIVATE_KEY" -keyform DER -sign < "$ROOT_NAMESPACE_PREFIX.hash" > "$ROOT_NAMESPACE_PREFIX.signature"
```

最后，组装签名和准备好的交易。有关支持的签名格式的更多信息，请参阅下表：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/assemble-cert.sh" --prepared-transaction "$ROOT_NAMESPACE_PREFIX.prep" --signature "$ROOT_NAMESPACE_PREFIX.signature" --signature-algorithm ecdsa256 --output "$ROOT_NAMESPACE_PREFIX.cert"
```

这创建了所谓的签名拓扑事务。

##### 使用 GCP KMS

如果您使用的是 GCP KMS，则可以使用 KMS CLI ([https://cloud.google.com/kms/docs/create-validate-signatures](https://cloud.google.com/kms/docs/create-validate-signatures)) 和以下命令来生成密钥：

```
gcloud kms keyrings create key-ring --location location (APPROXIMATE)
```

并且可以使用以下命令来生成签名：

```
gcloud kms asymmetric-sign \
    --version key-version \
    --key <root-key> \
    --keyring key-ring \
    --location location \
    --digest-algorithm digest-algorithm \
    --input-file root-delegation.prep \
    --signature-file root-delegation.signature
```

#### 5. 创建中间证书

如果根密钥和自签名根委派可用，您可以创建中间证书。步骤与根证书非常相似，但目标是中间密钥的公钥，并且使用`--intermediate-delegation`标志而不是`--root-delegation`。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/prepare-certs.sh" --intermediate-delegation --root-pub-key "$PUBLIC_KEY" --canton-target-pub-key "$CANTON_NAMESPACE_DELEGATION_PUB_KEY" --output "$INTERMEDIATE_NAMESPACE_PREFIX"
```

验证生成的拓扑事务（打印到标准输出）是否正确并引用正确的键。验证后，需要对生成的哈希进行签名：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "$PRIVATE_KEY" -keyform DER -sign < "$INTERMEDIATE_NAMESPACE_PREFIX.hash" > "$INTERMEDIATE_NAMESPACE_PREFIX.signature"
```

同样，可以组合签名和准备好的交易：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/assemble-cert.sh" --prepared-transaction "$INTERMEDIATE_NAMESPACE_PREFIX.prep" --signature "$INTERMEDIATE_NAMESPACE_PREFIX.signature" --signature-algorithm ecdsa256 --output "$INTERMEDIATE_NAMESPACE_PREFIX.cert"
```

#### 7. 将证书复制到在线站点

生成的证书（不是根私钥）需要传输到在线站点。公钥包含在证书中，不需要单独传输。您需要将两个证书（根委派和中间委派）传输到在线站点。

#### 8. 将证书导入节点

在目标站点上，使用控制台命令将证书导入到等待节点```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.init_id(identifier = "participant1", delegationFiles = Seq("/tmp/canton/certs/root_namespace.cert", "/tmp/canton/certs/intermediate_namespace.cert"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res5: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::1220e5af5c84328a08bbaf051a1a00ec514755465a66e5a03e78b6c0ba11fe3a4362
    Uptime: 0.119182s
    Ports: 
    	ledger: 33078
    	admin: 33079
    Connected 同步器s: None
    Unhealthy 同步器s: None
    Active: true
    Components: 
    	memory_storage : Ok()
    	connected-同步器 : Not Initialized
    	sync-ephemeral-state : Not Initialized
    	sequencer-client : Not Initialized
    	acs-commitment-processor : Not Initialized
    Version: 3.6.0-SNAPSHOT
    Supported protocol version(s): 35, dev
```

或者，可以通过`grpccurl`直接使用管理API来初始化节点。

### 预生成的证书

如果证书已预先生成，也可以直接通过节点的配置文件提供。在这种情况下，必须在 KMS 上生成密钥并下载其公钥材料，而不是如上所述通过节点的 `generate_signing_key` 命令生成中间密钥。然后可以使用相同的脚本生成证书，但中间公钥不是 Canton 格式而是 DER 格式，因此应使用 `--target-pub-key` 设置。证书可用后，您必须通过运行以下命令来注册中间 KMS 密钥：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val middleKey = node.keys.secret
  .register_kms_signing_key(
    中间NsKmsKeyId，
    SigningKeyUsage.NamespaceOnly，
    name = s"${node.name}-${SigningKeyUsage.Namespace.identifier}",
  ）
// 用户手册条目开始：ManualRegisterKmsNamespaceKey
节点.crypto.cryptoPrivateStore
  .existsPrivateKey(intermediateKey.id, 签名)
  .valueOrFail("中间密钥未注册")
  .futureValueUS

// 用户手册条目开始：ManualRegisterKmsKeys

// 注册用于定义节点身份的KMS签名密钥。
val 命名空间Key = node.keys.secret
  .register_kms_signing_key(
    命名空间KmsKeyId,
    SigningKeyUsage.NamespaceOnly，
    name = s"${node.name}-${SigningKeyUsage.Namespace.identifier}",
  ）

// 注册用于向 Sequencer 验证节点的 KMS 签名密钥。
val sequencerAuthKey = node.keys.secret
  .register_kms_signing_key(
    序列器AuthKmsKeyId，
    SigningKeyUsage.SequencerAuthenticationOnly，
    name = s"${node.name}-${SigningKeyUsage.SequencerAuthentication.identifier}",
  ）

// 注册用于签署协议消息的签名密钥。
val签名密钥=node.keys.secret
  .register_kms_signing_key(
    签名KmsKeyId，
    SigningKeyUsage.ProtocolOnly，
    name = s"${node.name}-${SigningKeyUsage.Protocol.identifier}",
  ）

// 注册加密密钥。
val 加密密钥 = node.keys.secret
  .register_kms_encryption_key(encryptionKmsKeyId, name = node.name + "-加密")

// 用户手册条目结束：ManualRegisterKmsKeys

（命名空间密钥、sequencerAuthKey、签名密钥、加密密钥）
} 否则{
// 架构手册条目开始：ManualInitKeys

// 创建用于定义节点身份的签名密钥。
val 命名空间键 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Namespace.identifier}",
      SigningKeyUsage.NamespaceOnly，
    ）

// 创建一个签名密钥，用于向 Sequencer 验证节点。
val 序列器验证密钥 =
  节点.keys.secret.generate_signing_key(
    name = node.name + s"-${SigningKeyUsage.SequencerAuthentication.identifier}",
    SigningKeyUsage.SequencerAuthenticationOnly，
  ）

// 创建用于签署协议消息的签名密钥。
val 签名密钥 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Protocol.identifier}",
      SigningKeyUsage.ProtocolOnly，
    ）

// 创建加密密钥。
val 加密密钥 =
  node.keys.secret.generate_encryption_key(name = node.name + "-加密")

// 架构手册条目结束：ManualInitKeys

（命名空间密钥、sequencerAuthKey、签名密钥、加密密钥）
}

// 架构手册条目开始：ManualInitNode// 使用该密钥的指纹作为节点身份。
val 命名空间 = 命名空间(namespaceKey.id)
节点.拓扑.init_id_from_uid(
UniqueIdentifier.tryCreate("手动-" + node.name, 命名空间)
）

// 等待节点准备好接收节点身份。
node.health.wait_for_ready_for_node_拓扑()

// 创建自签名根证书。
node.拓扑.namespace_delegations.propose_delegation(
命名空间，
命名空间键，
可以签署所有映射，
）

// 将新键分配给该节点。
节点.拓扑.owner_to_key_mappings.propose(
成员=节点.id.成员，
键= NonEmpty（Seq，sequencerAuthKey，signingKey，加密密钥），
signedBy = Seq（namespaceKey.fingerprint，sequencerAuthKey.fingerprint，signingKey.fingerprint），
）

// 架构手册条目结束：ManualInitNode

}

}
```

and then import the certificates to the node.

This configuration directive has no effect once the node is initialized and can subsequently be removed.

### Delegation Restrictions

You can further restrict the kind of 拓扑 transactions a delegation can authorize. The `prepare-certs` script exposes a `--delegation-restrictions` flag for that purpose.

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
“$SCRIPTS_ROOT/prepare-certs.sh”--委托限制 PARTY_TO_PARTICIPANT，PARTY_TO_KEY_MAPPING --root-pub-key“$PUBLIC_KEY”--canton-target-pub-key“$CANTON_RESTRICTED_PUB_KEY”--输出“$RESTRICTED_KEY_NAMESPACE_PREFIX”
```

The delegation can then be signed and assembled as before. Once the signed certificate is available, load it onto the node:

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
参与者1.拓扑.transactions.load_single_from_file(s"$opensslKeysDirectory/restricted_key_namespace.cert", 拓扑StoreId.Authorized)
```

### Rotate the Intermediate Key

#### Create new Intermediate Key

In order to create another intermediate key, we follow the same steps as before. Create the key on the online site and export it.

Follow the same steps to create a new intermediate delegation for the new intermediate key:

* copy to secure site
* generate the intermediate delegation (skip self-signed root delegation as it has already been generated)
* copy the certificate to the node site

The new intermediate delegation can then be imported into the node as shown here.

Once the new delegation has been imported, the old intermediate key can be revoked.

#### Revoking the Intermediate Key

To revoke the intermediate key, the root key needs to be used to sign a revocation transaction. The revocation transaction is prepared in the same way as the intermediate delegation. Also, the generated hash needs to be signed and then subsequently assembled into a certificate:

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
./prepare-cert.sh --delegation-restrictions PARTY_TO_PARTICIPANT,PARTY_TO_KEY_MAPPING --root-pub-key "/tmp/canton/certs/root_public_key.der" --canton-target-pub-key "/tmp/canton/certs/restricted_key.pub" --output "/tmp/canton/certs/restricted_key_namespace"
```

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "/tmp/canton/certs/root_private_key.der" -keyform DER -sign -in "/tmp/canton/certs/restricted_key_namespace.hash" -out "/tmp/canton/certs/restricted_key_namespace.signature"
```

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
./assemble-cert.sh --prepared-transaction "/tmp/canton/certs/restricted_key_namespace.prep" --signature "/tmp/canton/certs/restricted_key_namespace.signature" --signature-algorithm "ed25519" --output "/tmp/canton/certs/restricted_key_namespace"
```

On the node site, the revocation certificate can be imported using:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@participant1.拓扑.transactions.load_single_from_file("/tmp/canton/certs/restricted_key_namespace.cert", 拓扑StoreId.Authorized)
````

#### 轮换根命名空间密钥

您无法轮换根命名空间密钥。如果您需要停止使用命名空间，则需要在该新命名空间中创建新的命名空间、新的各方和参与者，并将合约转移给新的各方。

{/* 已复制_END */}

## 配置会话密钥Canton 使用会话密钥来减少协议执行期间昂贵的加密操作，从而提高性能。有两种类型：会话加密密钥，可减少非对称加密的数量；会话签名密钥，有助于避免频繁调用 KMS 等外部签名者。

您可以在 [Canton 的加密密钥](/overview/learn/cryptographic-keys) 中阅读有关基本原理和安全注意事项的更多信息。

延长会话密钥的生命周期可以最大限度地减少重复密钥协商或远程签名的需要，但它也增加了密钥存储在内存中的时间窗口，从而增加了泄露的风险。

### 增加会话**加密**密钥的生命周期

您可以通过调整配置中的 `expire-after-timeout` 值来控制会话加密密钥保持活动状态的时间。要全局增加会话加密密钥的生命周期，请增加 `sender-cache` 和 `receiver-cache` 的 `expire-after-timeout`。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1 {
    caching {
        session-encryption-key-cache {
            # these are the default values
            enabled = true
            sender-cache {
                maximum-size = 10000
                expire-after-timeout = 10s
            }
            receiver-cache {
                maximum-size = 10000
                expire-after-timeout = 10s
            }
        }
    }
}
```

### 增加会话**签名**密钥的生命周期

使用外部 KMS（密钥管理服务）提供商时，您可以通过调整 `key-validity-duration` 和 `key-eviction-period` 来控制会话签名密钥保持活动状态的时间。 `key-eviction-period` 应始终比 `key-validity-duration` 长，并且至少与动态同步器参数中配置的 `confirmation_response_timeout` 和 `mediator_reaction_timeout` 之和一样长。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.kms {
  session-signing-keys {
    # these are the default values
    enabled = true
    key-validity-duration = 5m
    cut-off-duration = 30s,
    key-eviction-period = 10m,
    signing-algorithm-spec = ed-25519,
    signing-key-spec = ec-curve-25519,
  }
}
```

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
