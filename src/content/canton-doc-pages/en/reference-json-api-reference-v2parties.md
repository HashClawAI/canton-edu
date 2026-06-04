---
title: "/v2/parties/{party}"
slug: "reference-json-api-reference-v2parties"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2parties.md"
source_title: "/v2/parties/{party}"
tags:
  - reference
  - json-api-reference
  - v2parties
---

# /v2/parties/{party}

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/parties/{party}

> Update selected modifiable participant-local attributes of a party details resource.
Can update the participant's local information for local parties.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml patch /v2/parties/{party}
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
  /v2/parties/{party}:
    patch:
      summary: /v2/parties/{party}
      description: >-
        Update selected modifiable participant-local attributes of a party
        details resource.

        Can update the participant's local information for local parties.
      operationId: patchV2PartiesParty
      parameters:
        - name: party
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdatePartyDetailsRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdatePartyDetailsResponse'
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
    UpdatePartyDetailsRequest:
      title: UpdatePartyDetailsRequest
      description: >-
        Required authorization: ``HasRight(ParticipantAdmin) OR
        IsAuthenticatedIdentityProviderAdmin(party_details.identity_provider_id)``
      type: object
      required:
        - partyDetails
        - updateMask
      properties:
        partyDetails:
          $ref: '#/components/schemas/PartyDetails'
          description: |-
            Party to be updated
            Modifiable

            Required
        updateMask:
          $ref: '#/components/schemas/FieldMask'
          description: >-
            An update mask specifies how and which properties of the
            ``PartyDetails`` message are to be updated.

            An update mask consists of a set of update paths.

            A valid update path points to a field or a subfield relative to the
            ``PartyDetails`` message.

            A valid update mask must:


            1. contain at least one update path,

            2. contain only valid update paths.


            Fields that can be updated are marked as ``Modifiable``.

            An update path can also point to non-``Modifiable`` fields such as
            'party' and 'local_metadata.resource_version'

            because they are used:


            1. to identify the party details resource subject to the update,

            2. for concurrent change control.


            An update path can also point to non-``Modifiable`` fields such as
            'is_local'

            as long as the values provided in the update request match the
            server values.

            Examples of update paths: 'local_metadata.annotations',
            'local_metadata'.

            For additional information see the documentation for standard
            protobuf3's ``google.protobuf.FieldMask``.

            For similar Ledger API see
            ``com.daml.ledger.api.v2.admin.UpdateUserRequest``.


            Required
    UpdatePartyDetailsResponse:
      title: UpdatePartyDetailsResponse
      type: object
      required:
        - partyDetails
      properties:
        partyDetails:
          $ref: '#/components/schemas/PartyDetails'
          description: |-
            Updated party details

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
    PartyDetails:
      title: PartyDetails
      type: object
      required:
        - party
      properties:
        party:
          description: |-
            The stable unique identifier of a Daml party.
            Must be a valid PartyIdString (as described in ``value.proto``).

            Required
          type: string
        isLocal:
          description: >-
            true if party is hosted by the participant and the party shares the
            same identity provider as the user issuing the request.


            Optional
          type: boolean
        localMetadata:
          $ref: '#/components/schemas/ObjectMeta'
          description: |-
            Participant-local metadata of this party.
            Modifiable

            Optional
        identityProviderId:
          description: >-
            The id of the ``Identity Provider``

            Optional, if not set, there could be 3 options:


            1. the party is managed by the default identity provider.

            2. party is not hosted by the participant.

            3. party is hosted by the participant, but is outside of the user's
            identity provider.


            Optional
          type: string
    FieldMask:
      title: FieldMask
      type: object
      required:
        - unknownFields
      properties:
        paths:
          type: array
          items:
            type: string
        unknownFields:
          $ref: '#/components/schemas/UnknownFieldSet'
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
    ObjectMeta:
      title: ObjectMeta
      description: >-
        Represents metadata corresponding to a participant resource (e.g. a
        participant user or participant local information about a party).


        Based on ``ObjectMeta`` meta used in Kubernetes API.

        See
        https://github.com/kubernetes/apimachinery/blob/master/pkg/apis/meta/v1/generated.proto#L640
      type: object
      properties:
        resourceVersion:
          description: >-
            An opaque, non-empty value, populated by a participant server which
            represents the internal version of the resource

            this ``ObjectMeta`` message is attached to. The participant server
            will change it to a unique value each time the corresponding
            resource is updated.

            You must not rely on the format of resource version. The participant
            server might change it without notice.

            You can obtain the newest resource version value by issuing a read
            request.

            You may use it for concurrent change detection by passing it back
            unmodified in an update request.

            The participant server will then compare the passed value with the
            value maintained by the system to determine

            if any other updates took place since you had read the resource
            version.

            Upon a successful update you are guaranteed that no other update
            took place during your read-modify-write sequence.

            However, if another update took place during your read-modify-write
            sequence then your update will fail with an appropriate error.

            Concurrent change control is optional. It will be applied only if
            you include a resource version in an update request.

            When creating a new instance of a resource you must leave the
            resource version empty.

            Its value will be populated by the participant server upon
            successful resource creation.


            Optional
          type: string
        annotations:
          $ref: '#/components/schemas/Map_String'
          description: >-
            A set of modifiable key-value pairs that can be used to represent
            arbitrary, client-specific metadata.

            Constraints:


            1. The total size over all keys and values cannot exceed 256kb in
            UTF-8 encoding.

            2. Keys are composed of an optional prefix segment and a required
            name segment such that:

               - key prefix, when present, must be a valid DNS subdomain with at most 253 characters, followed by a '/' (forward slash) character,
               - name segment must have at most 63 characters that are either alphanumeric ([a-z0-9A-Z]), or a '.' (dot), '-' (dash) or '_' (underscore);
                 and it must start and end with an alphanumeric character.

            3. Values can be any non-empty strings.


            Keys with empty prefix are reserved for end-users.

            Properties set by external tools or internally by the participant
            server must use non-empty key prefixes.

            Duplicate keys are disallowed by the semantics of the protobuf3
            maps.

            See: https://developers.google.com/protocol-buffers/docs/proto3#maps

            Annotations may be a part of a modifiable resource.

            Use the resource's update RPC to update its annotations.

            In order to add a new annotation or update an existing one using an
            update RPC, provide the desired annotation in the update request.

            In order to remove an annotation using an update RPC, provide the
            target annotation's key but set its value to the empty string in the
            update request.

            Modifiable


            Optional: can be empty
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
