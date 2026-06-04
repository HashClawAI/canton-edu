---
title: "Installation Issues"
slug: "global-synchronizer-troubleshooting-guide-installation-issues"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/installation-issues.md"
source_title: "Installation Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - installation-issues
---

# Installation Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation Issues

> Resolving Docker, Kubernetes, and network problems during validator installation

Installation failures typically fall into three categories: container runtime issues, Kubernetes provisioning problems, or network-level blocks that prevent your validator from reaching the synchronizer.

## Docker Issues

### Image Pull Failures

If `docker compose up` fails with an image pull error:

```
Error response from daemon: pull access denied for digitalasset/canton-participant
```

Possible causes:

* You are not logged in to the container registry. Run `docker login digitalasset-docker.jfrog.io` with your JFrog credentials.
* Your JFrog account does not have access to the required repositories. Request access through [support.digitalasset.com](https://support.digitalasset.com).
* A typo in the image tag. Verify the image name and version in your `docker-compose.yaml` or `.env` file against the release notes.

### Resource Limits

Containers that crash immediately or show `OOMKilled` status need more memory.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check if any container was OOM-killed
docker inspect --format='{{.State.OOMKilled}}' <container_name>
```

Minimum resource requirements for a validator:

* **Memory:** 8 GB allocated to Docker
* **CPU:** 4 cores
* **Disk:** 50 GB free

For Colima users on macOS:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
colima stop
colima start --memory 8 --cpu 4 --disk 100
```

### Volume Permission Errors

If a container fails with permission denied errors on mounted volumes:

```
java.io.IOException: Permission denied: /data/canton
```

The container user (typically UID 1000) must have write access to the host directory. Fix this with:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo chown -R 1000:1000 ./data
```

## Kubernetes Issues

### Helm Chart Errors

Common Helm failures during `helm install` or `helm upgrade`:

* **`Error: INSTALLATION FAILED: cannot re-use a name that is still in use`** -- A previous release exists. Use `helm upgrade` instead, or uninstall first with `helm uninstall validator -n validator`.
* **`Error: template: splice-validator/templates/...: ... not defined`** -- Your values file references a variable that does not exist in this chart version. Compare your `validator-values.yaml` against the chart's `values.yaml` for the target version.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Inspect the chart's default values
helm show values splice-validator/splice-validator --version 0.5.4
```

### PVC Provisioning Failures

If pods remain in `Pending` state, check PersistentVolumeClaim (PVC) events:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl describe pvc -n validator
```

Common causes:

* The StorageClass does not exist in your cluster. List available classes with `kubectl get storageclass`.
* Insufficient disk quota in your cloud provider account.
* The requested storage size exceeds available capacity.

### Init Container Failures

If the main container never starts, an init container may be failing:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl logs -n validator <pod-name> -c init-db --previous
```

Init containers commonly fail due to database connectivity issues -- the PostgreSQL instance is unreachable or the credentials are wrong.

### Image Pull Secrets

Kubernetes needs explicit credentials to pull from private registries:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret docker-registry jfrog-creds \
  --docker-server=digitalasset-docker.jfrog.io \
  --docker-username=$JFROG_USER \
  --docker-password=$JFROG_TOKEN \
  -n validator
```

Then reference `jfrog-creds` in your `validator-values.yaml` under `imagePullSecrets`.

## Network Issues

### DNS Resolution

If your validator cannot resolve synchronizer hostnames:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# From inside a Kubernetes pod
kubectl exec -n validator deployment/validator-app -- nslookup sequencer.sync.global
```

If DNS fails, check your cluster's CoreDNS pods and any custom DNS configuration.

### Firewall Rules

Your validator needs outbound access on the following ports:

* **443 (HTTPS/gRPC-TLS)** -- to the synchronizer sequencer
* **5432** -- to your PostgreSQL database (if external)
* **443** -- to your OIDC provider (if using authentication)

Test connectivity:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nc -zv sequencer.sync.global 443
nc -zv sequencer.test.sync.global 443
```

If connections time out, work with your network team to open the required egress rules. For DevNet, you also need VPN connectivity to the DevNet sequencer.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
