---
title: "Observability"
slug: "appdev-modules-m4-observability"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-observability.md"
source_title: "Observability"
tags:
  - appdev
  - modules
  - m4-observability
---

# Observability

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Observability

> Setting up logging, metrics, and dashboards for Canton applications

Running a Canton application in production means you need visibility into what your backend and the underlying Canton nodes are doing. This page covers logging, metrics, and dashboards from an application developer's perspective.

## Logging

### Structured Logging with Logback

Canton nodes and cn-quickstart both use [Logback](https://logback.qos.ch/) for logging. The default configuration writes human-readable logs to the console, but for production you should switch to structured JSON output. JSON logs are easier to ingest into log aggregation systems like the ELK stack or Grafana Loki.

A typical `logback.xml` configuration for JSON output:

```xml theme={"theme":{"light":"github-light","dark":"github-dark"}}
<configuration>
  <appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
    <encoder class="net.logstash.logback.encoder.LogstashEncoder">
      <includeMdcKeyName>command-id</includeMdcKeyName>
      <includeMdcKeyName>party</includeMdcKeyName>
    </encoder>
  </appender>

  <root level="INFO">
    <appender-ref ref="JSON" />
  </root>
</configuration>
```

Including the `command-id` in your MDC (Mapped Diagnostic Context) lets you trace a single Ledger API command through your backend logs and correlate it with the Canton node logs that processed it.

### What to Log

Focus your application logs on:

* **Command submissions** -- Log the command ID, template or choice name, and submitting party before each Ledger API call
* **Command completions** -- Log success or failure, including the error code on failure
* **PQS query performance** -- Log slow queries (above a threshold you define) with the SQL and elapsed time
* **Authentication events** -- Log token validation failures and party resolution

Avoid logging contract payloads in production. They may contain private data that should not leave the validator boundary.

## Metrics

### Prometheus Endpoints

Canton nodes expose Prometheus-compatible metrics endpoints. When running cn-quickstart locally, the validator's metrics are available at `http://localhost:10013/metrics` by default.

Key metrics to monitor from your application's perspective:

* `daml_commands_submissions_total` -- Total commands submitted, broken down by status (success, failure)
* `daml_commands_completions_total` -- Completed commands with their result status
* `daml_commands_delayed_submissions` -- Commands that were delayed due to backpressure
* `daml_execution_total` -- Daml interpretation count and duration
* `canton_sequencer_client_submissions_sequencing_time` -- Time from submission to sequencing, which reflects synchronizer latency

### Application-Level Metrics

cn-quickstart includes OpenTelemetry tracing via the `@WithSpan` annotation on service methods. You can export these spans to any OpenTelemetry-compatible backend (Jaeger, Zipkin, Grafana Tempo).

For custom metrics in your backend, use Micrometer (bundled with Spring Boot) or the OpenTelemetry metrics API:

```java theme={"theme":{"light":"github-light","dark":"github-dark"}}
@WithSpan
public CompletableFuture<ResponseEntity<List<License>>> listLicenses() {
    // The @WithSpan annotation creates a trace span automatically
    return damlRepository.findActiveLicenses()
        .thenApply(licenses -> ResponseEntity.ok(licenses));
}
```

## Dashboards

### Grafana with cn-quickstart

cn-quickstart ships with pre-configured Grafana dashboards in the `ops/` directory. When you run `make start`, Grafana is available at `http://localhost:3000`.

The bundled dashboards cover:

* **Ledger API overview** -- Command submission rates, latencies, and error rates
* **Canton node health** -- JVM memory, gRPC connection states, sequencer connectivity
* **PQS indexing** -- Lag between the ledger head and the PQS projection offset

### Building Your Own Dashboard

If you add application-specific metrics, create a Grafana dashboard that combines Canton node metrics with your backend metrics. A practical starting layout:

* **Top row** -- Command submission rate and error rate (from the Canton node Prometheus endpoint)
* **Middle row** -- Your application's REST endpoint latencies (from Spring Boot Actuator or OpenTelemetry)
* **Bottom row** -- PQS query latencies and active contract counts for your key templates

### Alerting

Set up alerts for conditions that affect your application's reliability:

* Command error rate exceeding a threshold (e.g., more than 5% of submissions failing)
* PQS indexing lag above a few seconds (queries return stale data)
* Traffic budget dropping below your auto-top-up threshold (transactions will start failing)
* JVM heap usage consistently above 80% on the validator

## Further Reading

* [Backend Development](/docs/canton/appdev-modules-m4-backend-dev) -- Error handling patterns that pair with observability
* [Canton Coin and Traffic](/docs/canton/appdev-modules-m4-canton-coin) -- Monitoring your traffic budget
* [cn-quickstart repository](https://github.com/digital-asset/cn-quickstart) -- Pre-configured observability stack

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
