---
title: "Validator Ingress and Egress Requirements"
slug: "global-synchronizer-deployment-validator-networking"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/validator-networking.md"
source_title: "Validator Ingress and Egress Requirements"
tags:
  - global-synchronizer
  - deployment
  - validator-networking
---

# Validator Ingress and Egress Requirements

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Validator Ingress and Egress Requirements

> Network ingress and egress requirements for validator nodes

## Ingress

The validators have no external ingress requirements and don't need to whitelist any other SVs or validators.

## Egress

The validators must be able to connect to all the SVs, thus whitelisting of egress on port 443 for the IPs of all the SVs is required (refer to the network diagram for a networking overview). Note that egress is often allowed by default, so in many cases this requires no action.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
