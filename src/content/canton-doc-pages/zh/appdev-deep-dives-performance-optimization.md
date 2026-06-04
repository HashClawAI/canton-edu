---
title: "性能优化"
slug: "appdev-deep-dives-performance-optimization"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/performance-optimization.md"
source_title: "Performance Optimization"
tags:
  - appdev
  - deep-dives
  - performance-optimization
---

# 性能优化

> 扩展 Canton 应用吞吐量与延迟：网络/节点扩展、争用、ACS、批处理与配置调优。

# 扩展与性能

# Performance Optimization

# Performance Optimization

# Scaling and Performance

## 网络扩展

Canton 系统的扩展与性能特征取决于多种因素 of a Canton-based system are determined by many factors. The simplest approach is to deploy Canton as a simple monolith where vertical scaling would add more CPUs, memory, etc. to the compute resource. However, the most frequent and expected deployment of Canton is as a distributed, micro-service architecture, running in different data centers of different organizations, with many opportunities to incrementally increase throughput. This is outlined below.

The ledger state in Canton does not exist globally so there is no single node that, by design, hosts all contracts. Instead, participant nodes are involved in transactions that operate on the ledger state on a strict need-to-know basis (data minimization), only exchanging (encrypted) information on the synchronizers used as coordination points for the given input contracts. For example, if participants Alice and Bank transact on an i-owe-you contract on synchronizer A, another participant Bob, or another synchronizer B, does not receive a single bit related to this transaction. This is in contrast to blockchains, where each node has to process each block regardless of how active or directly affected they are by a given transaction. This lends itself to a micro-service approach that can scale horizontally.

The micro-services deployment of Canton includes the set of participant nodes (hereafter, "participant" or "participants") and synchronizers, as well as the services internal to the synchronizer (e.g., Topology Manager). In general, each Canton micro-service follows the best practice of having its own local database which increases throughput. Deploying a service to its own compute server increases throughput because of the additional CPU and disk capacity. A vertical scaling approach can be used to increase throughput if a single service becomes a bottleneck, along with the option of horizontal scaling that is discussed next.

An initial Canton deployment can increase its scaling in multiple ways that build on each other. If a single participant node has many parties, then throughput can be increased by migrating parties off to a new, additional participant node (currently supported as a manual early access feature). For example, if 100 parties are performing multi-lateral transactions with each other, then the system can reallocate parties to 10 participants with 10 parties each, or 100 participants with 1 party each. As most of the computation occurs on the participants, a synchronizer can sustain a very substantial load from multiple participants. If the synchronizer were to be a bottleneck then the sequencer(s), topology manager, and mediator can be run on their own compute server which increases the synchronizer throughput. Therefore, new compute servers with additional Canton nodes can be added to the network when needed, allowing the entire system to scale horizontally.

If even more throughput is needed then the multi-synchronizer feature of Canton can be leveraged to increase throughput. In a large and active network where a synchronizer reaches the capacity limit, additional synchronizers can be rolled out, such that the workflows can be sharded over the available synchronizers (early access). This is a standard technique for load balancing where the client application does the load balancing via sharding.

If a single party is a bottleneck then the throughput can be increased by sharding the workflow across multiple parties hosted on separate participants. If a workflow is involving some large operator (i.e. an exchange), then an option would be to shard the operator by creating two operator parties and distribute the workflows evenly over the two operators (eventually hosted on different participants), and by adding some intermediate steps for the few cases where the workflows would span across the two shards.

Some anti-patterns need to be avoided for the maximum scaling opportunity. For example, having almost all of the parties on a single participant is an anti-pattern to be avoided since that participant will be a bottleneck. Similarly, the design of the Daml model has a strong impact on the degree to which sharding is possible. For example, having a Daml application that introduces a synchronization party through which all transactions need to be validated introduces a bottleneck so it is also an anti-pattern to avoid.

The bottom line is that a Canton system can scale out horizontally if commands involve only a small number of participants and synchronizers.

<div className="enterprise-only" />

## 节点扩展

The Daml Enterprise edition of Canton supports the following scaling of nodes:

* The database-backed drivers (Postgres and Oracle) can run in an active-active setup with parallel processing, supporting multiple writer and reader processes. Thus, such nodes can scale horizontally.
* The enterprise participant node processes transactions in parallel (except the process of conflict detection which by definition must be sequential), allowing much higher throughput than the community version. The community version processes each transaction sequentially. Canton processes make use of multiple CPUs and will detect the number of available CPUs automatically. The number of parallel threads can be controlled by setting the JVM properties `scala.concurrent.context.numThreads` to the desired value.

Generally, the performance of Canton nodes is currently storage I/O bound. Therefore, their performance depends on the scaling behavior and throughput performance of the underlying storage layer, which can be a database or a distributed ledger for some drivers. Therefore, appropriately sizing the database is key to achieving the necessary performance.

On a related note: the Daml interpretation is a pure operation, without side-effects. Therefore, the interpretation of each transaction can run in parallel, and only the conflict detection between transactions must run sequentially.

## 性能与容量规划

A Daml workflow can be computationally arbitrarily complex, performing lots of computation (cpu!) or fetching many contracts (io!), and involve different numbers of parties, participants, and synchronizers. Canton nodes store their entire data in the storage layer (database), with additional indexes. Every workflow and topology is different, and therefore, sizing requirements depend on the Daml application that is going to run, and on the resource requirements of the storage layer. Therefore, to obtain sizing estimates you must measure the resource usage of dominant workflows using a representative topology and setup of your use case.

## 批处理

As every transaction comes with an overhead (signatures, symmetric encryption keys, serialization and wrapping into messages for transport, HTTP headers, etc), we recommend designing the applications submitting commands in a way that batches smaller requests together into a single transaction.

Optimal batch sizes depend on the workflow and the topology and need to be determined experimentally.

## 异步提交

In order to achieve the best performance, we suggest that you use asynchronous command submissions. However, please note that the async submission is only partially asynchronous, as the initial command interpretation and transaction building are included in that step, while the transaction validation and result finalization are not. This means that an async submission takes between 50 to 1000 ms, depending on command size and complexity. In the extreme case with a single thread submitting transactions, this would mean that you would only achieve a rate of one command per second.

If you use synchronous command submissions, the system will wait for the entire transaction to complete, which will require even more threads. Also, please note that the synchronous command submission has a default upper limit of 256 in flight commands, which can be reconfigured using

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.ledger-api.command-service.max-commands-in-flight = 256 // default value

```

## 存储估算

A priori storage estimation of a Canton installation is tricky. As explained above, storage usage depends on topology, payload, Daml models used, and what type of storage layer is configured. However, the following example may help you understand the storage usage for your use case:

First, a command submitted through the gRPC Ledger API is sent to the participant as a serialized gRPC request.

This command is first interpreted and translated into a Daml-LF transaction. The interpreted transaction is next translated into a Canton transaction view-decomposition, which is a privacy-preserving representation of the full transaction tree structure. A transaction typically consists of several transaction views; in the worst case, every action node in the transaction tree becomes a separate transaction view. Each view contains the full set of arguments required by that view, including the contract arguments of the input contracts. So the data representation can be multiplied quite a bit. Here, we cannot estimate the resulting size without having a concrete example. For simplicity, let us consider the simple case where a participant is exercising a simple "Transfer" choice on an typical "Iou" contract to a new owner, preserving the other contract arguments. We assume that the old and new owners of the IOU are hosted on the same participant whereas the IOU issuer is hosted on a second participant.

The resulting Canton transaction consists of two views (one for the **Exercise** node of the Transfer choice and one for the **Create** node of the transferred IOU). Both views contain some metadata such as the package and template identifiers, contract keys, stakeholders, and involved participants. The view for the **Exercise** node contains the contract arguments of the input IOU, say of size `Y`. The view for the **Create** node contains the updated contract arguments for the created contract, again of size `Y`. Note that there is no fixed relation between the command size `X` and the size of the input contracts `Y`. Typically `X` only contains the receiver of the transfer, but not the contract arguments that are stored on the ledger.

Then, we observe the following storage usage:

* Two encrypted envelopes with payload `Y` each, one view seed per view, one symmetric key per informee group, two root hashes for each participant and the participant IDs as recipients at the sequencer store, and the informee tree for the mediator (informees and transaction metadata, but no payload), together with the sequencer database indexes.
* Two encrypted envelopes with payload `Y` each and the symmetric keys for the views, in the participant events table of each participant (as both receive the data)
* Decrypted new resulting contract of size `Y` in the private contract store and some status information of that contract on the active contract journal of the sync service.
* The full decrypted transaction with a payload of size `Y` for the created contract, in the sync service linear event log. This transaction does not contain the input contract arguments.
* The full decrypted transaction with `Y` in the indexer events table, excluding input contracts, but including newly divulged input contracts.

If we assume that payloads dominate the storage requirements, we conclude that the storage requirement is given by the payload multiplication due to the view decomposition. In our example, the transaction requires `5\*Y` storage on each participant and `2\*Y` on the sequencer. For the two participants and the sequencer, this makes `12\*Y` in total.

Additionally to this, some indexes have to be built by the database to serve the contracts and events efficiently. The exact estimation of the size usage of such indexes for each database layer is beyond the scope of our documentation.

<Note>
  Please note that we do have plans to remove the storage duplication between the sync service and the indexer. Ideally, will be able to reduce the storage on the participant for this example from `5\*Y` down to \`3\*Y\`: once for the unencrypted created contract and twice for the two encrypted transaction views.
</Note>

Generally, to recover used storage, a participant and a synchronizer can be pruned. Pruning is available on Canton Enterprise through a set of console commands and allows removal of past events and archived contracts based on a timestamp. The storage usage of a Canton deployment can be kept constant by continuously removing obsolete data. Non-repudiation and auditability of the unpruned history are preserved due to the bilateral commitments.

## 配置 Canton 以获得最佳性能

In this section, the findings from internal performance tests are outlined to help you achieve optimal performance for your Canton application.

### System Design / Architecture

We recommend the version of Canton included in the Daml Enterprise edition, which is heavily optimized when compared with the community edition.

Plan your topology such that your Daml parties can be partitioned into independent blocks. That means most of your Daml commands involve parties of a single block only. It is ok if some commands involve parties of several (or all) blocks, as long as this happens only very rarely. In particular, avoid having a single master party that is involved in every command, because that party bottlenecks the system.

If your participants are becoming a bottleneck, add more participant nodes to your system. Make sure that each block runs on its own participant. If your synchronizer(s) are becoming a bottleneck, add more synchronizer nodes and distribute the load evenly over all synchronizers.

Prefer sending big commands with multiple actions (creates / exercises) over sending numerous small commands. Avoid sending unnecessary commands through the gRPC Ledger API. Try to minimize the payload of commands.

Further information can be found in Section `scaling_and_performance`.

### Hardware and Database

Do not run Canton nodes with an in-memory storage or with an H2 storage in production or during performance tests. You may observe very good performance in the beginning, but performance can degrade substantially once the data stores fill up.

Measure memory usage, CPU usage and disk throughput and improve your hardware as needed. For simplicity, it makes sense to start on a single machine. Once the resources of a machine are becoming a bottleneck, distribute your nodes and databases to different machines.

Try to make sure that the latency between a Canton node and its database is very low (ideally in the order of microseconds). The latency between Canton nodes has a much lower impact on throughput than the latency between a Canton node and its database.

Please check the Postgres persistence section for tuning instructions.

### Configuration

In the following, we go through the parameters with known impact on performance.

**Timeouts.** Under high load, you may observe that commands timeout. This will negatively impact throughput, because the commands consume resources without contributing to the number of accepted commands. To avoid this situation increase timeout parameters from the Canton console:

<div className="todo">
  \#22917: Fix broken literalinclude literalinclude:: CANTON/scripts/canton-testing/config/run-synchronizers.canton start-after: user-manual-entry-begin: BumpSynchronizerTimeouts end-before: user-manual-entry-end: BumpSynchronizerTimeouts
</div>

If timeouts keep occurring, change your setup to submit commands at a lower rate. In addition, take the next paragraph on resource limits into account.

<div id="tuning_resource_limits">
  **Tune resource limits at the Canton protocol level.** Resource limits are used to prevent ledger applications from overloading Canton by sending commands at an excessive rate. While resource limits are necessary to protect the system from denial of service attacks in a production environment, they can prevent Canton from achieving maximum throughput. Resource limits at the Canton protocol level can be configured as follows from the Canton console:
</div>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.resources.set_resource_limits(
  ResourceLimits(
    // Allow for submitting at most 200 commands per second
    maxSubmissionRate = Some(200),

    // Limit the number of in-flight requests to 500.
    // A "request" includes every transaction that needs to be validated by participant1:
    // - transactions originating from commands submitted to participant1
    // - transaction originating from commands submitted to different participants.
    // The chosen configuration allows for processing up to 100 requests per second
    // with an average latency of 5 seconds.
    maxInflightValidationRequests = Some(500),

    // Allow submission bursts of up to `factor * maxSubmissionRate`
    maxSubmissionBurstFactor = 0.5,
  )
)
```

As a rule of thumb, configure `maxDirtyRequests` to be slightly larger than `throughput * latency`, where

* `throughput` is the number of requests per second Canton needs to handle and
* `latency` is the time taken to process a single request while Canton is receiving requests at rate `throughput`.

You should run performance tests to ensure that `throughput` and `latency` are actually realistic. Otherwise, an application may overload Canton by submitting more requests than Canton can handle.

Configure the `maxRate` parameter to be slightly higher than the expected maximal `throughput`.

If you need to support command bursts, configure the `maxBurstFactor` accordingly. Then, the `maxRate` limitation will only start to enforce the rate after having received the initial burst of `maxBurstFactor * maxRate`.

To find optimal resource limits you need to run performance tests. The `maxDirtyRequest` parameter will protect Canton from being overloaded, if requests are arriving at a constant rate. The `maxRate` parameter offers additional protection, if requests are arriving at a variable rate.

If you choose higher resource limits, you may observe a higher throughput, at the risk of a higher latency. In the extreme case however, latency grows so much that commands will timeout; as a result, the command processing consumes resources even though some commands are not committed to the ledger.

If you choose lower resource limits, you may observe a lower latency, at the cost of lower throughput and commands getting rejected with the error code `PARTICIPANT_BACKPRESSURE`.

<div id="tuning_ledger_api_limits">
  **Tune resource limits at the gRPC Ledger API level.** Resource limits can also be imposed on the gRPC Ledger API level. As these settings are applied closer to the ledger applications, they can be used for protecting the resources of individual participants rather than the entire Canton system.
</div>

You can modify the following configuration options:

```
canton.participants.<participant-name>.ledger-api.rate-limit {
  max-streams = 333
  max-api-services-queue-size = 444
  max-api-services-index-db-queue-size = 555
  max-used-heap-space-percentage = 66
  min-free-heap-space-bytes = 7777777
}
```

You can cap the number of gRPC Ledger API streams open at any given time by modifying the `max-streams` parameter. When the number of simultaneously open transaction, transaction-tree, completion, or acs streams reaches the maximum, it doesn't accept any additional get stream requests and returns a `MAXIMUM_NUMBER_OF_STREAMS` error code instead.

You can cap the number of items pending in the thread pools serving the Ledger API and the index database read requests by modifying the `max-api-services-queue-size` and `max-api-services-index-db-queue-size` respectively. When the CPU worker thread pool or the database communication thread pool is overloaded, the server responds with a `THREADPOOL_OVERLOADED` error code.

You can cap the percentage of the memory heap used by changing the `max-used-heap-space-percentage` parameter. If this percentage is exceeded following a garbage collection of the `tenured` memory pool, the system is rate-limited until additional space is freed up.

Similarly, you can set the minimum heap space in absolute terms by changing the `min-free-heap-space-bytes` parameter. If the amount of free space is below this value following a garbage collection of the `tenured` memory pool, the system is rate-limited until additional space is freed up. When the maximum memory thresholds are exceeded the server responds to gRPC Ledger API requests with a `HEAP_MEMORY_OVER_LIMIT` error code.

The following configuration values are the defaults:

```
max-streams = 1000
max-api-services-queue-size = 10000
max-api-services-index-db-queue-size = 1000
max-used-heap-space-percentage = 100
min-free-heap-space-bytes = 0
```

The memory-related settings of 100 for `max-used-heap-space-percentage` and 0 for `min-free-heap-space-bytes` render them effectively inactive. This is done on purpose. They are highly sensitive to the operating environment and should only be configured where memory profiling has highlighted spikes in memory usage that need to be flattened.

It is possible to turn off rate limiting at the gRPC Ledger API level:

```
canton.participants.<participant-name>.ledger-api {
  rate-limit = null
}
```

<div id="tuning_stream_api_limits">
  **Number of Open Streams**: Similarly to the Ledger API, the number of open streams on the Admin API and the Sequencer API can be configured using the `limits.active` section of the configuration:
</div>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.sequencers.sequencer.public-api.limits.active = {
  "com.digitalasset.canton.sequencer.api.v30.SequencerService/DownloadTopologyStateForInit" : 10,
  "com.digitalasset.canton.sequencer.api.v30.SequencerService/Subscribe" : 1000,
}
```

<div id="size_of_connection_pools">
  **Size of connection pools.** Make sure that every node uses a connection pool to communicate with the database. This avoids the extra cost of creating a new connection on every database query. Canton chooses a suitable connection pool by default, but for performance sensitive applications you may want to optimize. Configure the maximum number of connections such that the database is fully loaded, but not overloaded. Allocating too many database connections will lead to resource waste (each thread costs), context switching and contention on the database system, slowing the overall system down. If this occurs, the query latencies reported by Canton go up (check the troubleshooting guide).
</div>

Detailed instructions on handling this issue can also be found in `max_connection_settings`.

**Size of database task queue.** If you are seeing frequent `RejectedExecutionExceptions` when Canton queries the database, increase the size of the task queue, as described in `database_task_queue_full`. The rejection is otherwise harmless. It just points out that the database is overloaded.

**Database Latency.** Ensure that the database latency is low. The higher the database latency, the lower the actual bandwidth and the lower the throughput of the system.

**Throttling configuration for SequencerClient.** The `SequencerClient` is the component responsible for managing the connection of any member (participant, mediator, or topology manager) in a Canton network to the synchronizer. Each synchronizer can have multiple sequencers, and the `SequencerClient` connects to one of them. However, there is a possibility that the `SequencerClient` can become overwhelmed and struggle to keep up with the incoming messages. To address this issue, a configuration parameter called `maximum-in-flight-event-batches` is available:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.sequencer-client.maximum-in-flight-event-batches = 100
  canton.mediators.mediator1.sequencer-client.maximum-in-flight-event-batches = 100
  canton.sequencers.sequencer1.sequencer-client.maximum-in-flight-event-batches = 100
  canton.monitoring.metrics.qualifiers = [debug, traffic, errors, saturation, latency]

```

By setting the `maximum-in-flight-event-batches` parameter, you can control the maximum number of event batches that the system processes concurrently. This configuration helps prevent overload and ensures that the system can handle the workload effectively.

It's important to note that the value you choose for `maximum-in-flight-event-batches` impacts the `SequencerClient`'s performance in several ways. A higher value can potentially increase the `SequencerClient`'s throughput, allowing it to handle more events simultaneously. However, this comes at the cost of higher memory consumption and longer processing times for each batch.

On the other hand, a lower value for `maximum-in-flight-event-batches` might limit the throughput, as it can process fewer events concurrently. However, this approach can result in more stable and predictable `SequencerClient` behavior.

To monitor the performance of the `SequencerClient` and ensure it is operating within the desired limits, you can observe the metric `sequencer-client.handler.actual-in-flight-event-batches`. This metric provides the current value of the in-flight event batches, indicating how close it is to the configured limit. Additionally, you can also reference the metric `sequencer-client.handler.max-in-flight-event-batches` to determine the configured maximum value.

By monitoring these metrics, you can gain insights into the actual workload being processed and assess whether it is approaching the specified limit. This information is valuable for maintaining optimal `SequencerClient` performance and preventing any potential bottlenecks or overload situations.

**Turn on High-Throughput Sequencer.** The database sequencer has a number of parameters that can be tuned. The trade-off is low-latency or high-throughput. In the low-latency setting, every submission will be immediately processed as a single item. In the high-throughput setting, the sequencer will accumulate a few events before writing them together at once. While the latency added is only a few ms, it does make a difference during development and testing of your Daml applications. Therefore, the default setting is `low-latency`. A production deployment with high throughput demand should choose the `high-throughput` setting by configuring:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// example setting for synchronizers nodes. database sequencer nodes have the exact same settings.
canton.sequencers.sequencer1.sequencer {
    type = BFT
    block {
        writer = {
            // choose between high-throughput or low-latency
            type = high-throughput
        }
    }
}
```

There are additional parameters that can in theory be fine-tuned, but we recommend to leave the defaults and use either high-throughput or low-latency. In our experience, a high-throughput sequencer can handle several thousand submissions per second.

**JVM heap size.** In case you observe `OutOfMemoryErrors` or high overhead of garbage collection, you must increase the heap size of the JVM, as described in Section `jvm_arguments`. Use tools of your JVM provider (such as VisualVM) to monitor the garbage collector to check whether the heap size is tight.

**Size of thread pools.** Every Canton process has a thread pool for executing internal tasks. By default, the size of the thread-pool is configured as the number of (virtual) cores of the underlying (physical) machine. If the underlying machine runs other processes (e.g., a database) or if Canton runs inside of a container, the thread-pool may be too big, resulting in excessive context switching. To avoid that, configure the size of the thread pool explicitly like this:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"bin/canton -Dscala.concurrent.context.numThreads=12 --config examples/01-simple-topology/simple-topology.conf"
```

As a result, Canton will log the following line:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
"INFO  c.d.canton.environment.Environment - Deriving 12 as number of threads from '-Dscala.concurrent.context.numThreads'."
```

**Asynchronous commits.** If you are using a Postgres database, configure the Participant's Ledger API server to commit database transactions asynchronously by including the following line into your Canton configuration:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.ledger-api.postgres-data-source.synchronous-commit = off
```

**Logging Settings.** Make sure that Canton outputs log messages only at level INFO and above and turn off immediate log flushing using the `--log-immediate-flush=false` commandline flag, at the risk of missing log entries during a host system crash.

**Replication.** If (and **only if**) using single nodes for participant, sequencer, and/or mediator, replication can be turned off by setting `replication.enabled = false` in their respective configuration.

<Warning>
  While replication can be turned off to try to obtain performance gains, it must **not** be disabled when running multiple nodes for HA.
</Warning>

<div id="caching_configuration">
  **Caching Configuration.** In some cases, you might also want to tune caching configurations and either reduce or increase them, depending on your situation. This can also be helpful if you need to reduce the memory foot-print of Canton, which can be large, as the default cache configurations are tailored for high-throughput, high-memory and small transaction sizes.
</div>

Generally, the caches that usually matter with respect to size are the contract caches and the in-memory fan-out event buffer. You can tune these using the following configurations. The values depicted here are the ones recommended for smaller memory-footprints and are therefore also helpful if you run into out-of-memory issues:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1 {
      // tune caching configs of the ledger api server
      ledger-api {
          index-service {
              max-contract-state-cache-size = 1000 // default 1e4
              max-contract-key-state-cache-size = 1000 // default 1e4

              // The in-memory fan-out will serve the transaction streams from memory as they are finalized, rather than
              // using the database. Therefore, you should choose this buffer to be large enough such that the likeliness of
              // applications having to stream transactions from the database is low. Generally, having a 10s buffer is
              // sensible. Therefore, if you expect e.g. a throughput of 20 tx/s, then setting this number to 200 is sensible.
              // The default setting assumes 100 tx/s.
              max-transactions-in-memory-fan-out-buffer-size = 200 // default 1000
          }
      }
      // tune the synchronisation protocols contract store cache
      parameters.caching {
          contract-store {
              maximum-size = 1000 // default 1e6
              expire-after-access = 120s // default 10 minutes
          }
      }
  }

```

## 模型 Tuning

How you write your Daml model has a large impact on the performance of your system. There are instances of good models running with 3000 ledger events/second (v2.7) on a single participant node. A bad model will reach a fraction of that. Therefore, it is important to understand the connection between the model and the performance implications. This section aims to give a few guidelines.

### Reduce the Number of Views

One key performance driver in Canton is the transaction structure resulting from the model. A Daml command is effectively a "program" that computes a transaction structure. This transaction structure is then broken up by Canton into pieces called "transaction views". The transaction views are then encrypted and sent to the participants who then confirm each view. Each view requires cryptography and creates additional payload that needs to be processed and validated.

As a result, the performance of your system directly depends on how many views the transaction creates. The number of views of a transaction is logged on the participant side as a DEBUG log message:

```
Computed transaction tree with total=27 for #root-nodes=8
```

If you submit a Ledger API command (which can have multiple Daml commands), then every Daml command will create one so-called root-node, (two for the `CreateAndExercise` command). Each root node creates one view.

Just putting all Daml commands into a single batch command does not help, as you might still create lots of views.

Currently, Canton creates a view for every action node in the transaction tree if the **participants that host their informees are not a subset of their parent view's informee participants**. A view's informee participants are all the participants that must be informed about the view. Therefore, to reduce the number of views, you should try to reduce either the number of times the set of informees grows or make sure most of your actions share the same pool of participants. Alternatively, you can add informees to the action nodes close to the root (e.g., by including choice observers) so that their children nodes are aggregated in the initial view, since these children nodes target only a subset of those participants.

One concrete way to reduce the number of views being generated by a Daml model is to write batch commands and group the operations on the ledger based on their informees' participants. In other words, you can create a single choice and batch all the operations that share the same informee participant group.

You can also reduce the number of views being generated for the children of a node (i.e., parent-child views) when creating your Daml model. With the below example as reference, instead of sending a batch with 20 exercise commands `Foo`, you can group your contracts by a set of stakeholders that cover the exercise's informee participants and send one exercise command on a generator contract with the list of contracts that in turn exercises the Foo choice per stakeholder group. This way you can perform these operations in a single view, instead of having them spawn multiple different views.

For example, if the `doUpdate` below is called from a choice visible to the `owner` party alone, then whether the `efficient` flag is set or not has a huge impact on the number of views created. In the choice `Foo` of the `Example` contract, even though the participants to be informed are a subset of the contract's informee participants they are not merged into a single view if this choice is called independently each time. On the contrary, you will produce multiple root actions each belonging to their own view. Finally, aligning the choice observer of `Run` to its template contract means that either the choice observer is the same in each case or the new observer is hosted by any of the contract's informee participants.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
doUpdate : Bool -> Party -> Party -> [ContractId Example] -> Update ()

doUpdate efficient owner obs batch = do
  if efficient then do
    batcher <- create BatchFoo with owner
    -- This only works out if obs is the same observer on all the exercised Example contracts
    batcher `exercise` Run with batch = batch; obs = obs
  else do
    -- Canton will create one view per exercise
    forA_ batch (`exercise` Foo)
  pure ()

template Example with
    owner : Party
    obs: Party
  where
    signatory owner
    observer obs

    choice Foo : ()
      controller owner
      do
        return ()

template BatchFoo with
    owner : Party
  where
    signatory owner

    choice Run : () with
        batch : [ContractId Example]
        obs : Party
      -- The observer here is a choice observer. Therefore, Canton will
      -- ship a single view with the top node of this choice if the observer of the
      -- choice aligns with the observer of the contract.
      observer obs
      controller owner
      do
        forA_ batch (`exercise` Foo)
```

As a rule, the number of views should depend on the number of groups of informee participants you have in your batch choice, not the number of "batches" you process in parallel within one command. An informee's participants group is formed by aggregating the participants that host each stakeholder, or in other words, the set of participants that need to see a particular view.

The informees for the different type of transaction tree nodes are (also see `da-model-projections`):

* create: signatories, observers
* consuming exercise: signatories, observers, stakeholders of the choice (controller, choice observers)
* nonconsuming exercise: signatories, stakeholders of the choice (controller, choice observers), but not the observers of the contract
* fetch: signatories + actors of the fetch, which are all stakholders which are in the authorization context that the fetch executed in
* lookupByKey: only key maintainers

### Reduce Ledger Events

The best optimisation is always to just not do something. A ledger is meant to store relevant data and coordinate different parties. If you use the ledger as processing queue, you run into performance issues, as each transaction view is cryptographically secured and processed extensively to ensure privacy and integrity, which is unnecessary for intermediate steps. The rule is: if the output of a transaction submitted by a party is immediately consumed by the same party, then you are using the ledger as a processing queue. Instead, restructure your command such that the two steps happen as one.

Furthermore, each `create` creates a contract, causing data to be written to the ledger. Each `fetch` causes the interpreter to halt interpretation, asking the ledger for a contract, which in the worst case requires a lookup in the database. As the interpretation must happen sequentially, this means a one-by-one lookup of contracts, causing load and latency. Fetching data is important and a key feature, but you should apply the same reasoning as you would for a database: A database lookup is expensive and should only be done if necessary, ideally caching repetive computing results.

As an example, if you have a high throughput process that always resolves some data by a chain `A -\> B -\> C -\> D` (four fetches), then change your model to use a single cache contract `ABCD`, only fetch that contract and ensure that there is a process that whenever one of the contracts changes, `ABCD` is updated.

Also, avoid unnecessary transient contracts, as they may cause additional views. `createAndExercise` is not a single command, but translated to one create and an exercise. Use a `nonconsuming` choice instead, possibly with a choice observer if you need to leave a trace on the ledger for audit purposes.

Generally, using `lookupKey` is also discouraged. If you use `lookupByKey` for on-ledger deduplication, the lookup requires a database lookup, as the lookupByKey will resolve to `None` in most cases. Instead, use command deduplication on the Ledger API. Second, the current `lookupByKey` will not be supported in a multi-synchronizer deployment, as the current semantic only works on a single-synchronizer deployment and can not be translated 1:1 to multi-synchronizer.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/optimise/latency-and-throughput.rst" hash="bcca0bd1" */}

# Managing Latency and Throughput

## 问题定义

Latency is a measure of how long a business transaction takes to complete. Throughput measures, on average, the number of business transactions possible per second while taking into account any lower or upper bounds which may point to bottlenecks. Defense against latency and throughput issues can be written into the Daml application during design.

First we need to identify the potential bottlenecks in a Daml application. We can do this by analyzing the sync-domain-specific transactions.

Each Daml business transaction kicks off when a Ledger API client sends the commands `create` or `exercise` to a participant.

<Warning>
  * Ledger transactions are not synonymous with business transactions.
  * Often a complete business transaction spans multiple workflow steps and thus multiple ledger transactions.
  * Multiple business transactions can be processed in a single ledger transaction through batching.
  * Expected ledger transaction latencies are on the order of 0.5-1 seconds on database sequencers, and multiple seconds on blockchain sequencers.
</Warning>

Refer to the Daml execution model :ref: that describes a ledger transaction processed by the Canton ledger. The table below highlights potential resource-intensive activities at each step.

<table>
  <colgroup>
    <col style={{width: "10%"}} />

    <col style={{width: "25%"}} />

    <col style={{width: "35%"}} />

    <col style={{width: "30%"}} />
  </colgroup>

  <thead>
    <tr className="header">
      <th>Step</th>
      <th>Participant</th>
      <th>Resources used</th>
      <th>Possible bottleneck drivers</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td>Interpretation</td>

      <td>
        <ul>
          <li>Submitting participant node</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>CPU</li>
          <li>Memory</li>
          <li>DB read access</li>
        </ol>
      </td>

      <td>
        <ol>
          <li>Calculation complexity</li>
          <li>Size and number of variables</li>
          <li>Number of contract fetches</li>
        </ol>
      </td>
    </tr>

    <tr className="even">
      <td>Blinding</td>

      <td>
        <ul>
          <li>Submitting participant node</li>
        </ul>
      </td>

      <td>
        <ul>
          <li>CPU/memory</li>
        </ul>
      </td>

      <td>
        <ul>
          <li>Number and size of views</li>
        </ul>
      </td>
    </tr>

    <tr className="odd">
      <td>Submission</td>

      <td>
        <ul>
          <li>Submitting participant node</li>
          <li>Sequencer</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>CPU</li>
          <li>Memory</li>
        </ol>
      </td>

      <td>
        <ol>
          <li>Serialization/deserialization</li>
          <li>Transaction size/number of views</li>
        </ol>
      </td>
    </tr>

    <tr className="even">
      <td>Sequencing</td>

      <td>
        <ul>
          <li>Sequencer</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>Backend storage</li>
          <li>Network bandwidth</li>
        </ol>
      </td>

      <td>
        <ol>
          <li>Transaction size</li>
          <li>Transaction size/number of views</li>
        </ol>
      </td>
    </tr>

    <tr className="odd">
      <td>Validation</td>

      <td>
        <ul>
          <li>Receiving participant nodes</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>Network bandwidth</li>
          <li>CPU</li>
          <li>Memory</li>
          <li>DB read throughput</li>
        </ol>
      </td>

      <td>
        <ol>
          <li>Transaction size -> download, deserialization, storage costs</li>
          <li>Computation complexity</li>
          <li>Number of contract fetch reads</li>
          <li>Number and size of variables</li>
        </ol>
      </td>
    </tr>

    <tr className="even">
      <td>Confirmation</td>

      <td>
        <ul>
          <li>Validating participant nodes</li>
          <li>Sequencer</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>Network bandwidth</li>
          <li>Sequencer network</li>
          <li>Backend write throughput</li>
        </ol>
      </td>

      <td>
        <ul>
          <li>Number of confirming parties</li>
        </ul>
      </td>
    </tr>

    <tr className="odd">
      <td>Mediation</td>

      <td>
        <ul>
          <li>Mediator nodes</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>Network throughput</li>
          <li>CPU</li>
          <li>Memory</li>
        </ol>
      </td>

      <td>
        <ul>
          <li>Number of confirming parties</li>
        </ul>
      </td>
    </tr>

    <tr className="even">
      <td>Commit</td>

      <td>
        <ul>
          <li>Mediator nodes</li>
          <li>Sequencer</li>
        </ul>
      </td>

      <td>
        <ol>
          <li>CPU</li>
          <li>Memory</li>
          <li>DB</li>
          <li>Network bandwidth</li>
        </ol>
      </td>

      <td>
        <ul>
          <li>Number of confirming parties</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Possible Throughput Bottlenecks in Order of Likelihood

1. Transaction size causing high serialization/deserialization and encryption/decryption costs on participant nodes.
2. Transaction size causing sequencer backend overload, especially on blockchains.
3. High interpretation and validation cost due to calculation complexity or memory use.
4. Large number of involved nodes and associated network bandwidth on sequencer.

Latency can also be affected by the above factors. However, baseline latency usually has more to do with system set-up issues (DB or blockchain latency) rather than Daml modeling problems.

### Solutions

1. **Minimize transaction size.**

Each of the following actions in Daml adds a node to the transaction containing the payload of the contract being acted on. A large number of such operations, and/or operations of this kind on large contracts, are the most common cause of performance bottlenecks.

> * `create`
> * `fetch`
> * `fetchByKey`
> * `lookupByKey`
> * `exercise`
> * `exerciseByKey`
> * `archive`

Use the above actions sparingly. For example, if contracts have intermediary states within a transaction, you can often skip them by writing only the end state. For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Incrementor
with
p : Party
n : Int
where
signatory p

choice Increment : ContractId Incrementor
    controller p
    do create this with n = n+1

-- This adds all m-1 intermediary versions of
-- the contract to the transaction tree
choice BadIncrementMany : ContractId Incrementor
    with m : Int
    controller p
    do foldlA (\self' _ -> exercise self' Increment) self [1..m]

-- This only adds the end result to the transaction
choice GoodIncrementMany : ContractId Incrementor
    with m : Int
    controller p
    do create this with n = n+m
```

When you need to read a contract, or act on a single contract in multiple ways, you can often bundle those operations into a single action. For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Asset
with
issuer : Party
owner : Party
quantity : Decimal
where
signatory [issuer, owner]

-- BadMerge acts on each of the otherCids three times:
-- Once for validation
-- Once to extract the quantities
-- Once to archive
choice BadMerge : ContractId Asset
 with otherCids : [ContractId Asset]
 controller owner
 do
   -- validate the cids.
   forA_ otherCids (\cid -> do
     other <- fetch cid
     assert (other.issuer == issuer && other.owner == owner))

   -- extract the quantities
   quantities <- forA otherCids (\cid -> do
     other <- fetch cid
     return other.quantity)

   -- archive the others
   forA_ otherCids archive

   create this with quantity = quantity + sum quantities

-- Allow us to do a fetch and an archive in one action
choice ConsumingFetch : Asset
 controller owner
 do return this

-- GoodMerge only acts on each of the other assets once.
choice GoodMerge : ContractId Asset
 with otherCids : [ContractId Asset]
 controller owner
 do
   -- Get and archive the others
   others <- forA otherCids (`exercise` ConsumingFetch)

   -- validate
   forA_ others (\other -> do
     assert (other.issuer == issuer && other.owner == owner))

   -- extract the quantities
   let quantities = map (.quantity) others

   create this with quantity = quantity + sum quantities
```

Separate templates for large payloads that change rarely and require minimum access from those for fields that change with almost every action. This optimizes resource consumption for multiple business transactions.

This batching approach makes updates in one transaction submission rather than requiring separate transactions for each update. Note: this option can cause a small increase in latency and may increase the possibility of command failure but this can be avoided. For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template T
with
p : Party
where
signatory p

choice Foo : ()
    controller p
    do return ()

batching : Script ()
batching = do
p <- allocateParty "p"

-- without batching we have 10 ledger
-- transactions.
cid1 <- submit p do createCmd T with ..
cid2 <- submit p do createCmd T with ..
cid3 <- submit p do createCmd T with ..
cid4 <- submit p do createCmd T with ..
cid5 <- submit p do createCmd T with ..

submit p do exerciseCmd cid1 Foo
submit p do exerciseCmd cid2 Foo
submit p do exerciseCmd cid3 Foo
submit p do exerciseCmd cid4 Foo
submit p do exerciseCmd cid5 Foo

-- With batching, there are only two ledger transactions.
cids <- submit p do
replicateA 5 $ createCmd T with ..
submit p do
forA_ cids (`exerciseCmd` Foo)
```

2. CPU and memory issues: Use the Daml profiler to analyze Daml code execution.
3. Once you feel interpretation is not the bottleneck, scale up your machine.

<Tip>
  Profile the JVM and monitor your databases to see where the bottlenecks occur.
</Tip>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/optimise/active-contract-set.rst" hash="d8f44824" */}

# Managing Active Contract Set (ACS) Size

## 问题定义

The Active Contract Set (ACS) size makes up the load related to the number of active contracts in the system at any one time. It means the totality of all the contracts that have been created but not yet archived. ACS size may come from a deliberate Daml workflow design, but the size may also be unexpected when insufficient care is given to supporting and auxiliary contract lifetimes.

<Tip>
  See the documentation on Daml contracts for more information.
</Tip>

When the ACS size is in the high 100s GBs or TBs, local database access performance may deteriorate. We will look at potential issues around large ACS size and possible solutions.

## 关系型数据库

Large ACS can have a negative impact on many aspects of system performance in relational databases. The following points focus on PostgreSQL as the underlying database; the details differ in the case of Oracle but the results are similar.

* Large ACS size directly affects the resource consumption and performance of a Ledger API client application dealing with a large data set that may not fit into the memory or the application database.
* ACS size directly affects the speed at which the ACS can be transmitted from the Ledger API server using the StateService. In extreme cases, it could take hours to transfer the complete set requested by the application due to the limits imposed by the gRPC channel capacity and the speed of storage queries.
* Increased latency is a less direct impact which shows up wherever a query is issued to the database index to make progress. Large ACS size means that the corresponding indices are also large, and at a certain point they will no longer fit into the shared-buffer space. It then takes increasingly longer for the database engine to produce query results. This affects activities such as contract lookups during the command submission, transaction tree streaming, or pointwise transaction lookups.
* Large ACS size may affect the speed at which the database underpinning the participant ingests new transactions. Normally, as new updates pour in the write-ahead log commits the table and index changes immediately. Those updates come in two shapes; full-page writes or differential writes. With large volumes, many are full-page writes.
* Finally, many dirty pages also translate into prolonged and expensive flushes to the disk as part of the checkpointing process.

### Solutions

* Pay attention to the lifetime of the contracts. Make sure that the supporting and auxiliary contracts don’t clutter the ACS and archive them as soon as it is practical to do so.

* Set up a frequent pruning schedule. Be aware that pruning is only effective if there are archived contracts available for pruning. If all contracts are still active, pruning has limited success. Refer to our [pruning documentation](/zh/docs/canton/overview-reference-pruning) for more information.

* Implement an ODS in your ledger client application to limit reliance on read access to the ACS. Do this whenever you notice that the time to initialize the application from the ACS exceeds your pain level.

* Monitor database performance.
  * Monitor the disk read and write activity. Look for sudden changes in the operation patterns. For instance, a sudden increase in the disk’s read activity may be a sign of indices no longer fitting into the shared buffers.
  * Observe the performance of the database queries. Check our [monitoring documentation](/zh/docs/canton/global-synchronizer-extension-synchronizers-synchronizer-monitoring) for query [metrics](/zh/docs/canton/global-synchronizer-reference-canton-metrics#daml-sequencer-db-storage-write-executor-waittime) that can assist. You may also consider setting up a [log\_min\_duration\_statement parameter](https://www.postgresql.org/docs/current/runtime-config-logging.html#GUC-LOG-MIN-DURATION-STATEMENT) in the PostgreSQL configuration.

* Set up [autovacuum](https://www.postgresql.org/docs/current/routine-vacuuming.html#AUTOVACUUM) on the PostgreSQL database. Note that, after pruning, a lot of dead tuples will need removing.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/optimise/contention-avoiding.rst" hash="9368bace" */}

# Avoid Contention Issues

Measuring the performance of business applications involves more than considering the transactions per second and transaction latency of the underlying blockchain and Distributed Ledger Technology (DLT). Blockchains are distributed systems; even the highest-performance blockchains have considerably higher transaction latencies than traditional databases. These factors make the systems prone to contention, which can stifle the performance of applications when not handled appropriately.

It is, unfortunately, easy to design low-performance applications even on a high-performance blockchain system. Applications that initially perform well may fail under pressure. It is better to plan around contention in your application design than to fix issues later. The marginal cost of including extra business logic within a blockchain transaction is often small.

Contention is expected in distributed systems. The aim is to reduce it to acceptable levels and handle it gracefully, not to eliminate it at all costs. If contention only occurs rarely, it may be cheaper for both performance and complexity to simply let the occasional allocation fail and retry, rather than implement an advanced technique to avoid it.

As an added benefit to reducing contention issues, carefully bundling or batching strategic business logic can improve performance by yielding business transaction throughput that far exceeds the blockchain transaction throughput.

## Daml 中的争用

Daml uses an unspent transaction output (UTXO) ledger model. UTXO models enable higher performance by supporting parallel transactions. This means that you can send new transactions while other transactions are still processing. The downside is that contention can occur if a second transaction arrives while a conflicting earlier transaction is still pending.

Daml guarantees that there can only be one consuming choice exercised per contract. If you try to commit two transactions that would consume the same contract, you have write-write contention.

Contention can also result from incomplete or stale knowledge. For example, a contract may have been archived, but a client hasn’t yet been notified due to latencies or a privacy model might prevent the client from ever knowing. If you try to commit two transactions on the same contract where one transaction reads and the other one consumes an input, you run the risk of a read-write contention.

A contract is considered pending when you do not know if the output has been consumed. It is best to assume that your transactions will go through and to treat pending ones as probably consumed. You must also assume that acting on a pending contract will fail.

You need to wait while the sequencer is processing a transaction in order to confirm that an input was consumed from a consuming input request. If you do not get confirmation back from the first transaction before submitting a second transaction on the same contract, the sequence is not guaranteed. The only way to avoid this conflict is to control the sequence of those two transactions.

Ledger state is read in the following places within the Daml Execution Model :

1. A client submits a command based on the client’s latest view of the state of the shared ledger. The command might include references to `ContractIds` that the client believes are active.
2. During interpretation, ledger state is used to look up active contracts.
3. During validation, ledger state is again used to look up contracts and to validate the transaction by reinterpreting it.

Contention can occur both between #1 and #2 and between #2 and #3:

* The client is constructing the command in #1 based on contracts it believes to be active. But by the time the participant performs interpretation in #2, it has processed the commit of another transaction that consumed those contracts. The participant node rejects the command due to contention.
* The participant successfully constructs a transaction in #2 based on contracts it believes to be active. But by the time validation happens in #3, another transaction that consumes the same contracts has already been sequenced. The validating participants reject the command due to contention.

The complete and relevant ledger state at the time of the transaction is known only after sequencing, which happens between #2 and #3. That ledger state takes precedence to ensure double spend protection.

Contention slows performance significantly. While you cannot avoid contention completely, you can design logic to minimize it. The same considerations apply to any UTXO ledger.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/optimise/contention-reducing.rst" hash="bfd45687" */}

# Reduce Contention

Contention is natural and expected when programming within a distributed system like Daml in which every action is asynchronous. It is important to understand the different causes of contention, be able to diagnose the root cause if errors of this type occur, and be able to avoid contention by designing contracts appropriately.

You can use different techniques to manage contention and to improve performance by increasing throughput and decreasing latency. These techniques include the following:

* Add retry logic.
* Run transactions that have causality in series.
* Bundle or batch business logic to increase business transaction throughput.
* Maximize parallelism with techniques such as sharding, while ensuring no contention between shards.
* Split contracts across natural lines to reduce single, high-contention contracts.
* Avoid write-write and write-read contention on contracts. This type of contention occurs when one requester submits a transaction with a consuming exercise on a contract while another requester submits another exercise or a fetch on the same contract. This type of contention cannot be eliminated entirely, since there will always be some latency between a client submitting a command to a participant and other clients learning of the committed transaction. Here are a few scenarios and specific measures you can take to reduce this type of collision:
  * Shard data. Imagine you want to store a user directory on the ledger. At the core, this is of type `[(Text, Party)]`, where `Text` is a display name and `Party` is the associated Party. If you store this entire list on a single contract, any two users wanting to update their display name at the same time will cause a collision. If you instead keep each `(Text, Party)` on a separate contract, these write operations become independent from each other.

    A helpful analogy when structuring your data is to envision that a template defines a table, where a contract is a row in that table. Keeping large pieces of data on a contract is like storing big blobs in a database row. If these blobs can change through different actions, you have write conflicts.

  * Use non-consuming choices, where possible, as they do not collide. Non-consuming choices can be used to model events that have occurred, so instead of creating a short-lived contract to hold some data that needs to be referenced, that data could be recorded as a ledger event using a non-consuming choice.

  * Avoid workflows that encourage multiple parties to simultaneously exercise a consuming choice on the same contract. For example, imagine an auction contract containing a field `highestBid : (Party, Decimal)`. If Alice tries to bid \$100 at the same time that Bob tries to bid \$90, it does not matter that Alice’s bid is higher. The sequencer rejects the second because it has a write collision with the first transaction. It is better to record the bids in separate Bid contracts, which can be updated independently. Think about how you would structure this data in a relational database to avoid data loss due to race conditions.

  * Think carefully about storing `ContractIds`. Imagine that you create a sharded user directory according to the first bullet in this list. Each user has a `User` contract that stores their display name and party. Now assume that you write a chat application, where each `Message` contract refers to the sender by `ContractId` User.

    If a user changes the display name, that reference goes stale. You either have to modify all messages that the user ever sent, or you cannot use the sender contract in Daml.

    Contract keys can be used to make this link inside Daml. If the only place you need to link `Party` to `User` is in the user interface, it might be best to not store contract references in Daml at all.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/sdlc-howtos/applications/optimise/contention-techniques.rst" hash="c49bf0bb" */}

# Example Application with Techniques for Reducing Contention

The example application below illustrates the relationship between blockchain and business application performance, as well as the impact of design choices. Trading, settlement, and related systems are core use cases of blockchain technology, so this example demonstrates different ways of designing such a system within a UTXO ledger model and how the design choices affect application performance.

## The Example Minimal Settlement System

This section defines the requirements that the example application should fulfill, as well as how to measure its performance and where contention might occur. Assume that there are initial processes already in place to issue assets to parties. All of the concrete numbers in the example are realistic order-of-magnitude figures that are for illustrative purposes only.

### Basic functional requirements for the example application

A trading system is a system that allows parties to swap assets. In this example, the parties are Alice and Bob, and the assets are shares and dollars. The basic settlement workflow could be:

1. **Proposal**: Alice offers Bob to swap one share for \$1.
2. **Acceptance**: Bob agrees to the swap.
3. **Settlement**: The swap is settled atomically, meaning that at the same time Alice transfers \$1 to Bob, Bob transfers one share to Alice.

### Practical and security requirements for the example application

The following list adds some practical matters to complete the rough functional requirements of an example minimal trading system.

* Parties can hold *asset positions* of different asset types which they control.
  * An asset position consists of the type, owner, and quantity of the asset.
  * An asset type is usually the combination of an on-ledger issuer and a symbol (such as currency, CUSIP, or ISIN).
* Parties can transfer an asset position (or part of a position) to another party.
* Parties can agree on a settlement consisting of a swap of one position for another.
* Settlement happens atomically.
* There are no double spends.
* It is possible to constrain the *total asset position* of an owner to be non-negative. In other words, it is possible to ensure that settlements are funded. The total asset position is the sum of the quantities of all assets of a given type by that owner.

### Performance measurement in the example application

Performance in the example can be measured by latency and throughput; specifically, settlement latency and settlement throughput. Another important factor in measuring performance is the ledger transaction latency.

* **Settlement latency**: the time it takes from one party wanting to settle (just before the proposal step) to the time that party receives final confirmation that the settlement was committed (after the settlement step). For this example, assume that the best possible path occurs and that parties take zero time to make decisions.

* **Settlement throughput**: the maximum number of settlements per second that the system as a whole can process over a long period.

* **Transaction latency**: the time it takes from when a client application submits a command or transaction to the ledger to the time it receives the commit confirmation. The length of time depends on the command. A transaction settling a batch of 100 settlements will take longer than a transaction settling a single swap. For this example, assume that transaction latency has a simple formula of a fixed cost `fixed_tx` and a variable processing cost of `var_tx` times the number of settlements, as shown here:

  `transaction latency = fixed_tx + (var_tx * #settlements)`

* Note that the example application does not assign any latency cost to settlement proposals and acceptances.

* For the example application, assume that:

  * `fixed_tx = 250ms`
  * `var_tx = 10ms`

To set a baseline performance measure for the example application, consider the simplest possible settlement workflow, consisting of one proposal transaction plus one settlement transaction done back-to-back. The following formula approximates the settlement latency of the simple workflow:

> `(2 * fixed_tx) + var_tx`

`=` `(2 * 250ms) + 10ms`

`=` `510ms`

To find out how many settlements per second are possible if you perform them in series, throughput evaluates to the following formula (there are 1,000ms in one second):

> `1000ms / (fixed_tx + var_tx) settlements per second`

`=` `1000ms / (250ms + 10ms)`

`=` `1000 / 260`

`=` `3.85 or ≈ 4 settlements per second`

These calculations set the optimal baselines for a high performance system.

The next goal is to increase throughput without dramatically increasing latency. Assume that the underlying DLT has limits on total throughput and on transaction size. Use a simple cost model in a unit called `dlt_min_tx` representing the minimum throughput unit in the DLT system. An empty transaction has a fixed cost `dlt_fixed_tx` which is:

> `dlt_fixed_tx = 1 dlt_min_tx`

Assume that the ratio of the marginal throughput cost of a settlement to the throughput cost of a transaction is roughly the same as the ratio of marginal latency to transaction latency (shown previously). A marginal settlement throughput cost `dlt_var_tx` can then be determined by this calculation:

> `dlt_var_tx = ratio * dlt_fixed_tx`

`=` `dlt_var_tx = (var_tx / fixed_tx) * dlt_fixed_tx`

`=` `dlt_var_tx = 10sm/250ms * dlt_fixed_tx`

`=` `dlt_var_tx = 0.04 * dlt_fixed_tx`

and, since from previously

> `dlt_fixed_tx = 1 dlt_min_tx`

then

> `dlt_var_tx = 0.04 * dlt_min_tx`

Even with good parallelism, ledgers have limitations. The limitations might involve CPUs, databases, or networks. Calculate and design for whatever ceiling you hit first. Specifically, there is a maximum throughput `max_throughput` (measured in `dlt_min_tx/second`) and a maximum transaction size `max_transaction` (measured in `dlt_min_tx`). For this example, assume that `max_throughput` is limited by being CPU-bound. Assume that there are 10 CPUs available and that an empty transaction takes 10ms of CPU time. For each second:

> `max_throughput = 10 * each CPU’s capacity`

Each `dlt_min_tx` takes 10ms and there are 1,000 ms in a second. The capacity for each CPU is then 100 `dlt_min_tx` per second. The throughput calculation becomes:

> `max_throughput = 10 * 100 dlt_min_tx/second`

`=` `max_throughput = 1,000 dlt_min_tx/second`

Similarly, `max_transaction` could be limited by message size limit. For this example, assume that the message size limit is 3 MB and that an empty transaction `dlt_min_tx` is 1 MB. So

> `max_transaction = 3 * dlt_min_tx`

One of the three transactions needs to hold an approval with no settlements. That leaves the equivalent of `(2 * dlt_min_tx)` available to hold many settlements in the biggest possible transaction. Using the ratio described earlier, each marginal settlement `dlt_var_tx` takes `0.04 * dlt_min_tx`. So the maximum number of settlements per second is:

> `(2 * dlt_min_tx)/(0.04 * dlt_min_tx)`

`=` `50 settlements/second`

Using the same assumptions, if you process settlements in parallel rather than in series (with only one settlement per transaction), latency stays constant while settlement throughput increases. Earlier, it was noted that a simple workflow can be `(2 * fixed_tx) + var_tx`. In the DLT system, the simple workflow calculation is:

> `(2 * dlt_min_tx) + dlt_var_tx`

`=` `(2 * dlt_min_tx) + (0.04 * dlt_min_tx)`

`=` `2.04 * dlt_min_tx`

It was assumed earlier that max\_throughput is `1,000 dlt_min_tx/second`. So the maximum number of settlements per second possible through parallel processing alone in the example DLT system is:

> `1,000/2.04 settlements per second`

`=` `490.196 or ~490 settlements per second`

These calculations provide a baseline when comparing various techniques that can improve performance. The techniques are described in the following sections.

## Prepare Transactions for Contention-Free Parallelism

This section examines which aspects of UTXO ledger models can be processed in parallel to improve performance. In UTXO ledger models, the state of the system consists of a set of immutable contracts, sometimes also called UTXOs.

Only two things can happen to a contract: it is created and later it is consumed (or spent). Each transaction is a set of input contracts and a set of output contracts, which may overlap. The transaction creates any output contracts that are not also consumed in the same transaction. It also consumes any input contracts, unless they are defined as non-consumed in the smart contract logic.

Other than smart contract logic, the execution model is the same for all UTXO ledger systems:

1. **Interpretation**: the submitting party precalculates the transaction, which consists of input and output contracts.
2. **Submission**: the submitting party submits the transaction to the network.
3. **Sequencing**: the consensus algorithm for the network assigns the transaction a place in the total order of all transactions.
4. **Validation**: the transaction is validated and considered valid if none of the inputs were already spent by a previous transaction.
5. **Commitment**: the transaction is committed.
6. **Response**: the submitting party receives a response that the transaction was committed.

The only step in this process which has a sequential component is sequencing. All other stages of transaction processing are parallelizable, which makes UTXO a good model for high-performance systems. However, the submitting party has a challenge. The interpretation step relies on knowing possible input contracts, which are by definition unspent outputs from a previous transaction. Those outputs only become known in the response step, after a minimum delay of `fixed_tx`.

For example, if a party has a single \$1,000 contract and wants to perform 1,000 settlements of \$1 each, sequencing in parallel for all 1,000 settlements leads to 1,000 transactions, each trying to consume the same contract. Only one succeeds, and all the others fail due to contention. The system could retry the remaining 999 settlements, then the remaining 998, and so on, but this does not lead to a performant system. On the other hand, using the example latency of 260ms per settlement, processing these in series would take 260s or four minutes 20s, instead of the theoretical optimum of one second given by `max_throughput`. The trading party needs a better strategy. Assume that:

> `max_transaction > dlt_fixed_tx + 1,000 * dlt_var_tx = 41 dlt_min_tx`

The trading party could perform all 1,000 settlements in a single transaction that takes:

> `fixed_tx + 1,000 * var_tx = 10.25s`

If the latency limit is too small or this latency is unacceptable, the trading party could perform three steps to split \$1,000 into:

* 10 \* \$100
* 100 \* \$10
* 1,000 \* \$1

and perform the 1,000 settlements in parallel. Latency would then be theoretically around:

> `3 * fixed_tx + (fixed_tx + var_tx) = 1.01s`

However, since the actual settlement starts after 750 ms, and the `max_throughput` is `1,000 dlt_min_tx/s`, it would actually be:

> `0.75s + (1,000 * (dlt_fixed_tx + dlt_var_tx)) / 1,000 dlt_min_tx/s = 1.79s`

These strategies apply to one particular situation with a very static starting state. In a real-world high performance system, your strategy needs to perform with these assumptions:

* There are constant incoming settlement requests, which you have limited ability to predict. Treat this as an infinite stream of random settlements from some distribution and maximize settlement throughput with reasonable latency.
* Not all settlements are successful, due to withdrawals, rejections, and business errors.

To compare between different techniques, assume that the settlement workflow consists of the steps previously illustrated with Alice and Bob:

1. **Proposal**: proposal of the settlement
2. **Acceptance**: acceptance of the settlement
3. **Settlement**: actual settlement

These steps are usually split across two transactions by bundling the acceptance and settlement steps into one transaction. Assume that the first two steps, proposal and acceptance, are contention-free and that all contention is on settlement in the last step. Note that the cost model allocates the entire latency and throughput costs `var_tx` and `dlt_var_tx` to the settlement, so rather than discussing performant trading systems, the concern is for performant settlement systems. The following sections describe some strategies for trading under these assumptions and their tradeoffs.

## Non-UTXO Alternative Ledger Models

As an alternative to a UTXO ledger model, you could use a replicated state machine ledger model, where the calculation of the transaction only happens after the sequencing.

The steps would be:

1. **Submission**: the submitting party submits a command to the network.
2. **Sequencing**: the consensus algorithm of the network assigns the command a place in the total order of all commands.
3. **Validation**: the command is evaluated to a transaction and then validated.
4. **Response**: the submitting party receives a response about the effect of the command.

**Pros**

This technique has a major advantage for the submitting party: no contention. The party pipes the stream of incoming transactions into a stream of commands to the ledger, and the ledger takes care of the rest.

**Cons**

The disadvantage of this approach is that the submitting party cannot predict the effect of the command. This makes systems vulnerable to attacks such as frontrunning and reordering.

In addition, the validation step is difficult to optimize. Command evaluation may still depend on the effects of previous commands, so it is usually done in a single-threaded manner. Transaction evaluation is at least as expensive as transaction validation. Simplifying and assuming that `var_tx` is mostly due to evaluation and validation cost, a single-threaded system would be limited to `1s / var_tx = 100` settlements per second. It could not be scaled further by adding more hardware.

## Simple Strategies for UTXO Ledger Models

To attain high throughput and scalability, UTXO is the best option for a ledger model. However, you need strategies to reduce contention so that you can parallelize settlement processing.

### Batch transactions sequentially

Since `(var_tx << fixed_tx)`, processing two settlements in one transaction is much cheaper than processing them in two transactions. One strategy is to batch transactions and submit one batch at a time in series.

**Pros**

This technique completely removes contention, just as the replicated state machine model does. It is not susceptible to reordering or frontrunning attacks.

**Cons**

As in the replicated state machine technique, each batch is run in a single-threaded manner. However, on top of the evaluation time, there is transaction latency. Assuming a batch size of `N < max_settlements`, the latency is:

> `fixed_tx + N * var_tx`

and transaction throughput is:

> `N / (fixed_tx + N * var_tx)`

As `N` goes up, this tends toward `1 / var_tx = 100`, which is the same as the throughput of replicated state machine ledgers.

In addition, there is the `max_settlements` ceiling. Assuming `max_settlements = 50`, you are limited to a throughput of `50 / 0.75 = 67` settlement transactions per second, with a latency of 750ms. Assuming that the proposal and acceptance steps add another transaction before settlement, the settlement throughput is 67 settlements per second, with a settlement latency of one second. This is better than the original four settlements per second, but far from the 490 settlements per second that is achievable with full parallelism.

Additionally, the success or failure of a whole batch of transactions is tied together. If one transaction fails in any way, all will fail, and the error handling is complex. This can be somewhat mitigated by using features such as Daml exception handling, but contention errors cannot be handled. As long as there is more than one party acting on the system and contention is possible between parties (which is usually the case), batches may fail. The larger the batch is, the more likely it is to fail, and the more costly the failure is.

### Use sequential processing or batching per asset type and owner

In this technique, assume that all contention is within the asset allocation steps. Imagine that there is a single contract on the ledger that takes care of all bookkeeping, as shown in this Daml code snippet:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template AllAssets
  with
    -- A map from owner and type to quantity
    holdings : Map Party (Map AssetType Decimal)
  where
    signatory (keys holdings)
```

This is a typical pattern in replicated state machine ledgers, where contention does not matter. On a UTXO ledger, however, this pattern means that any two operations on assets experience contention. With this representation of assets, you cannot do better than sequential batching. There are many additional issues with this approach, including privacy and contract size.

Since you typically only need to touch one owner’s asset of one type at a time and constraints such as non-negativity are also at that level, assets are usually represented by asset positions in UTXO ledgers, as shown in this Daml code snippet:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template
  with
    assetType : AssetType
    owner : Party
    quantity : Decimal
  where
    signatory assetType.issuer, owner
```

An asset position is a contract containing a triple (owner, asset type, and quantity). The total asset position of an asset type for an owner is the sum of the quantities for all asset positions with that owner and asset type. If the settlement transaction touches two total asset positions for the buy-side and two total asset positions for the sell-side, batching by asset type and owner does not help much.

Imagine that Alice wants to settle USD for EUR with Bob, Bob wants to settle EUR for GBP with Carol, and Carol wants to settle GBP for USD with Alice. The three settlement transactions all experience contention, so you cannot do better than sequential batching.

However, if you could ensure that each transaction only touches one total asset position, you could then apply sequential processing or batching per total asset position. This is always possible to do by decomposing the settlement step into the following:

1. **Buy-side allocation**: the buy-side splits out an asset position from their total asset position and allocates it to the settlement.
2. **Sell-side allocation**: the sell-side splits out an asset position from their total asset position and allocates it to the settlement.
3. **Settlement**: the asset positions change ownership.
4. **Buy-side merge**: the buy-side merges their new position back into the total asset position.
5. **Sell-side merge**: the sell-side merges their new position back into the total asset position.

This does not need to result in five transactions.

* Buy-side allocation is usually done as part of a settlement proposal.
* Sell-side allocation is typically handled as part of the settlement.
* Buy-side merge and sell-side merge technically do not need any action. By definition of total asset positions, merging is an optional step. It is easy to keep things organized without extra transactions. Every time a total asset position is touched as part of buy-side allocation or sell-side allocation above, you merge all positions into a single one. As long as there is a similar amount of inbound and outbound traffic on the total asset position, the number of individual positions stays low.

**Pros**

Assuming that a settlement is considered complete after the settlement step and that you bundle the allocation steps above into the proposal and settlement steps, the system performance will stay at the optimum settlement latency of 510ms.

Also, if there are enough open settlements on distinct total asset positions, the total throughput may reach up to the optimal 490 settlements per second.

With batch sizes of `N=50` for both proposals and settlements and sufficient total asset positions with open settlements, the maximum theoretical settlement throughput is:

`50 stls * 1,000 dlt_min_tx/s / (2 * dlt_fixed_tx + 50 * dlt_var_tx) = 12,500 stls/s`

**Cons**

Without batching, you are limited to the original four outgoing settlements per second, per total asset position. If there are high-traffic assets, such as the USD position of a central counterparty, this can bottleneck the system as a whole.

Using higher batch sizes, you have the same tradeoffs as for sequential batching, except that it is at a total asset position level rather than a global level. Latency also scales exactly as it does for sequential batching.

Using a batch size of 50, you would get settlement latencies of around 1.5s and a maximum throughput per total asset position of 67 settlements per second, per total asset position.

Another disadvantage is that allocating the buy-side asset in a transaction before the settlement means that asset positions can be locked up for short periods.

Additionally, if the settlement fails, the already allocated asset needs to be merged back into the total asset position.

## Shard Asset Positions for UTXO Ledger Models

In systems where peak loads on a single total asset position is in the tens or hundreds of settlements per second, more sophisticated strategies are needed. The total asset positions in question cannot be made up of a single asset position. They need to be sharded.

### Shard total asset positions without global constraints

Consider a total asset position that represents a bookkeeping position without any on-ledger constraints. For example, the trading system may deal with fiat settlement off-ledger, and you simply want to record a balance, whether it is positive or negative. In this situation, you can easily get rid of contention altogether by assigning all allocations an arbitrary amount. To allocate \$1 to a settlement, write two new asset positions of \$1 and -\$1 to the ledger, then use the \$1 to allocate. The total asset position is unchanged.

**Pros**

This approach removes all contention on a total asset position.

Trading between two such total asset positions without global constraints can run at the theoretically optimal latency and throughput. Combining this with batching of batch size 50, it is possible to achieve settlements per second up to the same 12,500 settlements per second per total asset position that are possible globally.

**Cons**

Besides the inability to enforce any global constraints on the total asset position, this creates many new contracts. At 500 settlements per second, two allocations per settlement, and two new assets per allocation, that results in 2,000 new asset positions per second, which adds up quickly.

This effect has to be mitigated by a netting automation that nets them up into a single position once a period (for example, every time it sees >= 100 asset positions for a total position). This automation does not contend with the trading, but it adds up to 20 large transactions per second to the system and slightly reduces total throughput.

### Shard total asset positions with global constraints

As an example of a global constraint, assume that the total asset position has to stay positive. This is usually done by ensuring that each individual asset position is positive. If that is the case, the strategy is to define a sharding scheme where the total position is decomposed into `N` smaller shard positions and then run sequential processing or batching per shard position.

Each asset position has to be clearly assignable to a single shard position so that there is no contention between shards. The partitioning of the total asset position does not have to be done on-ledger. If the automation for all shards can communicate off-ledger, it is possible to run a sharding strategy where you simply set the total number of desired asset positions.

For example, assume that there should be 100 asset positions for a total asset position with some minimal value.

* The automation keeps track of a synchronized pending set of asset positions, which marks asset positions that are in use.
* Every time the automation triggers (which may happen concurrently), it looks at how many asset positions there are relative to the desired 100 and how much quantity is needed to allocate the open settlements.
* It then selects an appropriate set of non-pending asset positions so that it can allocate the open settlements and return new asset positions to move the total number closer to 100.
* Before sending the transaction, it adds those positions to the pending set to make sure that another thread does not also use them.

Alternatively, if you have a sufficiently large total position compared to settlement values, you can pick the 99th percentile `p_99` of settlement values and maintain `N-1` positions of value between `p_99` and `2 * p_99` and one of the (still large) remainder. 99% of transactions will be processed in the `N-1` shard positions, and the remaining 1% will be processed against the remaining pool. Whenever a shard moves out of the desired range, it is balanced against the pool.

**Pros**

Assuming that there is always enough liquidity in the total asset position, the performance can be the same as without global constraints: up to 12,500 settlements per second on a single total asset position.

**Cons**

If settlement values are large compared to total asset holdings, this technique helps little. In an extreme case, if every settlement needs more than 50% of the total holding, it does not perform any better than the sequential processing or batching per asset type and owner technique.

In realistic scenarios where settlement values are distributed on a broad range relative to total asset position and those relativities change as holdings go up and down, developing strategies that perform optimally is complex. There are competing priorities that need to be balanced carefully:

* Keeping the total number of asset positions limited so that the number of active contracts does not impact system performance.
* Having sufficient large asset positions so that frequent small settlements can be processed in parallel.
* Having a mechanism that ensures large settlements, possibly requiring as much as 100% of the available total asset position, are not blocked.

## Application development performance practice

*Material relocated from Module 7 — Performance Best Practices.*

Performance optimization for Canton applications means understanding the boundary between on-ledger and off-ledger operations, and making deliberate choices about what crosses that boundary. Ledger operations carry synchronization overhead that database operations don't, so the goal is to minimize unnecessary ledger interaction while keeping business-critical state on-ledger.

## On-Ledger vs. Off-Ledger

Canton Network application design should account for performance characteristics, carefully considering on-ledger versus off-ledger implementation. When deciding whether information should be stored on-ledger:

* **State** — Essential facts in the workflow. When these facts require agreement across organizations, store them on-ledger.
* **Data** — Non-essential facts. For efficiency, use off-ledger technologies for sharing non-critical data.
* **Workflows** — Only workflows that cross organizational boundaries should be on-ledger.

A practical example: in a licensing application, the license itself (who holds it, what it covers, whether it's active) belongs on-ledger because both parties need to agree on its status. The license's detailed description text, marketing materials, or usage analytics belong off-ledger in a conventional database.

## Contract Design for Performance

### Avoid contract fan-out

When a single transaction creates or archives many contracts, it requires all stakeholders of all those contracts to participate in the transaction. Design your templates to avoid creating large numbers of contracts in a single transaction.

Instead of creating one contract per item in a batch:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Avoid: creates N contracts in one transaction
choice ProcessBatch : [ContractId Item]
  controller processor
  do mapA (\item -> create Item with ...) items
```

Consider batching into a single contract with a list field, or processing items in separate transactions:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Better: one contract representing the batch
choice ProcessBatch : ContractId BatchResult
  controller processor
  do create BatchResult with items = processedItems
```

### Minimize stakeholders per transaction

Each additional signatory or observer on a contract adds a party that must participate in the transaction protocol. Keep the stakeholder set as small as the business logic requires.

### Use contract keys judiciously

Contract keys enable efficient lookups but introduce contention. If multiple transactions try to create or exercise contracts with the same key concurrently, they will conflict. Design keys that partition naturally by party or business entity to reduce contention.

## PQS Query Optimization

PQS stores contract data in JSONB columns in PostgreSQL. For read-heavy workloads, proper indexing is critical.

### Creating indexes

Use the PQS helper function to create JSONB indexes:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
   call create_index_for_contract('token_wallet_holder_idx',
                                  'register:DA.Register:Token',
                                  '(payload->''wallet''->>''holder'')',
                                  'hash');

```

This index allows efficient lookups on the wallet holder field without scanning the entire JSONB payload.

### PostgreSQL tuning

The default PostgreSQL Docker image ships with minimal settings. For any realistic workload, tune the following:

* `shared_buffers` — Set to 25% of available RAM
* `effective_cache_size` — Set to 75% of available RAM
* `max_connections` — Match to your expected connection pool size
* `autovacuum` settings — Tune for your write patterns

Resource requirements depend on your workload. Consult the [PQS operations guide](/sdks-tools/development-tools/pqs) for sizing guidance specific to your query patterns and contract volumes.

### Query patterns

* Use `explain analyze` to verify that queries use your indexes
* Prefer filtering in SQL over fetching all contracts and filtering in application code
* For time-series queries, use the event tables rather than the active contract set
* Consider materialized views for frequently-run aggregation queries

## Parallel Command Submission

The Ledger API supports parallel command submissions. Commands that affect different contracts can execute concurrently on the synchronizer. Structure your backend to take advantage of this:

* Use async/concurrent command submission from your backend
* Assign unique command IDs to enable deduplication
* Group commands by the contracts they affect to avoid contention
* Monitor command completion times to detect bottleneck patterns

## Traffic Management

On DevNet, TestNet, and MainNet, every ledger transaction consumes traffic credits purchased with Canton Coin (CC). Optimize your traffic costs by:

* Reducing the number and size of on-ledger transactions
* Using batch operations where possible
* Configuring auto-top-up to avoid running out of traffic during peak usage
* Monitoring traffic consumption patterns to forecast costs

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
