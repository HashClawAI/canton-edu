---
title: "Local Testing"
slug: "global-synchronizer-understand-local-testing"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/understand/local-testing.md"
source_title: "Local Testing"
tags:
  - global-synchronizer
  - understand
  - local-testing
---

# Local Testing

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Local Testing

> Docker-Compose based deployment of a local Canton Network for development and testing

LocalNet provides a straightforward topology comprising three participants, three validators, a PostgreSQL database, and several web applications (wallet, sv, scan) behind an NGINX gateway. Each validator plays a distinct role within the Splice ecosystem:

* **app-provider**: for the user operating their application
* **app-user**: for a user wanting to use the app from the App Provider
* **sv**: for providing the Global Synchronizer and handling AMT

Designed primarily for development and testing, LocalNet is not intended for production use.

## Setup

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. Download the release artifacts from the <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">Download Bundle (DevNet 0.6.4)</a> link, and extract the bundle:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.4_splice-node.tar.gz
       > ```

       The extracted docker compose files defining LocalNet are located in `splice-node/docker-compose/localnet`.

    2. Export these two environment variables used in the later commands:

       * **LOCALNET\_DIR**: Specifies the path to the LocalNet directory.
       * **IMAGE\_TAG**: Specifies the version of Splice to be used in LocalNet.

       For the bundle that you downloaded use:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.4
       > ```

    3. See `use-localnet` for the commands to start, stop, inspect, and administrate the LocalNet nodes.

    Optional: use the Docker Compose profiles (e.g., `--profile app-provider`) alongside the corresponding environment variables (e.g., `APP_PROVIDER_PROFILE=on/off`) to disable specific validator nodes; for example, to reduce the resource needs of LocalNet. By default, all three validators are active.

    Optional: use the following additional environment variables to configure:

    * **LOCALNET\_DIR/compose.env**: Contains Docker Compose configuration variables.
    * **LOCALNET\_ENV\_DIR**: Overrides the default environment file directory. The default is `$LOCALNET_DIR/env`.
    * **LOCALNET\_ENV\_DIR/common.env**: Shared environment variables across Docker Compose and container configurations. It sets default ports, DB credentials, and Splice UI configurations.

    Resource constraints for containers can be configured via: - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. Download the release artifacts from the <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">Download Bundle (TestNet 0.6.3)</a> link, and extract the bundle:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.3_splice-node.tar.gz
       > ```

       The extracted docker compose files defining LocalNet are located in `splice-node/docker-compose/localnet`.

    2. Export these two environment variables used in the later commands:

       * **LOCALNET\_DIR**: Specifies the path to the LocalNet directory.
       * **IMAGE\_TAG**: Specifies the version of Splice to be used in LocalNet.

       For the bundle that you downloaded use:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.3
       > ```

    3. See `use-localnet` for the commands to start, stop, inspect, and administrate the LocalNet nodes.

    Optional: use the Docker Compose profiles (e.g., `--profile app-provider`) alongside the corresponding environment variables (e.g., `APP_PROVIDER_PROFILE=on/off`) to disable specific validator nodes; for example, to reduce the resource needs of LocalNet. By default, all three validators are active.

    Optional: use the following additional environment variables to configure:

    * **LOCALNET\_DIR/compose.env**: Contains Docker Compose configuration variables.
    * **LOCALNET\_ENV\_DIR**: Overrides the default environment file directory. The default is `$LOCALNET_DIR/env`.
    * **LOCALNET\_ENV\_DIR/common.env**: Shared environment variables across Docker Compose and container configurations. It sets default ports, DB credentials, and Splice UI configurations.

    Resource constraints for containers can be configured via: - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Download the release artifacts from the <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">Download Bundle (MainNet 0.6.2)</a> link, and extract the bundle:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > tar xzvf 0.6.2_splice-node.tar.gz
       > ```

       The extracted docker compose files defining LocalNet are located in `splice-node/docker-compose/localnet`.

    2. Export these two environment variables used in the later commands:

       * **LOCALNET\_DIR**: Specifies the path to the LocalNet directory.
       * **IMAGE\_TAG**: Specifies the version of Splice to be used in LocalNet.

       For the bundle that you downloaded use:

       > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       > export LOCALNET_DIR=$PWD/splice-node/docker-compose/localnet
       > export IMAGE_TAG=0.6.2
       > ```

    3. See `use-localnet` for the commands to start, stop, inspect, and administrate the LocalNet nodes.

    Optional: use the Docker Compose profiles (e.g., `--profile app-provider`) alongside the corresponding environment variables (e.g., `APP_PROVIDER_PROFILE=on/off`) to disable specific validator nodes; for example, to reduce the resource needs of LocalNet. By default, all three validators are active.

    Optional: use the following additional environment variables to configure:

    * **LOCALNET\_DIR/compose.env**: Contains Docker Compose configuration variables.
    * **LOCALNET\_ENV\_DIR**: Overrides the default environment file directory. The default is `$LOCALNET_DIR/env`.
    * **LOCALNET\_ENV\_DIR/common.env**: Shared environment variables across Docker Compose and container configurations. It sets default ports, DB credentials, and Splice UI configurations.

    Resource constraints for containers can be configured via: - **LOCALNET\_DIR/resource-constraints.yaml**
  </Tab>
</Tabs>

## Exposed Ports

The following section details the ports used by various services. The default database port is **DB\_PORT=5432**.

Other ports are generated using specific patterns based on the validator:

* For the Super Validator (sv), the port is specified as `4${PORT_SUFFIX}`.
* For the App Provider, the port is specified as `3${PORT_SUFFIX}`.
* For the App User, the port is specified as `2${PORT_SUFFIX}`.

These patterns apply to the following ports suffixes:

* **PARTICIPANT\_LEDGER\_API\_PORT\_SUFFIX**: 901
* **PARTICIPANT\_ADMIN\_API\_PORT\_SUFFIX**: 902
* **PARTICIPANT\_JSON\_API\_PORT\_SUFFIX**: 975
* **VALIDATOR\_ADMIN\_API\_PORT\_SUFFIX**: 903
* **CANTON\_HTTP\_HEALTHCHECK\_PORT\_SUFFIX**: 900
* **CANTON\_GRPC\_HEALTHCHECK\_PORT\_SUFFIX**: 961

UI Ports are defined as follows:

* **APP\_USER\_UI\_PORT**: 2000
* **APP\_PROVIDER\_UI\_PORT**: 3000
* **SV\_UI\_PORT**: 4000

## Database

LocalNet uses a single PostgreSQL database for all components. Database configurations are sourced from `LOCALNET_ENV_DIR/postgres.env`.

## Application UIs

* **App User Wallet UI**

  > * **URL**: [http://wallet.localhost:2000](http://wallet.localhost:2000)
  > * **Description**: Interface for managing user wallets.

* **App Provider Wallet UI**

  > * **URL**: [http://wallet.localhost:3000](http://wallet.localhost:3000)
  > * **Description**: Interface for managing user wallets.

* **Super Validator Web UI**

  > * **URL**: [http://sv.localhost:4000](http://sv.localhost:4000)
  > * **Description**: Interface for super validator functionalities.

* **Scan Web UI**

  > * **URL**: [http://scan.localhost:4000](http://scan.localhost:4000)
  > * **Description**: Interface to monitor transactions.

<Note>
  `LocalNet` rounds may take up to 6 rounds (equivalent to one hour) to display in the scan UI.
</Note>

In most scenarios, the `*.localhost` domains (e.g., `http://scan.localhost`) will resolve to your local host IP `127.0.0.1`. There are some situations where the resolution does not occur and the solution is to add entries to your `/etc/hosts` file. For example, to resolve `http://scan.localhost` and `http://wallet.localhost` add these entry to the file:

```
127.0.0.1   scan.localhost
127.0.0.1   wallet.localhost
```

## Default Wallet Users

* **App User**: app-user
* **App Provider**: app-provider
* **SV**: sv

## Swagger UI

When the `swagger-ui` profile is enabled, the Swagger UI for the `JSON Ledger API HTTP Endpoints` across all running participants is available at [http://localhost:9090](http://localhost:9090). Note: Some endpoints require a JWT token when using the **Try it out** feature. One method to obtain this token is via the Canton Console. Start the Canton Console `make canton-console` and execute the following command:

```
`app-provider`.adminToken
```

For proper functionality, Swagger UI relies on a localhost nginx proxy for `canton.localhost` configured for each participant. For example, the `JSON Ledger API HTTP Endpoints` for the app-provider can be accessed at the nginx proxy URL `http://canton.localhost:${APP_PROVIDER_UI_PORT}` via Swagger UI, which corresponds to accessing `localhost:3${PARTICIPANT_JSON_API_PORT}` directly. The nginx proxy only adds additional headers to resolve CORS issues within Swagger UI.

## Use LocalNet

### Start LocalNet nodes

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user up -d
```

### Stop LocalNet nodes

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user down -v
```

### Start nodes including a swagger-ui

See `swagger-ui` for more information.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user \
               --profile swagger-ui up -d
```

### Stop nodes including a swagger-ui

See `swagger-ui` for more information.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               --profile sv \
               --profile app-provider \
               --profile app-user \
               --profile swagger-ui down -v
```

### Access the Canton Admin Console

Use the Canton Admin Console to inspect and modify the run configuration of the Canton sequencer, mediator, and participant nodes in your LocalNet deployment.

* [Canton Console How-To](/docs/canton/global-synchronizer-canton-console-console-overview)
* [Canton Console commands](/docs/canton/global-synchronizer-reference-canton-console-commands)

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose --env-file $LOCALNET_DIR/compose.env \
               --env-file $LOCALNET_DIR/env/common.env \
               -f $LOCALNET_DIR/compose.yaml \
               -f $LOCALNET_DIR/resource-constraints.yaml \
               run --rm console
```

## Multiple Synchronizers

LocalNet supports running multiple synchronizers side by side.

By default, a single synchronizer controlled by the Super Validator (sv) is active. This synchronizer simulates the **Global Synchronizer**.

To enable a second synchronizer called `app-synchronizer`, start LocalNet with the `multi-sync` Docker Compose profile (`--profile multi-sync`). The additional synchronizer has the following characteristics:

* It is managed by the `app-sequencer` and `app-mediator` nodes.
* It simulates a **private synchronizer**.
* Both the `app-provider` and `app-user` participants are cross-connected to the Global Synchronizer and the `app-synchronizer`.

## Using Non-Default Protocol Versions

The protocol version used in the LocalNet synchronizer and participants can be configured by setting the `CANTON_PROTOCOL_VERSION` environment variable to the required version prior to launching LocalNet. Non-stable protocol versions can be used for early testing, but require explicit opt-in. To enable that, export also a `ALPHA_PROTOCOL_VERSION_ENV=$LOCALNET_DIR/env/alpha-protocol-version.env` environment variable.

<Warning>
  Non-stable protocol versions are unreleased versions that are under development, and are subject to announced breaking changes. One implication of this is that this environment usually cannot be upgraded, and will therefore require a full reset for every change. Use only for early testing and development purposes.
</Warning>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
