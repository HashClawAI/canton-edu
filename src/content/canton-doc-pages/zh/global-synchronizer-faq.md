---
title: "常见问题"
slug: "global-synchronizer-faq"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/faq.md"
source_title: "FAQ"
tags:
  - global-synchronizer
  - faq
---

# 常见问题

> Canton Network 验证者与超级验证者常见问题解答。

> Canton Network 验证者和超级验证者常见问题解答

## 超级验证者

<div className="glossary">
  在哪里可以找到所有列入白名单的节点运营商？

  > 所有列入白名单的 SV 均列在 [公共全局同步器配置存储库](https://github.com/global-synchronizer-foundation/configs) 中。

  在哪里生成验证者入门令牌？

  > SV 在 SV UI 中生成验证者加入令牌。
</div>

## 验证者

<div className="glossary">
  我的验证者入门令牌的有效期是多长时间？

  > 对于 SV 创建的机密，它们可以使用 48 小时；对于通过 DevNet 自助接入端点创建的机密，它们可以使用 1 小时。它们仅供一次性使用。

  如何查看我的验证者活跃度奖励？

  > 您可以通过检查交易历史记录来检查验证人的活跃度奖励，并查找产生验证人奖励的交易。
  >
  > <img src="https://mintcdn.com/cantonfoundation/eCttQejvyGlU5PC2/images/splice/transaction_history.png?fit=max&auto=format&n=eCttQejvyGlU5PC2&q=85&s=1f98314e5c77507ffe9b1d78c31a0e70" width="700" alt="显示验证者奖励交易的交易历史记录。" data-path="images/splice/transaction_history.png" />

  如何确定特定交易使用的流量？> 从 Splice 0.5.x 开始，有两个选项：(1) 使用准备交易返回的流量成本估算，或 (2) 检查参与者日志以了解实际使用的流量。
  >
  > **选项1：**调用`/v2/interactive-submission/prepare` [Ledger API端点](https://github.com/digital-asset/canton/blob/025cdcf3c04ef052f775d6ccfb88c049a82d65a8/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L1916) 并检查响应中的 `costEstimation` 字段。它包含用于提交的流量和用于确认的流量的估计。这是一个估计，因为拓扑状态可能会在准备和提交事务之间发生变化。
  >
  > **选项 2：** 检查参与者日志以了解用于特定事务的实际流量。为此，请按照下列步骤操作：
  >
  > 1. 确保您在参与者配置中启用了 `DEBUG` 日志。
  > 2. 确定参与者日志中命令提交的跟踪 ID。
  > 3. 搜索包含 `EventCost` 和 `trace-id` 的`DEBUG` 日志行。由于 [Canton 协议](/zh/docs/canton/overview-learn-architecture) 的工作原理，通常有两个这样的日志行。第一个是提交确认请求的成本，第二个是提交参与方节点进行的 tx 验证的确认响应的成本。
  >
  > 例如，以下日志行（由 lnav 漂亮地打印）显示了来自点击某个 Amulet 的跟踪 id `1e2d6bf54d150e230fd0c7f348707bf6` 的命令提交。
  >
  > ````text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  > 2025-07-10T14:39:43.155Z [⋮] INFO - c.d.c.p.a.s.c.CommandSubmissionServiceImpl:participant=aliceParticipant (1e2d6bf54d150e230fd0c7f348707bf6---) - Phase 1 started: Submitting commands for interpretation: Commands(
  >   commandId = org.lfdecentralizedtrust.splice.钱包.tap_92d9ffae4bd90068a15dad747559ed641572f057e3beb03f2a9b024f388bdc20,
  >   submissionId = 0a3e62aa-c4e7-44ba-ad8a-fdbd0e55b9e9,
  >   userId = alice_验证者_user-b7e18d55,
  >   actAs = alice-验证者b7e18d55-1::12204bfd2aa7...,
  >   readAs = alice__钱包__user-b7e18d55__tc0::12204bfd2aa7...,
  >   submittedAt = 2025-07-10T14:39:43.154021Z,
  >   ledgerEffectiveTime = 1970-01-01T01:11:10Z,
  >   deduplicationPeriod = (duration=PT24H),
  >   同步器Id = global-domain::12203755b6a7...,
  >   ...
  > ).
  > ```文字
  >
  > 搜索与模式 `aliceParticipant.*1e2d6bf54d150e230fd0c7f348707bf6.*EventCost` 匹配的日志行将产生以下两条日志行：
  >
  > ``` text
  > 2025-07-10T14:39:43.202Z [⋮] DEBUG - c.d.c.s.t.流量StateController:participant=aliceParticipant/同步器Id=global-domain::12203755b6a7 (1e2d6bf54d150e230fd0c7f348707bf6---) - Computed following cost for submission request using 拓扑 at 1970-01-01T01:11:10.000177Z: EventCostDetails(
  >   cost multiplier = 4,
  >   group to members size = MediatorGroupRecipient(group = 0) -> 1,
  >   envelopes cost details = Seq(
  >     EnvelopeCostDetails(write cost = 1541, read cost = 0, final cost = 1541, recipients = MediatorGroupRecipient(group = 0)),
  >     EnvelopeCostDetails(
  >       write cost = 137,
  >       read cost = 0,
  >       final cost = 137,
  >       recipients = Seq(MemberRecipient(PAR::alice验证者::12204bfd2aa7...), MediatorGroupRecipient(group = 0), MemberRecipient(PAR::sv1::1220c1e24991...))
  >     ),
  >     EnvelopeCostDetails(write cost = 1904, read cost = 0, final cost = 1904, recipients = MemberRecipient(PAR::alice验证者::12204bfd2aa7...)),
  >     EnvelopeCostDetails(write cost = 2509, read cost = 2, final cost = 2511, recipients = Seq(MemberRecipient(PAR::alice验证者::12204bfd2aa7...), MemberRecipient(PAR::sv1::1220c1e24991...)))
  >   ),
  >   event cost = 6093
  > )
  > 2025-07-10T14:39:43.414Z [⋮] DEBUG - c.d.c.s.t.流量StateController:participant=aliceParticipant/同步器Id=global-domain::12203755b6a7 (1e2d6bf54d150e230fd0c7f348707bf6---) - Computed following cost for submission request using 拓扑 at 1970-01-01T01:11:10.000179Z: EventCostDetails(
  >   cost multiplier = 4,
  >   group to members size = MediatorGroupRecipient(group = 0) -> 1,
  >   envelopes cost details = EnvelopeCostDetails(write cost = 651, read cost = 0, final cost = 651, recipients = MediatorGroupRecipient(group = 0)),
  >   event cost = 651
  > )
  > ```文字
  >
  > 因此提交确认请求花费了6093字节的流量，提交确认响应花费了651字节的流量。
  >
  > 阅读成本是指将信封递送给所有收件人的成本。计算公式为 `readCost = writeCost * #recipients * costMultiplier / 10_000` （[代码]（https://github.com/digital-asset/canton/blob/1f7d0513843ae791f870ac2caeb4402f73109f86/community/base/src/main/scala/com/digitalasset/canton/sequencing/流量/EventCostCalculator.scala#L118-L123））。
  >````是否有 API 可以获取验证方 ID？

  > 请参阅 [/v0/验证者-user](https://github.com/canton-network/splice/blob/c712e75775a7d3229eff2a1837b06417a02b03f3/apps/验证者/src/main/openapi/验证者-internal.yaml#L14)。
</div>

## 应用程序开发

### JSON API

<div className="glossary">
  如何通过 JSON API 获取超过 200 个 ACS 条目？

  > 有一个服务器限制，默认为 200。可以如下所示更新配置文件，其中它将 `http-list-max-elements-limit` 的值增加到 1,000。
  >
  > ````text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  > canton {
  >   participants {
  >     participant1 {
  >       http-ledger-api {
  >         address = 0.0.0.0
  >         port = 10010
  >         port-file = "./json.port"
  >         path-prefix = "my-prefix"
  >         websocket-config {
  >             http-list-max-elements-limit = 1000,
  >             http-list-wait-time = 2s,
  >         }
  >         daml-definitions-service-enabled = true
  >       }
  >     }
  >   }
  > }
  > ```文字
  >
  > 根据添加临时配置中的信息，将环境变量 `ADDITIONAL_CONFIG_JSON_LIMIT=canton.participants.participant.http-ledger-api.websocket-config { http-list-max-elements-limit = 1000, http-list-wait-time = 2s }` 添加到您的 Canton 参与者 docker 进程。
  >
  > 然后您可以在请求中添加额外的查询`(?limit=xyz)`限制，但结果永远不会超出服务器限制。
  >
  > 一种替代方法是使用没有硬性限制的 [websockets API](/reference/json-api-asyncapi-reference)。
  >
  > 另一种选择是使用 [PQS](/appdev/deep-dives/query-with-pqs)，它可以通过 [Daml Shell](/sdks-tools/cli-tools/daml-shell#contract-summaries) 简化调试。
  >````

  如何创建具有多个根节点的交易？

  > 可能发生这种情况的一个示例是一项事务，其中一个根用于标记创建，一个根用于实际用户命令。此错误消息表示尝试具有多个根的事务：`Only single root transactions can currently be externally signed`。
  >
  > 推荐的方法是将这两个调用包装在一个小助手合约中。这是[示例](https://github.com/canton-network/splice/pull/1907/files#diff-90d0ed0955b3e59b9edec55e5191d155335bae39a258dbd029b53a4e53e15db3)。

  我们的应用程序如何将注册的公钥与其对应方进行匹配，以识别与已注册用户关联的方？

  > 有多种选择。
  >
  >> * 使用 Canton API，[调用listPartyToKeyMappingRequest](https://github.com/digital-asset/canton/blob/eeb56bc5d9779a7f918893b7a6b15e0b312a044e/社区/base/src/main/protobuf/com/digitalasset/canton/拓扑/admin/v30/拓扑_manager_read_service.proto#L19)没有过滤器，然后反转映射，将其存储在本地（例如，在数据库中）以便快速访问。
  >> * 使映射具有确定性。各方采用格式`name::key_fingerprint`，其中指纹是根据公钥计算的。因此，如果您始终选择确定性名称（例如“分类帐”或其他指纹），那么您根本不需要读取映射，因为您可以计算指纹。如果您开始对“命名空间根”使用不同的密钥，则此处需要特别考虑，该密钥确定指纹、签名密钥和/或委托的“中间命名空间密钥”。
  >> * 您还可以通过 `base_query` 中的 `filter_signed_key` 字段按签名密钥进行过滤。如果你使用派对的指纹，它应该会给你一个不错的过滤器。任何`List***Request`都可以使用[API](https://github.com/digital-asset/canton/blob/eeb56bc5d9779a7f918893b7a6b15e0b312a044e/community/base/src/main/protobuf/com/digitalasset/canton/拓扑/admin/v30/拓扑_manager_read_service.proto#L14)，例如`ListPartyToKeyMapping`。

  如何找到开发/测试/主网版本的最新 API 版本的规范？> Canton Network的能力一直在增强，因此您需要使用最新的API版本规范。 JSON API 或 gRPC API 的步骤类似。
  >
  >> * 对于 JSON API 的 OpenAPI 或 AsyncAPI 规范，请按照以下步骤操作：
  >> * 在 [版本兼容性仪表板](/shared/version-compatibility-dashboard) 中查找网络的 SDK 版本。
  >> * 记录Canton版本的主要和次要 semver 数字。例如，如果快照是`3.3.0-snapshot.20250827.16063.0.vdc9a8874`，则重要版本信息是`3.3`。
  >> * 前往开源 [Canton Git repo](https://github.com/digital-asset/canton)。
  >> * 通过选择显示 `main` 的下拉菜单来选择适当的发布行，以公开可用的不同分支。然后选择与上面找到的版本相同的发布线。在本例中，要选择的释放线是`release-line-3.3`。
  >> * 这是该发行版的最新代码。因此，沿着路径 `/canton/tree/main/community/ledger/ledger-json-api/src/test/resources/json-api-docs` 到达 `openapi.yaml` 和 `asyncapi.yaml` 文件。
  >> * JSON API 规范的另一个来源是从正在运行的 Canton 参与方节点检索它们。对此的描述位于 [验证 - 下载 OpenAPI](/sdks-tools/api-reference/json-api#configuration) 部分。规格如下：
  >> * 对于 OpenAPI：`http://<host>:<port>/docs/openapi`
  >> * 对于 AsyncAPI：`http://<host>:<port>/docs/asyncapi`
  >> * 对于 GRPC protobuf 定义，请遵循与上述相同的步骤，但将最后一步更改为：
  >> * 沿着路径 `/community/ledger-api/src/main/protobuf/com/daml/ledger/api/v2` 到达 `proto` 文件。

  是否有使用 json api 的 websocket 版本的工作示例？

  > 有可用的示例。请参阅[此处](https://github.com/digital-asset/canton/tree/main/community/app/src/pack/examples/09-json-api)。此 [文件](https://github.com/digital-asset/canton/blob/main/community/app/src/pack/examples/09-json-api/wsacs.sh) 通过 websocket 发送请求，作为场景的一部分，该场景中描述[README.md](https://github.com/digital-asset/canton/blob/main/community/app/src/pack/examples/09-json-api/README.md)。

  `v2/updates/trees` JSON ledger api 已弃用，那么用什么来替代它呢？

  > 3.3 中添加了`v2/updates`，即将推出。在此期间，您可以使用 `v2/updates/flat`，其行为与 `UpdateService.GetUpdates` 相同。
</div>

### 代币标准

<div className="glossary">
  将代币标准的 `DAR` 文件包含到我的 `daml` 项目中以供数据依赖项指向，最佳实践是什么？

  > * 从 [repo](https://github.com/canton-network/splice/tree/main/daml/dars) 复制代币标准 dars 并将其签入您自己的 repo 中。
  > * 确保您的主文件仅依赖于 `splice-token-api-*` 包。这些保证是稳定的。
  > * 将工作流程的 Daml 脚本测试放入单独的 `*-test` daml 项目中，如 [splice] 中所做的那样（https://github.com/canton-network/splice/tree/b91cf9a77bad6c513658401a57db87d975f9a526/token-standard/splice-token-standard-test）。有关详细信息，请参阅 [daml.yaml](https://github.com/canton-network/splice/blob/b91cf9a77bad6c513658401a57db87d975f9a526/token-standard/splice-token-standard-test/daml.yaml)。

  有没有广州币的开源钱包实现？

  > [此处](/integrations/钱包/guidance) 有一个钱包 SDK，正在快速开发中。不过还没有 OSS UI。
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
