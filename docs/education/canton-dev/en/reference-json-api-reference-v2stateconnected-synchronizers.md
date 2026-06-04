---
title: "/v2/state/connected-synchronizers"
slug: "reference-json-api-reference-v2stateconnected-synchronizers"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateconnected-synchronizers.md"
source_title: "/v2/state/connected-synchronizers"
tags:
  - reference
  - json-api-reference
  - v2stateconnected-synchronizers
---

# /v2/state/connected-synchronizers

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/state/connected-synchronizers

> Get the list of connected synchronizers at the time of the query.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/state/connected-synchronizers
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
  /v2/state/connected-synchronizers:
    get:
      summary: /v2/state/connected-synchronizers
      description: Get the list of connected synchronizers at the time of the query.
      operationId: getV2StateConnected-synchronizers
      parameters:
        - name: party
          in: query
          required: false
          schema:
            type: string
        - name: participantId
          in: query
          required: false
          schema:
            type: string
        - name: identityProviderId
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
                $ref: '#/components/schemas/GetConnectedSynchronizersResponse'
        '400':
          description: >-
            Invalid value, Invalid value for: query parameter party, Invalid
            value for: query parameter participantId, Invalid value for: query
            parameter identityProviderId
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
    GetConnectedSynchronizersResponse:
      title: GetConnectedSynchronizersResponse
      type: object
      properties:
        connectedSynchronizers:
          description: 'Optional: can be empty'
          type: array
          items:
            $ref: '#/components/schemas/ConnectedSynchronizer'
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
    ConnectedSynchronizer:
      title: ConnectedSynchronizer
      type: object
      required:
        - synchronizerAlias
        - synchronizerId
      properties:
        synchronizerAlias:
          description: |-
            The alias of the synchronizer

            Required
          type: string
        synchronizerId:
          description: |-
            The ID of the synchronizer

            Required
          type: string
        permission:
          description: |-
            The permission on the synchronizer
            Set if a party was used in the request, otherwise unspecified.

            Optional
          type: string
          enum:
            - PARTICIPANT_PERMISSION_UNSPECIFIED
            - PARTICIPANT_PERMISSION_SUBMISSION
            - PARTICIPANT_PERMISSION_CONFIRMATION
            - PARTICIPANT_PERMISSION_OBSERVATION
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
