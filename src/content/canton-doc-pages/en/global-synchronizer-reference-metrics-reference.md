---
title: "Splice Metrics Reference"
slug: "global-synchronizer-reference-metrics-reference"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/metrics-reference.md"
source_title: "Splice Metrics Reference"
tags:
  - global-synchronizer
  - reference
  - metrics-reference
---

# Splice Metrics Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Splice Metrics Reference

> Reference for monitoring metrics exposed by Canton Network validator and super validator nodes

You can check your validator's health using the readiness endpoints. All CN applications provide the `/readyz` and `/livez` endpoints, which are used for readiness and liveness probes.

* **Checking readiness**

  * In Kubernetes: readiness and liveness probes are already configured.

    You can also manually check validator readiness with the following command:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl exec &lt;pod-name&gt; -n <namespace> -- curl -v http://localhost:5003/api/validator/readyz
    ```

  * In Docker: run for example this command to check validator liveness inside a container:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker exec &lt;container-name&gt; -- curl -v http://localhost:5003/api/validator/livez
    ```

  You should expect in both case HTTP status code 200 if the validator is ready and live.

* **Using metrics**

  The `splice_store_last_ingested_record_time_ms` metric represents the last ingested record time in each validator store. It can be used to track general activity of the node:

  * If this value continues to increase over time, your node is active and stays in sync with the network. Note that it only advances if your node actually ingests new transactions. For a validator collecting validator liveness rewards this happens every round so you should expect your lag to never go above 20min.
  * If it remains static, further investigation may be required.

  For more details and to visualize this metric on its dedicated dashboard `Splice Store Last Ingested Record Time`, refer to the documentation about Metrics.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
