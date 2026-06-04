---
title: "/v2/commands/completions"
slug: "reference-json-api-reference-v2commandscompletions"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandscompletions.md"
source_title: "/v2/commands/completions"
tags:
  - reference
  - json-api-reference
  - v2commandscompletions
---

# /v2/commands/completions

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/commands/completions

> Query completions list (blocking call)

Subscribe to command completion events.
Notice: This endpoint should be used for small results set.
When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
there will be an error (`413 Content Too Large`) returned.
Increasing this limit may lead to performance issues and high memory consumption.
Consider using websockets (asyncapi) for better efficiency with larger results.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/completions
openapi: 3.0.3
info:
  title: JSON Ledger API HTTP endpoints
  version: 3.5.0-SNAPSHOT
  description: >-
    This specification version fixes the API inconsistencies where certain
    fields marked as required in the spec are in fact optional.

    If you use code generation tool based on this file, you might need to adjust
    the existing application code to handle those fields as optional.

    If you do not want to change your client code, continue using the OpenAPI
    specification for the latest Canton 3.4 patch release.

    MINIMUM_CANTON_VERSION=3.5.0
servers: []
security: []
paths:
  /v2/commands/completions:
    post:
      summary: /v2/commands/completions
      description: >-
        Query completions list (blocking call)


        Subscribe to command completion events.

        Notice: This endpoint should be used for small results set.

        When number of results exceeded node configuration limit
        (`http-list-max-elements-limit`)

        there will be an error (`413 Content Too Large`) returned.

        Increasing this limit may lead to performance issues and high memory
        consumption.

        Consider using websockets (asyncapi) for better efficiency with larger
        results.
      operationId: postV2CommandsCompletions
      parameters:
        - name: limit
          in: query
          description: >-
            maximum number of elements to return, this param is ignored if is
            bigger than server setting
          required: false
          schema:
            type: integer
            format: int64
        - name: stream_idle_timeout_ms
          in: query
          description: >-
            timeout to complete and send result if no new elements are received
            (for open ended streams)
          required: false
          schema:
            type: integer
            format: int64
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompletionStreamRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/CompletionStreamResponse'
        '400':
          description: >-
            Invalid value, Invalid value for: body, Invalid value for: query
            parameter limit, Invalid value for: query parameter
            stream_idle_timeout_ms
          content:
            text/plain:
              schema:
                type: string
        default:
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsCantonError'
      security:
        - httpAuth: []
        - apiKeyAuth: []
components:
  schemas:
    CompletionStreamRequest:
      title: CompletionStreamRequest
      type: object
      required:
        - parties
      properties:
        userId:
          description: >-
            Only completions of commands submitted with the same user_id will be
            visible in the stream.

            Must be a valid UserIdString (as described in ``value.proto``).


            Required unless authentication is used with a user token.

            In that case, the token's user-id will be used for the request's
            user_id.


            Optional
          type: string
        parties:
          description: >-
            Non-empty list of parties whose data should be included.

            The stream shows only completions of commands for which at least one
            of the ``act_as`` parties is in the given set of parties.

            Must be a valid PartyIdString (as described in ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        beginExclusive:
          description: >-
            This optional field indicates the minimum offset for completions.
            This can be used to resume an earlier completion stream.

            If not set the ledger uses the ledger begin offset instead.

            If specified, it must be a valid absolute offset (positive integer)
            or zero (ledger begin offset).

            If the ledger has been pruned, this parameter must be specified and
            greater than the pruning offset.


            Optional
          type: integer
          format: int64
    CompletionStreamResponse:
      title: CompletionStreamResponse
      type: object
      properties:
        completionResponse:
          $ref: '#/components/schemas/CompletionResponse'
    JsCantonError:
      title: JsCantonError
      type: object
      required:
        - code
        - cause
        - context
        - errorCategory
      properties:
        code:
          type: string
        cause:
          type: string
        correlationId:
          type: string
        traceId:
          type: string
        context:
          $ref: '#/components/schemas/Map_String'
        resources:
          type: array
          items:
            $ref: '#/components/schemas/Tuple2_String_String'
        errorCategory:
          type: integer
          format: int32
        grpcCodeValue:
          type: integer
          format: int32
        retryInfo:
          type: string
        definiteAnswer:
          type: boolean
    CompletionResponse:
      title: CompletionResponse
      description: Required
      oneOf:
        - type: object
          required:
            - Completion
          properties:
            Completion:
              $ref: '#/components/schemas/Completion'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty4'
        - type: object
          required:
            - OffsetCheckpoint
          properties:
            OffsetCheckpoint:
              $ref: '#/components/schemas/OffsetCheckpoint'
    Map_String:
      title: Map_String
      type: object
      additionalProperties:
        type: string
    Tuple2_String_String:
      title: Tuple2_String_String
      type: array
      maxItems: 2
      minItems: 2
      items:
        type: string
    Completion:
      title: Completion
      description: >-
        A completion represents the status of a submitted command on the ledger:
        it can be successful or failed.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Completion1'
    Empty4:
      title: Empty
      type: object
    OffsetCheckpoint:
      title: OffsetCheckpoint
      description: |-
        OffsetCheckpoints may be used to:

        - detect time out of commands.
        - provide an offset which can be used to restart consumption.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/OffsetCheckpoint1'
    Completion1:
      title: Completion
      description: >-
        A completion represents the status of a submitted command on the ledger:
        it can be successful or failed.
      type: object
      required:
        - commandId
        - userId
        - offset
        - actAs
        - synchronizerTime
      properties:
        commandId:
          description: |-
            The ID of the succeeded or failed command.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        status:
          $ref: '#/components/schemas/JsStatus'
          description: >-
            Identifies the exact type of the error.

            It uses the same format of conveying error details as it is used for
            the RPC responses of the APIs.


            Optional
        updateId:
          description: >-
            The update_id of the transaction or reassignment that resulted from
            the command with command_id.


            Only set for successfully executed commands.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        userId:
          description: >-
            The user-id that was used for the submission, as described in
            ``commands.proto``.

            Must be a valid UserIdString (as described in ``value.proto``).


            Required
          type: string
        actAs:
          description: >-
            The set of parties on whose behalf the commands were executed.

            Contains the ``act_as`` parties from ``commands.proto``

            filtered to the requesting parties in CompletionStreamRequest.

            The order of the parties need not be the same as in the submission.

            Each element must be a valid PartyIdString (as described in
            ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        submissionId:
          description: >-
            The submission ID this completion refers to, as described in
            ``commands.proto``.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        deduplicationPeriod:
          $ref: '#/components/schemas/DeduplicationPeriod1'
        traceContext:
          $ref: '#/components/schemas/TraceContext'
          description: >-
            The Ledger API trace context


            The trace context transported in this message corresponds to the
            trace context supplied

            by the client application in a HTTP2 header of the original command
            submission.

            We typically use a header to transfer this type of information. Here
            we use message

            body, because it is used in gRPC streams which do not support per
            message headers.

            This field will be populated with the trace context contained in the
            original submission.

            If that was not provided, a unique ledger-api-server generated trace
            context will be used

            instead.


            Optional
        offset:
          description: >-
            May be used in a subsequent CompletionStreamRequest to resume the
            consumption of this stream at a later time.

            Must be a valid absolute offset (positive integer).


            Required
          type: integer
          format: int64
        synchronizerTime:
          $ref: '#/components/schemas/SynchronizerTime'
          description: >-
            The synchronizer along with its record time.

            The synchronizer id provided, in case of


            - successful/failed transactions: identifies the synchronizer of the
            transaction

            - for successful/failed unassign commands: identifies the source
            synchronizer

            - for successful/failed assign commands: identifies the target
            synchronizer


            Required
        paidTrafficCost:
          description: >-
            The traffic cost paid by this participant node for the confirmation
            request

            for the submitted command.


            Commands whose execution is rejected before their corresponding

            confirmation request is ordered by the synchronizer will report a
            paid

            traffic cost of zero.

            If a confirmation request is ordered for a command, but the request
            fails

            (e.g., due to contention with a concurrent contract archival), the
            traffic

            cost is paid and reported on the failed completion for the request.


            If you want to correlate the traffic cost of a successful completion

            with the transaction that resulted from the command, you can use the

            ``offset`` field to retrieve the transaction using

            ``UpdateService.GetUpdateByOffset`` on the same participant node; or
            alternatively use the ``update_id``

            field to retrieve the transaction using
            ``UpdateService.GetUpdateById`` on any participant node

            that sees the transaction.


            Note: for completions processed before the participant started
            serving

            traffic cost on the Ledger API, this field will be set to zero.

            Additionally, the total cost incurred by the submitting node for the
            submission of the transaction may be greater

            than the reported cost, for example if retries were issued due to
            failed submissions to the synchronizer.

            The cost reported here is the one paid for ordering the confirmation
            request.


            Optional
          type: integer
          format: int64
    OffsetCheckpoint1:
      title: OffsetCheckpoint
      description: |-
        OffsetCheckpoints may be used to:

        - detect time out of commands.
        - provide an offset which can be used to restart consumption.
      type: object
      required:
        - offset
      properties:
        offset:
          description: >-
            The participant's offset, the details of the offset field are
            described in ``community/ledger-api/README.md``.

            Must be a valid absolute offset (positive integer).


            Required
          type: integer
          format: int64
        synchronizerTimes:
          description: |-
            The times associated with each synchronizer at this offset.

            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/SynchronizerTime'
    JsStatus:
      title: JsStatus
      type: object
      required:
        - code
        - message
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
        details:
          type: array
          items:
            $ref: '#/components/schemas/ProtoAny'
    DeduplicationPeriod1:
      title: DeduplicationPeriod
      description: >-
        The actual deduplication window used for the submission, which is
        derived from

        ``Commands.deduplication_period``. The ledger may convert the
        deduplication period into other

        descriptions and extend the period in implementation-specified ways.


        Used to audit the deduplication guarantee described in
        ``commands.proto``.


        The deduplication guarantee applies even if the completion omits this
        field.


        Optional
      oneOf:
        - type: object
          required:
            - DeduplicationDuration
          properties:
            DeduplicationDuration:
              $ref: '#/components/schemas/DeduplicationDuration1'
        - type: object
          required:
            - DeduplicationOffset
          properties:
            DeduplicationOffset:
              $ref: '#/components/schemas/DeduplicationOffset1'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty3'
    TraceContext:
      title: TraceContext
      type: object
      properties:
        traceparent:
          description: |-
            https://www.w3.org/TR/trace-context/

            Optional
          type: string
        tracestate:
          description: Optional
          type: string
    SynchronizerTime:
      title: SynchronizerTime
      type: object
      required:
        - synchronizerId
        - recordTime
      properties:
        synchronizerId:
          description: |-
            The id of the synchronizer.

            Required
          type: string
        recordTime:
          description: >-
            All commands with a maximum record time below this value MUST be
            considered lost if their completion has not arrived before this
            checkpoint.


            Required
          type: string
    ProtoAny:
      title: ProtoAny
      type: object
      required:
        - typeUrl
        - value
        - unknownFields
      properties:
        typeUrl:
          type: string
        value:
          type: string
        unknownFields:
          $ref: '#/components/schemas/UnknownFieldSet'
        valueDecoded:
          type: string
    DeduplicationDuration1:
      title: DeduplicationDuration
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Duration'
    DeduplicationOffset1:
      title: DeduplicationOffset
      type: object
      required:
        - value
      properties:
        value:
          type: integer
          format: int64
    Empty3:
      title: Empty
      type: object
    UnknownFieldSet:
      title: UnknownFieldSet
      type: object
      required:
        - fields
      properties:
        fields:
          $ref: '#/components/schemas/Map_Int_Field'
    Duration:
      title: Duration
      type: object
      required:
        - seconds
        - nanos
      properties:
        seconds:
          type: integer
          format: int64
        nanos:
          type: integer
          format: int32
        unknownFields:
          $ref: '#/components/schemas/UnknownFieldSet'
          description: >-
            This field is automatically added as part of protobuf to json
            mapping
    Map_Int_Field:
      title: Map_Int_Field
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Field'
    Field:
      title: Field
      type: object
      properties:
        varint:
          type: array
          items:
            type: integer
            format: int64
        fixed64:
          type: array
          items:
            type: integer
            format: int64
        fixed32:
          type: array
          items:
            type: integer
            format: int32
        lengthDelimited:
          type: array
          items:
            type: string
  securitySchemes:
    httpAuth:
      type: http
      description: Ledger API standard JWT token
      scheme: bearer
    apiKeyAuth:
      type: apiKey
      description: Ledger API standard JWT token (websocket)
      name: Sec-WebSocket-Protocol
      in: header

````

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
