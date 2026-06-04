---
title: "Kubernetes 验证者部署"
slug: "global-synchronizer-deployment-validator-kubernetes"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-kubernetes.md"
source_title: "Kubernetes Validator Deployment"
tags:
  - global-synchronizer
  - deployment
  - validator-kubernetes
---

# Kubernetes 验证者部署

> 使用 Kubernetes Helm 部署 Canton Network 验证者。

> 使用 Helm 图表在 Kubernetes 上部署 Canton Network 验证者

本节介绍如何使用 Helm 图表在 Kubernetes 中部署独立验证者节点。 Helm 图表部署验证者节点以及关联的钱包和 CNS UI，并将其连接到全局同步器。

## 要求

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。

    2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，将其提供给您的 SV 赞助商，他们将建议将其添加到其他 SV 的 IP 许可名单中。

    4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">下载捆绑包 (DevNet 0.6.4)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.4_splice-node.tar.gz
    ```

    <Warning>
      **如果您丢失了钥匙，您就无法使用您的代币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证者保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证者无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证者的备份部分](https://docs.canton.network/global-synchronizer/production-operations/验证者-backups)或[SV的备份部分](/zh/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>要初始化验证者节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。</p>

    <ul>
      <li>**MIGRATION\_ID** — 您尝试连接的网络 (dev/test/mainnet) 的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到此内容。</li>

      <li>**SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用的 URL。其格式应为 <a href="https://sv.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.dev.global.canton.network.sync.global">[https://sv.sv-1.dev.global.canton.network.sync.global](https://sv.sv-1.dev.global.canton.network.sync.global)</a>。</li>
    </ul>

    <p>**入职\_秘密**<br />
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。</p>

    <注意>
      在 DevNet 上，您可以通过调用任何 SV 上的以下端点（将 `SPONSOR_SV_URL` 替换为上面定义的 SV 应用程序 URL）来自动获取入驻密钥：
    </注>

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -X POST SPONSOR_SV_URL/api/sv/v0/devnet/onboard/验证者/prepare
    ```

    <注意>
      确保使用 **SV 应用程序 URL**（以 `sv.` 开头），而不是扫描 URL（以 `scan.` 开头）。
    </注>

    <注意>
      请注意，此自助密钥仅在 1 小时内有效。
    </注>

    * **TRUSTED\_SCAN\_URL** — 您信任的 SV 的扫描 URL，您的验证者（通常是您的 SV 赞助商）可以访问该 URL。其格式应为 <a href="https://scan.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，对于 全局同步器 Foundation SV，它是 <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>。下面描述了描述您自己的设置而不是网络连接的其他参数。
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。

    2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，将其提供给您的 SV 赞助商，他们将建议将其添加到其他 SV 的 IP 许可名单中。

    4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">下载捆绑包 (TestNet 0.6.3)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.3_splice-node.tar.gz
    ```

    <Warning>
      **如果您丢失了钥匙，您就无法使用您的代币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证者保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证者无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证者的备份部分](https://docs.canton.network/global-synchronizer/production-operations/验证者-backups)或[SV的备份部分](/zh/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>要初始化验证者节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。</p>

    <ul>
      <li>**MIGRATION\_ID** — 您尝试连接的网络 (dev/test/mainnet) 的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到此内容。</li>

      <li>**SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用的 URL。格式应为 <a href="https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.test.global.canton.network.sync.global">[https://sv.sv-1.test.global.canton.network.sync.global](https://sv.sv-1.test.global.canton.network.sync.global)</a>。</li>
    </ul>

    <p>**入职\_秘密**<br />
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。</p>

    * **TRUSTED\_SCAN\_URL** — 您信任的 SV 的扫描 URL，您的验证者（通常是您的 SV 赞助商）可以访问该 URL。其格式应为 <a href="https://scan.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，对于 全局同步器 Foundation SV，它是 <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>。

    下面描述了描述您自己的设置而不是网络连接的其他参数。
  </Tabs>

  <Tab title="主网 (0.6.2)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。

    2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，将其提供给您的 SV 赞助商，他们将建议将其添加到其他 SV 的 IP 许可名单中。4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">下载捆绑包 (MainNet 0.6.2)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.2_splice-node.tar.gz
    ```

    <Warning>
      **如果您丢失了钥匙，您就无法使用您的代币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证者保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证者无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证者的备份部分](https://docs.canton.network/global-synchronizer/production-operations/验证者-backups)或[SV的备份部分](/zh/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>要初始化验证者节点，您需要以下参数来定义您要加入的网络以及执行此操作所需的密钥。</p>

    <ul>
      <li>**MIGRATION\_ID** — 您尝试连接的网络 (dev/test/mainnet) 的当前迁移 ID。该值已被冻结，不得更改上一个值。您可以在 [https://sync.global/sv-network/](https://sync.global/sv-network/) 上找到此内容。</li>

      <li>**SPONSOR\_SV\_URL** — SV 赞助商的 SV 应用的 URL。格式应为 <a href="https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，如果 全局同步器 基金会是您的赞助商，则使用 <a href="https://sv.sv-1.global.canton.network.sync.global">[https://sv.sv-1.global.canton.network.sync.global](https://sv.sv-1.global.canton.network.sync.global)</a>。</li>
    </ul>

    <p>**入职\_秘密**<br />
    您的赞助商提供的入职秘密。如果您还没有，请询​​问您的赞助商。请注意，入职密码是一次性使用的，并在 48 小时后过期。如果您在过期前未加入，则需要向 SV 赞助商请求新的密钥。</p>

    * **TRUSTED\_SCAN\_URL** — 您信任的 SV 的扫描 URL，您的验证者（通常是您的 SV 赞助商）可以访问该 URL。其格式应为 <a href="https://scan.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>，例如，对于 全局同步器 Foundation SV，它是 <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>。

    下面描述了描述您自己的设置而不是网络连接的其他参数。
  </Tabs>
</Tabs>

## 验证者网络图

<img src="https://mintcdn.com/cantonfoundation/eCttQejvyGlU5PC2/images/splice/验证者-network-diagram.png?fit=max&auto=format&n=eCttQejvyGlU5PC2&q=85&s=6d476d77a060cd47d92bbf8347ae1ff4" width="600" alt="验证者网络图" data-path="images/splice/验证者-network-diagram.png" />

## 准备安装集群

在 Kubernetes 中创建应用程序命名空间。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create ns 验证者
```

<注意>
  验证者部署假定每个命名空间有一个验证者。如果您希望在同一集群中运行多个验证者，请为每个验证者创建一个单独的命名空间。
</注>

## HTTP 代理配置

如果您需要在环境中使用 HTTP 转发代理进行出口，则需要在验证者和参与者 Helm 图表中的 `additionalJvmOptions` 中设置 `https.proxyHost` 和 `https.proxyPort`，以使用 HTTP 代理进行传出连接：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
```将 `your.proxy.host` 和 `your_proxy_port` 替换为 HTTP 代理的实际主机和端口。目前不支持代理身份验证。

### 绕过特定主机的代理

<注意>
  设置 `http.nonProxyHosts` 会影响：

  * CN 应用程序（验证者、扫描、SV、钱包）使用的 HTTP 客户端。
  * 同一 JVM 中的 JDK 级 HTTP 客户端（通过默认的 `ProxySelector`）。这包括 CN 应用程序**和 Canton 参与者用于 JWKS / OIDC 发现的 Auth0 JWK 库，以及使用 `java.net.HttpURLConnection` 的文件下载。
  * gRPC 来自其他组件的出口，因为 gRPC 的 Netty 传输将代理决策委托给默认的 JDK `ProxySelector`。
</注>

您可以设置`http.nonProxyHosts`绕过特定目标主机的代理。将直接联系匹配的主机，而不是通过配置的代理。这对于本地网络上可访问的服务非常有用，例如集群内扫描实例或内部监控端点。

该值是一个以 `|` 分隔的模式列表，遵循标准 Java `nonProxyHosts` 语法：

* 模式与请求主机名匹配，不区分大小写。
* `*` 是通配符。通常，它用在模式的开头 (`*.internal`) 或结尾 (`10.*`)。
* 对请求 URI 中的原始主机字符串执行匹配。不执行 DNS 解析，因此 `localhost` 和 `127.0.0.1` 被视为不同的名称，除非您同时列出这两个名称。
* 空值（例如`-Dhttp.nonProxyHosts=`）表示“无旁路模式”。

示例 `additionalJvmOptions` 用于代理外部流量但绕过 `localhost` / `127.0.0.1`、`.internal` 域中的任何主机以及其文字字符串表示形式以 `10.` 开头的任何 IPv4 地址的代理：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
  -Dhttp.nonProxyHosts=localhost|127.0.0.1|*.internal|10.*
```

## 配置 PostgreSQL 身份验证

Helm Chart 创建的 PostgreSQL 实例以及依赖它的所有应用程序都需要通过 Kubernetes 密钥设置用户密码。目前，所有应用程序都使用 Postgres 用户 `cnadmin`。假设您将环境变量 `POSTGRES_PASSWORD` 设置为安全值，可以使用以下命令设置密码：

<div className="todo">
  调出使用托管 postgres 实例的选项
</div>

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic postgres-secrets \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD} \
    -n 验证者
```

## 准备验证者入职

确保您的验证者入门密钥`ONBOARDING_SECRET`已在您之前创建的命名空间中设置。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic splice-app-验证者-入驻-验证者 \
    "--from-literal=secret=${ONBOARDING_SECRET}" \
    -n 验证者
```

## 配置身份验证

为了安全起见，组成验证者节点的各个组件需要能够相互验证自身身份，并且能够验证外部 UI 和 API 用户的身份。我们使用 JWT 访问令牌进行身份验证，并期望这些令牌由（外部）[OpenID Connect](https://openid.net/connect/) (OIDC) 提供商颁发。您必须：

1. 设置 OIDC 提供程序，使后端和 Web UI 用户都能够以受支持的形式获取 JWT。
2. 配置您的后端以使用该 OIDC 提供商。

验证者也支持未经身份验证的部署，但强烈建议不要在生产部署中这样做。如果您想免认证运行，请参考`helm-验证者-no-auth`中的注意事项。

### OIDC 提供商要求

本节提供有关设置 OIDC 提供程序以与验证者节点一起使用的指南。如果您打算使用 [Auth0](https://auth0.com) 来满足您的 验证者 节点的身份验证需求，请直接跳到`helm-验证者-auth0`。

这些文档重点关注 Auth0，并且正在不断测试和维护。可以使用其他 OIDC 提供程序，并且各个社区成员正在积极使用这些提供程序，他们在 Okta 和 Keycloak 社区编写的示例中贡献了一些注释和示例。您的 OIDC 提供商必须可以通过众所周知的 (HTTPS) URL 访问[^1]。在下文中，我们将该 URL 称为 `OIDC_AUTHORITY_URL`。您的验证者节点和任何希望通过连接到验证者节点的 Web UI 进行身份验证的用户都必须能够访问 `OIDC_AUTHORITY_URL`。我们要求您的 OIDC 提供商在 `OIDC_AUTHORITY_URL/.well-known/openid-configuration` 提供[发现文档](https://openid.net/specs/openid-connect-discovery-1_0.html)。我们还要求您的 OIDC 提供商公开 [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517) 文档。在本文档中，我们假设该文档可在 `OIDC_AUTHORITY_URL/.well-known/jwks.json` 获取。

对于机器到机器（验证者节点组件到验证者节点组件）身份验证，您的 OIDC 提供程序必须支持 [OAuth 2.0 客户端凭据授予](https://tools.ietf.org/html/rfc6749#section-4.4) 流程。这意味着您必须能够为所有需要向其他组件验证自身身份的验证者节点组件配置 (`CLIENT_ID`, `CLIENT_SECRET`) 对。目前，这是验证者应用程序后端 - 需要对验证者节点的 Canton 参与者进行身份验证。通过此流程发出的 JWT 的 `sub` 字段必须与 `helm-验证者-auth-secrets-config` 中配置为 `ledger-api-user` 的用户 ID 匹配。在本文档中，我们假设这些 JWT 的 `sub` 字段形成为 `CLIENT_ID@clients`。如果您的 OIDC 提供商的情况并非如此，请在配置下面的 `ledger-api-user` 值时格外注意。

对于面向用户的身份验证 - 允许用户访问验证者节点上托管的各种 Web UI，您的 OIDC 提供商必须支持 [OAuth 2.0 授权代码授予](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) 流程，并允许您获取验证者节点将托管的 Web UI 的客户端标识符。目前，它们是钱包 Web UI 和 CNS Web UI。您可能需要将 OIDC 提供商上的一系列 URL 列入白名单，例如“允许的回调 URL”、“允许的注销 URL”、“允许的 Web 来源”和“允许的来源 (CORS)”。如果您使用此 Runbook 的入口配置，则此处要配置的正确 URL 是`https://钱包.验证者.YOUR_HOSTNAME`（对于钱包 Web UI）和`https://cns.验证者.YOUR_HOSTNAME`（对于 CNS Web UI）。

`YOUR_HOSTNAME` 是一个占位符，您需要将其替换为托管服务的服务器的实际域名或 IP 地址。

必须通过发布的 JWT 的 `sub` 字段设置用户唯一的标识符。在某些情况下，此标识符将用作验证者节点的 Canton 参与者上该用户的用户名。在 `helm-验证者-install` 中，您需要将用户标识符配置为 `validatorWalletUser` - 确保您配置的任何内容与为该用户颁发的 JWT 的 `sub` 字段的内容相匹配。

*所有* JWT 发行用于您的验证者节点：

* 必须使用RS256签名算法进行签名

将来，您的 OIDC 提供商可能还需要颁发 JWT，其中 `scope` 显式设置为 `daml_ledger_api`（当要求这样做作为 OAuth 2.0 授权代码流程的一部分时）。

总而言之，您的 OIDC 提供商设置必须为您提供以下配置值：

|名称 |价值|
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| OIDC\_AUTHORITY\_URL |您的 OIDC 提供商用于获取 `openid-configuration` 和 `jwks.json` 的 URL。 |
|验证者\_客户端\_ID |验证者应用程序后端的 OIDC 提供商的客户端 ID。                      |
|验证者\_客户端\_秘密|验证者应用程序后端的 OIDC 提供商的客户端密钥。                  |
|钱包\_UI\_客户端\_ID |钱包 UI 的 OIDC 提供商的客户端 ID。                                  |
| CNS\_UI\_CLIENT\_ID | CNS UI 的 OIDC 提供商的客户端 ID。                                     |

我们将使用这些值，导出到根据`Name`列命名的环境变量，在`helm-验证者-auth-secrets-config`和`helm-验证者-install`中。第一次开始时，建议将以下两个 JWT 令牌受众配置为相同的值：`https://canton.network.global`。

一旦您可以使用此（简单）默认值确认您的设置正常工作，我们建议您配置与您的部署和 URL 匹配的专用受众值。这对于安全性非常重要，可以避免一个网络上的验证者的令牌可用于另一网络上的验证者。您可以为参与者分类账 API 和验证者后端 API 配置您选择的受众。我们将使用以下配置值来引用它们：

|名称 |价值|
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE |参与者分类帐 API 的受众。例如`https://ledger_api.example.com` |
| OIDC\_AUTHORITY\_VALIDATOR\_AUDIENCE |验证者后端 API 的受众。例如`https://验证者.example.com/api` |

当验证者后端请求分类帐 API 的令牌时，您的 IAM 可能还需要指定范围。我们将使用以下配置值来引用它：

|名称 |价值|
| ----------------------------------- | -------------------------------------------------- |
| OIDC\_AUTHORITY\_LEDGER\_API\_SCOPE |参与者分类帐 API 的范围。可选|

如果您在设置（非 Auth0）OIDC 提供商时遇到问题，浏览 `helm-验证者-auth0` 中的说明也可能会有所帮助，以检查您的 OIDC 提供商设置可能缺少的功能或配置详细信息。

### 配置 Auth0 租户

要将 [Auth0](https://auth0.com) 配置为验证者的 OIDC 提供商，请执行以下操作：

1. 为您的验证者创建 Auth0 租户

2. 创建一个 Auth0 API 来控制对账本 API 的访问：

   > 1. 导航至应用程序 > API，然后单击“创建 API”。将名称设置为`Daml Ledger API`，将标识符设置为`https://canton.network.global`。或者，如果您想配置自己的受众，可以在此处设置标识符。例如`https://ledger_api.example.com`。
   > 2. 在新 API 的“权限”选项卡下，添加范围为 `daml_ledger_api` 的权限以及您选择的说明。
   > 3. 在“设置”选项卡上，向下滚动到“访问设置”并启用“允许离线访问”，以自动刷新令牌。

3. （可选）如果您想要为 API 配置不同的受众，您可以通过创建新的 Auth0 API 并将标识符设置为您选择的受众来实现。例如，

   > 1. 通过将名称设置为`验证者 App API`来创建另一个API，为验证者后端应用程序设置标识符，例如`https://验证者.example.com/api`。

4. 为验证者后端创建 Auth0 应用程序：

   > 1. 在 Auth0 中，导航至应用程序 -> 应用程序，然后单击“创建应用程序”按钮。
   > 2. 将其命名为`验证者 app backend`，选择“机器到机器应用程序”，然后单击“创建”。
   > 3. 在“授权机器对机器应用程序”对话框中选择您在步骤 2 中创建的 `Daml Ledger API` API，然后单击授权。

5. 为钱包 Web UI 创建 Auth0 应用程序。

   > 1. 在 Auth0 中，导航至应用程序 -> 应用程序，然后单击“创建应用程序”按钮。
   > 2. 选择“单页Web应用程序”，命名为`钱包 web UI`，然后单击创建。
   > 3. 确定验证者钱包 UI 的 URL。如果您使用此 Runbook 的入口配置，则为 `https://钱包.验证者.YOUR_HOSTNAME`。
   > 4. 在 Auth0 应用程序设置中，将验证者钱包的 URL 添加到以下内容：
   > *“允许的回调 URL”
   > *“允许的注销 URL”
   > *“允许的 Web 来源”
   > *“允许的来源 (CORS)”
   > 5. 保存您的应用程序设置。

6. 为 CNS Web UI 创建 Auth0 应用程序。重复步骤 5 中描述的所有步骤，并进行以下修改：

   * 在步骤 b 中，使用 `CNS web UI` 作为应用程序的名称。
   * 在步骤 c 和 d 中，使用验证者的 *CNS* UI 的 URL。如果您使用此 Runbook 的入口配置，则为 `https://cns.验证者.YOUR_HOSTNAME`。请参阅 Auth0 的 [自己的用户管理文档](https://auth0.com/docs/manage-users)，了解如何为您创建的两个 Web UI 应用程序设置最终用户帐户。请注意，您将需要创建至少一个此类用户帐户来完成`helm-验证者-install`中的步骤 - 以便能够以验证者节点管理员的身份登录。系统将要求您获取该用户帐户的用户标识符。它可以在 Auth0 界面中的用户管理 -> 用户 -> 您的用户名 -> user\_id（顶部用户名正下方的字段）下找到。

我们将使用下表中列出的环境变量来引用您的 Auth0 配置的各个方面：

|名称 |价值|
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_URL | `https://AUTH0_TENANT_NAME.us.auth0.com` |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE |您为 Ledger API 选择的可选受众。例如`https://ledger_api.example.com` |
|验证者\_客户端\_ID |验证者应用程序后端的 Auth0 应用程序的客户端 ID |
|验证者\_客户端\_秘密|验证者应用程序后端的 Auth0 应用程序的客户端密钥 |
|钱包\_UI\_客户端\_ID |钱包 UI 的 Auth0 应用程序的客户端 ID |
| CNS\_UI\_CLIENT\_ID | CNS UI 的 Auth0 应用程序的客户端 ID |

`AUTH0_TENANT_NAME` 是 Auth0 租户的名称，如 Auth0 项目左上角所示。您可以从每个 Auth0 应用程序的设置页面获取该应用程序的客户端 ID 和密钥。

### 在验证者上配置身份验证

我们现在将根据您在 `helm-验证者-auth-requirements` 或 `helm-验证者-auth0` 末尾导出到环境变量的 OIDC 提供程序配置值来配置您的验证者节点软件。 （注意`helm-验证者-install`中也包含了一些与身份验证相关的配置步骤）

验证者应用程序后端需要以下秘密（如果您的设置中不需要，请忽略范围）

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace 验证者 secret generic splice-app-验证者-ledger-api-auth \
    "--from-literal=ledger-api-user=${VALIDATOR_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${VALIDATOR_CLIENT_ID}" \
    "--from-literal=client-secret=${VALIDATOR_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}" \
    "--from-literal=scope=${OIDC_AUTHORITY_LEDGER_API_SCOPE}"
```

要设置钱包和 CNS UI，请创建以下两个密钥。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace 验证者 secret generic splice-app-钱包-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${WALLET_UI_CLIENT_ID}"

kubectl create --namespace 验证者 secret generic splice-app-cns-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${CNS_UI_CLIENT_ID}"
```

### 无需身份验证即可运行

<Warning>
  在没有身份验证的情况下运行是非常不安全的。任何有权访问钱包用户界面或以任何其他方式访问验证者的人都可以以其选择的用户身份登录您的钱包，或以其他方式代表您进行账本交易。对于任何生产用途，您应该按照上面各节所述配置正确的身份验证。
</Warning>

为了在没有身份验证的情况下运行验证者，请将`disableAuth: true`添加到`splice-node/examples/sv-helm/验证者-values.yaml`和`splice-node/examples/sv-helm/participant-values.yaml`。请注意，您必须在这两个地方禁用身份验证，否则验证者将无法连接到参与者。

无需认证运行时，验证人管理员的用户名是`administrator`。

## 安装软件<注意>
  我们建议安装 [Stakater Reloader](https://github.com/stakater/Reloader)，它会在引用的 Secret 或 ConfigMap 发生更改时自动执行 Pod 的滚动重启。

  默认情况下，Splice Helm 图表包含 `reloader.stakater.com/auto: "true"` 注释。

  如果不使用Reloader，该注解是无害的并且会被忽略。

  要删除它，请在 Helm 值文件中设置 `enableReloader: false`。
</注>

### 配置 Helm 图表

<Tabs>
  <Tab title="DevNet (0.6.4)">
    要安装启动连接到集群的 验证者 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.4
    ```

    请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：

    * 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，您可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。

    如果您使用提供的 postgres helm 图表，请修改 `splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml` 如下：

    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）

    另外，请将文件`splice-node/examples/sv-helm/standalone-participant-values.yaml`修改如下：

    * 将`MIGRATION_ID`替换为您要连接的网络（devnet/testnet/mainnet）上全局同步器的迁移ID。

    您需要通过在`standalone-验证者-values.yaml`中定义`scanClient`块来配置验证者连接到网络的**扫描**服务的方式。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the 验证者 makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The 验证者 connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```对于您选择的 `scanClient` 类型，将 `TRUSTED_SCAN_URL` 替换为您托管的或验证者可访问的信任扫描的 URL。例如，GSF 扫描 URL <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>。对于`scanClient`的`bft-custom`和`bft`模式，您可以指定多个扫描种子URL，并用逗号分隔它们。

    * 如果您想配置 验证者 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为 验证者 应用后端 API 的受众。例如`https://验证者.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-验证者-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为验证者操作方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不*只有后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。请注意，此联系信息将公开可见。如果您不想共享联系信息，可以输入空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。

    您需要通过在 `standalone-验证者-values.yaml` 中定义 `同步器` 配置来配置验证者的参与者连接到 **sequencers** 的方式。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    同步器:
      connectionType: "bft"

    # 同步器 configuration enables to configure how the 验证者's participant connects to the 同步器.
    # 同步器 configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available 同步器 connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # 同步器:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # 同步器:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #同步器:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted 同步器 sequencer url
    ```

    另外，请将文件`splice-node/examples/sv-helm/standalone-验证者-values.yaml`修改如下：

    * 将`MIGRATION_ID`替换为您要连接的网络上的全局同步器的迁移ID。
    * 将 `SPONSOR_SV_URL` 替换为为您提供秘密的 SV 的 URL。
    * 将 `YOUR_VALIDATOR_PARTY_HINT` 替换为验证者操作方所需的名称。它的格式必须是`<organization>-<function>-<enumerator>`。
    * 将 `YOUR_VALIDATOR_NODE_NAME` 替换为您希望验证者节点在网络上表示的名称。通常您可以使用与 `验证者PartyHint` 相同的值。

    最后，请从[https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml)下载UI配置值文件并将其中的值添加到您的`standalone-验证者-values.yaml`。
  </Tabs><Tab title="测试网 (0.6.3)">
    要安装启动连接到集群的 验证者 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.3
    ```

    请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：

    * 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。

    如果您使用提供的 postgres helm 图表，请修改 `splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml` 如下：

    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）

    另外，请将文件`splice-node/examples/sv-helm/standalone-participant-values.yaml`修改如下：

    * 将`MIGRATION_ID`替换为您要连接的网络（devnet/testnet/mainnet）上全局同步器的迁移ID。

    您需要通过在`standalone-验证者-values.yaml`中定义`scanClient`块来配置验证者连接到网络的**扫描**服务的方式。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the 验证者 makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The 验证者 connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```

    对于您选择的 `scanClient` 类型，将 `TRUSTED_SCAN_URL` 替换为您托管的或验证者可访问的信任扫描的 URL。例如，GSF 扫描 URL <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>。对于`scanClient`的`bft-custom`和`bft`模式，您可以指定多个扫描种子URL，并用逗号分隔它们。* 如果您想配置 验证者 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为 验证者 应用后端 API 的受众。例如`https://验证者.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-验证者-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为验证者操作方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不仅仅是*后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。请注意，此联系信息将公开可见。如果您不想共享联系信息，可以输入空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。

    您需要通过在 `standalone-验证者-values.yaml` 中定义 `同步器` 配置来配置验证者的参与者如何连接到 **sequencers**。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    同步器:
      connectionType: "bft"

    # 同步器 configuration enables to configure how the 验证者's participant connects to the 同步器.
    # 同步器 configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available 同步器 connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # 同步器:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # 同步器:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #同步器:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted 同步器 sequencer url
    ```

    另外，请将文件`splice-node/examples/sv-helm/standalone-验证者-values.yaml`修改如下：

    * 将`MIGRATION_ID`替换为您要连接的网络上的全局同步器的迁移ID。
    * 将 `SPONSOR_SV_URL` 替换为为您提供秘密的 SV 的 URL。
    * 将 `YOUR_VALIDATOR_PARTY_HINT` 替换为验证者操作方所需的名称。它的格式必须是`<organization>-<function>-<enumerator>`。
    * 将 `YOUR_VALIDATOR_NODE_NAME` 替换为您希望验证者节点在网络上表示的名称。通常您可以使用与 `验证者PartyHint` 相同的值。

    最后，请从[https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml)下载UI配置值文件并将其中的值添加到您的`standalone-验证者-values.yaml`。
  </Tabs>

  <Tab title="主网 (0.6.2)">
    要安装启动连接到集群的 验证者 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.2
    ```

    请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：* 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，则可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。

    如果您使用提供的 postgres helm 图表，请修改 `splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml` 如下：

    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）

    另外，请将文件`splice-node/examples/sv-helm/standalone-participant-values.yaml`修改如下：

    * 将`MIGRATION_ID`替换为您要连接的网络（devnet/testnet/mainnet）上全局同步器的迁移ID。

    您需要通过在`standalone-验证者-values.yaml`中定义`scanClient`块来配置验证者连接到网络的**扫描**服务的方式。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the 验证者 makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The 验证者 connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```

    对于您选择的 `scanClient` 类型，将 `TRUSTED_SCAN_URL` 替换为您托管的或验证者可访问的信任扫描的 URL。例如，GSF 扫描 URL <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>。对于`scanClient`的`bft-custom`和`bft`模式，您可以指定多个扫描种子URL，并用逗号分隔它们。* 如果您想配置 验证者 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为 验证者 应用后端 API 的受众。例如`https://验证者.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-验证者-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为验证者操作方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不仅仅是*后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。请注意，此联系信息将公开可见。如果您不想共享联系信息，可以输入空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。

    您需要通过在 `standalone-验证者-values.yaml` 中定义 `同步器` 配置来配置验证者的参与者如何连接到 **sequencers**。

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    同步器:
      connectionType: "bft"

    # 同步器 configuration enables to configure how the 验证者's participant connects to the 同步器.
    # 同步器 configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available 同步器 connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # 同步器:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # 同步器:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #同步器:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted 同步器 sequencer url
    ```

    另外，请将文件`splice-node/examples/sv-helm/standalone-验证者-values.yaml`修改如下：

    * 将 `MIGRATION_ID` 替换为您要连接的网络上的全局同步器的迁移 ID。
    * 将 `SPONSOR_SV_URL` 替换为为您提供秘密的 SV 的 URL。
    * 将 `YOUR_VALIDATOR_PARTY_HINT` 替换为验证者操作方所需的名称。它的格式必须是`<organization>-<function>-<enumerator>`。
    * 将 `YOUR_VALIDATOR_NODE_NAME` 替换为您希望验证者节点在网络上表示的名称。通常您可以使用与 `验证者PartyHint` 相同的值。

    最后，请从[https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-同步器-foundation/configs/blob/main/configs/ui-config-values.yaml)下载UI配置值文件并将其中的值添加到您的`standalone-验证者-values.yaml`。
  </Tabs>
</Tabs>

### 安装 Helm Charts

<Tabs>
  <Tab title="DevNet (0.6.4)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install 验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-验证者 -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-values.yaml -f splice-node/examples/sv-helm/standalone-验证者-values.yaml --wait
    ```

    一旦运行，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n 验证者
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    验证者         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    验证者         participant-8988dfb54-m9655           1/1     Running            0               26m
    验证者         postgres-0                            1/1     Running            0               37m
    验证者         验证者-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    验证者         钱包-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。例如，在`postgres`运行之前，`participant`无法启动。
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install 验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-验证者 -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-values.yaml -f splice-node/examples/sv-helm/standalone-验证者-values.yaml --wait
    ```

    一旦运行，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n 验证者
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    验证者         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    验证者         participant-8988dfb54-m9655           1/1     Running            0               26m
    验证者         postgres-0                            1/1     Running            0               37m
    验证者         验证者-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    验证者         钱包-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。例如，`postgres` 运行后，`participant` 才能启动。
  </Tabs>

  <Tab title="主网 (0.6.2)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-验证者-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install 验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-验证者 -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-values.yaml -f splice-node/examples/sv-helm/standalone-验证者-values.yaml --wait
    ```

    一旦运行，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n 验证者
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    验证者         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    验证者         participant-8988dfb54-m9655           1/1     Running            0               26m
    验证者         postgres-0                            1/1     Running            0               37m
    验证者         验证者-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    验证者         钱包-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。例如，`postgres` 运行后，`participant` 才能启动。
  </Tabs>
</Tabs>

## 配置集群入口

应在集群入口控制器中配置以下路由。

|服务 |港口|路线 |
| ---------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `钱包-web-ui` |      | `https://钱包.验证者.<YOUR_HOSTNAME>` |
| `验证者-app` `ans-web-ui` | 5003 | 5003 `https://钱包.验证者.<YOUR_HOSTNAME>/api/验证者` `https://cns.验证者.<YOUR_HOSTNAME>` |
| `验证者-app` | 5003 | 5003 `https://cns.验证者.<YOUR_HOSTNAME>/api/验证者` |
| `participant` | 7575 | 7575 `https://<YOUR_HOSTNAME>/api/json-api`（可选，验证者本身不需要，但如果您想自己访问账本API。您可以自由更改路线）|

* `https://钱包.验证者.<YOUR_HOSTNAME>` 应路由到 `验证者` 命名空间中的服务 `钱包-web-ui`
* `https://钱包.验证者.<YOUR_HOSTNAME>/api/验证者` 应路由到 `验证者` 命名空间中服务 `验证者-app` 端口 5003 处的 `/api/验证者`
* `https://cns.验证者.<YOUR_HOSTNAME>` 应路由到 `验证者` 命名空间中的服务 `ans-web-ui`
* `https://cns.验证者.<YOUR_HOSTNAME>/api/验证者` 应路由到 `验证者` 命名空间中服务 `验证者-app` 端口 5003 处的 `/api/验证者`

<Warning>
  为了保持验证者部署上的攻击面较小，请禁止与验证者部署中的所有其他服务的入口连接。应该假设开放“任何”附加端口或服务都会带来安全风险，需要根据具体情况仔细评估。此外，建议将对上述服务的访问限制在有限数量的明确信任的 IP 地址范围内。
</Warning>Internet 入口配置通常特定于正在配置的集群的网络配置和场景。为了说明 验证者 节点 ingress 的基本要求，我们提供了一个 Helm 图表，该图表使用 Istio 根据上述路由配置 ingress，如下部分详细介绍。

### 要求

为了安装参考图表，您的集群中必须满足以下条件：

* *cert-manager* 必须在集群中可用（请参阅 [cert-manager 文档](https://cert-manager.io/docs/installation/helm/)）
* *istio* 应安装在集群中（请参阅 [istio 文档](https://istio.io/latest/docs/setup/)）

*请注意，它们的部署通常依赖于平台，并且可以在线找到有关如何设置它们的良好文档。*

**Istio 安装示例：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-base istio/base -n istio-system --set defaults.global.istioNamespace=cluster-ingress --wait
helm install istiod istio/istiod -n cluster-ingress --set global.istioNamespace="cluster-ingress" --set meshConfig.accessLogFile="/dev/stdout"  --wait
```

### 安装说明

<Tabs>
  <Tab title="DevNet (0.6.4)">
    创建一个`cluster-ingress`命名空间：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    确保名为 `cn-net-tls` 的密钥中有可用的证书管理器证书。合适的证书定义的示例：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.验证者.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    创建一个名为 `istio-gateway-values.yaml` 的文件，其中包含以下内容（提示：在 GCP 上，您可以从 `gcloud compute addresses list` 获取集群 IP）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    并将其安装到您的集群中：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    在 `cluster-ingress` 命名空间中创建 Istio 网关资源。将以下内容保存到名为 `gateway.yaml` 的文件中，并将 `YOUR_HOSTNAME` 替换为您要用于验证者节点的实际主机名（并且具有指向您上面配置的集群 IP 的 DNS 记录）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    并将其应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    该网关使用您在上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml
    ```
  </Tabs>

  <Tab title="测试网 (0.6.3)">
    创建一个`cluster-ingress`命名空间：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    确保名为 `cn-net-tls` 的机密中有可用的证书管理器证书。合适的证书定义的示例：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.验证者.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    创建一个名为 `istio-gateway-values.yaml` 的文件，其中包含以下内容（提示：在 GCP 上，您可以从 `gcloud compute addresses list` 获取集群 IP）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    并将其安装到您的集群中：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    在 `cluster-ingress` 命名空间中创建 Istio 网关资源。将以下内容保存到名为 `gateway.yaml` 的文件中，并将 `YOUR_HOSTNAME` 替换为您要用于验证者节点的实际主机名（并且具有指向您上面配置的集群 IP 的 DNS 记录）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    并将其应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    该网关使用您在上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml
    ```
  </Tabs>

  <Tab title="主网 (0.6.2)">
    创建一个`cluster-ingress`命名空间：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    确保名为 `cn-net-tls` 的密钥中有可用的证书管理器证书。合适的证书定义的示例：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.验证者.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```创建一个名为 `istio-gateway-values.yaml` 的文件，其中包含以下内容（提示：在 GCP 上，您可以从 `gcloud compute addresses list` 获取集群 IP）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    并将其安装到您的集群中：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    在 `cluster-ingress` 命名空间中创建 Istio 网关资源。将以下内容保存到名为 `gateway.yaml` 的文件中，并将 `YOUR_HOSTNAME` 替换为您要用于验证者节点的实际主机名（并且具有指向您上面配置的集群 IP 的 DNS 记录）：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    并将其应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    该网关使用您在上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-验证者 oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n 验证者 --version ${CHART_VERSION} -f splice-node/examples/sv-helm/验证者-cluster-ingress-values.yaml
    ```
  </Tabs>
</Tabs>

## 登录钱包界面

部署入口后，打开浏览器 [https://钱包.验证者.YOUR\_HOSTNAME](https://钱包.验证者.YOUR_HOSTNAME) 并使用您之前配置为 `validatorWalletUser` 的用户凭据登录。登录后，应该会看到交易页面。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/钱包_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=7df40cdc3f81b03dcb50ce9175c7e280" width="600" alt="登录钱包界面后" data-path="images/splice/钱包_home.png" />

<div className="todo">
  以一种让 Docker compose 用户也可以访问的方式解释下面的配置部分
</div>

## 配置自动流量购买

默认情况下，您的节点将配置为按即用即付方式自动购买流量（请参阅自动购买流量）。要禁用或调整您的需求，请编辑 验证者-values.yaml 文件中的以下部分：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Configuring a 验证者's 流量 top-up loop;
# see documentation for more detailed information.
topup:
  # set to false in order to disable automatic 流量 top-ups
  enabled: true
  # target throughput in bytes / second of sequenced 流量; targetThroughput=0 <=> enabled=false
  targetThroughput: 20000
  # minTopupInterval - minimum time interval that must elapse before the next top-up
  minTopupInterval: "1m"
```<p>每次成功充值时，验证者应用都会购买 `top-up amount` 大约 `targetThroughput * minTopupInterval` 字节的流量（具体金额可能因四舍五入而异）。 `minTopupInterval` 允许验证者操作员控制自动充值发生的上限频率。如果充值金额低于同步器范围的`minTopupAmount`（请参阅[流量参数](https://docs.canton.network/global-synchronizer/deployment/synchronizer-流量#流量-parameters)），`minTopupInterval`会自动拉伸，以便在尊重配置的`targetThroughput`的同时至少购买`minTopupAmount`字节的流量。</p>

<p>当满足以下所有条件时，将触发下一次充值：</p>

<ul>
  <li>可用的[额外流量余额](https://docs.canton.network/global-synchronizer/deployment/synchronizer-流量#流量-accounting-what-counts-as-流量)低于配置的充值金额（即低于`targetThroughput * minTopupInterval`）。</li>

  <li>自上次充值以来至少已过去 `minTopupInterval`。</li>

  <li>验证者的钱包中有足够的 CC 来购买流量的充值金额（DevNet 上除外，验证者应用程序将自动挖掘足够的代币来购买流量）。</li>
</ul>

<p>验证者会从超级验证者那里获得少量的免费流量，足以提交充值交易。但是，如果提交了很多其他交易，则可能会遇到免费流量也耗尽的情况，从而验证者无法提交充值交易。免费流量补贴逐步持续积累。在没有提交交易的情况下，免费流量大约需要二十分钟才能积累到最大可能。如果您在未购买流量的情况下提交过多交易而耗尽了流量余额，请暂停您的验证者节点（验证者应用和参与者）二十分钟，以积累免费流量余额。</p>

<div className="todo">
  \* 因资金不足导致购买流量失败时显示错误信息；目前在这里：`error-insufficient-funds` \* 链接到禁用自动充值的选项，并调出使用第三方流量提供商的选项
</div>

## 配置扫描和自动接受转让优惠

<p>您可以选择将验证者配置为在其托管的某些方的余额超过特定阈值时自动创建向网络上其他方的转移要约。</p>

<p>每当`<senderPartyID>`的余额超过`maxBalanceUSD`时，验证者就会自动向`<receiverPartyId>`创建转账要约，金额将`minBalanceUSD`留在发送者的钱包中。请注意，您需要知道发送方和接收方的参与方 ID，可以从相应用户的钱包 UI（位于右上角）复制该 ID。因此，一旦知道了参与方 ID，就需要在初始部署后的第二步中将其应用于 Helm 图表。</p>

<p>每当验证者收到从`<senderPartyID>`到`<receiverPartyId>`的转账要约时，它都会自动接受。与扫描类似，必须知道参与方 ID 才能应用此配置。</p>

为此，请取消注释并填写 `验证者-values.yaml` 文件中的以下部分：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# If you want funds sweeped out of parties in this 验证者, uncomment and fill in the following:
#walletSweep:
#  "<senderPartyId>":
#    maxBalanceUSD: <maxBalanceUSD>
#    minBalanceUSD: <minBalanceUSD>
#    receiver: "<receiverPartyId>"
#    useTransferPreapproval: false # sweep by transferring directly through the transfer preapproval of the receiver,
#                                    if set to false sweeping creates transfer offers that need to be accepted on the receiver side.
#                                    Note that this refers to the preapprovals described in /appdev/modules/m7-canton-coin-preapprovals
#                                    and not to auto accepting transfers. Auto accept transfers does not setup preapproval contracts that allow
#                                    for a direct transfer but just automates the acceptance of the transfer offer so in that case
#                                    useTransferPreapproval should be set to false.
```同样，您可以将验证者配置为自动接受网络上某些方的转账要约。为此，请取消注释并填写 `验证者-values.yaml` 文件中的以下部分：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# To configure the 验证者 to auto-accept transfer offers from specific parties, uncomment and fill in the following:
#autoAcceptTransfers:
#  "<receiverPartyId>":
#    fromParties:
#      - "<senderPartyId>"
```

## 登录 CNS UI

您可以打开浏览器 [https://cns.验证者.YOUR_HOSTNAME](https://cns.验证者.YOUR_HOSTNAME) 并使用您之前配置为 `validatorWalletUser` 的用户凭据登录。您将能够在 Canton Name Service 上注册一个名称。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/ans_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0084097a0e8f4d5d73d901049a71b3c3" width="600" alt="登录 CNS UI 后" data-path="images/splice/ans_home.png" />

## 参与者修剪

默认情况下，参与者保留所有历史记录。然而，这会导致数据库逐渐增长，并可能减慢某些查询的速度，特别是对账本 API 上的活动合约集的查询。

为了缓解这种情况，可以启用参与者修剪，这将删除指定保留点之外的所有历史记录，并仅保留活动合约集。

请注意，这仅影响参与商店。 CN 应用程序（验证者、SV 和 Scan）不受启用此功能的影响，因此，您钱包中的历史记录永远不会被删除。

下面您可以看到需要添加到 `验证者-values.yaml` 以仅保留过去 48 小时的历史记录的修剪配置示例。

请注意，如果您的节点关闭时间超过了修剪窗口（在上面的示例中为 48 小时），您的节点很可能会被损坏，因为应用程序会追赶参与者尝试继续修剪的速度。因此，建议将修剪窗口设置为您在保证节点正常运行时间方面感到满意的值。将其设置为 30 天通常是一个合理的选择，因为目前Sequencer也会在 30 天后被修剪，因此在较长的停机时间后您将无法赶上网络（有关灾难恢复指南，请参阅灾难恢复）。

有关参与者剪枝的更多详细信息，请参阅[剪枝指南](https://docs.canton.network/global-synchronizer/production-operations/剪枝)。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# To configure participant pruning uncomment the following section.
# Refer to the documentation for more details.
# participantPruningSchedule:
#   cron: 0 /10 * * * ? # Run every 10min
#   maxDuration: 5m # Run for a max of 5min per iteration
#   retention: 48h # Retain history that is newer than 48h.
```

## 配置初始化容器

如果您需要在参与者或验证者部署上配置 init 容器，您可以对 `splice-participant` 或 `splice-验证者` 使用以下 helm 值：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# if you want to disable the default postgres init container:
persistence:
  enablePgInitContainer: false

# if you want additional init containers:
extraInitContainers:
  - name: my-extra-container
    image: busybox
    command: [ "sh", "-c", "echo 'example extra container'" ]
```

## 解决卷所有权问题

出于安全原因，`splice-验证者` 图表中的容器以非 root 用户身份运行（具体来说，用户：组 1001:1001）。 Pod 安装卷供容器使用，并且这些卷需要由容器运行的用户拥有。 Helm 图表使用 `fsGroup` [安全上下文](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) 来确保安装的卷由正确的用户拥有。然而，在某些环境中，这不会按预期工作，并且安装的卷归 root 所有。如果遇到此问题，您可以通过创建 init 容器来解决此问题，将已安装卷的所有权更改为正确的用户。

例如，对于 `/domain-upgrade-dump` 卷（同步器升级所需），您可以将以下内容添加到 `验证者-values.yaml` 文件中：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
extraInitContainers:
    - name: chown-domain-upgrade-dump
      image: busybox:1.37.0
      command: ["sh", "-c", "chown -R 1001:1001 /domain-upgrade-dump"]
      volumeMounts:
        - name: domain-upgrade-dump-volume
          mountPath: /domain-upgrade-dump
```

安装可用的`/participant-bootstrapping-dump`（从身份备份恢复时需要）需要类似的解决方法。

[^1]：该 URL 必须可从集群中运行的 Canton 参与者和验证者应用程序以及所有能够与钱包和 CNS UI 交互的 Web 浏览器访问。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
