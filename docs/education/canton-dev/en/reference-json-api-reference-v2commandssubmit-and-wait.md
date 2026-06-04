---
title: "/v2/commands/submit-and-wait"
slug: "reference-json-api-reference-v2commandssubmit-and-wait"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandssubmit-and-wait.md"
source_title: "/v2/commands/submit-and-wait"
tags:
  - reference
  - json-api-reference
  - v2commandssubmit-and-wait
---

# /v2/commands/submit-and-wait

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/commands/submit-and-wait

> Submits a single composite command and waits for its result.
Propagates the gRPC error of failed submissions including Daml interpretation errors.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/submit-and-wait
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
  /v2/commands/submit-and-wait:
    post:
      summary: /v2/commands/submit-and-wait
      description: >-
        Submits a single composite command and waits for its result.

        Propagates the gRPC error of failed submissions including Daml
        interpretation errors.
      operationId: postV2CommandsSubmit-and-wait
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JsCommands'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmitAndWaitResponse'
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
    JsCommands:
      title: JsCommands
      description: A composite command that groups multiple commands together.
      type: object
      required:
        - commandId
        - commands
        - actAs
      properties:
        commands:
          description: |-
            Individual elements of this atomic command. Must be non-empty.

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/Command'
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
        actAs:
          description: >-
            Set of parties on whose behalf the command should be executed.

            If ledger API authorization is enabled, then the authorization
            metadata must authorize the sender of the request

            to act on behalf of each of the given parties.

            Each element must be a valid PartyIdString (as described in
            ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        userId:
          description: >-
            Uniquely identifies the participant user that issued the command.

            Must be a valid UserIdString (as described in ``value.proto``).

            Required unless authentication is used with a user token.

            In that case, the token's user-id will be used for the request's
            user_id.


            Optional
          type: string
        readAs:
          description: >-
            Set of parties on whose behalf (in addition to all parties listed in
            ``act_as``) contracts can be retrieved.

            This affects Daml operations such as ``fetch``, ``fetchByKey``,
            ``lookupByKey``, ``exercise``, and ``exerciseByKey``.

            Note: A participant node of a Daml network can host multiple
            parties. Each contract present on the participant

            node is only visible to a subset of these parties. A command can
            only use contracts that are visible to at least

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
        workflowId:
          description: |-
            Identifier of the on-ledger workflow that this command is a part of.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
          type: string
        deduplicationPeriod:
          $ref: '#/components/schemas/DeduplicationPeriod'
        minLedgerTimeAbs:
          description: >-
            Lower bound for the ledger time assigned to the resulting
            transaction.

            Note: The ledger time of a transaction is assigned as part of
            command interpretation.

            Use this property if you expect that command interpretation will
            take a considerate amount of time, such that by

            the time the resulting transaction is sequenced, its assigned ledger
            time is not valid anymore.

            Must not be set at the same time as min_ledger_time_rel.


            Optional
          type: string
        minLedgerTimeRel:
          $ref: '#/components/schemas/Duration'
          description: >-
            Same as min_ledger_time_abs, but specified as a duration, starting
            from the time the command is received by the server.

            Must not be set at the same time as min_ledger_time_abs.


            Optional
        submissionId:
          description: >-
            A unique identifier to distinguish completions for different
            submissions with the same change ID.

            Typically a random UUID. Applications are expected to use a
            different UUID for each retry of a submission

            with the same change ID.

            Must be a valid LedgerString (as described in ``value.proto``).


            If omitted, the participant or the committer may set a value of
            their choice.


            Optional
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
          description: |-
            Must be a valid synchronizer id

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
    SubmitAndWaitResponse:
      title: SubmitAndWaitResponse
      type: object
      required:
        - updateId
        - completionOffset
      properties:
        updateId:
          description: |-
            The id of the transaction that resulted from the submitted command.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        completionOffset:
          description: >-
            The details of the offset field are described in
            ``community/ledger-api/README.md``.


            Required
          type: integer
          format: int64
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
    DeduplicationPeriod:
      title: DeduplicationPeriod
      description: >-
        Specifies the deduplication period for the change ID.

        If omitted, the participant will assume the configured maximum
        deduplication time.


        Optional
      oneOf:
        - type: object
          required:
            - DeduplicationDuration
          properties:
            DeduplicationDuration:
              $ref: '#/components/schemas/DeduplicationDuration'
        - type: object
          required:
            - DeduplicationOffset
          properties:
            DeduplicationOffset:
              $ref: '#/components/schemas/DeduplicationOffset'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty'
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
    DeduplicationDuration:
      title: DeduplicationDuration
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Duration'
    DeduplicationOffset:
      title: DeduplicationOffset
      type: object
      required:
        - value
      properties:
        value:
          type: integer
          format: int64
    Empty:
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
