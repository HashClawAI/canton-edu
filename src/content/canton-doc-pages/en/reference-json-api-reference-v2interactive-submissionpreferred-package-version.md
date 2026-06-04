---
title: "/v2/interactive-submission/preferred-package-version"
slug: "reference-json-api-reference-v2interactive-submissionpreferred-package-version"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionpreferred-package-version.md"
source_title: "/v2/interactive-submission/preferred-package-version"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionpreferred-package-version
---

# /v2/interactive-submission/preferred-package-version

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/interactive-submission/preferred-package-version

> A preferred package is the highest-versioned package for a provided package-name
that is vetted by all the participants hosting the provided parties.

Ledger API clients should use this endpoint for constructing command submissions
that are compatible with the provided preferred package, by making informed decisions on:
- which are the compatible packages that can be used to create contracts
- which contract or exercise choice argument version can be used in the command
- which choices can be executed on a template or interface of a contract

Can be accessed by any Ledger API client with a valid token when Ledger API authorization is enabled.

Provided for backwards compatibility, it will be removed in the Canton version 3.4.0



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml get /v2/interactive-submission/preferred-package-version
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
  /v2/interactive-submission/preferred-package-version:
    get:
      summary: /v2/interactive-submission/preferred-package-version
      description: >-
        A preferred package is the highest-versioned package for a provided
        package-name

        that is vetted by all the participants hosting the provided parties.


        Ledger API clients should use this endpoint for constructing command
        submissions

        that are compatible with the provided preferred package, by making
        informed decisions on:

        - which are the compatible packages that can be used to create contracts

        - which contract or exercise choice argument version can be used in the
        command

        - which choices can be executed on a template or interface of a contract


        Can be accessed by any Ledger API client with a valid token when Ledger
        API authorization is enabled.


        Provided for backwards compatibility, it will be removed in the Canton
        version 3.4.0
      operationId: getV2Interactive-submissionPreferred-package-version
      parameters:
        - name: parties
          in: query
          required: false
          schema:
            type: array
            items:
              type: string
        - name: package-name
          in: query
          required: true
          schema:
            type: string
        - name: vetting_valid_at
          in: query
          required: false
          schema:
            type: string
            format: date-time
        - name: synchronizer-id
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
                $ref: '#/components/schemas/GetPreferredPackageVersionResponse'
        '400':
          description: >-
            Invalid value, Invalid value for: query parameter parties, Invalid
            value for: query parameter package-name, Invalid value for: query
            parameter vetting_valid_at, Invalid value for: query parameter
            synchronizer-id
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
    GetPreferredPackageVersionResponse:
      title: GetPreferredPackageVersionResponse
      type: object
      properties:
        packagePreference:
          $ref: '#/components/schemas/PackagePreference'
          description: |-
            Not populated when no preferred package is found

            Optional
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
    PackagePreference:
      title: PackagePreference
      type: object
      required:
        - synchronizerId
        - packageReference
      properties:
        packageReference:
          $ref: '#/components/schemas/PackageReference'
          description: |-
            The package reference of the preferred package.

            Required
        synchronizerId:
          description: >-
            The synchronizer for which the preferred package was computed.

            If the synchronizer_id was specified in the request, then it matches
            the request synchronizer_id.


            Required
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
    PackageReference:
      title: PackageReference
      type: object
      required:
        - packageId
        - packageName
        - packageVersion
      properties:
        packageId:
          description: Required
          type: string
        packageName:
          description: Required
          type: string
        packageVersion:
          description: Required
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
