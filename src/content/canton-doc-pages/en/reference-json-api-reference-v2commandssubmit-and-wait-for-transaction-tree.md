---
title: "/v2/commands/submit-and-wait-for-transaction-tree"
slug: "reference-json-api-reference-v2commandssubmit-and-wait-for-transaction-tree"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandssubmit-and-wait-for-transaction-tree.md"
source_title: "/v2/commands/submit-and-wait-for-transaction-tree"
tags:
  - reference
  - json-api-reference
  - v2commandssubmit-and-wait-for-transaction-tree
---

# /v2/commands/submit-and-wait-for-transaction-tree

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/commands/submit-and-wait-for-transaction-tree

> Submit a batch of commands and wait for the transaction trees response. Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use submit-and-wait-for-transaction instead.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/submit-and-wait-for-transaction-tree
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
  /v2/commands/submit-and-wait-for-transaction-tree:
    post:
      summary: /v2/commands/submit-and-wait-for-transaction-tree
      description: >-
        Submit a batch of commands and wait for the transaction trees response.
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0, use submit-and-wait-for-transaction instead.
      operationId: postV2CommandsSubmit-and-wait-for-transaction-tree
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
                $ref: '#/components/schemas/JsSubmitAndWaitForTransactionTreeResponse'
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
      deprecated: true
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
    JsSubmitAndWaitForTransactionTreeResponse:
      title: JsSubmitAndWaitForTransactionTreeResponse
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.
      type: object
      properties:
        transactionTree:
          $ref: '#/components/schemas/JsTransactionTree'
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
    JsTransactionTree:
      title: JsTransactionTree
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.

        Complete view of an on-ledger transaction.
      type: object
      required:
        - updateId
        - effectiveAt
        - offset
        - eventsById
        - synchronizerId
        - recordTime
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
          description: >-
            The workflow ID used in command submission. Only set if the
            ``workflow_id`` for the command was set.

            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
          type: string
        effectiveAt:
          description: |-
            Ledger effective time.
            Required
          type: string
        offset:
          description: >-
            The absolute offset. The details of this field are described in
            ``community/ledger-api/README.md``.

            Required, it is a valid absolute offset (positive integer).
          type: integer
          format: int64
        eventsById:
          $ref: '#/components/schemas/Map_Int_TreeEvent'
          description: >-
            Changes to the ledger that were caused by this transaction. Nodes of
            the transaction tree.

            Each key must be a valid node ID (non-negative integer).

            Required
        synchronizerId:
          description: |-
            A valid synchronizer id.
            Identifies the synchronizer that synchronized the transaction.
            Required
          type: string
        traceContext:
          $ref: '#/components/schemas/TraceContext'
          description: >-
            Optional; ledger API trace context


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
        recordTime:
          description: >-
            The time at which the transaction was recorded. The record time
            refers to the synchronizer

            which synchronized the transaction.

            Required
          type: string
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
    Map_Int_TreeEvent:
      title: Map_Int_TreeEvent
      type: object
      additionalProperties:
        $ref: '#/components/schemas/TreeEvent'
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
    Map_Int_Field:
      title: Map_Int_Field
      type: object
      additionalProperties:
        $ref: '#/components/schemas/Field'
    TreeEvent:
      title: TreeEvent
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.

        Each tree event message type below contains a ``witness_parties`` field
        which

        indicates the subset of the requested parties that can see the event

        in question.


        Note that transaction trees might contain events with

        _no_ witness parties, which were included simply because they were

        children of events which have witnesses.
      oneOf:
        - type: object
          required:
            - CreatedTreeEvent
          properties:
            CreatedTreeEvent:
              $ref: '#/components/schemas/CreatedTreeEvent'
        - type: object
          required:
            - ExercisedTreeEvent
          properties:
            ExercisedTreeEvent:
              $ref: '#/components/schemas/ExercisedTreeEvent'
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
    CreatedTreeEvent:
      title: CreatedTreeEvent
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CreatedEvent'
    ExercisedTreeEvent:
      title: ExercisedTreeEvent
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/ExercisedEvent'
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
