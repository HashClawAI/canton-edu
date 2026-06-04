---
title: "DamlRecord"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-damlrecord"
locale: "zh"
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

> 所有解码为 codegen Daml 记录的基类，不带类型参数。此类别包括所有模板有效负载、所有界面视图和[按照惯例，但不是按照规则]所有选择参数。它的编码对应项是 DamlRecord，可以使用 toValue() 生成。

## DamlRecord - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
public abstract class DamlRecord<T> extends Object implements DefinedDataType<T>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html#%3Cinit%3E%28%29) | `DamlRecord()` | `3.4.8` | - | - |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/DamlRecord.html#toValue%28%29) | `toValue()` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
