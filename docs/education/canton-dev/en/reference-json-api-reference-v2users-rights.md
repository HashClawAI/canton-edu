---
title: "/v2/users/{user-id}/rights"
slug: "reference-json-api-reference-v2users-rights"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2users-rights.md"
source_title: "/v2/users/{user-id}/rights"
tags:
  - reference
  - json-api-reference
  - v2users-rights
---

# /v2/users/{user-id}/rights

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/users/{user-id}/rights

> Revoke rights from a user.
Revoking rights does not affect the resource version of the corresponding user.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml patch /v2/users/{user-id}/rights
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
  /v2/users/{user-id}/rights:
    patch:
      summary: /v2/users/{user-id}/rights
      description: >-
        Revoke rights from a user.

        Revoking rights does not affect the resource version of the
        corresponding user.
      operationId: patchV2UsersUser-idRights
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
              $ref: '#/components/schemas/RevokeUserRightsRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RevokeUserRightsResponse'
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
    RevokeUserRightsRequest:
      title: RevokeUserRightsRequest
      description: >-
        Remove the rights from the set of rights granted to the user.


        Required authorization: ``HasRight(ParticipantAdmin) OR
        IsAuthenticatedIdentityProviderAdmin(identity_provider_id)``
      type: object
      required:
        - userId
      properties:
        userId:
          description: |-
            The user from whom to revoke rights.

            Required
          type: string
        rights:
          description: |-
            The rights to revoke.

            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/Right'
        identityProviderId:
          description: >-
            The id of the ``Identity Provider``

            If not set, assume the user is managed by the default identity
            provider.


            Optional
          type: string
    RevokeUserRightsResponse:
      title: RevokeUserRightsResponse
      type: object
      properties:
        newlyRevokedRights:
          description: |-
            The rights that were actually revoked by the request.

            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/Right'
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
    Right:
      title: Right
      description: A right granted to a user.
      type: object
      properties:
        kind:
          $ref: '#/components/schemas/Kind'
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
    Kind:
      title: Kind
      description: Required
      oneOf:
        - type: object
          required:
            - CanActAs
          properties:
            CanActAs:
              $ref: '#/components/schemas/CanActAs'
        - type: object
          required:
            - CanExecuteAs
          properties:
            CanExecuteAs:
              $ref: '#/components/schemas/CanExecuteAs'
        - type: object
          required:
            - CanExecuteAsAnyParty
          properties:
            CanExecuteAsAnyParty:
              $ref: '#/components/schemas/CanExecuteAsAnyParty'
        - type: object
          required:
            - CanReadAs
          properties:
            CanReadAs:
              $ref: '#/components/schemas/CanReadAs'
        - type: object
          required:
            - CanReadAsAnyParty
          properties:
            CanReadAsAnyParty:
              $ref: '#/components/schemas/CanReadAsAnyParty'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty8'
        - type: object
          required:
            - IdentityProviderAdmin
          properties:
            IdentityProviderAdmin:
              $ref: '#/components/schemas/IdentityProviderAdmin'
        - type: object
          required:
            - ParticipantAdmin
          properties:
            ParticipantAdmin:
              $ref: '#/components/schemas/ParticipantAdmin'
    CanActAs:
      title: CanActAs
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CanActAs1'
    CanExecuteAs:
      title: CanExecuteAs
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CanExecuteAs1'
    CanExecuteAsAnyParty:
      title: CanExecuteAsAnyParty
      description: >-
        The rights of a user to prepare and execute transactions as any party.

        Its utility is predominantly for users that perform interactive
        submissions

        on behalf of many parties.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CanExecuteAsAnyParty1'
    CanReadAs:
      title: CanReadAs
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CanReadAs1'
    CanReadAsAnyParty:
      title: CanReadAsAnyParty
      description: >-
        The rights of a participant's super reader. Its utility is predominantly
        for

        feeding external tools, such as PQS, continually without the need to
        change subscriptions

        as new parties pop in and out of existence.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/CanReadAsAnyParty1'
    Empty8:
      title: Empty
      type: object
    IdentityProviderAdmin:
      title: IdentityProviderAdmin
      description: >-
        The right to administer the identity provider that the user is assigned
        to.

        It means, being able to manage users and parties that are also assigned

        to the same identity provider.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/IdentityProviderAdmin1'
    ParticipantAdmin:
      title: ParticipantAdmin
      description: The right to administer the participant node.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/ParticipantAdmin1'
    CanActAs1:
      title: CanActAs
      type: object
      required:
        - party
      properties:
        party:
          description: |-
            The right to authorize commands for this party.

            Required
          type: string
    CanExecuteAs1:
      title: CanExecuteAs
      type: object
      required:
        - party
      properties:
        party:
          description: >-
            The right to prepare and execute submissions as this party.

            This right does not entitle the user to perform any reads.

            If reading is required, a separate ReadAs right must be added.

            Right to execute as a party is also implicitly contained in the
            CanActAs right.


            Required
          type: string
    CanExecuteAsAnyParty1:
      title: CanExecuteAsAnyParty
      description: >-
        The rights of a user to prepare and execute transactions as any party.

        Its utility is predominantly for users that perform interactive
        submissions

        on behalf of many parties.
      type: object
    CanReadAs1:
      title: CanReadAs
      type: object
      required:
        - party
      properties:
        party:
          description: |-
            The right to read ledger data visible to this party.

            Required
          type: string
    CanReadAsAnyParty1:
      title: CanReadAsAnyParty
      description: >-
        The rights of a participant's super reader. Its utility is predominantly
        for

        feeding external tools, such as PQS, continually without the need to
        change subscriptions

        as new parties pop in and out of existence.
      type: object
    IdentityProviderAdmin1:
      title: IdentityProviderAdmin
      description: >-
        The right to administer the identity provider that the user is assigned
        to.

        It means, being able to manage users and parties that are also assigned

        to the same identity provider.
      type: object
    ParticipantAdmin1:
      title: ParticipantAdmin
      description: The right to administer the participant node.
      type: object
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
