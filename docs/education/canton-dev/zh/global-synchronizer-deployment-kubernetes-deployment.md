---
title: "超级验证者 Helm 部署"
slug: "global-synchronizer-deployment-kubernetes-deployment"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/kubernetes-deployment.md"
source_title: "Super Validator Helm Deployment"
tags:
  - global-synchronizer
  - deployment
  - kubernetes-deployment
---

# 超级验证者 Helm 部署

> Global Synchronizer 超级验证者 Kubernetes/Helm 部署指南。

> 使用 Helm 图表在 Kubernetes 上部署超级验证器节点

本节介绍使用 Helm 图表在 Kubernetes 中部署超级验证器 (SV) 节点。 Helm 图表部署一个完整的节点并将其连接到目标集群。

## 要求

<标签>
  <Tab title="DevNet (0.6.4)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。

    2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，建议其他 SV 将其添加到 IP 白名单中。

    4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">下载捆绑包 (DevNet 0.6.4)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.4_splice-node.tar.gz
    ```

    5. 请查询您的目标网络上全局同步器的迁移id和序列id。迁移 ID 冻结为上次重大升级后的值，仅用于 helm 图表值中的`migration.id`。初始同步器部署时序列 ID 为 0，每次逻辑同步器升级时序列 ID 加 1。序列 ID 用于 helm 版本名称、DNS 条目、数据库名称和部署命名。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export MIGRATION_ID=0
    export SERIAL_ID=0
    ```

    <警告>
      **如果您丢失了钥匙，您就无法使用您的硬币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证器保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证器无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证器的备份部分](/global-同步器/生产操作/validator-backups)或[SV的备份部分](/global-同步器/生产操作/sv-backup))
    </警告>
  </标签>

  <Tab title="测试网 (0.6.3)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，建议其他 SV 将其添加到 IP 白名单中。

    4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">下载捆绑包 (TestNet 0.6.3)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.3_splice-node.tar.gz
    ```

    5. 请查询您的目标网络上全局同步器的迁移id和序列id。迁移 ID 冻结为上次重大升级后的值，仅用于 helm 图表值中的`migration.id`。初始同步器部署时序列 ID 为 0，每次逻辑同步器升级时序列 ID 加 1。序列 ID 用于 helm 版本名称、DNS 条目、数据库名称和部署命名。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export MIGRATION_ID=0
    export SERIAL_ID=0
    ```

    <警告>
      **如果您丢失了钥匙，您就无法使用您的硬币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证器保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证器无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证器的备份部分](/global-同步器/生产操作/validator-backups)或[SV的备份部分](/global-同步器/生产操作/sv-backup))
    </警告>
  </标签>

  <Tab title="主网 (0.6.2)">
    1. 一个正在运行的 Kubernetes 集群，您拥有管理员访问权限来创建和管理命名空间。

    2. 一个开发工作站，具有以下功能：

       > 1. `kubectl` - 至少 v1.26.1
       > 2. `helm` - 至少 v3.11.1

    3. 您的集群需要静态出口 IP。获取后，建议其他 SV 将其添加到 IP 白名单中。4. 请从此处下载包含示例 Helm 值文件的发布工件：<a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">下载捆绑包 (MainNet 0.6.2)</a>，并解压该捆绑包：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.2_splice-node.tar.gz
    ```

    5. 请查询您的目标网络上全局同步器的迁移id和序列id。迁移 ID 冻结为上次重大升级后的值，仅用于 helm 图表值中的`migration.id`。初始同步器部署时序列 ID 为 0，每次逻辑同步器升级时序列 ID 加 1。序列 ID 用于 helm 版本名称、DNS 条目、数据库名称和部署命名。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export MIGRATION_ID=0
    export SERIAL_ID=0
    ```

    <警告>
      **如果您丢失了钥匙，您就无法使用您的硬币**。虽然运行节点不需要定期备份，

      **强烈**建议将它们用于恢复目的。

      您应该定期备份部署中的所有数据库，并确保始终拥有最新的身份备份。

      超级验证器保留必要的信息，以便您从身份备份中恢复您的 Canton Coin。

      另一方面，超级验证者**不会**保留他们不参与的应用程序的交易详细信息。

      这意味着，如果您安装了其他应用程序，超级验证器无法帮助您从这些应用程序中恢复数据；

      您只能依靠自己的备份。

      （更多信息请参见[验证器的备份部分](/global-同步器/生产操作/validator-backups)或[SV的备份部分](/global-同步器/生产操作/sv-backup))
    </警告>
  </标签>
</标签>

## 生成SV身份

SV 运营商由人类可读的名称和 EC 公钥来标识。该标识在全局同步器的部署中是稳定的。例如，您应该在（测试）网络重置之间重复使用您的 SV 名称和公钥。

使用以下 shell 命令以 SV 节点软件所需的格式生成密钥对：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 生成密钥对
openssl ecparam -名称 prime256v1 -genkey -noout -out sv-keys.pem

# 对密钥进行编码
public_key_base64=$(openssl ec -in sv-keys.pem -pubout -outform DER 2>/dev/null | base64 | tr -d "\n")
private_key_base64=$(openssl pkcs8 -topk8 -nocrypt -in sv-keys.pem -outform DER 2>/dev/null | base64 | tr -d "\n")# 输出密钥
echo "公钥 = \"$public_key_base64\""
echo "私钥 = \"$private_key_base64\""

# 清理
rm sv-keys.pem
```

These commands should result in an output similar to:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
公钥=“MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAE1eb+JkH2QFRCZedO/P5cq5d2+yfdwP+jE+9w3cT6BqfHxCd/PyA0mmWMePovShmf97HlUajFuN05kZgxvjcPQw==”
私钥=“MEECAQAwEwYHKoZIzj0CAQYIKoZIzj0DAQcEJzAlAgEBBCBsFuFa7Eumkdg4dcf/vxIXgAje2ULVz+qTKP3s/tHqKw==”
```

Store both keys in a safe location. You will be using them every time you want to deploy a new SV node, i.e., also when deploying an SV node to a different deployment of the 全局同步器 and for redeploying an SV node after a (test-)network reset.

The `public-key` and your desired *SV name* need to be approved by a threshold of currently active SVs in order for you to be able to join the network as an SV. For `DevNet` and the current early version of `TestNet`, send the `public-key` and your desired SV name to your point of contact at Digital Asset (DA) and wait for confirmation that your SV identity has been approved and configured at existing SV nodes.

<div className="todo">
  adjust wording above to the fact the MainNet is live
</div>

## Preparing a Cluster for Installation

Create the application namespace within Kubernetes.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl 创建 ns sv
````

## 配置身份验证

为了安全起见，组成 SV 节点的各个组件需要能够相互验证自身身份，并且能够验证外部 UI 和 API 用户的身份。我们使用 JWT 访问令牌进行身份验证，并期望这些令牌由（外部）[OpenID Connect](https://openid.net/connect/) (OIDC) 提供商颁发。您必须：

1. 设置 OIDC 提供程序，使后端和 Web UI 用户都能够以受支持的形式获取 JWT。
2. 配置您的后端以使用该 OIDC 提供商。

### OIDC 提供商要求

本节提供有关设置 OIDC 提供程序以与 SV 节点一起使用的指南。如果您打算使用 [Auth0](https://auth0.com) 来满足 SV 节点的身份验证需求，请直接跳到`helm-sv-auth0`。也就是说，我们鼓励您迁移到与 Auth0 不同的 OIDC 提供商来进行 SV 的长期生产部署，以避免大多数 SV 依赖于同一身份验证提供商而导致的安全风险（这可能会使整个网络面临该提供商的潜在安全问题）。您的 OIDC 提供商必须可以通过众所周知的 (HTTPS) URL 访问[^1]。在下文中，我们将该 URL 称为 `OIDC_AUTHORITY_URL`。您的 SV 节点和任何希望对连接到您的 SV 节点的 Web UI 进行身份验证的用户都必须能够访问 `OIDC_AUTHORITY_URL`。我们要求您的 OIDC 提供商在 `OIDC_AUTHORITY_URL/.well-known/openid-configuration` 提供[发现文档](https://openid.net/specs/openid-connect-discovery-1_0.html)。我们还要求您的 OIDC 提供商公开 [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517) 文档。在本文档中，我们假设该文档可在 `OIDC_AUTHORITY_URL/.well-known/jwks.json` 获取。

对于机器到机器（SV 节点组件到 SV 节点组件）身份验证，您的 OIDC 提供商必须支持 [OAuth 2.0 客户端凭据授予](https://tools.ietf.org/html/rfc6749#section-4.4) 流程。这意味着您必须能够为所有需要向其他节点进行身份验证的 SV 节点组件配置 (`CLIENT_ID`、`CLIENT_SECRET`) 对。目前，这些是验证器应用程序后端和 SV 应用程序后端 - 两者都需要向 SV 节点的 Canton 参与者进行身份验证。通过此流程发出的 JWT 的 `sub` 字段必须与 `helm-sv-auth-secrets-config` 中配置为 `ledger-api-user` 的用户 ID 匹配。在本文档中，我们假设这些 JWT 的 `sub` 字段形成为 `CLIENT_ID@clients`。如果您的 OIDC 提供商的情况并非如此，请在配置下面的 `ledger-api-user` 值时格外注意。对于面向用户的身份验证 - 允许用户访问 SV 节点上托管的各种 Web UI，您的 OIDC 提供商必须支持 [OAuth 2.0 授权代码授予](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) 流程，并允许您获取 SV 节点将托管的 Web UI 的客户端标识符。目前，这些是 SV Web UI、钱包 Web UI 和 CNS Web UI。您可能需要将 OIDC 提供商上的一系列 URL 列入白名单，例如“允许的回调 URL”、“允许的注销 URL”、“允许的 Web 来源”和“允许的来源 (CORS)”。如果您使用此 Runbook 的入口配置，则此处要配置的正确 URL 为 `https://sv.sv.YOUR_HOSTNAME`（对于 SV Web UI）、`https://wallet.sv.YOUR_HOSTNAME`（对于钱包 Web UI）和 `https://cns.sv.YOUR_HOSTNAME`（对于 CNS Web UI）。必须通过发布的 JWT 的 `sub` 字段设置用户唯一的标识符。在某些情况下，此标识符将用作 SV 节点的 Canton 参与者上该用户的用户名。在`helm-sv-install`中，您将需要将用户标识符配置为`validatorWalletUser` - 确保您在那里配置的任何内容都与为该用户颁发的JWT的`sub`字段的内容相匹配。

为与您的 SV 节点一起使用而发布的*所有* JWT：

* 必须使用 RS256 签名算法进行签名。

将来，您的 OIDC 提供商可能还需要颁发 JWT，其中 `scope` 显式设置为 `daml_ledger_api`（当要求这样做作为 OAuth 2.0 授权代码流程的一部分时）。

总而言之，您的 OIDC 提供商设置必须为您提供以下配置值：|名称 |价值|
| ---------------------------------- | ------------------------------------------------------------------------------------------- |
| OIDC\_AUTHORITY\_URL |您的 OIDC 提供商用于获取 `openid-configuration` 和 `jwks.json` 的 URL。 |
|验证者\_客户端\_ID |验证器应用程序后端的 OIDC 提供商的客户端 ID |
|验证者\_客户端\_秘密|验证器应用程序后端的 OIDC 提供商的客户端密钥 |
| SV\_CLIENT\_ID | SV 应用程序后端的 OIDC 提供商的客户端 ID |
| SV\_客户端\_秘密 | SV 应用程序后端的 OIDC 提供商的客户端密钥 |
|钱包\_UI\_客户端\_ID |钱包 UI 的 OIDC 提供商的客户端 ID。                                  |
| SV\_UI\_CLIENT\_ID | SV UI 的 OIDC 提供商的客户端 ID。                                      |
| CNS\_UI\_CLIENT\_ID | CNS UI 的 OIDC 提供商的客户端 ID。                                     |

我们将使用这些值，导出到根据`Name`列命名的环境变量，在`helm-sv-auth-secrets-config`和`helm-sv-install`中。

第一次开始时，建议将以下所有三个 JWT 令牌受众配置为相同的值：`https://canton.network.global`。

一旦您可以使用此（简单）默认值确认您的设置正常工作，我们强烈建议您配置与您的部署和 URL 匹配的专用受众值。这将帮助您避免因对所有组件使用相同的受众而可能出现的潜在安全问题。

您可以为参与者分类账 API、验证器后端 API 和 SV 后端 API 配置您选择的受众。我们将使用以下配置值来引用它们：

|名称 |价值|
| -------------------------------------- | ------------------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE |参与者分类帐 API 的受众。例如`https://ledger_api.example.com` |
| OIDC\_AUTHORITY\_VALIDATOR\_AUDIENCE |验证器后端 API 的受众。例如`https://validator.example.com/api` |
| OIDC\_AUTHORITY\_SV\_AUDIENCE | SV 后端 API 的受众。例如`https://sv.example.com/api` |当 SV、验证器和扫描后端请求分类帐 API 的令牌时，您的 IAM 可能还需要指定范围。我们将使用以下配置值来引用它：

|名称 |价值|
| ----------------------------------- | -------------------------------------------------- |
| OIDC\_AUTHORITY\_LEDGER\_API\_SCOPE |参与者分类帐 API 的范围。可选|

如果您在设置（非 Auth0）OIDC 提供商时遇到问题，浏览 `helm-sv-auth0` 中的说明也可能会有所帮助，以检查您的 OIDC 提供商设置可能缺少的功能或配置详细信息。

### 配置 Auth0 租户

要将 [Auth0](https://auth0.com) 配置为 SV 的 OIDC 提供商，请执行以下操作：

1. 为您的 SV 创建 Auth0 租户

2. 创建一个 Auth0 API 来控制对账本 API 的访问：

   > 1. 导航至应用程序 > API，然后单击“创建 API”。将名称设置为`Daml Ledger API`，将标识符设置为`https://canton.network.global`。或者，如果您想配置自己的受众，可以在此处设置标识符。例如`https://ledger_api.example.com`。
   > 2. 在新 API 的“权限”选项卡下，添加范围为 `daml_ledger_api` 的权限以及您选择的描述。
   > 3. 在“设置”选项卡上，向下滚动到“访问设置”并启用“允许离线访问”，以自动刷新令牌。

3. 为验证器后端创建 Auth0 应用程序：

   > 1. 在 Auth0 中，导航至应用程序 -> 应用程序，然后单击“创建应用程序”按钮。
   > 2. 将其命名为`Validator app backend`，选择“机器到机器应用程序”，然后单击“创建”。
   > 3. 在“授权机器对机器应用程序”对话框中选择您在步骤 2 中创建的 `Daml Ledger API` API，然后单击授权。

4. 为 SV 后端创建 Auth0 应用程序。重复步骤 3 中描述的所有步骤，使用 `SV app backend` 作为应用程序的名称。

5. 为 SV Web UI 创建 Auth0 应用程序：

   > 1. 在 Auth0 中，导航至应用程序 -> 应用程序，然后单击“创建应用程序”按钮。
   > 2. 选择“单页Web应用程序”，命名为`SV web UI`，然后点击创建。
   > 3. 确定验证器 SV UI 的 URL。如果您使用此 Runbook 的入口配置，则为 `https://sv.sv.YOUR_HOSTNAME`。
   > 4. 在 Auth0 应用程序设置中，将 SV URL 添加到以下内容：
   > *“允许的回调 URL”
   > *“允许的注销 URL”
   > *“允许的 Web 来源”
   > *“允许的来源 (CORS)”
   > 5. 保存您的应用程序设置。6. 为钱包 Web UI 创建 Auth0 应用程序。重复步骤 5 中描述的所有步骤，并进行以下修改：

   * 在步骤 b 中，使用 `Wallet web UI` 作为您的应用程序的名称。
   * 在步骤 c 和 d 中，使用 SV 的 *钱包 * UI 的 URL。如果您使用此 Runbook 的入口配置，则为 `https://wallet.sv.YOUR_HOSTNAME`。

7. 为 CNS Web UI 创建 Auth0 应用程序。重复步骤 5 中描述的所有步骤，并进行以下修改：

   * 在步骤 b 中，使用 `CNS web UI` 作为应用程序的名称。
   * 在步骤 c 和 d 中，使用 SV 的 *CNS* UI 的 URL。如果您使用此 Runbook 的入口配置，则为 `https://cns.sv.YOUR_HOSTNAME`。

8.（可选）与上面的账本API类似，默认受众设置为`https://canton.network.global`。
   如果您想为 API 配置不同的受众，可以通过创建新的 Auth0 API 并将标识符设置为您选择的受众来实现。例如，

   1. 导航至应用程序 > API，然后单击“创建 API”。将名称设置为`SV App API`，设置 SV 后端应用程序 API 的标识符，例如`https://sv.example.com/api`。
   2. 通过将名称设置为`Validator App API`来创建另一个API，为验证器后端应用程序设置标识符，例如`https://validator.example.com/api`。

请参阅 Auth0 的 [自己的用户管理文档](https://auth0.com/docs/manage-users)，了解如何为您创建的两个 Web UI 应用程序设置最终用户帐户。请注意，您将需要创建至少一个此类用户帐户才能完成`helm-sv-install`中的步骤 - 以便能够以 SV 节点管理员身​​份登录。系统将要求您获取该用户帐户的用户标识符。它可以在 Auth0 界面中的用户管理 -> 用户 -> 您的用户名 -> user\_id（顶部用户名正下方的字段）下找到。

我们将使用下表中列出的环境变量来引用您的 Auth0 配置的各个方面：|名称 |价值|
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_URL | `https://AUTH0_TENANT_NAME.us.auth0.com` |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE |您为 Ledger API 选择的可选受众。例如`https://ledger_api.example.com` |
|验证者\_客户端\_ID |验证器应用程序后端的 Auth0 应用程序的客户端 ID |
|验证者\_客户端\_秘密|验证器应用程序后端的 Auth0 应用程序的客户端密钥 |
| SV\_CLIENT\_ID | SV 应用程序后端的 Auth0 应用程序的客户端 ID |
| SV\_客户端\_秘密 | SV 应用程序后端的 Auth0 应用程序的客户端密钥 |
|钱包\_UI\_客户端\_ID |钱包 UI 的 Auth0 应用程序的客户端 ID。                                          |
| SV\_UI\_CLIENT\_ID | SV UI 的 Auth0 应用程序的客户端 ID。                                              |
| CNS\_UI\_CLIENT\_ID | CNS UI 的 Auth0 应用程序的客户端 ID。                                             |

`AUTH0_TENANT_NAME` 是 Auth0 租户的名称，如 Auth0 项目左上角所示。您可以从每个 Auth0 应用程序的设置页面获取该应用程序的客户端 ID 和密钥。

### 在 SV 节点上配置身份验证

我们现在将根据您在`helm-sv-auth-requirements`或`helm-sv-auth0`末尾导出到环境变量的OIDC提供商配置值来配置您的SV节点软件。 （请注意，一些与身份验证相关的配置步骤也包含在`helm-sv-install`中。）

以下 kubernetes 密钥将指示参与者为您的 SV 应用程序创建服务用户（如果您的设置中不需要，请忽略范围）。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace sv secret generic splice-app-sv-ledger-api-auth \
    "--from-literal=ledger-api-user=${SV_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${SV_CLIENT_ID}" \
    "--from-literal=client-secret=${SV_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}"
    "--from-literal=scope=${OIDC_AUTHORITY_LEDGER_API_SCOPE}"
```验证器应用程序后端需要以下秘密（如果您的设置中不需要，请忽略范围）。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace sv secret generic splice-app-validator-ledger-api-auth \
    "--from-literal=ledger-api-user=${VALIDATOR_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${VALIDATOR_CLIENT_ID}" \
    "--from-literal=client-secret=${VALIDATOR_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}" \
    "--from-literal=scope=${OIDC_AUTHORITY_LEDGER_API_SCOPE}"
```

要设置钱包、CNS 和 SV UI，请创建以下两个密钥。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace sv secret generic splice-app-wallet-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${WALLET_UI_CLIENT_ID}"

kubectl create --namespace sv secret generic splice-app-sv-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${SV_UI_CLIENT_ID}"

kubectl create --namespace sv secret generic splice-app-cns-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${CNS_UI_CLIENT_ID}"
```

## 配置您的 CometBFT 节点

每个SV节点还部署一个CometBFT节点。该节点必须配置为加入现有的 全局同步器 BFT 链。为此，您首先必须生成可识别节点的密钥。

### 生成您的 CometBFT 节点密钥

<标签>
  <Tab title="DevNet (0.6.4)">
    要生成节点配置，请使用通过 Github 容器注册表 (ghcr.io/digital-asset/decentralized-canton-sync/docker) 提供的 CometBFT docker 映像。

    使用以下 shell 命令生成正确的密钥：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Create a folder to store the config
    mkdir cometbft
    cd cometbft
    # Init the node
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.4 init --home /init
    # Read the node id and keep a note of it for the deployment
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.4 show-node-id --home /init
    ```

    请记下上面打印的节点 ID。

    此外，请保留一些生成的配置文件，如下所示（您可能需要更改它们的权限/所有权，因为它们只能由 root 用户访问）：

    ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cometbft/config/node_key.json
    cometbft/config/priv_validator_key.json
    ```任何其他文件都可以忽略。
  </标签>

  <Tab title="测试网 (0.6.3)">
    要生成节点配置，请使用通过 Github 容器注册表 (ghcr.io/digital-asset/decentralized-canton-sync/docker) 提供的 CometBFT docker 映像。

    使用以下 shell 命令生成正确的密钥：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Create a folder to store the config
    mkdir cometbft
    cd cometbft
    # Init the node
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.3 init --home /init
    # Read the node id and keep a note of it for the deployment
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.3 show-node-id --home /init
    ```

    请记下上面打印的节点 ID。

    此外，请保留一些生成的配置文件，如下所示（您可能需要更改它们的权限/所有权，因为它们只能由 root 用户访问）：

    ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cometbft/config/node_key.json
    cometbft/config/priv_validator_key.json
    ```

    任何其他文件都可以忽略。
  </标签>

  <Tab title="主网 (0.6.2)">
    要生成节点配置，请使用通过 Github 容器注册表 (ghcr.io/digital-asset/decentralized-canton-sync/docker) 提供的 CometBFT docker 映像。

    使用以下 shell 命令生成正确的密钥：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Create a folder to store the config
    mkdir cometbft
    cd cometbft
    # Init the node
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.2 init --home /init
    # Read the node id and keep a note of it for the deployment
    docker run --rm -v "$(pwd):/init" ghcr.io/digital-asset/decentralized-canton-sync/docker/cometbft:0.6.2 show-node-id --home /init
    ```

    请记下上面打印的节点 ID。

    此外，请保留一些生成的配置文件，如下所示（您可能需要更改它们的权限/所有权，因为它们只能由 root 用户访问）：

    ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cometbft/config/node_key.json
    cometbft/config/priv_validator_key.json
    ```

    任何其他文件都可以忽略。
  </标签>
</标签>

### 配置您的 CometBFT 节点密钥根据生成 CometBFT 节点身份的输出，CometBFT 节点配置了一个秘密。秘密的创建如下，其中 `node_key.json` 和 `priv_validator_key.json` 文件代表作为节点身份的一部分生成的文件：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace sv secret generic cometbft-keys \
    "--from-file=node_key.json=node_key.json" \
    "--from-file=priv_validator_key.json=priv_validator_key.json"
```

### 配置 CometBFT 状态同步

<警告>
  CometBFT 状态同步引入了对发起节点在启动时获取状态快照的依赖，因此导致了单点故障。仅当将新节点加入到已经运行一段时间的链时才应启用它。在所有其他情况下，包括完成初始化后和网络重置后的新节点，应禁用状态同步。
</警告>

CometBFT 有一个称为状态同步的功能，允许新的对等点通过读取链头或附近的数据快照并验证它来快速赶上，而不是获取和重放每个块。 （请参阅 [CometBFT 文档](https://docs.cometbft.com/v0.34/core/state-sync)）。这导致新节点上线的时间大大缩短，但代价是新节点的区块历史记录被截断。此外，当链被修剪后，需要在新节点上启用状态同步才能成功引导它们。

CometBFT 中有 3 个控制状态同步的主要配置参数：

* `rpc_servers` - 要连接以获取快照的 CometBFT RPC 服务器列表
* `trust_height` - 您应该信任链条的高度
* `trust_hash` - 可信高度对应的哈希值

使用我们的 helm 图表（参见 `helm-sv-install`）安装的 CometBFT 节点，并在 `splice-node/examples/sv-helm/cometbft-values.yaml` 中设置默认值，在以下情况下会自动使用状态同步进行引导：

* 尚未通过将 `stateSync.enable` 设置为 `false` 来显式禁用它
* 区块链足够成熟，至少可以拍摄 1 个状态快照，即最新区块的高度大于或等于配置的快照间隔

这些快照是从您的入职赞助商处获取的，该赞助商在 `https://sv.sv-X.TARGET_HOSTNAME:443/cometbft-rpc/` 公开了其 CometBFT RPC API。这可以通过相应设置`stateSync.rpcServers`来更改。 `trust_height` 和 `trust_hash` 通过初始化脚本动态计算，不需要且当前不支持显式设置它们。

## 配置 BFT 定序器连接默认情况下，SV 参与者使用 BFT 定序器连接与全局同步器交互，即，它们维护与所有定序器的随机子集（其中大多数通常由其他 SV 操作）的连接，并以与常规验证器使用的相同 `BFT` 方式执行读取和写入。原则上，这种操作模式比使用与 SV 本身操作的定序器的单一连接更稳健。然而，BFT 定序器连接逻辑中的错误或其他 SV 定序器的严重不稳定可能会让您谨慎地暂时切换回使用单个定序器连接。

为此，SV 操作员必须执行以下步骤。

步骤1.在`sv-validator-values.yaml`中，添加以下`同步器`配置。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
同步器:
  connectionType: "trust-single"
  url: "SEQUENCER_PUBLIC_URI" # 同步器s.current.sequencerPublicUrl from sv-values.yaml
```

步骤 2. 在 `validator-values.yaml` 中，添加以下或等效的配置覆盖：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_NO_BFT_SEQUENCER_CONNECTION
      value: "canton.validator-apps.validator_backend.disable-sv-validator-bft-sequencer-connection = true"
```

步骤 3. 在 `sv-values.yaml` 中，添加以下或等效的配置覆盖：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_NO_BFT_SEQUENCER_CONNECTION
      value: "canton.sv-apps.sv.bft-sequencer-connection = false"
```

通过撤消上述更改即可恢复默认行为。

要确认 SV 参与者的当前配置，请打开其 Canton 控制台并执行 `participant.同步器s.config("global")`。如果 BFT 定序器连接被禁用，则应在类似于以下内容的输出中返回单个定序器连接：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.同步器s.config("global")
res1: Option[同步器ConnectionConfig] = Some(
  value = 同步器ConnectionConfig(
    同步器 = 同步器 'global',
    sequencerConnections = SequencerConnections(
      connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://global-domain-0-sequencer:5008),
      sequencer trust threshold = 1,
      submission request amplification = SubmissionRequestAmplification(factor = 1, patience = 10s)
    ),
    manualConnect = false,
    timeTracker = 同步器TimeTrackerConfig(minObservationDuration = 30m)
  )
)
```或者，您也可以在参与者日志中搜索 `DEBUG` 级别条目，例如 `Connecting to 同步器 with config: 同步器ConnectionConfig(...)`，其中包含相同的信息。

## 安装 Postgres 实例

SV 节点需要 4 个 Postgres 实例：一个用于排序器，一个用于调解器，一个用于参与者，一个用于 CN 应用程序。虽然它们都可以使用同一个实例，但我们建议将它们分成 4 个独立的实例，以获得更好的操作灵活性，并更好地控制备份过程。

我们支持云托管的 Postgres 实例和在集群中运行的 Postgres 实例。

### 为 Postgres 密码创建 k8s 密钥

所有应用程序都支持从 Kubernetes 密钥读取 Postgres 密码。目前，所有应用程序都使用 Postgres 用户 `cnadmin`。假设您将环境变量 `POSTGRES_PASSWORD_XXX` 设置为安全值，可以使用以下命令设置密码：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic sequencer-pg-secret \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD_SEQUENCER} \
    -n sv
kubectl create secret generic mediator-pg-secret \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD_MEDIATOR} \
    -n sv
kubectl create secret generic participant-pg-secret \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD_PARTICIPANT} \
    -n sv
kubectl create secret generic apps-pg-secret \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD_APPS} \
    -n sv
```

### 集群中的 Postgres

<标签>
  <Tab title="DevNet (0.6.4)">
    如果您希望将 Postgres 实例作为集群中的 Pod 运行，可以使用 `splice-postgres` Helm 图表来安装它们：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sequencer-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-sequencer.yaml --wait
    helm install mediator-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-mediator.yaml --wait
    helm install participant-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-participant.yaml --wait
    helm install apps-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-apps.yaml --wait
    ```
  </标签><Tab title="测试网 (0.6.3)">
    如果您希望将 Postgres 实例作为集群中的 Pod 运行，可以使用 `splice-postgres` Helm 图表来安装它们：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sequencer-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-sequencer.yaml --wait
    helm install mediator-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-mediator.yaml --wait
    helm install participant-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-participant.yaml --wait
    helm install apps-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-apps.yaml --wait
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    如果您希望将 Postgres 实例作为集群中的 pod 运行，您可以使用 `splice-postgres` Helm 图表来安装它们：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sequencer-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-sequencer.yaml --wait
    helm install mediator-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-mediator.yaml --wait
    helm install participant-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-participant.yaml --wait
    helm install apps-pg oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-apps.yaml --wait
    ```
  </标签>
</标签>

### 云托管 Postgres

如果您希望使用云托管的 Postgres 实例，请按如下方式配置和初始化每个实例：

* 使用 Postgres 版本 14
* 创建一个名为 `cantonnet` 的数据库（这是一个虚拟数据库，不会填充实际数据；作为部署和初始化的一部分，将创建其他数据库）
* 创建一个名为 `cnadmin` 的用户，密码与上面 kubernetes Secret 中配置的密码相同请注意，下面使用的默认 Helm 值文件假设 Postgres 实例是使用上面的 Helm 图表部署的，因此可以通过主机名sequencer-pg、mediator-pg 等进行访问。如果您使用云托管的 Postgres 实例，请使用 Postgres 实例的 IP 地址覆盖 `persistence.host` 下的主机名。为了避免迁移 ID 之间发生冲突，您还需要确保 `persistence.databaseName` 对于每个组件（参与者、定序器、中介器）和迁移 ID 都是唯一的。

## 安装软件

<注意>
  我们建议安装 [Stakater Reloader](https://github.com/stakater/Reloader)，它会在引用的 Secret 或 ConfigMap 发生更改时自动执行 Pod 的滚动重启。

  默认情况下，Splice Helm 图表包含 `reloader.stakater.com/auto: "true"` 注释。

  如果不使用Reloader，该注解是无害的并且会被忽略。

  要删除它，请在 Helm 值文件中设置 `enableReloader: false`。
</注>

### 配置 Helm 图表

<标签>
  <Tab title="DevNet (0.6.4)">
    要安装启动连接到集群的 SV 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.4
    ```

    SV 节点包含 CometBFT 节点，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/cometbft-values.yaml`如下：

    * 根据您要连接的集群，将 `TARGET_CLUSTER` 的所有实例替换为 dev。
    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 dev.global.canton.network.digitalasset.com。
    * 将`SERIAL_ID`的所有实例替换为目标集群上全局同步器的序列ID。请注意，此处 URL 的端口号中也使用了 `SERIAL_ID`！
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 将`YOUR_COMETBFT_NODE_ID`替换为生成CometBFT节点配置时获得的id
    * 将 `YOUR_HOSTNAME` 替换为将用于入口的主机名
    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 根据您要连接的集群，取消注释 `sv1` 部分中相应的 `nodeId`、`publicKey` 和 `keyAddress` 值。<div id="helm-configure-global-domain">
      请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：
    </div>

    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，您可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。
    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 将`YOUR_NODE_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/global-domain-values.yaml`如下：

    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 将`YOUR_SV_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/scan-values.yaml`如下：

    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。

    SV 节点包含一个验证器应用程序，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/validator-values.yaml`如下：* 将 `TRUSTED_SCAN_URL` 替换为您托管的扫描的 URL。如果您使用此 Runbook 的入口配置，则可以使用 `"http://scan-app.sv:5012"`。
    * 如果您想配置 Validator 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为 Validator 应用后端 API 的受众。例如`https://validator.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-sv-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为 SV 方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不仅仅是*后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为您在 `sv-values.yaml` 中使用的相同接触点。将此设置为空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您的验证器不应该持有任何 CC，您应该通过将 `enableWallet` 设置为 `false` 来禁用钱包。请注意，如果钱包被禁用，您不应安装钱包或 CNS UI，因为它们将无法工作。

    另外，请将文件`splice-node/examples/sv-helm/sv-validator-values.yaml`修改如下：

    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 dev.global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`SERIAL_ID`的所有实例替换为目标集群上全局同步器的序列ID。

    SV 的私钥和公钥在 K8s 密钥中定义。如果您尚未执行此操作，请首先按照生成 SV 身份部分中的说明操作，获取并注册您的 SV 的名称和密钥对。将 `YOUR_PUBLIC_KEY` 和 `YOUR_PRIVATE_KEY` 替换为在生成 SV 身份时获取的 `public-key` 和 `private-key` 值。

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create secret --namespace sv generic splice-app-sv-key \
        --from-literal=public=YOUR_PUBLIC_KEY \
        --from-literal=private=YOUR_PRIVATE_KEY
    ```

    要配置您的 sv 应用程序，请修改文件`splice-node/examples/sv-helm/sv-values.yaml`，如下所示：* 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 dev.global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 如果您想配置 SV 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_SV_AUDIENCE` 替换为 SV 应用后端 API 的受众。例如`https://sv.example.com/api`。
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 请在 SV 配置中将 `同步器s.current.sequencerPublicUrl` 设置为您的定序器服务的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 请在 SV 配置中将 `scan.publicUrl` 设置为扫描应用程序的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 建议配置剪枝。
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。如果您不想共享它，请将其设置为空字符串。
    * 如果您想与其他方重新分配全部或部分SV奖励，您可以在`extraBeneficiaries`部分填写所需的参与方以及对应的奖励百分比。请注意，您注册的一方必须在网络上已知，才能成功发放优惠券。此外，该方必须托管在验证器节点上，其钱包才能收集 SV 奖励优惠券。如果钱包正在运行，该收集将自动进行。如果在领取奖励券的时间内没有运行，则相应的奖励将被标记为无人领取，并存储在 DSO 范围内的无人领取奖励池中。只需重新启动 SV 应用程序即可更改 `extraBeneficiaries`。
    * （可选）取消注释 `initialAmuletPrice` 行并将其设置为您想要的护身符价格。这将从您的 SV 使用入职时配置的价格创建护身符价格投票。如果未设置，则不会投票。稍后可以通过 SV 应用程序 UI 手动完成此操作。```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Replace MIGRATION_ID with the migration ID of the 全局同步器.
    migration:
      # This should stay constant after the introduction of logical 同步器 upgrades.
      id: "MIGRATION_ID"
    ```

    请修改文件`splice-node/examples/sv-helm/info-values.yaml`如下：

    * 将`TARGET_CLUSTER`替换为dev
    * 将`MD5_HASH_OF_ALLOWED_IP_RANGES`替换为开发网络对应的`allowed-ip-ranges.json`文件的MD5哈希值。
    * 将`MD5_HASH_OF_APPROVED_SV_IDENTITIES`替换为开发网络对应的`approved-sv-id-values.yaml`文件的MD5哈希值。
    * 将`MIGRATION_ID`替换为目标集群上全局同步器的迁移ID。
    * 将`CHAIN_ID_SUFFIX`的所有实例替换为开发网络的链ID后缀。
    * 如果您正在使用`staging`同步器和`legacy`同步器部分，请取消注释它们。
    * 将 `STAGING_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上暂存同步器的迁移 ID。
    * 将 `STAGING_SYNCHRONIZER_VERSION` 替换为目标集群上的暂存同步器的版本。
    * 将 `LEGACY_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上旧同步器的迁移 ID。
    * 将 `LEGACY_SYNCHRONIZER_VERSION` 替换为目标集群上旧同步器的版本。

    [configs repo](https://github.com/global-同步器-foundation/configs) 包含用于配置 SV 节点的建议值。将这些 YAML 文件的路径存储在以下环境变量中：

    1. `SV_IDENTITIES_FILE`：您的节点自动批准为对等 SV 的 SV 身份列表。找到并查看与您要连接的网络相对应的 `approved-sv-id-values.yaml` 文件。
    2. `UI_CONFIG_VALUES_FILE`：文件位于`configs/ui-config-values.yaml`，所有网络都相同。

    下面将使用这些环境变量。
  </标签>

  <Tab title="测试网 (0.6.3)">
    要安装启动连接到集群的 SV 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.3
    ```

    SV 节点包含 CometBFT 节点，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/cometbft-values.yaml`如下：* 根据您要连接的集群，将 `TARGET_CLUSTER` 的所有实例替换为 test。
    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 test.global.canton.network.digitalasset.com。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。请注意，此处 URL 的端口号中也使用了 `SERIAL_ID`！
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 将`YOUR_COMETBFT_NODE_ID`替换为生成CometBFT节点配置时获得的id
    * 将 `YOUR_HOSTNAME` 替换为将用于入口的主机名
    * 将`db.volumeSize`和`db.volumeStorageClass`添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 根据您要连接的集群，取消注释 `sv1` 部分中相应的 `nodeId`、`publicKey` 和 `keyAddress` 值。

    <div id="helm-configure-global-domain">
      请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：
    </div>

    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，则可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。
    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 将`YOUR_NODE_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/global-domain-values.yaml`如下：

    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 将`YOUR_SV_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/scan-values.yaml`如下：* 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。

    SV 节点包含一个验证器应用程序，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/validator-values.yaml`如下：

    * 将 `TRUSTED_SCAN_URL` 替换为您托管的扫描的 URL。如果您使用此 Runbook 的入口配置，则可以使用 `"http://scan-app.sv:5012"`。
    * 如果您想配置验证器应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为验证器应用后端 API 的受众。例如`https://validator.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-sv-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为 SV 方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不仅仅是*后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为您在 `sv-values.yaml` 中使用的相同接触点。将此设置为空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您的验证器不应该持有任何 CC，您应该通过将 `enableWallet` 设置为 `false` 来禁用钱包。请注意，如果钱包被禁用，您不应安装钱包或 CNS UI，因为它们将无法工作。

    另外，请将文件`splice-node/examples/sv-helm/sv-validator-values.yaml`修改如下：

    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 test.global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`SERIAL_ID`的所有实例替换为目标集群上全局同步器的序列ID。

    SV 的私钥和公钥在 K8s 密钥中定义。如果您尚未执行此操作，请首先按照生成 SV 身份部分中的说明操作，获取并注册您的 SV 的名称和密钥对。将 `YOUR_PUBLIC_KEY` 和 `YOUR_PRIVATE_KEY` 替换为在生成 SV 身份时获取的 `public-key` 和 `private-key` 值。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create secret --namespace sv generic splice-app-sv-key \
        --from-literal=public=YOUR_PUBLIC_KEY \
        --from-literal=private=YOUR_PRIVATE_KEY
    ```

    要配置您的 sv 应用程序，请修改文件`splice-node/examples/sv-helm/sv-values.yaml`，如下所示：* 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 test.global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 如果您想配置 SV 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_SV_AUDIENCE` 替换为 SV 应用后端 API 的受众。例如`https://sv.example.com/api`。
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 请在 SV 配置中将 `同步器s.current.sequencerPublicUrl` 设置为您的定序器服务的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 请在 SV 配置中将 `scan.publicUrl` 设置为扫描应用程序的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 建议配置剪枝。
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。如果您不想共享它，请将其设置为空字符串。
    * 如果您想与其他方重新分配全部或部分SV奖励，您可以在`extraBeneficiaries`部分填写所需的参与方以及对应的奖励百分比。请注意，您注册的一方必须在网络上已知，才能成功发放优惠券。此外，该方必须托管在验证器节点上，其钱包才能收集 SV 奖励优惠券。如果钱包正在运行，该收集将自动进行。如果在领取奖励券的时间内没有运行，则相应的奖励将被标记为无人领取，并存储在 DSO 范围内的无人领取奖励池中。只需重新启动 SV 应用程序即可更改 `extraBeneficiaries`。
    * （可选）取消注释 `initialAmuletPrice` 行并将其设置为您想要的护身符价格。这将从您的 SV 使用入职时配置的价格创建护身符价格投票。如果未设置，则不会投票。稍后可以通过 SV 应用程序 UI 手动完成此操作。```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Replace MIGRATION_ID with the migration ID of the 全局同步器.
    migration:
      # This should stay constant after the introduction of logical 同步器 upgrades.
      id: "MIGRATION_ID"
    ```

    请修改文件`splice-node/examples/sv-helm/info-values.yaml`如下：

    * 将`TARGET_CLUSTER`替换为测试
    * 将`MD5_HASH_OF_ALLOWED_IP_RANGES`替换为测试网络对应的`allowed-ip-ranges.json`文件的MD5哈希值。
    * 将`MD5_HASH_OF_APPROVED_SV_IDENTITIES`替换为测试网络对应的`approved-sv-id-values.yaml`文件的MD5哈希值。
    * 将`MIGRATION_ID`替换为目标集群上全局同步器的迁移ID。
    * 将`CHAIN_ID_SUFFIX`的所有实例替换为测试网络的链ID后缀。
    * 如果您正在使用`staging`同步器和`legacy`同步器部分，请取消注释它们。
    * 将 `STAGING_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上暂存同步器的迁移 ID。
    * 将 `STAGING_SYNCHRONIZER_VERSION` 替换为目标集群上的暂存同步器的版本。
    * 将 `LEGACY_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上旧同步器的迁移 ID。
    * 将 `LEGACY_SYNCHRONIZER_VERSION` 替换为目标集群上旧同步器的版本。

    [configs repo](https://github.com/global-同步器-foundation/configs) 包含用于配置 SV 节点的建议值。将这些 YAML 文件的路径存储在以下环境变量中：

    1. `SV_IDENTITIES_FILE`：您的节点自动批准为对等 SV 的 SV 身份列表。找到并查看与您要连接的网络相对应的 `approved-sv-id-values.yaml` 文件。
    2. `UI_CONFIG_VALUES_FILE`：文件位于`configs/ui-config-values.yaml`，所有网络都相同。

    下面将使用这些环境变量。
  </标签>

  <Tab title="主网 (0.6.2)">
    要安装启动连接到集群的 SV 节点所需的 Helm 图表，您需要满足一些先决条件。首先，需要定义一个环境变量来引用连接到该环境所需的 Helm 图表版本：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.2
    ```

    SV 节点包含 CometBFT 节点，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/cometbft-values.yaml`如下：* 根据您要连接的集群，将 `TARGET_CLUSTER` 的所有实例替换为 main。
    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 global.canton.network.digitalasset.com。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。请注意，此处 URL 的端口号中也使用了 `SERIAL_ID`！
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 将`YOUR_COMETBFT_NODE_ID`替换为生成CometBFT节点配置时获得的id
    * 将 `YOUR_HOSTNAME` 替换为将用于入口的主机名
    * 将`db.volumeSize`和`db.volumeStorageClass`添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 根据您要连接的集群，取消注释 `sv1` 部分中相应的 `nodeId`、`publicKey` 和 `keyAddress` 值。

    <div id="helm-configure-global-domain">
      请修改文件`splice-node/examples/sv-helm/participant-values.yaml`如下：
    </div>

    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`auth.targetAudience`条目中的`OIDC_AUTHORITY_LEDGER_API_AUDIENCE`替换为账本API的受众。例如`https://ledger_api.example.com`。如果您还没有准备好使用自定义受众，则可以使用建议的默认值`https://canton.network.global`。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您运行的 Kubernetes 版本早于 1.24，请将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。
    * 将 `db.volumeSize` 和 `db.volumeStorageClass` 添加到值文件中，如有必要，调整持久存储大小和存储类别。 （这些值默认为 20GiB 和 `standard-rwo`）
    * 将`YOUR_NODE_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/global-domain-values.yaml`如下：

    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 将`YOUR_SV_NAME`替换为您在创建SV身份时选择的名称。

    请修改文件`splice-node/examples/sv-helm/scan-values.yaml`如下：* 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。

    SV 节点包含一个验证器应用程序，因此您还需要对其进行配置。请修改文件`splice-node/examples/sv-helm/validator-values.yaml`如下：

    * 将 `TRUSTED_SCAN_URL` 替换为您托管的扫描的 URL。如果您使用此 Runbook 的入口配置，则可以使用 `"http://scan-app.sv:5012"`。
    * 如果您想配置验证器应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` 替换为验证器应用后端 API 的受众。例如`https://validator.example.com/api`。
    * 如果要配置 Ledger API 的受众，请将 `splice-app-sv-ledger-api-auth` k8s 密钥中的 `audience` 字段设置为 Ledger API 的受众。例如`https://ledger_api.example.com`。
    * 将 `OPERATOR_WALLET_USER_ID` 替换为 IAM 中您想要用来作为 SV 方登录钱包的用户 ID。请注意，这应该是完整的用户 ID，例如 `auth0|43b68e1e4978b000cefba352`，*不仅仅是*后缀 `43b68e1e4978b000cefba352`
    * 将 `YOUR_CONTACT_POINT` 替换为您在 `sv-values.yaml` 中使用的相同接触点。将此设置为空字符串。
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 如果您的验证器不应该持有任何 CC，您应该通过将 `enableWallet` 设置为 `false` 来禁用钱包。请注意，如果钱包被禁用，您不应安装钱包或 CNS UI，因为它们将无法工作。

    另外，请将文件`splice-node/examples/sv-helm/sv-validator-values.yaml`修改如下：

    * 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将`SERIAL_ID`的所有实例替换为目标集群上全局同步器的序列ID。

    SV 的私钥和公钥在 K8s 密钥中定义。如果您尚未执行此操作，请首先按照生成 SV 身份部分中的说明操作，获取并注册您的 SV 的名称和密钥对。将 `YOUR_PUBLIC_KEY` 和 `YOUR_PRIVATE_KEY` 替换为在生成 SV 身份时获取的 `public-key` 和 `private-key` 值。```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create secret --namespace sv generic splice-app-sv-key \
        --from-literal=public=YOUR_PUBLIC_KEY \
        --from-literal=private=YOUR_PRIVATE_KEY
    ```

    要配置您的 sv 应用程序，请修改文件`splice-node/examples/sv-helm/sv-values.yaml`，如下所示：* 根据您要连接的集群，将 `TARGET_HOSTNAME` 的所有实例替换为 global.canton.network.digitalasset.com。
    * 将`MIGRATION_ID`的所有实例替换为目标集群上全局同步器的迁移ID。
    * 将 `SERIAL_ID` 的所有实例替换为目标集群上全局同步器的序列 ID。
    * 如果您想配置 SV 应用后端 API 的受众，请将 `auth.audience` 条目中的 `OIDC_AUTHORITY_SV_AUDIENCE` 替换为 SV 应用后端 API 的受众。例如`https://sv.example.com/api`。
    * 将 `YOUR_SV_NAME` 替换为您在创建 SV 身份时选择的名称（这必须与您的 SV 批准加入的字符串完全匹配）
    * 如上所述，通过将 `OIDC_AUTHORITY_URL` 替换为您的身份验证提供商的 OIDC URL，更新 `auth.jwksUrl` 条目以指向您的身份验证提供商的 JWK 设置文档。
    * 请在 SV 配置中将 `同步器s.current.sequencerPublicUrl` 设置为您的定序器服务的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 请在 SV 配置中将 `scan.publicUrl` 设置为扫描应用程序的 URL。如果您使用此 Runbook 的入口配置，则只需将 `YOUR_HOSTNAME` 替换为您的主机名即可。
    * 建议配置剪枝。
    * 将 `YOUR_CONTACT_POINT` 替换为 slack 用户名或电子邮件地址，节点操作员可以使用该用户名或电子邮件地址在您的节点出现问题时与您联系。如果您不想共享它，请将其设置为空字符串。
    * 如果您想与其他方重新分配全部或部分SV奖励，您可以在`extraBeneficiaries`部分填写所需的参与方以及对应的奖励百分比。请注意，您注册的一方必须在网络上已知，才能成功发放优惠券。此外，该方必须托管在验证器节点上，其钱包才能收集 SV 奖励优惠券。如果钱包正在运行，该收集将自动进行。如果在领取奖励券的时间内没有运行，则相应的奖励将被标记为无人领取，并存储在 DSO 范围内的无人领取奖励池中。只需重新启动 SV 应用程序即可更改 `extraBeneficiaries`。
    * （可选）取消注释 `initialAmuletPrice` 行并将其设置为您想要的护身符价格。这将从您的 SV 使用入职时配置的价格创建护身符价格投票。如果未设置，则不会投票。稍后可以通过 SV 应用程序 UI 手动完成此操作。```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Replace MIGRATION_ID with the migration ID of the 全局同步器.
    migration:
      # This should stay constant after the introduction of logical 同步器 upgrades.
      id: "MIGRATION_ID"
    ```

    请修改文件`splice-node/examples/sv-helm/info-values.yaml`如下：

    * 将`TARGET_CLUSTER`替换为main
    * 将`MD5_HASH_OF_ALLOWED_IP_RANGES`替换为主网对应的`allowed-ip-ranges.json`文件的MD5哈希值。
    * 将`MD5_HASH_OF_APPROVED_SV_IDENTITIES`替换为主网对应的`approved-sv-id-values.yaml`文件的MD5哈希值。
    * 将`MIGRATION_ID`替换为目标集群上全局同步器的迁移ID。
    * 将`CHAIN_ID_SUFFIX`的所有实例替换为主网的链ID后缀。
    * 如果您正在使用`staging`同步器和`legacy`同步器部分，请取消注释它们。
    * 将 `STAGING_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上暂存同步器的迁移 ID。
    * 将 `STAGING_SYNCHRONIZER_VERSION` 替换为目标集群上的暂存同步器的版本。
    * 将 `LEGACY_SYNCHRONIZER_MIGRATION_ID` 替换为目标集群上旧同步器的迁移 ID。
    * 将 `LEGACY_SYNCHRONIZER_VERSION` 替换为目标集群上旧同步器的版本。

    [configs repo](https://github.com/global-同步器-foundation/configs) 包含用于配置 SV 节点的建议值。将这些 YAML 文件的路径存储在以下环境变量中：

    1. `SV_IDENTITIES_FILE`：您的节点自动批准为对等 SV 的 SV 身份列表。找到并查看与您要连接的网络相对应的 `approved-sv-id-values.yaml` 文件。
    2. `UI_CONFIG_VALUES_FILE`：文件位于`configs/ui-config-values.yaml`，所有网络都相同。

    下面将使用这些环境变量。
  </标签>
</标签>

### 安装 Helm Charts

<标签>
  <Tab title="DevNet (0.6.4)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。

    安装 Canton 和 CometBFT 组件：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install global-domain-${SERIAL_ID}-cometbft oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cometbft -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/cometbft-values.yaml --wait
    helm install global-domain-${SERIAL_ID} oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-global-domain -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/global-domain-values.yaml --wait
    ```

    请注意，我们在命名 Canton 同步器组件时使用序列号。这是为了支持并行操作这些组件的多个实例，作为逻辑同步器升级的一部分。

    安装参与者：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml --wait
    ```

    安装 SV 节点应用程序：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-sv-node -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-values.yaml -f ${SV_IDENTITIES_FILE} -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install scan oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-scan -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/scan-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/sv-validator-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    ```

    安装 INFO 应用程序，该应用程序用于提供有关 SV 节点及其配置的信息：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install info oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-info -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/info-values.yaml
    ```

    一旦一切都运行起来，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n sv
    NAME                                         READY   STATUS    RESTARTS      AGE
    apps-pg-0                                    2/2     Running   0             14m
    ans-web-ui-5cf76bfc98-bh6tw                  2/2     Running   0             10m
    global-domain-0-cometbft-c584c9468-9r2v5     2/2     Running   2 (14m ago)   14m
    global-domain-0-mediator-7bfb5f6b6d-ts5zp    2/2     Running   0             13m
    global-domain-0-sequencer-6c85d98bb6-887c7   2/2     Running   0             13m
    info-9fb7bc859-27226                         2/2     Running   0             10m
    mediator-pg-0                                2/2     Running   0             14m
    participant-0-57579c64ff-wmzk5               2/2     Running   0             14m
    participant-pg-0                             2/2     Running   0             14m
    scan-app-b8456cc64-stjm2                     2/2     Running   0             10m
    scan-web-ui-7c6b5b59dc-fjxjg                 2/2     Running   0             10m
    sequencer-pg-0                               2/2     Running   0             14m
    sv-app-7f4b6f468c-sj7ch                      2/2     Running   0             13m
    sv-web-ui-67bfbdfc77-wwvp9                   2/2     Running   0             13m
    validator-app-667445fdfc-rcztx               2/2     Running   0             10m
    wallet-web-ui-648f86f9f9-lffz5               2/2     Running   0             10m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。 `participant` 运行后，`splice-sv-node` 才能启动，`participant` `postgres` 运行后，`participant` 无法启动。
  </标签>

  <Tab title="测试网 (0.6.3)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。

    安装 Canton 和 CometBFT 组件：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install global-domain-${SERIAL_ID}-cometbft oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cometbft -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/cometbft-values.yaml --wait
    helm install global-domain-${SERIAL_ID} oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-global-domain -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/global-domain-values.yaml --wait
    ```请注意，我们在命名 Canton 同步器组件时使用序列号。这是为了支持并行操作这些组件的多个实例，作为逻辑同步器升级的一部分。

    安装参与者：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml --wait
    ```

    安装 SV 节点应用程序：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-sv-node -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-values.yaml -f ${SV_IDENTITIES_FILE} -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install scan oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-scan -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/scan-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/sv-validator-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    ```

    安装 INFO 应用程序，该应用程序用于提供有关 SV 节点及其配置的信息：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install info oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-info -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/info-values.yaml
    ```

    一旦一切都运行起来，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n sv
    NAME                                         READY   STATUS    RESTARTS      AGE
    apps-pg-0                                    2/2     Running   0             14m
    ans-web-ui-5cf76bfc98-bh6tw                  2/2     Running   0             10m
    global-domain-0-cometbft-c584c9468-9r2v5     2/2     Running   2 (14m ago)   14m
    global-domain-0-mediator-7bfb5f6b6d-ts5zp    2/2     Running   0             13m
    global-domain-0-sequencer-6c85d98bb6-887c7   2/2     Running   0             13m
    info-9fb7bc859-27226                         2/2     Running   0             10m
    mediator-pg-0                                2/2     Running   0             14m
    participant-0-57579c64ff-wmzk5               2/2     Running   0             14m
    participant-pg-0                             2/2     Running   0             14m
    scan-app-b8456cc64-stjm2                     2/2     Running   0             10m
    scan-web-ui-7c6b5b59dc-fjxjg                 2/2     Running   0             10m
    sequencer-pg-0                               2/2     Running   0             14m
    sv-app-7f4b6f468c-sj7ch                      2/2     Running   0             13m
    sv-web-ui-67bfbdfc77-wwvp9                   2/2     Running   0             13m
    validator-app-667445fdfc-rcztx               2/2     Running   0             10m
    wallet-web-ui-648f86f9f9-lffz5               2/2     Running   0             10m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。 `participant` 运行后，`splice-sv-node` 才能启动，`participant` `postgres` 运行后，`participant` 无法启动。
  </标签>

  <Tab title="主网 (0.6.2)">
    准备好这些文件后，您可以按顺序执行以下 helm 命令。通常最好等到每个部署达到稳定状态后再继续下一步。

    安装 Canton 和 CometBFT 组件：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install global-domain-${SERIAL_ID}-cometbft oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cometbft -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/cometbft-values.yaml --wait
    helm install global-domain-${SERIAL_ID} oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-global-domain -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/global-domain-values.yaml --wait
    ```请注意，我们在命名 Canton 同步器组件时使用序列号。这是为了支持并行操作这些组件的多个实例，作为逻辑同步器升级的一部分。

    安装参与者：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml --wait
    ```

    安装 SV 节点应用程序：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-sv-node -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-values.yaml -f ${SV_IDENTITIES_FILE} -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install scan oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-scan -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/scan-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/sv-validator-values.yaml -f ${UI_CONFIG_VALUES_FILE} --wait
    ```

    安装 INFO 应用程序，该应用程序用于提供有关 SV 节点及其配置的信息：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install info oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-info -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/info-values.yaml
    ```

    一旦一切都运行起来，您应该能够检查集群的状态并观察在新命名空间中运行的 Pod。典型的查询可能如下所示：```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n sv
    NAME                                         READY   STATUS    RESTARTS      AGE
    apps-pg-0                                    2/2     Running   0             14m
    ans-web-ui-5cf76bfc98-bh6tw                  2/2     Running   0             10m
    global-domain-0-cometbft-c584c9468-9r2v5     2/2     Running   2 (14m ago)   14m
    global-domain-0-mediator-7bfb5f6b6d-ts5zp    2/2     Running   0             13m
    global-domain-0-sequencer-6c85d98bb6-887c7   2/2     Running   0             13m
    info-9fb7bc859-27226                         2/2     Running   0             10m
    mediator-pg-0                                2/2     Running   0             14m
    participant-0-57579c64ff-wmzk5               2/2     Running   0             14m
    participant-pg-0                             2/2     Running   0             14m
    scan-app-b8456cc64-stjm2                     2/2     Running   0             10m
    scan-web-ui-7c6b5b59dc-fjxjg                 2/2     Running   0             10m
    sequencer-pg-0                               2/2     Running   0             14m
    sv-app-7f4b6f468c-sj7ch                      2/2     Running   0             13m
    sv-web-ui-67bfbdfc77-wwvp9                   2/2     Running   0             13m
    validator-app-667445fdfc-rcztx               2/2     Running   0             10m
    wallet-web-ui-648f86f9f9-lffz5               2/2     Running   0             10m
    ```

    另请注意，在启动期间可能会发生 `Pod` 重新启动，特别是在同时部署所有 Helm Chart 的情况下。 `participant` 运行后，`splice-sv-node` 才能启动；`postgres` 运行后，`participant` 无法启动。
  </标签>
</标签>

## SV 网络图

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/sv-network-diagram.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=d0e4f1d6ff1316b793a2f32f788ed9d5" width="600" alt="SV 网络图" data-path="images/splice/sv-network-diagram.png" />

## 配置集群入口

### 主机名和 URL

SV 运营商决定对所有 SV 主机名和 URL 遵循以下约定：* 对于 DevNet，所有主机名应采用 `<service-name>.sv-<enumerator>.dev.global.canton.network.<companyTLD>` 格式，其中：
  * `<service-name>` 是服务名称，例如 `sv`、`wallet`、`scan`
  * `<enumerator>`是同一组织运营的每个SV节点的唯一编号，从1开始，例如`sv-1` 代表组织运营的第一个节点。
  * `<companyTLD>`为SV节点运营公司的顶级域名，例如： `digitalasset.com` 数字资产。
* 对于 TestNet，所有主机名都应采用类似的格式 `<service-name>.sv-<enumerator>.test.global.canton.network.<companyTLD>`。
* 对于 MainNet，所有主机名应采用 `<service-name>.sv-<enumerator>.global.canton.network.<companyTLD>` 格式（请注意，对于 MainNet，网络名称，例如 dev/test/main 从主机名中省略）。

请注意，下面提供的参考入口图表并不完全满足这些要求，因为它们省略了主机名的 `enumerator` 部分。

### 入口配置

在 [private SV configs repo](https://github.com/global-同步器-foundation/configs-private) 中为每个相关网络（DevNet、TestNet、MainNet）维护一个 IP 白名单 json 文件 `allowed-ip-ranges.json`。此文件包含需要访问您的 SV 组件的其他集群的出口 IP。例如，它包含属于对等超级验证者和验证者的 IP。

<警告>
  为了使 SV 部署和全局同步器上的攻击面保持较小，请确保只有来自受信任 IP（白名单文件中的 IP 以及您手动验证并明确信任自己的任何 IP）的流量才能到达您的 SV 部署。
</警告>

每个 SV 都需要配置其集群入口，以允许来自这些 IP 的流量正常运行。* `https://wallet.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中的服务 `wallet-web-ui`。
* `https://wallet.sv.<YOUR_HOSTNAME>/api/validator` 应路由到 `sv` 命名空间中服务 `validator-app` 端口 5003 处的 `/api/validator`。
* `https://sv.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中的服务 `sv-web-ui`。
* `https://sv.sv.<YOUR_HOSTNAME>/api/sv` 应路由到 `sv` 命名空间中服务 `sv-app` 端口 5014 处的 `/api/sv`。
* `https://scan.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中的服务 `scan-web-ui`。
* `https://scan.sv.<YOUR_HOSTNAME>/api/scan` 应路由到 `sv` 命名空间中服务 `scan-app` 端口 5012 处的`/api/scan`。
* `https://scan.sv.<YOUR_HOSTNAME>/registry` 应路由到 `sv` 命名空间中服务 `scan-app` 端口 5012 处的`/registry`。
* `global-domain-<SERIAL_ID>-cometbft.sv.<YOUR_HOSTNAME>:26<SERIAL_ID>56` 应使用 TCP 协议路由到 `sv` 命名空间中服务 `global-domain-<SERIAL_ID>-cometbft-cometbft-p2p` 的端口 26656。请注意，cometBFT 流量纯粹是 TCP。不支持 TLS，因此无法对这些流量进行 SNI 主机路由。
* `https://cns.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中的服务 `ans-web-ui`。
* `https://cns.sv.<YOUR_HOSTNAME>/api/validator` 应路由到 `sv` 命名空间中服务 `validator-app` 端口 5003 处的 `/api/validator`。
* `https://sequencer-<SERIAL_ID>.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中服务 `global-domain-<SERIAL_ID>-sequencer` 的端口 5008。
* `https://info.sv.<YOUR_HOSTNAME>` 应路由到 `sv` 命名空间中的服务 `info`。该端点应该可以公开访问，没有任何 IP 限制。

<警告>
  为了使 SV 部署和 全局同步器 上的攻击面保持较小，请禁止与 SV 部署中的所有其他服务的入口连接。应该假设开放“任何”附加端口或服务都会带来安全风险，需要根据具体情况仔细评估。
</警告>

Internet 入口配置通常特定于正在配置的集群的网络配置和场景。为了说明 SV 节点入口的基本要求，我们提供了一个 Helm 图表，根据上面的路由配置上述集群，如下部分详细介绍。

您的 SV 节点应该配置一个指向您的 `global-domain-sequencer` 的 url，以便其他验证者可以订阅它。确保为排序器服务正确配置了集群的入口，并且可以通过提供的 URL 进行访问。要检查定序器是否可访问，我们可以使用以下命令和 [grpcurl 工具](https://github.com/fullstorydev/grpcurl) ：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl <sequencer host>:<sequencer port> grpc.health.v1.Health/Check
```

如果您使用此 Runbook 的入口配置，则 `<sequencer host>:<sequencer port>` 应为 `sequencer-SERIAL_ID.sv.YOUR_HOSTNAME:443` 请将 `YOUR_HOSTNAME` 替换为您的主机名，将 `SERIAL_ID` 替换为定序器所属同步器的序列 ID。

如果您看到下面的响应，则意味着定序器已启动并可通过 URL 进行访问。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "status": "SERVING"
}
```

### 要求

为了安装参考图表，您的集群中必须满足以下条件：

* cert-manager 必须在集群中可用（请参阅 [cert-manager 文档](https://cert-manager.io/docs/installation/helm/)）
* istio应该安装在集群中（参见[istio文档](https://istio.io/latest/docs/setup/)）

**Istio 安装示例：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-base istio/base -n istio-system --set defaults.global.istioNamespace=cluster-ingress --wait
helm install istiod istio/istiod -n cluster-ingress --set global.istioNamespace="cluster-ingress" --set meshConfig.accessLogFile="/dev/stdout"  --wait
```

### 安装说明

<标签>
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
        - '*.sv.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    创建一个名为 `istio-gateway-values.yaml` 的文件，其中包含以下内容（提示：在 GCP 上，您可以从 `gcloud compute addresses list` 获取集群 IP）：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

    在`cluster-ingress`命名空间中创建Istio网关资源。将以下内容保存到名为 `gateways.yaml` 的文件中，并进行以下修改：

    * 将 `YOUR_HOSTNAME` 替换为您的 SV 节点的实际主机名
    * 第二个网关 (cn-apps-gateway) 公开 SV 节点的 CometBFT 应用程序的三个迁移 ID（0、1 和 2）的端口。如果达到更高的迁移 ID，请使用相同的模式扩展该列表。

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
    ---
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-apps-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 26016
          name: cometbft-0-1-6-gw
          protocol: TCP
        hosts:
          # We cannot really distinguish TCP traffic by hostname, so configuring to "*" to be explicit about that
          - "*"
      - port:
          number: 26116
          name: cometbft-1-1-6-gw
          protocol: TCP
        hosts:
          - "*"
      - port:
          number: 26216
          name: cometbft-2-1-6-gw
          protocol: TCP
        hosts:
          - "*"
    ```

    并将它们应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateways.yaml -n cluster-ingress
    ```http 网关使用您上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml
    ```
  </标签>

  <Tab title="测试网 (0.6.3)">
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
        - '*.sv.YOUR_HOSTNAME'
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

    在 `cluster-ingress` 命名空间中创建 Istio Gateway 资源。将以下内容保存到名为 `gateways.yaml` 的文件中，并进行以下修改：

    * 将`YOUR_HOSTNAME`替换为您的SV节点的实际主机名
    * 第二个网关 (cn-apps-gateway) 公开 SV 节点的 CometBFT 应用程序的三个迁移 ID（0、1 和 2）的端口。如果达到更高的迁移 ID，请使用相同的模式扩展该列表。```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
    ---
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-apps-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 26016
          name: cometbft-0-1-6-gw
          protocol: TCP
        hosts:
          # We cannot really distinguish TCP traffic by hostname, so configuring to "*" to be explicit about that
          - "*"
      - port:
          number: 26116
          name: cometbft-1-1-6-gw
          protocol: TCP
        hosts:
          - "*"
      - port:
          number: 26216
          name: cometbft-2-1-6-gw
          protocol: TCP
        hosts:
          - "*"
    ```

    并将它们应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateways.yaml -n cluster-ingress
    ```

    http 网关使用您上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    创建一个`cluster-ingress`命名空间：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```确保名为 `cn-net-tls` 的密钥中有可用的证书管理器证书。合适的证书定义的示例：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.sv.YOUR_HOSTNAME'
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

    在`cluster-ingress`命名空间中创建Istio网关资源。将以下内容保存到名为 `gateways.yaml` 的文件中，并进行以下修改：

    * 将 `YOUR_HOSTNAME` 替换为您的 SV 节点的实际主机名
    * 第二个网关 (cn-apps-gateway) 公开 SV 节点的 CometBFT 应用程序的三个迁移 ID（0、1 和 2）的端口。如果达到更高的迁移 ID，请使用相同的模式扩展该列表。```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
    ---
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-apps-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 26016
          name: cometbft-0-1-6-gw
          protocol: TCP
        hosts:
          # We cannot really distinguish TCP traffic by hostname, so configuring to "*" to be explicit about that
          - "*"
      - port:
          number: 26116
          name: cometbft-1-1-6-gw
          protocol: TCP
        hosts:
          - "*"
      - port:
          number: 26216
          name: cometbft-2-1-6-gw
          protocol: TCP
        hosts:
          - "*"
    ```

    并将它们应用到您的集群：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateways.yaml -n cluster-ingress
    ```

    http 网关使用您上面配置的密钥终止 tls，并在其出站端口 443 中公开原始 http 流量。现在可以创建 Istio VirtualServices，以将流量从那里路由到集群内所需的 pod。为此提供了参考 Helm 图表，可以在之后安装

    1. 将`YOUR_HOSTNAME`替换为`splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml`并且
    2. 将同一文件中的`nameServiceDomain`设置为`"cns"`

    使用：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-sv oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n sv --version ${CHART_VERSION} -f splice-node/examples/sv-helm/sv-cluster-ingress-values.yaml
    ```
  </标签>
</标签>

## 配置集群出口以下是来自超级验证器节点的出站流量目的地的完整列表。此列表对于希望限制出口以仅允许最小必要的出站流量的 SV 很有用。 `S` 将用作`SERIAL_ID` 的简写。下表很宽 - 您可能需要垂直滚动才能看到最右边的列。

在整个操作过程中需要连接到以下目的地，以确保排序层和扫描的稳健性：

|目的地 |网址 |协议|来源吊舱 |
| ------------ | -------------------------------------------------------------------------------- | -------- | ---------------------------- |
| CometBft P2P | CometBft p2p IP 和端口 `26<S>16`、`26<S>26`、`26<S>36`、`26<S>46`、`26<S>56` | TCP | `global-domain-<S>-cometbft` |
|所有 SV 扫描 |全部从`https://scan.sv-1.<TARGET_HOSTNAME>/api/scan/v0/scans`返回 | HTTPS |扫描应用程序 |

需要从本地扫描应用程序到所有其他 SV 的扫描实例的连接，以便扫描应用程序可以以 `BFT` 方式回填其数据。将来可能还需要支持排序层的操作（CometBFT 后）。要获取所有当前扫描实例的列表，您可以查询您已知的任何扫描实例上的 `/api/scan/v0/scans` 端点。例如，使用赞助商的扫描实例（并使用 [jq](https://jqlang.org/) 进行一些可选的后处理）：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl https://scan.sv-1.<TARGET_HOSTNAME>/api/scan/v0/scans | jq -r '.scans.[].scans.[].publicUrl'
```

<div id="helm-sv-wallet-ui">
  除了上述目的地之外，SV 节点还必须能够到达其加入赞助商和所有扫描实例以加入网络：
</div>

|目的地 |网址 |协议|来源吊舱 |
| -------------------- | ------------------------------------------------------------------------------------ | -------- | ---------------------------- |
|赞助商SV | `sv.sv-1.<TARGET_HOSTNAME>:443` | HTTPS | sv-应用程序 |
| CometBft JSON RPC | `sv.sv-1.<TARGET_HOSTNAME>:443/api/sv/v0/admin/domain/cometbft/json-rpc` | HTTPS | `global-domain-<S>-cometbft` |
|赞助 SV 音序器 | `sequencer-<S>.sv-1.<TARGET_HOSTNAME>:443` | HTTPS | `participant-<S>` |
|赞助商 SV 扫描 | `scan.sv-1.<TARGET_HOSTNAME>:443` | HTTPS |验证器应用程序 |请注意，您需要替换上表中的`<TARGET_HOSTNAME>`和`sv-1`以匹配您的SV入职赞助商的地址。另请注意，CometBft JSON RPC 的地址是在`cometbft-values.yaml`（在`stateSync.rpcServers` 下）中配置的。任何入职 SV 都可以充当 SV 入职发起人。

一般来说，仅在 SV 加入期间才需要连接到赞助商 SV（扫描之外）。在加入后的有限过渡时间内也需要连接到赞助商 SV 定序器，在此期间新加入的 SV 定序器尚未准备好使用（当前全局同步器配置为 60 秒）。

## 登录钱包界面

部署入口后，打开浏览器 [https://wallet.sv.YOUR\_HOSTNAME](https://wallet.sv.YOUR_HOSTNAME) 并使用您之前配置为 `validatorWalletUser` 的用户凭据登录。随着挖矿轮次每 2.5 分钟进行一次，您将能够看到您的余额增加，并且您将在交易历史记录中看到 `sv_reward_collected` 条目。登录后，应该会看到交易页面。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/wallet_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=7df40cdc3f81b03dcb50ce9175c7e280" width="600" alt="登录钱包界面后" data-path="images/splice/wallet_home.png" />

## 登录 CNS UI

您可以打开浏览器 [https://cns.sv.YOUR_HOSTNAME](https://cns.sv.YOUR_HOSTNAME) 并使用您之前配置为 `validatorWalletUser` 的用户凭据登录。您将能够在 Canton Name Service 上注册一个名称。

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/ans_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0084097a0e8f4d5d73d901049a71b3c3" width="600" alt="登录 CNS UI 后" data-path="images/splice/ans_home.png" />

## 登录 SV UI

打开浏览器 [https://sv.sv.YOUR_HOSTNAME](https://sv.sv.YOUR_HOSTNAME) 以登录 SV Operations 用户界面。您可以使用`validatorWalletUser`的凭证登录。这些凭据与您用于上面钱包登录的凭据相同。请注意，只有超级验证者才能登录。登录后，您应该会看到一个包含一些 SV 集体信息的页面。

<img src="https://mintcdn.com/cantonfoundation/Ps1aWN9aLFijpT3F/images/splice/sv_home.png?fit=max&auto=format&n=Ps1aWN9aLFijpT3F&q=85&s=e5f24d59975c2666f3bc745888d1a06b" width="600" alt="登录 sv UI 后" data-path="images/splice/sv_home.png" />SV UI 还提供了 CometBFT 节点的一些有用的调试信息。要查看它，请单击“CometBFT 调试信息”选项卡。如果您的 CometBFT 配置正确，并且它与所有其他节点都有连接，您应该看到 `n_peers` 等于 DSO 的大小，不包括您自己的节点，并且您应该看到所有对等 SV 列为对等点（它们的人类友好名称将列在 `moniker` 字段中）。

<div id="sv-ui-global-domain">
  SV UI 还显示全局同步器节点的状态。要查看它，请单击“域节点状态”选项卡。
</div>

## 关注 Amulet 转化率 Feed

每个 SV 都可以在 SV UI 中选择他们想要设置的护身符转换率。然后将每轮挖矿的转化率选择为所有 SV 公布的转化率的中位数。

还可以配置 SV 应用程序以遵循给定发布商提供的转化率 Feed，而不是通过 SV UI 手动更新转化率。

为此，请将以下内容添加到 SV 应用程序的环境变量中：

这将自动从`publisher::namespace`方发布的`#splice-amulet-name-service:Splice.Ans.AmuletConversionRateFeed:AmuletConversionRateFeed`合约中获取兑换率，并将SV的配置设置为发布者的最新汇率。如果发布的速率超出可接受的范围，则会记录警告，并将发布的速率限制在配置的范围内。

请注意，SV 在更新其速率之间必须等待`voteCooldownTime`（默认为 1 分钟的治理参数）。因此，发布者所做的更新不会立即传播。

```
- name: ADDITIONAL_CONFIG_FOLLOW_AMULET_CONVERSION_RATE_FEED
  value: |
    canton.sv-apps.sv.follow-amulet-conversion-rate-feed {
      publisher = "publisher::namespace"
      accepted-range = {
        min = 0.01
        max = 100.0
      }
    }
```

[^1]：该 URL 必须可从集群中运行的 Canton 参与者、验证器应用程序和 SV 应用程序以及所有能够与 SV 和钱包 UI 交互的 Web 浏览器访问。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
