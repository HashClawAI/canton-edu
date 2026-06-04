---
title: "Validator Upgrades"
slug: "global-synchronizer-production-operations-validator-upgrades"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/validator-upgrades.md"
source_title: "Validator Upgrades"
tags:
  - global-synchronizer
  - production-operations
  - validator-upgrades
---

# Validator Upgrades

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Validator Upgrades

> Minor upgrade procedures for validator nodes

There are two types of upgrades:

Version upgrades (this corresponds to an upgrade from `0.A.X` to `0.B.Y`) and protocol upgrades (the actual version can remain the same, only the protocol is upgraded and it requires no action).

Version upgrades can be done by each node independently and only require an upgrade of the docker-compose file or a `helm upgrade` for a kubernetes deployment. You must not delete or uninstall any Postgres database, change migration IDs or secrets for a version upgrade; Make sure to read the `release_notes` to learn about changes you may need to make as part of the upgrade.

Note that for docker-compose you must update the full bundle including the docker compose file and the start.sh script and adjust `IMAGE_TAG`. Only updating `IMAGE_TAG` is insufficient as the old docker compose files might be incompatible with the new version.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
