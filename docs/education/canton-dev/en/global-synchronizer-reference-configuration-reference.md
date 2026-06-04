---
title: "Configuration Reference"
slug: "global-synchronizer-reference-configuration-reference"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/configuration-reference.md"
source_title: "Configuration Reference"
tags:
  - global-synchronizer
  - reference
  - configuration-reference
---

# Configuration Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration Reference

> Complete configuration reference for Canton Network validator and SV operators

This page covers the configuration options available to validator and Super Validator (SV) operators on Canton Network. It covers Splice app configuration, Canton participant settings, database setup, authentication, traffic management, pruning, and observability.

For application developer configuration (Canton + DPM), see the [AppDev Configuration Reference](/appdev/reference/configuration-reference).

## Configuration format

### Helm chart configuration

When deploying with Helm, pass `ADDITIONAL_CONFIG` values through the `additionalEnvVars` field in your Helm values file. See the `standalone-validator-values.yaml` section below for the full set of Helm values.

### Custom bootstrap scripts

Custom bootstrap scripts run Canton Console commands at node startup. This section will be expanded in a future update. See the [Canton Console Scripting](/global-synchronizer/canton-console/scripting) page for script syntax and examples.

## Validator node configuration

### Required network parameters

Your validator needs these values to connect to a network (DevNet, TestNet, or MainNet):

* **MIGRATION\_ID** -- The current migration ID of the target network. Find it at [sync.global/sv-network](https://sync.global/sv-network/).
* **SPONSOR\_SV\_URL** -- The URL of your sponsoring SV's app (e.g., the GSF SV URL).
* **ONBOARDING\_SECRET** -- A one-time secret from your sponsor SV. Secrets expire after 48 hours.
* **TRUSTED\_SCAN\_URL** -- The Scan URL of a trusted SV, used to obtain additional Scan URLs for BFT reads.

### Helm values: standalone-validator-values.yaml

This file defines your validator's identity and network binding:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# URL of the sponsoring SV
svSponsorAddress: "SPONSOR_SV_URL"

# Party hint: must be <organization>-<function>-<enumerator>
validatorPartyHint: "YOUR_VALIDATOR_PARTY_HINT"

# Node identifier, usually the same as your party hint
nodeIdentifier: "YOUR_VALIDATOR_NODE_NAME"

# Synchronizer migration
migration:
  id: "MIGRATION_ID"
  # Uncomment when redeploying as part of a synchronizer migration:
  # migrating: true

# Database
persistence:
  secretName: postgres-secrets
  host: postgres
  databaseName: participant_MIGRATION_ID
  schema: participant
```

### Helm values: validator-values.yaml

This file covers the validator app behavior, authentication, and wallet settings:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Scan endpoint for BFT reads
scanAddress: "TRUSTED_SCAN_URL"

# Wallet admin user(s) -- full IAM user ID, e.g. auth0|43b68e1e4978b000cefba352
validatorWalletUsers:
  - "OPERATOR_WALLET_USER_ID"

# Authentication
auth:
  audience: "OIDC_AUTHORITY_VALIDATOR_AUDIENCE"
  jwksUrl: "https://OIDC_AUTHORITY_URL/.well-known/jwks.json"

# Contact point visible to other operators (Slack handle or email)
contactPoint: "YOUR_CONTACT_POINT"

# Wallet HTTP server and automations
enableWallet: true
```

### Helm values: participant-values.yaml

This file configures the Canton participant that underlies the validator:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
persistence:
  host: participant-pg
  port: 5432
  secretName: participant-pg-secret
  databaseName: participant_MIGRATION_ID
  schema: participant

auth:
  jwksUrl: "https://OIDC_AUTHORITY_URL/.well-known/jwks.json"
  targetAudience: "OIDC_AUTHORITY_LEDGER_API_AUDIENCE"

enableHealthProbes: true
```

<Note>
  On Kubernetes versions earlier than 1.24, set `enableHealthProbes` to `false` to disable gRPC liveness and readiness probes.
</Note>

## Synchronizer connection options

By default, the validator discovers multiple Scan instances and sequencer connections for BFT reads. This is the recommended production configuration, as it distributes trust across multiple SVs.

### BFT via Scan proxy (recommended)

The default behavior uses the `TRUSTED_SCAN_URL` to discover additional Scan instances and sequencer endpoints. No extra configuration is needed beyond the required network parameters above. The validator reads from multiple Scans and connects to multiple sequencers automatically.

### Single trusted Scan

To connect to only one trusted Scan instead (accepting the single-point-of-failure trade-off):

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonSvValidatorTrustSingleScan: true
scanAddress: "TRUSTED_SCAN_URL"
```

### Single trusted sequencer

Similarly, to route through a single sequencer instead of the set discovered from Scan:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
useSequencerConnectionsFromScan: false
decentralizedSynchronizerUrl: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL"
```

<Warning>
  Both single-trust options mean your validator depends entirely on that one SV. If it is offline or compromised, your validator cannot transact.
</Warning>

## Database configuration

### PostgreSQL setup (Helm)

The Helm-deployed PostgreSQL instance and all Splice apps share a password stored in a Kubernetes secret. All apps use the `cnadmin` database user.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic postgres-secrets \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD} \
    -n validator
```

To adjust persistent storage size and storage class, add these to your postgres Helm values file:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
db:
  volumeSize: 20Gi
  volumeStorageClass: standard-rwo
```

### PostgreSQL configuration (standalone Canton)

For a standalone Canton participant connected to PostgreSQL:

```
canton.participants.participant1.storage {
  type = postgres
  config {
    dataSourceClassName = "org.postgresql.ds.PGSimpleDataSource"
    properties = {
      serverName = "localhost"
      databaseName = "participant1_db"
      portNumber = "5432"
      user = ${POSTGRES_USER}
      password = ${POSTGRES_PASSWORD}
    }
  }
}
```

Canton uses [HikariCP](https://github.com/brettwooldridge/HikariCP) for connection pooling. See the [HikariCP pool sizing guide](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) for tuning recommendations.

### PostgreSQL SSL

Enable SSL on the database connection with these `PGSimpleDataSource` properties:

* `ssl = true` -- verify the SSL certificate and hostname
* `sslmode = "verify-ca"` -- check the certificate chain against the root certificate
* `sslrootcert = "path/to/root.cert"` -- path to the root CA certificate

For mutual TLS, add `sslcert` and `sslkey` pointing to the client certificate and key.

## Authentication

Validator components authenticate to each other and to external users through JWT tokens issued by an OpenID Connect (OIDC) provider. Full setup instructions are on the [OIDC Providers](/global-synchronizer/deployment/oidc-providers) page. The key configuration secrets are:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Validator backend -> participant authentication
kubectl create secret generic splice-app-validator-ledger-api-auth \
    "--from-literal=ledger-api-user=${VALIDATOR_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${VALIDATOR_CLIENT_ID}" \
    "--from-literal=client-secret=${VALIDATOR_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}" \
    -n validator

# Wallet UI
kubectl create secret generic splice-app-wallet-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${WALLET_UI_CLIENT_ID}" \
    -n validator

# CNS UI
kubectl create secret generic splice-app-cns-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${CNS_UI_CLIENT_ID}" \
    -n validator
```

To disable authentication (strongly discouraged for production), set `disableAuth: true` in both `validator-values.yaml` and `participant-values.yaml`.

## TLS configuration

Canton APIs (Ledger API and Admin API) support TLS with optional mutual authentication. A minimal server-side TLS configuration for the Ledger API:

```
canton.participants.participant.ledger-api.tls {
  cert-chain-file = "./tls/ledger-api.crt"
  private-key-file = "./tls/ledger-api.pem"
  trust-collection-file = "./tls/root-ca.crt"
}
```

To require client certificate authentication (mTLS), add:

```
canton.participants.participant.ledger-api.tls.client-auth {
  type = require
  admin-client {
    cert-chain-file = "./tls/admin-client.crt"
    private-key-file = "./tls/admin-client.pem"
  }
}
```

All private keys must be in PKCS#8 PEM format. You can also restrict the minimum TLS version and allowed cipher suites:

```
canton.participants.participant.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
```

## Traffic configuration

Your validator automatically purchases traffic (sequencer throughput) using Canton Coin. Configure the top-up behavior in `standalone-validator-values.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
topup:
  enabled: true
  targetThroughput: 20000   # bytes/second of sequenced traffic
  minTopupInterval: "1m"    # minimum interval between purchases
```

Set `enabled: false` or `targetThroughput: 0` to disable automatic top-ups. Current traffic parameters (base rate limits, extra traffic price, minimum top-up amount) are recorded on the `AmuletRules` contract and can be queried from any Scan instance.

For Docker Compose deployments, set these as environment variables instead:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export TARGET_TRAFFIC_THROUGHPUT=20000
export MIN_TRAFFIC_TOPUP_INTERVAL="1m"
```

## Participant pruning

By default, participants preserve full transaction history. Enabling pruning removes history older than the retention window, keeping only the active contract set. Pruning does not affect Splice app data (wallet history, for example, is never pruned).

Add this to `validator-values.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 /10 * * * ?"  # every 10 minutes
  maxDuration: 5m         # max run time per iteration
  retention: 48h          # keep history newer than 48 hours
```

<Warning>
  If your node is offline longer than the pruning retention window, it may become corrupted as apps race to catch up with pruned data. Set the retention to a value that reflects your uptime guarantee -- 30 days is a reasonable starting point, since sequencers are also pruned after 30 days.
</Warning>

See the Canton documentation on [pruning operations](/global-synchronizer/production-operations/pruning#participant-node-pruning) for more details.

## Monitoring and observability

### Metrics endpoint

**Helm deployments**: set `metrics.enable: true` in your Helm values to create a `ServiceMonitor` custom resource (requires the Prometheus Operator). Alternatively, add Prometheus scrape annotations targeting port 10013.

**Docker Compose deployments**: metrics are enabled by default at `http://validator.localhost/metrics` (validator app) and `http://participant.localhost/metrics` (participant).

### Histograms

Metrics are built with OpenTelemetry and exposed as [Prometheus native histograms](https://prometheus.io/docs/specs/native_histograms/). Enable this in Prometheus with `-enable-feature=native-histograms`. To fall back to regular histograms:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
ADDITIONAL_CONFIG_DISABLE_NATIVE_HISTOGRAMS="canton.monitoring.metrics.histograms=[]"
```

### Topology metrics

The validator app can export synchronizer topology metrics (prefixed `splice.synchronizer-topology`) by enabling a polling trigger:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
ADDITIONAL_CONFIG_TOPOLOGY_METRICS_EXPORT="canton.validator-apps.validator_backend.automation.topology-metrics-polling-interval = 5m"
```

### Health checks

All Splice apps provide `/readyz` and `/livez` endpoints on port 5003. In Kubernetes, liveness and readiness probes are preconfigured. You can also check them manually:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl exec <pod-name> -n validator -- curl -s https://localhost:5003/api/validator/readyz
```

A 200 response indicates the validator is healthy.

### Grafana dashboards

The release bundle includes Grafana dashboards that assume a Kubernetes deployment and use Prometheus native histogram queries. Up to and including Splice `0.6.4`, use the `grafana-dashboards/` folder. Starting with Splice `0.6.5`, Validator operators should use `validator-grafana-dashboards/`, and Super Validator operators should use `sv-grafana-dashboards/`.

## HTTP proxy configuration

If your environment routes egress through an HTTP forward proxy, set the proxy host and port in your Helm values:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
```

Apply this to both the validator and participant Helm charts. Use `https.nonProxyHosts` to exclude specific addresses. Proxy authentication is not currently supported.

## Wallet automations

### Sweep configuration

Automatically sweep funds from a party when its balance exceeds a threshold:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
walletSweep:
  "<senderPartyId>":
    maxBalanceUSD: 1000
    minBalanceUSD: 100
    receiver: "<receiverPartyId>"
    useTransferPreapproval: false
```

### Auto-accept transfers

Automatically accept transfer offers from specific parties:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
autoAcceptTransfers:
  "<receiverPartyId>":
    fromParties:
      - "<senderPartyId>"
```

Both configurations require party IDs, which are available from the wallet UI after initial deployment.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
