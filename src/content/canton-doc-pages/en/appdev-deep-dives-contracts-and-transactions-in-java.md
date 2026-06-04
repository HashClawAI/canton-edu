---
title: "Contracts and Transactions in Java"
slug: "appdev-deep-dives-contracts-and-transactions-in-java"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/contracts-and-transactions-in-java.md"
source_title: "Contracts and Transactions in Java"
tags:
  - appdev
  - deep-dives
  - contracts-and-transactions-in-java
---

# Contracts and Transactions in Java

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Contracts and Transactions in Java

> Work with Daml contracts and transactions through the Java client libraries.

# How to work with contracts and transactions in Java

When writing Canton Network applications in Java, it is convenient to work with a representation of Daml templates and data types in Java that closely resemble the original Daml code while still being as close to the native types of Java as possible. To achieve this, use the Daml Codegen for Java to generate Java types based on a Daml model. You can then use these types in your Java code when reading information from and sending data to the ledger.

## Setup the codegen

Run and configure the code generator for Java according to Daml Codegen for Java to use and generate the Java classes for your project.

See also in Generated code how the generated code looks for the Daml built-in and user-defined types.

## Use the generated classes in your project

In order to compile the resulting Java classes, you need to add the Java bindings library as dependency to your build tools.

Add the following **Maven** dependency to your project:

```XML theme={"theme":{"light":"github-light","dark":"github-dark"}}
<dependency>
    <groupId>com.daml</groupId>
    <artifactId>bindings-java</artifactId>
    <version>YOUR_SDK_VERSION</version>
</dependency>
```

<Note>
  Replace `YOUR_SDK_VERSION` with the version of your SDK.
</Note>

Find the available versions in the Maven Central [Repository]().

## Access the gRPC Ledger API using Java bindings

The `bindings-java` library comes pre-packaged with the generated gRPC stubs allowing you to access the Ledger API.

For each Ledger API service, there is a dedicated Java class with a matching name. For instance, the gRPC counterpart of `CommandSubmissionService` is `CommandSubmissionServiceGrpc`.

### Connect to the ledger

To establish a connection to the ledger and access the Ledger API services create an instance of a `ManagedChannel` using the static `NettyChannelBuilder.forAddress(..)` method. Then, call the factory method on the respective service to create a stub e.g. `CommandSubmissionServiceGrpc.newFutureStub`. Use one of the helper classes provided by the `bindings-java` to create an object representing the request service request arguments, convert them to a proto message. Finally, call the desired method offered by the service.

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Create a managed channel object pointing to the Ledger API address.
ManagedChannel channel = NettyChannelBuilder.forAddress(host, port).usePlaintext().build();

// Create a stub connecting to the desired service on the ledger.
CommandSubmissionServiceFutureStub submissionService = CommandSubmissionServiceGrpc.newFutureStub(channel);

// Create an object representing the service call arguments
CommandsSubmission commandsSubmission = CommandsSubmission.create(...);

// Convert the command submission to a proto data structure
final var request = SubmitRequest.toProto(commandsSubmission);

// Issue the service call
final var response = submissionService.submit(request)
```

### Perform authorization

Some ledgers enforce authorization and require to send an access token along with each request. For more details on authorization, read the Authorization overview.

To use the same token for all Ledger API requests, use the `withCallCredentials` method of the service stub class. As an argument, this method takes a class that derives from `CallCredentials`. Implement your own derivation that provides the token in the header.

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class LedgerCallCredentials extends CallCredentials {

    private static Metadata.Key<String> header =
            Metadata.Key.of("Authorization", Metadata.ASCII_STRING_MARSHALLER);

    private final String token;

    public LedgerCallCredentials(String token) {
        super();
        this.token = token;
    }

    @Override
    public void applyRequestMetadata(
            RequestInfo requestInfo, Executor appExecutor, MetadataApplier applier) {
        Metadata metadata = new Metadata();
        metadata.put(LedgerCallCredentials.header, token.startsWith("Bearer ") ? token : "Bearer " + token);
        applier.apply(metadata);
    }
}
```

If your application is long-lived and your tokens are bound to expire, reload the necessary token when needed and pass it explicitly for every call.

If you are communicating with a ledger that verifies authorization it is very important to secure the communication channel to prevent your tokens to be exposed to man-in-the-middle attacks. The next chapter describes how to enable TLS.

### Connect securely

The builders created by `NettyChannelBuilder.forAddress` default to a tls connection, where the keys are taken from the configured Java Keystore. You can override this behavior by providing your own cryptographic settings. To do so, invoke `sslContext` and pass an `SslContext`.

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
NettyChannelBuilder.forAddress(host, port)
            .useTransportSecurity()
            .sslContext(sslContext)
            .build();
```

<Warning>
  You can also configure a plaintext connection invoking `usePlaintext()`. Use it only when connecting to a locally running ledger for development purposes.
</Warning>

Secure connections to a ledger must be configured to use client authentication certificates, which can be provided by a ledger operator.

For information on how to set up an `SslContext` with the provided certificates for client authentication, please consult the gRPC documentation on TLS with OpenSSL as well as the HelloWorldClientTls example of the `grpc-java` project.

## Use asynchronous stubs

The classes generated for the Ledger API gRPC services come in several flavors: blocking, future-based and asynchronous. The latter is the recommended way of interacting with the gRPC layer. In the example of the `CommandService` utilized above they are called `CommandServiceBlockingStub`, `CommandServiceFutureStub` and `CommandServiceStub` respectively.

For each gRPC endpoint that you want to call from your Java application, create a gRPC StreamObserver providing implementations of the `onNext`, `onError` and `onComplete` observer methods. To decode and encode the gRPC messages, use the `fromProto` and `toProto` methods of the generated classes of the Java bindings library.

### Use OpenAPI definitions

The OpenAPI definitions provide a definition for each Ledger API service and allows you to access it via the JSON Ledger API. Use those definitions to encode/decode the gRPC messages as/from JSON payloads required by the JSON Ledger API. For more details see Get started with Canton and the JSON Ledger API.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
