---
title: "InterfaceCompanion"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-interfacecompanion"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/interfacecompanion.md"
source_title: "InterfaceCompanion"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - interfacecompanion
---

# InterfaceCompanion

> 与整个界面相关的元数据和实用程序。它的子类用于消除各种生成的 toInterface 重载的歧义。

## InterfaceCompanion - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/InterfaceCompanion.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public abstract class InterfaceCompanion<I,Id,View> extends ContractTypeCompanion<Contract<Id,View>,Id,I,View>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/InterfaceCompanion.html#fromCreatedEvent%28com.daml.ledger.javaapi.data.CreatedEvent%29) | `fromCreatedEvent(CreatedEvent)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/InterfaceCompanion.html#fromJson%28java.lang.String%29) | `fromJson(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/InterfaceCompanion.html#valueDecoder) | `valueDecoder` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
