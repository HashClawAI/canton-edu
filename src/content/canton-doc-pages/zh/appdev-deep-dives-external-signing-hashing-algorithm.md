---
title: "外部签名：哈希算法"
slug: "appdev-deep-dives-external-signing-hashing-algorithm"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/external-signing-hashing-algorithm.md"
source_title: "External Signing: Hashing Algorithm"
tags:
  - appdev
  - deep-dives
  - external-signing-hashing-algorithm
---

# 外部签名：哈希算法

> 外部签名所用 PreparedTransaction 的确定性哈希规范（V2）。

# 外部签名哈希算法

## 简介

本文规定用于对 `com.daml.ledger.api.v2.interactive.PreparedTransaction` 产生确定性哈希的编码算法。外部 Party 私钥持有者对该哈希签名，以代表该外部 Party 授权交易所描述的账本变更。

可在任意语言实现；因 Canton 基于 JVM 并使用 Java protobuf 库，部分编码模式带有实现偏好，规范中已明示。

Protobuf 序列化不适合直接用于密码学签名哈希，因其非规范形式。须定义更精确的编码规范以便跨语言确定性重实现并提供密码学保证。详见 [https://protobuf.dev/programming-guides/serialization-not-canonical/](https://protobuf.dev/programming-guides/serialization-not-canonical/)。

## 版本

### 哈希方案版本

哈希算法整体带版本号，以便在底层 Daml 格式或签名验证方式变更时演进；实现须遵循所实现版本的规范。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// The hashing scheme version used when building the hash of the PreparedTransaction
enum HashingSchemeVersion {
  HASHING_SCHEME_VERSION_UNSPECIFIED = 0;
  reserved 1; // Hashing Scheme V1 - unsupported
  HASHING_SCHEME_VERSION_V2 = 2;
}
```

哈希算法与用于同步交易的 synchronizer 协议版本绑定；各哈希方案版本在一个或多个协议版本上受支持，提交交易的 synchronizer 上须使用受支持的哈希方案版本。

| 协议版本 | 支持的哈希方案 |
| ---------------- | ------------------------- |
| v33              | v2                        |

### 交易节点
交易节点另以 Daml（LF）版本单独版本化。编码版本与 LF 版本解耦，实现应聚焦哈希版本；新 LF 版本可能引入新字段或节点类型，故节点 protobuf 亦版本化。实践中每个新 Daml 语言版本对应新哈希版本。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
message Node {
  string node_id = 1;

  // Versioned node
  oneof versioned_node {
    // Start at 1000 so we can add more fields before if necessary
    // When new versions will be added, they will show here
    interactive.transaction.v1.Node v1 = 1000;
  }
}
```

## V2
### 总体方法
`PreparedTransaction` 的哈希通过将消息各 protobuf 字段编码为字节数组并送入 `SHA-256` 哈希构建器计算。下文说明如何确定性编码各 proto 消息；部分中间结果会先 SHA-256，其哈希作为上层编码（必要时会明示）。

数值使用大端序；protobuf 数值按 Java 类型表示编码，映射见 [https://protobuf.dev/programming-guides/proto3/#scalar](https://protobuf.dev/programming-guides/proto3/#scalar)。

<Note>
  在 Java 中，无符号 32/64 位整数用有符号对应类型表示，最高位存放在符号位
</Note> 32-bit and 64-bit integers are represented using their signed counterparts, with the top bit simply being stored in the sign bit
</Note>

Canton 底层序列化 protobuf 使用的 Java 库：[https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java](https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java)

### 相对 V1 的变更
* Fetch 节点新增 `interface_id` 以支持 Daml 接口 field in Fetch nodes for support of Daml interfaces.

* 最终哈希中加入哈希方案版本，降低跨版本碰撞风险 in the final hash to make the hash more robust to cross version collisions.

* 元数据中以 `min_ledger_effective_time` 与 `max_ledger_effective_time` 替代 `ledger_effective_time` in the metadata with `min_ledger_effective_time` and `max_ledger_effective_time`.

  > * 以时间界替代固定 ledger 时间，使 Daml 模型可基于时间断言而不把签名窗口限制得过窄 a fixed ledger time with time bounds, allowing Daml Models to make assertions based on time without restricting the signing window as was required

### 符号与工具函数
* `encode`: Function that takes a protobuf message or primitive type `T` and transforms it into an array of bytes: `encode: T =\> byte\[\]`

e.g:

```
encode(false) = [0x00]
```

* `to_utf_8`: Function converting a Java `String` to its UTF-8 encoded version: `to_utf_8: string => byte[]`

e.g:

```
to_utf_8("hello") = [0x68, 0x65, 0x6c, 0x6c, 0x6f]
```

* `len`: Function returning the size of a collection (`array`, `list` etc...) as a signed 4 bytes integer: `len: Col => Int`

e.g:

```
len([4, 2, 8]) = 3
```

* `split`: Function converting a Java `String` to a list of `String`, by splitting the input using the provided delimiter: `split: (string, char) => byte[]`

e.g:

```
split("com.digitalasset.canton", '.') = ["com", "digitalasset", "canton"]
```

* `||`: Symbol representing concatenation of byte arrays

e.g:

```
[0x00] || [0x01] = [0x00, 0x01]
```

* `[]`: Empty byte array. Denotes that the value should not be encoded.
* `from_hex_string`: Function that takes a string in the hexadecimal format as input and decodes it as a byte array: `from_hex_string: string => byte[]`

e.g:

```
from_hex_string("08020a") = [0x08, 0x02, 0x0a]
```

* `int_to_string`: Function that takes an int and converts it to a string : `int_to_string: int => string`

e.g:

```
int_to_string(42) = "42"
```

* `some`: Value wrapped in a defined optional. Should be encoded as a defined optional value: `some: T => optional T`

e.g:

```
encode(some(5)) = 0x01 || encode(5)
```

See encoding of optional values below for details.

### Primitive Types

除非另有说明，原始 protobuf 类型编码如下, this is how primitive protobuf types should be encoded.

<Note>
  此处仅列出编码 `PreparedTransaction` 所需的 protobuf 类型，并非全部类型
</Note> are described here, only the ones necessary to encode a `PreparedTransaction` message.
</Note>

<Warning>
  即使默认值也必须编码。例如 int32 未设置时仍应编码 0；空 repeated 字段仍编码为 `0x00` 字节（详见 repeated 节）
</Warning> must be included in the encoding. For instance if an int32 field is not set in the serialized protobuf, its default value (0) should be encoded. Similarly, an empty repeated field still results in a `0x00` byte encoding (see the `repeated` section below for more details)
</Warning>

#### google.protobuf.Empty

```
fn encode(empty): 0x00
```

#### bool

```
fn encode(bool):
   if (bool)
      0x01
   else
      0x00
```

#### int64 - uint64 - sint64 - sfixed64

```
fn encode(long):
   long # Java `Long` value equivalent: 8 bytes
```

e.g:

```
31380 (base 10) == 0x0000000000007a94
```

#### int32 - uint32 - sint32 - sfixed32

```
fn encode(int):
   int # Java `Int` value equivalent: 4 bytes
```

e.g:

```
5 (base 10) == 0x00000005
```

#### bytes / byte\[]

```
fn encode(bytes):
encode(len(bytes)) || bytes
```

e.g

```
0x68656c6c6f ->
    0x00000005 || # length
    0x68656c6c6f # content
```

#### string

```
fn encode(string):
   encode(to_utf8(string))
```

e.g

```
"hello" ->
    0x00000005 || # length
    0x68656c6c6f # utf-8 encoding of "hello"
```

### 集合与包装类型
#### repeated
`repeated` 字段为有序集合，列表顺序在编码过程与提交交易的 protobuf 中均不得改变 an ordered collection of values of a specific message of type `T``. It is critical that the order of values in the list is not modified, both for the encoding process and in the protobuf itself when submitting the transaction for execution. Below is the pseudocode algorithm encoding a protobuf value ``repeated T list;`\`

```
fn encode(list):
   # prefix the result with the serialized length of the list
   result = encode(len(list)) # (result is mutable)

   # successively add encoded elements to the result, in order
   for each element in list:
      result = result || encode(element)

   return result
```

<Note>
  该编码函数同样适用于工具函数生成的列表（如 `split`）
</Note> to lists generated from utility functions (e.g: `split`).
</Note>

#### optional```
fn encode(optional):
   if (is_set(optional))
      0x01 || encode(optional.value)
   else
      0x00
```

`is_set` returns `true` if the value was set in the protobuf, `false` otherwise.

#### map
protobuf `map` 条目顺序不保证，不利于确定性编码；因此在 protobuf 定义中普遍用 `repeated` 替代 `map` in protobuf serialization is not guaranteed, making it problematic for deterministic encoding. To address this, `repeated` values are used instead of `map` throughout the protobuf definitions.

### gRPC Ledger API Value
编码 `com.daml.ledger.api.v2.value.proto` 中的 `Value` 消息。为清晰起见列出全部值类型；各值前有类型唯一标签（见下文） defined in `com.daml.ledger.api.v2.value.proto` For clarity, all value types are exhaustively listed here. Each value is prefixed by a tag unique to its type, which is explicitly specified for each value below.

#### Unit

```
fn encode(unit):
    0X00 # Unit Type Tag
```

Protobuf [Definition]()

#### Bool

```
fn encode(bool):
    0X01 || # Bool Type Tag
encode(bool) # Primitive boolean encoding
```

Protobuf [Definition]()

#### Int64

```
fn encode(int64):
    0X02 || # Int64 Type Tag
    encode(int64) # Primitive int64 encoding
```

Protobuf [Definition]()

#### Numeric

```
fn encode(numeric):
    0X03 || # Numeric Type Tag
    encode(numeric) # Primitive string encoding
```

Protobuf [Definition]()

#### Timestamp

```
fn encode(timestamp):
    0X04 || # Timestamp Type Tag
    encode(timestamp) # Primitive sfixed64 encoding
```

Protobuf [Definition]()

#### Date

```
fn encode(date):
    0X05 || # Date Type Tag
    encode(date) # Primitive int32 encoding
```

Protobuf [Definition]()

#### Party

```
fn encode(party):
    0X06 || # Party Type Tag
    encode(party) # Primitive string encoding
```

Protobuf [Definition]()

#### Text

```
fn encode(text):
    0X07 || # Text Type Tag
    encode(text) # Primitive string encoding
```

Protobuf [Definition]()

#### Contract\_id

```
fn encode(contract_id):
    0X08 || # Contract Id Type Tag
    from_hex_string(contract_id) # Contract IDs are hexadecimal strings, so they need to be decoded as such. They should not be encoded as classic strings
```

Protobuf [Definition]()

#### Optional

```
fn encode(optional):
   if (optional.value is set)
      0X09 || # Optional Type Tag
      0x01 || # Defined optional
      encode(optional.value)
   else
      0X09 || # Optional Type Tag
      0x00 || # Undefined optional
```

Protobuf [Definition]()

Note this is conceptually the same as for the primitive `optional` protobuf modifier, with the addition of the type tag prefix.

#### List

```
fn encode(list):
   0X0a || # List Type Tag
   encode(list.elements)
```

Protobuf [Definition]()

#### TextMap

```
fn encode(text_map):
   0X0b || # TextMap Type Tag
   encode(text_map.entries)
```

Protobuf [Definition]()

**TextMap.Entry**

```
fn encode(entry):
   encode(entry.key) || encode(entry.value)
```

Protobuf [Definition]()

#### Record

```
fn encode(record):
   0X0c || # Record Type Tag
   encode(some(record.record_id)) ||
   encode(record.fields)
```

Protobuf [Definition]()

**RecordField**

```
fn encode(record_field):
   encode(some(record_field.label)) || encode(record_field.value)
```

Protobuf [Definition]()

#### Variant

```
fn encode(variant):
   0X0d || # Variant Type Tag
   encode(some(variant.variant_id)) ||
   encode(variant.constructor) || encode(variant.value)
```

Protobuf [Definition]()

#### Enum

```
fn encode(enum):
   0X0e || # Enum Type Tag
   encode(some(enum.enum_id)) ||
   encode(enum.constructor)
```

Protobuf [Definition]()

#### GenMap

```
fn encode(gen_map):
   0X0f || # GenMap Type Tag
   encode(gen_map.entries)
```

Protobuf [Definition]()

**GenMap.Entry**

```
fn encode(entry):
   encode(entry.key) || encode(entry.value)
```

Protobuf [Definition]()

#### Identifier

```
fn encode(identifier):
   encode(identifier.package_id) || encode(split(identifier.module_name, '.')) || encode(split(identifier.entity_name, '.')))
```

Protobuf [Definition]()

## Transaction
交易是森林（树列表），由如下 protobuf 消息表示 (list of trees). It is represented

交易编码函数为

```
fn encode(transaction):
   encode(transaction.version) || encode_node_ids(transaction.roots)
```

`encode_node_ids(node_ids)` encodes lists in the same way as described before, except the encoding of a `node_id` is NOT done by encoding it as a string, but instead uses the following `encode(node_id)` function:

```
fn encode(node_id):
    for node in nodes:
        if node.node_id == node_id:
           return sha_256(encode_node(node))
    fail("Missing node") # All node ids should have a unique node in the nodes list. If a node is missing it should be reported as a bug.
```

<Warning>
  `encode(node_id)` 会在 nodes 列表中找到对应节点并编码；`node_id` 本身从不编码，仅作引用。每个节点编码会 **经 sha_256 哈希**，在编码根节点及递归编码 `Exercise`/`Rollback` 子节点时均相关
</Warning> finds the corresponding node in the list of nodes and encodes the node. The `node_id` is an opaque value only used to reference nodes and is itself never encoded. Additionally, each node's encoding is **hashed using the sha\_256 hashing algorithm**. This is relevant when encoding root nodes here as well as when recursively encoding sub-nodes of `Exercise` and `Rollback` nodes as seen below.
</Warning>

### Node
<Note>
  每个节点编码前会加节点元信息前缀，在各节点编码中明示
</Note> with additional meta-information about the node, this is made explicit in the encoding of each node.
</Note>

`Exercise` 与 `Rollback` 节点的 `children` 字段通过 `NodeId` 引用其他节点 have a `children` field that references other nodes by their `NodeId`.

The following `find_seed: NodeId => optional bytes` function is used in the encoding:

```
fn find_seed(node_id):
    for node_seed in node_seeds:
        if int_to_string(node_seed.node_id) == node_id
            return some(node_seed.seed)
    return none

# There's no need to prefix the seed with its length because it has a fixed length. So its encoding is the identity function
fn encode_seed(seed):
    seed

# Normal optional encoding, except the seed is encoded with `encode_seed`
fn encode_optional_seed(optional_seed):
    if (is_some(optional_seed))
      0x01 || encode_seed(optional_seed.get)
   else
      0x00
```

`some` represents a set optional field, `none` an empty optional field.

#### Create```
fn encode_node(create):
    0x01 || # Node encoding version
    encode(create.lf_version) || # Node LF version
    0x00 || # Create node tag
    encode_optional_seed(find_seed(node.node_id)) ||
    encode(create.contract_id) ||
    encode(create.package_name) ||
    encode(create.template_id) ||
    encode(create.argument) ||
    encode(create.signatories) ||
    encode(create.stakeholders)
```

#### Exercise```
fn encode_node(exercise):
    0x01 || # Node encoding version
    encode(exercise.lf_version) || # Node LF version
    0x01 || # Exercise node tag
    encode_seed(find_seed(node.node_id).get) ||
    encode(exercise.contract_id) ||
    encode(exercise.package_name) ||
    encode(exercise.template_id) ||
    encode(exercise.signatories) ||
    encode(exercise.stakeholders) ||
    encode(exercise.acting_parties) ||
    encode(exercise.interface_id) ||
    encode(exercise.choice_id) ||
    encode(exercise.chosen_value) ||
    encode(exercise.consuming) ||
    encode(exercise.exercise_result) ||
    encode(exercise.choice_observers) ||
    encode(exercise.children)
```

<Warning>
  Exercise 节点的 node seed **必须**已定义，因此按非 optional 编码（见 `find_seed(...).get`）。若在 `node_seeds` 中找不到 seed，应停止编码并报错
</Warning>, the node seed **MUST** be defined. Therefore it is encoded as a **non** optional field, as noted via the `.get` in `find_seed(node.node_id).get`. If the seed of an exercise node cannot be found in the list of `node_seeds`, encoding must be stopped and it should be reported as a bug.
</Warning>

<Note>
  Exercise 节点最后编码的是 `children` 字段，会递归遍历交易树
</Note> node is its `children` field. This recursively traverses the transaction tree.
</Note>

#### Fetch```
fn encode_node(fetch):
    0x01 || # Node encoding version
    encode(fetch.lf_version) || # Node LF version
    0x02 || # Fetch node tag
    encode(fetch.contract_id) ||
    encode(fetch.package_name) ||
    encode(fetch.template_id) ||
    encode(fetch.signatories) ||
    encode(fetch.stakeholders) ||
    encode(fetch.interface_id) ||
    encode(fetch.acting_parties)
```

#### Rollback```
fn encode_node(rollback):
   0x01 || # Node encoding version
   0x03 || # Rollback node tag
   encode(rollback.children)
```

<Note>
  Rollback 节点没有 lf version
</Note> have an lf version.
</Note>

#### 交易哈希
交易编码完成后，对编码字节数组运行 `sha_256`，并加哈希用途前缀, the hash is obtained by running `sha_256` over the encoded byte array,

```
fn hash(transaction):
    sha_256(
        0x00000030 || # Hash purpose
        encode(transaction)
    )
```

## Metadata
`PreparedTransaction` 的最后部分是元数据。元数据所有字段均须签名；仅部分字段影响账本变更，其余为 Canton 协议所需或已通过签名交易间接承诺. Note that all fields

```
fn encode(metadata, prepare_submission_request):
    0x01 || # Metadata Encoding Version
    encode(metadata.submitter_info.act_as) ||
    encode(metadata.submitter_info.command_id) ||
    encode(metadata.transaction_uuid) ||
    encode(metadata.mediator_group) ||
    encode(metadata.synchronizer_id) ||
    encode(metadata.min_ledger_effective_time) ||
    encode(metadata.max_ledger_effective_time) ||
    encode(metadata.submission_time) ||
    encode(metadata.disclosed_events)
```

### ProcessedDisclosedContract```
fn encode(processed_disclosed_contract):
    encode(processed_disclosed_contract.created_at) ||
    encode(processed_disclosed_contract.contract)
```

### 元数据哈希
元数据编码完成后，对编码字节数组运行 `sha_256` 并加哈希用途前缀得到哈希：

```
fn hash(metadata):
    sha_256(
        0x00000030 || # Hash purpose
        encode(metadata)
    )
```

## 最终哈希
最后计算须由外部 Party 协议签名私钥签名的哈希，以承诺账本变更 that needs to be signed to commit to the ledger changes.

```
fn encode(prepared_transaction):
    0x00000030 || # Hash purpose
    0x02 || # Hashing Scheme Version
    hash(transaction) ||
    hash(metadata)
```

```
fn hash(prepared_transaction):
    sha_256(encode(prepared_transaction))
```

须用入网外部 Party 时使用的协议签名私钥对该哈希签名，并将签名与 `PreparedTransaction` 一并提交 API 以写入账本 with the protocol signing private key(s)

## 示例
Python 示例实现
<div className="toggle">
  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
  # SPDX-License-Identifier: Apache-2.0

  # Implements the transaction hashing specification defined in the README.md at https://github.com/digital-asset/canton/blob/main/community/ledger-api/src/release-line-3.2/protobuf/com/daml/ledger/api/v2/interactive/README.md

  import com.daml.ledger.api.v2.interactive.interactive_submission_service_pb2 as interactive_submission_service_pb2
  import hashlib
  import struct

  # Hash purpose reserved for prepared transaction
  PREPARED_TRANSACTION_HASH_PURPOSE = b"\x00\x00\x00\x30"
  # Version of the hashing scheme implemented in this file as a byte
  # Used in the encoding
  HASHING_SCHEME_VERSION_V2 = (
      interactive_submission_service_pb2.HashingSchemeVersion.HASHING_SCHEME_VERSION_V2
  )
  # Byte version for the encoding (\x02)
  HASHING_SCHEME_VERSION = HASHING_SCHEME_VERSION_V2.to_bytes(
      length=1, byteorder="big", signed=False
  )
  # Version of the protobuf encoding the transaction nodes
  # See DamlTransaction.Node.versioned_node in the interactive_submission_service.proto file
  NODE_ENCODING_VERSION = b"\x01"


  def encode_bool(value):
      return b"\x01" if value else b"\x00"


  def encode_int32(value):
      if not (-(2**31) <= value < 2**31):
          raise ValueError(f"Value {value} out of range for int32")
      return struct.pack(">i", value)


  def encode_int64(value):
      return struct.pack(">q", value)


  def encode_string(value):
      utf8_bytes = value.encode("utf-8")
      return encode_bytes(utf8_bytes)


  def encode_bytes(value):
      length = encode_int32(len(value))
      return length + value

  # Like encode_bytes but without the length prefix, as hashes have a fixed size
  def encode_hash(value):
      return value


  def encode_hex_string(value):
      return encode_bytes(bytes.fromhex(value))


  def encode_optional(value, encode_fn):
      if value is not None:
          return b"\x01" + encode_fn(value)
      else:
          return b"\x00"


  def encode_proto_optional(parent_value, field_name, value, encode_fn):
      if parent_value.HasField(field_name):
          return b"\x01" + encode_fn(value)
      else:
          return b"\x00"


  def encode_repeated(values, encode_fn):
      length = encode_int32(len(values))
      encoded_values = b"".join(encode_fn(v) for v in values)
      return length + encoded_values


  def sha256(data):
      return hashlib.sha256(data).digest()


  def find_seed(
      node_id, node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed]
  ):
      for node_seed in node_seeds:
          if str(node_seed.node_id) == node_id:
              return node_seed.seed
      return None


  def encode_prepared_transaction(
      prepared_transaction: interactive_submission_service_pb2.PreparedTransaction,
      nodes_dict: dict,
  ):
      transaction_hash = hash_transaction(prepared_transaction.transaction, nodes_dict)
      metadata_hash = hash_metadata(prepared_transaction.metadata)
      return sha256(
          PREPARED_TRANSACTION_HASH_PURPOSE
          + HASHING_SCHEME_VERSION
          + transaction_hash
          + metadata_hash
      )


  def hash_transaction(
      transaction: interactive_submission_service_pb2.DamlTransaction, nodes_dict: dict
  ):
      encoded_transaction = encode_transaction(
          transaction, nodes_dict, transaction.node_seeds
      )
      return sha256(PREPARED_TRANSACTION_HASH_PURPOSE + encoded_transaction)


  def encode_transaction(
      transaction,
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      version = encode_string(transaction.version)
      roots = encode_repeated(transaction.roots, encode_node_id(nodes_dict, node_seeds))
      return version + roots


  def encode_identifier(identifier):
      return (
          encode_string(identifier.package_id)
          + encode_repeated(identifier.module_name.split("."), encode_string)
          + encode_repeated(identifier.entity_name.split("."), encode_string)
      )


  def encode_node_id(
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      def encode(node_id):
          node = nodes_dict[node_id]
          return sha256(encode_node(node, nodes_dict, node_seeds))

      return encode


  def encode_node(
      node,
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      node_id = node.node_id
      if node.HasField("v1"):
          return encode_node_v1(node.v1, node_id, nodes_dict, node_seeds)
      raise ValueError("Unsupported node version")


  def encode_node_v1(
      node,
      node_id,
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      if node.HasField("create"):
          return encode_create_node(node.create, node_id, node_seeds)
      elif node.HasField("exercise"):
          return encode_exercise_node(node.exercise, node_id, nodes_dict, node_seeds)
      elif node.HasField("fetch"):
          return encode_fetch_node(node.fetch, node_id)
      elif node.HasField("rollback"):
          return encode_rollback_node(node.rollback, node_id, nodes_dict, node_seeds)
      raise ValueError("Unsupported node type")


  def encode_create_node(
      create,
      node_id,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      return (
          NODE_ENCODING_VERSION
          + encode_string(create.lf_version)
          + b"\x00"  # Create node tag
          + encode_optional(find_seed(node_id, node_seeds), encode_hash)
          + encode_hex_string(create.contract_id)
          + encode_string(create.package_name)
          + encode_identifier(create.template_id)
          + encode_value(create.argument)
          + encode_repeated(create.signatories, encode_string)
          + encode_repeated(create.stakeholders, encode_string)
      )


  def encode_exercise_node(
      exercise,
      node_id,
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      return (
          NODE_ENCODING_VERSION
          + encode_string(exercise.lf_version)
          + b"\x01"  # Exercise node tag
          + encode_hash(find_seed(node_id, node_seeds))
          + encode_hex_string(exercise.contract_id)
          + encode_string(exercise.package_name)
          + encode_identifier(exercise.template_id)
          + encode_repeated(exercise.signatories, encode_string)
          + encode_repeated(exercise.stakeholders, encode_string)
          + encode_repeated(exercise.acting_parties, encode_string)
          + encode_proto_optional(
              exercise, "interface_id", exercise.interface_id, encode_identifier
          )
          + encode_string(exercise.choice_id)
          + encode_value(exercise.chosen_value)
          + encode_bool(exercise.consuming)
          + encode_proto_optional(
              exercise, "exercise_result", exercise.exercise_result, encode_value
          )
          + encode_repeated(exercise.choice_observers, encode_string)
          + encode_repeated(exercise.children, encode_node_id(nodes_dict, node_seeds))
      )


  def encode_fetch_node(fetch, node_id):
      return (
          NODE_ENCODING_VERSION
          + encode_string(fetch.lf_version)
          + b"\x02"  # Fetch node tag
          + encode_hex_string(fetch.contract_id)
          + encode_string(fetch.package_name)
          + encode_identifier(fetch.template_id)
          + encode_repeated(fetch.signatories, encode_string)
          + encode_repeated(fetch.stakeholders, encode_string)
          + encode_proto_optional(
              fetch, "interface_id", fetch.interface_id, encode_identifier
          )
          + encode_repeated(fetch.acting_parties, encode_string)
      )


  def encode_rollback_node(
      rollback,
      node_id,
      nodes_dict: dict,
      node_seeds: [interactive_submission_service_pb2.DamlTransaction.NodeSeed],
  ):
      return (
          NODE_ENCODING_VERSION
          + b"\x03"  # Rollback node tag
          + encode_repeated(rollback.children, encode_node_id(nodes_dict, node_seeds))
      )


  def hash_metadata(metadata):
      encoded_metadata = encode_metadata(metadata)
      return sha256(PREPARED_TRANSACTION_HASH_PURPOSE + encoded_metadata)


  def encode_metadata(metadata):
      return (
          b"\x01"
          + encode_repeated(metadata.submitter_info.act_as, encode_string)
          + encode_string(metadata.submitter_info.command_id)
          + encode_string(metadata.transaction_uuid)
          + encode_int32(metadata.mediator_group)
          + encode_string(metadata.synchronizer_id)
          + encode_proto_optional(
              metadata,
              "min_ledger_effective_time",
              metadata.min_ledger_effective_time,
              encode_int64,
          )
          + encode_proto_optional(
              metadata,
              "max_ledger_effective_time",
              metadata.max_ledger_effective_time,
              encode_int64,
          )
          + encode_int64(metadata.preparation_time)
          + encode_repeated(metadata.input_contracts, encode_input_contract)
      )


  def encode_input_contract(contract):
      return encode_int64(contract.created_at) + sha256(
          encode_create_node(contract.v1, "unused_node_id", [])
      )


  def encode_value(value):
      if value.HasField("unit"):
          return b"\x00"
      elif value.HasField("bool"):
          return b"\x01" + encode_bool(value.bool)
      elif value.HasField("int64"):
          return b"\x02" + encode_int64(value.int64)
      elif value.HasField("numeric"):
          return b"\x03" + encode_string(value.numeric)
      elif value.HasField("timestamp"):
          return b"\x04" + encode_int64(value.timestamp)
      elif value.HasField("date"):
          return b"\x05" + encode_int32(value.date)
      elif value.HasField("party"):
          return b"\x06" + encode_string(value.party)
      elif value.HasField("text"):
          return b"\x07" + encode_string(value.text)
      elif value.HasField("contract_id"):
          return b"\x08" + encode_hex_string(value.contract_id)
      elif value.HasField("optional"):
          return b"\x09" + encode_proto_optional(
              value.optional, "value", value.optional.value, encode_value
          )
      elif value.HasField("list"):
          return b"\x0a" + encode_repeated(value.list.elements, encode_value)
      elif value.HasField("text_map"):
          return b"\x0b" + encode_repeated(value.text_map.entries, encode_text_map_entry)
      elif value.HasField("record"):
          return (
              b"\x0c"
              + encode_proto_optional(
                  value.record, "record_id", value.record.record_id, encode_identifier
              )
              + encode_repeated(value.record.fields, encode_record_field)
          )
      elif value.HasField("variant"):
          return (
              b"\x0d"
              + encode_proto_optional(
                  value.variant, "variant_id", value.variant.variant_id, encode_identifier
              )
              + encode_string(value.variant.constructor)
              + encode_value(value.variant.value)
          )
      elif value.HasField("enum"):
          return (
              b"\x0e"
              + encode_proto_optional(
                  value.enum, "enum_id", value.enum.enum_id, encode_identifier
              )
              + encode_string(value.enum.constructor)
          )
      elif value.HasField("gen_map"):
          return b"\x0f" + encode_repeated(value.gen_map.entries, encode_gen_map_entry)
      raise ValueError("Unsupported value type")


  def encode_text_map_entry(entry):
      return encode_string(entry.key) + encode_value(entry.value)


  def encode_record_field(field):
      return encode_optional(field.label, encode_string) + encode_value(field.value)


  def encode_gen_map_entry(entry):
      return encode_value(entry.key) + encode_value(entry.value)


  def create_nodes_dict(prepared_transaction):
      nodes_dict = {}
      for node in prepared_transaction.transaction.nodes:
          nodes_dict[node.node_id] = node
      return nodes_dict
  ```
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
