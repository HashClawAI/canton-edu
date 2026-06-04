---
title: "Performance Optimization"
slug: "global-synchronizer-production-operations-performance-optimization"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/performance-optimization.md"
source_title: "Performance Optimization"
tags:
  - global-synchronizer
  - production-operations
  - performance-optimization
---

# Performance Optimization

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Optimization

> Tuning database, JVM, and Canton configuration for validator and SV node performance

Canton node performance depends on database throughput, JVM configuration, sequencer capacity, and pruning strategy. This page covers the key tuning areas for validator and SV node operators.

## Database optimization

PostgreSQL is the primary performance bottleneck in most Canton deployments.

### Connection pools

Canton uses HikariCP for database connection pooling. The default pool size works for light workloads, but high-throughput deployments benefit from tuning:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant.storage {
  type = "memory"

  config {
    # Maximum number of connections in the pool
    maxConnections = 30

```

Set `maxConnections` based on your PostgreSQL `max_connections` setting and the number of Canton processes sharing the database server. A good starting point is `max_connections / number_of_canton_processes`, leaving headroom for monitoring and maintenance connections.

### PostgreSQL tuning

These PostgreSQL parameters have the most impact on Canton workloads:

* **`shared_buffers`** — Set to 25% of available RAM. For a 64 GB database server, use `16GB`.
* **`effective_cache_size`** — Set to 50-75% of available RAM. This tells the query planner how much memory is available for caching, including OS cache.
* **`work_mem`** — Controls memory for sort operations and hash tables. Start with `64MB` and increase if you see disk-based sorts in query plans.
* **`maintenance_work_mem`** — Memory for VACUUM and index operations. Set to `1GB` or higher for large databases.
* **`max_wal_size`** — Controls checkpoint frequency. Increase to `4GB` or `8GB` to reduce checkpoint pressure under heavy write loads.
* **`random_page_cost`** — Set to `1.1` if your database runs on SSD storage (default is `4.0`, which is tuned for spinning disks).

Example `postgresql.conf` additions:

```ini theme={"theme":{"light":"github-light","dark":"github-dark"}}
shared_buffers = 16GB
effective_cache_size = 48GB
work_mem = 64MB
maintenance_work_mem = 1GB
max_wal_size = 8GB
random_page_cost = 1.1
checkpoint_completion_target = 0.9
wal_buffers = 64MB
```

### Indexing

Canton creates the necessary indexes during schema migration. Do not modify or drop Canton-managed indexes. If you observe slow queries in your PostgreSQL logs, check that autovacuum is running properly — bloated tables and stale statistics are the most common cause of query plan degradation.

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Check for tables that need vacuuming
SELECT schemaname, relname, n_dead_tup, last_autovacuum
FROM pg_stat_user_tables
WHERE n_dead_tup > 10000
ORDER BY n_dead_tup DESC;
```

## JVM tuning

Canton runs on the JVM. The default JVM settings are conservative, and production deployments benefit from explicit configuration.

### Heap size

Set the heap size based on the node type and expected workload:

* **Validator (participant)** — Start with `-Xmx4g`. Increase to 8-12 GB for high-throughput workloads or when hosting many parties.
* **Sequencer** — Start with `-Xmx4g`. The sequencer's memory needs scale with message throughput.
* **Mediator** — Start with `-Xmx2g`. The mediator has lighter memory requirements than the sequencer or participant.

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Helm values for JVM settings
participant:
  jvmOptions: "-Xms4g -Xmx4g -XX:+UseG1GC -XX:MaxGCPauseMillis=200"
```

### Garbage collection

G1GC is the recommended garbage collector for Canton. It provides good throughput with predictable pause times. Key settings:

* **`-XX:+UseG1GC`** — Enable G1 garbage collector
* **`-XX:MaxGCPauseMillis=200`** — Target maximum GC pause. Lower values reduce latency spikes but may reduce throughput.
* **`-XX:G1HeapRegionSize=16m`** — For heaps above 8 GB, increasing the region size improves G1 efficiency

Monitor GC activity with `-Xlog:gc*:file=/var/log/canton/gc.log:time,uptime,level,tags` and watch for frequent full GC pauses, which indicate the heap is too small.

## Sequencer throughput

The sequencer's throughput is determined by its ordering backend and database performance. For the centralized (PostgreSQL) ordering backend (currently in Alpha):

* The single database is the serialization point for all message ordering
* Vertical scaling of the database server (faster CPU, more IOPS) directly improves throughput
* Network latency between the sequencer process and its database affects every message

For the decentralized (BFT) ordering backend, throughput depends on consensus round time and the number of sequencer nodes. BFT consensus adds latency per message but provides fault tolerance.

## Traffic management

On the Global Synchronizer, every transaction consumes traffic, which is paid for with Canton Coin. To reduce traffic costs:

* **Batch operations** — Submit multiple related commands together rather than individually. Canton processes batched commands more efficiently.
* **Contract design** — Smaller contracts and fewer contract creates/archives per transaction reduce traffic consumption.
* **Synchronizer assignment** — Move high-frequency bilateral workflows to a private synchronizer where no traffic fees apply.

Monitor your traffic consumption through the validator's wallet or the Splice admin API to avoid running out of traffic balance during peak periods.

## Pruning

Canton stores a full history of transactions and ACS (Active Contract Set) snapshots. Over time, this data accumulates and can slow down queries. Pruning removes historical data that is no longer needed.

### Impact on performance

* Pruning reduces database size, which improves backup times and query performance
* The pruning process itself is resource-intensive — schedule it during low-traffic periods
* After pruning, run `VACUUM ANALYZE` on the affected tables to reclaim disk space and update query statistics

### Configuration

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
    connectionTimeout = 30000
  }
}

```

<Warning>
  Pruned data cannot be recovered. Ensure you have backups before enabling aggressive pruning. Some regulatory contexts require retaining transaction history for a defined period.
</Warning>

## Batch sizes

Canton processes commands in batches internally. The default batch sizes balance latency and throughput. For high-throughput workloads, you can increase batch sizes:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
  # Prune data older than this duration
  max-pruning-batch-size = 1000
}

canton.participants.participant.parameters {
```

Larger batches improve throughput at the cost of slightly higher per-command latency. Monitor sequencer and command completion latency metrics to find the right balance.

## Monitoring performance

Track these metrics to identify bottlenecks: `canton_participant_command_completion_latency` (end-to-end command time), `canton_sequencer_send_latency` (sequencer throughput), `canton_participant_db_query_latency` (database health), `hikaricp_connections_active` (connection pool saturation), and JVM heap/GC metrics. Set up dashboards and alert when values exceed your baseline — performance degradation is usually gradual, and early detection prevents outages.

Document howto enable replication (on by default) on enterprise nodes with supported storage. Document health check configuration and fail-over times. Document admin commands to work with multiple replicas (find active replica), document commands to inspect activeness. For participant: load balancer configuration in front of gRPC Ledger API to route to active instance. Link to explanation on HA architecture.

## High Availability Usage

This section looks at some of the components already mentioned and supplies useful Canton commands.

### Participant

High availability of a participant node is achieved by running multiple participant node replicas that have access to a shared database.

Participant node replicas are configured in the Canton configuration file as individual participants with two required changes for each participant node replica:

* Using the same storage configuration to ensure access to the shared database. Only PostgreSQL and Oracle-based storage is supported for HA. For Oracle it is crucial that the participant replicas use the same username to access the shared database.
* Set `replication.enabled = true` for each participant node replica.

<Note>
  Starting from Canton 2.4.0, participant replication is enabled by default when using supported storage.
</Note>

#### Manual trigger of a fail-over

Fail-over from the active to a passive replica is done automatically when the active replica has a failure, but one can also initiate a graceful fail-over with the following command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
activeParticipantReplica.replication.set_passive()
```

The command succeeds if there is at least another passive replica that takes over from the current active replica, otherwise the active replica remains active.

#### Load balancer configuration

Many replicated participants can be placed behind an appropriately sophisticated load balancer that will by health checks determine which participant instance is active and direct ledger and admin api requests to that instance appropriately. This makes participant replication and failover transparent from the perspective of the ledger-api application or canton console administering the logical participant, as they will simply be pointed at the load balancer.

Participants should be configured to expose an "IsActive" health status on our health HTTP server using the following monitoring configuration:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton {
  monitoring {
    health {
      server {
        address = 0.0.0.0
        port = 8000
      }

      check.type = is-active
    }
  }
}
```

Once running, this server reports a HTTP 200 status code on a http/1 GET request to `/health` if the Participant is currently the active replica. Otherwise, an error will be returned.

To use a load balancer it must support http/1 health checks for routing requests on a separate http/2 (GRPC) server. This is possible with [HAProxy](http://www.haproxy.org/) using the following example configuration:

global
log stdout format raw local0

defaults
log global
mode http
option httplog

# enabled so long running connections are logged immediately upon connect

option logasap

# expose the admin-api and ledger-api as separate servers

frontend admin-api
bind :15001 proto h2
default\_backend admin-api

backend admin-api

# enable HTTP health checks

option httpchk

# required to create a separate connection to query the load balancer.

# this is particularly important as the health HTTP server does not support h2

# which would otherwise be the default.

http-check connect

# set the health check uri

http-check send meth GET uri /health

# list all participant backends

server participant1 participant1.lan:15001 proto h2 check port 8080
server participant2 participant2.lan:15001 proto h2 check port 8080
server participant3 participant3.lan:15001 proto h2 check port 8080

# repeat a similar configuration to the above for the ledger-api

frontend ledger-api
bind :15000 proto h2
default\_backend ledger-api

backend ledger-api
option httpchk
http-check connect
http-check send meth GET uri /health

server participant1 participant1.lan:15000 proto h2 check port 8080
server participant2 participant2.lan:15000 proto h2 check port 8080
server participant3 participant3.lan:15000 proto h2 check port 8080

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/optimize/storage.rst" hash="b2f96e3b" */}

Add query cost logging.

## Optimize Storage

### General Settings

#### Max Connection Settings

The storage configuration can further be tuned using the following additional setting:

```
canton.participants.<service-name>.storage.parameters.max-connections = X
```

This allows you to set the maximum number of DB connections used by a Canton node. If the value is None or non-positive, the value will be the number of processors. The setting has no effect if the number of connections is already set via slick options (i.e. storage.config.numThreads).

If you are unsure how to size your connection pools, [this article](https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing) may be a good starting point.

Generally, the number of connections should be up to two times the number of CPUs on the database machine.

The number of parallel indexer connections can be configured via

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.<participant-name>.parameters.ledger-api-server-parameters.indexer.ingestion-parallelism = Y
```

The number `Z` of the connections used by the exclusive sequencer writer component is the final parameter that can be controlled.

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.sequencers.<sequencer-name>.sequencer.high-availability.exclusive-storage.max-connections = Z
```

A Canton participant node will establish up to `X + Y + 2` permanent connections with the database, whereas a synchronizer will use up to `X` permanent connections, except for a sequencer with HA setup that will allocate up to `2X` connections. During startup, the node will use an additional set of at most `X` temporary connections during database initialisation.

The number `X` represents an upper bound of permanent connections and is divided internally for different purposes, depending on the implementation. Consequently, the actual size of the write connection pool, for example, could be smaller. Some of the allotted connections will be taken by the *read* pool, some will be taken by the *Write* pool, and a single additional connection will be reserved to a dedicated *main* connection responsible for managing the locking mechanism.

The following table summarizes the detailed split of the connection pools in different Canton nodes. `R` signifies a *Read* pool, `W` a *Write* pool, `A` a *Ledger API* pool, `I` an *Indexer* pool, `RW` a combined *Read/Write* pool, and `M` the *Main* pool.

| Node Type                  | Enterprise Edition with Replication                               | Enterprise Edition                                                | Community Edition                    |
| -------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------ |
| Participant                | A = X / 2<br />R = X / 4<br />W = X / 4 - 1<br />M = 1<br />I = Y | A = X / 2<br />R = X / 4<br />W = X / 4 - 1<br />M = 1<br />I = Y | A = X / 2<br />RW = X / 2<br />I = Y |
| Mediator                   | R = X / 2<br />W = X / 2 - 1<br />M = 1                           | N/A                                                               | N/A                                  |
| Sequencer                  | RW = X                                                            | N/A                                                               | N/A                                  |
| Sequencer writer           | R = X / 2<br />W = X / 2 - 1<br />M = 1                           | N/A                                                               | N/A                                  |
| Sequencer exclusive writer | R = Z / 2<br />W = Z / 2                                          | N/A                                                               | N/A                                  |
| Synchronizer               | N/A                                                               | RW = X                                                            | RW = X                               |

The results of the divisions are always rounded down unless they yield a zero. In that case, a minimal pool size of 1 is ascertained.

The values obtained from that formula can be overridden using explicit configuration settings for the *Ledger API* `A`, the *Read* `R`, the *Write* `W` pools.

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-reads = R-overwrite
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-writes = W-overwrite
    canton.participants.<participant-name>.storage.parameters.connection-allocation.num-ledger-api = A-overwrite
```

Similar parameters exist also for other Canton node types:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.sequencers.sequencer.storage.parameters.connection-allocation...
    canton.mediators.mediator.storage.parameters.connection-allocation...
```

Where a node operates a combined *Read/Write* connection pool, the numbers for `R` and `W` overwrites are added together to determine the overall pool size.

The effective connection pool sizes are reported by the Canton nodes at startup.

INFO  c.d.c.r.DbStorageMulti\$:participant=participant\_b - Creating storage, num-reads: 5, num-writes: 4

#### Queue Size

Canton may schedule more database queries than the database can handle. As a result, these queries will be placed into the database queue. By default, the database queue has a size of 1000 queries. Reaching the queueing limit will lead to a `DB_STORAGE_DEGRADATION` warning. The impact of this warning is that the queuing will overflow into the asynchronous execution context and slowly degrade the processing, which will result in fewer database queries being created. However, for high-performance setups, such spikes might occur more regularly. Therefore, to avoid the degradation warning appearing too frequently, the queue size can be configured using:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.storage.config.queueSize = 10000

```

### Postgres

#### Postgres Configuration

For Postgres, [the PGTune online tool](https://pgtune.leopard.in.ua/) is a good starting point for finding reasonable parameters (use online transaction processing system), but you need to increase the settings of `shared_buffers`, `checkpoint_timeout` and `max_wal_size`, as explained below.

Beyond the initial configuration, note that most indexes Canton uses are "hash based". Therefore, read and write access to these indexes is uniformly distributed. However, Postgres reads and writes indexes in pages of 8kb, while a simple index might only be a couple of writes. Therefore, it is very important to be able to keep the indexes in memory and only write updates to the disk from time to time; otherwise, a simple change of 32 bytes requires 8kb I/O operations.

Configuring the `shared_buffers` setting to hold 60-70% of the host memory is recommended, rather than the default suggestion of 25%, as the Postgres caching appears to be more effective than the host-based file access caching.

Also increase the following variables beyond their default: Increase the `checkpoint_timeout` so that the flushing to disk includes several writes and not just one per page, accumulated over time, together with a higher `max_wal_size` to ensure that the system does not prematurely flush before reaching the `checkpoint_timeout`. Monitor your system during load testing and tune the parameters accordingly to your use case. The downside of changing the checkpointing parameters is that crash recovery takes longer.

#### Sizing and Performance

Note that your Postgres database setup requires appropriate tuning to achieve the desired performance. Canton is database-heavy. This section should give you a starting point for your tuning efforts. You may want to consult the troubleshooting section on how to analyze whether the database is a limiting factor.

This guide can give you a starting point for tuning. Ultimately, every use case is different and the exact resource requirements cannot be predicted, but have to be measured.

First, ensure that the database you are using is appropriately sized for your use case. The number of cores depends on your throughput requirements. The rule of thumb is:

* 1 db core per 1 participant core.
* 1 participant core for 30-100 ledger events per second (depends on the complexity of the commands).

The memory requirements depend on your data retention period and the size of the data you are storing. Ideally, you monitor the database index cache hit/miss ratio. If your instance needs to keep on loading indexes from the disk, performance suffers. It might make sense to start with 128GB, run a long-running scale & performance test, and [monitor the cache hit/miss ratio](https://www.postgresql.org/docs/current/monitoring-stats.html#MONITORING-PG-STATIO-ALL-INDEXES-VIEW).

Most Canton indexes are contract-id based, which means that the index lookups are randomly distributed. Solid state drives with high throughput perform much better than spinning disks for this purpose.

#### Predictability of Shared Environments

The throughput and latency of a Canton node depends on the performance of the database. Sharing hardware or software saves cost and better utilizes available resources, but it comes with some drawbacks: If the database is operated in a shared environment such as the Cloud, where other applications are using the same database or are operated on the same hardware, the performance of the Canton node varies due to contention on shared resources. This is a natural effect of shared environments and cannot be entirely avoided. It can be difficult to diagnose as a user of the shared environment due to lack of visibility into the other applications and the host system.

If you are operating in a shared environment, you should monitor the performance of the database and expect a higher variance in latency and throughput.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
