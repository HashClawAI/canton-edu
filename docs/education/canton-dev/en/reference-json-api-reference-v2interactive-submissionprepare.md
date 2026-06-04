---
title: "/v2/interactive-submission/prepare"
slug: "reference-json-api-reference-v2interactive-submissionprepare"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionprepare.md"
source_title: "/v2/interactive-submission/prepare"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionprepare
---

# /v2/interactive-submission/prepare

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/interactive-submission/prepare

> Requires `readAs` scope for the submitting party when LAPI User authorization is enabled



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/prepare
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
  /v2/interactive-submission/prepare:
    post:
      summary: /v2/interactive-submission/prepare
      description: >-
        Requires `readAs` scope for the submitting party when LAPI User
        authorization is enabled
      operationId: postV2Interactive-submissionPrepare
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JsPrepareSubmissionRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsPrepareSubmissionResponse'
        '400':
          description: 'Invalid value, Invalid value for: body'
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
    JsPrepareSubmissionRequest:
      title: JsPrepareSubmissionRequest
      type: object
      required:
        - commandId
        - commands
        - actAs
      properties:
        userId:
          description: >-
            Uniquely identifies the participant user that prepares the
            transaction.

            Must be a valid UserIdString (as described in ``value.proto``).

            Required unless authentication is used with a user token.

            In that case, the token's user-id will be used for the request's
            user_id.


            Optional
          type: string
        commandId:
          description: >-
            Uniquely identifies the command.

            The triple (user_id, act_as, command_id) constitutes the change ID
            for the intended ledger change,

            where act_as is interpreted as a set of party names.

            The change ID can be used for matching the intended ledger changes
            with all their completions.

            Must be a valid LedgerString (as described in ``value.proto``).


            Required
          type: string
        commands:
          description: >-
            Individual elements of this atomic command. Must be non-empty.

            Limitation: Only single command transaction are currently supported
            by the API.

            The field is marked as repeated in preparation for future support of
            multiple commands.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/Command'
        minLedgerTime:
          $ref: '#/components/schemas/MinLedgerTime'
          description: Optional
        actAs:
          description: >-
            Set of parties on whose behalf the command should be executed, if
            submitted.

            If ledger API authorization is enabled, then the authorization
            metadata must authorize the sender of the request

            to **read** (not act) on behalf of each of the given parties. This
            is because this RPC merely prepares a transaction

            and does not execute it. Therefore read authorization is sufficient
            even for actAs parties.

            Note: This may change, and more specific authorization scope may be
            introduced in the future.

            Each element must be a valid PartyIdString (as described in
            ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        readAs:
          description: >-
            Set of parties on whose behalf (in addition to all parties listed in
            ``act_as``) contracts can be retrieved.

            This affects Daml operations such as ``fetch``, ``fetchByKey``,
            ``lookupByKey``, ``exercise``, and ``exerciseByKey``.

            Note: A command can only use contracts that are visible to at least

            one of the parties in ``act_as`` or ``read_as``. This visibility
            check is independent from the Daml authorization

            rules for fetch operations.

            If ledger API authorization is enabled, then the authorization
            metadata must authorize the sender of the request

            to read contract data on behalf of each of the given parties.


            Optional: can be empty
          type: array
          items:
            type: string
        disclosedContracts:
          description: >-
            Additional contracts used to resolve contract & contract key
            lookups.


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/DisclosedContract'
        synchronizerId:
          description: >-
            Must be a valid synchronizer id

            If not set, a suitable synchronizer that this node is connected to
            will be chosen


            Optional
          type: string
        packageIdSelectionPreference:
          description: >-
            The package-id selection preference of the client for resolving

            package names and interface instances in command submission and
            interpretation


            Optional: can be empty
          type: array
          items:
            type: string
        verboseHashing:
          description: >-
            When true, the response will contain additional details on how the
            transaction was encoded and hashed

            This can be useful for troubleshooting of hash mismatches. Should
            only be used for debugging.

            Defaults to false


            Optional
          type: boolean
        prefetchContractKeys:
          description: >-
            Fetches the contract keys into the caches to speed up the command
            processing.

            Should only contain contract keys that are expected to be resolved
            during interpretation of the commands.

            Keys of disclosed contracts do not need prefetching.


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/PrefetchContractKey'
        maxRecordTime:
          description: >-
            Maximum timestamp at which the transaction can be recorded onto the
            ledger via the synchronizer specified in the
            `PrepareSubmissionResponse`.

            If submitted after it will be rejected even if otherwise valid, in
            which case it needs to be prepared and signed again

            with a new valid max_record_time.

            Use this to limit the time-to-life of a prepared transaction,

            which is useful to know when it can definitely not be accepted

            anymore and resorting to preparing another transaction for the same

            intent is safe again.


            Optional
          type: string
        estimateTrafficCost:
          $ref: '#/components/schemas/CostEstimationHints'
          description: >-
            Hints to improve the accuracy of traffic cost estimation.

            The estimation logic assumes that this node will be used for the
            execution of the transaction

            If another node is used instead, the estimation may be less precise.

            Request amplification is not accounted for in the estimation: each
            amplified request will

            result in the cost of the confirmation request to be charged
            additionally.


            Traffic cost estimation is enabled by default if this field is not
            set

            To turn off cost estimation, set the CostEstimationHints#disabled
            field to true


            Optional
        tapsMaxPasses:
          description: >-
            The maximum number of passes for the Topology-Aware Package
            Selection (TAPS).

            Higher values can increase the chance of successful package
            selection for routing of interpreted transactions.

            If unset, this defaults to the value defined in the participant
            configuration.

            The provided value must not exceed the limit specified in the
            participant configuration.


            Optional
          type: integer
          format: int32
        hashingSchemeVersion:
          description: |-
            The hashing scheme version to be used when building the hash.
            Defaults to HASHING_SCHEME_VERSION_V2.

            Optional
          type: string
          enum:
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
    JsPrepareSubmissionResponse:
      title: JsPrepareSubmissionResponse
      description: '[docs-entry-end: HashingSchemeVersion]'
      type: object
      required:
        - preparedTransaction
        - preparedTransactionHash
        - hashingSchemeVersion
      properties:
        preparedTransaction:
          description: >-
            The interpreted transaction, it represents the ledger changes
            necessary to execute the commands specified in the request.

            Clients MUST display the content of the transaction to the user for
            them to validate before signing the hash if the preparing
            participant is not trusted.


            Required
          type: string
        preparedTransactionHash:
          description: >-
            Hash of the transaction, this is what needs to be signed by the
            party to authorize the transaction.

            Only provided for convenience, clients MUST recompute the hash from
            the raw transaction if the preparing participant is not trusted.

            May be removed in future versions


            Required: must be non-empty
          type: string
        hashingSchemeVersion:
          description: |-
            The hashing scheme version used when building the hash

            Required
          type: string
          enum:
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
        hashingDetails:
          description: >-
            Optional additional details on how the transaction was encoded and
            hashed. Only set if verbose_hashing = true in the request

            Note that there are no guarantees on the stability of the format or
            content of this field.

            Its content should NOT be parsed and should only be used for
            troubleshooting purposes.


            Optional
          type: string
        costEstimation:
          $ref: '#/components/schemas/CostEstimation'
          description: |-
            Traffic cost estimation of the prepared transaction

            Optional
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
    Command:
      title: Command
      description: >-
        A command can either create a new contract or exercise a choice on an
        existing contract.
      oneOf:
        - type: object
          required:
            - CreateAndExerciseCommand
          properties:
            CreateAndExerciseCommand:
              $ref: '#/components/schemas/CreateAndExerciseCommand'
        - type: object
          required:
            - CreateCommand
          properties:
            CreateCommand:
              $ref: '#/components/schemas/CreateCommand'
        - type: object
          required:
            - ExerciseByKeyCommand
          properties:
            ExerciseByKeyCommand:
              $ref: '#/components/schemas/ExerciseByKeyCommand'
        - type: object
          required:
            - ExerciseCommand
          properties:
            ExerciseCommand:
              $ref: '#/components/schemas/ExerciseCommand'
    MinLedgerTime:
      title: MinLedgerTime
      type: object
      properties:
        time:
          $ref: '#/components/schemas/Time'
    DisclosedContract:
      title: DisclosedContract
      description: |-
        An additional contract that is used to resolve
        contract & contract key lookups.
      type: object
      required:
        - createdEventBlob
      properties:
        templateId:
          description: >-
            The template id of the contract.

            The identifier uses the package-id reference format.


            If provided, used to validate the template id of the contract
            serialized in the created_event_blob.


            Optional
          type: string
        contractId:
          description: >-
            The contract id


            If provided, used to validate the contract id of the contract
            serialized in the created_event_blob.


            Optional
          type: string
        createdEventBlob:
          description: >-
            Opaque byte string containing the complete payload required by the
            Daml engine

            to reconstruct a contract not known to the receiving participant.


            Required: must be non-empty
          type: string
        synchronizerId:
          description: |-
            The ID of the synchronizer where the contract is currently assigned

            Optional
          type: string
    PrefetchContractKey:
      title: PrefetchContractKey
      description: Preload contracts
      type: object
      required:
        - templateId
        - contractKey
      properties:
        templateId:
          description: >-
            The template of contract the client wants to prefetch.

            Both package-name and package-id reference identifier formats for
            the template-id are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        contractKey:
          description: |-
            The key of the contract the client wants to prefetch.

            Required
    CostEstimationHints:
      title: CostEstimationHints
      description: Hints to improve cost estimation precision of a prepared transaction
      type: object
      properties:
        disabled:
          description: |-
            Disable cost estimation
            Default (not set) is false

            Optional
          type: boolean
        expectedSignatures:
          description: >-
            Details on the keys that will be used to sign the transaction (how
            many and of which type).

            Signature size impacts the cost of the transaction.

            If empty, the signature sizes will be approximated with
            threshold-many signatures (where threshold is defined

            in the PartyToParticipant of the external party), using keys in the
            order they are registered.

            Empty list is equivalent to not providing this field


            Optional: can be empty
          type: array
          items:
            type: string
            enum:
              - SIGNING_ALGORITHM_SPEC_UNSPECIFIED
              - SIGNING_ALGORITHM_SPEC_ED25519
              - SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_256
              - SIGNING_ALGORITHM_SPEC_EC_DSA_SHA_384
    CostEstimation:
      title: CostEstimation
      description: >-
        Estimation of the cost of submitting the prepared transaction

        The estimation is done against the synchronizer chosen during
        preparation of the transaction

        (or the one explicitly requested).

        The cost of re-assigning contracts to another synchronizer when
        necessary is not included in the estimation.
      type: object
      required:
        - confirmationRequestTrafficCostEstimation
        - confirmationResponseTrafficCostEstimation
        - totalTrafficCostEstimation
        - estimationTimestamp
      properties:
        estimationTimestamp:
          description: |-
            Timestamp at which the estimation was made

            Required
          type: string
        confirmationRequestTrafficCostEstimation:
          description: >-
            Estimated traffic cost of the confirmation request associated with
            the transaction


            Required
          type: integer
          format: int64
        confirmationResponseTrafficCostEstimation:
          description: >-
            Estimated traffic cost of the confirmation response associated with
            the transaction

            This field can also be used as an indication of the cost that other
            potential confirming nodes

            of the party will incur to approve or reject the transaction


            Required
          type: integer
          format: int64
        totalTrafficCostEstimation:
          description: |-
            Sum of the fields above

            Required
          type: integer
          format: int64
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
    CreateAndExerciseCommand:
      title: CreateAndExerciseCommand
      description: Create a contract and exercise a choice on it in the same transaction.
      type: object
      required:
        - templateId
        - createArguments
        - choice
        - choiceArgument
      properties:
        templateId:
          description: >-
            The template of the contract the client wants to create.

            Both package-name and package-id reference identifier formats for
            the template-id are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        createArguments:
          description: |-
            The arguments required for creating a contract from this template.

            Required
        choice:
          description: |-
            The name of the choice the client wants to exercise.
            Must be a valid NameString (as described in ``value.proto``).

            Required
          type: string
        choiceArgument:
          description: |-
            The argument for this choice.

            Required
    CreateCommand:
      title: CreateCommand
      description: Create a new contract instance based on a template.
      type: object
      required:
        - templateId
        - createArguments
      properties:
        templateId:
          description: >-
            The template of contract the client wants to create.

            Both package-name and package-id reference identifier formats for
            the template-id are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        createArguments:
          description: |-
            The arguments required for creating a contract from this template.

            Required
    ExerciseByKeyCommand:
      title: ExerciseByKeyCommand
      description: Exercise a choice on an existing contract specified by its key.
      type: object
      required:
        - templateId
        - contractKey
        - choice
        - choiceArgument
      properties:
        templateId:
          description: >-
            The template of contract the client wants to exercise.

            Both package-name and package-id reference identifier formats for
            the template-id are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        contractKey:
          description: |-
            The key of the contract the client wants to exercise upon.

            Required
        choice:
          description: |-
            The name of the choice the client wants to exercise.
            Must be a valid NameString (as described in ``value.proto``)

            Required
          type: string
        choiceArgument:
          description: |-
            The argument for this choice.

            Required
    ExerciseCommand:
      title: ExerciseCommand
      description: Exercise a choice on an existing contract.
      type: object
      required:
        - templateId
        - contractId
        - choice
        - choiceArgument
      properties:
        templateId:
          description: >-
            The template or interface of the contract the client wants to
            exercise.

            Both package-name and package-id reference identifier formats for
            the template-id are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.

            To exercise a choice on an interface, specify the interface
            identifier in the template_id field.


            Required
          type: string
        contractId:
          description: |-
            The ID of the contract the client wants to exercise upon.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        choice:
          description: |-
            The name of the choice the client wants to exercise.
            Must be a valid NameString (as described in ``value.proto``)

            Required
          type: string
        choiceArgument:
          description: |-
            The argument for this choice.

            Required
    Time:
      title: Time
      description: Required
      oneOf:
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty9'
        - type: object
          required:
            - MinLedgerTimeAbs
          properties:
            MinLedgerTimeAbs:
              $ref: '#/components/schemas/MinLedgerTimeAbs'
        - type: object
          required:
            - MinLedgerTimeRel
          properties:
            MinLedgerTimeRel:
              $ref: '#/components/schemas/MinLedgerTimeRel'
    Empty9:
      title: Empty
      type: object
    MinLedgerTimeAbs:
      title: MinLedgerTimeAbs
      type: object
      required:
        - value
      properties:
        value:
          type: string
    MinLedgerTimeRel:
      title: MinLedgerTimeRel
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Duration'
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
    UnknownFieldSet:
      title: UnknownFieldSet
      type: object
      required:
        - fields
      properties:
        fields:
          $ref: '#/components/schemas/Map_Int_Field'
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
