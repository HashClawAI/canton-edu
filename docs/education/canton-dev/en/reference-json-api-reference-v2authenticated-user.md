---
title: "/v2/authenticated-user"
slug: "reference-json-api-reference-v2authenticated-user"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2authenticated-user.md"
source_title: "/v2/authenticated-user"
tags:
  - reference
  - json-api-reference
  - v2authenticated-user
---

# /v2/authenticated-user

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/authenticated-user

> Get the user data of the current authenticated user.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/authenticated-user
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
  /v2/authenticated-user:
    get:
      summary: /v2/authenticated-user
      description: Get the user data of the current authenticated user.
      operationId: getV2Authenticated-user
      parameters:
        - name: identity-provider-id
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetUserResponse'
        '400':
          description: >-
            Invalid value, Invalid value for: query parameter
            identity-provider-id
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
    GetUserResponse:
      title: GetUserResponse
      type: object
      required:
        - user
      properties:
        user:
          $ref: '#/components/schemas/User'
          description: |-
            Retrieved user.

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
    User:
      title: User
      description: |2-
         Users and rights
        /////////////////
         Users are used to dynamically manage the rights given to Daml applications.
         They are stored and managed per participant node.
      type: object
      required:
        - id
      properties:
        id:
          description: >-
            The user identifier, which must be a non-empty string of at most 128

            characters that are either alphanumeric ASCII characters or one of
            the symbols "@^$.!`-#+'~_|:()".


            Required
          type: string
        primaryParty:
          description: >-
            The primary party as which this user reads and acts by default on
            the ledger

            *provided* it has the corresponding ``CanReadAs(primary_party)`` or

            ``CanActAs(primary_party)`` rights.

            Ledger API clients SHOULD set this field to a non-empty value for
            all users to

            enable the users to act on the ledger using their own Daml party.

            Users for participant administrators MAY have an associated primary
            party.

            Modifiable


            Optional
          type: string
        isDeactivated:
          description: >-
            When set, then the user is denied all access to the Ledger API.

            Otherwise, the user has access to the Ledger API as per the user's
            rights.

            Modifiable


            Optional
          type: boolean
        metadata:
          $ref: '#/components/schemas/ObjectMeta'
          description: >-
            The metadata of this user.

            Note that the ``metadata.resource_version`` tracks changes to the
            properties described by the ``User`` message and not the user's
            rights.

            Modifiable


            Optional
        identityProviderId:
          description: >-
            The ID of the identity provider configured by ``Identity Provider
            Config``

            If not set, assume the user is managed by the default identity
            provider.


            Optional
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
