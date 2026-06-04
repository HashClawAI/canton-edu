---
title: "Logical Synchronizer Upgrades"
slug: "global-synchronizer-production-operations-logical-synchronizer-upgrade"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/logical-synchronizer-upgrade.md"
source_title: "Logical Synchronizer Upgrades"
tags:
  - global-synchronizer
  - production-operations
  - logical-synchronizer-upgrade
---

# Logical Synchronizer Upgrades

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Logical Synchronizer Upgrades

> Upgrade the protocol version of a Global Synchronizer with very limited network downtime through Logical Synchronizer Upgrades (LSU)

export const networkData = {
  mainnet: {
    name: 'MainNet',
    description: 'Production network for live applications. Data is permanent and never reset. Upgrades follow DevNet and TestNet validation.',
    color: '#22c55e',
    versions: {
      splice: '0.6.2',
      damlSdk: '3.4.12',
      pqs: '3.4.6',
      tokenStandard: '1.3.1',
      walletSdk: '1.3.1',
      dappSdk: '1.1.0',
      walletGateway: '1.2.0'
    },
    advanced: {
      minProtocolVersion: '6',
      migrationId: '4',
      darVersions: [{
        name: 'splice-amulet',
        version: '0.1.14'
      }, {
        name: 'splice-wallet',
        version: '0.1.14'
      }, {
        name: 'splice-dso-governance',
        version: '0.1.20'
      }],
      releaseUrl: 'https://github.com/canton-network/splice/releases/tag/0.6.2'
    },
    endpoint: 'scan.sv-1.global.canton.network.sync.global',
    substitutions: {
      splice_cluster: 'main',
      da_hostname: 'global.canton.network.digitalasset.com',
      gsf_sv_url: 'https://sv.sv-1.global.canton.network.sync.global',
      generic_sv_url: 'https://sv.sv-1.global.canton.network.YOUR_SV_SPONSOR',
      gsf_scan_url: 'https://scan.sv-1.global.canton.network.sync.global',
      generic_scan_url: 'https://scan.sv-1.global.canton.network.YOUR_SV_SPONSOR',
      gsf_sequencer_url: 'https://sequencer-MIGRATION_ID.sv-1.global.canton.network.sync.global',
      version: '0.6.2',
      version_literal: '0.6.2',
      chart_version_literal: '0.6.2',
      chart_version_set: 'export CHART_VERSION=0.6.2',
      image_tag_set: 'export IMAGE_TAG=0.6.2',
      image_tag_set_plain: 'export IMAGE_TAG=0.6.2',
      bundle_download_link: {
        label: 'Download Bundle',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_splice-node.tar.gz'
      },
      openapi_download_link: {
        label: 'Download OpenAPI specs',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.2/0.6.2_openapi.tar.gz'
      },
      helm_repo_prefix: 'oci://ghcr.io/digital-asset/decentralized-canton-sync/helm',
      docker_repo_prefix: 'ghcr.io/digital-asset/decentralized-canton-sync/docker'
    }
  },
  testnet: {
    name: 'TestNet',
    description: 'Pre-production environment for final validation. Requires MainNet approval to join. May be reset periodically.',
    color: '#eab308',
    versions: {
      splice: '0.6.3',
      damlSdk: '3.5.1',
      pqs: '3.5.1-rc6',
      tokenStandard: '1.3.1',
      walletSdk: '1.3.1',
      dappSdk: '1.1.0',
      walletGateway: '1.2.0'
    },
    advanced: {
      minProtocolVersion: '6',
      migrationId: '1',
      darVersions: [{
        name: 'splice-amulet',
        version: '0.1.15'
      }, {
        name: 'splice-wallet',
        version: '0.1.15'
      }, {
        name: 'splice-dso-governance',
        version: '0.1.21'
      }],
      releaseUrl: 'https://github.com/canton-network/splice/releases/tag/0.6.3'
    },
    endpoint: 'scan.sv-1.test.global.canton.network.sync.global',
    substitutions: {
      splice_cluster: 'test',
      da_hostname: 'test.global.canton.network.digitalasset.com',
      gsf_sv_url: 'https://sv.sv-1.test.global.canton.network.sync.global',
      generic_sv_url: 'https://sv.sv-1.test.global.canton.network.YOUR_SV_SPONSOR',
      gsf_scan_url: 'https://scan.sv-1.test.global.canton.network.sync.global',
      generic_scan_url: 'https://scan.sv-1.test.global.canton.network.YOUR_SV_SPONSOR',
      gsf_sequencer_url: 'https://sequencer-MIGRATION_ID.sv-1.test.global.canton.network.sync.global',
      version: '0.6.3',
      version_literal: '0.6.3',
      chart_version_literal: '0.6.3',
      chart_version_set: 'export CHART_VERSION=0.6.3',
      image_tag_set: 'export IMAGE_TAG=0.6.3',
      image_tag_set_plain: 'export IMAGE_TAG=0.6.3',
      bundle_download_link: {
        label: 'Download Bundle',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_splice-node.tar.gz'
      },
      openapi_download_link: {
        label: 'Download OpenAPI specs',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.3/0.6.3_openapi.tar.gz'
      },
      helm_repo_prefix: 'oci://ghcr.io/digital-asset/decentralized-canton-sync/helm',
      docker_repo_prefix: 'ghcr.io/digital-asset/decentralized-canton-sync/docker'
    }
  },
  devnet: {
    name: 'DevNet',
    description: 'Development environment with latest features. Open to any validator (IP allowlist required). Reset every 3 months. Best for testing upgrades.',
    color: '#a78bfa',
    versions: {
      splice: '0.6.4',
      damlSdk: '3.5.1',
      pqs: '3.5.1-rc6',
      tokenStandard: '1.3.1',
      walletSdk: '1.3.1',
      dappSdk: '1.1.0',
      walletGateway: '1.2.0'
    },
    advanced: {
      minProtocolVersion: '6',
      migrationId: '1',
      darVersions: [{
        name: 'splice-amulet',
        version: '0.1.15'
      }, {
        name: 'splice-wallet',
        version: '0.1.15'
      }, {
        name: 'splice-dso-governance',
        version: '0.1.21'
      }],
      releaseUrl: 'https://github.com/canton-network/splice/releases/tag/0.6.4'
    },
    endpoint: 'scan.sv-1.dev.global.canton.network.sync.global',
    substitutions: {
      splice_cluster: 'dev',
      da_hostname: 'dev.global.canton.network.digitalasset.com',
      gsf_sv_url: 'https://sv.sv-1.dev.global.canton.network.sync.global',
      generic_sv_url: 'https://sv.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR',
      gsf_scan_url: 'https://scan.sv-1.dev.global.canton.network.sync.global',
      generic_scan_url: 'https://scan.sv-1.dev.global.canton.network.YOUR_SV_SPONSOR',
      gsf_sequencer_url: 'https://sequencer-MIGRATION_ID.sv-1.dev.global.canton.network.sync.global',
      version: '0.6.4',
      version_literal: '0.6.4',
      chart_version_literal: '0.6.4',
      chart_version_set: 'export CHART_VERSION=0.6.4',
      image_tag_set: 'export IMAGE_TAG=0.6.4',
      image_tag_set_plain: 'export IMAGE_TAG=0.6.4',
      bundle_download_link: {
        label: 'Download Bundle',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_splice-node.tar.gz'
      },
      openapi_download_link: {
        label: 'Download OpenAPI specs',
        href: 'https://github.com/digital-asset/decentralized-canton-sync/releases/download/v0.6.4/0.6.4_openapi.tar.gz'
      },
      helm_repo_prefix: 'oci://ghcr.io/digital-asset/decentralized-canton-sync/helm',
      docker_repo_prefix: 'ghcr.io/digital-asset/decentralized-canton-sync/docker'
    }
  }
};

export const VersionOption = ({children}) => <>{children}</>;

export const Version = ({children, title, description, defaultLabel, networkData = {}}) => {
  const networkOrder = ['mainnet', 'testnet', 'devnet'];
  const networksForVersion = version => {
    return networkOrder.filter(networkKey => networkData[networkKey]?.versions?.splice === version);
  };
  const labelForVersion = version => {
    const networks = networksForVersion(version);
    if (networks.length === 1) {
      const networkKey = networks[0];
      return `${networkData[networkKey]?.name ?? networkKey} (${version})`;
    }
    return `CN ${version}`;
  };
  const labelWithVersion = (label, version) => {
    return version ? `${label} (${version})` : label;
  };
  const optionLabel = option => option.props.label ? labelWithVersion(option.props.label, option.props.version) : labelForVersion(option.props.version);
  const renderOption = option => {
    if (option.props.code) {
      return <pre>
          <code>{option.props.code}</code>
        </pre>;
    }
    return option;
  };
  const options = React.Children.toArray(children).filter(child => child?.props?.label || child?.props?.version);
  const tabOptions = options.flatMap(option => {
    if (option.props.label) {
      return [{
        label: optionLabel(option),
        option
      }];
    }
    const networks = networksForVersion(option.props.version);
    if (!networks.length) {
      return [{
        label: optionLabel(option),
        option
      }];
    }
    return networks.map(networkKey => ({
      label: labelWithVersion(networkData[networkKey]?.name ?? networkKey, option.props.version),
      option
    }));
  });
  const defaultIndex = Math.max(0, tabOptions.findIndex(tab => tab.label === defaultLabel));
  const [activeIndex, setActiveIndex] = React.useState(defaultIndex);
  const activeOption = tabOptions[activeIndex]?.option ?? tabOptions[0]?.option;
  if (!tabOptions.length) {
    return null;
  }
  return <div data-component="version" className="my-6 overflow-hidden rounded-lg border border-gray-200 bg-white shadow-sm dark:border-gray-800 dark:bg-gray-950">
      {(title || description) && <div className="border-b border-gray-200 px-4 py-3 dark:border-gray-800">
          {title && <div className="text-sm font-semibold text-gray-950 dark:text-gray-100">{title}</div>}
          {description && <div className="mt-1 text-sm leading-6 text-gray-600 dark:text-gray-400">{description}</div>}
        </div>}
      <div role="tablist" className="flex gap-1 border-b border-gray-200 bg-gray-50 p-1 dark:border-gray-800 dark:bg-gray-900">
        {tabOptions.map(({label}, index) => {
    const isActive = index === activeIndex;
    const buttonClass = isActive ? 'rounded-md bg-white text-gray-950 shadow-sm dark:bg-gray-800 dark:text-gray-100' : 'rounded-md text-gray-600 hover:bg-white/80 hover:text-gray-950 dark:text-gray-400 dark:hover:bg-gray-800/70 dark:hover:text-gray-100';
    return <button key={`${label}-${index}`} type="button" role="tab" aria-selected={isActive} onClick={() => setActiveIndex(index)} className={`min-h-9 px-3 text-sm font-medium transition-colors ${buttonClass}`}>
              {label}
            </button>;
  })}
      </div>
      <div role="tabpanel" className="px-4 py-4 text-sm leading-6 text-gray-800 dark:text-gray-200">
        {renderOption(activeOption)}
      </div>
    </div>;
};

<Warning>
  Logical Synchronizer Upgrades (LSU) are still in development and the instructions here are intended as a preview primarily targeted at Super Validators but will likely change in minor ways before the full release.
</Warning>

Logical synchronizer upgrades (LSUs) allow upgrading the protocol version of a synchronizer
**with very limited network downtime** and no operational overhead for validator operators and app devs around upgrades.
Super validators still have to perform operational steps to deploy successor nodes and schedule the upgrade but those are done asynchronously before the actual upgrade happens.

## High-Level Overview

1. A new Canton release with an updated protocol version becomes available, along with a compatible Splice release. For testing purposes or in some disaster recovery scenarios this can also be the same version and/or protocol version.
   This release supports both the old and new protocol version.

2. Validators and super validators upgrade to the new release, but continue running the original physical synchronizer with the old protocol version. This is a regular upgrade and can be done asynchronously
   but must be done before the actual upgrade time.

3. A vote is created in the SV UI to schedule an LSU through the `nextScheduledLogicalSynchronizerUpgrade` field in `DsoRulesConfig`.
   The schedule includes

   1. **topology freeze time**: after this time, no topology transactions can be sequenced until the upgrade time, so in particular no parties can be added and no Daml packages can be vetted
   2. **upgrade time**: at this time Daml transactions on the original physical synchronizer will time out and new Daml transactions will run on the new physical synchronizer
   3. **new physical synchronizer serial**: usually just the old serial incremented by 1
   4. **new protocol version**: the protocol version of the successor synchronizer

4. All SVs deploy *successor* synchronizer nodes (sequencer, mediator, and optionally CometBFT if DABFT is not used) alongside their existing nodes. Note: There is no new participant, the participant is tied to a logical synchronizer so it does not change on an LSU. As part of that they also [configure](#super-validator-deployment-changes) the successor synchronizer in their SV and scan config.
   This deployment should be completed before the freeze time.

5. At the scheduled **topology freeze time**, the SV app automation of each SV transfers the topology state to the successor nodes and publishes the sequencer URL for the new sequencer in the topology state (this is the only topology transaction that can be published after the freeze time).

6. Between the topology freeze time and the upgrade time, SV app
   automation will periodically send special health check events on
   the new physical synchronizer to verify its health.  Each super
   validator should use their metrics to validate that they observe at
   least one event from each other super validator in the `LSU
   Sequencing Test` dashboard as well as that the BFT peer
   connections (CometBFT or DABFT) of the successor nodes are healthy.

   <div className="todo">add more details once we have added this</div>

7. At the scheduled **upgrade time**, participants automatically connect to the successor synchronizer.
   The SV automation transfers traffic control state from the current sequencer to the successor.
   The successor physical synchronizer may be configured with a lower initial rate limit that will be
   raised by the SV app after a configurable amount of time to avoid an initial traffic surge on the new synchronizer.

   <div className="todo">add more details once we have added this.</div>

8. The successor physical synchronizer is now fully usable. Super Validators update their [configuration](#super-validator-deployment-changes) to mark the original synchronizer as legacy
   and successor as the current synchronizer.

9. After 30 days, the super validators remove the old physical synchronizer node deployment. Super Validators update their [configuration](#super-validator-deployment-changes) to remove the
   legacy synchronizer configuration.

### LSU Cancellation

Between the topology freeze time and and upgrade time, the upgrade can be cancelled if the successor physical synchronizer is deemed unhealthy, e.g., because the health checks fail.
To do so, a threshold of super validators must send a `POST` request to the `/v0/admin/synchronizer/lsu/cancel` endpoint on the SV API.

### Disaster Recovery through Roll-Forward LSU

In case of a disaster that causes the current physical synchronizer to become unavailable, an LSU can be used as a roll-forward recovery mechanism.
The procedure is similar to a regular LSU but because the current physical synchronizer is unusable, the coordination through a vote and topology transactions is not possible and instead validators and super validators need to manually initiate the upgrade.

This procedure can also be used for recovering from a failed LSU. There are two relevant cases:

1. The LSU did not get cancelled before the upgrade time but no Daml transactions and topology transactions were able to be sequenced on the successor physical synchronizer after the upgrade time. In this case, the original successor synchronizer can be thrown away and replaced
   by a new successor synchronizer with a serial incremented by 1 (so 2 compared to the original non-successor synchronizer).
2. The LSU proceeded and some transactions did get sequenced on the successor physical synchronizer but the successor physical synchronizer then became unusable. The procedure is the same in this case but
   the SVs should keep both the original synchronizer and the broken successor synchronizer running (assuming it can still serve events just not sequence new messages) to allow nodes to catchup first and spin up a new successor synchronizer on the side
   so they are running 3 synchronizer nodes for some period of time. Allowing nodes to catch up as much as possible limits the potential for desynchronization requiring manual resolution through ACS commitment mismatches.

Concretely, the procedure is as follows:

1. The old physical synchronizer is deemed broken and the last sequenced message was at record time R.
2. Super validators configure this as the max sequencing time on the old sequencer to guarantee that nothing accidentally gets sequenced after that time. This is done by applying the following environment variable to the existing sequencer:

```
- name: ADDITIONAL_CONFIG_SEQUENCER_LSU_MAX_SEQUENCING_TIME
  value: |
    canton.sequencers.sequencer.parameters.lsu-repair.global-max-sequencing-time-exclusive=MAX_SEQUENCING_TIME
```

2. Super validators deploy successor nodes. Depending on the issue,
   the successor nodes may be configured with older image and protocol
   versions if the issue is limited to the new version.  The successor
   sequencer must be configured with two timestamps:
   `lower-bound-sequencing-time-exclusive` and
   `upgrade-time`. These correspond to the topology freeze time and
   the upgrade time in a regular LSU. In particular, after
   `lower-bound-sequencing-time-exclusive` sequencing test messages
   can be submitted and observed in the `LSU Sequencing Test`
   dashboard. After `upgrade-time` all Daml transactions can be
   submitted. The actual timestamps will be chosen through coordination with all SVs.
   The timestamps are applied through an environment variable on the successor sequencer:

<Version title="LSU sequencing bounds configuration" networkData={networkData}>
  <VersionOption
    version="0.5.18"
    code={`- name: ADDITIONAL_CONFIG_SEQUENCER_LSU_SEQUENCING_BOUNDS
value: |
canton.sequencers.sequencer.parameters.parameters.lsu-repair.lsu-sequencing-bounds-override.lower-bound-sequencing-time-exclusive=LOWER_BOUND_SEQUENCING_TIME_EXCLUSIVE
canton.sequencers.sequencer.parameters.parameters.lsu-repair.lsu-sequencing-bounds-override.upgrade-time=UPGRADE_TIME`}
  />

  <VersionOption
    version="0.6.3"
    code={`- name: ADDITIONAL_CONFIG_SEQUENCER_LSU_SEQUENCING_BOUNDS
value: |
canton.sequencers.sequencer.parameters.lsu-repair.lsu-sequencing-bounds-override.lower-bound-sequencing-time-exclusive=LOWER_BOUND_SEQUENCING_TIME_EXCLUSIVE
canton.sequencers.sequencer.parameters.lsu-repair.lsu-sequencing-bounds-override.upgrade-time=UPGRADE_TIME`}
  />
</Version>

3. Super validators wait until ingestion completed.

4. Super validators configure their SV app app to transfer the topology and traffic state from the old physical synchronizer to the successor nodes.
   To do so, add the following helm values to the SV app:

```
rollForwardLsu:
  newPhysicalSynchronizerSerial: NEW_PHYSICAL_SYNCHRONIZER_SERIAL # Must be agreed between SVs, usually existing (broken) synchronizer serial + 1
  newPhysicalSynchronizerProtocolVersion: NEW_PHYSICAL_SYNCHRONIZER_PROTOCOL_VERSION # Must be agreed between SVs, usually existing (broken) synchronizer serial + 1
  exportTimes:
    topologyExportTime: TOPOLOGY_EXPORT_TIME # Must be agreed between SVs
    trafficExportTime: TRAFFIC_EXPORT_TIME # Must be agreed between SVs
    upgradeTime: UPGRADE_TIME # Must be agreed between SVs
```

5. Validators initiate the *procedure* on their side.

#### Recovery from a failed LSU where nothing got sequenced

For the special case where an LSU was announced and not cancelled but
failed and nothing got sequenced on the successor synchronizer, there
is a variant that avoids the need to manually check for ingestion
being completed and does not require explicit interaction from validators.

To do so, use the following steps:

1. Super validators configure the manual LSU in their scan.

```
rollForwardLsu:
   enabled: true
   upgradeTime: UPGRADE_TIME # Must be agreed between SVs, optional, if not specified it is taken from an existing LSU announcement which should usually be sufficient.
```

2. Validator app automation picks up that configuration and initiates a manual roll-forward LSU to the new synchronizer.

#### Resolving ACS mismatches

Note that depending on how exactly the old synchronizer failed,
validators may desynchronize if some validators have observed a
transaction before the failure while others have not. To recover from
that follow the instructions for *validators*.

## Super Validator Deployment Changes

<div className="todo">update helm values and link them here</div>

LSU requires deployment changes for super validators. Concretely:

1. Participants are now preserved as part of LSUs. So if you previously assumed participant, sequencer and mediator always come as one unit per migration id, you now need to move the participant out of that.
2. The `domain` value on the sv app helm chart should be replaced by `synchronizers`. `synchronizers.current` replaces the synchronizer previously configured through `domain`. `synchronizers.successor`
   should be configured to the successor physical synchronizer when that is deployed. After the upgrade, `synchronizers.current` becomes `synchronizers.legacy` and `synchronizers.successor` becomes `synchronizers.current`. The legacy configuration should be removed together with removing the old physical synchronizer after 30 days. If you already have a node in `legacy` and it should not yet be decommissioned, move it to `additionalLegacy`, which accepts an array of synchronizers.
   The CometBFT configuration also moves under `synchronizers.(current|successor|legacy)`.
3. The `sequencerAddress` and `mediatorAddress`values in scan should be replaced by `synchronizers.current.sequencer` and `synchronizers.current.mediator`. The corresponding values under `synchronizers.successor` should be set together with
   the deployment of the successor physical synchronizer. After the upgrade `successor` becomes `current` and `current` is removed.
4. When using DABFT as the successor node, further changes will be required. Most notably the cometbft node goes away as DABFT runs as part of the sequencer pod. The sequencer pod and SV app will require some additional configuration. Details of this will be added later.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
