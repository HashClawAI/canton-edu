---
title: "ContractFilter"
slug: "reference-java-com-daml-ledger-javaapi-data-contractfilter"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data/contractfilter.md"
source_title: "ContractFilter"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data
  - contractfilter
---

# ContractFilter

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# ContractFilter

> This class contains utilities to decode a CreatedEvent and create an UpdateFormat, a TransactionFormat or a EventFormat by provided parties. It can only be instantiated with a subtype of ContractCompanion

## ContractFilter - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class ContractFilter<Ct> extends Object
```

**Members**

| Docs                                                                                                                                                                                  | Member                                     | Introduced | Deprecated | Removed |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#eventFormat%28java.util.Optional%29)                                     | `eventFormat(Optional<Set<String>>)`       | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#of%28com.daml.ledger.javaapi.data.codegen.ContractCompanion%29)          | `of(ContractCompanion<Ct, ?, ?>)`          | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#of%28com.daml.ledger.javaapi.data.codegen.InterfaceCompanion%29)         | `of(InterfaceCompanion<?, Cid, View>)`     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#toContract%28com.daml.ledger.javaapi.data.CreatedEvent%29)               | `toContract(CreatedEvent)`                 | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#transactionFormat%28java.util.Optional%29)                               | `transactionFormat(Optional<Set<String>>)` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#updateFormat%28java.util.Optional%29)                                    | `updateFormat(Optional<Set<String>>)`      | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withIncludeCreatedEventBlob%28boolean%29)                                | `withIncludeCreatedEventBlob(boolean)`     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withTransactionShape%28com.daml.ledger.javaapi.data.TransactionShape%29) | `withTransactionShape(TransactionShape)`   | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withVerbose%28boolean%29)                                                | `withVerbose(boolean)`                     | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
