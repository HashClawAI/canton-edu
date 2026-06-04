---
title: "社区 Keycloak 配置"
slug: "global-synchronizer-deployment-community-keycloak-config"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/community-keycloak-config.md"
source_title: "Keycloak Configuration Guide for Canton Validator (Community)"
tags:
  - global-synchronizer
  - deployment
  - community-keycloak-config
---

# 社区 Keycloak 配置

> Canton 验证者 Keycloak 认证配置指南（社区）。

> 社区贡献的 Canton 验证器端到端 Keycloak 配置指南

<Warning>
  This section features solutions shared by community members. While they haven't been formally tested by the Splice maintainers, users are encouraged to verify the information independently. Contributions to enhance accuracy and completeness are always welcome.
</Warning>

要部署具有 Keycloak 身份验证的验证器节点，请按照以下详细配置步骤操作。本指南提供了有关将 Keycloak 设置为验证者的 OIDC 提供商的全面说明，包括 Canton 网络部署所需的所有自定义设置。

有关其他身份验证提供程序和配置详细信息，请参阅配置身份验证。

## 先决条件

在继续配置之前，请确保您拥有：

* 具有管理访问权限的正在运行的 Keycloak 实例
* 管理控制台访问您的 Keycloak 部署
* 配置以下主机名：
  * 验证器 API 基本 URL：`https://validator-api.your-domain.example/api`
  * 钱包界面：`https://wallet.your-domain.example`
  *中枢神经系统用户界面：`https://cns.your-domain.example`
* Canton 网络为您分配的 `PARTY_HINT` 标识符

## 领域配置

1. 为您的 Canton 验证器创建领域。
   1. 导航到 **管理控制台** → **管理领域** → **创建领域**。
   2. 将 **领域名称** 设置为 `canton`（或您的环境特定名称）。
   3. 单击“**创建**”以初始化领域。
2. 配置离线访问和刷新令牌的会话设置。
   1. 导航到 **领域设置** → **会话**。
   2. 配置以下设置：
      * 将 **离线会话最大限制** 设置为 `ON`
      * 将 **离线会话最大值** 设置为 `5,184,000` 秒（60 天；根据需要调整）
      * 将 **离线会话空闲超时** 设置为 `2,592,000` 秒（30 天；根据需要调整）
   3. 单击“**保存**”应用更改。

## 客户端范围设置

3. 创建 `daml_ledger_api` 客户端范围。
   1. 导航到 **客户端范围** → **创建**。

   2. 配置基本设置：

      * **姓名**：`daml_ledger_api`
      * **协议**：`OpenID Connect`
      * **类型**：`Default`
      * **在同意屏幕上显示**：`OFF`
      * **包含在代币范围内**：`OFF`

   3. 单击**保存**。

   4. 将所需的映射器添加到`daml_ledger_api`：

      **用户客户端角色映射器：**

      * 导航到 **daml\_ledger\_api** → **映射器** → **创建**
      * 将**映射器类型**设置为`User Client Role`
      * 将**名称**设置为`daml_ledger_api_scope`
      * 设置**添加访问令牌**为`ON`
      * 将**添加到ID令牌**、**添加到用户信息**、**添加到令牌内省**和**多值**设置为`OFF`
      * 点击**保存**

      **受众映射器：**

      * 导航到 **daml\_ledger\_api** → **映射器** → **创建**
      * 将**映射器类型**设置为`Audience`
      * 将**名称**设置为`audience`
      * 将 **包含的自定义受众** 设置为 `https://canton.network.global`
      * 将**添加到访问令牌**和**添加到令牌内省**设置为`ON`
      * 将**添加到ID令牌**和**添加到轻量级访问令牌**设置为`OFF`
      * 点击**保存**
4. 创建`openid`客户端范围。
   1. 导航到 **客户端范围** → **创建**。

   2. 配置设置：

      * **姓名**：`openid`
      * **协议**：`OpenID Connect`
      * **类型**：`Default`
      * **在同意屏幕上显示**：`OFF`
      * **包含在代币范围内**：`ON`

   3. 单击**保存**。4. 将所需的映射器添加到`openid`：

      **验证器 API 受众映射器：**

      * 导航到 **openid** → **映射器** → **创建**
      * 将 **映射器类型** 设置为 `Audience`
      * 将**名称**设置为`aud`
      * 将 **包含的自定义受众** 设置为 `https://validator-api.your-domain.example/api`
      * 将**添加到访问令牌**和**添加到令牌内省**设置为`ON`
      * 将**添加到ID令牌**和**添加到轻量级访问令牌**设置为`OFF`
      * 点击**保存**

      **主题映射器：**

      * 导航到 **openid** → **映射器** → **创建**
      * 将 **映射器类型** 设置为 `Subject (sub)`
      * 将**名称**设置为`sub`
      * 将**添加到访问令牌**和**添加到令牌内省**设置为`ON`
      * 将**添加到轻量级访问令牌**设置为`OFF`
      * 点击**保存**

## 客户端配置

5. 创建账本API资源客户端。
   1. 导航到 **客户端** → **创建客户端**。
   2. 将**客户端类型**设置为`OpenID Connect`，将**客户端ID**设置为`ledger-api`。
   3. 单击**下一步**。
   4. 在**功能配置**中，将所有开关设置为`OFF`。
   5. 单击**下一步**。
   6. 将所有 **登录设置** 字段留空，然后单击 **保存**。
   7. 添加客户端范围：导航到 **客户端范围** → **添加客户端范围** → 选择 `daml_ledger_api` → **添加为“默认”**。
6. 创建验证器应用程序后端服务帐户客户端。
   1. 导航到 **客户端** → **创建客户端**。
   2. 将**客户端类型**设置为`OpenID Connect`，将**客户端ID**设置为`validator-app-backend`。
   3. 单击**下一步**。
   4. 在**能力配置**中：
      * 将**客户端身份验证**设置为`ON`
      * 将**服务帐户**设置为`ON`
      * 将所有其他选项设置为`OFF`
   5. 单击**下一步**。
   6. 将**登录设置**字段留空，然后单击**保存**。
   7. 记录凭据：
      * 从 **Credentials 选项卡**，复制 **Client Secret**
      * 从 **服务帐户角色选项卡**，单击服务帐户用户链接
      * 从浏览器 URL 复制 **用户 ID (UUID)**（用作 `LEDGER_API_ADMIN_USER`）
   8. 添加客户端范围：导航到 **客户端范围** → **添加客户端范围** → 选择 `daml_ledger_api` → **添加为“默认”**。
7. 创建钱包 Web UI 公共客户端。
   1. 导航到 **客户端** → **创建客户端**。
   2. 将**客户端类型**设置为`OpenID Connect`，将**客户端ID**设置为`wallet-web-ui`。
   3. 单击**下一步**。
   4. 在**能力配置**中：
      * 将**标准流量**设置为`ON`
      * 将所有其他选项设置为`OFF`
   5. 单击**下一步**。
   6. 配置**登录设置**：
      * **有效的重定向 URI**： `https://wallet.your-domain.example/*`
      * **有效的注销后重定向 URI**： `https://wallet.your-domain.example`
      * **网络来源**：`https://wallet.your-domain.example`
   7. 单击“**保存**”。
   8. 配置客户端范围：
      * 添加 `openid` 和 `daml_ledger_api` 作为 **“默认”**
      * 添加 `offline_access` 作为 **“可选”**（如果需要）
8. 创建 CNS UI 公共客户端。
   1. 按照与钱包 Web UI 相同的流程进行以下修改：
      * 将 **客户端 ID** 设置为 `cns-ui`
      * 将 **有效的重定向 URI** 设置为 `https://cns.your-domain.example/*`
      * 将 **有效的注销后重定向 URI** 设置为 `https://cns.your-domain.example`
      * 将 **Web 来源** 设置为 `https://cns.your-domain.example`
      * 配置与 wallet-web-ui 相同的客户端范围

## 用户管理9. 创建运营商钱包用户。
   1. 导航至 **用户** → **添加用户**。
   2.配置用户：
      * 将 **用户名** 设置为您的确切 `PARTY_HINT` 值
      * 将 **用户启用** 设置为 `ON`
   3. 单击**保存**。
   4. 设置永久密码：导航至 **凭据选项卡** → 设置密码，并将 **临时** 设置为 `OFF`。
   5. 从浏览器 URL 复制 **用户 ID (UUID)**（用作 `WALLET_ADMIN_USER`）。

<Warning>
  The username must exactly match your assigned `PARTY_HINT` identifier from the Canton network.
</Warning>

## 应用程序配置

使用以下与 Keycloak 相关的环境变量配置验证器应用程序：

# Keycloak 领域端点

AUTH\_URL=[https://your-keycloak-host/realms/canton](https://your-keycloak-host/realms/canton)
AUTH\_WELLKNOWN\_URL=[https://your-keycloak-host/realms/canton/.well-known/openid-configuration](https://your-keycloak-host/realms/canton/.well-known/openid-configuration)
AUTH\_JWKS\_URL=[https://your-keycloak-host/realms/canton/protocol/openid-connect/certs](https://your-keycloak-host/realms/canton/protocol/openid-connect/certs)

# 后端客户端凭据

VALIDATOR\_AUTH\_CLIENT\_ID=validator-app-backend
验证者\_AUTH\_CLIENT\_SECRET=替换\_WITH\_CLIENT\_SECRET

# 用户身份 UUID（来自 Keycloak 用户 URL）

LEDGER\_API\_ADMIN\_USER=替换\_WITH\_SERVICE\_ACCOUNT\_USER\_UUID
钱包\_ADMIN\_USER=替换\_WITH\_OPERATOR\_USER\_UUID

# OAuth 范围和受众

LEDGER\_API\_AUTH\_SCOPE=daml\_ledger\_api
LEDGER\_API\_AUTH\_AUDIENCE=[https://canton.network.global](https://canton.network.global)
VALIDATOR\_AUTH\_AUDIENCE=[https://validator-api.your-domain.example/api](https://validator-api.your-domain.example/api)

# UI 客户端 ID

WALLET\_UI\_CLIENT\_ID=wallet-web-ui
ANS\_UI\_CLIENT\_ID=cns-ui

## 验证和测试

10. 通过测试后端客户端凭据流程来验证您的配置：

    curl -X POST "[https://your-keycloak-host/realms/canton/protocol/openid-connect/token](https://your-keycloak-host/realms/canton/protocol/openid-connect/token)" \
    -H“内容类型：application/x-www-form-urlencoded”\
    -d "grant\_type=client\_credentials" \
    -d "client\_id=validator-app-backend" \
    -d“客户端\_秘密=您的\_客户端\_秘密”

    解码返回的`access_token`并验证其包含：

    * `aud`: `["https://canton.network.global"]`
    * `scope`: `"daml_ledger_api"`

## 配置注意事项

<Note>
  * **User Identifiers**: Both `LEDGER_API_ADMIN_USER` and `WALLET_ADMIN_USER` must be UUIDs from Keycloak URLs, not usernames
  * **Mapper Configuration**: The `daml_ledger_api` scope uses both User Client Role and Audience mappers for comprehensive authorization
  * **Token Audiences**: UI tokens contain both standard OpenID Connect claims and your validator API audience
  * **Username Matching**: The wallet admin user's username must exactly match your `PARTY_HINT` value
</Note>

## 故障排除

如果您遇到身份验证问题：

* 验证所有受众映射是否已正确配置
* 确保客户端范围被正确分配为“默认”类型
* 确认用户 UUID 是从 Keycloak URL 复制的，而不是使用用户名
* 检查会话超时值是否适合您的用例

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
