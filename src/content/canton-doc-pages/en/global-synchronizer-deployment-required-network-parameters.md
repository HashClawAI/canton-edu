---
title: "Required Network Parameters"
slug: "global-synchronizer-deployment-required-network-parameters"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/required-network-parameters.md"
source_title: "Required Network Parameters"
tags:
  - global-synchronizer
  - deployment
  - required-network-parameters
---

# Required Network Parameters

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Required Network Parameters

> Parameters required to initialise a validator node and connect to the network

{/* NETWORKVARS_START source="/snippets/networkvars/global-synchronizer/deployment/required-network-parameters-1.mdx" */}

<Tabs>
  <Tab title="DevNet (0.6.4)">
    To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.

    * **MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).
    * **SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.dev.global.canton.network.sync.global">[https://sv.sv-1.dev.global.canton.network.sync.global](https://sv.sv-1.dev.global.canton.network.sync.global)</a>.

    ONBOARDING\_SECRET
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.

    <Note>
      You can obtain an onboarding secret automatically by calling the following endpoint on any SV (replace `SPONSOR_SV_URL` with the SV app URL defined above):

      ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
      curl -X POST SPONSOR_SV_URL/api/sv/v0/devnet/onboard/validator/prepare
      ```

      Make sure to use the **SV app URL** (starting with `sv.`), not the Scan URL (starting with `scan.`).

      Note that this self-served secret is only valid for 1 hour.
    </Note>
  </Tab>

  <Tab title="TestNet (0.6.3)">
    To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.

    * **MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).
    * **SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.test.global.canton.network.sync.global">[https://sv.sv-1.test.global.canton.network.sync.global](https://sv.sv-1.test.global.canton.network.sync.global)</a>.

    ONBOARDING\_SECRET
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.

    * **MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).
    * **SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.global.canton.network.sync.global">[https://sv.sv-1.global.canton.network.sync.global](https://sv.sv-1.global.canton.network.sync.global)</a>.

    ONBOARDING\_SECRET
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.
  </Tab>
</Tabs>

{/* COPIED_END */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
