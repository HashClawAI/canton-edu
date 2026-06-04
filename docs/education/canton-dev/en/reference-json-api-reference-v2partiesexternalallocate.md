---
title: "/v2/parties/external/allocate"
slug: "reference-json-api-reference-v2partiesexternalallocate"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2partiesexternalallocate.md"
source_title: "/v2/parties/external/allocate"
tags:
  - reference
  - json-api-reference
  - v2partiesexternalallocate
---

# /v2/parties/external/allocate

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/parties/external/allocate

> Alpha 3.3: Endpoint to allocate a new external party on a synchronizer

Expected to be stable in 3.5

The external party must be hosted (at least) on this node with either confirmation or observation permissions
It can optionally be hosted on other nodes (then called a multi-hosted party).
If hosted on additional nodes, explicit authorization of the hosting relationship must be performed on those nodes
before the party can be used.
Decentralized namespaces are supported but must be provided fully authorized by their owners.
The individual owner namespace transactions can be submitted in the same call (fully authorized as well).
In the simple case of a non-multi hosted, non-decentralized party, the RPC will return once the party is
effectively allocated and ready to use, similarly to the AllocateParty behavior.
For more complex scenarios applications may need to query the party status explicitly (only through the admin API as of now).



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/parties/external/allocate
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
  /v2/parties/external/allocate:
    post:
      summary: /v2/parties/external/allocate
      description: >-
        Alpha 3.3: Endpoint to allocate a new external party on a synchronizer


        Expected to be stable in 3.5


        The external party must be hosted (at least) on this node with either
        confirmation or observation permissions

        It can optionally be hosted on other nodes (then called a multi-hosted
        party).

        If hosted on additional nodes, explicit authorization of the hosting
        relationship must be performed on those nodes

        before the party can be used.

        Decentralized namespaces are supported but must be provided fully
        authorized by their owners.

        The individual owner namespace transactions can be submitted in the same
        call (fully authorized as well).

        In the simple case of a non-multi hosted, non-decentralized party, the
        RPC will return once the party is

        effectively allocated and ready to use, similarly to the AllocateParty
        behavior.

        For more complex scenarios applications may need to query the party
        status explicitly (only through the admin API as of now).
      operationId: postV2PartiesExternalAllocate
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AllocateExternalPartyRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AllocateExternalPartyResponse'
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
    AllocateExternalPartyRequest:
      title: AllocateExternalPartyRequest
      description: |-
        Required authorization:
          ``HasRight(ParticipantAdmin) OR IsAuthenticatedIdentityProviderAdmin(identity_provider_id) OR IsAuthenticatedUser(user_id)``
      type: object
      required:
        - synchronizer
        - onboardingTransactions
      properties:
        synchronizer:
          description: |-
            TODO(#27670) support synchronizer aliases
            Synchronizer ID on which to onboard the party

            Required
          type: string
        onboardingTransactions:
          description: >-
            TopologyTransactions to onboard the external party

            Can contain:

            - A namespace for the party.

            This can be either a single NamespaceDelegation,

            or DecentralizedNamespaceDefinition along with its authorized
            namespace owners in the form of NamespaceDelegations.

            May be provided, if so it must be fully authorized by the signatures
            in this request combined with the existing topology state.

            - A PartyToParticipant to register the hosting relationship of the
            party, and the party's signing keys and threshold.

            Must be provided.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/SignedTransaction'
        multiHashSignatures:
          description: >-
            Optional signatures of the combined hash of all
            onboarding_transactions

            This may be used instead of providing signatures on each individual
            transaction


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/Signature'
        identityProviderId:
          description: >-
            The id of the ``Identity Provider``

            If not set, assume the party is managed by the default identity
            provider.


            Optional
          type: string
        waitForAllocation:
          description: >-
            When true, this RPC will attempt to wait for the party to be
            allocated on the synchronizer before returning.

            When false, the allocation will happen asynchronously.

            This is a best effort only as this synchronization is only possible
            for non decentralized parties (single hosting node).

            For decentralized parties, this flag is ignored.

            Defaults to true.


            Optional
          type: boolean
        userId:
          description: >-
            The user who will get the act_as rights to the newly allocated
            party.

            If set to an empty string (the default), no user will get rights to
            the party.


            Optional
          type: string
    AllocateExternalPartyResponse:
      title: AllocateExternalPartyResponse
      type: object
      required:
        - partyId
      properties:
        partyId:
          description: |-
            The allocated party id

            Required
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
    SignedTransaction:
      title: SignedTransaction
      type: object
      required:
        - transaction
      properties:
        transaction:
          description: |-
            The serialized TopologyTransaction

            Required: must be non-empty
          type: string
        signatures:
          description: >-
            Additional signatures for this transaction specifically

            Use for transactions that require additional signatures beyond the
            namespace key signatures

            e.g: PartyToParticipant must be signed by all registered keys


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/Signature'
    Signature:
      title: Signature
      type: object
      required:
        - format
        - signature
        - signedBy
        - signingAlgorithmSpec
      properties:
        format:
          description: Required
          type: string
        signature:
          description: 'Required: must be non-empty'
          type: string
        signedBy:
          description: >-
            The fingerprint/id of the keypair used to create this signature and
            needed to verify.


            Required
          type: string
        signingAlgorithmSpec:
          description: |-
            The signing algorithm specification used to produce this signature

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
