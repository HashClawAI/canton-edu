---
title: "Package Management"
slug: "appdev-modules-m7-package-management"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-package-management.md"
source_title: "Package Management"
tags:
  - appdev
  - modules
  - m7-package-management
---

# Package Management

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Package Management

> Managing DAR files across environments, version pinning, dependency management, and coordinating package distribution

Daml packages (DARs) are the deployment units for on-ledger logic. Managing them across environments and organizations requires more oversight than typical software artifacts because every validator that participates in a workflow needs the same packages.

## DAR Lifecycle

A DAR file goes through several stages:

1. **Build** — `dpm build` compiles your Daml source into a DAR. The output is deterministic: the same source and SDK version produces the same DAR.
2. **Test** — Upload the DAR to a sandbox or LocalNet and run your test suite against it.
3. **Store** — Publish the DAR to an artifact repository (Artifactory, Nexus, S3, or your CI system's artifact storage).
4. **Distribute** — Share the DAR with counterparties who need it on their validators.
5. **Deploy** — Upload the DAR to production validators and vet it.
6. **Deprecate** — After a successful upgrade cycle, unvet old package versions.

## Version Pinning

Pin the SDK version in your `daml.yaml` to avoid accidental upgrades:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: 3.4.9
name: com-example-licensing
version: 1.2.0
```

Run `dpm install package` to install the SDK version specified in `daml.yaml`. The pinned `sdk-version` field ensures everyone on the team builds with the same SDK version.

## Dependency Management

Multi-package projects use `multi-package.yaml` to declare dependencies between packages. `dpm build` resolves and builds them in topological order.

For external dependencies (packages published by other organizations), manage them as DAR files in your project:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml.yaml
dependencies:
  - daml-prim
  - daml-stdlib
  - ./deps/com-acme-tokens-1.0.0.dar
```

Store dependency DARs in your repository or use environment variable interpolation to pull them from a shared artifact store:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
  - daml-prim
  - daml-stdlib
  - ${DEPS_DIR}/com-acme-tokens-1.0.0.dar
```

When a dependency publishes a new version, test your packages against it before updating the pinned version. Dependency updates can change the behavior of interfaces and choices your code uses.

## Artifact Repositories

Store production DARs in a dedicated artifact repository alongside version metadata. A typical structure:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
artifacts/
├── com-example-licensing/
│   ├── 1.0.0/
│   │   ├── com-example-licensing-1.0.0.dar
│   │   └── metadata.json
│   └── 1.1.0/
│       ├── com-example-licensing-1.1.0.dar
│       └── metadata.json
```

DARs are small, so checking them into version control is also a viable approach for smaller projects. The advantage of a dedicated repository is that it separates artifact management from source control and makes distribution to counterparties easier.

## Distributing Packages to Counterparties

The same DAR files must be deployed on all validators hosting parties involved in the workflow. Daml code defines the API for state and workflows synchronized across validators, similar to `.proto` files for a gRPC server shared with gRPC client developers.

It is recommended to store Daml code in a separate repo from backend and frontend code and provide app user organizations with a tarball or read-only access to this repo. This allows organizations to review and build the code to ensure confidence in the behavior of the DAR file installed on their validators.

Practical steps for distribution:

* Publish DARs to a shared artifact repository that counterparties can access
* Provide build instructions so counterparties can compile from source and verify the DAR matches
* Include a changelog documenting what changed between versions
* Communicate upgrade timelines (see [Upgrade Deployment](/docs/canton/appdev-modules-m6-deployment))

## Package Modularization

* **Stakeholder-oriented modules** — Modularize workflows based on stakeholder interaction to simplify upgrades and maintain privacy. DAR files only need to be distributed to validators hosting the parties involved in the workflow.
* **Public and private APIs** — Minimize public workflows and store internal workflows in separate DAR files to allow more flexibility in adapting to evolving business needs.  Separate interface definitions in their own package for better workflow management.  Use interface definitions to specify public APIs which will make application upgrades easier.
* **Test code separation** — Keep test code in separate DAR files from production code. Test DARs should not be deployed to production validators.

## Next Steps

* [Security Best Practices](/docs/canton/appdev-modules-m7-security) — Securing your packages and deployment pipeline
* [Performance](/docs/canton/appdev-modules-m7-performance) — Optimization strategies for Canton applications

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
