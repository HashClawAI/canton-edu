---
title: "Canton API Configuration"
slug: "global-synchronizer-reference-api-configuration"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/api-configuration.md"
source_title: "Canton API Configuration"
tags:
  - global-synchronizer
  - reference
  - api-configuration
---

# Canton API Configuration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton API Configuration

> Configure Admin API, Ledger API, JSON Ledger API, and caching for Canton nodes.

# API Configuration

Participant nodes expose the Admin API, the gRPC Ledger API, and optionally the JSON Ledger API.

This page explains how to configure general options that apply to both the Admin API and the gRPC Ledger API. For the configuration options that apply only to specific APIs, please refer to the Administration API, the gRPC Ledger API, and the JSON Ledger API pages.

## Ports

Ports for the Admin API, gRPC Ledger API and JSON Ledger API have to be provided explicitly:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1 {
  storage.type = memory
  admin-api.port = 5012
  ledger-api.port = 5011
  http-ledger-api.port = 5013
}
```

Note that if JSON Ledger API is disabled, then its port does not have to be provided:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant3 {
  ledger-api.port = 13031
  admin-api.port = 13032
  http-ledger-api.enabled = false
  storage.type = memory
}
```

## Keep Alive

Canton enables keep-alive by default on all gRPC connections in order to prevent load-balancers or firewalls from terminating long-running RPC calls in the event of some silence on the connection.

To tweak the keep-alive configuration of a connection, adjust the following parameters:

* `time`
* `timeout`
* `permit-keep-alive-time`
* `permit-keep-alive-without-calls`

You can adjust the first two parameters for either the Synchronizer Public API client in the `keep-alive-client` section, or for the server side of the Admin API and the gRPC Ledger API in the `keep-alive-server` section. The last two parameters are server only, and you can therefore adjust them only in the `keep-alive-server` section of the Admin API and the gRPC Ledger API.

The gRPC [documentation]() further describes these parameters and their effect.

<Note>
  `permit-keep-alive-time` specifies the most aggressive keep-alive time that a client is permitted to use. If a client uses a keep-alive `time` that is more aggressive than the server's `permit-keep-alive-time`, the connection is terminated with a `GOAWAY` error with “too\_many\_pings” as the debug data.
</Note>

<Note>
  Setting `permit-keep-alive-without-calls` to `true` allows clients to send ping messages outside of any ongoing gRPC call. Such a ping otherwise results in a `GOAWAY` error.
</Note>

Canton sets different default values for these parameters depending on the API:

| API                             | Admin API | Ledger API |
| ------------------------------- | --------- | ---------- |
| time                            | 40s       | 10min      |
| timeout                         | 20s       | 20s        |
| permit-keep-alive-time          | 20s       | 10s        |
| permit-keep-alive-without-calls | false     | false      |

The following is an example that demonstrates how to configure the keep-alive for the various APIs:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer-client {
    keep-alive-client {
        time = 60s
        timeout = 30s
    }
}

admin-api {
    keep-alive-server {
        time = 40s
        timeout = 20s
        permit-keep-alive-time = 20s
    }
}

ledger-api {
    keep-alive-server {
        time = 40s
        timeout = 20s
        permit-keep-alive-time = 20s
        permit-keep-alive-without-calls = true
    }
}
```

## Native libraries usage by Netty

Canton ships with native libraries (for some processor architectures: x86\_64, ARM64, S390\_64) so that the Netty network access library can take advantage of the `epoll` system [call]() on Linux. This generally leads to improved performance and less pressure on the JVM garbage collector.

The system automatically picks the native library if available for the current operating system and architecture, or falls back to the standard NIO library if the native library is not available.

To switch off using the native library, set the following when running Canton:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
-Dio.grpc.netty.shaded.io.netty.transport.noNative=true
```

Even when this is expected, falling back to NIO might lead to a warning being emitted at `DEBUG` level on your log.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/configure/apis/admin_api.rst" hash="eb18a523" */}

# Admin API Configuration

## Administration API

The nature and scope of the Admin API on participant nodes and the Admin API on synchronizers has some overlap. As an example, you will find the same key management commands on the synchronizer and the participant node API, whereas the participant has different commands to connect to several synchronizers.

The configuration is currently simple (see the TLS example below) and specifically takes an address and a port. The address defaults to `127.0.0.1` and a default port is assigned if not explicitly configured.

You should not expose the admin-api publicly in an unsecured way as it serves administrative purposes only.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/configure/apis/ledger_api.rst" hash="1c225af4" */}

# gRPC Ledger API Configuration

The configuration of the gRPC Ledger API is similar to the Admin API configuration, except that the group starts with `ledger-api` instead of `admin-api`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  participants {
    participant {
      ledger-api {
        port = 5011
        address = localhost
        auth-services = [{
          type = jwt-jwks
          url = "https://target.audience.url/jwks.json"
          target-audience = "https://rewrite.target.audience.url"
        }]
        jwt-timestamp-leeway {
          default = 5
          expires-at = 10
          issued-at = 15
          not-before = 20
        }
        keep-alive-server {
          time = 40s
          timeout = 20s
          permit-keep-alive-time = 20s
        }
        max-inbound-message-size = 20971520
      }
    }
  }
}
```

To configure the gRPC Ledger API connectivity, you should specify **address** and **port**. All other attributes are optional and have intuitive default values.

* Define **tls** parameter group to to configure TLS
* Define **auth-services** parameter group to to configure JWT authorization
* Define **jwt-timestamp-leeway** parameter group to to configure JWT leeway
* Define **keep-alive-server** parameter group to to configure gRPC keepalive
* Define **max-inbound-message-size** parameter to control the max size of gRPC messages

## Ledger API Caches

The `max-contract-state-cache-size` and `max-contract-key-state-cache-size` parameters control the sizes of the Ledger API contract and contract key caches, respectively. Modifying these parameters changes the likelihood that a transaction using a contract or a contract key that was recently accessed (created or read) can still find it in the memory, rather than needing to query it from the database. Larger caches might be of interest when there is a big pool of ambient contracts that are consistently being fetched or used for non-consuming exercises. Larger caches can also benefit use cases where a big pool of contracts rotates through a create -> archive -> create-successor cycle. Consider adjusting these parameters explicitly if the performance of your specific workflow depends on large caches.

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant.ledger-api.index-service {
      max-transactions-in-memory-fan-out-buffer-size = 10000 // default 1000
  }

```

## Max Transactions in the In-Memory Fan-Out

The `max-transactions-in-memory-fan-out-buffer-size` parameter controls the size of the in-memory fan-out buffer. This buffer allows serving the transaction streams from memory as they are finalized, rather than from the database. Make sure this buffer is large enough so applications are less likely to have to stream transactions from the database. In most cases, a 10s buffer works well. For example, if you expect a throughput of 20 tx/s, set this number to 200. The new default setting of 1000 assumes 100 tx/s. Consider adjusting these parameters explicitly if the performance of your workflow foresees transaction rates larger than 100 tx/s.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.ledger-api.index-service {
    max-transactions-in-memory-fan-out-buffer-size = 10000 // default 1000
}
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/configure/apis/json_api.rst" hash="a4b05afb" */}

# JSON Ledger API Configuration

The configuration of the JSON Ledger API is similar to the gRPC Ledger API configuration. The corresponding parameter group starts with `http-ledger-api`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  participants {
    participant1 {
      http-ledger-api {
        enabled = true
        address = 0.0.0.0
        port = 10010
        port-file = "./json.port"
        path-prefix = "my-prefix"
        websocket-config {
            http-list-max-elements-limit = 1000,
            http-list-wait-time = 2s,
        }
        daml-definitions-service-enabled = true
      }
    }
  }
}
```

The JSON Ledger API is enabled by default. If you want to disable it, set the `enabled` field to `false`.

## JSON Ledger API Endpoint

Configure the JSON API endpoint by adding the `server` parameter group.

* Specify the `address` to indicate the IP address to listen on.
* Specify the `port` to indicate the port.
* Specify `port-file`, if you want the Participant Node to write a text file with the port on which the JSON Ledger API is listening. This is useful as a tool to synchronize the start-up of dependent services, as the Participant Node only writes the file once the JSON Ledger API is fully initialized.
* Specify `path-prefix` if you want the JSON Ledger API content to be served on a customized path instead of `/`.

## Websockets

The endpoints that result in large data sets (`/v2/commands/completions`, `/v2/state/active-contracts`, `/v2/updates`, `/v2/updates/flats`, and `/v2/updates/trees`) come in two flavors:

* a websocket capable of returning an arbitrarily long result set in a stream
* a HTTP post request returning a limited list of results

The latter type of requests can be parameterized in the Participant Node's config.

* Set the `http-list-max-elements-limit` to specify the maximum number of returned rows.
* Set the `http-list-wait-time` to specify the number of milliseconds of idle time to wait before sending result This parameter is needed in case of open-ended streams such as completions. JSON Ledger API reads from the gRPC stream, and when there are no new elements for "wait" milliseconds -> the result is sent to the client.

## Daml definitions service

You can enable the experimental `Daml Definitions Service` by setting the `daml-definitions-service-enabled` parameter to `true`.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/optimize/caching.rst" hash="89c687c5" */}

# Configure Caching

## Ledger API Caches

The `max-contract-state-cache-size` and `max-contract-key-state-cache-size` parameters control the size of the Ledger API contract and contract key caches, respectively. Modifying these parameters changes the likelihood that a transaction using a contract or a contract key that was recently accessed (created or read) can still find it in the memory, rather than needing to query it from the database. Larger caches might be of interest when there is a big pool of ambient contracts that are consistently fetched or used for non-consuming exercises. Larger caches can also benefit use cases where a big pool of contracts rotates through a create -> archive -> create-successor cycle. Consider adjusting these parameters explicitly if the performance of your specific workflow depends on large caches.

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant.ledger-api.index-service {
      max-contract-state-cache-size = 100000      // default 1e4
      max-contract-key-state-cache-size = 100000  // default 1e4
  }

```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
