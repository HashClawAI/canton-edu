---
title: "Troubleshooting Cheat Sheet"
slug: "appdev-troubleshooting"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting.md"
source_title: "Troubleshooting Cheat Sheet"
tags:
  - appdev
  - troubleshooting
---

# Troubleshooting Cheat Sheet

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting Cheat Sheet

> Index of detailed troubleshooting guides for Canton Network application development

For detailed troubleshooting steps, see the topic guides below. For diagnostic and debugging tooling, see [Debugging Tools](/docs/canton/appdev-tooling-debugging-tools).

<CardGroup cols={2}>
  <Card title="Installation Issues" icon="wrench" href="/docs/canton/appdev-troubleshooting-guide-installation-issues">
    Nix shell failures, Docker configuration, memory allocation, JDK setup.
  </Card>

  <Card title="Development Issues" icon="bug" href="/docs/canton/appdev-troubleshooting-guide-development-issues">
    Daml compilation errors, API connection problems, transaction failures during development.
  </Card>

  <Card title="Operational Issues" icon="server" href="/docs/canton/appdev-troubleshooting-guide-operational-issues">
    Traffic exhaustion, upgrade problems, PQS failures on DevNet, TestNet, and MainNet.
  </Card>

  <Card title="Common Issues FAQ" icon="circle-question" href="/docs/canton/appdev-faq">
    Frequently encountered app development and validator operation issues with short answers and next steps.
  </Card>

  <Card title="Common Questions" icon="circle-question" href="/docs/canton/appdev-troubleshooting-guide-common-questions">
    Frequently asked questions about Canton Network application development.
  </Card>

  <Card title="Daml Error Codes" icon="circle-exclamation" href="/docs/canton/appdev-troubleshooting-guide-error-code-reference">
    Daml compilation errors and Canton runtime error codes with causes and resolutions.
  </Card>

  <Card title="Ledger API Errors" icon="circle-exclamation" href="/docs/canton/appdev-troubleshooting-guide-ledger-api-errors">
    Common Ledger API error codes encountered during command submission.
  </Card>
</CardGroup>

## Diagnostic tooling

For log capture, lnav workflows, Canton Console diagnostics, and PQS query examples used while troubleshooting, see [Debugging Tools](/docs/canton/appdev-tooling-debugging-tools).

## Getting help

If the topic guides above do not resolve your issue:

* **Self-service**: Search this troubleshooting guide and the [debugging tools](/docs/canton/appdev-tooling-debugging-tools) page.
* **Community**: Post in `#gsf-global-synchronizer-appdev` (Slack) or [forum.canton.network](https://forum.canton.network/) with your error message, redacted logs, and environment details (validator ID, network, SDK/Splice version).
* **Email support**: `da-support@digitalasset.com` for best-effort discretionary support.
* **Paid support with SLAs**: `support@digitalasset.com` (opens a tracked Jira ticket).

When asking for help, include:

* Your validator ID and network (DevNet, TestNet, or MainNet)
* The Splice / SDK version you are running
* Relevant log excerpts (redact private keys, passwords, and JWT tokens; preserve error codes, correlation IDs, and timestamps)
* A timeline of when the issue started and any recent changes

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
