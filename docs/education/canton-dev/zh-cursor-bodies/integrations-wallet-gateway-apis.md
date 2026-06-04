> 钱包 Gateway dApp API and 用户 API reference

钱包 Gateway exposes two JSON-RPC 2.0 APIs: one for dApps interactions and one for 用户 interactions. Both APIs use the same base URL but different paths.

## API 端点

* **dApp API**: `/api/v0/dapp` - Used by decentralized 应用 to interact with wallets and submit 交易
* **用户 API**: `/api/v0/用户` - Used by 用户 to manage wallets, networks, and signing 提供方

Both APIs follow the JSON-RPC 2.0 specification and use JWT-based 认证 for secure access.

## dApp API 参考

The dApp API enables decentralized 应用 to connect to wallets, query ledger state, prepare 交易, and submit 命令. This API is designed for programmatic access from web or mobile 应用.

**认证:**

The dApp API requires a valid JWT token in the `授权` header:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
Authorization: Bearer <jwt-token>
```

**Full API Specification:**

The complete OpenRPC specification is available at [openrpc-dapp-api.json](https://github.com/canton-网络/钱包-gateway/blob/main/api-specs/openrpc-dapp-api.json).

## 用户 API 参考

The 用户 API enables 用户 to manage their wallets, configure networks, manage identity 提供方, create Party, and interact with their 钱包 through the web UI.

**方法:**

| 类别           | 方法                 | 说明                                                         |
| ------------------ | ---------------------- | ------------------------------------------------------------------- |
| 会话           | `addSession()`         | 创建 a new 会话 (unauthenticated, used for initial connection) |
|                    | `removeSession()`      | End the current 会话                                             |
|                    | `listSessions()`       | 列出 会话 for the current 用户                                  |
| Networks           | `listNetworks()`       | 列出 all configured networks                                        |
|                    | `addNetwork()`         | 添加 a new 网络 配置                                     |
|                    | `removeNetwork()`      | 移除 a 网络 配置                                      |
| Identity 提供方 | `listIdps()`           | 列出 all identity 提供方                                         |
|                    | `addIdp()`             | 添加 a new identity 提供方                                         |
|                    | `removeIdp()`          | 移除 an identity 提供方                                         |
| Wallets            | `createWallet()`       | 创建 a new 钱包 (party) on a 网络                            |
|                    | `listWallets()`        | 列出 all wallets for the current 用户                               |
|                    | `setPrimaryWallet()`   | 设置 the primary 钱包                                              |
|                    | `removeWallet()`       | 移除 a 钱包                                                     |
|                    | `syncWallets()`        | Sync wallets with the ledger                                        |
|                    | `isWalletSyncNeeded()` | 检查 if 钱包 sync is needed                                      |
| 交易       | `sign()`               | 签名 a 交易                                                  |
|                    | `execute()`            | 执行 a signed 交易                                        |
|                    | `getTransaction()`     | 获取 a 交易 by ID                                             |
|                    | `listTransactions()`   | 列出 交易                                                   |

**认证:**

Most 用户 API 方法 require 认证 via JWT token. However, the following 方法 are available without 认证:

* `addSession()`
* `listNetworks()`
* `listIdps()`

**Full API Specification:**

The complete OpenRPC specification is available at [openrpc-用户-api.json](https://github.com/canton-网络/钱包-gateway/blob/main/api-specs/openrpc-用户-api.json).

## 服务器发送事件（SSE） (SSE) Support

The dApp API supports 服务器发送事件（SSE） (SSE) for real-time notifications. 连接 to the `/事件` path relative to the dApp API base URL (e.g. `/api/v0/dapp/事件`). Authenticate by passing the JWT token as the `token` query parameter (the `授权: Bearer` header is also supported):

```javascript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const eventsUrl = new URL('events', dappApiUrl + '/')
eventsUrl.searchParams.set('token', jwtToken)
const eventSource = new EventSource(eventsUrl.toString())

eventSource.addEventListener('accountsChanged', (e) => {
    /* ... */
})
eventSource.addEventListener('statusChanged', (e) => {
    /* ... */
})
eventSource.addEventListener('connected', (e) => {
    /* ... */
})
eventSource.addEventListener('txChanged', (e) => {
    /* ... */
})
```

SSE connections receive real-time updates about:

* 交易 status changes (`txChanged`)
* 账户 changes (`accountsChanged`)
* 会话/connection state (`connected`, `statusChanged`)

## 速率限制

API requests are rate-limited to prevent abuse. The default limits can be configured in the server 配置. Rate limit headers are included in responses:

* `X-RateLimit-Limit` - Maximum number of requests per window
* `X-RateLimit-Remaining` - Remaining requests in current window
* `X-RateLimit-Reset` - Time when the rate limit resets

## CORS 配置

Cross-Origin Resource Sharing (CORS) is configured via the `allowedOrigins` setting in the server 配置. By default, all origins are allowed (`['*']`), but for 生产 deployments, you should restrict this to known dApp origins.

示例 配置：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "server": {
        "allowedOrigins": [
            "https://my-dapp.example.com",
            "https://another-dapp.example.com"
        ]
    }
}
```

Alternatively, you can allow all origins by setting `allowedOrigins` to `"*"`.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "server": {
        "allowedOrigins": ["*"]
    }
}
```

