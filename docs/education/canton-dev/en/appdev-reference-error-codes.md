---
title: "Error Codes"
slug: "appdev-reference-error-codes"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/error-codes.md"
source_title: "Error Codes"
tags:
  - appdev
  - reference
  - error-codes
---

# Error Codes

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Error Codes

> Reference for Canton error codes, categories, gRPC status mappings, and retry strategies

Canton returns structured error information through gRPC responses. Every error carries a machine-readable code, a category that determines the gRPC status code, and a human-readable description. You can use these components to build automated error handling in your application.

## Machine-readable error details

Each gRPC error response includes structured details following the [rich gRPC error model](https://cloud.google.com/apis/design/errors#error_details):

* `ErrorInfo` (mandatory) -- contains the error code ID in `reason` and the category ID in `metadata["category"]`
* `RequestInfo` (mandatory) -- contains the full correlation ID (not truncated) in `requestId`
* `RetryInfo` (optional) -- contains the recommended retry interval when the error is retryable
* `ResourceInfo` (optional) -- identifies the resource involved in the failure (contract, contract key, package, party, synchronizer, etc.)

<Warning>
  Some errors are redacted for security. The API response omits sensitive details, but the full error message appears in server-side logs. Work with your operator if you need the complete error context.
</Warning>

## Retry strategy by category

### Automatic retry (categories 1-3)

Categories 1, 2, and 3 represent transient conditions. Your application should retry these automatically. For category 1 (UNAVAILABLE), retry quickly — a load balancer can handle this. For category 2 (ABORTED), use exponential backoff since the issue is resource contention. For category 3 (DEADLINE\_EXCEEDED), retry a limited number of times and use command deduplication to avoid duplicate submissions.

### Fix and retry (categories 6-8)

These errors indicate a problem with the request itself. Category 6 (UNAUTHENTICATED) means your JWT token is missing or invalid. Category 7 (PERMISSION\_DENIED) means the token lacks the required rights. Category 8 (INVALID\_ARGUMENT) means the request is malformed regardless of system state. Fix the issue in your application or configuration before retrying.

### State-dependent (categories 9-12)

These errors depend on the current state of the ledger. A `CONTRACT_NOT_FOUND` (category 11) might be expected in a multi-party workflow where another party archived the contract, or it might indicate an application bug. Your handling strategy depends on your application's logic.

### Do not retry (categories 4, 5, 14)

These indicate internal errors, security issues, or unimplemented operations. Escalate to your operator or check server-side logs for details.

## Common error codes for app developers

### Authentication and authorization

| Error code                   | Category | Description                                                         |
| ---------------------------- | -------- | ------------------------------------------------------------------- |
| `UNAUTHENTICATED`            | 6        | No JWT token provided on a participant that requires authentication |
| `PERMISSION_DENIED`          | 7        | JWT token lacks sufficient rights for the operation                 |
| `ACCESS_TOKEN_EXPIRED`       | 2        | JWT token has expired; obtain a fresh token                         |
| `INVALID_TOKEN`              | 8        | JWT token is malformed or otherwise invalid                         |
| `STALE_STREAM_AUTHORIZATION` | 2        | User rights changed during an active stream; reconnect              |

### Contracts and transactions

| Error code               | Category | Description                                                                                                 |
| ------------------------ | -------- | ----------------------------------------------------------------------------------------------------------- |
| `CONTRACT_NOT_FOUND`     | 11       | Contract does not exist or is not visible to the requesting party                                           |
| `TRANSACTION_NOT_FOUND`  | 11       | Transaction does not exist or is not visible                                                                |
| `CONTRACT_KEY_NOT_FOUND` | 11       | No active contract found for the given key                                                                  |
| `DUPLICATE_CONTRACT_KEY` | 10       | A contract with this key already exists (contract key semantics are changing in Canton 3.x; see note below) |
| `INCONSISTENT_CONTRACTS` | 9        | Contracts referenced in the command have changed                                                            |

### Submission and processing

| Error code                 | Category | Description                                                 |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `ABORTED_DUE_TO_SHUTDOWN`  | 1        | Node is shutting down; retry against an available node      |
| `SERVER_OVERLOADED`        | 2        | Node is at capacity; retry with exponential backoff         |
| `SEQUENCER_REQUEST_FAILED` | 2        | Request to the sequencer failed (e.g., batch size exceeded) |
| `PACKAGE_SELECTION_FAILED` | 9        | Required package not found or not vetted                    |

## Extracting error details from gRPC responses

The following Scala example shows how to extract error components from a `StatusRuntimeException`:

The following Java example shows the equivalent extraction. Java has first-class codegen support in Canton, so this is the most common non-Scala pattern:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
import com.google.rpc.ErrorInfo;
import com.google.rpc.RequestInfo;
import com.google.rpc.RetryInfo;
import io.grpc.StatusRuntimeException;
import io.grpc.protobuf.StatusProto;

try {
    // your gRPC call here
} catch (StatusRuntimeException e) {
    com.google.rpc.Status status = StatusProto.fromThrowable(e);

    // gRPC status code
    int code = status.getCode();

    // Full error description
    String message = status.getMessage();

    // Extract structured details
    for (com.google.protobuf.Any detail : status.getDetailsList()) {
        if (detail.is(ErrorInfo.class)) {
            ErrorInfo info = detail.unpack(ErrorInfo.class);
            String errorId = info.getReason();
            String category = info.getMetadataMap().get("category");
        }
        if (detail.is(RequestInfo.class)) {
            String requestId = detail.unpack(RequestInfo.class).getRequestId();
        }
        if (detail.is(RetryInfo.class)) {
            RetryInfo retry = detail.unpack(RetryInfo.class);
            long retryMs = retry.getRetryDelay().getSeconds() * 1000
                + retry.getRetryDelay().getNanos() / 1_000_000;
        }
    }
}
```

These error codes are also surfaced through the JSON API (HTTP Ledger API) with equivalent error detail structures. For other languages, use the equivalent gRPC status and protobuf utilities to unpack `com.google.rpc.Status` details from the trailing metadata.

## Further reading

* [Troubleshooting cheat sheet](/docs/canton/appdev-troubleshooting) -- quick-reference solutions for common issues including specific error codes
* [gRPC status codes](https://grpc.github.io/grpc/core/md_doc_statuscodes.html) -- official gRPC status code definitions
* [gRPC rich error model](https://cloud.google.com/apis/design/errors#error_details) -- the error detail types used in Canton responses

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
