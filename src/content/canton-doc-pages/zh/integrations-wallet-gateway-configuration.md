---
title: "配置"
slug: "integrations-wallet-gateway-configuration"
locale: "zh"
category: "integrations"
source_url: "https://docs.canton.network/integrations/wallet-gateway/configuration.md"
source_title: "Configuration"
tags:
  - integrations
  - wallet-gateway
  - configuration
---

# 配置

> 配置 a remote 钱包 Gateway

本节介绍 the different ways the 钱包 Gateway can be configured to support a variety of use cases and deployment scenarios.

## 概览

钱包 Gateway 配置 is a JSON file that defines:

* **Kernel Settings**: Identity and client type information
* **Server Settings**: 网络 binding, ports, API paths, and admin 用户
* **Store 配置**: Database connection and persistence settings
* **Bootstrap 配置**: Initial identity 提供方 and 网络 definitions seeded on first run
* **Signing Store**: 可选 database for key storage (when using internal signing)

## 默认配置示例

Here is a minimalistic 配置 example that can be used against a Splice localnet using SQLite storage and a mock OAuth setup. The mock OAuth 配置 showcases how an IDP 配置 would look.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "kernel": {
        "id": "remote-da",
        "clientType": "remote"
    },
    "server": {
        "port": 3030,
        "dappPath": "/api/v0/dapp",
        "userPath": "/api/v0/user",
        "allowedOrigins": ["http://localhost:8080", "http://localhost:8081"],
        "admin": "operator"
    },
    "store": {
        "connection": {
            "type": "sqlite",
            "database": "store.sqlite"
        }
    },
    "signingStore": {
        "connection": {
            "type": "sqlite",
            "database": "signingStore.sqlite"
        }
    },
    "bootstrap": {
        "idps": [
            {
                "id": "idp-mock-oauth",
                "type": "oauth",
                "issuer": "http://127.0.0.1:8889",
                "configUrl": "http://127.0.0.1:8889/.well-known/openid-configuration"
            }
        ],
        "networks": [
            {
                "id": "canton:localnet",
                "name": "LocalNet",
                "description": "LocalNet configuration",
                "identityProviderId": "idp-self-signed",
                "auth": {
                    "method": "self_signed",
                    "issuer": "self-signed",
                    "audience": "https://canton.network.global",
                    "scope": "openid daml_ledger_api offline_access",
                    "clientId": "ledger-api-user",
                    "clientSecret": "unsafe"
                },
                "adminAuth": {
                    "method": "self_signed",
                    "issuer": "self-signed",
                    "scope": "openid daml_ledger_api offline_access",
                    "audience": "https://canton.network.global",
                    "clientId": "ledger-api-user",
                    "clientSecret": "unsafe"
                },
                "ledgerApi": {
                    "baseUrl": "http://localhost:2975"
                }
            }
        ]
    }
}
```

你可以 easily create a similar 配置 file by running:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
wallet-gateway --config-example > config.json
```

To view the complete possible JSON Schema of the 配置 file, see [Schema.md](https://github.com/canton-网络/钱包-gateway/blob/82ec39c9/docs/dapp-building/钱包-gateway/配置/schema.md).

## 配置结构

The 配置 file has the following main sections:

* **kernel**: Basic information about the 钱包 Gateway identity
* **server**: 网络 binding, ports, API 端点 配置, and admin 用户 designation
* **store**: Database connection and persistence settings
* **bootstrap**: Initial identity 提供方 and 网络 definitions seeded when the database is first created
* **signingStore**: (optional) Secondary database for key storage when using internal signing

## Configuring Kernel Settings

The **kernel** section contains information that is served to dApps and used to uniquely identify the Gateway instance.

**kernel:**

* *id* (required): A unique identifier for this Gateway instance. This should be a stable, unique string (e.g., `"my-gateway-prod"` or `"remote-da"`).
* *publicUrl* (optional): The base URL used for redirecting clients. If not provided, it will be automatically derived from the server host and port settings. This is particularly important when running behind a reverse proxy or load balancer.
* *clientType* (required): The type of client. For a remote 钱包 Gateway, this should always be set to `'remote'`.

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "kernel": {
        "id": "my-production-gateway",
        "clientType": "remote",
        "publicUrl": "https://wallet.example.com"
    }
}
```

## Configuring Server Settings

The **server** section configures 网络 binding, ports, and API paths.

**server:**

* *port* (optional, default: `3030`): The port on which the Node.js server will bind. This port is also used for generating popup URLs in the discovery flow.
* *dAppPath* (optional, default: `'/api/v0/dapp'`): The API path for dApp JSON-RPC requests. This is where dApps connect to interact with wallets.
* *userPath* (optional, default: `'/api/v0/用户'`): The API path for 用户 JSON-RPC requests. This is used by the web UI and 用户-facing 应用.
* *allowedOrigins* (optional, default: `['*']`): CORS allowed origins. For 生产, specify exact origins instead of `'*'` for better security. 示例: `["https://my-dapp.com", "https://another-dapp.com"]`.
* *requestSizeLimit* (optional, default: `'1mb'`): Maximum 请求 body size the server will accept. Use standard size notation (e.g., `'1mb'`, `'10mb'`, `'50kb'`).
* *requestRateLimit* (optional, default: `10000`): Maximum number of requests per minute from a single IP address (this excludes health 端点).
* *admin* (optional): The 用户 ID (JWT `sub` claim) of the admin 用户. When set, the matching 用户 is granted admin privileges, allowing them to manage networks and identity 提供方 through the 用户 API and web UI. Other 用户 can only view these settings. If omitted, no 用户 has admin privileges and 网络/IDP management is restricted to the bootstrap 配置.

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "server": {
        "port": 3030,
        "dAppPath": "/api/v0/dapp",
        "userPath": "/api/v0/user",
        "allowedOrigins": ["https://my-dapp.example.com"],
        "requestSizeLimit": "10mb",
        "requestRateLimit": 10000,
        "admin": "operator"
    }
}
```

**store:**

* *connection:* Configures the database connection. 参见 [Configuring Store](#configuring-store) for details.

**bootstrap:**

* *idps:* Configures the initial identity 提供方 (IDPs) seeded when the database is first created. 参见 [Configuring Identity 提供方](#configuring-identity-提供方) for details.
* *networks:* Configures the initial networks seeded when the database is first created. 参见 [Configuring Networks](#configuring-networks) for details.

## Configuring Store

The store connection determines where the 钱包 Gateway persists its data, including 会话, 钱包 configurations, networks, identity 提供方, and 交易.

**Available Storage Options:**

Three storage backends are available: **memory**, **sqlite**, and **postgres**.

**建议：**

* **生产/Test Environments**: Use **postgres** for reliability, scalability, and 备份 capabilities
* **Local 开发**: Use **sqlite** for simplicity and persistence across restarts
* **Quick 测试**: Use **memory** for temporary setups (all data is lost on restart)

> \[!IMPORTANT]
> If using Docker or Kubernetes with the memory store, all data will be lost when the container/pod is recreated. SQLite will persist only if the database file is stored on a persistent volume.

**PostgreSQL 配置：**

For 生产 deployments, PostgreSQL is recommended due to its robustness, concurrent access support, and 备份/恢复 capabilities.

**postgres:**

* *type* (required): Must be `'postgres'`
* *host* (required): The hostname or IP address of the PostgreSQL server
* *port* (optional, default: `5432`): The port on which PostgreSQL is listening
* *用户* (required): The database 用户 to connect with
* *password* (required): The password for the database 用户
* *database* (required): The name of the database to use (must exist)

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "store": {
        "connection": {
            "type": "postgres",
            "host": "db.example.com",
            "port": 5432,
            "user": "wallet_gateway",
            "password": "secure-password",
            "database": "wallet_gateway_db"
        }
    }
}
```

**SQLite 配置：**

SQLite is suitable for single-instance deployments and local 开发. It stores all data in a single file.

**sqlite:**

* *type* (required): Must be `'sqlite'`
* *database* (required): Path to the SQLite database file (e.g., `'store.sqlite'` or `'/var/lib/钱包-gateway/store.sqlite'`)

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "store": {
        "connection": {
            "type": "sqlite",
            "database": "store.sqlite"
        }
    }
}
```

**Memory Store 配置：**

The memory store keeps all data in RAM. Useful for 测试 but not suitable for any 生产 use.

**memory:**

* *type* (required): Must be `'memory'`

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "store": {
        "connection": {
            "type": "memory"
        }
    }
}
```

### Database Recovery and Backups

For 生产 and sensitive environments, regular database backups are **strongly recommended**.

**What's Stored in the Database:**

The store database contains:

* 用户 会话 and 认证 state
* Networks and identity 提供方 (seeded from bootstrap 配置 on first run, manageable by admin at runtime)
* 钱包 configurations and party mappings
* In-flight 交易 (pending signing or signed but not yet submitted)

**What Happens Without Backups:**

若 database is lost and cannot be restored:

* All 用户 会话 will be invalidated (用户 must log in again)
* Networks and IDPs will be re-seeded from the bootstrap 配置, but any runtime modifications made by the admin will be lost
* In-flight 交易 will be lost (may require manual intervention)
* 钱包 configurations referencing lost networks may need to be reconfigured

**备份 建议：**

* **PostgreSQL**: Use `pg_dump` or automated 备份 solutions (e.g., pgBackRest, WAL-E)
* **SQLite**: Copy the database file regularly, ensuring no writes occur during the copy
* 设置 up automated daily backups with retention policies
* Test 恢复 procedures regularly

> \[!IMPORTANT]
> 若 钱包 gateway is used as signing 提供方 then clients private keys will be lost! It is therefor highly recommended
> to not use 钱包 gateway as signing 提供方 in any important system.

## Configuring Identity 提供方

Identity 提供方 (IDPs) are used for generating JWT tokens that authenticate against Canton validator networks. Each 网络 must reference an IDP that provides or generates the required 认证 tokens.

IDPs are defined in the `bootstrap` section of the 配置 and are seeded into the database when it is first created. After initial setup, IDPs can be managed at runtime through the 用户 API or web UI by the admin 用户 (see `server.admin`).

**Supported IDP Types:**

钱包 Gateway supports two types of identity 提供方: **self\_signed** and **oauth**.

> \[!IMPORTANT]
> For 生产 environments, it is **highly recommended** to use an **oauth** IDP 提供方. Self-signed tokens should only be used for 开发 and 测试.

**Self-Signed IDP:**

Self-signed IDPs generate JWT tokens locally using a secret key. This is convenient for 开发 but less secure for 生产.

**self\_signed:**

* *id* (required): Unique identifier that must match the `identityProviderId` referenced in 网络 configurations
* *type* (required): Must be `'self_signed'`
* *issuer* (required): The issuer value that will be set in the JWT token's `iss` claim. This must match the issuer expected by the 验证者节点

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "bootstrap": {
        "idps": [
            {
                "id": "idp-self-signed",
                "type": "self_signed",
                "issuer": "self-signed"
            }
        ]
    }
}
```

**OAuth IDP:**

OAuth IDPs integrate with external OAuth 2.0 / OpenID 连接 提供方 to obtain 认证 tokens. This is the recommended approach for 生产.

**oauth:**

* *id* (required): Unique identifier that must match the `identityProviderId` referenced in 网络 configurations
* *type* (required): Must be `'oauth'`
* *issuer* (required): The issuer value that will be set in the JWT token's `iss` claim. This should match the issuer from your OAuth 提供方's 配置
* *configUrl* (required): The OpenID 连接 discovery 端点 URL. Typically follows the pattern: `${OAuthServerURL}/.well-known/openid-配置`

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "bootstrap": {
        "idps": [
            {
                "id": "idp-production",
                "type": "oauth",
                "issuer": "https://auth.example.com",
                "configUrl": "https://auth.example.com/.well-known/openid-configuration"
            }
        ]
    }
}
```

## Configuring Networks

Networks represent different Canton 验证者节点 that clients can connect to through the 钱包 Gateway.
Networks defined in the `bootstrap` section are seeded into the database when it is first created and serve as the default networks available to all 用户. After initial setup, networks can be managed at runtime through the 用户 API or web UI by the admin 用户 (see `server.admin`).

**网络 配置：**

Networks is an array, so you can define multiple networks in a single 配置:

**networks** (array):

* *id* (required): Unique identifier for the 网络. Should follow CAIP-2 format (e.g., `"canton:localnet"` or `"canton:生产"`)
* *name* (required): 用户-friendly name displayed in the UI (e.g., `"Local 网络"` or `"生产 网络"`)
* *description* (optional): A description of the 网络 shown to 用户
* *synchronizerId* (required): The 同步器 ID used on the validator. If your validator has multiple synchronizers, create separate 网络 configurations for each
* *identityProviderId* (required): Must match the `id` of an IDP defined in the `idps` section
* *ledgerApi* (required): 配置 object for the Ledger API:
  * *baseUrl* (required): The base URL of the Canton validator's Ledger API (e.g., `"http://localhost:2975"` or `"https://ledger.example.com"`)
* *auth* (required): 认证 配置 for normal ledger operations
* *adminAuth* (optional): 认证 配置 for admin operations. Only needed for operations requiring elevated privileges

**认证 方法:**

钱包 Gateway supports three 认证 方法 for 网络 access: **授权\_code**, **client\_credentials**, and **self\_signed**.

**建议：**

* **生产**: Use **client\_credentials** for machine-to-machine 认证
* **Interactive/用户-facing**: Use **授权\_code** for 用户-initiated flows
* **开发/测试**: Use **self\_signed** for local 开发

**授权 Code:**

Used for interactive 认证 flows where 用户 grant 授权 through their browser.

**授权\_code:**

* *方法* (required): Must be `'authorization_code'`
* *audience* (required): The audience claim (`aud`) in the JWT token. Must match the audience expected by the validator
* *scope* (required): Space-separated list of OAuth scopes. Typically includes `'openid daml_ledger_api offline_access'`
* *clientId* (required): The OAuth client ID registered with the identity 提供方

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "auth": {
        "method": "authorization_code",
        "audience": "https://canton.network.global",
        "scope": "openid daml_ledger_api offline_access",
        "clientId": "my-client-id"
    }
}
```

**Client Credentials:**

Used for machine-to-machine 认证. 推荐 for 生产 server deployments.

**client\_credentials:**

* *方法* (required): Must be `'client_credentials'`
* *audience* (required): The audience claim (`aud`) in the JWT token. Must match the audience expected by the validator
* *scope* (required): Space-separated list of OAuth scopes. Typically includes `'openid daml_ledger_api offline_access'`
* *clientId* (required): The OAuth client ID registered with the identity 提供方
* *clientSecret* (required): The OAuth client secret for authenticating with the IDP

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "auth": {
        "method": "client_credentials",
        "audience": "https://canton.network.global",
        "scope": "openid daml_ledger_api offline_access",
        "clientId": "my-service-client",
        "clientSecret": "my-secure-secret"
    }
}
```

**Self-Signed:**

Used for 开发 and 测试. The Gateway generates and signs JWT tokens locally.

**self\_signed:**

* *方法* (required): Must be `'self_signed'`
* *issuer* (required): The issuer claim (`iss`) in the JWT token. Must match the issuer expected by the validator
* *audience* (required): The audience claim (`aud`) in the JWT token. Must match the audience expected by the validator
* *scope* (required): Space-separated list of scopes. Typically includes `'openid daml_ledger_api offline_access'`
* *clientId* (required): The client identifier used in the token
* *clientSecret* (required): The secret used to sign the JWT token. Must match the secret expected by the validator

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "auth": {
        "method": "self_signed",
        "issuer": "self-signed",
        "audience": "https://canton.network.global",
        "scope": "openid daml_ledger_api offline_access",
        "clientId": "ledger-api-user",
        "clientSecret": "unsafe-secret-for-development"
    }
}
```

**Complete 网络 配置 示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "bootstrap": {
        "networks": [
            {
                "id": "canton:localnet",
                "name": "Local Network",
                "description": "Local development network",
                "synchronizerId": "local",
                "identityProviderId": "idp-self-signed",
                "auth": {
                    "method": "self_signed",
                    "issuer": "self-signed",
                    "audience": "https://canton.network.global",
                    "scope": "openid daml_ledger_api offline_access",
                    "clientId": "ledger-api-user",
                    "clientSecret": "unsafe"
                },
                "ledgerApi": {
                    "baseUrl": "http://localhost:2975"
                }
            }
        ]
    }
}
```

## Configuring Signing Store

The signing store is an optional secondary database used for storing private keys when the 钱包 Gateway is configured to act as a signing 提供方 (using the `wallet-kernel` signing 提供方).

> \[!IMPORTANT]
> 若你 use the 钱包 Gateway as a signing 提供方, private keys will be stored in the signing store database. This is **not recommended** for 生产 environments with valuable assets. Use external signing 提供方 (Dfns, Fireblocks, Blockdaemon, or 参与者-based) for 生产.

**配置：**

The signing store uses the same connection 配置 options as the main store. 参见 [Configuring Store](#configuring-store) for available options (memory, sqlite, postgres).

**When is Signing Store 必需?**

The signing store is only needed if:

* You're using the `wallet-kernel` signing 提供方 (internal signing)
* You want to store keys managed by the 钱包 Gateway itself

若你're using external signing 提供方 (Dfns, Fireblocks, Blockdaemon, 参与者), you can omit the `signingStore` 配置 entirely.

**示例:**

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
    "signingStore": {
        "connection": {
            "type": "sqlite",
            "database": "signingStore.sqlite"
        }
    }
}
```

**安全注意事项:**

* Store the signing store database file in a secure location with restricted access
* Use strong filesystem permissions (e.g., `chmod 600` for SQLite files)
* For PostgreSQL, use separate credentials with minimal privileges
* Consider encrypting the database at rest
* Regularly 备份 the signing store if it contains 生产 keys
* Never commit signing store files to version control

## Configuring for Different Environments

**按环境配置 Files**

It is recommended to maintain separate 配置 files for each environment (开发, staging, 生产). This allows you to:

* Isolate settings per environment
* Apply different security levels and policies
* Prevent accidental use of 生产 credentials in 开发
* Simplify environment-specific deployments

**Best Practices:**

1. **Use separate files**: 创建 `config.dev.json`, `config.staging.json`, `config.prod.json`

2. **Sensitive data**: Never commit sensitive values (passwords, secrets, API keys) directly in 配置 files, especially if stored in version control

3. **Environment variables**: Use environment variables to override sensitive 配置 values:

   ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {
       "bootstrap": {
           "networks": [
               {
                   "auth": {
                       "clientSecretEnv": "OAUTH_CLIENT_SECRET"
                   }
               }
           ]
       }
   }
   ```

   Then set the environment variable when running:

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   export OAUTH_CLIENT_SECRET="my-secret"
   wallet-gateway -c ./config.json
   ```

4. **Access control**: Be aware that:
   * 网络 and IDP configurations (excluding secrets) are visible to 用户 with ledger access
   * If 配置 files are stored in shared repositories, anyone with read access can see non-secret 配置
   * Use environment variables or secret management systems (e.g., HashiCorp Vault, AWS Secrets Manager) for sensitive values

5. **Admin 认证**: The `adminAuth` 配置 contains sensitive credentials and should be:
   * Stored securely (not in version control)
   * Rotated regularly
   * Restricted to 生产 environments where truly needed

**示例 Environment 设置：**

**开发 (config.dev.json):**

* SQLite or memory store
* Self-signed 认证
* Localhost 网络 端点
* Permissive CORS settings

**生产 (config.prod.json):**

* PostgreSQL store
* OAuth 认证
* 生产 网络 端点
* Restricted CORS settings
* Secrets via environment variables

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
