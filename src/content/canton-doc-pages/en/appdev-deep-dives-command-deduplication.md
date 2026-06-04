---
title: "Command Deduplication"
slug: "appdev-deep-dives-command-deduplication"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/command-deduplication.md"
source_title: "Command Deduplication"
tags:
  - appdev
  - deep-dives
  - command-deduplication
---

# Command Deduplication

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Command Deduplication

> How Daml command deduplication works and how applications can use it to achieve exactly-once ledger changes.

The interaction of a Daml application with the ledger is inherently asynchronous: applications send commands to the ledger, and some time later they see the effect of that command on the ledger. Many things can fail during this time window:

* The application can crash.
* The participant node can crash.
* Messages can be lost on the network.
* The ledger may be slow to respond due to a high load.

If you want to make sure that an intended ledger change is not executed twice, your application needs to robustly handle all failure scenarios. This guide covers the following topics:

* How command deduplication works.
* How applications can effectively use the command deduplication.

## How Command Deduplication Works

The following fields in a command submissions are relevant for command deduplication. The first three form the change ID that identifies the intended ledger change.

* The act\_as define the submitting parties.
* The user ID identifies the user that submits the command.
* The command ID is chosen by the user to identify the intended ledger change.
* The deduplication period specifies the period for which no earlier submissions with the same change ID should have been accepted, as witnessed by a completion event on the Command Completion Service. If such a change has been accepted in that period, the current submission shall be rejected. The period is specified either as a deduplication duration or as a deduplication offset (inclusive).
* The submission ID is chosen by the application to identify a specific submission. It is included in the corresponding completion event so that the application can correlate specific submissions to specific completions. An application should never reuse a submission ID.

The ledger may arbitrarily extend the deduplication period specified in the submission.

<Note>
  The maximum deduplication duration is the length of the deduplication period guaranteed to be supported by the participant.
</Note>

The deduplication period chosen by the ledger is the *effective deduplication period*. The ledger may also convert a requested deduplication duration into an effective deduplication offset or vice versa. The effective deduplication period is reported in the command completion event in the deduplication duration or deduplication offset fields.

A command submission is considered a **duplicate submission** if at least one of the following holds:

* The submitting participant's completion service contains a successful completion event for the same change ID within the *effective* deduplication period.
* The participant or Daml ledger are aware of another command submission in-flight with the same change ID when they perform command deduplication.

The outcome of command deduplication is communicated as follows:

* Command submissions via the Command Service indicate the command deduplication outcome as a synchronous gRPC response unless the [gRPC deadline](https://grpc.io/blog/deadlines/) was exceeded. (Note: the outcome MAY additionally appear as a completion event on the Command Completion Service, but applications using the Command Service typically need not process completion events.)

* Command submissions via the Command Submission Service can indicate the outcome as a synchronous gRPC response, or asynchronously through the Command Completion Service. In particular, the submission may be a duplicate even if the Command Submission Service acknowledges the submission with the gRPC status code `OK`.

Independently of how the outcome is communicated, command deduplication generates the following outcomes of a command submission:

* If there is no conflicting submission with the same change ID on the Daml ledger or in-flight, the completion event and possibly the response convey the result of the submission (success or a gRPC error; `error_codes` explains how errors are communicated).

* The gRPC status code `ALREADY_EXISTS` with error code ID DUPLICATE\_COMMAND indicates that there is an earlier command completion for the same change ID within the effective deduplication period.

* The gRPC status code `ABORTED` with error code id SUBMISSION\_ALREADY\_IN\_FLIGHT indicates that another submission for the same change ID was in flight when this submission was processed.

* The gRPC status code `FAILED_PRECONDITION` with error code id INVALID\_DEDUPLICATION\_PERIOD indicates that the specified deduplication period is not supported. The fields `longest_duration` or `earliest_offset` in the metadata specify the longest duration or earliest offset that is currently supported on the Ledger API endpoint. At least one of the two fields is present.

  Neither deduplication durations up to the maximum deduplication duration configured nor deduplication offsets published within that duration SHOULD result in this error. Participants may accept longer periods at their discretion.

* The gRPC status code `FAILED_PRECONDITION` with error code id PARTICIPANT\_PRUNED\_DATA\_ACCESSED, when specifying a deduplication period represented by an offset, indicates that the specified deduplication offset has been pruned. The field `earliest_offset` in the metadata specifies the last pruned offset.

For deduplication to work as intended, all submissions for the same ledger change must be submitted via the same participant. Whether a submission is considered a duplicate is determined by completion events, and by default a participant outputs only the completion events for submissions that were requested via the very same participant.

## How to Use Command Deduplication

To effectuate a ledger change exactly once, the application must resubmit a command if an earlier submission was lost. However, the application typically cannot distinguish a lost submission from slow submission processing by the ledger. Command deduplication allows the application to resubmit the command until it is executed and reject all duplicate submissions thereafter.

Some ledger changes can be executed at most once, so no command deduplication is needed for them. For example, if the submitted command exercises a consuming choice on a given contract ID, this command can be accepted at most once because every contract can be archived at most once. All duplicate submissions of such a change will be rejected with CONTRACT\_NOT\_ACTIVE.

In contrast, a Create command would create a fresh contract instance of the given template for each submission that reaches the ledger (unless other constraints such as the template preconditions or contract key uniqueness are violated). Similarly, an Exercise command on a non-consuming choice or an Exercise-By-Key command may be executed multiple times if submitted multiple times. With command deduplication, applications can ensure such intended ledger changes are executed only once within the deduplication period, even if the application resubmits, say because it considers the earlier submissions to be lost or forgot during a crash that it had already submitted the command.

### Known Processing Time Bounds

For this strategy, you must estimate a bound `B` on the processing time and forward clock drifts in the Daml ledger with respect to the application’s clock. If processing measured across all retries takes longer than your estimate `B`, the ledger change may take effect several times. Under this caveat, the following strategy works for applications that use the Command Service or the Command Submission and Command Completion Service.

<Note>
  The bound `B` should be at most the configured maximum deduplication duration. Otherwise you rely on the ledger accepting longer deduplication durations. Such reliance makes your application harder to port to other Daml ledgers and fragile, as the ledger may stop accepting such extended durations at its own discretion.
</Note>

1. Choose a command ID for the ledger change, in a way that makes sure the same ledger change is always assigned the same command ID. Either determine the command ID deterministically (e.g., if your contract payload contains a globally unique identifier, you can use that as your command ID), or choose the command ID randomly and persist it with the ledger change so that the application can use the same command ID in resubmissions after a crash and restart. (Note: make sure that you assign the same command ID to all command (re-)submissions of the same ledger change. This is useful for the recovery procedure after an application crash/restart. After a crash, the application in general cannot know whether it has submitted a set of commands before the crash. If in doubt, resubmit the commands using the same command ID. If the commands had been submitted before the crash, command deduplication on the ledger will reject the resubmissions.)

2. When you use the Command Submission Service, obtain a recent offset on the State Service `OFF1`, say the current ledger end.

3. Submit the command with the following parameters:

   * Set the command ID to the chosen command ID from Step 1.

   * Set the deduplication duration to the bound `B`. (Note: it is prudent to explicitly set the deduplication duration to the desired bound `B`, to guard against the case where a ledger configuration update shortens the maximum deduplication duration. With the bound `B`, you will be notified of such a problem via an INVALID\_DEDUPLICATION\_PERIOD error if the ledger does not support deduplication durations of length `B` any more. If you omitted the deduplication period, the currently valid maximum deduplication duration would be used. In this case, a ledger configuration update could silently shorten the deduplication period and thus invalidate your deduplication analysis.)

   * Set the submission ID to a fresh value, e.g., a random UUID.

   * Set the timeout (gRPC deadline) to the expected submission processing time (Command Service) or submission hand-off time (Command Submission Service).

     The **submission processing time** is the time between when the application sends off a submission to the Command Service and when it receives (synchronously, unless it times out) the acceptance or rejection. The **submission hand-off time** is the time between when the application sends off a submission to the Command Submission Service and when it obtains a synchronous response for this gRPC call. After the RPC timeout, the application considers the submission as lost and enters a retry loop. This timeout is typically much shorter than the deduplication duration.

4. Wait until the RPC call returns a response.

   * Status codes other than `OK` should be handled according to error handling.

   * When you use the Command Service and the response carries the status code `OK`, the ledger change took place. You can report success.

   * When you use the Command Submission Service, subscribe with the Command Completion Service for completions for `actAs` from `OFF1` (exclusive) until you see a completion event for the change ID and the submission ID chosen in Step 3. If the completion’s status is `OK`, the ledger change took place and you can report success. Other status codes should be handled according to error handling.

     This step needs no timeout as the Command Submission Service acknowledges a submission only if there will eventually be a completion event, unless relevant parts of the system become permanently unavailable.

#### Error Handling

Error handling is needed when the status code of the command submission RPC call or in the completion event is not `OK`. The following table lists appropriate reactions by status code (written as `STATUS_CODE`) and error code (written in capital letters with a link to the error code documentation). Fields in the error metadata are written as `field` in lowercase letters.

<table>
  <caption>Command deduplication error handling with known processing time bound</caption>

  <colgroup>
    <col style={{ width: "16%" }} />

    <col style={{ width: "83%" }} />
  </colgroup>

  <thead>
    <tr className="header">
      <th>Error condition</th>
      <th>Reaction</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td>
        <code>DEADLINE\_EXCEEDED</code>
      </td>

      <td>
        <p>Consider the submission lost.</p>

        <p>
          Retry from <code>Step 2 \<dedup-bounded-step-offset></code>, obtaining the
          completion offset <code>OFF1</code>, and possibly increase the timeout.
        </p>
      </td>
    </tr>

    <tr className="even">
      <td>Application crashed</td>

      <td>
        Retry from <code>Step 2 \<dedup-bounded-step-offset></code>, obtaining the
        completion offset <code>OFF1</code>.
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>ALREADY\_EXISTS</code> / <code>DUPLICATE\_COMMAND \<error\_code\_DUPLICATE\_COMMAND></code>
      </td>

      <td>
        The change ID has already been accepted by the ledger within the reported deduplication
        period. The optional field <code>completion\_offset</code> contains the precise offset. The
        optional field <code>existing\_submission\_id</code> contains the submission ID of the
        successful submission. Report success for the ledger change.
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>FAILED\_PRECONDITION</code> /{" "}
        <code>PARTICIPANT\_PRUNED\_DATA\_ACCESSED \<error\_code\_PARTICIPANT\_PRUNED\_DATA\_ACCESSED></code>
      </td>

      <td>
        <p>
          The specified deduplication offset has been pruned by the participant.{" "}
          <code>earliest\_offset</code> contains the last pruned offset.
        </p>

        <p>
          Use the <code>Command Completion Service \<command-completion-service></code> by
          asking for the{" "}
          <code>completions \<com.daml.ledger.api.v2.CompletionStreamRequest></code>,
          starting from the last pruned offset by setting{" "}
          <code>offset \<com.daml.ledger.api.v2.CompletionStreamRequest.begin\_exclusive></code>{" "}
          to the value of <code>earliest\_offset</code>, and use the first received{" "}
          <code>completion offset \<com.daml.ledger.api.v2.Completion.offset></code> or{" "}
          <code>checkpoint offset \<com.daml.ledger.api.v2.OffsetCheckpoint.offset></code> as
          a deduplication offset.
        </p>
      </td>
    </tr>

    <tr className="odd">
      <td>
        <code>ABORTED</code> / other error codes
      </td>

      <td>
        Wait a bit and retry from <code>Step 2 \<dedup-bounded-step-offset></code>,
        obtaining the completion offset <code>OFF1</code>.
      </td>
    </tr>

    <tr className="even">
      <td>Other error conditions</td>

      <td>
        <p>
          Use background knowledge about the business workflow and the current ledger state to
          decide whether earlier submissions might still get accepted.
        </p>

        <ul>
          <li>
            If you conclude that it cannot be accepted any more, stop retrying and report that the
            ledger change failed.
          </li>

          <li>
            Otherwise, retry from <code>Step 2 \<dedup-bounded-step-offset></code>, obtaining
            a completion offset <code>OFF1</code>, or give up without knowing for sure that the
            ledger change will not happen.
          </li>
        </ul>

        <p>
          For example, if the ledger change only creates a contract instance of a template, you can
          never be sure, as any outstanding submission might still be accepted on the ledger. In
          particular, you must not draw any conclusions from not having received a{" "}
          <code>SUBMISSION\_ALREADY\_IN\_FLIGHT \<error\_code\_SUBMISSION\_ALREADY\_IN\_FLIGHT></code>{" "}
          error, because the outstanding submission may be queued somewhere and will reach the
          relevant processing point only later.
        </p>
      </td>
    </tr>
  </tbody>
</table>

Command deduplication error handling with known processing time bound

#### Failure Scenarios

The above strategy can fail in the following scenarios:

1. The bound `B` is too low: The command can be executed multiple times.

   Possible causes:

   * You have retried for longer than the deduplication duration, but never got a meaningful answer, e.g., because the timeout (gRPC deadline) is too short. For example, this can happen due to long-running Daml interpretation when using the Command Service.
   * The application clock drifts significantly from the participant's or ledger's clock.
   * There are unexpected network delays.
   * Submissions are retried internally in the participant or Daml ledger and those retries do not stop before `B` is over. Refer to the specific ledger's documentation for more information.

2. Unacceptable changes cause infinite retries

   You need business workflow knowledge to decide that retrying does not make sense any more. Of course, you can always stop retrying and accept that you do not know the outcome for sure.

### Unknown Processing Time Bounds

Finding a good bound `B` on the processing time is hard, and there may still be unforeseen circumstances that delay processing beyond the chosen bound `B`. You can avoid these problems by using deduplication offsets instead of durations. An offset defines a point in the history of the ledger and is thus not affected by clock skews and network delays. Offsets are arguably less intuitive and require more effort by the application developer. We recommend the following strategy for using deduplication offsets:

1. Choose a fresh command ID for the ledger change and the `actAs` parties, which (together with the application ID) determine the change ID. Remember the command ID across application crashes. (Analogous to Step 1 above)

2. Obtain a recent offset `OFF0` on the completion stream and remember across crashes that you use `OFF0` with the chosen command ID. There are several ways to do so:

* Use the State Service by asking for the current ledger end.

  <Note>
    Some ledger implementations reject deduplication offsets that do not identify a command
    completion visible to the submitting parties with the error code id
    <code> INVALID\_DEDUPLICATION\_PERIOD</code>. In general, the ledger end need not identify a
    command completion that is visible to the submitting parties. When running on such a ledger,
    use the Command Service approach described next.
  </Note>

* Use the Command Service to obtain a recent offset by repeatedly submitting a dummy command, e.g.,
  a Create-And-Exercise command of some single-signatory template with the Archive choice, until
  you get a successful response. The response contains the completion offset.

3. When you use the Command Completion Service:

   * If you execute this step the first time, set `OFF1 = OFF0`.
   * If you execute this step as part of error handling retrying from Step 3, obtaining the completion offset `OFF1`, obtain a recent offset on the completion stream `OFF1`, say its current end. (Analogous to step 2 above)

4. Submit the command with the following parameters (analogous to Step 3 above except for the deduplication period):

   * Set the command ID to the chosen command ID from Step 1.
   * Set the deduplication offset to `OFF0`.
   * Set the submission ID to a fresh value, e.g., a random UUID.
   * Set the timeout (gRPC deadline) to the expected submission processing time (Command Service) or submission hand-off time (Command Submission Service).

5. Wait until the RPC call returns a response.

   * Status codes other than `OK` should be handled according to error handling.
   * When you use the Command Service and the response carries the status code `OK`, the ledger change took place. You can report success. The response contains a completion offset that you can use in Step 2 of later submissions.
   * When you use the Command Submission Service, subscribe with the Command Completion Service for completions for `actAs` from `OFF1` (exclusive) until you see a completion event for the change ID and the submission ID chosen in step 3. If the completion’s status is `OK`, the ledger change took place and you can report success. Other status codes should be handled according to error handling.

#### Error Handling

The same as for known bounds, except that the former retry from Step 2 becomes retry from Step 3.

#### Failure Scenarios

The above strategy can fail in the following scenarios:

1. No success within the supported deduplication period

   When the application receives a INVALID\_DEDUPLICATION\_PERIOD error, it cannot achieve exactly once execution any more within the originally intended deduplication period.

2. Unacceptable changes cause infinite retries

   You need business workflow knowledge to decide that retrying does not make sense any more. Of course, you can always stop retrying and accept that you do not know the outcome for sure.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
