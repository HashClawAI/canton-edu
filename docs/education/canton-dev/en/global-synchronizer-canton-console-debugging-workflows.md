---
title: "Debugging Workflows"
slug: "global-synchronizer-canton-console-debugging-workflows"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/debugging-workflows.md"
source_title: "Debugging Workflows"
tags:
  - global-synchronizer
  - canton-console
  - debugging-workflows
---

# Debugging Workflows

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Debugging Workflows

> Step-by-step diagnostic procedures for common Canton issues using the console

When transactions fail, nodes disconnect, or the system behaves unexpectedly, the Canton Console provides the tools to diagnose the problem. This page walks through common debugging scenarios with concrete console commands.

## Debugging Stuck Transactions

A transaction appears "stuck" when a command was submitted but no completion event arrives. Common causes: a stakeholder's participant is unreachable, a required package isn't vetted, or the synchronizer rejected the transaction.

### Step 1: Check Node Health

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res1: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
    Uptime: 19.211042s
    Ports: 
    	ledger: 32794
    	admin: 32795
    	json: 32796
    Connected synchronizers: 
    	da::122032922613...::35-0
    Unhealthy synchronizers: None
    Active: true
    Components: 
    	memory_storage : Ok()
    	connected-synchronizer : Ok()
    	sync-ephemeral-state : Ok()
    	sequencer-client : Ok()
    	acs-commitment-processor : Ok()
    	sequencer-connection-pool : Ok()
    	sequencer-subscription-pool : Ok()
    	internal-sequencer-connection-sequencer1-0 : Ok()
    	subscription-sequencer-connection-sequencer1-0 : Ok()
    Version: 3.6.0-SNAPSHOT
    Supported protocol version(s): 35, dev
```

If the participant isn't active or has no connected synchronizers, the transaction can't proceed.

### Step 2: Verify Synchronizer Connectivity

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected()
    res2: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'da',
        physicalSynchronizerId = da::122032922613...::35-0,
        healthy = true
      )
    )
```

If the synchronizer is disconnected, check network connectivity and try reconnecting:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.reconnect(synchronizerAlias)
    res3: Boolean = true
```

### Step 3: Check Package Vetting

A transaction fails if a stakeholder's participant hasn't vetted the required packages.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list()
    res4: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:50:08.491115Z,
          validUntil = None,
          sequenced = 2026-05-04T17:50:08.241115Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:8352cebba166...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = VettedPackages(
          participantId = PAR::participant1::12201ff69b1d...,
          packages = VettedPackage(packageId = 6f8e6085f576..., unbounded),VettedPackage(packageId = 60c61c542207..., unbounded),VettedPackage(packageId = a1fa18133ae4..., unbounded),VettedPackage(packageId = cae345b5500e..., unbounded),VettedPackage(packageId = c3bb0c5d0479..., unbounded),... 25 more
        )
      )
    )
```

If the package isn't vetted, upload and vet it:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list().filter(_.item.packages.exists(_.packageId.toString.contains(targetPackageId)))
    res5: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector()
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res6: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

### Step 4: Check Party Hosting

Verify that all parties involved in the transaction are properly hosted:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect("unreachable_synchronizer", "http://non-existent-sequencer.local:12345")
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...
      Request: ConnectSynchronizer(SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'unreachable_synchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(sequencerAlias = Sequ ...
      DecodedCantonError(
      code = 'SYNC_SERVICE_BAD_CONNECTIVITY',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...",
      traceId = 'e3186611ac49ae5f2f63d4b1c5d8f6cd',
      context = Seq(
        'participant=>participant1',
        'test=>DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest',
        'errors=>List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-existent-sequencer.local: nodename nor servname provided, or not known
        non-existent-sequencer.local: nodename nor servname provided, or not known)))'
      )
    )
      Command ParticipantAdministration$synchronizers$.connect invoked from cmd10000021.sc:1
```

If a party isn't mapped to any active participant, the synchronizer can't deliver transaction views to that party's stakeholder.

## Connectivity Issues

### Synchronizer Connection Failures

When a participant can't connect to the synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect("unreachable_synchronizer", "http://non-existent-sequencer.local:12345")
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...
      Request: ConnectSynchronizer(SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'unreachable_synchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(sequencerAlias = Sequ ...
      DecodedCantonError(
      code = 'SYNC_SERVICE_BAD_CONNECTIVITY',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "SYNC_SERVICE_BAD_CONNECTIVITY(9,e3186611): The provided sequencer connections are inconsistent: List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-exis...",
      traceId = 'e3186611ac49ae5f2f63d4b1c5d8f6cd',
      context = Seq(
        'participant=>participant1',
        'test=>DocsCantonNetworkGlobalSynchronizerCantonConsoleDebuggingWorkflowsTest',
        'errors=>List(NotValid(GrpcSequencerConnection(sequencerAlias = Sequencer 'DefaultSequencer', endpoints = http://non-existent-sequencer.local:12345),SynchronizerIsNotAvailableError(Synchronizer 'unreachable_synchronizer',Request failed for unreachable_synchronizer/sequencer-public-api. Is the url correct?
      GrpcServiceUnavailable: UNAVAILABLE/Unable to resolve host non-existent-sequencer.local
      Request: GetApiInfo
      Causes: java.net.UnknownHostException: non-existent-sequencer.local: nodename nor servname provided, or not known
        non-existent-sequencer.local: nodename nor servname provided, or not known)))'
      )
    )
      Command ParticipantAdministration$synchronizers$.connect invoked from cmd10000021.sc:1
```

Common causes:

* Network firewall blocking sequencer ports
* TLS certificate mismatch
* Authentication token expired or invalid
* Sequencer endpoint unreachable

### Verifying Sequencer Connectivity (from Sequencer Console)

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res7: NodeStatus[sequencer1.Status] = Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
    Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
    Uptime: 1m 17.038832s
    Ports: 
    	public: 32798
    	admin: 32799
    Connected participants: 
    	PAR::participant1::12201ff69b1d...
    Connected mediators: 
    	MED::mediator1::122009299340...
    Sequencer: SequencerHealthStatus(active = true)
    details-extra: None
    Components: 
    	memory_storage : Ok()
    	sequencer : Ok()
    Accepts admin changes: true
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

## Identity Problems

### Party Not Found

If a party ID returns no results:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list().filter(_.party.toProtoPrimitive.startsWith("Bob"))
    res8: Seq[ListPartiesResult] = Vector()
```

The party may be hosted on a different participant, or the party-to-participant mapping may not have propagated yet. Topology changes take a short time to distribute across the network.

### Multi-Hosting Proposal Status

If a multi-hosting setup isn't taking effect:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list_hosting_proposals(synchronizerId, participant1.id)
    res9: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMultiHostingProposal] = Vector(
      ListMultiHostingProposal(
        txHash = SHA-256:f77e8ccd88df...,
        party = Alice::12201ff69b1d...,
        permission = Confirmation$,
        others = PAR::participant2::1220a4d7463b... -> Confirmation$,
        threshold = 1
      )
    )
```

A pending proposal means the second participant hasn't signed yet. See [Multi-Hosting](/docs/canton/appdev-deep-dives-multi-hosting) for the authorization procedure.

## ACS Inspection

When application behavior is unexpected, inspect the active contract set to verify on-ledger state:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val contracts = participant1.testing.acs_search(synchronizerAlias, filterTemplate = "Iou:Iou")
    contracts : List[com.digitalasset.canton.protocol.package.ContractInstance] = List(
      ContractInstanceImpl(
        contractId = 185a4f643c67...ca1212207c34f33a...,
        metadata = ContractMetadata(
          signatories = Alice::12201ff69b1d...,
          stakeholders = Alice::12201ff69b1d...
        ),
        created at = 2026-05-04T17:51:39.410348Z
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ s"Found ${contracts.size} active contracts"
    res11: String = "Found 1 active contracts"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ contracts.headOption.map { c => (c.contractId, c.toLf.arg) }
    res12: Option[(com.digitalasset.canton.protocol.package.LfContractId, com.digitalasset.daml.lf.value.package.Value)] = Some(
      value = (
        V1(
          discriminator = Hash(185a4f643c674e59891e9f4340060205cebdb9b9bee7046a9ea1728f54bd4a3d),
          suffix = Bytes(ca1212207c34f33a388c409c1b4f2bdd5e6cc46625cc8ff16865d5ff363ef1a9550f8c4f)
        ),
        Record(
          tycon = None,
          fields = ImmArray((None,Party(Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c)),(None,Party(Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c)),(None,Record(None,ImmArray((None,Numeric(100.0000000000)),(None,Text(EUR))))),(None,List(FrontStack())))
        )
      )
    )
```

### Comparing ACS Across Participants

If two participants see different state for the same party, compare their ACS counts for specific templates. Discrepancies indicate a synchronization issue — check that both participants are connected to the same synchronizer and have the same packages vetted.

## Diagnostic Checklist

When investigating any issue, work through this sequence:

1. **Health** — Is the node running? `participant.health.status`
2. **Connectivity** — Is the synchronizer connected? `participant.synchronizers.list_connected`
3. **Packages** — Are required packages uploaded and vetted? `participant.topology.vetted_packages.list()`
4. **Parties** — Are parties correctly hosted? `participant.parties.hosted()`
5. **Topology** — Are party-to-participant mappings correct? `participant.topology.party_to_participant_mappings.list(syncId)`
6. **ACS** — Does the on-ledger state match expectations? `participant.testing.acs_search(...)`

## Next Steps

* [Essential Commands](/docs/canton/global-synchronizer-canton-console-essential-commands) — Quick reference for all key commands
* [Console Overview](/docs/canton/global-synchronizer-canton-console-console-overview) — How to access the console in different environments

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
