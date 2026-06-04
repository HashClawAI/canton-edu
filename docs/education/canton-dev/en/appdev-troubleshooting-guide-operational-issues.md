---
title: "Operational Issues"
slug: "appdev-troubleshooting-guide-operational-issues"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/operational-issues.md"
source_title: "Operational Issues"
tags:
  - appdev
  - troubleshooting-guide
  - operational-issues
---

# Operational Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Operational Issues

> Troubleshooting traffic exhaustion, upgrade problems, and PQS failures on DevNet, TestNet, and MainNet

This page covers problems that arise when your application runs against a live network: DevNet, TestNet, or MainNet. Local development issues are covered in [Development Issues](/appdev/troubleshooting-guide/development-issues).

## Traffic Exhaustion

Every transaction on Canton Network consumes traffic, which is paid for with Canton Coin (CC). When your validator runs out of traffic, transactions are rejected.

### Symptoms

```
FAILED_PRECONDITION: INSUFFICIENT_TRAFFIC - Not enough traffic remaining
```

Or transactions time out with `MEDIATOR_SAYS_TX_TIMED_OUT` and the `unresponsiveParties` field points to your validator.

### Check your balance

Query your validator's traffic state through the Admin API:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl http://localhost/api/validator/readyz
```

You can also check the wallet UI if your validator has one configured.

### Enable auto-top-up

Configure automatic traffic purchases so your validator buys more traffic before it runs out:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# In .env or validator-values.yaml
TARGET_TRAFFIC_THROUGHPUT=20000
MIN_TRAFFIC_TOPUP_INTERVAL=1m
```

### Tap on DevNet

On DevNet, you can request free test CC from the faucet. Open the wallet UI and use the **Tap** function, or call the tap endpoint directly. Test CC has no real value and exists only for development testing.

<Note>
  On MainNet, CC has real value. Monitor your balance and set up auto-top-up before deploying production workloads.
</Note>

## Upgrade Issues

### Version skew between Daml packages

When you deploy a new version of your Daml package alongside an existing version, both must be uploaded and vetted on all validators that process your contracts. If validator A has package v2 but validator B only has v1, transactions involving both parties will fail.

```
NOT_FOUND: PACKAGE_NOT_FOUND - Could not find package <new-package-id>
```

**Fix:** Synchronize package deployment across all validators before submitting transactions that reference the new package. Use the SCU (Smart Contract Upgrade) mechanism so that existing contracts on v1 can be exercised with v2 code.

### Mixed-version deployments

If your application's backend expects a newer Daml package version than what is deployed on the validator, commands will fail at submission time. Keep your application version in sync with the deployed DAR.

After uploading a new DAR, verify it is vetted:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check uploaded packages
curl http://localhost:5002/v2/packages | jq '.package_ids'
```

### Splice version mismatches

When the network upgrades (e.g., from Splice 0.4.x to 0.5.x), your validator must run a compatible version. An incompatible validator logs errors like:

```
You don't speak 0.5.x
```

Check the current network version at [canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/) and upgrade directly to the required version. Do not step through intermediate versions.

## PQS Issues

The Participant Query Store (PQS) mirrors ledger data into a PostgreSQL database for efficient querying. Several things can go wrong.

### Connection failures

If PQS cannot reach its PostgreSQL database or the validator's Ledger API, it logs errors and stops streaming:

```
UNAVAILABLE: io exception - Connection refused to localhost:5001
```

**Checklist:**

* PostgreSQL is running and accepting connections on the configured host/port
* The PQS database user has the required permissions
* The Ledger API (gRPC) port is accessible from the PQS process
* Network policies or firewalls are not blocking the connection

### Stale data

PQS maintains a streaming connection to the Ledger API. If this connection drops, PQS may fall behind. Check the PQS offset against the ledger end:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# PQS latest offset (query PQS database)
psql -h localhost -U pqs -d pqs -c "SELECT max(offset) FROM _pqs_offsets;"

# Ledger end offset
grpcurl -plaintext localhost:5001 \
  com.daml.ledger.api.v2.StateService/GetLedgerEnd
```

If PQS is significantly behind, restart it. PQS will resume from its last committed offset.

### Schema migration with Flyway

PQS uses Flyway for database schema management. When upgrading PQS, Flyway runs migrations automatically. If a migration fails:

```
FlywayException: Validate failed: Migration checksum mismatch
```

This usually means the database was manually altered or a previous migration was partially applied. To recover:

1. Back up the PQS database
2. Check which migrations have been applied: `SELECT * FROM flyway_schema_history;`
3. If a migration is marked as failed, repair the history: `flyway repair`
4. Re-run the PQS startup

<Warning>
  Never manually edit PQS tables that Flyway manages. Schema changes should only come through PQS upgrades.
</Warning>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
