---
title: "/v2/interactive-submission/preferred-packages"
slug: "reference-json-api-reference-v2interactive-submissionpreferred-packages"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionpreferred-packages.md"
source_title: "/v2/interactive-submission/preferred-packages"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionpreferred-packages
---

# /v2/interactive-submission/preferred-packages

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/interactive-submission/preferred-packages

> Compute the preferred packages for the vetting requirements in the request.
A preferred package is the highest-versioned package for a provided package-name
that is vetted by all the participants hosting the provided parties.

Ledger API clients should use this endpoint for constructing command submissions
that are compatible with the provided preferred packages, by making informed decisions on:
- which are the compatible packages that can be used to create contracts
- which contract or exercise choice argument version can be used in the command
- which choices can be executed on a template or interface of a contract

If the package preferences could not be computed due to no selection satisfying the requirements,
a `FAILED_PRECONDITION` error will be returned.

Can be accessed by any Ledger API client with a valid token when Ledger API authorization is enabled.

Experimental API: this endpoint is not guaranteed to provide backwards compatibility in future releases



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/preferred-packages
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
  /v2/interactive-submission/preferred-packages:
    post:
      summary: /v2/interactive-submission/preferred-packages
      description: >-
        Compute the preferred packages for the vetting requirements in the
        request.

        A preferred package is the highest-versioned package for a provided
        package-name

        that is vetted by all the participants hosting the provided parties.


        Ledger API clients should use this endpoint for constructing command
        submissions

        that are compatible with the provided preferred packages, by making
        informed decisions on:

        - which are the compatible packages that can be used to create contracts

        - which contract or exercise choice argument version can be used in the
        command

        - which choices can be executed on a template or interface of a contract


        If the package preferences could not be computed due to no selection
        satisfying the requirements,

        a `FAILED_PRECONDITION` error will be returned.


        Can be accessed by any Ledger API client with a valid token when Ledger
        API authorization is enabled.


        Experimental API: this endpoint is not guaranteed to provide backwards
        compatibility in future releases
      operationId: postV2Interactive-submissionPreferred-packages
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GetPreferredPackagesRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GetPreferredPackagesResponse'
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
    GetPreferredPackagesRequest:
      title: GetPreferredPackagesRequest
      type: object
      required:
        - packageVettingRequirements
      properties:
        packageVettingRequirements:
          description: >-
            The package-name vetting requirements for which the preferred
            packages should be resolved.


            Generally it is enough to provide the requirements for the intended
            command's root package-names.

            Additional package-name requirements can be provided when additional
            Daml transaction informees need to use

            package dependencies of the command's root packages.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/PackageVettingRequirement'
        synchronizerId:
          description: >-
            The synchronizer whose vetting state should be used for resolving
            this query.

            If not specified, the vetting states of all synchronizers to which
            the participant is connected are used.


            Optional
          type: string
        vettingValidAt:
          description: >-
            The timestamp at which the package vetting validity should be
            computed

            on the latest topology snapshot as seen by the participant.

            If not provided, the participant's current clock time is used.


            Optional
          type: string
    GetPreferredPackagesResponse:
      title: GetPreferredPackagesResponse
      type: object
      required:
        - synchronizerId
        - packageReferences
      properties:
        packageReferences:
          description: >-
            The package references of the preferred packages.

            Must contain one package reference for each requested package-name.


            If you build command submissions whose content depends on the
            returned

            preferred packages, then we recommend submitting the preferred
            package-ids

            in the ``package_id_selection_preference`` of the command submission
            to

            avoid race conditions with concurrent changes of the on-ledger
            package vetting state.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/PackageReference'
        synchronizerId:
          description: >-
            The synchronizer for which the package preferences are computed.

            If the synchronizer_id was specified in the request, then it matches
            the request synchronizer_id.


            Required
          type: string
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
    PackageVettingRequirement:
      title: PackageVettingRequirement
      description: >-
        Defines a package-name for which the commonly vetted package with the
        highest version must be found.
      type: object
      required:
        - packageName
        - parties
      properties:
        parties:
          description: >-
            The parties whose participants' vetting state should be considered
            when resolving the preferred package.


            Required: must be non-empty
          type: array
          items:
            type: string
        packageName:
          description: |-
            The package-name for which the preferred package should be resolved.

            Required
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
