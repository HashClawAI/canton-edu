---
title: "Completion"
slug: "reference-java-com-daml-ledger-javaapi-data-completion"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/completion.md"
source_title: "Completion"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - completion
---

# Completion

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Completion

> Generated object reference page for Completion from local Javadoc snapshots.

## Completion - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class Completion extends Object
```

**Members**

| Docs                                                                                                                                                                                                                                                                                                                                                                          | Member                                                                                                                                    | Introduced | Deprecated | Removed |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#%3Cinit%3E%28java.lang.String,com.google.rpc.Status,java.lang.String,java.lang.String,java.util.List,java.lang.String,java.time.Duration,com.daml.ledger.api.v2.TraceContextOuterClass.TraceContext,java.lang.Long,com.daml.ledger.javaapi.data.SynchronizerTime%29) | `Completion(String, Status, String, String, List<String>, String, Duration, TraceContextOuterClass.TraceContext, Long, SynchronizerTime)` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#%3Cinit%3E%28java.lang.String,com.google.rpc.Status,java.lang.String,java.lang.String,java.util.List,java.lang.String,java.lang.Long,com.daml.ledger.api.v2.TraceContextOuterClass.TraceContext,java.lang.Long,com.daml.ledger.javaapi.data.SynchronizerTime%29)     | `Completion(String, Status, String, String, List<String>, String, Long, TraceContextOuterClass.TraceContext, Long, SynchronizerTime)`     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#equals%28java.lang.Object%29)                                                                                                                                                                                                                                        | `equals(Object)`                                                                                                                          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#fromProto%28com.daml.ledger.api.v2.CompletionOuterClass.Completion%29)                                                                                                                                                                                               | `fromProto(CompletionOuterClass.Completion)`                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getActAs%28%29)                                                                                                                                                                                                                                                      | `getActAs()`                                                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getCommandId%28%29)                                                                                                                                                                                                                                                  | `getCommandId()`                                                                                                                          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getDeduplicationDuration%28%29)                                                                                                                                                                                                                                      | `getDeduplicationDuration()`                                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getDeduplicationOffset%28%29)                                                                                                                                                                                                                                        | `getDeduplicationOffset()`                                                                                                                | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getOffset%28%29)                                                                                                                                                                                                                                                     | `getOffset()`                                                                                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getStatus%28%29)                                                                                                                                                                                                                                                     | `getStatus()`                                                                                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getSubmissionId%28%29)                                                                                                                                                                                                                                               | `getSubmissionId()`                                                                                                                       | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getSynchronizerTime%28%29)                                                                                                                                                                                                                                           | `getSynchronizerTime()`                                                                                                                   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getTraceContext%28%29)                                                                                                                                                                                                                                               | `getTraceContext()`                                                                                                                       | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getUpdateId%28%29)                                                                                                                                                                                                                                                   | `getUpdateId()`                                                                                                                           | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#getUserId%28%29)                                                                                                                                                                                                                                                     | `getUserId()`                                                                                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#hashCode%28%29)                                                                                                                                                                                                                                                      | `hashCode()`                                                                                                                              | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#toProto%28%29)                                                                                                                                                                                                                                                       | `toProto()`                                                                                                                               | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/Completion.html#toString%28%29)                                                                                                                                                                                                                                                      | `toString()`                                                                                                                              | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
