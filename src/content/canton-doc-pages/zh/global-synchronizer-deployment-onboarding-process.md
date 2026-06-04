---
title: "验证者入驻流程"
slug: "global-synchronizer-deployment-onboarding-process"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/onboarding-process.md"
source_title: "Validator Onboarding Process"
tags:
  - global-synchronizer
  - deployment
  - onboarding-process
---

# 验证者入驻流程

> Canton Network 验证者入驻流程与网络准入说明。

> 如何通过超级验证者赞助商在 DevNet、TestNet 和 MainNet 上加入您的验证者

## 网络

共有三种不同的网络：DevNet、TestNet 和 MainNet。如果您只对设置验证器节点感兴趣，可以在 DevNet 上设置一个节点进行练习，然后跳转到 MainNet。如果您想构建、测试或部署应用程序，我们建议您在 DevNet、TestNet 和 MainNet 上运行节点。

* **DevNet** — DevNet 对任何节点开放，但仍要求将验证者的出口 IP 添加到 SV 节点运营商维护的白名单中。每 3 个月重置一次。 DevNet 总是在 TestNet 和 MainNet 之前升级到新版本，因此这是在应用程序到达 MainNet 之前测试节点升级及其对应用程序影响的好方法。
* **测试网** — 加入测试网需要您获得 全局同步器 基金会代币经济委员会批准加入主网。您可以通过 [https://sync.global/validator-request/](https://sync.global/validator-request/) 发起请求来执行此操作。就像 DevNet 一样，仍然需要将验证者的出口 IP 添加到白名单中，并且需要 SV 赞助商提供的入职密钥。就像 DevNet 一样，TestNet 每 3-6 个月重置一次，但重置时间表会发生变化，因此 TestNet 永远不会与 DevNet 同时重置。 TestNet 在 DevNet 之后、MainNet 之前升级到新版本，因此它提供了额外的测试层。鼓励应用程序提供商在 TestNet 上维护其应用程序的长期运行实例，这允许使用 TestNet 测试组合应用程序。
* **MainNet** - MainNet 需要 TestNet 所需的一切，因此需要 Tokenomics 委员会的批准、允许名单上的 IP 以及来自 SV 赞助商的入门秘密。主网永远不会重置，因此是唯一始终保留数据的网络。继 DevNet 和 TestNet 之后，MainNet 升级到新版本。

## 入职流程概述

加入验证者涉及以下步骤（针对您要加入的每个网络）。

1. 向您的赞助 SV 提供您的验证器节点的出口 IP。每个网络只能提供一个 IP，并且该 IP 必须与您用于三个网络中任何其他网络的 IP 不同。

   <注意>
     此时，还可以通过 SV 运行的 VPN 连接验证器来完成此操作，这在尝试从本地笔记本电脑运行验证器时非常有用。该选项将来可能会被删除。
   </注>

2. 等待超级验证者采用新的 IP 白名单。这通常需要 2-7 天。3. 如果您想从笔记本电脑访问 Canton Coin Scan Web UI，您还需要确保可以连接到由其中一个 SV 运营的 VPN。这是必需的，因为笔记本电脑通常没有静态 IP 地址，并且扫描 Web UI 尚未完全公开。如果您也可以使用验证器出口 IP 来浏览 Web UI，则没有必要。

4. 向您的 SV 发起人请求入职密码。在 DevNet 上，您可以通过 API 调用自行执行此操作（有关详细信息，请参阅部署说明）。在测试网和主网上，您的 SV 赞助商需要手动为您提供此信息。请注意，onboarding Secrets 的有效期仅为 48 小时，并且是一次性使用，而自行生成的 DevNet Secrets 的有效期仅为 1 小时。如果过期了，您需要申请新的。

5. 使用 docker compose 或 Kubernetes 部署节点。有关如何在这两种方法之间进行选择的信息以及对这两种方法的参考，请参阅部署选项。您需要确保从验证器到 SV 的所有 IP 流量都使用您提供给 SV 发起人的出口 IP，并且您需要提供登录密码。

## 验证您的 IP 已被批准

<标签>
  <Tab title="DevNet (0.6.4)">
    要验证 SV 是否已将您添加到其各自的 IP 允许列表中，您可以查询其扫描 URL。请注意，这必须从您要部署验证器的同一出口 IP 运行，例如，从您要运行 docker compose 设置的虚拟机或从 Kubernetes 集群内运行。

    首先，请通过运行以下命令确认您运行命令的终端中的出口 IP 确实是您为白名单提供的 IP：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -sSL http://checkip.amazonaws.com
    ```

    并确认 IP 与您为白名单提供的 IP 匹配。如果是，请运行以下命令来检查您可以连接到哪个 Scan 实例。

    请注意，以下代码片段需要安装 [jq](https://jqlang.org/)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    CURL='curl -fsS -m 5 --connect-timeout 5'
    for url in $($CURL https://scan.sv-1.dev.global.canton.network.sync.global/api/scan/v0/scans | jq -r '.scans[].scans[].publicUrl'); do
      echo -n "$url: "
      $CURL "$url"/api/scan/version | jq -r '.version'
    done)
    ```

    您应该看到如下所示的输出，其中每一行表示一个 SV 及其所在的版本。如果您看到超时，表明 SV 尚未将您添加到他们的白名单中，如果您没有收到任何错误，则所有 SV 都已添加您。请注意，URL 和版本会随着时间的推移而变化，因此请勿尝试进行精确比较。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    https://scan.sv-2.test.global.canton.network.digitalasset.com: 0.3.6
    https://scan.sv.test.global.canton.network.tradeweb.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.orb1lp.mpch.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.sync.global: 0.3.6
    https://scan.sv.test.global.canton.network.sv-nodeops.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.mpch.io: 0.3.6
    https://scan.sv-2.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.c7.digital: 0.3.6
    https://scan.sv-1.test.global.canton.network.digitalasset.com: 0.3.6
    ```

    除了连接到 Scan 之外，您的验证器还必须能够连接到 SV 的定序器端点。如果您遇到与连接到同步器相关的问题，您可以使用以下代码片段来确认您是否能够到达这些端点（即，SV 也已将您的 IP 列入这些端点的白名单）。请注意，以下代码片段需要安装 [jq](https://jqlang.org/) 和 [grpcurl](https://github.com/fullstorydev/grpcurl)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    for url in $(curl -fsS -m 5 --connect-timeout 5 https://scan.sv-1.dev.global.canton.network.sync.global/api/scan/v0/dso-sequencers | jq -r '.domainSequencers[].sequencers[].url | sub("https://"; "")'); do
      echo -n "$url: "
      grpcurl --max-time 10 "$url":443 grpc.health.v1.Health/Check
    done)
    ```

    正常运行且已正确将您的 IP 列入白名单的排序器将在 `grpcurl` 输出中返回 `"status": "SERVING"`。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    sequencer-1.sv-2.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.tradeweb.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.orb1lp.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.sync.global: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.sv-nodeops.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-2.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.c7.digital: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    ```

    这两者的默认配置都需要访问每个扫描和定序器至少 2/3 的 SV。您可以根据自己的选择并自行承担风险，按照验证器舵图配置中所述配置与单个可信扫描和排序器的连接，但代价是失去 BFT 完整性保证。
  </标签>

  <Tab title="测试网 (0.6.3)">
    要验证 SV 是否已将您添加到其各自的 IP 允许列表中，您可以查询其扫描 URL。请注意，这必须从您要部署验证器的同一出口 IP 运行，例如，从您要运行 docker compose 设置的虚拟机或从 Kubernetes 集群内运行。

    首先，请通过运行以下命令确认您运行命令的终端中的出口 IP 确实是您为白名单提供的 IP：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -sSL http://checkip.amazonaws.com
    ```

    并确认 IP 与您为白名单提供的 IP 匹配。如果是，请运行以下命令来检查您可以连接到哪个 Scan 实例。

    请注意，以下代码片段需要安装 [jq](https://jqlang.org/)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    CURL='curl -fsS -m 5 --connect-timeout 5'
    for url in $($CURL https://scan.sv-1.test.global.canton.network.sync.global/api/scan/v0/scans | jq -r '.scans[].scans[].publicUrl'); do
      echo -n "$url: "
      $CURL "$url"/api/scan/version | jq -r '.version'
    done)
    ```您应该看到如下所示的输出，其中每一行表示一个 SV 及其所在的版本。如果您看到超时，表明 SV 尚未将您添加到他们的白名单中，如果您没有收到任何错误，则所有 SV 都已添加您。请注意，URL 和版本会随着时间的推移而变化，因此请勿尝试进行精确比较。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    https://scan.sv-2.test.global.canton.network.digitalasset.com: 0.3.6
    https://scan.sv.test.global.canton.network.tradeweb.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.orb1lp.mpch.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.sync.global: 0.3.6
    https://scan.sv.test.global.canton.network.sv-nodeops.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.mpch.io: 0.3.6
    https://scan.sv-2.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.c7.digital: 0.3.6
    https://scan.sv-1.test.global.canton.network.digitalasset.com: 0.3.6
    ```

    除了连接到 Scan 之外，您的验证器还必须能够连接到 SV 的定序器端点。如果您遇到与连接到同步器相关的问题，您可以使用以下代码片段来确认您是否能够到达这些端点（即，SV 也已将您的 IP 列入这些端点的白名单）。请注意，以下代码片段需要安装 [jq](https://jqlang.org/) 和 [grpcurl](https://github.com/fullstorydev/grpcurl)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    for url in $(curl -fsS -m 5 --connect-timeout 5 https://scan.sv-1.test.global.canton.network.sync.global/api/scan/v0/dso-sequencers | jq -r '.domainSequencers[].sequencers[].url | sub("https://"; "")'); do
      echo -n "$url: "
      grpcurl --max-time 10 "$url":443 grpc.health.v1.Health/Check
    done)
    ```

    正常运行且已正确将您的 IP 列入白名单的排序器将在 `grpcurl` 输出中返回 `"status": "SERVING"`。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    sequencer-1.sv-2.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.tradeweb.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.orb1lp.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.sync.global: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.sv-nodeops.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-2.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.c7.digital: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    ```

    这两者的默认配置都需要访问每个扫描和定序器至少 2/3 的 SV。您可以根据自己的选择并自行承担风险，按照验证器舵图配置中所述配置与单个可信扫描和排序器的连接，但代价是失去 BFT 完整性保证。
  </标签>

  <Tab title="主网 (0.6.2)">
    要验证 SV 是否已将您添加到其各自的 IP 允许列表中，您可以查询其扫描 URL。请注意，这必须从您要部署验证器的同一出口 IP 运行，例如，从您要运行 docker compose 设置的虚拟机或从 Kubernetes 集群内运行。

    首先，请通过运行以下命令确认您运行命令的终端中的出口 IP 确实是您为白名单提供的 IP：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -sSL http://checkip.amazonaws.com
    ```

    并确认 IP 与您为白名单提供的 IP 匹配。如果是，请运行以下命令来检查您可以连接到哪个 Scan 实例。

    请注意，以下代码片段需要安装 [jq](https://jqlang.org/)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    CURL='curl -fsS -m 5 --connect-timeout 5'
    for url in $($CURL https://scan.sv-1.global.canton.network.sync.global/api/scan/v0/scans | jq -r '.scans[].scans[].publicUrl'); do
      echo -n "$url: "
      $CURL "$url"/api/scan/version | jq -r '.version'
    done)
    ```您应该看到如下所示的输出，其中每一行表示一个 SV 及其所在的版本。如果您看到超时，表明 SV 尚未将您添加到他们的白名单中，如果您没有收到任何错误，则所有 SV 都已添加您。请注意，URL 和版本会随着时间的推移而变化，因此请勿尝试进行精确比较。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    https://scan.sv-2.test.global.canton.network.digitalasset.com: 0.3.6
    https://scan.sv.test.global.canton.network.tradeweb.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.orb1lp.mpch.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.sync.global: 0.3.6
    https://scan.sv.test.global.canton.network.sv-nodeops.com: 0.3.6
    https://scan.sv-1.test.global.canton.network.mpch.io: 0.3.6
    https://scan.sv-2.test.global.canton.network.cumberland.io: 0.3.6
    https://scan.sv-1.test.global.canton.network.c7.digital: 0.3.6
    https://scan.sv-1.test.global.canton.network.digitalasset.com: 0.3.6
    ```

    除了连接到 Scan 之外，您的验证器还必须能够连接到 SV 的定序器端点。如果您遇到与连接到同步器相关的问题，您可以使用以下代码片段来确认您是否能够到达这些端点（即，SV 也已将您的 IP 列入这些端点的白名单）。请注意，以下代码片段需要安装 [jq](https://jqlang.org/) 和 [grpcurl](https://github.com/fullstorydev/grpcurl)。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    (set -o pipefail
    for url in $(curl -fsS -m 5 --connect-timeout 5 https://scan.sv-1.global.canton.network.sync.global/api/scan/v0/dso-sequencers | jq -r '.domainSequencers[].sequencers[].url | sub("https://"; "")'); do
      echo -n "$url: "
      grpcurl --max-time 10 "$url":443 grpc.health.v1.Health/Check
    done)
    ```

    正常运行且已正确将您的 IP 列入白名单的排序器将在 `grpcurl` 输出中返回 `"status": "SERVING"`。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    sequencer-1.sv-2.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.tradeweb.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.orb1lp.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.sync.global: {
      "status": "SERVING"
    }
    sequencer-1.sv.test.global.canton.network.sv-nodeops.com: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.mpch.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-2.test.global.canton.network.cumberland.io: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.c7.digital: {
      "status": "SERVING"
    }
    sequencer-1.sv-1.test.global.canton.network.digitalasset.com: {
      "status": "SERVING"
    }
    ```

    这两者的默认配置都需要访问每个扫描和定序器至少 2/3 的 SV。您可以根据自己的选择并自行承担风险，按照验证器舵图配置中所述配置与单个可信扫描和排序器的连接，但代价是失去 BFT 完整性保证。
  </标签>
</标签>

## 保持联系

为了与其他验证器运营商保持联系，有一个共享的 Slack 通道和一些邮件列表：

### 松弛

使用 Slack Connect 加入由 `全局同步器 Foundation` 托管的 `#validator-operations` 频道：[https://daholdings.slack.com/archives/C08AP9QR7K4](https://daholdings.slack.com/archives/C08AP9QR7K4)。您的 Slack 工作区可能允许您浏览到此频道，或者您可以要求您的 SV 赞助商向您发送邀请。

### 邮件列表

您可以注册`全局同步器 Foundation`提供的各种邮件列表。为此，请首先在 [https://groups.io/](https://groups.io/) 创建帐户，然后登录 [https://lists.sync.global/](https://lists.sync.global/)。我们推荐以下列表：

* [main](https://lists.sync.global/g/main/messages)：有关 Canton Network 的整体信息。
* [cip 公告](https://lists.sync.global/g/cip-announce/messages)：新的广州改进提案 (CIP)。
* [tokenomics-announce](https://lists.sync.global/g/tokenomics-announce/messages)：用于 Tokenomics 委员会的公告。这还包括新验证者的批准。
* [validator-announce](https://lists.sync.global/g/validator-announce/messages)：用于验证器运营商的其他公告。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
