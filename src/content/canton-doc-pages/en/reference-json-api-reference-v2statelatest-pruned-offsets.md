---
title: "/v2/state/latest-pruned-offsets"
slug: "reference-json-api-reference-v2statelatest-pruned-offsets"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2statelatest-pruned-offsets.md"
source_title: "/v2/state/latest-pruned-offsets"
tags:
  - reference
  - json-api-reference
  - v2statelatest-pruned-offsets
---

# /v2/state/latest-pruned-offsets

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/state/latest-pruned-offsets

> Get the latest successfully pruned ledger offsets



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/state/latest-pruned-offsets
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
  /v2/state/latest-pruned-offsets:
    get:
      summary: /v2/state/latest-pruned-offsets
      description: Get the latest successfully pruned ledger offsets
      operationId: getV2StateLatest-pruned-offsets
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetLatestPrunedOffsetsResponse'
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
    GetLatestPrunedOffsetsResponse:
      title: GetLatestPrunedOffsetsResponse
      type: object
      properties:
        participantPrunedUpToInclusive:
          description: >-
            It will always be a non-negative integer.

            If positive, the absolute offset up to which the ledger has been
            pruned,

            disregarding the state of all divulged contracts pruning.

            If zero, the ledger has not been pruned yet.


            Optional
          type: integer
          format: int64
        allDivulgedContractsPrunedUpToInclusive:
          description: >-
            It will always be a non-negative integer.

            If positive, the absolute offset up to which all divulged events
            have been pruned on the ledger.

            It can be at or before the ``participant_pruned_up_to_inclusive``
            offset.

            For more details about all divulged events pruning,

            see ``PruneRequest.prune_all_divulged_contracts`` in
            ``participant_pruning_service.proto``.

            If zero, the divulged events have not been pruned yet.


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
