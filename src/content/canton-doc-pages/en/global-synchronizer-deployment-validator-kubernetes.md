---
title: "Kubernetes Validator Deployment"
slug: "global-synchronizer-deployment-validator-kubernetes"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-kubernetes.md"
source_title: "Kubernetes Validator Deployment"
tags:
  - global-synchronizer
  - deployment
  - validator-kubernetes
---

# Kubernetes Validator Deployment

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Kubernetes Validator Deployment

> Deploy a Canton Network validator on Kubernetes using Helm charts

This section describes how to deploy a standalone validator node in Kubernetes using Helm charts. The Helm charts deploy a validator node along with associated wallet and CNS UIs, and connect it to a global synchronizer.

## Requirements

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. A running Kubernetes cluster in which you have administrator access to create and manage namespaces.

    2. A development workstation with the following:

       > 1. `kubectl` - At least v1.26.1
       > 2. `helm` - At least v3.11.1

    3. Your cluster needs a static egress IP. After acquiring that, provide it to your SV sponsor who will propose adding it to the IP allowlist to the other SVs.

    4. Please download the release artifacts containing the sample Helm value files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">Download Bundle (DevNet 0.6.4)</a>, and extract the bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.4_splice-node.tar.gz
    ```

    <Warning>
      **If you lose your keys, you lose access to your coins**. While regular backups are not necessary to run your node,

      they are **strongly** recommended for recovery purposes.

      You should regularly back up all databases in your deployment and ensure you always have an up-to-date identities backup.

      Super Validators retain the information necessary to allow you to recover your Canton Coin from an identities backup.

      On the other hand, Super Validators **do not** retain transaction details from applications they are not involved in.

      This means that if you have other applications installed, the Super Validators cannot help you recover data from those apps;

      you can only rely on your own backups.

      (More information in [Backups section for Validators](/docs/canton/global-synchronizer-production-operations-validator-backups) or [Backups section for SVs](/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.</p>

    <ul>
      <li>**MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).</li>

      <li>**SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.dev.global.canton.network.sync.global">[https://sv.sv-1.dev.global.canton.network.sync.global](https://sv.sv-1.dev.global.canton.network.sync.global)</a>.</li>
    </ul>

    <p>**ONBOARDING\_SECRET**<br />
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.</p>

    <Note>
      On DevNet, you can obtain an onboarding secret automatically by calling the following endpoint on any SV (replace `SPONSOR_SV_URL` with the SV app URL defined above):
    </Note>

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -X POST SPONSOR_SV_URL/api/sv/v0/devnet/onboard/validator/prepare
    ```

    <Note>
      Make sure to use the **SV app URL** (starting with `sv.`), not the Scan URL (starting with `scan.`).
    </Note>

    <Note>
      Note that this self-served secret is only valid for 1 hour.
    </Note>

    * **TRUSTED\_SCAN\_URL** — The scan URL of an SV that you trust and that is reachable by your validator, often your SV sponsor. This should be of the form <a href="https://scan.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.dev.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., for the Global Synchronizer Foundation SV it is <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>.

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. A running Kubernetes cluster in which you have administrator access to create and manage namespaces.

    2. A development workstation with the following:

       > 1. `kubectl` - At least v1.26.1
       > 2. `helm` - At least v3.11.1

    3. Your cluster needs a static egress IP. After acquiring that, provide it to your SV sponsor who will propose adding it to the IP allowlist to the other SVs.

    4. Please download the release artifacts containing the sample Helm value files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">Download Bundle (TestNet 0.6.3)</a>, and extract the bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.3_splice-node.tar.gz
    ```

    <Warning>
      **If you lose your keys, you lose access to your coins**. While regular backups are not necessary to run your node,

      they are **strongly** recommended for recovery purposes.

      You should regularly back up all databases in your deployment and ensure you always have an up-to-date identities backup.

      Super Validators retain the information necessary to allow you to recover your Canton Coin from an identities backup.

      On the other hand, Super Validators **do not** retain transaction details from applications they are not involved in.

      This means that if you have other applications installed, the Super Validators cannot help you recover data from those apps;

      you can only rely on your own backups.

      (More information in [Backups section for Validators](/docs/canton/global-synchronizer-production-operations-validator-backups) or [Backups section for SVs](/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.</p>

    <ul>
      <li>**MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).</li>

      <li>**SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.test.global.canton.network.sync.global">[https://sv.sv-1.test.global.canton.network.sync.global](https://sv.sv-1.test.global.canton.network.sync.global)</a>.</li>
    </ul>

    <p>**ONBOARDING\_SECRET**<br />
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.</p>

    * **TRUSTED\_SCAN\_URL** — The scan URL of an SV that you trust and that is reachable by your validator, often your SV sponsor. This should be of the form <a href="https://scan.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., for the Global Synchronizer Foundation SV it is <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>.

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. A running Kubernetes cluster in which you have administrator access to create and manage namespaces.

    2. A development workstation with the following:

       > 1. `kubectl` - At least v1.26.1
       > 2. `helm` - At least v3.11.1

    3. Your cluster needs a static egress IP. After acquiring that, provide it to your SV sponsor who will propose adding it to the IP allowlist to the other SVs.

    4. Please download the release artifacts containing the sample Helm value files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">Download Bundle (MainNet 0.6.2)</a>, and extract the bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    tar xzvf 0.6.2_splice-node.tar.gz
    ```

    <Warning>
      **If you lose your keys, you lose access to your coins**. While regular backups are not necessary to run your node,

      they are **strongly** recommended for recovery purposes.

      You should regularly back up all databases in your deployment and ensure you always have an up-to-date identities backup.

      Super Validators retain the information necessary to allow you to recover your Canton Coin from an identities backup.

      On the other hand, Super Validators **do not** retain transaction details from applications they are not involved in.

      This means that if you have other applications installed, the Super Validators cannot help you recover data from those apps;

      you can only rely on your own backups.

      (More information in [Backups section for Validators](/docs/canton/global-synchronizer-production-operations-validator-backups) or [Backups section for SVs](/docs/canton/global-synchronizer-production-operations-sv-backup))
    </Warning>

    <p>To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.</p>

    <ul>
      <li>**MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).</li>

      <li>**SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.global.canton.network.sync.global">[https://sv.sv-1.global.canton.network.sync.global](https://sv.sv-1.global.canton.network.sync.global)</a>.</li>
    </ul>

    <p>**ONBOARDING\_SECRET**<br />
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.</p>

    * **TRUSTED\_SCAN\_URL** — The scan URL of an SV that you trust and that is reachable by your validator, often your SV sponsor. This should be of the form <a href="https://scan.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://scan.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., for the Global Synchronizer Foundation SV it is <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>.

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>
</Tabs>

## Validator Network Diagram

<img src="https://mintcdn.com/cantonfoundation/eCttQejvyGlU5PC2/images/splice/validator-network-diagram.png?fit=max&auto=format&n=eCttQejvyGlU5PC2&q=85&s=6d476d77a060cd47d92bbf8347ae1ff4" width="600" alt="Validator Network Diagram" data-path="images/splice/validator-network-diagram.png" />

## Preparing a Cluster for Installation

Create the application namespace within Kubernetes.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create ns validator
```

<Note>
  The validator deployment assumes one validator per namespace. If you wish to run multiple validators in the same cluster, please create a separate namespace for each.
</Note>

## HTTP Proxy configuration

If you need to use an HTTP forward proxy for egress in your environment, you need to set `https.proxyHost` and `https.proxyPort` in `additionalJvmOptions` in the validator and participant helm charts to use the HTTP proxy for outgoing connections:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
```

Replace `your.proxy.host` and `your_proxy_port` with the actual host and port of your HTTP proxy. Proxy authentication is currently not supported.

### Bypassing the proxy for specific hosts

<Note>
  Setting `http.nonProxyHosts` affects:

  * The HTTP client used by the CN apps (Validator, Scan, SV, Wallet).
  * JDK-level HTTP clients in the same JVM (via the default `ProxySelector`). This includes the Auth0 JWK library used by the CN apps **and** by the Canton participant for JWKS / OIDC discovery, as well as file downloads that use `java.net.HttpURLConnection`.
  * gRPC egress from other components, because gRPC's Netty transport delegates proxy decisions to the default JDK `ProxySelector`.
</Note>

You can set `http.nonProxyHosts` to bypass the proxy for specific target hosts. Matching hosts will be contacted directly rather than through the configured proxy. This is useful for services that are reachable on the local network, such as an in-cluster Scan instance or internal monitoring endpoints.

The value is a `|`-separated list of patterns that follows the standard Java `nonProxyHosts` grammar:

* Patterns match the request host name case-insensitively.
* `*` is a wildcard. Conventionally it is used at the start (`*.internal`) or end (`10.*`) of a pattern.
* Matching is performed on the raw host string from the request URI. No DNS resolution is performed, so `localhost` and `127.0.0.1` are treated as different names unless you list both.
* An empty value (e.g. `-Dhttp.nonProxyHosts=`) means "no bypass patterns".

Example `additionalJvmOptions` for the validator helm chart that proxies external traffic but bypasses the proxy for `localhost` / `127.0.0.1`, any host in the `.internal` domain, and any IPv4 address whose literal string representation starts with `10.`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalJvmOptions: |
  -Dhttps.proxyHost=your.proxy.host
  -Dhttps.proxyPort=your_proxy_port
  -Dhttp.nonProxyHosts=localhost|127.0.0.1|*.internal|10.*
```

## Configuring PostgreSQL authentication

The PostgreSQL instance that the helm charts create, and all apps that depend on it, require the user's password to be set through Kubernetes secrets. Currently, all apps use the Postgres user `cnadmin`. The password can be setup with the following command, assuming you set the environment variable `POSTGRES_PASSWORD` to a secure value:

<div className="todo">
  call out the option of using a managed postgres instance
</div>

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic postgres-secrets \
    --from-literal=postgresPassword=${POSTGRES_PASSWORD} \
    -n validator
```

## Preparing for Validator Onboarding

Ensure that your validator onboarding secret `ONBOARDING_SECRET` is set in the namespace you created earlier.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret generic splice-app-validator-onboarding-validator \
    "--from-literal=secret=${ONBOARDING_SECRET}" \
    -n validator
```

## Configuring Authentication

For security, the various components that comprise your Validator node need to be able to authenticate themselves to each other, as well as be able to authenticate external UI and API users. We use JWT access tokens for authentication and expect these tokens to be issued by an (external) [OpenID Connect](https://openid.net/connect/) (OIDC) provider. You must:

1. Set up an OIDC provider in such a way that both backends and web UI users are able to obtain JWTs in a supported form.
2. Configure your backends to use that OIDC provider.

The validator supports non-authenticated deployments as well, but this is strongly discouraged for production deployments. If you wish to run without authentication, please refer to the notes in `helm-validator-no-auth`.

### OIDC Provider Requirements

This section provides pointers for setting up an OIDC provider for use with your Validator node. Feel free to skip directly to `helm-validator-auth0` if you plan to use [Auth0](https://auth0.com) for your Validator node's authentication needs.

These docs focus on Auth0, and are being continuously tested and maintained. Other OIDC providers can be used, and are in active use by various community members, who have contributed some notes and examples in Okta and Keycloak community authored examples.

Your OIDC provider must be reachable[^1] at a well known (HTTPS) URL. In the following, we will refer to this URL as `OIDC_AUTHORITY_URL`. Both your Validator node and any users that wish to authenticate to a web UI connected to your Validator node must be able to reach the `OIDC_AUTHORITY_URL`. We require your OIDC provider to provide a [discovery document](https://openid.net/specs/openid-connect-discovery-1_0.html) at `OIDC_AUTHORITY_URL/.well-known/openid-configuration`. We furthermore require that your OIDC provider exposes a [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517) document. In this documentation, we assume that this document is available at `OIDC_AUTHORITY_URL/.well-known/jwks.json`.

For machine-to-machine (Validator node component to Validator node component) authentication, your OIDC provider must support the [OAuth 2.0 Client Credentials Grant](https://tools.ietf.org/html/rfc6749#section-4.4) flow. This means that you must be able to configure (`CLIENT_ID`, `CLIENT_SECRET`) pairs for all Validator node components that need to authenticate themselves to other components. Currently, this is the validator app backend - which needs to authenticate to the Validator node's Canton participant. The `sub` field of JWTs issued through this flow must match the user ID configured as `ledger-api-user` in `helm-validator-auth-secrets-config`. In this documentation, we assume that the `sub` field of these JWTs is formed as `CLIENT_ID@clients`. If this is not true for your OIDC provider, pay extra attention when configuring `ledger-api-user` values below.

For user-facing authentication - allowing users to access the various web UIs hosted on your Validator node, your OIDC provider must support the [OAuth 2.0 Authorization Code Grant](https://datatracker.ietf.org/doc/html/rfc6749#section-4.1) flow and allow you to obtain client identifiers for the web UIs your Validator node will be hosting. Currently, these are the Wallet web UI and the CNS web UI. You might be required to whitelist a range of URLs on your OIDC provider, such as "Allowed Callback URLs", "Allowed Logout URLs", "Allowed Web Origins", and "Allowed Origins (CORS)". If you are using the ingress configuration of this runbook, the correct URLs to configure here are `https://wallet.validator.YOUR_HOSTNAME` (for the Wallet web UI) and `https://cns.validator.YOUR_HOSTNAME` (for the CNS web UI).

`YOUR_HOSTNAME` is a placeholder that you need to replace with the actual domain name or IP address of the server hosting your services.

An identifier that is unique to the user must be set via the `sub` field of the issued JWT. On some occasions, this identifier will be used as a user name for that user on your Validator node's Canton participant. In `helm-validator-install`, you will be required to configure a user identifier as the `validatorWalletUser` -make sure that whatever you configure there matches the contents of the `sub` field of JWTs issued for that user.

*All* JWTs issued for use with your Validator node:

* must be signed using the RS256 signing algorithm

In the future, your OIDC provider might additionally be required to issue JWTs with a `scope` explicitly set to `daml_ledger_api` (when requested to do so as part of the OAuth 2.0 authorization code flow).

Summing up, your OIDC provider setup must provide you with the following configuration values:

| Name                      | Value                                                                                   |
| ------------------------- | --------------------------------------------------------------------------------------- |
| OIDC\_AUTHORITY\_URL      | The URL of your OIDC provider for obtaining the `openid-configuration` and `jwks.json`. |
| VALIDATOR\_CLIENT\_ID     | The client id of your OIDC provider for the validator app backend.                      |
| VALIDATOR\_CLIENT\_SECRET | The client secret of your OIDC provider for the validator app backend.                  |
| WALLET\_UI\_CLIENT\_ID    | The client id of your OIDC provider for the wallet UI.                                  |
| CNS\_UI\_CLIENT\_ID       | The client id of your OIDC provider for the CNS UI.                                     |

We are going to use these values, exported to environment variables named as per the `Name` column, in `helm-validator-auth-secrets-config` and `helm-validator-install`.

When first starting out, it is suggested to configure both JWT token audiences below to the same value: `https://canton.network.global`.

Once you can confirm that your setup is working correctly using this (simple) default, we recommend that you configure dedicated audience values that match your deployment and URLs. This is important for security to avoid tokens for your validators on one network be usable for your validators on another network. You can configure audiences of your choice for the participant ledger API and the validator backend API. We will refer to these using the following configuration values:

| Name                                   | Value                                                                                |
| -------------------------------------- | ------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE | The audience for the participant ledger API. e.g. `https://ledger_api.example.com`   |
| OIDC\_AUTHORITY\_VALIDATOR\_AUDIENCE   | The audience for the validator backend API. e.g. `https://validator.example.com/api` |

Your IAM may also require a scope to be specified when the validator backend requests a token for the ledger API. We will refer to that using the following configuration value:

| Name                                | Value                                              |
| ----------------------------------- | -------------------------------------------------- |
| OIDC\_AUTHORITY\_LEDGER\_API\_SCOPE | The scope for the participant ledger API. Optional |

In case you are facing trouble with setting up your (non-Auth0) OIDC provider, it can be beneficial to skim the instructions in `helm-validator-auth0` as well, to check for functionality or configuration details that your OIDC provider setup might be missing.

### Configuring an Auth0 Tenant

To configure [Auth0](https://auth0.com) as your validator's OIDC provider, perform the following:

1. Create an Auth0 tenant for your validator

2. Create an Auth0 API that controls access to the ledger API:

   > 1. Navigate to Applications > APIs and click "Create API". Set name to `Daml Ledger API`, set identifier to `https://canton.network.global`. Alternatively, if you would like to configure your own audience, you can set the identifier here. e.g. `https://ledger_api.example.com`.
   > 2. Under the Permissions tab in the new API, add a permission with scope `daml_ledger_api`, and a description of your choice.
   > 3. On the Settings tab, scroll down to "Access Settings" and enable "Allow Offline Access", for automatic token refreshing.

3. (Optional) If you want to configure a different audience to your APIs, you can do so by creating new Auth0 APIs with an identifier set to the audience of your choice. For example,

   > 1. Create another API by setting name to `Validator App API`, set identifier for the Validator backend app e.g. `https://validator.example.com/api`.

4. Create an Auth0 Application for the validator backend:

   > 1. In Auth0, navigate to Applications -> Applications, and click the "Create Application" button.
   > 2. Name it `Validator app backend`, choose "Machine to Machine Applications", and click Create.
   > 3. Choose the `Daml Ledger API` API you created in step 2 in the "Authorize Machine to Machine Application" dialog and click Authorize.

5. Create an Auth0 Application for the wallet web UI.

   > 1. In Auth0, navigate to Applications -> Applications, and click the "Create Application" button.
   > 2. Choose "Single Page Web Applications", call it `Wallet web UI`, and click Create.
   > 3. Determine the URL for your validator's wallet UI. If you're using the ingress configuration of this runbook, that would be `https://wallet.validator.YOUR_HOSTNAME`.
   > 4. In the Auth0 application settings, add the URL of the validator wallet to the following:
   >    * "Allowed Callback URLs"
   >    * "Allowed Logout URLs"
   >    * "Allowed Web Origins"
   >    * "Allowed Origins (CORS)"
   > 5. Save your application settings.

6. Create an Auth0 Application for the CNS web UI. Repeat all steps described in step 5, with following modifications:

   * In step b, use `CNS web UI` as the name of your application.
   * In steps c and d, use the URL for your validator's *CNS* UI. If you're using the ingress configuration of this runbook, that would be `https://cns.validator.YOUR_HOSTNAME`.

Please refer to Auth0's [own documentation on user management](https://auth0.com/docs/manage-users) for pointers on how to set up end-user accounts for the two web UI applications you created. Note that you will need to create at least one such user account for completing the steps in `helm-validator-install` - for being able to log in as your Validator node's administrator. You will be asked to obtain the user identifier for this user account. It can be found in the Auth0 interface under User Management -> Users -> your user's name -> user\_id (a field right under the user's name at the top).

We will use the environment variables listed in the table below to refer to aspects of your Auth0 configuration:

| Name                                   | Value                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------ |
| OIDC\_AUTHORITY\_URL                   | `https://AUTH0_TENANT_NAME.us.auth0.com`                                                   |
| OIDC\_AUTHORITY\_LEDGER\_API\_AUDIENCE | The optional audience of your choice for Ledger API. e.g. `https://ledger_api.example.com` |
| VALIDATOR\_CLIENT\_ID                  | The client id of the Auth0 app for the validator app backend                               |
| VALIDATOR\_CLIENT\_SECRET              | The client secret of the Auth0 app for the validator app backend                           |
| WALLET\_UI\_CLIENT\_ID                 | The client id of the Auth0 app for the wallet UI                                           |
| CNS\_UI\_CLIENT\_ID                    | The client id of the Auth0 app for the CNS UI                                              |

The `AUTH0_TENANT_NAME` is the name of your Auth0 tenant as shown at the top left of your Auth0 project. You can obtain the client ID and secret of each Auth0 app from the settings pages of that app.

### Configuring Authentication on your Validator

We are now going to configure your Validator node software based on the OIDC provider configuration values you exported to environment variables at the end of either `helm-validator-auth-requirements` or `helm-validator-auth0`. (Note that some authentication-related configuration steps are also included in `helm-validator-install`)

The validator app backend requires the following secret (omit the scope if it is not needed in your setup)

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace validator secret generic splice-app-validator-ledger-api-auth \
    "--from-literal=ledger-api-user=${VALIDATOR_CLIENT_ID}@clients" \
    "--from-literal=url=${OIDC_AUTHORITY_URL}/.well-known/openid-configuration" \
    "--from-literal=client-id=${VALIDATOR_CLIENT_ID}" \
    "--from-literal=client-secret=${VALIDATOR_CLIENT_SECRET}" \
    "--from-literal=audience=${OIDC_AUTHORITY_LEDGER_API_AUDIENCE}" \
    "--from-literal=scope=${OIDC_AUTHORITY_LEDGER_API_SCOPE}"
```

To setup the wallet and CNS UI, create the following two secrets.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create --namespace validator secret generic splice-app-wallet-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${WALLET_UI_CLIENT_ID}"

kubectl create --namespace validator secret generic splice-app-cns-ui-auth \
    "--from-literal=url=${OIDC_AUTHORITY_URL}" \
    "--from-literal=client-id=${CNS_UI_CLIENT_ID}"
```

### Running without Authentication

<Warning>
  Running without authentication is highly insecure. Anyone with access to the wallet UI, or to the validator in any other way, may log in to your wallet as a user of their choice, or otherwise transact on-ledger on your behalf. For any production use, you should configure proper authentication as described in the sections above.
</Warning>

In order to run the validator without authentication, add `disableAuth: true` to both `splice-node/examples/sv-helm/validator-values.yaml` and `splice-node/examples/sv-helm/participant-values.yaml`. Note that you must disable auth in both places, otherwise the validator will not be able to connect to the participant.

When running without authentication, the username of the validator administrator is `administrator`.

## Installing the Software

<Note>
  We recommend installing [Stakater Reloader](https://github.com/stakater/Reloader), which automatically performs rolling restarts of pods when their referenced Secrets or ConfigMaps change.

  Splice Helm charts include the `reloader.stakater.com/auto: "true"` annotation by default.

  If you do not use Reloader, the annotation is harmless and will be ignored.

  To remove it, set `enableReloader: false` in your Helm values file.
</Note>

### Configuring the Helm Charts

<Tabs>
  <Tab title="DevNet (0.6.4)">
    To install the Helm charts needed to start a Validator node connected to the cluster, you will need to meet a few preconditions. The first is that there needs to be an environment variable defined to refer to the version of the Helm charts necessary to connect to this environment:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.4
    ```

    Please modify the file `splice-node/examples/sv-helm/participant-values.yaml` as follows:

    * Replace `OIDC_AUTHORITY_LEDGER_API_AUDIENCE` in the `auth.targetAudience` entry with audience for the ledger API. e.g. `https://ledger_api.example.com`. If you are not ready to use a custom audience, you can use the suggested default `https://canton.network.global`.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.
    * If you are running on a version of Kubernetes earlier than 1.24, set `enableHealthProbes` to `false` to disable the gRPC liveness and readiness probes.

    If you are using the provided postgres helm chart, modify `splice-node/examples/sv-helm/postgres-values-validator-participant.yaml` as follows:

    * Add `db.volumeSize` and `db.volumeStorageClass` to the values file adjust persistant storage size and storage class if necessary. (These values default to 20GiB and `standard-rwo`)

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-participant-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to (devnet/testnet/mainnet).

    You need to configure how your validator connects to the network's **scan** services by defining a `scanClient` block in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the validator makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The validator connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```

    For your selected `scanClient` type, replace `TRUSTED_SCAN_URL` with a URL of a Scan you host or trust that is reachable by your Validator. For example, the GSF scan URL, <a href="https://scan.sv-1.dev.global.canton.network.sync.global">[https://scan.sv-1.dev.global.canton.network.sync.global](https://scan.sv-1.dev.global.canton.network.sync.global)</a>. For `bft-custom` and `bft` modes of `scanClient`, you can specify more than one scan seed URL by separating them with commas.

    * If you want to configure the audience for the Validator app backend API, replace `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` in the `auth.audience` entry with audience for the Validator app backend API. e.g. `https://validator.example.com/api`.
    * If you want to configure the audience for the Ledger API, set the `audience` field in the `splice-app-validator-ledger-api-auth` k8s secret with the audience for the Ledger API. e.g. `https://ledger_api.example.com`.
    * Replace `OPERATOR_WALLET_USER_ID` with the user ID in your IAM that you want to use to log into the wallet as the validator operator party. Note that this should be the full user id, e.g., `auth0|43b68e1e4978b000cefba352`, *not* only the suffix `43b68e1e4978b000cefba352`
    * Replace `YOUR_CONTACT_POINT` by a slack user name or email address that can be used by node operators to contact you in case there are issues with your node. Note that this contact information will be publicly visible. If you do not want to share contact information, you can put an empty string.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.

    You need to configure how your validator's participant connects to **sequencers** by defining a `synchronizer` config in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    synchronizer:
      connectionType: "bft"

    # synchronizer configuration enables to configure how the validator's participant connects to the synchronizer.
    # synchronizer configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available synchronizer connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # synchronizer:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # synchronizer:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #synchronizer:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted synchronizer sequencer url
    ```

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-validator-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to.
    * Replace `SPONSOR_SV_URL` with the URL of the SV that provided you your secret.
    * Replace `YOUR_VALIDATOR_PARTY_HINT` with the desired name for your validator operator party. It must be of the format `<organization>-<function>-<enumerator>`.
    * Replace `YOUR_VALIDATOR_NODE_NAME` with the name you want your validator node to be represented as on the network. Usually you can use the same value as for your `validatorPartyHint`.

    Finally, please download the UI config values file from [https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml) and add the values from it to your `standalone-validator-values.yaml`.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    To install the Helm charts needed to start a Validator node connected to the cluster, you will need to meet a few preconditions. The first is that there needs to be an environment variable defined to refer to the version of the Helm charts necessary to connect to this environment:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.3
    ```

    Please modify the file `splice-node/examples/sv-helm/participant-values.yaml` as follows:

    * Replace `OIDC_AUTHORITY_LEDGER_API_AUDIENCE` in the `auth.targetAudience` entry with audience for the ledger API. e.g. `https://ledger_api.example.com`. If you are not ready to use a custom audience, you can use the suggested default `https://canton.network.global`.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.
    * If you are running on a version of Kubernetes earlier than 1.24, set `enableHealthProbes` to `false` to disable the gRPC liveness and readiness probes.

    If you are using the provided postgres helm chart, modify `splice-node/examples/sv-helm/postgres-values-validator-participant.yaml` as follows:

    * Add `db.volumeSize` and `db.volumeStorageClass` to the values file adjust persistant storage size and storage class if necessary. (These values default to 20GiB and `standard-rwo`)

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-participant-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to (devnet/testnet/mainnet).

    You need to configure how your validator connects to the network's **scan** services by defining a `scanClient` block in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the validator makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The validator connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```

    For your selected `scanClient` type, replace `TRUSTED_SCAN_URL` with a URL of a Scan you host or trust that is reachable by your Validator. For example, the GSF scan URL, <a href="https://scan.sv-1.test.global.canton.network.sync.global">[https://scan.sv-1.test.global.canton.network.sync.global](https://scan.sv-1.test.global.canton.network.sync.global)</a>. For `bft-custom` and `bft` modes of `scanClient`, you can specify more than one scan seed URL by separating them with commas.

    * If you want to configure the audience for the Validator app backend API, replace `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` in the `auth.audience` entry with audience for the Validator app backend API. e.g. `https://validator.example.com/api`.
    * If you want to configure the audience for the Ledger API, set the `audience` field in the `splice-app-validator-ledger-api-auth` k8s secret with the audience for the Ledger API. e.g. `https://ledger_api.example.com`.
    * Replace `OPERATOR_WALLET_USER_ID` with the user ID in your IAM that you want to use to log into the wallet as the validator operator party. Note that this should be the full user id, e.g., `auth0|43b68e1e4978b000cefba352`, *not* only the suffix `43b68e1e4978b000cefba352`
    * Replace `YOUR_CONTACT_POINT` by a slack user name or email address that can be used by node operators to contact you in case there are issues with your node. Note that this contact information will be publicly visible. If you do not want to share contact information, you can put an empty string.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.

    You need to configure how your validator's participant connects to **sequencers** by defining a `synchronizer` config in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    synchronizer:
      connectionType: "bft"

    # synchronizer configuration enables to configure how the validator's participant connects to the synchronizer.
    # synchronizer configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available synchronizer connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # synchronizer:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # synchronizer:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #synchronizer:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted synchronizer sequencer url
    ```

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-validator-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to.
    * Replace `SPONSOR_SV_URL` with the URL of the SV that provided you your secret.
    * Replace `YOUR_VALIDATOR_PARTY_HINT` with the desired name for your validator operator party. It must be of the format `<organization>-<function>-<enumerator>`.
    * Replace `YOUR_VALIDATOR_NODE_NAME` with the name you want your validator node to be represented as on the network. Usually you can use the same value as for your `validatorPartyHint`.

    Finally, please download the UI config values file from [https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml) and add the values from it to your `standalone-validator-values.yaml`.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    To install the Helm charts needed to start a Validator node connected to the cluster, you will need to meet a few preconditions. The first is that there needs to be an environment variable defined to refer to the version of the Helm charts necessary to connect to this environment:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    export CHART_VERSION=0.6.2
    ```

    Please modify the file `splice-node/examples/sv-helm/participant-values.yaml` as follows:

    * Replace `OIDC_AUTHORITY_LEDGER_API_AUDIENCE` in the `auth.targetAudience` entry with audience for the ledger API. e.g. `https://ledger_api.example.com`. If you are not ready to use a custom audience, you can use the suggested default `https://canton.network.global`.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.
    * If you are running on a version of Kubernetes earlier than 1.24, set `enableHealthProbes` to `false` to disable the gRPC liveness and readiness probes.

    If you are using the provided postgres helm chart, modify `splice-node/examples/sv-helm/postgres-values-validator-participant.yaml` as follows:

    * Add `db.volumeSize` and `db.volumeStorageClass` to the values file adjust persistant storage size and storage class if necessary. (These values default to 20GiB and `standard-rwo`)

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-participant-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to (devnet/testnet/mainnet).

    You need to configure how your validator connects to the network's **scan** services by defining a `scanClient` block in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    scanClient:
      scanType: "bft"
      seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url. Supports multiple urls, separated by comma.

    # scanClient denotes how the validator makes connections to scan service and supports three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Connects to all available scans in the network. It validates responses by ensuring
    # at least f+1 matching responses are received.

    # scanClient:
    #   scanType: "bft"
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with scan seed url(s).  Supports multiple urls, separated by comma.

    # Mode 2: bft-custom
    # A specialized version of bft where you specify a subset of trusted SVs.
    # The validator connects only to the scans of the SVs listed in 'svNames'.
    # Optional param 'threshold' defines how many identical responses are required to consider the scan responses valid.

    # scanClient:
    #   scanType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV names(s)
    #   seedUrls: ["TRUSTED_SCAN_URL"] # replace with actual scan seed urls(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-single
    # Connects to a single trusted scan address.
    # This means that you depend on that single SV and if it is broken or malicious you will be unable to use the network.
    # Hence, usually you want to default to not enabling this

    # scanClient:
    #   scanType: "trust-single"
    #   scanAddress: "TRUSTED_SCAN_URL" # replace with the trusted scan url
    ```

    For your selected `scanClient` type, replace `TRUSTED_SCAN_URL` with a URL of a Scan you host or trust that is reachable by your Validator. For example, the GSF scan URL, <a href="https://scan.sv-1.global.canton.network.sync.global">[https://scan.sv-1.global.canton.network.sync.global](https://scan.sv-1.global.canton.network.sync.global)</a>. For `bft-custom` and `bft` modes of `scanClient`, you can specify more than one scan seed URL by separating them with commas.

    * If you want to configure the audience for the Validator app backend API, replace `OIDC_AUTHORITY_VALIDATOR_AUDIENCE` in the `auth.audience` entry with audience for the Validator app backend API. e.g. `https://validator.example.com/api`.
    * If you want to configure the audience for the Ledger API, set the `audience` field in the `splice-app-validator-ledger-api-auth` k8s secret with the audience for the Ledger API. e.g. `https://ledger_api.example.com`.
    * Replace `OPERATOR_WALLET_USER_ID` with the user ID in your IAM that you want to use to log into the wallet as the validator operator party. Note that this should be the full user id, e.g., `auth0|43b68e1e4978b000cefba352`, *not* only the suffix `43b68e1e4978b000cefba352`
    * Replace `YOUR_CONTACT_POINT` by a slack user name or email address that can be used by node operators to contact you in case there are issues with your node. Note that this contact information will be publicly visible. If you do not want to share contact information, you can put an empty string.
    * Update the `auth.jwksUrl` entry to point to your auth provider's JWK set document by replacing `OIDC_AUTHORITY_URL` with your auth provider's OIDC URL, as explained above.

    You need to configure how your validator's participant connects to **sequencers** by defining a `synchronizer` config in your `standalone-validator-values.yaml`.

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    synchronizer:
      connectionType: "bft"

    # synchronizer configuration enables to configure how the validator's participant connects to the synchronizer.
    # synchronizer configuration has three modes of operation.

    # Mode 1: bft (Byzantine Fault Tolerance)
    # Uses all available synchronizer connections provided by the scan service.
    # Responses are validated against the network's f+1 fault tolerance logic.

    # synchronizer:
    #   connectionType: "bft"

    # Mode 2: bft-custom
    # Connects only to sequencers operated by the specific SVs listed in 'svNames'.
    # optional param 'threshold' defines the minimum number of matching responses required for validation.

    # synchronizer:
    #   connectionType: "bft-custom"
    #   svNames: ["TRUSTED_SV"] # replace with trusted SV name(s)
    #   threshold: <TRUST_THRESHOLD> # optional integer indicating the number of matching responses required for validation

    # Mode 3: trust-Single
    # Connects to a single specified sequencer URL.
    # trust-single makes you dependent on a single SV; if it is malicious or down, you will be unable to use the network.

    #synchronizer:
    #   connectionType: "trust-single"
    #   url: "TRUSTED_SYNCHRONIZER_SEQUENCER_URL" # replace with the trusted synchronizer sequencer url
    ```

    Additionally, please modify the file `splice-node/examples/sv-helm/standalone-validator-values.yaml` as follows:

    * Replace `MIGRATION_ID` with the migration ID of the global synchronizer on the network you are connecting to.
    * Replace `SPONSOR_SV_URL` with the URL of the SV that provided you your secret.
    * Replace `YOUR_VALIDATOR_PARTY_HINT` with the desired name for your validator operator party. It must be of the format `<organization>-<function>-<enumerator>`.
    * Replace `YOUR_VALIDATOR_NODE_NAME` with the name you want your validator node to be represented as on the network. Usually you can use the same value as for your `validatorPartyHint`.

    Finally, please download the UI config values file from [https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml](https://github.com/global-synchronizer-foundation/configs/blob/main/configs/ui-config-values.yaml) and add the values from it to your `standalone-validator-values.yaml`.
  </Tab>
</Tabs>

### Installing the Helm Charts

<Tabs>
  <Tab title="DevNet (0.6.4)">
    With these files in place, you can execute the following helm commands in sequence. It's generally a good idea to wait until each deployment reaches a stable state prior to moving on to the next step.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-validator-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/standalone-validator-values.yaml --wait
    ```

    Once this is running, you should be able to inspect the state of the cluster and observe pods running in the new namespace. A typical query might look as follows:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n validator
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    validator         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    validator         participant-8988dfb54-m9655           1/1     Running            0               26m
    validator         postgres-0                            1/1     Running            0               37m
    validator         validator-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    validator         wallet-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    Note also that `Pod` restarts may happen during bringup, particularly if all helm charts are deployed at the same time. For example, the `participant` cannot start until `postgres` is running.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    With these files in place, you can execute the following helm commands in sequence. It's generally a good idea to wait until each deployment reaches a stable state prior to moving on to the next step.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-validator-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/standalone-validator-values.yaml --wait
    ```

    Once this is running, you should be able to inspect the state of the cluster and observe pods running in the new namespace. A typical query might look as follows:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n validator
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    validator         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    validator         participant-8988dfb54-m9655           1/1     Running            0               26m
    validator         postgres-0                            1/1     Running            0               37m
    validator         validator-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    validator         wallet-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    Note also that `Pod` restarts may happen during bringup, particularly if all helm charts are deployed at the same time. For example, the `participant` cannot start until `postgres` is running.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    With these files in place, you can execute the following helm commands in sequence. It's generally a good idea to wait until each deployment reaches a stable state prior to moving on to the next step.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install postgres oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-postgres -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/postgres-values-validator-participant.yaml --wait
    helm install participant oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-participant -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/participant-values.yaml -f splice-node/examples/sv-helm/standalone-participant-values.yaml --wait
    helm install validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-validator -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-values.yaml -f splice-node/examples/sv-helm/standalone-validator-values.yaml --wait
    ```

    Once this is running, you should be able to inspect the state of the cluster and observe pods running in the new namespace. A typical query might look as follows:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    $ kubectl get pods -n validator
    NAMESPACE         NAME                                  READY   STATUS             RESTARTS        AGE
    validator         ans-web-ui-5bf489db78-bdn2j           1/1     Running            0               24m
    validator         participant-8988dfb54-m9655           1/1     Running            0               26m
    validator         postgres-0                            1/1     Running            0               37m
    validator         validator-app-f8c74d5dd-zf9j4         1/1     Running            0               24m
    validator         wallet-web-ui-69d85cdb99-fnj7q        1/1     Running            0               24m
    ```

    Note also that `Pod` restarts may happen during bringup, particularly if all helm charts are deployed at the same time. For example, the `participant` cannot start until `postgres` is running.
  </Tab>
</Tabs>

## Configuring the Cluster Ingress

The following routes should be configured in your cluster ingress controller.

| Services                     | Port | Routes                                                                                                                                                                     |
| ---------------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `wallet-web-ui`              |      | `https://wallet.validator.<YOUR_HOSTNAME>`                                                                                                                                 |
| `validator-app` `ans-web-ui` | 5003 | `https://wallet.validator.<YOUR_HOSTNAME>/api/validator` `https://cns.validator.<YOUR_HOSTNAME>`                                                                           |
| `validator-app`              | 5003 | `https://cns.validator.<YOUR_HOSTNAME>/api/validator`                                                                                                                      |
| `participant`                | 7575 | `https://<YOUR_HOSTNAME>/api/json-api` (optional, not required by the validator itself but if you want to access the ledger API yourself. You can change the route freely) |

* `https://wallet.validator.<YOUR_HOSTNAME>` should be routed to service `wallet-web-ui` in the `validator` namespace
* `https://wallet.validator.<YOUR_HOSTNAME>/api/validator` should be routed to `/api/validator` at port 5003 of service `validator-app` in the `validator` namespace
* `https://cns.validator.<YOUR_HOSTNAME>` should be routed to service `ans-web-ui` in the `validator` namespace
* `https://cns.validator.<YOUR_HOSTNAME>/api/validator` should be routed to `/api/validator` at port 5003 of service `validator-app` in the `validator` namespace

<Warning>
  To keep the attack surface on your validator deployment small, please disallow ingress connections to all other services in your validator deployment. It should be assumed that opening up *any* additional port or service represents a security risk that needs to be carefully evaluated on a case-by-case basis. In addition, it is recommended to restrict access to above services to a limited number of explicitly trusted IP address ranges.
</Warning>

Internet ingress configuration is often specific to the network configuration and scenario of the cluster being configured. To illustrate the basic requirements of a Validator node ingress, we have provided a Helm chart that configures ingress according to the routes above using Istio, as detailed in the sections below.

### Requirements

In order to install the reference charts, the following must be satisfied in your cluster:

* *cert-manager* must be available in the cluster (See [cert-manager documentation](https://cert-manager.io/docs/installation/helm/))
* *istio* should be installed in the cluster (See [istio documentation](https://istio.io/latest/docs/setup/))

*Note that their deployments are often platform-dependent and good documentations on how to set them up can be found online.*

**Example of Istio installation:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
helm repo add istio https://istio-release.storage.googleapis.com/charts
helm repo update
helm install istio-base istio/base -n istio-system --set defaults.global.istioNamespace=cluster-ingress --wait
helm install istiod istio/istiod -n cluster-ingress --set global.istioNamespace="cluster-ingress" --set meshConfig.accessLogFile="/dev/stdout"  --wait
```

### Installation Instructions

<Tabs>
  <Tab title="DevNet (0.6.4)">
    Create a `cluster-ingress` namespace:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    Ensure that there is a cert-manager certificate available in a secret named `cn-net-tls`. An example of a suitable certificate definition:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.validator.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    Create a file named `istio-gateway-values.yaml` with the following content (Tip: on GCP you can get the cluster IP from `gcloud compute addresses list`):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    And install it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    Create an Istio Gateway resource in the `cluster-ingress` namespace. Save the following to a file named `gateway.yaml`, and replace `YOUR_HOSTNAME` with the actual hostname you want to use for your validator node (and has a DNS record pointing to the cluster IP you configured above):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    And apply it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    This gateway terminates tls using the secret that you configured above, and exposes raw http traffic in its outbound port 443. Istio VirtualServices can now be created to route traffic from there to the required pods within the cluster. A reference Helm chart is provided for that, which can be installed after

    1. replacing `YOUR_HOSTNAME` in `splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml` and
    2. setting `nameServiceDomain` in the same file to `"cns"`

    using:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    Create a `cluster-ingress` namespace:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    Ensure that there is a cert-manager certificate available in a secret named `cn-net-tls`. An example of a suitable certificate definition:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.validator.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    Create a file named `istio-gateway-values.yaml` with the following content (Tip: on GCP you can get the cluster IP from `gcloud compute addresses list`):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    And install it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    Create an Istio Gateway resource in the `cluster-ingress` namespace. Save the following to a file named `gateway.yaml`, and replace `YOUR_HOSTNAME` with the actual hostname you want to use for your validator node (and has a DNS record pointing to the cluster IP you configured above):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    And apply it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    This gateway terminates tls using the secret that you configured above, and exposes raw http traffic in its outbound port 443. Istio VirtualServices can now be created to route traffic from there to the required pods within the cluster. A reference Helm chart is provided for that, which can be installed after

    1. replacing `YOUR_HOSTNAME` in `splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml` and
    2. setting `nameServiceDomain` in the same file to `"cns"`

    using:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    Create a `cluster-ingress` namespace:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl create ns cluster-ingress
    ```

    Ensure that there is a cert-manager certificate available in a secret named `cn-net-tls`. An example of a suitable certificate definition:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: cert-manager.io/v1
    kind: Certificate
    metadata:
       name: cn-certificate
       namespace: cluster-ingress
    spec:
        dnsNames:
        - '*.validator.YOUR_HOSTNAME'
        issuerRef:
            name: letsencrypt-production
        secretName: cn-net-tls
    ```

    Create a file named `istio-gateway-values.yaml` with the following content (Tip: on GCP you can get the cluster IP from `gcloud compute addresses list`):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    service:
        loadBalancerIP: "YOUR_CLUSTER_IP"
        loadBalancerSourceRanges:
            - "35.194.81.56/32"
            - "35.198.147.95/32"
            - "35.189.40.124/32"
            - "34.132.91.75/32"
    ```

    And install it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install istio-ingress istio/gateway -n cluster-ingress -f istio-gateway-values.yaml
    ```

    Create an Istio Gateway resource in the `cluster-ingress` namespace. Save the following to a file named `gateway.yaml`, and replace `YOUR_HOSTNAME` with the actual hostname you want to use for your validator node (and has a DNS record pointing to the cluster IP you configured above):

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    apiVersion: networking.istio.io/v1alpha3
    kind: Gateway
    metadata:
      name: cn-http-gateway
      namespace: cluster-ingress
    spec:
      selector:
        app: istio-ingress
        istio: ingress
      servers:
      - port:
          number: 443
          name: https
          protocol: HTTPS
        tls:
          mode: SIMPLE
          credentialName: cn-net-tls # name of the secret created above
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
      - port:
          number: 80
          name: http
          protocol: HTTP
        tls:
          httpsRedirect: true
        hosts:
        - "*.YOUR_HOSTNAME"
        - "YOUR_HOSTNAME"
    ```

    And apply it to your cluster:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl apply -f gateway.yaml -n cluster-ingress
    ```

    This gateway terminates tls using the secret that you configured above, and exposes raw http traffic in its outbound port 443. Istio VirtualServices can now be created to route traffic from there to the required pods within the cluster. A reference Helm chart is provided for that, which can be installed after

    1. replacing `YOUR_HOSTNAME` in `splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml` and
    2. setting `nameServiceDomain` in the same file to `"cns"`

    using:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm install cluster-ingress-validator oci://ghcr.io/digital-asset/decentralized-canton-sync/helm/splice-cluster-ingress-runbook -n validator --version ${CHART_VERSION} -f splice-node/examples/sv-helm/validator-cluster-ingress-values.yaml
    ```
  </Tab>
</Tabs>

## Logging into the wallet UI

After you deploy your ingress, open your browser at [https://wallet.validator.YOUR\_HOSTNAME](https://wallet.validator.YOUR_HOSTNAME) and login using the credentials for the user that you configured as `validatorWalletUser` earlier. Once logged in one should see the transactions page.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/wallet_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=7df40cdc3f81b03dcb50ce9175c7e280" width="600" alt="After logged in into the wallet UI" data-path="images/splice/wallet_home.png" />

<div className="todo">
  explain the config sections below in a way that makes them also accessible to the Docker compose users
</div>

## Configuring automatic traffic purchases

By default your node will be configured to automatically purchase traffic on a pay-as-you-go basis (see automatically purchase traffic). To disable or tune to your needs, edit the following section in the validator-values.yaml file:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Configuring a validator's traffic top-up loop;
# see documentation for more detailed information.
topup:
  # set to false in order to disable automatic traffic top-ups
  enabled: true
  # target throughput in bytes / second of sequenced traffic; targetThroughput=0 <=> enabled=false
  targetThroughput: 20000
  # minTopupInterval - minimum time interval that must elapse before the next top-up
  minTopupInterval: "1m"
```

<p>On each successful top-up, the validator app purchases a `top-up amount` of roughly `targetThroughput * minTopupInterval` bytes of traffic (specific amount can vary due to rounding-up). The `minTopupInterval` allows validator operators to control the upper-bound frequency at which automated top-ups happen. If the top-up amount is below the synchronizer-wide `minTopupAmount` (see [traffic parameters](/docs/canton/global-synchronizer-deployment-synchronizer-traffic#traffic-parameters)), `minTopupInterval` is automatically stretched so that at least `minTopupAmount` bytes of traffic are purchased while respecting the configured `targetThroughput`.</p>

<p>The next top-up gets triggered when all of the following conditions are met:</p>

<ul>
  <li>The available [extra traffic balance](/docs/canton/global-synchronizer-deployment-synchronizer-traffic#traffic-accounting-what-counts-as-traffic) drops below the configured top-up amount (i.e., below `targetThroughput * minTopupInterval`).</li>

  <li>At least `minTopupInterval` has elapsed since the last top-up.</li>

  <li>The validator has sufficient CC in its wallet to buy the top-up amount worth on traffic (except on DevNet, where the validator app will automatically tap enough coin to purchase traffic).</li>
</ul>

<p>Validators receive a small amount of free traffic from the Super Validators, which suffices for submitting the top-up transaction. However, if many other transactions are submitted, you may run into a situation where you have exhausted also the free traffic, thus the validator cannot submit the top-up transaction. The free traffic grant accumulates gradually and continuously. When no transactions are submitted, it takes about twenty minutes for free traffic to accumulate to the maximum possible. If you've consumed your traffic balance by submitting too many transactions without purchasing traffic, pause your Validator node (validator app and participant) for twenty minutes to allow your free traffic balance to accumulate.</p>

<div className="todo">
  \* show error message that people will see while the traffic purchase fails due to insufficient funds; it is currentlye here: `error-insufficient-funds` \* link to the option to disable automatic top-ups, and call out the option of using third-party traffic providers
</div>

## Configuring sweeps and auto-accepts of transfer offers

<p>You can optionally configure the validator to automatically create transfer offers to other parties on the network whenever the balance of certain parties that it hosts exceeds a certain threshold.</p>

<p>Whenever the balance of `<senderPartyID>` exceeds `maxBalanceUSD`, the validator will automatically create a transfer offer to `<receiverPartyId>`, for an amount that leaves `minBalanceUSD` in the sender's wallet. Note that you will need to know the party IDs of both the sender and receiver, which can be copied from the wallet UIs of the respective users (in the top right corner). This therefore needs to be applied to the Helm chart in a second step after the initial deployment, once the party IDs are known.</p>

<p>Whenever the validator receives a transfer offer from `<senderPartyID>` to `<receiverPartyId>`, it will automatically accept it. Similarly to sweeps, party IDs must be known in order to apply this configuration.</p>

To do so, uncomment and fill in the following section in the `validator-values.yaml` file:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# If you want funds sweeped out of parties in this validator, uncomment and fill in the following:
#walletSweep:
#  "<senderPartyId>":
#    maxBalanceUSD: <maxBalanceUSD>
#    minBalanceUSD: <minBalanceUSD>
#    receiver: "<receiverPartyId>"
#    useTransferPreapproval: false # sweep by transferring directly through the transfer preapproval of the receiver,
#                                    if set to false sweeping creates transfer offers that need to be accepted on the receiver side.
#                                    Note that this refers to the preapprovals described in /appdev/modules/m7-canton-coin-preapprovals
#                                    and not to auto accepting transfers. Auto accept transfers does not setup preapproval contracts that allow
#                                    for a direct transfer but just automates the acceptance of the transfer offer so in that case
#                                    useTransferPreapproval should be set to false.
```

Similarly, you can configure the validator to automatically accept transfer offers from certain parties on the network. To do so, uncomment and fill in the following section in the `validator-values.yaml` file:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# To configure the validator to auto-accept transfer offers from specific parties, uncomment and fill in the following:
#autoAcceptTransfers:
#  "<receiverPartyId>":
#    fromParties:
#      - "<senderPartyId>"
```

## Logging into the CNS UI

You can open your browser at [https://cns.validator.YOUR\_HOSTNAME](https://cns.validator.YOUR_HOSTNAME) and login using the credentials for the user that you configured as `validatorWalletUser` earlier. You will be able to register a name on the Canton Name Service.

<img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/splice/ans_home.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=0084097a0e8f4d5d73d901049a71b3c3" width="600" alt="After logged in into the CNS UI" data-path="images/splice/ans_home.png" />

## Participant Pruning

By default, participants preserve all history. However, this leads to gradually growing databases and can slow down certain queries, in particular, queries for the active contract set on the ledger API.

To mitigate that, it is possible to enable participant pruning which will remove all history beyond a specified retention point and only preserve the active contract set.

Note that this only affects the participant stores. The CN apps (Validator, SV and Scan) are unaffected by enabling this, so e.g., the history in your wallet will never be pruned.

Below you can see an example of the pruning config that you need to add to `validator-values.yaml` to retain only the history for the last 48h.

Note that if your node is down for longer than the pruning window (48 hours in the example above), your node will most probably get corrupted, as the apps race catching up with the participant's attempts to keep pruning. It is therefore advisable to set the pruning window to a value that you are comfortable with in terms of guaranteeing uptime of your node. Setting it to 30 days is in general a reasonable choice, as the sequencers currently are also pruned after 30 days, so you will not be able to catch up with the network after a longer downtime anyway (see Disaster Recovery for disaster recovery guidelines).

Refer to the [pruning guide](/docs/canton/global-synchronizer-production-operations-pruning) for more details on participant pruning.

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# To configure participant pruning uncomment the following section.
# Refer to the documentation for more details.
# participantPruningSchedule:
#   cron: 0 /10 * * * ? # Run every 10min
#   maxDuration: 5m # Run for a max of 5min per iteration
#   retention: 48h # Retain history that is newer than 48h.
```

## Configuring init containers

If you need to configure init containers on the participant or validator deployments, you can use the following helm values for `splice-participant` or `splice-validator`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# if you want to disable the default postgres init container:
persistence:
  enablePgInitContainer: false

# if you want additional init containers:
extraInitContainers:
  - name: my-extra-container
    image: busybox
    command: [ "sh", "-c", "echo 'example extra container'" ]
```

## Working around volume ownership issues

The containers in the `splice-validator` chart run as non-root users (specifically, user:group 1001:1001) for security reasons. The pod mounts volumes for use by the containers, and these volumes need to be owned by the user that the containers run as. The Helm chart uses an `fsGroup` [security context](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) to ensure that the mounted volumes are owned by the correct user. In certain environments, however, this does not work as expected and the mounted volumes are owned by root. If you encounter this issue, you can work around it by creating init containers that change the ownership of the mounted volumes to the correct user.

For example, for the `/domain-upgrade-dump` volume (required for synchronizer upgrades), you can add the following to your `validator-values.yaml` file:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
extraInitContainers:
    - name: chown-domain-upgrade-dump
      image: busybox:1.37.0
      command: ["sh", "-c", "chown -R 1001:1001 /domain-upgrade-dump"]
      volumeMounts:
        - name: domain-upgrade-dump-volume
          mountPath: /domain-upgrade-dump
```

A similar workaround will be required for mounting a usable `/participant-bootstrapping-dump` (required when recovering from identities backup).

[^1]: The URL must be reachable from the Canton participant and validator app running in your cluster, as well as from all web browsers that should be able to interact with the wallet and CNS UIs.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
