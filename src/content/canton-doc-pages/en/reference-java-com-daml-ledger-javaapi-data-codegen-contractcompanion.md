---
title: "ContractCompanion"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-contractcompanion"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/contractcompanion.md"
source_title: "ContractCompanion"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - contractcompanion
---

# ContractCompanion

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# ContractCompanion

> Metadata and utilities associated with a template as a whole, rather than one single contract made from that template. Application code should not instantiate or subclass; instead, refer to the COMPANION field on generated Template subclasses. All protected members herein are considered part of the INTERNAL API. Every instance is either a ContractCompanion.WithKey or ContractCompanion.WithoutKey, depending on whether the template defined a key type. ContractCompanion.WithKey defines extra utilities for working with contract keys.

## ContractCompanion - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public abstract class ContractCompanion<Ct,Id,Data> extends ContractTypeCompanion<Ct,Id,Data,Data>
```

**Members**

| Docs                                                                                                                                                                                              | Member                                                                 | Introduced | Deprecated | Removed |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#fromJson)                                                                 | `fromJson`                                                             | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#fromJson%28java.lang.String%29)                                           | `fromJson(String)`                                                     | `3.4.8`    | -          | -       |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#valueDecoder%28com.daml.ledger.javaapi.data.codegen.ContractCompanion%29) | `valueDecoder(ContractCompanion<?, ? extends ContractId<Data>, Data>)` | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
