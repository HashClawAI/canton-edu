---
title: "SV 网络重置"
slug: "global-synchronizer-deployment-sv-network-resets"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/sv-network-resets.md"
source_title: "SV Network Resets"
tags:
  - global-synchronizer
  - deployment
  - sv-network-resets
---

# SV 网络重置

> 超级验证者应对 DevNet/TestNet 网络重置的操作指南。

> 处理超级验证器节点上的 DevNet 和 TestNet 重置

{/* NETWORKVARS_START source="/snippets/networkvars/global-同步器/deployment/sv-network-resets-1.mdx" */}

<标签>
  <Tab title="DevNet (0.6.4)">
    DevNet 和 TestNet 大约每 3 个月重置一次，并且重置是分散的，这样它们就不会在 DevNet 和 TestNet 上同时发生。具体时间在[全球同步器基金会](https://sync.global/)运行的`#supervalidator-operations`频道中公布。

    重置需要完全重新部署节点，并会丢失节点上的所有数据。在完成重置之前，您的节点将无法运行。等待引导 SV-1 宣布他们已完成节点的重新部署，然后再尝试重新部署您的节点。

    要完成重置，请执行以下步骤：

    1. 重置过程中要保留的备份信息
       1. 备份 DSO 配置（将 YOUR\_SCAN\_URL 替换为您自己的扫描，例如 <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>）：

          >curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          通过备份，您可以验证 SV 权重和软件包版本在重置过程中不会发生更改。

       2. 在 SV UI 中记下您想要的护身符价格。

       3. 记下 SV UI 中所有正在进行的投票。正在进行的投票将在重置过程中丢失，并且需要在重置后手动重新创建。

       4. 记下所有特色应用程序：

          >curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps)>featured.json

          特色应用程序权限将在重置过程中丢失，并且需要在重置后手动重新创建。
    2. 停用旧节点
       1. 卸载所有 Helm Chart。
       2. 删除所有 PVC、docker 卷和数据库（包括 Amazon AWS、GCP CloudSQL 或类似数据库）。
    3. 部署新节点
       1. 在 Helm Chart 值中将迁移 ID 设置为 0。迁移 id 出现在所有 helm 图表中，都作为其自己的值，例如：

          > 迁移：
          > id: "迁移\_ID"

          并作为各种值的一部分，例如：

          >sequencerPublicUrl：“https://sequencer-MIGRATION_ID.sv.YOUR_HOSTNAME”

       2. 将`sv-values.yaml`中的`skipInitialization`设置为`false`。

       3. 在 `sv-values.yaml` 中将 `initialAmuletPrice` 设置为您想要的价格（参见步骤 1.b）。4. 将`chainIdSuffix` 设置为`cometbft-values.yaml` 和`info-values.yaml` 中的新值。通常，该值只会在网络重置时增加 1，但请与其他 SV 运营商仔细检查已达成一致的内容。

       5. 仅创始节点：设置影响网络参数的所有 helm 图表值，以便通过下面列出的验证步骤。

       6. 安装所有舵图。

       7. 等待 SV 节点发送状态报告。
    4. 验证网络参数是否已保留
       1. 重复步骤 1.a 并比较结果，确认重置没有改变 dso 规则：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          重置应保留 SV 奖励权重，即以下 diff 应为空：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          重置还应保留护身符规则模加密密钥，即以下差异应仅显示对 dso 和同步器命名空间的更改：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. 在 SV UI 中检查您想要的代币价格，并验证其是否与重置之前的值相符（请参阅步骤 1.b.）3. 在扫描 UI 中检查当前轮次，并验证其是否与预期值相符。轮数影响奖励分配。我们通常希望 TestNet 比 MainNet 早一周（大约 1008 轮），而 DevNet 通常重置为第 0 轮。
    5. 当节点身份在重置过程中发生更改时，对其进行备份。
    6. 重置后的其他操作
       1. 重新创建重置时正在进行的投票，请参阅步骤 1.c。
       2. 向您赞助的验证者重新发布入职密钥（仅限 TestNet，在 DevNet 上他们可以自行发布密钥）。
       3. 根据验证者的要求，重新为特色应用程序创建投票。我们期望验证者联系他们的发起人，然后发起人发起投票。如有必要，请查阅您在步骤 1.d 中备份的特色应用程序列表。
       4. 更新您的自动清理配置，因为重置过程中派对 ID 会发生变化。
  </标签>

  <Tab title="测试网 (0.6.3)">
    DevNet 和 TestNet 大约每 3 个月重置一次，并且重置是分散的，这样它们就不会在 DevNet 和 TestNet 上同时发生。具体时间在[全球同步器基金会](https://sync.global/)运行的`#supervalidator-operations`频道中公布。

    重置需要完全重新部署节点，并会丢失节点上的所有数据。在完成重置之前，您的节点将无法运行。等待引导 SV-1 宣布他们已完成节点的重新部署，然后再尝试重新部署您的节点。

    要完成重置，请执行以下步骤：

    1. 重置过程中要保留的备份信息
       1. 备份 DSO 配置（将 YOUR\_SCAN\_URL 替换为您自己的扫描，例如 <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>）：

          >curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          通过备份，您可以验证 SV 权重和软件包版本在重置过程中不会发生更改。

       2. 在 SV UI 中记下您想要的护身符价格。

       3. 记下 SV UI 中所有正在进行的投票。正在进行的投票将在重置过程中丢失，并且需要在重置后手动重新创建。

       4. 记下所有特色应用程序：

          >curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps)>featured.json特色应用程序权限将在重置过程中丢失，并且需要在重置后手动重新创建。
    2. 停用旧节点
       1. 卸载所有 Helm Chart。
       2. 删除所有 PVC、docker 卷和数据库（包括 Amazon AWS、GCP CloudSQL 或类似数据库）。
    3. 部署新节点
       1. 在 Helm Chart 值中将迁移 ID 设置为 0。迁移 id 出现在所有 helm 图表中，都作为其自己的值，例如：

          > 迁移：
          > id: "迁移\_ID"

          并作为各种值的一部分，例如：

          >sequencerPublicUrl：“https://sequencer-MIGRATION_ID.sv.YOUR_HOSTNAME”

       2. 将`sv-values.yaml`中的`skipInitialization`设置为`false`。

       3. 在 `sv-values.yaml` 中将 `initialAmuletPrice` 设置为您想要的价格（参见步骤 1.b）。

       4. 将 `chainIdSuffix` 设置为 `cometbft-values.yaml` 和 `info-values.yaml` 中的新值。通常，该值只会在网络重置时增加 1，但请与其他 SV 运营商仔细检查已达成一致的内容。

       5. 仅创始节点：设置影响网络参数的所有 helm 图表值，以便通过下面列出的验证步骤。

       6. 安装所有舵图。

       7. 等待 SV 节点发送状态报告。
    4. 验证网络参数是否已保留
       1. 重复步骤 1.a 并比较结果，确认重置没有改变 dso 规则：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          重置应保留 SV 奖励权重，即以下 diff 应为空：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          重置还应保留护身符规则模加密密钥，即以下差异应仅显示对 dso 和同步器命名空间的更改：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. 在 SV UI 中检查您想要的代币价格，并验证其是否与重置之前的值相符（请参阅步骤 1.b.）3. 在扫描 UI 中检查当前轮次，并验证其是否与预期值相符。轮数影响奖励分配。我们通常希望 TestNet 比 MainNet 早一周（大约 1008 轮），而 DevNet 通常重置为第 0 轮。
    5. 当节点身份在重置过程中发生更改时，对其进行备份。
    6. 重置后的其他操作
       1. 重新创建重置时正在进行的投票，请参阅步骤 1.c。
       2. 向您赞助的验证者重新发布入职密钥（仅限 TestNet，在 DevNet 上他们可以自行发布密钥）。
       3. 根据验证者的要求，重新为特色应用程序创建投票。我们期望验证者联系他们的发起人，然后发起人发起投票。如有必要，请查阅您在步骤 1.d 中备份的特色应用程序列表。
       4. 更新您的自动清理配置，因为重置过程中派对 ID 会发生变化。
  </标签>

  <Tab title="主网 (0.6.2)">
    DevNet 和 TestNet 大约每 3 个月重置一次，并且重置是分散的，这样它们就不会在 DevNet 和 TestNet 上同时发生。具体时间在[全球同步器基金会](https://sync.global/)运行的`#supervalidator-operations`频道中公布。

    重置需要完全重新部署节点，并会丢失节点上的所有数据。在完成重置之前，您的节点将无法运行。等待引导 SV-1 宣布他们已完成节点的重新部署，然后再尝试重新部署您的节点。

    要完成重置，请执行以下步骤：

    1. 重置过程中要保留的备份信息
       1. 备份 DSO 配置（将 YOUR\_SCAN\_URL 替换为您自己的扫描，例如 <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>）：

          >curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          通过备份，您可以验证 SV 权重和软件包版本在重置过程中不会发生更改。

       2. 在 SV UI 中记下您想要的护身符价格。

       3. 记下 SV UI 中所有正在进行的投票。正在进行的投票将在重置过程中丢失，并且需要在重置后手动重新创建。

       4. 记下所有特色应用程序：

          >curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps)>featured.json特色应用程序权限将在重置过程中丢失，并且需要在重置后手动重新创建。
    2. 停用旧节点
       1. 卸载所有 Helm Chart。
       2. 删除所有 PVC、docker 卷和数据库（包括 Amazon AWS、GCP CloudSQL 或类似数据库）。
    3. 部署新节点
       1. 在 Helm Chart 值中将迁移 ID 设置为 0。迁移 id 出现在所有 helm 图表中，都作为其自己的值，例如：

          > 迁移：
          > id: "迁移\_ID"

          并作为各种值的一部分，例如：

          >sequencerPublicUrl：“https://sequencer-MIGRATION_ID.sv.YOUR_HOSTNAME”

       2. 将`sv-values.yaml`中的`skipInitialization`设置为`false`。

       3. 在 `sv-values.yaml` 中将 `initialAmuletPrice` 设置为您想要的价格（参见步骤 1.b）。

       4. 将 `chainIdSuffix` 设置为 `cometbft-values.yaml` 和 `info-values.yaml` 中的新值。通常，该值只会在网络重置时增加 1，但请与其他 SV 运营商仔细检查已达成一致的内容。

       5. 仅创始节点：设置影响网络参数的所有 helm 图表值，以便通过下面列出的验证步骤。

       6. 安装所有舵图。

       7. 等待 SV 节点发送状态报告。
    4. 验证网络参数是否已保留
       1. 重复步骤 1.a 并比较结果，确认重置没有改变 dso 规则：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          重置应保留 SV 奖励权重，即以下 diff 应为空：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          重置还应保留护身符规则模加密密钥，即以下差异应仅显示对 dso 和同步器命名空间的更改：

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. 在 SV UI 中检查您想要的代币价格，并验证其是否与重置之前的值相符（请参阅步骤 1.b.）3. 在扫描 UI 中检查当前轮次，并验证其是否与预期值相符。轮数影响奖励分配。我们通常希望 TestNet 比 MainNet 早一周（大约 1008 轮），而 DevNet 通常重置为第 0 轮。
    5. 当节点身份在重置过程中发生更改时，对其进行备份。
    6. 重置后的其他操作
       1. 重新创建重置时正在进行的投票，请参阅步骤 1.c。
       2. 向您赞助的验证者重新发布入职密钥（仅限 TestNet，在 DevNet 上他们可以自行发布密钥）。
       3. 根据验证者的要求，重新为特色应用程序创建投票。我们期望验证者联系他们的发起人，然后发起人发起投票。如有必要，请查阅您在步骤 1.d 中备份的特色应用程序列表。
       4. 更新您的自动清理配置，因为重置过程中派对 ID 会发生变化。
  </标签>
</标签>

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
