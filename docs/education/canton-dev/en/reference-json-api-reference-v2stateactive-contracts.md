---
title: "/v2/state/active-contracts"
slug: "reference-json-api-reference-v2stateactive-contracts"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateactive-contracts.md"
source_title: "/v2/state/active-contracts"
tags:
  - reference
  - json-api-reference
  - v2stateactive-contracts
---

# /v2/state/active-contracts

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/state/active-contracts

> Query active contracts list (blocking call).
Querying active contracts is an expensive operation and if possible should not be repeated often.
Consider querying active contracts initially (for a given offset)
and then repeatedly call one of `/v2/updates/...`endpoints  to get subsequent modifications.
You can also use websockets to get updates with better performance.

Returns a stream of the snapshot of the active contracts and incomplete (un)assignments at a ledger offset.
Once the stream of GetActiveContractsResponses completes,
the client SHOULD begin streaming updates from the update service,
starting at the GetActiveContractsRequest.active_at_offset specified in this request.
Clients SHOULD NOT assume that the set of active contracts they receive reflects the state at the ledger end.

Notice: This endpoint should be used for small results set.
When number of results exceeded node configuration limit (`http-list-max-elements-limit`)
there will be an error (`413 Content Too Large`) returned.
Increasing this limit may lead to performance issues and high memory consumption.
Consider using websockets (asyncapi) for better efficiency with larger results.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/state/active-contracts
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
  /v2/state/active-contracts:
    post:
      summary: /v2/state/active-contracts
      description: >-
        Query active contracts list (blocking call).

        Querying active contracts is an expensive operation and if possible
        should not be repeated often.

        Consider querying active contracts initially (for a given offset)

        and then repeatedly call one of `/v2/updates/...`endpoints  to get
        subsequent modifications.

        You can also use websockets to get updates with better performance.


        Returns a stream of the snapshot of the active contracts and incomplete
        (un)assignments at a ledger offset.

        Once the stream of GetActiveContractsResponses completes,

        the client SHOULD begin streaming updates from the update service,

        starting at the GetActiveContractsRequest.active_at_offset specified in
        this request.

        Clients SHOULD NOT assume that the set of active contracts they receive
        reflects the state at the ledger end.


        Notice: This endpoint should be used for small results set.

        When number of results exceeded node configuration limit
        (`http-list-max-elements-limit`)

        there will be an error (`413 Content Too Large`) returned.

        Increasing this limit may lead to performance issues and high memory
        consumption.

        Consider using websockets (asyncapi) for better efficiency with larger
        results.
      operationId: postV2StateActive-contracts
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
              $ref: '#/components/schemas/GetActiveContractsRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/JsGetActiveContractsResponse'
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
    GetActiveContractsRequest:
      title: GetActiveContractsRequest
      description: >-
        If the given offset is different than the ledger end, and there are
        (un)assignments in-flight at the given offset,

        the snapshot may fail with
        "FAILED_PRECONDITION/PARTICIPANT_PRUNED_DATA_ACCESSED".

        Note that it is ok to request acs snapshots for party migration with
        offsets other than ledger end, because party

        migration is not concerned with incomplete (un)assignments.
      type: object
      required:
        - activeAtOffset
      properties:
        filter:
          $ref: '#/components/schemas/TransactionFilter'
          description: >-
            Provided for backwards compatibility, it will be removed in the
            Canton version 3.5.0.

            Templates to include in the served snapshot, per party.

            Optional, if specified event_format must be unset, if not specified
            event_format must be set.
        verbose:
          description: >-
            Provided for backwards compatibility, it will be removed in the
            Canton version 3.5.0.

            If enabled, values served over the API will contain more information
            than strictly necessary to interpret the data.

            In particular, setting the verbose flag to true triggers the ledger
            to include labels for record fields.

            Optional, if specified event_format must be unset.
          type: boolean
        activeAtOffset:
          description: >-
            The offset at which the snapshot of the active contracts will be
            computed.

            Must be no greater than the current ledger end offset.

            Must be greater than or equal to the last pruning offset.

            Must be a valid absolute offset (positive integer) or ledger begin
            offset (zero).

            If zero, the empty set will be returned.


            Required
          type: integer
          format: int64
        eventFormat:
          $ref: '#/components/schemas/EventFormat'
          description: >-
            Format of the contract_entries in the result. In case of
            CreatedEvent the presentation will be of

            TRANSACTION_SHAPE_ACS_DELTA.

            Optional for backwards compatibility, defaults to an EventFormat
            where:


            - filters_by_party is the filter.filters_by_party from this request

            - filters_for_any_party is the filter.filters_for_any_party from
            this request

            - verbose is the verbose field from this request
        streamContinuationToken:
          description: >-
            Opaque representation of a continuation token defining a position in
            the active contracts snapshot.

            The prefix of the active contracts snapshot will be omitted up to
            and including the element from which

            the continuation token was read.

            To reuse the continuation token from a
            `GetActiveContractsPageResponse`:


            - subsequent request must be executed on the same participant with
            the same version of canton,

            - subsequent request must have the same active_at_offset,

            - subsequent request must have the same event_format

            - and the participant must not have been pruned after the
            active_at_offset.


            If not specified, the whole active contracts snapshot will be
            returned.


            Optional: can be empty
          type: string
    JsGetActiveContractsResponse:
      title: JsGetActiveContractsResponse
      type: object
      properties:
        workflowId:
          description: >-
            The workflow ID used in command submission which corresponds to the
            contract_entry. Only set if

            the ``workflow_id`` for the command was set.

            Must be a valid LedgerString (as described in ``value.proto``).


            Optional
          type: string
        contractEntry:
          $ref: '#/components/schemas/JsContractEntry'
        streamContinuationToken:
          description: >-
            Opaque representation of a continuation token which can be used in
            the request to bypass the already processed part

            of the active contracts snapshot.

            Only populated for the streaming ``GetActiveContracts`` rpc call.


            Optional: can be empty
          type: string
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
    JsContractEntry:
      title: JsContractEntry
      description: >-
        For a contract there could be multiple contract_entry-s in the entire
        snapshot. These together define

        the state of one contract in the snapshot.

        A contract_entry is included in the result, if and only if there is at
        least one stakeholder party of the contract

        that is hosted on the synchronizer at the time of the event and the
        party satisfies the

        ``TransactionFilter`` in the query.


        Required
      oneOf:
        - type: object
          required:
            - JsActiveContract
          properties:
            JsActiveContract:
              $ref: '#/components/schemas/JsActiveContract'
        - type: object
          required:
            - JsEmpty
          properties:
            JsEmpty:
              $ref: '#/components/schemas/JsEmpty'
        - type: object
          required:
            - JsIncompleteAssigned
          properties:
            JsIncompleteAssigned:
              $ref: '#/components/schemas/JsIncompleteAssigned'
        - type: object
          required:
            - JsIncompleteUnassigned
          properties:
            JsIncompleteUnassigned:
              $ref: '#/components/schemas/JsIncompleteUnassigned'
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
    JsActiveContract:
      title: JsActiveContract
      type: object
      required:
        - createdEvent
        - synchronizerId
        - reassignmentCounter
      properties:
        createdEvent:
          $ref: '#/components/schemas/CreatedEvent'
          description: >-
            The event as it appeared in the context of its last update (i.e.
            daml transaction or

            reassignment). In particular, the last offset, node_id pair is
            preserved.

            The last update is the most recent update created or assigned this
            contract on synchronizer_id synchronizer.

            The offset of the CreatedEvent might point to an already pruned
            update, therefore it cannot necessarily be used

            for lookups.


            Required
        synchronizerId:
          description: |-
            A valid synchronizer id

            Required
          type: string
        reassignmentCounter:
          description: >-
            Each corresponding assigned and unassigned event has the same
            reassignment_counter. This strictly increases

            with each unassign command for the same contract. Creation of the
            contract corresponds to reassignment_counter

            equals zero.

            This field will be the reassignment_counter of the latest observable
            activation event on this synchronizer, which is

            before the active_at_offset.


            Required
          type: integer
          format: int64
    JsEmpty:
      title: JsEmpty
      type: object
    JsIncompleteAssigned:
      title: JsIncompleteAssigned
      type: object
      required:
        - assignedEvent
      properties:
        assignedEvent:
          $ref: '#/components/schemas/JsAssignedEvent'
          description: Required
    JsIncompleteUnassigned:
      title: JsIncompleteUnassigned
      type: object
      required:
        - createdEvent
        - unassignedEvent
      properties:
        createdEvent:
          $ref: '#/components/schemas/CreatedEvent'
          description: >-
            The event as it appeared in the context of its last activation
            update (i.e. daml transaction or

            reassignment). In particular, the last activation offset, node_id
            pair is preserved.

            The last activation update is the most recent update created or
            assigned this contract on synchronizer_id synchronizer before

            the unassigned_event.

            The offset of the CreatedEvent might point to an already pruned
            update, therefore it cannot necessarily be used

            for lookups.


            Required
        unassignedEvent:
          $ref: '#/components/schemas/UnassignedEvent'
          description: Required
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
    JsAssignedEvent:
      title: JsAssignedEvent
      description: >-
        Records that a contract has been assigned, and it can be used on the
        target synchronizer.
      type: object
      required:
        - source
        - target
        - reassignmentId
        - reassignmentCounter
        - createdEvent
      properties:
        source:
          description: |-
            The ID of the source synchronizer.
            Must be a valid synchronizer id.

            Required
          type: string
        target:
          description: |-
            The ID of the target synchronizer.
            Must be a valid synchronizer id.

            Required
          type: string
        reassignmentId:
          description: |-
            The ID from the unassigned event.
            For correlation capabilities.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        submitter:
          description: |-
            Party on whose behalf the assign command was executed.
            Empty if the assignment happened offline via the repair service.
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
        createdEvent:
          $ref: '#/components/schemas/CreatedEvent'
          description: |-
            The offset of this event refers to the offset of the assignment,
            while the node_id is the index of within the batch.

            Required
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
