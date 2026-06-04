---
title: "Key Management"
slug: "global-synchronizer-production-operations-key-management"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/key-management.md"
source_title: "Key Management"
tags:
  - global-synchronizer
  - production-operations
  - key-management
---

# Key Management

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Key Management

> Manage cryptographic keys for Canton nodes - listing, rotation, generation, and restrictions

## Crypto key management

This page explains how to list, rotate, generate, deactivate, and delete keys of a Canton node. It also explains how to configure the cryptographic schemes supported by a node.

There is a separate section on the management of namespace keys.

### List keys

Use the following command to enumerate the public keys that the node `myNode` stores in its vault:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.public.list()
    res1: Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 12207872a327...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(sequencer-auth, proof-of-ownership)
        ),
        name = Some(KeyName(mediator1-sequencer-auth))
      ),
    ..
```

This will show a non-empty sequence of keys, assuming `myNode` is running and has created keys during startup, which is the default behavior.

Similarly, a user can enumerate the private keys of `myNode`:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.list()
    res2: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12207872a327...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(mediator1-sequencer-auth))
    ..
```

A user can list the keys that a node has authorized for usage at a Synchronizer like this:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.owner_to_key_mappings
                                .list(store = mySynchronizerId, filterKeyOwnerUid = myNode.id.filterString)
                                .flatMap(_.item.keys)
    res3: Seq[PublicKey] = Vector(
      SigningPublicKey(
        id = 12207872a327...,
        format = DER-encoded X.509 SubjectPublicKeyInfo,
        keySpec = EC-Curve25519,
        usage = Set(sequencer-auth, proof-of-ownership)
      ),
      SigningPublicKey(
        id = 1220db0eb017...,
        format = DER-encoded X.509 SubjectPublicKeyInfo,
    ..
```

### Rotate keys

Canton supports rotating the keys of a node `myNode` with a single command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.rotate_node_keys()
```

In order to ensure continuous operation, the command first activates the new key and only then deactivates the old key. The command rotates **all** keys of `myNode`. But the command does not rotate namespace keys. The node deactivates the old keys on all Synchronizers, but they remain in the vault of `myNode`.

The following command rotates a single key of `myNode`:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.rotate_node_key(oldKeyFingerprint, "newKeyName")
    res5: PublicKey = SigningPublicKey(
      id = 1220ad959eff...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(sequencer-auth, proof-of-ownership)
    )
```

<Note>
  Key rotation should be interleaved with taking a backup.
</Note>

### Generate and activate keys

Canton creates keys with default parameters for all nodes. To have different key parameters, generate keys manually.

To generate and activate a new signing key for `myNode`, run the following commands:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = myNode.keys.secret.generate_signing_key(
      "mySigningKeyName",
      SigningKeyUsage.ProtocolOnly,
      Some(SigningKeySpec.EcCurve25519)
    )
    key : SigningPublicKey = SigningPublicKey(
      id = 1220b8113819...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.owner_to_key_mappings.add_key(key.fingerprint, key.purpose)
```

Likewise, the following commands generate and activate a new encryption key:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = myNode.keys.secret.generate_encryption_key(
      "myEncryptionKeyName",
      Some(EncryptionKeySpec.EcP256)
    )
    key : EncryptionPublicKey = EncryptionPublicKey(
      id = 1220c6f1c9da...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-P256
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.owner_to_key_mappings.add_key(key.fingerprint, key.purpose)
```

Refer to the page on key restrictions for further information on `SigningKeyUsage`. Keys are generated according to specific cryptographic key formats. Please refer to the following tables for more information on the expected key formats in Canton.

### Deactivate keys

To deactivate a key on all Synchronizers run the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.owner_to_key_mappings.remove_key(key.fingerprint, key.purpose)
```

Node operators normally do not need to deactivate keys, as a node deactivates old keys when rolling keys. When changing to a different scheme, it may be necessary that an operator explicitly deactivates a key.

### Delete keys

After rotating or deactivating a key it remains in the node's vault. To permanently delete a key from the vault, use the following console command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.keys.secret.delete(key.fingerprint, force = true)
```

<Warning>
  Exercise caution when deleting a private key. Ensure that the key is no longer in use and is not needed for decrypting or creating signatures for old messages. Therefore, only delete a key after deactivating the key and pruning the node for a timestamp later than the deactivation. This is especially crucial for sequencers in open networks. For example, if a participant lags in retrieving sequenced events, and the operator of the sequencer rolls the sequencer’s signing key, the old signing key must remain accessible to sign the events from before the key roll for lagging participants. Otherwise, deleting the key prematurely may cause irreversible issues for these participants.
</Warning>

### Configure cryptographic schemes

Canton supports several cryptographic schemes. By default, a node allows for using all cryptographic schemes supported by Canton.

To configure the default and allowed schemes for a node include a snippet like the following into the Canton configuration:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    participants.participant1 {
       crypto {
         provider = jce

         # signing
         signing.algorithms {
           default = ed-25519
           allowed = [ed-25519, ec-dsa-sha-256, ec-dsa-sha-384]
         }
         signing.keys {
           default = ec-curve-25519
           allowed = [ec-curve-25519, ec-p-256, ec-p-384, ec-secp-256k-1]
         }

         # asymmetric encryption
         encryption.algorithms {
           default = ecies-hkdf-hmac-sha-256-aes-128-cbc
           allowed = [ecies-hkdf-hmac-sha-256-aes-128-cbc, rsa-oaep-sha-256]
         }
         encryption.keys {
           default = ec-p-256
           allowed = [ec-p-256, rsa-2048]
         }
      }
    }
  }

```

<Note>
  Every Synchronizer imposes a minimum set of cryptographic schemes that its members must support. If a node does not support this minimum set of schemes, it is unable to connect to the Synchronizer.
</Note>

### Disable Session keys

An explanation of the purpose and security implications of session keys is available in [Cryptographic keys in Canton](/overview/learn/cryptographic-keys).

While session keys improve performance, they also introduce a security risk, as the keys are stored in memory—even if only for a short duration. If you prefer to disable session keys and accept the resulting performance degradation, you can do so by setting the following configurations.

To disable **session encryption keys**:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant3.caching.session-encryption-key-cache.enabled = false
```

To disable **session signing keys**:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant3.crypto.kms.session-signing-keys.enabled = false
```

Please note that **session signing keys** are only used with an external KMS (Key Management Service) provider.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/keys/key_restrictions.rst" hash="52807875" */}

## Restrict key usage

This page explains how to limit the usage of cryptographic keys of a Canton node to specific purposes, as best practice to contain damage of potentially compromised keys.

### Signing key usage

Canton defines the following key usages for signing keys:

* `Namespace`: a key that defines a node's identity and signs topology requests (see namespace key management)
* `SequencerAuthentication`: a key that authenticates members of the network towards a sequencer
* `Protocol`: a key that signs various structures as part of the synchronization protocol execution

#### Restrict the usage of a signing key

Set the `usage` parameter with the desired usages when you generate a new key.

For example, use the following command to generate a signing key restricted to `Protocol` usage only:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val myKey = myNode.keys.secret.generate_signing_key(
      name = "mySigningKey",
      usage = SigningKeyUsage.ProtocolOnly,
    )
    myKey : SigningPublicKey = SigningPublicKey(
      id = 1220a5fb14f5...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

Some predefined sets are available for common usages: `NamespaceOnly`, `SequencerAuthenticationOnly`, `ProtocolOnly`, `All`. Individual usages can otherwise be combined in a `Set`, but this is not recommended to avoid that keys are used for multiple purposes.

<Note>
  Once specified during key generation, the set of usages is fixed and cannot be modified during the lifetime of that key. Instead, a new key must be generated and activated, and the old one deactivated. See key management for more information regarding the key management commands.
</Note>

If you are using a Key Management Service (KMS) to handle Canton's keys in external key storage mode, and want to use manually generated keys that are already stored in the KMS, set the `usage` parameter with the desired usages when you register the keys with Canton:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
node.keys.secret.register_kms_signing_key(
  kmsKeyId,
  usage = SigningKeyUsage.ProtocolOnly,
  name = s"${node.name}-signing-new",
)
```

The returned key can be used in other key management commands.

#### Determine the usage of an existing signing key

To find what usage a signing key has been assigned, use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.public.list(
      filterFingerprint = myKey.id.unwrap,
    )
    intermediateKey : Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220a5fb14f5...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mySigningKey))
      )
    )
```

If you omit the `filterFingerprint` parameter, all the existing keys will be returned.

#### Determine the existing keys with a given usage

To find all the signing keys that have been assigned a given usage, use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.public.list(
      filterUsage = SigningKeyUsage.ProtocolOnly,
    )
    intermediateKey : Seq[PublicKeyWithName] = Vector(
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220033a8e3d...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mediator1-signing))
      ),
      SigningPublicKeyWithName(
        publicKey = SigningPublicKey(
          id = 1220a5fb14f5...,
          format = DER-encoded X.509 SubjectPublicKeyInfo,
          keySpec = EC-Curve25519,
          usage = Set(signing, proof-of-ownership)
        ),
        name = Some(KeyName(mySigningKey))
      )
    )
```

All the keys that have been assigned at least one of the usages specified in `filterUsage` will be returned.

### Namespace key delegation restrictions

As described in the identity management page, Canton uses topology transactions to manage identities, and these transactions are signed by keys with `Namespace` usage. Namespace key management shows that you can create intermediate keys to sign topology transactions, thereby limiting exposure of the root namespace key. These intermediate keys can be further restricted in terms of which kind of topology transactions they can sign using fine-grained delegation restrictions.

Canton defines the following restrictions for namespace keys:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// the key can sign all currently known mappings and all mappings that will be added in future releases
message CanSignAllMappings {}
// the key can sign all currently known mappings and all mappings that will be added in future releases, except for
// namespace delegations
message CanSignAllButNamespaceDelegations {}
// the key can only sign the explicitly specified mappings
message CanSignSpecificMappings {
  repeated Enums.TopologyMappingCode mappings = 1;
}
```

#### Restrict the types of mappings that a key can sign

You must first create a new key with at least `Namespace` usage, then delegate the signing privileges for a namespace to that key, specifying the desired restrictions in the `delegationRestriction` parameter.

For example, in the following, the first command creates an intermediate key for the root namespace, then the second one delegates the signing privileges to it, allowing it to sign all types of topology mappings except namespace delegations themselves:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKey = myNode.keys.secret.generate_signing_key(
      name = "intermediate-key",
      usage = SigningKeyUsage.NamespaceOnly,
    )
    intermediateKey : SigningPublicKey = SigningPublicKey(
      id = 1220481ada67...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.namespace_delegations.propose_delegation(
      namespace = myNode.namespace,
      targetKey = intermediateKey,
      delegationRestriction = CanSignAllButNamespaceDelegations,
    )
    res5: SignedTopologyTransaction[TopologyChangeOp, NamespaceDelegation] = SignedTopologyTransaction(
      TopologyTransaction(
        NamespaceDelegation(
          namespace = 122009299340...,
          target = SigningPublicKey(
            id = 1220481ada67...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = not-nsd
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:b9b6a4bf20d3...
      ),
      signatures = 122009299340...
    )
```

Like all topology mappings, the delegation restrictions on a namespace key can be updated. To do so, issue a new `propose_delegation` command with the updated delegation restrictions.

<Warning>
  If you define intermediate namespace keys with restricted delegations, you must ensure that all authorizations are covered and that by combining multiple namespace keys together, they can authorize all topology transactions. Otherwise, some operational procedures may fail. For example, rotating a key will fail if there is not at least one namespace key that can authorize `OwnerToKey` mappings.

  In such cases, the operation will fail with a "Could not find an appropriate signing key to issue the topology transaction" error message and code `TOPOLOGY_NO_APPROPRIATE_SIGNING_KEY_IN_STORE`.
</Warning>

#### Determine the restrictions of an existing namespace key

To find what signing restrictions have been defined on a namespace key, use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ myNode.topology.namespace_delegations.list(
      store = TopologyStoreId.Authorized,
      filterTargetKey = Some(intermediateKey.id),
    )
    res6: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListNamespaceDelegationResult] = Vector(
      ListNamespaceDelegationResult(
        context = BaseResult(
          storeId = Authorized,
          validFrom = 2026-05-04T17:53:53.944669Z,
          validUntil = None,
          sequenced = 2026-05-04T17:53:53.944669Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:b9b6a4bf20d3...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(122009299340...)
        ),
        item = NamespaceDelegation(
          namespace = 122009299340...,
          target = SigningPublicKey(
            id = 1220481ada67...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = not-nsd
        )
      )
    )
```

If you omit the `filterTargetKey` parameter, all the existing namespace delegations will be returned.

{/* COPIED_END */}

This document is a work in progress. The feature will be developed and released in the future, following the procedures described in the document.

## Namespace Key Management

### Online Root Namespace Key

By default, the Canton node creates a root namespace key during the initialization of the node. Operators can manually create an intermediate key on the node to authorize topology transactions. Only the intermediate key can be changed. Therefore, it is important to keep the root key secure.

If a Canton node is configured to use a KMS system, then the root key can be administratively isolated, using the KMS Administration controls to remove node access to the root key. As the root key is only required when authorizing a new intermediate key or revoking an existing authorization, it is sufficient to just selectively allow the node to access the key only whenever such operations are performed.

Only the root key can be isolated. All the other keys are essential for Canton to operate correctly. Optionally, the intermediate key can also be isolated but will have to be turned on and off as needed during administrative operations such as uploading DARs or adding parties.

### Offline Root Namespace Key

A more secure way to manage the root namespace key is to use an offline root namespace key. In this case, the root namespace key is stored in a secure, possibly air gapped location, inaccessible from the Canton node.

Where the root key is stored depends on your organization's security requirements. For the remainder of this guide, assume that there are two sites, the online site of the node with its intermediate key and the offline site of the root key. The offline root key is used to sign a delegation to the node's intermediate key, which is then used to authorize topology transactions.

The offline root key procedure is supported by a set of utility scripts, which can be found in the Canton `scripts` directory (`scripts/offline-root-key`).

#### Channel for Key Exchange

There must be a channel or method which allows to exchange the public intermediate key and the signed intermediate namespace delegations between the online and offline sites. The channel must be trusted in terms of authenticity, but not confidentiality, as no secret information is exchanged. This means you need to ensure that the data is not tampered with during transport, but the data itself does not need to be encrypted.

This can be done using multiple methods, depending on whether the sites are air-gapped or connected through a network. Possible examples are: secure file transfer, QR codes, physical storage medium.

Assuming that such a trusted channel exists, the following steps are required to set up the offline root namespace key:

#### 1. Configure Node To Expect External Root Key

Before the first start-up, the Canton node must be configured not to initialize automatically. This is done by setting

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.init.identity.type = manual
```

The node can then be started with this configuration. It starts the Admin API, but halts the startup process and wait for the initialization of the node identity together with the necessary topology transactions.

#### 2. Export Public Key of Node

Assuming you have access to the remote console of the node, create a new signing key to use as the intermediate key:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val key = participant1.keys.secret.generate_signing_key(name = "NamespaceDelegation", usage = com.digitalasset.canton.crypto.SigningKeyUsage.NamespaceOnly)
    key : SigningPublicKey = SigningPublicKey(
      id = 122080b595e9...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val intermediateKeyPath = better.files.File.newTemporaryFile(prefix = "intermediate-key.pub").pathAsString
    intermediateKeyPath : String = "/tmp/intermediate-key.pub3520580670384386470"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.public.download_to(key.id, intermediateKeyPath)
```

This creates a file with the public key of the intermediate key.

The supported key specifications are listed in the follow protobuf definition:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
enum SigningKeySpec {
  SIGNING_KEY_SPEC_UNSPECIFIED = 0;

  // Elliptic Curve Key from Curve25519
  // as defined in http://ed25519.cr.yp.to/
  SIGNING_KEY_SPEC_EC_CURVE25519 = 1;

  // Elliptic Curve Key from the NIST P-256 curve (aka secp256r1)
  // as defined in https://doi.org/10.6028/NIST.FIPS.186-4
  SIGNING_KEY_SPEC_EC_P256 = 2;

  // Elliptic Curve Key from the NIST P-384 curve (aka secp384r1)
  // as defined in https://doi.org/10.6028/NIST.FIPS.186-4
  SIGNING_KEY_SPEC_EC_P384 = 3;

  // Elliptic Curve Key from SECG P256k1 curve (aka secp256k1)
  // commonly used in bitcoin and ethereum
  // as defined in https://www.secg.org/sec2-v2.pdf
  SIGNING_KEY_SPEC_EC_SECP256K1 = 4;
}
```

The synchronizer the participant node intends to connect to might restrict further the list of supported key specifications. To obtain this information from the synchronizer directly, run the following command on the synchronizer Public API.

```
grpcurl -d '{}' &lt;sequencer_endpoint&gt; com.digitalasset.canton.sequencer.api.v30.SequencerConnectService/GetSynchronizerParameters
```

If a console is not accessible, you can use either a bootstrap script or `grpccurl` against the Admin API to invoke the commands.

#### 3. Share Public Key of Node with Offline Site

Next, the intermediate public key must be transported to the offline site as described above. Ensure that the public key is not tampered with during transport.

#### 4. Generate Root Key and The Root Certificate

##### Using OpenSSL

Ensure that the necessary scripts are available on the secure site. These scripts are included in the Canton release packages at `scripts/offline-root-key`. An example demonstrating usage of those scripts using `openssl` to generate keys and sign certificates is available at `examples/10-offline-root-namespace-init`. Run the next set of commands from the `examples/10-offline-root-namespace-init` directory.

Start by initializing variables used in the snippets below

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Points to the location of the offline root key scripts under the scripts/offline-root-key directory in the release artifact
SCRIPTS_ROOT="$(dirname "$0")/../../scripts/offline-root-key"
PRIVATE_KEY="$OUTPUT_DIR/root_private_key.der"
PUBLIC_KEY="$OUTPUT_DIR/root_public_key.der"
ROOT_NAMESPACE_PREFIX="$OUTPUT_DIR/root_namespace"
INTERMEDIATE_NAMESPACE_PREFIX="$OUTPUT_DIR/intermediate_namespace"
```

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
mkdir -p tmp/certs
OUTPUT_DIR="tmp/certs"
CANTON_NAMESPACE_DELEGATION_PUB_KEY=<Path to the intermediate key downloaded from Canton. ``intermediateKeyPath`` in this example>
```

As well as setting the path to the protobuf image containing the required protobuf definitions to generate certificates.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
CURRENT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" > /dev/null && pwd)
export BUF_PROTO_IMAGE="$CURRENT_DIR/../../scripts/offline-root-key/root_namespace_buf_image.json.gz"
source "$CURRENT_DIR/../../scripts/offline-root-key/utils.sh"
```

Then, generate the root key in the secure environment and extract the public key:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl ecparam -name prime256v1 -genkey -noout -outform DER -out "$PRIVATE_KEY"
openssl ec -inform der -in "$PRIVATE_KEY" -pubout -outform der -out "$PUBLIC_KEY" 2> /dev/null
```

Then, create the self-signed root namespace delegation, which is effectively a self-signed certificate used as the trust anchor of the given namespace:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/prepare-certs.sh" --root-delegation --root-pub-key "$PUBLIC_KEY" --target-pub-key "$PUBLIC_KEY" --output "$ROOT_NAMESPACE_PREFIX"
```

Note that the root public key must be in the `x509 SPKI DER` format. For more information on Canton's supported key formats, please refer to the following tables. This generates two files, `root-delegation.prep` and `root-delegation.hash`. `.prep` files contain unsigned topology transactions serialized to bytes. If you really want to be sure what you are signing, inspect the `prepare-certs.sh` script to see how it generates the topology transaction and how it computes the hash. Next, the hash needs to be signed.

If you are using openssl, the following command can be used to sign the hash:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "$PRIVATE_KEY" -keyform DER -sign < "$ROOT_NAMESPACE_PREFIX.hash" > "$ROOT_NAMESPACE_PREFIX.signature"
```

Finally, assemble the signature and the prepared transaction. For more information on the supported signature formats, please refer to the following table:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/assemble-cert.sh" --prepared-transaction "$ROOT_NAMESPACE_PREFIX.prep" --signature "$ROOT_NAMESPACE_PREFIX.signature" --signature-algorithm ecdsa256 --output "$ROOT_NAMESPACE_PREFIX.cert"
```

This creates a so-called signed topology transaction.

##### Using GCP KMS

If you are using GCP KMS, you can use KMS CLI ([https://cloud.google.com/kms/docs/create-validate-signatures](https://cloud.google.com/kms/docs/create-validate-signatures)) with the following commands to generate the key:

```
gcloud kms keyrings create key-ring --location location (APPROXIMATE)
```

And the following command can be used to generate the signature:

```
gcloud kms asymmetric-sign \
    --version key-version \
    --key &lt;root-key&gt; \
    --keyring key-ring \
    --location location \
    --digest-algorithm digest-algorithm \
    --input-file root-delegation.prep \
    --signature-file root-delegation.signature
```

#### 5. Create the Intermediate Certificate

If the root key and the self-signed root delegation are available, you can create the intermediate certificate. The steps are very similar to the root certificate, but the target is the public key of the intermediate key, and the `--intermediate-delegation` flag is used instead of `--root-delegation`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/prepare-certs.sh" --intermediate-delegation --root-pub-key "$PUBLIC_KEY" --canton-target-pub-key "$CANTON_NAMESPACE_DELEGATION_PUB_KEY" --output "$INTERMEDIATE_NAMESPACE_PREFIX"
```

Verify that the generated topology transaction (printed to stdout) is correct and refers to the correct keys. Once verified, the generated hash needs to be signed:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "$PRIVATE_KEY" -keyform DER -sign < "$INTERMEDIATE_NAMESPACE_PREFIX.hash" > "$INTERMEDIATE_NAMESPACE_PREFIX.signature"
```

Again, the signature and the prepared transaction can be assembled:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/assemble-cert.sh" --prepared-transaction "$INTERMEDIATE_NAMESPACE_PREFIX.prep" --signature "$INTERMEDIATE_NAMESPACE_PREFIX.signature" --signature-algorithm ecdsa256 --output "$INTERMEDIATE_NAMESPACE_PREFIX.cert"
```

#### 7. Copy the Certificates to the Online Site

The generated certificates (never the root private key) need to be transferred to the online site. The public keys are included in the certificates and don't need to be transported separately. You need to transfer both certificates, the root delegation and the intermediate delegation, to the online site.

#### 8. Import the Certificates to the Node

On the target site, import the certificates into the waiting node using the console command

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.init_id(identifier = "participant1", delegationFiles = Seq("/tmp/canton/certs/root_namespace.cert", "/tmp/canton/certs/intermediate_namespace.cert"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res5: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::1220e5af5c84328a08bbaf051a1a00ec514755465a66e5a03e78b6c0ba11fe3a4362
    Uptime: 0.119182s
    Ports: 
    	ledger: 33078
    	admin: 33079
    Connected synchronizers: None
    Unhealthy synchronizers: None
    Active: true
    Components: 
    	memory_storage : Ok()
    	connected-synchronizer : Not Initialized
    	sync-ephemeral-state : Not Initialized
    	sequencer-client : Not Initialized
    	acs-commitment-processor : Not Initialized
    Version: 3.6.0-SNAPSHOT
    Supported protocol version(s): 35, dev
```

Alternatively, the Admin API can be used directly via `grpccurl` to initialize the node.

### Pre-Generated Certificates

The certificates can also be provided directly via the node's configuration file if they've been generated beforehand. In this scenario, instead of generating the intermediate key via the node's `generate_signing_key` command as described above, they key must be generated on a KMS and its public key material downloaded. The same scripts can then be used to generate the certificate, with the exception that the intermediate public key will not be in the Canton format but in a DER format and should therefore be set with `--target-pub-key`. Once the certificates are available, you must register the intermediate KMS key by running:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val intermediateKey = node.keys.secret
  .register_kms_signing_key(
    intermediateNsKmsKeyId,
    SigningKeyUsage.NamespaceOnly,
    name = s"${node.name}-${SigningKeyUsage.Namespace.identifier}",
  )
// user-manual-entry-begin: ManualRegisterKmsNamespaceKey
node.crypto.cryptoPrivateStore
  .existsPrivateKey(intermediateKey.id, Signing)
  .valueOrFail("intermediate key not registered")
  .futureValueUS

// user-manual-entry-begin: ManualRegisterKmsKeys

// Register the KMS signing key used to define the node identity.
val namespaceKey = node.keys.secret
  .register_kms_signing_key(
    namespaceKmsKeyId,
    SigningKeyUsage.NamespaceOnly,
    name = s"${node.name}-${SigningKeyUsage.Namespace.identifier}",
  )

// Register the KMS signing key used to authenticate the node toward the Sequencer.
val sequencerAuthKey = node.keys.secret
  .register_kms_signing_key(
    sequencerAuthKmsKeyId,
    SigningKeyUsage.SequencerAuthenticationOnly,
    name = s"${node.name}-${SigningKeyUsage.SequencerAuthentication.identifier}",
  )

// Register the signing key used to sign protocol messages.
val signingKey = node.keys.secret
  .register_kms_signing_key(
    signingKmsKeyId,
    SigningKeyUsage.ProtocolOnly,
    name = s"${node.name}-${SigningKeyUsage.Protocol.identifier}",
  )

// Register the encryption key.
val encryptionKey = node.keys.secret
  .register_kms_encryption_key(encryptionKmsKeyId, name = node.name + "-encryption")

// user-manual-entry-end: ManualRegisterKmsKeys

(namespaceKey, sequencerAuthKey, signingKey, encryptionKey)
} else {
// architecture-handbook-entry-begin: ManualInitKeys

// Create a signing key used to define the node identity.
val namespaceKey =
  node.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Namespace.identifier}",
      SigningKeyUsage.NamespaceOnly,
    )

// Create a signing key used to authenticate the node toward the Sequencer.
val sequencerAuthKey =
  node.keys.secret.generate_signing_key(
    name = node.name + s"-${SigningKeyUsage.SequencerAuthentication.identifier}",
    SigningKeyUsage.SequencerAuthenticationOnly,
  )

// Create a signing key used to sign protocol messages.
val signingKey =
  node.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Protocol.identifier}",
      SigningKeyUsage.ProtocolOnly,
    )

// Create the encryption key.
val encryptionKey =
  node.keys.secret.generate_encryption_key(name = node.name + "-encryption")

// architecture-handbook-entry-end: ManualInitKeys

(namespaceKey, sequencerAuthKey, signingKey, encryptionKey)
}

// architecture-handbook-entry-begin: ManualInitNode

// Use the fingerprint of this key for the node identity.
val namespace = Namespace(namespaceKey.id)
node.topology.init_id_from_uid(
UniqueIdentifier.tryCreate("manual-" + node.name, namespace)
)

// Wait until the node is ready to receive the node identity.
node.health.wait_for_ready_for_node_topology()

// Create the self-signed root certificate.
node.topology.namespace_delegations.propose_delegation(
namespace,
namespaceKey,
CanSignAllMappings,
)

// Assign the new keys to this node.
node.topology.owner_to_key_mappings.propose(
member = node.id.member,
keys = NonEmpty(Seq, sequencerAuthKey, signingKey, encryptionKey),
signedBy = Seq(namespaceKey.fingerprint, sequencerAuthKey.fingerprint, signingKey.fingerprint),
)

// architecture-handbook-entry-end: ManualInitNode

}

}
```

and then import the certificates to the node.

This configuration directive has no effect once the node is initialized and can subsequently be removed.

### Delegation Restrictions

You can further restrict the kind of topology transactions a delegation can authorize. The `prepare-certs` script exposes a `--delegation-restrictions` flag for that purpose.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"$SCRIPTS_ROOT/prepare-certs.sh" --delegation-restrictions PARTY_TO_PARTICIPANT,PARTY_TO_KEY_MAPPING --root-pub-key "$PUBLIC_KEY" --canton-target-pub-key "$CANTON_RESTRICTED_PUB_KEY" --output "$RESTRICTED_KEY_NAMESPACE_PREFIX"
```

The delegation can then be signed and assembled as before. Once the signed certificate is available, load it onto the node:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.topology.transactions.load_single_from_file(s"$opensslKeysDirectory/restricted_key_namespace.cert", TopologyStoreId.Authorized)
```

### Rotate the Intermediate Key

#### Create new Intermediate Key

In order to create another intermediate key, we follow the same steps as before. Create the key on the online site and export it.

Follow the same steps to create a new intermediate delegation for the new intermediate key:

* copy to secure site
* generate the intermediate delegation (skip self-signed root delegation as it has already been generated)
* copy the certificate to the node site

The new intermediate delegation can then be imported into the node as shown here.

Once the new delegation has been imported, the old intermediate key can be revoked.

#### Revoking the Intermediate Key

To revoke the intermediate key, the root key needs to be used to sign a revocation transaction. The revocation transaction is prepared in the same way as the intermediate delegation. Also, the generated hash needs to be signed and then subsequently assembled into a certificate:

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
./prepare-cert.sh --delegation-restrictions PARTY_TO_PARTICIPANT,PARTY_TO_KEY_MAPPING --root-pub-key "/tmp/canton/certs/root_public_key.der" --canton-target-pub-key "/tmp/canton/certs/restricted_key.pub" --output "/tmp/canton/certs/restricted_key_namespace"
```

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
openssl pkeyutl -rawin -inkey "/tmp/canton/certs/root_private_key.der" -keyform DER -sign -in "/tmp/canton/certs/restricted_key_namespace.hash" -out "/tmp/canton/certs/restricted_key_namespace.signature"
```

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
./assemble-cert.sh --prepared-transaction "/tmp/canton/certs/restricted_key_namespace.prep" --signature "/tmp/canton/certs/restricted_key_namespace.signature" --signature-algorithm "ed25519" --output "/tmp/canton/certs/restricted_key_namespace"
```

On the node site, the revocation certificate can be imported using:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.transactions.load_single_from_file("/tmp/canton/certs/restricted_key_namespace.cert", TopologyStoreId.Authorized)
```

#### Rotating the Root Namespace Key

You cannot rotate the root namespace key. If you need to discontinue the usage of the namespace, you need to create a new namespace, new parties and participants in that new namespace, and transfer the contracts to the new parties.

{/* COPIED_END */}

## Configure session keys

Canton uses session keys to reduce expensive cryptographic operations during protocol execution, improving performance. There are two types: session encryption keys, which reduce the number of asymmetric encryptions, and session signing keys, which help avoid frequent calls to external signers such as a KMS.

You can read more about the rationale and security considerations in [Cryptographic keys in Canton](/overview/learn/cryptographic-keys).

Extending the lifetime of session keys minimizes the need for repeated key negotiation or remote signing—but it also increases the window during which keys are stored in memory, raising the risk of compromise.

### Increase session **encryption** keys lifetime

You can control how long a session encryption key remains active by adjusting the `expire-after-timeout` values in your configuration. To globally increase the lifetime of session encryption keys, increase the `expire-after-timeout` for both the `sender-cache` and `receiver-cache`.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1 {
    caching {
        session-encryption-key-cache {
            # these are the default values
            enabled = true
            sender-cache {
                maximum-size = 10000
                expire-after-timeout = 10s
            }
            receiver-cache {
                maximum-size = 10000
                expire-after-timeout = 10s
            }
        }
    }
}
```

### Increase session **signing** keys lifetime

When using external KMS (Key Management Service) provider you can control how long a session signing key remains active by adjusting the `key-validity-duration` and the `key-eviction-period`. The `key-eviction-period` should always be longer than the `key-validity-duration` and at least as long as the sum of `confirmation_response_timeout` and `mediator_reaction_timeout`, as configured in the dynamic Synchronizer parameters.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.kms {
  session-signing-keys {
    # these are the default values
    enabled = true
    key-validity-duration = 5m
    cut-off-duration = 30s,
    key-eviction-period = 10m,
    signing-algorithm-spec = ed-25519,
    signing-key-spec = ec-curve-25519,
  }
}
```

{/* COPIED_END */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
