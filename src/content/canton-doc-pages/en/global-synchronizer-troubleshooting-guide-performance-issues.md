---
title: "Performance Issues"
slug: "global-synchronizer-troubleshooting-guide-performance-issues"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/performance-issues.md"
source_title: "Performance Issues"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - performance-issues
---

# Performance Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance Issues

> Resolving slow transactions, resource exhaustion, and database bottlenecks

Performance degrades gradually, so it often goes unnoticed until transactions start timing out or the validator falls behind on event processing. This page covers the most common performance problems and their solutions.

## Slow Transactions

If transaction latency has increased, check these areas in order.

### Traffic Balance

Low traffic balance causes the sequencer to throttle your validator's messages. Check it with:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.traffic_control.traffic_state(participant1.synchronizers.id_of("da"))
    res1: com.digitalasset.canton.sequencing.protocol.TrafficState = TrafficState(
      extraTrafficLimit = 0,
      extraTrafficConsumed = 0,
      baseTrafficRemainder = 0,
      lastConsumedCost = 0,
      timestamp = 1970-01-01T00:00:00Z,
      availableTraffic = 0
    )
```

If `availableTraffic` is near zero (or traffic limits are exhausted), top up immediately and enable auto-top-up to prevent recurrence.

### Database Performance

Query the database for active slow queries:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT pid, now() - query_start AS duration, query
FROM pg_stat_activity
WHERE state = 'active'
ORDER BY duration DESC
LIMIT 10;
```

If you see queries running for more than a few seconds, the database is likely the bottleneck. Common causes:

* **Tables have grown too large.** Enable pruning (see below).
* **Missing indexes.** After a version or protocol upgrade, run `ANALYZE` on the participant database to update query planner statistics.
* **Insufficient IOPS.** If running on cloud infrastructure, upgrade your storage class (e.g., switch from gp2 to gp3 on AWS and increase provisioned IOPS).

### JVM Heap Pressure

If the validator process is spending significant time in garbage collection, transaction processing slows down. Check for GC pressure in logs:

```
GC overhead limit exceeded
```

or frequent `Full GC` entries. Increase heap allocation:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# In Docker Compose, set JAVA_OPTS
JAVA_OPTS="-Xmx4g -Xms4g"

# In Kubernetes, set in the values file
jvmOptions: "-Xmx4g -Xms4g"
```

Monitor heap usage through JMX or by enabling GC logging with `-Xlog:gc*`.

## Resource Exhaustion

### Disk Space

The participant database grows continuously as new transactions are processed. Without pruning, it will eventually exhaust disk space.

**Symptoms:**

* PostgreSQL errors: `could not extend file ... No space left on device`
* Pod eviction in Kubernetes due to ephemeral storage limits

**Check disk usage:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# On the database host
df -h /var/lib/postgresql/data

# In Kubernetes
kubectl exec -n validator statefulset/postgres -- df -h /var/lib/postgresql/data
```

**Enable pruning** to reclaim space:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
participantPruningSchedule:
  cron: "0 */10 * * * ?"
  maxDuration: 30m
  retention: 90d
```

After enabling pruning, the first run may take significantly longer than subsequent runs. Set `maxDuration` generously for the initial prune (60 minutes or more).

### Memory

If the validator pod is killed by the OOM killer (exit code 137), increase the memory limit:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# In Kubernetes values
resources:
  limits:
    memory: "8Gi"
  requests:
    memory: "4Gi"
```

For Docker Compose, increase Docker's total memory allocation to at least 8 GB.

### CPU

High CPU usage is usually caused by runaway automation (a script that retries in a tight loop) or heavy ACS (Active Contract Set) processing.

**Identify the cause:**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check which threads are consuming CPU
jcmd <pid> Thread.print | grep -A2 "java.lang.Thread.State: RUNNABLE"
```

If your application includes automation that retries failed commands, confirm it uses exponential backoff rather than a fixed-interval retry loop.

## Database Query Optimization

### Missing Indexes

After an upgrade or migration, indexes may not have been created for new columns. Check for sequential scans on large tables:

```sql theme={"theme":{"light":"github-light","dark":"github-dark"}}
SELECT relname, seq_scan, idx_scan
FROM pg_stat_user_tables
WHERE seq_scan > 1000
ORDER BY seq_scan DESC;
```

Tables with a high `seq_scan` count and low `idx_scan` count are candidates for missing indexes. Consult the Canton release notes for any required index additions.

### Connection Pool Exhaustion

If you see errors like:

```
HikariPool-1 - Connection is not available, request timed out after 30000ms
```

The database connection pool is fully utilized. Causes include:

* Long-running queries holding connections
* Too many concurrent operations for the configured pool size
* Database-side connection limits reached

Increase the pool size in your Canton configuration:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.storage.parameters {
  max-connections = 32
}
```

Also check the PostgreSQL `max_connections` setting to confirm it accommodates all connection pools across your deployment.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
