---
title: "DamlRecord"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-damlrecord"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/damlrecord.md"
source_title: "DamlRecord"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - damlrecord
---

# DamlRecord

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DamlRecord

> Base class of all decoded-to-codegen Daml records with no type parameters. This category includes all Template payloads, all interface views, and [by convention albeit not by rule] all choice arguments. Its encoded counterpart is DamlRecord, which can be produced with toValue().

## DamlRecord - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public abstract class DamlRecord<T> extends Object implements DefinedDataType<T>
```

**Members**

| Docs                                                                                                                               | Member         | Introduced | Deprecated | Removed |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html#%3Cinit%3E%28%29) | `DamlRecord()` | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html#toValue%28%29)    | `toValue()`    | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
