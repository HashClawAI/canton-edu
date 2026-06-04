---
title: "DA.Crypto.Text"
slug: "appdev-reference-daml-standard-library-da-crypto-text"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-crypto-text.md"
source_title: "DA.Crypto.Text"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-crypto-text
---

# DA.Crypto.Text

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Crypto.Text

> Reference documentation for Daml module DA.Crypto.Text.

<span id="module-da-crypto-text-67266" />

# DA.Crypto.Text

Functions for working with Crypto builtins.

For example, as used to implement CCTP functionality.

## Module Snapshot

<CardGroup cols={2}>
  <Card title="Lifecycle">
    Alpha (experimental).
  </Card>

  <Card title="Notices">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `2`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

<Warning>
  DA.Crypto.Text is an alpha feature. It can change without notice.
</Warning>

<AccordionGroup>
  <Accordion title="All warnings (2)">
    * DA.Crypto.Text is an alpha feature. It can change without notice.
    * use -Wno-crypto-text-is-alpha in build-options to disable this warning
  </Accordion>
</AccordionGroup>

## Data Types

<span id="type-da-crypto-text-byteshex-47880" />

### `type BytesHex = Text`

<span id="type-da-crypto-text-publickeyhex-51359" />

### `type PublicKeyHex = Text`

A DER formatted public key to be used for ECDSA signature verification

<span id="type-da-crypto-text-signaturehex-12945" />

### `type SignatureHex = Text`

A DER formatted SECP256K1 signature

## Typeclasses

<span id="class-da-crypto-text-hastohex-92431" />

### `class HasToHex a`

Methods:

* `toHex : a -> BytesHex`
  Converts a typed data value into a hex encoded string.

Instances:

* `instance HasToHex Party`
* `instance HasToHex Int`
* `instance HasToHex Text`

<span id="class-da-crypto-text-hasfromhex-84972" />

### `class HasFromHex a`

Methods:

* `fromHex : BytesHex -> a`
  Converts a hex encoded string into a typed data value.

Instances:

* `instance HasFromHex (Optional Party)`
* `instance HasFromHex (Optional Int)`
* `instance HasFromHex (Optional Text)`

## Functions

<span id="function-da-crypto-text-ishex-17968" />

### `isHex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isHex : Text -> Bool
```

`isHex` is `True` if `t` is not empty and consists only of
hex or hexadecimal characters.

<span id="function-da-crypto-text-sha256-84499" />

### `sha256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sha256 : BytesHex -> BytesHex
```

Computes the SHA256 hash of the decoded UTF8 bytes of the `Text`, and returns it in its hex-encoded
form. The hex encoding uses lowercase letters.

<span id="function-da-crypto-text-keccak256-57106" />

### `keccak256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
keccak256 : BytesHex -> BytesHex
```

Computes the KECCAK256 hash of the UTF8 bytes of the `Text`, and returns it in its hex-encoded
form. The hex encoding uses lowercase letters.

<span id="function-da-crypto-text-secp256k1withecdsaonly-56908" />

### `secp256k1WithEcdsaOnly`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
secp256k1WithEcdsaOnly : SignatureHex -> BytesHex -> PublicKeyHex -> Bool
```

Validate the SECP256K1 signature given a hex encoded message and a hex encoded DER formatted public key.

<span id="function-da-crypto-text-secp256k1-38075" />

### `secp256k1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
secp256k1 : SignatureHex -> BytesHex -> PublicKeyHex -> Bool
```

Validate the SECP256K1 signature given a SHA256 hash of a hex encoded message and a hex encoded DER formatted public key.

<span id="function-da-crypto-text-numericviastringtohex-44461" />

### `numericViaStringToHex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
numericViaStringToHex : NumericScale n => Numeric n -> BytesHex
```

<span id="function-da-crypto-text-numericviastringfromhex-60098" />

### `numericViaStringFromHex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
numericViaStringFromHex : NumericScale n => BytesHex -> Optional (Numeric n)
```

<span id="function-da-crypto-text-bytecount-29784" />

### `byteCount`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
byteCount : BytesHex -> Int
```

Number of bytes present in a byte encoded string.

<span id="function-da-crypto-text-minbytes32hex-29458" />

### `minBytes32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minBytes32Hex : BytesHex
```

Minimum Bytes32 hex value

<span id="function-da-crypto-text-maxbytes32hex-56560" />

### `maxBytes32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxBytes32Hex : BytesHex
```

Maximum Bytes32 hex value

<span id="function-da-crypto-text-isbytes32hex-1801" />

### `isBytes32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isBytes32Hex : BytesHex -> Bool
```

Validate that the byte encoded string is Bytes32Hex

<span id="function-da-crypto-text-minuint32hex-58146" />

### `minUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt32Hex : BytesHex
```

Minimum UInt32 hex value

<span id="function-da-crypto-text-maxuint32hex-80016" />

### `maxUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt32Hex : BytesHex
```

Maximum UInt32 hex value

<span id="function-da-crypto-text-isuint32hex-65583" />

### `isUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUInt32Hex : BytesHex -> Bool
```

Validate that the byte encoded string is UInt32Hex

<span id="function-da-crypto-text-minuint64hex-67161" />

### `minUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt64Hex : BytesHex
```

Minimum UInt64 hex value

<span id="function-da-crypto-text-maxuint64hex-40555" />

### `maxUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt64Hex : BytesHex
```

Maximum UInt64 hex value

<span id="function-da-crypto-text-isuint64hex-49912" />

### `isUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUInt64Hex : BytesHex -> Bool
```

Validate that the byte encoded string is UInt64Hex

<span id="function-da-crypto-text-minuint256hex-23801" />

### `minUInt256Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt256Hex : BytesHex
```

Minimum UInt256 hex value

<span id="function-da-crypto-text-maxuint256hex-58651" />

### `maxUInt256Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt256Hex : BytesHex
```

Maximum UInt256 hex value

<span id="function-da-crypto-text-isuint256hex-33362" />

### `isUInt256Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUInt256Hex : BytesHex -> Bool
```

Validate that the byte encoded string is UInt256Hex

<span id="function-da-crypto-text-packhexbytes-55939" />

### `packHexBytes`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
packHexBytes : BytesHex -> Int -> Optional BytesHex
```

Pack a byte encoded string to a given byte count size. If the byte string is shorter than the pad
size, then prefix with 00 byte strings. If the byte string is larger, then truncate the byte string.

<span id="function-da-crypto-text-slicehexbytes-22633" />

### `sliceHexBytes`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sliceHexBytes : BytesHex -> Int -> Int -> Either Text BytesHex
```

Extract the byte string starting at startByte up to, but excluding, endByte. Byte indexing starts at 1.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
