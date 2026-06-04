---
title: "LocalNet Development"
slug: "appdev-modules-m5-localnet-development"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m5-localnet-development.md"
source_title: "LocalNet Development"
tags:
  - appdev
  - modules
  - m5-localnet-development
---

# LocalNet Development

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# LocalNet Development

> Using cn-quickstart's LocalNet as your primary development and testing environment

LocalNet is a Docker Compose-based local network that mirrors the Canton Network topology on your development machine. It gives you multiple validators, wallet services, PQS, and the full Splice applications  — everything you need to build and test multi-party applications without connecting to a shared network.

## What LocalNet Provides

LocalNet provides a topology comprising three participants, three validators, a PostgreSQL database, and several web applications (wallet, SV, scan) behind an NGINX gateway. Each validator plays a distinct role within the Splice ecosystem:

* **app-provider** — For the user operating their application
* **app-user** — For a user wanting to use the app from the app provider
* **sv** — Super validator, for providing the Global Synchronizer and handling automated market trading (AMT)

LocalNet is designed for development and testing. It is not intended for production use.

## The Development Lifecycle

Most development teams go through five distinct phases with the cn-quickstart:

### Learning phase (1-2 days)

Your first interaction with cn-quickstart focuses on getting the environment running, exploring the sample application, and understanding the architecture. Keep your local copy current by pulling from main:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git clone https://github.com/digital-asset/cn-quickstart.git
cd cn-quickstart

# Regular updates during learning
git pull origin main
```

### Experimentation phase (1-2 weeks)

You begin modifying configurations, exploring APIs, and changing Daml code to test integration patterns. Set up upstream tracking so you can selectively incorporate changes:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git remote add upstream https://github.com/digital-asset/cn-quickstart.git
git checkout -b experiments
git fetch upstream
git merge upstream/main
```

### Development phase (2-3 weeks)

You start building your own application alongside the sample. Many developers create their code in parallel directories:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
cn-quickstart/
├── quickstart/    # Original sample code
│   ├── daml/
│   ├── backend/
│   └── frontend/
└── myapp/         # Your application code
    ├── daml/
    ├── backend/
    └── frontend/
```

Update `settings.gradle.kts` to include both project structures. Use `.envrc.private` for local environment overrides. Create custom Docker Compose files that extend the cn-quickstart configuration.

### Separation phase

Once your application's complexity exceeds the cn-quickstart sample, remove the dependency on the original code. Delete the sample directories, update build files, and remove the upstream git remote:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
git remote remove upstream
rm -rf quickstart/
# Update settings.gradle.kts, build.gradle.kts, etc.
```

### Ongoing updates

After separation, periodically review cn-quickstart's changelog for tooling improvements and updated tool versions you can adopt. The cn-quickstart becomes a reference rather than a dependency.

## Starting and Stopping LocalNet

If you're using cn-quickstart, the Makefile wraps the Docker Compose commands:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cd quickstart
make setup    # First-time setup
make build    # Build Daml and backend
make start    # Start LocalNet
make stop     # Stop LocalNet
```

For direct Docker Compose control, set the environment variables `LOCALNET_DIR` (path to the LocalNet directory) and `IMAGE_TAG` (Splice version), then use:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Start all nodes
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user up -d

# Stop all nodes
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user down -v
```

You can use Docker Compose profiles (`--profile app-provider`, etc.) alongside environment variables (`APP_PROVIDER_PROFILE=on/off`) to disable specific validators and reduce resource usage.

## Ports and Services

Ports follow a pattern based on the validator role:

* **SV**: `4${PORT_SUFFIX}` (e.g., Ledger API at `4901`)
* **App Provider**: `3${PORT_SUFFIX}` (e.g., Ledger API at `3901`)
* **App User**: `2${PORT_SUFFIX}` (e.g., Ledger API at `2901`)

Key port suffixes:

* `901` — Participant Ledger API (gRPC)
* `902` — Participant Admin API
* `975` — JSON API (HTTP)
* `903` — Validator Admin API
* `900` — Canton HTTP health check
* `961` — Canton gRPC health check

Web UIs:

* App User Wallet: `http://wallet.localhost:2000`
* App Provider Wallet: `http://wallet.localhost:3000`
* SV UI: `http://sv.localhost:4000`
* Scan UI: `http://scan.localhost:4000`

<Note>
  If `*.localhost` domains don't resolve on your machine, add entries to `/etc/hosts`:

  ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  127.0.0.1   scan.localhost
  127.0.0.1   wallet.localhost
  127.0.0.1   sv.localhost
  ```
</Note>

## Debugging with LocalNet

### Capturing and viewing logs

The fastest way to start debugging is to capture all logs at once:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make capture-logs
```

Use [lnav](https://lnav.org/) to analyze the captured log files — it handles multiple log formats and lets you filter, search, and correlate events across services.

### Viewing live logs

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# All containers
docker compose -f $LOCALNET_DIR/compose.yaml logs -f

# Specific service
docker compose -f $LOCALNET_DIR/compose.yaml logs -f app-provider-participant

# Filter for errors
docker compose -f $LOCALNET_DIR/compose.yaml logs -f 2>&1 | grep -i error
```

### Accessing the Canton Console

The Canton Console gives you direct access to inspect and modify the participant, sequencer, and mediator nodes:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               run --rm console
```

Or with cn-quickstart: `make canton-console`.

### Common issues

* **Containers fail to start** — Check available memory. LocalNet with all three validators requires significant resources. Disable unused profiles to reduce the footprint.
* **Scan UI shows no rounds** — It may take several minutes after startup before data appears in the Scan UI. This is expected behavior during initial network bootstrapping.
* **Database connection errors** — The single PostgreSQL instance handles all components. Check that it started successfully before other services.

## Next Steps

* [Testing Strategies](/docs/canton/appdev-modules-m5-testing-strategies) — Testing pyramid and approaches for Canton applications
* [Deployment Progression](/docs/canton/appdev-modules-m5-deployment-progression) — Moving from LocalNet to DevNet, TestNet, and MainNet

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
