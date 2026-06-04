---
title: "ValueDecoder"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-valuedecoder"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/java/com-daml-ledger-javaapi-data-codegen/valuedecoder.md"
source_title: "ValueDecoder"
tags:
  - reference
  - java
  - com-daml-ledger-javaapi-data-codegen
  - valuedecoder
---

# ValueDecoder

> 从 Daml 值的编码形式（由 Value 表示）到 codegen 解码形式（由 Data 表示）的转换器。模板、记录或变体的每个 codegen 类都包含一个 valueDecoder 方法，用于生成其中之一。如果数据类型具有类型参数，则 valueDecoder 具有与这些类型参数的 ValueDecoder 相对应的参数。对于不是代码生成的基元类型，请参阅 PrimitiveValueDecoders。 // 给定模板 'Foo' 和编码后的有效负载 'Value fooValue' Foo foo = Foo.valueDecoder().decode(fooValue); // 给定 Daml 数据类型 'Bar a b' 和 'Baz'， // 以及编码的 'Bar' 'Value barValue' Bar<Baz, Long> bar = Bar.valueDecoder( Baz.valueDecoder(), PrimitiveValueDecoders.fromInt64) .decode(barValue); Bar<List<Baz>, Map<Long, String>> barWithAggregates = Bar.valueDecoder( PrimitiveValueDecoders.fromList(Baz.valueDecoder), PrimitiveValueDecoders.fromGenMap( PrimitiveValueDecoders.fromInt64, PrimitiveValueDecoders.fromText)) .decode(barAggregateValue);

## ValueDecoder - 稳定

上游文档：[打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ValueDecoder.html)

**签名**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
@FunctionalInterface public interface ValueDecoder<Data>
```

**会员**

|文档 |会员|介绍 |已弃用 |已删除 |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ---------- | ---------- | -------- |
| [打开](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ValueDecoder.html#decode%28com.daml.ledger.javaapi.data.Value%29) | `decode(Value)` | `3.4.8` | - | - |

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
