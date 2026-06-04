---
title: "/v2/version"
slug: "reference-json-api-reference-v2version"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2version.md"
source_title: "/v2/version"
tags:
  - reference
  - json-api-reference
  - v2version
---

# /v2/version

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/version

> Read the Ledger API version



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/version
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
  /v2/version:
    get:
      summary: /v2/version
      description: Read the Ledger API version
      operationId: getV2Version
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLedgerApiVersionResponse'
        '400':
          description: Invalid value
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
    GetLedgerApiVersionResponse:
      title: GetLedgerApiVersionResponse
      type: object
      required:
        - version
        - features
      properties:
        version:
          description: |-
            The version of the ledger API.

            Required
          type: string
        features:
          $ref: '#/components/schemas/FeaturesDescriptor'
          description: |-
            The features supported by this Ledger API endpoint.

            Daml applications CAN use the feature descriptor on top of
            version constraints on the Ledger API version to determine
            whether a given Ledger API endpoint supports the features
            required to run the application.

            See the feature descriptions themselves for the relation between
            Ledger API versions and feature presence.

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
    FeaturesDescriptor:
      title: FeaturesDescriptor
      type: object
      required:
        - experimental
        - userManagement
        - partyManagement
        - offsetCheckpoint
        - packageFeature
      properties:
        experimental:
          $ref: '#/components/schemas/ExperimentalFeatures'
          description: |-
            Features under development or features that are used
            for ledger implementation testing purposes only.

            Daml applications SHOULD not depend on these in production.

            Required
        userManagement:
          $ref: '#/components/schemas/UserManagementFeature'
          description: >-
            If set, then the Ledger API server supports user management.

            It is recommended that clients query this field to gracefully adjust
            their behavior for

            ledgers that do not support user management.


            Required
        partyManagement:
          $ref: '#/components/schemas/PartyManagementFeature'
          description: >-
            If set, then the Ledger API server supports party management
            configurability.

            It is recommended that clients query this field to gracefully adjust
            their behavior to

            maximum party page size.


            Required
        offsetCheckpoint:
          $ref: '#/components/schemas/OffsetCheckpointFeature'
          description: >-
            It contains the timeouts related to the periodic offset checkpoint
            emission


            Required
        packageFeature:
          $ref: '#/components/schemas/PackageFeature'
          description: >-
            If set, then the Ledger API server supports package listing

            configurability. It is recommended that clients query this field to

            gracefully adjust their behavior to maximum package listing page
            size.


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
    ExperimentalFeatures:
      title: ExperimentalFeatures
      description: See the feature message definitions for descriptions.
      type: object
      properties:
        staticTime:
          $ref: '#/components/schemas/ExperimentalStaticTime'
          description: Optional
        commandInspectionService:
          $ref: '#/components/schemas/ExperimentalCommandInspectionService'
          description: Optional
    UserManagementFeature:
      title: UserManagementFeature
      type: object
      required:
        - supported
        - maxRightsPerUser
        - maxUsersPageSize
      properties:
        supported:
          description: |-
            Whether the Ledger API server provides the user management service.

            Required
          type: boolean
        maxRightsPerUser:
          description: >-
            The maximum number of rights that can be assigned to a single user.

            Servers MUST support at least 100 rights per user.

            A value of 0 means that the server enforces no rights per user
            limit.


            Required
          type: integer
          format: int32
        maxUsersPageSize:
          description: >-
            The maximum number of users the server can return in a single
            response (page).

            Servers MUST support at least a 100 users per page.

            A value of 0 means that the server enforces no page size limit.


            Required
          type: integer
          format: int32
    PartyManagementFeature:
      title: PartyManagementFeature
      type: object
      required:
        - maxPartiesPageSize
      properties:
        maxPartiesPageSize:
          description: >-
            The maximum number of parties the server can return in a single
            response (page).


            Required
          type: integer
          format: int32
    OffsetCheckpointFeature:
      title: OffsetCheckpointFeature
      type: object
      required:
        - maxOffsetCheckpointEmissionDelay
      properties:
        maxOffsetCheckpointEmissionDelay:
          $ref: '#/components/schemas/Duration'
          description: |-
            The maximum delay to emmit a new OffsetCheckpoint if it exists

            Required
    PackageFeature:
      title: PackageFeature
      type: object
      required:
        - maxVettedPackagesPageSize
      properties:
        maxVettedPackagesPageSize:
          description: >-
            The maximum number of vetted packages the server can return in a
            single

            response (page) when listing them.


            Required
          type: integer
          format: int32
    ExperimentalStaticTime:
      title: ExperimentalStaticTime
      description: Ledger is in the static time mode and exposes a time service.
      type: object
      required:
        - supported
      properties:
        supported:
          description: Required
          type: boolean
    ExperimentalCommandInspectionService:
      title: ExperimentalCommandInspectionService
      description: Whether the Ledger API supports command inspection service
      type: object
      required:
        - supported
      properties:
        supported:
          description: Required
          type: boolean
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
