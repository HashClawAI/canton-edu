---
title: "Canton Console Commands"
slug: "global-synchronizer-reference-canton-console-commands"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/canton-console-commands.md"
source_title: "Canton Console Commands"
tags:
  - global-synchronizer
  - reference
  - canton-console-commands
---

# Canton Console Commands

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Console Commands

> Canton admin console command reference: participant, mediator, sequencer, and topology commands.

<div id="canton_console_reference">
  <Note>
    split by participant and synchronizer, put shared commands in extend/participant section, and add a section for the synchronizer
  </Note>
</div>

# Console Commands

## Top-level Commands

The following commands are available for convenience:

<div id="exit" />

### `exit`

Leave the console.

<div id="help" />

### `help`

Help with console commands; type help("\<command>") for detailed help for \<command>.

<div id="bootstrap.decentralized_namespace" />

### `bootstrap.decentralized_namespace`

Bootstraps a decentralized namespace for the provided owners.

Returns the decentralized namespace, the fully authorized transaction of its definition, as well as all root certificates of the owners. This allows other nodes to import and fully validate the decentralized namespace definition. After this call has finished successfully, all of the owners have stored the co-owners' identity topology transactions as well as the fully authorized decentralized namespace definition in the specified topology store.

**Arguments**

* `owners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

**Returns:** `(com.digitalasset.canton.topology.Namespace, Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction])`

<div id="bootstrap.help" />

### `bootstrap.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="bootstrap.onboard_new_sequencer" />

### `bootstrap.onboard_new_sequencer`

Onboards a new Sequencer node.

Onboards a new Sequencer node using an existing node from the network.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `newSequencer`: `com.digitalasset.canton.console.SequencerReference`
* `existingSequencer`: `com.digitalasset.canton.console.SequencerReference`
* `synchronizerOwners`: `Set[com.digitalasset.canton.console.InstanceReference]`
* `customCommandTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `isBftSequencer`: `Boolean`

<div id="bootstrap.synchronizer" />

### `bootstrap.synchronizer`

Bootstraps a new synchronizer.

Bootstraps a new synchronizer with the given static synchronizer parameters and members. Any participants as synchronizer owners must still manually connect to the synchronizer afterwards.

Parameters: mediatorsToSequencers: map of mediator reference to a tuple of a sequence of sequencer references, the sequencer trust threshold and the liveness margin for the given mediator.

**Arguments**

* `synchronizerName`: `String`
* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `mediatorsToSequencers`: `Map[com.digitalasset.canton.console.MediatorReference,(Seq[com.digitalasset.canton.console.SequencerReference], com.digitalasset.canton.config.RequireTypes.PositiveInt, com.digitalasset.canton.config.RequireTypes.NonNegativeInt)]`
* `synchronizerOwners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `synchronizerThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `staticSynchronizerParameters`: `com.digitalasset.canton.admin.api.client.data.StaticSynchronizerParameters`
* `mediatorRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `mediatorThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `com.digitalasset.canton.topology.PhysicalSynchronizerId`

<div id="bootstrap.synchronizer_1" />

### `bootstrap.synchronizer_1`

Bootstraps a new synchronizer.

Bootstraps a new synchronizer with the given static synchronizer parameters and members. Any participants as synchronizer owners must still manually connect to the synchronizer afterwards.

**Arguments**

* `synchronizerName`: `String`
* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `mediators`: `Seq[com.digitalasset.canton.console.MediatorReference]`
* `synchronizerOwners`: `Seq[com.digitalasset.canton.console.InstanceReference]`
* `synchronizerThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `staticSynchronizerParameters`: `com.digitalasset.canton.admin.api.client.data.StaticSynchronizerParameters`
* `mediatorRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `mediatorThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `com.digitalasset.canton.topology.PhysicalSynchronizerId`

<div id="bootstrap.synchronizer_local" />

### `bootstrap.synchronizer_local`

Bootstraps a local synchronizer using default arguments.

This is a convenience method for bootstrapping a local synchronizer.The synchronizer will include all sequencers and mediators that are currently running.It will be owned by the sequencers, while the mediator threshold will be set to requireall mediators to confirm.

**Arguments**

* `synchronizerName`: `String`

**Returns:** `com.digitalasset.canton.topology.SynchronizerId`

<div id="console.command_timeout" />

### `console.command_timeout`

Yields the timeout for running console commands.

Yields the timeout for running console commands. When the timeout has elapsed, the console stops waiting for the command result. The command will continue running in the background.

**Returns:** `com.digitalasset.canton.config.NonNegativeDuration`

<div id="console.help" />

### `console.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="console.set_command_timeout" />

### `console.set_command_timeout`

Sets the timeout for running console commands.

Sets the timeout for running console commands. When the timeout has elapsed, the console stops waiting for the command result. The command will continue running in the background. The new timeout must be positive.

**Arguments**

* `newTimeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="mediators" />

### `mediators`

All mediator nodes (.all, .local, .remote).

<div id="nodes" />

### `nodes`

All nodes (.all, .local, .remote).

<div id="participants" />

### `participants`

All participant nodes (.all, .local, .remote).

<div id="sequencers" />

### `sequencers`

All sequencer nodes (.all, .local, .remote).

<div id="ledger_api_utils.create" />

### `ledger_api_utils.create`

Build create command.

**Arguments**

* `packageId`: `String`
* `module`: `String`
* `template`: `String`
* `arguments`: `Map[String,Any]`

**Returns:** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.exercise" />

### `ledger_api_utils.exercise`

Build exercise command from CreatedEvent.

**Arguments**

* `choice`: `String`
* `arguments`: `Map[String,Any]`
* `event`: `com.daml.ledger.api.v2.event.CreatedEvent`

**Returns:** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.exercise_1" />

### `ledger_api_utils.exercise_1`

Build exercise command.

**Arguments**

* `packageId`: `String`
* `module`: `String`
* `template`: `String`
* `choice`: `String`
* `arguments`: `Map[String,Any]`
* `contractId`: `String`

**Returns:** `com.daml.ledger.api.v2.commands.Command`

<div id="ledger_api_utils.help" />

### `ledger_api_utils.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="logging.get_level" />

### `logging.get_level`

Determine current logging level.

**Arguments**

* `loggerName`: `String`

**Returns:** `Option[ch.qos.logback.classic.Level]`

<div id="logging.help" />

### `logging.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="logging.last_error_trace" />

### `logging.last_error_trace`

Returns log events for an error with the same trace-id.

**Arguments**

* `traceId`: `String`

**Returns:** `Seq[String]`

<div id="logging.last_errors" />

### `logging.last_errors`

Returns the last errors (trace-id -> error event) that have been logged locally.

**Returns:** `Map[String,String]`

<div id="logging.set_level" />

### `logging.set_level`

Dynamically change log level (TRACE, DEBUG, INFO, WARN, ERROR, OFF, null).

**Arguments**

* `loggerName`: `String`
* `level`: `String`

<div id="mediator1" />

### `mediator1`

Manage local mediator 'mediator1'; type 'mediator1 help' or 'mediator1 help("\<methodName>")' for more help.

<div id="participant1" />

### `participant1`

Manage participant 'participant1'; type 'participant1 help' or 'participant1 help("\<methodName>")' for more help.

<div id="participant2" />

### `participant2`

Manage participant 'participant2'; type 'participant2 help' or 'participant2 help("\<methodName>")' for more help.

<div id="participant3" />

### `participant3`

Manage participant 'participant3'; type 'participant3 help' or 'participant3 help("\<methodName>")' for more help.

<div id="sequencer1" />

### `sequencer1`

Manage local sequencer 'sequencer1'; type 'sequencer1 help' or 'sequencer1 help("\<methodName>")' for more help.

<div id="utils.auto_close" />

### `utils.auto_close`

Register `AutoCloseable` object to be shutdown if Canton is shut down.

**Arguments**

* `closeable`: `AutoCloseable`

<div id="utils.cantonprocesslogger" />

### `utils.cantonprocesslogger`

A process logger that forwards process logs to the canton logs.

**Arguments**

* `tracedLogger`: `com.digitalasset.canton.logging.TracedLogger`

**Returns:** `scala.sys.process.ProcessLogger`

<div id="utils.generate_daml_script_participants_conf" />

### `utils.generate_daml_script_participants_conf`

Create a participants config for Daml script.

The generated config can be passed to `daml script` via the `participant-config` parameter. More information about the file format can be found in the documentation: It takes three arguments:

* file (default to "participant-config.json")
* useParticipantAlias (default to true): participant aliases are used instead of UIDs
* defaultParticipant (default to None): adds a default participant if provided

**Arguments**

* `file`: `Option[String]`
* `useParticipantAlias`: `Boolean`
* `defaultParticipant`: `Option[com.digitalasset.canton.console.ParticipantReference]`

**Returns:** `java.io.File`

<div id="utils.help" />

### `utils.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="utils.object_args" />

### `utils.object_args`

Reflective inspection of object arguments, handy to inspect case class objects.

Return the list field names of the given object. Helpful function when inspecting the return result.

**Arguments**

* `obj`: `T`

**Returns:** `List[String]`

<div id="utils.read_all_messages_from_file" />

### `utils.read_all_messages_from_file`

Reads several Protobuf messages from a file.

Fails with an exception, if the file can't be read or parsed.

**Arguments**

* `fileName`: `String`

**Returns:** `Seq[A]`

<div id="utils.read_byte_string_from_file" />

### `utils.read_byte_string_from_file`

Reads a ByteString from a file.

Fails with an exception, if the file can't be read.

**Arguments**

* `fileName`: `String`

**Returns:** `com.google.protobuf.ByteString`

<div id="utils.read_first_message_from_file" />

### `utils.read_first_message_from_file`

Reads a single Protobuf message from a file.

Fails with an exception, if the file can't be read or parsed.

**Arguments**

* `fileName`: `String`

**Returns:** `A`

<div id="utils.retry_until_true" />

### `utils.retry_until_true`

Wait for a condition to become true.

Wait `timeout` duration until `condition` becomes true. Retry evaluating `condition` with an exponentially increasing back-off up to `maxWaitPeriod` duration between retries.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `maxWaitPeriod`: `com.digitalasset.canton.config.NonNegativeDuration`
* `condition`: `=> Boolean`
* `failure`: `=> String`

**Returns:** `(condition: => Boolean, failure: => String): Unit`

<div id="utils.retry_until_true_1" />

### `utils.retry_until_true_1`

Wait for a condition to become true, using default timeouts.

Wait until condition becomes true, with a timeout taken from the parameters.timeouts.console.bounded configuration parameter.

**Arguments**

* `condition`: `=> Boolean`

<div id="utils.synchronize_topology" />

### `utils.synchronize_topology`

Wait until all topology changes have been effected on all accessible nodes.

**Arguments**

* `timeoutO`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="utils.type_args" />

### `utils.type_args`

Reflective inspection of type arguments, handy to inspect case class types.

Return the list of field names of the given type. Helpful function when creating new objects for requests.

**Returns:** `List[String]`

<div id="utils.write_to_file" />

### `utils.write_to_file`

Writes a ByteString to a file.

**Arguments**

* `data`: `com.google.protobuf.ByteString`
* `fileName`: `String`

<div id="utils.write_to_file_1" />

### `utils.write_to_file_1`

Writes a Protobuf message to a file.

**Arguments**

* `data`: `scalapb.GeneratedMessage`
* `fileName`: `String`

<div id="utils.write_to_file_2" />

### `utils.write_to_file_2`

Writes several Protobuf messages to a file.

**Arguments**

* `data`: `Seq[scalapb.GeneratedMessage]`
* `fileName`: `String`

## Participant Commands

<div id="clear_cache" />

### `clear_cache`

Clear locally cached variables.

Some commands cache values on the client side. Use this command to explicitly clear the caches of these values.

<div id="config" />

### `config`

Return participant config.

**Returns:** `com.digitalasset.canton.participant.config.ParticipantNodeConfig`

<div id="help_1" />

### `help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="id" />

### `id`

Yields the globally unique id of this participant. Throws an exception, if the id has not yet been allocated (e.g., the participant has not yet been started).

**Returns:** `com.digitalasset.canton.topology.ParticipantId`

<div id="is_initialized" />

### `is_initialized`

Check if the local instance is running and is fully initialized.

**Returns:** `Boolean`

<div id="is_running" />

### `is_running`

Check if the local instance is running.

**Returns:** `Boolean`

<div id="maybeid" />

### `maybeid`

Yields Some(id) of this participant if id present. Returns None, if the id has not yet been allocated (e.g., the participant has not yet been initialised).

**Returns:** `Option[com.digitalasset.canton.topology.ParticipantId]`

<div id="simclock" />

### `simclock`

Returns the node specific simClock, possible race condition if using environment.SimClock as well.

**Returns:** `Option[com.digitalasset.canton.time.DelegatingSimClock]`

<div id="start" />

### `start`

Start the instance.

<div id="stop" />

### `stop`

Stop the instance.

### Bilateral Commitments

<div id="commitments.add_config_distinguished_slow_counter_participants" />

### `commitments.add_config_distinguished_slow_counter_participants`

Add additional distinguished counter participants to already existing slow counter participant configuration.

The configuration can be extended by adding additional counter participants to existing synchronizers. if a given synchronizer is not already configured then it will be ignored without error.

**Arguments**

* `counterParticipantsDistinguished`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

<div id="commitments.add_participant_to_individual_metrics" />

### `commitments.add_participant_to_individual_metrics`

Add additional individual metrics participants to already existing slow counter participant configuration.

The configuration can be extended by adding additional counter participants to existing synchronizers. if a given synchronizer is not already configured then it will be ignored without error.

**Arguments**

* `individualMetrics`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

<div id="commitments.computed" />

### `commitments.computed`

Lookup ACS commitments locally computed as part of the reconciliation protocol.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `start`: `java.time.Instant`
* `end`: `java.time.Instant`
* `counterParticipant`: `Option[com.digitalasset.canton.topology.ParticipantId]`

**Returns:** `Iterable[(com.digitalasset.canton.protocol.messages.CommitmentPeriod, com.digitalasset.canton.topology.ParticipantId, com.digitalasset.canton.protocol.messages.AcsCommitment.HashedCommitmentType)]`

<div id="commitments.get_config_for_slow_counter_participants" />

### `commitments.get_config_for_slow_counter_participants`

Lists for the given synchronizers the configuration of metrics for slow counter-participants (i.e., thatare behind in sending commitments).

Lists the following config per synchronizer. If `synchronizers` is empty, the command lists config for all synchronizers:

* The participants in the distinguished group, which have two metrics: the maximum number of intervals that a participant is behind, and the number of participants that are behind by at least `thresholdDistinguished` reconciliation intervals
* The participants not in the distinguished group, which have two metrics: the maximum number of intervals that a participant is behind, and the number of participants that are behind by at least `thresholdDefault` reconciliation intervals
* Parameters `thresholdDistinguished` and `thresholdDefault`
* The participants in `individualMetrics`, which have individual metrics per participant showing how many reconciliation intervals that participant is behind

**Arguments**

* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.SlowCounterParticipantSynchronizerConfig]`

<div id="commitments.get_intervals_behind_for_counter_participants" />

### `commitments.get_intervals_behind_for_counter_participants`

Lists for every participant and synchronizer the number of intervals that the participant is behind in sending commitmentsif that participant is behind by at least threshold intervals.

If `counterParticipants` is empty, the command considers all counter-participants. If `synchronizers` is empty, the command considers all synchronizers. If `threshold` is not set, the command considers 0. For counter-participant that never sent a commitment, the output shows they are behind by MaxInt

**Arguments**

* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`
* `threshold`: `Option[com.digitalasset.canton.config.RequireTypes.NonNegativeInt]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.CounterParticipantInfo]`

<div id="commitments.get_wait_commitments_config_from" />

### `commitments.get_wait_commitments_config_from`

Retrieves the latest (i.e., w\.r.t. the query execution time) configuration of waiting for commitments from counter-participants.

The configuration for waiting for commitments from counter-participants is returned as two sets: a set of ignored counter-participants, the synchronizers and the timestamp, and a set of not-ignored counter-participants and the synchronizers. Filters by the specified counter-participants and synchronizers. If the counter-participant and / or synchronizers are empty, it considers all synchronizers and participants known to the participant, regardless of whether they share contracts with the participant. Even if some participants may not be connected to some synchronizers at the time the query executes, the response still includes them if they are known to the participant or specified in the arguments.

**Arguments**

* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`
* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`

**Returns:** `(Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Pruning.NoWaitCommitments], Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Pruning.WaitCommitments])`

<div id="commitments.help" />

### `commitments.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="commitments.inspect_commitment_contracts" />

### `commitments.inspect_commitment_contracts`

Download states of contracts and contract payloads necessary for commitment inspection and reconciliation.

Returns the contract states (created, assigned, unassigned, archived, unknown) of the given contracts on all synchronizers the participant knows from the beginning of time until the present time on each synchronizer. The command returns best-effort the contract changes available. Specifically, it does not fail if the ACS and/or reassignment state has been pruned during the time interval, or if parts of the time interval are ahead of the clean ACS state. Optionally returns the contract payload if requested and available. The arguments are:

* `contracts`: The contract ids whose state and payload we want to fetch
* `timestamp`: The timestamp when some counter-participants reported the given contracts as active on the expected synchronizer.
* `expectedSynchronizerId`: The synchronizer that the contracts are expected to be active on
* `downloadPayload`: If true, the payload of the contracts is also downloaded
* `timeout`: Time limit for the grpc call to complete

**Arguments**

* `contracts`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `expectedSynchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `downloadPayload`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `Seq[com.digitalasset.canton.participant.pruning.CommitmentInspectContract]`

<div id="commitments.lookup_received_acs_commitments" />

### `commitments.lookup_received_acs_commitments`

List the counter-participants of a participant and the ACS commitments received from them together withthe commitment state.

Optional filtering through the arguments: synchronizerTimeRanges: Lists commitments received on the given synchronizers whose period overlaps with any of the given time ranges per synchronizer. If the list is empty, considers all synchronizers the participant is connected to. For synchronizers with an empty time range, considers the latest period the participant knows of for that synchronizer. Synchronizers can appear multiple times in the list with various time ranges, in which case we consider the union of the time ranges. counterParticipants: Lists commitments received only from the given counter-participants. If a counter-participant is not a counter-participant on some synchronizer, no commitments appear in the reply from that counter-participant on that synchronizer. commitmentState: Lists commitments that are in one of the given states. By default considers all states:

* `MATCH`: the remote commitment matches the local commitment
* `MISMATCH`: the remote commitment does not match the local commitment
* `BUFFERED`: the remote commitment is buffered because the corresponding local commitment has not been computed yet
* `OUTSTANDING`: we expect a remote commitment that has not yet been received verboseMode: If false, the reply does not contain the commitment bytes. If true, the reply contains:
* In case of a mismatch, the reply contains both the received and the locally computed commitment that do not match.
* In case of outstanding, the reply does not contain any commitment.
* In all other cases (match and buffered), the reply contains the received commitment.

**Arguments**

* `synchronizerTimeRanges`: `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.SynchronizerTimeRange]`
* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `commitmentState`: `Seq[com.digitalasset.canton.participant.pruning.AcsCommitmentProcessor.ReceivedCmtState]`
* `verboseMode`: `Boolean`

**Returns:** `Map[com.digitalasset.canton.topology.SynchronizerId,Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.ReceivedAcsCmt]]`

<div id="commitments.lookup_sent_acs_commitments" />

### `commitments.lookup_sent_acs_commitments`

List the counter-participants of a participant and the ACS commitments that the participant computed and sent to them. Specifically, the command returns a map from synchronizer IDs to tuples of sent commitment data, specifying the period, target counter-participant, the commitment state, and additional data according to verbose mode.

Optional filtering through the arguments: synchronizerTimeRanges: Lists commitments received on the given synchronizers whose period overlap with any of the given time ranges per synchronizer. If the list is empty, considers all synchronizers the participant is connected to. For synchronizers with an empty time range, considers the latest period the participant knows of for that synchronizer. Synchronizers can appear multiple times in the list with various time ranges, in which case we consider the union of the time ranges. counterParticipants: Lists commitments sent only to the given counter-participants. If a counter-participant is not a counter-participant on some synchronizer, no commitments appear in the reply for that counter-participant on that synchronizer. commitmentState: Lists sent commitments that are in one of the given states. By default considers all states:

* `MATCH`: The local commitment matches the remote commitment
* `MISMATCH`: The local commitment does not match the remote commitment
* `NOT_COMPARED`: The local commitment has been computed and sent but no corresponding remote commitment has been received, which essentially indicates that a counter-participant is running behind verboseMode: If true, the reply contains the commitment bytes, as follows:
* In case of a mismatch, the reply contains both the received and the locally computed commitment that do not match.
* In all other cases (MATCH and NOT\_COMPARED), the reply contains the sent commitment bytes.

**Arguments**

* `synchronizerTimeRanges`: `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.SynchronizerTimeRange]`
* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `commitmentState`: `Seq[com.digitalasset.canton.participant.pruning.AcsCommitmentProcessor.SentCmtState]`
* `verboseMode`: `Boolean`

**Returns:** `Map[com.digitalasset.canton.topology.SynchronizerId,Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.SentAcsCmt]]`

<div id="commitments.open_commitment" />

### `commitments.open_commitment`

Opens a commitment by retrieving the metadata of active contracts shared with the counter-participant.

Retrieves the contract ids and the reassignment counters of the shared active contracts at the given timestamp and on the given synchronizer. Returns an error if the participant cannot retrieve the data for the given commitment anymore. The arguments are:

* `commitment`: The commitment to be opened
* `physicalSynchronizerId`: The synchronizer for which the commitment was computed
* `timestamp`: The timestamp of the commitment. Needs to correspond to a commitment tick.
* `counterParticipant`: The counter participant to whom we previously sent the commitment
* `outputFile`: Optional file to which the result is written
* `timeout`: Time limit for the grpc call to complete

**Arguments**

* `commitment`: `com.digitalasset.canton.protocol.messages.AcsCommitment.HashedCommitmentType`
* `physicalSynchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `counterParticipant`: `com.digitalasset.canton.topology.ParticipantId`
* `outputFile`: `Option[String]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `Seq[com.digitalasset.canton.participant.pruning.CommitmentContractMetadata]`

<div id="commitments.received" />

### `commitments.received`

Lookup ACS commitments received from other participants as part of the reconciliation protocol.

The arguments are:

* `synchronizerAlias`: the alias of the synchronizer
* `start`: lowest time exclusive
* `end`: highest time inclusive
* `counterParticipant`: optionally filter by counter participant

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `start`: `java.time.Instant`
* `end`: `java.time.Instant`
* `counterParticipant`: `Option[com.digitalasset.canton.topology.ParticipantId]`

**Returns:** `Iterable[com.digitalasset.canton.protocol.messages.SignedProtocolMessage[com.digitalasset.canton.protocol.messages.AcsCommitment]]`

<div id="commitments.reinitialize_commitments" />

### `commitments.reinitialize_commitments`

Reinitializes commitments from the current ACS. Filtering is possible by synchronizers, counter-participantsand stakeholder groups.

The command is useful if the participant's commitments got corrupted due to a bug. The command reinitializes the commitments for the given synchronizers and counter-participants, and containing contracts with stakeholders including the given parties. If `synchronizers` is empty, the command considers all synchronizers. If `counterParticipants` is empty, the command considers all counter-participants. If `partyIds` is empty, the command considers all stakeholder groups. `timeout` specifies how long the commands waits for the reinitialization to complete. Granularities smaller than a second are ignored. Past this timeout, the operator can query the status of the reinitialization using `commitment_reinitialization_status`. The command returns a sequence pairs of synchronizer IDs and the reinitialization status for each synchronizer: either the ACS timestamp of the reinitialization, or an error message if reinitialization failed.

**Arguments**

* `synchronizerIds`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`
* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `partyIds`: `Seq[com.digitalasset.canton.topology.PartyId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.ReinitCommitments.CommitmentReinitializationInfo]`

<div id="commitments.remove_config_distinguished_slow_counter_participants" />

### `commitments.remove_config_distinguished_slow_counter_participants`

removes existing configurations from synchronizers and distinguished counter participants.

The configurations can be removed from distinguished counter participant and synchronizers use empty sequences correlates to selecting all, so removing all distinguished participants from a synchronizer can be done with Seq.empty for 'counterParticipantsDistinguished' and Seq(SynchronizerId) for synchronizers. Leaving both sequences empty clears all configs on all synchronizers.

**Arguments**

* `counterParticipantsDistinguished`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

<div id="commitments.remove_participant_from_individual_metrics" />

### `commitments.remove_participant_from_individual_metrics`

removes existing configurations from synchronizers and individual metrics participants.

The configurations can be removed from individual metrics counter participant and synchronizers use empty sequences correlates to selecting all, so removing all individual metrics participants from a synchronizer can be done with Seq.empty for 'individualMetrics' and Seq(SynchronizerId) for synchronizers. Leaving both sequences empty clears all configs on all synchronizers.

**Arguments**

* `individualMetrics`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizers`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

<div id="commitments.set_config_for_slow_counter_participants" />

### `commitments.set_config_for_slow_counter_participants`

Configure metrics for slow counter-participants (i.e., that are behind in sending commitments) andconfigure thresholds for when a counter-participant is deemed slow.

The configurations are per synchronizer or set of synchronizers and concern the following metrics issued per synchronizer:

* The maximum number of intervals that a distinguished participant falls behind. All participants that are not in the distinguished or the individual group are automatically part of the default group
* The maximum number of intervals that a participant in the default groups falls behind
* The number of participants in the distinguished group that are behind by at least `thresholdDistinguished` reconciliation intervals.
* The number of participants not in the distinguished or the individual group that are behind by at least `thresholdDefault` reconciliation intervals.
* Separate metric for each participant in `individualMetrics` argument tracking how many intervals that participant is behind

**Arguments**

* `configs`: `Seq[com.digitalasset.canton.admin.api.client.commands.ParticipantAdminCommands.Inspection.SlowCounterParticipantSynchronizerConfig]`

<div id="commitments.set_no_wait_commitments_from" />

### `commitments.set_no_wait_commitments_from`

Disable waiting for commitments from the given counter-participants.

Disabling waiting for commitments disregards these counter-participants w\.r.t. pruning, which gives up non-repudiation for those counter-participants, but increases pruning resilience to failures and slowdowns of those counter-participants and/or the network. If the participant set is empty, the command does nothing.

**Arguments**

* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizerIds`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

<div id="commitments.set_wait_commitments_from" />

### `commitments.set_wait_commitments_from`

Enable waiting for commitments from the given counter-participants. Waiting for commitments from all counter-participants is the default behavior; explicitly enabling waitingfor commitments is only necessary if it was previously disabled.

Enables waiting for commitments, which blocks pruning at offsets where commitments from these counter-participants are missing. If the participant set is empty or the synchronizer set is empty, the command does nothing.

**Arguments**

* `counterParticipants`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `synchronizerIds`: `Seq[com.digitalasset.canton.topology.SynchronizerId]`

### DAR Management

<div id="dars.download" />

### `dars.download`

Downloads the DAR file with the provided main package-id to the given directory.

**Arguments**

* `mainPackageId`: `String`
* `directory`: `String`

<div id="dars.get_contents" />

### `dars.get_contents`

List contents of DAR files.

**Arguments**

* `mainPackageId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.DarContents`

<div id="dars.help" />

### `dars.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="dars.list" />

### `dars.list`

List installed DAR files.

List DARs installed on this participant The arguments are: filterName: filter by name filterDescription: filter by description limit: Limit number of results (default none)

**Arguments**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `filterName`: `String`
* `filterDescription`: `String`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.DarDescription]`

<div id="dars.remove" />

### `dars.remove`

Remove a DAR from the participant.

Can be used to remove a DAR from the participant, if the following conditions are satisfied: 1. The main package of the DAR must be unused -- there should be no active contract from this package

2. All package dependencies of the DAR should either be unused or contained in another of the participant node's uploaded DARs. Canton uses this restriction to ensure that the package dependencies of the DAR don't become "stranded" if they're in use.

3. The main package of the dar should not be vetted. If it is vetted, Canton will try to automatically revoke the vetting for the main package of the DAR, but this automatic vetting revocation will only succeed if the main package vetting originates from a standard `dars.upload`. Even if the automatic revocation fails, you can always manually revoke the package vetting.

If synchronizeVetting is true (default), then the command will block until the participant has observed the vetting transactions to be registered with the synchronizer.

**Arguments**

* `mainPackageId`: `String`
* `synchronizeVetting`: `Boolean`

<div id="dars.upload" />

### `dars.upload`

Upload a DAR to Canton.

Daml code is normally shipped as a Dar archive and must explicitly be uploaded to a participant. A Dar is a collection of LF-packages, the native binary representation of Daml smart contracts.

The Dar can be provided either as a link to a local file or as a URL. If a URL is provided, then any request headers can be provided as a map. The Dar will be downloaded and then uploaded to the participant.

In order to use Daml templates on a participant, the Dar must first be uploaded and then vetted by the participant. Vetting will ensure that other participants can check whether they can actually send a transaction referring to a particular Daml package and participant. Packages must be vetted on each synchronizer by registering a VettedPackages topology transaction.

If synchronizerId is not set (default), the packages will be vetted, if the participant is connected to only one synchronizer. If synchronizeVetting is true (default), then the command will block until the participant has observed the vetting transactions to be registered with the synchronizer.

This command waits for the vetting transaction to be successfully registered on the synchronizer. This is the safe default setting minimizing race conditions.

Note that synchronize vetting might block on permissioned synchronizers that do not just allow participants to update the topology state. In such cases, synchronizeVetting should be turned off. Synchronize vetting can be invoked manually using \$participant.package.synchronize\_vettings()

**Arguments**

* `path`: `String`
* `description`: `String`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `expectedMainPackageId`: `String`
* `requestHeaders`: `Map[String,String]`

**Returns:** `String`

<div id="dars.upload_many" />

### `dars.upload_many`

Upload many DARs to Canton.

Daml code is normally shipped as a Dar archive and must explicitly be uploaded to a participant. A Dar is a collection of LF-packages, the native binary representation of Daml smart contracts.

The Dars can be provided either as a link to a local file or as a URL. If a URL is provided, then any request headers can be provided as a map. The Dars will be downloaded and then uploaded to the participant.

In order to use Daml templates on a participant, the Dars must first be uploaded and then vetted by the participant. Vetting will ensure that other participants can check whether they can actually send a transaction referring to a particular Daml package and participant. Packages must be vetted on each synchronizer by registering a VettedPackages topology transaction.

If synchronizerId is not set (default), the packages will be vetted, if the participant is connected to only one synchronizer. If synchronizeVetting is true (default), then the command will block until the participant has observed the vetting transactions to be registered with the synchronizer.

This command waits for the vetting transaction to be successfully registered on the synchronizer. This is the safe default setting minimizing race conditions.

Note that synchronize vetting might block on permissioned synchronizers that do not just allow participants to update the topology state. In such cases, synchronizeVetting should be turned off. Synchronize vetting can be invoked manually using \$participant.package.synchronize\_vettings()

**Arguments**

* `paths`: `Seq[String]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `requestHeaders`: `Map[String,String]`

**Returns:** `Seq[String]`

<div id="dars.validate" />

### `dars.validate`

Validate DARs against the current participants' state.

Performs the same DAR and Daml package validation checks that the upload call performs, but with no effects on the target participants: the DAR is not persisted or vetted.

**Arguments**

* `path`: `String`

**Returns:** `String`

<div id="dars.vetting.disable" />

### `dars.vetting.disable`

Revoke vetting for all packages contained in the DAR archive identified by the provided main package-id.

This command succeeds if the vetting command used to vet the DAR's packages was symmetric and resulted in a single vetting topology transaction for all the packages in the DAR. This command is potentially dangerous and misuse can lead the participant to fail in processing transactions

**Arguments**

* `mainPackageId`: `String`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

<div id="dars.vetting.enable" />

### `dars.vetting.enable`

Vet all packages contained in the DAR archive identified by the provided main package-id.

**Arguments**

* `mainPackageId`: `String`
* `synchronize`: `Boolean`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

<div id="dars.vetting.help" />

### `dars.vetting.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

### Database

<div id="db.help" />

### `db.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="db.migrate" />

### `db.migrate`

Migrates the instance's database if using a database storage.

When instances reside on different nodes, their database migration can be run in parallel to save time. Please not that the migration commands must however must be run on each node individually, because remote migration through `participants.remote...` is not supported.

<div id="db.repair_migration" />

### `db.repair_migration`

Only use when advised - repairs the database migration of the instance's database.

In some rare cases, we change already applied database migration files in a new release and the repair command resets the checksums we use to ensure that in general already applied migration files have not been changed. You should only use `db.repair_migration` when advised and otherwise use it at your own risk - in the worst case running it may lead to data corruption when an incompatible database migration (one that should be rejected because the already applied database migration files have changed) is subsequently falsely applied.

**Arguments**

* `force`: `Boolean`

### Synchronizer connectivity

<div id="synchronizers.active" />

### `synchronizers.active`

Test whether a participant is connected to and permissioned on a synchronizer.

Yields false, if the synchronizer is not connected or not healthy. Yields false, if the synchronizer is configured in the Canton configuration and the participant is not active from the perspective of the synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `Boolean`

<div id="synchronizers.config" />

### `synchronizers.config`

Returns the current configuration of a given synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `Option[com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig]`

<div id="synchronizers.connect" />

### `synchronizers.connect`

Macro to connect a participant to a synchronizer given by connection.

The connect macro performs a series of commands in order to connect this participant to a synchronizer. First, `register` will be invoked with the given arguments, but first registered with manualConnect = true. If you already set manualConnect = true, then nothing else will happen and you will have to do the remaining steps yourselves. Finally, the command will invoke `reconnect` to startup the connection. If the reconnect succeeded, the registered configuration will be updated with manualStart = true. If anything fails, the synchronizer will remain registered with `manualConnect = true` and you will have to perform these steps manually. The arguments are:

* `synchronizerAlias`: The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `connection`: The connection string to connect to this synchronizer. I.e. [https://url:port](https://url:port) manualConnect - Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: Optionally the physical id you expect to see on this synchronizer.
* `certificatesPath`: Path to TLS certificate files to use as a trust anchor.
* `priority`: The priority of the synchronizer. The higher the more likely a synchronizer will be used.
* `timeTrackerConfig`: The configuration for the synchronizer time tracker.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `connection`: `String`
* `manualConnect`: `Boolean`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `certificatesPath`: `String`
* `priority`: `Int`
* `timeTrackerConfig`: `com.digitalasset.canton.config.SynchronizerTimeTrackerConfig`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `sequencerAlias`: `com.digitalasset.canton.SequencerAlias`

**Returns:** `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`

<div id="synchronizers.connect_1" />

### `synchronizers.connect_1`

Macro to connect a participant to a synchronizer given by instance.

This variant of connect expects an instance with a sequencer connection. Otherwise the behaviour is equivalent to the connect command with explicit arguments. If the synchronizer is already configured, the synchronizer connection will be attempted. If however the synchronizer is offline, the command will fail. Generally, this macro should only be used for the first connection to a new synchronizer. However, for convenience, we support idempotent invocations where subsequent calls just ensure that the participant reconnects to the synchronizer.

**Arguments**

* `instance`: `com.digitalasset.canton.console.SequencerReference`
* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="synchronizers.connect_bft" />

### `synchronizers.connect_bft`

Macro to connect to multiple sequencers of the same synchronizer.

The arguments are:

* `synchronizerAlias`: The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `connections`: The list of sequencer connections, can be defined by urls.
* `manualConnect`: Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: An optional Synchronizer Id to ensure the connection is made to the correct synchronizer.
* `priority`: The priority of the synchronizer. The higher the more likely a synchronizer will be used.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `sequencerTrustThreshold`: Set the minimum number of sequencers that must agree before a message is considered valid.
* `sequencerLivenessMargin`: Set the number of extra subscriptions to maintain beyond `sequencerTrustThreshold` in order to ensure liveness.
* `submissionRequestAmplification`: Define how often client should try to send a submission request that is eligible for deduplication.
* `sequencerConnectionPoolDelays`: Define the various delays used by the sequencer connection pool.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `connections`: `Seq[com.digitalasset.canton.sequencing.SequencerConnection]`
* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `manualConnect`: `Boolean`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `sequencerTrustThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `sequencerLivenessMargin`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `submissionRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `sequencerConnectionPoolDelays`: `com.digitalasset.canton.sequencing.SequencerConnectionPoolDelays`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="synchronizers.connect_by_config" />

### `synchronizers.connect_by_config`

Macro to connect a participant to a synchronizer given by connection.

This variant of connect expects a synchronizer connection config. Otherwise the behaviour is equivalent to the connect command with explicit arguments. If the synchronizer is already configured, the synchronizer connection will be attempted. If however the synchronizer is offline, the command will fail. Generally, this macro should only be used for the first connection to a new synchronizer. However, for convenience, we support idempotent invocations where subsequent calls just ensure that the participant reconnects to the synchronizer.

validation - Whether to validate the connectivity and ids of the given sequencers (default all)

**Arguments**

* `config`: `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="synchronizers.connect_local" />

### `synchronizers.connect_local`

Macro to connect a participant to a locally configured synchronizer given by sequencer reference.

The arguments are:

* `sequencer`: A local sequencer reference alias - The name you will be using to refer to this synchronizer. Can not be changed anymore.
* `manualConnect`: Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: An optional Synchronizer Id to ensure the connection is made to the correct synchronizer.
* `maxRetryDelayMillis`: Maximal amount of time (in milliseconds) between two connection attempts.
* `priority`: The priority of the synchronizer. The higher the more likely a synchronizer will be used.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.SynchronizerAlias`
* `manualConnect`: `Boolean`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="synchronizers.connect_local_bft" />

### `synchronizers.connect_local_bft`

Macro to connect to multiple local sequencers of the same synchronizer.

The arguments are:

* `synchronizerAlias`: The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `sequencers`: The list of sequencer references to connect to.
* `manualConnect`: Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: An optional Synchronizer Id to ensure the connection is made to the correct synchronizer.
* `priority`: The priority of the synchronizer. The higher the more likely a synchronizer will be used.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `sequencerTrustThreshold`: Set the minimum number of sequencers that must agree before a message is considered valid.
* `sequencerLivenessMargin`: Set the number of extra subscriptions to maintain beyond `sequencerTrustThreshold` in order to ensure liveness.
* `submissionRequestAmplification`: Define how often client should try to send a submission request that is eligible for deduplication.
* `sequencerConnectionPoolDelays`: Define the various delays used by the sequencer connection pool.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `sequencers`: `Seq[com.digitalasset.canton.console.SequencerReference]`
* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `manualConnect`: `Boolean`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `sequencerTrustThreshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `sequencerLivenessMargin`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `submissionRequestAmplification`: `com.digitalasset.canton.sequencing.SubmissionRequestAmplification`
* `sequencerConnectionPoolDelays`: `com.digitalasset.canton.sequencing.SequencerConnectionPoolDelays`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="synchronizers.connect_multi" />

### `synchronizers.connect_multi`

Macro to connect a participant to a synchronizer that supports connecting via many endpoints.

Synchronizers can provide many endpoints to connect to for availability and performance benefits. This version of connect allows specifying multiple endpoints for a single synchronizer connection: connect\_multi("mysynchronizer", Seq(sequencer1, sequencer2)) or: connect\_multi("mysynchronizer", Seq("[https://host1.mysynchronizer.net](https://host1.mysynchronizer.net)", "[https://host2.mysynchronizer.net](https://host2.mysynchronizer.net)", "[https://host3.mysynchronizer.net](https://host3.mysynchronizer.net)"))

To create a more advanced connection config use synchronizers.to\_config with a single host, then use config.addConnection to add additional connections before connecting: config = myparticipaint.synchronizers.to\_config("mysynchronizer", "[https://host1.mysynchronizer.net](https://host1.mysynchronizer.net)", ...otherArguments) config = config.addConnection("[https://host2.mysynchronizer.net](https://host2.mysynchronizer.net)", "[https://host3.mysynchronizer.net](https://host3.mysynchronizer.net)") myparticipant.synchronizers.connect(config)

The arguments are:

* `synchronizerAlias`: The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `connections`: The sequencer connection definitions (can be an URL) to connect to this synchronizer. I.e. [https://url:port](https://url:port) synchronize - A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `connections`: `Seq[com.digitalasset.canton.sequencing.SequencerConnection]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

**Returns:** `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`

<div id="synchronizers.disconnect" />

### `synchronizers.disconnect`

Disconnect this participant from the given synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="synchronizers.disconnect_all" />

### `synchronizers.disconnect_all`

Disconnect this participant from all connected synchronizers.

<div id="synchronizers.disconnect_local" />

### `synchronizers.disconnect_local`

Disconnect this participant from the given local synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="synchronizers.help" />

### `synchronizers.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="synchronizers.id_of" />

### `synchronizers.id_of`

Returns the id of the given synchronizer alias.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `com.digitalasset.canton.topology.SynchronizerId`

<div id="synchronizers.is_connected" />

### `synchronizers.is_connected`

Test whether a participant is connected to a synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `Boolean`

<div id="synchronizers.is_connected_1" />

### `synchronizers.is_connected_1`

Test whether a participant is connected to physical a synchronizer.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`

**Returns:** `Boolean`

<div id="synchronizers.is_connected_2" />

### `synchronizers.is_connected_2`

Test whether a participant is connected to a synchronizer.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`

**Returns:** `Boolean`

<div id="synchronizers.is_registered" />

### `synchronizers.is_registered`

Returns true if a synchronizer is registered using the given alias.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `Boolean`

<div id="synchronizers.list_connected" />

### `synchronizers.list_connected`

List the connected synchronizers of this participant.

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListConnectedSynchronizersResult]`

<div id="synchronizers.list_registered" />

### `synchronizers.list_registered`

List the configured synchronizer of this participant.

For each returned synchronizer, the boolean indicates whether the participant is currently connected to the synchronizer.

**Returns:** `Seq[(com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig, com.digitalasset.canton.topology.ConfiguredPhysicalSynchronizerId, Boolean)]`

<div id="synchronizers.logout" />

### `synchronizers.logout`

Revoke this participant's authentication tokens and close all the sequencer connections in the given synchronizer.

synchronizerAlias: the synchronizer alias from which to logout On all the sequencers from the specified synchronizer, all existing authentication tokens for this participant will be revoked. Note that the participant is not disconnected from the synchronizer; only the connections to the sequencers are closed. The participant will automatically reopen connections, perform a challenge-response and obtain new tokens.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="synchronizers.modify" />

### `synchronizers.modify`

Modify existing synchronizer connection.

The arguments are:

* `synchronizerAlias`: Alias of the synchronizer modifier - The change to be applied to the config.
* `validation`: The validations which need to be done to the connection.
* `physicalSynchronizerId`: Physical id of the synchronizer. If empty, the active one will be updated (if none is active, an error is returned).

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `modifier`: `[com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig => com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/participant/synchronizer/SynchronizerConnectionConfig.html)`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`

<div id="synchronizers.physical_id_of" />

### `synchronizers.physical_id_of`

Returns the physical id of the given synchronizer alias.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `com.digitalasset.canton.topology.PhysicalSynchronizerId`

<div id="synchronizers.reconnect" />

### `synchronizers.reconnect`

Reconnect this participant to the given synchronizer.

Idempotent attempts to re-establish a connection to a certain synchronizer. If retry is set to false, the command will throw an exception if unsuccessful. If retry is set to true, the command will terminate after the first attempt with the result, but the server will keep on retrying to connect to the synchronizer.

The arguments are:

* `synchronizerAlias`: The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `retry`: Whether the reconnect should keep on retrying until it succeeded or abort noisily if the connection attempt fails.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `retry`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `Boolean`

<div id="synchronizers.reconnect_all" />

### `synchronizers.reconnect_all`

Reconnect this participant to all synchronizer which are not marked as manual start.

The arguments are: ignoreFailures - If set to true (default), we'll attempt to connect to all, ignoring any failure synchronize - A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `ignoreFailures`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="synchronizers.reconnect_local" />

### `synchronizers.reconnect_local`

Reconnect this participant to the given local synchronizer.

Idempotent attempts to re-establish a connection to the given local synchronizer. Same behaviour as generic reconnect.

The arguments are:

* `synchronizerAlias`: The synchronizer alias to connect to retry - Whether the reconnect should keep on retrying until it succeeded or abort noisily if the connection attempt fails.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `retry`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `Boolean`

<div id="synchronizers.reconnect_local_1" />

### `synchronizers.reconnect_local_1`

Reconnect this participant to the given local synchronizer.

Idempotent attempts to re-establish a connection to the given local synchronizer. Same behaviour as generic reconnect.

The arguments are:

* `ref`: The synchronizer reference to connect to retry - Whether the reconnect should keep on retrying until it succeeded or abort noisily if the connection attempt fails.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `ref`: `com.digitalasset.canton.console.SequencerReference`

**Returns:** `Boolean`

<div id="synchronizers.register" />

### `synchronizers.register`

Macro to register a locally configured synchronizer given by sequencer reference.

The arguments are:

* `sequencer`: A local sequencer reference alias - The name you will be using to refer to this synchronizer. Cannot be changed anymore.
* `performHandshake`: If true (default), will perform a handshake with the synchronizer. If no, will only store the configuration without any query to the synchronizer.
* `manualConnect`: Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: An optional Synchronizer Id to ensure the connection is made to the correct synchronizer.
* `maxRetryDelayMillis`: Maximal amount of time (in milliseconds) between two connection attempts.
* `priority`: The priority of the synchronizer. The higher the more likely a synchronizer will be used.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All)

**Arguments**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.SynchronizerAlias`
* `performHandshake`: `Boolean`
* `manualConnect`: `Boolean`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `maxRetryDelayMillis`: `Option[Long]`
* `priority`: `Int`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="synchronizers.register_by_config" />

### `synchronizers.register_by_config`

Macro to register a locally configured synchronizer.

The arguments are:

* `config`: Config for the synchronizer connection performHandshake - If true (default), will perform handshake with the synchronizer. If no, will only store configuration without any query to the synchronizer.
* `validation`: Whether to validate the connectivity and ids of the given sequencers (default All) synchronize - A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `config`: `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`
* `performHandshake`: `Boolean`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

### Health

<div id="health.active" />

### `health.active`

Check if the node is running and is the active instance (mediator, participant).

**Returns:** `Boolean`

<div id="health.count_in_flight" />

### `health.count_in_flight`

Counts pending command submissions and transactions on a synchronizer.

This command finds the current number of pending command submissions and transactions on a selected synchronizer.

There is no synchronization between pending command submissions and transactions. And the respective counts are an indication only!

This command is in particular useful to re-assure oneself that there are currently no in-flight submissions or transactions present for the selected synchronizer. Such re-assurance is then helpful to proceed with repair operations, for example.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

**Returns:** `com.digitalasset.canton.admin.api.client.data.InFlightCount`

<div id="health.dump_1" />

### `health.dump_1`

Collect Canton system information to help diagnose issues.

Generates a comprehensive health report for the local Canton process and any connected remote nodes.

The arguments are:

* `outputFile`: Specifies the file path to save the report. If not set, a default path is used.
* `timeout`: Sets a custom timeout for gathering data, useful for large reports from slow remote nodes.
* `chunkSize`: Adjusts the data stream chunk size from remote nodes. Use this to prevent gRPC errors related to 'max inbound message size'

**Arguments**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**Returns:** `String`

<div id="health.has_identity" />

### `health.has_identity`

Returns true if the node has an identity.

**Returns:** `Boolean`

<div id="health.help_1" />

### `health.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="health.initialized" />

### `health.initialized`

Returns true if node has been initialized.

**Returns:** `Boolean`

<div id="health.is_ready_for_id" />

### `health.is_ready_for_id`

Check if the node is ready for setting the node's id.

**Returns:** `Boolean`

<div id="health.is_ready_for_initialization" />

### `health.is_ready_for_initialization`

Check if the node is ready for initialization.

**Returns:** `Boolean`

<div id="health.is_ready_for_node_topology" />

### `health.is_ready_for_node_topology`

Check if the node is ready for uploading the node's identity topology.

**Returns:** `Boolean`

<div id="health.is_running" />

### `health.is_running`

Check if the node is running.

**Returns:** `Boolean`

<div id="health.last_error_trace" />

### `health.last_error_trace`

Show all messages logged with the given traceId in a recent interval.

Returns a list of buffered log messages associated to a given trace-id. Usually, the trace-id is taken from last\_errors()

**Arguments**

* `traceId`: `String`

**Returns:** `Seq[String]`

<div id="health.last_errors" />

### `health.last_errors`

Show the last errors logged.

Returns a map with the trace-id as key and the most recent error messages as value. Requires that --log-last-errors is enabled (and not turned off).

**Returns:** `Map[String,String]`

<div id="health.maybe_ping" />

### `health.maybe_ping`

Sends a ping to the target participant over the ledger. Yields Some(duration) in case of success and None in case of failure.

**Arguments**

* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `id`: `String`

**Returns:** `Option[scala.concurrent.duration.Duration]`

<div id="health.ping" />

### `health.ping`

Sends a ping to the target participant over the ledger. Yields the duration in case of success and throws a RuntimeException in case of failure.

**Arguments**

* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `id`: `String`

**Returns:** `scala.concurrent.duration.Duration`

<div id="health.set_log_level" />

### `health.set_log_level`

Change the log level of the process.

If the default logback configuration is used, this will change the log level of the process.

**Arguments**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_1" />

### `health.status_1`

Get human (and machine) readable status information.

**Returns:** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity" />

### `health.wait_for_identity`

Wait for the node to have an identity.

<div id="health.wait_for_initialized" />

### `health.wait_for_initialized`

Wait for the node to be initialized.

<div id="health.wait_for_ready_for_id" />

### `health.wait_for_ready_for_id`

Wait for the node to be ready for setting the node's id.

<div id="health.wait_for_ready_for_initialization" />

### `health.wait_for_ready_for_initialization`

Wait for the node to be ready for initialization.

<div id="health.wait_for_ready_for_node_topology" />

### `health.wait_for_ready_for_node_topology`

Wait for the node to be ready for uploading the node's identity topology.

<div id="health.wait_for_running" />

### `health.wait_for_running`

Wait for the node to be running.

### Key administration

<div id="keys.help" />

### `keys.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.download" />

### `keys.public.download`

Download public key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.public.download_to" />

### `keys.public.download_to`

Download public key and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help" />

### `keys.public.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.list" />

### `keys.public.list`

List public keys in registry.

Returns all public keys that have been added to the key registry. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner" />

### `keys.public.list_by_owner`

List keys for given keyOwner.

This command is a convenience wrapper for `list_key_owners`, taking an explicit keyOwner as search argument. The response includes the public keys.

**Arguments**

* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners" />

### `keys.public.list_owners`

List active owners with keys for given search arguments.

This command allows deep inspection of the topology state. The response includes the public keys. Optional filterKeyOwnerType type can be 'ParticipantId.Code' , 'MediatorId.Code','SequencerId.Code'.

**Arguments**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.topology.MemberCode]`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload" />

### `keys.public.upload`

Upload public key.

Import a public key and store it together with a name used to provide some context to that key.

**Arguments**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from" />

### `keys.public.upload_from`

Upload public key.

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete" />

### `keys.secret.delete`

Delete private key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download" />

### `keys.secret.download`

Download key pair.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to" />

### `keys.secret.download_to`

Download key pair and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key" />

### `keys.secret.generate_encryption_key`

Generate new public/private key pair for encryption and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key" />

### `keys.secret.generate_signing_key`

Generate new public/private key pair for signing and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id" />

### `keys.secret.get_wrapper_key_id`

Get the wrapper key id that is used for the encrypted private keys store.

**Returns:** `String`

<div id="keys.secret.help" />

### `keys.secret.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.secret.list" />

### `keys.secret.list`

List keys in private vault.

Returns all public keys to the corresponding private keys in the key vault. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key" />

### `keys.secret.register_kms_encryption_key`

Register the specified KMS encryption key in canton storing its public information in the vault.

The id for the KMS encryption key. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key" />

### `keys.secret.register_kms_signing_key`

Register the specified KMS signing key in canton storing its public information in the vault.

The id for the KMS signing key. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key" />

### `keys.secret.rotate_kms_node_key`

Rotate a given node's keypair with a new pre-generated KMS keypair.

Rotates an existing encryption or signing key stored externally in a KMS with a pre-generated key. NOTE: A namespace root signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. The id of the new KMS key (e.g. Resource Name). An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key" />

### `keys.secret.rotate_node_key`

Rotate a node's public/private key pair.

Rotates an existing encryption or signing key. NOTE: A namespace root or intermediate signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys" />

### `keys.secret.rotate_node_keys`

Rotate the node's public/private key pairs.

For a participant node it rotates the signing and encryption key pair. For a sequencer or mediator node it rotates the signing key pair as those nodes do not have an encryption key pair. NOTE: Namespace root or intermediate signing keys are NOT rotated by this command.

<div id="keys.secret.rotate_wrapper_key" />

### `keys.secret.rotate_wrapper_key`

Change the wrapper key for encrypted private keys store.

Change the wrapper key (e.g. AWS KMS key) being used to encrypt the private keys in the store. newWrapperKeyId: The optional new wrapper key id to be used. If the wrapper key id is empty Canton will generate a new key based on the current configuration.

**Arguments**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload" />

### `keys.secret.upload`

Upload a key pair.

Upload the previously downloaded key pair. pairBytes: The binary representation of a previously downloaded key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from" />

### `keys.secret.upload_from`

Upload (load and import) a key pair from file.

Upload the previously downloaded key pair from a file. filename: The name of the file holding the key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### Ledger API Access

The following commands on a participant reference provide access to the participant's Ledger API services.

<div id="ledger_api.help" />

### `ledger_api.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.javaapi.help" />

### `ledger_api.javaapi.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

#### Command Completion Service

<div id="ledger_api.completions.help" />

### `ledger_api.completions.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.completions.list" />

### `ledger_api.completions.list`

Lists command completions following the specified offset.

If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. An empty offset denotes the beginning of the participant's offsets.

**Arguments**

* `partyId`: `com.digitalasset.canton.topology.Party`
* `atLeastNumCompletions`: `Int`
* `beginOffsetExclusive`: `Long`
* `userId`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `filter`: `com.daml.ledger.api.v2.completion.Completion => Boolean`

**Returns:** `Seq[com.daml.ledger.api.v2.completion.Completion]`

<div id="ledger_api.completions.subscribe" />

### `ledger_api.completions.subscribe`

Subscribe to the command completion stream.

This function connects to the command completion stream and passes command completions to `observer` until the stream is completed. Only completions for parties in `parties` will be returned. The returned completions start at `beginOffset` (default: the zero value denoting the participant begin). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error.

**Arguments**

* `observer`: `io.grpc.stub.StreamObserver[com.daml.ledger.api.v2.completion.Completion]`
* `parties`: `Seq[com.digitalasset.canton.topology.Party]`
* `beginOffsetExclusive`: `Long`
* `userId`: `String`

**Returns:** `AutoCloseable`

#### Command Submission Service

<div id="ledger_api.commands.failed" />

### `ledger_api.commands.failed`

Investigate failed commands.

Same as status(..., state = CommandState.Failed).

**Arguments**

* `commandId`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.commands.help" />

### `ledger_api.commands.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.commands.status" />

### `ledger_api.commands.status`

Investigate successful and failed commands.

Find the status of commands. Note that only recent commands which are kept in memory will be returned.

**Arguments**

* `commandIdPrefix`: `String`
* `state`: `com.daml.ledger.api.v2.admin.command_inspection_service.CommandState`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.commands.submit" />

### `ledger_api.commands.submit`

Submit command and wait for the resulting transaction, returning the transaction or failing otherwise.

Submits a command on behalf of the `actAs` parties, waits for the resulting transaction to commit, and returns the "flattened" transaction. If the timeout is set, it also waits for the transaction to appear at all other configured participants who were involved in the transaction. The call blocks until the transaction commits or fails; the timeout only specifies how long to wait at the other participants. Fails if the transaction doesn't commit, or if it doesn't become visible to the involved participants in the allotted time. Note that if the optTimeout is set and the involved parties are concurrently enabled/disabled or their participants are connected/disconnected, the command may currently result in spurious timeouts or may return before the transaction appears at all the involved participants.

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `commandId`: `String`
* `optTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `com.daml.ledger.api.v2.transaction.Transaction`

<div id="ledger_api.commands.submit_assign" />

### `ledger_api.commands.submit_assign`

Submit assign command and wait for the resulting reassignment, returning the reassignment or failing otherwise.

Submits an assignment command on behalf of `submitter` party, waits for the resulting assignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other configured participants who were involved in the assignment. The call blocks until the assignment commits or fails. Fails if the assignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants. The reassignmentId should be the one returned by the corresponding submit\_unassign command.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `reassignmentId`: `String`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.AssignedWrapper`

<div id="ledger_api.commands.submit_assign_async" />

### `ledger_api.commands.submit_assign_async`

Submit assign command asynchronously.

Provides access to the command submission service of the Ledger API. See the [Ledger API reference](https://docs.canton.network/sdks-tools/api-reference/ledger-api) for documentation of the parameters.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `reassignmentId`: `String`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `commandId`: `String`
* `submissionId`: `String`

<div id="ledger_api.commands.submit_assign_with_format" />

### `ledger_api.commands.submit_assign_with_format`

Submit assign command and wait for the resulting reassignment, returning the reassignment or failing otherwise.

Submits an assignment command on behalf of `submitter` party, waits for the resulting assignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other configured participants who were involved in the assignment. The call blocks until the assignment commits or fails. Fails if the assignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants. The reassignmentId should be the one returned by the corresponding submit\_unassign command.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `reassignmentId`: `String`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `eventFormat`: `Option[com.daml.ledger.api.v2.transaction_filter.EventFormat]`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.EmptyOrAssignedWrapper`

<div id="ledger_api.commands.submit_async" />

### `ledger_api.commands.submit_async`

Submit command asynchronously.

Provides access to the command submission service of the Ledger API. See the [Ledger API reference](https://docs.canton.network/sdks-tools/api-reference/ledger-api) for documentation of the parameters.

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.PartyId]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `commandId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`

<div id="ledger_api.commands.submit_reassign" />

### `ledger_api.commands.submit_reassign`

Combines `submit_unassign` and `submit_assign` in a single macro.

See `submit_unassign` and `submit_assign` for the parameters.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `(com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UnassignedWrapper, com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.AssignedWrapper)`

<div id="ledger_api.commands.submit_unassign" />

### `ledger_api.commands.submit_unassign`

Submit unassign command and wait for the resulting reassignment, returning the reassignment or failing otherwise.

Submits an unassignment command on behalf of `submitter` party, waits for the resulting unassignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other configured participants who were involved in the unassignment. The call blocks until the unassignment commits or fails. Fails if the unassignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UnassignedWrapper`

<div id="ledger_api.commands.submit_unassign_async" />

### `ledger_api.commands.submit_unassign_async`

Submit unassign command asynchronously.

Provides access to the command submission service of the Ledger API. See the [Ledger API reference](https://docs.canton.network/sdks-tools/api-reference/ledger-api) for documentation of the parameters.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `commandId`: `String`
* `submissionId`: `String`

<div id="ledger_api.commands.submit_unassign_with_format" />

### `ledger_api.commands.submit_unassign_with_format`

Submit unassign command and wait for the resulting reassignment, returning the reassignment or failing otherwise.

Submits an unassignment command on behalf of `submitter` party, waits for the resulting unassignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other configured participants who were involved in the unassignment. The call blocks until the unassignment commits or fails. Fails if the unassignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `eventFormat`: `Option[com.daml.ledger.api.v2.transaction_filter.EventFormat]`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.EmptyOrUnassignedWrapper`

<div id="ledger_api.javaapi.commands.help" />

### `ledger_api.javaapi.commands.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.javaapi.commands.submit" />

### `ledger_api.javaapi.commands.submit`

Submit java codegen command and wait for the resulting transaction, returning the transaction or failing otherwise.

Submits a command on behalf of the `actAs` parties, waits for the resulting transaction to commit, and returns the "flattened" transaction. If the timeout is set, it also waits for the transaction to appear at all other configured participants who were involved in the transaction. The call blocks until the transaction commits or fails; the timeout only specifies how long to wait at the other participants. Fails if the transaction doesn't commit, or if it doesn't become visible to the involved participants in the allotted time. Note that if the optTimeout is set and the involved parties are concurrently enabled/disabled or their participants are connected/disconnected, the command may currently result in spurious timeouts or may return before the transaction appears at all the involved participants.

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `commandId`: `String`
* `optTimeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `com.daml.ledger.javaapi.data.Transaction`

<div id="ledger_api.javaapi.commands.submit_assign" />

### `ledger_api.javaapi.commands.submit_assign`

Submit assign command and wait for the resulting java codegen reassignment, returning the reassignment or failing otherwise.

Submits a assignment command on behalf of `submitter` party, waits for the resulting assignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other participants who were involved in the assignment. The call blocks until the assignment commits or fails. Fails if the assignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants. The reassignmentId should be the one returned by the corresponding submit\_unassign command.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `reassignmentId`: `String`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `com.daml.ledger.javaapi.data.Reassignment`

<div id="ledger_api.javaapi.commands.submit_async" />

### `ledger_api.javaapi.commands.submit_async`

Submit java codegen command asynchronously.

Provides access to the command submission service of the Ledger API. See the [Ledger API reference](https://docs.canton.network/sdks-tools/api-reference/ledger-api) for documentation of the parameters.

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.PartyId]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `commandId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `submissionId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`

<div id="ledger_api.javaapi.commands.submit_unassign" />

### `ledger_api.javaapi.commands.submit_unassign`

Submit assign command and wait for the resulting java codegen reassignment, returning the reassignment or failing otherwise.

Submits an unassignment command on behalf of `submitter` party, waits for the resulting unassignment to commit, and returns the reassignment. If timeout is set, it also waits for the reassignment(s) to appear at all other participants who were involved in the unassignment. The call blocks until the unassignment commits or fails. Fails if the unassignment doesn't commit, or if it doesn't become visible to the involved participants in time. Timeout specifies the time how long to wait until the reassignment appears in the update stream for the submitting and all the involved participants.

**Arguments**

* `submitter`: `com.digitalasset.canton.topology.PartyId`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`
* `workflowId`: `String`
* `userId`: `String`
* `submissionId`: `String`
* `timeout`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.daml.ledger.javaapi.data.Reassignment`

<div id="ledger_api.interactive_submission.execute" />

### `ledger_api.interactive_submission.execute`

Execute a prepared submission.

preparedTransaction: the prepared transaction bytestring, typically obtained from the preparedTransaction field of the \[\[prepare]] response. transactionSignatures: the signatures of the hash of the transaction. The hash is typically obtained from the preparedTransactionHash field of the \[\[prepare]] response. Note however that the caller should re-compute the hash and ensure it matches the one provided in \[\[prepare]], to be certain they're signing a hash that correctly represents the transaction they want to submit.

**Arguments**

* `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.topology.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`

**Returns:** `com.daml.ledger.api.v2.interactive.interactive_submission_service.ExecuteSubmissionResponse`

<div id="ledger_api.interactive_submission.execute_and_wait" />

### `ledger_api.interactive_submission.execute_and_wait`

Execute a prepared submission and wait for it to complete (successfully or not).

Similar to execute, except it will wait for the command to be completed before returning. Equivalent of "submitAndWait" in the CommandService. IMPORTANT: this command assumes that the executing participant is trusted to return a valid command completion. A dishonest executing participant could incorrectly respond that the command failed even though it succeeded.

**Arguments**

* `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.topology.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`

**Returns:** `com.daml.ledger.api.v2.interactive.interactive_submission_service.ExecuteSubmissionAndWaitResponse`

<div id="ledger_api.interactive_submission.execute_and_wait_for_transaction" />

### `ledger_api.interactive_submission.execute_and_wait_for_transaction`

Execute a prepared submission and return the resulting transaction.

Similar to executeAndWait, but returns the resulting transaction. IMPORTANT: this command assumes that the executing participant is trusted to return a valid command completion. A dishonest executing participant could incorrectly respond that the command failed even though it succeeded.

**Arguments**

* `preparedTransaction`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.PreparedTransaction`
* `transactionSignatures`: `Map[com.digitalasset.canton.topology.PartyId,Seq[com.digitalasset.canton.crypto.Signature]]`
* `submissionId`: `String`
* `hashingSchemeVersion`: `com.daml.ledger.api.v2.interactive.interactive_submission_service.HashingSchemeVersion`
* `transactionShape`: `Option[com.daml.ledger.api.v2.transaction_filter.TransactionShape]`
* `userId`: `String`
* `deduplicationPeriod`: `Option[com.digitalasset.canton.data.DeduplicationPeriod]`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `com.daml.ledger.api.v2.transaction.Transaction`

<div id="ledger_api.interactive_submission.help" />

### `ledger_api.interactive_submission.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.interactive_submission.preferred_package_version" />

### `ledger_api.interactive_submission.preferred_package_version`

Get the preferred package version for constructing a command submission.

A preferred package is the highest-versioned package for a provided package-name that is vetted by all the participants hosting the provided parties. Ledger API clients should use this endpoint for constructing command submissions that are compatible with the provided preferred package, by making informed decisions on:

* which are the compatible packages that can be used to create contracts
* which contract or exercise choice argument version can be used in the command
* which choices can be executed on a template or interface of a contract parties: The parties whose vetting state should be considered when computing the preferred package packageName: The package name for which the preferred package is requested synchronizerId: The synchronizer whose topology state to use for resolving this query. If not specified. the topology state of all the synchronizers the participant is connected to will be used. vettingValidAt: The timestamp at which the package vetting validity should be computed If not provided, the participant's current clock time is used.

**Arguments**

* `parties`: `Set[com.digitalasset.canton.topology.Party]`
* `packageName`: `com.digitalasset.canton.LfPackageName`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vettingValidAt`: `Option[com.digitalasset.canton.data.CantonTimestamp]`

**Returns:** `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.PackagePreference]`

<div id="ledger_api.interactive_submission.preferred_packages" />

### `ledger_api.interactive_submission.preferred_packages`

Get the preferred packages for constructing a command submission.

A preferred package is the highest-versioned package for a provided package-name that is vetted by all the participants hosting the provided parties. Ledger API clients should use this endpoint for constructing command submissions that are compatible with the provided preferred package, by making informed decisions on:

* which are the compatible packages that can be used to create contracts
* which contract or exercise choice argument version can be used in the command
* which choices can be executed on a template or interface of a contract

Generally it is enough to provide the requirements for the command's root package-names. Additional package-name requirements can be provided when additional informees need to use package dependencies of the command's root packages.

parties: The parties whose vetting state should be considered when computing the preferred package packageName: The package name for which the preferred package is requested synchronizerId: The synchronizer whose topology state to use for resolving this query. If not specified. the topology state of all the synchronizers the participant is connected to will be used. vettingValidAt: The timestamp at which the package vetting validity should be computed If not provided, the participant's current clock time is used.

**Arguments**

* `packageVettingRequirements`: `Map[com.digitalasset.canton.LfPackageName,Set[com.digitalasset.canton.topology.PartyId]]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vettingValidAt`: `Option[com.digitalasset.canton.data.CantonTimestamp]`

**Returns:** `com.daml.ledger.api.v2.interactive.interactive_submission_service.GetPreferredPackagesResponse`

<div id="ledger_api.interactive_submission.prepare" />

### `ledger_api.interactive_submission.prepare`

Prepare a transaction for interactive submission.

Prepare a transaction for interactive submission. Similar to submit, except instead of submitting the transaction to the network, a serialized version of the transaction will be returned, along with a hash. This allows non-hosted parties to sign the hash with they private key before submitting it via the execute command. If you wish to directly submit a command instead without the external signing step, use submit instead.

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `commands`: `Seq[com.daml.ledger.api.v2.commands.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `commandId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.api.v2.commands.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `verboseHashing`: `Boolean`
* `prefetchContractKeys`: `Seq[com.daml.ledger.api.v2.commands.PrefetchContractKey]`
* `maxRecordTime`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `estimateTrafficCost`: `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.CostEstimationHints]`

**Returns:** `com.daml.ledger.api.v2.interactive.interactive_submission_service.PrepareSubmissionResponse`

<div id="ledger_api.javaapi.interactive_submission.help" />

### `ledger_api.javaapi.interactive_submission.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.javaapi.interactive_submission.prepare" />

### `ledger_api.javaapi.interactive_submission.prepare`

Prepare a transaction for interactive submission.

Prepare a transaction for interactive submission

**Arguments**

* `actAs`: `Seq[com.digitalasset.canton.topology.PartyId]`
* `commands`: `Seq[com.daml.ledger.javaapi.data.Command]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `commandId`: `String`
* `minLedgerTimeAbs`: `Option[java.time.Instant]`
* `readAs`: `Seq[com.digitalasset.canton.topology.Party]`
* `disclosedContracts`: `Seq[com.daml.ledger.javaapi.data.DisclosedContract]`
* `userId`: `String`
* `userPackageSelectionPreference`: `Seq[com.digitalasset.canton.LfPackageId]`
* `verboseHashing`: `Boolean`
* `prefetchContractKeys`: `Seq[com.daml.ledger.javaapi.data.PrefetchContractKey]`
* `maxRecordTime`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `estimateTrafficCost`: `Option[com.daml.ledger.api.v2.interactive.interactive_submission_service.CostEstimationHints]`

**Returns:** `com.daml.ledger.api.v2.interactive.interactive_submission_service.PrepareSubmissionResponse`

#### Event Service

<div id="ledger_api.event_query.by_contract_id" />

### `ledger_api.event_query.by_contract_id`

Get events by contract Id.

Return events associated with the given contract Id

**Arguments**

* `contractId`: `String`
* `requestingParties`: `Seq[com.digitalasset.canton.topology.Party]`

**Returns:** `com.daml.ledger.api.v2.event_query_service.GetEventsByContractIdResponse`

<div id="ledger_api.event_query.help" />

### `ledger_api.event_query.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.javaapi.event_query.by_contract_id" />

### `ledger_api.javaapi.event_query.by_contract_id`

Get events in java codegen by contract Id.

Return events associated with the given contract Id

**Arguments**

* `contractId`: `String`
* `requestingParties`: `Seq[com.digitalasset.canton.topology.Party]`

**Returns:** `com.daml.ledger.api.v2.EventQueryServiceOuterClass.GetEventsByContractIdResponse`

<div id="ledger_api.javaapi.event_query.help" />

### `ledger_api.javaapi.event_query.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

#### Identity Provider Configuration Management

<div id="ledger_api.identity_provider_config.create" />

### `ledger_api.identity_provider_config.create`

Create a new identity provider configuration.

Create an identity provider configuration. The request will fail if the maximum allowed number of separate configurations is reached.

**Arguments**

* `identityProviderId`: `String`
* `isDeactivated`: `Boolean`
* `jwksUrl`: `String`
* `issuer`: `String`
* `audience`: `Option[String]`

**Returns:** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

<div id="ledger_api.identity_provider_config.delete" />

### `ledger_api.identity_provider_config.delete`

Delete an identity provider configuration.

Delete an existing identity provider configuration

**Arguments**

* `identityProviderId`: `String`

<div id="ledger_api.identity_provider_config.get" />

### `ledger_api.identity_provider_config.get`

Get an identity provider configuration.

Get identity provider configuration by id

**Arguments**

* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

<div id="ledger_api.identity_provider_config.help" />

### `ledger_api.identity_provider_config.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.identity_provider_config.list" />

### `ledger_api.identity_provider_config.list`

List identity provider configurations.

List all existing identity provider configurations

**Returns:** `Seq[com.digitalasset.canton.ledger.api.IdentityProviderConfig]`

<div id="ledger_api.identity_provider_config.update" />

### `ledger_api.identity_provider_config.update`

Update an identity provider.

Update identity provider

**Arguments**

* `identityProviderId`: `String`
* `isDeactivated`: `Boolean`
* `jwksUrl`: `String`
* `issuer`: `String`
* `audience`: `Option[String]`
* `updateMask`: `com.google.protobuf.field_mask.FieldMask`

**Returns:** `com.digitalasset.canton.ledger.api.IdentityProviderConfig`

#### User Management Service

<div id="ledger_api.users.create" />

### `ledger_api.users.create`

Create a user with the given id.

Users are used to dynamically managing the rights given to Daml users. They allow us to link a stable local identifier (of an application) with a set of parties. id: the id used to identify the given user actAs: the set of parties this user is allowed to act as primaryParty: the optional party that should be linked to this user by default readAs: the set of parties this user is allowed to read as participantAdmin: flag (default false) indicating if the user is allowed to use the admin commands of the Ledger Api identityProviderAdmin: flag (default false) indicating if the user is allowed to manage users and parties assigned to the same identity provider isDeactivated: flag (default false) indicating if the user is active annotations: the set of key-value pairs linked to this user identityProviderId: identity provider id readAsAnyParty: flag (default false) indicating if the user is allowed to read as any party executeAs: the set of parties for whom this user is allowed to operate interactive submissions executeAsAnyParty: flag (default false) indicating if the user is allowed to operate interactive submissions as any party

**Arguments**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `primaryParty`: `Option[com.digitalasset.canton.topology.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `participantAdmin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `isDeactivated`: `Boolean`
* `annotations`: `Map[String,String]`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `executeAsAnyParty`: `Boolean`

**Returns:** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.delete" />

### `ledger_api.users.delete`

Delete a user.

Delete a user by id. id: user id identityProviderId: identity provider id

**Arguments**

* `id`: `String`
* `identityProviderId`: `String`

<div id="ledger_api.users.get" />

### `ledger_api.users.get`

Get the user data of the user with the given id.

Fetch the data associated with the given user id failing if there is no such user. You will get the user's primary party, active status and annotations. If you need the user rights, use rights.list instead. id: user id identityProviderId: identity provider id

**Arguments**

* `id`: `String`
* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.help" />

### `ledger_api.users.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.users.list" />

### `ledger_api.users.list`

List users.

List users of this participant node filterUser: filter results using the given filter string pageToken: used for pagination (the result contains a page token if there are further pages) pageSize: default page size before the filter is applied identityProviderId: identity provider id

**Arguments**

* `filterUser`: `String`
* `pageToken`: `String`
* `pageSize`: `Int`
* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.UsersPage`

<div id="ledger_api.users.update" />

### `ledger_api.users.update`

Update a user.

Currently you can update the annotations, active status and primary party. You cannot update other user attributes. id: id of the user to be updated modifier: a function for modifying the user; e.g: `user => { user.copy(isActive = false, primaryParty = None, annotations = user.annotations.updated("a", "b").removed("c")) }` identityProviderId: identity provider id

**Arguments**

* `id`: `String`
* `modifier`: `[com.digitalasset.canton.admin.api.client.data.User => com.digitalasset.canton.admin.api.client.data.User](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/User.html)`
* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.User`

<div id="ledger_api.users.update_idp" />

### `ledger_api.users.update_idp`

Update user's identity provider id.

Updates user's identity provider id. id: the id used to identify the given user sourceIdentityProviderId: source identity provider id targetIdentityProviderId: target identity provider id

**Arguments**

* `id`: `String`
* `sourceIdentityProviderId`: `String`
* `targetIdentityProviderId`: `String`

<div id="ledger_api.users.rights.grant" />

### `ledger_api.users.rights.grant`

Grant new rights to a user.

Users are used to dynamically managing the rights given to Daml applications. This function is used to grant new rights to an existing user. id: the id used to identify the given user actAs: the set of parties this user is allowed to act as readAs: the set of parties this user is allowed to read as participantAdmin: flag (default false) indicating if the user is allowed to use the admin commands of the Ledger Api identityProviderAdmin: flag (default false) indicating if the user is allowed to manage users and parties assigned to the same identity provider identityProviderId: identity provider id readAsAnyParty: flag (default false) indicating if the user is allowed to read as any party executeAs: the set of parties for whom this user is allowed to operate interactive submissions executeAsAnyParty: flag (default false) indicating if the user is allowed to operate interactive submissions as any party

**Arguments**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `participantAdmin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `executeAsAnyParty`: `Boolean`

**Returns:** `com.digitalasset.canton.admin.api.client.data.UserRights`

<div id="ledger_api.users.rights.help" />

### `ledger_api.users.rights.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.users.rights.list" />

### `ledger_api.users.rights.list`

List rights of a user.

Lists the rights of a user, or the rights of the current user. id: user id identityProviderId: identity provider id

**Arguments**

* `id`: `String`
* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.UserRights`

<div id="ledger_api.users.rights.revoke" />

### `ledger_api.users.rights.revoke`

Revoke user rights.

Use to revoke specific rights from a user. id: the id used to identify the given user actAs: the set of parties this user should not be allowed to act as readAs: the set of parties this user should not be allowed to read as participantAdmin: if set to true, the participant admin rights will be removed identityProviderAdmin: if set to true, the identity provider admin rights will be removed identityProviderId: identity provider id readAsAnyParty: flag (default false) indicating if the user is allowed to read as any party executeAs: the set of parties for whom this user is allowed to operate interactive submissions executeAsAnyParty: flag (default false) indicating if the user is allowed to operate interactive submissions as any party

**Arguments**

* `id`: `String`
* `actAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `readAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `participantAdmin`: `Boolean`
* `identityProviderAdmin`: `Boolean`
* `identityProviderId`: `String`
* `readAsAnyParty`: `Boolean`
* `executeAs`: `Set[com.digitalasset.canton.topology.PartyId]`
* `executeAsAnyParty`: `Boolean`

**Returns:** `com.digitalasset.canton.admin.api.client.data.UserRights`

#### Package Service

<div id="ledger_api.packages.help" />

### `ledger_api.packages.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.packages.list" />

### `ledger_api.packages.list`

List Daml Packages.

**Arguments**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.daml.ledger.api.v2.admin.package_management_service.PackageDetails]`

<div id="ledger_api.packages.upload_dar" />

### `ledger_api.packages.upload_dar`

Upload packages from Dar file.

Uploading the Dar can be done either through the ledger Api server or through the Canton admin Api. The Ledger Api is the portable method across ledgers. The Canton admin Api is more powerful as it allows for controlling Canton specific behaviour. In particular, a Dar uploaded using the ledger Api will not be available in the Dar store and can not be downloaded again. Additionally, Dars uploaded using the ledger Api will be vetted, but the system will not wait for the Dars to be successfully registered with all connected synchronizers. As such, if a Dar is uploaded and then used immediately thereafter, a command might bounce due to missing package vettings.

**Arguments**

* `darPath`: `String`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

<div id="ledger_api.packages.validate_dar" />

### `ledger_api.packages.validate_dar`

Validate a DAR against the current participants' state.

Performs the same DAR and Daml package validation checks that the upload call performs, but with no effects on the target participants: the DAR is not persisted or vetted.

**Arguments**

* `darPath`: `String`

#### Party Management Service

<div id="ledger_api.parties.allocate" />

### `ledger_api.parties.allocate`

Allocate a new party.

Allocates a new party on the ledger. party: a hint for generating the party identifier annotations: key-value pairs associated with this party and stored locally on this Ledger API server identityProviderId: identity provider id synchronizerId: The synchronizer on which the party should be allocated. The participant must be connected to the synchronizer. The parameter may be omitted if the participant is connected to only one synchronizer.

**Arguments**

* `party`: `String`
* `annotations`: `Map[String,String]`
* `identityProviderId`: `String`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `userId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.parties.PartyDetails`

<div id="ledger_api.parties.allocate_external" />

### `ledger_api.parties.allocate_external`

Allocate a new external party.

Allocates a new external party on the ledger. synchronizerId: SynchronizerId on which to allocate the party transactions: onboarding transactions and their individual signatures multiSignatures: Signatures over the combined hash of all onboarding transactions

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `transactions`: `Seq[(com.digitalasset.canton.topology.transaction.TopologyTransaction.GenericTopologyTransaction, Seq[com.digitalasset.canton.crypto.Signature])]`
* `multiSignatures`: `Seq[com.digitalasset.canton.crypto.Signature]`

**Returns:** `com.daml.ledger.api.v2.admin.party_management_service.AllocateExternalPartyResponse`

<div id="ledger_api.parties.generate_topology" />

### `ledger_api.parties.generate_topology`

Generate topology transactions for an external party.

Convenience function to generate the necessary topology transactions. For more complex setups, please generate your topology transactions manually. synchronizerId: SynchronizerId for which the transactions should be generated. partyHint: the prefix for the party publicKey: the signing public key of the external party localParticipantObservationOnly: if true, then the allocating participant will only be an observer otherConfirmingParticipantUids: list of other participants that will be confirming daml transactions on behalf of the party confirmationThreshold: number of confirming participants which need to approve a daml transaction observingParticipantUids: list of other participants that should observe the transactions of the external party

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `partyHint`: `String`
* `publicKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `localParticipantObservationOnly`: `Boolean`
* `otherConfirmingParticipantIds`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `confirmationThreshold`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `observingParticipantIds`: `Seq[com.digitalasset.canton.topology.ParticipantId]`

**Returns:** `com.digitalasset.canton.admin.api.client.data.parties.GenerateExternalPartyTopology`

<div id="ledger_api.parties.get" />

### `ledger_api.parties.get`

Get party details for known parties.

Get party details for parties known by the Ledger API server for the given identity provider. identityProviderId: identity provider id

**Arguments**

* `parties`: `Seq[com.digitalasset.canton.topology.PartyId]`
* `identityProviderId`: `String`
* `failOnNotFound`: `Boolean`

**Returns:** `Map[com.digitalasset.canton.topology.PartyId,com.digitalasset.canton.admin.api.client.data.parties.PartyDetails]`

<div id="ledger_api.parties.help" />

### `ledger_api.parties.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.parties.list" />

### `ledger_api.parties.list`

List parties known by the Ledger API server.

Lists parties known by the Ledger API server. identityProviderId: identity provider id filterParty: Filter party by name

**Arguments**

* `identityProviderId`: `String`
* `filterParty`: `String`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.parties.PartyDetails]`

<div id="ledger_api.parties.update" />

### `ledger_api.parties.update`

Update participant-local party details.

Currently you can update only the annotations. You cannot update other user attributes. party: party to be updated, modifier: a function to modify the party details, e.g.: `partyDetails => { partyDetails.copy(annotations = partyDetails.annotations.updated("a", "b").removed("c")) }` identityProviderId: identity provider id

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `modifier`: `[com.digitalasset.canton.admin.api.client.data.parties.PartyDetails => com.digitalasset.canton.admin.api.client.data.parties.PartyDetails](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/parties/PartyDetails.html)`
* `identityProviderId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.parties.PartyDetails`

<div id="ledger_api.parties.update_idp" />

### `ledger_api.parties.update_idp`

Update party's identity provider id.

Updates party's identity provider id. party: party to be updated sourceIdentityProviderId: source identity provider id targetIdentityProviderId: target identity provider id

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `sourceIdentityProviderId`: `String`
* `targetIdentityProviderId`: `String`

#### State Service

<div id="ledger_api.state.connected_synchronizers" />

### `ledger_api.state.connected_synchronizers`

Read the current connected synchronizers for a party.

**Arguments**

* `partyId`: `Option[com.digitalasset.canton.topology.PartyId]`

**Returns:** `com.daml.ledger.api.v2.state_service.GetConnectedSynchronizersResponse`

<div id="ledger_api.state.end" />

### `ledger_api.state.end`

Read the current ledger end offset.

**Returns:** `Long`

<div id="ledger_api.state.failed" />

### `ledger_api.state.failed`

Investigate failed commands.

Same as status(..., state = CommandState.Failed).

**Arguments**

* `commandId`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.state.help" />

### `ledger_api.state.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.state.status" />

### `ledger_api.state.status`

Investigate successful and failed commands.

Find the status of commands. Note that only recent commands which are kept in memory will be returned.

**Arguments**

* `commandIdPrefix`: `String`
* `state`: `com.daml.ledger.api.v2.admin.command_inspection_service.CommandState`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.platform.apiserver.execution.CommandStatus]`

<div id="ledger_api.javaapi.state.help" />

### `ledger_api.javaapi.state.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.state.acs.active_contracts_of_party" />

### `ledger_api.state.acs.active_contracts_of_party`

List the set of active contracts of a given party.

This command will return the current set of active contracts for the given party.

Supported arguments:

* `party`: for which party you want to load the acs
* `limit`: limit (default set via canton.parameter.console)
* `verbose`: whether the resulting events should contain detailed type information
* `filterTemplate`: list of templates ids to filter for, empty sequence acts as a wildcard
* `filterInterfaces`: list of interface ids to filter for, empty sequence does not influence the resulting filter
* `activeAtOffsetO`: the offset at which the snapshot of the active contracts will be computed, it must be no greater than the current ledger end offset and must be greater than or equal to the last pruning offset. If no offset is specified then the current participant end will be used.
* `timeout`: the maximum wait time for the complete acs to arrive
* `includeCreatedEventBlob`: whether the result should contain the createdEventBlobs, it works only if the filterTemplate is non-empty

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `Seq[com.daml.ledger.api.v2.state_service.ActiveContract]`

<div id="ledger_api.state.acs.await_active_contract" />

### `ledger_api.state.acs.await_active_contract`

Wait until the party sees the given contract in the active contract service.

Will throw an exception if the contract is not found to be active within the given timeout

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `contractId`: `com.digitalasset.canton.protocol.LfContractId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="ledger_api.state.acs.find_generic" />

### `ledger_api.state.acs.find_generic`

Generic search for contracts.

This search function returns an untyped ledger-api event. The find will wait until the contract appears or throw an exception once it times out.

**Arguments**

* `partyId`: `com.digitalasset.canton.topology.Party`
* `filter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry => Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry`

<div id="ledger_api.state.acs.help" />

### `ledger_api.state.acs.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.state.acs.incomplete_assigned_of_party" />

### `ledger_api.state.acs.incomplete_assigned_of_party`

List the set of incomplete assigned events of a given party.

This command will return the current set of incomplete assigned events for the given party.

Supported arguments:

* `party`: for which party you want to load the acs
* `limit`: limit (default set via canton.parameter.console)
* `verbose`: whether the resulting events should contain detailed type information
* `filterTemplate`: list of templates ids to filter for, empty sequence acts as a wildcard
* `filterInterfaces`: list of interface ids to filter for, empty sequence does not influence the resulting filter
* `activeAtOffsetO`: the offset at which the snapshot of the events will be computed, it must be no greater than the current ledger end offset and must be greater than or equal to the last pruning offset. If no offset is specified then the current participant end will be used.
* `timeout`: the maximum wait time for the complete acs to arrive
* `includeCreatedEventBlob`: whether the result should contain the createdEventBlobs, it works only if the filterTemplate is non-empty

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedIncompleteAssigned]`

<div id="ledger_api.state.acs.incomplete_unassigned_of_party" />

### `ledger_api.state.acs.incomplete_unassigned_of_party`

List the set of incomplete unassigned events of a given party.

This command will return the current set of incomplete unassigned events for the given party.

Supported arguments:

* `party`: for which party you want to load the acs
* `limit`: limit (default set via canton.parameter.console)
* `verbose`: whether the resulting events should contain detailed type information
* `filterTemplate`: list of templates ids to filter for, empty sequence acts as a wildcard
* `filterInterfaces`: list of interface ids to filter for, empty sequence does not influence the resulting filter
* `activeAtOffsetO`: the offset at which the snapshot of the events will be computed, it must be no greater than the current ledger end offset and must be greater than or equal to the last pruning offset. If no offset is specified then the current participant end will be used.
* `timeout`: the maximum wait time for the complete acs to arrive
* `includeCreatedEventBlob`: whether the result should contain the createdEventBlobs, it works only if the filterTemplate is non-empty

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedIncompleteUnassigned]`

<div id="ledger_api.state.acs.of_all" />

### `ledger_api.state.acs.of_all`

List the set of active contracts for all parties hosted on this participant.

This command will return the current set of active contracts for all parties.

Supported arguments:

* `limit`: limit (default set via canton.parameter.console)
* `verbose`: whether the resulting events should contain detailed type information
* `filterTemplate`: list of templates ids to filter for, empty sequence acts as a wildcard
* `filterInterfaces`: list of interface ids to filter for, empty sequence does not influence the resulting filter
* `activeAtOffsetO`: the offset at which the snapshot of the active contracts will be computed, it must be no greater than the current ledger end offset and must be greater than or equal to the last pruning offset. If no offset is specified then the current participant end will be used.
* `timeout`: the maximum wait time for the complete acs to arrive
* `identityProviderId`: limit the response to parties governed by the given identity provider
* `includeCreatedEventBlob`: whether the result should contain the createdEventBlobs, it works only if the filterTemplate is non-empty
* `resultFilter`: custom filter of the results, applies before limit

**Arguments**

* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `identityProviderId`: `String`
* `includeCreatedEventBlob`: `Boolean`
* `resultFilter`: `com.daml.ledger.api.v2.state_service.GetActiveContractsResponse => Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry]`

<div id="ledger_api.state.acs.of_party" />

### `ledger_api.state.acs.of_party`

List the set of active contract entries of a given party.

This command will return the current set of active contracts and incomplete reassignments for the given party.

Supported arguments:

* `party`: for which party you want to load the acs
* `limit`: limit (default set via canton.parameter.console)
* `verbose`: whether the resulting events should contain detailed type information
* `filterTemplate`: list of templates ids to filter for, empty sequence acts as a wildcard
* `activeAtOffsetO`: the offset at which the snapshot of the active contracts will be computed, it must be no greater than the current ledger end offset and must be greater than or equal to the last pruning offset. If no offset is specified then the current participant end will be used.
* `timeout`: the maximum wait time for the complete acs to arrive
* `includeCreatedEventBlob`: whether the result should contain the createdEventBlobs, it works only if the filterTemplate is non-empty
* `resultFilter`: custom filter of the results, applies before limit

**Arguments**

* `party`: `com.digitalasset.canton.topology.Party`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `verbose`: `Boolean`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `filterInterfaces`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `activeAtOffsetO`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `includeCreatedEventBlob`: `Boolean`
* `resultFilter`: `com.daml.ledger.api.v2.state_service.GetActiveContractsResponse => Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry]`

<div id="ledger_api.javaapi.state.acs.await" />

### `ledger_api.javaapi.state.acs.await`

Wait until a contract becomes available and return the Java codegen contract.

This function can be used for contracts with a code-generated Java model. You can refine your search using the `filter` function argument. You can restrict search to a synchronizer by specifying the optional synchronizer id. The command will wait until the contract appears or throw an exception once it times out.

**Arguments**

* `companion`: `com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T]`
* `partyId`: `com.digitalasset.canton.topology.Party`
* `predicate`: `TC => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `(companion: com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T])(partyId: com.digitalasset.canton.topology.Party, predicate: TC => Boolean, synchronizerFilter: Option[com.digitalasset.canton.topology.SynchronizerId], timeout: com.digitalasset.canton.config.NonNegativeDuration): TC`

<div id="ledger_api.javaapi.state.acs.filter" />

### `ledger_api.javaapi.state.acs.filter`

Filter the ACS for contracts of a particular Java code-generated template.

To use this function, ensure a code-generated Java model for the target template exists. You can refine your search using the `predicate` function argument. You can restrict search to a synchronizer by specifying the optional synchronizer id.

**Arguments**

* `templateCompanion`: `com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T]`
* `partyId`: `com.digitalasset.canton.topology.Party`
* `predicate`: `TC => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

**Returns:** `(templateCompanion: com.daml.ledger.javaapi.data.codegen.ContractCompanion[TC,TCid,T])(partyId: com.digitalasset.canton.topology.Party, predicate: TC => Boolean, synchronizerFilter: Option[com.digitalasset.canton.topology.SynchronizerId]): Seq[TC]`

<div id="ledger_api.javaapi.state.acs.help" />

### `ledger_api.javaapi.state.acs.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

#### Time Service

<div id="ledger_api.time.get" />

### `ledger_api.time.get`

Get the participants time.

Returns the current timestamp of the participant which is either the system clock or the static time

**Returns:** `com.digitalasset.canton.data.CantonTimestamp`

<div id="ledger_api.time.set" />

### `ledger_api.time.set`

Set the participants time.

Sets the participants time if the participant is running in static time mode

**Arguments**

* `currentTime`: `com.digitalasset.canton.data.CantonTimestamp`
* `nextTime`: `com.digitalasset.canton.data.CantonTimestamp`

#### Updates Service

<div id="ledger_api.updates.help" />

### `ledger_api.updates.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.updates.reassignments" />

### `ledger_api.updates.reassignments`

Get reassignments.

This function connects to the update stream for the given parties and template ids and collects reassignment events (assigned and unassigned) until either `completeAfter` updates have been received or `timeout` has elapsed. If the party ids set is empty then the reassignments for all the parties will be fetched. If the template ids collection is empty then the reassignments for all the template ids will be fetched. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `partyIds`: `Set[com.digitalasset.canton.topology.PartyId]`
* `filterTemplates`: `Seq[com.digitalasset.canton.admin.api.client.data.TemplateId]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.ReassignmentWrapper]`

<div id="ledger_api.updates.start_measuring" />

### `ledger_api.updates.start_measuring`

Starts measuring throughput at the update service.

This function will subscribe on behalf of `parties` to the update stream and notify various metrics: The metric `<name>.<metricSuffix>` counts the number of update trees emitted. The metric `<name>.<metricSuffix>-tx-node-count` tracks the number of events emitted as part of update. The metric `<name>.<metricSuffix>-tx-size` tracks the number of bytes emitted as part of update trees.

To stop measuring, you need to close the returned `AutoCloseable`. Use the `onUpdate` parameter to register a callback that is called on every update tree.

**Arguments**

* `parties`: `Set[com.digitalasset.canton.topology.Party]`
* `metricName`: `String`
* `onUpdate`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Unit`

**Returns:** `AutoCloseable`

<div id="ledger_api.updates.subscribe_updates" />

### `ledger_api.updates.subscribe_updates`

Subscribe to the update stream.

This function connects to the update stream and passes updates to `observer` until the stream is completed. The updates as described in the update format will be returned. Use `EventFormat(Map(myParty.toLf -> Filters()))` to return transactions or reassignments for `myParty: PartyId`. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `observer`: `io.grpc.stub.StreamObserver[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`

**Returns:** `AutoCloseable`

<div id="ledger_api.updates.topology_transactions" />

### `ledger_api.updates.topology_transactions`

Get topology transactions.

This function connects to the update stream for the given parties and collects topology transaction events until either `completeAfter` updates have been received or `timeout` has elapsed. If the party ids seq is empty then the topology transactions for all the parties will be fetched. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `partyIds`: `Seq[com.digitalasset.canton.topology.Party]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.TopologyTransactionWrapper]`

<div id="ledger_api.updates.transactions" />

### `ledger_api.updates.transactions`

Get transactions.

This function connects to the update stream for the given parties and collects updates until either `completeAfter` transactions have been received or `timeout` has elapsed. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If you need to specify filtering conditions for template IDs and including create event blobs for explicit disclosure, consider using `tx_with_tx_format`. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `partyIds`: `Set[com.digitalasset.canton.topology.Party]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`
* `includeCreatedEventBlob`: `Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.TransactionWrapper]`

<div id="ledger_api.updates.transactions_with_tx_format" />

### `ledger_api.updates.transactions_with_tx_format`

Get updates.

This function connects to the update stream for the given transaction format and collects updates until either `completeAfter` transactions have been received or `timeout` has elapsed. The returned transactions can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If you only need to filter by a set of parties, consider using `transactions` instead. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `transactionFormat`: `com.daml.ledger.api.v2.transaction_filter.TransactionFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.update_by_id" />

### `ledger_api.updates.update_by_id`

Get an update by its ID.

Get an update by its ID. Returns None if the update is not (yet) known at the participant or all the events of the update are filtered due to the update format or if the update has been pruned via `pruning.prune`.

**Arguments**

* `id`: `String`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`

**Returns:** `Option[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.update_by_offset" />

### `ledger_api.updates.update_by_offset`

Get an update by its offset.

Get an update by its offset. Returns None if the update is not (yet) known at the participant or all the events of the update are filtered due to the update format or if the update has been pruned via `pruning.prune`.

**Arguments**

* `offset`: `Long`
* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`

**Returns:** `Option[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.updates.updates" />

### `ledger_api.updates.updates`

Get updates.

This function connects to the update stream for the given parties and collects updates until either `completeAfter` updates have been received or `timeout` has elapsed. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper]`

<div id="ledger_api.javaapi.updates.help" />

### `ledger_api.javaapi.updates.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="ledger_api.javaapi.updates.transactions" />

### `ledger_api.javaapi.updates.transactions`

Get transactions in the format expected by the Java bindings.

This function connects to the update stream for the given parties and collects updates until either `completeAfter` transactions have been received or `timeout` has elapsed. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If you need to specify filtering conditions for template IDs and including create event blobs for explicit disclosure, consider using `tx_with_tx_format`. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `partyIds`: `Set[com.digitalasset.canton.topology.Party]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `verbose`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `transactionShape`: `com.daml.ledger.api.v2.transaction_filter.TransactionShape`

**Returns:** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

<div id="ledger_api.javaapi.updates.transactions_with_tx_format" />

### `ledger_api.javaapi.updates.transactions_with_tx_format`

Get transactions in the format expected by the Java bindings.

This function connects to the update stream for the given transaction format and collects updates until either `completeAfter` transactions have been received or `timeout` has elapsed. The returned transactions can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If you only need to filter by a set of parties, consider using `flat` or `trees` instead. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `transactionFormat`: `com.daml.ledger.javaapi.data.TransactionFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`

**Returns:** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

<div id="ledger_api.javaapi.updates.updates" />

### `ledger_api.javaapi.updates.updates`

Get updates in the format expected by the Java bindings.

This function connects to the update stream for the given parties and collects updates until either `completeAfter` updates have been received or `timeout` has elapsed. The returned updates can be filtered to be between the given offsets (default: no filtering). If the participant has been pruned via `pruning.prune` and if `beginOffset` is lower than the pruning offset, this command fails with a `NOT_FOUND` error. If the beginOffset is zero then the participant begin is taken as beginning offset. If the endOffset is None then a continuous stream is returned.

**Arguments**

* `updateFormat`: `com.daml.ledger.api.v2.transaction_filter.UpdateFormat`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `resultFilter`: `com.digitalasset.canton.admin.api.client.commands.LedgerApiCommands.UpdateService.UpdateWrapper => Boolean`
* `synchronizerFilter`: `Option[com.digitalasset.canton.topology.SynchronizerId]`

**Returns:** `Seq[com.daml.ledger.javaapi.data.GetUpdatesResponse]`

### Ledger Pruning

<div id="pruning.clear_schedule_1" />

### `pruning.clear_schedule_1`

Deactivate automatic pruning.

<div id="pruning.find_safe_offset" />

### `pruning.find_safe_offset`

Return the highest participant ledger offset whose record time is before or at the given one (if any) at which pruning is safely possible.

**Arguments**

* `beforeOrAt`: `java.time.Instant`

**Returns:** `Option[Long]`

<div id="pruning.get_offset_by_time" />

### `pruning.get_offset_by_time`

Identify the participant ledger offset to prune up to based on the specified timestamp.

Return the largest participant ledger offset that has been processed before or at the specified timestamp. The time is measured on the participant's local clock at some point while the participant has processed the the event. Returns `None` if no such offset exists.

**Arguments**

* `upToInclusive`: `java.time.Instant`

**Returns:** `Option[Long]`

<div id="pruning.get_participant_schedule" />

### `pruning.get_participant_schedule`

Inspect the automatic, participant-specific pruning schedule.

The schedule consists of a "cron" expression and "max\_duration" and "retention" durations as described in the `get_schedule` command description. Additionally "prune\_internally" indicates if the schedule mandates pruning of internal state.

**Returns:** `Option[com.digitalasset.canton.admin.api.client.data.ParticipantPruningSchedule]`

<div id="pruning.get_schedule" />

### `pruning.get_schedule`

Inspect the automatic pruning schedule.

The schedule consists of a "cron" expression and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period. Returns `None` if no schedule has been configured via `set_schedule` or if `clear_schedule` has been invoked.

**Returns:** `Option[com.digitalasset.canton.admin.api.client.data.PruningSchedule]`

<div id="pruning.help_1" />

### `pruning.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="pruning.prune" />

### `pruning.prune`

Prune the ledger up to the specified offset inclusively.

Prunes the participant ledger up to the specified offset inclusively returning `Unit` if the ledger has been successfully pruned. Note that upon successful pruning, subsequent attempts to read transactions via `ledger_api.transactions.flat` or `ledger_api.transactions.trees` or command completions via `ledger_api.completions.list` by specifying a begin offset lower than the returned pruning offset will result in a `NOT_FOUND` error. The `prune` operation performs a "full prune" freeing up significantly more space and also performs additional safety checks returning a `NOT_FOUND` error if `pruneUpTo` is higher than the offset returned by `find_safe_offset` on any synchronizer with events preceding the pruning offset.

**Arguments**

* `pruneUpTo`: `Long`

<div id="pruning.prune_internally" />

### `pruning.prune_internally`

Prune only internal ledger state up to the specified offset inclusively.

Special-purpose variant of the `prune` command that prunes only partial, internal participant ledger state freeing up space not needed for serving `ledger_api.transactions` and `ledger_api.completions` requests. In conjunction with `prune`, `prune_internally` enables pruning internal ledger state more aggressively than externally observable data via the ledger api. In most use cases `prune` should be used instead. Unlike `prune`, `prune_internally` has no visible effect on the Ledger API. The command returns `Unit` if the ledger has been successfully pruned or an error if the timestamp performs additional safety checks returning a `NOT_FOUND` error if `pruneUpTo` is higher than the offset returned by `find_safe_offset` on any synchronizer with events preceding the pruning offset.

**Arguments**

* `pruneUpTo`: `Long`
* `safeToPruneCommitmentState`: `Option[com.digitalasset.canton.scheduler.SafeToPruneCommitmentState]`

<div id="pruning.set_cron" />

### `pruning.set_cron`

Modify the cron used by automatic pruning.

The schedule is specified in cron format and refers to pruning start times in the GMT time zone. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `cron`: `String`

<div id="pruning.set_max_duration" />

### `pruning.set_max_duration`

Modify the maximum duration used by automatic pruning.

The `maxDuration` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_participant_schedule" />

### `pruning.set_participant_schedule`

Activate automatic pruning according to the specified schedule with participant-specific options.

Refer to the `set_schedule` description for information about the "cron", "max\_duration", and "retention" parameters. Setting the "prune\_internally\_only" flag causes pruning to only remove internal state as described in more detail in the `prune_internally` command description.

**Arguments**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `pruneInternallyOnly`: `Boolean`

<div id="pruning.set_retention" />

### `pruning.set_retention`

Update the pruning retention used by automatic pruning.

The `retention` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this update, pruning is actively running, a best effort is made to pause pruning and restart with the newly specified retention. This allows for the case that the new retention mandates retaining more data than previously.

**Arguments**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_schedule_1" />

### `pruning.set_schedule_1`

Activate automatic pruning according to the specified schedule.

The schedule is specified in cron format and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period.

**Arguments**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

### Metrics

<div id="metrics.get" />

### `metrics.get`

Get a particular metric.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point" />

### `metrics.get_double_point`

Get a particular double point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram" />

### `metrics.get_histogram`

Get a particular histogram.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point" />

### `metrics.get_long_point`

Get a particular long point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary" />

### `metrics.get_summary`

Get a particular summary.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list" />

### `metrics.list`

List all metrics.

Returns the metric with the given name and optionally matching attributes.

**Arguments**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

## Multiple Participants

This section lists the commands available for a sequence of participants. They can be used on the participant references `participants.all`, `.local` or `.remote` as:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.all.dars.upload("my.dar")
```

<div id="help_4" />

### `help_4`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="dars.help_1" />

### `dars.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="dars.upload_1" />

### `dars.upload_1`

Upload DARs to participants.

If synchronizerId is set, the participants will vet the packages on the specified synchronizer. If synchronizeVetting is true, the command will block until the package vetting transaction has been registered with all connected synchronizers.

**Arguments**

* `darPath`: `String`
* `description`: `String`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `expectedMainPackageId`: `String`
* `requestHeaders`: `Map[String,String]`

**Returns:** `Map[com.digitalasset.canton.console.ParticipantReference,String]`

<div id="dars.upload_many_1" />

### `dars.upload_many_1`

Upload DARs to participants.

If synchronizerId is set, the participants will vet the packages on the specified synchronizer. If synchronizeVetting is true, the command will block until the package vetting transaction has been registered with all connected synchronizers.

**Arguments**

* `paths`: `Seq[String]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `vetAllPackages`: `Boolean`
* `synchronizeVetting`: `Boolean`
* `requestHeaders`: `Map[String,String]`
* `logger`: `com.digitalasset.canton.logging.TracedLogger`

**Returns:** `Map[com.digitalasset.canton.console.ParticipantReference,Seq[String]]`

<div id="dars.validate_1" />

### `dars.validate_1`

Validate DARs against the current participants' state.

Performs the same DAR and Daml package validation checks that the upload call performs, but with no effects on the target participants: the DAR is not persisted or vetted.

**Arguments**

* `darPath`: `String`

**Returns:** `Map[com.digitalasset.canton.console.ParticipantReference,String]`

<div id="synchronizers.connect_2" />

### `synchronizers.connect_2`

Connect to a synchronizer.

**Arguments**

* `config`: `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="synchronizers.connect_local_1" />

### `synchronizers.connect_local_1`

Register and potentially connect to new local synchronizer.

The arguments are:

* `sequencer`: A local sequencer reference alias - A synchronizer alias to register this connection for.
* `manualConnect`: Whether this connection should be handled manually and also excluded from automatic re-connect.
* `physicalSynchronizerId`: An optional Synchronizer Id to ensure the connection is made to the correct synchronizer.
* `synchronize`: A timeout duration indicating how long to wait for all topology changes to have been effected on all local nodes.

**Arguments**

* `sequencer`: `com.digitalasset.canton.console.SequencerReference`
* `alias`: `com.digitalasset.canton.SynchronizerAlias`
* `manualConnect`: `Boolean`
* `physicalSynchronizerId`: `Option[com.digitalasset.canton.topology.PhysicalSynchronizerId]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="synchronizers.disconnect_1" />

### `synchronizers.disconnect_1`

Disconnect from synchronizer.

**Arguments**

* `alias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="synchronizers.disconnect_all_1" />

### `synchronizers.disconnect_all_1`

Disconnect from all connected synchronizers.

<div id="synchronizers.help_1" />

### `synchronizers.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="synchronizers.reconnect_1" />

### `synchronizers.reconnect_1`

Reconnect to synchronizer.

If retry is set to true (default), the command will return after the first attempt, but keep on trying in the background.

**Arguments**

* `alias`: `com.digitalasset.canton.SynchronizerAlias`
* `retry`: `Boolean`

<div id="synchronizers.reconnect_all_1" />

### `synchronizers.reconnect_all_1`

Reconnect to all synchronizers for which `manualStart` = false.

If ignoreFailures is set to true (default), the reconnect all will succeed even if some synchronizers are offline. The participants will continue attempting to establish a synchronizer connection.

**Arguments**

* `ignoreFailures`: `Boolean`

<div id="synchronizers.register_1" />

### `synchronizers.register_1`

Register a synchronizer.

**Arguments**

* `config`: `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`
* `performHandshake`: `Boolean`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

### Packages

<div id="packages.find_by_module" />

### `packages.find_by_module`

Find packages that contain a module with the given name.

**Arguments**

* `moduleName`: `String`
* `limitPackages`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.PackageDescription]`

<div id="packages.get_contents" />

### `packages.get_contents`

Get the package contents.

**Arguments**

* `packageId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.PackageDescription.PackageContents`

<div id="packages.get_references" />

### `packages.get_references`

Returns the list of DARs referencing the given package.

**Arguments**

* `packageId`: `String`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.DarDescription]`

<div id="packages.help" />

### `packages.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="packages.list" />

### `packages.list`

List packages stored on the participant.

Supported arguments:

limit - Limit on the number of packages returned (defaults to canton.parameters.console.default-limit)

**Arguments**

* `filterName`: `String`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.PackageDescription]`

<div id="packages.remove" />

### `packages.remove`

Remove the package from Canton's package store.

The standard operation of this command checks that a package is unused and unvetted, and if so removes the package. The force flag can be used to disable the checks, but do not use the force flag unless you're certain you know what you're doing.

**Arguments**

* `packageId`: `String`
* `force`: `Boolean`

<div id="packages.synchronize_vetting" />

### `packages.synchronize_vetting`

Ensure that all vetting transactions issued by this participant have been observed by all configured participants.

Sometimes, when scripting tests and demos, a dar or package is uploaded and we need to ensure that commands are only submitted once the package vetting has been observed by some other connected participant known to the console. This command can be used in such cases.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

### Party Management

The party management commands allow to conveniently enable and disable parties on the local node. Under the hood, they use the more complicated but feature-richer identity management commands.

<div id="parties.add_party_async" />

### `parties.add_party_async`

Add a previously existing party to the local participant.

Initiate adding a previously existing party to this participant on the specified synchronizer. Performs some checks synchronously and then initiates party replication asynchronously. The returned `addPartyRequestId` parameter allows identifying asynchronous progress and errors.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `sourceParticipant`: `com.digitalasset.canton.topology.ParticipantId`
* `serial`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `participantPermission`: `com.digitalasset.canton.topology.transaction.ParticipantPermission`

**Returns:** `String`

<div id="parties.clear_party_onboarding_flag" />

### `parties.clear_party_onboarding_flag`

Clears the onboarding flag for a party.

Instructs the participant to unilaterally clear the 'onboarding' flag on the party-to-participant topology mapping.

This operation is time-sensitive. If run too soon, the flag cannot be safely cleared, and another attempt needs to be made.

This endpoint is idempotent and can be safely called multiple times. Polling is necessary because the flag can only be cleared after a specific time has passed, and the underlying change may take time to become effective.

Prerequisite: A prior party-to-participant mapping topology transaction must exist that activates the party on the participant with the onboarding flag set to true.

Returns a tuple with the current status:

* `Cleared`: (true, None) – The flag is successfully cleared.
* `Pending`: (false, Some(timestamp)) – The flag is still set. The timestamp indicates the earliest safe time to clear the flag. You may wait until after this time to run the command again.

The arguments are:

* `party`: The party being onboarded, it must already be active on the participant.
* `synchronizerId`: Restricts the party onboarding to the given synchronizer.
* `beginOffsetExclusive`: Exclusive ledger offset used as a starting point to find the party's activation on the participant.
* `waitForActivationTimeout`: The maximum duration the service will wait to find the topology transaction that activates the party.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `beginOffsetExclusive`: `Long`
* `waitForActivationTimeout`: `Option[com.digitalasset.canton.config.NonNegativeFiniteDuration]`

**Returns:** `(Boolean, Option[com.digitalasset.canton.data.CantonTimestamp])`

<div id="parties.disable" />

### `parties.disable`

Disable party on participant.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `synchronizer`: `Option[com.digitalasset.canton.SynchronizerAlias]`

<div id="parties.enable" />

### `parties.enable`

Enable/add party to participant.

This function registers a new party on a synchronizer with the current participant within the participants namespace. The function fails if the participant does not have appropriate signing keys to issue the corresponding PartyToParticipant topology transaction, or if the participant is not connected to any synchronizers. The synchronizer parameter does not have to be specified if the participant is connected only to one synchronizer. If the participant is connected to multiple synchronizers, the party needs to be enabled on each synchronizer explicitly. Additionally, a sequence of additional participants can be added to be synchronized to ensure that the party is known to these participants as well before the function terminates.

**Arguments**

* `name`: `String`
* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `synchronizer`: `Option[com.digitalasset.canton.SynchronizerAlias]`
* `synchronizeParticipants`: `Seq[com.digitalasset.canton.console.ParticipantReference]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.PartyId`

<div id="parties.export_party_acs" />

### `parties.export_party_acs`

Export active contracts for a given party to replicate it.

This command exports the current Active Contract Set (ACS) for a given party to facilitate its replication from a source to a target participant.

It uses the party's most recent activation on the target participant to determine the precise historical state of the ACS to export from the source participant.

"Activation" on the target participant means the new hosting arrangement has been authorized by both the party itself and the target participant via party-to-participant topology transactions.

This command will fail if the party has not yet been activated on the target participant.

Upon successful completion, the command writes a GZIP-compressed ACS snapshot file. This file should then be imported into the target participant's ACS using the `import_party_acs` command.

The arguments are:

* `party`: The party being replicated, it must already be active on the target participant.
* `synchronizerId`: Restricts the export to the given synchronizer.
* `targetParticipantId`: Unique identifier of the target participant where the party will be replicated.
* `beginOffsetExclusive`: Exclusive ledger offset used as starting point fo find the party's activation on the target participant.
* `exportFilePath`: The path denoting the file where the ACS snapshot will be stored.
* `waitForActivationTimeout`: The maximum duration the service will wait to find the topology transaction that activates the party on the target participant.
* `timeout`: A timeout for this operation to complete.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `targetParticipantId`: `com.digitalasset.canton.topology.ParticipantId`
* `beginOffsetExclusive`: `Long`
* `exportFilePath`: `String`
* `waitForActivationTimeout`: `Option[com.digitalasset.canton.config.NonNegativeFiniteDuration]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="parties.find" />

### `parties.find`

Find a party from a filter string.

Will search for all parties that match this filter string. If it finds exactly one party, it will return that one. Otherwise, the function will throw.

**Arguments**

* `filterParty`: `String`

**Returns:** `com.digitalasset.canton.topology.PartyId`

<div id="parties.find_highest_offset_by_timestamp" />

### `parties.find_highest_offset_by_timestamp`

Find highest ledger offset by timestamp.

This command attempts to find the highest ledger offset among all events belonging to a synchronizer that have a record time before or at the given timestamp.

Returns the highest ledger offset, or an error.

Possible failure causes:

* The requested timestamp is too far in the past for which no events exist anymore.
* There are no events for the given synchronizer.
* Not all events have been processed fully and/or published to the Ledger API DB until the requested timestamp.

Depending on the failure cause, this command can be tried to get a ledger offset. For example, if not all events have been processed fully and/or published to the Ledger API DB, a retry makes sense.

The arguments are:

* `synchronizerId`: Restricts the query to a particular synchronizer.
* `timestamp`: A point in time.
* `force`: Defaults to false. If true, returns the highest currently known ledger offset with a record time before or at the given timestamp.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `timestamp`: `java.time.Instant`
* `force`: `Boolean`

**Returns:** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="parties.find_party_max_activation_offset" />

### `parties.find_party_max_activation_offset`

Finds a party's highest activation offset.

This command locates the highest ledger offset where a party's activation matches specified criteria.

It searches the ledger for topology transactions, sequenced by the given synchronizer (`synchronizerId`), that result in the party (`partyId`) being newly hosted on the participant (`participantId`). An optional `validFrom` timestamp filters the topology transactions for their effective time.

The ledger search occurs within the specified offset range, targeting a specific number of topology transactions (`completeAfter`).

The search begins at the ledger start if `beginOffsetExclusive` is default. If the participant was pruned and `beginOffsetExclusive` is below the pruning offset, a `NOT_FOUND` error occurs. Use an `beginOffsetExclusive` near, but before, the desired topology transactions.

If `endOffsetInclusive` is not set (`None`), the search continues until `completeAfter` number of transactions are found or the `timeout` expires. Otherwise, the ledger search ends at the specified offset.

This command is useful for creating ACS snapshots with `export_acs`, which requires the party activation ledger offset.

The arguments are:

* `partyId`: The party to find activations for.
* `participantId`: The participant hosting the new party.
* `synchronizerId`: The synchronizer sequencing the activations.
* `validFrom`: The activation's effective time (default: None).
* `beginOffsetExclusive`: Starting ledger offset (default: 0).
* `endOffsetInclusive`: Ending ledger offset (default: None = trailing search).
* `completeAfter`: Number of transactions to find (default: Maximum = no limit).
* `timeout`: Search timeout (default: 1 minute).

**Arguments**

* `partyId`: `com.digitalasset.canton.topology.PartyId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `validFrom`: `Option[java.time.Instant]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="parties.find_party_max_deactivation_offset" />

### `parties.find_party_max_deactivation_offset`

Finds a party's highest deactivation offset.

This command locates the highest ledger offset where a party's deactivation matches specified criteria.

It searches the ledger for topology transactions, sequenced by the given synchronizer (`synchronizerId`), that result in the party (`partyId`) being revoked on the participant (`participantId`). An optional `validFrom` timestamp filters the topology transactions for their effective time.

The ledger search occurs within the specified offset range, targeting a specific number of topology transactions (`completeAfter`).

The search begins at the ledger start if `beginOffsetExclusive` is default. If the participant was pruned and `beginOffsetExclusive` is below the pruning offset, a `NOT_FOUND` error occurs. Use an `beginOffsetExclusive` near, but before, the desired topology transactions.

If `endOffsetInclusive` is not set (`None`), the search continues until `completeAfter` number of transactions are found or the `timeout` expires. Otherwise, the ledger search ends at the specified offset.

This command is useful for finding active contracts at the ledger offset where a party has been off-boarded from a participant.

The arguments are:

* `partyId`: The party to find deactivations for.
* `participantId`: The participant hosting the new party.
* `synchronizerId`: The synchronizer sequencing the deactivations.
* `validFrom`: The deactivation's effective time (default: None).
* `beginOffsetExclusive`: Starting ledger offset (default: 0).
* `endOffsetInclusive`: Ending ledger offset (default: None = trailing search).
* `completeAfter`: Number of transactions to find (default: Maximum = no limit).
* `timeout`: Search timeout (default: 1 minute).

**Arguments**

* `partyId`: `com.digitalasset.canton.topology.PartyId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `validFrom`: `Option[java.time.Instant]`
* `beginOffsetExclusive`: `Long`
* `endOffsetInclusive`: `Option[Long]`
* `completeAfter`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="parties.get_add_party_status" />

### `parties.get_add_party_status`

Obtain status on a pending `add_party_async` call.

Retrieve status information on a party previously added via the `add_party_async` endpoint by specifying the previously returned `addPartyRequestId` parameter.

**Arguments**

* `addPartyRequestId`: `String`

**Returns:** `com.digitalasset.canton.admin.api.client.data.AddPartyStatus`

<div id="parties.help" />

### `parties.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="parties.hosted" />

### `parties.hosted`

List parties hosted by this participant.

Inspect the parties hosted by this participant as used for synchronisation. The response is built from the timestamped topology transactions of each synchronizer, excluding the authorized store of the given node. The search will include all hosted parties and is equivalent to running the `list` method using the participant id of the invoking participant.

filterParty: Filter by parties starting with the given string. filterSynchronizerId: Filter by synchronizers whose id starts with the given string. asOf: Optional timestamp to inspect the topology state at a given point in time. limit: How many items to return (defaults to canton.parameters.console.default-limit)

Example: participant1.parties.hosted(filterParty="alice")

**Arguments**

* `filterParty`: `String`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListPartiesResult]`

<div id="parties.import_party_acs" />

### `parties.import_party_acs`

Import active contracts from a snapshot file to replicate a party.

This command imports contracts from an Active Contract Set (ACS) snapshot file into the participant's ACS. It expects the given ACS snapshot file to be the result of a previous `export_party_acs` command invocation.

The argument is:

* `importFilePath`: The path denoting the file from where the ACS snapshot will be read. Defaults to "canton-acs-export.gz" when undefined.
* `workflowIdPrefix`: Sets a custom prefix for the workflow ID to easily identify all transactions generated by this import. Defaults to "import-\<random\_UUID>" when unspecified.
* `contractImportMode`: Governs contract authentication processing on import. Options include Validation (default), \[Accept, Recomputation].
* `representativePackageIdOverride`: Defines override mappings for assigning representative package IDs to contracts upon ACS import. Defaults to NoOverride when undefined.

**Arguments**

* `importFilePath`: `String`
* `workflowIdPrefix`: `String`
* `contractImportMode`: `com.digitalasset.canton.participant.admin.data.ContractImportMode`
* `representativePackageIdOverride`: `com.digitalasset.canton.participant.admin.data.RepresentativePackageIdOverride`

<div id="parties.list" />

### `parties.list`

List active parties, their active participants, and the participants' permissions on synchronizers.

Inspect the parties known by this participant as used for synchronisation. The response is built from the timestamped topology transactions of each synchronizer, excluding the authorized store of the given node. For each known party, the list of active participants and their permission on the synchronizer for that party is given.

filterParty: Filter by parties starting with the given string. filterParticipant: Filter for parties that are hosted by a participant with an id starting with the given string filterSynchronizerId: Filter by synchronizers whose id starts with the given string. asOf: Optional timestamp to inspect the topology state at a given point in time. limit: Limit on the number of parties fetched (defaults to canton.parameters.console.default-limit).

Example: participant1.parties.list(filterParty="alice")

**Arguments**

* `filterParty`: `String`
* `filterParticipant`: `String`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListPartiesResult]`

### Participant Repair

<div id="repair.add" />

### `repair.add`

Add specified contracts to a specific synchronizer on the participant.

This is a last resort command to recover from data corruption, e.g. in scenarios in which participant contracts have somehow gotten out of sync and need to be manually created. The participant needs to be disconnected from the specified "synchronizer" at the time of the call, and as of now the synchronizer cannot have had any inflight requests. The effects of the command will take affect upon reconnecting to the sync synchronizer. As repair commands are powerful tools to recover from unforeseen data corruption, but dangerous under normal operation, use of this command requires (temporarily) enabling the "features.enable-repair-commands" configuration. In addition repair commands can run for an unbounded time depending on the number of contracts passed in. Be sure to not connect the participant to the synchronizer until the call returns.

The arguments are:

* `synchronizerId`: the id of the synchronizer to which to add the contract
* `protocolVersion`: to protocol version used by the synchronizer
* `contracts`: list of contracts to add with witness information

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `contracts`: `Seq[com.digitalasset.canton.participant.admin.data.RepairContract]`
* `allowContractIdSuffixRecomputation`: `Boolean`

**Returns:** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.change_assignation" />

### `repair.change_assignation`

Change assignation of contracts from one synchronizer to another.

This is a last resort command to recover from data corruption in scenarios in which a synchronizer is irreparably broken and formerly connected participants need to change the assignation of contracts to another, healthy synchronizer. The participant needs to be disconnected from both the "sourceSynchronizer" and the "targetSynchronizer". The target synchronizer cannot have had any inflight requests. Contracts already assigned to the target synchronizer will be skipped, and this makes it possible to invoke this command in an "idempotent" fashion in case an earlier attempt had resulted in an error. The "skipInactive" flag makes it possible to only change the assignment of active contracts in the "sourceSynchronizer". As repair commands are powerful tools to recover from unforeseen data corruption, but dangerous under normal operation, use of this command requires (temporarily) enabling the "features.enable-repair-commands" configuration. In addition repair commands can run for an unbounded time depending on the number of contract ids passed in. Be sure to not connect the participant to either synchronizer until the call returns.

Arguments:

* contractsIds
* Set of contract ids that should change assignation to the new synchronizer
* sourceSynchronizerAlias
* alias of the source synchronizer
* targetSynchronizerAlias
* alias of the target synchronizer
* reassignmentCounterOverride
* by default, the reassignment counter is increased by one during the change assignation procedure if the value of the reassignment counter needs to be forced, the new value can be passed in the map
* skipInactive - (default true) whether to skip inactive contracts mentioned in the contractIds list

**Arguments**

* `contractsIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `sourceSynchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `targetSynchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `reassignmentCounterOverride`: `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.ReassignmentCounter]`
* `skipInactive`: `Boolean`

<div id="repair.export_acs" />

### `repair.export_acs`

Export active contracts for the given set of parties to a file.

This command exports the current Active Contract Set (ACS) of a given set of parties to a GZIP compressed ACS snapshot file. Afterwards, the `import_acs` repair command imports it into a participant's ACS again.

The arguments are:

* `parties`: Identifying contracts having at least one stakeholder from the given set.
* `ledgerOffset`: The offset at which the ACS snapshot is exported.
* `exportFilePath`: The path denoting the file where the ACS snapshot will be stored.
* `excludedStakeholders`: When defined, any contract that has one or more of these parties as a stakeholder will be omitted from the ACS snapshot.
* `synchronizerId`: When defined, restricts the export to the given synchronizer.
* `contractSynchronizerRenames`: Changes the associated synchronizer id of contracts from one synchronizer to another based on the mapping.
* `timeout`: A timeout for this operation to complete.

**Arguments**

* `parties`: `Set[com.digitalasset.canton.topology.PartyId]`
* `ledgerOffset`: `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`
* `exportFilePath`: `String`
* `excludedStakeholders`: `Set[com.digitalasset.canton.topology.PartyId]`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `contractSynchronizerRenames`: `Map[com.digitalasset.canton.topology.SynchronizerId,com.digitalasset.canton.topology.SynchronizerId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="repair.export_acs_old" />

### `repair.export_acs_old`

Export active contracts for the given set of parties to a file. (DEPRECATED).

This command exports the current Active Contract Set (ACS) of a given set of parties to ACS snapshot file. Afterwards, the 'import\_acs\_old' command allows importing it into a participant's ACS again. Such ACS export (and import) is interesting for recovery and operational purposes only.

Note that the 'export\_acs\_old' command execution may take a long time to complete and may require significant resources.

DEPRECATION NOTICE: A future release removes this command, use `export_acs` instead.

The arguments are:

* `parties`: identifying contracts having at least one stakeholder from the given set. if empty, contracts of all parties will be exported.
* `partiesOffboarding`: true if the parties will be offboarded (party migration)
* `outputFile`: the output file name where to store the data.
* `filterSynchronizerId`: restrict the export to a given synchronizer
* `timestamp`: optionally a timestamp for which we should take the state (useful to reconcile states of a synchronizer)
* `contractSynchronizerRenames`: As part of the export, allow to rename the associated synchronizer id of contracts from one synchronizer to another based on the mapping.
* `force`: if is set to true, then the check that the timestamp is clean will not be done. For this option to yield a consistent snapshot, you need to wait at least confirmationResponseTimeout + mediatorReactionTimeout after the last submitted request.

**Arguments**

* `parties`: `Set[com.digitalasset.canton.topology.PartyId]`
* `partiesOffboarding`: `Boolean`
* `outputFile`: `String`
* `filterSynchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `timestamp`: `Option[java.time.Instant]`
* `force`: `Boolean`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="repair.help_1" />

### `repair.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="repair.ignore_events" />

### `repair.ignore_events`

Mark sequenced events as ignored.

This is the last resort to ignore events that the participant is unable to process. Ignoring events may lead to subsequent failures, e.g., if the event creating a contract is ignored and that contract is subsequently used. It may also lead to ledger forks if other participants still process the ignored events. It is possible to mark events as ignored that the participant has not yet received.

The command will fail, if marking events between `fromInclusive` and `toInclusive` as ignored would result in a gap in sequencer counters, namely if `from <= to` and `from` is greater than `maxSequencerCounter + 1`, where `maxSequencerCounter` is the greatest sequencer counter of a sequenced event stored by the underlying participant.

The command will also fail, if `force == false` and `from` is smaller than the sequencer counter of the last event that has been marked as clean. (Ignoring such events would normally have no effect, as they have already been processed.)

**Arguments**

* `physicalSynchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`
* `fromInclusive`: `com.digitalasset.canton.SequencerCounter`
* `toInclusive`: `com.digitalasset.canton.SequencerCounter`
* `force`: `Boolean`

<div id="repair.import_acs" />

### `repair.import_acs`

Import active contracts from an Active Contract Set (ACS) snapshot file.

This command imports contracts from an ACS snapshot file into the participant's ACS. It expects the given ACS snapshot file to be the result of a previous `export_acs` command invocation.

The contract IDs of the imported contracts may be checked ahead of starting the process. If any contract ID doesn't match the contract ID scheme associated to the synchronizer where the contract is assigned to, the whole import process fails depending on the value of `contractImportMode`.

By default `contractImportMode` is set to `ContractImportMode.Validation`. If set to `ContractImportMode.Recomputation`, any contract ID that wouldn't pass the check above will be recomputed. Note that the recomputation of contract IDs fails under the following circumstances:

* the contract salt used to compute the contract ID is missing
* the contract ID discriminator version is unknown

Note that only the Canton-specific contract ID suffix will be recomputed. The discriminator cannot be recomputed and will be left as is.

The recomputation will not be performed on contract IDs referenced in the payload of some imported contract but is missing from the import itself (this should mean that the contract was archived, which makes recomputation unnecessary).

Expert only: As validation or recomputation on contract IDs may lengthen the import significantly, you have the option to simply accept the contract IDs as they are using `ContractImportMode.Accept`.

If the import process succeeds, the mapping from the old contract IDs to the new contract IDs will be returned. An empty map means that all contract IDs were valid, or have been accept as they are, and no contract ID was recomputed.

The arguments are:

* `importFilePath`: The path denoting the file from where the ACS snapshot will be read. Defaults to "canton-acs-export.gz" when undefined.
* `workflowIdPrefix`: Sets a custom prefix for the workflow ID to easily identify all transactions generated by this import. Defaults to "import-\<random\_UUID>" when unspecified.
* `contractImportMode`: Governs contract authentication processing on import. Options include Validation (default), \[Accept, Recomputation].
* `representativePackageIdOverride`: Defines override mappings for assigning representative package IDs to contracts upon ACS import.
* `excludedStakeholders`: When defined, any contract that has one or more of these parties as a stakeholder will be omitted from the import.

**Arguments**

* `importFilePath`: `String`
* `workflowIdPrefix`: `String`
* `contractImportMode`: `com.digitalasset.canton.participant.admin.data.ContractImportMode`
* `representativePackageIdOverride`: `com.digitalasset.canton.participant.admin.data.RepresentativePackageIdOverride`
* `excludedStakeholders`: `Set[com.digitalasset.canton.topology.PartyId]`

**Returns:** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.import_acs_old" />

### `repair.import_acs_old`

Import active contracts from an Active Contract Set (ACS) snapshot file. (DEPRECATED).

This command imports contracts from an ACS snapshot file into the participant's ACS. The given ACS snapshot file needs to be the resulting file from a previous 'export\_acs\_old' command invocation.

The contract IDs of the imported contracts will be checked ahead of starting the process. If any contract ID doesn't match the contract ID scheme associated to the synchronizer where the contract is assigned to, the whole import process will fail depending on the value of `allowContractIdSuffixRecomputation`.

By default `allowContractIdSuffixRecomputation` is set to `false`. If set to `true`, any contract ID that wouldn't pass the check above will be recomputed. Note that the recomputation of contract IDs fails under the following circumstances:

* the contract salt used to compute the contract ID is missing
* the contract ID discriminator version is unknown

Note that only the Canton-specific contract ID suffix will be recomputed. The discriminator cannot be recomputed and will be left as is.

The recomputation will not be performed on contract IDs referenced in the payload of some imported contract but is missing from the import itself (this should mean that the contract was archived, which makes recomputation unnecessary).

If the import process succeeds, the mapping from the old contract IDs to the new contract IDs will be returned. An empty map means that all contract IDs were valid and no contract ID was recomputed.

DEPRECATION NOTICE: A future release removes this command, use `export_acs` instead.

**Arguments**

* `inputFile`: `String`
* `workflowIdPrefix`: `String`
* `allowContractIdSuffixRecomputation`: `Boolean`

**Returns:** `Map[com.digitalasset.canton.protocol.LfContractId,com.digitalasset.canton.protocol.LfContractId]`

<div id="repair.migrate_synchronizer" />

### `repair.migrate_synchronizer`

Migrate contracts from one synchronizer to another one.

Migrates all contracts associated with a synchronizer to a new synchronizer. This method will register the new synchronizer, connect to it and then re-associate all contracts from the source synchronizer to the target synchronizer. Please note that this migration needs to be done by all participants at the same time. The target synchronizer should only be used once all participants have finished their migration.

WARNING: The migration does not start in case of in-flight transactions on the source synchronizer. Forcing the migration may lead to a ledger fork! Instead of forcing the migration, ensure the source synchronizer has no in-flight transactions by reconnecting all participants to the source synchronizer, halting activity on these participants and waiting for the in-flight transactions to complete or time out. Forcing a migration is intended for disaster recovery when a source synchronizer cannot be recovered anymore.

The arguments are: source: the synchronizer alias of the source synchronizer target: the configuration for the target synchronizer force: if true, migration is forced ignoring in-flight transactions. Defaults to false.

**Arguments**

* `source`: `com.digitalasset.canton.SynchronizerAlias`
* `target`: `com.digitalasset.canton.participant.synchronizer.SynchronizerConnectionConfig`
* `force`: `Boolean`

<div id="repair.purge" />

### `repair.purge`

Purge contracts with specified Contract IDs from local participant.

This is a last resort command to recover from data corruption, e.g. in scenarios in which participant contracts have somehow gotten out of sync and need to be manually purged, or in situations in which stakeholders are no longer available to agree to their archival. The participant needs to be disconnected from the synchronizer on which the contracts with "contractIds" reside at the time of the call, and as of now the synchronizer cannot have had any inflight requests. The effects of the command will take affect upon reconnecting to the synchronizer. The "ignoreAlreadyPurged" flag makes it possible to invoke the command multiple times with the same parameters in case an earlier command invocation has failed. As repair commands are powerful tools to recover from unforeseen data corruption, but dangerous under normal operation, use of this command requires (temporarily) enabling the "features.enable-repair-commands" configuration. In addition repair commands can run for an unbounded time depending on the number of contract ids passed in. Be sure to not connect the participant to the synchronizer until the call returns.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `contractIds`: `Seq[com.digitalasset.canton.protocol.LfContractId]`
* `ignoreAlreadyPurged`: `Boolean`

<div id="repair.purge_deactivated_synchronizer" />

### `repair.purge_deactivated_synchronizer`

Purge the data of a deactivated synchronizer.

This command deletes synchronizer data and helps to ensure that stale data in the specified, deactivated synchronizer is not acted upon anymore. The specified synchronizer needs to be in the `Inactive` status for purging to occur. Purging a deactivated synchronizer is typically performed automatically as part of a hard synchronizer migration via `repair.migrate_synchronizer`.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`

<div id="repair.rollback_unassignment" />

### `repair.rollback_unassignment`

Rollback an unassignment by re-assigning the contract to the source synchronizer.

This is a last resort command to recover from an unassignment that cannot be completed on the target synchronizer. Arguments:

* reassignmentId
* set of contract ids that should change assignation to the new synchronizer
* source
* the source synchronizer id
* target
* alias of the target synchronizer

**Arguments**

* `reassignmentId`: `String`
* `source`: `com.digitalasset.canton.topology.SynchronizerId`
* `target`: `com.digitalasset.canton.topology.SynchronizerId`

<div id="repair.unignore_events" />

### `repair.unignore_events`

Remove the ignored status from sequenced events.

This command has no effect on ordinary (i.e., not ignored) events and on events that do not exist.

The command will fail, if marking events between `fromInclusive` and `toInclusive` as unignored would result in a gap in sequencer counters, namely if there is one empty ignored event with sequencer counter between `from` and `to` and another empty ignored event with sequencer counter greater than `to`. An empty ignored event is an event that has been marked as ignored and not yet received by the participant.

The command will also fail, if `force == false` and `from` is smaller than the sequencer counter of the last event that has been marked as clean. (Unignoring such events would normally have no effect, as they have already been processed.)

**Arguments**

* `physicalSynchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`
* `fromInclusive`: `com.digitalasset.canton.SequencerCounter`
* `toInclusive`: `com.digitalasset.canton.SequencerCounter`
* `force`: `Boolean`

### Replication

<div id="replication.help" />

### `replication.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="replication.set_passive" />

### `replication.set_passive`

Set the participant replica to passive.

Trigger a graceful fail-over from this active replica to another passive replica. The command completes after the replica had a chance to become active. After this command you need to check the health status of this replica to ensure it is not active anymore.

### Resource Management

<div id="resources.help" />

### `resources.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="resources.resource_limits" />

### `resources.resource_limits`

Get the resource limits of the participant.

**Returns:** `com.digitalasset.canton.participant.admin.ResourceLimits`

<div id="resources.set_resource_limits" />

### `resources.set_resource_limits`

Set resource limits for the participant.

While a resource limit is attained or exceeded, the participant will reject any additional submission with GRPC status ABORTED. Most importantly, a submission will be rejected **before** it consumes a significant amount of resources.

There are three kinds of limits: `maxInflightValidationRequests`,  `maxSubmissionRate` and `maxSubmissionBurstFactor`. The number of inflight validation requests of a participant P covers (1) requests initiated by P as well as (2) requests initiated by participants other than P that need to be validated by P. Compared to the maximum rate, the maximum number of inflight validation requests reflects the load on the participant more accurately. However, the maximum number of inflight validation requests alone does not protect the system from "bursts": If an application submits a huge number of commands at once, the maximum number of inflight validation requests will likely be exceeded, as the system is registering inflight validation requests only during validation and not already during submission.

The maximum rate is a hard limit on the rate of commands submitted to this participant through the Ledger API. As the rate of commands is checked and updated immediately after receiving a new command submission, an application cannot exceed the maximum rate.

The `maxSubmissionBurstFactor` parameter (positive, default 0.5) allows to configure how permissive the rate limitation should be with respect to bursts. The rate limiting will be enforced strictly after having observed `max_burst` \* `max_submission_rate` commands.

For the sake of illustration, let's assume the configured rate limit is `100 commands/s` with a burst ratio of 0.5. If an application submits 100 commands within a single second, waiting exactly 10 milliseconds between consecutive commands, then the participant will accept all commands. With a `maxSubmissionBurstFactor` of 0.5, the participant will accept the first 50 commands and reject the remaining 50. If the application then waits another 500 ms, it may submit another burst of 50 commands. If it waits 250 ms, it may submit only a burst of 25 commands.

Resource limits can only be changed, if the server runs Canton enterprise. In the community edition, the server uses fixed limits that cannot be changed.

**Arguments**

* `limits`: `com.digitalasset.canton.participant.admin.ResourceLimits`

### Testing

<div id="testing.acs_search" />

### `testing.acs_search`

Lookup of active contracts.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `exactId`: `String`
* `filterPackage`: `String`
* `filterTemplate`: `String`
* `filterStakeholder`: `Option[com.digitalasset.canton.topology.PartyId]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `List[com.digitalasset.canton.protocol.ContractInstance]`

<div id="testing.await_synchronizer_time" />

### `testing.await_synchronizer_time`

Await for the given time to be reached on the given synchronizer.

**Arguments**

* `synchronizer`: `com.digitalasset.canton.topology.Synchronizer`
* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.await_synchronizer_time_1" />

### `testing.await_synchronizer_time_1`

Await for the given time to be reached on the given synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.bong" />

### `testing.bong`

Send a bong to a set of target parties over the ledger. Levels > 0 leads to an exploding ping with exponential number of contracts. Throw a RuntimeException in case of failure.

Initiates a racy ping to multiple participants, measuring the roundtrip time of the fastest responder, with an optional timeout. Grace-period is the time the bong will wait for a duplicate spent (which would indicate an error in the system) before exiting. If levels > 0, the ping command will lead to a binary explosion and subsequent dilation of contracts, where `level` determines the number of levels we will explode. As a result, the system will create (2^(L+2) - 3) contracts (where L stands for `level`). Normally, only the initiator is a validator. Additional validators can be added using the validators argument. The bong command comes handy to run a burst test against the system and quickly leads to an overloading state.

**Arguments**

* `targets`: `Set[com.digitalasset.canton.topology.ParticipantId]`
* `validators`: `Set[com.digitalasset.canton.topology.ParticipantId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `levels`: `Int`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `id`: `String`

**Returns:** `scala.concurrent.duration.Duration`

<div id="testing.crypto_api" />

### `testing.crypto_api`

Return the sync crypto api provider, which provides access to all cryptographic methods.

**Returns:** `com.digitalasset.canton.crypto.SyncCryptoApiParticipantProvider`

<div id="testing.fetch_synchronizer_time" />

### `testing.fetch_synchronizer_time`

Fetch the current time from the given synchronizer.

**Arguments**

* `synchronizer`: `com.digitalasset.canton.topology.Synchronizer`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.fetch_synchronizer_time_1" />

### `testing.fetch_synchronizer_time_1`

Fetch the current time from the given synchronizer.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.fetch_synchronizer_times" />

### `testing.fetch_synchronizer_times`

Fetch the current time from all connected synchronizers.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.find_clean_commitments_timestamp" />

### `testing.find_clean_commitments_timestamp`

The latest timestamp before or at the given one for which no commitment is outstanding.

The latest timestamp before or at the given one for which no commitment is outstanding. Note that this doesn't imply that pruning is possible at this timestamp, as the system might require some additional data for crash recovery. Thus, this is useful for testing commitments; use the commands in the pruning group for pruning. Additionally, the result needn't fall on a "commitment tick" as specified by the reconciliation interval.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `beforeOrAt`: `com.digitalasset.canton.data.CantonTimestamp`

**Returns:** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="testing.help" />

### `testing.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="testing.lookup_transaction" />

### `testing.lookup_transaction`

Lookup of accepted transactions by update ID.

**Arguments**

* `updateId`: `String`

**Returns:** `Option[com.digitalasset.canton.protocol.LfVersionedTransaction]`

<div id="testing.maybe_bong" />

### `testing.maybe_bong`

Like bong, but returns None in case of failure.

**Arguments**

* `targets`: `Set[com.digitalasset.canton.topology.ParticipantId]`
* `validators`: `Set[com.digitalasset.canton.topology.ParticipantId]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `levels`: `Int`
* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `workflowId`: `String`
* `id`: `String`

**Returns:** `Option[scala.concurrent.duration.Duration]`

<div id="testing.pcs_search" />

### `testing.pcs_search`

Lookup contracts in the Private Contract Store.

Get raw access to the PCS of the given synchronizer sync controller. The filter commands will check if the target value `contains` the given string. The arguments can be started with `^` such that `startsWith` is used for comparison or `!` to use `equals`. The `activeSet` argument allows to restrict the search to the active contract set. For contract ID filtration only exact match is supported.

**Arguments**

* `synchronizerAlias`: `com.digitalasset.canton.SynchronizerAlias`
* `exactId`: `String`
* `filterPackage`: `String`
* `filterTemplate`: `String`
* `activeSet`: `Boolean`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `List[(Boolean, com.digitalasset.canton.protocol.ContractInstance)]`

<div id="testing.sequencer_messages" />

### `testing.sequencer_messages`

Retrieve all sequencer messages.

Optionally allows filtering for sequencer from a certain time span (inclusive on both ends) and limiting the number of displayed messages. The returned messages will be ordered on most synchronizer ledger implementations if a time span is given.

Fails if the participant has never connected to the synchronizer.

**Arguments**

* `physicalSynchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`
* `from`: `Option[java.time.Instant]`
* `to`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `warnOnDiscardedEnvelopes`: `Boolean`

**Returns:** `Seq[com.digitalasset.canton.sequencing.PossiblyIgnoredProtocolEvent]`

<div id="testing.state_inspection" />

### `testing.state_inspection`

Obtain access to the state inspection interface. Use at your own risk.

The state inspection methods can fatally and permanently corrupt the state of a participant. The API is subject to change in any way.

**Returns:** `com.digitalasset.canton.participant.admin.inspection.SyncStateInspection`

### Topology Administration

The topology commands can be used to manipulate and inspect the topology state. In all commands, we use fingerprints to refer to public keys. Internally, these fingerprints are resolved using the key registry (which is a map of Fingerprint -> PublicKey). Any key can be added to the key registry using the `keys.public.load` commands.

<div id="topology.help" />

### `topology.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.init_id" />

### `topology.init_id`

Initialize the node with a unique identifier.

Every node in Canton is identified using a unique identifier, which is composed of a user-chosen string and the fingerprint of a signing key. The signing key is the root key defining a so-called namespace, where the signing key has the ultimate control over issuing new identifiers. During initialisation, we have to pick such a unique identifier. By default, initialisation happens automatically, but it can be changed to either initialize manually or to read a set of identities and certificates from a file.

Automatic node initialisation is usually turned off to preserve the identity of a participant or synchronizer node (during major version upgrades) or if the root namespace key of the node is kept offline.

If known, the namespace can be set to verify that it matches the root certificate. Otherwise it will be read from the delegation.

Optionally, a set of delegations can be provided if the root namespace key is not available. These delegations can be either in files or passed as objects. Their version needs to match the necessary protocol version of the synchronizers we are going to connect to.

**Arguments**

* `identifier`: `String`
* `namespace`: `String`
* `delegations`: `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction]`
* `delegationFiles`: `Seq[String]`
* `waitForReady`: `Boolean`

<div id="topology.init_id_from_uid" />

### `topology.init_id_from_uid`

Initialize the node with a unique identifier.

Every node in Canton is identified using a unique identifier, which is composed of a user-chosen string and the fingerprint of a signing key. The signing key is the root key defining a so-called namespace, where the signing key has the ultimate control over issuing new identifiers. During initialisation, we have to pick such a unique identifier. By default, initialisation happens automatically, but it can be changed to either initialize manually or to read a set of identities and delegations from a file.

Automatic node initialisation is usually turned off to preserve the identity of a participant or synchronizer node (during major version upgrades) or if the root namespace key of the node is kept offline.

Optionally, a set of delegations can be provided if the root namespace key is not available. These delegations can be either in files or passed as objects. Their version needs to match the necessary protocol version of the synchronizers we are going to connect to.

**Arguments**

* `identifier`: `com.digitalasset.canton.topology.UniqueIdentifier`
* `delegations`: `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction.GenericSignedTopologyTransaction]`
* `delegationFiles`: `Seq[String]`
* `waitForReady`: `Boolean`

<div id="topology.transactions.authorize" />

### `topology.transactions.authorize`

Authorize a transaction by its hash.

**Arguments**

* `txHash`: `com.digitalasset.canton.topology.transaction.TopologyTransaction.TxHash`
* `mustBeFullyAuthorized`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,M]`

<div id="topology.transactions.authorize_1" />

### `topology.transactions.authorize_1`

Authorize a transaction by its hash.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `txHash`: `com.digitalasset.canton.topology.transaction.TopologyTransaction.TxHash`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.TopologyMapping]`

<div id="topology.transactions.export_identity_transactions" />

### `topology.transactions.export_identity_transactions`

Serializes node's topology identity transactions to a file.

Transactions serialized this way should be loaded into another node with load\_from\_file

**Arguments**

* `file`: `String`

<div id="topology.transactions.export_identity_transactionsv2" />

### `topology.transactions.export_identity_transactionsv2`

Serializes node's topology identity transactions to a file.

Transactions serialized this way should be loaded into another node with load\_from\_file

**Arguments**

* `file`: `String`

<div id="topology.transactions.export_topology_snapshot" />

### `topology.transactions.export_topology_snapshot`

Export topology snapshot.

This command export the node's topology transactions as byte string.

The arguments are: excludeMappings: a list of topology mapping codes to exclude from the export. If not provided, all mappings are included. filterNamespace: the namespace to filter the transactions by. protocolVersion: the protocol version used to serialize the topology transactions. If not provided, the latest protocol version is used.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="topology.transactions.export_topology_snapshotv2" />

### `topology.transactions.export_topology_snapshotv2`

Export topology snapshot.

This command export the node's topology transactions as byte string.

The arguments are: excludeMappings: a list of topology mapping codes to exclude from the export. If not provided, all mappings are included. filterNamespace: the namespace to filter the transactions by. protocolVersion: the protocol version used to serialize the topology transactions. If not provided, the latest protocol version is used.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="topology.transactions.find_latest_by_mapping" />

### `topology.transactions.find_latest_by_mapping`

Find the latest transaction for a given mapping hash.

store:

* "Authorized": the topology transaction will be looked up in the node's authorized store.
* `"<synchronizer id>"`: the topology transaction will be looked up in the specified synchronizer store. includeProposals: when true, the result could be the latest proposal, otherwise will only return the latest fully authorized transaction

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `includeProposals`: `Boolean`

**Returns:** `Option[com.digitalasset.canton.topology.store.StoredTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,M]]`

<div id="topology.transactions.find_latest_by_mapping_hash" />

### `topology.transactions.find_latest_by_mapping_hash`

Find the latest transaction for a given mapping hash.

mappingHash: the unique key of the topology mapping to find store:

* "Authorized": the topology transaction will be looked up in the node's authorized store.
* `"<synchronizer id>"`: the topology transaction will be looked up in the specified synchronizer store. includeProposals: when true, the result could be the latest proposal, otherwise will only return the latest fully authorized transaction

**Arguments**

* `mappingHash`: `com.digitalasset.canton.topology.transaction.TopologyMapping.MappingHash`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `includeProposals`: `Boolean`

**Returns:** `Option[com.digitalasset.canton.topology.store.StoredTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,M]]`

<div id="topology.transactions.genesis_state" />

### `topology.transactions.genesis_state`

Download the genesis state for a sequencer. This method should be used when performing a major synchronizer upgrade.

Download the topology snapshot which includes the entire history of topology transactions to initialize a sequencer for a major synchronizer upgrade. The validFrom and validUntil are set to SignedTopologyTransaction.InitialTopologySequencingTime. filterSynchronizerStore: Must be specified if the genesis state is requested from a participant node. timestamp: If not specified, the max effective time of the latest topology transaction is used. Otherwise, the given timestamp is used.

**Arguments**

* `filterSynchronizerStore`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Synchronizer]`
* `timestamp`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="topology.transactions.genesis_statev2" />

### `topology.transactions.genesis_statev2`

Download the genesis state for a sequencer. This method should be used when performing a major synchronizer upgrade.

Download the topology snapshot which includes the entire history of topology transactions to initialize a sequencer for a major synchronizer upgrades. The validFrom and validUntil are set to SignedTopologyTransaction.InitialTopologySequencingTime. filterSynchronizerStore: Must be specified if the genesis state is requested from a participant node. timestamp: If not specified, the max effective time of the latest topology transaction is used. Otherwise, the given timestamp is used.

**Arguments**

* `filterSynchronizerStore`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Synchronizer]`
* `timestamp`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="topology.transactions.identity_transactions" />

### `topology.transactions.identity_transactions`

Downloads the node's topology identity transactions.

The node's identity is defined by topology transactions of type NamespaceDelegation and OwnerToKeyMapping.

**Returns:** `Seq[com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.TopologyMapping]]`

<div id="topology.transactions.import_topology_snapshot_from" />

### `topology.transactions.import_topology_snapshot_from`

Loads topology transactions from a file into the specified topology store.

The file must contain data serialized by TopologyTransactions.

**Arguments**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

<div id="topology.transactions.import_topology_snapshot_fromv2" />

### `topology.transactions.import_topology_snapshot_fromv2`

Loads topology transactions from a file into the specified topology store.

The file must contain data serialized by TopologyTransactions.

**Arguments**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`

<div id="topology.transactions.list" />

### `topology.transactions.list`

List all transaction.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `excludeMappings`: `Seq[com.digitalasset.canton.topology.transaction.TopologyMapping.Code]`
* `filterAuthorizedKey`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `protocolVersion`: `Option[String]`
* `filterNamespace`: `String`

**Returns:** `com.digitalasset.canton.topology.store.StoredTopologyTransactions[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.TopologyMapping]`

<div id="topology.transactions.load_multiple_from_file" />

### `topology.transactions.load_multiple_from_file`

Loads topology transactions from a file into the specified topology store.

The file must contain data serialized by SignedTopologyTransactions.

**Arguments**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.load_single_from_file" />

### `topology.transactions.load_single_from_file`

Loads topology transactions from a file into the specified topology store.

The file must contain data serialized by SignedTopologyTransaction.

**Arguments**

* `file`: `String`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.load_single_from_files" />

### `topology.transactions.load_single_from_files`

Loads topology transactions from a list of files into the specified topology store.

The files must contain data serialized by SignedTopologyTransaction.

**Arguments**

* `files`: `Seq[String]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.transactions.logical_upgrade_state" />

### `topology.transactions.logical_upgrade_state`

Download the upgrade state for a sequencer. This method should be used when performing a logical synchronizer upgrade.

Download the topology snapshot which includes the entire history of topology transactions to initialize a sequencer for a logical synchronizer upgrade. A logical synchronizer upgrade must be ongoing for this call to succeed.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="topology.transactions.propose" />

### `topology.transactions.propose`

Propose a transaction.

Raw access to admin API command

**Arguments**

* `mapping`: `M`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`
* `mustFullyAuthorize`: `Boolean`
* `forceChanges`: `com.digitalasset.canton.topology.ForceFlags`
* `waitToBecomeEffective`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,M]`

<div id="topology.decentralized_namespaces.help" />

### `topology.decentralized_namespaces.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.decentralized_namespaces.propose" />

### `topology.decentralized_namespaces.propose`

Propose changes to a decentralized namespace.

decentralizedNamespace: the DecentralizedNamespaceDefinition to propose

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `decentralizedNamespace`: `com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition]`

<div id="topology.decentralized_namespaces.propose_new" />

### `topology.decentralized_namespaces.propose_new`

Propose the creation of a new decentralized namespace.

owners: the namespaces of the founding members of the decentralized namespace, which are used to compute the name of the decentralized namespace. threshold: this threshold specifies the minimum number of signatures of decentralized namespace members that are required to satisfy authorization requirements on topology transactions for the namespace of the decentralized namespace.

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `owners`: `Set[com.digitalasset.canton.topology.Namespace]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.DecentralizedNamespaceDefinition]`

<div id="topology.synchronizer_parameters.get_dynamic_synchronizer_parameters" />

### `topology.synchronizer_parameters.get_dynamic_synchronizer_parameters`

Get the configured dynamic synchronizer parameters.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`

**Returns:** `com.digitalasset.canton.admin.api.client.data.DynamicSynchronizerParameters`

<div id="topology.synchronizer_parameters.help" />

### `topology.synchronizer_parameters.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.synchronizer_parameters.latest" />

### `topology.synchronizer_parameters.latest`

Latest dynamic synchronizer parameters.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `filterSynchronizer`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `com.digitalasset.canton.admin.api.client.data.DynamicSynchronizerParameters`

<div id="topology.synchronizer_parameters.list" />

### `topology.synchronizer_parameters.list`

List dynamic synchronizer parameters.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterSynchronizer`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListSynchronizerParametersStateResult]`

<div id="topology.synchronizer_parameters.propose" />

### `topology.synchronizer_parameters.propose`

Propose changes to dynamic synchronizer parameters.

synchronizerId: the target synchronizer parameters: the new dynamic synchronizer parameters to be used on the synchronizer

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node waitForParticipants: if synchronize is defined, the command will also wait until parameters have been propagated to the listed participants force: must be set to true when performing a dangerous operation, such as increasing the preparationTimeRecordTimeTolerance

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `parameters`: `com.digitalasset.canton.admin.api.client.data.DynamicSynchronizerParameters`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `force`: `com.digitalasset.canton.topology.ForceFlags`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.SynchronizerParametersState]`

<div id="topology.synchronizer_parameters.propose_update" />

### `topology.synchronizer_parameters.propose_update`

Propose an update to dynamic synchronizer parameters.

synchronizerId: the target synchronizer update: the new dynamic synchronizer parameters to be used on the synchronizer mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node waitForParticipants: if synchronize is defined, the command will also wait until the update has been propagated to the listed participants force: must be set to true when performing a dangerous operation, such as increasing the preparationTimeRecordTimeTolerance

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `update`: `[com.digitalasset.canton.admin.api.client.data.DynamicSynchronizerParameters => com.digitalasset.canton.admin.api.client.data.DynamicSynchronizerParameters](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/admin/api/client/data/DynamicSynchronizerParameters.html)`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `force`: `com.digitalasset.canton.topology.ForceFlags`

<div id="topology.synchronizer_parameters.set_ledger_time_record_time_tolerance" />

### `topology.synchronizer_parameters.set_ledger_time_record_time_tolerance`

Update the ledger time record time tolerance in the dynamic synchronizer parameters.

synchronizerId: the target synchronizer newLedgerTimeRecordTimeTolerance: the new ledgerTimeRecordTimeTolerance value to apply to the synchronizer

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `newLedgerTimeRecordTimeTolerance`: `com.digitalasset.canton.config.NonNegativeFiniteDuration`

<div id="topology.synchronizer_parameters.set_preparation_time_record_time_tolerance" />

### `topology.synchronizer_parameters.set_preparation_time_record_time_tolerance`

Update the preparation time record time tolerance in the dynamic synchronizer parameters.

If it would be insecure to perform the change immediately, the command will block and wait until it is secure to perform the change. The command will block for at most twice of `newPreparationTimeRecordTimeTolerance`.

The method will fail if `mediatorDeduplicationTimeout` is less than twice of `newPreparationTimeRecordTimeTolerance`.

Do not modify synchronizer parameters concurrently while running this command, because the command may override concurrent changes.

force: update `newPreparationTimeRecordTimeTolerance` immediately without blocking. This is safe to do during synchronizer bootstrapping and in test environments, but should not be done in operational production systems.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `newPreparationTimeRecordTimeTolerance`: `com.digitalasset.canton.config.NonNegativeFiniteDuration`
* `force`: `Boolean`

<div id="topology.synchronizer_trust_certificates.help" />

### `topology.synchronizer_trust_certificates.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.synchronizer_trust_certificates.propose" />

### `topology.synchronizer_trust_certificates.propose`

Propose a change to a participant's synchronizer trust certificate.

A participant's synchronizer trust certificate signals to the synchronizer that the participant would like to act on the synchronizer.

participantId: the identifier of the trust certificate's target participant synchronizerId: the identifier of the synchronizer on which the participant would like to act

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`
* `featureFlags`: `Seq[com.digitalasset.canton.topology.transaction.SynchronizerTrustCertificate.ParticipantTopologyFeatureFlag]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.SynchronizerTrustCertificate]`

<div id="topology.mediators.help" />

### `topology.mediators.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.mediators.list" />

### `topology.mediators.list`

List mediator synchronizer topology state.

synchronizerId: the optional target synchronizer proposals: if true then proposals are shown, otherwise actual validated state

**Arguments**

* `synchronizerId`: `Option[com.digitalasset.canton.topology.SynchronizerId]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterSynchronizer`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`
* `group`: `Option[com.digitalasset.canton.config.RequireTypes.NonNegativeInt]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMediatorSynchronizerStateResult]`

<div id="topology.mediators.propose" />

### `topology.mediators.propose`

Replace the mediator topology.

synchronizerId: the target synchronizer threshold: the minimum number of mediators that need to come to a consensus for a message to be sent to other members. active: the list of mediators that will take part in the mediator consensus in this mediator group passive: the mediators that will receive all messages but will not participate in mediator consensus group: the mediator group identifier store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `active`: `Seq[com.digitalasset.canton.topology.MediatorId]`
* `observers`: `Seq[com.digitalasset.canton.topology.MediatorId]`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.MediatorSynchronizerState]`

<div id="topology.mediators.propose_delta" />

### `topology.mediators.propose_delta`

Propose changes to the mediator topology.

synchronizerId: the target synchronizer group: the mediator group identifier adds: The unique identifiers of the active mediators to add. removes: The unique identifiers of the mediators that should no longer be active mediators. observerAdds: The unique identifiers of the observer mediators to add. observerRemoves: The unique identifiers of the mediators that should no longer be observer mediators. updateThreshold: Optionally an updated value for the threshold of the mediator group. await: optional timeout to wait for the proposal to be persisted in the specified topology store mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `adds`: `List[com.digitalasset.canton.topology.MediatorId]`
* `removes`: `List[com.digitalasset.canton.topology.MediatorId]`
* `observerAdds`: `List[com.digitalasset.canton.topology.MediatorId]`
* `observerRemoves`: `List[com.digitalasset.canton.topology.MediatorId]`
* `updateThreshold`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`

<div id="topology.mediators.remove_group" />

### `topology.mediators.remove_group`

Propose to remove a mediator group.

synchronizerId: the target synchronizer group: the mediator group identifier

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `group`: `com.digitalasset.canton.config.RequireTypes.NonNegativeInt`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.MediatorSynchronizerState]`

<div id="topology.namespace_delegations.help" />

### `topology.namespace_delegations.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.namespace_delegations.propose_delegation" />

### `topology.namespace_delegations.propose_delegation`

Propose a new namespace delegation that is restricted to certain topology mapping types.

A namespace delegation allows the owner of a namespace to delegate signing privileges for topology transactions on behalf of said namespace to additional signing keys.

namespace: the namespace for which the target key can be used to sign topology transactions targetKey: the target key to be used for signing topology transactions on behalf of the namespace delegationRestriction: the types of topology mappings for which targetKey can sign. Can be one of the following values:

* `CanSignAllMappings`: the target key can sign all topology mappings that are currently known or will be added in future releases.
* `CanSignAllButNamespaceDelegations`: the target key can sign all topology mappings that are currently known or will be added in future releases, except for namespace delegations.
* CanSignSpecificMappings(TopologyMapping.Code\*): the target key can only sign the specified topology mappings.

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. If this is not the case, the request fails. When set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `targetKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `delegationRestriction`: `com.digitalasset.canton.topology.transaction.DelegationRestriction`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.NamespaceDelegation]`

<div id="topology.namespace_delegations.propose_revocation" />

### `topology.namespace_delegations.propose_revocation`

Revoke an existing namespace delegation.

A namespace delegation allows the owner of a namespace to delegate signing privileges for topology transactions on behalf of said namespace to additional signing keys.

namespace: the namespace for which the target key should be revoked targetKey: the target key to be revoked

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. If this is not the case, the request fails. When set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. force: must be set to true when performing a dangerous operation, such as revoking a root certificate

**Arguments**

* `namespace`: `com.digitalasset.canton.topology.Namespace`
* `targetKey`: `com.digitalasset.canton.crypto.SigningPublicKey`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `forceChanges`: `com.digitalasset.canton.topology.ForceFlags`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.NamespaceDelegation]`

<div id="topology.owner_to_key_mappings.add_key" />

### `topology.owner_to_key_mappings.add_key`

Add a key to an owner to key mapping.

Add a key to an owner to key mapping. A key owner is anyone in the system that needs a key-pair known to all members (participants, mediators, sequencers) of a synchronizer. If no owner to key mapping exists for the specified key owner, create a new mapping with the specified key. The specified key needs to have been created previously via the `keys.secret` api.

key: Fingerprint of the key purpose: The key purpose, i.e. whether the key is for signing or encryption keyOwner: The member that owns the key signedBy: Optional fingerprint of the authorizing key which in turn refers to a specific, locally existing certificate. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node mustFullyAuthorize: Whether to only add the key if the member is in the position to authorize the change.

**Arguments**

* `key`: `com.digitalasset.canton.crypto.Fingerprint`
* `purpose`: `com.digitalasset.canton.crypto.KeyPurpose`
* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

<div id="topology.owner_to_key_mappings.add_keys" />

### `topology.owner_to_key_mappings.add_keys`

Add a set of keys to an owner to key mapping.

Add a set of keys to an owner to key mapping. A key owner is anyone in the system that needs a key-pair known to all members (participants, mediators, sequencers) of a synchronizer. If no owner to key mapping exists for the specified key owner, create a new mapping with the specified keys. The specified keys needs to have been created previously via the `keys.secret` api.

keys: Fingerprint and key purpose of the keys keyOwner: The member that owns the key signedBy: Optional fingerprint of the authorizing key which in turn refers to a specific, locally existing certificate. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node mustFullyAuthorize: Whether to only add the key if the member is in the position to authorize the change.

**Arguments**

* `keys`: `Seq[(com.digitalasset.canton.crypto.Fingerprint, com.digitalasset.canton.crypto.KeyPurpose)]`
* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`

<div id="topology.owner_to_key_mappings.help" />

### `topology.owner_to_key_mappings.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.owner_to_key_mappings.list" />

### `topology.owner_to_key_mappings.list`

List owner to key mapping transactions.

**Arguments**

* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.topology.MemberCode]`
* `filterKeyOwnerUid`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListOwnerToKeyMappingResult]`

<div id="topology.owner_to_key_mappings.remove_key" />

### `topology.owner_to_key_mappings.remove_key`

Remove a key from an owner to key mapping.

Remove a key from an owner to key mapping. A key owner is anyone in the system that needs a key-pair known to all members (participants, mediators, sequencers) of a synchronizer. If the specified key is the last key in the owner to key mapping (which requires the force to be true), the owner to key mapping will be removed. The specified key needs to have been created previously via the `keys.secret` api.

key: Fingerprint of the key purpose: The key purpose, i.e. whether the key is for signing or encryption keyOwner: The member that owns the key signedBy: Optional fingerprint of the authorizing key which in turn refers to a specific, locally existing certificate. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node mustFullyAuthorize: Whether to only add the key if the member is in the position to authorize the change. force: removing the last key is dangerous and must therefore be manually forced

**Arguments**

* `key`: `com.digitalasset.canton.crypto.Fingerprint`
* `purpose`: `com.digitalasset.canton.crypto.KeyPurpose`
* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `force`: `com.digitalasset.canton.topology.ForceFlags`

<div id="topology.owner_to_key_mappings.rotate_key" />

### `topology.owner_to_key_mappings.rotate_key`

Rotate the key for an owner to key mapping.

Rotates an existing key of the owner's owner to key mapping by adding the new key and removing the previous key.

nodeInstance: The node instance that is used to verify that both the current and new key pertain to this node. This avoids conflicts when there are different nodes with the same uuid (i.e., multiple sequencers). owner: The member that owns the owner to key mapping currentKey: The current public key that will be rotated newKey: The new public key that has been generated

**Arguments**

* `member`: `com.digitalasset.canton.topology.Member`
* `currentKey`: `com.digitalasset.canton.crypto.PublicKey`
* `newKey`: `com.digitalasset.canton.crypto.PublicKey`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

<div id="topology.participant_synchronizer_permissions.find" />

### `topology.participant_synchronizer_permissions.find`

Looks up the participant permission for a participant on a synchronizer.

Returns the optional participant synchronizer permission.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`

**Returns:** `Option[com.digitalasset.canton.admin.api.client.data.topology.ListParticipantSynchronizerPermissionResult]`

<div id="topology.participant_synchronizer_permissions.help" />

### `topology.participant_synchronizer_permissions.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.participant_synchronizer_permissions.propose" />

### `topology.participant_synchronizer_permissions.propose`

Propose changes to the synchronizer permissions of participants.

Synchronizer operators may use this command to change a participant's permissions on a synchronizer.

synchronizerId: the target synchronizer participantId: the participant whose permissions should be changed permission: the participant's permission loginAfter: the earliest time a participant may connect to the synchronizer limits: synchronizer limits for this participant

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `permission`: `com.digitalasset.canton.topology.transaction.ParticipantPermission`
* `loginAfter`: `Option[com.digitalasset.canton.data.CantonTimestamp]`
* `limits`: `Option[com.digitalasset.canton.topology.transaction.ParticipantSynchronizerLimits]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `change`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.ParticipantSynchronizerPermission]`

<div id="topology.participant_synchronizer_permissions.revoke" />

### `topology.participant_synchronizer_permissions.revoke`

Revokes the synchronizer permissions of a participant.

Synchronizer operators may use this command to revoke a participant's permissions on a synchronizer.

synchronizerId: the target synchronizer participantId: the participant whose permissions should be revoked

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.ParticipantSynchronizerPermission]`

<div id="topology.participant_synchronizer_states.active" />

### `topology.participant_synchronizer_states.active`

Returns true if the given participant is currently active on the given synchronizer.

Active means that the participant has been granted at least observation rights on the synchronizer and that the participant has registered a synchronizer trust certificate

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`

**Returns:** `Boolean`

<div id="topology.participant_synchronizer_states.help" />

### `topology.participant_synchronizer_states.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.party_hosting_limits.help" />

### `topology.party_hosting_limits.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.party_to_key_mappings.help" />

### `topology.party_to_key_mappings.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.party_to_key_mappings.list" />

### `topology.party_to_key_mappings.list`

List party to key mapping transactions.

**Arguments**

* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterParty`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToKeyMappingResult]`

<div id="topology.party_to_key_mappings.propose" />

### `topology.party_to_key_mappings.propose`

Propose a party to key mapping.

**Arguments**

* `partyId`: `com.digitalasset.canton.topology.PartyId`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `signingKeys`: `com.daml.nonempty.NonEmpty[Seq[com.digitalasset.canton.crypto.SigningPublicKey]]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `ops`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `force`: `com.digitalasset.canton.topology.ForceFlags`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.PartyToKeyMapping]`

<div id="topology.party_to_participant_mappings.help" />

### `topology.party_to_participant_mappings.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.party_to_participant_mappings.list" />

### `topology.party_to_participant_mappings.list`

List party to participant mapping transactions from synchronizer store.

List the party to participant mapping transactions present in the stores. Party to participant mappings are topology transactions used to allocate a party to certain participants. The same party can be allocated on several participants with different privileges.

synchronizerId: Synchronizer to be considered proposals: Whether to query proposals instead of authorized transactions. timeQuery: The time query allows to customize the query by time. The following options are supported: TimeQuery.HeadState (default): The most recent known state. TimeQuery.Snapshot(ts): The state at a certain point in time. TimeQuery.Range(fromO, toO): Time-range of when the transaction was added to the store operation: Optionally, what type of operation the transaction should have. filterParty: Filter for parties starting with the given filter string. filterParticipant: If non-empty, returns only parties that are hosted on this participant. filterSigningKey: Filter for transactions that are authorized with a key that starts with the given filter string. protocolVersion: Export the topology transactions in the optional protocol version.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Synchronizer`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterParty`: `String`
* `filterParticipant`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult]`

<div id="topology.party_to_participant_mappings.list_from_all" />

### `topology.party_to_participant_mappings.list_from_all`

List party to participant mapping transactions from all stores.

List the party to participant mapping transactions present in the stores. Party to participant mappings are topology transactions used to allocate a party to certain participants. The same party can be allocated on several participants with different privileges.

proposals: Whether to query proposals instead of authorized transactions. timeQuery: The time query allows to customize the query by time. The following options are supported: TimeQuery.HeadState (default): The most recent known state. TimeQuery.Snapshot(ts): The state at a certain point in time. TimeQuery.Range(fromO, toO): Time-range of when the transaction was added to the store operation: Optionally, what type of operation the transaction should have. filterParty: Filter for parties starting with the given filter string. filterParticipant: Filter for participants starting with the given filter string. filterSigningKey: Filter for transactions that are authorized with a key that starts with the given filter string. protocolVersion: Export the topology transactions in the optional protocol version.

**Arguments**

* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterParty`: `String`
* `filterParticipant`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult]`

<div id="topology.party_to_participant_mappings.list_from_authorized" />

### `topology.party_to_participant_mappings.list_from_authorized`

List party to participant mapping transactions from the authorized store.

List the party to participant mapping transactions present in the stores. Party to participant mappings are topology transactions used to allocate a party to certain participants. The same party can be allocated on several participants with different privileges.

proposals: Whether to query proposals instead of authorized transactions. timeQuery: The time query allows to customize the query by time. The following options are supported: TimeQuery.HeadState (default): The most recent known state. TimeQuery.Snapshot(ts): The state at a certain point in time. TimeQuery.Range(fromO, toO): Time-range of when the transaction was added to the store operation: Optionally, what type of operation the transaction should have. filterParty: Filter for parties starting with the given filter string. filterParticipant: Filter for participants starting with the given filter string. filterSigningKey: Filter for transactions that are authorized with a key that starts with the given filter string. protocolVersion: Export the topology transactions in the optional protocol version.

**Arguments**

* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterParty`: `String`
* `filterParticipant`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListPartyToParticipantResult]`

<div id="topology.party_to_participant_mappings.list_hosting_proposals" />

### `topology.party_to_participant_mappings.list_hosting_proposals`

List multi-hosted party proposals.

Multi-hosted parties require all involved actors to sign the topology transaction. Topology transactions without sufficient signatures are called proposals. They are distributed the same way as fully authorized topology transactions, and signatures are aggregated until the transaction is fully authorized. This method here allows to inspect the pending queue of open hosting proposals. The proposals are returned as seen on the specified synchronizer. They can be approved by the individual participants by invoking node.topology.transactions.authorize(\<synchronizer-id>, \<tx-hash>).

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `participantId`: `com.digitalasset.canton.topology.ParticipantId`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListMultiHostingProposal]`

<div id="topology.party_to_participant_mappings.propose" />

### `topology.party_to_participant_mappings.propose`

Replace party to participant mapping.

Replace the association of a party to hosting participants. party: The unique identifier of the party whose set of participant permissions to modify. newParticipants: The unique identifier of the participants to host the party. Each participant entry specifies the participant's permissions (submission, confirmation, observation). participantsRequiringPartyToBeOnboarded: The participants that need to onboard the party independently from this call before the participants fully host the party. threshold: The threshold is `1` for regular parties and larger than `1` for "consortium parties". The threshold indicates how many participant confirmations are needed in order to confirm a Daml transaction on behalf the party. partySigningKeys: Party signing keys with threshold. If specified, the keys will be taken from this field. Otherwise, they have to be specified earlier in PartyToKey mappings. signedBy: Refers to the optional fingerprint of the authorizing key which in turn refers to a specific, locally existing certificate. serial: The expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. operation: The operation to use. When adding a mapping or making changes, use TopologyChangeOp.Replace. When removing a mapping, use TopologyChangeOp.Remove and pass the same values as the currently effective mapping. The default value is TopologyChangeOp.Replace. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node mustFullyAuthorize: When set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. If this is not the case, the request fails. When set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. store:

* "Authorized": The topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: The topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `newParticipants`: `Seq[(com.digitalasset.canton.topology.ParticipantId, com.digitalasset.canton.topology.transaction.ParticipantPermission)]`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `partySigningKeys`: `Option[com.digitalasset.canton.crypto.SigningKeysWithThreshold]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Seq[com.digitalasset.canton.crypto.Fingerprint]`
* `operation`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `participantsRequiringPartyToBeOnboarded`: `Seq[com.digitalasset.canton.topology.ParticipantId]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.PartyToParticipant]`

<div id="topology.party_to_participant_mappings.propose_delta" />

### `topology.party_to_participant_mappings.propose_delta`

Change party to participant mapping.

Change the association of a party to hosting participants. party: The unique identifier of the party whose set of participants or permission to modify. adds: The unique identifiers of the participants to host the party each specifying the participant's permissions (submission, confirmation, observation). If the participant already hosts the specified party, update the participant's permissions. removes: The unique identifiers of the participants that should no longer host the party. signedBy: Refers to the optional fingerprint of the authorizing key which in turn refers to a specific, locally existing certificate. serial: The expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. synchronize: Synchronize timeout can be used to ensure that the state has been propagated into the node mustFullyAuthorize: When set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. If this is not the case, the request fails. When set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. store:

* "Authorized": The topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: The topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. force: must be set when disabling a party with active contracts requiresPartyToBeOnboarded: When set to true, indicate that the added participants need to first onboard the party independently from this call before the added participants fully host the party.

**Arguments**

* `party`: `com.digitalasset.canton.topology.PartyId`
* `adds`: `Seq[(com.digitalasset.canton.topology.ParticipantId, com.digitalasset.canton.topology.transaction.ParticipantPermission)]`
* `removes`: `Seq[com.digitalasset.canton.topology.ParticipantId]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `mustFullyAuthorize`: `Boolean`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `forceFlags`: `com.digitalasset.canton.topology.ForceFlags`
* `requiresPartyToBeOnboarded`: `Boolean`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.PartyToParticipant]`

<div id="topology.sequencers.help" />

### `topology.sequencers.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.sequencers.propose" />

### `topology.sequencers.propose`

Propose changes to the sequencer topology.

synchronizerId: the target synchronizer active: the list of active sequencers passive: sequencers that receive messages but are not available for members to connect to

store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal serial: the expected serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. synchronize: Synchronization timeout to wait until the proposal has been observed on the synchronizer.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`
* `threshold`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `active`: `Seq[com.digitalasset.canton.topology.SequencerId]`
* `passive`: `Seq[com.digitalasset.canton.topology.SequencerId]`
* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `mustFullyAuthorize`: `Boolean`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`

**Returns:** `com.digitalasset.canton.topology.transaction.SignedTopologyTransaction[com.digitalasset.canton.topology.transaction.TopologyChangeOp,com.digitalasset.canton.topology.transaction.SequencerSynchronizerState]`

<div id="topology.synchronisation.await_idle" />

### `topology.synchronisation.await_idle`

Wait until the topology processing of a node is idle.

This function waits until the `is_idle()` function returns true.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="topology.synchronisation.is_idle" />

### `topology.synchronisation.is_idle`

Check if the topology processing of a node is idle.

Topology transactions pass through a set of queues before becoming effective on a synchronizer. This function allows to check if all the queues are empty. While both synchronizer and participant nodes support similar queues, there is some ambiguity around the participant queues. While the synchronizer does really know about all in-flight transactions at any point in time, a participant won't know about the state of any transaction that is currently being processed by the synchronizer topology dispatcher.

**Returns:** `Boolean`

<div id="topology.stores.create_temporary_topology_store" />

### `topology.stores.create_temporary_topology_store`

Creates a temporary topology store.

A temporary topology store is useful for orchestrating the synchronizer founding ceremony or importing a topology snapshot for later inspection. Temporary topology stores are not persisted and all transactions are kept in memory only, which means restarting the node causes the loss of all transactions in that store. Additionally, temporary topology stores are not connected to any synchronizer, so there is no automatic propagation of topology transactions from the temporary store to connected synchronizers.

**Arguments**

* `name`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**Returns:** `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Temporary`

<div id="topology.stores.drop_temporary_topology_store" />

### `topology.stores.drop_temporary_topology_store`

This command drops a temporary topology store and all transactions contained in it.

Dropping a temporary topology store is not reversible and all topology transactions in the store will be permanently dropped. It's not possible to delete the authorized store or any synchronizer store with this command.

**Arguments**

* `temporaryStoreId`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId.Temporary`

<div id="topology.stores.help" />

### `topology.stores.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.stores.list" />

### `topology.stores.list`

List available topology stores.

**Returns:** `Seq[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`

<div id="topology.vetted_packages.help" />

### `topology.vetted_packages.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="topology.vetted_packages.list" />

### `topology.vetted_packages.list`

List vetted packages.

store: the optional topology store to query from proposals: if true then proposals are shown, otherwise actual validated state

**Arguments**

* `store`: `Option[com.digitalasset.canton.topology.admin.grpc.TopologyStoreId]`
* `proposals`: `Boolean`
* `timeQuery`: `com.digitalasset.canton.topology.store.TimeQuery`
* `operation`: `Option[com.digitalasset.canton.topology.transaction.TopologyChangeOp]`
* `filterParticipant`: `String`
* `filterSigningKey`: `String`
* `protocolVersion`: `Option[String]`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.topology.ListVettedPackagesResult]`

<div id="topology.vetted_packages.propose" />

### `topology.vetted_packages.propose`

Replace package vettings.

A participant will only process transactions that reference packages that all involved participants have vetted previously. Vetting is done by registering a respective topology transaction with the synchronizer, which can then be used by other participants to verify that a transaction is only using vetted packages. Note that all referenced and dependent packages must exist in the package store.

participantId: the identifier of the participant vetting the packages packages: The lf-package ids with validity boundaries to be vetted that will replace the previous vetted packages. store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. serial: ted serial this topology transaction should have. Serials must be contiguous and start at 1. This transaction will be rejected if another fully authorized transaction with the same serial already exists, or if there is a gap between this serial and the most recently used serial. If None, the serial will be automatically selected by the node. signedBy: the fingerprint of the key to be used to sign this proposal force: must be set when revoking the vetting of packagesIds

**Arguments**

* `participant`: `com.digitalasset.canton.topology.ParticipantId`
* `packages`: `Seq[com.digitalasset.canton.topology.transaction.VettedPackage]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `serial`: `Option[com.digitalasset.canton.config.RequireTypes.PositiveInt]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `force`: `com.digitalasset.canton.topology.ForceFlags`
* `operation`: `com.digitalasset.canton.topology.transaction.TopologyChangeOp`

<div id="topology.vetted_packages.propose_delta" />

### `topology.vetted_packages.propose_delta`

Change package vettings.

A participant will only process transactions that reference packages that all involved participants have vetted previously. Vetting is done by registering a respective topology transaction with the synchronizer, which can then be used by other participants to verify that a transaction is only using vetted packages. Note that all referenced and dependent packages must exist in the package store.

participantId: the identifier of the participant vetting the packages adds: The lf-package ids to be vetted. removes: The lf-package ids to be unvetted. store:

* "Authorized": the topology transaction will be stored in the node's authorized store and automatically propagated to connected synchronizers, if applicable.
* `"<synchronizer id>"`: the topology transaction will be directly submitted to the specified synchronizer without storing it locally first. This also means it will *not* be synchronized to other synchronizers automatically. filterParticipant: Filter for participants starting with the given filter string. mustFullyAuthorize: when set to true, the proposal's previously received signatures and the signature of this node must be sufficient to fully authorize the topology transaction. if this is not the case, the request fails. when set to false, the proposal retains the proposal status until enough signatures are accumulated to satisfy the mapping's authorization requirements. signedBy: the fingerprint of the key to be used to sign this proposal force: must be set when revoking the vetting of packagesIds

**Arguments**

* `participant`: `com.digitalasset.canton.topology.ParticipantId`
* `adds`: `Seq[com.digitalasset.canton.topology.transaction.VettedPackage]`
* `removes`: `Seq[com.digitalasset.daml.lf.data.Ref.PackageId]`
* `store`: `com.digitalasset.canton.topology.admin.grpc.TopologyStoreId`
* `mustFullyAuthorize`: `Boolean`
* `synchronize`: `Option[com.digitalasset.canton.config.NonNegativeDuration]`
* `signedBy`: `Option[com.digitalasset.canton.crypto.Fingerprint]`
* `force`: `com.digitalasset.canton.topology.ForceFlags`

### Traffic

<div id="traffic_control.help" />

### `traffic_control.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="traffic_control.traffic_state" />

### `traffic_control.traffic_state`

Return the traffic state of the node.

Use this command to get the traffic state of the node at a given time for a specific synchronizer id.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`

**Returns:** `com.digitalasset.canton.sequencing.protocol.TrafficState`

## Sequencer Administration Commands

<div id="bft.add_peer_endpoint" />

### `bft.add_peer_endpoint`

Add a new peer endpoint.

**Arguments**

* `endpointConfig`: `com.digitalasset.canton.synchronizer.sequencer.block.bftordering.core.BftBlockOrdererConfig.P2PEndpointConfig`

<div id="bft.disable_performance_metrics" />

### `bft.disable_performance_metrics`

Disable BFT ordering performance metrics.

<div id="bft.enable_performance_metrics" />

### `bft.enable_performance_metrics`

Enable BFT ordering performance metrics.

<div id="bft.get_ordering_topology" />

### `bft.get_ordering_topology`

Get the currently active ordering topology.

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.block.bftordering.admin.SequencerBftAdminData.OrderingTopology`

<div id="bft.get_peer_network_status" />

### `bft.get_peer_network_status`

Get peer network status.

**Arguments**

* `endpoints`: `Option[Iterable[com.digitalasset.canton.synchronizer.sequencer.block.bftordering.core.BftBlockOrdererConfig.EndpointId]]`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.block.bftordering.admin.SequencerBftAdminData.PeerNetworkStatus`

<div id="bft.remove_peer_endpoint" />

### `bft.remove_peer_endpoint`

Remove a peer endpoint.

**Arguments**

* `peerEndpointId`: `com.digitalasset.canton.synchronizer.sequencer.block.bftordering.core.BftBlockOrdererConfig.EndpointId`

<div id="clear_cache_2" />

### `clear_cache_2`

Clear locally cached variables.

Some commands cache values on the client side. Use this command to explicitly clear the caches of these values.

<div id="config_2" />

### `config_2`

Returns the sequencer configuration.

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.config.SequencerNodeConfig`

<div id="help_3" />

### `help_3`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="id_2" />

### `id_2`

Yields the globally unique id of this sequencer. Throws an exception, if the id has not yet been allocated (e.g., the sequencer has not yet been started).

**Returns:** `com.digitalasset.canton.topology.SequencerId`

<div id="is_initialized_2" />

### `is_initialized_2`

Check if the local instance is running and is fully initialized.

**Returns:** `Boolean`

<div id="is_running_2" />

### `is_running_2`

Check if the local instance is running.

**Returns:** `Boolean`

<div id="maybeid_2" />

### `maybeid_2`

Yields Some(id) of this sequencer if id present. Returns None, if the id has not yet been allocated (e.g., the sequencer has not yet been initialised).

**Returns:** `Option[com.digitalasset.canton.topology.SequencerId]`

<div id="physical_synchronizer_id" />

### `physical_synchronizer_id`

Returns the physical synchronizer id of the synchronizer.

**Returns:** `com.digitalasset.canton.topology.PhysicalSynchronizerId`

<div id="pruning.clear_schedule_3" />

### `pruning.clear_schedule_3`

Deactivate automatic pruning.

<div id="pruning.find_pruning_timestamp_1" />

### `pruning.find_pruning_timestamp_1`

Obtain a timestamp at or near the beginning of sequencer state.

This command provides insight into the current state of sequencer pruning when called with the default value of `index` 1. When pruning the sequencer manually via `prune_at` and with the intent to prune in batches, specify a value such as 1000 to obtain a pruning timestamp that corresponds to the "end" of the batch.

**Arguments**

* `index`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="pruning.force_prune" />

### `pruning.force_prune`

Force remove data from the Sequencer including data that may have not been read by offline clients.

Will force pruning up until the default retention period by potentially disabling clients that have not yet read data we would like to remove. Disabling these clients will prevent them from ever reconnecting to the Synchronizer so should only be used if the Synchronizer operator is confident they can be permanently ignored. Run with `dryRun = true` to review a description of which clients will be disabled first. Run with `dryRun = false` to disable these clients and perform a forced pruning.

**Arguments**

* `dryRun`: `Boolean`

**Returns:** `String`

<div id="pruning.force_prune_at" />

### `pruning.force_prune_at`

Force removing data from the Sequencer including data that may have not been read by offline clients up until the specified time.

Similar to the above `force_prune` command but allows specifying the exact time at which to prune

**Arguments**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `dryRun`: `Boolean`

**Returns:** `String`

<div id="pruning.force_prune_with_retention_period" />

### `pruning.force_prune_with_retention_period`

Force removing data from the Sequencer including data that may have not been read by offline clients up until a custom retention period.

Similar to the above `force_prune` command but allows specifying a custom retention period

**Arguments**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`
* `dryRun`: `Boolean`

**Returns:** `String`

<div id="pruning.get_schedule_2" />

### `pruning.get_schedule_2`

Inspect the automatic pruning schedule.

The schedule consists of a "cron" expression and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period. Returns `None` if no schedule has been configured via `set_schedule` or if `clear_schedule` has been invoked.

**Returns:** `Option[com.digitalasset.canton.admin.api.client.data.PruningSchedule]`

<div id="pruning.help_3" />

### `pruning.help_3`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="pruning.prune_2" />

### `pruning.prune_2`

Remove unnecessary data from the Sequencer up until the default retention point.

Removes unnecessary data from the Sequencer that is earlier than the default retention period. The default retention period is set in the configuration of the canton processing running this command under `parameters.retention-period-defaults.sequencer`. This pruning command requires that data is read and acknowledged by clients before considering it safe to remove.

If no data is being removed it could indicate that clients are not reading or acknowledging data in a timely fashion (typically due to nodes going offline for long periods). You have the option of disabling the members running on these nodes to allow removal of this data, however this will mean that they will be unable to reconnect to the synchronizer in the future. To do this run `force_prune(dryRun = true)` to return a description of which members would be disabled in order to prune the Sequencer. If you are happy to disable the described clients then run `force_prune(dryRun = false)` to permanently remove their unread data.

Once offline clients have been disabled you can continue to run `prune` normally.

**Returns:** `String`

<div id="pruning.prune_at_1" />

### `pruning.prune_at_1`

Remove data that has been read up until the specified time.

Similar to the above `prune` command but allows specifying the exact time at which to prune. The command will fail if a client has not yet read and acknowledged some data up to the specified time.

**Arguments**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**Returns:** `String`

<div id="pruning.prune_with_retention_period_1" />

### `pruning.prune_with_retention_period_1`

Remove data that has been read up until a custom retention period.

Similar to the above `prune` command but allows specifying a custom retention period

**Arguments**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`

**Returns:** `String`

<div id="pruning.set_cron_2" />

### `pruning.set_cron_2`

Modify the cron used by automatic pruning.

The schedule is specified in cron format and refers to pruning start times in the GMT time zone. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `cron`: `String`

<div id="pruning.set_max_duration_2" />

### `pruning.set_max_duration_2`

Modify the maximum duration used by automatic pruning.

The `maxDuration` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_retention_2" />

### `pruning.set_retention_2`

Update the pruning retention used by automatic pruning.

The `retention` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this update, pruning is actively running, a best effort is made to pause pruning and restart with the newly specified retention. This allows for the case that the new retention mandates retaining more data than previously.

**Arguments**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_schedule_3" />

### `pruning.set_schedule_3`

Activate automatic pruning according to the specified schedule.

The schedule is specified in cron format and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period.

**Arguments**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.status" />

### `pruning.status`

Status of the sequencer and its connected clients.

Provides a detailed breakdown of information required for pruning:

* the current time according to this sequencer instance
* synchronizer members that the sequencer supports
* for each member when they were registered and whether they are enabled
* a list of clients for each member, their last acknowledgement, and whether they are enabled

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.SequencerPruningStatus`

<div id="repair.disable_member" />

### `repair.disable_member`

Disable the provided member at the Sequencer that will allow any unread data for them to be removed.

This will prevent any client for the given member to reconnect the Sequencer and allow any unread/unacknowledged data they have to be removed. This should only be used if the synchronizer operation is confident the member will never need to reconnect as there is no way to re-enable the member. To view members using the sequencer run `sequencer.status()`."

**Arguments**

* `member`: `com.digitalasset.canton.topology.Member`

<div id="setup.assign_from_genesis_state" />

### `setup.assign_from_genesis_state`

Initialize a sequencer from the beginning of the event stream. This should only be called for sequencer nodes being initialized at the same time as the corresponding synchronizer node. This is called as part of the synchronizer.setup.bootstrap command, so you are unlikely to need to call this directly.

**Arguments**

* `genesisState`: `com.google.protobuf.ByteString`
* `synchronizerParameters`: `com.digitalasset.canton.admin.api.client.data.StaticSynchronizerParameters`
* `waitForReady`: `Boolean`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_genesis_statev2" />

### `setup.assign_from_genesis_statev2`

Initialize a sequencer from the beginning of the event stream. This should only be called for sequencer nodes being initialized at the same time as the corresponding synchronizer node. This is called as part of the synchronizer.setup.bootstrap command, so you are unlikely to need to call this directly.

**Arguments**

* `genesisState`: `com.google.protobuf.ByteString`
* `synchronizerParameters`: `com.digitalasset.canton.admin.api.client.data.StaticSynchronizerParameters`
* `waitForReady`: `Boolean`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_onboarding_state" />

### `setup.assign_from_onboarding_state`

Dynamically initialize a sequencer from a point later than the beginning of the event stream.

**Arguments**

* `onboardingState`: `com.google.protobuf.ByteString`
* `waitForReady`: `Boolean`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.assign_from_onboarding_statev2" />

### `setup.assign_from_onboarding_statev2`

Dynamically initialize a sequencer from a point later than the beginning of the event stream.

**Arguments**

* `onboardingState`: `com.google.protobuf.ByteString`
* `waitForReady`: `Boolean`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.admin.grpc.InitializeSequencerResponse`

<div id="setup.help_1" />

### `setup.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="setup.initialize_from_synchronizer_predecessor" />

### `setup.initialize_from_synchronizer_predecessor`

Initialize a sequencer for the logical upgrade from the state of its predecessor.

**Arguments**

* `predecessorState`: `com.google.protobuf.ByteString`
* `synchronizerParameters`: `com.digitalasset.canton.admin.api.client.data.StaticSynchronizerParameters`
* `waitForReady`: `Boolean`

<div id="setup.onboarding_state_at_timestamp" />

### `setup.onboarding_state_at_timestamp`

Download the onboarding state at a given point in time to bootstrap another sequencer.

**Arguments**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="setup.onboarding_state_for_sequencer" />

### `setup.onboarding_state_for_sequencer`

Download the onboarding state for a given sequencer.

**Arguments**

* `sequencerId`: `com.digitalasset.canton.topology.SequencerId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="setup.onboarding_state_for_sequencerv2" />

### `setup.onboarding_state_for_sequencerv2`

Download the onboarding state for a given sequencer.

**Arguments**

* `sequencerId`: `com.digitalasset.canton.topology.SequencerId`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.google.protobuf.ByteString`

<div id="setup.snapshot" />

### `setup.snapshot`

Download sequencer snapshot at given point in time to bootstrap another sequencer.

It is recommended to use onboarding\_state\_for\_sequencer for onboarding a new sequencer.

**Arguments**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.SequencerSnapshot`

<div id="start_2" />

### `start_2`

Start the instance.

<div id="stop_2" />

### `stop_2`

Stop the instance.

<div id="synchronizer_id" />

### `synchronizer_id`

Returns the logical synchronizer id of the synchronizer.

**Returns:** `com.digitalasset.canton.topology.SynchronizerId`

### Database

<div id="db.help_2" />

### `db.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="db.migrate_2" />

### `db.migrate_2`

Migrates the instance's database if using a database storage.

When instances reside on different nodes, their database migration can be run in parallel to save time. Please not that the migration commands must however must be run on each node individually, because remote migration through `participants.remote...` is not supported.

<div id="db.repair_migration_2" />

### `db.repair_migration_2`

Only use when advised - repairs the database migration of the instance's database.

In some rare cases, we change already applied database migration files in a new release and the repair command resets the checksums we use to ensure that in general already applied migration files have not been changed. You should only use `db.repair_migration` when advised and otherwise use it at your own risk - in the worst case running it may lead to data corruption when an incompatible database migration (one that should be rejected because the already applied database migration files have changed) is subsequently falsely applied.

**Arguments**

* `force`: `Boolean`

### Synchronizer parameters

<div id="synchronizer_parameters" />

### `synchronizer_parameters`

Synchronizer parameters related commands.

**Returns:** `SequencerReference.this.synchronizer_parameters.type`

### Health

<div id="health.active_2" />

### `health.active_2`

Check if the node is running and is the active instance (mediator, participant).

**Returns:** `Boolean`

<div id="health.dump_3" />

### `health.dump_3`

Collect Canton system information to help diagnose issues.

Generates a comprehensive health report for the local Canton process and any connected remote nodes.

The arguments are:

* `outputFile`: Specifies the file path to save the report. If not set, a default path is used.
* `timeout`: Sets a custom timeout for gathering data, useful for large reports from slow remote nodes.
* `chunkSize`: Adjusts the data stream chunk size from remote nodes. Use this to prevent gRPC errors related to 'max inbound message size'

**Arguments**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**Returns:** `String`

<div id="health.has_identity_2" />

### `health.has_identity_2`

Returns true if the node has an identity.

**Returns:** `Boolean`

<div id="health.help_3" />

### `health.help_3`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="health.initialized_2" />

### `health.initialized_2`

Returns true if node has been initialized.

**Returns:** `Boolean`

<div id="health.is_ready_for_id_2" />

### `health.is_ready_for_id_2`

Check if the node is ready for setting the node's id.

**Returns:** `Boolean`

<div id="health.is_ready_for_initialization_2" />

### `health.is_ready_for_initialization_2`

Check if the node is ready for initialization.

**Returns:** `Boolean`

<div id="health.is_ready_for_node_topology_2" />

### `health.is_ready_for_node_topology_2`

Check if the node is ready for uploading the node's identity topology.

**Returns:** `Boolean`

<div id="health.is_running_2" />

### `health.is_running_2`

Check if the node is running.

**Returns:** `Boolean`

<div id="health.last_error_trace_2" />

### `health.last_error_trace_2`

Show all messages logged with the given traceId in a recent interval.

Returns a list of buffered log messages associated to a given trace-id. Usually, the trace-id is taken from last\_errors()

**Arguments**

* `traceId`: `String`

**Returns:** `Seq[String]`

<div id="health.last_errors_2" />

### `health.last_errors_2`

Show the last errors logged.

Returns a map with the trace-id as key and the most recent error messages as value. Requires that --log-last-errors is enabled (and not turned off).

**Returns:** `Map[String,String]`

<div id="health.set_log_level_2" />

### `health.set_log_level_2`

Change the log level of the process.

If the default logback configuration is used, this will change the log level of the process.

**Arguments**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_3" />

### `health.status_3`

Get human (and machine) readable status information.

**Returns:** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity_2" />

### `health.wait_for_identity_2`

Wait for the node to have an identity.

<div id="health.wait_for_initialized_2" />

### `health.wait_for_initialized_2`

Wait for the node to be initialized.

<div id="health.wait_for_ready_for_id_2" />

### `health.wait_for_ready_for_id_2`

Wait for the node to be ready for setting the node's id.

<div id="health.wait_for_ready_for_initialization_2" />

### `health.wait_for_ready_for_initialization_2`

Wait for the node to be ready for initialization.

<div id="health.wait_for_ready_for_node_topology_2" />

### `health.wait_for_ready_for_node_topology_2`

Wait for the node to be ready for uploading the node's identity topology.

<div id="health.wait_for_running_2" />

### `health.wait_for_running_2`

Wait for the node to be running.

### Key Administration

<div id="keys.help_2" />

### `keys.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.download_2" />

### `keys.public.download_2`

Download public key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.public.download_to_2" />

### `keys.public.download_to_2`

Download public key and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help_2" />

### `keys.public.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.list_2" />

### `keys.public.list_2`

List public keys in registry.

Returns all public keys that have been added to the key registry. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner_2" />

### `keys.public.list_by_owner_2`

List keys for given keyOwner.

This command is a convenience wrapper for `list_key_owners`, taking an explicit keyOwner as search argument. The response includes the public keys.

**Arguments**

* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners_2" />

### `keys.public.list_owners_2`

List active owners with keys for given search arguments.

This command allows deep inspection of the topology state. The response includes the public keys. Optional filterKeyOwnerType type can be 'ParticipantId.Code' , 'MediatorId.Code','SequencerId.Code'.

**Arguments**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.topology.MemberCode]`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload_2" />

### `keys.public.upload_2`

Upload public key.

Import a public key and store it together with a name used to provide some context to that key.

**Arguments**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from_2" />

### `keys.public.upload_from_2`

Upload public key.

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete_2" />

### `keys.secret.delete_2`

Delete private key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download_2" />

### `keys.secret.download_2`

Download key pair.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to_2" />

### `keys.secret.download_to_2`

Download key pair and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key_2" />

### `keys.secret.generate_encryption_key_2`

Generate new public/private key pair for encryption and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key_2" />

### `keys.secret.generate_signing_key_2`

Generate new public/private key pair for signing and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id_2" />

### `keys.secret.get_wrapper_key_id_2`

Get the wrapper key id that is used for the encrypted private keys store.

**Returns:** `String`

<div id="keys.secret.help_2" />

### `keys.secret.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.secret.list_2" />

### `keys.secret.list_2`

List keys in private vault.

Returns all public keys to the corresponding private keys in the key vault. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key_2" />

### `keys.secret.register_kms_encryption_key_2`

Register the specified KMS encryption key in canton storing its public information in the vault.

The id for the KMS encryption key. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key_2" />

### `keys.secret.register_kms_signing_key_2`

Register the specified KMS signing key in canton storing its public information in the vault.

The id for the KMS signing key. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key_2" />

### `keys.secret.rotate_kms_node_key_2`

Rotate a given node's keypair with a new pre-generated KMS keypair.

Rotates an existing encryption or signing key stored externally in a KMS with a pre-generated key. NOTE: A namespace root signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. The id of the new KMS key (e.g. Resource Name). An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key_2" />

### `keys.secret.rotate_node_key_2`

Rotate a node's public/private key pair.

Rotates an existing encryption or signing key. NOTE: A namespace root or intermediate signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys_2" />

### `keys.secret.rotate_node_keys_2`

Rotate the node's public/private key pairs.

For a participant node it rotates the signing and encryption key pair. For a sequencer or mediator node it rotates the signing key pair as those nodes do not have an encryption key pair. NOTE: Namespace root or intermediate signing keys are NOT rotated by this command.

<div id="keys.secret.rotate_wrapper_key_2" />

### `keys.secret.rotate_wrapper_key_2`

Change the wrapper key for encrypted private keys store.

Change the wrapper key (e.g. AWS KMS key) being used to encrypt the private keys in the store. newWrapperKeyId: The optional new wrapper key id to be used. If the wrapper key id is empty Canton will generate a new key based on the current configuration.

**Arguments**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload_2" />

### `keys.secret.upload_2`

Upload a key pair.

Upload the previously downloaded key pair. pairBytes: The binary representation of a previously downloaded key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from_2" />

### `keys.secret.upload_from_2`

Upload (load and import) a key pair from file.

Upload the previously downloaded key pair from a file. filename: The name of the file holding the key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### Metrics

<div id="metrics.get_2" />

### `metrics.get_2`

Get a particular metric.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point_2" />

### `metrics.get_double_point_2`

Get a particular double point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram_2" />

### `metrics.get_histogram_2`

Get a particular histogram.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point_2" />

### `metrics.get_long_point_2`

Get a particular long point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary_2" />

### `metrics.get_summary_2`

Get a particular summary.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list_2" />

### `metrics.list_2`

List all metrics.

Returns the metric with the given name and optionally matching attributes.

**Arguments**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

### Traffic

<div id="traffic_control.help_2" />

### `traffic_control.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="traffic_control.last_traffic_state_update_of_members" />

### `traffic_control.last_traffic_state_update_of_members`

Return the last traffic state update of the given members, per member.

Use this command to get the last traffic state update of each member. It will be last updated when a member consumed traffic.

**Arguments**

* `members`: `Seq[com.digitalasset.canton.topology.Member]`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus`

<div id="traffic_control.set_traffic_balance" />

### `traffic_control.set_traffic_balance`

Set the traffic purchased entry of a member.

Use this command to set the new traffic purchased entry of a member. member: member for which the traffic purchased entry is to be set serial: serial number of the request, must be strictly greater than the latest update made for that member newBalance: new traffic purchased entry to be set

returns: the max sequencing time used for the update After and only after that time, if the new balance still does not appear in the traffic state, the update can be considered failed and should be retried.

**Arguments**

* `member`: `com.digitalasset.canton.topology.Member`
* `serial`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`
* `newBalance`: `com.digitalasset.canton.config.RequireTypes.NonNegativeLong`

<div id="traffic_control.traffic_state_2" />

### `traffic_control.traffic_state_2`

Return the traffic state of the node.

Use this command to get the traffic state of the node at a given time for a specific synchronizer id.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`

**Returns:** `com.digitalasset.canton.sequencing.protocol.TrafficState`

<div id="traffic_control.traffic_state_of_all_members" />

### `traffic_control.traffic_state_of_all_members`

Return the traffic state of the all members.

Use this command to get the traffic state of all members. Set latestApproximate to true to get an approximation of the traffic state (including base traffic) at the latest possible timestamp the sequencer can calculate it. This an approximation only because the sequencer may use its wall clock which could be beyond the synchronizer time.

**Arguments**

* `latestApproximate`: `Boolean`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus`

<div id="traffic_control.traffic_state_of_members" />

### `traffic_control.traffic_state_of_members`

Return the traffic state of the given members.

Use this command to get the traffic state of a list of members at the latest safe timestamp.

**Arguments**

* `members`: `Seq[com.digitalasset.canton.topology.Member]`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus`

<div id="traffic_control.traffic_state_of_members_approximate" />

### `traffic_control.traffic_state_of_members_approximate`

Return the traffic state of the given members at the latest approximate time.

Use this command to get the traffic state of a list of members using the latest possible time the sequencer can estimate the state. CAREFUL: The returned state is only an approximation in the future and might not be the actual correct state by the time this timestamp is reached by the synchronizer.

**Arguments**

* `members`: `Seq[com.digitalasset.canton.topology.Member]`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus`

<div id="traffic_control.traffic_state_of_members_at_timestamp" />

### `traffic_control.traffic_state_of_members_at_timestamp`

Return the traffic state of the given members at a specific timestamp.

Use this command to get the traffic state of specified members at a given timestamp.

**Arguments**

* `members`: `Seq[com.digitalasset.canton.topology.Member]`
* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

**Returns:** `com.digitalasset.canton.synchronizer.sequencer.traffic.SequencerTrafficStatus`

## Mediator Administration Commands

<div id="clear_cache_1" />

### `clear_cache_1`

Clear locally cached variables.

Some commands cache values on the client side. Use this command to explicitly clear the caches of these values.

<div id="config_1" />

### `config_1`

Returns the mediator configuration.

**Returns:** `com.digitalasset.canton.synchronizer.mediator.MediatorNodeConfig`

<div id="help_2" />

### `help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="id_1" />

### `id_1`

Yields the mediator id of this mediator. Throws an exception, if the id has not yet been allocated (e.g., the mediator has not yet been initialised).

**Returns:** `com.digitalasset.canton.topology.MediatorId`

<div id="inspection" />

### `inspection`

Inspection functionality for the mediator.

**Returns:** `com.digitalasset.canton.console.commands.MediatorInspectionGroup`

<div id="is_initialized_1" />

### `is_initialized_1`

Check if the local instance is running and is fully initialized.

**Returns:** `Boolean`

<div id="is_running_1" />

### `is_running_1`

Check if the local instance is running.

**Returns:** `Boolean`

<div id="maybeid_1" />

### `maybeid_1`

Yields Some(id) of this mediator if id present. Returns None, if the id has not yet been allocated (e.g., the mediator has not yet been initialised).

**Returns:** `Option[com.digitalasset.canton.topology.MediatorId]`

<div id="setup.assign" />

### `setup.assign`

Assign a mediator to a synchronizer.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.PhysicalSynchronizerId`
* `sequencerConnections`: `com.digitalasset.canton.sequencing.SequencerConnections`
* `sequencerConnectionValidation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`
* `waitForReady`: `Boolean`

<div id="setup.help" />

### `setup.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="start_1" />

### `start_1`

Start the instance.

<div id="stop_1" />

### `stop_1`

Stop the instance.

### Database

<div id="db.help_1" />

### `db.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="db.migrate_1" />

### `db.migrate_1`

Migrates the instance's database if using a database storage.

When instances reside on different nodes, their database migration can be run in parallel to save time. Please not that the migration commands must however must be run on each node individually, because remote migration through `participants.remote...` is not supported.

<div id="db.repair_migration_1" />

### `db.repair_migration_1`

Only use when advised - repairs the database migration of the instance's database.

In some rare cases, we change already applied database migration files in a new release and the repair command resets the checksums we use to ensure that in general already applied migration files have not been changed. You should only use `db.repair_migration` when advised and otherwise use it at your own risk - in the worst case running it may lead to data corruption when an incompatible database migration (one that should be rejected because the already applied database migration files have changed) is subsequently falsely applied.

**Arguments**

* `force`: `Boolean`

### Health

<div id="health.active_1" />

### `health.active_1`

Check if the node is running and is the active instance (mediator, participant).

**Returns:** `Boolean`

<div id="health.dump_2" />

### `health.dump_2`

Collect Canton system information to help diagnose issues.

Generates a comprehensive health report for the local Canton process and any connected remote nodes.

The arguments are:

* `outputFile`: Specifies the file path to save the report. If not set, a default path is used.
* `timeout`: Sets a custom timeout for gathering data, useful for large reports from slow remote nodes.
* `chunkSize`: Adjusts the data stream chunk size from remote nodes. Use this to prevent gRPC errors related to 'max inbound message size'

**Arguments**

* `outputFile`: `String`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`
* `chunkSize`: `Option[Int]`

**Returns:** `String`

<div id="health.has_identity_1" />

### `health.has_identity_1`

Returns true if the node has an identity.

**Returns:** `Boolean`

<div id="health.help_2" />

### `health.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="health.initialized_1" />

### `health.initialized_1`

Returns true if node has been initialized.

**Returns:** `Boolean`

<div id="health.is_ready_for_id_1" />

### `health.is_ready_for_id_1`

Check if the node is ready for setting the node's id.

**Returns:** `Boolean`

<div id="health.is_ready_for_initialization_1" />

### `health.is_ready_for_initialization_1`

Check if the node is ready for initialization.

**Returns:** `Boolean`

<div id="health.is_ready_for_node_topology_1" />

### `health.is_ready_for_node_topology_1`

Check if the node is ready for uploading the node's identity topology.

**Returns:** `Boolean`

<div id="health.is_running_1" />

### `health.is_running_1`

Check if the node is running.

**Returns:** `Boolean`

<div id="health.last_error_trace_1" />

### `health.last_error_trace_1`

Show all messages logged with the given traceId in a recent interval.

Returns a list of buffered log messages associated to a given trace-id. Usually, the trace-id is taken from last\_errors()

**Arguments**

* `traceId`: `String`

**Returns:** `Seq[String]`

<div id="health.last_errors_1" />

### `health.last_errors_1`

Show the last errors logged.

Returns a map with the trace-id as key and the most recent error messages as value. Requires that --log-last-errors is enabled (and not turned off).

**Returns:** `Map[String,String]`

<div id="health.set_log_level_1" />

### `health.set_log_level_1`

Change the log level of the process.

If the default logback configuration is used, this will change the log level of the process.

**Arguments**

* `level`: `ch.qos.logback.classic.Level`

<div id="health.status_2" />

### `health.status_2`

Get human (and machine) readable status information.

**Returns:** `com.digitalasset.canton.admin.api.client.data.NodeStatus[S]`

<div id="health.wait_for_identity_1" />

### `health.wait_for_identity_1`

Wait for the node to have an identity.

<div id="health.wait_for_initialized_1" />

### `health.wait_for_initialized_1`

Wait for the node to be initialized.

<div id="health.wait_for_ready_for_id_1" />

### `health.wait_for_ready_for_id_1`

Wait for the node to be ready for setting the node's id.

<div id="health.wait_for_ready_for_initialization_1" />

### `health.wait_for_ready_for_initialization_1`

Wait for the node to be ready for initialization.

<div id="health.wait_for_ready_for_node_topology_1" />

### `health.wait_for_ready_for_node_topology_1`

Wait for the node to be ready for uploading the node's identity topology.

<div id="health.wait_for_running_1" />

### `health.wait_for_running_1`

Wait for the node to be running.

### Key Administration

<div id="keys.help_1" />

### `keys.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.download_1" />

### `keys.public.download_1`

Download public key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.public.download_to_1" />

### `keys.public.download_to_1`

Download public key and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`

<div id="keys.public.help_1" />

### `keys.public.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.public.list_1" />

### `keys.public.list_1`

List public keys in registry.

Returns all public keys that have been added to the key registry. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterContext`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.PublicKeyWithName]`

<div id="keys.public.list_by_owner_1" />

### `keys.public.list_by_owner_1`

List keys for given keyOwner.

This command is a convenience wrapper for `list_key_owners`, taking an explicit keyOwner as search argument. The response includes the public keys.

**Arguments**

* `keyOwner`: `com.digitalasset.canton.topology.Member`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.list_owners_1" />

### `keys.public.list_owners_1`

List active owners with keys for given search arguments.

This command allows deep inspection of the topology state. The response includes the public keys. Optional filterKeyOwnerType type can be 'ParticipantId.Code' , 'MediatorId.Code','SequencerId.Code'.

**Arguments**

* `filterKeyOwnerUid`: `String`
* `filterKeyOwnerType`: `Option[com.digitalasset.canton.topology.MemberCode]`
* `synchronizerIds`: `Set[com.digitalasset.canton.topology.SynchronizerId]`
* `asOf`: `Option[java.time.Instant]`
* `limit`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Seq[com.digitalasset.canton.admin.api.client.data.ListKeyOwnersResult]`

<div id="keys.public.upload_1" />

### `keys.public.upload_1`

Upload public key.

Import a public key and store it together with a name used to provide some context to that key.

**Arguments**

* `keyBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.public.upload_from_1" />

### `keys.public.upload_from_1`

Upload public key.

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`

**Returns:** `com.digitalasset.canton.crypto.Fingerprint`

<div id="keys.secret.delete_1" />

### `keys.secret.delete_1`

Delete private key.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `force`: `Boolean`

<div id="keys.secret.download_1" />

### `keys.secret.download_1`

Download key pair.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

**Returns:** `com.google.protobuf.ByteString`

<div id="keys.secret.download_to_1" />

### `keys.secret.download_to_1`

Download key pair and save it to a file.

**Arguments**

* `fingerprint`: `com.digitalasset.canton.crypto.Fingerprint`
* `outputFile`: `String`
* `protocolVersion`: `com.digitalasset.canton.version.ProtocolVersion`
* `password`: `Option[String]`

<div id="keys.secret.generate_encryption_key_1" />

### `keys.secret.generate_encryption_key_1`

Generate new public/private key pair for encryption and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `keySpec`: `Option[com.digitalasset.canton.crypto.EncryptionKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.generate_signing_key_1" />

### `keys.secret.generate_signing_key_1`

Generate new public/private key pair for signing and store it in the vault.

The optional name argument allows you to store an associated string for your convenience. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The keySpec can be used to select a key specification, e.g., which elliptic curve to use, and the default spec is used if left unspecified.

**Arguments**

* `name`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `keySpec`: `Option[com.digitalasset.canton.crypto.SigningKeySpec]`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.get_wrapper_key_id_1" />

### `keys.secret.get_wrapper_key_id_1`

Get the wrapper key id that is used for the encrypted private keys store.

**Returns:** `String`

<div id="keys.secret.help_1" />

### `keys.secret.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="keys.secret.list_1" />

### `keys.secret.list_1`

List keys in private vault.

Returns all public keys to the corresponding private keys in the key vault. Optional arguments can be used for filtering.

**Arguments**

* `filterFingerprint`: `String`
* `filterName`: `String`
* `filterPurpose`: `Set[com.digitalasset.canton.crypto.KeyPurpose]`
* `filterUsage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`

**Returns:** `Seq[com.digitalasset.canton.crypto.admin.grpc.PrivateKeyMetadata]`

<div id="keys.secret.register_kms_encryption_key_1" />

### `keys.secret.register_kms_encryption_key_1`

Register the specified KMS encryption key in canton storing its public information in the vault.

The id for the KMS encryption key. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.EncryptionPublicKey`

<div id="keys.secret.register_kms_signing_key_1" />

### `keys.secret.register_kms_signing_key_1`

Register the specified KMS signing key in canton storing its public information in the vault.

The id for the KMS signing key. The usage specifies the intended use for the signing key that can be:

* `Namespace`: for the root namespace key that defines a node's identity and signs topology requests;
* `SequencerAuthentication`: for a signing key that authenticates members of the network towards a sequencer;
* `Protocol`: for a signing key that deals with all the signing that happens as part of the protocol. The optional name argument allows you to store an associated string for your convenience.

**Arguments**

* `kmsKeyId`: `String`
* `usage`: `Set[com.digitalasset.canton.crypto.SigningKeyUsage]`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.SigningPublicKey`

<div id="keys.secret.rotate_kms_node_key_1" />

### `keys.secret.rotate_kms_node_key_1`

Rotate a given node's keypair with a new pre-generated KMS keypair.

Rotates an existing encryption or signing key stored externally in a KMS with a pre-generated key. NOTE: A namespace root signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. The id of the new KMS key (e.g. Resource Name). An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `newKmsKeyId`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_key_1" />

### `keys.secret.rotate_node_key_1`

Rotate a node's public/private key pair.

Rotates an existing encryption or signing key. NOTE: A namespace root or intermediate signing key CANNOT be rotated by this command. The fingerprint of the key we want to rotate. An optional name for the new key.

**Arguments**

* `fingerprint`: `String`
* `name`: `String`

**Returns:** `com.digitalasset.canton.crypto.PublicKey`

<div id="keys.secret.rotate_node_keys_1" />

### `keys.secret.rotate_node_keys_1`

Rotate the node's public/private key pairs.

For a participant node it rotates the signing and encryption key pair. For a sequencer or mediator node it rotates the signing key pair as those nodes do not have an encryption key pair. NOTE: Namespace root or intermediate signing keys are NOT rotated by this command.

<div id="keys.secret.rotate_wrapper_key_1" />

### `keys.secret.rotate_wrapper_key_1`

Change the wrapper key for encrypted private keys store.

Change the wrapper key (e.g. AWS KMS key) being used to encrypt the private keys in the store. newWrapperKeyId: The optional new wrapper key id to be used. If the wrapper key id is empty Canton will generate a new key based on the current configuration.

**Arguments**

* `newWrapperKeyId`: `String`

<div id="keys.secret.upload_1" />

### `keys.secret.upload_1`

Upload a key pair.

Upload the previously downloaded key pair. pairBytes: The binary representation of a previously downloaded key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `pairBytes`: `com.google.protobuf.ByteString`
* `name`: `Option[String]`
* `password`: `Option[String]`

<div id="keys.secret.upload_from_1" />

### `keys.secret.upload_from_1`

Upload (load and import) a key pair from file.

Upload the previously downloaded key pair from a file. filename: The name of the file holding the key pair name: The (optional) descriptive name of the key pair password: Optional password to decrypt an encrypted key pair

**Arguments**

* `filename`: `String`
* `name`: `Option[String]`
* `password`: `Option[String]`

### Metrics

<div id="metrics.get_1" />

### `metrics.get_1`

Get a particular metric.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue`

<div id="metrics.get_double_point_1" />

### `metrics.get_double_point_1`

Get a particular double point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.DoublePoint`

<div id="metrics.get_histogram_1" />

### `metrics.get_histogram_1`

Get a particular histogram.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Histogram`

<div id="metrics.get_long_point_1" />

### `metrics.get_long_point_1`

Get a particular long point.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.LongPoint`

<div id="metrics.get_summary_1" />

### `metrics.get_summary_1`

Get a particular summary.

Returns the metric with the given name and optionally matching attributes, or error if multiple matching are found.

**Arguments**

* `metricName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `com.digitalasset.canton.metrics.MetricValue.Summary`

<div id="metrics.list_1" />

### `metrics.list_1`

List all metrics.

Returns the metric with the given name and optionally matching attributes.

**Arguments**

* `filterName`: `String`
* `attributes`: `Map[String,String]`

**Returns:** `Map[String,Seq[com.digitalasset.canton.metrics.MetricValue]]`

### Sequencer Connection

<div id="sequencer_connection.get" />

### `sequencer_connection.get`

Get Sequencer Connection.

Use this command to get the currently configured sequencer connection details for this sequencer client. If this node has not yet been initialized, this will return None.

**Returns:** `Option[com.digitalasset.canton.sequencing.SequencerConnections]`

<div id="sequencer_connection.help" />

### `sequencer_connection.help`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="sequencer_connection.logout" />

### `sequencer_connection.logout`

Revoke this sequencer client node's authentication tokens and close all the sequencers connections.

On all the sequencers, all existing authentication tokens for this sequencer client node will be revoked. Note that the node is not disconnected from the synchronizer; only the connections to the sequencers are closed. The node will automatically reopen connections, perform a challenge-response and obtain new tokens.

<div id="sequencer_connection.modify" />

### `sequencer_connection.modify`

Modify Default Sequencer Connection.

Modify sequencer connection details for this sequencer client node, by passing a modifier function that operates on the existing default connection.

**Arguments**

* `modifier`: `[com.digitalasset.canton.sequencing.SequencerConnection => com.digitalasset.canton.sequencing.SequencerConnection](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/sequencing/SequencerConnection.html)`

<div id="sequencer_connection.modify_connections" />

### `sequencer_connection.modify_connections`

Modify Sequencer Connections.

Modify sequencer connection details for this sequencer client node, by passing a modifier function that operates on the existing connection configuration.

**Arguments**

* `modifier`: `[com.digitalasset.canton.sequencing.SequencerConnections => com.digitalasset.canton.sequencing.SequencerConnections](https://docs.digitalasset.com/operate/3.4/scaladoc/com/digitalasset/canton/sequencing/SequencerConnections.html)`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="sequencer_connection.set" />

### `sequencer_connection.set`

Set Sequencer Connection.

Set new sequencer connection details for this sequencer client node. This will replace any pre-configured connection details. This command will only work after the node has been initialized.

**Arguments**

* `connections`: `com.digitalasset.canton.sequencing.SequencerConnections`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

<div id="sequencer_connection.set_single" />

### `sequencer_connection.set_single`

Set Sequencer Connection.

Set new sequencer connection details for this sequencer client node. This will replace any pre-configured connection details. This command will only work after the node has been initialized.

**Arguments**

* `connection`: `com.digitalasset.canton.sequencing.SequencerConnection`
* `validation`: `com.digitalasset.canton.sequencing.SequencerConnectionValidation`

### Testing

<div id="pruning.clear_schedule_2" />

### `pruning.clear_schedule_2`

Deactivate automatic pruning.

<div id="pruning.find_pruning_timestamp" />

### `pruning.find_pruning_timestamp`

Obtain a timestamp at or near the beginning of mediator state.

This command provides insight into the current state of mediator pruning when called with the default value of `index` 1. When pruning the mediator manually via `prune_at` and with the intent to prune in batches, specify a value such as 1000 to obtain a pruning timestamp that corresponds to the "end" of the batch.

**Arguments**

* `index`: `com.digitalasset.canton.config.RequireTypes.PositiveInt`

**Returns:** `Option[com.digitalasset.canton.data.CantonTimestamp]`

<div id="pruning.get_schedule_1" />

### `pruning.get_schedule_1`

Inspect the automatic pruning schedule.

The schedule consists of a "cron" expression and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period. Returns `None` if no schedule has been configured via `set_schedule` or if `clear_schedule` has been invoked.

**Returns:** `Option[com.digitalasset.canton.admin.api.client.data.PruningSchedule]`

<div id="pruning.help_2" />

### `pruning.help_2`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="pruning.prune_1" />

### `pruning.prune_1`

Prune the mediator of unnecessary data while keeping data for the default retention period.

Removes unnecessary data from the Mediator that is earlier than the default retention period. The default retention period is set in the configuration of the canton node running this command under `parameters.retention-period-defaults.mediator`.

<div id="pruning.prune_at" />

### `pruning.prune_at`

Prune the mediator of unnecessary data up to and including the given timestamp.

**Arguments**

* `timestamp`: `com.digitalasset.canton.data.CantonTimestamp`

<div id="pruning.prune_with_retention_period" />

### `pruning.prune_with_retention_period`

Prune the mediator of unnecessary data while keeping data for the provided retention period.

**Arguments**

* `retentionPeriod`: `scala.concurrent.duration.FiniteDuration`

<div id="pruning.set_cron_1" />

### `pruning.set_cron_1`

Modify the cron used by automatic pruning.

The schedule is specified in cron format and refers to pruning start times in the GMT time zone. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `cron`: `String`

<div id="pruning.set_max_duration_1" />

### `pruning.set_max_duration_1`

Modify the maximum duration used by automatic pruning.

The `maxDuration` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this modification, pruning is actively running, a best effort is made to pause pruning and restart according to the new schedule. This allows for the case that the new schedule no longer allows pruning at the current time.

**Arguments**

* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_retention_1" />

### `pruning.set_retention_1`

Update the pruning retention used by automatic pruning.

The `retention` is specified as a positive duration and has at most per-second granularity. This call returns an error if no schedule has been configured via `set_schedule` or if automatic pruning has been disabled via `clear_schedule`. Additionally if at the time of this update, pruning is actively running, a best effort is made to pause pruning and restart with the newly specified retention. This allows for the case that the new retention mandates retaining more data than previously.

**Arguments**

* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="pruning.set_schedule_2" />

### `pruning.set_schedule_2`

Activate automatic pruning according to the specified schedule.

The schedule is specified in cron format and "max\_duration" and "retention" durations. The cron string indicates the points in time at which pruning should begin in the GMT time zone, and the maximum duration indicates how long from the start time pruning is allowed to run as long as pruning has not finished pruning up to the specified retention period.

**Arguments**

* `cron`: `String`
* `maxDuration`: `com.digitalasset.canton.config.PositiveDurationSeconds`
* `retention`: `com.digitalasset.canton.config.PositiveDurationSeconds`

<div id="testing.await_synchronizer_time_2" />

### `testing.await_synchronizer_time_2`

Await for the given time to be reached on the synchronizer.

**Arguments**

* `time`: `com.digitalasset.canton.data.CantonTimestamp`
* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

<div id="testing.fetch_synchronizer_time_2" />

### `testing.fetch_synchronizer_time_2`

Fetch the current time from the synchronizer.

**Arguments**

* `timeout`: `com.digitalasset.canton.config.NonNegativeDuration`

**Returns:** `com.digitalasset.canton.data.CantonTimestamp`

<div id="testing.help_1" />

### `testing.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

### Traffic

<div id="traffic_control.help_1" />

### `traffic_control.help_1`

Help for specific commands (use help() or help("method") for more information).

**Arguments**

* `methodName`: `String`

<div id="traffic_control.traffic_state_1" />

### `traffic_control.traffic_state_1`

Return the traffic state of the node.

Use this command to get the traffic state of the node at a given time for a specific synchronizer id.

**Arguments**

* `synchronizerId`: `com.digitalasset.canton.topology.SynchronizerId`

**Returns:** `com.digitalasset.canton.sequencing.protocol.TrafficState`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
