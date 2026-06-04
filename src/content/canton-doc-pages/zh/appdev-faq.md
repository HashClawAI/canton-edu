---
title: "常见问题 FAQ"
slug: "appdev-faq"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/faq.md"
source_title: "Common Issues FAQ"
tags:
  - appdev
  - faq
---

# 常见问题 FAQ

> Canton Network 验证者与应用开发者常见问题

汇总 Canton Network 验证者与应用开发者的常见问题，来自实际支持互动，涵盖最易混淆之处。

***

## 入门

<AccordionGroup>
  <Accordion title="运行 Canton Quickstart 有哪些前置条件？">
    **硬件要求：**

    * 至少 8GB RAM（建议 16GB）
    * 至少 4 核 CPU
    * 至少 50GB 可用磁盘

    **软件要求：**

    * Docker Desktop，Docker Compose 2.26.0+
    * Java 17 或 21（不支持 Java 22+）
    * Node.js 18.x 或更高
    * Git

    **Mac 用户使用 Colima：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    colima start --memory 8 --cpu 4
    ```

    <Warning>
      前置文档可能未列出所有依赖的精确版本。若遇错误，请先核对 Docker Compose 版本——这是 quickstart 失败最常见原因。
    </Warning>
  </Accordion>

  <Accordion title="LocalNet、DevNet、TestNet 与 MainNet 有何区别？">
    | 环境 | 用途 | 访问 | 真实价值 |
    | ------------ | --------------------------- | ------------------------- | ----------------- |
    | **LocalNet** | 本机开发 | 无需申请 | 无 |
    | **DevNet** | 集成测试 | VPN + SV 赞助 | 无 |
    | **TestNet** | 预生产/ staging | 须 IP 白名单 | 无 |
    | **MainNet** | 生产 | IP 白名单 + onboarding | 有（Canton Coin） |

    **LocalNet** 完全在本机运行本地同步器，用于初期开发与单元测试。

    **DevNet** 连接公共开发环境，需 VPN 与 Super Validator 赞助，审批通常需 2–4 周。

    **TestNet** 用于生产前 staging，比 DevNet 更稳定，需 IP 白名单。

    **MainNet**（Global Synchronizer）为生产环境，Canton Coin 有真实价值，须完整验证者 onboarding。
  </Accordion>

  <Accordion title="如何获得 DevNet 访问权限？">
    1. 联系 [canton.foundation](https://canton.foundation) 所列 Super Validator 赞助方
    2. 赞助方将：
       * 提供 VPN 凭证
       * 将你的验证者 IP 加入白名单
       * 提交赞助信息

    **审批通常需 2–4 周。**

    <Info>
      DevNet 面向集成测试，须与 Super Validator 赞助方保持活跃关系。
    </Info>
  </Accordion>
</AccordionGroup>

***

## 验证者运维

<AccordionGroup>
  <Accordion title="公共浏览器显示验证者版本错误——如何修复？">
    若 helm 升级成功后，ccview.io 或 CantonLoop Lighthouse 等仍显示旧版本，常见原因是使用了 `--reuse-values` 标志。

    **解决方案：**
    升级时**不要**使用 `--reuse-values`：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    helm upgrade validator splice-validator/splice-validator \
      --version 0.5.4 \
      -f validator-values.yaml \
      --namespace validator
    ```

    **验证：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl -n validator get deploy validator-app \
      -o "jsonpath={.spec.template.spec.containers[0].image}"
    ```

    `--reuse-values` 可能导致升级到新 chart 版本后仍保留旧版本配置。
  </Accordion>

  <Accordion title="SV URL 与 Scan URL 有何区别？">
    二者用途不同，**切勿**混用：

    **SV URL**（Super Validator URL）：

    * 用途：验证者 onboarding 与赞助
    * 格式：`https://sv.sv-2.global.canton.network.digitalasset.com`
    * 配置位置：`svSponsorAddress`

    **Scan URL**：

    * 用途：查看网络数据、浏览交易
    * 格式：`https://scan.sv-2.global.canton.network.digitalasset.com`
    * 用于：区块浏览器等对外工具

    <Warning>
      在 `svSponsorAddress` 中使用 Scan URL 会导致 onboarding 失败，错误如「Gave up getting app version」。
    </Warning>
  </Accordion>

  <Accordion title="如何在验证者上启用修剪（pruning）？">
    在 `validator-values.yaml` 中添加修剪配置：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    participantPruningSchedule:
      cron: "0 */10 * * * ?"   # 每 10 分钟
      maxDuration: 30m          # 单次修剪最长时长
      retention: 90d            # 保留 90 天历史
    ```

    **MainNet 首次修剪：**
    若历史很大，可增大 `maxDuration` 或先用较大 `retention`：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    participantPruningSchedule:
      cron: "0 */10 * * * ?"
      maxDuration: 60m          # 首次修剪可更长
      retention: 180d           # 先设高，后续再降低
    ```

    **监控进度：**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.pruning.get_schedule()
        res1: Option[PruningSchedule] = Some(value = PruningSchedule(cron = "0 */10 * * * ?", maxDuration = 30m, retention = 2160h))
    ```

    检查 `/v2/state/latest-pruned-offsets` 端点确认修剪在运行。
  </Accordion>

  <Accordion title="如何检查验证者是否健康？">
    **HTTP 端点：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # 验证者健康
    curl http://localhost/api/validator/readyz

    # Participant 健康  
    curl http://localhost:5003/health
    ```

    **Canton Console：**

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

    **Kubernetes：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    kubectl get pods -n validator
    kubectl logs -n validator deployment/validator-app --tail=100
    ```

    **健康验证者的迹象：**

    * 所有 Pod 为 Running
    * 健康端点返回 200
    * 已连接同步器
    * 无持续错误日志
    * MainNet 上收到 liveness 奖励
  </Accordion>

  <Accordion title="网络升级时会发生什么？我需要做什么？">
    网络升级按协调时间表进行：

    1. **查看目标版本**：[canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/)

    2. **阅读发布说明**，了解破坏性变更与迁移要求

    3. **版本升级**（如 0.4.x → 0.5.x）：
       * 升级前备份/快照
       * 更新迁移配置：
         ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
         migration:
           id: 4  # 与当前网络 migration 一致
           migrating: true
         ```
       * 如需要，更新数据库名：
         ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
         persistence:
           databaseName: participant_4
         ```

    4. **升级 helm chart 或 Docker 镜像**至网络版本

    5. **验证**验证者重新加入网络并恢复运行

    <Warning>
      不要逐级升级中间版本，应直接升级到当前网络版本。
    </Warning>
  </Accordion>
</AccordionGroup>

***

## 认证与安全

<AccordionGroup>
  <Accordion title="如何配置 OIDC 认证（Auth0/Keycloak）？">
    1. **配置 OIDC 提供方**（Auth0、Keycloak 等）

    2. **在 `.env` 中设置环境变量：**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       AUTH_URL="https://your-tenant.auth0.com"
       AUTH_JWKS_URL="https://your-tenant.auth0.com/.well-known/jwks.json"
       AUTH_WELLKNOWN_URL="https://your-tenant.auth0.com/.well-known/openid-configuration"
       LEDGER_API_AUTH_AUDIENCE="https://ledger_api.your-domain.com"
       VALIDATOR_ADMIN_USER="auth0|123456789"
       WALLET_ADMIN_USER="auth0|123456789"
       ```

    3. **带认证启动验证者：**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       ./start.sh -a
       ```

    **从无认证迁移到认证：**

    * 停止验证者：`./stop.sh`
    * 用 `-a` 重启：`./start.sh -a`
    * 验证者运营用户将自动迁移

    <Info>
      OIDC 提供方在请求时须签发带 `daml_ledger_api` scope 的 JWT。
    </Info>
  </Accordion>

  <Accordion title="频繁出现 ACCESS_TOKEN_EXPIRED——如何解决？">
    通常因令牌生命周期过短。较新 splice 版本可能需要更长令牌寿命。

    **解决方案：**
    在 OIDC 提供方中延长访问令牌超时：

    **Auth0：**

    1. Applications → Your App → Settings
    2. Advanced Settings → Access Token Lifetime
    3. 设为 900 秒（15 分钟）或更长

    **Keycloak：**

    1. Realm Settings → Tokens
    2. Access Token Lifespan → 900（15 分钟）

    然后重启验证者。
  </Accordion>

  <Accordion title="验证者认证推荐的令牌生命周期是多少？">
    **推荐设置：**

    * 访问令牌：15–30 分钟
    * 刷新令牌：24 小时

    部分 OIDC 默认 5 分钟访问令牌，对 Canton 验证者（尤其高负载或高延迟时）往往不足。
  </Accordion>
</AccordionGroup>

***

## 交易与错误

<AccordionGroup>
  <Accordion title="MEDIATOR_SAYS_TX_TIMED_OUT 是什么意思？">
    表示中介者在超时内未收到所有必需 Party 的足够确认。

    **常见原因：**

    1. **Canton Coin 不足**——某 Party 无法为 traffic 充值
    2. **验证者离线**——涉及某验证者不可达
    3. **网络延迟**——临时网络问题

    **解决方案：**

    1. 检查所有相关 Party 的 CC 余额
    2. 确认所有验证者健康
    3. 必要时充值 CC：
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
         -H "Authorization: Bearer $TOKEN"
       ```

    错误信息中的 `unresponsiveParties` 指出未响应的 Party。
  </Accordion>

  <Accordion title="提交命令时出现 503 超时——为什么？">
    503 通常表示 participant 过载。检查：

    **数据库队列溢出：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    grep "DB_STORAGE_DEGRADATION" participant.log
    grep "queued tasks = 2000" participant.log
    ```

    **解决方案：**

    1. **启用修剪**减小数据库规模
    2. **增加数据库资源**（IOPS、内存）
    3. **考虑 PQS** 分担读负载
    4. **实现带指数退避的重试**

    若提交大量交易，考虑批处理或限流。
  </Accordion>

  <Accordion title="ContentionOnSharedResources 是什么意思？">
    表示多笔交易竞争同一锁定合约或资源。

    **解决方案：**
    用指数退避重试：

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

    并发环境下此错误**属预期**，重试是正确做法。
  </Accordion>

  <Accordion title="交易被拒绝——如何调试？">
    **调试步骤：**

    1. **从错误响应获取 trace ID**

    2. **在日志中搜索 trace ID：**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       grep "trace-id\":\"YOUR_TRACE_ID" participant.log validator.log
       ```

    3. **检查常见原因：**
       * 授权失败（Party 无权限）
       * 包未 vet
       * traffic（CC）不足
       * 合约已归档
       * 超时

    4. **用 Canton Console 深入调查：**

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

## Quickstart 问题

<AccordionGroup>
  <Accordion title="splice 容器反复崩溃——怎么办？">
    **诊断步骤：**

    1. **查看日志：**
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       docker logs splice-validator-participant-1
       ```

    2. **核对资源：**
       * Docker 内存 ≥ 8GB
       * Docker CPU ≥ 4 核

    3. **检查 `.env` 配置错误**

    **常见解决方案：**

    Colima 用户：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    colima stop
    colima start --memory 8 --cpu 4
    ```

    Docker Desktop：

    * Settings → Resources → Memory → 8GB+
    * Apply & Restart

    然后干净启动：

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    make clean
    make setup && make build
    make start
    ```
  </Accordion>

  <Accordion title="make build 报 env_file 类型错误——原因？">
    **错误：**

    ```
    'env_file[1]' expected type 'string', got unconvertible type 'map[string]interface {}'
    ```

    **原因：** Docker Compose 版本低于 2.26.0

    **解决方案：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # 检查版本
    docker compose version

    # 升级（Mac Homebrew）
    brew install docker-compose

    # 或更新 Docker Desktop
    ```

    Canton Quickstart 需要 Docker Compose 2.26.0+。
  </Accordion>

  <Accordion title="Quickstart 启动一般要多久？">
    在足够硬件（8GB RAM、4 CPU）上：

    * **首次运行：** 10–15 分钟（下载镜像、构建）
    * **后续运行：** 2–5 分钟

    若超过 20 分钟，检查：

    * 系统资源是否充足
    * Docker 日志是否有错误
    * 拉取镜像的网络连接
  </Accordion>
</AccordionGroup>

***

## 备份与恢复

<AccordionGroup>
  <Accordion title="如何备份验证者身份？">
    **导出节点 ID dump：**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.health.dump()
        res7: String = "/Users/ibosy/work/b9lab/projects/canton/repos/source_repos/canton-new-2/canton-dump-2026-05-06T11-38-47.245535Z.zip"
    ```

    生成的 JSON 包含：

    * Participant ID
    * 密钥对（namespace、signing、encryption）
    * 授权存储快照
    * 版本

    **安全保存**——此备份可用于恢复验证者身份。

    <Warning>
      节点 ID dump 含私钥。须加密并按组织密钥管理策略安全存储。
    </Warning>
  </Accordion>

  <Accordion title="旧版本节点 ID 备份还能恢复吗？">
    可以，但可能需更新 JSON 中的密钥名称。

    **旧格式（0.4.x 前）：**

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
      "keys": [
        { "name": "participant-namespace", ... },
        { "name": "participant-signing", ... },
        { "name": "participant-encryption", ... }
      ]
    }
    ```

    **当前格式：**

    ```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
    {
      "keys": [
        { "name": "namespace", ... },
        { "name": "signing", ... },
        { "name": "encryption", ... }
      ]
    }
    ```

    恢复前更新密钥名与 version 字段。
  </Accordion>

  <Accordion title="升级前应备份什么？">
    **任何升级前：**

    1. **数据库快照**（PostgreSQL dump）
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       pg_dump -h localhost -U cnadmin cantonnet_participant > backup.sql
       ```

    2. **持久卷快照**（Kubernetes）
       * Validator PV
       * Participant PV

    3. **节点 ID dump**

    ```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
    @ participant1.health.dump()
        res8: String = "/Users/ibosy/work/b9lab/projects/canton/repos/source_repos/canton-new-2/canton-dump-2026-05-06T11-38-48.208558Z.zip"
    ```

    4. **配置文件**
       * `validator-values.yaml`
       * `.env`
       * 自定义配置

    5. **记录当前状态**
       * 当前版本
       * Migration ID
       * 数据库名
  </Accordion>
</AccordionGroup>

***

## 性能与扩展

<AccordionGroup>
  <Accordion title="如何提升 Ledger API 性能？">
    **可选措施：**

    1. **启用修剪**减小 ACS：
       ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
       participantPruningSchedule:
         cron: "0 */10 * * * ?"
         maxDuration: 30m
         retention: 90d
       ```

    2. **使用 PQS**（Participant Query Store）分担读负载，将查询移出主 participant

    3. **增加数据库资源：**
       * 升级存储（AWS 上 gp2 → gp3）
       * 提高 IOPS
       * 增加内存/CPU

    4. **调优连接池：**

    ```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
    canton.participants.participant1.storage.parameters.connection-allocation {
        num-ledger-api = 32
    }
    ```

    5. **客户端批处理与限流**
  </Accordion>

  <Accordion title="数据库很大（350GB+）正常吗？">
    MainNet 验证者长期运行且未修剪时，数据库很大较常见。

    **解决方案：**

    1. **启用修剪**（见上文 FAQ）

    2. **保守 retention** 降低首次修剪量：
       ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
       retention: 180d  # 先设高
       maxDuration: 60m # 允许更长修剪
       ```

    3. **监控增长**并调整 retention

    4. **数据库维护：**
       * PostgreSQL VACUUM ANALYZE
       * 索引优化
  </Accordion>
</AccordionGroup>

***

## 钱包与 Canton Coin

<AccordionGroup>
  <Accordion title="如何为 traffic 充值 Canton Coin？">
    **钱包 UI：**
    在钱包界面使用充值功能。

    **API：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    curl -X POST "http://localhost/api/validator/v0/admin/traffic/purchase" \
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type: application/json"
    ```

    **自动充值：**
    在验证者配置中设置自动购买 traffic：

    ```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # 在 .env 或 validator-values.yaml
    TARGET_TRAFFIC_THROUGHPUT=20000
    MIN_TRAFFIC_TOPUP_INTERVAL=1m
    ```
  </Accordion>

  <Accordion title="如何在 DevNet/TestNet 领取测试 CC？">
    **DevNet/TestNet 提供水龙头**获取测试 Canton Coin：

    1. 打开钱包 UI
    2. 使用「Tap」或水龙头功能
    3. 测试 CC 将记入钱包

    <Info>
      测试 CC 无真实价值，仅用于 DevNet 与 TestNet 测试。
    </Info>
  </Accordion>

  <Accordion title="升级后钱包余额为 0——CC 丢了吗？">
    通常未丢失，多为同步问题。

    **步骤：**

    1. 等待验证者完全重新同步（协议升级后可能需数小时）
    2. 检查日志错误：
       ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
       grep "503\|UNAVAILABLE" logs-validator.log
       ```
    3. 确认各组件健康
    4. 若 24 小时后仍异常，携带日志联系支持

    验证者须处理全部历史事件才能显示正确余额。
  </Accordion>
</AccordionGroup>

***

## 培训与认证

<AccordionGroup>
  <Accordion title="Daml 认证课程还有效吗？">
    **注意：** 部分认证内容可能教授已弃用模式。

    为 Daml 2.x 设计的课程可能与 Canton Network 3.x 架构不一致。若在 Canton Network 上开发：

    1. **以本站当前文档为主**
    2. **用 Canton Quickstart 动手练习**

    <Warning>
      若课程未提及 Canton Network 或 Daml 3.x，或仅讲 Daml 2.x，其架构模式可能不适用于当前 Canton Network 开发。
    </Warning>
  </Accordion>

  <Accordion title="在哪里学习 Canton Network 开发？">
    **推荐资源：**

    1. **官方文档：**
       * [构建文档](/appdev/get-started/choose-your-path)
       * [运营文档](/global-synchronizer/understand/introduction)

    2. **动手：**
       * [Canton Quickstart](https://github.com/digital-asset/cn-quickstart)
       * 完整跑通 quickstart

    3. **社区：**
       * 加入 Slack（#gsf-global-synchronizer-appdev）
       * 运维问题可在 validator-operations 频道提问

    4. **视频：**
       * [Digital Asset YouTube](https://www.youtube.com/@digitalassetcom)
       * [Canton Network YouTube](https://www.youtube.com/@CantonNetwork)
  </Accordion>
</AccordionGroup>

***

## 支持与升级

<AccordionGroup>
  <Accordion title="如何联系支持？">
    **支持渠道：**

    | 类型 | 联系方式 | 响应 |
    | -------------------- | ----------------------------------------------------------------- | ----------- |
    | **酌情支持** | [da-support@digitalasset.com](mailto:da-support@digitalasset.com) | 尽力而为 |
    | **SLA（企业）** | [support@digitalasset.com](mailto:support@digitalasset.com) | 按 SLA |
    | **社区** | Slack 频道 | 社区 |
    | **论坛** | [discuss.daml.com](https://discuss.daml.com) | 社区 |

    **联系支持时请提供：**

    * 验证者 ID
    * 网络（DevNet/TestNet/MainNet）
    * Splice 版本
    * 基础设施（Docker/K8s、云厂商）
    * 相关日志
    * 复现步骤
    * 问题开始时间
  </Accordion>

  <Accordion title="支持工单应包含哪些信息？">
    **必备信息：**

    1. **环境：**
       * Splice/Canton 版本
       * 部署方式（Docker Compose / Kubernetes）
       * 云厂商与基础设施
       * 数据库配置

    2. **问题详情：**
       * 清晰描述
       * 预期与实际行为
       * 开始时间
       * 近期变更

    3. **日志：**
       * Participant 日志
       * Validator 日志
       * 相关堆栈
       * 错误时间戳

    4. **标识符：**
       * 验证者 ID
       * 相关 Party ID
       * 交易 ID（如适用）
       * 错误中的 Trace ID

    <Info>
      分享日志前请脱敏（私钥、密码、JWT 等）。
    </Info>
  </Accordion>
</AccordionGroup>

***

## 网络相关问题

<AccordionGroup>
  <Accordion title="如何从 DevNet 迁移到 TestNet 再到 MainNet？">
    **DevNet → TestNet：**

    1. 申请 TestNet IP 白名单
    2. 更新配置：
       * 更改同步器 URL
       * 更新 SV 赞助地址
    3. 全新部署或按场景迁移

    **TestNet → MainNet：**

    1. 完成 MainNet 验证者 onboarding
    2. 申请 MainNet IP 白名单
    3. 遵循 [MainNet onboarding 文档](/global-synchronizer/deployment/onboarding-process)
    4. 以生产配置部署

    <Warning>
      DevNet 与 TestNet 数据无法迁移到 MainNet，须按全新部署规划。
    </Warning>
  </Accordion>

  <Accordion title="如何查看当前网络版本？">
    **网络状态：**
    访问 [canton.foundation/sv-network-status](https://canton.foundation/sv-network-status/) 查看当前版本。

    **本验证者版本：**

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    # Kubernetes
    kubectl -n validator get deploy validator-app -o jsonpath='{.spec.template.spec.containers[0].image}'

    # Docker
    docker inspect validator-app --format='{{.Config.Image}}'
    ```

    **Canton Console：**

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

## 仍有疑问？

若此处未涵盖你的问题：

1. **[搜索本站文档](https://docs.canton.network)**

2. **查阅 [故障排除速查表](/appdev/troubleshooting)** 获取具体错误方案

3. **在 [社区 Slack](https://docs.canton.network/shared/support-channels)** 向其他开发者请教

4. **携带详细信息 [联系支持](mailto:da-support@digitalasset.com)**

<Card title="为本 FAQ 贡献内容" icon="message-question" href="mailto:da-support@digitalasset.com">
  有应加入的常见问题？请通过支持渠道告知我们。
</Card>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
