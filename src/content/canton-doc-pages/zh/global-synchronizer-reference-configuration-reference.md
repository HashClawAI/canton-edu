---
title: "配置参考"
slug: "global-synchronizer-reference-configuration-reference"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/configuration-reference.md"
source_title: "Configuration Reference"
tags:
  - global-synchronizer
  - reference
  - configuration-reference
---

# 配置参考

> Canton Network 验证者与 SV 完整配置参考。

> Canton Network 验证器和 SV 算子的完整配置参考

本页面介绍了 Canton Network 上验证器和超级验证器 (SV) 操作员可用的配置选项。它涵盖 Splice 应用程序配置、Canton 参与者设置、数据库设置、身份验证、流量管理、修剪和可观察性。

对于应用程序开发人员配置（Canton + DPM），请参阅[AppDev 配置参考](/zh/docs/canton/appdev-reference-configuration-reference)。

## 配置格式

### Helm 图表配置

使用 Helm 进行部署时，通过 Helm 值文件中的 `additionalEnvVars` 字段传递 `ADDITIONAL_CONFIG` 值。有关完整的 Helm 值集，请参阅下面的 `standalone-validator-values.yaml` 部分。

### 自定义引导脚本

自定义引导脚本在节点启动时运行 Canton Console 命令。此部分将在未来的更新中扩展。有关脚本语法和示例，请参阅 [Canton Console 脚本](/zh/docs/canton/global-synchronizer-canton-console-scripting) 页面。

## 验证器节点配置

### 所需的网络参数

您的验证器需要这些值才能连接到网络（DevNet、TestNet 或 MainNet）：

* **MIGRATION\_ID** -- 目标网络的当前迁移ID。在 [sync.global/sv-network](https://sync.global/sv-network/) 中找到它。
* **SPONSOR\_SV\_URL** -- 赞助 SV 应用程序的 URL（例如，GSF SV URL）。
* **ONBOARDING\_SECRET** -- 来自赞助商 SV 的一次性秘密。秘密将在 48 小时后过期。
* **TRUSTED\_SCAN\_URL** -- 可信 SV 的扫描 URL，用于获取 BFT 读取的附加扫描 URL。

### Helm 值：standalone-validator-values.yaml

该文件定义了验证者的身份和网络绑定：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# URL of the sponsoring SV
svSponsorAddress: "SPONSOR_SV_URL"

# Party hint: must be <organization>-<function>-<enumerator>
验证者PartyHint: "YOUR_VALIDATOR_PARTY_HINT"

# Node identifier, usually the same as your party hint
nodeIdentifier: "YOUR_VALIDATOR_NODE_NAME"

# 同步器 migration
migration:
  id: "MIGRATION_ID"
  # Uncomment when redeploying as part of a 同步器 migration:
  # migrating: true

# Database
persistence:
  secretName: postgres-secrets
  host: postgres
  databaseName: 参与方_MIGRATION_ID
  schema: 参与方
```

### Helm 值：验证者-values.yaml

该文件涵盖验证器应用程序行为、身份验证和钱包设置：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Scan endpoint for BFT reads
scanAddress: "TRUSTED_SCAN_URL"

# 钱包 admin user(s) -- full IAM user ID, e.g. auth0|43b68e1e4978b000cefba352
验证者钱包Users:
  - "OPERATOR_WALLET_USER_ID"

# Authentication
auth:
  audience: "OIDC_AUTHORITY_VALIDATOR_AUDIENCE"
  jwksUrl: "https://OIDC_AUTHORITY_URL/.well-known/jwks.json"

# Contact point visible to other operators (Slack handle or email)
contactPoint: "YOUR_CONTACT_POINT"

# 钱包 HTTP server and automations
enable钱包: true
```

### Helm 值：参与方-values.yaml

该文件配置验证器底层的 Canton 参与者：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
persistence:
  host: 参与方-pg
  port: 5432
  secretName: 参与方-pg-secret
  databaseName: 参与方_MIGRATION_ID
  schema: 参与方

auth:
  jwksUrl: "https://OIDC_AUTHORITY_URL/.well-known/jwks.json"
  targetAudience: "OIDC_AUTHORITY_LEDGER_API_AUDIENCE"

enableHealthProbes: true
```

<Note>
  在 1.24 之前的 Kubernetes 版本上，将 `enableHealthProbes` 设置为 `false` 以禁用 gRPC liveness 和 readiness 探针。
</Note>

## 同步器连接选项

默认情况下，验证器会发现多个扫描实例和定序器连接以进行 BFT 读取。这是推荐的生产配置，因为它在多个 SV 之间分配信任。

### 通过扫描代理进行 BFT（推荐）

默认行为使用 `TRUSTED_SCAN_URL` 来发现其他扫描实例和排序器端点。除了上述所需的网络参数之外，无需进行额外配置。验证器从多个扫描中读取并自动连接到多个定序器。

### 单一可信扫描

要仅连接到一个受信任的扫描（接受单点故障权衡）：```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonSv验证者TrustSingleScan: true
scanAddress: "TRUSTED_SCAN_URL"
```

### 单一可信排序器

类似地，要通过单个定序器而不是从 Scan 发现的集合进行路由：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
useSequencerConnectionsFromScan: false
decentralized同步器Url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL"
```

<警告>
  两种单一信任选项都意味着您的验证器完全依赖于该 SV。如果它离线或受到威胁，您的验证器将无法进行交易。
</警告>

## 数据库配置

### PostgreSQL 设置 (Helm)

Helm 部署的 PostgreSQL 实例和所有 Splice 应用程序共享存储在 Kubernetes 密钥中的密码。所有应用程序都使用`cnadmin`数据库用户。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic postgres-secrets \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD} \
    -n 验证者
```

要调整持久存储大小和存储类别，请将它们添加到 postgres Helm 值文件中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
db:
  volumeSize: 20Gi
  volumeStorageClass: standard-rwo
```

### PostgreSQL 配置（独立Canton）

对于连接到 PostgreSQL 的独立 Canton 参与者：

```
canton.参与方s.参与方1.storage {
  type = postgres
  config {
    dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
    properties = {
      serverName = "localhost"
      databaseName = "参与方1_db"
      portNumber = "5432"
      user = ${POSTGRES_USER}
      password = ${POSTGRES_PASSWORD}
    }
  }
}
```

Canton 使用 [HikariCP](https://github.com/brettwooldridge/HikariCP) 进行连接池。请参阅 [HikariCP 池大小调整指南](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) 了解调整建议。

### PostgreSQL SSL

使用以下 `PGSimpleDataSource` 属性在数据库连接上启用 SSL：

* `ssl = true` -- 验证 SSL 证书和主机名
* `sslmode = "verify-ca"` -- 根据根证书检查证书链
* `sslrootcert = "path/to/root.cert"` -- 根CA证书的路径

对于双向 TLS，请添加指向客户端证书和密钥的 `sslcert` 和 `sslkey`。

## 身份验证

验证器组件通过 OpenID Connect (OIDC) 提供商颁发的 JWT 令牌相互进行身份验证并向外部用户进行身份验证。完整的设置说明位于 [OIDC 提供商](/zh/docs/canton/global-synchronizer-deployment-oidc-providers) 页面。关键配置秘密是：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 验证者 backend -> participant authentication
kubectl create secret generic splice-app-验证者-ledger-api-auth \
    "--from-literal=ledger-api-user=${VALIDATOR_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${VALIDATOR_CLIENT_ID}" \
    "--from-literal=client-secret=${VALIDATOR_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}" \
    -n 验证者

# 钱包 UI
kubectl create secret generic splice-app-钱包-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${WALLET_UI_CLIENT_ID}" \
    -n 验证者

# CNS UI
kubectl create secret generic splice-app-cns-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${CNS_UI_CLIENT_ID}" \
    -n 验证者
```

要禁用身份验证（强烈建议不要在生产环境中使用），请在 `验证者-values.yaml` 和 `参与方-values.yaml` 中设置 `disableAuth: true`。

## TLS 配置

Canton API（Ledger API 和 Admin API）支持 TLS 以及可选的相互身份验证。 Ledger API 的最小服务器端 TLS 配置：

```
canton.参与方s.参与方.ledger-api.tls {
  cert-chain-file = "./tls/ledger-api.crt"
  private-key-file = "./tls/ledger-api.pem"
  trust-collection-file = "./tls/root-ca.crt"
}
```

要要求客户端证书身份验证 (mTLS)，请添加：

```
canton.参与方s.参与方.ledger-api.tls.client-auth {
  type = require
  admin-client {
    cert-chain-file = "./tls/admin-client.crt"
    private-key-file = "./tls/admin-client.pem"
  }
}
```

所有私钥必须采用 PKCS#8 PEM 格式。您还可以限制最低 TLS 版本和允许的密码套件：```
canton.参与方s.参与方.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
```

## 流量配置

您的验证器使用 Canton Coin 自动购买流量（排序器吞吐量）。在`standalone-validator-values.yaml`中配置充值行为：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
topup:
  enabled: true
  targetThroughput: 20000   # bytes/second of sequenced 流量
  minTopupInterval: "1m"    # minimum interval between purchases
```

设置`enabled: false`或`targetThroughput: 0`禁用自动充值。当前的流量参数（基本速率限制、额外流量价格、最低充值金额）记录在`AmuletRules`合约上，可以从任何Scan实例中查询。

对于 Docker Compose 部署，请将这些设置为环境变量：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export TARGET_TRAFFIC_THROUGHPUT=20000
export MIN_TRAFFIC_TOPUP_INTERVAL="1m"
```

## 参与者修剪

默认情况下，参与者保留完整的交易历史记录。启用修剪会删除早于保留窗口的历史记录，仅保留活动合约集。修剪不会影响 Splice 应用程序数据（例如，钱包历史记录永远不会被修剪）。

将其添加到`验证者-values.yaml`：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
参与方修剪Schedule:
  cron: "0 /10 * * * ?"  # every 10 minutes
  maxDuration: 5m         # max run time per iteration
  retention: 48h          # keep history newer than 48 hours
```

<警告>
  如果您的节点离线时间超过了修剪保留窗口，则当应用程序竞相追赶修剪的数据时，它可能会被损坏。将保留时间设置为反映正常运行时间保证的值 - 30 天是一个合理的起点，因为排序器也会在 30 天后进行修剪。
</警告>

有关更多详细信息，请参阅有关 [修剪操作](/global-synchronizer/product-operations/修剪#参与方-node-修剪) 的 Canton 文档。

## 监控和可观察性

### 指标端点

**Helm 部署**：在 Helm 值中设置 `metrics.enable: true` 以创建 `ServiceMonitor` 自定义资源（需要 Prometheus Operator）。或者，添加针对端口 10013 的 Prometheus 抓取注释。

**Docker Compose 部署**：默认情况下在`http://验证者.localhost/metrics`（验证器应用程序）和`http://参与方.localhost/metrics`（参与者）启用指标。

### 直方图

指标是使用 OpenTelemetry 构建的，并作为 [Prometheus 原生直方图](https://prometheus.io/docs/specs/native_histograms/) 公开。在 Prometheus 中使用 `-enable-feature=native-histograms` 启用此功能。回到常规直方图：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
ADDITIONAL_CONFIG_DISABLE_NATIVE_HISTOGRAMS="canton.monitoring.metrics.histograms=[]"
```

### 拓扑指标

验证器应用程序可以通过启用轮询触发器来导出同步器拓扑指标（前缀`splice.同步器-拓扑`）：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
ADDITIONAL_CONFIG_TOPOLOGY_METRICS_EXPORT="canton.验证者-apps.验证者_backend.automation.拓扑-metrics-polling-interval = 5m"
```

### 健康检查

所有 Splice 应用程序在端口 5003 上提供 `/readyz` 和 `/livez` 端点。在 Kubernetes 中，活动性和就绪性探针是预先配置的。您也可以手动检查它们：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl exec <pod-name> -n 验证者 -- curl -s https://localhost:5003/api/验证者/readyz
```

200 响应表明验证器运行状况良好。

### Grafana 仪表板

该发行包包括采用 Kubernetes 部署并使用 Prometheus 本机直方图查询的 Grafana 仪表板。直到并包括拼接 `0.6.4`，请使用 `grafana-dashboards/` 文件夹。从 Splice `0.6.5` 开始，验证器操作员应使用 `验证者-grafana-dashboards/`，超级验证器操作员应使用 `sv-grafana-dashboards/`。

## HTTP代理配置

如果您的环境通过 HTTP 转发代理路由出口，请在 Helm 值中设置代理主机和端口：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
```将此应用于验证者和参与者 Helm 图表。使用`https.nonProxyHosts`排除特定地址。目前不支持代理身份验证。

## 钱包自动化

### 扫描配置

当一方的余额超过阈值时，自动清除一方的资金：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
钱包Sweep:
  "<senderPartyId>":
    maxBalanceUSD: 1000
    minBalanceUSD: 100
    receiver: "<receiverPartyId>"
    useTransferPreapproval: false
```

### 自动接受转账

自动接受特定方的转让要约：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
autoAcceptTransfers:
  "<receiverPartyId>":
    fromParties:
      - "<senderPartyId>"
```

两种配置都需要参与方 ID，初始部署后可从钱包 UI 获取这些 ID。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
