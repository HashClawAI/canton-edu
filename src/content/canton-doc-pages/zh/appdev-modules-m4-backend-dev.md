---
title: "后端开发"
slug: "appdev-modules-m4-backend-dev"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-backend-dev.md"
source_title: "Backend Development"
tags:
  - appdev
  - modules
  - m4-backend-dev
---

# 后端开发

> 构建连接 Canton Ledger API 与 PQS 的后端服务，代码示例来自 cn-quickstart

后端是前端与 Canton 账本之间的层。它提交命令、读取交易并查询合约状态。

本节以 [cn-quickstart](https://github.com/digital-asset/cn-quickstart) 为运行示例。cn-quickstart 是在 Canton Network 上实现软件许可工作流的全栈参考应用，包含 Spring Boot 后端、React 前端、Daml 智能合约及在本地或 DevNet 运行所需的全部配置。此处模式——连接 Ledger API、提交命令、查询 PQS、处理错误——适用于任何 Canton 后端，代码样例直接来自 [cn-quickstart 后端](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend)，便于在可运行上下文中查看。

## 后端语言

cn-quickstart 使用基于 Spring Boot 的 Java 后端。Java 有一流的代码生成支持（`dpm codegen-java`）。

TypeScript 也通过 `dpm codegen-js` 支持。TypeScript 后端使用相同的 Ledger API（经 gRPC-js 或 JSON API），若团队希望前后端统一语言，这是合适选择。

## 连接 Ledger API

Ledger API 由 validator 的 participant 节点暴露的服务。后端作为已认证客户端连接，代表一个或多个 party 操作。

在 cn-quickstart 中，[`LedgerApi.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/ledger/LedgerApi.java) 管理该连接。构造函数构建带认证拦截器的 gRPC channel，为每次调用附加 bearer token：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
ManagedChannelBuilder<?> builder = ManagedChannelBuilder
        .forAddress(ledgerConfig.getHost(), ledgerConfig.getPort())
        .usePlaintext();
builder.intercept(new Interceptor(tokenProvider));
ManagedChannel channel = builder.build();

submission = CommandSubmissionServiceGrpc.newFutureStub(channel);
commands = CommandServiceGrpc.newFutureStub(channel);
```

`Interceptor` 类在每次调用的 gRPC metadata 上附加 bearer token：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@Override
public <ReqT, RespT> ClientCall<ReqT, RespT> interceptCall(
        MethodDescriptor<ReqT, RespT> method, CallOptions callOptions, Channel next) {
    ClientCall<ReqT, RespT> clientCall = next.newCall(method, callOptions);
    return new ForwardingClientCall.SimpleForwardingClientCall<>(clientCall) {
        @Override
        public void start(Listener<RespT> responseListener, Metadata headers) {
            headers.put(AUTHORIZATION_HEADER, "Bearer " + tokenProvider.getToken());
            super.start(responseListener, headers);
        }
    };
}
```

在 LocalNet 上，token 来自 Keycloak。生产环境中来自你的 OAuth2 提供方。

## 命令提交

命令是写入账本的方式。主要有两种操作：创建合约与行使 choice。

### 创建合约

创建合约时，用模板标识符与载荷构建 `Create` 命令并提交。cn-quickstart 中 `LedgerApi.create()` 方法处理该流程：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public <T extends Template> CompletableFuture<Void> create(T entity, String commandId) {
    CommandsOuterClass.Command.Builder command = CommandsOuterClass.Command.newBuilder();
    ValueOuterClass.Value payload = dto2Proto.template(entity.templateId()).convert(entity);
    command.getCreateBuilder()
        .setTemplateId(toIdentifier(entity.templateId()))
        .setCreateArguments(payload.getRecord());
    return submitCommands(List.of(command.build()), commandId)
        .thenApply(submitResponse -> null);
}
```

`dto2Proto` 转换器将生成的 Java 类转为 Protobuf 值。`commandId` 是 Ledger API 用于去重的 UUID。

### 行使 choice

行使 choice 需要 contract ID 与 choice 参数。`exerciseAndGetResult()` 构建 `Exercise` 命令并通过 `CommandService` 提交，等待交易结果：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
CommandsOuterClass.Command.Builder cmdBuilder = CommandsOuterClass.Command.newBuilder();
ValueOuterClass.Value payload =
    dto2Proto.choiceArgument(choice.templateId(), choice.choiceName()).convert(choice);

cmdBuilder.getExerciseBuilder()
    .setTemplateId(toIdentifier(choice.templateId()))
    .setContractId(contractId.getContractId)
    .setChoice(choice.choiceName())
    .setChoiceArgument(payload);
```

行使 choice 的 REST 端点将这些部分串联。以下是 [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java) 如何使许可证过期：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@Override
public CompletableFuture<ResponseEntity<String>> expireLicense(
        String contractId, String commandId, LicenseExpireRequest request) {
    return auth.asAuthenticatedParty(party -> {
        return damlRepository.findLicenseById(contractId).thenCompose(optContract -> {
            var license = ensurePresent(optContract,
                "License not found for contract %s", contractId);
            License_Expire choice = new License_Expire(
                new Party(auth.getAppProviderPartyId()),
                toTokenStandardMetadata(request.getMeta().getData()));
            return ledger.exerciseAndGetResult(license.contractId, choice, commandId)
                .thenApply(result -> ResponseEntity.ok("License expired successfully"));
        });
    });
}
```

模式是：查找合约（来自 PQS）、构建 choice 对象（来自生成代码）、经 Ledger API 提交。

### 处理 Contract ID

每个活跃合约有唯一 contract ID。行使 choice 需要目标合约的 ID。后端通过查询 PQS 或从交易流读取获得 contract ID。cn-quickstart REST API 在 URL 路径中传递 contract ID（例如 `POST /api/licenses/{contractId}/expire`）。

Contract ID 是不透明字符串。不要手动解析或构造。

## 查询 PQS

读操作方面，cn-quickstart 后端查询 PQS 而非 Ledger API。PQS 维护 PostgreSQL 数据库，镜像 validator 托管 party 可见的账本状态。

### Pqs 适配器

[`Pqs.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs/Pqs.java) 包装 Spring 的 `JdbcTemplate`，用 PQS 的 `active()` 表值函数查询活跃合约：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public <T extends Template> CompletableFuture<List<Contract<T>>> active(Class<T> clazz) {
    Identifier identifier = Utils.getTemplateIdByClass(clazz);
    String sql = "select contract_id, payload from active(?)";
    return runAndTraceAsync(ctx, () ->
        jdbcTemplate.query(sql, new PqsContractRowMapper<>(identifier),
            identifier.qualifiedName())
    );
}
```

`active()` 接受限定模板名（如 `quickstart_licensing:Licensing.License:License`），返回该类型的全部活跃合约。每行含 `contract_id` 与 JSON `payload`。

过滤查询时，`activeWhere()` 追加 `WHERE` 子句：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public <T extends Template> CompletableFuture<List<Contract<T>>> activeWhere(
        Class<T> clazz, String whereClause, Object... params) {
    Identifier identifier = Utils.getTemplateIdByClass(clazz);
    String sql = "select contract_id, payload from active(?) where " + whereClause;
    return runAndTraceAsync(ctx, () ->
        jdbcTemplate.query(sql, new PqsContractRowMapper<>(identifier),
            combineParams(identifier.qualifiedName(), params))
    );
}
```

### 领域查询

[`DamlRepository.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository/DamlRepository.java) 构建更高级查询。例如 `findActiveLicenses()` 在单条 SQL 中将许可证与其续期请求、分配合约 join：

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT license.contract_id    AS license_contract_id,
       license.payload        AS license_payload,
       renewal.contract_id    AS renewal_contract_id,
       renewal.payload        AS renewal_payload,
       allocation.contract_id AS allocation_contract_id
FROM active(?) license
LEFT JOIN active(?) renewal ON
    license.payload->>'licenseNum' = renewal.payload->>'licenseNum'
    AND license.payload->>'user' = renewal.payload->>'user'
LEFT JOIN active(?) allocation ON
    renewal.payload->>'requestId' =
        allocation.payload->'allocation'->'settlement'->'settlementRef'->>'id'
WHERE license.payload->>'user' = ? OR license.payload->>'provider' = ?
ORDER BY license.contract_id
```

PQS 将合约载荷存为 JSONB，因此用 PostgreSQL 的 `->` 与 `->>` 在合约字段上过滤与 join。可对常查 JSON 路径建额外 PostgreSQL 索引以提升性能。

## 读取交易

Ledger API 也暴露后端可订阅的交易流。每笔交易包含对你 party 可见的创建与归档合约。需要实时事件处理而非轮询 PQS 时很有用。

交易流订阅使用 gRPC 服务端流。以下是 [docs-website quickstart](https://github.com/DACH-NY/docs-website) 中的模式：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
UpdateServiceGrpc.UpdateServiceStub updateServiceStub = UpdateServiceGrpc.newStub(channel);
updateServiceStub.getUpdates(getUpdatesRequest.toProto(), new StreamObserver<>() {
    public void onNext(UpdateServiceOuterClass.GetUpdatesResponse r) {
        GetUpdatesResponse response = GetUpdatesResponse.fromProto(r);
        response.getTransaction().ifPresent(transaction -> {
            for (Event event : transaction.getEvents()) {
                if (event instanceof CreatedEvent createdEvent) {
                    Iou.Contract contract = Iou.Contract.fromCreatedEvent(createdEvent);
                    // update local cache or trigger side effects
                } else if (event instanceof ArchivedEvent archivedEvent) {
                    // remove from local cache
                }
            }
        });
    }
    public void onError(Throwable throwable) { /* handle error */ }
    public void onCompleted() { /* stream ended */ }
});
```

cn-quickstart 中 PQS 处理读侧投影，后端不维护自有事件溯源状态。若不使用 PQS，流式交易并维护自有投影是替代方案。

## 错误处理

Canton 使用结构化错误码。命令失败时 Ledger API 返回带 Canton 专用错误码的 gRPC `StatusRuntimeException`。常见类别：

* **NOT_FOUND** — contract ID 不存在或对提交 party 不可见
* **ALREADY_EXISTS** — 重复提交命令（命令按 command ID 去重）
* **INVALID_ARGUMENT** — 命令载荷与模板或 choice 签名不匹配
* **FAILED_PRECONDITION** — 读取与行使之间合约已归档（争用）

在 Java 中捕获 `StatusRuntimeException` 并检查状态码：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
import io.grpc.StatusRuntimeException;
import io.grpc.Status;

try {
    ledger.exerciseAndGetResult(contractId, choice, commandId).join();
} catch (CompletionException e) {
    if (e.getCause() instanceof StatusRuntimeException sre) {
        if (sre.getStatus().getCode() == Status.Code.NOT_FOUND) {
            // contract was archived — re-query PQS and retry
        }
    }
}
```

对争用错误，重试策略常能解决问题：从 PQS 重新读取当前 contract ID，再重新提交命令。

<Note>
  每次新提交设置唯一 command ID。Ledger API 按该 ID 去重，若后端重试实际已成功但响应在传输中丢失的命令，可防止重复提交。
</Note>

## cn-quickstart 中的后端架构

cn-quickstart 后端采用以下模块结构（位于 [`backend/src/main/java/com/digitalasset/quickstart/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart)）：

* [`service/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service) — REST 端点实现。每个端点组合 PQS 查询或 Ledger API 命令。
* [`ledger/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/ledger) — gRPC Ledger API 客户端，向 validator 提交命令。
* [`repository/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository) — 领域专用 PQS 查询方法。
* [`pqs/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs) — 底层 SQL 生成与 PostgreSQL 访问。
* [`utility/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/utility) — JSON 配置、追踪与辅助方法。
* [`security/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/security) — OAuth2 bearer token 校验与 party 认证。
* [`config/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/config) — Spring Boot 配置属性。

该结构将读（PQS）与写（Ledger API）清晰分离，同时保持 REST 层精简。

## 练习：添加许可证评论

本练习带你为 cn-quickstart 添加评论功能。用户可在许可证上发表评论并查看某许可证的全部评论。该功能触及后端每一层：Daml 模型、代码生成、OpenAPI spec、PQS 查询与 REST 端点。

完成后，你将拥有可用的 `/licenses/{contractId}/comments` API：在账本上创建 `LicenseComment` 合约并通过 PQS 读回。

### 步骤 1：定义 Daml 模板

新建文件 `quickstart/daml/licensing/daml/Licensing/LicenseComment.daml`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Licensing.LicenseComment where

template LicenseComment
  with
    provider : Party
    user : Party
    licenseNum : Int
    commenter : Party
    body : Text
    createdAt : Time
  where
    signatory commenter
    observer provider, user
```

`commenter` 为 signatory——只有写评论的人能创建。`provider` 与 `user` 均为 observer，以便双方看到许可证上的评论。`licenseNum` 将评论关联到特定许可证，无需引用 contract ID（许可证续期或归档时引用 contract ID 会失效）。

可与 [`Licensing/License.daml`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml) 中的 `License` 模板对比：后者使用双 signatory（`signatory provider, user`）。评论只需 commenter 授权，创建更简单——无需多方工作流。

### 步骤 2：构建并生成 Java 绑定

编译新 Daml 模块并重新生成 Java 绑定。若在 cn-quickstart 外工作，可直接用 `dpm`：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
dpm codegen-java <DAR-file> -o <output-dir>
```

在 cn-quickstart 中，Gradle 构建同时处理两步。运行 Daml 构建任务，将 `.daml` 编译为 DAR 并运行 transcode 代码生成插件生成 Java 类：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./gradlew :daml:build
```

完成后，在 `backend/build/generated-daml-bindings/` 的 `quickstart_licensing.licensing.licensecomment` 包下会有生成的 `LicenseComment` Java 类。生成类使用 public final 字段（`getProvider`、`getUser`、`getLicenseNum` 等）而非 getter——这是 cn-quickstart 全程使用的 transcode 代码生成风格。

### 步骤 3：添加 OpenAPI Spec

在 `quickstart/common/openapi.yaml` 添加评论 schema 与端点。

先在 `components/schemas` 定义 schema：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    LicenseComment:
      type: object
      required:
        - contractId
        - provider
        - user
        - licenseNum
        - commenter
        - body
        - createdAt
      properties:
        contractId:
          type: string
        provider:
          type: string
        user:
          type: string
        licenseNum:
          type: integer
        commenter:
          type: string
        body:
          type: string
        createdAt:
          type: string
          format: date-time

    AddCommentRequest:
      type: object
      required:
        - body
      properties:
        body:
          type: string
```

再在 `paths` 下添加两个端点：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
  /licenses/{contractId}/comments:
    get:
      tags: [Licenses]
      summary: List comments for a license
      operationId: listLicenseComments
      parameters:
        - $ref: '#/components/parameters/ContractId'
      responses:
        '200':
          description: A list of comments
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/LicenseComment'
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
    post:
      tags: [Licenses]
      summary: Add a comment to a license
      operationId: addLicenseComment
      parameters:
        - $ref: '#/components/parameters/ContractId'
        - $ref: '#/components/parameters/CommandId'
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AddCommentRequest'
      responses:
        '201':
          description: Comment created
        '401':
          $ref: '#/components/responses/Unauthorized'
        '404':
          $ref: '#/components/responses/NotFound'
        '500':
          $ref: '#/components/responses/InternalError'
```

GET 端点仅接受 contract ID（用于查找许可证的 `licenseNum`）。POST 端点还接受 `commandId` 供 Ledger API 去重，与 `renewLicense`、`expireLicense` 约定一致。

使用 `tags: [Licenses]` 以便与现有许可证操作分组。cn-quickstart OpenAPI 生成器从路径以 `/licenses/` 开头的所有端点生成 `LicensesApi` Java 接口，新方法会出现在 `LicenseApiImpl` 已实现的同一接口中。

更新 spec 后重新生成 Spring 服务端 stub：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./gradlew openApiGenerate
```

该任务读取 `common/openapi.yaml`，将生成的接口与模型类写入 `backend/build/generated-spring/`。新的 `listLicenseComments` 与 `addLicenseComment` 会出现在 `LicensesApi` 接口，`LicenseComment` 与 `AddCommentRequest` 模型类生成在 `org.openapitools.model`。

### 步骤 4：添加 PQS 查询

在 [`DamlRepository.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository/DamlRepository.java) 添加按许可证号查找评论的方法，遵循过滤许可证时使用的 `activeWhere()` 模式：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public CompletableFuture<List<Contract<LicenseComment>>> findCommentsByLicenseNum(int licenseNum) {
    return pqs.activeWhere(
        LicenseComment.class,
        "payload->>'licenseNum' = ?",
        String.valueOf(licenseNum)
    );
}
```

PQS 将所有合约载荷存为 JSON，因此 `payload->>'licenseNum'` 以文本提取字段。[`Pqs.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs/Pqs.java) 中的 `activeWhere()` 将该 `WHERE` 子句追加到 `active()` 表值函数，仅返回 `licenseNum` 匹配的 `LicenseComment` 合约。

### 步骤 5：添加 REST 端点

在 [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java) 添加两个方法。Gradle 根据更新后的 OpenAPI spec 重新生成 `LicensesApi` 后，须实现两个新接口方法 `LicenseApiImpl` 才能编译。两者遵循既有模式：认证、查数据、执行、返回响应。

**列出评论** — 认证调用方，查找许可证获取 `licenseNum`，经 PQS 查询匹配评论：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@Override
@WithSpan
public CompletableFuture<ResponseEntity<List<LicenseComment>>> listLicenseComments(
        String contractId) {
    var ctx = tracingCtx(logger, "listLicenseComments", "contractId", contractId);
    return auth.asAuthenticatedParty(party -> traceServiceCallAsync(ctx, () ->
            damlRepository.findLicenseById(contractId).thenCompose(optLicense -> {
                var license = ensurePresent(optLicense,
                    "License not found for contract %s", contractId);
                return damlRepository.findCommentsByLicenseNum(
                        license.payload.getLicenseNum.intValue())
                    .thenApply(comments -> {
                        var result = comments.stream()
                            .map(LicenseApiImpl::toLicenseCommentApi)
                            .toList();
                        return ResponseEntity.ok(result);
                    });
            })
    ));
}
```

**添加评论** — 认证调用方，查找许可证，在账本上创建 `LicenseComment` 合约：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@Override
@WithSpan
public CompletableFuture<ResponseEntity<Void>> addLicenseComment(
        String contractId, String commandId, AddCommentRequest request) {
    var ctx = tracingCtx(logger, "addLicenseComment",
            "contractId", contractId, "commandId", commandId);
    return auth.asAuthenticatedParty(party -> traceServiceCallAsync(ctx, () ->
            damlRepository.findLicenseById(contractId).thenCompose(optLicense -> {
                var license = ensurePresent(optLicense,
                    "License not found for contract %s", contractId);
                var now = Instant.now();
                var comment = new quickstart_licensing.licensing
                        .licensecomment.LicenseComment(
                    license.payload.getProvider,
                    license.payload.getUser,
                    license.payload.getLicenseNum,
                    new Party(party),
                    request.getBody(),
                    now
                );
                return ledger.create(comment, commandId)
                    .thenApply(v -> ResponseEntity.status(HttpStatus.CREATED)
                        .<Void>build());
            })
    ));
}
```

注意完全限定类型名 `quickstart_licensing.licensing.licensecomment.LicenseComment`——这是 Daml 生成类，与 REST 响应用的 OpenAPI 生成 `org.openapitools.model.LicenseComment` 不同。字段访问（`license.payload.getProvider`、`license.payload.getLicenseNum`）是 transcode 生成类上的 public final 字段，不是 getter。

还需转换方法，在两种 `LicenseComment` 类型间映射——从 PQS 读的 Daml 合约到作为 JSON 返回的 API 模型：

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
private static LicenseComment toLicenseCommentApi(
        Contract<quickstart_licensing.licensing.licensecomment.LicenseComment> contract) {
    var p = contract.payload;
    var api = new LicenseComment();
    api.setContractId(contract.contractId.getContractId);
    api.setProvider(p.getProvider.getParty);
    api.setUser(p.getUser.getParty);
    api.setLicenseNum(p.getLicenseNum.intValue());
    api.setCommenter(p.getCommenter.getParty);
    api.setBody(p.getBody);
    api.setCreatedAt(toOffsetDateTime(p.getCreatedAt));
    return api;
}
```

这与文件中已有的 `toLicenseApi()` 模式一致。写路径使用 `ledger.create()`——与上文 [命令提交](#creating-a-contract) 中创建合约一节相同。读路径经 `DamlRepository` 查询 PQS，读写分离。

### 步骤 6：测试

因修改了 Daml 模型，需要干净环境——新 DAR 无法覆盖已有 DAR。停止并重置 LocalNet，再重建并全新启动：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make clean-docker
make build
make start
```

等待所有服务就绪。onboarding 容器会自动注册 app-user 租户。

**获取认证 token。** 后端经 Keycloak 使用 OAuth2。用后端服务账号的 client credentials grant 获取 token：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
TOKEN=$(curl -s -X POST \
  "http://localhost:8082/realms/AppProvider/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=app-provider-backend" \
  -d "client_secret=05dmL9DAUmDnIlfoZ5EQ7pKskWmhBlNz" \
  -d "grant_type=client_credentials" \
  -d "scope=openid" | jq -r .access_token)
```

凭据来自 `docker/backend-service/onboarding/env/oauth2.env`，仅适用于本地开发环境。

**创建用于测试的许可证。** quickstart 不会自动创建许可证——由应用提供方通过 `AppInstall` 工作流创建。先从 app-user participant 创建 `AppInstallRequest`：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make create-app-install-request
```

然后经后端 API 接受请求并创建许可证：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Get the AppInstallRequest contract ID
REQUEST_CID=$(curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/app-install-requests | jq -r '.[0].contractId')

# Accept the install request
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"installMeta":{"data":{}},"meta":{"data":{}}}' \
  "http://localhost:8080/app-install-requests/${REQUEST_CID}:accept?commandId=accept-$(date +%s)"

# Wait a moment for PQS to index, then get the AppInstall contract ID
sleep 3
INSTALL_CID=$(curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/app-installs | jq -r '.[0].contractId')

# Create a license from the AppInstall
curl -s -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"params":{"meta":{"data":{}}}}' \
  "http://localhost:8080/app-installs/${INSTALL_CID}:create-license?commandId=license-$(date +%s)"
```

**测试评论端点。** 列出活跃许可证并选取 contract ID：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
LICENSE_CID=$(curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/licenses | jq -r '.[0].contractId')
```

测试评论端点：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Add a comment
curl -X POST "http://localhost:8080/licenses/${LICENSE_CID}/comments?commandId=$(uuidgen)" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -d '{"body": "Renewed for another quarter"}'

# Wait for PQS to index, then list comments
sleep 3
curl -s "http://localhost:8080/licenses/${LICENSE_CID}/comments" \
  -H "Authorization: Bearer $TOKEN" | jq .
```

## 下一步

* [前端开发](/appdev/modules/m4-frontend-dev) — 构建消费本后端 REST API 的 React UI，含基于这些后端端点添加评论 UI 的前端练习
* [Canton Coin 与 Traffic](/appdev/modules/m4-canton-coin) — 了解 traffic 成本与支付钱包集成
* [cn-quickstart 仓库](https://github.com/digital-asset/cn-quickstart) — 完整可运行的后端实现

## 进阶主题

* [命令去重](/appdev/deep-dives/command-deduplication) — 设计应用命令流，使预期账本变更在重试、崩溃与网络消息丢失下仍恰好执行一次。
* [显式合约披露](/appdev/deep-dives/explicit-contract-disclosure) — 提交读取你非 stakeholder 的合约的命令时，在 Ledger API 上将其作为 disclosed contract 传入。


---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
