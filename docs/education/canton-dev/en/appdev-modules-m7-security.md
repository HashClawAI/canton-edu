---
title: "Security Best Practices"
slug: "appdev-modules-m7-security"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m7-security.md"
source_title: "Security Best Practices"
tags:
  - appdev
  - modules
  - m7-security
---

# Security Best Practices

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Security Best Practices

> Authorization patterns, API authentication, key management, and secure configuration for Canton applications

Canton provides structural security guarantees at the protocol level — authorization is declared in Daml, privacy is enforced by the synchronizer, and the ledger ensures non-repudiation. Your job as an application developer is to build on these foundations without introducing gaps in the off-ledger layers.

## On-Ledger Security

### Signatory and controller declarations

Daml's authorization model is your first line of defense. Every template declares its signatories (who must authorize creation) and each choice declares its controller (who can exercise it). The protocol enforces these declarations — no amount of API manipulation can bypass them.

Design principles:

* Declare the minimum set of signatories needed for each template
* Use the `observer` keyword to control who can see a contract without giving them the ability to act on it
* Prefer the propose-accept pattern for multi-party agreements so no party can unilaterally create obligations for others
* Validate business logic in `ensure` clauses that run at creation time and on every fetch/exercise

### Authorization chains

For complex workflows, use delegation patterns rather than granting broad permissions. A party can delegate specific actions through a separate authorization contract:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AuthorizedAgent
  with
    principal : Party
    agent : Party
    scope : Text
  where
    signatory principal
    observer agent

    choice ActOnBehalf : ()
      controller agent
      do assertMsg "Action not in scope"
           (scope == "transfer")
         pure ()
```

This keeps authorization explicit and auditable. The principal can revoke the delegation by archiving the `AuthorizedAgent` contract.

## Ledger API Authentication

Canton validators protect the Ledger API with token-based authentication (JWT). Your application must obtain valid tokens and present them on every API call.

### Token management in backends

* Store tokens securely — never in client-side code, environment variables exposed to logs, or version control
* Implement token refresh before expiry to avoid failed commands
* Use separate service accounts for different application components (backend, automation, admin tools) to limit blast radius if a token is compromised
* For gRPC clients, configure call credentials with the token. For HTTP/JSON clients, use the `Authorization: Bearer <token>` header on the participant's integrated JSON API endpoint

### TLS configuration

Production deployments must use TLS for all Ledger API connections. Configure your gRPC client with the validator's CA certificate:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
ManagedChannel channel = NettyChannelBuilder
    .forAddress(host, port)
    .sslContext(GrpcSslContexts.forClient()
        .trustManager(new File("ca-cert.pem"))
        .build())
    .build();
```

In LocalNet development, TLS is disabled by default. Do not carry this configuration into production.

## Key Management

Canton uses cryptographic keys for party identity, node identity, and transaction signing. Protect these keys according to their sensitivity.

### Development vs. production

On LocalNet, keys are generated and stored locally — this is fine for development. In production:

* Use [Hardware Security Modules (HSM) or cloud Key Management Services (KMS)](/global-synchronizer/production-operations/kms-operations) for private keys
* Never store production keys on developer machines or in CI systems
* Rotate keys according to your organization's security policy
* Back up key material securely — losing keys means losing access to your party identity

### Validator key protection

If you operate your own validator, its signing keys are the most critical secrets. Anyone with access to these keys can submit transactions as your parties. Ensure they are stored in an HSM or KMS and that access is restricted to the validator's runtime environment.

## Secure Configuration

### Secrets management

* Use a secrets manager (Vault, AWS Secrets Manager, GCP Secret Manager) for database credentials, API keys, and auth tokens
* Do not pass secrets through environment variables that might appear in process listings or container inspection
* Rotate credentials regularly and ensure your application can handle rotation without downtime

### Network isolation

* Place your validator in a private network segment
* Expose only the Ledger API port to your application servers
* Use firewall rules or security groups to restrict which systems can reach the validator's Admin API
* The Admin API provides privileged operations (party management, package upload) and should not be exposed to application code

### Input validation at system boundaries

Validate all user input before it reaches the Ledger API. While Daml's type system and authorization model prevent many categories of attacks, your backend should still:

* Validate that party identifiers in requests match the authenticated user
* Sanitize text fields before including them in contract payloads
* Enforce size limits on request payloads
* Rate-limit API endpoints to prevent abuse

## Next Steps

* [Package Management](/appdev/modules/m7-package-management) — Securing DAR distribution and deployment
* [Performance](/appdev/modules/m7-performance) — Optimization strategies for Canton applications

## Advanced Topics

* [Open Tracing in Ledger API Client Applications](/appdev/deep-dives/open-tracing) — Adding OpenTelemetry-based distributed tracing to applications using the Ledger API.
* [Authorization](/appdev/deep-dives/authorization) — Access tokens, identity providers, scopes, and rights for the Ledger API.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
