---
title: "/v2/events/events-by-contract-id"
slug: "reference-json-api-reference-v2eventsevents-by-contract-id"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2eventsevents-by-contract-id.md"
source_title: "/v2/events/events-by-contract-id"
tags:
  - reference
  - json-api-reference
  - v2eventsevents-by-contract-id
---

# /v2/events/events-by-contract-id

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/events/events-by-contract-id

> Get the create and the consuming exercise event for the contract with the provided ID.
No events will be returned for contracts that have been pruned because they
have already been archived before the latest pruning offset.
If the contract cannot be found for the request, or all the contract-events are filtered, a CONTRACT_EVENTS_NOT_FOUND error will be raised.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/events/events-by-contract-id
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
  /v2/events/events-by-contract-id:
    post:
      summary: /v2/events/events-by-contract-id
      description: >-
        Get the create and the consuming exercise event for the contract with
        the provided ID.

        No events will be returned for contracts that have been pruned because
        they

        have already been archived before the latest pruning offset.

        If the contract cannot be found for the request, or all the
        contract-events are filtered, a CONTRACT_EVENTS_NOT_FOUND error will be
        raised.
      operationId: postV2EventsEvents-by-contract-id
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetEventsByContractIdRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsGetEventsByContractIdResponse'
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
    GetEventsByContractIdRequest:
      title: GetEventsByContractIdRequest
      type: object
      required:
        - contractId
        - eventFormat
      properties:
        contractId:
          description: |-
            The contract id being queried.

            Required
          type: string
        eventFormat:
          $ref: '#/components/schemas/EventFormat'
          description: >-
            Format of the events in the result, the presentation will be of
            TRANSACTION_SHAPE_ACS_DELTA.


            Required
    JsGetEventsByContractIdResponse:
      title: JsGetEventsByContractIdResponse
      type: object
      properties:
        created:
          $ref: '#/components/schemas/JsCreated'
          description: >-
            The create event for the contract with the ``contract_id`` given in
            the request

            provided it exists and has not yet been pruned.


            Optional
        archived:
          $ref: '#/components/schemas/JsArchived'
          description: >-
            The archive event for the contract with the ``contract_id`` given in
            the request

            provided such an archive event exists and it has not yet been
            pruned.


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
    JsCreated:
      title: JsCreated
      type: object
      required:
        - createdEvent
        - synchronizerId
      properties:
        createdEvent:
          $ref: '#/components/schemas/CreatedEvent'
          description: >-
            The event as it appeared in the context of its original update (i.e.
            daml transaction or

            reassignment) on this participant node. You can use its offset and
            node_id to find the

            corresponding update and the node within it.


            Required
        synchronizerId:
          description: |-
            The synchronizer which sequenced the creation of the contract

            Required
          type: string
    JsArchived:
      title: JsArchived
      type: object
      required:
        - archivedEvent
        - synchronizerId
      properties:
        archivedEvent:
          $ref: '#/components/schemas/ArchivedEvent'
          description: Required
        synchronizerId:
          description: |-
            The synchronizer which sequenced the archival of the contract

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
