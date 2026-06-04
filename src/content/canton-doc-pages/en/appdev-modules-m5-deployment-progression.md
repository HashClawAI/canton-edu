---
title: "Deployment Progression"
slug: "appdev-modules-m5-deployment-progression"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-deployment-progression.md"
source_title: "Deployment Progression"
tags:
  - appdev
  - modules
  - m5-deployment-progression
---

# Deployment Progression

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Progression

> Moving your Canton application from LocalNet through DevNet, TestNet, and into MainNet production

Canton application development spans four environments, each serving a different stage of the development and deployment lifecycle. Your application moves through them sequentially: LocalNet for development, DevNet for early integration, TestNet for pre-production validation, and MainNet for production.

## Environment Overview

* **LocalNet** — Runs entirely on your machine via Docker Compose. You control all validators and the synchronizer. No external dependencies, no costs.
* **DevNet** — A shared development network operated by the Global Synchronizer Foundation. Used for early integration testing with the real Global Synchronizer infrastructure. It is periodically reset. Updates frequently and may have breaking changes.
* **TestNet** — A pre-production network that mirrors MainNet's configuration and upgrade cadence. Used for final validation before production deployment.
* **MainNet** — The production Canton Network. Real Canton Coin (CC), real traffic costs, real users.

## What Changes Between Environments

The core architecture stays the same across all four environments: your application talks to a validator's participant node via the Ledger API. What changes is the infrastructure around it.

| Category                      | LocalNet                                   | Shared Networks (DevNet / TestNet / MainNet)                                              |
| ----------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| **Identity & Authentication** | Pre-configured Keycloak with default users | Validator onboarding required + valid JWT from validator's auth provider                  |
| **Network Connectivity**      | Runs on localhost                          | Validator must connect to Global Synchronizer sequencer nodes                             |
| **Canton Coin & Traffic**     | Simulated CC and traffic provided          | Real CC required to buy traffic (auto-top-up configurable). `Tap` is available on DevNet. |
| **DAR Deployment**            | Direct DAR upload to local validators      | Upload via validator participant node; may require synchronization with counterparties    |

## Upgrade Types on the Global Synchronizer

<Note>
  For detailed upgrade procedures, see the [Validator Upgrades](/global-synchronizer/production-operations/validator-upgrades) page.
</Note>

The super validators (SVs) periodically implement upgrades to the Global Synchronizer to improve functionality, resolve issues, and introduce new features. As a node operator or application provider you should be aware of the three types of upgrades that may occur.

### Type 1: Backward-compatible changes

Type 1 upgrades involve backward-compatible changes to the Splice applications and/or modifications to the behavior of the Canton synchronization layer. These non-breaking changes occur on Mondays, every week.

While validators can operate effectively when behind by a Splice version or two, the SVs recommend keeping your node up to date with weekly upgrades. "Skip upgrades" (jumping multiple versions at once) are not officially tested by the SVs, so while they generally work, they come with increased risk.

### Type 2: Daml model changes

Type 2 upgrades modify the Daml models that underlie the Splice applications. These changes introduce a fork in the application chains and occur every few months.

The process for Type 2 upgrades begins with distribution of the new Daml models through Type 1 upgrades, followed by an offline Canton Improvement Proposal (CIP) that must be approved by the SV node owners. Next, the SVs conduct an onchain vote to establish a specific date and time when the new models take effect. At this cutoff point, only validators running the most recent Splice version can participate in transactions using the new models. Validators that haven't adopted the latest version cannot participate.

### Type 3: Non-compatible protocol changes

Type 3 upgrades involve fundamental changes to the Canton synchronization protocol. These major upgrades require downtime (sometimes called Hard Migrations) and occur every three to four months.

The implementation of Type 3 upgrades requires a Canton Improvement Proposal (CIP) approved through an offchain vote, followed by an onchain vote by the SVs to schedule the upgrade. These migrations impact all SVs and validators, requiring a coordinated transition from the prior protocol to the new one. Currently, Canton requires all nodes to migrate together during these upgrades.

## Promotion Checklist

Before promoting your application to the next environment, verify:

### LocalNet → DevNet

* All Daml Script unit tests pass (`dpm test`)
* Backend integration tests pass against LocalNet
* DARs compile cleanly (`dpm build`)
* Your validator is onboarded to DevNet
* Authentication is configured for DevNet (no more default Keycloak users)

### DevNet → TestNet

* End-to-end tests pass on DevNet with real multi-party workflows
* Your application handles Type 1 upgrades (weekly Splice updates) without breaking
* Performance under expected load is acceptable
* DAR deployment process is documented and tested
* Monitoring and alerting are configured

### TestNet → MainNet

* Full regression suite passes on TestNet
* You've successfully gone through at least one Type 1 upgrade cycle on TestNet
* Operational runbooks exist for incident response
* CC and traffic management is configured (auto-top-up, budget monitoring)
* Your organization has reviewed the DAR deployment coordination process with counterparties

Application providers should maintain nodes on DevNet, TestNet, and MainNet to guarantee smooth operations during upgrades. By maintaining nodes across all three environments you substantially increase the likelihood that MainNet upgrades proceed without disrupting your services or customers.

## Next Steps

* [Environment Configuration](/appdev/modules/m5-environment-configuration) — DPM configuration for each environment
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — Automating the promotion pipeline

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
