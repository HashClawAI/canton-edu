---
title: "Security Issues"
slug: "global-synchronizer-troubleshooting-guide-security-issues"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/security-issues.md"
source_title: "Security Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - security-issues
---

# Security Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Issues

> Troubleshooting certificate problems, JWT validation failures, and key management errors

Security-related failures typically block your validator from starting or from authenticating to the synchronizer and its APIs. The errors are often cryptic, but they fall into a few well-defined categories.

## Certificate Problems

### Certificate Expiry

TLS certificates used by your validator (for its Ledger API, admin API, or ingress) expire on a fixed date. When they expire, connections fail immediately.

**Symptom:**

```
javax.net.ssl.SSLHandshakeException: PKIX path validation failed:
java.security.cert.CertPathValidatorException: validity check failed
```

**Check expiry dates:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check a PEM file
openssl x509 -in /path/to/cert.pem -noout -enddate

# Check a running server
openssl s_client -connect your-validator:443 2>/dev/null | openssl x509 -noout -dates
```

**Resolution:** Renew the certificate through your CA or certificate manager (Let's Encrypt, AWS ACM, etc.). After replacing the certificate file, restart the service that uses it. For Kubernetes ingress controllers, the restart is often automatic once the Secret is updated.

### Certificate Renewal in Kubernetes

If you use cert-manager, check whether the Certificate resource shows a renewal failure:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl describe certificate validator-tls -n validator
```

Look for events like `The certificate request has failed` or `Order is in state errored`. Common causes: DNS challenge failed (check DNS propagation), HTTP challenge failed (check ingress routing), or the issuer's credentials have expired.

### Incomplete CA Chain

If clients can connect to your validator from some locations but not others, the server may be presenting an incomplete certificate chain. Verify:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl s_client -connect your-validator:443 -servername your-validator 2>&1 | grep "verify return"
```

If you see `verify return:0`, the chain is broken. Concatenate the intermediate CA certificates into your server certificate file, in order from leaf to root.

## JWT Validation Failures

JWT tokens authenticate API clients (your application, wallet UI, or automation scripts) to the validator's Ledger API.

### Clock Skew

```
ACCESS_TOKEN_EXPIRED(2,0): Claims were valid until 2025-09-08T08:32:07Z,
current time is 2025-09-08T08:32:07.254413051Z
```

Even a sub-second difference between the token issuer's clock and the validator's clock can cause expiry failures if the token lifetime is short. Fixes:

* Increase the access token lifetime in your OIDC provider to at least 15 minutes.
* Ensure NTP is running and synchronized on the validator host:

  ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
  timedatectl status
  # or
  chronyc tracking
  ```

### Wrong Audience Claim

```
PERMISSION_DENIED: JWT token has wrong audience. Expected: https://ledger_api.example.com
```

The `aud` claim in the JWT must match the `LEDGER_API_AUTH_AUDIENCE` configured on the validator. Check your OIDC provider's application settings and align the audience with your validator config.

### Expired Tokens

If API calls fail intermittently with `UNAUTHENTICATED`, your token refresh logic may not be working correctly. Verify:

* The token refresh interval is shorter than the token lifetime.
* The OIDC provider's token endpoint is reachable from the application making the calls.
* The refresh token itself has not expired (refresh tokens often have a longer but still finite lifetime).

### JWKS Endpoint Unreachable

If the validator cannot reach the JWKS (JSON Web Key Set) endpoint to validate token signatures:

```
Failed to fetch JWKS from https://your-tenant.auth0.com/.well-known/jwks.json
```

Check network connectivity from the validator to the OIDC provider. In Kubernetes, DNS resolution issues or egress restrictions can block this.

## Key Management

### KMS Connectivity

If your validator uses a cloud KMS (AWS KMS, GCP Cloud KMS, Azure Key Vault) for signing keys, connectivity failures prevent transaction signing.

**Symptom:**

```
com.amazonaws.SdkClientException: Unable to execute HTTP request: Connect to kms.us-east-1.amazonaws.com:443
```

**Checks:**

* Verify the KMS endpoint is reachable from the validator pod.
* Confirm the IAM role or service account has `kms:Sign`, `kms:GetPublicKey`, and `kms:Decrypt` permissions.
* If using IRSA (IAM Roles for Service Accounts) in EKS, verify the service account annotation and OIDC provider trust.

### Permission Errors

```
AccessDeniedException: User: arn:aws:sts::123456789:assumed-role/validator-role/...
is not authorized to perform: kms:Sign on resource: arn:aws:kms:...
```

The IAM policy attached to the validator's role must include the specific KMS key ARN. A wildcard (`*`) in the resource field works for testing but should be scoped to the exact key in production.

### Key Rotation

Canton generates cryptographic keys during node initialization. If you need to rotate keys (e.g., after a suspected compromise), use the Canton Console:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.secret.list()
    res1: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12201ff69b1d...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          name = Some(KeyName(participant1-namespace))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12200cd80d7c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(signing, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-signing))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 1220176a4b95...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-sequencer-auth))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = EncryptionPublicKeyWithName(
          publicKey = EncryptionPublicKey(
            id = 122029634afd...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-P256
          ),
          name = Some(KeyName(participant1-encryption))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newKey = participant1.keys.secret.generate_signing_key(name = "new-signing-key", usage = SigningKeyUsage.All)
    newKey : SigningPublicKey = SigningPublicKey(
      id = 122034956d8a...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(namespace, sequencer-auth, signing, proof-of-ownership)
    )
```

Key rotation requires careful coordination. Always test in a non-production environment first.

# Troubleshoot TLS

TLS can be configured using the parameters described here.

If you are having trouble setting up SSL/TLS, you can enable SSL debugging, increase netty logging, or generate test keys and certificates to validate your configuration.

## Enable debug logging for ssl

You can enable SSL debugging by adding the following flag to the command line when starting Canton:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
bin/canton -Djavax.net.debug=all
```

This will print verbose SSL-related information to the console, including details of the handshake process. It is recommended to use this flag only when troubleshooting, as the output can be very verbose and may impact performance of your application.

## Enable debug logging for netty

The error messages on TLS issues provided by the networking library `netty` are less than optimal. If you are struggling with setting up TLS, please enable `DEBUG` logging on the `io.netty` logger. This can typically be done by adding the following line to your logback logging configuration:

```xml theme={"theme":{"light":"github-light","dark":"github-dark"}}
<logger name="io.grpc.netty.shaded.io.netty.handler.ssl" level="DEBUG"/>
```

## Generate test keys and certificates

If you need to generate test TLS certificates to test your configuration, you can use the following OpenSSL script:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# include certs-common.sh from config/tls
. "$(dirname "${BASH_SOURCE[0]}")/certs-common.sh"

# create root certificate such that we can issue self-signed certs
create_key "root-ca"
create_certificate "root-ca" "/O=TESTING/OU=ROOT CA/emailAddress=canton@digitalasset.com"
print_certificate "root-ca"

# create public api certificate
create_key "public-api"
create_csr "public-api" "/O=TESTING/OU=DOMAIN/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "public-api" "root-ca"
print_certificate "public-api"

# create participant ledger-api certificate
create_key "ledger-api"
create_csr "ledger-api" "/O=TESTING/OU=PARTICIPANT/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "ledger-api" "root-ca"

# create participant admin-api certificate
create_key "admin-api"
create_csr "admin-api" "/O=TESTING/OU=PARTICIPANT ADMIN/CN=localhost/emailAddress=canton@digitalasset.com" "DNS:localhost,IP:127.0.0.1"
sign_csr "admin-api" "root-ca"

# create participant client key and certificate
create_key "admin-client"
create_csr "admin-client" "/O=TESTING/OU=PARTICIPANT ADMIN CLIENT/CN=localhost/emailAddress=canton@digitalasset.com"
sign_csr "admin-client" "root-ca"
print_certificate "admin-client"
```

If you'd prefer to manually generate your own set of keys and certificates, the commands used in this process are documented here:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
DAYS=3650

function create_key {
  local name=$1
  openssl genrsa -out "${name}.key" 4096
  # netty requires the keys in pkcs8 format, therefore convert them appropriately
  openssl pkcs8 -topk8 -nocrypt -in "${name}.key" -out "${name}.pem"
}

# create self signed certificate
function create_certificate {
  local name=$1
  local subj=$2
  openssl req -new -x509 -sha256 -key "${name}.key" \
              -out "${name}.crt" -days ${DAYS} -subj "$subj"
}

# create certificate signing request with subject and SAN
# we need the SANs as our certificates also need to include localhost or the
# loopback IP for the console access to the admin-api and the ledger-api
function create_csr {
  local name=$1
  local subj=$2
  local san=$3
  (
    echo "authorityKeyIdentifier=keyid,issuer"
    echo "basicConstraints=CA:FALSE"
    echo "keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment"
  ) > ${name}.ext
  if [[ -n $san ]]; then
    echo "subjectAltName=${san}" >> ${name}.ext
  fi
  # create certificate (but ensure that localhost is there as SAN as otherwise, admin local connections won't work)
  openssl req -new -sha256 -key "${name}.key" -out "${name}.csr" -subj "$subj"
}

function sign_csr {
  local name=$1
  local sign=$2
  openssl x509 -req -sha256 -in "${name}.csr" -extfile "${name}.ext" -CA "${sign}.crt" -CAkey "${sign}.key" -CAcreateserial  \
               -out "${name}.crt" -days ${DAYS}
  rm "${name}.ext" "${name}.csr"
}

function print_certificate {
  local name=$1
  openssl x509 -in "${name}.crt" -text -noout
}
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
