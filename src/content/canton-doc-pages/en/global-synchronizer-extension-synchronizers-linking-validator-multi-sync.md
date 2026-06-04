---
title: "Connecting a Validator to Multiple Synchronizers"
slug: "global-synchronizer-extension-synchronizers-linking-validator-multi-sync"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/linking-validator-multi-sync.md"
source_title: "Connecting a Validator to Multiple Synchronizers"
tags:
  - global-synchronizer
  - extension-synchronizers
  - linking-validator-multi-sync
---

# Connecting a Validator to Multiple Synchronizers

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting a Validator to Multiple Synchronizers

> How to connect a single validator to the Global Synchronizer and private synchronizers simultaneously

Canton validators can connect to multiple synchronizers at the same time. This is the foundation of hybrid deployments — your validator participates in the Global Synchronizer for network-wide interoperability while also connecting to one or more private synchronizers for specialized workflows.

## How multi-synchronizer connections work

Each synchronizer connection is independent. Your validator maintains a separate communication channel to each synchronizer's sequencer, and contracts are assigned to a specific synchronizer. When you create a contract, it is assigned to one synchronizer. You can later move it to another synchronizer using the unassignment/reassignment protocol.

The validator tracks which synchronizer each contract belongs to and routes transactions accordingly. If a transaction involves contracts on different synchronizers, Canton synchronizes the transaction across both — though this adds latency compared to single-synchronizer transactions.

## Adding a synchronizer connection

### Via Canton Console

If your validator is already running and connected to the Global Synchronizer, you can add a private synchronizer connection at runtime:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ bootstrap.synchronizer(synchronizerName = "private-sync", sequencers = Seq(sequencer1), mediators = Seq(mediator1), synchronizerOwners = Seq(sequencer1), synchronizerThreshold = PositiveInt.one, staticSynchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.forSynchronizer))
    res1: PhysicalSynchronizerId = private-sync::122032922613...::35-0
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.connect_local(sequencer1, "private-sync")
```

The `alias` is a local name you choose to identify the synchronizer. It does not need to match any network-level name — it is only used in your local configuration and API calls.

To verify the connection:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_connected()
    res3: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'private-sync',
        physicalSynchronizerId = private-sync::122032922613...::35-0,
        healthy = true
      )
    )
```

This returns the list of all connected synchronizers with their status and synchronizer ID.

### Via Admin API

You can also register a new synchronizer connection through the Admin API's gRPC interface. The relevant service is `SynchronizerConnectivityService`, with the `ConnectSynchronizer` RPC:

```protobuf theme={"theme":{"light":"github-light","dark":"github-dark"}}
message ConnectSynchronizerRequest {
  string synchronizer_alias = 1;
  SynchronizerConnectionConfig config = 2;
}
```

The `SynchronizerConnectionConfig` includes the sequencer connection URL and any TLS settings.

### Via Helm values

For validators deployed with Helm, you can declare additional synchronizer connections in the values file so they are established on startup:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant:
  additionalSynchronizerConnections:
    - alias: "private-sync"
      sequencerConnection: "https://sequencer.private-sync.example.com"
    - alias: "consortium-sync"
      sequencerConnection: "https://sequencer.consortium.example.com"
```

## Managing synchronizer connections

### Listing connections

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_connected()
    res4: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'private-sync',
        physicalSynchronizerId = private-sync::122032922613...::35-0,
        healthy = true
      )
    )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.list_registered()
    res5: Seq[(SynchronizerConnectionConfig, ConfiguredPhysicalSynchronizerId, Boolean)] = Vector(
      (
        SynchronizerConnectionConfig(
          synchronizer = Synchronizer 'private-sync',
          sequencerConnections = SequencerConnections(
            connections = Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://127.0.0.1:32670
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
        ),
        private-sync::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0,
        true
      )
    )
```

### Disconnecting from a synchronizer

You can disconnect from a synchronizer without losing contract data:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.disconnect("private-sync")
```

Contracts assigned to that synchronizer remain in your local store but cannot be used in transactions until you reconnect. Disconnecting does not unassign contracts — they are still associated with that synchronizer.

### Reconnecting

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant.synchronizers.reconnect("private-sync")
    res7: Boolean = true
```

The validator resumes receiving updates from the synchronizer and can transact on contracts assigned to it.

## Contract assignment and reassignment

When a contract is created, it is assigned to the synchronizer where the creating transaction executes. You control this by submitting the command through the appropriate synchronizer connection.

To move a contract to a different synchronizer:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Unassign from current synchronizer
val unassignId = participant.ledger_api.commands.reassignment.unassign(
  contractId = contractId,
  source = sourceSynchronizerId,
  target = synchronizerId
)

// Reassign to target synchronizer
participant.ledger_api.commands.reassignment.assign(
  unassignId = unassignId,
  source = sourceSynchronizerId,
  target = synchronizerId
)
```

The contract is briefly unavailable between unassignment and reassignment. Both the source and target synchronizer must be connected to your validator, and all stakeholders of the contract must have validators connected to the target synchronizer.

## Choosing the right synchronizer for a contract

Consider these factors when deciding where to assign a contract:

* **Who needs to see it?** All validators hosting the contract's stakeholders must be connected to the contract's synchronizer. Use the Global Synchronizer for contracts involving external parties.
* **Transaction frequency** — High-frequency bilateral workflows run more efficiently on a private synchronizer where you control capacity and avoid traffic fees.
* **Settlement needs** — If a contract will eventually interact with Canton Coin or Global Synchronizer contracts, plan for a reassignment step.
* **Privacy requirements** — Contracts on a private synchronizer are processed exclusively by infrastructure you control. On the Global Synchronizer, the sequencer and mediator are operated by super-validators.

## Troubleshooting

**Connection refused or timeout:**

* Verify the sequencer URL is correct and reachable from your validator's network
* Check that TLS certificates are valid and trusted
* Confirm any firewall or network policy allows outbound connections to the sequencer port

**Synchronizer not listed after connect:**

* Check the validator logs for connection errors
* Verify the synchronizer is initialized and the sequencer is healthy
* Ensure the validator's identity is authorized on the target synchronizer

**Contract reassignment fails:**

* Confirm your validator is connected to both the source and target synchronizers
* Verify all contract stakeholders have validators connected to the target synchronizer
* Check that the contract is not currently being exercised in another transaction

# Synchronizer connections

A Participant Node connects to the Synchronizer by connecting to one or many Sequencers of this Synchronizer.

A Participant Node can connect to multiple Synchronizers at once. The synchronizer connectivity commands allow the administrator of a Participant Node to manage connectivity to Synchronizers.

The following sections explain how to manage such Sequencer connections for a Participant Node.

## Connect

### Connect to a Sequencer by Reference

To connect a Participant Node to a Sequencer by reference (local or remote reference), follow the steps below.

1. Define a Synchronizer alias. An alias is a name chosen by the Participant's operator to manage the connection. For example:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val synchronizerAlias = "mysynchronizer"
    synchronizerAlias : String = "mysynchronizer"
```

2. Set Optional Sequencer Connection Validation. This parameter determines how thoroughly the provided Sequencer connections are validated before being persisted.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerConnectionValidation = com.digitalasset.canton.sequencing.SequencerConnectionValidation.Active
    sequencerConnectionValidation : Active.type = com.digitalasset.canton.sequencing.SequencerConnectionValidation$Active$@e82f02d
```

3. Execute the `connect_local` command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.connect_local(sequencerReference, synchronizerAlias, validation = sequencerConnectionValidation)
```

4. List the connected Synchronizers to verify that the connection is listed. See inspect connections.

### Connect to a Sequencer by URL

To connect to a remote Sequencer:

1. Obtain the Sequencer address and port from the Synchronizer Operator.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerUrl = s"https://${sequencerAddress}:${port}"
    sequencerUrl : String = "https://127.0.0.1:30147"
```

2. Provide custom certificates (if necessary). If the Sequencer uses TLS certificates that cannot be automatically validated using your JVM's trust store (for example, self-signed certificates), you have to provide a custom certificate such that the client can verify the Sequencer's public API TLS certificate. The operate must trust the custom root CA. Let's assume that this root certificate is given by:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val certificatesPath = "tls/root-ca.crt"
    certificatesPath : String = "tls/root-ca.crt"
```

3. Connect the Participant to the Sequencer using the `connect` console command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.connect("mysynchronizer", connection = sequencerUrl, certificatesPath = certificatesPath)
    res6: SynchronizerConnectionConfig = SynchronizerConnectionConfig(
      synchronizer = Synchronizer 'mysynchronizer',
      sequencerConnections = SequencerConnections(
        connections = Sequencer 'DefaultSequencer' -> GrpcSequencerConnection(
          sequencerAlias = Sequencer 'DefaultSequencer',
          endpoints = https://127.0.0.1:32814,
          transportSecurity,
          customTrustCertificates
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
```

4. List the connected Synchronizers to verify that the connection is listed. See inspect connections.

### Connect to decentralized Sequencers

To enhance reliability and security, you can connect to multiple Sequencers of the same Synchronizer using the `connect_bft` command.

1. Create the URL for each Sequencer by referencing its public API address and port.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer1Url = s"http://${sequencer1Address}:${sequencer1Port}"
    sequencer1Url : String = "http://0.0.0.0:30143"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer2Url = s"http://${sequencer2Address}:${sequencer2Port}"
    sequencer2Url : String = "http://127.0.0.1:30145"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Url = s"https://${sequencer3Address}:${sequencer3Port}"
    sequencer3Url : String = "https://127.0.0.1:30147"
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencer3Certificate = com.digitalasset.canton.util.BinaryFileUtil.tryReadByteStringFromFile(certificatesPath)
    sequencer3Certificate : com.google.protobuf.ByteString = <ByteString@3fc760d size=1960 contents="-----BEGIN CERTIFICATE-----\nMIIFeTCCA2GgAwIBAgI...">
```

2. Create the Sequencer connections.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val connections = Seq(
     GrpcSequencerConnection.tryCreate(sequencer1Url, sequencerAlias = "sequencer1"),
     GrpcSequencerConnection.tryCreate(sequencer2Url, sequencerAlias = "sequencer2"),
     GrpcSequencerConnection.tryCreate(sequencer3Url, sequencerAlias = "sequencer3", customTrustCertificates = Some(sequencer3Certificate)),
   )
    connections : Seq[GrpcSequencerConnection] = List(
      GrpcSequencerConnection(sequencerAlias = Sequencer 'sequencer1', endpoints = http://0.0.0.0:32810),
      GrpcSequencerConnection(
        sequencerAlias = Sequencer 'sequencer2',
        endpoints = http://127.0.0.1:32812
      ),
      GrpcSequencerConnection(
        sequencerAlias = Sequencer 'sequencer3',
        endpoints = https://127.0.0.1:32814,
        transportSecurity,
        customTrustCertificates
      )
    )
```

3. Configure the Sequencer trust threshold by setting the minimum number of Sequencers that must agree before a message is considered valid.

* Default: 1
* Maximum: Number of connections

For example, setting the threshold to 2:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerTrustThreshold = 2
    sequencerTrustThreshold : Int = 2
```

4. \[Specific to the connection pool] Configure the Sequencer liveness margin; this sets the number of Sequencer connections, in addition to `sequencerTrustThreshold`-many, from which we attempt to read messages.

* Default: 0
* Higher values increase the resilience to Sequencer delays or failures, but having (`sequencerTrustThreshold` + `sequencerLivenessMargin` > number of connections) provides no benefit.

For example, setting the liveness margin to 1:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val sequencerLivenessMargin = 1
    sequencerLivenessMargin : Int = 1
```

5. Configure submission request amplification: define how often the client should try to send a submission request that is eligible for deduplication.

* Higher values increase the chance of a submission request being accepted by the system, but also increase the load on the Sequencers.
* Default: `SubmissionRequestAmplification.NoAmplification`

In this example, I want to ensure that submission requests are sent to two Sequencers. Therefore, I set the amplification factor to 2 and the patience to 0 seconds.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val submissionRequestAmplification = SubmissionRequestAmplification(factor = 2, patience = 0.seconds)
    submissionRequestAmplification : SubmissionRequestAmplification = SubmissionRequestAmplification(factor = 2, patience = 0s)
```

6. Connect using the `connect_bft` command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.connect_bft(
     connections,
     synchronizerAlias,
     sequencerTrustThreshold = sequencerTrustThreshold,
     sequencerLivenessMargin = sequencerLivenessMargin,
     submissionRequestAmplification = submissionRequestAmplification,
   )
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.list_registered()
    res16: Seq[(SynchronizerConnectionConfig, ConfiguredPhysicalSynchronizerId, Boolean)] = Vector(
      (
        SynchronizerConnectionConfig(
          synchronizer = Synchronizer 'mysynchronizer',
          sequencerConnections = SequencerConnections(
            connections = Map(
              Sequencer 'sequencer1' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer1',
                sequencerId = SEQ::sequencer1::1220cb0a22fb...,
                endpoints = http://0.0.0.0:30143
              ),
              Sequencer 'sequencer2' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer2',
                sequencerId = SEQ::sequencer2::12203a55a279...,
                endpoints = http://127.0.0.1:30145
              ),
              Sequencer 'sequencer3' -> GrpcSequencerConnection(
                sequencerAlias = Sequencer 'sequencer3',
                endpoints = https://127.0.0.1:30147,
                transportSecurity,
                customTrustCertificates
              )
            ),
            sequencer trust threshold = 2,
            sequencer liveness margin = 1,
            submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
            sequencer connection pool delays = SequencerConnectionPoolDelays(
              minRestartDelay = 0.01s,
              maxRestartDelay = 10s,
              warnValidationDelay = 20s,
              subscriptionRequestDelay = 1s
            )
          ),
          manualConnect = false
        ),
        da::1220222f081c6c7d7dd4cba1612b1c80e12e0a7c1eef2139be2d928d903fccf9f090::34-0,
        true
      )
    )
```

7. List the connected Synchronizers to verify that the connection is listed. See inspect connections.

## Inspect connections

You can inspect the connected Synchronizer connections, as well as the configuration of a specific connection.

1. List connected Synchronizer connections. You can get the Synchronizer aliases and Synchronizer IDs of all connected Synchronizers:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.list_connected()
    res17: Seq[ListConnectedSynchronizersResult] = Vector(
      ListConnectedSynchronizersResult(
        synchronizerAlias = Synchronizer 'mysynchronizer',
        physicalSynchronizerId = da::1220222f081c...::35-0,
        healthy = true
      )
    )
```

And you can inspect the configuration of a specific Synchronizer connection using:

2. Inspect the configuration of a specific connection:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.config("mysynchronizer")
    res20: Option[SynchronizerConnectionConfig] = Some(
      value = SynchronizerConnectionConfig(
        synchronizer = Synchronizer 'mysynchronizer',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:32810
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:32812
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              sequencerId = SEQ::sequencer3::122076e8bfb8...,
              endpoints = https://127.0.0.1:32814,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 1,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
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

## Modify

### Update Sequencer trust threshold

You can modify the Sequencer trust threshold to control how many Sequencers must agree before a message is considered valid.

1. Define a valid threshold. Set the threshold value between 1 and the number of connected Sequencers.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.modify("mysynchronizer", _.tryWithSequencerTrustThreshold(1))
```

2. Verify the updated configuration using:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.config("mysynchronizer")
    res22: Option[SynchronizerConnectionConfig] = Some(
      value = SynchronizerConnectionConfig(
        synchronizer = Synchronizer 'mysynchronizer',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:32810
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:32812
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              sequencerId = SEQ::sequencer3::122076e8bfb8...,
              endpoints = https://127.0.0.1:32814,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
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

### \[Specific to the connection pool] Update Sequencer liveness margin

You can modify the Sequencer liveness margin to control the resilience to faulty Sequencers.

1. Update the configuration with the new liveness margin:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.modify("mysynchronizer", _.withSequencerLivenessMargin(0))
```

2. Verify the updated configuration using:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.config("mysynchronizer")
    res22: Option[SynchronizerConnectionConfig] = Some(
      value = SynchronizerConnectionConfig(
        synchronizer = Synchronizer 'mysynchronizer',
        sequencerConnections = SequencerConnections(
          connections = Map(
            Sequencer 'sequencer1' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer1',
              sequencerId = SEQ::sequencer1::1220cb0a22fb...,
              endpoints = http://0.0.0.0:30143
            ),
            Sequencer 'sequencer2' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer2',
              sequencerId = SEQ::sequencer2::12203a55a279...,
              endpoints = http://127.0.0.1:30145
            ),
            Sequencer 'sequencer3' -> GrpcSequencerConnection(
              sequencerAlias = Sequencer 'sequencer3',
              endpoints = https://127.0.0.1:30147,
              transportSecurity,
              customTrustCertificates
            )
          ),
          sequencer trust threshold = 1,
          sequencer liveness margin = 0,
          submission request amplification = SubmissionRequestAmplification(factor = 2, patience = 0s),
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

### Update request amplification

1. Configure submission request amplification. Amplification makes Sequencer clients send eligible submission requests to multiple Sequencers to overcome message loss in faulty Sequencers.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.modify("mysynchronizer", _.withSubmissionRequestAmplification(SubmissionRequestAmplification.NoAmplification))
```

2. Same as above, verify the updated configuration using `config` command.

### Synchronizer priority

When connected to multiple Synchronizers, transaction routing will select the Synchronizer with the highest priority for submitting transactions. You can adjust the priority of a Synchronizer to control which one is preferred for submissions. For more details, refer to the multiple synchronizer documentation

1. Update the priority of the Synchronizer connection.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.modify("mysynchronizer", _.withPriority(0))
```

2. Same as above, verify the updated configuration using `config` command.

### Update a custom TLS trust certificate

Whenever the root of trust changes, the clients need to update the custom root certificate accordingly. To update a custom TLS trust certificate, particularly when using self-signed certificates as the root of trust for a TLS Sequencer connection, follow these steps:

1. Load the root certificate from a file:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val certificate = com.digitalasset.canton.util.BinaryFileUtil.tryReadByteStringFromFile("tls/root-ca.crt")
    certificate : com.google.protobuf.ByteString = <ByteString@7e88e992 size=1960 contents="-----BEGIN CERTIFICATE-----\nMIIFeTCCA2GgAwIBAgI...">
```

2. Create a new connection instance and pass the certificate into this new connection.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val connection = com.digitalasset.canton.sequencing.GrpcSequencerConnection.tryCreate(sequencerUrl, customTrustCertificates = Some(certificate))
    connection : GrpcSequencerConnection = GrpcSequencerConnection(
      sequencerAlias = Sequencer 'DefaultSequencer',
      endpoints = https://127.0.0.1:30147,
      transportSecurity,
      customTrustCertificates
    )
```

3. Update the Sequencer connection settings on the Participant Node:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.modify("mysynchronizer", _.copy(sequencerConnections=SequencerConnections.single(connection)))
```

For Mediators, update the certificate settings using a similar approach.

## Disconnect and reconnect

1. Disconnect from the Synchronizer by using the `disconnect` command with the Synchronizer alias:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.disconnect("mysynchronizer")
```

2. Verify the disconnection:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.list_connected().isEmpty
    res29: Boolean = true
```

3. Reconnect to a specific Synchronizer using the `reconnect` command with the Synchronizer alias:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.reconnect("mysynchronizer")
    res30: Boolean = true
```

4. To reconnect all Synchronizers that are not configured to require a manual connection, use the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participantReference.synchronizers.reconnect_all()
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
