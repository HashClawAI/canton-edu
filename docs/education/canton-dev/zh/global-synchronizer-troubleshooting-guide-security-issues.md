---
title: "安全问题"
slug: "global-synchronizer-troubleshooting-guide-security-issues"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/security-issues.md"
source_title: "Security Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - security-issues
---

# 安全问题

> 证书、JWT 与 KMS 相关的安全故障排查。

与安全相关的故障通常会阻止验证者启动或对synchronizer及其 API 进行身份验证。这些错误通常很神秘，但它们属于几个明确定义的类别。

## 证书问题

### 证书到期

验证者（用于其 Ledger API、管理 API 或入口）使用的 TLS 证书将在固定日期到期。当它们过期时，连接会立即失败。

**症状：**

```
javax.net.ssl.SSLHandshakeException: PKIX path validation failed:
java.security.cert.CertPathValidatorException: validity check failed
```

**检查有效期：**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check a PEM file
openssl x509 -in /path/to/cert.pem -noout -enddate

# Check a running server
openssl s_client -connect your-validator:443 2>/dev/null | openssl x509 -noout -dates
```

**解决方案：** 通过您的 CA 或证书管理器（Let's Encrypt、AWS ACM 等）续订证书。替换证书文件后，重新启动使用它的服务。对于 Kubernetes 入口控制器，一旦 Secret 更新，通常会自动重新启动。

### Kubernetes 中的证书续订

如果您使用cert-manager，请检查证书资源是否显示续订失败：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl describe certificate validator-tls -n validator
```

查找类似 `The certificate request has failed` 或 `Order is in state errored` 的事件。常见原因：DNS 质询失败（检查 DNS 传播）、HTTP 质询失败（检查入口路由）或颁发者的凭据已过期。

### 不完整的CA链

如果客户端可以从某些位置连接到验证者，但不能从其他位置连接到验证者，则服务器可能会提供不完整的证书链。验证：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect your-validator:443 -servername your-validator 2>&1 | grep "verify return"
```

如果您看到`verify return:0`，则链条已损坏。按照从叶到根的顺序将中间 CA 证书连接到服务器证书文件中。

## JWT 验证失败

JWT 令牌向验证者的 Ledger API 验证 API 客户端（您的应用程序、钱包 UI 或自动化脚本）。

### 时钟偏差

```
ACCESS_TOKEN_EXPIRED(2,0): Claims were valid until 2025-09-08T08:32:07Z,
current time is 2025-09-08T08:32:07.254413051Z
```

如果令牌生命周期很短，即使令牌发行者的时钟和验证者的时钟之间存在亚秒级的差异，也可能导致过期失败。修复：

* 将 OIDC 提供商中的访问令牌生命周期增加到至少 15 分钟。
* 确保 NTP 正在验证者主机上运行并同步：

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  timedatectl status
  # or
  chronyc tracking
  ```

### 错误的观众主张

```
PERMISSION_DENIED: JWT token has wrong audience. Expected: https://ledger_api.example.com
```

JWT 中的 `aud` 声明必须与验证者上配置的 `LEDGER_API_AUTH_AUDIENCE` 匹配。检查您的 OIDC 提供商的应用程序设置，并使受众与您的验证者配置保持一致。

### 过期的令牌

如果 API 调用间歇性失败并显示 `UNAUTHENTICATED`，则您的令牌刷新逻辑可能无法正常工作。验证：

* 令牌刷新间隔比令牌生命周期短。
* OIDC 提供商的令牌端点可从进行调用的应用程序访问。
* 刷新令牌本身尚未过期（刷新令牌通常具有较长但仍然有限的生命周期）。

### JWKS 端点无法访问

如果验证者无法到达 JWKS（JSON Web 密钥集）端点来验证令牌签名：

```
Failed to fetch JWKS from https://your-tenant.auth0.com/.well-known/jwks.json
```

检查从验证者到 OIDC 提供商的网络连接。在 Kubernetes 中，DNS 解析问题或出口限制可能会阻止此操作。

## 密钥管理

### KMS 连接

如果您的验证者使用云 KMS（AWS KMS、GCP Cloud KMS、Azure Key Vault）来签名密钥，连接故障会阻止事务签名。

**症状：**

```
com.amazonaws.SdkClientException: Unable to execute HTTP request: Connect to kms.us-east-1.amazonaws.com:443
```

**检查：*** 验证 KMS 端点是否可以从验证者 Pod 访问。
* 确认 IAM 角色或服务账户具有 `kms:Sign`、`kms:GetPublicKey` 和 `kms:Decrypt` 权限。
* 如果在 EKS 中使用 IRSA（服务帐户的 IAM 角色），请验证服务帐户注释和 OIDC 提供商信任。

### 权限错误

```
AccessDeniedException: User: arn:aws:sts::123456789:assumed-role/validator-role/...
is not authorized to perform: kms:Sign on resource: arn:aws:kms:...
```

附加到验证者角色的 IAM 策略必须包含特定的 KMS 密钥 ARN。资源字段中的通配符 (`*`) 用于测试，但应将范围限定为生产中的确切键。

### 按键轮换

Canton 在节点初始化期间生成加密密钥。如果您需要轮换密钥（例如，在可疑的泄露之后），请使用 Canton 控制台：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.secret.list()
    res1: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12201ff69b1d...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          name = Some(KeyName(participant1-namespace))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12200cd80d7c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(signing, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-signing))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 1220176a4b95...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-sequencer-auth))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = EncryptionPublicKeyWithName(
          publicKey = EncryptionPublicKey(
            id = 122029634afd...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-P256
          ),
          name = Some(KeyName(participant1-encryption))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newKey = participant1.keys.secret.generate_signing_key(name = "new-signing-key", usage = SigningKeyUsage.All)
    newKey : SigningPublicKey = SigningPublicKey(
      id = 122034956d8a...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(namespace, sequencer-auth, signing, proof-of-ownership)
    )
```

密钥轮换需要仔细协调。始终首先在非生产环境中进行测试。

# TLS 故障排除

可以使用此处描述的参数配置 TLS。

如果您在设置 SSL/TLS 时遇到问题，您可以启用 SSL 调试、增加 netty 日志记录或生成测试密钥和证书来验证您的配置。

## 启用 ssl 调试日志记录

您可以通过在启动 Canton 时将以下标志添加到命令行来启用 SSL 调试：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton -Djavax.net.debug=all
```

这会将详细的 SSL 相关信息打印到控制台，包括握手过程的详细信息。建议仅在故障排除时使用此标志，因为输出可能非常冗长，并且可能会影响应用程序的性能。

## 启用 netty 的调试日志记录

网络库`netty`提供的有关 TLS 问题的错误消息并不理想。如果您在设置 TLS 时遇到困难，请在 `io.netty` 记录器上启用 `DEBUG` 日志记录。这通常可以通过将以下行添加到 logback 日志配置中来完成：```xml theme={"theme":{"light":"github-light","dark":"github-dark"}}
<logger name="io.grpc.netty.shaded.io.netty.handler.ssl" level="DEBUG"/>
```

## 生成测试密钥和证书

如果您需要生成测试 TLS 证书来测试您的配置，可以使用以下 OpenSSL 脚本：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# include certs-common.sh from config/tls
. "$(dirname "${BASH_SOURCE[0]}")/certs-common.sh"

# create root certificate such that we can issue self-signed certs
create_key "root-ca"
create_certificate "root-ca" "/O=TESTING/OU=ROOT CA/emailAddress=canton@digitalasset.com"
print_certificate "root-ca"

# create public api certificate
create_key "public-api"
create_csr "public-api" "/O=TESTING/OU=DOMAIN/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "public-api" "root-ca"
print_certificate "public-api"

# create participant ledger-api certificate
create_key "ledger-api"
create_csr "ledger-api" "/O=TESTING/OU=PARTICIPANT/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "ledger-api" "root-ca"

# create participant admin-api certificate
create_key "admin-api"
create_csr "admin-api" "/O=TESTING/OU=PARTICIPANT ADMIN/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "admin-api" "root-ca"

# create participant client key and certificate
create_key "admin-client"
create_csr "admin-client" "/O=TESTING/OU=PARTICIPANT ADMIN CLIENT/CN=localhost/emailAddress=canton@digitalasset.com"
sign_csr "admin-client" "root-ca"
print_certificate "admin-client"
```

如果您希望手动生成自己的密钥和证书集，则在此过程中使用的命令记录在此处：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
DAYS=3650

function create_key {
  local name=$1
  openssl genrsa -out "${name}.key" 4096
  # netty requires the keys in pkcs8 format, therefore convert them appropriately
  openssl pkcs8 -topk8 -nocrypt -in "${name}.key" -out "${name}.pem"
}

# create self signed certificate
function create_certificate {
  local name=$1
  local subj=$2
  openssl req -new -x509 -sha256 -key "${name}.key" \
              -out "${name}.crt" -days ${DAYS} -subj "$subj"
}

# create certificate signing request with subject and SAN
# we need the SANs as our certificates also need to include localhost or the
# loopback IP for the console access to the admin-api and the ledger-api
function create_csr {
  local name=$1
  local subj=$2
  local san=$3
  (
    echo "authorityKeyIdentifier=keyid,issuer"
    echo "basicConstraints=CA:FALSE"
    echo "keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment"
  ) > ${name}.ext
  if [[ -n $san ]]; then
    echo "subjectAltName=${san}" >> ${name}.ext
  fi
  # create certificate (but ensure that localhost is there as SAN as otherwise, admin local connections won't work)
  openssl req -new -sha256 -key "${name}.key" -out "${name}.csr" -subj "$subj"
}

function sign_csr {
  local name=$1
  local sign=$2
  openssl x509 -req -sha256 -in "${name}.csr" -extfile "${name}.ext" -CA "${sign}.crt" -CAkey "${sign}.key" -CAcreateserial  \
               -out "${name}.crt" -days ${DAYS}
  rm "${name}.ext" "${name}.csr"
}

function print_certificate {
  local name=$1
  openssl x509 -in "${name}.crt" -text -noout
}
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
