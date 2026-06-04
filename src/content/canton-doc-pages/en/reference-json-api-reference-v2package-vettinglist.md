---
title: "/v2/package-vetting/list"
slug: "reference-json-api-reference-v2package-vettinglist"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2package-vettinglist.md"
source_title: "/v2/package-vetting/list"
tags:
  - reference
  - json-api-reference
  - v2package-vettinglist
---

# /v2/package-vetting/list

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/package-vetting/list

> Lists which participant node vetted what packages on which synchronizer.
Can be called by any authenticated user.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/package-vetting/list
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
  /v2/package-vetting/list:
    post:
      summary: /v2/package-vetting/list
      description: |-
        Lists which participant node vetted what packages on which synchronizer.
        Can be called by any authenticated user.
      operationId: postV2Package-vettingList
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ListVettedPackagesRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListVettedPackagesResponse'
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
    ListVettedPackagesRequest:
      title: ListVettedPackagesRequest
      type: object
      properties:
        packageMetadataFilter:
          $ref: '#/components/schemas/PackageMetadataFilter'
          description: >-
            The package metadata filter the returned vetted packages set must
            satisfy.


            Optional
        topologyStateFilter:
          $ref: '#/components/schemas/TopologyStateFilter'
          description: |-
            The topology filter the returned vetted packages set must satisfy.

            Optional
        pageToken:
          description: >-
            Pagination token to determine the specific page to fetch. Using the
            token

            guarantees that ``VettedPackages`` on a subsequent page are all
            greater

            (``VettedPackages`` are sorted by synchronizer ID then participant
            ID) than

            the last ``VettedPackages`` on a previous page.


            The server does not store intermediate results between calls chained
            by a

            series of page tokens. As a consequence, if new vetted packages are
            being

            added and a page is requested twice using the same token, more
            packages can

            be returned on the second call.


            Leave unspecified (i.e. as empty string) to fetch the first page.


            Optional
          type: string
        pageSize:
          description: >-
            Maximum number of ``VettedPackages`` results to return in a single
            page.


            If the page_size is unspecified (i.e. left as 0), the server will
            decide

            the number of results to be returned.


            If the page_size exceeds the maximum supported by the server, an

            error will be returned.


            To obtain the server's maximum consult the PackageService descriptor

            available in the VersionService.


            Optional
          type: integer
          format: int32
    ListVettedPackagesResponse:
      title: ListVettedPackagesResponse
      type: object
      properties:
        vettedPackages:
          description: >-
            All ``VettedPackages`` that contain at least one ``VettedPackage``
            matching

            both a ``PackageMetadataFilter`` and a ``TopologyStateFilter``.

            Sorted by synchronizer_id then participant_id.


            Optional: can be empty
          type: array
          items:
            $ref: '#/components/schemas/VettedPackages'
        nextPageToken:
          description: |-
            Pagination token to retrieve the next page.
            Empty string if there are no further results.

            Optional
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
    PackageMetadataFilter:
      title: PackageMetadataFilter
      description: >-
        Filter the VettedPackages by package metadata.


        A PackageMetadataFilter without package_ids and without
        package_name_prefixes

        matches any vetted package.


        Non-empty fields specify candidate values of which at least one must
        match.

        If both fields are set, then a candidate is returned if it matches one
        of the fields.
      type: object
      properties:
        packageIds:
          description: >-
            If this list is non-empty, any vetted package with a package ID in
            this

            list will match the filter.


            Optional: can be empty
          type: array
          items:
            type: string
        packageNamePrefixes:
          description: >-
            If this list is non-empty, any vetted package with a name matching
            at least

            one prefix in this list will match the filter.


            Optional: can be empty
          type: array
          items:
            type: string
    TopologyStateFilter:
      title: TopologyStateFilter
      description: >-
        Filter the vetted packages by the participant and synchronizer that they
        are

        hosted on.


        Empty fields are ignored, such that a ``TopologyStateFilter`` without

        participant_ids and without synchronizer_ids matches a vetted package
        hosted

        on any participant and synchronizer.


        Non-empty fields specify candidate values of which at least one must
        match.

        If both fields are set then at least one candidate value must match from
        each

        field.
      type: object
      properties:
        participantIds:
          description: >-
            If this list is non-empty, only vetted packages hosted on
            participants

            listed in this field match the filter.

            Query the current Ledger API's participant's ID via the public

            ``GetParticipantId`` command in ``PartyManagementService``.


            Optional: can be empty
          type: array
          items:
            type: string
        synchronizerIds:
          description: >-
            If this list is non-empty, only vetted packages from the topology
            state of

            the synchronizers in this list match the filter.


            Optional: can be empty
          type: array
          items:
            type: string
    VettedPackages:
      title: VettedPackages
      description: >-
        The list of packages vetted on a given participant and synchronizer,
        modelled

        after ``VettedPackages`` in `topology.proto
        <https://github.com/digital-asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_.

        The list only contains packages that matched a filter in the query that

        originated it.
      type: object
      required:
        - participantId
        - synchronizerId
        - topologySerial
        - packages
      properties:
        packages:
          description: >-
            Sorted by package_name and package_version where known, and
            package_id as a

            last resort.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/VettedPackage'
        participantId:
          description: |-
            Participant on which these packages are vetted.

            Required
          type: string
        synchronizerId:
          description: |-
            Synchronizer on which these packages are vetted.

            Required
          type: string
        topologySerial:
          description: >-
            Serial of last ``VettedPackages`` topology transaction of this
            participant

            and on this synchronizer.


            Required
          type: integer
          format: int32
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
    VettedPackage:
      title: VettedPackage
      description: >-
        A package that is vetting on a given participant and synchronizer,

        modelled after ``VettedPackage`` in `topology.proto
        <https://github.com/digital-asset/canton/blob/main/community/base/src/main/protobuf/com/digitalasset/canton/protocol/v30/topology.proto#L206>`_,

        enriched with the package name and version.
      type: object
      required:
        - packageId
      properties:
        packageId:
          description: |-
            Package ID of this package

            Required
          type: string
        validFromInclusive:
          description: >-
            The time from which this package is vetted. Empty if vetting time
            has no

            lower bound.


            Optional
          type: string
        validUntilExclusive:
          description: >-
            The time until which this package is vetted. Empty if vetting time
            has no

            upper bound.


            Optional
          type: string
        packageName:
          description: >-
            Name of this package.

            Only available if the package has been uploaded to the current
            participant.


            Optional
          type: string
        packageVersion:
          description: >-
            Version of this package.

            Only available if the package has been uploaded to the current
            participant.


            Optional
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
