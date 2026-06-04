---
title: "超级验证者修剪"
slug: "global-synchronizer-production-operations-sv-pruning"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/sv-pruning.md"
source_title: "SV Pruning"
tags:
  - global-synchronizer
  - production-operations
  - sv-pruning
---

# 超级验证者修剪

> 超级验证者节点 Sequencer 与 CometBFT 修剪。

> 超级验证者节点上的 Sequencer 与 CometBFT 修剪

Sequencer、参与方与 CometBFT 均提供修剪选项，可将存储占用控制在合理范围内。

## Sequencer 修剪

可在 Helm 中通过以下配置启用：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
synchronizers:
  current:
    sequencerPruningConfig:
      # Enable or disable sequencer pruning
      enabled: true
      # The pruning interval is the time between two consecutive prunings.
      pruningInterval: "1 hour"
      # The retention period is the time for which the sequencer will retain the data.
      retentionPeriod: "30 days"
```

<Note>
  建议启用 Sequencer 修剪，将 `pruningInterval` 设为 `1 hour`，将 `retentionPeriod` 设为 `30 days`。
</Note>

## CometBFT 修剪

默认已启用。修剪按保留的区块数量定义，更早的区块会被修剪。

可在 `node` Helm 值键下配置保留区块数：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Number of blocks to keep, used for pruning. 0 -> keep all blocks.
  # Number of blocks to keep for 30 days with an upper bound of 7k blocks/h.
  retainBlocks: 5040000
```

## 参与方修剪

也支持并建议启用参与方修剪。在验证者 chart 上设置以下 Helm 值即可启用：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: 0 /10 * * * ? # Run every 10min
  maxDuration: 5m # Run for a max of 5min per iteration
  retention: 30d # Retain history that is newer than 30d.
```

还需让参与方在即便过去 30 天未收到某个对等参与方的 ACS commitment 时仍继续修剪。否则在主网上修剪几乎不会运行（验证者会较频繁停机）。在参与方的 `additionalEnvVars` 中设置：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_PRUNING_ACS_COMMITMENTS
      value: |
        canton.participants.participant.parameters.stores.safe-to-prune-commitment-state = "all"
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
