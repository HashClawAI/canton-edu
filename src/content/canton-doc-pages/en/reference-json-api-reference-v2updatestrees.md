---
title: "/v2/updates/trees"
slug: "reference-json-api-reference-v2updatestrees"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2updatestrees.md"
source_title: "/v2/updates/trees"
tags:
  - reference
  - json-api-reference
  - v2updatestrees
---

# /v2/updates/trees

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/updates/trees

> Query update transactions tree list (blocking call). Provided for backwards compatibility, it will be removed in the Canton version 3.5.0, use v2/updates instead.
Notice: This endpoint should be used for small results set.
When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
there will be an error (`413 Content Too Large`) returned.
Increasing this limit may lead to performance issues and high memory consumption.
Consider using websockets (asyncapi) for better efficiency with larger results.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/updates/trees
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
  /v2/updates/trees:
    post:
      summary: /v2/updates/trees
      description: >-
        Query update transactions tree list (blocking call). Provided for
        backwards compatibility, it will be removed in the Canton version 3.5.0,
        use v2/updates instead.

        Notice: This endpoint should be used for small results set.

        When number of results exceeded node configuration limit
        (`http-list-max-elements-limit`)

        there will be an error (`413 Content Too Large`) returned.

        Increasing this limit may lead to performance issues and high memory
        consumption.

        Consider using websockets (asyncapi) for better efficiency with larger
        results.
      operationId: postV2UpdatesTrees
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
              $ref: '#/components/schemas/GetUpdatesRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/JsGetUpdateTreesResponse'
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
      deprecated: true
      security:
        - httpAuth: []
        - apiKeyAuth: []
components:
  schemas:
    GetUpdatesRequest:
      title: GetUpdatesRequest
      type: object
      required:
        - beginExclusive
      properties:
        beginExclusive:
          description: >-
            Exclusive lower bound offset of the requested ledger section
            (non-negative integer).

            The response will only contain transactions whose offset is strictly
            greater than this.

            If set to zero, the lower bound is set to the beginning of the
            ledger.

            If the participant has been pruned, this parameter must be greater
            or equal than the pruning offset.

            Required
          type: integer
          format: int64
        endInclusive:
          description: >-
            Inclusive higher bound offset of the requested ledger section.

            If specified the response will only contain transactions whose
            offset is less than or equal to this.

            If not specified,


            - the descending_order must not be selected,

            - the stream will not terminate.


            Optional
          type: integer
          format: int64
        filter:
          $ref: '#/components/schemas/TransactionFilter'
          description: >-
            Provided for backwards compatibility, it will be removed in the
            Canton version 3.5.0.

            Requesting parties with template filters.

            Template filters must be empty for GetUpdateTrees requests.

            Optional for backwards compatibility, if defined update_format must
            be unset
        verbose:
          description: >-
            Provided for backwards compatibility, it will be removed in the
            Canton version 3.5.0.

            If enabled, values served over the API will contain more information
            than strictly necessary to interpret the data.

            In particular, setting the verbose flag to true triggers the ledger
            to include labels, record and variant type ids

            for record fields.

            Optional for backwards compatibility, if defined update_format must
            be unset
          type: boolean
        updateFormat:
          $ref: '#/components/schemas/UpdateFormat'
          description: >-
            Must be unset for GetUpdateTrees request.

            Optional for backwards compatibility for GetUpdates request:
            defaults to an UpdateFormat where:


            - include_transactions.event_format.filters_by_party = the
            filter.filters_by_party on this request

            - include_transactions.event_format.filters_for_any_party = the
            filter.filters_for_any_party on this request

            - include_transactions.event_format.verbose = the same flag
            specified on this request

            - include_transactions.transaction_shape =
            TRANSACTION_SHAPE_ACS_DELTA

            - include_reassignments.filter = the same filter specified on this
            request

            - include_reassignments.verbose = the same flag specified on this
            request

            -
            include_topology_events.include_participant_authorization_events.parties
            = all the parties specified in filter
        descendingOrder:
          description: |-
            If set, the stream will populate the elements in descending order.

            Optional
          type: boolean
    JsGetUpdateTreesResponse:
      title: JsGetUpdateTreesResponse
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.
      type: object
      properties:
        update:
          $ref: '#/components/schemas/Update1'
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
    TransactionFilter:
      title: TransactionFilter
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.

        Used both for filtering create and archive events as well as for
        filtering transaction trees.
      type: object
      properties:
        filtersByParty:
          $ref: '#/components/schemas/Map_Filters'
          description: >-
            Each key must be a valid PartyIdString (as described in
            ``value.proto``).

            The interpretation of the filter depends on the transaction-shape
            being filtered:


            1. For **transaction trees** (used in GetUpdateTreesResponse for
            backwards compatibility) all party keys used as
               wildcard filters, and all subtrees whose root has one of the listed parties as an informee are returned.
               If there are ``CumulativeFilter``s, those will control returned ``CreatedEvent`` fields where applicable, but will
               not be used for template/interface filtering.
            2. For **ledger-effects** create and exercise events are returned,
            for which the witnesses include at least one of
               the listed parties and match the per-party filter.
            3. For **transaction and active-contract-set streams** create and
            archive events are returned for all contracts whose
               stakeholders include at least one of the listed parties and match the per-party filter.
        filtersForAnyParty:
          $ref: '#/components/schemas/Filters'
          description: >-
            Wildcard filters that apply to all the parties existing on the
            participant. The interpretation of the filters is the same

            with the per-party filter as described above.
    UpdateFormat:
      title: UpdateFormat
      description: A format specifying what updates to include and how to render them.
      type: object
      properties:
        includeTransactions:
          $ref: '#/components/schemas/TransactionFormat'
          description: |-
            Include Daml transactions in streams.
            If unset, no transactions are emitted in the stream.

            Optional
        includeReassignments:
          $ref: '#/components/schemas/EventFormat'
          description: |-
            Include (un)assignments in the stream.
            The events in the result take the shape TRANSACTION_SHAPE_ACS_DELTA.
            If unset, no (un)assignments are emitted in the stream.

            Optional
        includeTopologyEvents:
          $ref: '#/components/schemas/TopologyFormat'
          description: |-
            Include topology events in streams.
            If unset no topology events are emitted in the stream.

            Optional
    Update1:
      title: Update
      oneOf:
        - type: object
          required:
            - OffsetCheckpoint
          properties:
            OffsetCheckpoint:
              $ref: '#/components/schemas/OffsetCheckpoint3'
        - type: object
          required:
            - Reassignment
          properties:
            Reassignment:
              $ref: '#/components/schemas/Reassignment1'
        - type: object
          required:
            - TransactionTree
          properties:
            TransactionTree:
              $ref: '#/components/schemas/TransactionTree'
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
    TopologyFormat:
      title: TopologyFormat
      description: >-
        A format specifying which topology transactions to include and how to
        render them.
      type: object
      properties:
        includeParticipantAuthorizationEvents:
          $ref: '#/components/schemas/ParticipantAuthorizationTopologyFormat'
          description: >-
            Include participant authorization topology events in streams.

            If unset, no participant authorization topology events are emitted
            in the stream.


            Optional
    OffsetCheckpoint3:
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
    Reassignment1:
      title: Reassignment
      description: Complete view of an on-ledger reassignment.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/JsReassignment'
    TransactionTree:
      title: TransactionTree
      description: >-
        Provided for backwards compatibility, it will be removed in the Canton
        version 3.5.0.

        Complete view of an on-ledger transaction.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/JsTransactionTree'
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
    ParticipantAuthorizationTopologyFormat:
      title: ParticipantAuthorizationTopologyFormat
      description: >-
        A format specifying which participant authorization topology
        transactions to include and how to render them.
      type: object
      properties:
        parties:
          description: |-
            List of parties for which the topology transactions should be sent.
            Empty means: for all parties.

            Optional: can be empty
          type: array
          items:
            type: string
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
    JsReassignment:
      title: JsReassignment
      description: Complete view of an on-ledger reassignment.
      type: object
      required:
        - updateId
        - offset
        - recordTime
        - synchronizerId
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
            The ID of the command which resulted in this reassignment. Missing
            for everyone except the submitting party on the submitting
            participant.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        workflowId:
          description: >-
            The workflow ID used in reassignment command submission. Only set if
            the ``workflow_id`` for the command was set.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        offset:
          description: >-
            The participant's offset. The details of this field are described in
            ``community/ledger-api/README.md``.

            Must be a valid absolute offset (positive integer).


            Required
          type: integer
          format: int64
        events:
          description: |-
            The collection of reassignment events.

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/JsReassignmentEvent'
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
            The time at which the reassignment was recorded. The record time
            refers to the source/target

            synchronizer for an unassign/assign event respectively.


            Required
          type: string
        synchronizerId:
          description: |-
            A valid synchronizer id.
            Identifies the synchronizer that synchronized this Reassignment.

            Required
          type: string
        paidTrafficCost:
          description: >-
            The traffic cost that this participant node paid for the
            corresponding (un)assignment request.


            Not set for transactions that were

            - initiated by another participant

            - initiated offline via the repair service

            - processed before the participant started serving traffic cost on
            the Ledger API

            - returned as part of a query filtering for a non submitting party


            Optional
          type: integer
          format: int64
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
    JsReassignmentEvent:
      title: JsReassignmentEvent
      oneOf:
        - type: object
          required:
            - JsAssignmentEvent
          properties:
            JsAssignmentEvent:
              $ref: '#/components/schemas/JsAssignmentEvent'
        - type: object
          required:
            - JsUnassignedEvent
          properties:
            JsUnassignedEvent:
              $ref: '#/components/schemas/JsUnassignedEvent'
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
    Map_Int_TreeEvent:
      title: Map_Int_TreeEvent
      type: object
      additionalProperties:
        $ref: '#/components/schemas/TreeEvent'
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
    JsAssignmentEvent:
      title: JsAssignmentEvent
      type: object
      required:
        - source
        - target
        - reassignmentId
        - submitter
        - reassignmentCounter
        - createdEvent
      properties:
        source:
          type: string
        target:
          type: string
        reassignmentId:
          type: string
        submitter:
          type: string
        reassignmentCounter:
          type: integer
          format: int64
        createdEvent:
          $ref: '#/components/schemas/CreatedEvent'
    JsUnassignedEvent:
      title: JsUnassignedEvent
      description: >-
        Records that a contract has been unassigned, and it becomes unusable on
        the source synchronizer
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/UnassignedEvent'
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
    UnassignedEvent:
      title: UnassignedEvent
      description: >-
        Records that a contract has been unassigned, and it becomes unusable on
        the source synchronizer
      type: object
      required:
        - reassignmentId
        - contractId
        - source
        - target
        - reassignmentCounter
        - packageName
        - offset
        - nodeId
        - templateId
        - witnessParties
      properties:
        reassignmentId:
          description: >-
            The ID of the unassignment. This needs to be used as an input for a
            assign ReassignmentCommand.

            Must be a valid LedgerString (as described in ``value.proto``).


            Required
          type: string
        contractId:
          description: |-
            The ID of the reassigned contract.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        templateId:
          description: |-
            The template of the reassigned contract.
            The identifier uses the package-id reference format.

            Required
          type: string
        source:
          description: |-
            The ID of the source synchronizer
            Must be a valid synchronizer id

            Required
          type: string
        target:
          description: |-
            The ID of the target synchronizer
            Must be a valid synchronizer id

            Required
          type: string
        submitter:
          description: |-
            Party on whose behalf the unassign command was executed.
            Empty if the unassignment happened offline via the repair service.
            Must be a valid PartyIdString (as described in ``value.proto``).

            Optional
          type: string
        reassignmentCounter:
          description: >-
            Each corresponding assigned and unassigned event has the same
            reassignment_counter. This strictly increases

            with each unassign command for the same contract. Creation of the
            contract corresponds to reassignment_counter

            equals zero.


            Required
          type: integer
          format: int64
        assignmentExclusivity:
          description: >-
            Assignment exclusivity

            Before this time (measured on the target synchronizer), only the
            submitter of the unassignment can initiate the assignment

            Defined for reassigning participants.


            Optional
          type: string
        witnessParties:
          description: |-
            The parties that are notified of this event.

            Required: must be non-empty
          type: array
          items:
            type: string
        packageName:
          description: |-
            The package name of the contract.

            Required
          type: string
        offset:
          description: >-
            The offset of origin.

            Offsets are managed by the participant nodes.

            Reassignments can thus NOT be assumed to have the same offsets on
            different participant nodes.

            Must be a valid absolute offset (positive integer)


            Required
          type: integer
          format: int64
        nodeId:
          description: |-
            The position of this event in the originating reassignment.
            Node IDs are not necessarily equal across participants,
            as these may see different projections/parts of reassignments.
            Must be valid node ID (non-negative integer)

            Required
          type: integer
          format: int32
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
