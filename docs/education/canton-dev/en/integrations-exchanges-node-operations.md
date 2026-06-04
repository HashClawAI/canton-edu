---
title: "Validator Node Operations"
slug: "integrations-exchanges-node-operations"
locale: "en"
category: "integrations"
source_url: "https://docs.canton.network/integrations/exchanges/node-operations.md"
source_title: "Validator Node Operations"
tags:
  - integrations
  - exchanges
  - node-operations
---

# Validator Node Operations

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Validator Node Operations

> Operate an Exchange Validator Node: reward minting, traffic funding, exchange parties setup, Ledger API users, .dar file management, monitoring, and major Splice upgrades.

## Reward Minting and Traffic Funding

As explained in *tokenomics-and-rewards*, your validator node will need traffic to submit
the transactions to execute withdrawals or accept multi-step deposits.
As also explained in that section, the network provides rewards that can be used to fund traffic.

Note also that every validator node has an associated **validator operator party** that represents
that validator node's administrator ([docs](/docs/canton/global-synchronizer-deployment-validator-docker-compose#deployment)).
The validator node automatically mints rewards for that party.
It can further be configured to
[automatically purchase traffic](/docs/canton/global-synchronizer-deployment-validator-kubernetes#configuring-automatic-traffic-purchases)
using that party's CC balance, which includes the minted rewards.

We thus recommend the following setup as a starting point to mint
rewards and automatically fund traffic:

1. Use the validator operator party as your featured `exchangeParty`.
   Follow [exchange-party-setup](#setup-the-featured-exchange-party) to get it featured.
2. [treasury-party-setup](#setup-the-treasury-party) to create a `treasuryParty` with a transfer preapproval managed by your `exchangeParty`.
3. Setup [automatic traffic purchases in the validator app](/docs/canton/global-synchronizer-deployment-validator-kubernetes#configuring-automatic-traffic-purchases).
4. Optional: setup [auto-sweep](/docs/canton/global-synchronizer-deployment-validator-kubernetes#configuring-sweeps-and-auto-accepts-of-transfer-offers) from the `exchangParty` to your `treasuryParty` to limit the funds managed directly by the validator node.

As a starting point for the automatic traffic purchase configuration, set `targetThroughput` to 2kB/s
and `minTopupInterval` to 1 minute, which should be sufficient to execute about one withdrawal or deposit acceptance every 10 seconds.
Please test this with your expected traffic pattern and adjust as needed.
See this [FAQ to measure the traffic spent on an individual transaction](/docs/canton/global-synchronizer-faq#how-do-i-determine-the-traffic-used-for-a-specific-transaction).

## Setup Exchange Parties

### Setup the featured exchange party

As explained above in [reward-minting-and-traffic-funding](#reward-minting-and-traffic-funding), we recommend to use the validator operator party
as your featured `exchangeParty`. This party is automatically created when you
[deploy your validator node](/docs/canton/global-synchronizer-deployment-validator-docker-compose#deployment).
Thus the only setup step is to get it featured by the SVs:

**On DevNet**, you can self-feature your validator operator party as follows:

1. [Log into the wallet UI for the validator user](/docs/canton/global-synchronizer-deployment-validator-kubernetes#logging-into-the-wallet-ui), which presents itself as in this screenshot:

   <img src="https://mintcdn.com/cantonfoundation/zmlOjLpKuDjnaObr/images/exchange-integration/wallet_ui.png?fit=max&auto=format&n=zmlOjLpKuDjnaObr&q=85&s=4b058b9539d00bf9985434af3c2d005f" alt="image" width="2260" height="523" data-path="images/exchange-integration/wallet_ui.png" />

2. Tap 20 \$ of CC to ensure that your validator operator party has enough funds to purchase traffic.

3. Click on the "Self-grant featured app rights" button.

4. The button is replaced with a star ⭐ icon once the `FeaturedAppRight` contract has been created for your validator operator party. This may take about 10 seconds.

That's all. Continue with [setting up your treasury party](#setup-the-treasury-party).

**On MainNet**, apply for featured status for your validator operator party as follows:

1. [Log into the wallet UI for the validator user](/docs/canton/global-synchronizer-deployment-validator-kubernetes#logging-into-the-wallet-ui) on your MainNet validator node.
2. Copy the party-id of your validator operator party using the copy button right of the abbreviated `"google-oaut.."` party name in the screenshot above.
3. Apply for featured application status using this link: [https://sync.global/featured-app-request/](https://sync.global/featured-app-request/)

Wait until your application is approved.
The validator node will automatically pick up the featured status via the corresponding
`FeaturedAppRight` contract issued by the DSO party for its validator operator party.

**On TestNet** there is currently no official process, but you should be able to use the same procedure as the one for MainNet.

### Setup the treasury party

Setup the `treasuryParty` as follows with a transfer preapproval managed by your `exchangeParty`:

1. Create the `treasuryParty` using the wallet SDK to *create-an-external-party* with a key managed in a system of your choice

2. Copy the party id of your `exchangeParty` from the Splice Wallet UI as explained above, or retrieve it
   by calling `/v0/validator-user` on the [Validator API](https://github.com/hyperledger-labs/splice/blob/36ed55ea1fbb9b0030000bb0d0265ba811101df5/apps/validator/src/main/openapi/validator-internal.yaml#L14C3-L14C21).

3. Call `/v2/commands/submit-and-wait` on the [Ledger API](https://github.com/digital-asset/canton/blob/eeb56bc5d9779a7f918893b7a6b15e0b312a044e/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L6C3-L6C31)
   to create a `#splice-wallet:Splice.Wallet.TransferPreapproval:TransferPreapprovalProposal`
   ([code](https://github.com/hyperledger-labs/splice/blob/edb2257410dfc3660314765c40e59f41e2381150/daml/splice-wallet/daml/Splice/Wallet/TransferPreapproval.daml#L9))
   directly with the `provider` set to your `exchangeParty`.

   Note that setting up this transfer preapproval requires the `exchangeParty` to pay a small fee of about 0.25 \$ worth of CC.
   The funds for this fee usually come from the validator liveness rewards that a validator node starts minting about 30 minutes after it is created.
   On DevNet or LocalNet, you don't have to wait that long: just "Tap" the required funds from the built-in faucet.

### Testing the party setup

You can test the party setup on LocalNet or DevNet as follows:

1. Setup your `exchangeParty` and `treasuryParty` as explained above.
2. Setup an additional `testParty` representing a customer.
3. Transfer some CC from the `testParty` to the `treasuryParty` to simulate a deposit.
4. Observe the successful deposit by listing holdings of the `treasuryParty`.
5. Observe about 30' later in the Splice Wallet UI of your validator operator user that the
   `exchangeParty` minted app rewards for this deposit. It takes 30', as activity recording and
   rewards minting happen in different phases of a minting round.

## Setup Ledger API Users

Clients need to
[authenticate as a Ledger API user](/docs/canton/global-synchronizer-deployment-identity-management#user-identity-management)
to access the Ledger API of your Exchange Validator Node.
You can manage Ledger API users and their rights using the
`/v2/users/...` [endpoints of the Ledger API](https://github.com/digital-asset/canton/blob/97b837d7b7e9a499963cba1d39a017648c46e8d7/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L1172).

You will need to authenticate as an existing user that has `participant_admin` rights
to create additional users and grant rights.
One option is to authenticate as the `ledger-api-user` that you
[configured when setting up authentication for your validator node](/docs/canton/global-synchronizer-deployment-validator-kubernetes#oidc-provider-requirements).
Another option is to
[log-in to your Splice Wallet UI for the validator operatory party](/docs/canton/global-synchronizer-deployment-validator-kubernetes#logging-into-the-wallet-ui)
and use the JWT token used by the UI.

We recommend that you setup one user per service that needs to access the Ledger API.
This way you can easily manage permissions and access rights for each service independently.
The [rights](/docs/canton/global-synchronizer-deployment-identity-management#manage-users)
required by the integration components are as follows:

| Component                                                                                      | Required Rights                                   | Purpose                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tx History Ingestion                                                                           | `canReadAs(treasuryParty)`                        | Read transactions and contracts for the `treasuryParty`.                                                                                                                                        |
| Withdrawal Automation                                                                          | `canActAs(treasuryParty)`                         | Prepare and execute transactions on behalf of the `treasuryParty`.                                                                                                                              |
| Multi-Step Deposit Automation                                                                  | `canActAs(treasuryParty)`                         | Prepare and execute transactions on behalf of the `treasuryParty`.                                                                                                                              |
| Automated [exchange parties setup](#setup-exchange-parties) for *exchange-integration-testing* | `participant_admin` and `canActAs(treasuryParty)` | Create parties and use the `treasuryParty` to create its `TransferPreapprovalProposal`. Hint: grant `canActAs(treasuryParty)` to the user doing the setup after allocating the `treasuryParty`. |

*Required Ledger API User Rights*

## .dar File Management

`.dar` files define the Daml workflows used by the token admins for their tokens.
They must be uploaded to your Exchange Validator Node to be able to process
withdrawals and deposits for those tokens.

The `.dar` files for Canton Coin are managed by the Validator Node itself.
The `.dar` files for other tokens need to be uploaded by you using the `/v2/packages` endpoint of the
[Ledger API](https://github.com/digital-asset/canton/blob/eeb56bc5d9779a7f918893b7a6b15e0b312a044e/community/ledger/ledger-json-api/src/test/resources/json-api-docs/openapi.yaml#L316).
See this [how-to guide](/appdev/deep-dives/manage-daml-packages)
for more information.

<Warning title="Important">
  Only upload `.dar` files from token admins that you trust. The uploaded `.dar` files define the choices available on active contracts. Uploading a malicious `.dar` file could result in granting an attacker an unintended delegation on your contracts, which could lead to loss of funds.
</Warning>

## Monitoring

See the Splice documentation for guidance on
[how to monitor your validator node](/docs/canton/global-synchronizer-production-operations-splice-metrics-overview).
Note in particular that it includes
[Grafana dashboards](/docs/canton/global-synchronizer-production-operations-splice-metrics-overview#grafana-dashboards)
for monitoring the traffic usage, balances of local parties (e.g., the `exchangeParty`).

## Rolling out Major Splice Upgrades

For major protocol changes, the global sychronizer undergoes a Major
Upgrade Procedure.
The schedule for these upgrades is published by the [Super Validators](https://docs.google.com/document/d/1QhLL5bL0u8temBL86y957VbWDtZJhH9udH-_C7nBlvc/edit?tab=t.0#heading=h.ripdn5ydglli)
and also announced in the `#validator-operations` slack channel.

As part of this procedure, the old synchronizer is paused, all
validator operators create an export of the state of their validator,
and deploy a new validator connected to the new synchronizer and
import their state again.

The procedure requires some experience to get it right, so it is highly
recommended to run nodes on DevNet and TestNet so you can practice the
procedure before you encounter it on MainNet.

From an integration perspective, there are a few things to keep in mind:

1. A major upgrade only preserves the active contracts but not the
   update history. In particular, you will not be able to get
   transactions from before the major upgrade on the update service on
   the Ledger API of the newly deployed validator node.
2. Offsets on the upgraded validator node start from `0` again.
3. The update history will include special import transactions for the
   contracts imported from the old synchronizer. They all have record time
   `0001-01-01T00:00:00.000000Z`, and represent the creation of the imported
   contracts.

### Runbook

We recommend to roll-out the upgrade as follows:

1. Wait for the synchronizer to be paused and your node to have
   written the migration dump.
2. Open the migration dump and extract the `acs_timestamp` from it, e.g., using `jq .acs_timestamp < /domain-upgrade-dump/domain_migration_dump.json`.
   This is the timestamp at which the synchronizer was paused.
3. Wait for your Tx History Ingestion to have caught up to record time
   `acs_timestamp` or higher. Note that you must consume *offset checkpoints*
   to guarantee that your Tx History Ingestion advances past `acs_timestamp`.
4. Stop your Tx History Ingestion component.
5. Upgrade your validator and connect it to the new synchronizer.
6. Follow the shortened version below of the
   [procedure for restoring a validator node from a backup](/docs/canton/global-synchronizer-production-operations-validator-disaster-recovery)
   to determine the offset from which to restart your Tx History Ingestion:

   1. Retrieve the `synchronizerId` of the last ingested transaction from the Canton Integration DB.

   2. Log into the [Canton Console of your validator node](/docs/canton/global-synchronizer-canton-console-console-overview) and query the offset `offRecovery` assigned to the ACS import transactions at time `0001-01-01T00:00:00.000000Z` using

      ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
      def parseTimestamp(t: String) = {
         val isoFormat = java.time.format.DateTimeFormatter.ISO_INSTANT.withZone(java.time.ZoneId.of("Z"))
         isoFormat.parse(t, java.time.Instant.from(_))
      }
      val synchronizerId = SynchronizerId.tryFromString("example::1220b1431ef217342db44d516bb9befde802be7d8899637d290895fa58880f19accc") // example
      val tRecovery = parseTimestamp("0001-01-01T00:00:00.000000Z")
      val offRecovery = participant.parties.find_highest_offset_by_timestamp(synchronizerId, tRecovery)
      ```

      Alternatively, you can use `grpcurl` to query the offset `offRecovery` from the command line as shown in the
      example below:

      ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
      grpcurl -plaintext -d \
        '{"synchronizerId" : "example::1220be58c29e65de40bf273be1dc2b266d43a9a002ea5b18955aeef7aac881bb471a",
           "timestamp": "0001-01-01T00:00:00.000000Z"}' \
        localhost:5002 \
        com.digitalasset.canton.admin.participant.v30.PartyManagementService.GetHighestOffsetByTimestamp
      ```

      If you use authentication for the Canton Admin gRPC API, then you need to add the appropriate
      authentication flags to the `grpcurl` command above.

   3. Configure the Tx History Ingestion component to start ingesting from offset `offRecovery`.

   4. Restart the Tx History Ingestion component.

Once you have completed these steps, the integration workflows will continue.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
