---
title: "Splice Metrics Overview"
slug: "global-synchronizer-production-operations-splice-metrics-overview"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/splice-metrics-overview.md"
source_title: "Splice Metrics Overview"
tags:
  - global-synchronizer
  - production-operations
  - splice-metrics-overview
---

# Splice Metrics Overview

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Splice Metrics Overview

> Prometheus metrics exposed by Canton Network components and how to scrape them

Every node exposes a set of metrics on the port 10013 under the path `/metrics`. These metrics can be used to monitor the health of the node, and to diagnose issues.

<Note>
  Apps expose metrics on the port 10013, under the path `/metrics` in the Prometheus format.
</Note>

For a validator the following components expose metrics:

* The validator app
* The participant

For a Super Validator, in addition, we have the following components:

* The SV app
* The scan app

<div className="todo">
  link to network or component diagram to improve understanding
</div>

## Scraping the metrics

We use OpenTelemetry to build the metrics and they are exposed in the Prometheus format, and can be scraped by a Prometheus server. For a reference of the existing metrics please check the metrics reference.

### Histograms

We expose the histograms as [exponential histograms](https://opentelemetry.io/docs/specs/otel/metrics/data-model/#exponentialhistogram) which are converted to [prometheus native histograms](https://prometheus.io/docs/specs/native_histograms/).

<Note>
  Prometheus support must be enabled using the flag `-enable-feature=native-histograms`.

  Native histograms are available only on the protobuf format so Prometheus will switch to the protobuf collection format.
</Note>

You can switch back to regular histograms node by adding the following environment variable to a node: `ADDITIONAL_CONFIG_DISABLE_NATIVE_HISTOGRAMS="canton.monitoring.metrics.histograms=\[\]"`

### Enabling metrics

#### Configuring a helm deployment to enable metrics

To enable metrics in a helm deployment, set the `metrics.enable` value to `true` (default `false`) in the helm values. This will create a `ServiceMonitor` kubernetes custom resource. For this to work it would require that the Prometheus operator is installed in the cluster.

Alternatively you can add prometheus scrape annotations to the charts that are configured to scrape port 10013.

#### Configuring a docker compose deployment to enable metrics

<Note>
  Validator nodes only
</Note>

When using docker compose for the deployment, the metrics are enabled by default. These can be accessed at `http://validator.localhost/metrics` for the validator app and at `http://participant.localhost/metrics` for the participant.

#### Enabling extra metric triggers

The validator app can be configured to run a trigger that polls the topology state and exports metrics summarizing that state. These metrics have the prefix `splice.synchronizer-topology`. See the `validator-metrics-reference` for the concrete set of metrics.

This trigger is disabled by default. As per the information in Adding ad-hoc configuration, add an environment variable `ADDITIONAL_CONFIG_TOPOLOGY_METRICS_EXPORT=canton.validator-apps.validator_backend.automation.topology-metrics-polling-interval = 5m` to enable the trigger with a polling interval of 5 minutes.

## Grafana Dashboards

The release bundle includes Grafana dashboards that can be imported into a Grafana instance. These dashboards assume a Kubernetes deployment and use Prometheus native histogram queries.

Dashboard folder locations depend on the Splice version:

* Up to and including Splice `0.6.4`, use the `grafana-dashboards/` folder.
* Starting with Splice `0.6.5`, Validator operators should use `validator-grafana-dashboards/`, and Super Validator operators should use `sv-grafana-dashboards/`.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
