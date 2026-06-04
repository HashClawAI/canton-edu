---
title: "Advanced Operations"
slug: "global-synchronizer-canton-console-advanced-operations"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/advanced-operations.md"
source_title: "Advanced Operations"
tags:
  - global-synchronizer
  - canton-console
  - advanced-operations
---

# Advanced Operations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Operations

> Advanced Canton console operations for experienced operators

This page covers advanced console operations: topology management, key rotation, and repair procedures. These operations go beyond day-to-day administration and typically require a deeper understanding of Canton's internal state.

## Topology management

Canton uses a topology state to track the mapping between parties, participants, synchronizers, and cryptographic keys. You can inspect and modify this state through the console.

### Inspecting topology state

List the current topology transactions for a participant:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.transactions.list()
    res1: com.digitalasset.canton.topology.store.StoredTopologyTransactions[TopologyChangeOp, TopologyMapping] = Seq(
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            NamespaceDelegation(
              namespace = 12201ff69b1d...,
              target = SigningPublicKey(
                id = 12201ff69b1d...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = namespace
              ),
              restriction = none
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:252f433640a0...
          ),
          signatures = 12201ff69b1d...
        ),
        sequenced = 2026-05-04T17:56:08.399704Z,
        validFrom = 2026-05-04T17:56:08.399704Z
      ),
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            OwnerToKeyMapping(
              member = PAR::participant1::12201ff69b1d...,
              signingKeys = Seq(12202ac7545b..., 122044fb1b35...),
              encryptionKeys = 1220f78c3e7e...
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:5486c1b52e15...
          ),
          signatures = Seq(12201ff69b1d..., 12202ac7545b..., 122044fb1b35...)
        ),
        sequenced = 2026-05-04T17:56:08.409867Z,
        validFrom = 2026-05-04T17:56:08.409867Z
      ),
      StoredTopologyTransaction(
        SignedTopologyTransaction(
          TopologyTransaction(
            SynchronizerTrustCertificate(
              participantId = PAR::participant1::12201ff69b1d...,
              synchronizerId = da::122032922613...
            ),
            serial = 1,
            operation = Replace,
            hash = SHA-256:b82608aa35af...
          ),
          signatures = 12201ff69b1d...
        ),
        sequenced = 2026-05-04T17:56:13.194363Z,
        validFrom = 2026-05-04T17:56:13.194363Z
      )
    )
```

To filter for a specific type of topology mapping:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list(synchronizerId)
    res2: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult] = Vector(
      ListPartyToParticipantResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:56:24.441742Z,
          validUntil = None,
          sequenced = 2026-05-04T17:56:24.191742Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:6882f6f9ceea...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant1::12201ff69b1d... -> Submission
        )
      )
    )
```

This shows which parties are hosted on which participants, along with their permission levels (Observation, Confirmation, or Submission).

### Party-to-participant mappings

Each party is associated with one or more participants through a party-to-participant mapping. You can inspect these mappings to verify hosting configuration:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list(synchronizerId = synchronizerId, filterParty = "Alice")
    res3: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult] = Vector(
      ListPartyToParticipantResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:56:24.441742Z,
          validUntil = None,
          sequenced = 2026-05-04T17:56:24.191742Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:6882f6f9ceea...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant1::12201ff69b1d... -> Submission
        )
      )
    )
```

The output includes the permission granted to each participant for the party. The three permission levels are:

* **Observation** -- read-only visibility of contracts involving the party
* **Confirmation** -- the participant can confirm transactions on behalf of the party
* **Submission** -- the participant can submit commands for the party (local parties only)

<Note>
  The term "domain" appears in some older console commands and configuration keys. Canton has deprecated "domain" in favor of "synchronizer." If you encounter `domain` in command names or output, treat it as equivalent to `synchronizer`.
</Note>

### Modifying topology state

Adding a new party to a participant:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceParty = participant1.parties.enable("Alice")
    aliceParty : PartyId = Alice::12201ff69b1d...
```

For more complex topology changes -- such as adjusting confirmation thresholds or adding hosting participants -- you work with the topology management commands:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.propose(party = aliceParty, newParticipants = Seq((participant2.id, ParticipantPermission.Observation)))
    res5: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = PAR::participant2::1220a4d7463b... -> Observation
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:9360f5c90483...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

Topology changes propagate through the synchronizer's topology protocol. There is a built-in delay between when a topology change is proposed and when it becomes effective. This delay is configurable at the synchronizer level and exists to prevent rapid, potentially harmful changes.

## Key management and rotation

Canton nodes use cryptographic keys for signing and encryption. Over time, you may need to rotate keys for security hygiene or in response to a suspected compromise.

### Listing keys

View the keys currently registered on a participant:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.keys.secret.list()
    res6: Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata] = Vector(
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12201ff69b1d...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          name = Some(KeyName(participant1-namespace))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 122044fb1b35...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(signing, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-signing))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = SigningPublicKeyWithName(
          publicKey = SigningPublicKey(
            id = 12202ac7545b...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = Set(sequencer-auth, proof-of-ownership)
          ),
          name = Some(KeyName(participant1-sequencer-auth))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      ),
      PrivateKeyMetadata(
        publicKeyWithName = EncryptionPublicKeyWithName(
          publicKey = EncryptionPublicKey(
            id = 1220f78c3e7e...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-P256
          ),
          name = Some(KeyName(participant1-encryption))
        ),
        wrapperKeyId = None,
        kmsKeyId = None
      )
    )
```

This shows key fingerprints, purposes (signing or encryption), and the key scheme.

### Generating new keys

Generate a new signing key:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newKey = participant1.keys.secret.generate_signing_key(name = "new-signing-key", usage = SigningKeyUsage.All)
    newKey : SigningPublicKey = SigningPublicKey(
      id = 122006262a3e...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(namespace, sequencer-auth, signing, proof-of-ownership)
    )
```

Generate a new encryption key:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newEncKey = participant1.keys.secret.generate_encryption_key(name = "new-encryption-key")
    newEncKey : EncryptionPublicKey = EncryptionPublicKey(
      id = 12209242c045...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-P256
    )
```

### Key rotation

Rotating a key involves generating a new key, authorizing it through a topology transaction, and then revoking the old key. The specific steps depend on the key's purpose:

1. Generate a new key (see above).
2. Authorize the new key in the topology state by proposing the updated mapping.
3. Wait for the topology change to become effective.
4. Verify that the node operates correctly with the new key.
5. Revoke the old key only after confirming the new key works.

<Warning>
  Do not revoke the old key before the new key is fully propagated and operational. Premature revocation can lock you out of your node.
</Warning>

### Exporting and importing keys

For backup or migration purposes:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Export secret keys to a directory
participant1.keys.secret.download("backup/keys/")

// Import keys from a backup
participant1.keys.secret.upload("backup/keys/my-key.bin")
```

If your deployment uses an external Key Management Service (KMS), key material is managed through the KMS rather than through local export/import. Both GCP and AWS KMS drivers are available in the community edition.

## Repair operations

<Warning>
  Repair operations are powerful but dangerous. They can cause permanent data corruption if used incorrectly. You should only use repair commands with guidance from Digital Asset technical support.

  These commands are documented here for completeness, but they are not intended for unsupervised use.
</Warning>

### Enabling repair commands

Repair commands are disabled by default. To enable them, add the following to your configuration:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.features.enable-preview-commands = yes
canton.features.enable-repair-commands = yes
```

Restart the node after making this change. When you are done with the repair, remove these settings and restart again to prevent accidental misuse.

### When repair is needed

Canton is designed to self-heal. Database outages, network interruptions, and similar infrastructure problems are handled automatically through retries and reconnection. Manual repair is a last resort for situations where automatic recovery cannot resolve the issue -- typically corruption of the active contract set (ACS) or inability to process sequenced events.

The general categories of repair scenarios are:

* **ACS inconsistencies** between participants that share contracts, caused by an infrastructure failure that led to divergent state
* **Blocked synchronizer connections** where a participant cannot process events from a synchronizer and crashes on reconnection
* **Lost synchronizer recovery** where a synchronizer is permanently unavailable and contracts need to be migrated

### Repair toolbox

The available repair operations include:

* **Adding or purging contracts** from the ACS to fix inconsistencies between participants
* **Ignoring faulty events** to unblock a participant that is stuck processing a corrupted event
* **Migrating contracts** from a lost synchronizer to a new one
* **Exporting and importing** identity state, topology transactions, and DARs for full node rehydration

### Repair macros

<Note>
  Repair macros are an advanced topic. They combine multiple repair commands into a single operation and are designed for use under the direction of technical support during incident recovery.
</Note>

Some repair operations are packaged as macros -- sequences of individual repair commands combined into a single console call. These macros handle common recovery scenarios such as cloning a node's identity state for rehydration.

For example, the identity download/upload macro exports a participant's topology state, identity, and (if not using KMS) secret keys to disk, allowing you to restore the participant from a clean database:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Download identity state
repair.identity.download(participant1, "backup/identity/")

// After database reset, upload identity state
repair.identity.upload(participant1, "backup/identity/")
```

### Coordinating multi-participant repair

When ACS inconsistencies affect multiple participants, the operators of all affected participants need to agree on which contracts to add or remove. This coordination is essential -- unilateral changes by one operator can make the inconsistency worse.

The typical process is:

1. Identify the inconsistency by examining ACS commitment mismatches in the logs (look for `ACS_COMMITMENT_MISMATCH` errors).
2. Agree with other affected operators on the target state.
3. Apply the agreed-upon additions and removals on each participant.
4. Verify that ACS commitments match after the repair.

Detailed procedures for specific repair scenarios are available in the Canton operations documentation. In all cases, work with technical support rather than attempting repair independently.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
