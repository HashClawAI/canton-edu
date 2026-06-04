---
title: "/v2/users/{user-id}/identity-provider-id"
slug: "reference-json-api-reference-v2users-identity-provider-id"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2users-identity-provider-id.md"
source_title: "/v2/users/{user-id}/identity-provider-id"
tags:
  - reference
  - json-api-reference
  - v2users-identity-provider-id
---

# /v2/users/{user-id}/identity-provider-id

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/users/{user-id}/identity-provider-id

> Update the assignment of a user from one IDP to another.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml patch /v2/users/{user-id}/identity-provider-id
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
  /v2/users/{user-id}/identity-provider-id:
    patch:
      summary: /v2/users/{user-id}/identity-provider-id
      description: Update the assignment of a user from one IDP to another.
      operationId: patchV2UsersUser-idIdentity-provider-id
      parameters:
        - name: user-id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUserIdentityProviderIdRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateUserIdentityProviderIdResponse'
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
    UpdateUserIdentityProviderIdRequest:
      title: UpdateUserIdentityProviderIdRequest
      description: 'Required authorization: ``HasRight(ParticipantAdmin)``'
      type: object
      required:
        - userId
      properties:
        userId:
          description: |-
            User to update

            Required
          type: string
        sourceIdentityProviderId:
          description: |-
            Current identity provider ID of the user
            If omitted, the default IDP is assumed

            Optional
          type: string
        targetIdentityProviderId:
          description: |-
            Target identity provider ID of the user
            If omitted, the default IDP is assumed

            Optional
          type: string
    UpdateUserIdentityProviderIdResponse:
      title: UpdateUserIdentityProviderIdResponse
      type: object
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
