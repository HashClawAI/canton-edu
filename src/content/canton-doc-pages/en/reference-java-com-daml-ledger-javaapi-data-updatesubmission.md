---
title: "UpdateSubmission"
slug: "reference-java-com-daml-ledger-javaapi-data-updatesubmission"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/updatesubmission.md"
source_title: "UpdateSubmission"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - updatesubmission
---

# UpdateSubmission

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# UpdateSubmission

> This class can be used to build a valid submission for an Update. It provides create(String, String, Update) for initial creation and methods to set optional parameters e.g withActAs(List), withWorkflowId(String) etc. Usage: var submission = UpdateSubmission.create(userId, commandId, update) .withAccessToken(token) .withParty(party) .with...

## UpdateSubmission - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class UpdateSubmission<U> extends Object
```

**Members**

| Docs                                                                                                                                                                                                      | Member                                                | Introduced | Deprecated | Removed |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#create%28java.lang.String,java.lang.String,com.daml.ledger.javaapi.data.codegen.Update%29) | `create(String, String, Update<U>)`                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getAccessToken%28%29)                                                                      | `getAccessToken()`                                    | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getActAs%28%29)                                                                            | `getActAs()`                                          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getCommandId%28%29)                                                                        | `getCommandId()`                                      | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDeduplicationDuration%28%29)                                                            | `getDeduplicationDuration()`                          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDeduplicationOffset%28%29)                                                              | `getDeduplicationOffset()`                            | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getDisclosedContracts%28%29)                                                               | `getDisclosedContracts()`                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getMinLedgerTimeAbs%28%29)                                                                 | `getMinLedgerTimeAbs()`                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getMinLedgerTimeRel%28%29)                                                                 | `getMinLedgerTimeRel()`                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getPackageIdSelectionPreference%28%29)                                                     | `getPackageIdSelectionPreference()`                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getPrefetchContractKeys%28%29)                                                             | `getPrefetchContractKeys()`                           | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getReadAs%28%29)                                                                           | `getReadAs()`                                         | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getSynchronizerId%28%29)                                                                   | `getSynchronizerId()`                                 | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getUpdate%28%29)                                                                           | `getUpdate()`                                         | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getUserId%28%29)                                                                           | `getUserId()`                                         | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#getWorkflowId%28%29)                                                                       | `getWorkflowId()`                                     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#toCommandsSubmission%28%29)                                                                | `toCommandsSubmission()`                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withAccessToken%28java.util.Optional%29)                                                   | `withAccessToken(Optional<String>)`                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withActAs%28java.util.List%29)                                                             | `withActAs(List<String>)`                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withActAs%28java.lang.String%29)                                                           | `withActAs(String)`                                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDeduplicationDuration%28java.util.Optional%29)                                         | `withDeduplicationDuration(Optional<Duration>)`       | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDeduplicationOffset%28java.util.Optional%29)                                           | `withDeduplicationOffset(Optional<Long>)`             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withDisclosedContracts%28java.util.List%29)                                                | `withDisclosedContracts(List<DisclosedContract>)`     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withMinLedgerTimeAbs%28java.util.Optional%29)                                              | `withMinLedgerTimeAbs(Optional<Instant>)`             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withMinLedgerTimeRel%28java.util.Optional%29)                                              | `withMinLedgerTimeRel(Optional<Duration>)`            | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withPackageIdSelectionPreference%28java.util.List%29)                                      | `withPackageIdSelectionPreference(List<String>)`      | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withPrefetchContractKeys%28java.util.List%29)                                              | `withPrefetchContractKeys(List<PrefetchContractKey>)` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withReadAs%28java.util.List%29)                                                            | `withReadAs(List<String>)`                            | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withSynchronizerId%28java.lang.String%29)                                                  | `withSynchronizerId(String)`                          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/UpdateSubmission.html#withWorkflowId%28java.lang.String%29)                                                      | `withWorkflowId(String)`                              | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
