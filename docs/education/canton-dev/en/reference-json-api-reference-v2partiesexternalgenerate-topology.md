---
title: "/v2/parties/external/generate-topology"
slug: "reference-json-api-reference-v2partiesexternalgenerate-topology"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2partiesexternalgenerate-topology.md"
source_title: "/v2/parties/external/generate-topology"
tags:
  - reference
  - json-api-reference
  - v2partiesexternalgenerate-topology
---

# /v2/parties/external/generate-topology

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/parties/external/generate-topology

> Alpha 3.3: Convenience endpoint to generate topology transactions for external signing

Expected to be stable in 3.5

You may use this endpoint to generate the common external topology transactions
which can be signed externally and uploaded as part of the allocate party process

Note that this request will create a normal namespace using the same key for the
identity as for signing. More elaborate schemes such as multi-signature
or decentralized parties require you to construct the topology transactions yourself.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/parties/external/generate-topology
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
  /v2/parties/external/generate-topology:
    post:
      summary: /v2/parties/external/generate-topology
      description: >-
        Alpha 3.3: Convenience endpoint to generate topology transactions for
        external signing


        Expected to be stable in 3.5


        You may use this endpoint to generate the common external topology
        transactions

        which can be signed externally and uploaded as part of the allocate
        party process


        Note that this request will create a normal namespace using the same key
        for the

        identity as for signing. More elaborate schemes such as multi-signature

        or decentralized parties require you to construct the topology
        transactions yourself.
      operationId: postV2PartiesExternalGenerate-topology
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/GenerateExternalPartyTopologyRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerateExternalPartyTopologyResponse'
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
    GenerateExternalPartyTopologyRequest:
      title: GenerateExternalPartyTopologyRequest
      type: object
      required:
        - synchronizer
        - partyHint
        - publicKey
      properties:
        synchronizer:
          description: |-
            Synchronizer-id for which we are building this request.
            TODO(#27670) support synchronizer aliases

            Required
          type: string
        partyHint:
          description: >-
            The actual party id will be constructed from this hint and a
            fingerprint of the public key


            Required
          type: string
        publicKey:
          $ref: '#/components/schemas/SigningPublicKey'
          description: |-
            Public key

            Required
        localParticipantObservationOnly:
          description: >-
            If true, then the local participant will only be observing, not
            confirming. Default false.


            Optional
          type: boolean
        otherConfirmingParticipantUids:
          description: |-
            Other participant ids which should be confirming for this party

            Optional: can be empty
          type: array
          items:
            type: string
        confirmationThreshold:
          description: >-
            Confirmation threshold >= 1 for the party. Defaults to all available
            confirmers (or if set to 0).


            Optional
          type: integer
          format: int32
        observingParticipantUids:
          description: |-
            Other observing participant ids for this party

            Optional: can be empty
          type: array
          items:
            type: string
    GenerateExternalPartyTopologyResponse:
      title: GenerateExternalPartyTopologyResponse
      description: >-
        Response message with topology transactions and the multi-hash to be
        signed.
      type: object
      required:
        - partyId
        - publicKeyFingerprint
        - multiHash
        - topologyTransactions
      properties:
        partyId:
          description: |-
            The generated party id

            Required
          type: string
        publicKeyFingerprint:
          description: |-
            The fingerprint of the supplied public key

            Required
          type: string
        topologyTransactions:
          description: >-
            The serialized topology transactions which need to be signed and
            submitted as part of the allocate party process

            Note that the serialization includes the versioning information.
            Therefore, the transaction here is serialized

            as an `UntypedVersionedMessage` which in turn contains the
            serialized `TopologyTransaction` in the version

            supported by the synchronizer.


            Required: must be non-empty
          type: array
          items:
            type: string
        multiHash:
          description: >-
            the multi-hash which may be signed instead of each individual
            transaction


            Required: must be non-empty
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
    SigningPublicKey:
      title: SigningPublicKey
      type: object
      required:
        - format
        - keyData
        - keySpec
      properties:
        format:
          description: |-
            The serialization format of the public key

            Required
          example: CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO
          type: string
        keyData:
          description: |-
            Serialized public key in the format specified above

            Required: must be non-empty
          type: string
        keySpec:
          description: |-
            The key specification

            Required
          example: SIGNING_KEY_SPEC_EC_CURVE25519
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
