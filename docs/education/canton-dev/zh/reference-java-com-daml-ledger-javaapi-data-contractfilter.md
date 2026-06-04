---
title: "ContractFilter"
slug: "reference-java-com-daml-ledger-javaapi-data-contractfilter"
locale: "zh"
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

> 此类包含用于解码 CreatedEvent 并由提供方创建 UpdateFormat、TransactionFormat 或 EventFormat 的实用程序。它只能用 ContractCompanion 的子类型实例化

## ContractFilter - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public final class ContractFilter<Ct> extends Object
```

**会员**|文档 |会员|介绍 |已弃用 |已删除 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#eventFormat%28java.util.Optional%29) | `eventFormat(Optional<Set<String>>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#of%28com.daml.ledger.javaapi.data.codegen.ContractCompanion%29) | `of(ContractCompanion<Ct, ?, ?>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#of%28com.daml.ledger.javaapi.data.codegen.InterfaceCompanion%29) | `of(InterfaceCompanion<?, Cid, View>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#toContract%28com.daml.ledger.javaapi.data.CreatedEvent%29) | `toContract(CreatedEvent)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#transactionFormat%28java.util.Optional%29) | `transactionFormat(Optional<Set<String>>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#updateFormat%28java.util.Optional%29) | `updateFormat(Optional<Set<String>>)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withIncludeCreatedEventBlob%28boolean%29) | `withIncludeCreatedEventBlob(boolean)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withTransactionShape%28com.daml.ledger.javaapi.data.TransactionShape%29) | `withTransactionShape(TransactionShape)`| `3.4.8` | - | - || [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/ContractFilter.html#withVerbose%28boolean%29) | `withVerbose(boolean)` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
