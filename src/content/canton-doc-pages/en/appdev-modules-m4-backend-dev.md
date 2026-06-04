---
title: "Backend Development"
slug: "appdev-modules-m4-backend-dev"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-backend-dev.md"
source_title: "Backend Development"
tags:
  - appdev
  - modules
  - m4-backend-dev
---

# Backend Development

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Backend Development

> Build a backend service that connects to the Canton Ledger API and PQS, with code examples from cn-quickstart

The backend is the layer between your frontend and the Canton ledger. It submits commands, reads transactions, and queries contract state.

This page uses [cn-quickstart](https://github.com/digital-asset/cn-quickstart) as a running example. cn-quickstart is a full-stack reference application that implements a software licensing workflow on Canton Network. It includes a Spring Boot backend, a React frontend, Daml smart contracts, and all the configuration needed to run locally or deploy to DevNet. The patterns shown here — connecting to the Ledger API, submitting commands, querying PQS, handling errors — apply to any Canton backend, but the code samples are drawn directly from the [cn-quickstart backend](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend) so you can see them in a working context.

## Backend Language

cn-quickstart uses a Java backend built on Spring Boot. Java has first-class code generation support (`dpm codegen-java`).

TypeScript is also supported through `dpm codegen-js`. A TypeScript backend uses the same Ledger API (via gRPC-js or the JSON API) and can be a good choice if your team prefers a single language across frontend and backend.

## Connecting to the Ledger API

The Ledger API is a service exposed by the validator's participant node. Your backend connects to it as an authenticated client, acting on behalf of one or more parties.

In cn-quickstart, [`LedgerApi.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/ledger/LedgerApi.java) manages this connection. The constructor builds a gRPC channel with an authentication interceptor that attaches a bearer token to every call:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
ManagedChannelBuilder<?> builder = ManagedChannelBuilder
        .forAddress(ledgerConfig.getHost(), ledgerConfig.getPort())
        .usePlaintext();
builder.intercept(new Interceptor(tokenProvider));
ManagedChannel channel = builder.build();

submission = CommandSubmissionServiceGrpc.newFutureStub(channel);
commands = CommandServiceGrpc.newFutureStub(channel);
```

The `Interceptor` class attaches the bearer token to gRPC metadata on every call:

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

On LocalNet, the token comes from Keycloak. In production, it comes from your OAuth2 provider.

## Command Submission

Commands are how you write to the ledger. There are two primary operations: creating a contract and exercising a choice.

### Creating a contract

To create a contract, build a `Create` command with the template identifier and payload, then submit it. In cn-quickstart, the `LedgerApi.create()` method handles this:

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

The `dto2Proto` converter translates generated Java classes into Protobuf values. The `commandId` is a UUID that the Ledger API uses for deduplication.

### Exercising a choice

Exercising a choice requires the contract ID and the choice arguments. The `exerciseAndGetResult()` method builds an `Exercise` command and submits it through the `CommandService`, which waits for the transaction result:

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

A REST endpoint that exercises a choice ties these pieces together. Here's how [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java) expires a license:

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

The pattern is: look up the contract (from PQS), build the choice object (from generated code), and submit it through the Ledger API.

### Handling Contract IDs

Every active contract has a unique contract ID. To exercise a choice, you need the target contract's ID. Your backend obtains contract IDs by querying PQS or reading them from the transaction stream. The cn-quickstart REST API passes contract IDs in URL paths (e.g., `POST /api/licenses/{contractId}/expire`).

Contract IDs are opaque strings. Do not parse or construct them manually.

## Querying PQS

For read operations, the cn-quickstart backend queries PQS rather than the Ledger API. PQS maintains a PostgreSQL database that mirrors the ledger state visible to the validator's hosted parties.

### The Pqs adapter

[`Pqs.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs/Pqs.java) wraps Spring's `JdbcTemplate` and uses PQS's `active()` table-valued function to query active contracts:

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

The `active()` function takes a qualified template name (e.g., `quickstart_licensing:Licensing.License:License`) and returns all active contracts of that type. Each row contains a `contract_id` and a JSON `payload`.

For filtered queries, `activeWhere()` appends a `WHERE` clause:

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

### Domain-specific queries

[`DamlRepository.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository/DamlRepository.java) builds higher-level queries. For example, `findActiveLicenses()` joins licenses with their renewal requests and allocation contracts in a single SQL query:

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

PQS stores contract payloads as JSONB, so you use PostgreSQL's `->` and `->>` operators to filter and join on contract fields. You can create additional PostgreSQL indexes on frequently queried JSON paths for performance.

## Reading Transactions

The Ledger API also exposes a transaction stream that your backend can subscribe to. Each transaction includes the created and archived contracts visible to your party. This is useful when you need real-time event processing rather than polling PQS.

A transaction stream subscription uses gRPC server streaming. Here's the pattern from the [docs-website quickstart](https://github.com/DACH-NY/docs-website):

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

In cn-quickstart, PQS handles read-side projection, so the backend does not maintain its own event-sourced state. If you are not using PQS, streaming transactions and maintaining your own projections is the alternative.

## Error Handling

Canton uses structured error codes. When a command fails, the Ledger API returns a gRPC `StatusRuntimeException` with a Canton-specific error code. Common categories:

* **NOT\_FOUND** -- The contract ID does not exist or is not visible to the submitting party
* **ALREADY\_EXISTS** -- A duplicate command was submitted (commands are deduplicated by command ID)
* **INVALID\_ARGUMENT** -- The command payload does not match the template or choice signature
* **FAILED\_PRECONDITION** -- A contract was archived between the time you read it and the time you exercised a choice on it (contention)

In Java, catch `StatusRuntimeException` and inspect the status code:

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

For contention errors, a retry strategy often resolves the issue: re-read the current contract ID from PQS, then resubmit the command.

<Note>
  Set a unique command ID on each new submission. The Ledger API deduplicates commands by this ID, which prevents double-submission if your backend retries a command that actually succeeded but whose response was lost in transit.
</Note>

## Backend Architecture in cn-quickstart

The cn-quickstart backend follows this module structure (under [`backend/src/main/java/com/digitalasset/quickstart/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart)):

* [`service/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service) -- REST endpoint implementations. Each endpoint combines a PQS query or a Ledger API command.
* [`ledger/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/ledger) -- The gRPC Ledger API client. Submits commands to the validator.
* [`repository/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository) -- Domain-specific PQS query methods.
* [`pqs/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs) -- Low-level SQL generation and PostgreSQL access.
* [`utility/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/utility) -- JSON configuration, tracing, and helper methods.
* [`security/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/security) -- OAuth2 bearer token validation and party authentication.
* [`config/`](https://github.com/digital-asset/cn-quickstart/tree/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/config) -- Spring Boot configuration properties.

This structure cleanly separates read concerns (PQS) from write concerns (Ledger API) while keeping the REST layer thin.

## Exercise: Add License Comments

This exercise walks you through adding a comment feature to cn-quickstart. Users will be able to post comments on licenses and view all comments for a given license. The feature touches every layer of the backend: Daml model, code generation, OpenAPI spec, PQS queries, and REST endpoints.

By the end, you'll have a working `/licenses/{contractId}/comments` API that creates `LicenseComment` contracts on the ledger and reads them back through PQS.

### Step 1: Define the Daml Template

Create a new file `quickstart/daml/licensing/daml/Licensing/LicenseComment.daml`:

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

The `commenter` is the signatory — only the person writing the comment can create it. Both `provider` and `user` are observers so they can see comments on their licenses. The `licenseNum` field links the comment to a specific license without requiring a contract ID reference (which would break if the license is renewed or archived).

Compare this with the `License` template in [`Licensing/License.daml`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/daml/licensing/daml/Licensing/License.daml), which uses dual signatories (`signatory provider, user`). A comment only needs the commenter's authority, making it simpler to create — no multi-party workflow required.

### Step 2: Build and Generate Java Bindings

Compile the new Daml module and regenerate the Java bindings. If you're working outside cn-quickstart, use `dpm` directly:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
dpm codegen-java &lt;DAR-file&gt; -o &lt;output-dir&gt;
```

In cn-quickstart, the Gradle build handles both steps. Run the Daml build task, which compiles the `.daml` files into a DAR and then runs the transcode codegen plugin to produce Java classes:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./gradlew :daml:build
```

After this step, you'll have a generated `LicenseComment` Java class under `backend/build/generated-daml-bindings/` in the `quickstart_licensing.licensing.licensecomment` package. The generated class uses public final fields (`getProvider`, `getUser`, `getLicenseNum`, etc.) rather than getter methods — this is the transcode codegen style used throughout cn-quickstart.

### Step 3: Add the OpenAPI Spec

Add the comment schema and endpoints to `quickstart/common/openapi.yaml`.

First, define the schemas in the `components/schemas` section:

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

Then add two endpoints under `paths`:

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

The GET endpoint takes only the contract ID (to look up the license's `licenseNum`). The POST endpoint also takes a `commandId` for Ledger API deduplication, following the same convention as `renewLicense` and `expireLicense`.

Use `tags: [Licenses]` so these endpoints are grouped with the existing license operations. The cn-quickstart OpenAPI generator produces a `LicensesApi` Java interface from all endpoints whose paths start with `/licenses/`, so your new methods will appear in the same interface that `LicenseApiImpl` already implements.

After updating the spec, regenerate the Spring server stubs:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./gradlew openApiGenerate
```

This reads `common/openapi.yaml` and writes the generated interfaces and model classes to `backend/build/generated-spring/`. Your new `listLicenseComments` and `addLicenseComment` methods will appear in the `LicensesApi` interface, and the `LicenseComment` and `AddCommentRequest` model classes will be generated in `org.openapitools.model`.

### Step 4: Add the PQS Query

Add a method to [`DamlRepository.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/repository/DamlRepository.java) that finds comments by license number. This follows the same `activeWhere()` pattern used for filtering licenses:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
public CompletableFuture<List<Contract<LicenseComment>>> findCommentsByLicenseNum(int licenseNum) {
    return pqs.activeWhere(
        LicenseComment.class,
        "payload->>'licenseNum' = ?",
        String.valueOf(licenseNum)
    );
}
```

PQS stores all contract payloads as JSON, so `payload->>'licenseNum'` extracts the field as text. The `activeWhere()` method in [`Pqs.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/pqs/Pqs.java) appends this `WHERE` clause to the `active()` table-valued function, returning only `LicenseComment` contracts whose `licenseNum` matches.

### Step 5: Add the REST Endpoints

Add two methods to [`LicenseApiImpl.java`](https://github.com/digital-asset/cn-quickstart/blob/main/quickstart/backend/src/main/java/com/digitalasset/quickstart/service/LicenseApiImpl.java). After the Gradle build regenerates `LicensesApi` from the updated OpenAPI spec, `LicenseApiImpl` won't compile until you implement the two new interface methods. Both follow the existing pattern: authenticate, look up data, execute, and return a response.

**List comments** — authenticate the caller, look up the license to get its `licenseNum`, query PQS for matching comments:

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

**Add a comment** — authenticate the caller, look up the license, create a `LicenseComment` contract on the ledger:

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

Note the fully-qualified `quickstart_licensing.licensing.licensecomment.LicenseComment` type name — this is the Daml-generated class, distinct from the OpenAPI-generated `org.openapitools.model.LicenseComment` that the REST response uses. The field accessors (`license.payload.getProvider`, `license.payload.getLicenseNum`) are public final fields on the transcode-generated classes, not getter methods.

You'll also need a converter method to map between the two `LicenseComment` types — from the Daml contract (read from PQS) to the API model (returned as JSON):

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

This follows the same pattern as `toLicenseApi()` already in the file. The write path uses `ledger.create()` — the same method shown in the [Command Submission](#creating-a-contract) section above. The read path queries PQS through `DamlRepository`, keeping reads and writes separated.

### Step 6: Test It

Since you changed the Daml model, you need a clean environment — the new DAR won't upload over an existing one. Stop and reset LocalNet, then rebuild and start fresh:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make clean-docker
make build
make start
```

Wait for all services to come up. The onboarding containers will automatically register the app-user tenant.

**Get an auth token.** The backend uses OAuth2 via Keycloak. Obtain a token using the client credentials grant with the backend service account:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
TOKEN=$(curl -s -X POST \
  "http://localhost:8082/realms/AppProvider/protocol/openid-connect/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=app-provider-backend" \
  -d "client_secret=05dmL9DAUmDnIlfoZ5EQ7pKskWmhBlNz" \
  -d "grant_type=client_credentials" \
  -d "scope=openid" | jq -r .access_token)
```

These credentials are from `docker/backend-service/onboarding/env/oauth2.env` and are only valid for the local development environment.

**Create a license to test with.** The quickstart doesn't create licenses automatically — they're created by the app provider through the `AppInstall` workflow. First, create an `AppInstallRequest` from the app-user participant:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
make create-app-install-request
```

Then accept the request and create a license using the backend API:

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

**Test the comment endpoints.** List the active licenses and pick a contract ID:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
LICENSE_CID=$(curl -s -H "Authorization: Bearer $TOKEN" \
  http://localhost:8080/licenses | jq -r '.[0].contractId')
```

Now test the comment endpoints:

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

## Next Steps

* [Frontend Development](/docs/canton/appdev-modules-m4-frontend-dev) -- Build a React UI that consumes this backend's REST API, including a frontend exercise that adds comment UI on top of these backend endpoints
* [Canton Coin and Traffic](/docs/canton/appdev-modules-m4-canton-coin) -- Understand traffic costs and wallet integration for payments
* [cn-quickstart repository](https://github.com/digital-asset/cn-quickstart) -- Full working backend implementation

## Advanced Topics

* [Command Deduplication](/docs/canton/appdev-deep-dives-command-deduplication) — Designing application command flows so an intended ledger change is executed exactly once, even under retries, crashes, and lost network messages.
* [Explicit Contract Disclosure](/docs/canton/appdev-deep-dives-explicit-contract-disclosure) — Submitting commands that read a contract you do not stakeholder by passing it as a disclosed contract on the Ledger API.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
