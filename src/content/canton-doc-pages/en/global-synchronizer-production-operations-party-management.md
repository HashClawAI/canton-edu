---
title: "Party Management"
slug: "global-synchronizer-production-operations-party-management"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/party-management.md"
source_title: "Party Management"
tags:
  - global-synchronizer
  - production-operations
  - party-management
---

# Party Management

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Party Management

> Manage parties on Canton nodes - allocation, replication, and decentralized party setup

# Party Management

Parties are the entities that interact with the Daml ledger, representing users or organizations. They can be onboarded to a Participant Node, which allows them to submit transactions and access the ledger.

The following section explains how to onboard a (local) party. Refer to the following howtos for onboarding of other kind of parties:

* For decentralized parties, refer to the Decentralized Party Overview documentation.
* For external parties, refer to the Onboard External Party tutorial.
* For a party that is already hosted on a participant, refer to the Party Replication documentation.

## Onboard a new party via the ledger API

If you have access to the ledger API, you can onboard a new party using the `parties` command. This command is simply a wrapper around the underlying Ledger API endpoints. For more information, see the Ledger API documentation.

1. Define a name for the Party. You can choose the name freely, but it must conform to the following format: `\[a-zA-Z0-9:-\_ \]`, must not exceed 185 characters, must not use two consecutive colons, and must be unique in the namespace.

For example, we want to host the Party `bob`.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bob = "bob"
    bob : String = "bob"
```

2. Specify an optional Synchronizer ID to which the party should be allocated. The participant must be connected to this Synchronizer. You may omit this parameter if the participant is connected to only one Synchronizer, otherwise the party needs to be enabled on each synchronizer explicitly.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of("my-synchronizer")
    synchronizerId : SynchronizerId = da::122032922613...
```

3. Define optional annotations. These are key-value pairs associated with this party and stored locally on this Ledger API server. Annotations are useful for maintaining metadata about allocated parties.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3")
    annotations : Map[String, String] = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3")
```

4. Define an optional identity provider id.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val idpId = "idp-id-" + java.util.UUID.randomUUID().toString
    idpId : String = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.identity_provider_config.create(identityProviderId = idpId, jwksUrl = "https://jwks:900", issuer = java.util.UUID.randomUUID().toString, audience = Option("someAudience"))
    res5: com.digitalasset.canton.ledger.api.IdentityProviderConfig = IdentityProviderConfig(
      identityProviderId = Id(value = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"),
      isDeactivated = false,
      jwksUrl = JwksUrl(value = "https://jwks:900"),
      issuer = "a8f1e514-a622-4a16-bb4c-85bfa83d2545",
      audience = Some(value = "someAudience")
    )
```

5. Enable the Party on this participant on ""my-synchronizer""

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.allocate(bob, annotations = annotations, identityProviderId = idpId, synchronizerId = Some(synchronizerId))
    res6: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

6. If you want to onboard the party on a second Synchronizer, you can do so by running the `allocate` command again with a different Synchronizer ID.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.allocate(bob, annotations = annotations, identityProviderId = idpId, synchronizerId = Some(synchronizerId))
    res6: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("k1" -> "v1", "k2" -> "v2", "k3" -> "v3"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

### Update a party

1. You can update the annotations of a party. To do so, use the `update` command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.update(bobPartyId, modifier = _.copy(annotations = Map("foo" -> "bar")), identityProviderId = idpId)
    res9: parties.PartyDetails = PartyDetails(
      party = bob::12201ff69b1d...,
      isLocal = true,
      annotations = Map("foo" -> "bar"),
      identityProviderId = "idp-id-476fc5dd-6d6f-47af-b20c-8e3ebaeef0ab"
    )
```

2. You can also update the identity provider of a party. To do so, use the `update_idp` command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.update_idp(bobPartyId, sourceIdentityProviderId = idpId, targetIdentityProviderId = "")
```

### Find a party

To find a party, you can use the `list` command.

1. You can filter parties by identity provider. Otherwise, all parties hosted on the participant will be returned.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.parties.list(idpId)
    res11: Seq[parties.PartyDetails] = Vector(
      PartyDetails(
        party = bob::12201ff69b1d...,
        isLocal = false,
        annotations = Map(),
        identityProviderId = ""
      ),
      PartyDetails(
        party = participant1::12201ff69b1d...,
        isLocal = false,
        annotations = Map(),
        identityProviderId = ""
      )
    )
```

## Onboard a new party via the admin API

If you need finer control when allocating a party, use the Admin API. To onboard a new party to a Participant Node, follow these steps:

1. Define a name for the Party (same rules as explained above). For example, we want to host the Party `alice`.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = "alice"
    alice : String = "alice"
```

2. Define an optional namespace. By default, Alice will use the namespace of the participant from whom you submit the command.

For more information on namespaces, refer to the Namespaces documentation.

3. Specify an optional Synchronizer alias to which the party should be allocated. The participant must be connected to this Synchronizer. You may omit this parameter if the participant is connected to only one Synchronizer, otherwise the party needs to be enabled on each synchronizer explicitly.

4. Enable the Party on this participant

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.enable(alice, synchronizer = Some("my-synchronizer"))
    res13: PartyId = alice::12201ff69b1d...
```

5. Verify that the party has been onboarded.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice", filterParticipant = participant1.filterString)
    res14: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
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

6. If you want to onboard the party on a second Synchronizer, you can do so by running the `enable` command again with a different Synchronizer alias.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.enable("alice", synchronizer = Some("my-second-synchronizer"))
    res15: PartyId = alice::12201ff69b1d...
```

### Find a party

To find a party, you can use the `list` command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice")
    res16: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
        participants = Vector(
          ParticipantSynchronizers(
            participant = PAR::participant1::12201ff69b1d...,
            synchronizers = Vector(
              SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission),
              SynchronizerPermission(synchronizerId = acme::122054fe9ea4..., permission = Submission)
            )
          )
        )
      )
    )
```

You can also filter by Participant Node and Synchronizers.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of("my-synchronizer")
    synchronizerId : SynchronizerId = da::122032922613...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list("alice", filterParticipant = participant1.filterString, synchronizerIds = Set(synchronizerId))
    res18: Seq[ListPartiesResult] = Vector(
      ListPartiesResult(
        partyResult = alice::12201ff69b1d...,
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

### Disable a party

<Warning>
  Disabling a party is not currently supported and is considered a dangerous operation.
</Warning>

If you are certain about what you are doing, you can disable a party on a specific Synchronizer using the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.disable(alicePartyId, synchronizer = Some("my-synchronizer"))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.disable(alicePartyId, synchronizer = Some("my-second-synchronizer"))
```

## Multi-hosted parties

A *multi-hosted party* is a party which is hosted on more than one participant. This poses the question how you can replicate a party from one participant to another?

The simplest and safest way to multi-host a party is only available to you while the party has not been involved in any Daml transaction. Otherwise, you have to perform an offline party replication procedure.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/operate/parties/party_replication.rst" hash="3d2e1e44" */}

# Party replication

*Party replication* is the process of duplicating an existing party onto an additional participant **within a single synchronizer**. In this process, the participant that already hosts the party is called the *source* participant, while the new participant is called the *target* participant.

The operational procedure differs substantially in complexity and risk depending on whether the party you replicate has already been involved in any Daml transaction.

Therefore, onboard your party on a participant, and **before you use the party** replicate it to other participants following the simple party replication steps.

Otherwise, you must apply an offline party replication procedure.

<Note>
  **Party replication** is different from **party migration**. A party migration includes an additional final step, that is removing (or *offboarding*) the party from its original participant.

  Party offboarding, and thus party migration, is currently not supported.
</Note>

## Party replication authorization

### How authorization works

Both the party and the new hosting participant must grant their consent by issuing each a party-to-participant mapping topology transaction. This ensures mutual agreement for the party replication.

### External parties

For external parties, changes to the party's topology must be explicitly authorized with a signature of the external party's namespace key. Whenever in the how-to authorization from the party is required, the distinction will be made between *local* and *external* parties. The procedure for external parties will refer to an abstract function authorizing updates to the party's party-to-participant mapping:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
class HostingParticipant:
    participant_uid: str
    permission: Enums.ParticipantPermission

def update_external_party_hosting(
    party_id: str,
    synchronizer_id: str,
    confirming_threshold: int,
    hosting_participants_add_or_update: [HostingParticipant]
)
```

An example implementation of this function is given in the external party onboarding documentation. The implementation additionally takes the private key of the party's namespace and a gRPC channel connected to the admin API of one of the party's confirming nodes. Those have been omitted in the function declared above for conciseness.

When the `source` participant is used in this how-to for actions other than authorizing topology changes, one of the existing confirming participants of the external party must be used.

### Parties with multiple owners

When a party is owned by a group of members in a decentralized namespace, a minimum number (a defined threshold) of those owners must approve the new hosting arrangement. This threshold is met once enough individual owners each issue their own party-to-participant mapping topology transaction.

### Activation

Completing the mutual authorization process *activates* the party on the target participant.

## Simple party replication

The simplest and safest way to replicate a party is to do so **before** it becomes a stakeholder in any contract.

<Warning>
  If a party has already participated in any Daml transaction, you must use offline party replication instead.
</Warning>

The simple party replication consists of these steps, follow them **in the order** they are listed:

1. Create the party, either in the namespace of a participant or in a dedicated namespace.
2. Vet packages.
3. Authorize one or more additional participants to host the party.
4. Use the party.

The following demonstrates these steps using two participants:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val source = participant1
    source : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant1'
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val target = participant2
    target : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant2'
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = source.synchronizers.id_of("mysynchronizer")
    synchronizerId : SynchronizerId = da::1220a82692ab...
```

### 1. Create party

Create a party Alice:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = source.parties.enable("Alice", synchronizer = Some("mysynchronizer"))
    alice : PartyId = Alice::12201ff69b1d...
```

<Note>
  In this example, the **local party Alice** is owned by the `source` participant, which is a simplification. It means that Alice is registered in the participant's namespace, but it is not a requirement.

  Alternatively, you can create the party in its own dedicated namespace, or create an external party.
</Note>

### 2. Vet packages

Vet packages on the target participant(s) **before** proceeding.

<Note>
  If you are unfamiliar with this process, read this general explanation of package vetting.
</Note>

### 3. Multi-host party

Party Alice needs to agree to be hosted on the target participant.

Because the source participant owns party Alice, you need to issue the party-to-participant mapping topology transaction on the `source` participant.

#### Authorize hosting update on the source participant

Local Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
        @ source.topology.party_to_participant_mappings
            .propose_delta(
              party = alice,
              adds = Seq(target.id -> ParticipantPermission.Submission),
              store = synchronizerId,
            )
            res5: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
              TopologyTransaction(
                PartyToParticipant(
                  partyId = Alice::12201ff69b1d...,
                  participants = Map(
                    PAR::participant1::12201ff69b1d... -> Submission,
                    PAR::participant2::1220a4d7463b... -> Submission
                  )
                ),
                serial = 2,
                operation = Replace,
                hash = SHA-256:20eef8c6481f...
              ),
              signatures = 12201ff69b1d...,
              proposal
            )
```

A participant can host a party with different permissions. In this example, the target participant will host party Alice with submission permission, that is party Alice can submit Daml transactions on it.

External Party

The onboarding process for external parties demonstrates how to declare the hosting relationship of the party during the creation of the party, including hosting on multiple nodes (multi-hosted external party). Unlike local parties who are always first hosted on a single node, and therefore always need to amend their party-to-participant mapping after the fact to be multi-hosted, external parties can do this in one step during the onboarding process. See onboarding process for more details.

#### Authorize hosting update on the target participant

To complete the process, also the target participant needs to agree to newly host Alice. Therefore, you need to issue the **same** party-to-participant mapping topology transaction on the `target` participant:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.topology.party_to_participant_mappings
    .propose_delta(
      party = alice,
      adds = Seq(target.id -> ParticipantPermission.Submission),
      store = synchronizerId,
    )
    res6: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Submission,
            PAR::participant2::1220a4d7463b... -> Submission
          )
        ),
        serial = 2,
        operation = Replace,
        hash = SHA-256:20eef8c6481f...
      ),
      signatures = 1220a4d7463b...,
      proposal
    )
```

<Note>
  The participant permission here must be the same as in the previous step. For external parties in particular this must be either `Confirmation` or `Observation`.
</Note>

Once the party-to-participant mapping takes effect, the replication is complete. This results in party Alice being multi-hosted on both the `source` and `target` participants.

To replicate Alice to more participants, repeat the procedure by first vetting the packages on a `newTarget` participant. Then, perform the replication again using the original `source` and `newTarget` participants.

### 3.a Replicate party with simultaneous confirmation threshold change (Variant to 3)

<Note>
  For **external parties**, the threshold is defined during the onboarding process already, so this section is not relevant to them.
</Note>

To change a party's confirmation threshold, you must use a different procedure for proposing the party-to-participant mapping than previously shown.

This alternative method allows you to perform the replication and update the threshold in a single operation.

The following example continues from the previous one, demonstrating how to replicate party Alice from the `source` participant to the `newTarget` participant while simultaneously setting the confirmation threshold to three. This operation also sets the participant permission to confirmation for all three participants that will be hosting Alice.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val newTarget = participant3
    newTarget : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant3'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val hostingParticipants = Seq(source, target, newTarget)
    hostingParticipants : Seq[com.digitalasset.canton.console.LocalParticipantReference] = List(Participant 'participant1', Participant 'participant2', Participant 'participant3')
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.topology.party_to_participant_mappings
    .propose(
      alice,
      newParticipants = hostingParticipants.map(_.id -> ParticipantPermission.Confirmation),
      threshold = PositiveInt.three,
      store = synchronizerId,
    )
    res9: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          threshold = 3,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Confirmation,
            PAR::participant2::1220a4d7463b... -> Confirmation,
            PAR::participant3::1220d6908163... -> Confirmation
          )
        ),
        serial = 3,
        operation = Replace,
        hash = SHA-256:7249f1511e32...
      ),
      signatures = 12201ff69b1d...,
      proposal
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ newTarget.topology.party_to_participant_mappings
    .propose(
      alice,
      newParticipants = hostingParticipants.map(_.id -> ParticipantPermission.Confirmation),
      threshold = PositiveInt.three,
      store = synchronizerId,
    )
    res10: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          threshold = 3,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Confirmation,
            PAR::participant2::1220a4d7463b... -> Confirmation,
            PAR::participant3::1220d6908163... -> Confirmation
          )
        ),
        serial = 3,
        operation = Replace,
        hash = SHA-256:7249f1511e32...
      ),
      signatures = 1220d6908163...,
      proposal
    )
```

## Offline party replication

Offline party replication is a multi-step, manual process.

Before replication can start, both the target participant and the party itself must explicitly consent to the new hosting arrangement.

Afterwards, the replication consists of exporting the party's Active Contract Set (ACS) from a source participant, and importing it to the target participant.

<Note>
  * Connect a single Canton console to both the source and target participants to export and import the party's ACS file using a single physical machine or environment. Otherwise, you need to securely transfer the ACS export file to the place where you import it to the target participant.
  * Offline party replication requires you to disconnect the target participant from all synchronizers before importing the party's ACS. Hence the name *offline* party replication.
  * While you onboard the party on the target participant you may detect ACS commitment mismatches. This is expected and resolves itself in time; ignore such errors during the party replication procedure.
</Note>

<Warning>
  **Be advised: You must back up the target participant before you start the ACS import!**

  This ensures you have a clean recovery point if the ACS import is interrupted (crash, unintended node restart, etc.), or when you otherwise were unable to follow this manual operational steps to completion. Having this backup allows you to safely reset the target participant and **still complete the ongoing offline party replication**.
</Warning>

## Offline party replication steps

These are the steps, which you must perform in **the exact order** they are listed:

1. **Target: Package Vetting** – Ensure the target participant vets all required packages.
2. **Source: Data Retention** - Ensure the source participant retains data long enough for the export.
3. **Target: Authorization** - Target participant authorizes new hosting with the onboarding flag set.
4. **Target: Isolation** - Disconnect from all synchronizers and disable auto-reconnect upon restart.
5. **Source: Party Authorization** - Party authorizes the replication with the onboarding flag set.
6. **Source: ACS Export** - The participant currently hosting the party exports the ACS.
7. **Target: Backup** - Back up the target participant before starting the ACS import.
8. **Target: ACS Import** - The target participant imports the ACS.
9. **Target: Reconnect** - The target participant reconnects to the synchronizers.
10. **Target: Onboarding Flag Clearance** - The target participant issues the onboarding flag clearance.

<Warning>
  Offline party replication must be performed with care, strictly following the documented **steps in order**. Not following the outlined operational flow will result in errors potentially requiring significant manual correction.

  This documentation provides a guide. Your environment may require adjustments. Test thoroughly in a test environment before production use.
</Warning>

### Scenario description

The following steps show how to replicate party `alice` from the `source` participant to a new `target` participant on the synchronizer `mysynchronizer`. The `source` can be any participant already hosting the party.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val source = participant1
    source : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant1'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val target = participant2
    target : com.digitalasset.canton.console.LocalParticipantReference = Participant 'participant2'
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val alice = source.parties.enable("Alice", synchronizer = Some("mysynchronizer")) // This command creates a local party. For external parties see the external party onboarding documentation (link found above in this page)
    alice : PartyId = Alice::12201ff69b1d...
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = source.synchronizers.id_of("mysynchronizer")
    synchronizerId : SynchronizerId = da::1220a82692ab...
```

### 1. Vet packages

Ensure the target participant vets all packages associated with contracts where the party is a stakeholder.

The party `alice` uses the package `CantonExamples` which is vetted on the `source` participant but not yet on the `target` participant.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mainPackageId = source.dars.list(filterName = "CantonExamples").head.mainPackageId
    mainPackageId : String = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.topology.vetted_packages.list()
    .filter(_.item.packages.exists(_.packageId == mainPackageId))
    .map(r => (r.context.storeId, r.item.participantId))
    res6: Seq[(TopologyStoreId, ParticipantId)] = Vector(
      (Synchronizer(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant1::12201ff69b1d...)
    )
```

Hence, upload the missing DAR package to the `target` participant.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.dars.upload("dars/CantonExamples.dar")
    res7: String = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.topology.vetted_packages.list()
    .filter(_.item.packages.exists(_.packageId == mainPackageId))
    .map(r => (r.context.storeId, r.item.participantId))
    res8: Seq[(TopologyStoreId, ParticipantId)] = Vector(
      (Synchronizer(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant1::12201ff69b1d...),
      (Synchronizer(id = Right(value = da::1220a82692ab...::35-0)), PAR::participant2::1220a4d7463b...)
    )
```

### 2. Data Retention

Ensure that the retention period on the source participant is long enough to cover the entire duration between the following two events:

1. The party-to-participant mapping topology transaction becoming effective.
2. The completion of the ACS export from the source participant.

If you are unsure whether the current retention period is sufficient, or as an additional precaution, you should temporarily disable automatic pruning on the source participant.

Retrieve the current automatic pruning schedule. This command returns `None` if no schedule is set.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val pruningSchedule = source.pruning.get_schedule()
    pruningSchedule : Option[PruningSchedule] = Some(value = PruningSchedule(cron = "0 0 20 * * ?", maxDuration = 2h, retention = 720h))
```

Clear the pruning schedule, disabling the automatic pruning on the `source` node.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.pruning.clear_schedule()
```

<Warning>
  Manual pruning cannot be programmatically disabled on the `source` participant. Coordinate closely with other operators and ensure that no external automation triggers pruning until the ACS export is complete.
</Warning>

### 3. Authorize new hosting on the target participant

First, have the `target` participant agree to host party Alice with the desired participant permission (*observation* in this example).

<Warning>
  Please ensure the onboarding flag is set with `requiresPartyToBeOnboarded = true`.
</Warning>

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val proposal = target.topology.party_to_participant_mappings
    .propose_delta(
      party = alice,
      adds = Seq((target.id, ParticipantPermission.Observation)),
      store = synchronizerId,
      requiresPartyToBeOnboarded = true
    )
    proposal : SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          partyId = Alice::12201ff69b1d...,
          participants = Map(
            PAR::participant1::12201ff69b1d... -> Submission,
            PAR::participant2::1220a4d7463b... -> Observation(onboarding)
          )
        ),
        serial = 2,
        operation = Replace,
        hash = SHA-256:4fc27cf93b27...
      ),
      signatures = 1220a4d7463b...,
      proposal
    )
```

### 4. Disconnect target participant from all synchronizers

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.disconnect_all()
```

### 5. Disable auto-reconnect on target participant

Ensure the target participant does not automatically reconnect to the synchronizer upon restart.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.config("mysynchronizer")
    res13: Option[SynchronizerConnectionConfig] = Some(
      value = SynchronizerConnectionConfig(
        synchronizer = Synchronizer 'mysynchronizer',
        sequencerConnections = SequencerConnections(
          connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
            sequencerAlias = Sequencer 'sequencer1',
            sequencerId = SEQ::sequencer1::1220cb0a22fb...,
            endpoints = http://127.0.0.1:30197
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 1, patience = 0s),
          sequencer connection pool delays = SequencerConnectionPoolDelays(
            minRestartDelay = 0.01s,
            maxRestartDelay = 10s,
            warnValidationDelay = 20s,
            subscriptionRequestDelay = 1s
          )
        ),
        manualConnect = false
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.modify("mysynchronizer", _.copy(manualConnect=true))
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.config("mysynchronizer")
    res15: Option[SynchronizerConnectionConfig] = Some(
      value = SynchronizerConnectionConfig(
        synchronizer = Synchronizer 'mysynchronizer',
        sequencerConnections = SequencerConnections(
          connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
            sequencerAlias = Sequencer 'sequencer1',
            sequencerId = SEQ::sequencer1::1220cb0a22fb...,
            endpoints = http://127.0.0.1:30197
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 1, patience = 0s),
          sequencer connection pool delays = SequencerConnectionPoolDelays(
            minRestartDelay = 0.01s,
            maxRestartDelay = 10s,
            warnValidationDelay = 20s,
            subscriptionRequestDelay = 1s
          )
        ),
        manualConnect = true
      )
    )
```

### 6. Authorize new hosting for the party

To later *find* the ledger offset of the topology transaction which authorizes the new hosting arrangement, take the current ledger end offset on the `source` participant as a starting point:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val beforeActivationOffset = source.ledger_api.state.end()
    beforeActivationOffset : Long = 23L
```

**Only after** the target participant has been disconnected from all synchronizers, have party Alice agree to be hosted on it.

<Warning>
  Again, please ensure the onboarding flag is set with `requiresPartyToBeOnboarded = true` for a local party, and with `onboarding = HostingParticipant.Onboarding()` for external party.
</Warning>

Local Party

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
        @ source.topology.party_to_participant_mappings
            .propose_delta(
              party = alice,
              adds = Seq((target.id, ParticipantPermission.Observation)),
              store = synchronizerId,
              requiresPartyToBeOnboarded = true
            )
            res17: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
              TopologyTransaction(
                PartyToParticipant(
                  partyId = Alice::12201ff69b1d...,
                  participants = Map(
                    PAR::participant1::12201ff69b1d... -> Submission,
                    PAR::participant2::1220a4d7463b... -> Observation(onboarding)
                  )
                ),
                serial = 2,
                operation = Replace,
                hash = SHA-256:4fc27cf93b27...
              ),
              signatures = 12201ff69b1d...,
              proposal
            )
```

External Party

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
update_external_party_hosting(
    party_id = alice,
    synchronizer_id = synchronizerId,
    confirming_threshold = None, # Keep current threshold
    hosting_participants_add_or_update: [
        HostingParticipant(participant_uid = target.id, ParticipantPermission.Observation, onboarding = HostingParticipant.Onboarding())
    ]
)
```

### 7. Export ACS

Export Alice's ACS from the `source` participant.

The following command finds internally the ledger offset where party Alice is activated on the `target` participant, starting the search from `beginOffsetExclusive`.

It then exports Alice's ACS from the `source` participant at that exact offset, and stores it in the export file named `party_replication.alice.acs.gz`.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.parties
    .export_party_acs(
      party = alice,
      synchronizerId = synchronizerId,
      targetParticipantId = target.id,
      beginOffsetExclusive = beforeActivationOffset,
      exportFilePath = "party_replication.alice.acs.gz",
    )
```

### 8. Optional: Re-enable automatic pruning

If you previously disabled automatic pruning on the `source` participant by following the data retention step, you may now re-enable it.

Run the following command using the original configuration parameters you recorded before disabling the schedule:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ source.pruning.set_schedule("0 0 20 * * ?", 2.hours, 30.days)
```

### 9. Back up target participant

<Warning>
  **Please back up the target participant before importing the ACS!**
</Warning>

### 10. Import ACS

Import Alice's ACS in the `target` participant:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.parties.import_party_acs("party_replication.alice.acs.gz")
```

### 11. Reconnect target participant to synchronizer

To later *find* the ledger offset of the topology transaction where the new hosting arrangement on the `target` participant has been authorized, take the current ledger end offset:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val targetLedgerEnd = target.ledger_api.state.end()
    targetLedgerEnd : Long = 17L
```

Now, reconnect that `target` participant to the synchronizer.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.reconnect_local("mysynchronizer")
    res22: Boolean = true
```

### 12. Optional: Re-enable auto-reconnect on target participant

If you previously disabled auto-reconnect following the earlier step, you may now re-enable it. This is only necessary if the target participant was originally configured to reconnect automatically upon restart.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ target.synchronizers.modify("mysynchronizer", _.copy(manualConnect=false))
```

### 13. Clear the participant's onboarding flag

After the `target` participant has completed the ACS import and reconnected to the synchronizer, you must clear the onboarding flag. This signals that the participant is fully ready to host the party.

There is a dedicated command to accomplish the onboarding flag clearance. It will issue the topology transaction to clear the flag for you, but only when it is safe to do so.

The following command uses the `targetLedgerEnd` captured in the previous step as the starting point to internally locate the effective party-to-participant mapping transaction that has activated `alice` on the `target` participant.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val (onboarded, minimalSafeClearingTs) = target.parties
    .clear_party_onboarding_flag(alice, synchronizerId, targetLedgerEnd)
    (onboarded, minimalSafeClearingTs) : (Boolean, Option[com.digitalasset.canton.data.CantonTimestamp]) = (false, Some(value = 2026-01-26T22:32:51.738792Z))
```

The command returns a tuple indicating the status:

* `(true, None)`: The onboarding flag is cleared. Proceed to the next step.
* `(false, Some(CantonTimestamp))`: The onboarding flag is still set. Removal is safe only after the indicated timestamp.

If the onboarding flag is still set, you must wait at least until the indicated timestamp (`minimalSafeClearingTs`). Only then will calling this command actually result in a topology transaction to clear the onboarding flag, which becomes effective thereafter.

Because this command is idempotent, you can call it repeatedly. Thus, you may also poll this command until it confirms that the onboarding flag has been cleared. The following snippet demonstrates how this command can be polled.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(timeout = 2.minutes, maxWaitPeriod = 30.seconds) {
      val (onboarded, _) = target.parties
        .clear_party_onboarding_flag(alice, synchronizerId, targetLedgerEnd)
      onboarded
    }
```

<Note>
  The `timeout` is based on the default *decision timeout* of 1 minute.
</Note>

### Summary

You have successfully multi-hosted Alice on `source` and `target` participants.

{/* COPIED_END */}

# Decentralized party overview

A decentralized party combines three different features:

* Decentralization of topology management of the party: A `decentralized namespace` to ensure that any topology transaction for that party requires signatures from a threshold of keys.
* Decentralization of transaction confirmations for the party: A `party to participant mapping` containing multiple confirming participants and a threshold to ensure that transactions requiring confirmations from that party also require confirmation from a threshold of participant nodes.
* Decentralization of transaction submissions for the party: Optionally, a `party to key mapping` to support submitting transactions that require direct authorization of the external party, for example creating a contract that the party is a signatory on by signing the prepared transaction with a threshold of keys. If no party-to-key mapping is defined, then the initial contracts need to be created when the `party to participant` threshold is 1 (if this was ever the case), and a node has submission rights, not just confirmation rights.

## Setup a decentralized party

While the decentralized namespace, the party to participant mapping, and the party to key mapping can be configured fully independently, a common scenario is that a set of entities jointly control all three i.e. all three have the same number of members and the same threshold. The instructions here describe that setup with the three members being `alice`, `bob`, and `charlie`, who use `participant1`, `participant2`, and `participant3` respectively.

First generate the keys used for the decentralized namespace:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceNamespaceKey = participant1.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    aliceNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 1220adfbf95c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobNamespaceKey = participant2.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    bobNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 122002ef937c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieNamespaceKey = participant3.keys.secret.generate_signing_key("decentralized-party-namespace", SigningKeyUsage.NamespaceOnly)
    charlieNamespaceKey : SigningPublicKey = SigningPublicKey(
      id = 1220d99d5e7c...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceNamespace = Namespace(aliceNamespaceKey.fingerprint)
    aliceNamespace : Namespace = 1220adfbf95c...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobNamespace = Namespace(bobNamespaceKey.fingerprint)
    bobNamespace : Namespace = 122002ef937c...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieNamespace = Namespace(charlieNamespaceKey.fingerprint)
    charlieNamespace : Namespace = 1220d99d5e7c...
```

Next, each node publishes the namespace delegation for that key to the synchronizer. This makes the key known to all nodes connected to the synchronizer and allows it to be used in later transactions:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerId = participant1.synchronizers.id_of(com.digitalasset.canton.SynchronizerAlias.tryCreate("global"))
    synchronizerId : SynchronizerId = global::1220f622b718...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.namespace_delegations.propose_delegation(aliceNamespace, aliceNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res8: SignedTopologyTransaction[TopologyChangeOp, NamespaceDelegation] = SignedTopologyTransaction(
      TopologyTransaction(
        NamespaceDelegation(
          1220adfbf95c...,
          SigningPublicKey(
            id = 1220adfbf95c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:62b8ebbd68b9...
      ),
      signatures = 1220adfbf95c...
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.namespace_delegations.propose_delegation(bobNamespace, bobNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res9: SignedTopologyTransaction[TopologyChangeOp, NamespaceDelegation] = SignedTopologyTransaction(
      TopologyTransaction(
        NamespaceDelegation(
          122002ef937c...,
          SigningPublicKey(
            id = 122002ef937c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:5ab6abc4efc3...
      ),
      signatures = 122002ef937c...
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.topology.namespace_delegations.propose_delegation(charlieNamespace, charlieNamespaceKey, DelegationRestriction.CanSignAllMappings, store = synchronizerId)
    res10: SignedTopologyTransaction[TopologyChangeOp, NamespaceDelegation] = SignedTopologyTransaction(
      TopologyTransaction(
        NamespaceDelegation(
          1220d99d5e7c...,
          SigningPublicKey(
            id = 1220d99d5e7c...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c2668b45ce0b...
      ),
      signatures = 1220d99d5e7c...
    )
```

Once the namespace delegations are published, you can create the decentralized namespace definition. For this, each node needs to sign and publish the same topology transaction to the synchronizer. They also need to choose a threshold, which determines how many signatures from the owners of the decentralized namespace are required for a topology transaction to be authorized on behalf of the decentralized namespace. This example uses a threshold of two. Note that the threshold does not apply to the initial transaction that establishes the decentralized namespace. For that, signatures from all owners are required, not just a threshold. Once all nodes publish their signed transaction, the decentralized namespace transaction shows up in the `list` command:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val namespaceDef = DecentralizedNamespaceDefinition.tryCreate(DecentralizedNamespaceDefinition.computeNamespace(Set(aliceNamespace, bobNamespace, charlieNamespace)), PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Set, aliceNamespace, bobNamespace, charlieNamespace))
    namespaceDef : DecentralizedNamespaceDefinition = DecentralizedNamespaceDefinition(
      12204768b31e...,
      PositiveNumeric(2),
      Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res12: SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 1220adfbf95c...,
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res13: SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 122002ef937c...,
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.topology.decentralized_namespaces.propose(namespaceDef, store = synchronizerId)
    res14: SignedTopologyTransaction[TopologyChangeOp, DecentralizedNamespaceDefinition] = SignedTopologyTransaction(
      TopologyTransaction(
        DecentralizedNamespaceDefinition(
          12204768b31e...,
          PositiveNumeric(2),
          Set(1220adfbf95c..., 122002ef937c..., 1220d99d5e7c...)
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:c0631e86a278...
      ),
      signatures = 1220d99d5e7c...,
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant1.topology.decentralized_namespaces.list(synchronizerId, filterNamespace = namespaceDef.namespace.filterString).nonEmpty)
```

The next step is to set up the `PartyToParticipant` mapping. For this, you need to chose a prefix for the party. The full party ID is then `prefix::namespace`. This example uses `decentralized-party` as the prefix. You also need to specify the list of participants that should host that party, the permissions (this should be `Confirmation` for all nodes participating in consensus for that party, but you may have additional read-only nodes with `Observation` permissions), and a threshold. The threshold determines how many confirmations are required for the decentralized party. This example uses the same threshold of two used for the decentralized namespace. As for the decentralized namespace, each node independently publishes the transaction; once all of them publish their transactions it becomes valid and shows up in `list`:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val partyId = PartyId(UniqueIdentifier.tryCreate("decentralized-party", namespaceDef.namespace))
    partyId : PartyId = decentralized-party::12204768b31e...
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res17: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(12201ff69b1d..., 1220adfbf95c...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res18: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(122002ef937c..., 1220a4d7463b...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.topology.party_to_participant_mappings.propose(partyId, Seq((participant1, ParticipantPermission.Confirmation), (participant2, ParticipantPermission.Confirmation), (participant3, ParticipantPermission.Confirmation)), PositiveInt.tryCreate(2), store = synchronizerId)
    res19: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          decentralized-party::12204768b31e...,
          PositiveNumeric(2),
          Vector(
            HostingParticipant(PAR::participant1::12201ff69b1d..., Confirmation, false),
            HostingParticipant(PAR::participant2::1220a4d7463b..., Confirmation, false),
            HostingParticipant(PAR::participant3::1220d6908163..., Confirmation, false)
          ),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:7ae22b0af452...
      ),
      signatures = Seq(1220d6908163..., 1220d99d5e7c...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant3.topology.party_to_participant_mappings.list(synchronizerId, filterParty = partyId.filterString).nonEmpty)
```

The last (optional) step is to set up the party to key mapping. This allows submitting transactions directly as the decentralized party through aggregating signatures offline. It is possible to reuse the same keys here that are used for the decentralized namespace (provided you change the SigningKeyUsage to be less restrictive) but we use separate keys here:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val aliceDamlKey = participant1.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    aliceDamlKey : SigningPublicKey = SigningPublicKey(
      id = 12204d33ee39...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val bobDamlKey = participant2.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    bobDamlKey : SigningPublicKey = SigningPublicKey(
      id = 1220565ad7f7...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val charlieDamlKey = participant3.keys.secret.generate_signing_key("decentralized-party-daml-transactions", SigningKeyUsage.ProtocolOnly)
    charlieDamlKey : SigningPublicKey = SigningPublicKey(
      id = 1220f4dd56cb...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = Set(signing, proof-of-ownership)
    )
```

With the keys set up, you can now create the `PartyToKey` topology transaction. Use a threshold of two signatures again:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res24: SignedTopologyTransaction[TopologyChangeOp, PartyToKeyMapping] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(12204d33ee39..., 1220adfbf95c...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.topology.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res25: SignedTopologyTransaction[TopologyChangeOp, PartyToKeyMapping] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(122002ef937c..., 1220565ad7f7...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant3.topology.party_to_key_mappings.propose(partyId, PositiveInt.tryCreate(2), com.daml.nonempty.NonEmpty(Seq, aliceDamlKey, bobDamlKey, charlieDamlKey), store = synchronizerId, mustFullyAuthorize = false)
    res26: SignedTopologyTransaction[TopologyChangeOp, PartyToKeyMapping] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToKeyMapping(
          decentralized-party::12204768b31e...,
          SigningKeysWithThreshold(
            Set(
              SigningPublicKey(
                id = 12204d33ee39...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220565ad7f7...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              ),
              SigningPublicKey(
                id = 1220f4dd56cb...,
                format = DER-encoded X.509 SubjectPublicKeyInfo,
                keySpec = EC-Curve25519,
                usage = Set(signing, proof-of-ownership)
              )
            ),
            PositiveNumeric(2)
          )
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:82990ca6e9a5...
      ),
      signatures = Seq(1220d99d5e7c..., 1220f4dd56cb...),
      proposal
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ utils.retry_until_true(participant3.topology.party_to_key_mappings.list(store = synchronizerId, filterParty = partyId.filterString).nonEmpty)
```

With that, the party is fully set up and can be used.

## Changing the set of members

To add and remove members, the steps are the same: There is a threshold of the existing members and any new members must submit the three topology transactions. It is also possible to only add them to some, but not all, of the three mappings, but usually it makes sense to keep the three in sync.

Note that adding a member to `PartyToParticipant` requires not just a topology transaction but a full party migration including an ACS export and import. The details of this are outside of the scope of this topic.

## Next steps

For details on how to submit an externally signed Daml transaction enabled by the `PartyToKey` mapping, refer to the external submission docs.

In this tutorial, both the namespace and protocol keys are held by the participant itself. It is also possible to hold them outside of the participant. The actual flow stays the same, but each submission of a topology transaction must be signed externally. Refer to the external topology signing docs for details on how to do this.

## Decentralized namespace computation

In the above example, we used `DecentralizedNamespaceDefinition.computeNamespace(Set(aliceNamespace, bobNamespace, charlieNamespace))` to compute the decentralized namespace from the namespaces of the initial owners. Note that only the initial owners matter here, the decentralized namespace does not change as owners get added or removed.

However, in some cases you might not run this from a Canton console (for example because you are working directly against the topology gRPC APIs) or need to compute the namespace yourself for other reasons. For those cases, we document how to compute it in Python here:

lexicographic ordering on namespaces:

```python theme={"theme":{"light":"github-light","dark":"github-dark"}}
def compute_decentralized_namespace(owners):
    builder = hashlib.sha256()
    # hash purpose prefix
    builder.update((37).to_bytes(4))
    for owner in sorted(owners):
        # namespace length
        builder.update(len(owner).to_bytes(4))
        builder.update(owner.encode("utf-8"))
    # 1220 is the Canton prefix for sha256 hashes
    return f"1220{builder.hexdigest()}"
```

{/* COPIED_END */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
