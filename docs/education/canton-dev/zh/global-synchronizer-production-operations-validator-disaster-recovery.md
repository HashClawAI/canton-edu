---
title: "验证者灾难恢复"
slug: "global-synchronizer-production-operations-validator-disaster-recovery"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/validator-disaster-recovery.md"
source_title: "Validator Disaster Recovery"
tags:
  - global-synchronizer
  - production-operations
  - validator-disaster-recovery
---

# 验证者灾难恢复

> 验证者节点的灾难恢复与恢复流程。

> 验证者节点的灾难恢复和恢复程序

从灾难中恢复的方法有以下三种：

1. 在仅单个节点受到影响但整个网络仍然正常的简单情况下，从备份恢复通常就足够了。
2. 如果没有完整备份，但已经创建了身份备份，则验证者的余额可以在新的验证者上恢复。
3. 如果全局同步器发生故障，超级验证器将启动前滚逻辑同步器升级以前滚到新的物理同步器。验证者需要根据 SV 传达的信息在其节点上启动该程序。

> 仅当至少满足以下条件之一时，才可以追回资产：
>
> * 最近的数据库备份可用，或者：
> * 有最新的身份备份可用，或者：
> * 验证者参与者使用外部 KMS 来管理其密钥，并且 KMS 仍然保留这些密钥。 （请注意，仅从 KMS 密钥恢复验证器
> \- 即，没有身份备份或数据库备份 - 是一个涉及的过程，此处未明确记录。）
>
> 如果以上都不成立，则无法恢复相关参与者密钥来证明资产所有权。

## 从备份中恢复验证器

只要满足以下条件，就可以从备份恢复整个节点：

* 数据库备份可用。
* 数据库备份的时间少于 30 天。由于Sequencer 修剪，落后超过 30 天的参与者将无法赶上同步器以再次完全运行。
* 如果在同步器进行逻辑同步器升级之前进行备份，则仅当旧物理同步器上的同步器节点仍然可用时才可以从备份恢复节点。如果是这样，您必须首先恢复旧物理同步器上的节点，以便它可以赶上并在新物理同步器上完全运行。

如果上述情况之一不成立，则仍然可以使用下面讨论的重新登录过程来恢复节点。

可以采取以下步骤从备份恢复节点：

1. 将验证器节点中的所有组件缩减至 0 个副本。
2. 从备份中恢复所有组件的存储和数据库。其具体过程取决于组件使用的存储和数据库，此处未记录。
3. 恢复所有存储后，将验证器节点中的所有组件扩展回 1 个副本。

**注意：** 目前，您必须手动重新加入备份后加入的所有用户。

如果您正在运行 docker-compose 部署，则可以按如下方式恢复 Postgres 数据库：

1. 使用`./stop.sh`停止验证者和参与者。
2. 擦除现有数据库卷：`docker volume rm compose_postgres-splice`。
3.仅启动postgres容器：`docker compose up -d postgres-splice`
4.检查postgres是否准备好：`docker exec splice-验证者-postgres-splice-1 pg_isready`（重新运行此命令直到成功）
5. 恢复验证者数据库（假设 `验证者_dump_file` 包含您要从中恢复的转储的文件名）： `docker exec -i splice-验证者-postgres-splice-1 psql -U cnadmin 验证者 < $验证者_dump_file`
6. 恢复参与者数据库（假设`participant_dump_file`包含要从中恢复的转储的文件名，`migration_id`包含最新的迁移ID）：`docker exec -i splice-验证者-postgres-splice-1 psql -U cnadmin participant-$migration_id < $participant_dump_file`
7.停止postgres实例：`docker compose down`
8. 像往常一样启动验证器

## 从身份备份中恢复：重新启动验证器并恢复其托管的所有用户的余额如果验证器节点发生灾难性故障，验证器及其托管用户拥有的一些数据可以从 SV 中恢复。该数据包括 Canton Coin 余额和 CNS 条目。这是通过部署一个新的验证者节点来实现的，该节点可以控制原始验证器的命名空间密钥。命名空间密钥必须通过身份备份文件提供。新验证器使用它来将原始验证器上托管的各方迁移到新验证者。 SV 通过提供其所知的迁移方作为利益相关者的所有合同的信息来协助此过程。

以下步骤假设您有验证器身份的备份，如节点身份备份部分中创建的。如果您没有此类备份，但有验证者参与者数据库的备份，则可以手动组装身份备份。

为了从身份备份中恢复，我们部署了一个新的验证者，其具有如下所述的一些特殊配置。根据您选择的设置，请参阅 docker-compose 部署说明或 kubernetes 说明。

一旦新的验证者启动并运行，您应该能够以管理员身份登录并查看其余额。验证器上托管的其他用户将需要重新登录，但他们的代币余额和 CNS 条目应该恢复，并且可供重新登录的用户访问。

如有问题，请参阅下面的故障排除部分。

<Warning>
  此过程保留所有参与方 ID 以及与 DSO 参与方共享的所有合同。这意味着您“必须”保留相同的验证方提示，并且不需要新的加入秘密。如果您收到任何有关需要新的入门密码的错误，请仔细检查您的配置，而不是请求新的密码。
</Warning>

### Kubernetes 部署

要在 Kubernetes 部署中重新加入验证器并恢复其托管的所有用户的余额，请重复`helm-验证者-install`中描述的步骤来安装验证者应用和参与者。执行此操作时，请注意以下事项：

* 使用身份备份文件的内容创建 Kubernetes 密钥。假设您将环境变量`PARTICIPANT_BOOTSTRAP_DUMP_FILE`设置为备份文件路径，则可以使用以下命令创建密钥：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic participant-bootstrap-dump \
    --from-file=content=${PARTICIPANT_BOOTSTRAP_DUMP_FILE} \
    -n 验证者
```

* 取消 `standalone-验证者-values.yaml` 文件中以下行的注释。这将为验证者指定一个新的参与者 ID。将 `put-some-new-string-never-used-before` 替换为以前从未使用过的字符串。确保同时调整 `nodeIdentifier` 以匹配相同的值。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# participantIdentitiesDumpImport:
#   secretName: participant-bootstrap-dump
#   # Make sure to also adjust nodeIdentifier to the same value
#   newParticipantIdentifier: put-some-new-string-never-used-before
# migrate验证者Party: true
```

### Docker-Compose 部署

要在 Docker-compose 部署中重新加入验证器并恢复其托管的所有用户的余额，请输入：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./start.sh -s "<SPONSOR_SV_URL>" -o "" -p <party_hint> -m "<MIGRATION_ID>" -i "<node_identities_dump_file>" -P "<new_participant_id>" -w
```

其中 `<node_identities_dump_file>` 是包含节点身份备份的文件的路径，`<new_participant_id>` 是用于新参与者的新标识符。它一定是以前从未使用过的。请注意，在验证器的后续重新启动中，您应该继续为 `-P` 提供相同的 `<new_participant_id>`。

### 从参与者数据库备份获取身份备份

如果您没有可用的身份备份，但有验证者参与者数据库的备份，则可以手动组装身份备份。这是一种可能的方法：

1. 将数据库备份恢复到临时 postgres 实例中，并针对该实例部署临时参与者。* 请参阅有关从备份恢复验证器的部分，以获取与您的部署模型相匹配的指针。
   * 您只需要恢复和扩容参与者，即可忽略验证者应用及其数据库。
   * 如果恢复后的参与者因故障立即关闭，请添加以下附加配置：

   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   additionalEnvVars:
       - name: ADDITIONAL_CONFIG_EXIT_ON_FATAL_FAILURES
         value: canton.parameters.exit-on-fatal-failures = false
   ```

2. 为临时参与者打开Canton 控制台。

3. 在打开的控制台中运行以下命令。这会将备份存储到名为 `identities-dump.json` 的*本地*文件（相对于您打开控制台的本地目录）。

   ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.topology.transaction.拓扑Mapping
   import com.digitalasset.canton.topology.store.TimeQuery
   import java.util.Base64

   val id = participant.id.toProtoPrimitive

   // This line needs to be adapted if your participant stores keys in an external KMS
   val keys = "[" + participant.keys.secret.list().filter(k => k.name.get.unwrap != "cometbft-governance-keys").map(key => s"{\"keyPair\": \"${Base64.getEncoder.encodeToString(participant.keys.secret.download(key.publicKey.fingerprint).toByteArray)}\", \"name\": \"${key.name.get.unwrap}\"}") .mkString(",") + "]"

   val authorizedStoreSnapshot = Base64.getEncoder.encodeToString(participant.topology.transactions.export_拓扑_snapshot(timeQuery = TimeQuery.Range(from = None, until = None), filterMappings = Seq(拓扑Mapping.Code.NamespaceDelegation, 拓扑Mapping.Code.OwnerToKeyMapping, 拓扑Mapping.Code.VettedPackages), filterNamespace = participant.id.namespace.toProtoPrimitive).toByteArray)

   val combinedJson = s"""{ "id" : "$id", "keys" : $keys, "authorizedStoreSnapshot" : "$authorizedStoreSnapshot" }"""

   // Write to file
   import java.nio.file.{Files, Paths}
   val dumpPath = Paths.get("identities-dump.json")
   Files.writeString(dumpPath, combinedJson)
   ```

   请注意，如果您的参与者配置为将密钥存储在外部 KMS 中，则需要调整上述命令。

### 限制和故障排除

在某些非标准情况下，从密钥备份自动重新加入可能无法成功迁移（即恢复）一方。请检查验证器的日志中是否有可能提供线索的警告或错误条目。

#### 各方不会自动迁移

默认情况下不会迁移以下类型的参与方：

* 由多个参与者主办的聚会。这些可能会脱离原始（失败）参与者的托管，但仍将托管在任何其他参与者上。
* 验证器上托管的外部各方。这些可能会从原始（失败的）参与者中取消托管。有关如何恢复外部各方的说明，请参阅`验证者_recover_external_party`。

在某些情况下，您可能希望强制尝试对一组未自动迁移的各方进行迁移尝试。为此，您可以在验证者应用上设置 `parties-to-migrate` 配置选项。将尝试为您传递给此选项的每一方进行迁移。验证者应用的初始化将在第一次失败的迁移尝试时中断。

#### ACS 导入失败故障排除

<Tabs>
  <Tab title="DevNet (0.6.4)">
    如果您仍然发现问题，特别是在参与者日志中观察到 `ACS_COMMITMENT_MISMATCH` 警告，则在导入节点上托管的至少一方的活动合约时可能出现问题。另一个常见症状（如果验证者方受到影响）是您的验证者初始化失败并出现 `Unknown secret` 错误，并且您的验证者日志包含 `验证者License not found` 消息。要解决`ACS`导入失败的问题，您通常可以：1. 首先确保所有各方都托管在同一节点上。最常见的情况是各方仍然在旧节点上且具有旧的参与者 ID，或者已经迁移到新节点。您可以通过向网络上的任何参与者打开 Canton 控制台（即，您也可以向其他验证者或 SV 操作员询问此信息）并运行以下查询来进行检查，其中 \<namespace> 是 `::` 之后的部分，例如您的验证者方 ID。

       ```
       val syncId = participant.同步器s.list_connected().head.同步器Id
       participant.topology.party_to_participant_mappings.list(syncId, filterParticipant = <namespace>)
       ```

       如果各方都在同一节点上，则继续下一步。如果有的在旧节点，有的在新节点，则将旧节点的迁移到新节点，方法是打开新节点的控制台并运行以下命令（根据各方需要调整参数）：

       ```
       val participantId = participant.id // ID of the new participant
       participant.topology.party_to_participant_mappings.propose(<party-id>, Seq((participantId, <participant-permission>)), store = syncId)
       ```

    2. 如果所有各方均已位于新节点上，您可以尝试手动（重新）导入这些各方的 ACS。以下步骤涉及您的新验证器节点：

       1. 停止您的验证者应用。

       2. 打开该新验证器的参与者控制台并使其保持打开状态以进行后续步骤。

       3. 从 Canton 控制台运行：

          ```
          participant.同步器s.disconnect_all()
          ```

       4. 对于您想要迁移/重新导入 ACS 的每个 `PARTY_ID`：

          从常规 shell 运行（与启动 Canton 控制台的工作目录相同）：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body 'https://scan.sv-1.dev.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID' -H 'Content-Type: application/json' | jq -r .acs_snapshot | base64 -d > acs_snapshot
          ```

          从 Canton 控制台：

          ```
          participant.repair.import_acs("acs_snapshot")
          ```

       5. 从 Canton 控制台运行 `participant.同步器s.reconnect_all()`。

       6. 再次启动您的验证者应用。

    3. 如果上一步失败或者您选择不尝试，您可以使用新的参与者重试迁移过程。如果您的各方仍在您从中进行身份备份的原始节点上，您可以使用现有的备份。如果您的各方已迁移到新节点，请从新节点获取新的身份转储。如果新节点处于无法获取新转储的状态，请使用旧转储，但将 `id` 字段编辑为新节点的参与者 ID。您可以通过例如在Canton控制台中向与会者运行`participant.id.toProtoPrimitive`来获取正确格式的`id`。现在，您可以删除最初尝试恢复的节点，并在具有不同参与者 ID 前缀（即不同的 `newParticipantIdentifier` / `&lt;new_participant_id&gt;`，具体取决于您的部署模型）的新节点上使用调整后的转储再次尝试恢复过程。
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    如果您仍然发现问题，特别是在参与者日志中观察到 `ACS_COMMITMENT_MISMATCH` 警告，则在导入节点上托管的至少一方的活动合约时可能出现问题。另一个常见症状（如果验证者方受到影响）是您的验证者初始化失败并出现 `Unknown secret` 错误，并且您的验证者日志包含 `验证者License not found` 消息。要解决`ACS`导入失败的问题，您通常可以：

    1. 首先确保所有各方都托管在同一节点上。最常见的情况是各方仍然在旧节点上且具有旧的参与者 ID，或者已经迁移到新节点。您可以通过向网络上的任何参与者打开 Canton 控制台（即，您也可以向其他验证者或 SV 操作员询问此信息）并运行以下查询来进行检查，其中 \<namespace> 是 `::` 之后的部分，例如您的验证者方 ID。```
       val syncId = participant.同步器s.list_connected().head.同步器Id
       participant.topology.party_to_participant_mappings.list(syncId, filterParticipant = <namespace>)
       ```

       如果各方都在同一节点上，则继续下一步。如果有的在旧节点，有的在新节点，则将旧节点的迁移到新节点，方法是打开新节点的控制台并运行以下命令（根据各方需要调整参数）：

       ```
       val participantId = participant.id // ID of the new participant
       participant.topology.party_to_participant_mappings.propose(<party-id>, Seq((participantId, <participant-permission>)), store = syncId)
       ```

    2. 如果所有各方均已位于新节点上，您可以尝试手动（重新）导入这些各方的 ACS。以下步骤涉及您的新验证器节点：

       1. 停止您的验证者应用。

       2. 打开该新验证器的参与者控制台并使其保持打开状态以进行后续步骤。

       3. 从 Canton 控制台运行：

          ```
          participant.同步器s.disconnect_all()
          ```

       4. 对于您想要迁移/重新导入 ACS 的每个 `PARTY_ID`：

          从常规 shell 运行（与启动 Canton 控制台的工作目录相同）：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body 'https://scan.sv-1.test.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID' -H 'Content-Type: application/json' | jq -r .acs_snapshot | base64 -d > acs_snapshot
          ```

          从 Canton 控制台：

          ```
          participant.repair.import_acs("acs_snapshot")
          ```

       5. 从 Canton 控制台运行 `participant.同步器s.reconnect_all()`。

       6. 再次启动您的验证者应用。

    3. 如果上一步失败或者您选择不尝试，您可以使用新的参与者重试迁移过程。如果您的各方仍在您从中进行身份备份的原始节点上，您可以使用现有的备份。如果您的各方已迁移到新节点，请从新节点获取新的身份转储。如果新节点处于无法获取新转储的状态，请使用旧转储，但将 `id` 字段编辑为新节点的参与者 ID。您可以通过例如在 Canton 控制台中向与会者运行`participant.id.toProtoPrimitive` 来获取正确格式的`id`。现在，您可以删除最初尝试恢复的节点，并在具有不同参与者 ID 前缀（即不同的 `newParticipantIdentifier` / `&lt;new_participant_id&gt;`，具体取决于您的部署模型）的新节点上使用调整后的转储再次尝试恢复过程。
  </Tabs>

  <Tab title="主网 (0.6.2)">
    如果您仍然发现问题，特别是在参与者日志中观察到 `ACS_COMMITMENT_MISMATCH` 警告，则在导入节点上托管的至少一方的活动合约时可能出现问题。另一个常见症状（如果验证者方受到影响）是您的验证者初始化失败并出现 `Unknown secret` 错误，并且您的验证者日志包含 `验证者License not found` 消息。要解决`ACS`导入失败的问题，您通常可以：

    1. 首先确保所有各方都托管在同一节点上。最常见的情况是各方仍然在旧节点上且具有旧的参与者 ID，或者已经迁移到新节点。您可以通过向网络上的任何参与者打开 Canton 控制台（即，您也可以向其他验证者或 SV 操作员询问此信息）并运行以下查询来进行检查，其中 \<namespace> 是 `::` 之后的部分，例如您的验证者方 ID。

       ```
       val syncId = participant.同步器s.list_connected().head.同步器Id
       participant.topology.party_to_participant_mappings.list(syncId, filterParticipant = <namespace>)
       ```

       如果各方都在同一节点上，则继续下一步。如果有的在旧节点，有的在新节点，则将旧节点的迁移到新节点，方法是打开新节点的控制台并运行以下命令（根据各方需要调整参数）：```
       val participantId = participant.id // ID of the new participant
       participant.topology.party_to_participant_mappings.propose(<party-id>, Seq((participantId, <participant-permission>)), store = syncId)
       ```

    2. 如果所有各方均已位于新节点上，您可以尝试手动（重新）导入这些各方的 ACS。以下步骤涉及您的新验证器节点：

       1. 停止您的验证者应用。

       2. 打开该新验证器的参与者控制台并使其保持打开状态以进行后续步骤。

       3. 从 Canton 控制台运行：

          ```
          participant.同步器s.disconnect_all()
          ```

       4. 对于您想要迁移/重新导入 ACS 的每个 `PARTY_ID`：

          从常规 shell 运行（与启动 Canton 控制台的工作目录相同）：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body 'https://scan.sv-1.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID' -H 'Content-Type: application/json' | jq -r .acs_snapshot | base64 -d > acs_snapshot
          ```

          从 Canton 控制台：

          ```
          participant.repair.import_acs("acs_snapshot")
          ```

       5. 从 Canton 控制台运行 `participant.同步器s.reconnect_all()`。

       6. 再次启动您的验证者应用。

    3. 如果上一步失败或者您选择不尝试，您可以使用新的参与者重试迁移过程。如果您的各方仍在您从中进行身份备份的原始节点上，您可以使用现有的备份。如果您的各方已迁移到新节点，请从新节点获取新的身份转储。如果新节点处于无法获取新转储的状态，请使用旧转储，但将 `id` 字段编辑为新节点的参与者 ID。您可以通过例如在Canton控制台中向与会者运行`participant.id.toProtoPrimitive`来获取正确格式的`id`。现在，您可以删除最初尝试恢复的节点，并在具有不同参与者 ID 前缀（即不同的 `newParticipantIdentifier` / `&lt;new_participant_id&gt;`，具体取决于您的部署模型）的新节点上使用调整后的转储再次尝试恢复过程。
  </Tabs>
</Tabs>

#### 排除拓扑快照被拒绝的故障

在极少数情况下，重新加入过程可能会在`Import拓扑Snapshot`步骤失败，因为旧参与者 ID 的`OwnerToKeyMapping`在拓扑快照中签名数量不足。这仅影响最初在 Splice 0.4.1 或更早版本上加载的验证器，该验证器使用不需要映射密钥来共同签署`OwnerToKeyMapping`交易的 Canton 版本。您可以通过在参与者日志中查找以下消息来识别此问题：

```
Missing authorizers: ReferencedAuthorizations(extraKeys = <key-id>...)
Rejected transaction ... OwnerToKeyMapping(...) ... due to Not authorized
```

要解决此问题，请按照下列步骤操作：

1. 仅启动新参与者（没有验证者应用）。请勿擦除上次（失败的）重新登录尝试的状态。

2. 向新参与者打开 Canton 控制台并运行以下命令以建议更正后的`OwnerToKeyMapping`。将密钥 ID 前缀替换为参与者日志中被拒绝的`OwnerToKeyMapping` 中的前缀，并将旧参与者 ID 替换为您实际的旧参与者 ID：

   ```
   val keys = Seq("<signing-key-id-prefix>", "<encryption-key-id-prefix>").map(prefix =>
     participant.keys.public.list().filter(_.publicKey.id.toProtoPrimitive.startsWith(prefix)).head.publicKey)

   val oldParticipantId = ParticipantId.fromProtoPrimitive("<old-participant-id>", "participant").toOption.get
   val otk = OwnerToKeyMapping(member = oldParticipantId, keys = NonEmpty.from(keys).get)
   participant.topology.owner_to_key_mappings.propose(otk, force = ForceFlag.AlienMember)
   ```

3. 使用原始身份转储配置启动验证者应用。

## 恢复外部方的Coin余额

<Tabs>
  <Tab title="DevNet (0.6.4)">
    对于依赖外部签名的一方，可以使用类似的程序来恢复其代币余额，以防最初托管该代币的验证器因某种原因变得无法使用。<Warning>
      恢复后用于托管聚会的目标验证器**必须**是**全新的验证者**。由于参与方迁移的一些限制，现有的验证器可能会完全变砖，并且目前无法从中恢复。从身份备份中恢复验证器在这里并不归类为全新的验证者。您必须使用全新的身份和完全干净的数据库来设置它。这一限制预计将来会被取消。
    </Warning>

    首先，按照标准验证者部署文档设置一个新的验证者。

    接下来，将 Canton 控制台连接到该新验证者。

    现在，我们需要签署并提交拓扑交易，以在新节点上托管外部方，并为该方导入 ACS。

    为此，首先生成拓扑事务。请注意，此处的说明假设聚会仅托管在单个参与者节点上。如果您想将其托管在多个节点上，则需要对此进行调整。

    ```
    // replace YOUR_PARTY_ID by the ID of your external party
    val partyId = PartyId.tryFromProtoPrimitive("YOUR_PARTY_ID")
    val participantId = participant.id
    val 同步器Id = participant.同步器s.id_of("global")

    // generate 拓扑 transaction
    val partyToParticipant = PartyToParticipant.tryCreate(
        partyId = partyId,
        threshold = PositiveInt.one,
        participants = Seq(
          HostingParticipant(
            participantId,
            ParticipantPermission.Confirmation,
          )
        ),
      )

    import com.digitalasset.canton.admin.api.client.commands.拓扑AdminCommands.Write.GenerateTransactions
    val 拓扑Transaction = participant.topology.transactions.generate(
      Seq(
        GenerateTransactions.Proposal(
          partyToParticipant,
          拓扑StoreId.同步器(同步器Id),
        )
      )
    ).head

    // Print out the hash that needs to be signed. Note that you need to sign
    // the actual bytes the hex string represents not the hex string
    拓扑Transaction.hash.hash.toHexString
    ```

    稍后我们将再次需要拓扑事务和此处定义的定义。要么保持 Canton 控制台打开，要么保存它们。

    拓扑事务哈希需要按照[外部签名文档](/zh/docs/canton/appdev-deep-dives-external-signing#external-party-入驻-transactions)进行外部签名。

    外部签名后，需要构建签名的拓扑交易，通过参与者进行额外签名，然后通过同步器提交。

    ```
    // Replace HASH_SIGNATURE_HEXSTRING with the signed 拓扑 transaction hash
    val signature = Signature.fromExternalSigning(SignatureFormat.Raw, HexString.parseToByteString("HASH_SIGNATURE_HEXSTRING").get, partyId.namespace.fingerprint, SigningAlgorithmSpec.Ed25519)
    val 拓扑TxSignedByParty = Signed拓扑Transaction.create(
      拓扑Transaction,
      NonEmpty(Set, SingleTransactionSignature(拓扑Transaction.hash, signature): 拓扑TransactionSignature),
      isProposal = false,
      ProtocolVersion.v34,
    )
    val 拓扑TxSignedByBoth = participant.topology.transactions.sign(
      拓扑TxSignedByParty,
      拓扑StoreId.同步器(同步器Id),
      signedBy = Seq(participantId.namespace.fingerprint)
    )
    participant.topology.transactions.load(
      拓扑TxSignedByBoth,
      拓扑StoreId.同步器(同步器Id),
    )
    ```

    我们现在可以检查拓扑事务是否已正确应用并获取 `validFrom` 时间：```
    // The detailed output will slightly vary. Make sure that you see the new participant ID though.
    participant.topology.party_to_participant_mappings.list(同步器Id, filterParty = partyId.filterString)
      res36: Seq[拓扑.ListPartyToParticipantResult] = Vector(
        ListPartyToParticipantResult(
          context = BaseResult(
            storeId = 同步器(id = global-domain::122025296c61...),
            validFrom = 2025-05-14T10:19:33.534074Z,
            validUntil = None,
            sequenced = 2025-05-14T10:19:33.534074Z,
            operation = Replace,
            transactionHash = <ByteString@2d53bfcc size=34 contents="\022 \320\215d\276\352m)\316 \231\345 \360\252WQB\331\3668\216\362\022\342S\310k\vF\267\347\374">,
            serial = PositiveNumeric(value = 1),
            signedBy = Vector(1220b529c1d9...)
          ),
          item = PartyToParticipant(YOUR_PARTY_ID, PositiveNumeric(1), Vector(HostingParticipant(YOUR_PARTICIPANT_ID..., Submission)))
        )
      )
    ```

    在此示例中，validFrom 时间为`2025-05-14T10:19:33.534074Z`。

    我们现在可以查询 CC Scan 以获取一方的活动合约集 (ACS) 并将其写入文件`acs_snapshot`：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Make sure to adjust YOUR_VALID_FROM to the time you got from the previous query and YOUR_PARY_ID
    curl -sSL --fail-with-body 'https://scan.sv-1.dev.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID?record_time=YOUR_VALID_FROM' -H 'Content-Type: application/json' | jq -r .acs_snapshot | base64 -d > acs_snapshot
    ```

    最后，我们可以导入 ACS：

    ```
    participant.同步器s.disconnect_all()
    participant.repair.import_acs("acs_snapshot")
    participant.同步器s.reconnect_all()
    ```

    该方现在托管在节点上并且可以参与交易。最后一步是设置必要的合约，以允许验证器自动化更新传输预批准并完成传输命令。为此，请执行与团队初始加入相同的流程，即`/v0/admin/external-party/setup-proposal`、`/v0/admin/external-party/setup-proposal/prepare-accept` 和 `/v0/admin/external-party/setup-proposal/submit-accept`。有关详细信息，请参阅验证器外部签名 API 的文档。
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    对于依赖外部签名的一方，可以使用类似的程序来恢复其代币余额，以防最初托管该代币的验证器因某种原因变得无法使用。

    <Warning>
      恢复后用于托管聚会的目标验证器**必须**是**全新的验证者**。由于参与方迁移的一些限制，现有的验证器可能会完全变砖，并且目前无法从中恢复。从身份备份中恢复验证器在这里并不归类为全新的验证者。您必须使用全新的身份和完全干净的数据库来设置它。这一限制预计将来会被取消。
    </Warning>

    首先，按照标准验证者部署文档设置一个新的验证者。

    接下来，将 Canton 控制台连接到该新验证者。

    现在，我们需要签署并提交拓扑交易，以在新节点上托管外部方，并为该方导入 ACS。

    为此，首先生成拓扑事务。请注意，此处的说明假设聚会仅托管在单个参与者节点上。如果您想将其托管在多个节点上，则需要对此进行调整。

    ````
    // 将 YOUR_PARTY_ID 替换为您的外部方的 ID
    val partyId = PartyId.tryFromProtoPrimitive("YOUR_PARTY_ID")
    val 参与者 ID = 参与者.id
    val 同步器Id =参与者.同步器s.id_of("全局")

    // 生成拓扑交易
    val partyToParticipant = PartyToParticipant.tryCreate(
        派对 ID = 派对 ID,
        阈值= PositiveInt.one，
        参与者 = 序列（
          主办参与者(
            参与者ID,
            参与者许可.确认,
          ）
        ),
      ）导入 com.digitalasset.canton.admin.api.client.commands.拓扑AdminCommands.Write.GenerateTransactions
    val拓扑Transaction =参与者.topology.transactions.generate(
      序列（
        生成交易.提案(
          partyTo参与者，
          拓扑StoreId.同步器(同步器Id),
        ）
      ）
    ).头

    // 打印出需要签名的哈希值。请注意，您需要签名
    // 十六进制字符串代表的实际字节不是十六进制字符串
    拓扑事务.hash.hash.toHexString
    ```

    We'll need the 拓扑 transaction and the definitions defined here later again. Either keep your Canton console open or save them.

    The 拓扑 transaction hash needs to be signed externally following the [documentation for external signing](/zh/docs/canton/appdev-deep-dives-external-signing#external-party-入驻-transactions).

    After you signed it externally, you need to construct the signed 拓扑 transaction, sign it additionally through the participant and then submit it through the 同步器.

    ```
    // 将 HASH_SIGNATURE_HEXSTRING 替换为签名的拓扑交易哈希
    val 签名 = Signature.fromExternalSigning(SignatureFormat.Raw, HexString.parseToByteString("HASH_SIGNATURE_HEXSTRING").get, partyId.namespace.fingerprint, SigningAlgorithmSpec.Ed25519)
    val拓扑TxSignedByParty = Signed拓扑Transaction.create(
      拓扑事务，
      NonEmpty(Set, SingleTransactionSignature(拓扑Transaction.hash, 签名): 拓扑TransactionSignature),
      提议=假，
      协议版本.v34,
    ）
    val拓扑TxSignedByBoth =参与者.topology.交易.sign(
      拓扑TxSignedByParty，
      拓扑StoreId.同步器(同步器Id),
      signedBy = Seq(participantId.namespace.fingerprint)
    ）
    参与者.topology.交易.负载(
      拓扑TxSignedByBoth，
      拓扑StoreId.同步器(同步器Id),
    ）
    ```

    We can now check that the 拓扑 transaction got correctly applied and get the `validFrom` time:

    ```
    // 详细输出会略有不同。但请确保您看到新的参与者 ID。
    参与者.topology.party_to_participant_mappings.list（同步器Id，filterParty = partyId.filterString）
      res36: Seq[拓扑.ListPartyToParticipantResult] = Vector(
        ListPartyToParticipantResult(
          上下文=基本结果（
            storeId = 同步器(id = 全局域::122025296c61...),
            有效来自 = 2025-05-14T10:19:33.534074Z,
            有效直到=无，
            测序 = 2025-05-14T10:19:33.534074Z,
            操作=更换，
            transactionHash = <ByteString@2d53bfcc size=34 content="\022 \320\215d\276\352m)\316 \231\345 \360\252WQB\331\3668\216\362\022\342S\310k\vF\267\347\374">,
            序列 = PositiveNumeric(值 = 1),
            有符号 = 矢量（1220b529c1d9...）
          ),
          item = PartyToParticipant(YOUR_PARTY_ID, PositiveNumeric(1), Vector(HostingParticipant(YOUR_PARTICIPANT_ID..., 提交)))
        ）
      ）
    ```

    In this example, the validFrom time is `2025-05-14T10:19:33.534074Z`.

    We can now query CC Scan to get the active contract set (ACS) for a party and write it to the file `acs_snapshot`:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // 确保将 YOUR_VALID_FROM 调整为从上一个查询获得的时间和 YOUR_PARY_ID
    curl -sSL --fail-with-body 'https://scan.sv-1.test.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID?record_time=YOUR_VALID_FROM' -H '内容类型：application/json' | jq -r .acs_snapshot | jq -r .acs_snapshot | base64 -d > acs_snapshot
    ```

    Lastly, we can import the ACS:

    ```
    参与者.同步器s.disconnect_all()
    参与者.repair.import_acs("acs_snapshot")
    参与者.同步器s.reconnect_all()
    ````

    该方现在托管在节点上并且可以参与交易。最后一步是设置必要的合约，以允许验证器自动化更新传输预批准并完成传输命令。为此，请执行与团队初始加入相同的流程，即`/v0/admin/external-party/setup-proposal`、`/v0/admin/external-party/setup-proposal/prepare-accept` 和 `/v0/admin/external-party/setup-proposal/submit-accept`。有关详细信息，请参阅验证器外部签名 API 的文档。
  </Tabs><Tab title="主网 (0.6.2)">
    对于依赖外部签名的一方，可以使用类似的程序来恢复其代币余额，以防最初托管该代币的验证器因某种原因变得无法使用。

    <Warning>
      恢复后用于托管聚会的目标验证器**必须**是**全新的验证者**。由于参与方迁移的一些限制，现有的验证器可能会完全变砖，并且目前无法从中恢复。从身份备份中恢复验证器在这里并不归类为全新的验证者。您必须使用全新的身份和完全干净的数据库来设置它。这一限制预计将来会被取消。
    </Warning>

    首先，按照标准验证者部署文档设置一个新的验证者。

    接下来，将 Canton 控制台连接到该新验证者。

    现在，我们需要签署并提交拓扑交易，以在新节点上托管外部方，并为该方导入 ACS。

    为此，首先生成拓扑事务。请注意，此处的说明假设聚会仅托管在单个参与者节点上。如果您想将其托管在多个节点上，则需要对此进行调整。

    ```
    // replace YOUR_PARTY_ID by the ID of your external party
    val partyId = PartyId.tryFromProtoPrimitive("YOUR_PARTY_ID")
    val participantId = participant.id
    val 同步器Id = participant.同步器s.id_of("global")

    // generate 拓扑 transaction
    val partyToParticipant = PartyToParticipant.tryCreate(
        partyId = partyId,
        threshold = PositiveInt.one,
        participants = Seq(
          HostingParticipant(
            participantId,
            ParticipantPermission.Confirmation,
          )
        ),
      )

    import com.digitalasset.canton.admin.api.client.commands.拓扑AdminCommands.Write.GenerateTransactions
    val 拓扑Transaction = participant.topology.transactions.generate(
      Seq(
        GenerateTransactions.Proposal(
          partyToParticipant,
          拓扑StoreId.同步器(同步器Id),
        )
      )
    ).head

    // Print out the hash that needs to be signed. Note that you need to sign
    // the actual bytes the hex string represents not the hex string
    拓扑Transaction.hash.hash.toHexString
    ```

    稍后我们将再次需要拓扑事务和此处定义的定义。要么保持 Canton 控制台打开，要么保存它们。

    拓扑事务哈希需要按照[外部签名文档](/zh/docs/canton/appdev-deep-dives-external-signing#external-party-入驻-transactions)进行外部签名。

    外部签名后，需要构建签名的拓扑交易，通过参与者进行额外签名，然后通过同步器提交。

    ```
    // Replace HASH_SIGNATURE_HEXSTRING with the signed 拓扑 transaction hash
    val signature = Signature.fromExternalSigning(SignatureFormat.Raw, HexString.parseToByteString("HASH_SIGNATURE_HEXSTRING").get, partyId.namespace.fingerprint, SigningAlgorithmSpec.Ed25519)
    val 拓扑TxSignedByParty = Signed拓扑Transaction.create(
      拓扑Transaction,
      NonEmpty(Set, SingleTransactionSignature(拓扑Transaction.hash, signature): 拓扑TransactionSignature),
      isProposal = false,
      ProtocolVersion.v34,
    )
    val 拓扑TxSignedByBoth = participant.topology.transactions.sign(
      拓扑TxSignedByParty,
      拓扑StoreId.同步器(同步器Id),
      signedBy = Seq(participantId.namespace.fingerprint)
    )
    participant.topology.transactions.load(
      拓扑TxSignedByBoth,
      拓扑StoreId.同步器(同步器Id),
    )
    ```

    我们现在可以检查拓扑事务是否已正确应用并获取 `validFrom` 时间：```
    // The detailed output will slightly vary. Make sure that you see the new participant ID though.
    participant.topology.party_to_participant_mappings.list(同步器Id, filterParty = partyId.filterString)
      res36: Seq[拓扑.ListPartyToParticipantResult] = Vector(
        ListPartyToParticipantResult(
          context = BaseResult(
            storeId = 同步器(id = global-domain::122025296c61...),
            validFrom = 2025-05-14T10:19:33.534074Z,
            validUntil = None,
            sequenced = 2025-05-14T10:19:33.534074Z,
            operation = Replace,
            transactionHash = <ByteString@2d53bfcc size=34 contents="\022 \320\215d\276\352m)\316 \231\345 \360\252WQB\331\3668\216\362\022\342S\310k\vF\267\347\374">,
            serial = PositiveNumeric(value = 1),
            signedBy = Vector(1220b529c1d9...)
          ),
          item = PartyToParticipant(YOUR_PARTY_ID, PositiveNumeric(1), Vector(HostingParticipant(YOUR_PARTICIPANT_ID..., Submission)))
        )
      )
    ```

    在此示例中，validFrom 时间为`2025-05-14T10:19:33.534074Z`。

    我们现在可以查询 CC Scan 以获取一方的活动合约集 (ACS) 并将其写入文件`acs_snapshot`：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    // Make sure to adjust YOUR_VALID_FROM to the time you got from the previous query and YOUR_PARY_ID
    curl -sSL --fail-with-body 'https://scan.sv-1.global.canton.network.sync.global/api/scan/v0/acs/YOUR_PARTY_ID?record_time=YOUR_VALID_FROM' -H 'Content-Type: application/json' | jq -r .acs_snapshot | base64 -d > acs_snapshot
    ```

    最后，我们可以导入 ACS：

    ```
    participant.同步器s.disconnect_all()
    participant.repair.import_acs("acs_snapshot")
    participant.同步器s.reconnect_all()
    ```

    该方现在托管在节点上并且可以参与交易。最后一步是设置必要的合约，以允许验证器自动化更新传输预批准并完成传输命令。为此，请执行与团队初始加入相同的流程，即`/v0/admin/external-party/setup-proposal`、`/v0/admin/external-party/setup-proposal/prepare-accept` 和 `/v0/admin/external-party/setup-proposal/submit-accept`。有关详细信息，请参阅验证器外部签名 API 的文档。
  </Tabs>
</Tabs>

## 前滚逻辑同步器升级

如果 SV 通知它们从物理同步器丢失中恢复，它们将通知 `newPhysical同步器Id` 和 `sequencerSuccessors`。

然后验证者需要：

1. 等待其节点完成追赶现有同步器上的最新事务。一个很好的指标是您在参与者信息日志中没有看到任何包含 `Processing event at` 的新日志。
2. 通过 Canton 控制台启动前滚 LSU：

```
val existingPhysical同步器Id = participant.同步器s.list_connected().find(_.同步器Alias == "global").head.physical同步器Id
participant.同步器s.perform_manual_lsu(
  existingPhysical同步器Id,
  newPhysical同步器Id,
  upgradeTime = None,
  sequencerSuccessors,
)
```

### 解决 ACS 不匹配问题

请注意，根据旧同步器失败的具体情况，如果某些验证器在失败之前观察到事务而其他验证器没有观察到，则验证器可能会不同步。在这种情况下，参与者将产生 ACS 不匹配，在迁移到新的物理同步器后，应使用[标准 ACS 不匹配解决过程](/zh/docs/canton/global-synchronizer-troubleshooting-guide-transaction-failures#troubleshoot-acs-commitments) 来解决这些不匹配。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
