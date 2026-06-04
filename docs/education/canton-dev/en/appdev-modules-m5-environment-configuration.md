---
title: "Environment Configuration"
slug: "appdev-modules-m5-environment-configuration"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-environment-configuration.md"
source_title: "Environment Configuration"
tags:
  - appdev
  - modules
  - m5-environment-configuration
---

# Environment Configuration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Environment Configuration

> Configuring DPM, project settings, and authentication for different Canton Network environments

Canton applications need different configurations for each environment — LocalNet, DevNet, TestNet, and MainNet. This page covers the configuration layers you work with: DPM global settings, project-level `daml.yaml`, environment variables, and authentication setup.

## DPM Configuration

DPM is Daml's package manager.

`dpm` can be configured through a config file and environment variables simultaneously. Environment variables take precedence over the config file.

### Config file

The config file lives at `${DPM_HOME}/dpm-config.yaml`:

* `registry` — Override the default location where `dpm` pulls SDKs and SDK components. Defaults to `europe-docker.pkg.dev/da-images/public` for stable releases. Use `europe-docker.pkg.dev/da-images/public-unstable` for unstable releases.
* `registry-auth-path` — Override the default auth file for the registry.
* `insecure` — Allow `dpm` to pull from insecure (HTTP) registries.

### Environment variables

These override the corresponding config file settings:

* `DPM_REGISTRY` — Registry location for SDK pulls
* `DPM_REGISTRY_AUTH` — Auth file for registry access
* `DPM_INSECURE_REGISTRY` — Allow insecure registry connections
* `DPM_LOG_LEVEL` — Log level for commands like `dpm install` and `dpm version` (`debug`, `info`, `error`, `warn`)
* `DAML_PACKAGE` — Run `dpm` commands in a package context without being in its directory (e.g., `DAML_PACKAGE=/path/to/package`)
* `DPM_SDK_VERSION` — Override the SDK version globally. This overrides the `sdk-version` in all `daml.yaml` files. It does not affect `dpm install`.

## Project Configuration

### daml.yaml

Each Daml package has a `daml.yaml` that specifies the SDK version, package name, source location, and dependencies. The `dpm build` command uses this file to resolve dependencies and compile the project.

### multi-package.yaml

For projects with multiple connected Daml packages, `multi-package.yaml` tells `dpm` how to find and build them:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  packages:
    - ./path/to/package/a
    - ./path/to/package/b

```

`dpm` builds these packages in topological order based on their dependencies.

### Environment variable interpolation

Both `daml.yaml` and `multi-package.yaml` support environment variable interpolation on all string fields. Use `${MY_VARIABLE}` syntax:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: ${SDK_VERSION}
name: ${PROJECT_NAME}_test
source: daml
version: ${PROJECT_VERSION}
dependencies:
  - ${DEPENDENCY_DIRECTORY}/my-dependency-1.0.0.dar
```

Escape with `\` prefix: `\${NOT_INTERPOLATED}`.

This is useful for extracting common values like SDK version and package version into `.envrc` files or build system variables. It also allows passing dependency DARs through environment variables, which is helpful when a build system manages DAR artifacts in a cache.

## Per-Environment Settings

Each environment typically needs different values for a small set of configuration points. Here's a pattern for managing them.

### LocalNet

LocalNet is self-contained. The cn-quickstart Makefile and Docker Compose configuration handle most settings:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# .envrc (or .envrc.private for overrides)
export PARTY_HINT="your-company"
export DAML_SDK_VERSION="3.4.9"
```

Authentication uses the bundled Keycloak instance with default users (`app-user`, `app-provider`, `sv`).

### DevNet / TestNet / MainNet

For shared networks, you configure connection details and authentication:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Environment-specific settings
export LEDGER_HOST="your-validator.example.com"
export LEDGER_GRPC_PORT="5001"    # gRPC Ledger API port (depends on validator config)
export LEDGER_HTTP_PORT="7575"    # HTTP JSON API port (depends on validator config)
export AUTH_URL="https://auth.your-validator.example.com"
export AUTH_CLIENT_ID="your-app-client-id"
```

The Ledger API endpoints, auth provider URLs, and party identifiers differ per environment. Store these in environment-specific files (`.envrc.devnet`, `.envrc.testnet`, `.envrc.mainnet`) and load the appropriate one.

## Authentication Configuration

Canton validators protect the Ledger API with JWT-based authentication. Your application needs a valid token to submit commands and read transactions.

### LocalNet with Keycloak

The cn-quickstart LocalNet includes a pre-configured Keycloak instance. Obtain tokens through the Keycloak token endpoint:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "http://localhost:8080/realms/canton/protocol/openid-connect/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=your-app" \
  -d "client_secret=your-secret"
```

### Production environments

On DevNet, TestNet, and MainNet, your validator's auth provider issues tokens. The exact mechanism depends on your validator's IAM setup, but the flow is the same: your application obtains a JWT and includes it in Ledger API requests as a Bearer token.

For gRPC clients, set the token as a call credential. For HTTP/JSON requests, include it in the `Authorization` header.

## Overriding SDK Components (Advanced)

<Warning>
  This is an advanced topic. Override SDK components only with guidance from support in the context of a specific incident or compatibility issue.
</Warning>

`dpm` supports overriding individual SDK components for a single package or an entire multi-package project. In `daml.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: 3.4.9
override-components:
  damlc:
    version: 3.4.0-snapshot.20251007.14274.0.ve2024cd6
```

In `multi-package.yaml`, the same `override-components` block applies to all packages. When both files specify overrides, `dpm` applies `multi-package.yaml` overrides first, then `daml.yaml` overrides on top (giving `daml.yaml` the highest precedence).

Install overridden components with:

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    dpm install package

```

## Next Steps

* [Deployment Progression](/appdev/modules/m5-deployment-progression) — Environment differences and promotion checklist
* [CI/CD Integration](/appdev/modules/m5-ci-cd-integration) — Using environment configuration in automated pipelines

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
