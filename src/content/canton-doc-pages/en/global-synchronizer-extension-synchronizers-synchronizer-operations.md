---
title: "Synchronizer Operations"
slug: "global-synchronizer-extension-synchronizers-synchronizer-operations"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/synchronizer-operations.md"
source_title: "Synchronizer Operations"
tags:
  - global-synchronizer
  - extension-synchronizers
  - synchronizer-operations
---

# Synchronizer Operations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Synchronizer Operations

> Bootstrap, configure, and operate Canton synchronizer nodes.

# Bootstrap a Synchronizer

This howto assumes familiarity with general Synchronizer concepts. Refer to the Canton overview for more information.

## Set up a centralized Synchronizer

In a **centralized** Synchronizer, the operator has access to all Sequencer and Mediator nodes.

A centralized Synchronizer is the simplest to set up and manage, but it assumes that a single fully trusted entity owns and operates the Synchronizer.

You can bootstrap a centralized Synchronizer by specifying a single owner and a `synchronizerThreshold` of 1. This respectively means that only that owner can authorize topology changes on the Synchronizer, and that one signature is sufficient for that.

First, make sure that the nodes are fresh and haven't yet been initialized:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.initialized()
    res1: Boolean = false
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.initialized()
    res2: Boolean = false
```

Now you can initialize the centralized Synchronizer as follows:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ bootstrap.synchronizer(
      synchronizerName = "mySynchronizer",
      sequencers = Seq(sequencer1),
      mediators = Seq(mediator1),
      synchronizerOwners = Seq(sequencer1),
      synchronizerThreshold = 1,
      staticSynchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer),
    )
    res3: PhysicalSynchronizerId = mySynchronizer::122032922613...::35-0
```

Instead of using the defaults, you can customize the static Synchronizer parameters. Refer to the parameters configuration section for more information about which static Synchronizer parameters are available and their value.

Now a Participant Node can connect to the Synchronizer via a Sequencer. Check that the Participant Node can use the Synchronizer through a `ping` command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1)
    res5: Duration = 4661 milliseconds
```

## Set up a decentralized Synchronizer

This subsection covers the most frequent case where distinct operators manage **decentralized** Synchronizer nodes on behalf of the respective owners. This also means that they're managed from separate console environments.

In this case, the bootstrapping process must be coordinated in lockstep between the Synchronizer nodes, with the coordination and exchange of data happening through secure communication channels.

As an overview, to bootstrap a decentralized Synchronizer with separate consoles, operators:

1. Fix the initial parameters.
2. Exchange Synchronizer identities.
3. Collectively create a decentralized namespace (see the Canton overview for more information); each operator:
   1. Signs the bootstrapping topology transactions.
   2. Exchanges the bootstrapping topology transactions with other operators.
   3. Initializes their Synchronizer nodes.

This how-to uses two Sequencer nodes and two Mediator nodes. The Sequencer nodes are Synchronizer owners and are managed by distinct operators on behalf of the respective entities.

This diagram illustrates the exchange of information between the operators:

<div style={{background: "#ffffff", padding: "1rem", borderRadius: "0.5rem", display: "inline-block", width: "80%"}}>
  <img src="https://mintcdn.com/cantonfoundation/QAGFSphBsRkeZIBi/images/docs_website/decentralized-synchronizer-bootstrap-data-exchange.png?fit=max&auto=format&n=QAGFSphBsRkeZIBi&q=85&s=c56d172bd4ddb3e7441e84214215cd9e" alt="Sequence diagram of information exchange between Synchronizer operators during decentralized bootstrap" style={{width: "100%", display: "block"}} width="671" height="391" data-path="images/docs_website/decentralized-synchronizer-bootstrap-data-exchange.png" />
</div>

<Note>
  Before proceeding, ensure that all of the nodes in the decentralized Synchronizer are started.
</Note>

All Synchronizer owners must agree on the static Synchronizer parameters in advance. You can achieve that, for example, by exporting and sharing a file containing their definition:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer)
    synchronizerParameters : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ synchronizerParameters.writeToFile("tmp/synchronizer-bootstrapping-files/params.proto")
```

Now create temporary topology stores to bootstrap the Synchronizer's topology in both Sequencers' consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Id = sequencer1.id
    sequencer1Id : SequencerId = SEQ::sequencer1::1220cb0a22fb...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1TempStore = sequencer1.topology.stores.create_temporary_topology_store("sequencer1-synchronizer-setup", synchronizerParameters.protocolVersion)
    sequencer1TempStore : TopologyStoreId.Temporary = Temporary(name = String185(str = "sequencer1-synchronizer-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Id = sequencer2.id
    sequencer2Id : SequencerId = SEQ::sequencer2::12203a55a279...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2TempStore = sequencer2.topology.stores.create_temporary_topology_store("sequencer2-synchronizer-setup", synchronizerParameters.protocolVersion)
    sequencer2TempStore : TopologyStoreId.Temporary = Temporary(name = String185(str = "sequencer2-synchronizer-setup"))
```

Export the Sequencer and Mediator identities from both Sequencers' consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator2.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto")
```

Import the node identities into the respective temporary topology stores from the respective consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto", sequencer2TempStore)
```

Propose and export the decentralized namespace declaration with the first Sequencer's signature:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq1DND = sequencer1.topology.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer1TempStore,
      )
    seq1DND : SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq1DND.writeToFile("tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = SynchronizerId(UniqueIdentifier.tryCreate("mySynchronizer", seq1DND.mapping.namespace.toProtoPrimitive))
    synchronizerId : SynchronizerId = mySynchronizer::12209266a807...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val physicalSynchronizerId = PhysicalSynchronizerId(synchronizerId, synchronizerParameters.toInternal)
    physicalSynchronizerId : PhysicalSynchronizerId = mySynchronizer::12209266a807...::35-0
```

On the second Sequencer's console, load the first Sequencer's decentralized namespace declaration, sign it, and share it again:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.load_single_from_file(
        "tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq2DND = sequencer2.topology.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer2TempStore,
      )
    seq2DND : SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 12203a55a279...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq2DND.writeToFile("tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto")
```

Generate the Synchronizer bootstrap transactions with the second Sequencer's signature and share them with the first Sequencer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerBootstrap =
        sequencer2.topology.synchronizer_bootstrap.download_genesis_topology(
          physicalSynchronizerId,
          synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
          sequencers = Seq(sequencer1Id, sequencer2Id),
          mediators = Seq(mediator1.id, mediator2.id),
          outputFile = "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
          store = sequencer2TempStore,
        )
```

On the first Sequencer's console, load the second Sequencer's decentralized namespace declaration and Synchronizer bootstrap transactions:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.load_single_from_file(
        "tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.load_multiple_from_file(
        "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

Still on the first Sequencer's console, generate and re-export the genesis topology. This also merges the signatures from both Sequencers:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.synchronizer_bootstrap.download_genesis_topology(
        physicalSynchronizerId,
        synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
        sequencers = Seq(sequencer1Id, sequencer2Id),
        mediators = Seq(mediator1.id, mediator2.id),
        outputFile = "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        store = sequencer1TempStore
      )
```

On the second Sequencer's console, load the first Sequencer's Synchronizer bootstrap transactions, which contain both Sequencers' signatures:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.load_multiple_from_file(
        "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

Bootstrap both Sequencers with the fully authorized initial topology snapshot from the respective consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer1.topology.transactions.export_topology_snapshot(store = sequencer1TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@79ade368 size=6293 contents="\n\2201\n\303\002\n\f\b\215\317\354\317\006\020\220\347\220\344\001\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParams = StaticSynchronizerParameters.tryReadFromFile("tmp/synchronizer-bootstrapping-files/params.proto")
    synchronizerParams : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res33: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer2.topology.transactions.export_topology_snapshot(store = sequencer2TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@70a7b5d8 size=6289 contents="\n\2141\n\303\002\n\f\b\215\317\354\317\006\020\250\373\260\357\002\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParams = StaticSynchronizerParameters.tryReadFromFile("tmp/synchronizer-bootstrapping-files/params.proto")
    synchronizerParams : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res36: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

Now that the Synchronizer has been successfully bootstrapped and the Sequencers initialized, remove the temporary topology stores:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.stores.drop_temporary_topology_store(sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.stores.drop_temporary_topology_store(sequencer2TempStore)
```

On both Sequencers' consoles, initialize the Mediators by connecting each of them to the associated Sequencer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator1.setup.assign(
        physicalSynchronizerId,
        SequencerConnections.single(sequencer1.sequencerConnection),
      )
      mediator1.health.wait_for_initialized()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator2.setup.assign(
        physicalSynchronizerId,
        SequencerConnections.single(sequencer2.sequencerConnection),
      )
      mediator2.health.wait_for_initialized()
```

Now the decentralized Synchronizer is completely initialized and a Participant Node is able to operate on this Synchronizer through its Sequencer connection:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.synchronizers.connect_local(sequencer2, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res43: Duration = 2295 milliseconds
```

## Set up a decentralized Synchronizer with a subset of Sequencers as owners

The previous subsection describes how to bootstrap a decentralized Synchronizer using multiple Sequencers that are all Synchronizer owners. This subsection describes how to bootstrap a decentralized Synchronizer using multiple Sequencers when only a subset of Sequencers are Synchronizer owners.

Similar to the previous subsection, distinct operators may manage different Synchronizer nodes from separate console environments. The bootstrapping process must be coordinated in lockstep between the Synchronizer nodes, with the coordination and exchange of data happening through secure communication channels.

This how-to uses four Sequencer nodes and two Mediator nodes. Only **two** of the Sequencer nodes (the first and second) are Synchronizer owners, and all four Sequencer nodes are managed by distinct operators. Although this how-to shares many bootstrapping commands in common with the previous subsection, there are subtle differences showing the commands that owner and non-owner Sequencer nodes should perform, respectively.

<Note>
  Before proceeding, ensure that all of the nodes in the decentralized Synchronizer are started.
</Note>

All Synchronizer owners must agree on the static Synchronizer parameters in advance. You can achieve that, for example, by exporting and sharing a file containing their definition:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer)
    synchronizerParameters : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ synchronizerParameters.writeToFile("tmp/synchronizer-bootstrapping-files/params.proto")
```

Now create temporary topology stores to bootstrap the Synchronizer's topology in all four Sequencer nodes' consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Id = sequencer1.id
    sequencer1Id : SequencerId = SEQ::sequencer1::1220cb0a22fb...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1TempStore = sequencer1.topology.stores.create_temporary_topology_store("sequencer1-synchronizer-setup", synchronizerParameters.protocolVersion)
    sequencer1TempStore : TopologyStoreId.Temporary = Temporary(name = String185(str = "sequencer1-synchronizer-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Id = sequencer2.id
    sequencer2Id : SequencerId = SEQ::sequencer2::12203a55a279...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2TempStore = sequencer2.topology.stores.create_temporary_topology_store("sequencer2-synchronizer-setup", synchronizerParameters.protocolVersion)
    sequencer2TempStore : TopologyStoreId.Temporary = Temporary(name = String185(str = "sequencer2-synchronizer-setup"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Id = sequencer3.id
    sequencer3Id : SequencerId = SEQ::sequencer3::122076e8bfb8...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer4Id = sequencer4.id
    sequencer4Id : SequencerId = SEQ::sequencer4::1220990c49ca...
```

Export the Sequencer and Mediator identities from all four Sequencer nodes' consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator2.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer3.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer3-identity.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer4.topology.transactions.export_identity_transactions("tmp/synchronizer-bootstrapping-files/sequencer4-identity.proto")
```

Import the node identities into the respective temporary topology stores from the respective consoles:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer3-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer4-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto", sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer2-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer3-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/sequencer4-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator1-identity.proto", sequencer2TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.import_topology_snapshot_from("tmp/synchronizer-bootstrapping-files/mediator2-identity.proto", sequencer2TempStore)
```

Propose and export the decentralized namespace declaration with the first Sequencer's signature:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq1DND = sequencer1.topology.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer1TempStore,
      )
    seq1DND : SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq1DND.writeToFile("tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = SynchronizerId(UniqueIdentifier.tryCreate("mySynchronizer", seq1DND.mapping.namespace.toProtoPrimitive))
    synchronizerId : SynchronizerId = mySynchronizer::12209266a807...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val physicalSynchronizerId = PhysicalSynchronizerId(synchronizerId, synchronizerParameters.toInternal)
    physicalSynchronizerId : PhysicalSynchronizerId = mySynchronizer::12209266a807...::35-0
```

On the second Sequencer's console, load the first Sequencer's decentralized namespace declaration, sign it, and share it again:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.load_single_from_file(
        "tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val seq2DND = sequencer2.topology.decentralized_namespaces.propose_new(
        owners = Set(sequencer1Id.namespace, sequencer2Id.namespace),
        threshold = PositiveInt.two,
        store = sequencer2TempStore,
      )
    seq2DND : SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          namespace = 12209266a807...,
          threshold = 2,
          owners = Seq(12203a55a279..., 1220cb0a22fb...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:baa5c4401f12...
      ),
      signatures = 12203a55a279...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ seq2DND.writeToFile("tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto")
```

Generate the Synchronizer bootstrap transactions with the second Sequencer's signature and share them with the first Sequencer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerBootstrap =
        sequencer2.topology.synchronizer_bootstrap.download_genesis_topology(
          physicalSynchronizerId,
          synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
          sequencers = Seq(sequencer1Id, sequencer2Id, sequencer3Id, sequencer4Id),
          mediators = Seq(mediator1.id, mediator2.id),
          outputFile = "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
          store = sequencer2TempStore,
        )
```

On the first Sequencer's console, load the second Sequencer's decentralized namespace declaration and Synchronizer bootstrap transactions:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.load_single_from_file(
        "tmp/synchronizer-bootstrapping-files/decentralized-namespace.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.transactions.load_multiple_from_file(
        "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        sequencer1TempStore,
        ForceFlag.AlienMember,
      )
```

Still on the first Sequencer's console, generate and re-export the genesis topology. This also merges the signatures from both Sequencers:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.synchronizer_bootstrap.download_genesis_topology(
        physicalSynchronizerId,
        synchronizerOwners = Seq(sequencer1Id, sequencer2Id),
        sequencers = Seq(sequencer1Id, sequencer2Id, sequencer3Id, sequencer4Id),
        mediators = Seq(mediator1.id, mediator2.id),
        outputFile = "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        store = sequencer1TempStore
      )
```

On the second Sequencer's console, load the first Sequencer's Synchronizer bootstrap transactions, which contain both Sequencers' signatures:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.transactions.load_multiple_from_file(
        "tmp/synchronizer-bootstrapping-files/synchronizer-bootstrap.proto",
        sequencer2TempStore,
        ForceFlag.AlienMember,
      )
```

Bootstrap all Sequencers with the fully authorized initial topology snapshot from the respective consoles. For the two Sequencers that are Synchronizer owners, the initial snapshot already exists locally in their respective temporary stores from the Synchronizer bootstrap process:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer1.topology.transactions.export_topology_snapshot(store = sequencer1TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@784b7f29 size=8481 contents="\n\234B\n\301\002\n\v\b\263\317\354\317\006\020\330\315\317n\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220c...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.write_to_file(initialSnapshot, "tmp/synchronizer-bootstrapping-files/initial-snapshot.proto")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParams = StaticSynchronizerParameters.tryReadFromFile("tmp/synchronizer-bootstrapping-files/params.proto")
    synchronizerParams : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res42: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = sequencer2.topology.transactions.export_topology_snapshot(store = sequencer2TempStore)
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@8eac748 size=8483 contents="\n\236B\n\303\002\n\f\b\263\317\354\317\006\020\330\250\376\227\002\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParams = StaticSynchronizerParameters.tryReadFromFile("tmp/synchronizer-bootstrapping-files/params.proto")
    synchronizerParams : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res45: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

For the non-owner Sequencers, externally share the initial topology snapshot to enable the *assign from genesis state* command. In this example, assume the first Sequencer externally shares the initial topology snapshot with the third and fourth Sequencers by sharing a written file:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val initialSnapshot = utils.read_byte_string_from_file("tmp/synchronizer-bootstrapping-files/initial-snapshot.proto")
    initialSnapshot : com.google.protobuf.ByteString = <ByteString@4fb0684b size=8481 contents="\n\234B\n\301\002\n\v\b\263\317\354\317\006\020\330\315\317n\032\244\002\n\237\002\n\215\001\n\210\001\b\001\020\001\032\201\001\n\177\nD1220c...">
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerParams = StaticSynchronizerParameters.tryReadFromFile("tmp/synchronizer-bootstrapping-files/params.proto")
    synchronizerParams : StaticSynchronizerParameters = StaticSynchronizerParameters(
      required signing specs = RequiredSigningSpecs(
        algorithms = Set(Ed25519, EC-DSA-SHA256, EC-DSA-SHA384),
        keys = Set(EC-Curve25519, EC-P256, EC-P384, EC-Secp256k1)
      ),
      required encryption specs = RequiredEncryptionSpecs(
        algorithms = Set(ECIES_HMAC256_AES128-CBC, RSA-OAEP-SHA256),
        keys = Set(EC-P256, RSA-2048)
      ),
      required symmetric key schemes = AES128-GCM,
      required hash algorithms = SHA-256,
      required crypto key formats = Set(
        Raw,
        DER-encoded X.509 SubjectPublicKeyInfo,
        DER-encoded PKCS #8 PrivateKeyInfo
      ),
      topology change delay = 0.25s,
      protocol version = 35,
      serial = 0
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer3.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res48: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer4.setup.assign_from_genesis_state(initialSnapshot, synchronizerParams)
    res49: com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse = InitializeSequencerResponse(replicated = true)
```

Now that the Synchronizer has been successfully bootstrapped and the Sequencers initialized, remove the temporary topology stores:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.stores.drop_temporary_topology_store(sequencer1TempStore)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer2.topology.stores.drop_temporary_topology_store(sequencer2TempStore)
```

On both Sequencer owners' consoles, initialize the Mediators by connecting each of them to the associated Sequencer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator1.setup.assign(
        physicalSynchronizerId,
        SequencerConnections.single(sequencer1.sequencerConnection),
      )
      mediator1.health.wait_for_initialized()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ 
      mediator2.setup.assign(
        physicalSynchronizerId,
        SequencerConnections.single(sequencer2.sequencerConnection),
      )
      mediator2.health.wait_for_initialized()
```

Now the decentralized Synchronizer is completely initialized and a Participant Node is able to operate on this Synchronizer through its Sequencer connection:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.synchronizers.connect_local(sequencer2, alias = "mySynchronizer")
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res56: Duration = 1972 milliseconds
```

## Bootstrap a permissioned Synchronizer

The first layer of Synchronizer security is restricting access to the Public API network endpoints of the Sequencers. This can be done using standard network tools such as firewall rules and virtual private networks.

Individual Synchronizers can be **open**, allowing any Participant with a connection to a Sequencer node to join and participate in the network, or **permissioned**, in which case the Synchronizer owners need to explicitly authorize a Participant before it can register with the Synchronizer and use it.

While the Canton architecture is designed to be resilient against malicious Participant Nodes, explicitly restricting which Participant Nodes can join the network constitutes an effective second line of defense.

This subsection explains how to make a decentralized Synchronizer permissioned. For simplicity, it assumes a single trusted operator accessing all nodes from a single console environment.

First, let all Synchronizer owners set the `onboardingRestriction` dynamic Synchronizer parameter to `RestrictedOpen`:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = sequencer1.synchronizer_id
    synchronizerId : SynchronizerId = mySynchronizer::1220a82692ab...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.synchronizer_parameters.propose_update(synchronizerId, _.update(onboardingRestriction = OnboardingRestriction.RestrictedOpen))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.synchronizer_parameters.propose_update(synchronizerId, _.update(onboardingRestriction = OnboardingRestriction.RestrictedOpen))
```

Now, when a Participant Node attempts to join the Synchronizer, it's rejected because it's unknown:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.register(sequencer1, alias = synchronizerName, manualConnect = true)
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:SynchronizerInstallationManual - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/INITIAL_ONBOARDING_ERROR(9,87b7eb17): Transport(Status{code=FAILED_PRECONDITION, description=Unable to register onboarding topology transactions, cause=null})
      Request: RegisterSynchronizer(SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'mySynchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(sequencerAlias = Sequencer 'sequence ...
      DecodedCantonError(
      code = 'INITIAL_ONBOARDING_ERROR',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "Transport(Status{code=FAILED_PRECONDITION, description=Unable to register onboarding topology transactions, cause=null})",
      traceId = '87b7eb177d91ea704571712f223280ce',
      context = Seq('participant=>participant1', 'test=>SynchronizerInstallationManual', 'synchronizer=>mySynchronizer')
    )
      Command ParticipantAdministration$synchronizers$.register invoked from cmd10000013.sc:1
```

To allow the Participant Node to join the Synchronizer, the Synchronizer owners must authorize it.

First, export the Participant Node's ID to a string:

Extract the ID of the Participant Node into a string:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val participantAsString = participant1.id.toProtoPrimitive
    participantAsString : String = "PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
```

Communicate this string to the Synchronizer owners, who import it as follows:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val participantIdFromString = ParticipantId.tryFromProtoPrimitive(participantAsString)
    participantIdFromString : ParticipantId = PAR::participant1::12201ff69b1d...
```

Let all Synchronizer owners authorize the Participant Node:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.participant_synchronizer_permissions.propose(synchronizerId, participantIdFromString, ParticipantPermission.Submission, store = Some(synchronizerId))
    res6: SignedTopologyTransaction[TopologyChangeOp, ParticipantSynchronizerPermission] = SignedTopologyTransaction(
      TopologyTransaction(
        ParticipantSynchronizerPermission(
          synchronizerId = mySynchronizer::1220a82692ab...,
          participantId = PAR::participant1::12201ff69b1d...,
          permission = Submission
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:0f3f9883b343...
      ),
      signatures = 1220cb0a22fb...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.participant_synchronizer_permissions.propose(synchronizerId, participantIdFromString, ParticipantPermission.Submission, store = Some(synchronizerId))
    res7: SignedTopologyTransaction[TopologyChangeOp, ParticipantSynchronizerPermission] = SignedTopologyTransaction(
      TopologyTransaction(
        ParticipantSynchronizerPermission(
          synchronizerId = mySynchronizer::1220a82692ab...,
          participantId = PAR::participant1::12201ff69b1d...,
          permission = Submission
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:0f3f9883b343...
      ),
      signatures = 122009299340...,
      proposal
    )
```

Check that the Participant Node isn't active yet:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.active(synchronizerName)
    res8: Boolean = false
```

When issuing the Participant Node Synchronizer permission for a given Participant Node, the Synchronizer owners declare that they agree that the Participant Node joins the Synchronizer. Inspect this declaration:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.participant_synchronizer_permissions.list(synchronizerId).map(_.item.permission)
    res9: Seq[ParticipantPermission] = Vector(Submission)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.participant_synchronizer_permissions.list(synchronizerId).map(_.item.permission)
    res10: Seq[ParticipantPermission] = Vector(Submission)
```

<Note>
  Propagating and processing topology proposals may require some time, so you may have to retry before the submission authorization is visible.
</Note>

To activate the Participant Node on the Synchronizer, register the signing keys and the "Synchronizer trust certificate" of the Participant Node (the Participant Node generates this certificate automatically and sends it to the Synchronizer during the initial handshake).

Trigger the handshake again by letting the Participant Node reconnect to the Synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.reconnect_all()
```

Now, check that the Participant Node is active:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.active(synchronizerName)
    res12: Boolean = true
```

You can also confirm that the Participant Node is active with:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.participant_synchronizer_states.active(synchronizerId, participantIdFromString)
    res13: Boolean = true
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.topology.participant_synchronizer_states.active(synchronizerId, participantIdFromString)
    res14: Boolean = true
```

Finally, check that the Participant Node is healthy and can use the Synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1)
    res15: Duration = 1057 milliseconds
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/operate/new_nodes.rst" hash="9f3029cf" */}

# Add New Nodes

## Add a new Sequencer to a distributed Synchronizer

You can either initialize Sequencers as part of the regular distributed synchronizer bootstrapping process, or dynamically add a new Sequencer at a later point as described in this section.

The reverse procedure is documented in the Sequencer decommissioning section.

### Database Sequencer

The Database Sequencer is currently unsupported.

### BFT Sequencer

1. Assuming that at least one existing Sequencer is accessible, prepare a new Sequencer and make sure it's running.

2. Run the following `bootstrap` command using instance references of the new Sequencer, the existing Sequencer, and the owners of the current Synchronizer:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > bootstrap
   >   .onboard_new_sequencer(
   >     synchronizerId.logical,
   >     newSequencerReference,
   >     existingSequencerReference,
   >     synchronizerOwners,
   >     // Avoid issues if things are slow
   >     customCommandTimeout = Some(config.NonNegativeDuration.tryFromDuration(2.minutes)),
   >     isBftSequencer = true,
   >   )
   > ```

3. Set up new connections in either or both directions for all Sequencers using the following commands:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > newSequencerReference.bft.add_peer_endpoint(existingSequencerEndpoint)
   > // existingSequencerReference.bft.add_peer_endpoint(newSequencerEndpoint) // Optional, one direction is enough
   > ```
   >
   > For the newly-onboarded Sequencer, the endpoints can be configured as part of the initial network.

4. Wait for the new Sequencer to get initialized:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > newSequencerReference.health.wait_for_initialized()
   > ```

At this point, other nodes should be able to connect to the new Sequencer. To avoid problems, the best practice is to wait at least for the "maximum decision duration" (the sum of the `participant_response_timeout` and `mediator_reaction_timeout` dynamic synchronizer parameters with a default of 30 seconds each) before connecting nodes to a newly-onboarded Sequencer.

If you encounter issues, refer to the troubleshooting guide.

<div className="todo" />

For details on the necessary admin commands, check the reference documentation.

### Use separate consoles

Similarly to initializing a distributed synchronizer with separate consoles, dynamically onboarding new Sequencers can be achieved in separate consoles as follows:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Third sequencer's console:
// * write file with identity topology transactions
{
  sequencer3.topology.transactions.export_identity_transactionsV2(identityFile)
}

// Fist and second sequencers' (i.e., owners) console:
// * load third sequencer's identity transactions
// * add the third sequencer to the sequencer synchronizer state
// * write the topology snapshot, sequencer snapshot and static synchronizer parameters to files
{
  // Store the third sequencer's identity topology transactions on the synchronizer
  sequencer1.topology.transactions
    .import_topology_snapshot_fromV2(identityFile, store = synchronizerId)
  sequencer2.topology.transactions
    .import_topology_snapshot_fromV2(identityFile, store = synchronizerId)

  // wait for the identity transactions to become effective
  sequencer1.topology.synchronisation.await_idle()
  sequencer2.topology.synchronisation.await_idle()

  // find the current sequencer synchronizer state
  val sequencerSynchronizerState =
    sequencer1.topology.sequencers
      .list(store = synchronizerId)
      .headOption
      .getOrElse(sys.error("Did not find sequencer synchronizer state on the synchronizer"))

  // add the third sequencer to the synchronizer state
  val threshold = sequencerSynchronizerState.item.threshold
  val activeSequencers = sequencerSynchronizerState.item.active :+ sequencer3.id
  val newSerial = Some(sequencerSynchronizerState.context.serial.increment)
  sequencer1.topology.sequencers.propose(
    synchronizerId,
    threshold,
    activeSequencers,
    serial = newSerial,
  )
  sequencer2.topology.sequencers.propose(
    synchronizerId,
    threshold,
    activeSequencers,
    serial = newSerial,
  )
  // wait for the topology change to be observed by the sequencer
  utils.retry_until_true(commandTimeouts.bounded) {
    sequencer1.topology.sequencers
      .list(sequencer1.synchronizer_id)
      .headOption
      .map(_.item.allSequencers.forgetNE)
      .getOrElse(Seq.empty)
      .contains(sequencer3.id)
  }

  // fetch the onboarding state and write it to a file
  val onboardingState = sequencer1.setup.onboarding_state_for_sequencer(sequencer3.id)
  utils.write_to_file(onboardingState, onboardingStateFile)
}

// Third sequencer's console:
// * read the onboarding state from file
// * initialize the third sequencer with the onboarding state
{
  val onboardingState = utils.read_byte_string_from_file(onboardingStateFile)
  sequencer3.setup.assign_from_onboarding_state(onboardingState)

  sequencer3.health.initialized() shouldBe true
}
```

## Add a new Mediator to a distributed Synchronizer

You can either initialize Mediators as part of the regular distributed synchronizer bootstrapping process, or dynamically add a new Mediator at a later point as described in this section.

1. Prepare a new Mediator node and make sure it's running.

2. Save the new Mediator's identity and load it to relevant Sequencers:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > val mediator2Identity = mediator2.topology.transactions.identity_transactions()
   > sequencer1.topology.transactions.load(
   >   mediator2Identity,
   >   store = synchronizer1Id,
   >   ForceFlag.AlienMember,
   > )
   > ```

3. Propose a new Mediator state with active Mediators including the newly-onboarding Mediator:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > sequencer1.topology.mediators.propose(
   >   synchronizer1Id,
   >   threshold = PositiveInt.one,
   >   active = Seq(mediator1.id, mediator2.id),
   >   group = NonNegativeInt.zero,
   > )
   > ```

4. Initialize the new Mediator:

   > ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
   > mediator2.setup.assign(
   >   synchronizer1Id,
   >   SequencerConnections.single(sequencer1.sequencerConnection),
   > )
   > mediator2.health.wait_for_initialized()
   > ```

The reverse procedure is documented in the Mediator decommissioning section.

<div className="todo" />

For details on the necessary admin commands, check the reference documentation.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/operate/dynamic_params.rst" hash="e8c87fd8" */}

# Manage dynamic Synchronizer parameters

<div id="dynamic_synchronizer_parameters">
  In addition to the static Synchronizer parameters that you specify during Synchronizer bootstrap, you can change some parameters at runtime ( while the Synchronizer is running); these are referred to as `dynamic synchronizer parameters`. When the Synchronizer is bootstrapped, the default values are used for the dynamic Synchronizer parameters.
</div>

## Get dynamic Synchronizer parameters

You can get the current parameters on a Synchronizer you are connected to using the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
myParticipant.topology.synchronizer_parameters.get_dynamic_synchronizer_parameters(
  synchronizerId
)
```

## Change dynamic Synchronizer parameters

<div id="change_dynamic_synchronizer_parameters">
  You can set several dynamic parameters at the same time:
</div>

<div className="todo" />

<div className="todo" />

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mySequencer.topology.synchronizer_parameters
  .propose_update(
    synchronizerId,
    _.update(
      confirmationResponseTimeout = 40.seconds,
      mediatorDeduplicationTimeout = 2.minutes,
      preparationTimeRecordTimeTolerance = 1.minute,
      mediatorReactionTimeout = 20.seconds,
      assignmentExclusivityTimeout = 1.second,
      reconciliationInterval = 5.seconds,
      confirmationRequestsMaxRate = 100,
      maxRequestSize = 100000,
      sequencerAggregateSubmissionTimeout = 5.minutes,
      trafficControl = Some(
        TrafficControlParameters(
          maxBaseTrafficAmount = NonNegativeLong.tryCreate(204800),
          readVsWriteScalingFactor = 200,
          maxBaseTrafficAccumulationDuration = 12.minutes,
          setBalanceRequestSubmissionWindowSize = 10.minutes,
          enforceRateLimiting = false,
          baseEventCost = NonNegativeLong.zero,
        )
      ),
    ),
  )

// For ledger time record time tolerance, use the dedicated set method
mySequencer.topology.synchronizer_parameters
  .set_ledger_time_record_time_tolerance(synchronizerId, 60.seconds)
```

<Note>
  When increasing `max request size`, the sequencer nodes need to be restarted for the new value to be taken into account.
</Note>

## Recover from too-small *max request size*

`MaxRequestSize` is a dynamic parameter. This parameter configures both the gRPC channel size on the Sequencer node and the maximum size that a Sequencer client is allowed to transfer.

If the parameter is set to a very small value (roughly under `30kb`), Canton can crash because all messages are rejected by the sequencer client or by the sequencer node. This cannot be corrected by setting a higher value within the console, because this change request needs to be sent via the sequencer and will also be rejected.

To recover from this crash, you need to configure `override-max-request-size` on both the Sequencer node and all Sequencer clients.

This means you need to modify both the Synchronizer and the Participant Node configuration as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    sequencer-client.override-max-request-size = 30000
  }
}
participants {
  participant1 {
    sequencer-client.override-max-request-size = 30000
  }
  participant2 {
    sequencer-client.override-max-request-size = 30000
  }
}
mediators {
  mediator1 {
    sequencer-client.override-max-request-size = 30000
  }
}
sequencers {
  sequencer1 {
    # overrides the maxRequestSize in bytes on the sequencer node
    public-api.override-max-request-size = 30000
  }
}
```

After the configuration is modified, disconnect all the Participant Nodes from the Synchronizer and then restart all nodes.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.all.synchronizers.disconnect(daName)
nodes.local.stop()
```

Then perform the restart:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
nodes.local.start()
participants.all.synchronizers.reconnect_all()
```

Once Canton has recovered, use the admin command to set the `maxRequestSize` value, then delete the added configuration in the previous step, and finally perform the restart again.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/operate/traffic.rst" hash="0308899a" */}

# Sequencer Traffic Management

<Note>
  Currently traffic management is supported only on Byzantine Fault Tolerant (BFT) Synchronizers.
</Note>

This page describes how to enable and configure traffic management on a Synchronizer, and how to inspect and manage the traffic balances of its members.

Inspecting how much traffic a Synchronizer member has from the member's perspective (for Participant Nodes and Mediator Nodes) is discussed in Manage Node traffic.

## Enable traffic management on a Synchronizer

Traffic management can be enabled or disabled on an existing Synchronizer via adjusting its dynamic synchronizer parameters. Please refer to the Change dynamic synchronizer parameters for more details.

First let's check the current traffic management status of a Synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.synchronizer_parameters.get_dynamic_synchronizer_parameters(sequencer1.synchronizer_id)
    res1: DynamicSynchronizerParameters = DynamicSynchronizerParameters(
      confirmation response timeout = 30s,
      mediator reaction timeout = 30s,
      assignment exclusivity timeout = 1m,
      ledger time record time tolerance = 1m,
      mediator deduplication timeout = 48h,
      reconciliation interval = 1m,
      confirmation requests max rate = 1000000,
      max request size = 10485760,
      sequencer aggregate submission timeout = 6m,
      ACS commitment catchup = AcsCommitmentsCatchUpParameters(
        catch up interval skip = 5,
        number of intervals to trigger catch up = 2
      ),
      participant synchronizer limits = ParticipantSynchronizerLimits(
        confirmation requests max rate = 1000000
      ),
      preparation time record time tolerance = 24h,
      onboarding restriction = UnrestrictedOpen
    )
```

If the field `trafficControl` of type `TrafficControlParameters` is not set (absent in the output above) or has `enforceRateLimiting` set to `false` then the traffic management is inactive.

To enable traffic management, you update the dynamic synchronizer parameters, setting the `TrafficControlParameters` with the `enforceRateLimiting = true` and specifying desired values for the other parameters documented in `configuration class Scaladoc reference`.

<Note>
  If you are using a Synchronizer with multiple owners, you need to ensure that the command to enable traffic management is submitted by at least the configured threshold of owners.
</Note>

Assuming `sequencer1` being the only synchronizer owner, run the following command to enable traffic management:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.canton.config.RequireTypes.{NonNegativeNumeric, PositiveNumeric}
  import com.digitalasset.canton.config.PositiveFiniteDuration
  import com.digitalasset.canton.admin.api.client.data.TrafficControlParameters
  val trafficControlParameters = TrafficControlParameters(
    enforceRateLimiting = true,
    maxBaseTrafficAmount = NonNegativeNumeric.tryCreate(20000L),
    readVsWriteScalingFactor = PositiveNumeric.tryCreate(200),
    maxBaseTrafficAccumulationDuration = PositiveFiniteDuration.ofSeconds(10L),
    setBalanceRequestSubmissionWindowSize = PositiveFiniteDuration.ofMinutes(5L),
    baseEventCost = NonNegativeNumeric.tryCreate(500L),
    freeConfirmationResponses = false,
  )
  sequencer1.topology.synchronizer_parameters.propose_update(
    synchronizerId = sequencer1.synchronizer_id,
    _.update(trafficControl = Some(trafficControlParameters)),
  )
```

Let's confirm that the traffic management is now enabled by checking the synchronizer parameters again:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.topology.synchronizer_parameters
  .get_dynamic_synchronizer_parameters(sequencer1.synchronizer_id)
    res3: DynamicSynchronizerParameters = DynamicSynchronizerParameters(
      confirmation response timeout = 30s,
      mediator reaction timeout = 30s,
      assignment exclusivity timeout = 1m,
      ledger time record time tolerance = 1m,
      mediator deduplication timeout = 48h,
      reconciliation interval = 1m,
      confirmation requests max rate = 1000000,
      max request size = 10485760,
      sequencer aggregate submission timeout = 6m,
      traffic control = TrafficControlParameters(
        max base traffic amount = 20000,
        read vs write scaling factor = 200,
        max base traffic accumulation duration = 10s,
        set balance request submission window size = 5m,
        enforce rate limiting = true,
        base event cost = 500,
        free confirmation responses = false
      ),
      ACS commitment catchup = AcsCommitmentsCatchUpParameters(
        catch up interval skip = 5,
        number of intervals to trigger catch up = 2
      ),
      participant synchronizer limits = ParticipantSynchronizerLimits(
        confirmation requests max rate = 1000000
      ),
      preparation time record time tolerance = 24h,
      onboarding restriction = UnrestrictedOpen
    )
```

Note the `traffic control` in the output above.

## Check the latest traffic balances of Synchronizer members

One can interactively inspect and modify the traffic balances of Synchronizer members using the Canton console commands under `sequencer.traffic_control`.

To inspect the traffic balances of all members of a Synchronizer, you can use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val allMembersTrafficState = sequencer1.traffic_control.traffic_state_of_all_members()
  allMembersTrafficState
    allMembersTrafficState : com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus = SequencerTrafficStatus(
      trafficStatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            availableTraffic = 20000
          )
        ),
        MED::mediator1::122009299340... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            availableTraffic = 20000
          )
        ),
        PAR::participant3::1220d6908163... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            availableTraffic = 20000
          )
        ),
        PAR::participant2::1220a4d7463b... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            availableTraffic = 20000
          )
        )
      )
    )
```

If you only want to check the traffic balance of a specific member, you can use:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.traffic_control.traffic_state_of_members(Seq(participant1))
    res5: com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus = SequencerTrafficStatus(
      trafficStatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:36.710049Z,
            availableTraffic = 20000
          )
        )
      )
    )
```

## Top up the traffic balance for a Synchronizer member

<Note>
  Traffic balance entitlements of members are decided by an external workflow and communicated via submitting the same traffic balance via one or multiple Sequencers.
</Note>

<Note>
  Top ups must be submitted by a quorum of Sequencers to become effective. This is configured by the `threshold` parameter of the `SequencerSynchronizerState` topology mapping.
</Note>

<div className="todo" />

Let's add some traffic for a member, for example, `participant1`. First we need to know the current `serial` (a per-member monotonically increasing `PositiveInt`), which corresponds to the last traffic balance top up for that member.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val nextSerial = allMembersTrafficState.trafficStates(participant1).serial
  .getOrElse(PositiveNumeric.tryCreate(1))
  .increment
    nextSerial : PositiveNumeric[Int] = PositiveNumeric(value = 2)
```

Now we can submit a command to increase the traffic balance for `participant1` by `newBalance`:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.traffic_control.set_traffic_balance(
    member = participant1,
    serial =  nextSerial,
    newBalance = NonNegativeNumeric.tryCreate(1000000L),
  )
```

Now the traffic balance for `participant1` has been updated. You can verify this by checking the traffic state again:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(
    sequencer1.traffic_control.traffic_state_of_members(Seq(participant1))
      .trafficStates(participant1)
      .serial
      .exists(_ >= nextSerial)
  )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val trafficStateBeforePing = sequencer1.traffic_control.traffic_state_of_members(Seq(participant1))
  trafficStateBeforePing
    trafficStateBeforePing : com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus = SequencerTrafficStatus(
      trafficStatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = TrafficState(
            extraTrafficLimit = 1000000,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:38.785734Z,
            serial = 2,
            availableTraffic = 1020000
          )
        )
      )
    )
```

Now let's run `ping` between participants and observe the traffic consumption:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant2)
    res10: Duration = 4511 milliseconds
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.health.ping(participant3)
    res11: Duration = 2843 milliseconds
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.traffic_control.traffic_state_of_all_members()
    res12: com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus = SequencerTrafficStatus(
      trafficStatesOrErrors = Map(
        PAR::participant1::12201ff69b1d... -> Right(
          value = TrafficState(
            extraTrafficLimit = 1000000,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 20000,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            serial = 2,
            availableTraffic = 1020000
          )
        ),
        MED::mediator1::122009299340... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 19351,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            availableTraffic = 19351
          )
        ),
        PAR::participant3::1220d6908163... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 16139,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            availableTraffic = 16139
          )
        ),
        PAR::participant2::1220a4d7463b... -> Right(
          value = TrafficState(
            extraTrafficLimit = 0,
            extraTrafficConsumed = 0,
            baseTrafficRemainder = 18160,
            lastConsumedCost = 0,
            timestamp = 2026-05-04T17:51:46.299586Z,
            availableTraffic = 18160
          )
        )
      )
    )
```

Observe the traffic balances for the Participants and the Mediator decrease.

For more information on traffic control and its configuration parameters, read the traffic control overview.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/operate/pruning.rst" hash="bb82d965" */}

# Synchronizer Pruning

## Prune the Mediator state

You can set up scheduled automatic pruning for each of your Mediators as explained here.

You can also directly prune the Mediator without using a schedule by calling the following command:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediator1.pruning.prune()
```

This operation prunes processed sequenced events and finalized confirmation response aggregations based on the configured default retention period.

This value is seven days by default; you can configure it as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
parameters {
  retention-period-defaults {
    mediator = "7 days"
  }
}
```

To choose another value, you can either change the config above or directly specify a retention period with the command `mediator.pruning.prune_with_retention_period` or even the exact timestamp to prune at, using `mediator.pruning.prune_at`.

## Prune the Sequencer state

You can prune the Sequencer by calling the following command:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val result = sequencer1.pruning.prune()
```

This command uses the configured Sequencer default retention period to compute the timestamp from which to prune sequenced events and returns a description of what was pruned.

This value is seven days by default; you can configure it as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
parameters {
  retention-period-defaults {
    sequencer = "7 days"
  }
}
```

Alternatively, you can directly specify a retention period with the command `sequencer.pruning.prune_with_retention_period` or even the exact timestamp to prune at, using `sequencer.pruning.prune_at`.

### Unblock pruning due to inactive sequencer members

All Sequencer clients, such as Participants or Mediators, periodically acknowledge the timestamp of the latest event they have received from the Sequencer. These acknowledgements, which all Sequencers can see, allow the Sequencers to compute the highest timestamp that all clients have achieved. This timestamp serves as a safe pruning point.

You can check the Sequencer pruning status as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val status = sequencer1.pruning.status()
```

The status contains the latest acknowledgement timestamp for all active clients, and you can check the computed safe pruning point by calling `status.safePruningTimestamp`. The Sequencer can only perform pruning earlier than that point. Otherwise, one or more clients would be unable to continue operation.

If a Sequencer client goes inactive for some time, then all Sequencers are blocked from pruning past this client's latest acknowledged timestamp. To unblock a Sequencer from pruning at more recent timestamps, either the client must come back and acknowledge newer events or you must disable that client on the Sequencer.

The Sequencer has force-prune commands. The difference between these and the regular prune commands is that the force-prune commands disable members that are preventing pruning from happening at the given timestamp.

You can force prune at a given timestamp as follows:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val result = sequencer1.pruning.force_prune_at(earliestAck, dryRun = false)
```

Setting `dryRun` to `true` produces a list of the clients that would be disabled, if any, as part of the operation, without actually performing the pruning. To perform the pruning operation, run it with `dryRun` set to `false`.

If you've identified a problematic client you don't need to serve, you can directly disable it by calling the repair command `repair.disable_member(client)`.

Note that when you disable a client on a Sequencer, this is a local operation; the client is still active on other Sequencers that have not performed the same operation.

### BFT Orderer Pruning

The BFT Orderer layer of the Sequencer is where distributed consensus on the order of transactions is reached across all Sequencer nodes. It has its own separate set of database tables and different considerations regarding pruning.

The BFT Orderer serves ordered events up to the Sequencer layer, which stores them and subsequently serves them to Sequencer clients. The BFT Orderer also needs to retain this data after it is served to the Sequencer layer, because it may need to assist other BFT Orderer nodes that are behind in catching up.

You must pick a pruning retention period long enough for BFT Orderer nodes to be able to catch up after crashing and coming back.

See below how to manually prune using an admin command and also check the status.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer1.bft.pruning.prune(retention = 30.days, minBlocksToKeep = 100)
val status = sequencer1.bft.pruning.status()
```

You can also set up scheduled automatic pruning for the BFT Orderer using the commands shown below as well as the ones explained here.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer1.bft.pruning.set_bft_schedule(
  cron = "0 0 8 ? * SAT",
  maxDuration = 8.hours,
  retention = 90.days,
  minBlocksToKeep = 50,
)
sequencer1.bft.pruning.set_min_blocks_to_keep(100)
val schedule = sequencer1.bft.pruning.get_bft_schedule()
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/operate/ha.rst" hash="711b141d" */}

# High Availability in Synchronizer

## Mediator

The mediator service uses a hot standby mechanism with an arbitrary number of replicas. During a mediator fail-over, all in-flight requests get purged. As a result, these requests will timeout at the participants. The applications need to retry the underlying commands.

### Running a Stand-Alone Mediator Node

A synchronizer may be statically configured with a single embedded mediator node or it may be configured to work with external mediators. Once the synchronizer has been initialized further mediators can be added at runtime.

By default, a synchronizer will run an embedded mediator node itself. This is useful in simple deployments where all synchronizer functionality can be co-located on a single host. In a distributed setup where synchronizer services are operated over many machines, you can instead configure a synchronizer manager node and bootstrap the synchronizer with mediator(s) running externally.

Mediator nodes can be defined in the same manner as Canton participants and synchronizers.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    admin-api.port = 5017
  }
```

When the synchronizer starts it will automatically provide the embedded mediator information about the synchronizer. External mediators have to be initialized using runtime administration in order to complete the synchronizer initialization.

### HA Configuration

HA mediator support is only available in the Daml Enterprise version of Canton and only PostgreSQL and Oracle-based storage are supported for HA.

Mediator node replicas are configured in the Canton configuration file as individual stand-alone mediator nodes with two required changes for each mediator node replica:

* Using the same storage configuration to ensure access to the shared database.
* Set `replication.enabled = true` for each mediator node replica.

<Note>
  Starting from canton 2.4.0, mediator replication is enabled by default when using supported storage.
</Note>

Only the active mediator node replica has to be initialized through the synchronizer bootstrap commands. The passive replicas observe the initialization via the shared database.

Further replicas can be started at runtime without any additional setup. They remain passive until the current active mediator node replica fails.

## Sequencer

The database-based sequencer can be horizontally scaled and placed behind a load balancer to provide high availability and performance improvements.

Deploy multiple sequencer nodes for the synchronizer with the following configuration:

> * All sequencer nodes share the same database so ensure that the storage configuration for each sequencer matches.
> * All sequencer nodes must be configured with `high-availability.enabled = true`.

<Note>
  Starting from Canton 2.4.0, sequencer high availability is enabled by default when using supported storage.
</Note>

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton {
    remote-sequencers {
      sequencer1 {
        # these details are provided to other nodes to use for how they should connect to the sequencer
        public-api {
          address = sequencer1.local
          port = 1235
          tls {
            enabled = true
            trust-collection-file = "community/app/src/test/resources/tls/some.pem"
          }
        }
        # the server used from running administration commands
        admin-api {
          address = sequencer1.local
          port = 1235
        }
      }
    }
  }

```

The synchronizer node only supports embedded sequencers, so a distributed setup using a synchronizer manager node must then be configured to use these sequencer nodes by pointing it at these external services.

Once configured the synchronizer must be bootstrapped with the new external sequencer using the bootstrap\_synchronizer operational process. These sequencers share a database so just use a single instance for bootstrapping and the replicas will come online once the shared database has a sufficient state for starting.

As these nodes are likely running in separate processes you could run this command entirely externally using a remote administration configuration.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  remote-sequencers {
    sequencer1 {
      # these details are provided to other nodes to use for how they should connect to the sequencer
      public-api {
        address = sequencer1.local
        port = 1235
      }
      # the server used from running administration commands
      admin-api {
        address = sequencer1.local
        port = 1235
      }
    }
  }
}
```

There are two methods available for exposing the horizontally scaled sequencer instances to participants.

### Total node count

The `sequencer.high-availability.total-node-count` parameter is used to divide up time among the database sequencers. The parameter should not be changed once a set of sequencer nodes has been deployed. Because each message sequenced must have a unique timestamp, a sequencer node will use timestamps `modulo` the `total-node-count` plus its own index to create timestamps that do not conflict with other sequencer nodes while sequencing the messages in a parallel database insertion process. Canton uses microseconds, which yields a theoretical max throughput of 1 million messages per second per synchronizer. Now, this theoretical throughput is divided equally among all sequencer nodes (`total-node-count`). Therefore, if you set `total-node-count` too high, then a sequencer might not be able to operate at the maximum theoretical throughput. We recommend keeping the default value of `10`, as all above explanations are only theoretical and we have not yet seen a database/hard disk that can handle the theoretical throughput. Also note that a message might contain multiple events, such that we are talking about high numbers here.

### External load balancer

Using a load balancer is recommended when you have a http2+grpc supporting load balancer available, and can't/don't want to expose details of the backend sequencers to clients. An advanced deployment could also support elastically scaling the number of sequencers available and dynamically reconfigure the load balancer for this updated set.

An example [HAProxy]() configuration for exposing GRPC services without TLS looks like:

frontend domain\_frontend
bind 1234 proto h2
default\_backend domain\_backend

backend domain\_backend
option httpchk
http-check connect
http-check send meth GET uri /health
balance roundrobin
server sequencer1 sequencer1.local:1234 proto h2 check port 8080
server sequencer2 sequencer2.local:1234 proto h2 check port 8080
server sequencer3 sequencer3.local:1234 proto h2 check port 8080

Please note that for quick failover, you also need to add HTTP health checks, as otherwise, you have to wait for the TCP timeout to occur before failover happens. The Public API of the sequencer exposes the standard GRPC health [endpoints](), but these are currently not supported by HAProxy, hence you need to fall back on the HTTP/health endpoint.

### Client-side load balancing

Using client-side load balancing is recommended where an external load-balancing service is unavailable (or lacks http2+grpc support), and the set of sequencers is static and can be configured at the client.

To simply specify multiple sequencers use the `synchronizers.connect_multi` console command when registering/connecting to the synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
myparticipant.synchronizers.connect_multi(
  "my_synchronizer_alias",
  Seq("https://sequencer1.example.com", "https://sequencer2.example.com", "https://sequencer3.example.com")
)
```

See the sequencer connectivity documentation for more details on how to add many sequencer URLs when combined with other synchronizer connection options. The synchronizer connection configuration can also be changed at runtime to add or replace configured sequencer connections. Note the synchronizer will have to be disconnected and reconnected at the participant for the updated configuration to be used.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/configure/apis.rst" hash="a0993dd6" */}

# Configure Synchronizer APIs

A Synchronizer exposes two main APIs, the Admin API and the Public API, while the Participant Node exposes the Ledger API and the Admin API. In this section, we explain what the APIs do and how they can be configured.

For details on how to configure endpoints and their addresses, ports, keep alive, and so on, see the general API documentation.

## Configure Sequencer Public API

The Sequencer Public API provides the services to other nodes to connect, authenticate, and exchange messages with a Synchronizer. To learn more about the Sequencer's role, visit the Sequencer overview page.

Configure the Public API `public-api` under a Sequencer node configuration:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    storage.type = memory
    public-api.port = 5001
    admin-api.port = 5002
    sequencer.type = BFT
  }
}
```

<div className="todo" />

All Sequencer Public API configuration parameters have defaults. For example, the default address to listen on is `127.0.0.1`. To find out more about the parameters, check the reference documentation.

## Configure Sequencer Admin API

The Sequencer Admin API can be configured in the standard way under the Sequencer node configuration (at the same level as the Public API).

## Configure Mediator Admin API

The Mediator Admin API can be configured in the standard way under the Mediator node configuration:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediators {
  mediator1 {
    storage.type = memory
    admin-api.port = 5202
  }
}
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/configure/sequencer_backend.rst" hash="f62eca63" */}

# Configure Sequencer Backend

The following page describes the basics of configuring Sequencer backends. For more advanced configuration, refer to the following sections:

> * High availability
> * Pruning
> * Optimization

## Database Sequencer

The Database Sequencer is currently unsupported and should not be configured.

## BFT Sequencer

### Minimal BFT Sequencer backend configuration

To use the Byzantine Fault Tolerant (BFT) Sequencer, set the `type` parameter to `BFT` under \`sequencer\`:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    sequencer.type = BFT
    public-api.port = 5001
    admin-api.port = 5002
  }
}
```

Note that this configuration is for single-node networks; you cannot add peers. For multi-node networks, refer to the next section.

### Configure initial peers (optional)

If the network contains more than one node, configure the server endpoint under `initial-network`. There, you can also configure peer endpoints, or do so using admin commands later. Pre-configuring the peer endpoints reduces the number of manual configuration steps, which saves time, reduces errors, and accelerates the deployment process.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
server-endpoint {
  address = "0.0.0.0"
  port = 31030
  external-address = "127.0.0.1"
  external-port = 31030
  external-tls-config.enabled = false
}
peer-endpoints = [
  {
    address = "127.0.0.1"
    port = 31031
    tls-config.enabled = false
  }
]
```

The `address` and `port` pair under `server-endpoint` make up an endpoint where the BFT Sequencer's gRPC server listens. If the `port` is not specified, the operating system chooses one for you. The `external-address` and `external-port` form an externally available endpoint that other peers can connect to. Usually, the `external-address` is the domain name of a reverse proxy that points to the listening endpoint. The external endpoint must be configured correctly for clients to successfully authenticate the server.

Transport Layer Security (TLS) is enabled by default for the external endpoint and peer endpoints. For simplicity, it is disabled in the config example. However, it is recommended to configure it in the standard way with:

> * `tls` under `server-endpoint` for the internal server endpoint
> * `external-tls-config` under `server-endpoint` for the external endpoint
> * `tls-config` under `peer-endpoints` for peer endpoints

<div className="todo" />

For more details on the `initial-network` configuration, check the reference documentation.

### Configure authentication (optional)

Authentication is enabled by default. It can be configured with `endpoint-authentication` under `initial-network` (at the same level as `server-endpoint`):

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
endpoint-authentication {
  auth-token = {}
}
```

For more details on authentication, visit the secure Synchronizer page.

### Configure dedicated storage (optional)

To use dedicated storage, configure `storage` under `config` as for the top-level Sequencer storage configuration.

While the BFT Sequencer defaults to using the top-level Sequencer storage, configuring dedicated storage offers greater flexibility. It allows you to:

> * Support distinct data read and write patterns with different database backends and settings
> * Separate backups

### Configure network-wide parameters

If you change the defaults, keep the following parameters in sync across the network:

> * \`epoch-length\`: a length of all epochs
> * \`max-requests-in-batch\`: a maximum number of requests in a batch, validated at runtime
> * \`max-batches-per-block-proposal\`: a maximum number of batches per block proposal, validated at runtime

All the above parameters reside under `config` and must be the same across all BFT Orderer nodes.

For details on the related concepts, check the BFT Orderer explanation page.

### Configure other (local) parameters

There are other (local) configuration parameters under `config` that can be changed.

<div className="todo" />

For details, check the reference documentation.

## External Sequencer

To use an external Sequencer (for example, CometBFT), configure the underlying Sequencer `type` under `config` in the `sequencer` configuration:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer {
    config {
        cometbft-node-host = "127.0.0.1"
        cometbft-node-port = 26627
    }
    type = CometBFT
}
```

Every external Sequencer requires a corresponding Sequencer Driver on the classpath.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/secure/apis.rst" hash="8b67f3f9" */}

# Secure Synchronizer APIs

## Sequencer Public API

### Public API

The synchronizer configuration requires the same configuration of the `Admin API` as the participant. Next to the `Admin API`, we need to configure the `Public API`, which is the API where all participants connect.

#### TLS Encryption

As with the Admin API, network traffic can (and should) be encrypted using TLS. This is particularly crucial for the Public API.

An example configuration section which enables TLS encryption and server-side TLS authentication is given by:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.synchronizer.acme.public-api {
  port = 5028
  address = localhost // defaults to 127.0.0.1
  tls {
    cert-chain-file = "./tls/public-api.crt"
    private-key-file = "./tls/public-api.pem"
    // minimum-server-protocol-version = TLSv1.3, optional argument
    // ciphers = null // use null to default to JVM ciphers
  }
}
```

If TLS is used on the server side with a self-signed certificate, we need to pass the certificate chain during the connect call of the participant. Otherwise, the default root certificates of the Java runtime will be used. An example would be:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/MultiSynchronizerIntegrationTests.scala start-after: architecture-handbook-entry-begin: TlsConnect end-before: architecture-handbook-entry-end: TlsConnect dedent:
</div>

#### Server Authentication

Canton has two ways to perform server authentication to protect from man-in-the-middle attacks: TLS and the synchronizer id.

If TLS is used on the Public API as described above, TLS also takes care of server authentication. This is one of the core functions of TLS.

Server authentication can also be performed by the synchronizer operator passing their synchronizer identity to the participant node operator, and checking that the identity matches that reported by the synchronizer to the participant node. Like all nodes, the synchronizer has an identity that corresponds to the fingerprint of its namespace root key. It reports its identity to connecting participant nodes and signs all its messages with keys authorized by that namespace root key on the topology ledger. Assuming no key compromises, this gives participants a guarantee that the reported identity is authentic. The synchronizer id of the sole connected synchronizer can be read out using console commands like:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.list_connected.last.synchronizerId.filterString
```

#### Client Authentication

Unlike the ledger or Admin API, the Public API uses Canton's cryptography and topology state for client authentication rather than mutual TLS (mTLS). Clients need to connect to the Public API in several steps:

1. The client calls the `SequencerConnectService` to align on Canton Protocol versions and obtain the synchronizer id.
2. During the first connection, the client registers by sending its minimal topology state (identity, key delegations, public keys) to the sequencer.
3. The client calls the `SequencerAuthenticationService` to authenticate using a challenge-response protocol and get an access token for the other sequencer services.
4. The client connects to the main `SequencerService` using the access token from 3.

The information the client provides in step 2 is verifiable since it is a certificate chain of keys. The synchronizer rejects this if the namespace root key fingerprint included is not permissioned (see `permissioned-synchronizer`) or if the topology state provided is invalid.

During step 3, the client claims an identity, which is the fingerprint of a namespace root key. If that identity is registered (as done in step 2), the sequencer responds with a challenge consisting of a nonce and all fingerprints of signing keys authorized for that member as per the topology ledger. If the challenge is met successfully by signing the nonce appropriately with a key matching one of the authorized keys, the `SequencerAuthenticationService` responds with a time-limited token which can be used to authenticate more cheaply on the other Public API services.

This authentication mechanism for the restricted services is built into the public sequencer API. You don't need to do anything to set this up; it is enforced automatically and can't be turned off.

The expiration of the token generated in step 2 is valid for one hour by default. The nodes automatically renew the token in the background before it expires. The lifetime of the tokens and of the nonce can be reconfigured using

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.sequencers.sequencer1.public-api {
    max-token-expiration-interval = 60m
    nonce-expiration-interval = 1m
}
```

However, we suggest keeping the default values.

As mentioned above, an issued token allows the member that provides it during a call to authenticate on public sequencer API services. Therefore, these tokens are sensitive information that must not be disclosed. If an operator suspects that the authentication token for a member has been leaked or somehow compromised, they should use the `logout` console command to immediately revoke all valid tokens of that member and close the sequencer connections. The legitimate member automatically reconnects and obtains new tokens through the challenge-response protocol described above.

The command is slightly different depending on whether the member is a participant or a mediator, for example:

<div className="todo">
  Replace with references to the commands. #22919
</div>

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.synchronizers.logout(mySynchronizerAlias)
mediator1.sequencer_connections.logout()
```

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/secure/limits.rst" hash="3828c946" */}

# Set sequencer resource limits

## Protect against large requests

Max request size is a dynamic Synchronizer parameter. You update the `maxRequestSize` field when you change the dynamic Synchronizer parameters.

## Protect the Sequencer via rate limiting

Confirmation request max rate is a dynamic Synchronizer parameter. You update the `confirmationRequestsMaxRate` field when you change the dynamic Synchronizer parameters.

## Protect the Byzantine Fault Tolerance orderer from large requests

When starting the Byzantine Fault Tolerance (BFT) orderer, you can provide limits for both `max-request-payload-bytes` how many bytes one transaction can handle, and `max-request-in-batch` for how many transactions can be handled in a batch.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers {
  sequencer1 {
    public-api.port = 5001
    admin-api.port = 5002
    sequencer {
      config {
        max-request-payload-bytes = 1000000
        max-requests-in-batch = 16
      }
      type = BFT
    }
  }
}
```

<Note>
  Do note that `max-requests-in-batch` is a network wide parameter and should be the same for all orderers in the network.
</Note>

## Protect the Sequencer from too many acknowledgements

To limit the amount of acknowledgements on the network, the Sequencer can conflate acknowledgements that come from the same member and are too close in time to each other. You can configure the window by setting the following value in the config.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencers.sequencer1.acknowledgements-conflate-window = "1 minute"
```

## Limit Sequencer submissions via traffic management

You can protect a Synchronizer from excessive traffic from its members by enabling traffic management.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/decommission/index.rst" hash="13c55e5a" */}

# Decommissioning Canton nodes and Synchronizer entities

This guide assumes general familiarity with Canton, in particular Canton identity management concepts and operations from the Canton console.

Note that, while onboarding new nodes is always possible, **a decommissioned node or entity is effectively disposed of and cannot rejoin a synchronizer**. **Decommissioning is thus an irreversible operation**.

In addition, **decommissioning procedures are currently experimental**; regardless, **backing up nodes to be decommissioned before decommissioning them is strongly recommended**.

## Decommissioning a Sequencer

Sequencers are part of a synchronizer’s messaging infrastructure and do not store application contracts, so they are disposable as long as precautions are taken to avoid disrupting the synchronization services. This means, concretely, ensuring that:

1. No active participant nor active mediator is connected to the sequencer to be decommissioned.
2. All active participants and mediators are connected to an active sequencer.

After that, the sequencer can be decommissioned by removing it from the synchronizer’s topology and finally disposed of.

### Disconnecting all nodes from the sequencer to be decommissioned

* Change the sequencer connection on the mediators connected to the sequencer to be decommissioned to use another active sequencer, as per mediator connectivity:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala language: scala start-after: user-manual-entry-begin: SequencerOffboardingSwitchAwayMediator end-before: user-manual-entry-end: SequencerOffboardingSwitchAwayMediator dedent:
</div>

* Reconnect participants to the Synchronizer, as described in Synchronizer connectivity, using a sequencer connection to another active sequencer:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala language: scala start-after: user-manual-entry-begin: SequencerOffboardingSwitchAwayParticipant end-before: user-manual-entry-end: SequencerOffboardingSwitchAwayParticipant dedent:
</div>

### Decommissioning the sequencer

Sequencers are part of the synchronizer by virtue of having their node ID equal to the synchronizer id, which also means they all have the same node ID. Since a sequencer’s identity is the same as the synchronizer’s identity, you should leave identity and namespace mappings intact.

However, a sequencer may use its own cryptographic material distinct from other sequencers. In that case, owner-to-key mappings must be removed for the keys it exclusively owns:

1. Find the keys on the sequencer to be decommissioned using the keys.secret.list command.
2. Among those keys, find the ones not shared by other sequencers. You can do this by issuing the keys.secret.list command on each of them: the fingerprints that appear only on the sequencer node to be decommissioned correspond to its exclusively-owned keys.

<div className="todo">
  \#22917: Fix broken ref #. Remove the mappings for its exclusively owned keys using the ref:topology.owner\_to\_key\_mappings.authorize command.
</div>

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/SequencerOffboardingIntegrationTest.scala language: scala start-after: user-manual-entry-begin: SequencerOffboardingRemoveExclusiveKeys end-before: user-manual-entry-end: SequencerOffboardingRemoveExclusiveKeys dedent:
</div>

Finally, the cryptographic material exclusively owned by a decommissioned sequencer must also be disposed of:

* If it was stored only on the decommissioned sequencer, it must be disposed of together with the decommissioned sequencer node.
* However, if a decommissioned sequencer’s cryptographic material is managed via a KMS system, it must be disposed of through the KMS; refer to your KMS’ documentation and internal procedures to handle this. KMS-managed cryptographic material of sequencer nodes.

## Decommissioning a Mediator

Mediators are also part of a synchronizer’s messaging infrastructure and do not store application contracts, so they are disposable as long as precautions are taken to avoid disrupting the synchronization services. This means ensuring that at least one mediator remains on the synchronizer.

<div className="todo">
  \#22917: Fix broken ref If other mediators exist on the synchronizer, a mediator can be decommissioned using a single console command ref:setup.offboard\_mediator.
</div>

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/enterprise/app/src/test/scala/com/digitalasset/canton/integration/tests/offboarding/MediatorOffboardingIntegrationTest.scala language: scala start-after: user-manual-entry-begin: OffboardMediator end-before: user-manual-entry-end: OffboardMediator dedent:
</div>

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/recover/index.rst" hash="4187dc6f" */}

# Backup and Restore

It is recommended that your database is frequently backed up so that the data can be restored in case of a disaster.

In the case of a restore, a participant can replay missing data from the synchronizer as long as the synchronizer's backup is more recent than that of the participant's.

<div className="todo" />

## Order of backups

It is important that the participant's backup is not more recent than that of the sequencer's, as that would constitute a ledger fork. Therefore, if you back up both participant, mediator and sequencer databases sequentially, the following constraints apply:

* Back up the mediators and participants before the sequencer; otherwise, they may not be able to reconnect to the sequencer (`ForkHappened`). The relative order of mediators, and participants does not matter.

If you perform a complete system backup in a single step (for example, using a cloud RDS), make sure no component writes to the database while the backup is in progress.

In case of a synchronizer restore from a backup, if a participant is ahead of the synchronizer the participant will refuse to connect to the synchronizer (`ForkHappened`) and you must either:

* restore the participant's state to a backup before the disaster of the synchronizer, or
* roll out a new Synchronizer as a repair strategy in order to recover from a lost Synchronizer

The state of applications that interact with a participant's Ledger API must be backed up before the participant, otherwise the application state has to be reset.

## Restore caveats

When restoring Canton nodes from a backup, the following caveats apply due to the loss of data between the point of backup and latest state of the nodes.

### Incomplete Command Deduplication State

After the restore, the participant's in-flight submission tracking will be out of sync with what the participant has sent to the sequencer after the backup was taken. If an application resubmits a duplicate command it may get accepted even though it should have been deduplicated by the participant.

This tracking will be in sync again when:

> * the participant has processed all events from the sequencer, and
> * no queue on the sequencer includes any submission request of a transfer/transaction request from before the restore that could be sequenced again

Such submission requests have a max sequencing time of the ledger time plus the ledger-time-record-time-tolerance of the synchronizer. It should be enough to observe a timestamp from the synchronizer that is after the time when the participant was stopped before the restore by more than the tolerance. Once such a timestamp is observed, the in-flight submission tracking is in sync again and applications can resume submitting commands with full command deduplication guarantees.

### Application State Reset

If the application's state is newer than the participant's state, either because the application was backed up after the participant or because the application is run by a different organization and wasn't restored from a backup, then the application state has to be reset. Otherwise the application has already requested and processed transactions that were lost by the participant due to the gap between when the backup was taken and when the node disaster happened.

This includes all applications that are Ledger API clients of the participant.

### Private Keys

Assume a scenario in which a node needs to rotate its cryptographic private key, which is currently stored in the database of the node. If the key rotation has been announced in the system before a backup has been performed, the new key will not be available on a restore, but all other nodes in the system expect the new key to be used.

To avoid this situation, perform the key rotation steps in this order:

1. Generate the new private key and store it in the database
2. Back up the database
3. Once the backup is complete, revoke the previous key

## Postgres example

If you are using Postgres to persist the Participant Node or Synchronizer data, you can create backups to a file and restore it using Postgres's utility commands `pg_dump` and `pg_restore` as shown below:

Backing up Postgres database to a file:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
pg_dump -U <user> -h <host> -p <port> -w -F tar -f <fileName> <dbName>
```

Restoring Postgres database data from a file:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
pg_restore -U <user> -h <host> -p <port> -w -d <dbName> <fileName>
```

Although the approach shown above works for small deployments, it is not recommended for larger deployments. For that, we suggest looking into incremental backups and refer to the resources below:

* PostgreSQL Documentation: Backup and Restore
* How incremental backups work in PostgreSQL

## Database Replication for Disaster Recovery

### Synchronous replication

We recommend that in production at least the synchronizer should be run with offsite synchronous replication to ensure that the state of the synchronizer is always newer than the state of the participants. However to avoid similar caveats as with backup restore the participants should either use synchronous replication too or as part of the manual disaster recovery failure procedure the caveats have to be addressed.

A database backup allows you to recover the ledger up to the point when the last backup was created. However, any command accepted after creation of the backup may be lost in case of a disaster. Therefore, restoring a backup will likely result in data loss.

If such data loss is unacceptable, you need to run Canton against a replicated database, which replicates its state to another site. If the original site is down due to a disaster, Canton can be started in the other site based on the replicated state in the database. It is crucial that there are no writers left in the original site to the database, because the database mechanism used in Canton to avoid multiple writers and thus avoid data corruption does not work across sites.

For detailed instructions on how to setup a replicated database and how to perform failovers, we refer to the database system documentation, e.g. the high availability documentation of PostgreSQL.

**It is strongly recommended to configure replication as synchronous.** That means, the database should report a database transaction as successfully committed only after it has been persisted to all database replicas. In PostgreSQL, this corresponds to the setting `synchronous_commit = on`. If you do not follow this recommendation, you may observe data loss and/or a corrupt state after a database failover. Enabling synchronous replication may impact the performance of Canton depending on the network latency between the primary and offsite database.

For PostgreSQL, Canton strives to validate the database replication configuration and fail with an error, if a misconfiguration is detected. However, this validation is of a best-effort nature; so it may fail to detect an incorrect replication configuration. For Oracle, no attempt is made to validate the database configuration. Overall, you should not rely on Canton detecting mistakes in the database configuration.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
