---
title: "/v2/idps/{idp-id}"
slug: "reference-json-api-reference-v2idps"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2idps.md"
source_title: "/v2/idps/{idp-id}"
tags:
  - reference
  - json-api-reference
  - v2idps
---

# /v2/idps/{idp-id}

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/idps/{idp-id}

> Update selected modifiable attribute of an identity provider config resource described
by the ``IdentityProviderConfig`` message.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml patch /v2/idps/{idp-id}
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
  /v2/idps/{idp-id}:
    patch:
      summary: /v2/idps/{idp-id}
      description: >-
        Update selected modifiable attribute of an identity provider config
        resource described

        by the ``IdentityProviderConfig`` message.
      operationId: patchV2IdpsIdp-id
      parameters:
        - name: idp-id
          in: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateIdentityProviderConfigRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateIdentityProviderConfigResponse'
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
    UpdateIdentityProviderConfigRequest:
      title: UpdateIdentityProviderConfigRequest
      type: object
      required:
        - identityProviderConfig
        - updateMask
      properties:
        identityProviderConfig:
          $ref: '#/components/schemas/IdentityProviderConfig'
          description: |-
            The identity provider config to update.
            Modifiable

            Required
        updateMask:
          $ref: '#/components/schemas/FieldMask'
          description: >-
            An update mask specifies how and which properties of the
            ``IdentityProviderConfig`` message are to be updated.

            An update mask consists of a set of update paths.

            A valid update path points to a field or a subfield relative to the
            ``IdentityProviderConfig`` message.

            A valid update mask must:


            1. contain at least one update path,

            2. contain only valid update paths.


            Fields that can be updated are marked as ``Modifiable``.

            For additional information see the documentation for standard
            protobuf3's ``google.protobuf.FieldMask``.


            Required
    UpdateIdentityProviderConfigResponse:
      title: UpdateIdentityProviderConfigResponse
      type: object
      required:
        - identityProviderConfig
      properties:
        identityProviderConfig:
          $ref: '#/components/schemas/IdentityProviderConfig'
          description: |-
            Updated identity provider config

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
    IdentityProviderConfig:
      title: IdentityProviderConfig
      type: object
      required:
        - identityProviderId
        - issuer
        - jwksUrl
      properties:
        identityProviderId:
          description: |-
            The identity provider identifier
            Must be a valid LedgerString (as describe in ``value.proto``).

            Required
          type: string
        isDeactivated:
          description: >-
            When set, the callers using JWT tokens issued by this identity
            provider are denied all access

            to the Ledger API.

            Modifiable


            Optional
          type: boolean
        issuer:
          description: >-
            Specifies the issuer of the JWT token.

            The issuer value is a case sensitive URL using the https scheme that
            contains scheme, host,

            and optionally, port number and path components and no query or
            fragment components.

            Modifiable


            Can be left empty when used in `UpdateIdentityProviderConfigRequest`
            if the issuer is not being updated.


            Required
          type: string
        jwksUrl:
          description: >-
            The JWKS (JSON Web Key Set) URL.

            The Ledger API uses JWKs (JSON Web Keys) from the provided URL to
            verify that the JWT has been

            signed with the loaded JWK. Only RS256 (RSA Signature with SHA-256)
            signing algorithm is supported.

            Modifiable


            Required
          type: string
        audience:
          description: >-
            Specifies the audience of the JWT token.

            When set, the callers using JWT tokens issued by this identity
            provider are allowed to get an access

            only if the "aud" claim includes the string specified here

            Modifiable


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
