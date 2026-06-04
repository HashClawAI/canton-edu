---
title: "Daml-LF Reference"
slug: "appdev-reference-daml-lf-reference"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-lf-reference.md"
source_title: "Daml-LF Reference"
tags:
  - appdev
  - reference
  - daml-lf-reference
---

# Daml-LF Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Daml-LF Reference

> Daml-LF type conversion, JSON encoding, Protobuf mapping, packages, and DAR file structure.

# Ledger API overview

## What is the Ledger API

The **Ledger API** is an API that's exposed by any Participant Node. Users access and manipulate the ledger state through the Ledger API. There are two protocols available for the Ledger API: gRPC and JSON. The core services are implemented using [gRPC]() and [Protobuf](). There is a translation layer that additionally exposes all the Ledger API services as JSON Ledger API.

For a high level introduction to the services see `ledger-api-services`.

You may also want to read the protobuf documentation of the API, which explains how each service is defined through its protobuf messages.

## How to Access the Ledger API

You can access the gRPC Ledger API via the Java bindings.

If you don't use a language that targets the JVM, you can use gRPC to generate the code to access the Ledger API in several programming languages that support the `proto` standard.

If you don't want to use the gRPC API, you can also use the JSON Ledger API. This API is formally described using an openapi and asyncapi descriptions. You can use any language that supports OpenAPI standard to generate the clients using the OpenAPI [Generators]().

## Daml-LF

When you compile Daml source into a .dar file, the underlying format is Daml-LF. Daml-LF is similar to Daml, but is stripped down to a core set of features. The relationship between the surface Daml syntax and Daml-LF is loosely similar to that between Java and JVM bytecode.

As a user, you don't need to interact with Daml-LF directly. But internally, it's used for:

* Executing Daml code on the Ledger
* Sending and receiving values via the Ledger API
* Generating code in other languages for interacting with Daml models (often called “codegen”)

Daml assistant offers two code generators that convert the DAML-LF to the idiomatic representations of Daml in Java or Typescript.

### When You Need to Know About Daml-LF

Daml-LF is only really relevant when you're dealing with the objects you send to or receive from the ledger. If you use any of the provided code generators, you don't need to know about Daml-LF at all.

Otherwise, it can be helpful to know what the types in your Daml code look like at the Daml-LF level, so you know what to expect from the Ledger API.

For example, if you are writing an application that creates some Daml contracts, you need to construct values to pass as parameters to the contract. These values are determined by the Daml-LF types in that contract template. This means you need an idea of how the Daml-LF types correspond to the types in the original Daml model.

For the most part the translation of types from Daml to Daml-LF should not be surprising. This page goes through all the cases in detail.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/sdk/reference/json-api/lf-value-specification.rst" hash="a3820c5d" */}

# Daml-LF JSON encoding

Daml-LF values are represented as JSON values in the JSON Ledger API. This representation is used whenever the `JSON Ledger API` expects a `Daml` record or value, such as in the `createArguments` field of the `CreateCommand` component. The conversion from Daml values to JSON also occurs when a value is returned from the `JSON Ledger API`. For more information about `Daml` types, see `daml-ref-built-in-types`.

| Daml-LF type | JSON type                                                                                                                                    | Example                                                                  |       |        |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----- | ------ |
| `Int`        | `string` preferred; number accepted as input. Range: `[-9223372036854775808, 9223372036854775807]`.                                          | `1234567890`                                                             |       |        |
| `Decimal`    | `string` preferred; number accepted as input. Range: `[-(10^38 - 1) / 10^10, (10^38 - 1) / 10^10]`. Format: `-?[0-9]{1,28}(\.[0-9]{1,10})?`. | `"1234.56"`                                                              |       |        |
| `Timestamp`  | `string` ISO 8601 timestamp.                                                                                                                 | `"2023-04-06T04:30:23.1234569Z"`                                         |       |        |
| `Date`       | `string` ISO 8601 date.                                                                                                                      | `"2023-04-06"`                                                           |       |        |
| `Unit`       | Empty JSON object.                                                                                                                           | `{}`                                                                     |       |        |
| `Text`       | `string`                                                                                                                                     | `"my text value"`                                                        |       |        |
| `Bool`       | `boolean`                                                                                                                                    | `false`                                                                  |       |        |
| `ContractId` | `string`                                                                                                                                     | `"1234:56:7890"`                                                         |       |        |
| `Party`      | `string`                                                                                                                                     | `"Alice:1234567890"`                                                     |       |        |
| `Record`     | JSON object with one property per record field.                                                                                              | `{"field1Label": "value of field1", "field2Label": "value of field2"}`   |       |        |
| `List`       | JSON array.                                                                                                                                  | `[1, 7, 3, 4, 5]`                                                        |       |        |
| `TextMap`    | JSON object keyed by text values.                                                                                                            | `{"key1": "value1", "key2": "value2"}`                                   |       |        |
| `Variant`    | JSON object with `tag` and `value` properties.                                                                                               | `{"tag": "InAccount", "value": {"number": "CH-1234567890", "bank": {}}}` |       |        |
| `Optional`   | JSON value when defined, or `null` when empty.                                                                                               | `null`                                                                   |       |        |
| `Enum`       | `string` enum value name.                                                                                                                    | `"Red"` for Daml \`data Color = Red                                      | Green | Blue\` |

<Note>
  Strings are preferred for `Int` and `Decimal` values because many languages, most notably JavaScript, use IEEE doubles for JSON numbers and cannot precisely represent every Daml-LF value. For convenience, parsing accepts both JSON numbers and strings.
</Note>

<Note>
  Timestamp parsing is flexible and accepts `yyyy-mm-ddThh:mm:ss(.s+)?Z`. Sub-second precision beyond microseconds is dropped. The UTC timezone designator must be included to reduce the risk of accidentally passing local times.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/damllf/daml-lf-translation.rst" hash="2de9f83c" */}

# How Daml Types are translated to Daml-LF

This page shows how types in Daml are translated into Daml-LF. It should help you understand and predict the generated client interfaces, which is useful when you're building a Daml-based application that uses the Ledger API or client bindings in other languages.

## Primitive types

Built-in data types in Daml have straightforward mappings to Daml-LF.

This section only covers the serializable types, as these are what client applications can interact with via the generated Daml-LF. (Serializable types are ones whose values can exist on the ledger. Function types, `Update` and `Scenario` types and any types built up from these are excluded, and there are several other restrictions.)

Most built-in types have the same name in Daml-LF as in Daml. These are the exact mappings:

| Daml primitive type | Daml-LF primitive type |
| ------------------- | ---------------------- |
| `Int`               | `Int64`                |
| `Time`              | `Timestamp`            |
| `()`                | `Unit`                 |
| `[]`                | `List`                 |
| `Decimal`           | `Decimal`              |
| `Text`              | `Text`                 |
| `Date`              | `Date`                 |
| `Party`             | `Party`                |
| `Optional`          | `Optional`             |
| `ContractId`        | `ContractId`           |

Be aware that only the Daml primitive types exported by the Prelude module map to the Daml-LF primitive types above. That means that, if you define your own type named `Party`, it will not translate to the Daml-LF primitive `Party`.

## Tuple types

Daml tuple type constructors take types `T1, T2, …, TN` to the type `(T1, T2, …, TN)`. These are exposed in the Daml surface language through the Prelude module.

The equivalent Daml-LF type constructors are `daml-prim:DA.Types:TupleN`, for each particular N (where 2 \<= N \<= 20). This qualified name refers to the package name (`ghc-prim`) and the module name (`GHC.Tuple`).

For example: the Daml pair type `(Int, Text)` is translated to `daml-prim:DA.Types:Tuple2 Int64 Text`.

## Data Types

Daml-LF has three kinds of data declarations:

* **Record** types, which define a collection of data
* **Variant** or **sum** types, which define a number of alternatives
* **Enum**, which defines simplified **sum** types without type parameters nor argument.

Data type declarations in Daml (starting with the `data` keyword) are translated to record, variant or enum types. It’s sometimes not obvious what they will be translated to, so this section lists many examples of data types in Daml and their translations in Daml-LF.

### Record declarations

This section uses the syntax for Daml records with curly braces.

| Daml declaration                           | Daml-LF translation                        |
| ------------------------------------------ | ------------------------------------------ |
| `data Foo = Foo { foo1: Int; foo2: Text }` | `record Foo ↦ { foo1: Int64; foo2: Text }` |
| `data Foo = Bar { bar1: Int; bar2: Text }` | `record Foo ↦ { bar1: Int64; bar2: Text }` |
| `data Foo = Foo { foo: Int }`              | `record Foo ↦ { foo: Int64 }`              |
| `data Foo = Bar { foo: Int }`              | `record Foo ↦ { foo: Int64 }`              |
| `data Foo = Foo {}`                        | `record Foo ↦ {}`                          |
| `data Foo = Bar {}`                        | `record Foo ↦ {}`                          |

### Variant declarations

| Daml declaration                                                                | Daml-LF translation                                                                                                                          |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| `data Foo = Bar Int \| Baz Text`                                                | `variant Foo ↦ Bar Int64 \| Baz Text`                                                                                                        |
| `data Foo a = Bar a \| Baz Text`                                                | `variant Foo a ↦ Bar a \| Baz Text`                                                                                                          |
| `data Foo = Bar Unit \| Baz Text`                                               | `variant Foo ↦ Bar Unit \| Baz Text`                                                                                                         |
| `data Foo = Bar Unit \| Baz`                                                    | `variant Foo ↦ Bar Unit \| Baz Unit`                                                                                                         |
| `data Foo a = Bar \| Baz`                                                       | `variant Foo a ↦ Bar Unit \| Baz Unit`                                                                                                       |
| `data Foo = Foo Int`                                                            | `variant Foo ↦ Foo Int64`                                                                                                                    |
| `data Foo = Bar Int`                                                            | `variant Foo ↦ Bar Int64`                                                                                                                    |
| `data Foo = Foo ()`                                                             | `variant Foo ↦ Foo Unit`                                                                                                                     |
| `data Foo = Bar ()`                                                             | `variant Foo ↦ Bar Unit`                                                                                                                     |
| `data Foo = Bar { bar: Int } \| Baz Text`                                       | `variant Foo ↦ Bar Foo.Bar \| Baz Text`, `record Foo.Bar ↦ { bar: Int64 }`                                                                   |
| `data Foo = Foo { foo: Int } \| Baz Text`                                       | `variant Foo ↦ Foo Foo.Foo \| Baz Text`, `record Foo.Foo ↦ { foo: Int64 }`                                                                   |
| `data Foo = Bar { bar1: Int; bar2: Decimal } \| Baz Text`                       | `variant Foo ↦ Bar Foo.Bar \| Baz Text`, `record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }`                                                   |
| `data Foo = Bar { bar1: Int; bar2: Decimal } \| Baz { baz1: Text; baz2: Date }` | `variant Foo ↦ Bar Foo.Bar \| Baz Foo.Baz`, `record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }`, `record Foo.Baz ↦ { baz1: Text; baz2: Date }` |

### Enum declarations

| Daml declaration                    | Daml-LF declaration                 |
| ----------------------------------- | ----------------------------------- |
| `data Foo = Bar \| Baz`             | `enum Foo ↦ Bar \| Baz`             |
| `data Color = Red \| Green \| Blue` | `enum Color ↦ Red \| Green \| Blue` |

### Banned declarations

There are two gotchas to be aware of: things you might expect to be able to do in Daml that you can't because of Daml-LF.

The first: a single constructor data type must be made unambiguous as to whether it is a record or a variant type. Concretely, the data type declaration `data Foo = Foo` causes a compile-time error, because it is unclear whether it is declaring a record or a variant type.

To fix this, you must make the distinction explicitly. Write `data Foo = Foo {}` to declare a record type with no fields, or `data Foo = Foo ()` for a variant with a single constructor taking unit argument.

The second gotcha is that a constructor in a data type declaration can have at most one unlabelled argument type. This restriction is so that we can provide a straight-forward encoding of Daml-LF types in a variety of client languages.

| Banned declaration               | Workaround                                                                                                  |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `data Foo = Foo`                 | `data Foo = Foo {}` to produce `record Foo ↦ {}` OR `data Foo = Foo ()` to produce `variant Foo ↦ Foo Unit` |
| `data Foo = Bar`                 | `data Foo = Bar {} to produce record Foo ↦ {}` OR `data Foo = Bar () to produce variant Foo ↦ Bar Unit`     |
| `data Foo = Foo Int Text`        | Name constructor arguments using a record declaration, for example `data Foo = Foo { x: Int; y: Text }`     |
| `data Foo = Bar Int Text`        | Name constructor arguments using a record declaration, for example `data Foo = Bar { x: Int; y: Text }`     |
| `data Foo = Bar \| Baz Int Text` | Name arguments to the Baz constructor, for example `data Foo = Bar \| Baz { x: Int; y: Text }`              |

### Restrictions for upgrades

The flavour of a datatype's Daml-LF representation restricts the ways in which it can be upgraded via smart contract upgrades: only records can add fields, and only variants and enums can add new constructors. It is not possible to change the flavour of a datatype once it has been chosen.

Therefore, the ideal choice of the flavour of a datatype strongly depends on what upgrade behaviours are planned for it. For example, the following datatype:

```
data Foo = Foo { foo: Int }
```

is translated to a record in Daml-LF:

```
record Foo ↦ { foo: Int64 }
```

We can add fields when upgrading it, because that does not change its flavour:

```
-- Add a field to Foo in version 2 of its package
data Foo = Foo { foo: Int, newField: Int }
```

```
// Still a record
record Foo ↦ { foo: Int64, newField: Int }
```

However, we cannot add a new constructor, because that would change its flavour from a record to a variant:

```
-- Add a constructor to Foo in version 2 of its package
data Foo
  = Foo { foo: Int }
  | NewConstructor
```

```
// Flavour changed from a record to a variant
variant Foo ↦ Foo Foo.Foo | NewConstructor
```

Note that, as above, a variant with fields will desugar to a single variant and a record for each constructor, such as the following:

```
-- Add a constructor to Foo in version
data Foo
  = Bar { bar1: Int; bar2: Decimal }
  | Baz { baz1: Text; baz2: Date }
```

```
// Desugars to a variant datatype and two record datatypes, one for each
// of the variant's constructors
variant Foo ↦ Bar Foo.Bar | Baz Foo.Baz
record Foo.Bar ↦ { bar1: Int64; bar2: Decimal }
record Foo.Baz ↦ { baz1: Text; baz2: Date }
```

This means that we can upgrade the fields of a constructor and add a new constructor to this particular datatype at the same time, because the changes are valid upgrades to the underlying Daml-LF definitions.

For example, if we add a field `bar3` and a constructor `Bat`:

```
data Foo
  = Bar { bar1: Int; bar2: Decimal, bar3: Text } -- Add a bar3 field
  | Baz { baz1: Text; baz2: Date }
  | Bat { bat1: Int } -- Add a Bat constructor
```

```
variant Foo ↦ Bar Foo.Bar | Baz Foo.Baz | Bat Foo.Bat // Variant adds a constructor - allowed under upgrades
record Foo.Bar ↦ { bar1: Int64; bar2: Decimal; bar3: Text } // Record adds a variant - allowed under upgrades
record Foo.Baz ↦ { baz1: Text; baz2: Date }
record Foo.Bat ↦ { bat1: Int64 } // New variant constructor's underlying datatype
```

In short: If the datatype is planned to gradually add more constructors over time, it should be defined as a variant. If the datatype is planned to add fields over time, it should be defined as a record. If the datatype is planned to do both, it should be defined as a variant with fields.

More information about restrictions imposed on different flavours of datatypes by smart contract upgrades is available in Limitations in Upgrading Variants.

## Type synonyms

Type synonyms (starting with the `type` keyword) are eliminated during conversion to Daml-LF. The body of the type synonym is inlined for all occurrences of the type synonym name.

For example, consider the following Daml type declarations.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type Username = Text
data User = User { name: Username }
```

The `Username` type is eliminated in the Daml-LF translation, as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record User ↦ { name: Text }
```

## Template Types

A template declaration in Daml results in one or more data type declarations behind the scenes. These data types, detailed in this section, are not written explicitly in the Daml program but are created by the compiler.

They are translated to Daml-LF using the same rules as for record declarations above.

These declarations are all at the top level of the module in which the template is defined.

### Template Data Types

Every contract template defines a record type for the parameters of the contract. For example, the template declaration:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Iou
  with
    issuer: Party
    owner: Party
    currency: Text
    amount: Decimal
  where
```

results in this record declaration:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Iou = Iou { issuer: Party; owner: Party; currency: Text; amount: Decimal }
```

This translates to the Daml-LF record declaration:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record Iou ↦ { issuer: Party; owner: Party; currency: Text; amount: Decimal }
```

### Choice Data Types

Every choice within a contract template results in a record type for the parameters of that choice. For example, let’s suppose the earlier `Iou` template has the following choices:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonconsuming choice DoNothing: ()
  controller owner
  do
    return ()

choice Transfer: ContractId Iou
  with newOwner: Party
  controller owner
  do
    updateOwner newOwner
```

This results in these two record types:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data DoNothing = DoNothing {}
data Transfer = Transfer { newOwner: Party }
```

Whether the choice is consuming or nonconsuming is irrelevant to the data type declaration. The data type is a record even if there are no fields.

These translate to the Daml-LF record declarations:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
record DoNothing ↦ {}
record Transfer ↦ { newOwner: Party }
```

## Names with Special Characters

All names in Daml—of types, templates, choices, fields, and variant data constructors—are translated to the more restrictive rules of Daml-LF. ASCII letters, digits, and `_` underscore are unchanged in Daml-LF; all other characters must be mangled in some way, as follows:

* `$` changes to `$$`,
* Unicode codepoints less than 65536 translate to `$uABCD`, where `ABCD` are exactly four (zero-padded) hexadecimal digits of the codepoint in question, using only lowercase `a-f`, and
* Unicode codepoints greater translate to `$UABCD1234`, where `ABCD1234` are exactly eight (zero-padded) hexadecimal digits of the codepoint in question, with the same `a-f` rule.

| Daml name | Daml-LF identifier       |
| --------- | ------------------------ |
| `Foo_bar` | `Foo_bar`                |
| `baz'`    | `baz$u0027`              |
| `:+:`     | `$u003a$u002b$u003a`     |
| `naïveté` | `na$u00efvet$u00e9`      |
| `:🙂:`    | `$u003a$U0001f642$u003a` |

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/integrate/grpc/daml-to-ledger-api.rst" hash="b7b29e30" */}

# How Daml Types are Translated to Protobuf

This page gives an overview and reference on how Daml types and contracts are represented by the gRPC Ledger API as protobuf messages, most notably:

* in the stream of transactions from the `com.daml.ledger.api.v1.transactionservice`
* as payload for `com.daml.ledger.api.v1.createcommand` and `com.daml.ledger.api.v1.exercisecommand` sent to `com.daml.ledger.api.v1.commandsubmissionservice` and `com.daml.ledger.api.v1.commandservice`.

The Daml code in the examples below is written in Daml *1.1*.

## Notation

The notation used on this page for the protobuf messages is the same as you get if you invoke `protoc --decode=Foo < some_payload.bin`. To illustrate the notation, here is a simple definition of the messages `Foo` and `Bar`:

```protobuf theme={"theme":{"light":"github-light","dark":"github-dark"}}
message Foo {
  string field_with_primitive_type = 1;
  Bar field_with_message_type = 2;
}

message Bar {
  repeated int64 repeated_field_inside_bar = 1;
}
```

A particular value of `Foo` is then represented by the Ledger API in this way:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Foo
  field_with_primitive_type: "some string"
  field_with_message_type { // Bar
    repeated_field_inside_bar: 17
    repeated_field_inside_bar: 42
    repeated_field_inside_bar: 3
  }
}
```

The name of messages is added as a comment after the opening curly brace.

## Records and Primitive Types

Records or product types are translated to `com.daml.ledger.api.v1.record`. Here's an example Daml record type that contains a field for each primitive type:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyProductType = MyProductType with
  intField : Int
  textField : Text
  decimalField : Decimal
  boolField : Bool
  partyField : Party
  timeField : Time
  listField : [Int]
  contractIdField : ContractId SomeTemplate
```

And here's an example of creating a value of type \`MyProductType\`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
alice <- allocateParty "Alice"
bob <- allocateParty "Bob"
someCid <- submit alice do createCmd SomeTemplate with owner=alice

let myProduct = MyProductType with
            intField = 17
            textField = "some text"
            decimalField = 17.42
            boolField = False
            partyField = bob
            timeField = datetime 2018 May 16 0 0 0
            listField = [1,2,3]
            contractIdField = someCid
```

For this data, the respective data on the Ledger API is shown below. Note that this value would be enclosed by a particular contract containing a field of type `MyProductType`. See [Contract templates](#contract-templates) for the translation of Daml contracts to the representation by the Ledger API.

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Record
  record_id { // Identifier
    package_id: "some-hash"
    name: "Types.MyProductType"
  }
  fields { // RecordField
    label: "intField"
    value { // Value
      int64: 17
    }
  }
  fields { // RecordField
    label: "textField"
    value { // Value
      text: "some text"
    }
  }
  fields { // RecordField
    label: "decimalField"
    value { // Value
      decimal: "17.42"
    }
  }
  fields { // RecordField
    label: "boolField"
    value { // Value
      bool: false
    }
  }
  fields { // RecordField
    label: "partyField"
    value { // Value
      party: "Bob"
    }
  }
  fields { // RecordField
    label: "timeField"
    value { // Value
      timestamp: 1526428800000000
    }
  }
  fields { // RecordField
    label: "listField"
    value { // Value
      list { // List
        elements { // Value
          int64: 1
        }
        elements { // Value
          int64: 2
        }
        elements { // Value
          int64: 3
        }
      }
    }
  }
  fields { // RecordField
    label: "contractIdField"
    value { // Value
      contract_id: "some-contract-id" 
    }
  }
}
```

## Variants

Variants or sum types are types with multiple constructors. This example defines a simple variant type with two constructors:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MySumType = MySumConstructor1 Int
               | MySumConstructor2 (Text, Bool)
```

The constructor `MyConstructor1` takes a single parameter of type `Integer`, whereas the constructor `MyConstructor2` takes a tuple with two fields as parameter. The snippet below shows how you can create values with either of the constructors.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let mySum1 = MySumConstructor1 17
let mySum2 = MySumConstructor2 ("it's a sum", True)
```

Similar to records, variants are also enclosed by a contract, a record, or another variant.

The snippets below shows the value of `mySum1` and `mySum2` respectively as they would be transmitted on the Ledger API within a contract.

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Value
  variant { // Variant
    variant_id { // Identifier
      package_id: "some-hash"
      name: "Types.MySumType"
    }
    constructor: "MyConstructor1"
    value { // Value
      int64:  17
    }
  }
}
```

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // Value
  variant { // Variant
    variant_id { // Identifier
      package_id: "some-hash"
      name: "Types.MySumType"
    }
    constructor: "MyConstructor2"
    value { // Value
      record { // Record
        fields { // RecordField
          label: "sumTextField"
          value { // Value
            text: "it's a sum"
          }
        }
        fields { // RecordField
          label: "sumBoolField"
          value { // Value
            bool: true
          }
        }
      }
    }
  }
}
```

## Contract Templates

Contract templates are represented as records with the same identifier as the template.

This first example template below contains only the signatory party and a simple choice to exercise:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MySimpleTemplateKey =
  MySimpleTemplateKey
    with
      party: Party

template MySimpleTemplate
    with
        owner: Party
    where
        signatory owner

        key MySimpleTemplateKey owner: MySimpleTemplateKey
        maintainer key.party
```

### Create a Contract

Creating contracts is done by sending a `com.daml.ledger.api.v1.createcommand` to the `com.daml.ledger.api.v1.commandsubmissionservice` or the `com.daml.ledger.api.v1.commandservice`. The message to create a `MySimpleTemplate` contract with *Alice* being the owner is shown below:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // CreateCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  create_arguments { // Record
    fields { // RecordField
      label: "owner"
      value { // Value
        party: "Alice"
      }
    }
  }
}
```

### Receive a Contract

Contracts are received from the `com.daml.ledger.api.v1.transactionservice` in the form of a `com.daml.ledger.api.v1.createdevent`. The data contained in the event corresponds to the data that was used to create the contract.

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // CreatedEvent
  event_id: "some-event-id"
  contract_id: "some-contract-id"
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  create_arguments { // Record
    fields { // RecordField
      label: "owner"
      value { // Value
        party: "Alice"
      }
    }
  }
  witness_parties: "Alice"
}
```

### Exercise a Choice

A choice is exercised by sending an `com.daml.ledger.api.v1.exercisecommand`. Taking the same contract template again, exercising the choice `MyChoice` would result in a command similar to the following:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // ExerciseCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  contract_id: "some-contract-id"
  choice: "MyChoice"
  choice_argument { // Value
    record { // Record
      fields { // RecordField
        label: "parameter"
        value { // Value
          int64: 42
        }
      }
    }
  }
}
```

If the template specifies a key, the `com.daml.ledger.api.v1.exercisebykeycommand` can be used. It works in a similar way as `com.daml.ledger.api.v1.exercisecommand`, but instead of specifying the contract identifier you have to provide its key. The example above could be rewritten as follows:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
{ // ExerciseByKeyCommand
  template_id { // Identifier
    package_id: "some-hash"
    name: "Templates.MySimpleTemplate"
  }
  contract_key { // Value
    record { // Record
      fields { // RecordField
        label: "party"
        value { // Value
          party: "Alice"
        }
      }
    }
  }
  choice: "MyChoice"
  choice_argument { // Value
    record { // Record
      fields { // RecordField
        label: "parameter"
        value { // Value
          int64: 42
        }
      }
    }
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/explanations/daml-packages-and-archive-files.rst" hash="b5af20b7" */}

# Daml packages and archive (.dar) files

When a Daml package is compiled, it is packed into a final artifact called a DAR (`.dar`) file. The purpose of this DAR file is to contain all of the necessary code and logic to run the package's templates, without requiring any other files.

For example, assume a simple package `mypkg` with a single dependency `dep`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: mypkg
version: 1.0.0
source: daml
...
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- /path/to/dep-1.0.0.dar
```

The command `dpm build` compiles it and reports the path of the resulting DAR as the last line:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm build

Running single package build of mypkg as no multi-package.yaml was found.
...
Compiling mypkg to a DAR.
...
Created .daml/dist/mypkg-1.0.0.dar
```

This DAR will contain all of the code for the package, as well as all of the code for its dependencies.

## Structure of an archive file

A DAR is actually a zip file which contains many different files, all of which work together to provide a ledger everything it needs to know in order to run the code it was compiled from.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> unzip -Z1 .daml/dist/mypkg-1.0.0.dar

META-INF/MANIFEST.MF
...
mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.daml
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hi
mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hie
mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
```

The majority of the files in a given DAR will be DALF files (`.dalf`). Each `.dalf` file contains the entire compiled code for a specific package.

One of the DALF files will be the "main" or "primary" package that the DAR was compiled from - this DALF will contain the definitions of templates, interfaces, datatypes, and functions that were originally described in the Daml code that the DAR was compiled from. In this case, that is the `mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf` file listed above.

All of the other DALF files will be for dependency packages of that "main" package, which are required to run the package. This includes the `dep-1.0.0-&lt;dep-package-id&gt;.dalf` file, as well as many DALF files for the `daml-prim` and `daml-stdlib` libraries.

Aside from these files, there will be:

* A `MANIFEST.MF` file, which contains metadata about the rest of the artifacts in the DAR.
  * the name of the "main" package that was compiled into the DAR
  * a list of all of the dependencies of the main package
  * some more metadata about the package
* The source code (`.daml`) for the primary package. This can be used by consumers of the DAR to verify that the DALF they're running corresponds to the code inside of it. It is also used by Daml Studio for code intelligence such as jump-to-definition when the DAR is included as a dependency of another project.
* Interface files (`.hi`, `.hie`, `.conf`) for the primary package. This is also used by Daml Studio to provide jump-to-definition.

Both the source code and interface files are not required by any other tool than Daml Studio - they can be safely removed from the DAR by consumers such as participant runners.

## Difference between DALF files and Daml files

A common question is why DAR files contain DALF files - why don't they just contain all of the source code for all of the packages directly?

To understand why, it is important to understand the distinction between Daml and DALF files:

* Daml files contain the Daml source code that Daml developers write. Daml source code is human-writable and human-readable, and is readable as a general purpose programming language.
* DALF files, on the other hand contain a compact, binary-encoded representation of Daml-LF. Daml-LF is very restricted, comparatively simple computer-executable programming language. Daml-LF is not intended to be human-readable nor human-writable, it is intended to be deterministic, fast to execute, and secure.

Because DAR files are intended to be executed and passed around, they primarily contain Daml-LF, which can be executed directly -- they do not need to store the Daml code from which it was compiled.

## DARs as dependencies

When a new project needs to depend on a different package, the DAR that the package was compiled to is supplied as a data-dependency in the new project's `daml.yaml`.

For example, suppose a new package `next-project` that uses the `mypkg` package as a dependency:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: next-project
version: 1.0.0
source: daml
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- ../mypkg/.daml/dist/mypkg-1.0.0.dar
```

In this case, the compilation process unpacks the `mypkg-1.0.0` DAR, finds its primary package, and exposes that as a dependency to code inside `next-project`. When `next-project` is compiled, it retains all of the DALF files inside the `mypkg` DAR, including the `mypkg` package's dependencies.

In general, any time a DAR is compiled for a package that has further DAR dependencies, those DAR dependencies are unpacked and all of their DALF files are copied into the new output DAR. However, while DALF files are copied over, the dependency DARs' manifest files are not copied over, and neither are the source code and interface files. Only the source code and interface files for the primary package of a DAR can show up in a DAR.

For more information on how to open up and inspect the DAR files and DALF files, refer to the documentation on how to parse Daml archive files.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/component-howtos/development-tooling-authors/how-to-parse-daml-archive-files.rst" hash="1a25e77f" */}

# How to parse Daml archive files

When a Daml project is compiled, it produces a DAR (extension `.dar`), short for Daml Archive. The Daml compiler exposes commands for inspecting this archive.

## Inspecting a DAR file

You can run `dpm damlc inspect-dar /path/to/your.dar` to get a human-readable listing of the files inside it and a list of packages and their package ids. This is often useful to find the package id of the project you just built.

For example, consider a package `mypkg` which depends on a package `dep`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: mypkg
version: 1.0.0
source: daml/Main.daml
...
data-dependencies:
- ../dep/.daml/dist/dep-1.0.0.dar
```

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
name: dep
version: 1.0.0
source: daml/Dep.daml
...
```

When `mypkg-1.0.0` is compiled to a DAR, we can inspect that DAR to ensure that it contains both the `mypkg` package and its dependency `dep`:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm build
...
Created .daml/dist/mypkg-1.0.0.dar

> dpm damlc inspect-dar .daml/dist/mypkg-1.0.0.dar

DAR archive contains the following files:

...
mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.daml
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.hi
mypkg-1.0.0-&lt;mypkg-package-id&gt;/MyPkg.hie
META-INF/MANIFEST.MF

DAR archive contains the following packages:

...
dep-1.0.0-&lt;dep-package-id&gt; "&lt;dep-package-id&gt;"
mypkg-1.0.0-&lt;mypkg-package-id&gt; "&lt;mypkg-package-id&gt;"
```

The first section reports all of the files in DAR, and the second section reports the package name and package ID for every DALF in the archive.

More information on the exact structure of the zip file is available in the explanation on Daml packages and archive files.

## Inspecting a DAR file as JSON

In addition to the human-readable output, you can also get the output as JSON. This is easier to consume programmatically and it is more robust to changes across SDK versions:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
> dpm damlc inspect-dar --json .daml/dist/mypkg-1.0.0.dar
{
    "files": [
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.daml",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hi",
        "mypkg-1.0.0-&lt;mypkg-package-id&gt;/Main.hie",
        "META-INF/MANIFEST.MF"
    ],
    "main_package_id": "&lt;mypkg-package-id&gt;",
    "packages": {
        "&lt;mypkg-package-id&gt;": {
            "name": "mypkg",
            "path":
              "mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf",
            "version": "1.0.0"
        },
        "&lt;dep-package-id&gt;": {
            "name": "dep",
            "path": "mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf",
            "version": "1.0.0"
        }
    }
}
```

Note that `name` and `version` will be `null` for packages in Daml-LF \< 1.8.

## Inspecting the main package of a DAR file

If you'd like to inspect the code inside the main package of a DAR, the Daml compiler provides the `inspect` tool; running `dpm damlc inspect &lt;path-to-dar-file&gt;` prints all of the code in the main package of that DAR file in a human-readable format.

For example, run the `inspect` tool on the DAR produced in the previous section:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Human-readable dump of code in "mypkg" package inside of "mypkg" DAR
> dpm damlc inspect .daml/dist/mypkg-1.0.0.dar
package &lt;mypkg-package-id&gt;
daml-lf 2.1
metadata mypkg-1.0.0

module Main where
...
```

## Inspecting a DALF file

The `inspect` tool also accepts DALF files; running `dpm damlc inspect &lt;path-to-dalf-file&gt;` on a DALF file prints all of the code in that DALF file.

We can unzip a DAR to access its dalfs and inspect them, for example with the DAR from the previous section:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Unzip the DAR to get its DALFs
> unzip .daml/dist/mypkg-1.0.0.dar

# Human-readable dump of code in dep
> dpm damlc inspect mypkg-1.0.0-&lt;mypkg-package-id&gt;/dep-1.0.0-&lt;dep-package-id&gt;.dalf
package &lt;dep-package-id&gt;
daml-lf 2.1
metadata dep-1.0.0

module Dep where
...
```

We can even inspect the main package of a DAR this way, even though running `inspect` directly on the DAR file would require fewer steps.

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Identical to dump from `dpm damlc inspect .daml/dist/mypkg-1.0.0.dar`
> dpm damlc inspect mypkg-1.0.0-&lt;mypkg-package-id&gt;/mypkg-1.0.0-&lt;mypkg-package-id&gt;.dalf
package &lt;mypkg-package-id&gt;
daml-lf 2.1
metadata mypkg-1.0.0

module Main where
...
```

## Parsing DAR and DALF files

To parse a DAR or DALF file from within Scala code, the `com-daml:daml-lf-archive-reader` library on Maven provides a Scala package object `com.digitalasset.daml.lf.archive` with several decoders. Below are the common types of inputs and outputs a decoder can have, and which decoders to use depending on the input and output that is desired. For more details on inputs, outputs, and decoders, please refer to Maven to find the source code for the associated libraries.

### Output types

When decoding a package, a decoder can have one of several possible outputs, depending on what is needed.

* When the full code of the package is needed, pick a decoder returning tuples `(PackageId, Package)`.

  In this case, `PackageId` is a string-like type that comes from `com.digitalasset.daml.lf.language.Ref` in the `com.daml:daml-lf-data` library on Maven. `Package` represents the full structure of a package, and comes from `com.digitalasset.daml.lf.language.Ast`, in the `com.daml:daml-lf-language` library on Maven.

  Because fully decoding the package takes more processing time than the next two examples, only use it when the full package code is needed.

  For example, the `com.digitalasset.daml.lf.typesig.reader.SignatureReader` class from the `com-daml:daml-lf-api-type-signature` library on Maven takes a `(PackageId, Package)` pair to produce a `com.digitalasset.daml.lf.typesig.PackageSignature` (also from the `api-type-signature`) package, which specifies all of the templates, datatypes, and interfaces in a package.

* When only the simplest representation of the protobuf of the package is needed, pick a decoder returning a `com.digitalasset.daml.lf.ArchivePayload` (from the `com-daml:daml-lf-archive` library on Maven). This should only be needed when working with internal protobuf representations of a package.

* When only the package's byte representation and hash is needed, use a decoder that returns `Archive` (from the `com-daml:daml-lf-archive-proto` library on Maven). When using this, the decoder will not spend time decoding any of the package's actual content, such as its metadata or its code.

### Input types

A decoder can either accept DALF files, DAR files, or it can accept both.

* If a decoder accepts DALF files, it will parse the single package in that DALF file to its output type (one of the three specified above).
* If a decoder accepts DAR files, it will parse multiple packages from a DAR file to a struct `Dar[X]`, which is a case class that encodes a DAR as two public fields, `main: X` and `dependencies: List[X]`.
* If a decoder accepts both, it will always produce a `Dar[X]`. When given a DAR, the decoder will run as a normal DAR decoder would. When given a DALF, the decoder will decode the DALF as a single package and return a `Dar[X]` with a `main` package and an empty list of dependencies.

### Decoders

Decoders for reading DALFs are instances of `GenReader[X]`, which provides the method `readArchiveFromFile(file: java.io.File): Either[Error, X]`.

* `val ArchiveReader: GenReader[ArchivePayload]`

  Run `ArchiveReader.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))` to parse out the `ArchivePayload` of a dalf file.

* `val ArchiveDecoder: GenReader[(PackageId, Ast.Package)]`

  Run `ArchiveDecoder.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))` to parse out the `(Ref.PackageId, Ast.Package)` of a dalf file.

* `val ArchiveParser: GenReader[DamlLf.Archive]`

  Run `ArchiveParser.readArchiveFromFile(new java.io.File("&lt;path-to-dalf&gt;"))` to parse out the `DamlLf.Archive` of a dalf file.

Decoders for reading DARs are instances of `GenDarReader`, which provides the method `readArchiveFromFile(file: java.io.File): Either[Error, Dar[X]]`.

* `val DarReader: GenDarReader[ArchivePayload]`

  Run `DarReader.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))` to parse out the `Dar[ArchivePayload]` of a dar file.

* `val DarDecoder: GenDarReader[(PackageId, Ast.Package)]`

  Run `DarDecoder.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))` to parse out the `Dar[(Ref.PackageId, Ast.Package)]` of a dar file.

* `val DarParser: GenDarReader[DamlLf.Archive]`

  Run `DarParser.readArchiveFromFile(new java.io.File("&lt;path-to-dar&gt;"))` to parse out the `Dar[DamlLf.Archive]` of a dar file.

Decoders for reading DARs are instances of `GenUniversalArchiveReader`, which provides the method `readFile(file: java.io.File): Either[Error, Dar[X]]`.

* `val UniversalArchiveReader: GenUniversalArchiveReader[ArchivePayload]`

  Run `UniversalArchiveReader.readFile(new java.io.File("&lt;path-to-dar-or-dalf&gt;"))` to parse out the `Dar[ArchivePayload]` of a dar file.

* `val UniversalArchiveDecoder: GenUniversalArchiveReader[(PackageId, Ast.Package)]`

  Run `UniversalArchiveDecoder.readFile(new java.io.File("&lt;path-to-dar-or-dalf&gt;"))` to parse out the `Dar[(Ref.PackageId, Ast.Package)]` of a dar file.

### Example

We can load up a Scala REPL with the `daml-lf-archive-reader` library to interactively parse our `mypkg` DAR:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> // Start a REPL
scala> val darEither = DarDecoder.readArchiveFromFile(".daml/dist/mypkg-1.0.0.dar")
val dar: Either[Error, Dar[(Ref.PackageId, Ast.Package)]]
Right(Dar((..., GenPackage(Map(Main -> ...
...

scala> // Extract the resulting value
scala> val dar = darEither.toOption.get

scala> :t dar.main
(Ref.PackageId, Ast.Package)

scala> :t dar.dependencies
List[(Ref.PackageId, Ast.Package)]
```

The Dar datatype also has a method `.all` which returns the main package and dependencies as a single list. Mapping `_1` over this gets all of the package IDs in the DAR:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> dar.all.map(_._1)
val res1: List[Ref.PackageId] = List(224..., 54f..., ...)
```

Get the names of all the dependency packages in the DAR by using the `.metadata.name` field in the `Ast.Package` datatype:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
scala> dar.dependencies.map(_._2.metadata.name)
val res2: List[com.digitalasset.daml.lf.data.Ref.PackageName] = List(daml-prim, daml-prim-DA-Exception-ArithmeticError, ...
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
