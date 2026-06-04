---
title: "Canton 安全配置"
slug: "global-synchronizer-reference-security-configuration"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/security-configuration.md"
source_title: "Canton Security Configuration"
tags:
  - global-synchronizer
  - reference
  - security-configuration
---

# Canton 安全配置

> 为 Canton 节点配置 TLS、JWT 认证与 API 限制。

> 为 Canton 节点配置 TLS、JWT 身份验证和 API 限制


gRPC Ledger API 和管理 API 都支持相同的 TLS 功能，并且可以使用相同的指令进行配置。 TLS 在服务器和客户端之间提供端到端通道加密，并且根据配置可以强制执行仅服务器身份验证或相互身份验证。

本节中提供的示例配置适用于 Ledger API，但它们对于 Admin API 来说是相同的。这些操作方法中提到的所有私钥都必须采用 PKCS#8 PEM 格式。

## 启用 TLS 进行服务器端身份验证

以下设置允许连接客户端验证其是否正在与目标服务器进行通信。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方4.ledger-api {
  address = "127.0.0.1" // IP / DNS must be SAN of certificate to allow local connections from the canton process
  port = 5041
  tls {
    // the certificate to be used by the server
    cert-chain-file = "./tls/ledger-api.crt"
    // private key of the server
    private-key-file = "./tls/ledger-api.pem"
    // trust collection, which means that all client certificates will be verified using the trusted
    // certificates in this store. if omitted, the JVM default trust store is used.
    trust-collection-file = "./tls/root-ca.crt"
  }
}

// architecture-handbook-entry-begin: 参与方TLSApiClient
canton.参与方s.参与方4.ledger-api.tls.client-auth =
  {
    // none, optional and require are supported
    type = require
    // If clients are required to authenticate as well, we need to provide a client
    // certificate and the key, as Canton has internal processes that need to connect to these
    // APIs. If the server certificate is trusted by the trust-collection, then you can
    // just use the server certificates. Otherwise, you need to create separate ones.
    admin-client {
      cert-chain-file = "./tls/admin-client.crt"
      private-key-file = "./tls/admin-client.pem"
    }
  }
// architecture-handbook-entry-end: 参与方TLSApiClient

// architecture-handbook-entry-begin: 参与方TLSApiRestrict
// optional, if omitted, defaults to the latest TLS protocol version
canton.参与方s.参与方4.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
// optional, if omitted, defaults to the latest supported secure ciphers
canton.参与方s.参与方4.ledger-api.tls.ciphers =
  [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256"
  ]
// architecture-handbook-entry-end: 参与方TLSApiRestrict

canton.参与方s.参与方4 {
  admin-api {
    address = "localhost"
    port= 5042
    tls {
      cert-chain-file = "./enterprise/app/src/test/resources/tls/admin-api.crt"
      private-key-file = "./enterprise/app/src/test/resources/tls/admin-api.pem"
    }
  }

  storage {
    type = "h2"
    config = {
      url = "jdbc:h2:mem:db4;MODE=PostgreSQL;LOCK_TIMEOUT=10000;DB_CLOSE_DELAY=-1"
      user = "参与方4"
      password = "pwd"
      driver = org.h2.Driver
    }
  }
}
```

`trust-collection-file` 允许您提供基于文件的信任存储。如果省略，系统将默认使用内置的`JVM`信任存储。该格式是 PEM 证书的集合（按正确的顺序或层次结构），而不是基于 Java 的信任存储。

## 启用 TLS 进行客户端身份验证

默认情况下禁用客户端身份验证。要启用它，您必须将`client-auth.type`配置为`require`。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方4.ledger-api.tls.client-auth =
  {
    // none, optional and require are supported
    type = require
    // If clients are required to authenticate as well, we need to provide a client
    // certificate and the key, as Canton has internal processes that need to connect to these
    // APIs. If the server certificate is trusted by the trust-collection, then you can
    // just use the server certificates. Otherwise, you need to create separate ones.
    admin-client {
      cert-chain-file = "./tls/admin-client.crt"
      private-key-file = "./tls/admin-client.pem"
    }
  }
```

这个新的`client-auth`设置启用客户端身份验证，这意味着客户端需要出示有效的证书（并具有相应的私钥）。`trust-collection-file` 必须包含受信任才能使用 API 的所有客户端证书（或用于签署客户端证书的父证书）。如果证书已由信任存储中的密钥签名，则该证书有效。

## 限制 TLS 密码和协议

假设服务器端配置已按照上面的操作方法中所述完成，则可以使用以下设置来限制允许的 TLS 密码和协议版本。默认情况下，Canton 使用 JVM 默认值，但您可以使用变量 `ciphers` 和 `minimum-server-protocol-version` 覆盖它们。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// optional, if omitted, defaults to the latest TLS protocol version
canton.参与方s.参与方4.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
// optional, if omitted, defaults to the latest supported secure ciphers
canton.参与方s.参与方4.ledger-api.tls.ciphers =
  [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256"
  ]
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/secure/apis/jwt.rst" hash="6dd0171a" */}

# 使用 JWT 配置 API 身份验证和授权

## 配置授权服务

Ledger API 支持基于 [JWT](https://jwt.io/) 的授权检查，如授权文档中所述。

为了启用 JWT 授权检查，您的安全配置选项是：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      // type can be
      //   jwt-rs-256-crt
      //   jwt-es-256-crt
      //   jwt-es-512-crt
      type = jwt-rs-256-crt
      // we need a certificate file (abcd.cert)
      certificate = ${JWT_CERTIFICATE_FILE}
    }]
  }
}
```

* `jwt-rs-256-crt`。参与者将期望所有令牌都使用 RS256（使用 SHA-256 的 RSA 签名）以及从给定 X.509 证书文件加载的公钥进行签名。支持 PEM 编码的证书（以`-----BEGIN CERTIFICATE-----` 开头的文本文件）和 DER 编码的证书（二进制文件）。
* `jwt-es-256-crt`。参与者期望所有令牌都使用 ES256（使用 P-256 和 SHA-256 的 ECDSA）进行签名，并使用从给定 X.509 证书文件加载的公钥。支持 PEM 编码的证书（以`-----BEGIN CERTIFICATE-----` 开头的文本文件）和 DER 编码的证书（二进制文件）。
* `jwt-es-512-crt`。参与者将期望所有令牌都使用 ES512（使用 P-521 和 SHA-512 的 ECDSA）以及从给定 X.509 证书文件加载的公钥进行签名。支持 PEM 编码的证书（以`-----BEGIN CERTIFICATE-----` 开头的文本文件）和 DER 编码的证书（二进制文件）。
* `jwt-jwks`。您可以指定 [JWKS](https://tools.ietf.org/html/rfc7517) URL，而不是指定证书的路径。在这种情况下，参与者节点希望所有令牌都使用从给定 JWKS URL 加载的公钥通过 RS256、ES256 或 ES512 进行签名。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      type = jwt-jwks
      // we need a URL to a jwks key, e.g. https://path.to/jwks.key
      url = ${JWT_URL}
    }]
  }
}
```

<Warning>
  仅出于测试目的，您还可以指定共享密钥。在这种情况下，参与者节点期望所有令牌都使用给定的明文密钥通过 HMAC256 进行签名。这对于生产来说不被认为是安全的。
</Warning>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      type = unsafe-jwt-hmac-256
      secret = "not-safe-for-production"
    }]
  }
}
```

<Note>
  为了防止中间人攻击，强烈建议对生产中发送到 Ledger API 的任何请求使用 TLS 和服务器身份验证，如 `tls-configuration` 中所述。
</Note>

请注意，您可以定义多个授权插件。如果定义了多个，系统将使用第一个不返回 Unauthorized 的 auth 插件的声明。

如果未定义授权插件，系统将使用默认（通配符）授权方法。

## 配置JWT授权的余地参数您可以使用 JWT 令牌定义授权的余地参数。由于令牌签名和验证之间的时钟偏差而导致授权失败，可以通过指定令牌仍被视为有效的余地窗口来缓解。回旋余地可以专门针对令牌的**过期时间（“exp”）**、**不早于（“nbf”）**和**发行时间（“iat”）**声明进行定义，也可以通过这三者的默认值来定义。定义三个特定字段中每一个字段余地的值将覆盖默认值（如果存在）。余地参数应以秒为单位给出，并且可以按照下面的示例配置进行定义：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方.ledger-api.jwt-timestamp-leeway {
    default = 5
    expires-at = 10
    issued-at = 15
    not-before = 20
}
```

## 配置 JWT 授权的目标受众

使用 JWT 在 Ledger API 上进行身份验证的默认受众（基于受众的令牌中的`aud`字段）是`https://daml.com/参与方/jwt/aud/参与方/${参与方Id}`。可以使用自定义目标受众配置选项显式配置其他受众：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    参与方s {
      参与方 {
        ledger-api {
          auth-services = [{
            type = jwt-jwks
            url = "https://some.url/jwks.json"
            target-scope = "custom/Scope-5:with_special_characters"
          }]
        }
      }
    }
  }

```

## 配置JWT授权的目标范围

使用 JWT 在 Ledger API 上进行身份验证的默认范围（基于范围的访问令牌中的`scope`字段）是`daml_ledger_api`。

可以使用自定义目标范围配置选项显式配置其他范围：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    参与方s {
      参与方 {
        ledger-api {
          port = 5001
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
          }]
        }
        admin-api {
          port = 5002
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
            users = [{
              user-id = alice
              allowed-services = [
                "admin.v0.参与方RepairService",
                "connection.v30.ApiInfoService",
                "v1.ServerReflection",
              ]
            }]
          }]
        }
      }
    }
  }

```

目标范围可以是任何包含字母数字字符、连字符、斜杠、冒号和下划线的区分大小写的字符串。 `target-scope` 或`target-audience` 参数可以单独配置，但不能同时配置。

## 使用用户列表配置授权服务

具有用户列表的授权服务是 JWT 授权的一种形式，可以在参与者、Sequencer和中介节点公开的管理 API 上进行配置，也可以在参与者节点的 Ledger API 上使用。

您可以指定应允许哪些用户进入以及他们应访问哪些 gRPC 服务。 Ledger 和 Admin API 的示例配置如下所示：

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    参与方s {
      参与方 {
        ledger-api {
          port = 5001
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
          }]
        }
        admin-api {
          port = 5002
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
            privileged = true
            access-level = wildcard
          }]
        }
      }
    }
  }

```与 Ledger API 不同，Admin API 不要求 JWT 令牌子声明中出现的用户存在于参与者的用户数据库中。授权服务配置中的用户可以是参与者节点运营商的任意选择。该用户还需要在颁发 JWT 令牌的关联 IDP 系统中进行配置。

配置可以包含目标受众或目标范围的定义，具体取决于客户组织的具体偏好。如果没有给出，则 IDP 铸造的 JWT 令牌必须指定 `daml_ledger_api` 作为其范围声明。

与运营商想要公开的特定服务无关，最好也授予`ServerReflection`服务的访问权限。某些工具（例如 `grpcurl` 或 `postman`）需要访问该服务来构建其请求。

## 配置特权令牌

特权令牌是 JWT 授权的另一种形式，可以在参与者、Sequencer和中介节点公开的管理 API 上进行配置，也可以在参与者节点的 Ledger API 上使用。配置遵循与普通用户令牌相同的模式，但它包含一个名为 `privileged` 设置为 true 的附加密钥。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  参与方s {
    参与方 {
      ledger-api {
        port = 5001
        auth-services = [{
          type = jwt-jwks
          url = "https://target.audience.url/jwks.json"
          target-audience = "https://rewrite.target.audience.url"
        }]
      }
      admin-api {
        port = 5002
        auth-services = [{
          type = jwt-jwks
          url = "https://target.audience.url/jwks.json"
          target-audience = "https://rewrite.target.audience.url"
          privileged = true
          access-level = wildcard
        }]
      }
    }
  }
}
```

您可以通过添加`access-level`密钥的定义并将其分别设置为`Admin`或`Wildcard`来确定使用特权令牌是否会导致授予`参与方_admin`或`wildcard`访问级别。 `Admin` 是默认值。

## 配置JWKS缓存过期

JWKS 缓存存储最近获得的公钥，这减少了对 JWKS HTTP 端点的昂贵的重复调用的需要。密钥在缓存中的默认保留时间为 5 分钟。此后，密钥将被逐出，参与者必须再次联系 JWKS 地址以检索最新的密钥。您可以通过设置来修改此行为：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方.ledger-api.jwks-cache-config {
  cache-expiration = 1.hour
}
```

类似的参数也可以在`admin-api`上设置。

## 配置 JWT 令牌的最大生存时间

为了提高 JWT 令牌被盗或丢失的安全性，建议使用过期时间非常短的令牌，最好在 5 到 15 分钟之间。有关此主题的更多详细信息，请参阅有关短期令牌重要性的文档。

您可以通过配置 `max-token-lifetime` 参数为参与者强制实施短期令牌策略。如果提供的令牌缺少`exp`（过期）字段，或者计算的生存时间大于此配置的最大值，则身份验证层将拒绝访问。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方.ledger-api {
  max-token-lifetime = 10.minutes
}
```

类似的参数也可以在`admin-api`上设置。

<Note>
  拒绝仅基于令牌的剩余生存时间。因此，假设 `max-token-lifetime` 设置为 5 分钟，最初有效期为 24 小时的令牌如果在其生命周期的最后 5 分钟内出现，仍然可以成功使用。
</Note>

## 配置远程控制台进行 JWT 授权

配置授权后，只有当配置中的 JWT 令牌可供控制台使用时，远程控制台才会对参与者起作用：```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  remote-参与方s {
    参与方 {
      ledger-api {
        address = 10.60.12.1
        port = 10001
      }
      admin-api {
        address = 10.60.12.1
        port = 10002
      }
     token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsInNjb3BlIjoibXktdGFyZ2V0LXNjb3BlIn0.AkbGOfUJwAafV1xCjjRqx3rC5fPoBxgYKPfUc043pts
    }
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/参与方/howtos/secure/apis/limits.rst" hash="c2b8d444" */}

涵盖 Admin API 和 Ledger API 的 gRPC 最大消息大小。涵盖 Ledger API 的速率限制。讨论 API 前面的负载均衡器作为额外保护的最佳实践。讨论如果速率限制过于严格可能对性能造成的影响。链接到如何了解参与者的资源限制。链接到“构建”站点以了解 daml 相关的大小限制。

# 配置API限制

## 最大入站消息大小

参与者（gRPC Ledger API 和 Admin API）以及同步器（公共 API 和 Admin API）公开的 API 对传入消息大小都有上限。为了增加此限制以适应更大的有效负载，必须为相应的 API 将标志 `max-inbound-message-size` 设置为最大消息大小（以 **字节** 为单位）。

例如，要将参与者的 gRPC Ledger API 限制配置为 20MB：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方2.ledger-api {
  address = "127.0.0.1"
  port = 5021
  max-inbound-message-size = 20971520
}
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
