---
title: "Transaction Failures"
slug: "global-synchronizer-troubleshooting-guide-transaction-failures"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/transaction-failures.md"
source_title: "Transaction Failures"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - transaction-failures
---

# Transaction Failures

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Transaction Failures

> Diagnosing authorization errors, package vetting failures, and transaction timeouts

Transaction failures on the Global Synchronizer produce specific error codes that point to the root cause. This page covers the three most common categories: authorization errors, package vetting issues, and timeouts.

## Authorization Errors

Authorization failures appear when a party attempts an action it does not have rights to perform.

### Missing Signatories

```
INVALID_ARGUMENT: DAML_AUTHORIZATION_ERROR: ... requires authorizers <party-id> but only <other-party-id> were given
```

This means the command is missing a required signatory. Check:

* The template's signatory declaration in the Daml model
* Whether the submitting party is listed as a signatory on the contract
* If using multi-party submissions, that all required parties are included in the `actAs` list

### Wrong Party

If you see authorization errors right after onboarding, verify that your party ID matches what was registered:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list()
    res1: Seq[ListPartiesResult] = Vector(
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
      )
    )
```

Compare the output against the party ID in your application configuration. Party IDs are case-sensitive and include a fingerprint suffix (e.g., `validator::1220abcd...`).

## Package Vetting Issues

Package vetting ensures that all validators involved in a transaction agree on the Daml code being executed.

### DAR Not Uploaded

```
PACKAGE_NOT_FOUND: Could not find package <package-id>
```

Upload the required DAR to your validator:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Via REST API
curl -X POST "http://localhost/api/validator/v0/admin/dars" \
  -H "Authorization: Bearer $TOKEN" \
  -F "dar=@path/to/your-app.dar"
```

Or via Canton Console:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res2: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

### DAR Not Vetted on Counterparty

Even if your validator has the package, the other party's validator must also have it uploaded and vetted. If you see:

```
PACKAGE_SELECTION_FAILED: No package found for module <module-name>
```

Contact the counterparty's validator operator to upload and vet the same DAR. Both sides of a transaction must have the package available.

### Checking Vetting Status

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list()
    res3: Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult] = Vector(
      ListVettedPackagesResult(
        context = BaseResult(
          storeId = Synchronizer(id = Right(value = da::122032922613...::35-0)),
          validFrom = 2026-05-04T17:57:04.619144Z,
          validUntil = None,
          sequenced = 2026-05-04T17:57:04.369144Z,
          operation = Replace,
          transactionHash = TxHash(hash = SHA-256:0508a1646517...),
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
@ participant1.packages.list().filter(_.packageId.toString.nonEmpty)
    res4: Seq[PackageDescription] = Vector(
      PackageDescription(
        packageId = 9e70a8b3510d...,
        name = ghc-stdlib-DA-Internal-Template,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 114
      ),
      PackageDescription(
        packageId = 0e4a572ab1fb...,
        name = daml-prim-DA-Internal-Erased,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 98
      ),
      PackageDescription(
        packageId = 5aee9b21b8e9...,
        name = daml-prim-DA-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 17554
      ),
      PackageDescription(
        packageId = 8287d565fd2f...,
        name = CantonExamples,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:57:07.314002Z,
        size = 221449
      ),
      PackageDescription(
        packageId = a1fa18133ae4...,
        name = daml-stdlib-DA-Action-State-Type,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 593
      ),
      PackageDescription(
        packageId = 60c61c542207...,
        name = daml-stdlib-DA-Stack-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 1194
      ),
      PackageDescription(
        packageId = d095a2ccf6dd...,
        name = daml-stdlib-DA-Semigroup-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 426
      ),
      PackageDescription(
        packageId = ee33fb70918e...,
        name = daml-prim-DA-Exception-ArithmeticError,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 286
      ),
      PackageDescription(
        packageId = c280cc3ef501...,
        name = daml-stdlib-DA-Internal-Interface-AnyView-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 826
      ),
      PackageDescription(
        packageId = de2cc2f90eb5...,
        name = canton-builtin-admin-workflow-ping,
        version = 3.4.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 148192
      ),
      PackageDescription(
        packageId = 22ffcbab726e...,
        name = daml-prim,
        version = 0.0.0,
        uploadedAt = 2026-05-04T17:57:07.314002Z,
        size = 286794
      ),
      PackageDescription(
        packageId = e5411f3d75f0...,
        name = daml-prim-DA-Internal-NatSyn,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 109
      ),
      PackageDescription(
        packageId = 7adc4c2d07fa...,
        name = daml-stdlib-DA-Internal-Fail-Types,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 802
      ),
      PackageDescription(
        packageId = 86d888f34152...,
        name = daml-stdlib-DA-Internal-Down,
        version = 1.0.0,
        uploadedAt = 2026-05-04T17:56:51.624802Z,
        size = 258
      ),
    ...
```

## Timeout Problems

Timeouts indicate that a transaction did not complete within the allowed window. The mediator rejects the transaction when confirmations arrive too late.

### Traffic Exhaustion

```
MEDIATOR_SAYS_TX_TIMED_OUT: Rejected transaction as the mediator did not receive
sufficient confirmations within the expected timeframe
```

The most common cause of timeouts is exhausted traffic balance. Every transaction on the Global Synchronizer costs traffic, which you purchase with Canton Coin.

**Check your traffic balance:**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res5: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

If the balance is zero or near-zero, transactions will fail because the sequencer will not accept messages from your validator.

**Top up traffic:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
  -H "Authorization: Bearer $TOKEN"
```

**Enable auto-top-up** to prevent this from recurring. In your `validator-values.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
topup:
  enabled: true
  targetThroughput: 100000
  minTopupInterval: 10m
```

### Slow Database Queries

If your validator has sufficient traffic but transactions still time out, the database may be the bottleneck. Check for slow queries:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT pid, now() - pg_stat_activity.query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active' AND (now() - pg_stat_activity.query_start) > interval '5 seconds';
```

Large un-pruned tables cause query latency to increase over time. Enable pruning if you have not already:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

### Unresponsive Counterparty

The timeout error includes a `context` field listing `unresponsiveParties`. If the unresponsive party is not yours, the issue is on the counterparty's side -- their validator may be offline, under-funded for traffic, or experiencing its own problems. You cannot fix this directly; contact the counterparty's operator.

# Troubleshoot ACS Commitments

A participant node generates commitments to the active contract set (ACS) at regular intervals and exchanges them with its counter-participants. These commitments are used to establish non-repudiation on the common ACS state between participants, which is necessary for pruning the participant state. More information on commitments is available in the Pruning overview section.

## Error codes

A participant node logs warning messages when it detects a fork with the ACS of a counter-participant, when commitment computation is slow, or when received commitments show evidence of tampering. The following error codes are relevant for troubleshooting commitments, which are described in detail in the Error codes reference section:

* `ACS_COMMITMENT_ALARM`: This warning indicates malicious behavior. It occurs when an ACS commitment received from a counter-participant has an invalid signature, and when the participant receives two correctly signed but different commitments from the same counter-participant covering the same interval.
* `ACS_COMMITMENT_MISMATCH`: This warning indicates a fork in the common ACS state of the participant and one or more counter-participants. Please consult the runbook for inspecting commitment mismatches.
* `ACS_MISMATCH_NO_SHARED_CONTRACTS`: This warning indicates a special case of a fork, where a counter-participant sent a commitment for a period, while this participant does not think that there are any shared active contracts at the end of that period. The counter-participant will log an `ACS_COMMITMENT_MISMATCH`.
* `ACS_COMMITMENT_DEGRADATION`: This warning indicates that the participant node is behind some of its counter-participants in commitment computation, perhaps due to heavy load, and enters catch-up mode. Counter-participants might blacklist this participant, because it prevents them from pruning.
* `ACS_COMMITMENT_DEGRADATION_WITH_INEFFECTIVE_CONFIG`: This error code indicates that there is a degradation in commitment computation and the catch-up mode started, however the catch-up mode configuration is invalid and will not improve performance.

## Inspection Tools

Inspection tools enable the operator to understand to what extent its participant node agrees on its ACS state with its counter-participants. This is especially useful in two situations:

* The operator suspects that agreement is slower than it could or should be, e.g., because commitment monitoring alerts the operator of slowdowns when sending or receiving commitments. Inspection tools enable the operator to investigate the reason for the alert: Which counter-participants are behind, how far they are behind, or whether the participant itself is behind.
* There is a fork between the participant's ACS state and the state of one or more counter-participants. The participant node operator wants to understand the context of the fork, e.g., was the fork transient or not, does the fork span several counter-participants or just one, etc.

### Troubleshoot Slow Commitments

Assume that the operator observes via commitment monitoring that the participant's own commitments or a counter-participants' commitments are slow, or when the operator observes `ACS_COMMITMENT_DEGRADATION` warnings in the logs. The participant operator can use the command `commitments.lookup_received_acs_commitments` in the admin console (or via gRPC) to understand which counter-participant is ahead of its own participant and how far ahead it is. If several counter-participants are ahead, then the operator can try to correlate the periods of the counter-participants' commitments when the slowdown started with any changes in the participant's load, connectivity, etc.

Refine when addressing [#27011](https://github.com/DACH-NY/canton/issues/27011)

The following examples show how the operator of `participant1` inspects the received commitments from all counter-participants, for specific time periods on synchronizer `synchronizerId`, filtered by buffered commitments, which means that the participant received but has not computed the commitments for that period yet:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
import com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.{
  TimeRange,
  SynchronizerTimeRange,
}
participant1.commitments.lookup_received_acs_commitments(
  synchronizerTimeRanges = Seq(
    SynchronizerTimeRange(
      synchronizerId,
      Some(TimeRange(startTimestamp, endTimestamp)),
    )
  ),
  counterParticipants = Seq.empty,
  commitmentState = Seq(ReceivedCmtState.Buffered),
  verboseMode = true,
)
```

The output indicates that counter-participant `participant2` has sent commitments for the periods `1970-01-01T00:00:20Z to 1970-01-01T00:00:25Z` and `1970-01-01T00:00:25Z to 1970-01-01T00:00:30Z`, shows the received commitment hashes but not the send commitments because the participant has not computed them yet, and the state that these commitments are buffered.

It would be better to have the output of the commands generated from an actual integration test. Our docs tooling supports that (see SphinxDocumentationGenerator and its implementations). It might be worth to convert the tooling integration test accordingly. [#27011](https://github.com/DACH-NY/canton/issues/27011)

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Map(synchronizer1::122025ee4d83... ->
  Vector(
    ReceivedAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:20Z, toInclusive = 1970-01-01T00:00:25Z),PAR::participant2::122080ac62a3...,Some(SHA-256:9a5a5575876d...),None,Buffered),
    ReceivedAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:25Z, toInclusive = 1970-01-01T00:00:30Z),PAR::participant2::122080ac62a3...,Some(SHA-256:ac9142943183...),None,Buffered)
  )
)
```

As another example, assume that the operator observes an `ACS_COMMITMENT_MISMATCH` in the logs. The operator can use `commitments.lookup_sent_acs_commitments` in the admin console (or via gRPC) as a first step to inspect the mismatch. Concretely, the operator can use this command to understand with which counter-participants the participant has mismatches, and for what periods. The operator could then correlate the periods of the mismatches with, e.g., potential repair commands on the participant, or even uncover misbehaving counter-participants.

Refine when addressing [#27011](https://github.com/DACH-NY/canton/issues/27011)

The following examples show how the operator of `participant1` inspects the commitments sent to all counter-participants, for specific time periods on synchronizer `synchronizerId`, filtered by mismatches commitments:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
import com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.{
  TimeRange,
  SynchronizerTimeRange,
}
participant1.commitments.lookup_sent_acs_commitments(
  synchronizerTimeRanges = Seq(
    SynchronizerTimeRange(
      synchronizerId,
      Some(TimeRange(startTimestamp, endTimestamp)),
    )
  ),
  counterParticipants = Seq.empty,
  commitmentState = Seq(SentCmtState.Mismatch),
  verboseMode = true,
)
```

The output indicates that participant `participant1` has sent a commitment for the period `1970-01-01T00:00:40Z to 1970-01-01T00:00:45Z` to `participant2`, shows the commitment bytestring for the sent and the received commitment, which are different, hence the mismatch state.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Map(synchronizer1::1220087eeae4... ->
  Vector(
    SentAcsCmt(CommitmentPeriod(fromExclusive = 1970-01-01T00:00:40Z, toInclusive = 1970-01-01T00:00:45Z),PAR::participant2::12208336b38e...,Some(SHA-256:1d7e803bed16...),Some(SHA-256:c72753e6adc6...),Mismatch)
  )
)
```

## Handle slow counter-participant

If a participant operator observes that a counter-participant is slow in sending commitments, then the operator can opt not to wait for commitments from specific counter participants across multiple synchronizers. The configuration place takes effect immediately. Pruning the participant can continue even if the participant misses commitments from these counter-participants, or if the commitments it receives do not match. Although the participant does not expect commitments from these counter-participants, it still computes and sends commitments to them, and it does process potential received commitments, e.g., logs mismatch warnings.

<Note>
  Disabling waiting for commitments disregards these counter-participants w\.r.t. non-repudiation when the participant is pruned, but increases pruning resilience to failures and slowdowns of those counter-participants and/or the network.
</Note>

The following shows how the operator of `participant1` can mark as no-wait counter-participant `participant2` on synchronizer `synchronizerId1`. This command, as well as the commands in this section, also accept multiple counter-participants and synchronizers.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.commitments.set_no_wait_commitments_from(Seq(participant2), Seq(synchronizerId1))
```

The operator can also reset the no-wait configuration, i.e., wait for commitments, for counter-participant `participant2` on synchronizer `synchronizerId1` using a similar command:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.commitments.set_wait_commitments_from(Seq(participant2), Seq(synchronizerId1))
```

To retrieve the current no-wait configuration for synchronizer `synchronizerId1` and all participants known to `participant1` on synchronizer `synchronizerId1`, whether or not they are connected to `synchronizerId1`, the operator can use the command below. The command allows for filtering by specific counter-participants and/or synchronizers.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
val (participant1FilterNoWaitList, participant1FilterWaitList) =
  participant1.commitments.get_wait_commitments_config_from(Seq(synchronizer1Id), Seq.empty)
```

The output shows that `participant2` is marked as no-wait on `synchronizerId1` for `participant1`, and that there are no participants from whom `participant1` currently waits for commitments on `synchronizerId1`.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
(Vector
  (NoWaitCommitments
    (no-wait counter-participant = PAR::participant2::12206a279664..., synchronizers = synchronizer1::1220034cf0b0...)
  ),
Vector()
)
```

<Note>
  A participant added to the no-wait will not affect the *Default* or *Distinguished* counter-participant latency monitoring.
</Note>

## Handle slow commitment computation

Catch-up mode is a behavior that automatically trigger when a participants detects itself being falling behind. The synchronizer operator can configure catch-up mode on a per-synchronizer basis.

Once a participant detects itself being a number of periods behind (`nrIntervalsToTriggerCatchUp` with default value 2), then it activates skipping periods (`catchUpIntervalSkip` with default value 5) in order to perform less computation and thereby catch up. This does mean that all periods in between will not be subject to fork detection and only the interval skip will be compared. If no forks are detected at the skip, then any potential forks have resolved themselves anyway.

An alternative configuration in the synchronizer is `reconciliationInterval` (default value one minute), this dictates how often the participant perform the commitment exchange with counter participants. A lower value means more frequent and quicker fork detection. A higher value means less computation, but longer time before noticing a fork. Catch-up mode is directly affected by the `reconciliationInterval`. With default values, catch-up will trigger once a participant observes itself being 10 minutes behind (`reconciliationInterval` \* `nrIntervalsToTriggerCatchUp` \* `catchUpIntervalSkip`).

To configure the parameters above, please refer to the synchronizer management section on Manage dynamic synchronizer parameters.

### Troubleshoot Forks (Commitment Mismatches)

When the operator observes an `ACS_COMMITMENT_MISMATCH` in the logs, it indicates that the participant's ACS state diverged from the counter-participant's state. In other words, the two participants do not agree on the shared contracts. In the example below, `participant1` received a commitment from `participant2` for the period `1970-01-01T00:01:35Z to 1970-01-01T00:01:40Z` on `synchronizer1`, but the received commitment does not match the local commitment for that period.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
ACS_COMMITMENT_MISMATCH(5,246a29fb): The local commitment does not match the remote commitment
err-context:
  {
    local=Vector((CommitmentPeriod(fromExclusive = 1970-01-01T00:01:35Z, toInclusive = 1970-01-01T00:01:40Z), SHA-256:cfd7fd917fb9...)),
    remote=AcsCommitment(
      synchronizerId = synchronizer1::1220b9dd1a9f199b898522ec31a8ce3ff098a7ce05b0cd3ce76e0a544959fe58c8e9::34-0,
      sender = PAR::participant2::1220b2063ef1...,
      counterParticipant = PAR::participant1::1220cc59a221...,
      period = CommitmentPeriod(fromExclusive = 1970-01-01T00:01:35Z, toInclusive = 1970-01-01T00:01:40Z),
      commitment = SHA-256:e2c0cf0361cb...
    ),
    synchronizerId=synchronizer1::1220b9dd1a9f...
  }
```

<Note>
  Troubleshooting a mismatch requires that the two participant operators collaborate in order to identify what caused the mismatch. Mismatches can happen due to misconfiguration, e.g., when changing contract stores via the repair service, bugs, or malicious behavior. The non-repudiation section provides more detail on forks. For example, one of the participants might not know of a contract the other participant claims to be shared at the mismatch timestamp, or it might have known about the contract in the past but deactivated it before the mismatch timestamp, or or it might have that contract active but on a different synchronizer. Thus, the outcome of troubleshooting a mismatch gives the type of mismatch for each contract that only one participant believes it shares with the other participant.
</Note>

If the participants are mutually distrustful, they may want to validate the data they exchange during the troubleshooting process. Thus, depending on the trust level, these validation steps are optional.

We troubleshoot the mismatch as follows:

1. **Inspect the local shared contract metadata** This data represents the set of contracts that the `participant1` believes it shares with the counter-participant `participant2` at timestamp `1970-01-01T00:01:40Z` on `synchronizer1`. The operator of `participant1` can obtain this set by first obtaining the commitment it sent using lookup\_sent\_acs\_commitments, and then opening the commitment using the command `commitments.open_commitment` in the admin console (or via gRPC) as follows:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val sentCommitmentP1 = participant1.commitments
     .lookup_sent_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant2.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .sentCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val contractsAndReassignmentCountersP1 = participant1.commitments.open_commitment(
     commitment = sentCommitmentP1,
     physicalSynchronizerId = synchronizerId1,
     timestamp = mismatchTimestamp,
     counterParticipant = participant2,
     outputFile = Some(openCmtLocalFilename),
   )
   ```

   where `mismatchTimestamp = 1970-01-01T00:01:40Z`. If the local and the remote commitments have different period ends, we take the period end of the local commitment.

   When the operator uses the console command, the operator can choose to optionally write the output into a file, in this case `openCmtLocalFilename`, which is useful for the next steps. The output in the `openCmtLocalFilename` file contains the local shared contract IDs and their reassignment counters:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {"cid":"00749df26491a08f246d4cd262307ea0c9676adde3861d6d2c80e081ddd8160430ca1112202942877d5c9e8d6f79d9167f9841fd4fd092ed2c97c47459c2c40f18a236b239","reassignmentCounter":"0"}
   {"cid":"008403c268ce244fda036c7916b1f33885df153e6a4b0f60e3c8724277100b4362ca111220f5a052b1c66024133c844a8e6f67dec9a1d3c6e0cd3cb0023843b10cdeff4126","reassignmentCounter":"0"}
   {"cid":"002e46d505d569ad80638831c5ad043d281960121f8b6a564e18937819cf1c8536ca111220985ed1546f8a45e39626290d80d0640c8663ed13d078f9761b0e1e2bd0c99ec5","reassignmentCounter":"0"}
   {"cid":"00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1","reassignmentCounter":"0"}
   {"cid":"00e577eb32be4082705edcccc231657551b83bef6076fafcd0f3a89f63f09645f3ca1112208604884e3c2d4711bae0ab6178238b36de6ba1e5f5913be6dce2016e6371725a","reassignmentCounter":"0"}
   {"cid":"002d6217d1ea6ff05ca0d089a8988465197e6c5518a9f83cb0dc69611cf0572acbca1112202329ef987c25375e0130580e289df681581dc9439737cd53f3223cb22e7c2ff9","reassignmentCounter":"0"}
   ```

   <Note>
     The files used for commitment mismatch inspection use a `.json` format; for some files, each line is a `JSON` object, rather than the file as a whole. We recommend, nonetheless, to use the provided tooling for reading / writing these files, as the contents of the files might evolve.
   </Note>

2. **Inspect the counter-participant's shared contract metadata from the counter-participant** This data represents the set of contracts that the counter-participant believes it shares with the participant at timestamp `1970-01-01T00:01:40Z` on `synchronizer1`. The operator of `participant1` asks the operator of `participant2` to run `commitments.open_commitment`, which the counter-participant operator probably intends to do anyway, as it also observes a mismatch warning in its logs.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   val sentCommitmentP2 = participant2.commitments
     .lookup_sent_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant1.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .sentCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val contractsAndReassignmentCountersP2 = participant2.commitments.open_commitment(
     commitment = sentCommitmentP2,
     physicalSynchronizerId = synchronizerId1,
     timestamp = mismatchTimestamp,
     counterParticipant = participant1,
     outputFile = Some(openCmtRemoteFilename),
   )
   ```

   where this time the operator of `participant2` retrieves the commitment it sent to `participant1` at `mismatchTimestamp = 1970-01-01T00:01:40Z`. If the local and the remote commitments had different period ends, we'd take the period end of the remote commitment.

   As before, the output in the `openCmtRemoteFilename` file contains the local shared contract IDs and their reassignment counters:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {"cid":"00749df26491a08f246d4cd262307ea0c9676adde3861d6d2c80e081ddd8160430ca1112202942877d5c9e8d6f79d9167f9841fd4fd092ed2c97c47459c2c40f18a236b239","reassignmentCounter":"0"}
   {"cid":"008403c268ce244fda036c7916b1f33885df153e6a4b0f60e3c8724277100b4362ca111220f5a052b1c66024133c844a8e6f67dec9a1d3c6e0cd3cb0023843b10cdeff4126","reassignmentCounter":"0"}
   {"cid":"002e46d505d569ad80638831c5ad043d281960121f8b6a564e18937819cf1c8536ca111220985ed1546f8a45e39626290d80d0640c8663ed13d078f9761b0e1e2bd0c99ec5","reassignmentCounter":"0"}
   {"cid":"00e577eb32be4082705edcccc231657551b83bef6076fafcd0f3a89f63f09645f3ca1112208604884e3c2d4711bae0ab6178238b36de6ba1e5f5913be6dce2016e6371725a","reassignmentCounter":"0"}
   {"cid":"002d6217d1ea6ff05ca0d089a8988465197e6c5518a9f83cb0dc69611cf0572acbca1112202329ef987c25375e0130580e289df681581dc9439737cd53f3223cb22e7c2ff9","reassignmentCounter":"0"}
   ```

   The operator of `participant2` can send the `openCmtRemoteFilename` file to the operator of `participant1`.

3. **Optional: validate counter-participant data** The operator of `participant1` can validate that the contract metadata received from `participant2` matches the commitment received from `participant2`:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.integration.tests.util.CommitmentTestUtil.computeHashedCommitment
   import com.digitalasset.canton.participant.pruning.OpenCommitmentHelper
   val remoteContractsAndTransferCounters =
     OpenCommitmentHelper.readFromFile(openCmtRemoteFilename)
   val receivedCommitmentP1fromP2 = participant1.commitments
     .lookup_received_acs_commitments(
       synchronizerTimeRanges = Seq(
         SynchronizerTimeRange(
           synchronizerId1,
           Some(
             TimeRange(
               mismatchTimestamp.minusMillis(1),
               mismatchTimestamp,
             )
           ),
         )
       ),
       counterParticipants = Seq(participant2.id),
       commitmentState = Seq.empty,
       verboseMode = true,
     )(synchronizerId1)
     .head
     .receivedCommitment
     .getOrElse(throw new IllegalStateException("Commitment is empty"))
   val receivedOpenedCommitmentP1fromP2 =
     computeHashedCommitment(remoteContractsAndTransferCounters)
   if (receivedOpenedCommitmentP1fromP2 != receivedCommitmentP1fromP2)
     throw new InvalidRequestStateException(
       s"The commitment does not match the opened contract metadata!"
     )
   ```

   where `openCmtRemoteFilename` is the file the operator of `participant1` received from the operator of `participant2` in step 2.

   If this step fails, then the counter-participant sent either the wrong commitment, or the wrong contract metadata, or perhaps both. In this case, it appears that the operator of `participant1` cannot reliably identify the mismatch cause because it cannot trust the input of the operator of `participant2`, and should not proceed with the troubleshooting steps below.

4. **Identify mismatching contracts** The operator of `participant1` can identify the mismatching contracts by checking its own opened commitment output in the `openCmtLocalFilename` file from step 1 against the counter-participant's opened commitment output in the `openCmtRemoteFilename` file received in step 2.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.participant.pruning.CommitmentContractMetadata
   import com.digitalasset.canton.participant.pruning.OpenCommitmentHelper
   val contractsAndTransferCounters1 =
     OpenCommitmentHelper.readFromFile(openCmtLocalFilename)
   val contractsAndTransferCountersCounterParticipant1 =
     OpenCommitmentHelper.readFromFile(openCmtRemoteFilename)
   val mismatchingContracts = CommitmentContractMetadata.compare(
     contractsAndTransferCounters1,
     contractsAndTransferCountersCounterParticipant1,
   )
   mismatchingContracts.writeToFile(mismatchingContractsFilename)
   ```

   As shown in the code excerpt, the operator can optionally write the output into a file, in this case `mismatchingContractsFilename`, which is useful for the next step.

   The output shows the mismatch: There is one contract that only `participant1` considers active. The output would also show if `participant2` had contracts that it considers active but `participant1` does not, and if there are contracts that both participants consider active but with different reassignment counters.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {
     "cidsOnlyLocal": [
       "00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1"
     ],
     "cidsOnlyRemote": [],
     "differentReassignmentCounters": []
   }
   ```

5. **Inspect mismatch cause** The operator of `participant1` can analyze the source of the mismatches by inspecting why contract `00e773decfb7f537880972943980da..` is active. The operator can optionally write the output in a file, in this case `inspectContractsFilename`, which it can exchange with the operator of `participant2` if needed for repairing the ACS state.

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   import com.digitalasset.canton.participant.pruning.CommitmentInspectContract
   val mismatches = CompareCmtContracts.readFromFile(mismatchingContractsFilename)

   val inspectContracts = participant1.commitments.inspect_commitment_contracts(
     contracts = mismatches.cidsOnlyLocal ++ mismatches.differentReassignmentCounters,
     timestamp = mismatchTimestamp,
     expectedSynchronizerId = synchronizerId1,
     downloadPayload = true,
   )
   CommitmentInspectContract.writeToFile(inspectContractsFilename, inspectContracts)
   ```

   The command returns the contract states (created, assigned, unassigned, archived, unknown) of the given contracts on all synchronizers the participant knows from the beginning of time until the present time on each synchronizer. In this case, `inspectContractsFilename` contains the contract states of contract `00e773decfb7f537880972943980da..` on all synchronizers the participant knows:

   ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
   {
     "cid":"00f22bb479621372e70bc1b9d83ea0a6741282ab014319ef1a7c4ae0b82f442785ca1112207e6d62fda4b9ae58fdc686332b4c7c688814cab840283d1f3245d7fc6c026fd1",
     "activeOnExpectedSynchronizer":true,
     "contract":"CgMyLjES4QQKRQDKmKJSNKcVjBs2yEfu9TDXuGxVS8/FDK3F3QxK8tOs58oREiA3S1IQ7INuTTYMHjMRm/fNx6VaEaI/t61bwhf5XN5NexIOQ2FudG9uRXhhbXBsZXMaTApAODIwYTA5MjEzYzgyYmRlNjdmZjUxODEyMWViMTFhYjdjYTUwNTA3MTAzNDIyMDMzNzEyN2UyNjhkMTVkZWI1NhIDSW91GgNJb3Ui3AFq2QEKVgpUOlJwYXJ0aWNpcGFudDE6OjEyMjA4OWRlZjczZGEzYTAzOTkzMDIxZmFjM2Q1NDY5ZDQ5YWJmMzc1NWFhNzJlNTFhNzc0MTEwNWJlMjFmOWVlZGJlClYKVDpScGFydGljaXBhbnQyOjoxMjIwYjdhMzBmMDYwODIxNzU1YzZmNDFlNTg2MDU3NDBiZGE0NWM0ZjM5ZmEzMTVjODAwOThkYTNhZjAwM2FhNzFjOAohCh9qHQoSChAyDjEwMC4wMDAwMDAwMDAwCgcKBUIDVVNECgQKAloAKlJwYXJ0aWNpcGFudDE6OjEyMjA4OWRlZjczZGEzYTAzOTkzMDIxZmFjM2Q1NDY5ZDQ5YWJmMzc1NWFhNzJlNTFhNzc0MTEwNWJlMjFmOWVlZGJlMlJwYXJ0aWNpcGFudDI6OjEyMjBiN2EzMGYwNjA4MjE3NTVjNmY0MWU1ODYwNTc0MGJkYTQ1YzRmMzlmYTMxNWM4MDA5OGRhM2FmMDAzYWE3MWM4OQEtMQEAAAAAQioKJgokCAESICk3eHUEqY8nX3bxxmkk5wkSkfDtDxlKUI52dC38tZU5EB4=",
     "state":[
       {
         "synchronizerId":"synchronizer1::12207195bde33b4c24dac3f1d7105873ff6c6724d9160491386d17d97e910f3155e3",
         "contractState":{"$type":"ContractCreated"}
       }
     ]
   }
   ```

   The operator of `participant2` can perform the commands in steps 4 and 5 to inspect the mismatch cause on its side, exchange the results with the operator of `participant1`, and jointly identify the root cause of the mismatch.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
