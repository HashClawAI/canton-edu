---
title: "Deployment Options"
slug: "global-synchronizer-deployment-deployment-options"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/deployment-options.md"
source_title: "Deployment Options"
tags:
  - global-synchronizer
  - deployment
  - deployment-options
---

# Deployment Options

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Deployment Options

> Choose between Docker Compose and Kubernetes for deploying your Canton Network validator

Canton Network validators can be deployed using Docker Compose or Kubernetes with Helm charts. Your choice depends on the target environment, operational maturity, and scale requirements.

## Docker Compose

Docker Compose is the simplest path to running a validator. It packages all components into a single-host deployment managed by a shell script.

**When to use Docker Compose:**

* LocalNet and DevNet development
* Proof-of-concept and integration testing
* Small-scale deployments without high-availability requirements
* Teams without Kubernetes expertise

**What you get:**

* Single `start.sh` / `stop.sh` workflow
* Pre-configured compose files in the Splice node bundle
* Local Traefik reverse proxy for UI routing
* Systemd integration for process management

**Limitations:**

* Runs on a single host — no built-in high availability
* Manual scaling and failover
* Not recommended for production MainNet deployments
* Database runs in-container unless you configure an external PostgreSQL instance

## Kubernetes with Helm

Kubernetes is the recommended deployment method for TestNet and MainNet. Helm charts provide parameterized configuration for all validator components.

**When to use Kubernetes:**

* TestNet and MainNet production deployments
* Environments requiring high availability and automated failover
* Organizations with existing Kubernetes infrastructure
* Deployments needing managed database services (RDS, Cloud SQL, Azure Database)

**What you get:**

* Helm charts for validator, participant, wallet UI, and CNS UI
* Managed rolling upgrades via `helm upgrade`
* Integration with cloud-native services (managed databases, KMS, monitoring)
* Ingress controller support for TLS termination and routing
* Scalable and reproducible across environments

**Requirements:**

* Kubernetes 1.27 or newer
* Helm 3.11.1 or newer
* An ingress controller (NGINX, Traefik, or cloud-native)
* External PostgreSQL (managed or self-hosted, not in-container for production)

## Cloud provider considerations

All three major cloud providers support validator deployments. The primary differences are in managed service names.

**AWS:**

* EKS for Kubernetes, RDS or Aurora for PostgreSQL
* NAT Gateway for static egress IP
* AWS KMS for key management (community edition)
* gp3 EBS volumes for storage

**Google Cloud:**

* GKE for Kubernetes, Cloud SQL for PostgreSQL
* Cloud NAT for static egress IP
* Cloud KMS for key management (community edition)
* SSD persistent disks for storage

**Azure:**

* AKS for Kubernetes, Azure Database for PostgreSQL
* NAT Gateway for static egress IP
* Premium SSD for storage

Regardless of cloud provider, place your managed database in the same region and availability zone as your Kubernetes cluster. Database latency directly affects validator performance.

## Choosing between options

For most teams, the decision comes down to environment and operational capacity:

* **Starting out or testing on DevNet** — Use Docker Compose. It gets you running in minutes with minimal infrastructure.
* **Moving to TestNet** — Either option works. Docker Compose is acceptable if you do not need high availability. Kubernetes is preferred if you want the same deployment method you will use in production.
* **MainNet production** — Use Kubernetes. The operational tooling (rolling upgrades, health checks, autoscaling) is necessary for a production validator that must maintain high availability.

<Note>
  You can start with Docker Compose on DevNet and migrate to Kubernetes for TestNet/MainNet. The validator state lives in PostgreSQL, and the onboarding identity persists across deployments as long as you retain the database.
</Note>

## Super Validator deployments

Super Validators must use Kubernetes. The additional components (CometBFT node, sequencer, mediator, SV app, Scan service) require orchestration that Docker Compose does not support at production scale. See the [Kubernetes Deployment](/global-synchronizer/deployment/kubernetes-deployment) guide.

## Next steps

<CardGroup cols={2}>
  <Card title="Prerequisites" icon="list-check" href="/global-synchronizer/deployment/prerequisites">
    System requirements for your chosen deployment method.
  </Card>

  <Card title="Docker Compose validator deployment" icon="docker" href="/global-synchronizer/deployment/validator-docker-compose">
    Step-by-step Docker Compose validator deployment.
  </Card>

  <Card title="Kubernetes validator deployment" icon="dharmachakra" href="/global-synchronizer/deployment/validator-kubernetes">
    Step-by-step Kubernetes validator deployment with Helm charts.
  </Card>
</CardGroup>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
