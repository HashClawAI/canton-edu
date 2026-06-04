---
title: "/v2/dars/validate"
slug: "reference-json-api-reference-v2darsvalidate"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2darsvalidate.md"
source_title: "/v2/dars/validate"
tags:
  - reference
  - json-api-reference
  - v2darsvalidate
---

# /v2/dars/validate

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/dars/validate

> Validates the DAR and checks the upgrade compatibility of the DAR's packages
with the set of the already vetted packages on the target vetting synchronizer.
See ValidateDarFileRequest for details regarding the target vetting synchronizer.

The operation has no effect on the state of the participant or the Canton ledger:
the DAR payload and its packages are not persisted neither are the packages vetted.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/dars/validate
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
  /v2/dars/validate:
    post:
      summary: /v2/dars/validate
      description: >-
        Validates the DAR and checks the upgrade compatibility of the DAR's
        packages

        with the set of the already vetted packages on the target vetting
        synchronizer.

        See ValidateDarFileRequest for details regarding the target vetting
        synchronizer.


        The operation has no effect on the state of the participant or the
        Canton ledger:

        the DAR payload and its packages are not persisted neither are the
        packages vetted.
      operationId: postV2DarsValidate
      parameters:
        - name: synchronizerId
          in: query
          required: false
          schema:
            type: string
      requestBody:
        content:
          application/octet-stream:
            schema:
              type: string
              format: binary
        required: true
      responses:
        '200':
          description: ''
        '400':
          description: >-
            Invalid value, Invalid value for: body, Invalid value for: query
            parameter synchronizerId
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
