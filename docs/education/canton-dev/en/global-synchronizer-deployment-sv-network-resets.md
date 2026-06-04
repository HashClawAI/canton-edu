---
title: "SV Network Resets"
slug: "global-synchronizer-deployment-sv-network-resets"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/sv-network-resets.md"
source_title: "SV Network Resets"
tags:
  - global-synchronizer
  - deployment
  - sv-network-resets
---

# SV Network Resets

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# SV Network Resets

> Handling DevNet and TestNet resets on Super Validator nodes

{/* NETWORKVARS_START source="/snippets/networkvars/global-synchronizer/deployment/sv-network-resets-1.mdx" */}

<Tabs>
  <Tab title="DevNet (0.6.4)">
    DevNet and TestNet get reset roughly every 3 months with the resets spread out such that they never happen at the same time on DevNet and TestNet. The exact time is announced in the `#supervalidator-operations` channel run by the [Global Synchronizer Foundation](https://sync.global/).

    A reset requires a full redeployment of your node and loses any data you had on the node. Your node will not be functional until you complete the reset. Wait for the bootstrapping SV-1 to announce that they completed redeployment of their node before attempting to redeploy your node.

    To complete the reset, go through the following steps:

    1. Backup information to be preserved across the reset
       1. Take a backup of the DSO configuration (replace YOUR\_SCAN\_URL with your own scan e.g. <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>):

          > curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          The backup allows you to verify that the SV weights and package versions do not change as part of the reset.

       2. Make a note of your desired amulet price in the SV UI.

       3. Make a note of all ongoing votes in the SV UI. Ongoing votes will be lost as part of the reset and need to be recreated manually after the reset.

       4. Make a note of all featured apps:

          > curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps) > featured.json

          Featured app rights will be lost as part of the reset and need to be recreated manually after the reset.
    2. Decommission your old node
       1. Uninstall all helm charts.
       2. Delete all PVCs, docker volumes and databases (including databases in Amazon AWS, GCP CloudSQL or similar).
    3. Deploy your new node
       1. Set the migration id to 0 in helm chart values. The migration id appears in all helm charts, both as its own value, e.g.:

          > migration:
          > id: "MIGRATION\_ID"

          and as part of various values, e.g.:

          > sequencerPublicUrl: "https\://sequencer-MIGRATION\_ID.sv.YOUR\_HOSTNAME"

       2. Set `skipInitialization` to `false` in `sv-values.yaml`.

       3. Set `initialAmuletPrice` to your desired price in `sv-values.yaml` (see step 1.b).

       4. Set `chainIdSuffix` to the new value in `cometbft-values.yaml` and `info-values.yaml`. Usually this will just increase by 1 on a network reset but double check with the other SV operators on what has been agreed upon.

       5. Founding node only: Set all helm chart values that affect network parameters, such that the verification steps listed below pass.

       6. Install all helm charts.

       7. Wait until your SV node is sending status reports.
    4. Verify that network parameters were preserved
       1. Confirm that the reset did not change the dso rules by repeating step 1.a and comparing the result:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          The reset should preserve SV reward weights, i.e., the following diff should be empty:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          The reset should also preserve the amulet rules modulo cryptographic keys, i.e., the following diff should only show changes to the dso and synchronizer namespaces:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. Check your desired coin price in the SV UI, and verify that it matches the value from before the reset (see step 1.b.)

       3. Check the current round in the Scan UI, and verify that it matches the expected value. The round number affects the reward distribution. We usually want TestNet to be one week (approximately 1008 rounds) ahead of MainNet, whereas DevNet is usually reset to round 0.
    5. Take a backup of your node identities as they change as part of the reset.
    6. Other post-reset actions
       1. Recreate votes that were ongoing at the time of the reset, see step 1.c.
       2. Re-issue onboarding secrets to validators you are sponsoring (TestNet only, on DevNet they can self-issue secrets).
       3. Recreate votes for featured apps when requested by validators. The expectation is that validators reach out to their sponsor and the sponsor initiates the vote. If necessary, consult the list of featured apps you backed up in step 1.d.
       4. Update your auto-sweeping configuration, as party ids change as part of the reset.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    DevNet and TestNet get reset roughly every 3 months with the resets spread out such that they never happen at the same time on DevNet and TestNet. The exact time is announced in the `#supervalidator-operations` channel run by the [Global Synchronizer Foundation](https://sync.global/).

    A reset requires a full redeployment of your node and loses any data you had on the node. Your node will not be functional until you complete the reset. Wait for the bootstrapping SV-1 to announce that they completed redeployment of their node before attempting to redeploy your node.

    To complete the reset, go through the following steps:

    1. Backup information to be preserved across the reset
       1. Take a backup of the DSO configuration (replace YOUR\_SCAN\_URL with your own scan e.g. <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>):

          > curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          The backup allows you to verify that the SV weights and package versions do not change as part of the reset.

       2. Make a note of your desired amulet price in the SV UI.

       3. Make a note of all ongoing votes in the SV UI. Ongoing votes will be lost as part of the reset and need to be recreated manually after the reset.

       4. Make a note of all featured apps:

          > curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps) > featured.json

          Featured app rights will be lost as part of the reset and need to be recreated manually after the reset.
    2. Decommission your old node
       1. Uninstall all helm charts.
       2. Delete all PVCs, docker volumes and databases (including databases in Amazon AWS, GCP CloudSQL or similar).
    3. Deploy your new node
       1. Set the migration id to 0 in helm chart values. The migration id appears in all helm charts, both as its own value, e.g.:

          > migration:
          > id: "MIGRATION\_ID"

          and as part of various values, e.g.:

          > sequencerPublicUrl: "https\://sequencer-MIGRATION\_ID.sv.YOUR\_HOSTNAME"

       2. Set `skipInitialization` to `false` in `sv-values.yaml`.

       3. Set `initialAmuletPrice` to your desired price in `sv-values.yaml` (see step 1.b).

       4. Set `chainIdSuffix` to the new value in `cometbft-values.yaml` and `info-values.yaml`. Usually this will just increase by 1 on a network reset but double check with the other SV operators on what has been agreed upon.

       5. Founding node only: Set all helm chart values that affect network parameters, such that the verification steps listed below pass.

       6. Install all helm charts.

       7. Wait until your SV node is sending status reports.
    4. Verify that network parameters were preserved
       1. Confirm that the reset did not change the dso rules by repeating step 1.a and comparing the result:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          The reset should preserve SV reward weights, i.e., the following diff should be empty:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          The reset should also preserve the amulet rules modulo cryptographic keys, i.e., the following diff should only show changes to the dso and synchronizer namespaces:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. Check your desired coin price in the SV UI, and verify that it matches the value from before the reset (see step 1.b.)

       3. Check the current round in the Scan UI, and verify that it matches the expected value. The round number affects the reward distribution. We usually want TestNet to be one week (approximately 1008 rounds) ahead of MainNet, whereas DevNet is usually reset to round 0.
    5. Take a backup of your node identities as they change as part of the reset.
    6. Other post-reset actions
       1. Recreate votes that were ongoing at the time of the reset, see step 1.c.
       2. Re-issue onboarding secrets to validators you are sponsoring (TestNet only, on DevNet they can self-issue secrets).
       3. Recreate votes for featured apps when requested by validators. The expectation is that validators reach out to their sponsor and the sponsor initiates the vote. If necessary, consult the list of featured apps you backed up in step 1.d.
       4. Update your auto-sweeping configuration, as party ids change as part of the reset.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    DevNet and TestNet get reset roughly every 3 months with the resets spread out such that they never happen at the same time on DevNet and TestNet. The exact time is announced in the `#supervalidator-operations` channel run by the [Global Synchronizer Foundation](https://sync.global/).

    A reset requires a full redeployment of your node and loses any data you had on the node. Your node will not be functional until you complete the reset. Wait for the bootstrapping SV-1 to announce that they completed redeployment of their node before attempting to redeploy your node.

    To complete the reset, go through the following steps:

    1. Backup information to be preserved across the reset
       1. Take a backup of the DSO configuration (replace YOUR\_SCAN\_URL with your own scan e.g. <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>):

          > curl -sSL --fail-with-body https\://YOUR\_SCAN\_URL/api/scan/v0/dso > backup.json

          The backup allows you to verify that the SV weights and package versions do not change as part of the reset.

       2. Make a note of your desired amulet price in the SV UI.

       3. Make a note of all ongoing votes in the SV UI. Ongoing votes will be lost as part of the reset and need to be recreated manually after the reset.

       4. Make a note of all featured apps:

          > curl -sSL --fail-with-body [https://YOUR\_SCAN\_URL/api/scan/v0/featured-apps](https://YOUR_SCAN_URL/api/scan/v0/featured-apps) > featured.json

          Featured app rights will be lost as part of the reset and need to be recreated manually after the reset.
    2. Decommission your old node
       1. Uninstall all helm charts.
       2. Delete all PVCs, docker volumes and databases (including databases in Amazon AWS, GCP CloudSQL or similar).
    3. Deploy your new node
       1. Set the migration id to 0 in helm chart values. The migration id appears in all helm charts, both as its own value, e.g.:

          > migration:
          > id: "MIGRATION\_ID"

          and as part of various values, e.g.:

          > sequencerPublicUrl: "https\://sequencer-MIGRATION\_ID.sv.YOUR\_HOSTNAME"

       2. Set `skipInitialization` to `false` in `sv-values.yaml`.

       3. Set `initialAmuletPrice` to your desired price in `sv-values.yaml` (see step 1.b).

       4. Set `chainIdSuffix` to the new value in `cometbft-values.yaml` and `info-values.yaml`. Usually this will just increase by 1 on a network reset but double check with the other SV operators on what has been agreed upon.

       5. Founding node only: Set all helm chart values that affect network parameters, such that the verification steps listed below pass.

       6. Install all helm charts.

       7. Wait until your SV node is sending status reports.
    4. Verify that network parameters were preserved
       1. Confirm that the reset did not change the dso rules by repeating step 1.a and comparing the result:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          curl -sSL --fail-with-body https://YOUR_SCAN_URL/api/scan/v0/dso > current_state.json
          ```

          The reset should preserve SV reward weights, i.e., the following diff should be empty:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' backup.json > weights_backup.json
          jq '.dso_rules.contract.payload.svs.[] | [.[1].name, .[1].svRewardWeight]' current_state.json > weights_current.json
          diff -C2 weights_backup.json weights_current.json
          ```

          The reset should also preserve the amulet rules modulo cryptographic keys, i.e., the following diff should only show changes to the dso and synchronizer namespaces:

          ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
          jq '.amulet_rules.contract.payload' backup.json > amulet_backup.json
          jq '.amulet_rules.contract.payload' current_state.json > amulet_current.json
          diff amulet_backup.json amulet_current.json
          ```

       2. Check your desired coin price in the SV UI, and verify that it matches the value from before the reset (see step 1.b.)

       3. Check the current round in the Scan UI, and verify that it matches the expected value. The round number affects the reward distribution. We usually want TestNet to be one week (approximately 1008 rounds) ahead of MainNet, whereas DevNet is usually reset to round 0.
    5. Take a backup of your node identities as they change as part of the reset.
    6. Other post-reset actions
       1. Recreate votes that were ongoing at the time of the reset, see step 1.c.
       2. Re-issue onboarding secrets to validators you are sponsoring (TestNet only, on DevNet they can self-issue secrets).
       3. Recreate votes for featured apps when requested by validators. The expectation is that validators reach out to their sponsor and the sponsor initiates the vote. If necessary, consult the list of featured apps you backed up in step 1.d.
       4. Update your auto-sweeping configuration, as party ids change as part of the reset.
  </Tab>
</Tabs>

{/* COPIED_END */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
