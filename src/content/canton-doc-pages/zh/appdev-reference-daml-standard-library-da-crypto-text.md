---
title: "DA.Crypto.Text"
slug: "appdev-reference-daml-standard-library-da-crypto-text"
locale: "zh"
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

> Daml 标准库模块 DA.Crypto.Text（Alpha）参考文档。

<span id="module-da-crypto-text-67266" />

# DA.Crypto.Text

用于使用 Crypto 内置函数的函数。

例如，用于实现 CCTP 功能。

## 模块快照

<CardGroup cols={2}>
  <Card title="Lifecycle">
      Alpha (experimental).
  </Card>

  <Card title="Notices">
    Status: `active`
    引入于：`3.4.9`
    Removed in: `-`
    警告：`2`
    Deprecations: `0`
    已弃用自：`-`
  </Card>
</CardGroup>

<Warning>
  DA.Crypto.Text is an alpha feature.它可能会更改，恕不另行通知。
</Warning>

<AccordionGroup>
  <Accordion title="所有警告 (2)">
    * DA.Crypto.Text 是一项 alpha 功能。它可能会更改，恕不另行通知。
    * 在构建选项中使用 -Wno-crypto-text-is-alpha 来禁用此警告
  </Accordion>
</AccordionGroup>

## 数据类型

<span id="type-da-crypto-text-byteshex-47880" />

### `type BytesHex = Text`

<span id="type-da-crypto-text-publickeyhex-51359" />

### `type PublicKeyHex = Text`

用于 ECDSA 签名验证的 DER 格式的公钥

<span id="type-da-crypto-text-signaturehex-12945" />

### `type SignatureHex = Text`

DER 格式的 SECP256K1 签名

## 类型类

<span id="class-da-crypto-text-hastohex-92431" />

### `class HasToHex a`

方法：

* `toHex : a -> BytesHex`
  将键入的数据值转换为十六进制编码的字符串。

实例：

* `instance HasToHex Party`
* `instance HasToHex Int`
* `instance HasToHex Text`

<span id="class-da-crypto-text-hasfromhex-84972" />

### `class HasFromHex a`

方法：

* `fromHex : BytesHex -> a`
  将十六进制编码的字符串转换为类型化数据值。

实例：

* `instance HasFromHex (Optional Party)`
* `instance HasFromHex (Optional Int)`
* `instance HasFromHex (Optional Text)`

## 函数

<span id="function-da-crypto-text-ishex-17968" />

### `isHex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isHex : Text -> Bool
```

如果 `t` 不为空且仅包含以下内容，则 `isHex` 为 `True`
十六进制或十六进制字符。

<span id="function-da-crypto-text-sha256-84499" />

### `sha256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sha256 : BytesHex -> BytesHex
```

计算 `Text` 的已解码 UTF8 字节的 SHA256 哈希值，并以其十六进制编码形式返回
形式。 The hex encoding uses lowercase letters.

<span id="function-da-crypto-text-keccak256-57106" />

### `keccak256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
keccak256 : BytesHex -> BytesHex
```

计算 `Text` UTF8 字节的 KECCAK256 哈希值，并以其十六进制编码形式返回
形式。十六进制编码使用小写字母。

<span id="function-da-crypto-text-secp256k1withecdsaonly-56908" />

### `secp256k1WithEcdsaOnly`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
secp256k1WithEcdsaOnly : SignatureHex -> BytesHex -> PublicKeyHex -> Bool
```

在给定十六进制编码消息和十六进制编码 DER 格式公钥的情况下验证 SECP256K1 签名。

<span id="function-da-crypto-text-secp256k1-38075" />

### `secp256k1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
secp256k1 : SignatureHex -> BytesHex -> PublicKeyHex -> Bool
```

给定十六进制编码消息的 SHA256 哈希值和十六进制编码 DER 格式的公钥，验证 SECP256K1 签名。

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

字节编码字符串中存在的字节数。

<span id="function-da-crypto-text-minbytes32hex-29458" />

### `minBytes32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minBytes32Hex : BytesHex
```

Minimum Bytes32 hex value

<span id="function-da-crypto-text-maxbytes32hex-56560" />

### `maxBytes32Hex````haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxBytes32Hex : BytesHex
```

最大 Bytes32 十六进制值

<span id="function-da-crypto-text-isbytes32hex-1801" />

### `isBytes32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isBytes32Hex : BytesHex -> Bool
```

验证字节编码字符串是否为 Bytes32Hex

<span id="function-da-crypto-text-minuint32hex-58146" />

### `minUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt32Hex : BytesHex
```

最小 UInt32 十六进制值

<span id="function-da-crypto-text-maxuint32hex-80016" />

### `maxUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt32Hex : BytesHex
```

最大 UInt32 十六进制值

<span id="function-da-crypto-text-isuint32hex-65583" />

### `isUInt32Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUInt32Hex : BytesHex -> Bool
```

验证字节编码字符串是否为 UInt32Hex

<span id="function-da-crypto-text-minuint64hex-67161" />

### `minUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt64Hex : BytesHex
```

最小 UInt64 十六进制值

<span id="function-da-crypto-text-maxuint64hex-40555" />

### `maxUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt64Hex : BytesHex
```

最大 UInt64 十六进制值

<span id="function-da-crypto-text-isuint64hex-49912" />

### `isUInt64Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUInt64Hex : BytesHex -> Bool
```

验证字节编码字符串是否为 UInt64Hex

<span id="function-da-crypto-text-minuint256hex-23801" />

### `minUInt256Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minUInt256Hex : BytesHex
```

最小 UInt256 十六进制值

<span id="function-da-crypto-text-maxuint256hex-58651" />

### `maxUInt256Hex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maxUInt256Hex : BytesHex
```

最大 UInt256 十六进制值

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

将字节编码字符串打包为给定的字节计数大小。如果字节串比 pad 短
size，然后以 00 字节字符串作为前缀。如果字节串较大，则截断该字节串。

<span id="function-da-crypto-text-slicehexbytes-22633" />

### `sliceHexBytes`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sliceHexBytes : BytesHex -> Int -> Int -> Either Text BytesHex
```

提取从 startByte 开始直到（但不包括 endByte）的字节字符串。字节索引从 1 开始。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
