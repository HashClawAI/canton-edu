---
title: "SV Pruning"
slug: "global-synchronizer-production-operations-sv-pruning"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/sv-pruning.md"
source_title: "SV Pruning"
tags:
  - global-synchronizer
  - production-operations
  - sv-pruning
---

# SV Pruning

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SV Pruning

> Sequencer and CometBFT pruning on Super Validator nodes

The sequencer, participant and CometBFT have pruning options that can be used to ensure storage use is kept within reasonable bounds.

## Sequencer pruning

Can be enabled in helm through the following config:

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
  It is recommended that sequencer pruning is enabled and the `pruningInterval` is set to `1 hour` and the `retentionPeriod` to `30 days`.
</Note>

## CometBFT pruning

It is enabled by default. Pruning is defined as the number of blocks to keep. Older blocks are pruned.

The number of blocks to keep can be configured under the `node` helm values key.

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Number of blocks to keep, used for pruning. 0 -> keep all blocks.
  # Number of blocks to keep for 30 days with an upper bound of 7k blocks/h.
  retainBlocks: 5040000
```

## Participant pruning

Participant pruning is also supported and recommend. To enable it, set the following helm value on your validator chart:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: 0 /10 * * * ? # Run every 10min
  maxDuration: 5m # Run for a max of 5min per iteration
  retention: 30d # Retain history that is newer than 30d.
```

You also need to tell the participant to continue pruning even if it has not received an ACS commitment from one of its counter participant in the last 30 days. Without this pruning will essentially never run on mainnet as validators get shut down relatively frequently: To do so, set the following through the `additionalEnvVars` on your participant:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_PRUNING_ACS_COMMITMENTS
      value: |
        canton.participants.participant.parameters.stores.safe-to-prune-commitment-state = "all"
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
