---
title: "ValueDecoder"
slug: "reference-java-com-daml-ledger-javaapi-data-codegen-valuedecoder"
locale: "en"
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

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# ValueDecoder

> A converter from the encoded form of a Daml value, represented by Value, to the codegen-decoded form, represented by Data. Every codegen class for a template, record, or variant includes a valueDecoder method that produces one of these. If the data type has type parameters, valueDecoder has arguments that correspond to ValueDecoders for those type arguments. For primitive types that are not code-generated, see PrimitiveValueDecoders. // given template 'Foo', and encoded payload 'Value fooValue' Foo foo = Foo.valueDecoder().decode(fooValue); // given Daml datatypes 'Bar a b' and 'Baz', // and encoded 'Bar' 'Value barValue' Bar<Baz, Long> bar = Bar.valueDecoder( Baz.valueDecoder(), PrimitiveValueDecoders.fromInt64) .decode(barValue); Bar<List<Baz>, Map<Long, String>> barWithAggregates = Bar.valueDecoder( PrimitiveValueDecoders.fromList(Baz.valueDecoder), PrimitiveValueDecoders.fromGenMap( PrimitiveValueDecoders.fromInt64, PrimitiveValueDecoders.fromText)) .decode(barAggregateValue);

## ValueDecoder - stable

Upstream docs: [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ValueDecoder.html)

**Signature**

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
@FunctionalInterface public interface ValueDecoder<Data>
```

**Members**

| Docs                                                                                                                                                               | Member          | Introduced | Deprecated | Removed |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ---------- | ---------- | ------- |
| [Open](https://javadoc.io/doc/com.daml/bindings-java/3.4.11/com/daml/ledger/javaapi/data/codegen/ValueDecoder.html#decode%28com.daml.ledger.javaapi.data.Value%29) | `decode(Value)` | `3.4.8`    | -          | -       |

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
