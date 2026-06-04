---
title: "Essential Commands"
slug: "global-synchronizer-canton-console-essential-commands"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/essential-commands.md"
source_title: "Essential Commands"
tags:
  - global-synchronizer
  - canton-console
  - essential-commands
---

# Essential Commands

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Essential Commands

> Key Canton Console commands for health checks, party management, package management, and topology inspection

This reference covers the most commonly used Canton Console commands, organized by task. All examples assume you're connected to a participant console unless otherwise noted.

When the Canton Console starts, it reads the configuration file and automatically binds a variable for each configured node. For example, if your configuration defines a participant node, the console makes it available as the `participant` variable (or whatever name you gave it in the config). You can use this variable directly to call commands like `participant.health.status` without any additional setup.

## Health and Status

Check whether the node is healthy and connected to the synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status
    res1: NodeStatus[ParticipantStatus] = Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
    Uptime: 18.722511s
    Ports: 
    	ledger: 30470
    	admin: 30471
    	json: 30472
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

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.is_running
    res2: Boolean = true
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected()
    res3: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'da',
        physicalSynchronizerId = da::122032922613...::35-0,
        healthy = true
      )
    )
```

For sequencer nodes:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res4: NodeStatus[sequencer1.Status] = Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
    Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
    Uptime: 14.142114s
    Ports: 
    	public: 30474
    	admin: 30475
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

## Party Management

### Listing Parties

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.hosted()
    res5: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = participant1::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      ),
      ListPartiesResult(
        partyResult = Alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.hosted("Alice")
    res6: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = Alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list()
    res7: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = participant1::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      ),
      ListPartiesResult(
        partyResult = Alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
            )
          )
        )
      )
    )
```

### Party Details

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.hosted("Alice").head
    res8: ListPartiesResult = ListPartiesResult(
      partyResult = Alice::12201ff69b1d...,
      participants = Vector(
        ParticipantSynchronizers(
          participant = PAR::participant1::12201ff69b1d...,
          synchronizers = Vector(
            SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
          )
        )
      )
    )
```

## Package Management

### Listing Packages

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.list()
    res9: Seq[DarDescription] = Vector(
      DarDescription(
        mainPackageId = "de2cc2f90eb523414ff54e899951dadd8789a4c07e0f71f6d6c9eaf57d412a54",
        name = "canton-builtin-admin-workflow-ping",
        version = "3.4.0",
        description = "System package"
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.list().filter(_.packageId.startsWith("com-example"))
    res10: Seq[PackageDescription] = Vector()
```

### Uploading Packages

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res11: String = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e"
```

### Package Vetting

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list()
    res12: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-06T12:03:46.575654Z,
          validUntil = None,
          sequenced = 2026-05-06T12:03:46.325654Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:566752a84b7c...),
          serial = PositiveNumeric(value = 2),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = VettedPackages(
          participantId = PAR::participant1::12201ff69b1d...,
          packages = VettedPackage(packageId = 6f8e6085f576..., unbounded),VettedPackage(packageId = 60c61c542207..., unbounded),VettedPackage(packageId = a1fa18133ae4..., unbounded),VettedPackage(packageId = cae345b5500e..., unbounded),VettedPackage(packageId = c3bb0c5d0479..., unbounded),... 29 more
        )
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list().filter(_.item.packages.exists(_.packageId.toString.contains(packageId)))
    res13: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-06T12:03:46.575654Z,
          validUntil = None,
          sequenced = 2026-05-06T12:03:46.325654Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:566752a84b7c...),
          serial = PositiveNumeric(value = 2),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = VettedPackages(
          participantId = PAR::participant1::12201ff69b1d...,
          packages = VettedPackage(packageId = 6f8e6085f576..., unbounded),VettedPackage(packageId = 60c61c542207..., unbounded),VettedPackage(packageId = a1fa18133ae4..., unbounded),VettedPackage(packageId = cae345b5500e..., unbounded),VettedPackage(packageId = c3bb0c5d0479..., unbounded),... 29 more
        )
      )
    )
```

## Topology Inspection

Topology commands show the current state of party-to-participant mappings, package vetting, and other network-wide configuration.

### Party-to-Participant Mappings

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.list(synchronizerId)
    res14: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult] = Vector(
      ListPartyToParticipantResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-06T12:03:40.402313Z,
          validUntil = None,
          sequenced = 2026-05-06T12:03:40.152313Z,
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

### Synchronizer Parameters

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.synchronizer_parameters.list(synchronizerId)
    res15: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListSynchronizerParametersStateResult] = Vector(
      ListSynchronizerParametersStateResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 0001-01-01T00:00:00.000001Z,
          validUntil = None,
          sequenced = 0001-01-01T00:00:00.000001Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:bb924a6165c0...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(1220cb0a22fb...)
        ),
        item = DynamicSynchronizerParameters(
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
            catchUpIntervalSkip = 5,
            nrIntervalsToTriggerCatchUp = 2
          ),
          participant synchronizer limits = ParticipantSynchronizerLimits(
            confirmation requests max rate = 1000000
          ),
          preparation time record time tolerance = 24h,
          onboarding restriction = UnrestrictedOpen
        )
      )
    )
```

### Namespace Delegations

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.namespace_delegations.list(store = synchronizerId)
    res16: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListNamespaceDelegationResult] = Vector(
      ListNamespaceDelegationResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 0001-01-01T00:00:00.000001Z,
          validUntil = None,
          sequenced = 0001-01-01T00:00:00.000001Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:9064e1eaf436...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(1220cb0a22fb...)
        ),
        item = NamespaceDelegation(
          namespace = 1220cb0a22fb...,
          target = SigningPublicKey(
            id = 1220cb0a22fb...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = none
        )
      ),
      ListNamespaceDelegationResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 0001-01-01T00:00:00.000001Z,
          validUntil = None,
          sequenced = 0001-01-01T00:00:00.000001Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:e5dfa02d10cf...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(122009299340...)
        ),
        item = NamespaceDelegation(
          namespace = 122009299340...,
          target = SigningPublicKey(
            id = 122009299340...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = none
        )
      ),
      ListNamespaceDelegationResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-06T12:03:32.886116Z,
          validUntil = None,
          sequenced = 2026-05-06T12:03:32.636116Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:252f433640a0...),
          serial = PositiveNumeric(value = 1),
          signedBy = Vector(12201ff69b1d...)
        ),
        item = NamespaceDelegation(
          namespace = 12201ff69b1d...,
          target = SigningPublicKey(
            id = 12201ff69b1d...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          restriction = none
        )
      )
    )
```

## Synchronizer Operations

### Listing Connected Synchronizers

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected()
    res17: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'da',
        physicalSynchronizerId = da::122032922613...::35-0,
        healthy = true
      )
    )
```

### Reconnecting to a Synchronizer

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val syncAlias = participant1.synchronizers.list_connected().head.synchronizerAlias
    syncAlias : SynchronizerAlias = Synchronizer 'da'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.reconnect(syncAlias)
    res19: Boolean = true
```

## Querying the Ledger

### Active Contract Set (ACS)

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.testing.acs_search(synchronizerAlias, filterTemplate = "Iou:Iou").size
    res20: Int = 1
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.testing.acs_search(synchronizerAlias, filterTemplate = "Iou:Iou", filterStakeholder = Some(partyId))
    res21: List[com.digitalasset.canton.protocol.package.ContractInstance] = List(
      ContractInstanceImpl(
        contractId = 6a1576b1b626...ca12122091ae7b9c...,
        metadata = ContractMetadata(
          signatories = Alice::12201ff69b1d...,
          stakeholders = Alice::12201ff69b1d...
        ),
        created at = 2026-05-06T12:03:56.479481Z
      )
    )
```

<Note>
  The `testing.acs_search` command is intended for debugging, not production queries. For production read access, use PQS.
</Note>

## Common Patterns

### Getting the Participant ID

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val participantId = participant1.id
    participantId : ParticipantId = PAR::participant1::12201ff69b1d...
```

### Getting a Party ID

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val partyId2 = participant1.parties.hosted("Alice").head.party
    partyId2 : PartyId = Alice::12201ff69b1d...
```

### Getting the Synchronizer ID

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val syncId2 = participant1.synchronizers.list_connected().head.synchronizerId
    syncId2 : SynchronizerId = da::122032922613...
```

## Next Steps

* [Debugging Workflows](/global-synchronizer/canton-console/debugging-workflows) — Using these commands in diagnostic scenarios
* [Console Overview](/global-synchronizer/canton-console/console-overview) — How to start the console

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
