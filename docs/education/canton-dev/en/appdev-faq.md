---
title: "Common Issues FAQ"
slug: "appdev-faq"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/faq.md"
source_title: "Common Issues FAQ"
tags:
  - appdev
  - faq
---

# Common Issues FAQ

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Common Issues FAQ

> Frequently asked questions from Canton Network validators and developers

Answers to frequently asked questions from Canton Network validators and application developers. This FAQ is compiled from actual support interactions and addresses the most common points of confusion.

***

## Getting Started

<AccordionGroup>
  <Accordion title="What are the prerequisites for running the Canton Quickstart?">
    **Hardware Requirements:**

    * 8GB RAM minimum (16GB recommended)
    * 4 CPU cores minimum
    * 50GB free disk space

    **Software Requirements:**

    * Docker Desktop with Docker Compose 2.26.0+
    * Java 17 or 21 (Java 22+ is not supported)
    * Node.js 18.x or higher
    * Git

    **For Mac users using Colima:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    colima start --memory 8 --cpu 4
    ```

    <Warning>
      The prerequisites documentation may not list specific version requirements for all dependencies. If you encounter errors, verify your Docker Compose version first—this is the most common source of quickstart failures.
    </Warning>
  </Accordion>

  <Accordion title="What's the difference between LocalNet, DevNet, TestNet, and MainNet?">
    | Environment  | Purpose                     | Access                    | Real Value        |
    | ------------ | --------------------------- | ------------------------- | ----------------- |
    | **LocalNet** | Development on your machine | No access needed          | No                |
    | **DevNet**   | Integration testing         | VPN + SV sponsorship      | No                |
    | **TestNet**  | Staging/pre-production      | IP whitelist required     | No                |
    | **MainNet**  | Production                  | IP whitelist + onboarding | Yes (Canton Coin) |

    **LocalNet** runs entirely on your machine with a local synchronizer. Use for initial development and unit testing.

    **DevNet** connects to the public development environment. Requires VPN access and Super Validator sponsorship. Allow 2-4 weeks for approval.

    **TestNet** is for staging deployments before production. More stable than DevNet. Requires IP whitelisting.

    **MainNet** (Global Synchronizer) is production. Real Canton Coin with real value. Full validator onboarding process required.
  </Accordion>

  <Accordion title="How do I get DevNet access?">
    1. Contact a Super Validator sponsor listed at [canton.foundation](https://canton.foundation)
    2. They will:
       * Provide VPN credentials
       * Whitelist your validator IP
       * Submit sponsorship information

    **Allow 2-4 weeks** for the approval process.

    <Info>
      DevNet is designed for integration testing and requires an active relationship with a Super Validator sponsor.
    </Info>
  </Accordion>
</AccordionGroup>

***

## Validator Operations

<AccordionGroup>
  <Accordion title="My validator shows the wrong version on public explorers - how do I fix this?">
    If your validator shows an old version on explorers like ccview\.io or CantonLoop Lighthouse despite successful helm upgrade, the issue is likely using the `--reuse-values` flag.

    **Solution:**
    Upgrade **without** `--reuse-values`:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm upgrade validator splice-validator/splice-validator \
      --version 0.5.4 \
      -f validator-values.yaml \
      --namespace validator
    ```

    **Verify:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl -n validator get deploy validator-app \
      -o "jsonpath={.spec.template.spec.containers[0].image}"
    ```

    The `--reuse-values` flag can cause the old version configuration to persist even when upgrading to a new chart version.
  </Accordion>

  <Accordion title="What's the difference between the SV URL and Scan URL?">
    These URLs serve different purposes and should **not** be confused:

    **SV URL** (Super Validator URL):

    * Used for: Validator onboarding and sponsorship
    * Format: `https://sv.sv-2.global.canton.network.digitalasset.com`
    * Goes in: `svSponsorAddress` configuration

    **Scan URL**:

    * Used for: Viewing network data, exploring transactions
    * Format: `https://scan.sv-2.global.canton.network.digitalasset.com`
    * Used by: Block explorers and public-facing tools

    <Warning>
      Using the Scan URL in your `svSponsorAddress` will cause onboarding failures with errors like "Gave up getting app version".
    </Warning>
  </Accordion>

  <Accordion title="How do I enable pruning on my validator?">
    Add pruning configuration to your `validator-values.yaml`:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    participantPruningSchedule:
      cron: "0 */10 * * * ?"   # Every 10 minutes
      maxDuration: 30m          # Max time per pruning run
      retention: 90d            # Keep 90 days of history
    ```

    **For first-time pruning on MainNet:**
    If you have a large history, increase `maxDuration` or start with a larger `retention`:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    participantPruningSchedule:
      cron: "0 */10 * * * ?"
      maxDuration: 60m          # Longer for initial pruning
      retention: 180d           # Start high, reduce later
    ```

    **Monitor progress:**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.pruning.get_schedule()
        res1: Option[PruningSchedule] = Some(value = PruningSchedule(cron = "0 */10 * * * ?", maxDuration = 30m, retention = 2160h))
    ```

    Check `/v2/state/latest-pruned-offsets` endpoint to verify pruning is running.
  </Accordion>

  <Accordion title="How do I check if my validator is healthy?">
    **Via HTTP endpoints:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Validator health
    curl http://localhost/api/validator/readyz

    # Participant health  
    curl http://localhost:5003/health
    ```

    **Via Canton Console:**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ health.status
        res2: CantonStatus = Status for Sequencer 'sequencer1':
        Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
        Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
        Uptime: 13.164832s
        Ports: 
        	public: 30438
        	admin: 30439
        Connected participants: 
        	PAR::participant1::12201ff69b1d...
        Connected mediators: 
        	MED::mediator1::122009299340...
        Sequencer: SequencerHealthStatus(active = true)
        details-extra: None
        Components: 
        	memory_storage : Ok()
        	sequencer : Ok()
        Accepts admin changes: true
        Version: 3.6.0-SNAPSHOT
        Protocol version: 35

        Status for Mediator 'mediator1':
        Node uid: mediator1::12200929934059da3e012af672ee8a5d26a7e4b3e5084920be298f791f7619843c78
        Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
        Uptime: 12.764755s
        Ports: 
        	admin: 30437
        Active: true
        Components: 
        	memory_storage : Ok()
        	sequencer-client : Ok()
        	sequencer-connection-pool : Ok()
        	sequencer-subscription-pool : Ok()
        	internal-sequencer-connection-sequencer1-0 : Ok()
        	subscription-sequencer-connection-sequencer1-0 : Ok()
        Version: 3.6.0-SNAPSHOT
        Protocol version: 35

        Status for Participant 'participant1':
        Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
        Uptime: 18.839917s
        Ports: 
        	ledger: 30434
        	admin: 30435
        	json: 30436
        Connected synchronizers: 
        	da::122032922613...::35-0
        Unhealthy synchronizers: None
        Active: true
        Components: 
        	memory_storage : Ok()
        	connected-synchronizer : Ok()
        	sync-ephemeral-state : Ok()
        	sequencer-client : Ok()
        	acs-commitment-processor : Ok()
        	sequencer-connection-pool : Ok()
        	sequencer-subscription-pool : Ok()
        	internal-sequencer-connection-sequencer1-0 : Ok()
        	subscription-sequencer-connection-sequencer1-0 : Ok()
        Version: 3.6.0-SNAPSHOT
        Supported protocol version(s): 35, dev

        Status for Participant 'participant2':
        Participant id: PAR::participant2::1220a4d7463bd34b2ba3704401b48ab41d8f88cdcbe512fc1ef071aad97fef106161
        Uptime: 20.666945s
        Ports: 
        	ledger: 30431
        	admin: 30432
        	json: 30433
        Connected synchronizers: None
        Unhealthy synchronizers: None
        Active: true
        Components: 
        	memory_storage : Ok()
        	connected-synchronizer : Not Initialized
        	sync-ephemeral-state : Not Initialized
        	sequencer-client : Not Initialized
        	acs-commitment-processor : Not Initialized
        Version: 3.6.0-SNAPSHOT
        Supported protocol version(s): 35, dev
    ```

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.synchronizers.list_connected()
        res3: Seq[ListConnectedSynchronizersResult] = Vector(
          ListConnectedSynchronizersResult(
            synchronizerAlias = Synchronizer 'da',
            physicalSynchronizerId = da::122032922613...::35-0,
            healthy = true
          )
        )
    ```

    **Via Kubernetes:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl get pods -n validator
    kubectl logs -n validator deployment/validator-app --tail=100
    ```

    **Signs of a healthy validator:**

    * All pods in Running state
    * Health endpoints return 200
    * Connected to synchronizer
    * No persistent error logs
    * Receiving liveness rewards (MainNet)
  </Accordion>

  <Accordion title="What happens during a network upgrade and what do I need to do?">
    Network upgrades follow a coordinated schedule. When an upgrade occurs:

    1. **Check the target version** at [canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/)

    2. **Review release notes** for breaking changes and migration requirements

    3. **For version upgrades** (e.g., 0.4.x → 0.5.x):
       * Take backups/snapshots before upgrading
       * Update migration configuration:
         ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
         migration:
           id: 4  # Match current network migration
           migrating: true
         ```
       * Update database name if required:
         ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
         persistence:
           databaseName: participant_4
         ```

    4. **Upgrade your helm charts** or Docker images to match network version

    5. **Verify** your validator rejoins the network and resumes operation

    <Warning>
      Do not upgrade incrementally through intermediate versions. Upgrade directly to the current network version.
    </Warning>
  </Accordion>
</AccordionGroup>

***

## Authentication & Security

<AccordionGroup>
  <Accordion title="How do I configure OIDC authentication (Auth0/Keycloak)?">
    1. **Set up your OIDC provider** (Auth0, Keycloak, etc.)

    2. **Configure environment variables** in your `.env` file:
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       AUTH_URL="https://your-tenant.auth0.com"
       AUTH_JWKS_URL="https://your-tenant.auth0.com/.well-known/jwks.json"
       AUTH_WELLKNOWN_URL="https://your-tenant.auth0.com/.well-known/openid-configuration"
       LEDGER_API_AUTH_AUDIENCE="https://ledger_api.your-domain.com"
       VALIDATOR_ADMIN_USER="auth0|123456789"
       WALLET_ADMIN_USER="auth0|123456789"
       ```

    3. **Start the validator with authentication:**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       ./start.sh -a
       ```

    **Migrating from non-authenticated to authenticated:**

    * Stop validator: `./stop.sh`
    * Restart with `-a` flag: `./start.sh -a`
    * The validator operator user will be automatically migrated

    <Info>
      Your OIDC provider must issue JWTs with the `daml_ledger_api` scope when requested.
    </Info>
  </Accordion>

  <Accordion title="I'm getting ACCESS_TOKEN_EXPIRED errors constantly - how do I fix this?">
    This typically occurs when token lifetime is too short. Newer splice versions may require longer token lifetimes.

    **Solution:**
    Increase access token timeout in your OIDC provider:

    **For Auth0:**

    1. Applications → Your App → Settings
    2. Advanced Settings → Access Token Lifetime
    3. Set to 900 seconds (15 minutes) or higher

    **For Keycloak:**

    1. Realm Settings → Tokens
    2. Access Token Lifespan → 900 (15 minutes)

    Then restart your validator.
  </Accordion>

  <Accordion title="What's the recommended token lifetime for validator authentication?">
    **Recommended settings:**

    * Access Token: 15-30 minutes
    * Refresh Token: 24 hours

    The default 5-minute token lifetime that some OIDC providers use is often insufficient for Canton validators, especially during high-activity periods or network latency.
  </Accordion>
</AccordionGroup>

***

## Transactions & Errors

<AccordionGroup>
  <Accordion title="What does MEDIATOR_SAYS_TX_TIMED_OUT mean?">
    This error indicates the mediator didn't receive sufficient confirmations from all required parties within the timeout period.

    **Common causes:**

    1. **Insufficient Canton Coin** - A party doesn't have enough CC for traffic top-ups
    2. **Validator offline** - One of the involved validators is down or unreachable
    3. **Network latency** - Temporary network issues

    **Solution:**

    1. Check Canton Coin balances for all involved parties
    2. Verify all validators are healthy
    3. Top up CC if needed:
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
         -H "Authorization: Bearer $TOKEN"
       ```

    The error message includes `unresponsiveParties` which tells you which party(ies) didn't respond.
  </Accordion>

  <Accordion title="Why am I getting 503 timeout errors when submitting commands?">
    503 errors typically indicate the participant is overloaded. Check for:

    **Database queue overflow:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    grep "DB_STORAGE_DEGRADATION" participant.log
    grep "queued tasks = 2000" participant.log
    ```

    **Solutions:**

    1. **Enable pruning** to reduce database size
    2. **Increase database resources** (IOPS, memory)
    3. **Consider PQS** for read-heavy workloads
    4. **Implement retry logic** with exponential backoff

    If you're submitting many transactions, consider batching or rate limiting your submissions.
  </Accordion>

  <Accordion title="What does ContentionOnSharedResources mean?">
    This error occurs when multiple transactions are competing for the same locked contracts or resources.

    **Solution:**
    Implement retry logic with exponential backoff:

    ```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
    async function submitWithRetry(command, maxRetries = 5) {
      for (let i = 0; i < maxRetries; i++) {
        try {
          return await submit(command);
        } catch (e) {
          if (e.code === 'ABORTED' && i < maxRetries - 1) {
            await sleep(Math.pow(2, i) * 100);
            continue;
          }
          throw e;
        }
      }
    }
    ```

    This error is **expected** in concurrent environments - the retry strategy is the correct solution.
  </Accordion>

  <Accordion title="My transaction was rejected - how do I debug it?">
    **Steps to debug:**

    1. **Get the trace ID** from the error response

    2. **Search logs** for the trace ID:
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       grep "trace-id\":\"YOUR_TRACE_ID" participant.log validator.log
       ```

    3. **Check common causes:**
       * Authorization failures (party not authorized)
       * Package not vetted
       * Insufficient traffic (Canton Coin)
       * Contract already archived
       * Timeout issues

    4. **Use Canton Console** for deeper investigation:

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.parties.list()
        res4: Seq[ListPartiesResult] = Vector(
          ListPartiesResult(
            partyResult = participant1::12201ff69b1d...,
            participants = Vector(
              ParticipantSynchronizers(
                participant = PAR::participant1::12201ff69b1d...,
                synchronizers = Vector(
                  SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
                )
              )
            )
          ),
          ListPartiesResult(
            partyResult = Alice::12201ff69b1d...,
            participants = Vector(
              ParticipantSynchronizers(
                participant = PAR::participant1::12201ff69b1d...,
                synchronizers = Vector(
                  SynchronizerPermission(synchronizerId = da::122032922613..., permission = Submission)
                )
              )
            )
          )
        )
    ```

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.packages.list()
        res5: Seq[PackageDescription] = Vector(
          PackageDescription(
            packageId = 9e70a8b3510d...,
            name = ghc-stdlib-DA-Internal-Template,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 114
          ),
          PackageDescription(
            packageId = 0e4a572ab1fb...,
            name = daml-prim-DA-Internal-Erased,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 98
          ),
          PackageDescription(
            packageId = 5aee9b21b8e9...,
            name = daml-prim-DA-Types,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 17554
          ),
          PackageDescription(
            packageId = a1fa18133ae4...,
            name = daml-stdlib-DA-Action-State-Type,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 593
          ),
          PackageDescription(
            packageId = 60c61c542207...,
            name = daml-stdlib-DA-Stack-Types,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 1194
          ),
          PackageDescription(
            packageId = d095a2ccf6dd...,
            name = daml-stdlib-DA-Semigroup-Types,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 426
          ),
          PackageDescription(
            packageId = ee33fb70918e...,
            name = daml-prim-DA-Exception-ArithmeticError,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 286
          ),
          PackageDescription(
            packageId = c280cc3ef501...,
            name = daml-stdlib-DA-Internal-Interface-AnyView-Types,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 826
          ),
          PackageDescription(
            packageId = de2cc2f90eb5...,
            name = canton-builtin-admin-workflow-ping,
            version = 3.4.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 148192
          ),
          PackageDescription(
            packageId = e5411f3d75f0...,
            name = daml-prim-DA-Internal-NatSyn,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 109
          ),
          PackageDescription(
            packageId = 7adc4c2d07fa...,
            name = daml-stdlib-DA-Internal-Fail-Types,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 802
          ),
          PackageDescription(
            packageId = 86d888f34152...,
            name = daml-stdlib-DA-Internal-Down,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 258
          ),
          PackageDescription(
            packageId = 99ea07e101ed...,
            name = daml-stdlib,
            version = 3.4.0.20251020.14338.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 711601
          ),
          PackageDescription(
            packageId = 6f8e6085f576...,
            name = ghc-stdlib-DA-Internal-Any,
            version = 1.0.0,
            uploadedAt = 2026-05-06T11:38:18.493783Z,
            size = 390
          ),
        ...
    ```

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.ledger_api.state.acs.of_party(alice)
        res6: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedContractEntry] = List(
          WrappedContractEntry(
            entry = ActiveContract(
              value = ActiveContract(
                createdEvent = Some(
                  value = CreatedEvent(
                    offset = 14L,
                    nodeId = 0,
                    contractId = "003cbd51cf2a27a93f4ebc0b6575ea7c8265d12f9f24e8d957c5a2294995030c96ca121220de0a46f603d2fe44146c675bc1bb93cda47de55c67cfb6aabad3d1f591d86c15",
                    templateId = Some(
                      value = Identifier(
                        packageId = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e",
                        moduleName = "Iou",
                        entityName = "Iou"
                      )
                    ),
                    contractKey = None,
                    contractKeyHash = <ByteString@442d6e47 size=0 contents="">,
                    createArguments = Some(
                      value = Record(
                        recordId = Some(
                          value = Identifier(
                            packageId = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e",
                            moduleName = "Iou",
                            entityName = "Iou"
                          )
                        ),
                        fields = Vector(
                          RecordField(
                            label = "payer",
                            value = Some(
                              value = Value(
                                sum = Party(
                                  value = "Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                                )
                              )
                            )
                          ),
                          RecordField(
                            label = "owner",
                            value = Some(
                              value = Value(
                                sum = Party(
                                  value = "Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                                )
                              )
                            )
                          ),
                          RecordField(
                            label = "amount",
                            value = Some(
                              value = Value(
                                sum = Record(
                                  value = Record(
                                    recordId = Some(
                                      value = Identifier(
                                        packageId = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e",
                                        moduleName = "Iou",
                                        entityName = "Amount"
                                      )
                                    ),
                                    fields = Vector(
                                      RecordField(
                                        label = "value",
                                        value = Some(value = Value(sum = Numeric(value = "100.0000000000")))
                                      ),
                                      RecordField(
                                        label = "currency",
                                        value = Some(value = Value(sum = Text(value = "EUR")))
                                      )
                                    )
                                  )
                                )
                              )
                            )
                          ),
                          RecordField(
                            label = "viewers",
                            value = Some(value = Value(sum = List(value = List(elements = Vector()))))
                          )
                        )
                      )
                    ),
                    createdEventBlob = <ByteString@442d6e47 size=0 contents="">,
                    interfaceViews = Vector(),
                    witnessParties = Vector(
                      "Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                    ),
                    signatories = Vector(
                      "Alice::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c"
                    ),
                    observers = Vector(),
                    createdAt = Some(
                      value = Timestamp(
                        seconds = 1778067525L,
        ...
    ```
  </Accordion>
</AccordionGroup>

***

## Quickstart Issues

<AccordionGroup>
  <Accordion title="The splice container keeps crashing - what should I do?">
    **Diagnostic steps:**

    1. **Check logs:**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       docker logs splice-validator-participant-1
       ```

    2. **Verify resources:**
       * Docker memory ≥ 8GB
       * Docker CPU ≥ 4 cores

    3. **Check for configuration errors** in your `.env` file

    **Common solutions:**

    For Colima users:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    colima stop
    colima start --memory 8 --cpu 4
    ```

    For Docker Desktop:

    * Settings → Resources → Memory → 8GB+
    * Apply & Restart

    Then clean start:

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    make clean
    make setup && make build
    make start
    ```
  </Accordion>

  <Accordion title="make build fails with env_file type errors - what's wrong?">
    **Error:**

    ```
    'env_file[1]' expected type 'string', got unconvertible type 'map[string]interface {}'
    ```

    **Cause:** Docker Compose version is below 2.26.0

    **Solution:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Check version
    docker compose version

    # Upgrade (Mac with Homebrew)
    brew install docker-compose

    # Or update Docker Desktop
    ```

    Canton Quickstart requires Docker Compose 2.26.0+.
  </Accordion>

  <Accordion title="How long should the quickstart take to start up?">
    On adequate hardware (8GB RAM, 4 CPU cores):

    * **First run:** 10-15 minutes (downloading images, building)
    * **Subsequent runs:** 2-5 minutes

    If startup exceeds 20 minutes, check:

    * Available system resources
    * Docker logs for errors
    * Network connectivity for image downloads
  </Accordion>
</AccordionGroup>

***

## Backup & Recovery

<AccordionGroup>
  <Accordion title="How do I back up my validator's identity?">
    **Export node ID dump:**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.health.dump()
        res7: String = "/Users/ibosy/work/b9lab/projects/canton/repos/source_repos/canton-new-2/canton-dump-2026-05-06T11-38-47.245535Z.zip"
    ```

    This produces a JSON file containing:

    * Participant ID
    * Cryptographic key pairs (namespace, signing, encryption)
    * Authorized store snapshot
    * Version

    **Store securely** - this backup allows recovery of your validator identity.

    <Warning>
      The node ID dump contains private keys. Encrypt and store securely, following your organization's key management policies.
    </Warning>
  </Accordion>

  <Accordion title="I have a node ID backup from an older version - can I still restore?">
    Yes, but you may need to update the key names in the JSON file.

    **Old format (pre-0.4.x):**

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
      "keys": [
        { "name": "participant-namespace", ... },
        { "name": "participant-signing", ... },
        { "name": "participant-encryption", ... }
      ]
    }
    ```

    **Current format:**

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
      "keys": [
        { "name": "namespace", ... },
        { "name": "signing", ... },
        { "name": "encryption", ... }
      ]
    }
    ```

    Update the key names and version field before restoration.
  </Accordion>

  <Accordion title="What should I back up before upgrading?">
    **Before any upgrade:**

    1. **Database snapshots** (PostgreSQL dump)
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       pg_dump -h localhost -U cnadmin cantonnet_participant > backup.sql
       ```

    2. **Persistent Volume snapshots** (Kubernetes)
       * Validator PV
       * Participant PV

    3. **Node ID dump**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.health.dump()
        res8: String = "/Users/ibosy/work/b9lab/projects/canton/repos/source_repos/canton-new-2/canton-dump-2026-05-06T11-38-48.208558Z.zip"
    ```

    4. **Configuration files**
       * `validator-values.yaml`
       * `.env` files
       * Custom configuration

    5. **Document current state**
       * Current version
       * Migration ID
       * Database names
  </Accordion>
</AccordionGroup>

***

## Performance & Scaling

<AccordionGroup>
  <Accordion title="How do I improve Ledger API performance?">
    **Options for improving performance:**

    1. **Enable pruning** to reduce ACS size:
       ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
       participantPruningSchedule:
         cron: "0 */10 * * * ?"
         maxDuration: 30m
         retention: 90d
       ```

    2. **Use PQS** (Participant Query Store) for read-heavy workloads - moves queries off the main participant

    3. **Increase database resources:**
       * Upgrade storage (gp2 → gp3 on AWS)
       * Increase IOPS
       * Add more memory/CPU

    4. **Tune connection pools:**

    ```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.participant1.storage.parameters.connection-allocation {
        num-ledger-api = 32
    }
    ```

    5. **Implement client-side batching** and rate limiting
  </Accordion>

  <Accordion title="My database is very large (350GB+) - is this normal?">
    Large databases are common on MainNet validators that have been running for a while without pruning.

    **Solutions:**

    1. **Enable pruning** (see pruning FAQ above)

    2. **Start with conservative retention** to reduce initial pruning volume:
       ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
       retention: 180d  # Start high
       maxDuration: 60m # Allow longer pruning runs
       ```

    3. **Monitor database growth** and adjust retention as needed

    4. **Consider database maintenance:**
       * VACUUM ANALYZE on PostgreSQL
       * Index optimization
  </Accordion>
</AccordionGroup>

***

## Wallet & Canton Coin

<AccordionGroup>
  <Accordion title="How do I top up Canton Coin for traffic?">
    **Via Wallet UI:**
    Navigate to the wallet interface and use the top-up functionality.

    **Via API:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json"
    ```

    **Automatic top-ups:**
    Configure automatic traffic purchases in your validator configuration:

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # In .env or validator-values.yaml
    TARGET_TRAFFIC_THROUGHPUT=20000
    MIN_TRAFFIC_TOPUP_INTERVAL=1m
    ```
  </Accordion>

  <Accordion title="How do I tap CC on DevNet/TestNet?">
    **DevNet/TestNet provide faucet functionality** for obtaining test Canton Coin:

    1. Access your wallet UI
    2. Use the "Tap" or faucet functionality
    3. Test CC will be credited to your wallet

    <Info>
      Test CC has no real value and is only for testing purposes on DevNet and TestNet.
    </Info>
  </Accordion>

  <Accordion title="My wallet balance shows 0 after upgrade - is my CC lost?">
    No, your CC is likely not lost. This usually indicates a sync issue.

    **Steps:**

    1. Wait for validator to fully resync (can take hours after a protocol upgrade)
    2. Check for errors in logs:
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       grep "503\|UNAVAILABLE" logs-validator.log
       ```
    3. Verify all components are healthy
    4. If issue persists after 24 hours, contact support with logs

    The validator needs to process all historical events to display correct balances.
  </Accordion>
</AccordionGroup>

***

## Training & Certification

<AccordionGroup>
  <Accordion title="Are the Daml certification courses still valid?">
    **Warning:** Some certification content may teach deprecated patterns.

    Courses built for Daml 2.x may not align with Canton Network 3.x architecture. If you're building on Canton Network:

    1. **Focus on current documentation** on this site
    2. **Use the Canton Quickstart** for hands-on learning

    <Warning>
      If a course doesn't mention Canton Network or Daml 3.x, or covers only Daml 2.x specifically, the architectural patterns may not apply to current Canton Network development.
    </Warning>
  </Accordion>

  <Accordion title="Where can I learn Canton Network development?">
    **Recommended resources:**

    1. **Official Documentation:**
       * [Build Documentation](/docs/canton/appdev-get-started-choose-your-path)
       * [Operator Documentation](/docs/canton/global-synchronizer-understand-introduction)

    2. **Hands-on:**
       * [Canton Quickstart](https://github.com/digital-asset/cn-quickstart)
       * Work through the quickstart end-to-end

    3. **Community:**
       * Join the Slack channels (#gsf-global-synchronizer-appdev)
       * Ask questions in validator-operations for operational topics

    4. **Videos:**
       * [Digital Asset YouTube](https://www.youtube.com/@digitalassetcom)
       * [Canton Network YouTube](https://www.youtube.com/@CantonNetwork)
  </Accordion>
</AccordionGroup>

***

## Support & Escalation

<AccordionGroup>
  <Accordion title="How do I contact support?">
    **Support Channels:**

    | Type                 | Contact                                                           | Response    |
    | -------------------- | ----------------------------------------------------------------- | ----------- |
    | **Discretionary**    | [da-support@digitalasset.com](mailto:da-support@digitalasset.com) | Best effort |
    | **SLA (Enterprise)** | [support@digitalasset.com](mailto:support@digitalasset.com)       | SLA-based   |
    | **Community**        | Slack channels                                                    | Community   |
    | **Forum**            | [discuss.daml.com](https://discuss.daml.com)                      | Community   |

    **When contacting support, include:**

    * Validator ID
    * Network (DevNet/TestNet/MainNet)
    * Splice version
    * Infrastructure details (Docker/K8s, cloud provider)
    * Relevant logs
    * Steps to reproduce
    * Timeline of when issue started
  </Accordion>

  <Accordion title="What information should I include in a support ticket?">
    **Essential information:**

    1. **Environment:**
       * Splice/Canton version
       * Deployment method (Docker Compose / Kubernetes)
       * Cloud provider and infrastructure details
       * Database setup

    2. **Issue details:**
       * Clear description of the problem
       * Expected vs actual behavior
       * When the issue started
       * Any recent changes made

    3. **Logs:**
       * Participant logs
       * Validator logs
       * Relevant stack traces
       * Timestamps of errors

    4. **Identifiers:**
       * Validator ID
       * Party IDs involved
       * Transaction IDs (if applicable)
       * Trace IDs from error messages

    <Info>
      Redact sensitive information (private keys, passwords, JWTs) before sharing logs.
    </Info>
  </Accordion>
</AccordionGroup>

***

## Network-Specific Questions

<AccordionGroup>
  <Accordion title="How do I move from DevNet to TestNet to MainNet?">
    **DevNet → TestNet:**

    1. Request TestNet IP whitelisting
    2. Update configuration:
       * Change synchronizer URLs
       * Update SV sponsor address
    3. Deploy fresh or migrate (depending on use case)

    **TestNet → MainNet:**

    1. Complete MainNet validator onboarding
    2. Request MainNet IP whitelisting
    3. Follow [MainNet onboarding documentation](/docs/canton/global-synchronizer-deployment-onboarding-process)
    4. Deploy with production configuration

    <Warning>
      DevNet and TestNet data cannot be migrated to MainNet. Plan for fresh deployment.
    </Warning>
  </Accordion>

  <Accordion title="How do I check current network versions?">
    **Network status:**
    Visit [canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/) for current version information.

    **Your validator version:**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Kubernetes
    kubectl -n validator get deploy validator-app -o jsonpath='{.spec.template.spec.containers[0].image}'

    # Docker
    docker inspect validator-app --format='{{.Config.Image}}'
    ```

    **Via Canton Console:**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ health.status
        res9: CantonStatus = Status for Sequencer 'sequencer1':
        Sequencer id: sequencer1::1220cb0a22fb0aef9243a11f778497d7cacb19f9c4bcc7606776a109983edfaa6b4a
        Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
        Uptime: 23.77778s
        Ports: 
        	public: 30438
        	admin: 30439
        Connected participants: 
        	PAR::participant1::12201ff69b1d...
        Connected mediators: 
        	MED::mediator1::122009299340...
        Sequencer: SequencerHealthStatus(active = true)
        details-extra: None
        Components: 
        	memory_storage : Ok()
        	sequencer : Ok()
        Accepts admin changes: true
        Version: 3.6.0-SNAPSHOT
        Protocol version: 35

        Status for Mediator 'mediator1':
        Node uid: mediator1::12200929934059da3e012af672ee8a5d26a7e4b3e5084920be298f791f7619843c78
        Synchronizer id: da::122032922613929d67857e621fb13e3da49ec13883e24908404520319eee6d31fb4d::35-0
        Uptime: 23.377743s
        Ports: 
        	admin: 30437
        Active: true
        Components: 
        	memory_storage : Ok()
        	sequencer-client : Ok()
        	sequencer-connection-pool : Ok()
        	sequencer-subscription-pool : Ok()
        	internal-sequencer-connection-sequencer1-0 : Ok()
        	subscription-sequencer-connection-sequencer1-0 : Ok()
        Version: 3.6.0-SNAPSHOT
        Protocol version: 35

        Status for Participant 'participant1':
        Participant id: PAR::participant1::12201ff69b1d24edbf0ee2028a304ea702ee8536790dab1a31e7136e6d90ff6d473c
        Uptime: 29.457585s
        Ports: 
        	ledger: 30434
        	admin: 30435
        	json: 30436
        Connected synchronizers: 
        	da::122032922613...::35-0
        Unhealthy synchronizers: None
        Active: true
        Components: 
        	memory_storage : Ok()
        	connected-synchronizer : Ok()
        	sync-ephemeral-state : Ok()
        	sequencer-client : Ok()
        	acs-commitment-processor : Ok()
        	sequencer-connection-pool : Ok()
        	sequencer-subscription-pool : Ok()
        	internal-sequencer-connection-sequencer1-0 : Ok()
        	subscription-sequencer-connection-sequencer1-0 : Ok()
        Version: 3.6.0-SNAPSHOT
        Supported protocol version(s): 35, dev

        Status for Participant 'participant2':
        Participant id: PAR::participant2::1220a4d7463bd34b2ba3704401b48ab41d8f88cdcbe512fc1ef071aad97fef106161
        Uptime: 31.282969s
        Ports: 
        	ledger: 30431
        	admin: 30432
        	json: 30433
        Connected synchronizers: None
        Unhealthy synchronizers: None
        Active: true
        Components: 
        	memory_storage : Ok()
        	connected-synchronizer : Not Initialized
        	sync-ephemeral-state : Not Initialized
        	sequencer-client : Not Initialized
        	acs-commitment-processor : Not Initialized
        Version: 3.6.0-SNAPSHOT
        Supported protocol version(s): 35, dev
    ```
  </Accordion>
</AccordionGroup>

***

## Still Have Questions?

If your question isn't answered here:

1. **[Search the documentation](https://docs.canton.network)** on this site

2. **Check the [Troubleshooting Cheat Sheet](/docs/canton/appdev-troubleshooting)** for specific error solutions

3. **Ask in [community Slack](https://docs.canton.network/shared/support-channels)** channels for guidance from other developers

4. **[Contact support](mailto:da-support@digitalasset.com)** with detailed information about your issue

<Card title="Contribute to this FAQ" icon="message-question" href="mailto:da-support@digitalasset.com">
  Have a common question that should be added? Let us know via support.
</Card>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
