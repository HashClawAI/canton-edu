---
title: "/v2/state/ledger-end"
slug: "reference-json-api-reference-v2stateledger-end"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2stateledger-end.md"
source_title: "/v2/state/ledger-end"
tags:
  - reference
  - json-api-reference
  - v2stateledger-end
---

# /v2/state/ledger-end

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/state/ledger-end

> Get the current ledger end.
Subscriptions started with the returned offset will serve events after this RPC was called.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/state/ledger-end
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
  /v2/state/ledger-end:
    get:
      summary: /v2/state/ledger-end
      description: >-
        Get the current ledger end.

        Subscriptions started with the returned offset will serve events after
        this RPC was called.
      operationId: getV2StateLedger-end
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLedgerEndResponse'
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
    GetLedgerEndResponse:
      title: GetLedgerEndResponse
      type: object
      properties:
        offset:
          description: >-
            It will always be a non-negative integer.

            If zero, the participant view of the ledger is empty.

            If positive, the absolute offset of the ledger as viewed by the
            participant.


            Optional
          type: integer
          format: int64
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
