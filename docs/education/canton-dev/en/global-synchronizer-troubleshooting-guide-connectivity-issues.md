---
title: "Connectivity Issues"
slug: "global-synchronizer-troubleshooting-guide-connectivity-issues"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/connectivity-issues.md"
source_title: "Connectivity Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - connectivity-issues
---

# Connectivity Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectivity Issues

> Diagnosing and resolving synchronizer connection failures, TLS errors, and VPN problems

Connectivity failures prevent your validator from communicating with the synchronizer. The symptoms vary -- from outright connection refusals to subtle TLS handshake errors -- but the diagnostic approach is consistent.

## Cannot Connect to Synchronizer

If your validator logs show:

```
Request failed for sequencer. Is the server running?
```

or

```
SEQUENCER_SUBSCRIPTION_LOST: Lost subscription to sequencer
```

Work through these checks in order.

### 1. Verify the Sequencer URL

Confirm that your configuration points to the correct sequencer endpoint for your target network:

* **DevNet:** `https://sequencer.dev.sync.global`
* **TestNet:** `https://sequencer.test.sync.global`
* **MainNet:** `https://sequencer.sync.global`

A common mistake is using the scan URL (`https://scan.sv-2...`) instead of the SV sponsor URL during onboarding. The scan URL is for read-only network data, not for validator registration.

### 2. Test Network Reachability

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# DNS resolution
dig +short sequencer.sync.global

# TCP connectivity
nc -zv sequencer.sync.global 443

# Full TLS handshake
openssl s_client -connect sequencer.sync.global:443 -servername sequencer.sync.global </dev/null
```

If `nc` times out, a firewall or security group is blocking egress on port 443.

### 3. Check Firewall and Security Groups

Your validator requires outbound HTTPS on port 443 to the synchronizer. If you run in a cloud environment, verify:

* The security group attached to your instance or pod allows outbound TCP/443.
* No network ACL is blocking the traffic.
* If you use an HTTP proxy, Canton supports proxy configuration via JVM system properties (`-Dhttps.proxyHost`, `-Dhttps.proxyPort`).

## TLS Handshake Failures

TLS errors typically produce log messages like:

```
io.grpc.StatusRuntimeException: UNAVAILABLE: io exception
Channel Pipeline: [SslHandler#0, ...]
Caused by: javax.net.ssl.SSLHandshakeException: PKIX path building failed
```

### Certificate Expiry

Check whether the server certificate has expired:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect sequencer.sync.global:443 -servername sequencer.sync.global 2>/dev/null \
  | openssl x509 -noout -dates
```

If the certificate has expired and you control it (e.g., for your own validator's TLS termination), renew it and restart the TLS-terminating proxy or ingress controller.

### CA Trust Chain

If you see `PKIX path building failed`, the validator's JVM does not trust the server's certificate authority. Possible fixes:

* Import the CA certificate into the JVM truststore:

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  keytool -importcert -alias myca -file ca-cert.pem \
    -keystore $JAVA_HOME/lib/security/cacerts -storepass changeit
  ```

* For Kubernetes, mount the CA bundle as a volume and set `JAVA_OPTS`:

  ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  env:
    - name: JAVA_OPTS
      value: "-Djavax.net.ssl.trustStore=/etc/ssl/truststore.jks"
  ```

### Hostname Mismatch

If the certificate's Subject Alternative Name (SAN) does not include the hostname you are connecting to, the handshake will fail. Verify with:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect sequencer.sync.global:443 2>/dev/null \
  | openssl x509 -noout -ext subjectAltName
```

## VPN Problems

DevNet requires a VPN connection. TestNet and MainNet validators connect over the public internet but may still use VPNs for internal infrastructure.

### VPN Connection Drops

If your validator periodically loses connectivity, check:

* VPN client logs for reconnection events
* Whether the VPN assigns a stable IP (some providers rotate IPs on reconnect, which can break IP-whitelisted access)

### MTU Issues

VPN tunnels reduce the effective MTU. If you see stalled connections that work for small requests but hang on larger payloads:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Test with reduced packet size
ping -M do -s 1400 sequencer.dev.sync.global
```

If pings succeed at 1400 bytes but fail at 1500, lower the MTU on the VPN interface:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
sudo ip link set dev tun0 mtu 1400
```

### Split-Tunnel Configuration

If your VPN routes all traffic through the tunnel, the validator may be unable to reach external services (OIDC provider, container registries). Configure split-tunnel routing so that only synchronizer traffic goes through the VPN, while other traffic uses the default gateway.

Consult your VPN provider's documentation for split-tunnel setup.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
