---
title: "Okta 与 Keycloak OIDC 配置"
slug: "global-synchronizer-deployment-oidc-providers"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/oidc-providers.md"
source_title: "Okta and Keycloak OIDC Configuration Guide"
tags:
  - global-synchronizer
  - deployment
  - oidc-providers
---

# Okta 与 Keycloak OIDC 配置

> Canton 验证者 OIDC 认证：Okta 与 Keycloak 配置 walkthrough。

> 部署 Canton Network 验证器节点时 Okta 和 Keycloak 的 OIDC 提供商分步设置演练。

<警告>
  本节介绍社区成员分享的解决方案。
  虽然它们还没有经过 Splice 维护者的正式测试，
  鼓励用户独立验证信息。
  我们始终欢迎为提高准确性和完整性做出贡献。
</警告>

要部署验证器节点，请使用您的首选 OIDC 提供商配置身份验证。
本部分提供 Okta 和 Keycloak 的说明。
有关 Auth0 说明和配置身份验证的更多详细信息，请参阅[配置身份验证](/global-同步器/deployment/installation#configuring-authentication)。

感谢 Stéphane Loeuillet 在[社区讨论](https://github.com/global-同步器-foundation/docs/discussions/15#discussioncomment-12877002)中提供的意见，这构成了本文档中 Okta 部分的基础。

## 奥克塔

请按照以下步骤将 Okta 配置为验证者的 OIDC 提供商：

1. 为验证器应用程序后端创建一个应用程序。

   一个。导航至“管理面板 > 应用程序 > 应用程序”，然后单击“创建应用程序集成”。
   b.选择“API 服务”作为登录方法（不是 OIDC）。
   c.对于“应用程序集成名称”，输入 `Validator app backend`。
   d.在常规设置中，取消选中“拥有证明”。
   e.单击“保存”并复制“客户端 ID”和“客户端密钥”。

2. 为钱包 Web UI 创建应用程序。

   一个。导航至“管理面板 > 应用程序 > 应用程序”，然后单击“创建应用程序集成”。
   b.选择“OIDC”作为登录方法，然后选择“单页应用程序”作为应用程序类型。
   c.对于“应用程序集成名称”，输入 `Wallet web UI`。

   * 在“登录重定向 URI”中，输入您的钱包 UI URL：`https://wallet.validator.YOUR_HOSTNAME`
   * 在“注销重定向 URI”中，输入您的钱包 UI URL：`https://wallet.validator.YOUR_HOSTNAME`
   * 在“Trusted Origins/Base URIs”中，输入您的钱包 UI URL：`https://wallet.validator.YOUR_HOSTNAME`

   d.将应用程序分配给您想要访问它的组。
   e.单击“保存”并复制“客户端 ID”。

3. 为 CNS Web UI 创建应用程序。

   一个。导航至“管理面板 > 应用程序 > 应用程序”，然后单击“创建应用程序集成”。
   b.选择“OIDC”作为登录方法，然后选择“单页应用程序”作为应用程序类型。
   c.对于“应用程序集成名称”，输入 `CNS web UI`。

   * 在“登录重定向 URI”中，输入您的 CNS UI URL：`https://cns.validator.YOUR_HOSTNAME`
   * 在“注销重定向 URI”中，输入您的 CNS UI URL：`https://cns.validator.YOUR_HOSTNAME`
   * 在“可信来源/基本 URI”中，输入您的 CNS UI URL：`https://cns.validator.YOUR_HOSTNAME`d.将应用程序分配给您想要访问它的组。
   e.单击“保存”并复制“客户端 ID”。

4. 为自定义受众创建客户端（可选）

   a.如果您希望其他应用程序访问账本 API，请按照步骤 1-3 创建一个额外的客户端。

5.为每个验证器/环境创建一个自定义授权服务器

   a.导航至“管理面板 > 目录 > 群组”，单击“添加群组”并将群组命名为“canton\_wallet\_admin”。
   b.添加另一个组“canton\_all”。
   c.导航至“管理面板 > 安全 > API”
   d.在“授权服务器”选项卡中，单击“添加授权服务器”。定义名称和受众。请注意，授权服务器用于 M2M 流程，出于安全原因，每个环境/验证器的授权服务器必须不同。
   e.在“范围”选项卡中，添加名为 `daml_ledger_api` 的自定义范围，然后单击“设置为默认范围”。
   f.在“Claims”选项卡中，将“sub”值更改为“app.clientId”。如果保留默认值，它将使用用户电子邮件，这需要在values.yaml中格式化为`' " email.address@domain " '`，不带空格。在更新 Helm 图表以正确引用它们之前，这是必要的。
   g。在“访问策略”选项卡中，为三个应用程序中的每一个创建一个策略。

   * 名称：`Validator app backend`

   * 分配给：在步骤 #1 中创建的`Validator app backend`

   * 单击“添加规则”。输入“规则名称”并选中“用户是”旁边的“分配该应用程序的任何用户”，以定义与分配给该应用程序的任何用户相匹配的规则。单击“创建规则”。

   * 姓名：`Wallet web UI`

   * 分配给：在步骤 #2 中创建的`Wallet web UI`

   * 单击“添加规则”。输入“规则名称”并选中“用户是”旁边的“已分配应用程序和以下之一的成员”。添加组“canton\_wallet\_admin”以定义与该组匹配的规则。单击“创建规则”。

   * 名称：`CNS web UI`

   * 分配给：在步骤 #3 中创建的`CNS web UI`

   * 单击“添加规则”。输入“规则名称”并选中“用户是”旁边的“已分配应用程序和以下之一的成员”。添加组“canton\_all”以定义与该组匹配的规则。单击“创建规则”。

## 钥匙斗篷

请按照以下步骤将 Keycloak 配置为验证者的 OIDC 提供程序：

1. 创建领域

   a.导航至“管理面板 > 管理领域”，单击“创建领域”，然后输入领域名称。

2. 为Ledger API创建客户端一个。导航至“管理面板 > 客户端”，然后单击“创建客户端”。
   b.将客户端类型设置为“OpenID Connect”，输入`ledger-api`作为客户端ID，然后单击“下一步”。
   c.在“功能配置”中，取消选中所有字段，然后单击“下一步”。
   d.在“登录设置”中，将“有效重定向 URI”和“Web 来源”字段留空，然后单击“保存”。
   e.导航到“管理面板 > 客户端范围”选项卡，然后单击“创建客户端范围”。
   f.输入`daml_ledger_api`作为名称并选择类型“默认”。
   g。在“映射器”选项卡中，单击“配置新映射器”。
   h.选择“User Client Role”作为映射器类型并将其命名为`daml_ledger_api_scope`。启用“添加到访问令牌”并禁用所有其他选项，例如“添加到 ID 令牌”、“添加到用户信息”和“添加到令牌内省”。单击“保存”。
   我。要将此范围添加到 `ledger-api` 客户端，请导航至“管理面板 > 客户端 > ledger\_api > 客户端范围”，然后单击“添加客户端范围”。选择`daml_ledger_api`，然后单击“添加”，类型为“默认”。
   j。导航到“管理面板 > 领域设置 > 会话”，并确保启用“离线会话最大限制”，并为“离线会话最大”设置足够的值。这将启用刷新令牌，类似于 Auth0 中的“允许离线访问”。单击“保存”。

3. 为自定义受众创建客户端（可选）

   a.如果您的后端服务需要不同的受众，请创建另一个客户端，并将“客户端 ID”设置为 `validator-app-api`（例如，`https://validator.example.com/api`），并可选择按照步骤 #2 中所述定义自定义客户端范围以区分此 API。

4. 为验证器应用程序后端创建客户端。

   一个。导航至“管理面板 > 客户端”，然后单击“创建客户端”。
   b.将客户端类型设置为“OpenID Connect”，输入`validator-app-backend`作为客户端ID，然后单击“下一步”。
   c.在“能力配置”中，仅勾选“客户端身份验证”和“服务帐户”。单击“下一步”。
   d.在“登录设置”中，将“有效重定向 URI”和“Web 来源”字段留空，然后单击“保存”。
   e.从“设置”选项卡复制“客户端 ID”，并从“凭据”选项卡复制“客户端密钥”。 Keycloak 中的客户端 ID 是创建时分配给客户端的名称 (`validator-app-backend`)。

5. 为钱包 Web UI 创建客户端。

   一个。导航至“管理面板 > 客户端”，然后单击“创建客户端”。
   b.将客户端类型设置为“OpenID Connect”，输入`wallet-web-ui`作为客户端ID，然后单击“下一步”。
   c.在“能力配置”中，只勾选“标准流程”，点击“下一步”。
   d.在“登录设置”中设置：*“有效重定向 URI”至：`https://wallet.validator.YOUR_HOSTNAME/*`
   *“有效的注销后重定向 URI”至：`https://wallet.validator.YOUR_HOSTNAME`
   *“网络起源”至：`https://wallet.validator.YOUR_HOSTNAME`
   * 单击“保存”。

   e.从“设置”选项卡 (`wallet-web-ui`) 复制“客户端 ID”。

6. 为 CNS Web UI 创建客户端。

   一个。按照与钱包 Web UI 相同的步骤，使用 `cns-ui` 作为“客户端 ID”，设置：

   *“有效重定向 URI”至：`https://cns.validator.YOUR_HOSTNAME/*`
   *“有效的注销后重定向 URI”至：`https://cns.validator.YOUR_HOSTNAME`
   *“网络起源”至：`https://cns.validator.YOUR_HOSTNAME`

   b.从“设置”选项卡 (`cns-ui`) 复制“客户端 ID”。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
