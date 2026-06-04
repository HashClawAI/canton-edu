---
title: "/v2/package-vetting"
slug: "reference-json-api-reference-v2package-vetting"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2package-vetting.md"
source_title: "/v2/package-vetting"
tags:
  - reference
  - json-api-reference
  - v2package-vetting
---

# /v2/package-vetting

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/package-vetting

> Update the vetted packages of this participant
This endpoint (POST /package-vetting) is deprecated and will be removed in a future release. Please use POST /package-vetting/update instead.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/package-vetting
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
  /v2/package-vetting:
    post:
      summary: /v2/package-vetting
      description: >-
        Update the vetted packages of this participant

        This endpoint (POST /package-vetting) is deprecated and will be removed
        in a future release. Please use POST /package-vetting/update instead.
      operationId: postV2Package-vetting
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateVettedPackagesRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UpdateVettedPackagesResponse'
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
      deprecated: true
      security:
        - httpAuth: []
        - apiKeyAuth: []
components:
  schemas:
    UpdateVettedPackagesRequest:
      title: UpdateVettedPackagesRequest
      type: object
      required:
        - changes
      properties:
        changes:
          description: >-
            Changes to apply to the current vetting state of the participant on
            the

            specified synchronizer. The changes are applied in order.

            Any package not changed will keep their previous vetting state.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/VettedPackagesChange'
        dryRun:
          description: >-
            If dry_run is true, then the changes are only prepared, but not
            applied. If

            a request would trigger an error when run (e.g.
            TOPOLOGY_DEPENDENCIES_NOT_VETTED),

            it will also trigger an error when dry_run.


            Use this flag to preview a change before applying it.

            Defaults to false.


            Optional
          type: boolean
        synchronizerId:
          description: >-
            If set, the requested changes will take place on the specified

            synchronizer. If synchronizer_id is unset and the participant is
            only

            connected to a single synchronizer, that synchronizer will be used
            by

            default. If synchronizer_id is unset and the participant is
            connected to

            multiple synchronizers, the request will error out with

            PACKAGE_SERVICE_CANNOT_AUTODETECT_SYNCHRONIZER.


            Optional
          type: string
        expectedTopologySerial:
          $ref: '#/components/schemas/PriorTopologySerial'
          description: >-
            The serial of the last ``VettedPackages`` topology transaction of
            this

            participant and on this synchronizer.


            Execution of the request fails if this is not correct. Use this to
            guard

            against concurrent changes.


            If left unspecified, no validation is done against the last
            transaction's

            serial.


            Optional
        updateVettedPackagesForceFlags:
          description: |-
            Controls whether potentially unsafe vetting updates are allowed.

            Optional: can be empty
          type: array
          items:
            type: string
            enum:
              - UPDATE_VETTED_PACKAGES_FORCE_FLAG_UNSPECIFIED
              - >-
                UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_VET_INCOMPATIBLE_UPGRADES
              - UPDATE_VETTED_PACKAGES_FORCE_FLAG_ALLOW_UNVETTED_DEPENDENCIES
    UpdateVettedPackagesResponse:
      title: UpdateVettedPackagesResponse
      type: object
      required:
        - newVettedPackages
      properties:
        pastVettedPackages:
          $ref: '#/components/schemas/VettedPackages'
          description: >-
            All vetted packages on this participant and synchronizer, before the

            specified changes. Empty if no vetting state existed beforehand.


            Not populated if no vetted topology state exists prior to the
            update.


            Optional
        newVettedPackages:
          $ref: '#/components/schemas/VettedPackages'
          description: >-
            All vetted packages on this participant and synchronizer, after the
            specified changes.


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
    VettedPackagesChange:
      title: VettedPackagesChange
      description: A change to the set of vetted packages.
      type: object
      properties:
        operation:
          $ref: '#/components/schemas/Operation'
    PriorTopologySerial:
      title: PriorTopologySerial
      description: |-
        The serial of last ``VettedPackages`` topology transaction on a given
        participant and synchronizer.
      type: object
      properties:
        serial:
          $ref: '#/components/schemas/Serial'
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
    Operation:
      title: Operation
      description: Required
      oneOf:
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty5'
        - type: object
          required:
            - Unvet
          properties:
            Unvet:
              $ref: '#/components/schemas/Unvet'
        - type: object
          required:
            - Vet
          properties:
            Vet:
              $ref: '#/components/schemas/Vet'
    Serial:
      title: Serial
      description: Optional
      oneOf:
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty6'
        - type: object
          required:
            - NoPrior
          properties:
            NoPrior:
              $ref: '#/components/schemas/NoPrior'
        - type: object
          required:
            - Prior
          properties:
            Prior:
              $ref: '#/components/schemas/Prior'
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
    Empty5:
      title: Empty
      type: object
    Unvet:
      title: Unvet
      description: Remove packages from the set of vetted packages
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Unvet1'
    Vet:
      title: Vet
      description: >-
        Set vetting bounds of a list of packages. Packages that were not
        previously

        vetted have their bounds added, previous vetting bounds are overwritten.
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Vet1'
    Empty6:
      title: Empty
      type: object
    NoPrior:
      title: NoPrior
      type: object
    Prior:
      title: Prior
      type: object
      required:
        - value
      properties:
        value:
          type: integer
          format: int32
    Unvet1:
      title: Unvet
      description: Remove packages from the set of vetted packages
      type: object
      required:
        - packages
      properties:
        packages:
          description: |-
            Packages to be unvetted.

            If a reference in this list matches multiple packages, they are all
            unvetted.

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/VettedPackagesRef'
    Vet1:
      title: Vet
      description: >-
        Set vetting bounds of a list of packages. Packages that were not
        previously

        vetted have their bounds added, previous vetting bounds are overwritten.
      type: object
      required:
        - packages
      properties:
        packages:
          description: >-
            Packages to be vetted.


            If a reference in this list matches more than one package, the
            change is

            considered ambiguous and the entire update request is rejected. In
            other

            words, every reference must match exactly one package.


            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/VettedPackagesRef'
        newValidFromInclusive:
          description: >-
            The time from which these packages should be vetted, prior lower
            bounds

            are overwritten.

            Optional
          type: string
        newValidUntilExclusive:
          description: >-
            The time until which these packages should be vetted, prior upper
            bounds

            are overwritten.

            Optional
          type: string
    VettedPackagesRef:
      title: VettedPackagesRef
      description: >-
        A reference to identify one or more packages.


        A reference matches a package if its ``package_id`` matches the
        package's ID,

        its ``package_name`` matches the package's name, and its
        ``package_version``

        matches the package's version. If an attribute in the reference is left

        unspecified (i.e. as an empty string), that attribute is treated as a

        wildcard. At a minimum, ``package_id`` or the ``package_name`` must be

        specified.


        If a reference does not match any package, the reference is considered

        unresolved and the entire update request is rejected.
      type: object
      properties:
        packageId:
          description: |-
            Package's package id must be the same as this field.

            Optional
          type: string
        packageName:
          description: |-
            Package's name must be the same as this field.

            Optional
          type: string
        packageVersion:
          description: |-
            Package's version must be the same as this field.

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
