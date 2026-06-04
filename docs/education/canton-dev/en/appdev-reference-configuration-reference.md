---
title: "Configuration Reference"
slug: "appdev-reference-configuration-reference"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/configuration-reference.md"
source_title: "Configuration Reference"
tags:
  - appdev
  - reference
  - configuration-reference
---

# Configuration Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration Reference

> Reference for Canton configuration files, DPM project settings, storage, command line arguments, and environment variables

Canton nodes use [HOCON](https://github.com/lightbend/config/blob/master/HOCON.md) (Human-Optimized Config Object Notation) for its static configuration files. Static configuration covers settings that must be known at process startup, such as storage backends, API ports, and node identities. Dynamic settings like party registration and synchronizer connections are managed at runtime through the [console](/global-synchronizer/reference/canton-console-reference) or administration APIs.

## HOCON Format Basics

HOCON supports JSON-like object syntax with relaxed quoting, nested key paths (`a.b.c = value`), and `//` or `#` comments. Repeated keys are merged, with the last definition winning.

### File Includes

### Environment Variable Substitution

HOCON substitutes environment variables using `${VAR_NAME}` syntax. Two forms are available:

* `${VAR_NAME}` -- required. The process fails to start if the variable is not set.
* `${?VAR_NAME}` -- optional. The key is only set when the variable exists.

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
dataSourceClass = "org.postgresql.ds.PGSimpleDataSource"
properties = {
    serverName = "localhost"
    serverName = ${?POSTGRES_HOST}  # overrides only if POSTGRES_HOST is set
    user = ${?POSTGRES_USER}          # required, fails if unset
    password = ${?POSTGRES_PASSWORD}  # required, fails if unset
```

<Warning>
  Never hardcode credentials in configuration files. Use environment variable substitution for passwords and other secrets.
</Warning>

## Canton Configuration Structure

CamelCase Scala names map to lowercase-with-dashes in config files (e.g., `synchronizerParameters` becomes `synchronizer-parameters`).

### Init Configuration

Some values apply only during the first initialization of a node and cannot be changed afterward. These live under the `init` section:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}

participant1 {
  init {
    ledger-api.max-deduplication-duration = 1 minute
    identity.node-identifier.type = random
  }
```

## Command Line Arguments

### Run Modes

### JVM Arguments

## Storage Configuration

Canton supports three storage backends:

* **Memory** -- for quick tests; data is lost on restart
* **H2** -- embedded database, suitable for local development
* **PostgreSQL** -- the only supported option for production

### PostgreSQL Example

Each Canton node requires its own database. Create databases with UTF-8 encoding:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
CREATE DATABASE participant1_db ENCODING = 'UTF8';
CREATE USER participant1_user WITH PASSWORD 'change-me';
GRANT ALL PRIVILEGES ON DATABASE participant1_db TO participant1_user;
```

Canton uses [HikariCP](https://github.com/brettwooldridge/HikariCP) for connection pooling. You can tune pool properties (`maximumPoolSize`, `connectionTimeout`, `idleTimeout`, etc.) under `storage.config`.

### Configuration Mixin Pattern

When running multiple nodes against the same database server, define shared storage settings in a mixin and reference them per node:

## Key Parameters

### Fail-Fast Mode

<Note>
  Use this with care -- disabling fail-fast can cause indefinite, noisy waits if the database is unreachable.
</Note>

### Protocol Version

### Early Access Protocol Versions

Alpha and beta protocol versions are for non-production environments only. Enabling them requires setting `non-standard-config = yes` at the `canton.parameters` level and the corresponding version support flag on the participant:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}

canton.parameters {
  non-standard-config = yes
  alpha-version-support = yes
}

canton.participants.participant1.parameters = {
  alpha-version-support = yes
```

## DPM Project Configuration

DPM uses YAML files for project configuration, separate from Canton's HOCON node configuration.

### daml.yaml (Single Package)

Each Daml package has a `daml.yaml` specifying the SDK version, package name, source directory, and dependencies.

### multi-package.yaml (Multi-Package Projects)

For multi-package project configuration, see [Building and Packaging](/appdev/modules/m3-building-packaging) which covers `multi-package.yaml` structure and dependency resolution.

### DPM Environment Variables

For DPM environment variable details, see [Building and Packaging](/appdev/modules/m3-building-packaging).

### DPM Global Configuration

DPM reads global settings from `${DPM_HOME}/dpm-config.yaml`. Environment variables take precedence over file values:

* `DPM_REGISTRY` -- override the Docker registry for SDKs and components
* `DPM_REGISTRY_AUTH` -- override the registry auth file
* `DPM_INSECURE_REGISTRY` -- allow pulling from HTTP registries
* `DPM_LOG_LEVEL` -- set log level (`debug`, `info`, `warn`, `error`)
* `DPM_SDK_VERSION` -- override the SDK version globally across all projects
* `DAML_PACKAGE` -- run `dpm` commands in a package context without changing directories

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
