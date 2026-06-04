---
title: "Canton KMS Operations"
slug: "global-synchronizer-production-operations-kms-operations"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/kms-operations.md"
source_title: "Canton KMS Operations"
tags:
  - global-synchronizer
  - production-operations
  - kms-operations
---

# Canton KMS Operations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton KMS Operations

> Configure and operate a KMS for Canton: AWS, GCP, driver-based; mode selection, migration, and key rotation.

# Key management service (KMS) configuration

By default Canton keys are generated in the node and stored in the node's primary storage. We currently support a version of Canton that can use a KMS to either: (a) protect Canton's private keys at rest or (b) protect the private keys both at rest and at use by storing the keys in the KMS.

Throughout these sections, we will sometimes refer to option (a) as **envelope encryption**, and option (b) as **external keys**.

You can find more background information on this key management feature in Secure cryptographic private key storage. See Protect private keys with envelope encryption and a Key Management Service if you want to know how Canton can protect private keys while they remain internally stored in Canton using a KMS, or Externalize private keys with a Key Management Service for more details on how Canton can enable private keys to be generated and stored by an external KMS.

The following sections focus on how to set up a Participant Node to run with a KMS; however, most configurations also apply to Sequencer and Mediator.

1. Configure a KMS

   We currently support three alternatives:

   1. AWS KMS\*
   2. GCP KMS\*
   3. Driver(-based) KMS allows users to integrate their own KMS provider by implementing the necessary hooks using Canton’s KMS Driver API. More information on how to implement a Canton KMS Driver can be found in the Canton KMS Driver developer guide.

<p style={{fontSize: "smaller", fontStyle: "italic"}}>\* only available in the Enterprise Edition.</p>

2. Select the mode of operation

   You can choose between:

   1. Enable encrypted private key storage with KMS – sometimes referred to as *envelope encryption*, protects Canton’s private keys only at rest.
   2. Enable external key storage with a KMS – sometimes referred to as *external KMS keys*, private keys are generated and stored entirely within a KMS.

3. Migrate to a KMS

   How to migrate between a non-KMS and a KMS node, and vice-versa.

4. Rotate keys with a KMS

   How to rotate existing KMS-managed keys using Canton console commands.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/configuration/kms_configuration.rst" hash="3c286d0d" */}

# Configure a KMS

This section explains how to configure a Key Management System (KMS) in Canton.

Currently, three KMS alternatives are available:

* AWS KMS\*
* GCP KMS\*
* Driver(-based) KMS allows users to integrate their own KMS provider by implementing the necessary hooks using Canton’s KMS Driver API. Learn more about how to implement a Canton KMS Driver in the Canton KMS Driver developer guide.

<p style={{fontSize: "smaller", fontStyle: "italic"}}>\* only available in the Enterprise Edition.</p>

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/mode/kms_mode.rst" hash="82b212ee" */}

# Select a KMS mode of operation

Canton supports using a Key Management Service (KMS) to increase the security of stored private keys. For Canton to actually use a KMS, you need to decide and configure one of the **two independent ways** to use this service:

1. Enable encrypted private key storage

   In this mode, Canton generates the private keys internally, and the KMS is used only to protect those keys at rest (i.e., the keys are encrypted before being stored in Canton’s database). This offers an additional layer of security without requiring external key generation.

2. Enable external key storage

   In this mode, the private keys are generated and stored entirely within the KMS. Canton never sees the raw private key material and interacts with the KMS only to perform cryptographic operations.

<Note>
  Throughout this documentation, these modes might be referred to as **envelope encryption** and **external keys**, respectively.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/mode/encrypted_key_storage.rst" hash="9b3e7c0c" */}

# Enable encrypted private key storage with a KMS

Canton can use a KMS to encrypt private keys at rest (envelope encryption):

1. Private keys are stored encrypted in the node's database.
2. On startup, the KMS decrypts them for in-memory use.

This improves security with no runtime performance impact. See Protect private keys with envelope encryption and a Key Management Service for details.

<Note>
  This assumes the KMS provider has already been configured. See Configure a KMS.
</Note>

## Enable envelope encryption

Envelope encryption is a common approach chosen by KMS vendors that uses a symmetric encryption key, called the **wrapper key**, to encrypt and decrypt the stored, private keys.

To enable encrypted private key storage with a KMS using envelope encryption, we must add the following configuration and restart the node.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.private-key-store.encryption.type = kms
```

Both new and existing nodes (including Participants) can be configured to use this feature.

**In both cases, keys are stored encrypted in the Canton node's database.**

<Warning>
  Restoring from a database backup requires access to the wrapper keys used during the encryption of the data in the backup. Deleting the wrapper keys renders the backup unusable.
</Warning>

## Manually generate a wrapper key

By default, a new symmetric wrapper key is automatically generated by Canton after the node restarts. If you want to use a pre-generated wrapper key, you must first create a new wrapper key in the KMS and record its identifier, taking into account the following requirements.

### AWS KMS wrapper key requirements

<div className="enterprise-only" />

Supported values for identifying the wrapper key:

* Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
* Key ARN (Amazon Resource Name): `arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab`
* Key alias: `alias/test-key`

Note that if you are using an existing key, it must be a symmetric key using the correct scheme. In AWS KMS, this means:

* Key specification: SYMMETRIC\_DEFAULT
* Key usage: ENCRYPT\_DECRYPT

### GCP KMS wrapper key requirements

<div className="enterprise-only" />

Supported values for identifying the wrapper key:

* Key name: `test-key`
* Key Resource Name (RN): `projects/gcp-kms-testing/locations/us-east1/keyRings/canton-test-keys/cryptoKeys/test-key/cryptoKeyVersions/1`

Note that if you are using an existing key, it must be created with the following attributes:

* Key algorithm: `GOOGLE_SYMMETRIC_ENCRYPTION`
* Key purpose: `ENCRYPT_DECRYPT`

### KMS Driver key requirements

The way keys are uniquely identified is left to the driver implementation. However, the following constraints must be observed:

* Keys must be **128-bit** in length and usable with the **AES-GCM** crypto scheme.

### Add new wrapper key to configuration

With the key created and its ID in hand, you must explicitly add the ID to the configuration using:

<div id="wrapper_key_config">
  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.crypto.private-key-store.encryption.wrapper-key-id = alias/canton-kms-test-key
  ```
</div>

An example configuration that puts together both AWS KMS and envelope encryption with a manually generated wrapper key is shown below:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
_shared_aws {
  # Configure an AWS KMS
  crypto {
    kms {
      type = aws
      region = us-east-1
      multi-region-key = false
      audit-logging = false
    }

    # Configure an encrypted store with KMS
    private-key-store {
      encryption.type = kms
      # In this example we are using the same wrapper key for all nodes. This is not recommended and you should
      # either let Canton generate those keys or choose a different one for each node.
      encryption.wrapper-key-id = alias/canton-kms-test-key
    }
  }
}
```

After subsequent restarts the operator does not need to specify the identifier for the wrapper key; Canton stores the wrapper key ID in the database.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/mode/external_key_storage.rst" hash="32773506" */}

# Enable external key storage with a KMS

This section shows how to enable external key storage for a Canton Participant, so that private keys are stored and managed by a KMS, and all cryptographic operations using those keys must go through the KMS.

<Note>
  This assumes the KMS provider has already been configured. See Configure a KMS.
</Note>

To enable external key storage and usage, apply the configuration below before the initial bootstrap of a new Participant node. **If you're updating an existing Participant, you must instead follow the migration guide:** Migrate to external key storage with a KMS.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.provider = kms
```

A complete example configuration that puts together both AWS KMS configuration and external key storage configuration is shown below:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.provider = kms
canton.participants.participant1.crypto.kms {
    type = aws
    region = us-east-1
    multi-region-key = false # optional, default is false
    audit-logging = true # optional, default is false
}
```

The same configuration is applicable for all KMS types, by selecting the correct `type` (AWS, GCP or Driver).

This configuration tells Canton that we want to use external keys in a KMS, which are **automatically created by default when a Participant starts — no further action is required.** Read on if you prefer to use your own manually generated keys that are already stored in the KMS.

## Run with manually-generated keys

This howto shows how to configure a participant node with keys that are generated manually in the KMS and not rely on automatic key generation by Canton

The first step is to manually generate new keys for the Participant in your KMS. All the necessary keys are listed below and include:

* a (signing) namespace key;
* a protocol signing key;
* a sequencer authentication key;
* an asymmetric encryption key;

Generate each key in your KMS with a supported key algorithm and purpose as shown in Table Key configuration for external keys and record the generated keys identifier.

To be able to use these keys, you must configure manual initialization in the Participant. This is explained in detail in Initialize node identity manually. However, it is important to note that contrary to what is described there, the keys are expected to be registered, not generated. Each key must be assigned the correct usage (see Signing Key Usage).

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
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
```

where `xyzKmsKeyId` is the KMS key identifier for a specific key (e.g. `KMS Key ARN`).

<Note>
  When using AWS cross account keys the key ID can't be used, use the key `ARN` instead.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/configuration/kms_aws_config.rst" hash="a785a56a" */}

# Configure a Amazon Web Services (AWS) KMS

<div className="enterprise-only" />

Like other Canton capabilities, AWS KMS configuration is enabled within a Canton node's configuration file. A KMS for AWS is configured as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.kms {
    type = aws
    region = us-east-1
    multi-region-key = false # optional, default is false
    audit-logging = false # optional, default is false
}
```

* `type` specifies which KMS to use.
* `region` specifies which region the AWS KMS is bound to.
* `multi-region-key` flag enables the replication of keys generated by the AWS KMS. With replication turned on, the operator can replicate a key from one region to another (Note: replication of a key is not done automatically by Canton) and change the region configured in Canton at a later point in time without any other key rotation required. **The standard single-region approach is applicable for most scenarios**.
* `audit-logging` flag enables logging of every call made to the AWS KMS.

## Configure AWS credentials and permissions

To make the API calls to the AWS KMS, Canton uses the standard AWS credential access. For example, the standard environment variables of `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` can be used. Alternatively, you can specify an AWS profile file (e.g. use a temporary access profile credentials - `sts`).

The protection and rotation of the credentials for AWS are the responsibility of the node operator.

The authorized actions, such as IAM permissions, required for AWS KMS depend on the selected mode of operation in Canton.

### Permissions for envelope encryption

The following IAM permissions are required when using **envelope encryption**:

* `kms:CreateKey`
* `kms:Encrypt`
* `kms:Decrypt`
* `kms:DescribeKey`

<Note>
  If you use cross-account keys, you do **not** need the `kms:CreateKey` permission.
</Note>

### Permissions for external KMS

The following IAM permissions are required when using an **external KMS**, where keys are fully managed and used directly from AWS KMS:

* `kms:CreateKey`
* `kms:TagResource`
* `kms:Decrypt`
* `kms:Sign`
* `kms:DescribeKey`
* `kms:GetPublicKey`

<Note>
  If you use cross-account keys, you do **not** need the `kms:CreateKey` and `kms:TagResource` permissions.
</Note>

## Auditability

AWS provides tools to monitor KMS keys. For AWS to set automatic external logging, refer to the AWS official documentation. This includes instructions on how to set AWS Cloud Trail or Cloud Watch Alarms to keep track of usage of KMS keys or of performed crypto operations. Canton logs errors resulting from the use of KMS keys.

## Logging

For further auditability, Canton can be configured to log every call made to the AWS KMS. To enable this feature, set the `audit-logging` field of the KMS configuration to `true`. By default, when using a file-based logging configuration, such logs are written into the main Canton log file. To write them to a dedicated log file, set the `KMS_LOG_FILE_NAME` environment variable or `--kms-log-file-name` CLI flag to the path of the file. These and other parameters can be configured using environment variables or CLI flags:

| Environment variable             | CLI Flag                       | Purpose                                                                      | Default           |
| -------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- | ----------------- |
| KMS\_LOG\_FILE\_NAME             | --kms-log-file-name            | Path to a dedicated KMS log file                                             | not set           |
| KMS\_LOG\_IMMEDIATE\_FLUSH       | --kms-log-immediate-flush      | When true, logs will be immediately flushed to the KMS log file              | true              |
| KMS\_LOG\_FILE\_ROLLING\_PATTERN | --kms-log-file-rolling-pattern | Pattern to use when using the rolling file strategy to roll KMS log files    | yyyy-MM-dd        |
| KMS\_LOG\_FILE\_HISTORY          | --kms-log-file-history         | Maximum number of KMS log files to keep when using the rolling file strategy | 0 (i.e. no limit) |

KMS logging configuration

Sample of an AWS KMS audit log:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
2023-09-12 15:44:54,426 [env-execution-context-27] INFO  c.d.c.c.k.a.a.AwsRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Sending request [06cc259e220da647]: DecryptRequest(CiphertextBlob=** Ciphertext placeholder **, KeyId=91c48ce4-ec80-44c1-a219-fdd07f12f002, EncryptionAlgorithm=RSAES_OAEP_SHA_256) to https://kms.us-east-1.amazonaws.com/
2023-09-12 15:44:54,538 [aws-java-sdk-NettyEventLoop-1-15] INFO  c.d.c.c.k.a.a.AwsRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Received response [06cc259e220da647]: [Aws-Id: 1836823c-bb8a-44bf-883d-f33d696bf84f] - DecryptResponse(Plaintext=** Redacted plaintext placeholder **, KeyId=arn:aws:kms:us-east-1:724647588434:key/91c48ce4-ec80-44c1-a219-fdd07f12f002, EncryptionAlgorithm=RSAES_OAEP_SHA_256)
2023-09-12 15:44:54,441 [env-execution-context-138] INFO  c.d.c.c.k.a.a.AwsRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Sending request [e28450df3a98ea23]: SignRequest(KeyId=f23b5b37-b4e8-494d-b2bc-1fca12308c99, Message=** Sign message text placeholder **, MessageType=RAW, SigningAlgorithm=ECDSA_SHA_256) to https://kms.us-east-1.amazonaws.com/
2023-09-12 15:44:54,554 [aws-java-sdk-NettyEventLoop-1-2] INFO  c.d.c.c.k.a.a.AwsRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Received response [e28450df3a98ea23]: [Aws-Id: 7085bcf3-1a36-4048-a38b-014b441afa11] - SignResponse(KeyId=arn:aws:kms:us-east-1:724647588434:key/f23b5b37-b4e8-494d-b2bc-1fca12308c99, Signature=** Signature message text placeholder **, SigningAlgorithm=ECDSA_SHA_256)
```

Note that sensitive data is removed before logging. The general log format is as follows:

`tid:<canton_trace_id> - Sending request [<canton_kms_request_id>]: <request details>` `tid:<canton_trace_id> - Received response [<canton_kms_request_id>]: [Aws-Id: <aws_request_id>] - <response details>`

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/configuration/kms_gcp_config.rst" hash="b03c88a5" */}

# Configure a Google Cloud Provider (GCP) KMS

<div className="enterprise-only" />

Like other Canton capabilities, GCP KMS configuration is enabled within a Canton node's configuration file. A KMS for GCP is configured in the following way:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant2.crypto.kms {
    type = gcp
    location-id = us-east1
    project-id = gcp-kms-testing
    key-ring-id = canton-test-keys-2023
    audit-logging = false # optional, default is false
}
```

* `type` specifies which KMS to use.
* `location-id` specifies which region the GCP KMS is bound to.
* `project-id` specifies which project are we binding to.
* `key-ring-id` specifies the keyring to use. Multi region keys are enabled for an entire keyring. Therefore, the KMS operator is responsible for setting the keyring correctly depending on the systems' needs.
* `audit-logging` flag that enables logging of every call made to the GCP KMS

## Configure GCP credentials and permissions

For GCP, Canton uses a GCP service account. For example, the standard environment variable `GOOGLE_APPLICATION_CREDENTIALS` can be used after setting up a local Application Default Credentials (ADC) file for the service account. For supported environments, e.g. GKE, Canton can pick up credentials from the metadata service Application Default Credentials.

The protection and rotation of the credentials for GCP are the responsibility of the node operator.

The authorized actions, such as IAM permissions, required for GCP KMS depend on the selected mode of operation in Canton.

### Permissions for envelope encryption

The following IAM permissions are required when using **envelope encryption**:

* `cloudkms.cryptoKeyVersions.create`
* `cloudkms.cryptoKeyVersions.useToEncrypt`
* `cloudkms.cryptoKeyVersions.useToDecrypt`
* `cloudkms.cryptoKeys.get`

<Note>
  If you use cross-project keys, you do **not** need the `cloudkms.cryptoKeyVersions.create` permission.
</Note>

### Permissions for external KMS

The following IAM permissions are required when using an **external KMS**, where keys are fully managed and used directly from GCP KMS:

* `cloudkms.cryptoKeyVersions.create`
* `cloudkms.cryptoKeyVersions.useToDecrypt`
* `cloudkms.cryptoKeyVersions.useToSign`
* `cloudkms.cryptoKeyVersions.get`
* `cloudkms.cryptoKeyVersions.viewPublicKey`

<Note>
  If you use cross-project keys, you do **not** need the `cloudkms.cryptoKeyVersions.create` permission.
</Note>

## Auditability

GCP provides tools to monitor KMS keys. For GCP logging information you can refer to the GCP official documentation. Canton logs errors resulting from the use of KMS keys.

## Logging

For further auditability, Canton can be configured to log every call made to the GCP KMS. To enable this feature, set the `audit-logging` field of the KMS configuration to `true`. By default, when using a file-based logging configuration, such logs are written into the main Canton log file. To write them to a dedicated log file, set the `KMS_LOG_FILE_NAME` environment variable or `--kms-log-file-name` CLI flag to the path of the file. These and other parameters can be configured using environment variables or CLI flags:

| Environment variable             | CLI Flag                       | Purpose                                                                      | Default           |
| -------------------------------- | ------------------------------ | ---------------------------------------------------------------------------- | ----------------- |
| KMS\_LOG\_FILE\_NAME             | --kms-log-file-name            | Path to a dedicated KMS log file                                             | not set           |
| KMS\_LOG\_IMMEDIATE\_FLUSH       | --kms-log-immediate-flush      | When true, logs will be immediately flushed to the KMS log file              | true              |
| KMS\_LOG\_FILE\_ROLLING\_PATTERN | --kms-log-file-rolling-pattern | Pattern to use when using the rolling file strategy to roll KMS log files    | yyyy-MM-dd        |
| KMS\_LOG\_FILE\_HISTORY          | --kms-log-file-history         | Maximum number of KMS log files to keep when using the rolling file strategy | 0 (i.e. no limit) |

KMS logging configuration

Sample of a GCP KMS audit log:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
2023-09-12 15:44:54,426 [env-execution-context-27] INFO  c.d.c.c.k.g.a.GcpRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Sending request [67d92ffb-438b-4dd5-8175-7a54ced7ac3a]: DecryptRequest(CiphertextBlob=** Ciphertext placeholder **, KeyId=canton-kms-test-key, EncryptionAlgorithm=RSAES_OAEP_SHA_256).
2023-09-12 15:44:54,538 [env-execution-context-32] INFO  c.d.c.c.k.g.a.GcpRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Received response DecryptResponse(Plaintext=** Redacted plaintext placeholder **, KeyId=canton-kms-test-key, EncryptionAlgorithm=RSAES_OAEP_SHA_256). Original request [67d92ffb-438b-4dd5-8175-7a54ced7ac3a]
2023-09-12 15:44:54,441 [env-execution-context-138] INFO  c.d.c.c.k.g.a.GcpRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Sending request [b3aa6202-1734-4751-8ae0-55b7d15c2abb]: SignRequest(KeyId=canton-kms-test-key, Message=** Sign message text placeholder **, MessageType=RAW, SigningAlgorithm=ECDSA_SHA_256).
2023-09-12 15:44:54,554 [env-execution-context-145] INFO  c.d.c.c.k.g.a.GcpRequestResponseLogger:participant=participant1 tid:40d47592f1bd50f37e6804fbdff404dd - Received response SignResponse(KeyId=canton-kms-test-key, Signature=** Signature message text placeholder **, SigningAlgorithm=ECDSA_SHA_256). Original request [b3aa6202-1734-4751-8ae0-55b7d15c2abb]
```

Note that sensitive data is removed before logging. The general log format is as follows:

`tid:<canton_trace_id> - Sending request [<canton_kms_request_id>]: <request details>` `tid:<canton_trace_id> - Received response <response details>. Original request [<canton_kms_request_id>]`

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/configuration/kms_driver_config.rst" hash="2ea5fd56" */}

# Configure a Driver-based KMS

Canton allows integration with a variety of KMS and HSM solutions through a KMS Driver. This approach enables you to connect Canton to an external key manager by building your own integration layer.

Configuring Canton to run with a KMS Driver is done similarly to other KMS providers by specifying:

```
type = driver
name = <name_of_driver>
```

For example, for a Participant named \`participant1\`:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.provider = kms
canton.participants.participant1.crypto.kms {
  type = driver
  name = "aws-kms"
    config = {
      region = us-east-1
      multi-region-key = false
      audit-logging = true
    }
}
```

* `type` specifies which KMS to use; in this case, a driver.
* `name` is a uniquely identifying name configured for the driver.
* KMS driver-specific configuration can be passed in through the `config` field.

In addition to this configuration, you must also provide a `.jar` file that implements the required API and acts as the bridge between Canton and the target KMS.

Run Canton with your driver `.jar` on its class path:

`java -cp driver.jar:canton.jar com.digitalasset.canton.CantonEnterpriseApp -c canton.conf # further canton arguments`

For guidance on developing and deploying your own KMS Driver in Canton, refer to the Canton KMS Driver developer guide. This guide includes instructions for building a custom driver, details on the necessary APIs, and steps to configure Canton to use the driver.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/migration/kms_migration.rst" hash="024d318f" */}

# Migrate to a KMS

This section outlines the steps required to migrate from a running non-KMS participant to one that is KMS-enabled, as well as the interoperability between nodes that use KMS and those that do not. The migration procedure depends on the selected mode of operation:

1. Migrate to encrypted private key storage with a Key Management Service (KMS)

   This process requires configuring the node to use a symmetric wrapper key. **Migration is done automatically after this configuration step.**

2. Migrate to external key storage with a Key Management Service (KMS)

   This approach involves creating a new KMS-enabled Participant and transferring all data (e.g., contracts) from the Participant node. **The process must be performed manually by each operator using the provided scripts and functions.**

   It offers a clean and self-contained transition but requires a namespace change and coordination with all affected Participant node operators.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/migration/encrypted_key_storage_migration.rst" hash="81793b9d" */}

# Migrate to encrypted private key storage with KMS

To migrate from a non-encrypted key storage to an encrypted private key storage using a KMS with an externally hosted symmetric wrapper key, you only need to configure a Participant (or any other node) to operate in this mode, as explained here. The process is seamless — after restarting the Participant, the new configuration is picked up and Canton's private keys are automatically encrypted and stored.

## Revert encrypted private key storage

Encrypted private key storage can be reverted back to unencrypted storage. To prevent accidental reverts, simply deleting the `private-key-store` configuration does **not** revert to unencrypted storage. Instead, the following configuration must be added, and the node restarted:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.crypto.private-key-store.encryption.reverted = true # default is false
```

<Warning>
  This forces Canton to decrypt its private keys and store them in clear; it is not recommended.
</Warning>

Encrypted private key storage can be enabled again by deleting the `reverted` field and reconfiguring the KMS.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/migration/external_key_storage_migration.rst" hash="00f0a330" */}

# Migrate to external key storage with a KMS

After creating a new Participant with the right configuration that connects to a KMS-compatible Synchronizer (e.g. running KMS or JCE with KMS-supported encryption and signing keys), you must transfer all parties, active contracts and DARs from the old Participant to the new one. The identities of the two Participants are different so you need to rewrite your contracts to refer to the new party ids. With this method, you can easily migrate your old Participant that runs an older protocol version to a new Participant with KMS enabled, that can run a more recent protocol version. Furthermore, you do not need to safe-keep the old node's root namespace key, because your Participant namespace changes. However, for it to work a single operator must control all the contracts or all Participant operators have to agree on this rewrite.

<Warning>
  This only works for a single operator or if all other Participant operators agree and follow the same steps.
</Warning>

First, you must recreate all parties of the old Participant in the new Participant, keeping the same display name, but resulting in different ids due to the new namespace key:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/security/kms/KmsMigrationWithNewNamespaceIntegrationTest.scala language: scala start-after: user-manual-entry-begin: KmsRecreatePartiesInNewParticipantNewNs end-before: user-manual-entry-end: KmsRecreatePartiesInNewParticipantNewNs dedent:
</div>

Secondly, you should migrate your DARs to the new Participant:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/security/kms/KmsMigrationWithNewNamespaceIntegrationTest.scala language: scala start-after: user-manual-entry-begin: KmsMigrateDarsNewNs end-before: user-manual-entry-end: KmsMigrateDarsNewNs dedent:
</div>

Finally, you need to transfer the active contracts of all the parties from the old Participant to the new one and rewrite the party ids mentioned in those contracts to match the new party ids. You can then connect to the new Synchronizer:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/security/kms/KmsMigrationWithNewNamespaceIntegrationTest.scala language: scala start-after: user-manual-entry-begin: KmsMigrateACSofPartiesNewNs end-before: user-manual-entry-end: KmsMigrateACSofPartiesNewNs dedent:
</div>

The result is a new Participant node, in a different namespace, with its keys stored and managed by a KMS connected to a Synchronizer that can communicate using the appropriate cryptographic schemes.

You need to follow the same steps if you want to migrate a Participant back to using a `non-KMS` provider.

## Interoperability with other nodes

By default, Canton nodes use the `jce` crypto provider, which is compatible with other nodes that use external KMS providers to store Canton private keys. If you change the default `jce` provider and use different cryptographic schemes, you must ensure that it supports the same algorithms and key schemes as the KMS providers, in order to interoperate with other KMS-enabled Canton nodes.

See the [Supported Cryptographic Schemes](/docs/canton/global-synchronizer-reference-crypto-schemes) reference for a description of the cryptographic schemes supported by a KMS provider and the ones used by default.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/key_rotation/kms_key_rotation.rst" hash="8b47170c" */}

# Rotate keys with KMS

Canton supports both rotating the wrapper key when using envelope encryption, and rotating Canton keys stored externally in a KMS.

For smooth disaster recovery, key rotation must be interleaved with backups as described under Backup and Restore.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/key_rotation/rotate_wrapper_key.rst" hash="dcb0594c" */}

# Rotate the envelope wrapper key

Some KMS providers (e.g., AWS) offer automatic rotation of symmetric KMS keys (typically yearly). Canton extends this by allowing node administrators to manually rotate the KMS wrapper key.

<Note>
  You can change the key specification (e.g., enabling multi-region in AWS) during rotation by updating the configuration before rotating the wrapper key.
</Note>

Key rotation does not delete the previous key. While the old key becomes inactive, it is still persisted. To permanently delete the previous key, see Delete Canton node keys.

## Rotate with an auto-generated key

Use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.keys.secret.rotate_wrapper_key()
```

Canton will automatically create a new wrapper key using the configured KMS.

## Rotate with a manually generated key

First, you must create a new wrapper key in your KMS that meets the requirements described here. Afterwards, you can rotate to that key using the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.keys.secret.rotate_wrapper_key(newWrapperKeyId)
```

* \`newWrapperKeyId\`: the identifier of the wrapper key you want to rotate to.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/secure/kms/key_rotation/rotate_external_keys.rst" hash="f1a0d457" */}

# Rotate external KMS keys

Canton keys can still be manually rotated even if they are externally stored in a KMS. To do that, you can use the standard rotate key commands, or **if you already have a pre-generated KMS key to rotate to**, run the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val newSigningKeyParticipant = participant1.keys.secret
  .rotate_kms_node_key(
    keyFingerprint,
    newKmsKeyId,
    "kms_key_rotated",
  )
```

* `fingerprint` - the fingerprint of the key we want to rotate.
* `newKmsKeyId` - the id of the new KMS key (e.g. Resource Name).
* `name` - an optional name for the new key.

No current KMS service offers automatic rotation of asymmetric keys so the node operator needs to be responsible for periodically rotating these keys.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
