---
title: "ContractCompanion"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-contractcompanion"
locale: "zh"
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

> 元数据和实用程序与整个模板关联，而不是根据该模板制定的单个合同。应用程序代码不应实例化或子类化；相反，请参阅生成的模板子类上的 COMPANION 字段。本文中所有受保护的成员均被视为 INTERNAL API 的一部分。每个实例都是 ContractCompanion.WithKey 或 ContractCompanion.WithoutKey，具体取决于模板是否定义了密钥类型。 ContractCompanion.WithKey 定义了用于处理合约密钥的额外实用程序。

## ContractCompanion - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public abstract class ContractCompanion<Ct,Id,Data> extends ContractTypeCompanion<Ct,Id,Data,Data>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#fromJson) | `fromJson` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#fromJson%28java.lang.String%29) | `fromJson(String)` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ContractCompanion.html#valueDecoder%28com.daml.ledger.javaapi.data.codegen.ContractCompanion%29) | `valueDecoder(ContractCompanion<?, ? extends ContractId<Data>, Data>)` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
