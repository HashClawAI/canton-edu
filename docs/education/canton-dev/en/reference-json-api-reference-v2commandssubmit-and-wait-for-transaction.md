---
title: "/v2/commands/submit-and-wait-for-transaction"
slug: "reference-json-api-reference-v2commandssubmit-and-wait-for-transaction"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandssubmit-and-wait-for-transaction.md"
source_title: "/v2/commands/submit-and-wait-for-transaction"
tags:
  - reference
  - json-api-reference
  - v2commandssubmit-and-wait-for-transaction
---

# /v2/commands/submit-and-wait-for-transaction

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/commands/submit-and-wait-for-transaction

> Submits a single composite command, waits for its result, and returns the transaction.
Propagates the gRPC error of failed submissions including Daml interpretation errors.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/submit-and-wait-for-transaction
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
  /v2/commands/submit-and-wait-for-transaction:
    post:
      summary: /v2/commands/submit-and-wait-for-transaction
      description: >-
        Submits a single composite command, waits for its result, and returns
        the transaction.

        Propagates the gRPC error of failed submissions including Daml
        interpretation errors.
      operationId: postV2CommandsSubmit-and-wait-for-transaction
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JsSubmitAndWaitForTransactionRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsSubmitAndWaitForTransactionResponse'
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
    JsSubmitAndWaitForTransactionRequest:
      title: JsSubmitAndWaitForTransactionRequest
      description: These commands are executed as a single atomic transaction.
      type: object
      required:
        - commands
      properties:
        commands:
          $ref: '#/components/schemas/JsCommands'
          description: |-
            The commands to be submitted.

            Required
        transactionFormat:
          $ref: '#/components/schemas/TransactionFormat'
          description: >-
            If no ``transaction_format`` is provided, a default will be used
            where ``transaction_shape`` is set to

            TRANSACTION_SHAPE_ACS_DELTA, ``event_format`` is defined with
            ``filters_by_party`` containing wildcard-template

            filter for all original ``act_as`` and ``read_as`` parties and the
            ``verbose`` flag is set.


            Optional
    JsSubmitAndWaitForTransactionResponse:
      title: JsSubmitAndWaitForTransactionResponse
      type: object
      required:
        - transaction
      properties:
        transaction:
          $ref: '#/components/schemas/JsTransaction'
          description: >-
            The transaction that resulted from the submitted command.

            The transaction might contain no events (request conditions result
            in filtering out all of them).


            Required
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
    TransactionFormat:
      title: TransactionFormat
      description: |-
        A format that specifies what events to include in Daml transactions
        and what data to compute and include for them.
      type: object
      required:
        - transactionShape
        - eventFormat
      properties:
        eventFormat:
          $ref: '#/components/schemas/EventFormat'
          description: Required
        transactionShape:
          description: >-
            What transaction shape to use for interpreting the filters of the
            event format.


            Required
          type: string
          enum:
            - TRANSACTION_SHAPE_UNSPECIFIED
            - TRANSACTION_SHAPE_ACS_DELTA
            - TRANSACTION_SHAPE_LEDGER_EFFECTS
    JsTransaction:
      title: JsTransaction
      description: Filtered view of an on-ledger transaction's create and archive events.
      type: object
      required:
        - updateId
        - effectiveAt
        - offset
        - synchronizerId
        - recordTime
        - events
      properties:
        updateId:
          description: |-
            Assigned by the server. Useful for correlating logs.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        commandId:
          description: >-
            The ID of the command which resulted in this transaction. Missing
            for everyone except the submitting party.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        workflowId:
          description: |-
            The workflow ID used in command submission.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
          type: string
        effectiveAt:
          description: |-
            Ledger effective time.

            Required
          type: string
        events:
          description: >-
            The collection of events.

            Contains:


            - ``CreatedEvent`` or ``ArchivedEvent`` in case of ACS_DELTA
            transaction shape

            - ``CreatedEvent`` or ``ExercisedEvent`` in case of LEDGER_EFFECTS
            transaction shape


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/Event'
        offset:
          description: >-
            The absolute offset. The details of this field are described in
            ``community/ledger-api/README.md``.

            It is a valid absolute offset (positive integer).


            Required
          type: integer
          format: int64
        synchronizerId:
          description: |-
            A valid synchronizer id.
            Identifies the synchronizer that synchronized the transaction.

            Required
          type: string
        traceContext:
          $ref: '#/components/schemas/TraceContext'
          description: >-
            Ledger API trace context


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
        recordTime:
          description: >-
            The time at which the transaction was recorded. The record time
            refers to the synchronizer

            which synchronized the transaction.


            Required
          type: string
        externalTransactionHash:
          description: >-
            For transaction externally signed, contains the external transaction
            hash

            signed by the external party. Can be used to correlate an external
            submission with a committed transaction.


            Optional: can be empty
          type: string
        paidTrafficCost:
          description: >-
            The traffic cost that this participant node paid for the
            confirmation

            request for this transaction.


            Not set for transactions that were

            - initiated by another participant

            - initiated offline via the repair service

            - processed before the participant started serving traffic cost on
            the Ledger API

            - returned as part of a query filtering for a non submitting party


            Optional
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
    EventFormat:
      title: EventFormat
      description: >-
        A format for events which defines both which events should be included

        and what data should be computed and included for them.


        Note that some of the filtering behavior depends on the
        `TransactionShape`,

        which is expected to be specified alongside usages of `EventFormat`.
      type: object
      properties:
        filtersByParty:
          $ref: '#/components/schemas/Map_Filters'
          description: >-
            Each key must be a valid PartyIdString (as described in
            ``value.proto``).

            The interpretation of the filter depends on the transaction-shape
            being filtered:


            1. For **ledger-effects** create and exercise events are returned,
            for which the witnesses include at least one of
               the listed parties and match the per-party filter.
            2. For **transaction and active-contract-set streams** create and
            archive events are returned for all contracts whose
               stakeholders include at least one of the listed parties and match the per-party filter.

            Optional: can be empty
        filtersForAnyParty:
          $ref: '#/components/schemas/Filters'
          description: >-
            Wildcard filters that apply to all the parties existing on the
            participant. The interpretation of the filters is the same

            with the per-party filter as described above.


            Optional
        verbose:
          description: >-
            If enabled, values served over the API will contain more information
            than strictly necessary to interpret the data.

            In particular, setting the verbose flag to true triggers the ledger
            to include labels for record fields.


            Optional
          type: boolean
    Event:
      title: Event
      description: |-
        Events in transactions can have two primary shapes:

        - ACS delta: events can be CreatedEvent or ArchivedEvent
        - ledger effects: events can be CreatedEvent or ExercisedEvent

        In the update service the events are restricted to the events
        visible for the parties specified in the transaction filter. Each
        event message type below contains a ``witness_parties`` field which
        indicates the subset of the requested parties that can see the event
        in question.
      oneOf:
        - type: object
          required:
            - ArchivedEvent
          properties:
            ArchivedEvent:
              $ref: '#/components/schemas/ArchivedEvent'
        - type: object
          required:
            - CreatedEvent
          properties:
            CreatedEvent:
              $ref: '#/components/schemas/CreatedEvent'
        - type: object
          required:
            - ExercisedEvent
          properties:
            ExercisedEvent:
              $ref: '#/components/schemas/ExercisedEvent'
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
    Map_Filters:
      title: Map_Filters
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Filters'
    Filters:
      title: Filters
      description: >-
        The union of a set of template filters, interface filters, or a
        wildcard.
      type: object
      properties:
        cumulative:
          description: >-
            Every filter in the cumulative list expands the scope of the
            resulting stream. Each interface,

            template or wildcard filter means additional events that will match
            the query.

            The impact of include_interface_view and include_created_event_blob
            fields in the filters will

            also be accumulated.

            A template or an interface SHOULD NOT appear twice in the
            accumulative field.

            A wildcard filter SHOULD NOT be defined more than once in the
            accumulative field.

            If no ``CumulativeFilter`` defined, the default of a single
            ``WildcardFilter`` with

            include_created_event_blob unset is used.


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/CumulativeFilter'
    ArchivedEvent:
      title: ArchivedEvent
      description: >-
        Records that a contract has been archived, and choices may no longer be
        exercised on it.
      type: object
      required:
        - offset
        - nodeId
        - contractId
        - templateId
        - packageName
        - witnessParties
      properties:
        offset:
          description: >-
            The offset of origin.

            Offsets are managed by the participant nodes.

            Transactions can thus NOT be assumed to have the same offsets on
            different participant nodes.

            It is a valid absolute offset (positive integer)


            Required
          type: integer
          format: int64
        nodeId:
          description: >-
            The position of this event in the originating transaction or
            reassignment.

            Node IDs are not necessarily equal across participants,

            as these may see different projections/parts of transactions.

            Must be valid node ID (non-negative integer)


            Required
          type: integer
          format: int32
        contractId:
          description: |-
            The ID of the archived contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        templateId:
          description: >-
            Identifies the template that defines the choice that archived the
            contract.

            This template's package-id may differ from the target contract's
            package-id

            if the target contract has been upgraded or downgraded.


            The identifier uses the package-id reference format.


            Required
          type: string
        witnessParties:
          description: >-
            The parties that are notified of this event. For an
            ``ArchivedEvent``,

            these are the intersection of the stakeholders of the contract in

            question and the parties specified in the ``TransactionFilter``. The

            stakeholders are the union of the signatories and the observers of

            the contract.

            Each one of its elements must be a valid PartyIdString (as described

            in ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        packageName:
          description: |-
            The package name of the contract.

            Required
          type: string
        implementedInterfaces:
          description: >-
            The interfaces implemented by the target template that have been

            matched from the interface filter query.

            Populated only in case interface filters with include_interface_view
            set.


            If defined, the identifier uses the package-id reference format.


            Optional: can be empty
          type: array
          items:
            type: string
    CreatedEvent:
      title: CreatedEvent
      description: >-
        Records that a contract has been created, and choices may now be
        exercised on it.
      type: object
      required:
        - offset
        - nodeId
        - contractId
        - templateId
        - createdAt
        - packageName
        - representativePackageId
        - acsDelta
        - createArgument
        - witnessParties
        - signatories
      properties:
        offset:
          description: >-
            The offset of origin, which has contextual meaning, please see
            description at messages that include a CreatedEvent.

            Offsets are managed by the participant nodes.

            Transactions can thus NOT be assumed to have the same offsets on
            different participant nodes.

            It is a valid absolute offset (positive integer)


            Required
          type: integer
          format: int64
        nodeId:
          description: >-
            The position of this event in the originating transaction or
            reassignment.

            The origin has contextual meaning, please see description at
            messages that include a CreatedEvent.

            Node IDs are not necessarily equal across participants,

            as these may see different projections/parts of transactions.

            Must be valid node ID (non-negative integer)


            Required
          type: integer
          format: int32
        contractId:
          description: |-
            The ID of the created contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        templateId:
          description: |-
            The template of the created contract.
            The identifier uses the package-id reference format.

            Required
          type: string
        contractKey:
          description: >-
            The key of the created contract.

            This will be set if and only if ``template_id`` defines a contract
            key.


            Optional
        contractKeyHash:
          description: >-
            The hash of contract_key.

            This will be set if and only if ``template_id`` defines a contract
            key.


            Optional: can be empty
          type: string
        createArgument:
          description: |-
            The arguments that have been used to create the contract.

            Required
        createdEventBlob:
          description: >-
            Opaque representation of contract create event payload intended for
            forwarding

            to an API server as a contract disclosed as part of a command

            submission.


            Optional: can be empty
          type: string
        interfaceViews:
          description: >-
            Interface views specified in the transaction filter.

            Includes an ``InterfaceView`` for each interface for which there is
            a ``InterfaceFilter`` with


            - its party in the ``witness_parties`` of this event,

            - and which is implemented by the template of this event,

            - and which has ``include_interface_view`` set.


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/JsInterfaceView'
        witnessParties:
          description: >-
            The parties that are notified of this event. When a ``CreatedEvent``

            is returned as part of a transaction tree or ledger-effects
            transaction, this will include all

            the parties specified in the ``TransactionFilter`` that are
            witnesses  of the event

            (the stakeholders of the contract and all informees of all the
            ancestors

            of this create action that this participant knows about).

            If served as part of a ACS delta transaction those will

            be limited to all parties specified in the ``TransactionFilter``
            that

            are stakeholders of the contract (i.e. either signatories or
            observers).

            If the ``CreatedEvent`` is returned as part of an AssignedEvent,

            ActiveContract or IncompleteUnassigned (so the event is related to

            an assignment or unassignment): this will include all parties of the

            ``TransactionFilter`` that are stakeholders of the contract.


            The behavior of reading create events visible to parties not hosted

            on the participant node serving the Ledger API is undefined.
            Concretely,

            there is neither a guarantee that the participant node will serve
            all their

            create events on the ACS stream, nor is there a guarantee that
            matching archive

            events are delivered for such create events.


            For most clients this is not a problem, as they only read events for
            parties

            that are hosted on the participant node. If you need to read events

            for parties that may not be hosted at all times on the participant
            node,

            subscribe to the ``TopologyEvent``s for that party by setting a
            corresponding

            ``UpdateFormat``.  Using these events, query the ACS as-of an offset
            where the

            party is hosted on the participant node, and ignore create events at
            offsets

            where the party is not hosted on the participant node.


            Required: must be non-empty
          type: array
          items:
            type: string
        signatories:
          description: |-
            The signatories for this contract as specified by the template.

            Required: must be non-empty
          type: array
          items:
            type: string
        observers:
          description: >-
            The observers for this contract as specified explicitly by the
            template or implicitly as choice controllers.

            This field never contains parties that are signatories.


            Optional: can be empty
          type: array
          items:
            type: string
        createdAt:
          description: |-
            Ledger effective time of the transaction that created the contract.

            Required
          type: string
        packageName:
          description: |-
            The package name of the created contract.

            Required
          type: string
        representativePackageId:
          description: >-
            A package-id present in the participant package store that
            typechecks the contract's argument.

            This may differ from the package-id of the template used to create
            the contract.

            For contracts created before Canton 3.4, this field matches the
            contract's creation package-id.


            NOTE: Experimental, server internal concept, not for client
            consumption. Subject to change without notice.


            Required
          type: string
        acsDelta:
          description: >-
            Whether this event would be part of respective ACS_DELTA shaped
            stream,

            and should therefore considered when tracking contract activeness on
            the client-side.


            Required
          type: boolean
    ExercisedEvent:
      title: ExercisedEvent
      description: Records that a choice has been exercised on a target contract.
      type: object
      required:
        - offset
        - nodeId
        - contractId
        - templateId
        - choice
        - choiceArgument
        - consuming
        - lastDescendantNodeId
        - packageName
        - acsDelta
        - actingParties
        - witnessParties
      properties:
        offset:
          description: >-
            The offset of origin.

            Offsets are managed by the participant nodes.

            Transactions can thus NOT be assumed to have the same offsets on
            different participant nodes.

            It is a valid absolute offset (positive integer)


            Required
          type: integer
          format: int64
        nodeId:
          description: >-
            The position of this event in the originating transaction or
            reassignment.

            Node IDs are not necessarily equal across participants,

            as these may see different projections/parts of transactions.

            Must be valid node ID (non-negative integer)


            Required
          type: integer
          format: int32
        contractId:
          description: |-
            The ID of the target contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        templateId:
          description: >-
            Identifies the template that defines the executed choice.

            This template's package-id may differ from the target contract's
            package-id

            if the target contract has been upgraded or downgraded.


            The identifier uses the package-id reference format.


            Required
          type: string
        interfaceId:
          description: |-
            The interface where the choice is defined, if inherited.
            If defined, the identifier uses the package-id reference format.

            Optional
          type: string
        choice:
          description: |-
            The choice that was exercised on the target contract.
            Must be a valid NameString (as described in ``value.proto``).

            Required
          type: string
        choiceArgument:
          description: |-
            The argument of the exercised choice.

            Required
        actingParties:
          description: >-
            The parties that exercised the choice.

            Each element must be a valid PartyIdString (as described in
            ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        consuming:
          description: |-
            If true, the target contract may no longer be exercised.

            Required
          type: boolean
        witnessParties:
          description: >-
            The parties that are notified of this event. The witnesses of an
            exercise

            node will depend on whether the exercise was consuming or not.

            If consuming, the witnesses are the union of the stakeholders,

            the actors and all informees of all the ancestors of this event this

            participant knows about.

            If not consuming, the witnesses are the union of the signatories,

            the actors and all informees of all the ancestors of this event this

            participant knows about.

            In both cases the witnesses are limited to the querying parties, or
            not

            limited in case anyParty filters are used.

            Note that the actors might not necessarily be observers

            and thus stakeholders. This is the case when the controllers of a

            choice are specified using "flexible controllers", using the

            ``choice ... controller`` syntax, and said controllers are not

            explicitly marked as observers.

            Each element must be a valid PartyIdString (as described in
            ``value.proto``).


            Required: must be non-empty
          type: array
          items:
            type: string
        lastDescendantNodeId:
          description: >-
            Specifies the upper boundary of the node ids of the events in the
            same transaction that appeared as a result of

            this ``ExercisedEvent``. This allows unambiguous identification of
            all the members of the subtree rooted at this

            node. A full subtree can be constructed when all descendant nodes
            are present in the stream. If nodes are heavily

            filtered, it is only possible to determine if a node is in a
            consequent subtree or not.


            Required
          type: integer
          format: int32
        exerciseResult:
          description: |-
            The result of exercising the choice.

            Optional
        packageName:
          description: |-
            The package name of the contract.

            Required
          type: string
        implementedInterfaces:
          description: >-
            If the event is consuming, the interfaces implemented by the target
            template that have been

            matched from the interface filter query.

            Populated only in case interface filters with include_interface_view
            set.


            The identifier uses the package-id reference format.


            Optional: can be empty
          type: array
          items:
            type: string
        acsDelta:
          description: >-
            Whether this event would be part of respective ACS_DELTA shaped
            stream,

            and should therefore considered when tracking contract activeness on
            the client-side.


            Required
          type: boolean
    Map_Int_Field:
      title: Map_Int_Field
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Field'
    CumulativeFilter:
      title: CumulativeFilter
      description: >-
        A filter that matches all contracts that are either an instance of one
        of

        the ``template_filters`` or that match one of the ``interface_filters``.
      type: object
      properties:
        identifierFilter:
          $ref: '#/components/schemas/IdentifierFilter'
    JsInterfaceView:
      title: JsInterfaceView
      description: View of a create event matched by an interface filter.
      type: object
      required:
        - interfaceId
        - viewStatus
      properties:
        interfaceId:
          description: |-
            The interface implemented by the matched event.
            The identifier uses the package-id reference format.

            Required
          type: string
        viewStatus:
          $ref: '#/components/schemas/JsStatus'
          description: >-
            Whether the view was successfully computed, and if not,

            the reason for the error. The error is reported using the same rules

            for error codes and messages as the errors returned for API
            requests.


            Required
        viewValue:
          description: |-
            The value of the interface's view method on this event.
            Set if it was requested in the ``InterfaceFilter`` and it could be
            successfully computed.

            Optional
        implementationPackageId:
          description: >-
            The package defining the interface implementation used to compute
            the view.

            Can be different from the package that was used to create the
            contract itself,

            as the contract arguments can be upgraded or downgraded using
            smart-contract upgrading

            as part of computing the interface view.

            Populated if the view computation is successful, otherwise empty.


            Optional
          type: string
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
    IdentifierFilter:
      title: IdentifierFilter
      description: Required
      oneOf:
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty1'
        - type: object
          required:
            - InterfaceFilter
          properties:
            InterfaceFilter:
              $ref: '#/components/schemas/InterfaceFilter'
        - type: object
          required:
            - TemplateFilter
          properties:
            TemplateFilter:
              $ref: '#/components/schemas/TemplateFilter'
        - type: object
          required:
            - WildcardFilter
          properties:
            WildcardFilter:
              $ref: '#/components/schemas/WildcardFilter'
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
    Empty1:
      title: Empty
      type: object
    InterfaceFilter:
      title: InterfaceFilter
      description: This filter matches contracts that implement a specific interface.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/InterfaceFilter1'
    TemplateFilter:
      title: TemplateFilter
      description: This filter matches contracts of a specific template.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/TemplateFilter1'
    WildcardFilter:
      title: WildcardFilter
      description: This filter matches all templates.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/WildcardFilter1'
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
    InterfaceFilter1:
      title: InterfaceFilter
      description: This filter matches contracts that implement a specific interface.
      type: object
      required:
        - interfaceId
      properties:
        interfaceId:
          description: >-
            The interface that a matching contract must implement.

            The ``interface_id`` needs to be valid: corresponding interface
            should be defined in

            one of the available packages at the time of the query.

            Both package-name and package-id reference formats for the
            identifier are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        includeInterfaceView:
          description: >-
            Whether to include the interface view on the contract in the
            returned ``CreatedEvent``.

            Use this to access contract data in a uniform manner in your API
            client.


            Optional
          type: boolean
        includeCreatedEventBlob:
          description: >-
            Whether to include a ``created_event_blob`` in the returned
            ``CreatedEvent``.

            Use this to access the contract create event payload in your API
            client

            for submitting it as a disclosed contract with future commands.


            Optional
          type: boolean
    TemplateFilter1:
      title: TemplateFilter
      description: This filter matches contracts of a specific template.
      type: object
      required:
        - templateId
      properties:
        templateId:
          description: >-
            A template for which the payload should be included in the response.

            The ``template_id`` needs to be valid: corresponding template should
            be defined in

            one of the available packages at the time of the query.

            Both package-name and package-id reference formats for the
            identifier are supported.

            Note: The package-id reference identifier format is deprecated. We
            plan to end support for this format in version 3.4.


            Required
          type: string
        includeCreatedEventBlob:
          description: >-
            Whether to include a ``created_event_blob`` in the returned
            ``CreatedEvent``.

            Use this to access the contract event payload in your API client

            for submitting it as a disclosed contract with future commands.


            Optional
          type: boolean
    WildcardFilter1:
      title: WildcardFilter
      description: This filter matches all templates.
      type: object
      properties:
        includeCreatedEventBlob:
          description: >-
            Whether to include a ``created_event_blob`` in the returned
            ``CreatedEvent``.

            Use this to access the contract create event payload in your API
            client

            for submitting it as a disclosed contract with future commands.


            Optional
          type: boolean
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
