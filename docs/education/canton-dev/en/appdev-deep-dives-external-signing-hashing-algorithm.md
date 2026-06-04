---
title: "External Signing: Hashing Algorithm"
slug: "appdev-deep-dives-external-signing-hashing-algorithm"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/external-signing-hashing-algorithm.md"
source_title: "External Signing: Hashing Algorithm"
tags:
  - appdev
  - deep-dives
  - external-signing-hashing-algorithm
---

# External Signing: Hashing Algorithm

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# External Signing: Hashing Algorithm

> Deterministic hashing specification for prepared transactions used by external signing.

# External Signing Hashing Algorithm

## Introduction

This document specifies the encoding algorithm used to produce a deterministic hash of a `com.daml.ledger.api.v2.interactive.PreparedTransaction`. The resulting hash is signed by the holder of the external party's private key. The signature authorizes the ledger changes described by the transaction on behalf of the external party.

The specification can be implemented in any language, but certain encoding patterns are biased due to Canton being implemented in a JVM-based language and using the Java protobuf library. Those biases are made explicit in the specification.

Protobuf serialization is unsuitable for signing cryptographic hashes because it is not canonical. We must define a more precise encoding specification that can be re-implemented deterministically across languages and provide the required cryptographic guarantees. See [https://protobuf.dev/programming-guides/serialization-not-canonical/](https://protobuf.dev/programming-guides/serialization-not-canonical/) for more information on the topic.

## Versioning

### Hashing Scheme Version

The hashing algorithm as a whole is versioned. This enables updates to accommodate changes in the underlying Daml format, or, for instance, to the way the protocol verifies signatures. The implementation must respect the specification of the version it implements.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// The hashing scheme version used when building the hash of the PreparedTransaction
enum HashingSchemeVersion {
  HASHING_SCHEME_VERSION_UNSPECIFIED = 0;
  reserved 1; // Hashing Scheme V1 - unsupported
  HASHING_SCHEME_VERSION_V2 = 2;
}
```

The hashing algorithm is tied to the protocol version of the synchronizer used to synchronize the transaction. Specifically, each hashing scheme version is supported on one or several protocol versions. Implementations must use a hashing scheme version supported on the synchronizer on which the transaction is submitted.

| Protocol Version | Supported Hashing Schemes |
| ---------------- | ------------------------- |
| v33              | v2                        |

### Transaction Nodes

Transaction nodes are additionally individually versioned with a Daml version (also called LF version). The encoding version is decoupled from the LF version and implementations should only focus on the hashing version. However, new LF versions may introduce new fields in nodes or new node types. For that reason, the protobuf representation of a node is versioned to accommodate those future changes. In practice, every new Daml language version results in a new hashing version.

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

### General approach

The hash of the `PreparedTransaction` is computed by encoding every protobuf field of the messages to byte arrays, and feeding those encoded values into a `SHA-256` hash builder. The rest of this section details how to deterministically encode every proto message into a byte array. Sometimes during the process, partially encoded results are hashed with SHA-256, and the resulting hash value serves as the encoding in messages further up. This is explicit when necessary.

Big Endian notation is used for numeric values. Furthermore, protobuf numeric values are encoded according to their Java type representation. Refer to the official protobuf documentation for more information about protobuf to Java type mappings: [https://protobuf.dev/programming-guides/proto3/#scalar](https://protobuf.dev/programming-guides/proto3/#scalar) In particular:

<Note>
  In Java, unsigned 32-bit and 64-bit integers are represented using their signed counterparts, with the top bit simply being stored in the sign bit
</Note>

Additionally, this is the java library used under the hood in Canton to serialize and deserialize protobuf: [https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java](https://github.com/protocolbuffers/protobuf/tree/v3.25.5/java)

### Changes from V1

* Addition of an `interface_id` field in Fetch nodes for support of Daml interfaces.

* Addition of the hashing scheme version in the final hash to make the hash more robust to cross version collisions.

* Replace `ledger_effective_time` in the metadata with `min_ledger_effective_time` and `max_ledger_effective_time`.

  > * These effectively replace a fixed ledger time with time bounds, allowing Daml Models to make assertions based on time without restricting the signing window as was required with a fixed set ledger time.

### Notation and Utility Functions

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

Unless otherwise specified, this is how primitive protobuf types should be encoded.

<Note>
  Not all protobuf types are described here, only the ones necessary to encode a `PreparedTransaction` message.
</Note>

<Warning>
  Even default values must be included in the encoding. For instance if an int32 field is not set in the serialized protobuf, its default value (0) should be encoded. Similarly, an empty repeated field still results in a `0x00` byte encoding (see the `repeated` section below for more details)
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

### Collections / Wrappers

#### repeated

`repeated` protobuf fields represent an ordered collection of values of a specific message of type `T``. It is critical that the order of values in the list is not modified, both for the encoding process and in the protobuf itself when submitting the transaction for execution. Below is the pseudocode algorithm encoding a protobuf value ``repeated T list;`\`

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
  This encoding function also applies to lists generated from utility functions (e.g: `split`).
</Note>

#### optional

```
fn encode(optional):
   if (is_set(optional))
      0x01 || encode(optional.value)
   else
      0x00
```

`is_set` returns `true` if the value was set in the protobuf, `false` otherwise.

#### map

The ordering of `map` entries in protobuf serialization is not guaranteed, making it problematic for deterministic encoding. To address this, `repeated` values are used instead of `map` throughout the protobuf definitions.

### gRPC Ledger API Value

Encoding for the `Value` message defined in `com.daml.ledger.api.v2.value.proto` For clarity, all value types are exhaustively listed here. Each value is prefixed by a tag unique to its type, which is explicitly specified for each value below.

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

A transaction is a forest (list of trees). It is represented with a following protobuf message found here.

The encoding function for a transaction is

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
  `encode(node_id)` effectively finds the corresponding node in the list of nodes and encodes the node. The `node_id` is an opaque value only used to reference nodes and is itself never encoded. Additionally, each node's encoding is **hashed using the sha\_256 hashing algorithm**. This is relevant when encoding root nodes here as well as when recursively encoding sub-nodes of `Exercise` and `Rollback` nodes as seen below.
</Warning>

### Node

<Note>
  Each node's encoding is prefixed with additional meta-information about the node, this is made explicit in the encoding of each node.
</Note>

`Exercise` and `Rollback` nodes both have a `children` field that references other nodes by their `NodeId`.

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

#### Create

```
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

#### Exercise

```
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
  For Exercise nodes, the node seed **MUST** be defined. Therefore it is encoded as a **non** optional field, as noted via the `.get` in `find_seed(node.node_id).get`. If the seed of an exercise node cannot be found in the list of `node_seeds`, encoding must be stopped and it should be reported as a bug.
</Warning>

<Note>
  The last encoded value of the exercise node is its `children` field. This recursively traverses the transaction tree.
</Note>

#### Fetch

```
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

#### Rollback

```
fn encode_node(rollback):
   0x01 || # Node encoding version
   0x03 || # Rollback node tag
   encode(rollback.children)
```

<Note>
  Rollback nodes do not have an lf version.
</Note>

#### Transaction Hash

Once the transaction is encoded, the hash is obtained by running `sha_256` over the encoded byte array, with a hash purpose prefix:

```
fn hash(transaction):
    sha_256(
        0x00000030 || # Hash purpose
        encode(transaction)
    )
```

## Metadata

The final part of `PreparedTransaction` is metadata. Note that all fields of the metadata need to be signed. Only some fields contribute to the ledger change triggered by the transaction. The rest of the fields are required by the Canton protocol but either have no impact on the ledger change, or have already been signed indirectly by signing the transaction itself.

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

### ProcessedDisclosedContract

```
fn encode(processed_disclosed_contract):
    encode(processed_disclosed_contract.created_at) ||
    encode(processed_disclosed_contract.contract)
```

### Metadata Hash

Once the metadata is encoded, the hash is obtained by running `sha_256` over the encoded byte array, with a hash purpose prefix:

```
fn hash(metadata):
    sha_256(
        0x00000030 || # Hash purpose
        encode(metadata)
    )
```

## Final Hash

Finally, compute the hash that needs to be signed to commit to the ledger changes.

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

This resulting hash must be signed with the protocol signing private key(s) used to onboard the external party. Both the signature along with the `PreparedTransaction` must be sent to the API to submit the transaction to the ledger.

## Example

Example implementation in Python

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

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
