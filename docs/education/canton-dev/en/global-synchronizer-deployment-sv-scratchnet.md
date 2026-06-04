---
title: "How to Bootstrap a Network"
slug: "global-synchronizer-deployment-sv-scratchnet"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/sv-scratchnet.md"
source_title: "How to Bootstrap a Network"
tags:
  - global-synchronizer
  - deployment
  - sv-scratchnet
---

# How to Bootstrap a Network

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# How to Bootstrap a Network

> Bootstrapping a new Canton Network from scratch as a Super Validator

<div className="todo">
  adjust style of write-up below to the rest of docs
</div>

## cometbft helm values

1. disable state sync

stateSync:

* enable: true
* rpcServers: "..."

- enable: false

2. For the single sv config, you are now bootstrapping a single sv so put your own keys in:

sv1:

* keyAddress: "..."
* nodeId: "..."
* publicKey: "..."

## scan helm values

add 1 value:

* isFirstSv: true

## sv helm values

1. remove joinWithKeyOnboarding

* joinWithKeyOnboarding:
* sponsorApiUrl: [https://sv.sv-2.whatever.global.canton.network.digitalasset.com](https://sv.sv-2.whatever.global.canton.network.digitalasset.com)

2. Add initial helm values You may use these number values or choose other ones

* isDevNet: true
* onboardingType: found-dso
*
* // see note below about the rest of these:
* initialSynchronizerFeesConfig:
* baseRateBurstAmount: 400000
* baseRateBurstWindowMins: 20
* extraTrafficPrice: 16.670000000000002
* minTopupAmount: 200000
* readVsWriteScalingFactor: 4
* onboardingFoundingSvRewardWeightBps: 10000

3. Remove the `decentralizedSynchronizerUrl` config from `sv-values.yaml`. It is only used for nodes that join after the initial SV.

## other helm values you may need to consider

* in all the places you use TARGET\_CLUSTER / TARGET\_HOSTNAME, you’ll want to point to your network’s base domain
  * for example, we’re basing our network on hub-scratch.global.canton.network.digitalasset.com, so we set:
    * targetCluster = hub-scratch
    * targetHostname = hub-scratch.global.canton.network.digitalasset.com
* if you use walletSweep, you probably won’t use it in this scratch environment unless you also plan to deploy a validator

## Infra-level things you might want to consider

* Configure the IP allowlist to expose the cluster to an internal VPN or similar network you control. It is not recommended to expose it to the public internet at this point.
* approved SV identities (which make their way into sv helm values): if you are deploying a single bootstrapping node, you can set this to \[]

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
