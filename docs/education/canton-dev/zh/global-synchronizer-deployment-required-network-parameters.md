---
title: "必需网络参数"
slug: "global-synchronizer-deployment-required-network-parameters"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/required-network-parameters.md"
source_title: "Required Network Parameters"
tags:
  - global-synchronizer
  - deployment
  - required-network-parameters
---

# 必需网络参数

> 验证者入网初始化所需网络参数与 onboarding secret 说明。

> 初始化验证器节点并连接到网络所需的参数

{/* NETWORKVARS_START source="/snippets/networkvars/global-同步器/deployment/required-network-parameters-1.mdx" */}

<标签>
  <Tab title="DevNet (0.6.4)">
    要初始化验证器节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。

    * **MIGRATION\_ID** — 您尝试连接的网络（dev/test/mainnet）的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到它。
    * **SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用程序的 URL。其格式应为 <a href="https://sv.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.dev.global.canton.network.sync.global">[https://sv.sv-1.dev.global.canton.network.sync.global](https://sv.sv-1.dev.global.canton.network.sync.global)</a>。

    入职\_秘密
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。

    <注意>
      您可以通过在任何 SV 上调用以下端点（将 `SPONSOR_SV_URL` 替换为上面定义的 SV 应用程序 URL）来自动获取登录密码：

      ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
      curl -X POST SPONSOR_SV_URL/api/sv/v0/devnet/onboard/validator/prepare
      ```

      确保使用 **SV 应用程序 URL**（以 `sv.` 开头），而不是扫描 URL（以 `scan.` 开头）。

      请注意，此自助密钥仅在 1 小时内有效。
    </注>
  </标签>

  <Tab title="测试网 (0.6.3)">
    要初始化验证器节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。* **MIGRATION\_ID** — 您尝试连接的网络（dev/test/mainnet）的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到它。
    * **SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用程序的 URL。格式应为 <a href="https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.test.global.canton.network.sync.global">[https://sv.sv-1.test.global.canton.network.sync.global](https://sv.sv-1.test.global.canton.network.sync.global)</a>。

    入职\_秘密
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。
  </标签>

  <Tab title="主网 (0.6.2)">
    要初始化验证器节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。

    * **MIGRATION\_ID** — 您尝试连接的网络（dev/test/mainnet）的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到它。
    * **SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用程序的 URL。格式应为 <a href="https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.global.canton.network.sync.global">[https://sv.sv-1.global.canton.network.sync.global](https://sv.sv-1.global.canton.network.sync.global)</a>。

    入职\_秘密
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。
  </标签>
</标签>

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
