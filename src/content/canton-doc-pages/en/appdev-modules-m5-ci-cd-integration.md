---
title: "CI/CD Integration"
slug: "appdev-modules-m5-ci-cd-integration"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-ci-cd-integration.md"
source_title: "CI/CD Integration"
tags:
  - appdev
  - modules
  - m5-ci-cd-integration
---

# CI/CD Integration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# CI/CD Integration

> Building CI/CD pipelines for Canton applications with dpm build, test, and deployment automation

A CI/CD pipeline for Canton applications follows the same structure as any other software project: build, package, test, deploy. The Canton-specific parts are the `dpm` commands for compiling Daml, running Script tests, and managing DAR artifacts.

## Pipeline Structure

A typical pipeline has four stages:

1. **Build** — Compile Daml code and generate client bindings
2. **Package** — Produce deployable artifacts (DARs, container images)
3. **Test** — Run Daml Script unit tests and backend integration tests
4. **Deploy** — Upload DARs and deploy off-ledger services to the target environment

## Build Stage

The build stage compiles your Daml packages and generates code bindings for your backend and frontend.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Install the SDK version from daml.yaml
`dpm install` <<version>>

# Compile Daml to DAR
dpm build

# Generate Java bindings
dpm codegen-java .daml/dist/<<your-project.dar>> -o <<output-directory>>

# Generate TypeScript bindings (if needed)
dpm codegen-js .daml/dist/<<your-project.dar>> -o <<output directory>>
```

For multi-package projects, `dpm build` in the root directory builds all packages in dependency order when a `multi-package.yaml` is present.

### Build caching

DAR compilation is deterministic: the same source code and SDK version produces the same DAR. Cache the `.daml/dist/` directory between CI runs to skip recompilation when Daml source hasn't changed. Most CI systems (GitHub Actions, GitLab CI, Jenkins) support caching by file hash.

## Test Stage

### Daml Script tests

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm test
```

This runs all `Script ()` declarations in your test package against the Sandbox. If any assertion fails, `dpm test` exits with a non-zero code and the pipeline fails.

For projects with separate test packages, run `dpm test` from each test package directory, or use a `multi-package.yaml` that includes the test packages.

### Backend integration tests

After Daml tests pass, run your backend's integration tests against a sandbox:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Start sandbox in the background
dpm sandbox &
SANDBOX_PID=$!

# Wait for sandbox to be ready
sleep 30  # Or use a health check loop

# Run backend tests, e.g. for a Java backend
cd backend && ./gradlew test

# Clean up
kill $SANDBOX_PID
```

For tests that need a full multi-validator setup, start [LocalNet](/appdev/modules/m5-localnet-development) with Docker Compose instead of the sandbox. This is heavier but covers cross-validator scenarios.

## Package Stage

### DAR artifacts

The `.dar` files produced by `dpm build` are your primary Daml artifacts. Store them in your CI artifact repository (Artifactory, Nexus, S3, or the CI system's built-in artifact storage) with version metadata.

A naming convention that includes the version simplifies tracking:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
your-app-1.0.0.dar
your-app-1.1.0.dar
```

The version in the DAR comes from the `version` field in `daml.yaml`. Use environment variable interpolation to set it from your CI pipeline:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# daml.yaml
version: ${PROJECT_VERSION}
```

### Container images

If your backend and frontend are containerized, build and tag images in this stage. Include the DAR as an embedded artifact or mount it at deployment time.

## Deploy Stage

Deployment to each environment involves two parts: uploading the DAR to the validator and deploying off-ledger services (backend, frontend, PQS).

### DAR upload

Upload your DAR to the target validator through the participant's HTTP Ledger API:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "https://${LEDGER_HOST}:${LEDGER_HTTP_PORT}/v2/packages" \
  -H "Authorization: Bearer ${AUTH_TOKEN}" \
  -H "Content-Type: application/octet-stream" \
  --data-binary @.daml/dist/your-project.dar
```

Verify the upload:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -s "https://${LEDGER_HOST}:${LEDGER_HTTP_PORT}/v2/packages" \
  -H "Authorization: Bearer ${AUTH_TOKEN}"
```

### Environment promotion

Use your CI system's environment or stage abstractions to gate promotions. A common pattern:

* Pushes to `main` deploy to DevNet automatically
* A manual approval gate promotes from DevNet to TestNet
* Another manual gate promotes from TestNet to MainNet

Each promotion runs the same deployment steps with different environment configuration (see [Environment Configuration](/appdev/modules/m5-environment-configuration)).

## Example: GitHub Actions

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: CI
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install DPM
        run: curl https://get.digitalasset.com/install/install.sh | sh

      - name: Install SDK
        run: dpm install package

      - name: Build Daml
        run: dpm build

      - name: Run Daml tests
        run: dpm test

      - name: Generate Java bindings
        run: dpm codegen-java .daml/dist/your-project.dar -o generated-java

      - name: Build backend
        run: cd backend && ./gradlew build

      - name: Upload DAR artifact
        uses: actions/upload-artifact@v4
        with:
          name: dar-${{ github.sha }}
          path: .daml/dist/*.dar
```

## Monitoring CI Health

Regularly review logs during development and testing, such as by capturing logs in CI runs and using them for debugging CI failures. Set up alerts on metrics to monitor the application's health during testing and development. This ensures operational reuse and integration into the long-running test instance. Well-tuned alerts established during development can be reused in operations to detect system health issues.

## Next Steps

* [Testing Strategies](/appdev/modules/m5-testing-strategies) — Testing pyramid and approach details
* [Environment Configuration](/appdev/modules/m5-environment-configuration) — Per-environment configuration management
* [Deployment Progression](/appdev/modules/m5-deployment-progression) — What to verify at each promotion stage

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
