---
title: "Runbooks"
slug: "global-synchronizer-troubleshooting-guide-runbooks"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/runbooks.md"
source_title: "Runbooks"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - runbooks
---

# Runbooks

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Runbooks

> Operational runbooks for common validator incidents with step-by-step procedures

Runbooks provide a structured response to known incident types. Each runbook follows the same phases: detect, assess, act, verify, and document.

## Incident Response Template

Use this template for any incident that does not have a dedicated runbook.

1. **Detect** -- Identify the symptom. How was the issue discovered? (Alert, user report, routine check.)
2. **Assess** -- Determine scope and severity. Is the validator offline? Are transactions failing? Is data at risk?
3. **Act** -- Execute the appropriate fix. Follow the relevant runbook below or the [troubleshooting methodology](/docs/canton/global-synchronizer-troubleshooting-guide-troubleshooting-methodology).
4. **Verify** -- Confirm the fix. Check health endpoints, submit a test transaction, review logs for recurring errors.
5. **Document** -- Record what happened, what caused it, what was done, and any follow-up actions.

***

## Runbook: Validator Offline

**Detection:** Health endpoint returns non-200, monitoring alert fires, or validator disappears from public network status.

**Assessment:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check pod/container status
kubectl get pods -n validator
# or
docker ps --filter "name=validator"
```

**Action:**

* If the pod is in `CrashLoopBackOff`, check logs for the root cause:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  kubectl logs -n validator deployment/validator-app --previous
  ```
* If the pod is not scheduled, check for resource quota issues or node availability:
  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  kubectl describe pod -n validator -l app=validator-app
  ```
* If the container exited with code 137, it was OOM-killed. Increase memory limits.
* If the container exited with code 1, check logs for a configuration or startup error.

**Verification:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost/api/validator/readyz
```

The endpoint should return HTTP 200.

***

## Runbook: Traffic Exhausted

**Detection:** Transactions fail with `PARTICIPANT_TRAFFIC_BELOW_LIMIT` or `MEDIATOR_SAYS_TX_TIMED_OUT` where your validator is in the `unresponsiveParties` list.

**Assessment:**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res1: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

If `availableTraffic` is 0 or traffic limits are exhausted, purchase traffic or enable auto-top-up before transactions can proceed normally.

**Action:**

1. Purchase traffic immediately:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
     -H "Authorization: Bearer $TOKEN"
   ```
2. Enable auto-top-up to prevent recurrence:
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   # In validator-values.yaml
   topup:
     enabled: true
     targetThroughput: 100000
     minTopupInterval: 10m
   ```
3. Check that the validator has sufficient Canton Coin balance to fund traffic purchases.

**Verification:** Submit a test transaction and confirm it succeeds.

***

## Runbook: Database Disk Full

**Detection:** PostgreSQL errors containing `No space left on device`, or disk usage alerts from monitoring.

**Assessment:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check disk usage
kubectl exec -n validator statefulset/postgres -- df -h /var/lib/postgresql/data
```

**Action:**

1. **Immediate relief** -- if the database is completely full, you may need to expand the PVC or free space before PostgreSQL will accept writes again.
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   # Resize PVC (if your StorageClass supports it)
   kubectl edit pvc postgres-data -n validator
   # Change spec.resources.requests.storage to a larger value
   ```
2. **Enable or fix pruning:**
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   participantPruningSchedule:
     cron: "0 */10 * * * ?"
     maxDuration: 60m
     retention: 90d
   ```
3. **Run a manual VACUUM** on PostgreSQL to reclaim space after pruning deletes rows:
   ```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   VACUUM FULL;
   ```
   Note: `VACUUM FULL` locks tables and requires approximately the same amount of free space as the table being vacuumed. Schedule during a maintenance window.

**Verification:** Confirm disk usage has dropped and the validator is processing transactions normally.

***

## Runbook: Failed Upgrade Rollback

**Detection:** After a `helm upgrade`, the validator is in a crash loop or producing `UnrecoverableError` messages.

**Assessment:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check the current release state
helm history validator -n validator

# Check pod logs for the specific error
kubectl logs -n validator deployment/validator-app --tail=200
```

**Action:**

1. **Do not** restart repeatedly -- this can worsen state corruption.
2. Roll back to the previous working Helm release:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   helm rollback validator <previous-revision> -n validator
   ```
3. If the rollback involves a synchronizer migration (Type 3 upgrade), you may also need to switch the database name back:
   ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   persistence:
     databaseName: participant_3  # Previous migration ID
   ```
4. Verify the rollback restored the previous container images:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   kubectl -n validator get deploy validator-app \
     -o "jsonpath={.spec.template.spec.containers[0].image}"
   ```
5. Once stable, investigate the upgrade failure before reattempting. Common causes: missing migration configuration, wrong database name, or incompatible values file.

**Verification:** Health endpoint returns 200 and the validator is processing transactions.

***

## Runbook: CometBFT Consensus Stall

**Detection:** This applies to Super Validator (SV) operators running CometBFT nodes. Block height stops advancing, or the CometBFT status endpoint shows no new blocks.

**Assessment:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check CometBFT status
curl -s http://localhost:26657/status | jq '.result.sync_info'
```

If `latest_block_height` has not changed in several minutes and `catching_up` is `false`, consensus has stalled.

**Action:**

1. Check the number of connected peers:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -s http://localhost:26657/net_info | jq '.result.n_peers'
   ```
   If peers have dropped below the threshold for consensus (2/3 of validators), blocks cannot be produced.

2. Check for validator signing issues:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -s http://localhost:26657/dump_consensus_state | jq '.result.round_state.votes'
   ```

3. If your own CometBFT node is the one not signing, restart it:
   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   kubectl rollout restart deployment/cometbft -n validator
   ```

4. If the stall is network-wide (multiple SV nodes are not signing), coordinate with other SV operators through the `#validator-operations` Slack channel.

**Verification:** Block height is advancing and the interval between blocks has returned to normal (typically a few seconds).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
