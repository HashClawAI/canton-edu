---
title: "Canton Security Configuration"
slug: "global-synchronizer-reference-security-configuration"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/security-configuration.md"
source_title: "Canton Security Configuration"
tags:
  - global-synchronizer
  - reference
  - security-configuration
---

# Canton Security Configuration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Security Configuration

> Configure TLS, JWT authentication, and API limits for Canton nodes

# TLS API Configuration

Both the gRPC Ledger API and the Admin API support the same TLS capabilities and can be configured using identical directives. TLS provides end-to-end channel encryption between the server and the client, and—depending on the configuration—can enforce either server-only or mutual authentication.

The example configurations presented in this section are for the Ledger API, but they are the same for the Admin API. All private keys mentioned in these how-tos must be in the PKCS#8 PEM format.

## Enable TLS for server side authentication

The following settings allow a connecting client to verify that it is communicating with the intended server.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant4.ledger-api {
  address = "127.0.0.1" // IP / DNS must be SAN of certificate to allow local connections from the canton process
  port = 5041
  tls {
    // the certificate to be used by the server
    cert-chain-file = "./tls/ledger-api.crt"
    // private key of the server
    private-key-file = "./tls/ledger-api.pem"
    // trust collection, which means that all client certificates will be verified using the trusted
    // certificates in this store. if omitted, the JVM default trust store is used.
    trust-collection-file = "./tls/root-ca.crt"
  }
}

// architecture-handbook-entry-begin: ParticipantTLSApiClient
canton.participants.participant4.ledger-api.tls.client-auth =
  {
    // none, optional and require are supported
    type = require
    // If clients are required to authenticate as well, we need to provide a client
    // certificate and the key, as Canton has internal processes that need to connect to these
    // APIs. If the server certificate is trusted by the trust-collection, then you can
    // just use the server certificates. Otherwise, you need to create separate ones.
    admin-client {
      cert-chain-file = "./tls/admin-client.crt"
      private-key-file = "./tls/admin-client.pem"
    }
  }
// architecture-handbook-entry-end: ParticipantTLSApiClient

// architecture-handbook-entry-begin: ParticipantTLSApiRestrict
// optional, if omitted, defaults to the latest TLS protocol version
canton.participants.participant4.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
// optional, if omitted, defaults to the latest supported secure ciphers
canton.participants.participant4.ledger-api.tls.ciphers =
  [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256"
  ]
// architecture-handbook-entry-end: ParticipantTLSApiRestrict

canton.participants.participant4 {
  admin-api {
    address = "localhost"
    port= 5042
    tls {
      cert-chain-file = "./enterprise/app/src/test/resources/tls/admin-api.crt"
      private-key-file = "./enterprise/app/src/test/resources/tls/admin-api.pem"
    }
  }

  storage {
    type = "h2"
    config = {
      url = "jdbc:h2:mem:db4;MODE=PostgreSQL;LOCK_TIMEOUT=10000;DB_CLOSE_DELAY=-1"
      user = "participant4"
      password = "pwd"
      driver = org.h2.Driver
    }
  }
}
```

The `trust-collection-file` allows you to provide a file-based trust store. If omitted, the system will default to the built-in `JVM` trust store. The format is a collection of PEM certificates (in the right order or hierarchy), not a Java-based trust store.

## Enable TLS for client side authentication

Client-side authentication is disabled by default. To enable it, you must configure the `client-auth.type` to `require`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant4.ledger-api.tls.client-auth =
  {
    // none, optional and require are supported
    type = require
    // If clients are required to authenticate as well, we need to provide a client
    // certificate and the key, as Canton has internal processes that need to connect to these
    // APIs. If the server certificate is trusted by the trust-collection, then you can
    // just use the server certificates. Otherwise, you need to create separate ones.
    admin-client {
      cert-chain-file = "./tls/admin-client.crt"
      private-key-file = "./tls/admin-client.pem"
    }
  }
```

This new `client-auth` setting enables client authentication, which means that the client needs to present a valid certificate (and have the corresponding private key).

The `trust-collection-file` must contain all client certificates (or parent certificates that were used to sign the client certificate) that are trusted to use the API. A certificate is valid if it has been signed by a key in the trust store.

## Restrict TLS ciphers and protocols

Assuming the server-side configuration has been completed as described in the howto above, the following settings can be used to restrict the allowed TLS ciphers and protocol versions. By default, Canton uses the JVM default values, but you can override them using the variables `ciphers` and `minimum-server-protocol-version`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// optional, if omitted, defaults to the latest TLS protocol version
canton.participants.participant4.ledger-api.tls.minimum-server-protocol-version = TLSv1.3
// optional, if omitted, defaults to the latest supported secure ciphers
canton.participants.participant4.ledger-api.tls.ciphers =
  [
    "TLS_AES_256_GCM_SHA384",
    "TLS_CHACHA20_POLY1305_SHA256"
  ]
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/apis/jwt.rst" hash="6dd0171a" */}

# Configure API Authentication and Authorization with JWT

## Configure authorization service

The Ledger API supports [JWT](https://jwt.io/) based authorization checks as described in the Authorization documentation.

In order to enable JWT authorization checks, your safe configuration options are:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      // type can be
      //   jwt-rs-256-crt
      //   jwt-es-256-crt
      //   jwt-es-512-crt
      type = jwt-rs-256-crt
      // we need a certificate file (abcd.cert)
      certificate = ${JWT_CERTIFICATE_FILE}
    }]
  }
}
```

* `jwt-rs-256-crt`. The participant will expect all tokens to be signed with RS256 (RSA Signature with SHA-256) with the public key loaded from the given X.509 certificate file. Both PEM-encoded certificates (text files starting with `-----BEGIN CERTIFICATE-----`) and DER-encoded certificates (binary files) are supported.
* `jwt-es-256-crt`. The participant will expect all tokens to be signed with ES256 (ECDSA using P-256 and SHA-256) with the public key loaded from the given X.509 certificate file. Both PEM-encoded certificates (text files starting with `-----BEGIN CERTIFICATE-----`) and DER-encoded certificates (binary files) are supported.
* `jwt-es-512-crt`. The participant will expect all tokens to be signed with ES512 (ECDSA using P-521 and SHA-512) with the public key loaded from the given X.509 certificate file. Both PEM-encoded certificates (text files starting with `-----BEGIN CERTIFICATE-----`) and DER-encoded certificates (binary files) are supported.
* `jwt-jwks`. Instead of specifying the path to a certificate, you can specify a[JWKS](https://tools.ietf.org/html/rfc7517) URL. In that case, the Participant Node expects all tokens to be signed with RS256, ES256, or ES512 with the public key loaded from the given JWKS URL.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      type = jwt-jwks
      // we need a URL to a jwks key, e.g. https://path.to/jwks.key
      url = ${JWT_URL}
    }]
  }
}
```

<Warning>
  For testing purposes only, you can also specify a shared secret. In that case, the Participant Node expects all tokens to be signed with HMAC256 with the given plaintext secret. This is not considered safe for production.
</Warning>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared {
  ledger-api {
    auth-services = [{
      type = unsafe-jwt-hmac-256
      secret = "not-safe-for-production"
    }]
  }
}
```

<Note>
  To prevent man-in-the-middle attacks, it is highly recommended to use TLS with server authentication as described in `tls-configuration` for any request sent to the Ledger API in production.
</Note>

Note that you can define multiple authorization plugins. If more than one is defined, the system will use the claim of the first auth plugin that does not return Unauthorized.

If no authorization plugins are defined, the system uses a default (wildcard) authorization method.

## Configure leeway parameters for JWT authorization

You can define leeway parameters for authorization using JWT tokens. An authorization that fails due to clock skew between the signing and the verification of the tokens can be eased by specifying a leeway window in which the token should still be considered valid. Leeway can be defined either specifically for the **Expiration Time ("exp")**, **Not Before ("nbf")** and **Issued At ("iat")** claims of the token or by a default value for all three. The values defining the leeway for each of the three specific fields override the default value if present. The leeway parameters should be given in seconds and can be defined as in the example configuration below:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.ledger-api.jwt-timestamp-leeway {
    default = 5
    expires-at = 10
    issued-at = 15
    not-before = 20
}
```

## Configure the target audience for JWT authorization

The default audience (`aud` field in the audience-based token) for authenticating on the Ledger API using JWT is `https://daml.com/participant/jwt/aud/participant/${participantId}`. Other audiences can be configured explicitly using the custom target audience configuration option:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    participants {
      participant {
        ledger-api {
          auth-services = [{
            type = jwt-jwks
            url = "https://some.url/jwks.json"
            target-scope = "custom/Scope-5:with_special_characters"
          }]
        }
      }
    }
  }

```

## Configure the target scope for JWT authorization

The default scope (`scope` field in the scope-based access token) for authenticating on the Ledger API using JWT is `daml_ledger_api`.

Other scopes can be configured explicitly using the custom target scope configuration option:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    participants {
      participant {
        ledger-api {
          port = 5001
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
          }]
        }
        admin-api {
          port = 5002
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
            users = [{
              user-id = alice
              allowed-services = [
                "admin.v0.ParticipantRepairService",
                "connection.v30.ApiInfoService",
                "v1.ServerReflection",
              ]
            }]
          }]
        }
      }
    }
  }

```

Target scope can be any case-sensitive string containing alphanumeric characters, hyphens, slashes, colons and underscores. Either the `target-scope` or the `target-audience` parameter can be configured individually, but not both at the same time.

## Configure authorization service with user list

Authorization service with user list is a form of JWT Authorization that can be configured on the Admin API exposed by the Participant, the Sequencer, and the Mediator Nodes as well as being available on the Ledger API of the Participant Node.

You can specify which users should be allowed in and which gRPC services should be accessible to them. An example configuration for both the Ledger and Admin APIs looks like this:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    participants {
      participant {
        ledger-api {
          port = 5001
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
          }]
        }
        admin-api {
          port = 5002
          auth-services = [{
            type = jwt-jwks
            url = "https://target.audience.url/jwks.json"
            target-audience = "https://rewrite.target.audience.url"
            privileged = true
            access-level = wildcard
          }]
        }
      }
    }
  }

```

Unlike the Ledger API, the Admin API doesn't require the users appearing in the sub-claims of the JWT tokens to be present in the Participant’s user database. The user in the authorization service configcan be an arbitrary choice of the Participant Node’s operator. This user also needs to be configured in the associated IDP system issuing the JWT tokens.

The configuration can contain a definition of either the target audience or the target scope depending on the specific preference of the client organization. If none is given, the JWT tokens minted by the IDP must specify `daml_ledger_api` as their scope claim.

Independent of the specific service that the operator wants to expose, it is a good practice to also give access rights to the `ServerReflection` service. Some tools such as `grpcurl` or `postman` need to hit that service to construct their requests.

## Configure privileged tokens

Privileged tokens are another form of JWT Authorization that can be configured on the Admin API exposed by the Participant, Sequencer, and Mediator Nodes, as well as being available on the Ledger API of the Participant Node. The configuration follows the same pattern as normal user tokens, but it contains an additional key called `privileged` set to true.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  participants {
    participant {
      ledger-api {
        port = 5001
        auth-services = [{
          type = jwt-jwks
          url = "https://target.audience.url/jwks.json"
          target-audience = "https://rewrite.target.audience.url"
        }]
      }
      admin-api {
        port = 5002
        auth-services = [{
          type = jwt-jwks
          url = "https://target.audience.url/jwks.json"
          target-audience = "https://rewrite.target.audience.url"
          privileged = true
          access-level = wildcard
        }]
      }
    }
  }
}
```

You can determine if the use of privileged tokens should result in granting of the `participant_admin` or the `wildcard` access levels by adding a definition of the `access-level` key and setting it to `Admin` or `Wildcard` respectively. The `Admin` is the default.

## Configure JWKS cache expiration

The JWKS cache stores recently obtained public keys, which reduces the need for expensive, repeated calls to the JWKS HTTP endpoint. Keys are kept in the cache for a default period of 5 minutes. After this time, a key is evicted, and the participant must contact the JWKS address again to retrieve the latest keys. You can modify this behavior by setting:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.ledger-api.jwks-cache-config {
  cache-expiration = 1.hour
}
```

Similar parameter can also be set on the `admin-api`.

## Configure maximum time-to-live of JWT tokens

To improve security against JWT token theft or loss, it is recommended to use tokens with a very short expiration time, ideally between 5 and 15 minutes. Further details on this topic are available in the documentation on the importance of short-lived tokens.

You can enforce a policy for short-lived tokens for a participant by configuring a `max-token-lifetime` parameter. If a presented token lacks an `exp` (expiration) field, or if its calculated time-to-live is greater than this configured maximum, the authentication layer will deny access.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.ledger-api {
  max-token-lifetime = 10.minutes
}
```

Similar parameter can also be set on the `admin-api`.

<Note>
  The rejection is based only on the remaining time-to-live of the token. Consequently, a token originally valid for 24 hours could still be used successfully if presented within the last 5 minutes of its lifetime, assuming a `max-token-lifetime` setting of 5 minutes.
</Note>

## Configure remote console for JWT authorization

When the authorization is configured, the remote console will only work against a participant when a JWT token is made available to the console in the config:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  remote-participants {
    participant {
      ledger-api {
        address = 10.60.12.1
        port = 10001
      }
      admin-api {
        address = 10.60.12.1
        port = 10002
      }
     token = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhbGljZSIsInNjb3BlIjoibXktdGFyZ2V0LXNjb3BlIn0.AkbGOfUJwAafV1xCjjRqx3rC5fPoBxgYKPfUc043pts
    }
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/apis/limits.rst" hash="c2b8d444" */}

Cover gRPC max message size for both Admin API and Ledger API. Cover rate limiting on the Ledger API. Discuss load balancer in front of APIs as best practice for additional protection. Discuss the possible performance impact if rate limits are too strict. Link to howto for resource limits on the participant. Link to "build" site for daml related size limits.

# Configure API Limits

## Max Inbound Message Size

The APIs exposed by both the participant (gRPC Ledger API and Admin API) as well as by the synchronizer (Public API and Admin API) have an upper limit on incoming message size. To increase this limit to accommodate larger payloads, the flag `max-inbound-message-size` has to be set for the respective API to the maximum message size in **bytes**.

For example, to configure a participant's gRPC Ledger API limit to 20MB:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant2.ledger-api {
  address = "127.0.0.1"
  port = 5021
  max-inbound-message-size = 20971520
}
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
