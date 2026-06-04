---
title: "错误码"
slug: "appdev-reference-error-codes"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/error-codes.md"
source_title: "Error Codes"
tags:
  - appdev
  - reference
  - error-codes
---

# 错误码

> Canton 错误码、类别、gRPC 状态映射与重试策略参考。

Canton 通过 gRPC 响应返回结构化错误信息。每个错误都带有机器可读的代码、确定 gRPC 状态代码的类别以及人类可读的描述。您可以使用这些组件在应用程序中构建自动错误处理。

## 机器可读的错误详细信息

每个 gRPC 错误响应都包含遵循[丰富的 gRPC 错误模型](https://cloud.google.com/apis/design/errors#error_details) 的结构化详细信息：

* `ErrorInfo`（强制）--包含`reason`中的错误代码ID和`metadata["category"]`中的类别ID
* `RequestInfo`（强制）--包含`requestId`中的完整相关ID（未截断）
* `RetryInfo`（可选）--包含当错误可重试时建议的重试间隔
* `ResourceInfo`（可选）——标识失败涉及的资源（合约、合约密钥、包、参与方、同步器等）

<Warning>
  部分错误会因安全原因被脱敏。API 响应会省略敏感细节，但完整错误信息会出现在服务端日志中。如需完整错误上下文，请联系运维人员。
</Warning>

## 按类别重试策略

### 自动重试（类别 1-3）

类别 1、2 和 3 代表瞬态条件。您的应用程序应该自动重试这些操作。对于类别 1（不可用），请快速重试 — 负载均衡器可以处理此问题。对于类别 2（已中止），请使用指数退避，因为问题是资源争用。对于类别 3 (DEADLINE\_EXCEEDED)，重试有限次数并使用命令重复数据删除以避免重复提交。

### 修复并重试（类别 6-8）

这些错误表明请求本身存在问题。类别 6（未经身份验证）表示您的 JWT 令牌丢失或无效。类别 7 (PERMISSION\_DENIED) 表示令牌缺乏所需的权限。类别 8 (INVALID\_ARGUMENT) 表示请求格式错误，无论系统状态如何。在重试之前修复应用程序或配置中的问题。

### 状态相关（类别 9-12）

这些错误取决于账本的当前状态。在另一方存档合同的多方工作流程中，可能会出现`CONTRACT_NOT_FOUND`（类别 11），或者它可能表明存在应用程序错误。您的处理策略取决于您的应用程序的逻辑。

### 不要重试（类别 4、5、14）

这些表明内部错误、安全问题或未执行的操作。升级给您的操作员或检查服务器端日志以了解详细信息。

## 应用开发者常见错误代码

### 身份验证和授权

|错误代码 |类别 |描述 |
| ---------------------------- | -------- | ---------------------------------------------------------------------------------- |
| `UNAUTHENTICATED` | 6 |没有为需要身份验证的参与者提供 JWT 令牌 |
| `PERMISSION_DENIED` | 7 | JWT 令牌缺乏足够的操作权限 |
| `ACCESS_TOKEN_EXPIRED` | 2 | JWT 令牌已过期；获取新令牌 |
| `INVALID_TOKEN` | 8 | JWT 令牌格式错误或无效 |
| `STALE_STREAM_AUTHORIZATION` | 2 |用户权限在活动流期间发生变化；重新连接 |

### 合约和交易|错误代码 |类别 |描述 |
| ------------------------ | -------- | -------------------------------------------------------------------------------------------------------------------------- |
| `CONTRACT_NOT_FOUND` | 11 | 合同不存在或对请求方不可见 |
| `TRANSACTION_NOT_FOUND` | 11 | 交易不存在或不可见 |
| `CONTRACT_KEY_NOT_FOUND` | 11 | 未找到给定密钥的有效合同 |
| `DUPLICATE_CONTRACT_KEY` | 10 | 具有此密钥的合约已存在（合约密钥语义在 Canton 3.x 中发生变化；请参阅下面的注释）|
| `INCONSISTENT_CONTRACTS` | 9 |命令中引用的合同已更改 |

### 提交和处理

|错误代码 |类别 |描述 |
| -------------------------- | -------- | ----------------------------------------------------------- |
| `ABORTED_DUE_TO_SHUTDOWN` | 1 |节点正在关闭；针对可用节点重试 |
| `SERVER_OVERLOADED` | 2 |节点已满；使用指数退避重试 |
| `SEQUENCER_REQUEST_FAILED` | 2 |对定序器的请求失败（例如，超出批量大小）|
| `PACKAGE_SELECTION_FAILED` | 9 |未找到或未审查所需的包 |

## 从 gRPC 响应中提取错误详细信息

以下 Scala 示例展示了如何从 `StatusRuntimeException` 中提取错误分量：

以下 Java 示例显示了等效的提取。 Java 在 Canton 拥有一流的代码生成支持，因此这是最常见的非 Scala 模式：

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

这些错误代码也通过具有等效错误详细信息结构的 JSON API（HTTP Ledger API）显示。对于其他语言，请使用等效的 gRPC 状态和 protobuf 实用程序从尾随元数据中解压 `com.google.rpc.Status` 详细信息。

## 进一步阅读

* [故障排除备忘单](/zh/docs/canton/appdev-troubleshooting) -- 常见问题的快速参考解决方案，包括特定的错误代码
* [gRPC 状态码](https://grpc.github.io/grpc/core/md_doc_statuscodes.html) -- 官方 gRPC 状态码定义
* [gRPC 丰富错误模型](https://cloud.google.com/apis/design/errors#error_details) -- Canton 响应中使用的错误详细信息类型

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
