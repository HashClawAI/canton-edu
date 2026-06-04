---
title: "Authorization"
slug: "appdev-deep-dives-authorization"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/authorization.md"
source_title: "Authorization"
tags:
  - appdev
  - deep-dives
  - authorization
---

# Authorization

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Authorization

> Access tokens, identity providers, scopes, and rights for the Canton Ledger API.

When developing Daml applications using SDK tools, your local setup will most likely not perform any Ledger API request authorization --by default, any valid Ledger API request will be accepted by the sandbox.

This is not the case for participant nodes of deployed ledgers. For every Ledger API request, the participant node checks whether the request contains an access token that is valid and sufficient to authorize that request. You thus need to add support for authorization using access tokens to your application to run it against a deployed ledger.

<Note>
  In case of mutual (two-way) TLS authentication, the Ledger API client must present its certificate (in addition to an access token) to the Ledger API server as part of the authentication process. The provided certificate must be signed by a certificate authority (CA) trusted by the Ledger API server. Note that the identity of the application will not be proven by using this method, i.e. the `application_id` field in the request is not necessarily correlated with the CN (Common Name) in the certificate.
</Note>

## Basic interaction

Your Daml application sends requests to the Ledger API exposed by a participant node to submit changes to the ledger (e.g., "*exercise choice X on contract Y as party Alice*"), or to read data from the ledger (e.g., "*read all active contracts visible to party Alice*").

Whether a participant node *can* serve such a request depends on whether the participant node hosts the respective parties, and whether the request is valid according to the Daml Ledger Model. Whether a participant node *will* serve such a request to a Daml application depends on whether the request includes an access token that is valid and sufficient to authorize the request for this participant node.

## Acquire and Use Access Tokens

How an application acquires access tokens depends on the participant node it talks to and is ultimately set up by the participant node operator. Many setups use a flow in the style of [OAuth 2.0](https://oauth.net/2/).

In this scenario, the Daml application first contacts a token issuer to get an access token. The token issuer verifies the identity of the requesting application, looks up the privileges of the application, and generates a signed access token describing those privileges.

Once the access token is issued, the Daml application sends it along with every Ledger API request. The Daml ledger verifies:

* that the token was issued by one of its trusted token issuers
* that the token has not been tampered with
* that the token has not expired
* that the privileges carried by the token authorize the request

<img src="https://mintcdn.com/cantonfoundation/53J3Euu6q0XOxgPz/appdev/deep-dives/images/Authentication.svg?fit=max&auto=format&n=53J3Euu6q0XOxgPz&q=85&s=8952d9ce94318681921618e798ffd2cb" alt="A flowchart illustrating the process of authentication described in the two paragraphs immediately above." width="712" height="468" data-path="appdev/deep-dives/images/Authentication.svg" />

How you attach tokens to requests depends on the tool or library you use to interact with the Ledger API. See the tool's or library's documentation for more information. (E.g. relevant documentation to access the gRPC Ledger API using Java bindings and the JSON Ledger API.)

## Access Token Formats

Applications should treat access tokens as opaque blobs. However, as an application developer it can be helpful to understand the format of access tokens to debug problems.

All Daml ledgers represent access tokens as [JSON Web Tokens (JWTs)](https://datatracker.ietf.org/doc/html/rfc7519).

<Note>
  To generate access tokens for testing purposes, you can use the [jwt.io](https://jwt.io/) web site.
</Note>

## Access Tokens and Rights

Access tokens contain information about the rights granted to the bearer of the token. These rights are specific to the API being accessed.

The Ledger API uses the following rights to govern request authorization:

* `public`: the right to retrieve publicly available information, such as the ledger identity
* `participant_admin`: the right to administer the participant node
* `idp_admin`: the right to administer the users and parties belonging the same identity provider configuration as the authenticated user
* `canReadAs(p)`: the right to read information off the ledger (like the active contracts) visible to the party `p`
* `canActsAs(p)`: same as `canReadAs(p)`, with the added right of issuing commands on behalf of the party `p`

The following table summarizes the rights required to access each Ledger API endpoint:

| Ledger API service            | Endpoint                                                     | Required right                                       |
| ----------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- |
| StateService                  | GetActiveContracts                                           | for each requested party p: canReadAs(p)             |
| CommandCompletionService      | CompletionEnd                                                | public                                               |
|                               | CompletionStream                                             | for each requested party p: canReadAs(p)             |
| CommandSubmissionService      | Submit                                                       | for submitting party p: canActAs(p)                  |
| CommandService                | All                                                          | for submitting party p: canActAs(p)                  |
| EventQueryService             | All                                                          | for each requesting party p: canReadAs(p)            |
| Health                        | All                                                          | no access token required for health checking         |
| IdentityProviderConfigService | All                                                          | participant\_admin                                   |
| PackageService                | All                                                          | public                                               |
| PackageManagementService      | All                                                          | participant\_admin                                   |
| PartyManagementService        | All                                                          | participant\_admin                                   |
|                               | All (except GetParticipantId, UpdatePartyIdentityProviderId) | idp\_admin                                           |
| ParticipantPruningService     | All                                                          | participant\_admin                                   |
| ServerReflection              | All                                                          | no access token required for gRPC service reflection |
| TimeService                   | GetTime                                                      | public                                               |
|                               | SetTime                                                      | participant\_admin                                   |
| UpdateService                 | LedgerEnd                                                    | public                                               |
|                               | All (except LedgerEnd)                                       | for each requested party p: canReadAs(p)             |
| UserManagementService         | All                                                          | participant\_admin                                   |
|                               | All (except UpdateUserIdentityProviderId)                    | idp\_admin                                           |
|                               | GetUser                                                      | authenticated users can get their own user           |
|                               | ListUserRights                                               | authenticated users can list their own rights        |
| VersionService                | All                                                          | public                                               |

## User Access Tokens

A participant node stores a dynamic set of users as well as their rights. User access tokens encode such participant user on whose behalf the request is issued.

When handling such requests, participant nodes look up the participant user's current rights before checking request authorization per the table above. Thus the rights granted to an application can be changed dynamically using the participant User Management Service *without* issuing new access tokens.

User access tokens are [JWTs](https://datatracker.ietf.org/doc/html/rfc7519) that follow the [OAuth 2.0 standard](https://datatracker.ietf.org/doc/html/rfc6749). There are two different JSON encodings: An audience-based token format that relies on the audience field to specify that it is designated for a specific Daml participant and a scope-based token format which relies on the scope field to designate the purpose. Both formats can be used interchangeably but if possible, use of the audience-based token format, as it is compatible with a wider range of IAMs, e.g. Kubernetes does not support setting the scope field and makes the participant id mandatory which prevents misuse of a token on a different participant.

### Audience-Based Tokens

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "aud": "https://daml.com/jwt/aud/participant/someParticipantId",
   "sub": "someUserId",
   "iss": "someIdpId",
   "exp": 1300819380
}
```

To interpret the above notation:

* `aud` is a required field which restricts the token to participant nodes with the given ID (e.g. `someParticipantId`)
* `sub` is a required field which specifies the participant user's ID
* `iss` is a field which specifies the identity provider id
* `exp` is an optional field which specifies the JWT expiration date (in seconds since EPOCH)

### Scope-Based Tokens

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "aud": "someParticipantId",
   "sub": "someUserId",
   "exp": 1300819380,
   "iss": "someIdpId",
   "scope": "daml_ledger_api"
}
```

To interpret the above notation:

* `aud` is an optional field which restricts the token to participant nodes with the given ID
* `sub` is a required field which specifies the participant user's ID
* `iss` is a field which specifies the identity provider id
* `exp` is an optional field which specifies the JWT expiration date (in seconds since EPOCH)
* `scope` is a space-separated list of [OAuth 2.0 scopes](https://datatracker.ietf.org/doc/html/rfc6749#section-3.3) that must contain the `"daml_ledger_api"` scope

### Requirements for User IDs

User IDs must be non-empty strings of at most 128 characters that are either alphanumeric ASCII characters or one of the symbols "@^\$.!\`-#+'\~\_|:()".

### Identity providers

An identity provider configuration can be thought of as a set of participant users which:

* Have a defined way to verify their access tokens
* Can be administered in isolation from the rest of the users on the same participant node
* Have an identity provider id unique per participant node
* Have a related set of parties that share the same identity provider id

A participant node always has a statically configured default identity provider configuration whose id is the empty string `""`. Additionally, you can configure a small number of non-default identity providers using `IdentityProviderConfigService` by supplying a non-empty identity provider id and a [JWK Set](https://datatracker.ietf.org/doc/html/rfc7517) URL which the participant node will use to retrieve the cryptographic data needed to verify the access tokens.

When authenticating as a user from a non-default identity provider configuration, your access tokens must contain the `iss` field whose value matches the identity provider id. In case of the default identity provider configuration, the `iss` field can be empty or omitted from the access tokens.

## Encoding and Signature

Access tokens conforming to the JWT specification are embedded in a larger JSON structure with a separate header and payload.

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
   "alg": "RS256",
   "typ": "JWT"
}
{
   "aud": "https://daml.com/jwt/aud/participant/someParticipantId",
   "sub": "someUserId",
   "iss": "someIdpId",
   "exp": 1300819380
}
```

Together they are then base64 encoded, forming the final token's stem. Subsequently, the stem is signed using the cryptographic algorithm identified in the header. The signature itself is also base64-encoded and appended to the stem. The resulting character string takes a shape similar to

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2RhbWwuY29tL2p3dC9hdWQvcGFydGljaXBhbnQvc29tZVBhcnRpY2lwYW50SWQiLCJzdWIiOiJzb21lVXNlcklkIiwiaXNzIjoic29tZUlkcElkIiwiZXhwIjoxMzAwODE5MzgwfQ.DLVPehRLt8WiddI6mwUU1lqIgRbysLK34mgkuzSDQTThCXlEY_S57SHKEQHw-Pai0Y0OeGP7wNsT6uq51vBVbRNfxOLwy5owQRm3LEeTbSXMjnnPVrtRrhelVQCsH2AcV4J4bbrAe6YfKGYFBXZOfeRL3Gy7KIplcfxDZekHdPD8lhwK8AkvAR4IaOX72Q5jhjB2yOY9IwpVxx-pN0vWCqmxTbQqnIpSGo185Y0f38nKZeofGT5jcJZaSv7z4Ks15gs9gm1pHorEL6TZLCbX7T064hQeTBFea-kxQlUkcfcgmUOMAmA05_4a8fdFz2uHq5km7ylp6pUITogN5MJ-_CVFEwOD0GveOgiUJBBMHDBjq_V_DfRE4nZ04tFQ0DDthWpMd0F59JFIhmjZSZT9DWppj6G7VBWpu9aIFPefyX--2U_aO0Smt_dBBV5A6pvbIgX6ITF2tjEvvOCLHtLKmNTlP8cclna70DCsDIrojNVDMFpLXYLvsP6DhQWkGaRb-nz0hLjQE_PtuQzSexrZG5d8tHFS351E2-aUVTKoJuEGHH3n1it-d9yHdt4fAynIbhWUVAervxc-oXyrA3-uafrxbIiQCpnw0kQ8K-HwJpkfz_Yqf-luI1FaRiPT9F-cYzwvceNf2_2hhmiuGiYp3rVIPwkFAuBc1vgpPiWSNLc
```

Note that access token generation in the correct format is typically delegated to the identity provider systems. Client application developers are unlikely to need to deal with it directly.

## Token expiration

JWT token-based authorization is inherently stateless, offering excellent scalability and eliminating the need for servers to manage client sessions or perform costly claim verification checks. However, this stateless nature means JWT tokens cannot be revoked.

To mitigate the risk associated with token loss or theft, we *strongly recommend* to follow the standard practice for systems utilizing JWT tokens: configure the IAM system to issue short-lived tokens, ideally lasting between 5 and 15 minutes. This limits the time window during which unauthorized actors can access the system.

Using long-lived tokens goes against best practices and risks a costly reconfiguration of your IAM token issuance mechanism should a token be compromised. A token loss may necessitate rotating the token signing key. This action invalidates all outstanding tokens through the JSON Web Key Set (JWKS) mechanism. Consult your IAM system's documentation for detailed strategies on mitigating JWT token theft.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
