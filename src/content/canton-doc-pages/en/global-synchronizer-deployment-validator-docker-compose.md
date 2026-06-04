---
title: "Docker Compose Validator Deployment"
slug: "global-synchronizer-deployment-validator-docker-compose"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-docker-compose.md"
source_title: "Docker Compose Validator Deployment"
tags:
  - global-synchronizer
  - deployment
  - validator-docker-compose
---

# Docker Compose Validator Deployment

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Docker Compose Validator Deployment

> Deploy a Canton Network validator using Docker Compose

This section describes how to deploy a standalone validator node on a VM or a local machine using [Docker Compose](https://docs.docker.com/compose/). The deployment consists of the validator node along with associated wallet and CNS UIs, and onboards the validator node to the target network.

This deployment is useful for:

* Application development, where one needs an ephemeral validator that is easy to deploy.
* Production validators, with the following caveats:
  * The default deployment is highly insecure. Authentication should be enabled as described in the authentication section.
  * There is no support for ingress from outside your machine, nor is there support for TLS. The deployment should be kept local to your machine only and not exposed externally.
  * Reliability & scalability: docker-compose will restart containers that crash, and the deployment supports backup\&restore as detailed below, but a docker-compose deployment is inherently more limited than a cloud-based Kubernetes one.
  * Monitoring: The deployment, as opposed to a Kubernetes-based one, does not include monitoring.
  * For production settings, you should aim to keep your validator up and running constantly, in order to avoid losing out on rewards, and avoid issues with catching up on ledger state after significant downtime.

## Requirements

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. A linux/MacOS machine with the following:

       1. [docker compose](https://docs.docker.com/compose/install/) - at least version 2.26.0 or newer
       2. [curl](https://curl.se/)
       3. [jq](https://jqlang.org/)

       Note that both AMD64 and ARM64 architectures are supported.

    To validate that the dependencies are set up correctly, run the following commands. All commands should succeed and print out the version. Note that the exact versions you see may be different from the example here. As long as you have docker-compose 2.26.0 or newer you should be fine.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > docker compose version
    Docker Compose version 2.32.1
    > curl --version
    curl 8.11.0 (x86_64-pc-linux-gnu) libcurl/8.11.0 OpenSSL/3.3.2 zlib/1.3.1 brotli/1.1.0 zstd/1.5.6 libidn2/2.3.7 libpsl/0.21.5 libssh2/1.11.1 nghttp2/1.64.0
    Release-Date: 2024-11-06
    Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
    > jq --version
    jq-1.7.1
    ```

    2. Your machine should either be connected to a VPN that is whitelisted on the network (contact your sponsor SV to obtain access), or have a static egress IP address. In the latter case, please provide that IP address to your sponsor SV to add it to the firewall rules.
    3. Please download the release artifacts containing the docker-compose files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz">Download Bundle (DevNet 0.6.4)</a>, and extract the bundle:

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

    ### Required Network Parameters

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

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. A linux/MacOS machine with the following:

       1. [docker compose](https://docs.docker.com/compose/install/) - at least version 2.26.0 or newer
       2. [curl](https://curl.se/)
       3. [jq](https://jqlang.org/)

       Note that both AMD64 and ARM64 architectures are supported.

    To validate that the dependencies are set up correctly, run the following commands. All commands should succeed and print out the version. Note that the exact versions you see may be different from the example here. As long as you have docker-compose 2.26.0 or newer you should be fine.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > docker compose version
    Docker Compose version 2.32.1
    > curl --version
    curl 8.11.0 (x86_64-pc-linux-gnu) libcurl/8.11.0 OpenSSL/3.3.2 zlib/1.3.1 brotli/1.1.0 zstd/1.5.6 libidn2/2.3.7 libpsl/0.21.5 libssh2/1.11.1 nghttp2/1.64.0
    Release-Date: 2024-11-06
    Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
    > jq --version
    jq-1.7.1
    ```

    2. Your machine should either be connected to a VPN that is whitelisted on the network (contact your sponsor SV to obtain access), or have a static egress IP address. In the latter case, please provide that IP address to your sponsor SV to add it to the firewall rules.
    3. Please download the release artifacts containing the docker-compose files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz">Download Bundle (TestNet 0.6.3)</a>, and extract the bundle:

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

    ### Required Network Parameters

    <p>To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.</p>

    <ul>
      <li>**MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).</li>

      <li>**SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.test.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.test.global.canton.network.sync.global">[https://sv.sv-1.test.global.canton.network.sync.global](https://sv.sv-1.test.global.canton.network.sync.global)</a>.</li>
    </ul>

    <p>**ONBOARDING\_SECRET**<br />
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.</p>

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. A linux/MacOS machine with the following:

       1. [docker compose](https://docs.docker.com/compose/install/) - at least version 2.26.0 or newer
       2. [curl](https://curl.se/)
       3. [jq](https://jqlang.org/)

       Note that both AMD64 and ARM64 architectures are supported.

    To validate that the dependencies are set up correctly, run the following commands. All commands should succeed and print out the version. Note that the exact versions you see may be different from the example here. As long as you have docker-compose 2.26.0 or newer you should be fine.

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > docker compose version
    Docker Compose version 2.32.1
    > curl --version
    curl 8.11.0 (x86_64-pc-linux-gnu) libcurl/8.11.0 OpenSSL/3.3.2 zlib/1.3.1 brotli/1.1.0 zstd/1.5.6 libidn2/2.3.7 libpsl/0.21.5 libssh2/1.11.1 nghttp2/1.64.0
    Release-Date: 2024-11-06
    Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns mqtt pop3 pop3s rtsp scp sftp smb smbs smtp smtps telnet tftp
    Features: alt-svc AsynchDNS brotli GSS-API HSTS HTTP2 HTTPS-proxy IDN IPv6 Kerberos Largefile libz NTLM PSL SPNEGO SSL threadsafe TLS-SRP UnixSockets zstd
    > jq --version
    jq-1.7.1
    ```

    2. Your machine should either be connected to a VPN that is whitelisted on the network (contact your sponsor SV to obtain access), or have a static egress IP address. In the latter case, please provide that IP address to your sponsor SV to add it to the firewall rules.
    3. Please download the release artifacts containing the docker-compose files, from here: <a href="https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz">Download Bundle (MainNet 0.6.2)</a>, and extract the bundle:

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

    ### Required Network Parameters

    <p>To initialize your validator node, you need the following parameters that define the network you're onboarding to and the secret required for doing so.</p>

    <ul>
      <li>**MIGRATION\_ID** — The current migration id of the network (dev/test/mainnet) you are trying to connect to. This value is frozen and must not be changed from the last value. You can find this on [https://sync.global/sv-network/](https://sync.global/sv-network/).</li>

      <li>**SPONSOR\_SV\_URL** — The URL of the SV app of your SV sponsor. This should be of the form <a href="https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR">https\://sv.sv-1.global.canton.network.YOUR\_SV\_SPONSOR</a>, e.g., if the Global Synchronizer Foundation is your sponsor use <a href="https://sv.sv-1.global.canton.network.sync.global">[https://sv.sv-1.global.canton.network.sync.global](https://sv.sv-1.global.canton.network.sync.global)</a>.</li>
    </ul>

    <p>**ONBOARDING\_SECRET**<br />
    The onboarding secret provided by your sponsor. If you don't already have one, ask your sponsor. Note that onboarding secrets are one-time use and expire after 48 hours. If you don't join before it expires, you need to request a new secret from your SV sponsor.</p>

    Additional parameters describing your own setup as opposed to the connection to the network are described below.
  </Tab>
</Tabs>

### HTTP Proxy configuration

If you need to use an HTTP forward proxy for egress in your environment, you need to set `https.proxyHost` and `https.proxyPort` in `JAVA_TOOL_OPTIONS` in `splice-node/docker-compose/validator/compose.yaml` to use the HTTP proxy for outgoing connections. You need to do this for both the validator and the participant services:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  services:
    validator:
      environment:
        JAVA_TOOL_OPTIONS: >-
          -Dhttps.proxyHost=your.proxy.host
          -Dhttps.proxyPort=your_proxy_port
```

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  services:
    participant:
      environment:
        JAVA_TOOL_OPTIONS: >-
          -Dhttps.proxyHost=your.proxy.host
          -Dhttps.proxyPort=your_proxy_port
```

Replace `your.proxy.host` and `your_proxy_port` with the actual host and port of your HTTP proxy. Proxy authentication is currently not supported.

## Bypassing the proxy for specific hosts

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

Example that proxies external traffic from the `validator` service but bypasses the proxy for `localhost` / `127.0.0.1`, any host in the `.internal` domain, and any IPv4 address whose literal string representation starts with `10.`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  services:
    validator:
      environment:
        JAVA_TOOL_OPTIONS: >-
          -Dhttps.proxyHost=your.proxy.host
          -Dhttps.proxyPort=your_proxy_port
          -Dhttp.nonProxyHosts=localhost|127.0.0.1|*.internal|10.*
```

## Deployment

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. Change to the `docker-compose` directory inside the extracted bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cd splice-node/docker-compose/validator
    ```

    2. Export the current version to an environment variable: export IMAGE\_TAG=0.6.4
    3. Run the following command to start the validator node, and wait for it to become ready (could take a few minutes):

    > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > ./start.sh -s "<SPONSOR_SV_URL>" -o "<ONBOARDING_SECRET>" -p "<party_hint>" -m "<MIGRATION_ID>" -w
    > ```
    >
    > Where:
    >
    > `<party_hint>` will be used as the prefix of the Party ID of your validator's administrator.
    > This must be of format `<organization>-<function>-<enumerator>`, e.g. `myCompany-myWallet-1`. It cannot be changed over time as it is part of the validator operator party ID.

    Note that the validator may be stopped with the command `./stop.sh` and restarted again with the same `start.sh` command as above. Its data will be retained between invocations. In subseqent invocations, the secret itself may be left empty, but the `-o` is still mandatory, so a `-o ""` argument should be provided.
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. Change to the `docker-compose` directory inside the extracted bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cd splice-node/docker-compose/validator
    ```

    2. Export the current version to an environment variable: export IMAGE\_TAG=0.6.3
    3. Run the following command to start the validator node, and wait for it to become ready (could take a few minutes):

    > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > ./start.sh -s "<SPONSOR_SV_URL>" -o "<ONBOARDING_SECRET>" -p "<party_hint>" -m "<MIGRATION_ID>" -w
    > ```
    >
    > Where:
    >
    > `<party_hint>` will be used as the prefix of the Party ID of your validator's administrator.
    > This must be of format `<organization>-<function>-<enumerator>`, e.g. `myCompany-myWallet-1`. It cannot be changed over time as it is part of the validator operator party ID.

    Note that the validator may be stopped with the command `./stop.sh` and restarted again with the same `start.sh` command as above. Its data will be retained between invocations. In subseqent invocations, the secret itself may be left empty, but the `-o` is still mandatory, so a `-o ""` argument should be provided.
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Change to the `docker-compose` directory inside the extracted bundle:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    cd splice-node/docker-compose/validator
    ```

    2. Export the current version to an environment variable: export IMAGE\_TAG=0.6.2
    3. Run the following command to start the validator node, and wait for it to become ready (could take a few minutes):

    > ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    > ./start.sh -s "<SPONSOR_SV_URL>" -o "<ONBOARDING_SECRET>" -p "<party_hint>" -m "<MIGRATION_ID>" -w
    > ```
    >
    > Where:
    >
    > `<party_hint>` will be used as the prefix of the Party ID of your validator's administrator.
    > This must be of format `<organization>-<function>-<enumerator>`, e.g. `myCompany-myWallet-1`. It cannot be changed over time as it is part of the validator operator party ID.

    Note that the validator may be stopped with the command `./stop.sh` and restarted again with the same `start.sh` command as above. Its data will be retained between invocations. In subseqent invocations, the secret itself may be left empty, but the `-o` is still mandatory, so a `-o ""` argument should be provided.
  </Tab>
</Tabs>

## Logging into the wallet UI

<Note>
  Docker Compose-based validator deployments use `.localhost` subdomains for addressing, such as `wallet.localhost`. `.localhost` URLs reportedly do not work on some browsers. If you encounter issues please try using a different browser such as Firefox or Chrome. If you're encountering issues with reaching APIs from a custom program or script, you may need to set the `HOST` header on HTTP requests explicitly to the target `.localhost` address.
</Note>

The wallet UI is accessible at [http://wallet.localhost](http://wallet.localhost) in your browser. The validator administrator's username is `administrator`. Insert that name into the username field and click `Log in`, and you should see the wallet of the administrator of your wallet.

You can also logout of the administrator account and login as any other username. The first time a user logs in, they will be prompted with a message asking them to confirm whether they wish to be onboarded to the validator node.

<div className="todo">
  link to section that explains what this onbarding means
</div>

## Logging into the CNS UI

You can open your browser at [http://ans.localhost](http://ans.localhost) (note that this is currently by default `ans` and not `cns`), and login using the same administrator user, or any other user that has been onboarded via the wallet, in order to purchase a CNS entry for that user.

### Accessing the Canton Participant APIs

The [JSON Ledger API](/sdks-tools/api-reference/json-api) is exposed under `json-ledger-api.localhost:80`. Note that for some clients you may explicitly need to set the `Host: json-ledger-api.localhost` header for this to get resolved correctly.

The [gRPC Ledger API](/sdks-tools/api-reference/ledger-api) is exposed under `grpc-ledger-api.localhost:80`. Note that for some clients you may explicitly need to set the `:authority: json-ledger-api.localhost` pseudo-header for this to get resolved correctly.

The Canton Admin API is not exposed by default as it does not yet support auth. There is a commented out section in `nginx.conf` that you can enable to expose it if you ensure that it is not exposed publicly, e.g., through network restrictions.

## Configuring Authentication

<Warning>
  The default deployment uses highly insecure self-signed tokens. Anyone with access to the wallet UI (or the machine and/or its network interface) may log in to your wallet as a user of their choice. For any production use, you should configure proper authentication as described in this section.
</Warning>

Please refer to the authentication section for instructions on how to set up an OAuth provider for your validator. The URLs to configure for callbacks are `http://wallet.localhost` and `http://ans.localhost`.

Once you have set up your OAuth provider, you need to configure it by setting the following environment variables in the `.env` file:

<table>
  <thead>
    <tr className="header">
      <th>Name</th>
      <th>Value</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td>AUTH\_URL</td>
      <td>The URL of your OIDC provider for obtaining the <code>openid-configuration</code> and <code>jwks.json</code>.</td>
    </tr>

    <tr className="even">
      <td>AUTH\_JWKS\_URL</td>
      <td>The URL of your OIDC provider for obtaining the <code>jwks.json</code>, will typically be <code>\${AUTH_URL}/.well-known/jwks.json</code>.</td>
    </tr>

    <tr className="odd">
      <td>AUTH\_WELLKNOWN\_URL</td>
      <td>The URL of your OIDC provider for obtaining the <code>openid-configuration</code>, will typically be <code>\${AUTH_URL}/.well-known/openid-configuration</code>.</td>
    </tr>

    <tr className="even">
      <td>LEDGER\_API\_AUTH\_AUDIENCE</td>
      <td>The audience for the participant ledger API, e.g. <code>[https://ledger\_api.example.com](https://ledger_api.example.com)</code>. This sets the <code>ledger-api.auth-services.target-audience</code> configuration for the participant.</td>
    </tr>

    <tr className="odd">
      <td>LEDGER\_API\_AUTH\_SCOPE</td>
      <td>The scope for the participant ledger API. This sets the participant's <code>ledger-api.auth-services.target-scope</code> configuration. Optional.</td>
    </tr>

    <tr className="even">
      <td>VALIDATOR\_AUTH\_AUDIENCE</td>
      <td>The audience for the validator backend API. e.g. <code>[https://validator.example.com](https://validator.example.com)</code>.</td>
    </tr>

    <tr className="odd">
      <td>VALIDATOR\_AUTH\_CLIENT\_ID</td>
      <td>The client id of the OAuth app for the validator app backend.</td>
    </tr>

    <tr className="even">
      <td>VALIDATOR\_AUTH\_CLIENT\_SECRET</td>
      <td>The client secret of the OAuth app for the validator app backend.</td>
    </tr>

    <tr className="odd">
      <td>LEDGER\_API\_ADMIN\_USER</td>
      <td>Should match the `sub` field of JWTs issued for the validator app. For some auth providers, this would be formed as <code>CLIENT\_ID\@clients</code>.</td>
    </tr>

    <tr className="even">
      <td>WALLET\_ADMIN\_USER</td>
      <td>The user ID of the user which should login as the wallet administrator. Note that this should be the full user id, e.g., <code>auth0|43b68e1e4978b000cefba352</code>, <em>not</em> only the suffix <code>43b68e1e4978b000cefba352</code>.</td>
    </tr>

    <tr className="odd">
      <td>WALLET\_UI\_CLIENT\_ID</td>
      <td>The client id of the OAuth app for the wallet UI.</td>
    </tr>

    <tr className="even">
      <td>ANS\_UI\_CLIENT\_ID</td>
      <td>The client id of the OAuth app for the CNS UI.</td>
    </tr>

    <tr className="odd">
      <td>CONTACT\_POINT</td>
      <td>The contact point for your validator node that can be used by other node operators to reach out to you if needed (slack username or an email address). Optional</td>
    </tr>
  </tbody>
</table>

In order to enable auth in the deployment, add the `-a` flag to the `start.sh` command, as follows:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./start.sh -s "<SPONSOR_SV_URL>" -o "<ONBOARDING_SECRET>" -p "<party_hint>" -m "<MIGRATION_ID>" -w -a
```

If you have already deployed a non-authenticated validator on your machine, you can migrate it to an authenticated one by stopping the validator with `./stop.sh` and restarting it with the `-a` flag as above. The validator operator user will be automatically migrated, and the user indicated by the `WALLET_ADMIN_USER` variable will be associated with the validator operator party. If you have also onboarded other users onto your validator, those will not be automatically migrated, and you need to manually associate the OAuth users with their corresponding parties. In order to do that, first take note of the party IDs of all relevant users (do this before stopping the unauthenticated validator), e.g. by copying them from the top-right corner of their wallet UIs. Now for every user that you wish to migrate, follow the instructions for associating a user with a party in the Users, Parties and Wallets in the Splice Wallet section, but replace the admin party ID with the party ID which you wish to associate with each user.

## Configuring Automatic Traffic Purchases

Your node is configured to automatically purchase traffic on a pay-as-you-go basis (see automatically purchase traffic). To tune to your needs, you can set environment variables, for example:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export TARGET_TRAFFIC_THROUGHPUT=20000 # target throughput in bytes/second
export MIN_TRAFFIC_TOPUP_INTERVAL="1m" # minimum interval between top-ups
```

<p>On each successful top-up, the validator app purchases a `top-up amount` of roughly `targetThroughput * minTopupInterval` bytes of traffic (specific amount can vary due to rounding-up). The `minTopupInterval` allows validator operators to control the upper-bound frequency at which automated top-ups happen. If the top-up amount is below the synchronizer-wide `minTopupAmount` (see [traffic parameters](/docs/canton/global-synchronizer-deployment-synchronizer-traffic#traffic-parameters)), `minTopupInterval` is automatically stretched so that at least `minTopupAmount` bytes of traffic are purchased while respecting the configured `targetThroughput`.</p>

<p>The next top-up gets triggered when all of the following conditions are met:</p>

<ul>
  <li>The available [extra traffic balance](/docs/canton/global-synchronizer-deployment-synchronizer-traffic#traffic-accounting-what-counts-as-traffic) drops below the configured top-up amount (i.e., below `targetThroughput * minTopupInterval`).</li>

  <li>At least `minTopupInterval` has elapsed since the last top-up.</li>

  <li>The validator has sufficient CC in its wallet to buy the top-up amount worth on traffic (except on DevNet, where the validator app will automatically tap enough coin to purchase traffic).</li>
</ul>

<p>Validators receive a small amount of free traffic from the Super Validators, which suffices for submitting the top-up transaction. However, if many other transactions are submitted, you may run into a situation where you have exhausted also the free traffic, thus the validator cannot submit the top-up transaction. The free traffic grant accumulates gradually and continuously. When no transactions are submitted, it takes about twenty minutes for free traffic to accumulate to the maximum possible. If you've consumed your traffic balance by submitting too many transactions without purchasing traffic, pause your Validator node (validator app and participant) for twenty minutes to allow your free traffic balance to accumulate.</p>

## Configuring sweeps and auto-accepts of transfer offers

<p>You can optionally configure the validator to automatically create transfer offers to other parties on the network whenever the balance of certain parties that it hosts exceeds a certain threshold.</p>

<p>Whenever the balance of `<senderPartyID>` exceeds `maxBalanceUSD`, the validator will automatically create a transfer offer to `<receiverPartyId>`, for an amount that leaves `minBalanceUSD` in the sender's wallet. Note that you will need to know the party IDs of both the sender and receiver, which can be copied from the wallet UIs of the respective users (in the top right corner). This therefore needs to be applied to the Helm chart in a second step after the initial deployment, once the party IDs are known.</p>

<p>Whenever the validator receives a transfer offer from `<senderPartyID>` to `<receiverPartyId>`, it will automatically accept it. Similarly to sweeps, party IDs must be known in order to apply this configuration.</p>

To do so, fill the following section and add the following additional config to your validator environment:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# sweep by transferring directly through the transfer preapproval of the receiver,
# if set to false sweeping creates transfer offers that need to be accepted on the receiver side.
# Note that this refers to the preapprovals described in /appdev/modules/m7-canton-coin-preapprovals
# and not to auto accepting transfers. Auto accept transfers does not setup preapproval contracts that allow
# for a direct transfer but just automates the acceptance of the transfer offer so in that case
# useTransferPreapproval should be set to false.
services:
  validator:
    environment:
       - |
          ADDITIONAL_CONFIG_WALLET_SWEEP=
            canton.validator-apps.validator_backend.wallet-sweep {
              "<senderPartyId1>" {
                max-balance-usd = 1000
                min-balance-usd = 100
                receiver = "<receiverPartyId>"
                use-transfer-preapproval = false
              }
            }
```

Similarly, you can configure the validator to automatically accept transfer offers from certain parties on the network. To do so, add the following additional config:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
   services:
     validator:
       environment:
          - |
             ADDITIONAL_CONFIG_AUTO_ACCEPT_TRANSFERS=
               canton.validator-apps.validator_backend.auto-accept-transfers {
                 "<receiverPartyId>" {
                   from-parties = ["<senderPartyId1>", "<senderPartyId2>"]
                 }
               }
```

## Integration with systemd and other init systems

If you want to manage the validator through systemd or a similar init system, create a service that calls the `start.sh` script with the right arguments. However, note that `start.sh` invokes `docker compose up` with the `-d/--detach` option so the script exits after the containers are up instead of continuing running.

You need to make sure that your service does not stop docker compose at that point. To accomplish this with systemd set `RemainAfterExit=true`. Refer to the [systemd documentation](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) for more details. If you are using another init system, look for similar options to ensure that docker compose continues running after the script exits.

Alternatively, you can edit the script to remove the `-d` option so the script continues running.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
