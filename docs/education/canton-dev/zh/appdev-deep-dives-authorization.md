---
title: "授权"
slug: "appdev-deep-dives-authorization"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/authorization.md"
source_title: "Authorization"
tags:
  - appdev
  - deep-dives
  - authorization
---

# 授权

> Canton Ledger API 的访问令牌、身份提供方、作用域与权限。

使用 SDK 工具开发 Daml 应用时，本地环境通常**不会**对 Ledger API 请求做授权——默认任何有效的 Ledger API 请求都会被 sandbox 接受。

已部署账本的 participant 节点则不同：每个 Ledger API 请求都会检查是否包含有效且足以授权该请求的访问令牌。因此对接已部署账本时，应用需支持基于访问令牌的授权。

<Note>
  在双向 TLS（mTLS）认证场景下，Ledger API 客户端除访问令牌外还须向服务端出示证书。证书须由 Ledger API 服务端信任的 CA 签发。注意：此方法**不能**证明应用身份，即请求中的 `application_id` 字段未必与证书 CN（Common Name）对应。
</Note>

## 基本交互

Daml 应用向 participant 暴露的 Ledger API 发送请求，以变更账本（例如「以 Party Alice 对合约 Y 行使 choice X」）或读取数据（例如「读取 Party Alice 可见的全部活跃合约」）。

participant 节点**能否**处理请求，取决于是否托管相关 Party，以及请求是否符合 Daml Ledger Model。**是否愿意**向应用提供服务，则取决于请求是否包含对该 participant 有效且足以授权的访问令牌。

## 获取与使用访问令牌

应用如何获取访问令牌取决于所连接的 participant 及其运营方配置，常见流程类似 [OAuth 2.0](https://oauth.net/2/)。

在此场景下，Daml 应用先向令牌颁发方获取访问令牌。颁发方验证应用身份、查询其权限，并生成描述这些权限的签名访问令牌。

令牌颁发后，Daml 应用在每个 Ledger API 请求中附带该令牌。账本会验证：

* 令牌由受信任的颁发方签发
* 令牌未被篡改
* 令牌未过期
* 令牌所载权限足以授权该请求

<img src="https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/appdev/deep-dives/images/Authentication.svg?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=8952d9ce94318681921618e798ffd2cb" alt="说明上文两段认证流程的流程图。" width="712" height="468" data-path="appdev/deep-dives/images/Authentication.svg" />

如何将令牌附加到请求取决于你使用的 Ledger API 工具或库，请参阅其文档。（例如通过 Java 绑定访问 gRPC Ledger API，或使用 JSON Ledger API。）

## 访问令牌格式

应用应将访问令牌视为不透明数据。但作为开发者，了解令牌格式有助于调试。

所有 Daml 账本将访问令牌表示为 [JSON Web Token（JWT）](https://datatracker.ietf.org/doc/html/rfc7519)。

<Note>
  测试用途可在 [jwt.io](https://jwt.io/) 网站生成访问令牌。
</Note>

## 访问令牌与权限（Rights）

访问令牌包含授予持有者的权限信息，具体因所访问 API 而异。

Ledger API 使用以下 rights 控制请求授权：

* `public`：读取公开信息（如账本标识）
* `participant_admin`：管理 participant 节点
* `idp_admin`：管理与已认证用户同一身份提供方配置下的用户与 Party
* `canReadAs(p)`：读取 Party `p` 在账本上的可见信息（如活跃合约）
* `canActsAs(p)`：同 `canReadAs(p)`，并可代表 Party `p` 提交命令

下表汇总访问各 Ledger API 端点所需权限：

| Ledger API 服务 | 端点 | 所需权限 |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| StateService | GetActiveContracts | 对每个请求的 Party p：`canReadAs(p)` |
| CommandCompletionService | CompletionEnd | `public` |
| | CompletionStream | 对每个请求的 Party p：`canReadAs(p)` |
| CommandSubmissionService | Submit | 对提交方 Party p：`canActAs(p)` |
| CommandService | All | 对提交方 Party p：`canActAs(p)` |
| EventQueryService | All | 对每个请求 Party p：`canReadAs(p)` |
| Health | All | 健康检查无需访问令牌 |
| IdentityProviderConfigService | All | `participant_admin` |
| PackageService | All | `public` |
| PackageManagementService | All | `participant_admin` |
| PartyManagementService | All | `participant_admin` |
| | All（除 GetParticipantId、UpdatePartyIdentityProviderId） | `idp_admin` |
| ParticipantPruningService | All | `participant_admin` |
| ServerReflection | All | gRPC 服务反射无需访问令牌 |
| TimeService | GetTime | `public` |
| | SetTime | `participant_admin` |
| UpdateService | LedgerEnd | `public` |
| | All（除 LedgerEnd） | 对每个请求的 Party p：`canReadAs(p)` |
| UserManagementService | All | `participant_admin` |
| | All（除 UpdateUserIdentityProviderId） | `idp_admin` |
| | GetUser | 已认证用户可获取自己的用户 |
| | ListUserRights | 已认证用户可列出自己的权限 |
| VersionService | All | `public` |

## 用户访问令牌

participant 节点维护动态用户集及其权限。用户访问令牌编码代表其发出请求的 participant 用户。

处理此类请求时，participant 会先查询该用户当前权限，再按上表检查授权。因此可通过 participant 用户管理服务**动态**调整应用权限，**无需**重新签发访问令牌。

用户访问令牌为遵循 [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) 的 [JWT](https://datatracker.ietf.org/doc/html/rfc7519)。有两种 JSON 编码：基于 audience 的格式（用 `aud` 指定面向特定 Daml participant），以及基于 scope 的格式（用 `scope` 指定用途）。两者可互换；若可能，优先使用基于 audience 的格式，因其与更多 IAM 兼容（例如 Kubernetes 不支持设置 scope 字段，且会强制 participant id，防止令牌被误用于其他 participant）。

### 基于 Audience 的令牌

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "aud": "https://daml.com/jwt/aud/participant/someParticipantId",
   "sub": "someUserId",
   "iss": "someIdpId",
   "exp": 1300819380
}
```

字段含义：

* `aud`（必填）：将令牌限制于指定 ID 的 participant（如 `someParticipantId`）
* `sub`（必填）：participant 用户 ID
* `iss`：身份提供方 ID
* `exp`（可选）：JWT 过期时间（自 EPOCH 起的秒数）

### 基于 Scope 的令牌

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "aud": "someParticipantId",
   "sub": "someUserId",
   "exp": 1300819380,
   "iss": "someIdpId",
   "scope": "daml_ledger_api"
}
```

字段含义：

* `aud`（可选）：限制于指定 ID 的 participant
* `sub`（必填）：participant 用户 ID
* `iss`：身份提供方 ID
* `exp`（可选）：过期时间（秒）
* `scope`：空格分隔的 [OAuth 2.0 scope](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3) 列表，须包含 `"daml_ledger_api"`

### 用户 ID 要求

用户 ID 须为非空字符串，最长 128 字符，且为字母数字 ASCII 或以下符号之一：`@^$.!\`-#+'~_|:()`。

### 身份提供方

身份提供方配置可理解为一组 participant 用户，其特点为：

* 有既定方式验证其访问令牌
* 可与同 participant 上其他用户隔离管理
* 在每个 participant 上拥有唯一的身份提供方 ID
* 关联一组共享同一身份提供方 ID 的 Party

participant 始终有静态配置的默认身份提供方，其 ID 为空字符串 `""`。此外，可通过 `IdentityProviderConfigService` 配置少量非默认身份提供方，需提供非空身份提供方 ID 与 [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517) URL，供 participant 获取验证令牌所需的密钥数据。

以非默认身份提供方用户认证时，访问令牌须包含与身份提供方 ID 匹配的 `iss` 字段。默认身份提供方下，`iss` 可为空或省略。

## 编码与签名

符合 JWT 规范的访问令牌嵌入更大的 JSON 结构中，含独立 header 与 payload。

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "alg": "RS256",
   "typ": "JWT"
}
{
   "aud": "https://daml.com/jwt/aud/participant/someParticipantId",
   "sub": "someUserId",
   "iss": "someIdpId",
   "exp": 1300819380
}
```

二者经 base64 编码形成令牌主体（stem），再按 header 中的算法签名，签名同样 base64 编码后附加到 stem，最终字符串形态类似：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2RhbWwuY29tL2p3dC9hdWQvcGFydGljaXBhbnQvc29tZVBhcnRpY2lwYW50SWQiLCJzdWIiOiJzb21lVXNlcklkIiwiaXNzIjoic29tZUlkcElkIiwiZXhwIjoxMzAwODE5MzgwfQ.DLVPehRLt8WiddI6mwUU1lqIgRbysLK34mgkuzSDQTThCXlEY_S57SHKEQHw-Pai0Y0OeGP7wNsT6uq51vBVbRNfxOLwy5owQRm3LEeTbSXMjnnPVrtRrhelVQCsH2AcV4J4bbrAe6YfKGYFBXZOfeRL3Gy7KIplcfxDZekHdPD8lhwK8AkvAR4IaOX72Q5jhjB2yOY9IwpVxx-pN0vWCqmxTbQqnIpSGo185Y0f38nKZeofGT5jcJZaSv7z4Ks15gs9gm1pHorEL6TZLCbX7T064hQeTBFea-kxQlUkcfcgmUOMAmA05_4a8fdFz2uHq5km7ylp6pUITogN5MJ-_CVFEwOD0GveOgiUJBBMHDBjq_V_DfRE4nZ04tFQ0DDthWpMd0F59JFIhmjZSZT9DWppj6G7VBWpu9aIFPefyX--2U_aO0Smt_dBBV5A6pvbIgX6ITF2tjEvvOCLHtLKmNTlP8cclna70DCsDIrojNVDMFpLXYLvsP6DhQWkGaRb-nz0hLjQE_PtuQzSexrZG5d8tHFS351E2-aUVTKoJuEGHH3n1it-d9yHdt4fAynIbhWUVAervxc-oXyrA3-uafrxbIiQCpnw0kQ8K-HwJpkfz_Yqf-luI1FaRiPT9F-cYzwvceNf2_2hhmiuGiYp3rVIPwkFAuBc1vgpPiWSNLc
```

注意：正确格式的访问令牌生成通常委托给身份提供方系统，客户端开发者一般无需直接处理。

## 令牌过期

基于 JWT 的授权本质无状态，扩展性好且服务端无需维护客户端会话或昂贵的声明校验。但这也意味着 JWT **无法撤销**。

为降低令牌丢失或被盗风险，我们**强烈建议**遵循 JWT 系统的标准做法：在 IAM 中配置**短生命周期**令牌，理想为 5–15 分钟，以限制未授权访问的时间窗口。

使用长生命周期令牌违背最佳实践；令牌泄露后可能需要代价高昂的 IAM 重配。丢失令牌可能导致轮换签名密钥，通过 JWKS 机制使所有未过期令牌失效。请参阅 IAM 文档了解缓解 JWT 被盗的策略。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
