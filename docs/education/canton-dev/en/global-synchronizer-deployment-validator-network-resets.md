---
title: "Validator Network Resets"
slug: "global-synchronizer-deployment-validator-network-resets"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-network-resets.md"
source_title: "Validator Network Resets"
tags:
  - global-synchronizer
  - deployment
  - validator-network-resets
---

# Validator Network Resets

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Validator Network Resets

> Handling DevNet and TestNet resets on validator nodes

DevNet and TestNet get reset roughly every 3 months with the resets spread out such that they never happen at the same time on DevNet and TestNet. The exact time is announced in the `#validator-operations` channel run by the [Global Synchronizer Foundation](https://sync.global/).

A reset requires a full redeployment of your node and loses any data you had on the node. Your node will not be functional until you complete the reset.

To complete the reset, go through the following steps:

1. Uninstall all helm charts.
2. Delete all PVCs, docker volumes and databases (including databases in Amazon AWS, GCP CloudSQL or similar).
3. Acquire a fresh onboarding secret (on DevNet you can do that yourself by calling the respective endpoint, on TestNet contact your SV sponsor).
4. Redeploy your node with migration id 0. Note that this requires changes to both the migration id in the validator helm chart values as well as the participant helm chart values.
5. Take a backup of your node identities as they change as part of the reset.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
