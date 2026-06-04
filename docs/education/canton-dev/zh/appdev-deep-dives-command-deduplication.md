---
title: "命令去重"
slug: "appdev-deep-dives-command-deduplication"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/command-deduplication.md"
source_title: "Command Deduplication"
tags:
  - appdev
  - deep-dives
  - command-deduplication
---

# 命令去重

> Daml 命令去重原理及应用在重试场景下实现恰好一次账本变更。

Daml 应用与账本的交互本质上是异步的：应用发送命令，一段时间后才在账本上看到效果。该时间窗口内可能发生：应用崩溃、participant 崩溃、网络丢包、账本高负载响应慢等。

若要确保预期账本变更不会执行两次，应用须稳健处理所有失败场景。本指南涵盖：

* 命令去重如何工作
* 应用如何有效使用命令去重

## 命令去重如何工作

命令提交中与去重相关的字段如下。前三项组成 **change ID**，标识预期的账本变更。

* `act_as`：提交方 Party
* user ID：提交命令的用户
* command ID：用户为预期账本变更选择的标识
* deduplication period：在此期限内，Command Completion Service 上不得已有相同 change ID 的成功完成事件；否则当前提交应被拒绝。可用 deduplication duration 或 deduplication offset（含）指定
* submission ID：应用为单次提交选择的标识，会出现在对应完成事件中以便关联；**不得**复用 submission ID

账本可任意延长提交中指定的去重期。

<Note>
  最大去重时长（maximum deduplication duration）是 participant 保证支持的去重期长度。
</Note>

账本选择的去重期称为 **effective deduplication period**。账本也可能将请求的 duration 转为 effective offset 或反之。effective 去重期在完成事件的 deduplication duration 或 deduplication offset 字段中报告。

在以下任一条件成立时，提交视为 **duplicate submission**：

* 提交 participant 的 completion 服务在 **effective** 去重期内已有相同 change ID 的成功完成事件
* participant 或 Daml ledger 在去重时发现另有相同 change ID 的在途提交

去重结果通信方式：

* 经 Command Service 的提交：除非超过 [gRPC deadline](https://grpc.io/blog/deadlines/)，以同步 gRPC 响应指示去重结果（结果**可能**也出现在 Command Completion Service，但使用 Command Service 的应用通常不必处理完成事件）
* 经 Command Submission Service：可同步 gRPC 响应，或经 Command Completion Service 异步通知；即使 Command Submission Service 以 `OK` 确认，提交仍可能是重复

无论通信方式，去重产生的结果包括：

* 账本与在途提交均无相同 change ID 冲突时，完成事件（及可能的响应）传达提交结果（成功或 gRPC 错误；`error_codes` 说明错误如何传达）
* gRPC `ALREADY_EXISTS`，错误码 `DUPLICATE_COMMAND`：effective 去重期内已有相同 change ID 的较早完成
* gRPC `ABORTED`，`SUBMISSION_ALREADY_IN_FLIGHT`：处理本提交时另有相同 change ID 在途
* gRPC `FAILED_PRECONDITION`，`INVALID_DEDUPLICATION_PERIOD`：不支持的去重期；元数据中 `longest_duration` 或 `earliest_offset` 至少其一表示当前端点支持的最长 duration 或最早 offset
* 配置的最大去重时长内的 duration 或该时长内发布的 offset **不应**触发此错误；participant 可自行接受更长周期
* gRPC `FAILED_PRECONDITION`，`PARTICIPANT_PRUNED_DATA_ACCESSED`（去重期用 offset 表示时）：指定 offset 已被修剪；元数据 `earliest_offset` 为最后修剪 offset

去重按设计须对同一账本变更的所有提交经 **同一 participant** 提交。是否重复由完成事件判定，默认 participant 仅输出经本 participant 请求的提交的完成事件。

## 如何使用命令去重

要恰好一次生效，须在较早提交丢失时重提交；应用通常无法区分丢失与账本处理缓慢。命令去重允许重提交直至执行，并拒绝之后的重复提交。

部分变更最多执行一次，无需去重，例如对给定 contract ID exercise consuming choice——每合约最多归档一次，重复提交将以 `CONTRACT_NOT_ACTIVE` 拒绝。

相反，`Create` 每次到达账本都会创建新实例（除非模板前置条件或 contract key 唯一性违反）。对 non-consuming choice 的 `Exercise` 或 `Exercise-By-Key` 若多次提交可能多次执行。借助去重，应用可确保在去重期内仅执行一次，即使因认为丢失或崩溃后忘记已提交而重试。

### 已知处理时间上界

须估计账本相对应用时钟的处理时间上界 `B`（含重试）。若所有重试累计处理超过 `B`，变更可能生效多次。在此前提下，以下策略适用于 Command Service 或 Command Submission + Command Completion Service。

<Note>
  `B` 应不超过配置的最大去重时长，否则依赖账本接受更长去重期，可移植性差且脆弱。
</Note>

1. 为账本变更选择 command ID，确保同一变更始终同一 command ID（确定性，如用合约载荷中的全局唯一 id；或随机生成并持久化以便崩溃后重提）。**注意**：同一变更的所有（重）提交须用同一 command ID；崩溃后通常不知是否已提交，存疑时用同一 command ID 重提，若已提交则去重拒绝。

2. 使用 Command Submission Service 时，在 State Service 获取近期 offset `OFF1`（如当前 ledger end）。

3. 提交命令并设置：

   * command ID（步骤 1）
   * deduplication duration = `B`（**建议**显式设置，避免配置缩短最大去重时长后静默缩短 effective 期；若省略则用当前最大去重时长，配置变更可能破坏去重分析）
   * submission ID 为新值（如随机 UUID）
   * timeout（gRPC deadline）为预期 **submission processing time**（Command Service）或 **submission hand-off time**（Command Submission Service）。hand-off 为发到 Command Submission Service 到收到同步响应的时间；超时后视为丢失并进入重试，通常远短于去重时长。

4. 等待 RPC 返回：

   * 非 `OK` 按错误处理
   * Command Service 且 `OK`：变更已生效，可报成功
   * Command Submission Service：从 `OFF1`（不含）订阅 `actAs` 的完成，直至见到该 change ID 与 submission ID 的完成；`OK` 则成功，否则按错误处理。此步无需超时——Command Submission Service 仅在最终会有完成事件时确认（除非系统永久不可用）。

#### 错误处理

当提交 RPC 或完成事件状态非 `OK` 时需错误处理。下表按状态码（`STATUS_CODE`）与错误码（大写，链至文档）列出反应；元数据字段以小写 `field` 表示。

<table>
  <caption>已知处理时间上界时的命令去重错误处理</caption>

  <colgroup>
    <col style={{ width: "16%" }} />

    <col style={{ width: "83%" }} />
  </colgroup>

  <thead>
    <tr className="header">
      <th>错误条件</th>
      <th>处理</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td>
        <code>DEADLINE\_EXCEEDED</code>
      </td>

      <td>
        <p>视为提交丢失。</p>

        <p>
          从 <code>Step 2 \<dedup-bounded-step-offset></code> 重试，重新获取完成 offset <code>OFF1</code>，必要时增大 timeout。
        </p>
      </td>
    </tr>

    <tr className="even">
      <td>应用崩溃</td>

      <td>
        从 <code>Step 2 \<dedup-bounded-step-offset></code> 重试，重新获取 <code>OFF1</code>。
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>ALREADY\_EXISTS</code> / <code>DUPLICATE\_COMMAND \<error\_code\_DUPLICATE\_COMMAND></code>
      </td>

      <td>
        change ID 在报告的去重期内已被账本接受。可选字段 <code>completion\_offset</code> 为精确 offset；<code>existing\_submission\_id</code> 为成功提交的 submission ID。对账本变更报成功。
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>FAILED\_PRECONDITION</code> /{" "}
        <code>PARTICIPANT\_PRUNED\_DATA\_ACCESSED \<error\_code\_PARTICIPANT\_PRUNED\_DATA\_ACCESSED></code>
      </td>

      <td>
        <p>
          指定去重 offset 已被 participant 修剪。<code>earliest\_offset</code> 为最后修剪 offset。
        </p>

        <p>
          使用 <code>Command Completion Service \<command-completion-service></code>，从最后修剪 offset 起请求 <code>completions \<com.daml.ledger.api.v2.CompletionStreamRequest></code>，将 <code>offset \<com.daml.ledger.api.v2.CompletionStreamRequest.begin\_exclusive></code> 设为 <code>earliest\_offset</code>，用首个 <code>completion offset \<com.daml.ledger.api.v2.Completion.offset></code> 或 <code>checkpoint offset \<com.daml.ledger.api.v2.OffsetCheckpoint.offset></code> 作为去重 offset。
        </p>
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>ABORTED</code> / 其他错误码
      </td>

      <td>
        稍等后从 <code>Step 2 \<dedup-bounded-step-offset></code> 重试，重新获取 <code>OFF1</code>。
      </td>
    </tr>

    <tr className="even">
      <td>其他错误条件</td>

      <td>
        <p>
          结合业务工作流知识与当前账本状态判断较早提交是否仍可能被接受。
        </p>

        <ul>
          <li>
            若结论为不可能再被接受，停止重试并报告变更失败。
          </li>

          <li>
            否则从 <code>Step 2 \<dedup-bounded-step-offset></code> 重试获取 <code>OFF1</code>，或放弃且不确定变更是否不会发生。
          </li>
        </ul>

        <p>
          例如仅创建某模板实例时，永远无法确定是否有在途提交稍后会被接受；尤其不得因未收到 <code>SUBMISSION\_ALREADY\_IN\_FLIGHT \<error\_code\_SUBMISSION\_ALREADY\_IN\_FLIGHT></code> 就认为安全——在途提交可能仍在队列中。
        </p>
      </td>
    </tr>
  </tbody>
</table>

命令去重错误处理（已知处理时间上界）

#### 失败场景

上述策略可能在以下情况失败：

1. **`B` 过低**：命令可能执行多次。原因包括：重试超过去重时长仍未得到有效答复（如 gRPC deadline 过短、Command Service 下 Daml 解释耗时长）、应用时钟与 participant/ledger 漂移、意外网络延迟、participant/ledger 内部重试未在 `B` 结束前停止等。

2. **不可接受的变更导致无限重试**：需业务知识判断不应再重试；也可停止重试并接受结果不确定。

### 未知处理时间上界

难以估计良好的 `B`，且可能有意外延迟超过 `B`。可用 **deduplication offset** 替代 duration 避免这些问题。offset 定义账本历史中的点，不受时钟偏移与网络延迟影响；但较不直观且对开发者要求更高。建议策略：

1. 为账本变更选择新 command ID 与 `actAs`（与应用 ID 组成 change ID），崩溃后记住 command ID。（同上文步骤 1）

2. 在 completion 流获取近期 offset `OFF0` 并记住与 command ID 关联。方式包括：

* State Service 的当前 ledger end。

  <Note>
    部分 ledger 实现会拒绝不对应提交方可见命令完成的去重 offset，返回 `INVALID_DEDUPLICATION_PERIOD`。ledger end 未必对应可见完成；此类 ledger 请用下述 Command Service 方式。
  </Note>

* 用 Command Service 反复提交哑命令（如单方模板的 Create-And-Exercise + Archive）直至成功，响应含 completion offset。

3. 使用 Command Completion Service 时：

   * 首次执行：设 `OFF1 = OFF0`
   * 错误处理从步骤 3 重试时：在 completion 流获取新的 `OFF1`（如当前 end）

4. 提交命令（同上文步骤 3，去重期使用 offset）：

   * command ID（步骤 1）
   * deduplication offset = `OFF0`
   * 新 submission ID
   * 与步骤 3 相同的 timeout 语义

5. 等待 RPC：

   * 非 `OK` 按错误处理
   * Command Service 且 `OK`：成功；响应含 completion offset 可供后续步骤 2 使用
   * Command Submission Service：从 `OFF1`（不含）订阅直至见到 change ID 与 submission ID 的完成；`OK` 则成功

#### 错误处理

与已知上界相同，但原「从步骤 2 重试」改为「从步骤 3 重试」。

#### 失败场景

1. **在支持的去重期内未成功**：收到 `INVALID_DEDUPLICATION_PERIOD` 时，无法在原先意图的去重期内再保证恰好一次。

2. **不可接受变更导致无限重试**：同前。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
