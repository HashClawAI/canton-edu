---
title: "Common Questions"
slug: "global-synchronizer-troubleshooting-guide-common-questions"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/common-questions.md"
source_title: "Common Questions"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - common-questions
---

# Common Questions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Questions

> Frequently asked questions about validator setup, operations, and upgrades

## Setup

### How do I get onboarded to TestNet or MainNet?

Onboarding to TestNet requires a Super Validator (SV) sponsor. Contact the SV you are working with, or reach out through the `#validator-operations-onboarding` Slack channel to find a sponsor. The sponsor submits a vote to approve your validator. The process typically takes 2-4 weeks.

MainNet onboarding follows the same pattern but with stricter requirements. You need a signed operator agreement and must demonstrate successful operation on TestNet. See the [onboarding process](/docs/canton/global-synchronizer-deployment-onboarding-process) documentation for the full checklist.

### What ports need to be open?

Your validator requires outbound access on:

* **TCP 443** -- HTTPS/gRPC-TLS to the synchronizer sequencer
* **TCP 5432** -- to your PostgreSQL database (if hosted externally)
* **TCP 443** -- to your OIDC provider (Auth0, Keycloak, etc.)

Inbound access depends on your setup:

* **TCP 443** -- if you expose the Ledger API or validator wallet UI externally
* **TCP 26656** -- if you run a CometBFT node (for SV operators)

DevNet additionally requires VPN connectivity.

### How much does it cost to run a validator?

Costs break down into infrastructure and network fees.

**Infrastructure costs** depend on your deployment choice. A minimal Kubernetes deployment on a cloud provider runs approximately \$500-800/month (compute, database, storage). Docker Compose on a single VM can be cheaper but is not recommended for production.

**Network fees** are paid through traffic, which is purchased with Canton Coin (CC). The amount depends on your transaction volume. Validators earn rewards that can offset these costs. Check the current reward rates on the [Global Synchronizer Foundation](https://sync.global/) website.

## Operations

### How do I check my traffic balance?

Via Canton Console:

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

Via the validator API:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s http://localhost/api/validator/readyz | jq '.traffic'
```

If the balance is low, purchase more traffic or enable auto-top-up in your `validator-values.yaml`.

### How often should I prune?

Prune frequently enough to keep the database manageable. A common schedule is every 10 minutes with 90 days of retention:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

If you run PQS (Participant Query Store) for your application, you can use a shorter retention period on the participant since PQS maintains its own data store for queries.

### What happens during a network reset?

Network resets are rare and only happen on DevNet and TestNet. During a reset:

* All ledger state is wiped
* Validator identities may need to be re-registered
* You re-onboard your validator using the same process as initial setup

MainNet has never been reset and is not expected to be. The network upgrade process (synchronizer migrations) preserves state across version changes.

## Upgrades

### Can I skip versions?

It depends on the upgrade type. For minor patch releases within the same Splice version, you can generally skip intermediate patches. For major version upgrades that involve a synchronizer migration, you must follow the specific upgrade path documented in the release notes.

If the network has moved several versions ahead while your validator was offline, upgrade directly to the current network version. Running an older version results in `You don't speak X.Y.Z` errors since the network rejects incompatible protocol versions.

### What is the difference between Type 1, Type 2, and Type 3 upgrades?

These categories describe the scope and impact of an upgrade:

* **Type 1 (patch)** -- Bug fixes and minor improvements. No synchronizer migration, no downtime expected. Apply by updating the Helm chart version and running `helm upgrade`.
* **Type 2 (minor)** -- New features or behavior changes. May require configuration updates. No synchronizer migration, but a rolling restart is needed.
* **Type 3 (major)** -- Involves a synchronizer migration. The network moves to a new synchronizer ID, and validators must update their database configuration (e.g., `participant_4` becomes `participant_5`). Coordinated across all validators with a scheduled migration window.

Check the release notes for each version to determine its upgrade type and follow the corresponding procedure.

### How do I verify my validator is running the correct version?

After upgrading, confirm the running version:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Kubernetes
kubectl -n validator get deploy validator-app \
  -o "jsonpath={.spec.template.spec.containers[0].image}"

# Docker
docker inspect validator-app --format='{{.Config.Image}}'
```

You can also check the public validator status page for your network, which shows the reported version of each registered validator.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
