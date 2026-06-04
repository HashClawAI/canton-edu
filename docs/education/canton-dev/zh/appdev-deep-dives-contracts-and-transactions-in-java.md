---
title: "Java 中的合约与交易"
slug: "appdev-deep-dives-contracts-and-transactions-in-java"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/contracts-and-transactions-in-java.md"
source_title: "Contracts and Transactions in Java"
tags:
  - appdev
  - deep-dives
  - contracts-and-transactions-in-java
---

# Java 中的合约与交易

> 通过 Java 客户端库处理 Daml 合约与交易。

用 Java 编写 Canton Network 应用时，宜使用与原始 Daml 代码相近、又贴近 Java 原生类型的模板与数据类型表示。使用 Daml Codegen for Java 根据 Daml 模型生成 Java 类型，再在读写账本时使用这些类型。

## 配置 Codegen

按 Daml Codegen for Java 文档运行并配置 Java 代码生成器，为项目生成 Java 类。

生成代码外观（内置与用户定义类型）另见 Generated code。

## 在项目中使用生成类

编译生成的 Java 类需在构建工具中加入 Java bindings 库依赖。

在 **Maven** 项目中添加：

```XML theme={"theme":{"light":"github-light","dark":"github-dark"}}
<dependency>
    <groupId>com.daml</groupId>
    <artifactId>bindings-java</artifactId>
    <version>YOUR_SDK_VERSION</version>
</dependency>
```

<Note>
  将 `YOUR_SDK_VERSION` 替换为你的 SDK 版本。
</Note>

可用版本见 Maven Central [Repository]()。

## 使用 Java bindings 访问 gRPC Ledger API

`bindings-java` 库预置生成的 gRPC stub，用于访问 Ledger API。

每个 Ledger API 服务都有对应名称的 Java 类，例如 `CommandSubmissionService` 的 gRPC 对应类为 `CommandSubmissionServiceGrpc`。

### 连接账本

使用 `NettyChannelBuilder.forAddress(..)` 静态方法创建 `ManagedChannel`，再调用各服务的工厂方法创建 stub，例如 `CommandSubmissionServiceGrpc.newFutureStub`。使用 `bindings-java` 提供的辅助类构造请求参数，转换为 proto 消息后调用服务方法。

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

### 执行授权

部分账本强制授权，要求每个请求携带访问令牌。详见 Authorization 概述。

若对所有 Ledger API 请求使用同一令牌，可在服务 stub 上使用 `withCallCredentials`，参数为继承自 `CallCredentials` 的类，在 header 中提供令牌。

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

长期运行的应用若令牌会过期，应在需要时重新加载令牌并显式传入每次调用。

与需验证授权的账本通信时，务必保护通道以防令牌遭受中间人攻击。下一节说明如何启用 TLS。

### 安全连接

`NettyChannelBuilder.forAddress` 创建的 builder 默认使用 TLS，密钥来自配置的 Java Keystore。可通过传入 `SslContext` 调用 `sslContext` 覆盖。

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
NettyChannelBuilder.forAddress(host, port)
            .useTransportSecurity()
            .sslContext(sslContext)
            .build();
```

<Warning>
  也可调用 `usePlaintext()` 配置明文连接。**仅**在连接本地开发用账本时使用。
</Warning>

连接账本的安全通道须配置客户端认证证书，通常由账本运营方提供。

如何用手头证书配置用于客户端认证的 `SslContext`，请参阅 gRPC 关于 OpenSSL TLS 的文档及 `grpc-java` 项目的 HelloWorldClientTls 示例。

## 使用异步 stub

Ledger API gRPC 服务生成多种 stub：阻塞、基于 Future 与异步。**推荐**使用异步方式。上文 `CommandService` 示例中，它们分别称为 `CommandServiceBlockingStub`、`CommandServiceFutureStub` 与 `CommandServiceStub`。

从 Java 应用调用各 gRPC 端点时，创建实现 `onNext`、`onError`、`onComplete` 的 gRPC `StreamObserver`。编解码 gRPC 消息时使用 Java bindings 生成类的 `fromProto` 与 `toProto`。

### 使用 OpenAPI 定义

OpenAPI 定义描述各 Ledger API 服务，可通过 JSON Ledger API 访问。用这些定义将 gRPC 消息编解码为 JSON Ledger API 所需的 JSON 载荷。详见 Get started with Canton and the JSON Ledger API。


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
