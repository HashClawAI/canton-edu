---
title: "Disaster Recovery"
slug: "global-synchronizer-production-operations-disaster-recovery"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/disaster-recovery.md"
source_title: "Disaster Recovery"
tags:
  - global-synchronizer
  - production-operations
  - disaster-recovery
---

# Disaster Recovery

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Disaster Recovery

> Recovery procedures for data corruption, SV re-onboarding, and CometBFT layer loss

There are three ways to recover from disasters:

1. In simple cases where only a single node is affected but the overall network is still healthy, a Restore from backup is usually sufficient.
2. If a full backup is unavailable but an identities backup has been created, the balance of the SV can be recovered on a dedicated validator but the SV must be onboarded as a separate node.

## Restoring From Data Corruption

While all components in the system are designed to be crash-fault-tolerant, there is always a chance of failures from which the system cannot immediately recover, e.g. due to misconfiguration or bugs. In such cases, we will need to restore a component, a full SV node, or even the whole network, from backups or from dumps from components that are still operational.

### Restoring a single component from backups

If a single component in an SV node is corrupted, it should be recoverable from backups without restoring the whole node. This scenario is not yet tested enough to be advisable for production. Moreover, there are certain dependencies between the components that are not yet documented here.

### Restoring a full SV node from backups

Assuming backups have been taken for the storage and DBs of all components per the instructions in `sv_backups`, the entire node can be restored from backups. Recall that in order for a set of backup snapshots to be consistent, the backup taken from the apps database instance must be taken at a time strictly earlier than that of the participant.

Assuming such a consistent set of backups is available, the following steps can be taken to restore the node:

Scale down all components in the SV node to 0 replicas (replace `-0` with the correct serial ID in case a logical synchronizer upgrade has already been performed):

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl scale deployment --replicas=0 -n sv \
  global-domain-0-cometbft \
  global-domain-0-mediator \
  global-domain-0-sequencer \
  participant \
  scan-app \
  sv-app \
  validator-app
```

Restore the storage and DBs of all components from the backups. The exact process for this depends on the storage and DBs used by the components, and is not documented here.

Once all storage has been restored, scale up all components in the SV node back to 1 replica (replace `-0` with the correct serial ID in case a logical synchronizer upgrade has already been performed):

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl scale deployment --replicas=1 -n sv \
  global-domain-0-cometbft \
  global-domain-0-mediator \
  global-domain-0-sequencer \
  participant \
  scan-app \
  sv-app \
  validator-app
```

Once all components are healthy again, they should start catching up their state from peer SVs, and eventually become functional again.

## Re-onboard an SV and recover Amulets with a validator

In the case of a catastrophic failure of the SV node, the amulets owned by the SV can be recovered via deploying a standalone validator node with control over the SV's participant keys. The SV node can be re-onboarded with a new identity and the amulets can be transferred from the validator to the new SV node.

In order to be able to recover the amulet, the backup of the identities of your SV node is required. The details of fetching the identities are provided in the Backup of Node Identities section.

From the backup of Node Identities, copy the content of the field `identities.participant` and save it as a separate JSON file. This file will be used as identities bootstrap dump for the validator runbook.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
jq '.identities.participant' backup.json > dump.json
```

Once the failed SV node is offboarded by a majority of SVs (via a governance vote on a `OffboardMember` action), we can deploy a standalone validator node for recovering the SV's amulets.

Repeat the steps described in `helm-validator-install` for installing the validator app and participant,

While doing so, please note the following:

* Modify the file `splice-node/examples/sv-helm/standalone-validator-values.yaml` so that `validatorPartyHint` is set to the name you chose when creating the SV identity.
* Follow the notes in Restoring from a Participant Identities Dump to restore the validator with the identities from the backup. Use the separate JSON file prepared previously.

Once the validator is up and running, login to the wallet of the validator `https://wallet.validator.YOUR_HOSTNAME` with the validator user account setup in `helm-validator-auth0`. Confirm that the wallet balance is as expected. It should be the same as the amount that the original SV owned.

You can now deploy and onboard a fresh SV node (reusing your SV identity but otherwise starting with a clean slate) by following the steps in `helm-sv-install`.

Login to the wallet of the new SV node, copy the new party ID. Switch to the wallet of the validator, create a new transfer offer sending the amulets to the new SV node with the copied party ID.

Switch to the wallet of the new SV node, accept the transfer offer from the wallet of the new SV node, and verify that the amulets have arrived as expected.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
