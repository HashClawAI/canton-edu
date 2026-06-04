---
title: "Synchronizer Monitoring"
slug: "global-synchronizer-extension-synchronizers-synchronizer-monitoring"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/extension-synchronizers/synchronizer-monitoring.md"
source_title: "Synchronizer Monitoring"
tags:
  - global-synchronizer
  - extension-synchronizers
  - synchronizer-monitoring
---

# Synchronizer Monitoring

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Synchronizer Monitoring

> Monitor sequencer and mediator health, inspect mediator state, and troubleshoot synchronizer issues

# Check and monitor Sequencer Node health

This page describes how to inspect and understand the current status of a Sequencer Node, and how to continuously monitor it using health checks.

See also the generic guide on How to check the status of a Node and monitor its health.

## Interactively check Node status

Canton console can be used to interactively inspect the state and get information about a running Sequencer Node. Execute the following command against a `sequencer` reference of interest.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequencer.health.status
```

For a Sequencer Node that has never been connected to a Synchronizer, the output looks like this:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res1: NodeStatus[sequencer1.Status] = NotInitialized(active = true, waitingFor = Initialization)
```

For a healthy state expect the Sequencer Node to report a status similar to:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.health.status
    res2: NodeStatus[sequencer1.Status] = Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
    Synchronizer id: da::1220222f081c6c7d7dd4cba1612b1c80e12e0a7c1eef2139be2d928d903fccf9f090::35-0
    Uptime: 7.080586s
    Ports: 
    	public: 33028
    	admin: 33029
    Connected participants: 
    	PAR::participant2::1220a4d7463b...
    	PAR::participant1::12201ff69b1d...
    	PAR::participant3::1220d6908163...
    Connected mediators: None
    Sequencer: SequencerHealthStatus(active = true)
    details-extra: None
    Components: 
    	db-storage : Ok()
    	sequencer : Ok()
    Accepts admin changes: true
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

The components status includes `sequencer` for the Sequencer Node itself, and `db-storage`. The latter not being `Ok()` indicates problems with the database storage backend or connectivity to it.

The status also shows the Synchronizer members connected to the Sequencer Node. These members have an active subscription to the Sequencer Node. They can send new submissions to, and read ordered transactions from the Synchronizer.

## BFT Orderer peer network status

For a BFT (Byzantine Fault Tolerance) Sequencer Node, you can inspect the connection status to the other peers of its BFT peer network.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sequencer1.bft.get_peer_network_status()
    res3: com.digitalasset.canton.synchronizer.sequencer.block.bftordering.admin.SequencerBftAdminData.PeerNetworkStatus = PeerNetworkStatus(
      endpoint statuses = Seq(
        PeerEndpointStatus(
          p2pEndpointId = Id(url = "http://localhost:33030", tls = false),
          health = PeerEndpointHealth(status = Authenticated(sequencerId = SEQ::sequencer3::122076e8bfb8...))
        ),
        PeerEndpointStatus(
          p2pEndpointId = Id(url = "http://localhost:33031", tls = false),
          health = PeerEndpointHealth(status = Authenticated(sequencerId = SEQ::sequencer2::12203a55a279...))
        )
      )
    )
```

## Health check endpoints

To monitor the health of a Sequencer Node with external tools, use the Canton Node health check endpoints.

Enabling the endpoint is described in the generic guide on How to check the status of a Node and monitor its health.

A Sequencer Node exposes a pair of health check endpoints: `readiness` (accepts traffic) and `liveness` (does not require a restart), to be used respectively for load balancing and orchestration with tools like Kubernetes.

The `readiness` endpoint corresponds to the health of `sequencer` (including the BFT Orderer), and the `liveness` endpoint corresponds to the health of `db-storage` component in the status command output described above. This means that a fatal failure of the database connection causes a restart of the Sequencer Node.

## Liveness watchdog

A Sequencer Node can be configured to automatically exit when it becomes unhealthy. The following configuration enables an internal watchdog service that checks the Sequencer Node health every `check-interval` seconds and kills the process after `kill-delay` seconds after the `liveness` reports the Node unhealthy.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
watchdog {
  enabled = true
  check-interval = 15s
  kill-delay = 30s
}
```

Place the above under `canton.sequencers.sequencer.parameters` in the configuration file of the Sequencer Node.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/observe/mediator_health.rst" hash="572f2273" */}

# Check and monitor Mediator Node health

This page describes how to inspect and understand the current status of a Mediator Node, and how to continuously monitor it using health checks.

See also the generic guide on How to check the status of a Node and monitor its health.

## Interactively check Node status

Canton console can be used to interactively inspect the state and get information about a running Mediator Node. Execute the following command against a `mediator` reference of interest.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
mediator.health.status
```

For a Mediator Node that has never been connected to a Synchronizer, the output looks like this:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.status
    res1: NodeStatus[mediator1.Status] = NotInitialized(active = true, waitingFor = Initialization)
```

For a healthy state expect the Mediator Node to report a status similar to:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.health.status
    res2: NodeStatus[mediator1.Status] = Node uid: mediator1::12200929934059da3e012af672ee8a5d26a7e4b3e5084920be298f791f7619843c78
    Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
    Uptime: 0.398993s
    Ports: 
    	admin: 32784
    Active: true
    Components: 
    	db-storage : Ok()
    	sequencer-client : Ok()
    	sequencer-connection-pool : Ok()
    	sequencer-subscription-pool : Ok()
    	internal-sequencer-connection-sequencer1-0 : Ok()
    	subscription-sequencer-connection-sequencer1-0 : Ok()
    Version: 3.6.0-SNAPSHOT
    Protocol version: 35
```

The components status includes `db-storage` for the database storage backend, and `sequencer-client`. The latter not being `Ok()` indicates problems with the Synchronizer connectivity.

The status also shows `Active: true` or `Active: false` for the Mediator Node, which in High Availability (HA) configuration indicates whether this Mediator Node is the active HA replica or not.

## Health check endpoints

To monitor the health of a Mediator Node with external tools, use the Canton Node health check endpoints.

Enabling the endpoint is described in the generic guide on How to check the status of a Node and monitor its health.

A Mediator Node exposes a pair of health check endpoints: `readiness` (accepts traffic) and `liveness` (does not require a restart), to be used respectively for load balancing and orchestration with tools like Kubernetes.

The `readiness` endpoint corresponds to the health of the storage backend of the Mediator, and the `liveness` endpoint corresponds to the health of `sequencer-client` component in the status command output described above. This means that a fatal failure of the Sequencer connection of the Mediator Node requires a restart of the Mediator Node.

## Liveness watchdog

A Mediator Node can be configured to automatically exit when it becomes unhealthy. The following configuration enables an internal watchdog service that checks the Mediator Node health every `check-interval` seconds and kills the process after `kill-delay` seconds after the `liveness` reports the Node unhealthy.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
watchdog {
  enabled = true
  check-interval = 15s
  kill-delay = 30s
}
```

Place the above under `canton.mediators.mediator.parameters` in the configuration file of the Mediator Node.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/observe/mediator_inspection.rst" hash="addb7204" */}

# Mediator inspection

The Mediator inspection provides access to metadata associated with finalized transactions, also known as verdicts, to give insights on the transactions completed on a Synchronizer. This page describes how to obtain the verdicts from the admin console.

## Obtain verdicts from the mediator

Use the `verdicts` admin command to inspect verdicts:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.canton.data.CantonTimestamp
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ mediator1.inspection.verdicts(fromRecordTimeOfRequestExclusive = CantonTimestamp.MinValue, maxItems = 1)
    res2: Seq[com.digitalasset.canton.mediator.admin.v30.Verdict] = List(
      Verdict(
        submittingParties = Vector(
          "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
        ),
        submittingParticipantUid = "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c",
        verdict = VERDICT_RESULT_ACCEPTED,
        finalizationTime = Some(
          value = Timestamp(
            seconds = 1777916965L,
            nanos = 327154000,
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        recordTime = Some(
          value = Timestamp(
            seconds = 1777916964L,
            nanos = 63195000,
            unknownFields = UnknownFieldSet(fields = Map())
          )
        ),
        mediatorGroup = 0,
        views = TransactionViews(
          value = TransactionViews(
            views = Map(
              0 -> TransactionView(
                informees = Vector(
                  "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                ),
                confirmingParties = Vector(
                  Quorum(
                    parties = Vector(
                      "participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                    ),
                    threshold = 1
                  )
                ),
                subViews = Vector(),
                viewHash = <ByteString@2c4c9a07 size=34 contents="\022 \312\320Fj\310\233\372\000\b\314\036\034C\300\006\311\215\363\227\343j\210\317\350\254}6\"\2639\362\300">
              )
            ),
            rootViews = Vector(0)
          )
        ),
        updateId = "12200320c85e320ef71daaca64b8ee8c00e79b0a2a0278f9fe5c5737df35af511cba"
      )
    )
```

The command requires a starting record time (exclusive) and a maximum number of verdicts to list. `CantonTimestamp.MinValue` can be used to obtain all verdicts from the beginning.

The output is a list of verdicts. Each verdict contains, among others, its result (accepted, rejected, unspecified), a submitting participant, submitting parties, a finalization time, a record time of the corresponding confirmation request, and metadata of transaction views.

{/* TODO: Link the Admin API Protobuf reference docs once available. https://github.com/DACH-NY/canton/issues/26126 */}

For more details on the `verdicts` admin command, check the reference documentation.

To learn more about related concepts, see the Mediator overview.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/synchronizer/howtos/troubleshoot/index.rst" hash="44a81d5c" */}

Link to participant docs for general troubleshooting guidelines.

# Synchronizer Troubleshooting

## Sequencer subscriptions fail for newly onboarded sequencers

Newly onboarded Sequencers only serve events more recent than the "onboarding snapshot" taken during the onboarding. In addition, some events may belong to transactions initiated before a Sequencer was onboarded, but the Sequencer is not in a position to sign such events and replaces them with "tombstones". If a participant (or mediator) connects to a newly onboarded Sequencer too soon and the subscription encounters a tombstone, the Sequencer subscription aborts with a `FAILED_PRECONDITION` error specifying `InvalidCounter` or `SEQUENCER_TOMBSTONE_ENCOUNTERED`. If this occurs, the participant or mediator should connect to another Sequencer with a longer history of sequenced events before switching to the newly onboarded Sequencer.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
