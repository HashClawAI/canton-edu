---
title: "SV 运维概览"
slug: "global-synchronizer-deployment-sv-operations"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/sv-operations.md"
source_title: "SV Operations Overview"
tags:
  - global-synchronizer
  - deployment
  - sv-operations
---

# SV 运维概览

> Global Synchronizer 超级验证者日常运维与治理操作参考。

> 超级验证者节点运营者操作流程

这些部分概述了通过 SV 节点启用的一些功能以及对 SV 节点操作员有用的一般信息。

<警告>
  作为 SV 运营商，我们非常欢迎您查看、安装和使用第三方 Daml 应用程序（只要您提供）

  **在与 SV 节点分开的验证器节点上安装第三方 Daml 应用程序**。

  不支持在 SV 节点上安装额外的 Daml 应用程序，这可能会损害其安全

  操作。特别是，请不要手动上传额外的`.dar`文件

  到您的 SV 节点或手动将其连接到第三方同步器。
</警告>

## 安全通知

有关强化 SV 节点的更多信息，请参阅`sv-security`。

## 生成验证者入门密码

如果您想加入新的验证器，可以直接从 SV Web UI 获取一次性使用的加入密码。

入职密码将在 48 小时后过期。

要生成此密钥，您需要登录 SV Web UI 并导航到 `Validator Onboarding` 选项卡。在该选项卡中，单击按钮创建秘密并复制最后生成的`入驻密钥`。

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/create-onboarding-secret.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=4c296d6b731ffa6f1563ea2df0d2b94b" width="600" alt="在 SV UI 中生成入门密码。" data-path="images/splice/create-onboarding-secret.png" />

使用该秘密，验证器操作员可以按照此说明为验证器加入做好准备。

## 不同层SV节点使用的身份

本节简要概述与单个 SV 节点相关的一些最重要的身份，以及每种类型的身份：其角色和与仲裁的相关性（如果有）、在什么情况下可以重用，以及丢失它的影响（例如，由于相关加密密钥的丢失或泄露）。

每个身份都与 Canton & 全局同步器 软件堆栈的不同层或不同子系统相关。我们努力减少层之间的耦合，以便通常可以彼此独立地轮换身份。

### SV身份* 用于在节点登录到系统之前*识别您的节点。参见`sv-identity`。
* 已建立的 SV 将确认 SV 的入职请求，这些 SV 可以就已批准的 SV 身份进行自我验证。
* SV 身份可以重复用于多个加入，只要它得到已建立 SV 法定人数的批准，并且对于非 DevNet 集群，没有同名的 SV 已加入。
* 失去对 SV 身份控制的运营商将无法加入 SV，直到已建立的 SV 运营商的法定人数批准了该运营商控制下的新身份。

### 参与者身份

* 用于保护 Daml 工作流程并确定 SV 的`svPartyId`，用于各种 DSO 治理流程以及接收 SV 奖励。有关 Canton 和 Daml 身份的一般信息，请参阅 [Canton 身份管理文档](/sdks-tools/api-reference/ledger-api-services#user-management-service)。
* 参与者身份对于多种类型的法定人数都很重要
  * 确认 Daml 交易作为 DSO 方的法定人数（>⅓ 已加入的 SV）
  * 代表 DSO 方管理域拓扑的法定人数（激活后超过⅔的已加入 SV）
  * 基于确认的 DSO Daml 工作流程的法定人数（>⅔ 已装载的 SV；在 DevNet 上通常 >½）
* 一般来说，参与者身份*不能*在同一个全局同步器上重复使用，即在不重置/重新部署网络的情况下。
* 失去对参与者命名空间的控制意味着失去对该命名空间下托管的所有各方的代币余额的控制。在网络级别上，参与者名称空间的丢失会构成 SV 故障并减少整体容错缓冲区，直到相应的 SV 从 DSO 中脱离。

### CometBFT 节点身份

* 在 SV 跨越的 CometBFT 网络中使用，用于操作全局同步器。参见`cometbft-identity`。
* CometBFT 验证器密钥用于 CometBFT 法定人数（>⅔ SV），这是推进 CometBFT 区块链并更改 CometBFT 配置和验证器集所必需的。
* 重复使用 CometBFT 节点身份可能会导致 CometBFT 网络出现（暂时）不稳定，因此不建议这样做。
* CometBFT 密钥材料的泄露构成 SV 故障并降低整体容错缓冲区。为了恢复，SV 运营商设置一个新的 CometBFT 节点（具有新的身份）并确保其 SV 应用程序后端正确注册（例如，通过修改其 SV 应用程序后端的配置并重新启动它）就足够了。

## 更新SV的奖励权重

更新SV的奖励权重需要执行以下步骤：1. 从 SV 所有者处收到商定的 SV 权重更新。
2. 如果正在调整权重的SV定义了`extraBeneficiaries`（如`sv-helm`中所述），则必须相应地更新它们。即：
   * 在重量增加时，他们应该添加一个具有额外重量的新条目，否则任何剩余的东西都将归 SV 方所有。
   * 在体重减少时，最后一位额外受益人的体重将受到限制。
3. 请注意，您可以而且通常应该在权重更改生效之前更新额外受益人配置。最后的额外条目将被忽略。
4. 启动治理投票。为此，请在 SV Web UI 的 `Governance` 选项卡下创建新的投票请求。选择“更新SV奖励权重”名称，然后选择SV会员并指定新的奖励权重。
5. 等待投票请求获得批准并执行。一旦发生这种情况，DSO 信息选项卡将显示更新的奖励权重，SV 将根据新的权重继续获得奖励。
6. 确保更改后的奖励也反映在[配置存储库](https://github.com/global-同步器-foundation/configs)上。否则，在入职和重新入职时，旧值将再次生效。

## 确定良好的同步器流量参数

SV 负责决定合适的同步器流量参数。下面我们描述了确定其中一些参数的良好值的方法。

### 确定单次 CC 传输的成本

根据 Canton 改进提案 [cip-0042](https://github.com/global-同步器-foundation/cips)，应设置 `extraTrafficPrice`，以使标准 CC 传输的成本为 1 美元。实际流量成本会根据 DSO 的大小（SV 数量）和 Canton 协议版本等因素而变化（因此也可能因协议升级而变化）。因此，建议SV定期测量当前成本并相应调整流量参数。

确定 CC 传输的当前流量消耗（以字节为单位）的一种方法是启动 CC 传输并观察与其对应的定序器日志。假设 TestNet 具有与 MainNet 相同的配置和 DSO 大小，在 TestNet 上进行此测量就足够了。建议的具体步骤如下：

1. 选择您控制的两个非 SV 验证器 - 一个将托管发送方，另一个将托管接收方。它们必须不同，才不会扭曲测量结果。只需要控制接收者即可接受传输。

2. 启动从所选发送方验证器上托管的一方到所选接收方验证器上托管的单个接收方的 CC 传输。在接收方接受传输。3. 检查`sender`端的`validator-app`日志，确认转账的最终交易是

   1. 不与其他硬币操作一起批量处理并且

   (b) 有一个硬币输入。您可以通过查看表单的匹配日志条目来确认这两个条件：

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   executing batch AmuletOperationBatch(
     nonMergeOperations = AmuletOperation(
       from = tid:80afc8ae63defcb7a636d2cd23e38c0d,
       op = CO_CompleteAcceptedTransfer(ContractId(00ebc78671f4b5f688d8245a1e0c6c72f378c0c90c7ca574a3c3a615489f3ca15dca1012208d8f9eb3ffe0d0a05b207e2bc3fb3f3e7d31c0b594eaefcfd486411386de775c)),
       priority = Low
     ),
     priority = Low
   ) with inputs Vector(InputAmulet(ContractId(002ace5687dc7f82cb0ca80d2b349a39b1127ffd01db2cd7172053fef88308e6faca1012202646cd3cbb31c78314c3ef22657d4ba6f7f096e90167dcd0d71eba565fa35844)))
   ```

   使用此日志条目元数据中的 `trace-id`（**不是**此处查看的 `tid`，而是来自日志条目 JSON 上的专用 `trace-id` 字段）来确认此日志条目与您的传输匹配（例如，通过按 `trace-id` 搜索日志以查找包含完整 `AcceptedTransferOffer` 的条目）。请注意，在此示例中，(a) 执行的 bach 中有一个操作，并且 (b) 该操作具有单个输入。如果您启动的传输不是这样，请返回步骤 2 并启动新的传输，因为批处理或多输入传输会使测量结果产生偏差。

4. 在 `sender` 上搜索`validator-app` 日志，查找上一步中可见的 `trace-id`。我们的目标是将这里的行动与广东队的`trace-id`联系起来。搜索以下形式的日志条目：

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   Request (tid:43fd8ad332ca637b0c7c1509b2bdf715) com.daml.ledger.api.v2.CommandService/SubmitAndWaitForTransactionTree to participant-1:5001: sending request
   ```

   此日志条目中的 `tid` 是您要查找的 `trace-id`。它与日志条目元数据中的`trace-id`不同（您用来将此日志条目链接到上面可见的传输操作）。

5. 在 SV 的 `sequencer` 日志中搜索上一步中的 `trace-id`。您想要使用日志过滤器（此处的所有规则均应使用逻辑“AND”连接）：

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   resource.labels.container_name="sequencer"
   jsonPayload.logger_name="c.d.c.s.t.TrafficConsumedManager:sequencer=sequencer"
   jsonPayload."trace-id"="43fd8ad332ca637b0c7c1509b2bdf715"
   ```6. 生成的日志行包含有关发送方和接收方参与者以及所有 SV 参与者的流量消耗信息。 （SV 参与者是所有 CC 传输的利益相关者。）要仅确定发送方和接收方参与者的流量消耗，您必须筛选发送方和接收方的参与者 ID。实现正确过滤的一个简单方法是过滤发送方和接收方的部分后缀，因为一方的后缀（命名空间）通常与托管该方的参与者的后缀相同。过滤生成的日志行以查找与发送者和接收者对应的参与者 ID，您应该获得类似于以下内容的日志行：

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   Consumed 16147 for PAR::sender::...
   Consumed 711 for PAR::receiver::...
   Consumed 1450 for PAR::sender::...
   ```

7. 将日志行中的数字相加，得到 CC 传输最后一段消耗的总流量。在此示例中，发送方消耗的总流量为 17597 字节，接收方消耗的总流量为 711 字节。

8. 将 1 MB 除以发送方消耗的总流量，即可得出此 CC 传输根据 cip-0042 应产生的美元费用。在此给出的示例中，成本应配置为 `1,000,000 / 6344 = 56.83` USD / MB，即 `extraTrafficPrice = 56.83`。

### 围绕读取缩放因子的注意事项

为了确定 `readVsWriteScalingFactor` 的良好值，请考虑以下约束：

#### 下界

读取流量的费用应涵盖互联网出口和消息传递所产生的计算成本。考虑以下示例计算：

* 根据对主要云提供商的出口成本的审查，我们假设平均成本为 0.10 美元/GB。
* 假设计算成本将由 10 倍的出口成本承担，因此计算成本为 1 美元/GB，总计为 1.1 美元/GB。
* 验证器以 `BFT` 方式从定序器中读取，因此，使用 `n` SV 并且在正常情况下，`2f+1 = 2 * floor((n-1)/3) + 1` 定序器将向同一个（验证器）接收者传递相同的消息。令同步器大小为`n = 16` SVs；那么读取放大系数为 11，消息传递到单个接收者的成本为 12.1 USD/GB。
* 设当前`extraTrafficPrice`为60.0 USD/MB，即60,000 USD/GB。
* `readVsWriteScalingFactor` 应设置为至少 `12.1 / 60,000` 的系数以覆盖成本，约为 2 个基点；即`readVsWriteScalingFactor >= 2`。请注意，为了简单起见，我们假设所有接收者都是以默认 BFT 方式使用排序器的验证者参与者。此计算还假设消息必须仅传递给接收者一次 - 只要验证器和 SV 没有故障并且接收者当前未从备份中恢复（这需要重播某些消息），该假设就成立。

#### 上限

消息的传递显然比它们的排序和持久性便宜，因此 `readVsWriteScalingFactor` 应明显低于 100%。也就是说：没有充分的理由对消息传递收取过高的费用。

## 在奖励到期自动化中忽略过时验证者的派对 ID

<注意>
  本节介绍了一种解决方法，预计随着 Canton 3.4 (Splice > 0.4) 中打包的改进，该解决方法将变得不必要。
</注>

由于当前的限制，当满足以下条件时，作为 SV 应用程序一部分的奖励到期自动化（更具体地说是`ExpireRewardCouponsTrigger`）可能会出现故障（记录警告或错误，无法在到期奖励方面取得进展）：

* 最近对核心 Daml 软件包进行了升级，最引人注目的是 `amulet`。
* 一些验证器尚未升级到足够新的 Splice 版本，因此无法在本地应用 Daml 升级（并审查新的软件包版本）。

简而言之，在这种情况下，与托管在过时验证器上的各方相关联的情况下，到期自动化将无法使奖励到期。为了解决此问题，目前要求**每个** SV 运营商在网络中的 **每个 Daml 升级** 中遵循以下步骤（直到 Splice 中解决此问题背后的基本限制；预计升级到 Canton 3.4）：

1. 在Daml升级生效前不久：每个SV通过以下方式在`sv-values.yaml`中扩展`.additionalEnvVars`来暂停其`ExpireRewardCouponsTrigger`触发器：

   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   additionalEnvVars:
     - name: ADDITIONAL_CONFIG_PAUSED_EXPIRY_TRIGGER
       value: |
         canton.sv-apps.sv.automation.paused-triggers += "org.lfdecentralizedtrust.splice.sv.automation.delegatebased.ExpireRewardCouponsTrigger"
   ```

2. Daml升级生效后不久：一名SV运营商构建一方排除配置，确认其正确性并与所有运营商组共享。

3. 每个 SV 操作员均采用参与方排除配置，并通过恢复步骤 1 中的更改来恢复 `ExpireRewardCouponsTrigger` 触发器。如果 `sv-values.yaml` 中的 `.additionalEnvVars` 在步骤 1 之前为空，则现在预计类似于以下内容：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   additionalEnvVars:
     - name: ADDITIONAL_CONFIG_IGNORED_EXPIRY_PARTY_IDS
       value: |
         canton.sv-apps.sv {
           automation.ignored-expired-rewards-party-ids = [ "party1::12345", "party2:57890" ]
         }
   ```

未来某个时间点可以更新参与方排除配置，例如，如果之前过时的验证器最终升级到足够新的 Splice 版本。

### 确定要忽略的各方

确定要忽略的正确各方的过程是先进的，并且可能涉及一些试错。单个操作员足以执行此工作并获得合适的配置。

下面我们列出了建立各方名单的补充方法。

前提步骤：

1. 等待新的Daml升级生效。
2. 选择Daml升级生效后不久开放的一轮（以辅助数据库查询）；下面我们将这一轮记为`UPGRADE_ROUND`。
3. 恢复到期触发器（接受在完成忽略列表之前它将失败）。
4. 将`delegatelessAutomationExpiredRewardCouponBatchSize: 1`设置为`sv-values.yaml`。

基于此：

* 您可以等到触发器失败，然后调查哪些参与方参与了失败的交易，并将这些参与方添加到要忽略的参与方集合中。

* 为了获得更快速的反馈循环，您可以尝试对 SV 应用程序 (postgres) 数据库进行查询。例如，您可以列出自 Daml 升级以来未过期的奖励接收者：

  ```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
  select distinct(reward_party) from dso_acs_store where reward_round < UPGRADE_ROUND;
  ```

  但请注意，此查询过于近似要忽略的各方集合，因此您可能需要稍后再次删除某些各方。

* 如果您想要忽略的一方是 SV，您很可能想忽略该 SV 的受益人（或者更好 - 与 SV 的运营商交谈以确保他们的受益人升级到更新的版本）。

* 一旦您对要忽略的各方有信心，请删除 `delegatelessAutomationExpiredRewardCouponBatchSize` 覆盖并确认触发器具有 100% 的成功率并且不会记录任何警告或错误。* 如果过时的验证者最终跟进升级，他们的参与方应再次从忽略列表中删除，以允许存档过期的奖励（旧的和新的），并避免阻止封闭采矿轮次的存档。以下数据库查询显示了 Daml 升级*之后*生成的过期奖励，这表明托管验证器已升级，因此不应再忽略这些各方：

  ```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
  select m.template_id_qualified_name, m.reward_party, min(m.reward_round) from (
    select c.reward_party, c.reward_round, c.template_id_qualified_name from dso_acs_store c
    join dso_acs_store r
    on r.mining_round = c.reward_round
    and r.mining_round > UPGRADE_ROUND
    and r.template_id_qualified_name = 'Splice.Round:ClosedMiningRound'
  ) as m group by (template_id_qualified_name, reward_party);
  ```

## 确定 CIP-66 流的过期 SV 奖励

SV 需要在 [CIP-0066 - 来自 Unminted/Unclaimed Pool 的 Mint Canton Coin](https://github.com/global-同步器-foundation/cips/blob/main/cip-0066/cip-0066.md) 的背景下，确定从未领取并因此在特定时间范围内过期的 SV 奖励总量。这些过期的奖励构成了以后可以通过 CIP-66 治理流程从无人认领的奖励池中铸造的金额的基础。

`unclaimed_sv_rewards.py` 实用程序分析通过 Splice Scan API 公开的交易日志，并识别为受益人发放但随后在配置的时间间隔内过期的所有奖励优惠券。然后，它汇总相应的奖励金额，以生成与 CIP-66 计算相关的过期总金额。

除了此聚合之外，该脚本还会验证是否已领取任何已检查的优惠券。在 GSF 运营的预期多租户托管设置中，不应发生对这些优惠券的索赔。因此，非零索赔金额表明 GSF 运营的多租户 SV 节点配置错误，必须在启动任何 CIP-0066 铸造提案之前进行调查。

该脚本是 Splice 存储库的一部分：

[无人认领\_sv\_rewards.py](https://github.com/canton-network/splice/blob/main/scripts/scan-txlog/unclaimed_sv_rewards.py)

`unclaimed_sv_rewards.py` 旨在供 SV 节点运营商操作使用。它不会修改账本状态；它从扫描 API 中读取数据，并生成检查时间范围内过期 SV 奖励的确定性且可重复的摘要。

### 先决条件* 可访问且最新的 Splice Scan API 端点。
* 奖励过期的受益方将被评估。运营商必须知道相关奖励期间使用的确切受益方ID。
* 与根据 CIP-0066 验证的里程碑相对应的正确记录时间间隔。
* 在 `begin-record-time` 处于活动状态的迁移 ID。
*Python 3。

### 输入

`unclaimed_sv_rewards.py` 脚本接受以下输入：

* `scan_urls` 熔接扫描服务器的地址。多个 URL 可以提高弹性（循环故障转移）并提高吞吐量，因为每个块都会选择不同的 URL 来最大限度地提高并发性。建议提供尽可能多的扫描端点以获得最佳性能。
* `--beneficiary` 应评估过期奖励的一方。
* `--begin-record-time` 检查记录时间间隔的唯一开始。
* `--begin-record-time` 检查记录时间间隔的唯一开始。预期为 ISO 格式，例如：`2025-07-01T10:30:00Z`。
* `--end-record-time` 包括要检查的记录时间间隔的结束。预期为 ISO 格式，例如：`2025-07-01T12:30:00Z`。
* `--weight` 计算每张优惠券相关金额时应用的权重。在 CIP 中，权重显示为 0.5、1、2 等值。在脚本中，这些权重通过将 CIP 权重乘以 10,000 来表示为基点（例如，0.5 → 5,000；1 → 10,000；2 → 20,000）。
* `--already-minted-weight` 同一时间间隔内已铸造的重量。使用与`--weight`相同的音阶。

可选输入：

* `--page-size`（默认值：`100`）每个扫描 API 请求检索的事务更新数。
* `--loglevel`（默认：`INFO`）日志记录级别。
* `--log-file-path`（默认：`log/unclaimed_sv_rewards.log`）保存应用程序日志的文件路径。
* `--grace-period-for-mining-rounds-in-minutes`（默认：`60`）检索采矿回合时，为`end-record-time`添加了额外时间。挖矿轮次包含计算最终奖励金额所需的发行信息。延长间隔可确保不会错过优惠券创建后不久创建的回合。
* `--concurrency`（默认值：130）并发块工作器的最大数量。
* `chunk-size-in-hours`（默认：0.1）每个处理块的大小，以小时表示（例如0.5、1、24）。
* `--cache-file-path` 通过将内部状态保存到指定文件来启用可恢复执行。
* `--rebuild-cache` 忽略任何现有的缓存文件并从头开始处理。

### 运行脚本

`unclaimed_sv_rewards.py` 脚本作为独立的 Python 程序执行。

使用默认可选参数的示例：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python3 unclaimed_sv_rewards.py \
    https://scan.sv-1.global.canton.network.c7.digital \
    https://scan.sv-1.global.canton.network.cumberland.io \
    https://scan.sv-2.global.canton.network.cumberland.io \
    https://scan.sv-1.global.canton.network.digitalasset.com \
    https://scan.sv-2.global.canton.network.digitalasset.com \
    https://scan.sv-1.global.canton.network.fivenorth.io \
    https://scan.sv-1.global.canton.network.sync.global \
    https://scan.sv-1.global.canton.network.lcv.mpch.io \
    https://scan.sv-1.global.canton.network.mpch.io \
    https://scan.sv-1.global.canton.network.orb1lp.mpch.io \
    https://scan.sv-1.global.canton.network.proofgroup.xyz \
    https://scan.sv.global.canton.network.sv-nodeops.com \
    https://scan.sv-1.global.canton.network.tradeweb.com \
    --beneficiary 'party::1234abcd' \
    --begin-record-time '2025-07-20T10:30:00Z' \
    --end-record-time '2025-07-20T11:30:00Z' \
    --begin-migration-id 3 \
    --weight 5000 \
    --already-minted-weight 0
```

带有可选参数的示例：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python3 unclaimed_sv_rewards.py \
    https://scan.sv-1.global.canton.network.c7.digital \
    https://scan.sv-1.global.canton.network.cumberland.io \
    https://scan.sv-2.global.canton.network.cumberland.io \
    https://scan.sv-1.global.canton.network.digitalasset.com \
    https://scan.sv-2.global.canton.network.digitalasset.com \
    https://scan.sv-1.global.canton.network.fivenorth.io \
    https://scan.sv-1.global.canton.network.sync.global \
    https://scan.sv-1.global.canton.network.lcv.mpch.io \
    https://scan.sv-1.global.canton.network.mpch.io \
    https://scan.sv-1.global.canton.network.orb1lp.mpch.io \
    https://scan.sv-1.global.canton.network.proofgroup.xyz \
    https://scan.sv.global.canton.network.sv-nodeops.com \
    https://scan.sv-1.global.canton.network.tradeweb.com \
    --loglevel DEBUG \
    --log-file-path 'log/unclaimed_sv_rewards_2.log' \
    --page-size 200 \
    --grace-period-for-mining-rounds-in-minutes 70 \
    --concurrency 117 \
    --chunk-size-in-hours 0.2 \
    --beneficiary 'party::1234abcd' \
    --begin-record-time '2025-07-20T10:30:00Z' \
    --end-record-time '2025-07-20T11:30:00Z' \
    --begin-migration-id 3 \
    --weight 5000 \
    --already-minted-weight 0
```

使用缓存：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python3 unclaimed_sv_rewards.py \
    https://scan.sv-1.global.canton.network.c7.digital \
    https://scan.sv-1.global.canton.network.cumberland.io \
    https://scan.sv-2.global.canton.network.cumberland.io \
    https://scan.sv-1.global.canton.network.digitalasset.com \
    https://scan.sv-2.global.canton.network.digitalasset.com \
    https://scan.sv-1.global.canton.network.fivenorth.io \
    https://scan.sv-1.global.canton.network.sync.global \
    https://scan.sv-1.global.canton.network.lcv.mpch.io \
    https://scan.sv-1.global.canton.network.mpch.io \
    https://scan.sv-1.global.canton.network.orb1lp.mpch.io \
    https://scan.sv-1.global.canton.network.proofgroup.xyz \
    https://scan.sv.global.canton.network.sv-nodeops.com \
    https://scan.sv-1.global.canton.network.tradeweb.com \
    --cache-file-path 'cache.json' \
    --beneficiary 'party::1234abcd' \
    --begin-record-time '2025-07-20T10:30:00Z' \
    --end-record-time '2025-07-20T11:30:00Z' \
    --begin-migration-id 3 \
    --weight 5000 \
    --already-minted-weight 0
```

重建缓存：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
python3 unclaimed_sv_rewards.py \
    https://scan.sv-1.global.canton.network.c7.digital \
    https://scan.sv-1.global.canton.network.cumberland.io \
    https://scan.sv-2.global.canton.network.cumberland.io \
    https://scan.sv-1.global.canton.network.digitalasset.com \
    https://scan.sv-2.global.canton.network.digitalasset.com \
    https://scan.sv-1.global.canton.network.fivenorth.io \
    https://scan.sv-1.global.canton.network.sync.global \
    https://scan.sv-1.global.canton.network.lcv.mpch.io \
    https://scan.sv-1.global.canton.network.mpch.io \
    https://scan.sv-1.global.canton.network.orb1lp.mpch.io \
    https://scan.sv-1.global.canton.network.proofgroup.xyz \
    https://scan.sv.global.canton.network.sv-nodeops.com \
    https://scan.sv-1.global.canton.network.tradeweb.com \
    --cache-file-path 'cache.json' \
    --beneficiary 'party::1234abcd' \
    --begin-record-time '2025-07-20T10:30:00Z' \
    --end-record-time '2025-07-20T11:30:00Z' \
    --begin-migration-id 3 \
    --weight 5000 \
    --already-minted-weight 0 \
    --rebuild-cache
```

有关缓存行为的操作详细信息，请参阅缓存机制

### 输出

在执行结束时，脚本会记录在检查的记录时间间隔内识别的 SV 奖励的摘要。报告以下字段：* `reward_expired_count` 未领取而过期的SV优惠券数量。
* `reward_expired_total_amount` 已过期SV优惠券对应的总金额。
* `reward_claimed_count` 已领取的SV优惠券数量。在预期的 GSF 多租户托管设置中，该值应始终为 `0`。非零值表示存在配置问题，必须在启动任何 CIP-0066 治理提案之前进行调查。
* `reward_claimed_total_amount` 领取SV奖励券对应的总金额。该值预计也为`0`。非零金额表示存在上述相同的配置问题，必须在启动任何 CIP-0066 治理提案之前进行调查。
* `reward_unclaimed_count` 处理后仍然有效的SV奖励券数量。在预期的设置中，所有优惠券都应该已过期或（意外）已被领取。非零值会导致脚本因断言错误而中止，并指示检查的时间间隔（包括任何宽限期）未完全涵盖相关优惠券的生命周期或需要检查输入参数。

### 缓存机制

`unclaimed_sv_rewards.py` 脚本通过可选的缓存文件支持可恢复执行。启用后，脚本会保留其内部状态，以便在运行中断时可以从最后完成的批次恢复处理。

当任何影响奖励分类的输入参数发生变化时，缓存文件将被自动忽略。以下参数是确定缓存有效性的指纹的一部分：

* `--beneficiary`
* `--begin-record-time`
* `--end-record-time`
* `--begin-migration-id`
* `--weight`
* `--already-minted-weight`

如果这些值中的任何一个发生更改，脚本将开始新的运行，忽略现有的缓存。

缓存可以通过以下方式控制：

* `--cache-file-path` 启用缓存机制并指定状态应写入何处。
* `--rebuild-cache` 强制脚本从头开始重新创建缓存，忽略任何现有文件。

### 示例：跨多个里程碑的奖励计算

此示例说明了如何在基于里程碑的设置中使用 `unclaimed_sv_rewards.py` 脚本，其中 SV 接收托管奖励权重，该权重随着达到里程碑而减少。每个里程碑的目标是确定 CIP-0066 下可能考虑的过期 SV 奖励金额。

受益人的托管奖励权重变化如下：```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
t0                   t1                 t2                     t3
| m₁ (w=10K)         | m₂ (w=10K)       | m₃ (w=20K)           |
---------------------------------------------------------------------------
|         40K        |        30K       |         20K          |   0 ...
```

**步骤**

* 在 t0 时刻

  * GSF 设置 `Ghost-party-A` 权重 = 40K。

* 在 t1 时（里程碑 1 完成）

  * GSF 设置权重 = 30K。
  * GSF 为 `(t0, t1]` 运行一次脚本：

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  --begin-record-time=t0 --end-record-time=t1 \
  --weight=10000 --already-minted-weight=0
  ```

  * 对 **m₁** 发起投票。

* 在 t2（里程碑 2 完成）

  * GSF 设置权重 = 20K。

  * GSF 运行脚本两次：

    * 对于`(t0, t1]`剩余部分：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    --begin-record-time=t0 --end-record-time=t1 \
    --weight=10000 --already-minted-weight=10000
    ```

    * 对于`(t1, t2]`：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    --begin-record-time=t1 --end-record-time=t2 \
    --weight=10000 --already-minted-weight=0
    ```

  * 为 **m2** 发起投票。

* t3 时（里程碑 3 完成）

  * GSF 设置权重 = 0（移除一方）。

  * GSF 运行脚本三次：

    * 对于`(t0, t1]`剩余部分：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    --begin-record-time=t0 --end-record-time=t1 \
    --weight=20000 --already-minted-weight=20000
    ```

    * 对于`(t1, t2]`剩余部分：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    --begin-record-time=t1 --end-record-time=t2 \
    --weight=20000 --already-minted-weight=10000
    ```

    * 对于`(t2, t3]`：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    --begin-record-time=t2 --end-record-time=t3 \
    --weight=20000 --already-minted-weight=0
    ```

  * 对 **m₃** 发起投票。

### 操作注意事项

在 CIP-0066 奖励计算中使用 `unclaimed_sv_rewards.py` 脚本时，SV 操作员应牢记以下注意事项：* **过期与领取。** 在预期的托管设置中，受益人的 SV 奖励优惠券应始终过期。任何已领取的优惠券都表明 GSF 运营的 SV 节点上存在配置问题，必须在继续执行 CIP-0066 治理提案之前进行调查。
* **CIP 权重与脚本权重。** CIP 中出现的权重（例如，0.5、1、2）在传递给脚本时必须乘以 10,000（例如，0.5 → 5,000；1 → 10,000；2 → 20,000）。
* **使用\`\`already-minted-weight\`\`。**此参数指示在同一时间间隔的早期里程碑计算中已使用了多少配置的权重。该脚本会根据每个奖励优惠券的权重验证该值，并在提供的值太高时自动调整计算。因此，错误的输入不会导致重复计算或错误的奖励金额，但会导致脚本发出警告。
* **挖矿轮次的宽限期。** 挖矿轮次包含计算与每个过期奖励相关的金额所需的发行信息。默认宽限期（60 分钟）通常就足够了。如果脚本报告缺少回合信息，请增加宽限期，以便包含优惠券创建后不久创建的回合。
* **处理有效优惠券。** 非零 `reward_unclaimed_count` 表示某些 SV 奖励优惠券仍然有效。这意味着它们的生命周期（过期或索赔）不在检查间隔内。该脚本将中止以避免产生不完整的结果。
* **账本状态永远不会被修改。** 该脚本是只读的，并且仅依赖于扫描 API 返回的数据。对于给定的一组输入，所有输出都是确定性的。
* **应用权重变化。** 在基于里程碑的流程中，GSF 应该仅在 SV 开始以新权重铸造后减少受益人的配置权重，以避免奖励归属中的竞争条件。
* **并发和扫描服务器使用情况。** 对于较大的时间范围，性能在很大程度上取决于工作负载在扫描服务器之间的分布方式。为了最大化吞吐量：
  * 提供尽可能多的扫描 URL。每个块都针对不同的扫描服务器启动，这提高了并行性并减少了每台服务器的负载。
  * 使用相对较小的块大小（例如，`0.1`–`0.2` 小时）来改善负载平衡和重试行为。
  * 避免页面尺寸过大；中等值（大约 100）往往会产生更好的延迟和更可预测的性能。
  * 将`--concurrency`设置为扫描服务器数量的倍数。实际上，所提供的扫描 URL 数量的 5-10 倍左右的值已显示出良好的结果。

## 触发扫描存储的重新摄取扫描应用程序使用存储描述符跟踪其数据库存储（ACS 存储和 TxLog 存储）的版本。将扫描应用程序二进制文件中的存储描述符与数据库中存储的存储描述符进行比较。如果描述符不同，扫描应用程序将更新数据库中的描述符并将所有数据重新摄取到新存储中。这允许在后续 Splice 版本中修复任何意外的解析或存储错误。

SV 操作员可以触发存储的重新摄取，而无需新的拼接释放。这是通过 Helm Chart 值在 Store Descriptor 上设置 `user version` 来完成的。一旦设置了`user version`，它将被比较并作为存储描述符的一部分存储在数据库中。

用户版本是可选的`Long`参数，默认情况下不设置。设置它会触发重新摄取。用户版本可以通过 Helm Chart 值提供。需要注意的是，用户版本应以 `1` 开头，并且在需要重新摄取时仅递增 1。设置用户版本后，需要在每个后续 Helm Chart 部署中保持该值，以防止不必要的重新摄取。

`ScanAppBackendConfig` 有一个字段用于 ACS 存储和 TxLog 存储用户版本，`acsStoreDescriptorUserVersion` 用于 ACS 存储，`txLogStoreDescriptorUserVersion` 用于 TxLog 存储。

helm 图表值 `acsStoreDescriptorUserVersion` 设置 ACS 存储的 `user version`，如下例所示：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Example to trigger re-ingestion of the ACS store for the first time
persistence:
  acsStoreDescriptorUserVersion: 1
```

可以通过增加该值来触发后续的重新摄取，如下例所示：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Example to trigger re-ingestion of the ACS store for the second time
persistence:
  acsStoreDescriptorUserVersion: 2
```

helm 图表值 `txLogStoreDescriptorUserVersion` 设置 TxLog 存储的 `user version`，如下例所示：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Example to trigger re-ingestion of the TxLog store for the first time
persistence:
  txLogStoreDescriptorUserVersion: 1
```

可以通过增加该值来触发后续的重新摄取，如下例所示：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Example to trigger re-ingestion of the TxLog store for the second time
persistence:
  txLogStoreDescriptorUserVersion: 2
````activityIngestionUserVersion` 字段控制活动记录摄取版本。增加此值会导致扫描应用程序记录新的应用程序活动记录完整性下限。奖励核算不包括此边界之前的回合，即使他们的活动记录被保留。因此，提升用户版本与从提升时开始重新初始化应用程序活动记录计算具有相同的效果。

增加用户版本的后果：

* 奖励核算不包括新边界之前的轮次，这可能会导致 SV 节点通过向其他 SV 节点询问其没有完整活动记录的轮次数据来参与奖励计算。
* 扫描不会提供在提升用户版本之前摄取的活动记录。因此，与其他扫描 API 的响应相比，该 SV 节点的 `v0/events` 扫描 API 的结果可能会丢失一些活动记录。

这对于从意外摄取或奖励处理错误中恢复而无需重新处理历史数据非常有用。

用户版本绝不能降低。低于之前存储的值将导致扫描应用程序关闭以防止数据损坏。

HOCON 配置键是`canton.scan-apps.scan-app.activity-ingestion-user-version`。它可以通过 `ADDITIONAL_CONFIG` 环境变量设置：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Example to reset the activity ingestion completeness boundary
additionalEnvVars:
  - name: ADDITIONAL_CONFIG_ACTIVITY_INGESTION_USER_VERSION
    value: canton.scan-apps.scan-app.activity-ingestion-user-version = 1
```

`activityIngestionUserVersion` 字段控制活动记录摄取版本。增加此值会导致扫描应用程序记录新的应用程序活动记录完整性下限。奖励核算不包括此边界之前的回合，即使他们的活动记录被保留。因此，提升用户版本与从提升时开始重新初始化应用程序活动记录计算具有相同的效果。

增加用户版本的后果：

* 奖励核算不包括新边界之前的轮次，这可能会导致 SV 节点通过向其他 SV 节点询问其没有完整活动记录的轮次数据来参与奖励计算。
* 扫描不会提供在提升用户版本之前摄取的活动记录。因此，与其他扫描 API 的响应相比，该 SV 节点的 `v0/events` 扫描 API 的结果可能会丢失一些活动记录。

这对于从意外摄取或奖励处理错误中恢复而无需重新处理历史数据非常有用。用户版本绝不能降低。低于之前存储的值将导致扫描应用程序关闭以防止数据损坏。

HOCON 配置键是`canton.scan-apps.scan-app.activity-ingestion-user-version`。它可以通过 `ADDITIONAL_CONFIG` 环境变量设置：

> ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
> # Example to reset the activity ingestion completeness boundary
> additionalEnvVars:
>   - name: ADDITIONAL_CONFIG_ACTIVITY_INGESTION_USER_VERSION
>     value: canton.scan-apps.scan-app.activity-ingestion-user-version = 1
> ```

## 取消不安全的软件包版本

<警告>
  仅在**与至少 2/3 的 SV** 达成一致后才设置这些配置。对 DSO 方的审查要求所有 SV 都经过审查，因此单个 SV 取消对程序包的审查将使其无法使用，因此除非达成协议，否则不得这样做。此配置中未包含的所有受支持的软件包都经过审查。
</警告>

该机制主要用于在出现重大问题时检查有缺陷或不安全的版本。

要取消受支持的软件包的审查，SV（但不是常规验证器）必须在其 SV 和验证器配置中设置以下环境变量。

以下是如何取消包的特定版本的示例：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
  - name: ADDITIONAL_CONFIG_ADDITIONAL_PACKAGES_TO_UNVET
    value: |
      canton.sv-apps.sv.additional-packages-to-unvet.splice-wallet = ["0.1.16"]
      canton.sv-apps.sv.additional-packages-to-unvet.splice-amulet = ["0.1.16", "0.1.17"]
```

<注意>
  仅 SV 和 SV 验证器支持取消审查，目前不支持依赖项取消审查。
</注>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
