---
title: "/v2/interactive-submission/executeAndWait"
slug: "reference-json-api-reference-v2interactive-submissionexecuteandwait"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2interactive-submissionexecuteandwait.md"
source_title: "/v2/interactive-submission/executeAndWait"
tags:
  - reference
  - json-api-reference
  - v2interactive-submissionexecuteandwait
---

# /v2/interactive-submission/executeAndWait

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/interactive-submission/executeAndWait

> Similar to ExecuteSubmission but _synchronously_ wait for the completion of the transaction
IMPORTANT: Relying on the response from this endpoint requires trusting the Participant Node to be honest.
A malicious node could make a successfully committed request appeared failed and vice versa



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/interactive-submission/executeAndWait
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
  /v2/interactive-submission/executeAndWait:
    post:
      summary: /v2/interactive-submission/executeAndWait
      description: >-
        Similar to ExecuteSubmission but _synchronously_ wait for the completion
        of the transaction

        IMPORTANT: Relying on the response from this endpoint requires trusting
        the Participant Node to be honest.

        A malicious node could make a successfully committed request appeared
        failed and vice versa
      operationId: postV2Interactive-submissionExecuteandwait
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/JsExecuteSubmissionAndWaitRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExecuteSubmissionAndWaitResponse'
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
    JsExecuteSubmissionAndWaitRequest:
      title: JsExecuteSubmissionAndWaitRequest
      type: object
      required:
        - preparedTransaction
        - partySignatures
        - submissionId
        - hashingSchemeVersion
      properties:
        preparedTransaction:
          description: >-
            the prepared transaction

            Typically this is the value of the `prepared_transaction` field in
            `PrepareSubmissionResponse`

            obtained from calling `prepareSubmission`.


            Required
          type: string
        partySignatures:
          $ref: '#/components/schemas/PartySignatures'
          description: >-
            The party(ies) signatures that authorize the prepared submission to
            be executed by this node.

            Each party can provide one or more signatures..

            and one or more parties can sign.

            Note that currently, only single party submissions are supported.


            Required
        deduplicationPeriod:
          $ref: '#/components/schemas/DeduplicationPeriod2'
        submissionId:
          description: >-
            A unique identifier to distinguish completions for different
            submissions with the same change ID.

            Typically a random UUID. Applications are expected to use a
            different UUID for each retry of a submission

            with the same change ID.

            Must be a valid LedgerString (as described in ``value.proto``).


            Required
          type: string
        userId:
          description: |-
            See [PrepareSubmissionRequest.user_id]

            Optional
          type: string
        hashingSchemeVersion:
          description: |-
            The hashing scheme version used when building the hash

            Required
          type: string
          enum:
            - HASHING_SCHEME_VERSION_UNSPECIFIED
            - HASHING_SCHEME_VERSION_V2
            - HASHING_SCHEME_VERSION_V3
        minLedgerTime:
          $ref: '#/components/schemas/MinLedgerTime'
          description: >-
            If set will influence the chosen ledger effective time but will not
            result in a submission delay so any override

            should be scheduled to executed within the window allowed by
            synchronizer.


            Optional
    ExecuteSubmissionAndWaitResponse:
      title: ExecuteSubmissionAndWaitResponse
      type: object
      required:
        - updateId
        - completionOffset
      properties:
        updateId:
          description: |-
            The id of the transaction that resulted from the submitted command.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        completionOffset:
          description: >-
            The details of the offset field are described in
            ``community/ledger-api/README.md``.


            Required
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
    PartySignatures:
      title: PartySignatures
      description: Additional signatures provided by the submitting parties
      type: object
      required:
        - signatures
      properties:
        signatures:
          description: |-
            Additional signatures provided by all individual parties

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/SinglePartySignatures'
    DeduplicationPeriod2:
      title: DeduplicationPeriod
      oneOf:
        - type: object
          required:
            - DeduplicationDuration
          properties:
            DeduplicationDuration:
              $ref: '#/components/schemas/DeduplicationDuration2'
        - type: object
          required:
            - DeduplicationOffset
          properties:
            DeduplicationOffset:
              $ref: '#/components/schemas/DeduplicationOffset2'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty10'
    MinLedgerTime:
      title: MinLedgerTime
      type: object
      properties:
        time:
          $ref: '#/components/schemas/Time'
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
    SinglePartySignatures:
      title: SinglePartySignatures
      description: Signatures provided by a single party
      type: object
      required:
        - party
        - signatures
      properties:
        party:
          description: |-
            Submitting party

            Required
          type: string
        signatures:
          description: |-
            Signatures

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/Signature'
    DeduplicationDuration2:
      title: DeduplicationDuration
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Duration'
    DeduplicationOffset2:
      title: DeduplicationOffset
      type: object
      required:
        - value
      properties:
        value:
          type: integer
          format: int64
    Empty10:
      title: Empty
      type: object
    Time:
      title: Time
      description: Required
      oneOf:
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty9'
        - type: object
          required:
            - MinLedgerTimeAbs
          properties:
            MinLedgerTimeAbs:
              $ref: '#/components/schemas/MinLedgerTimeAbs'
        - type: object
          required:
            - MinLedgerTimeRel
          properties:
            MinLedgerTimeRel:
              $ref: '#/components/schemas/MinLedgerTimeRel'
    Signature:
      title: Signature
      type: object
      required:
        - format
        - signature
        - signedBy
        - signingAlgorithmSpec
      properties:
        format:
          description: Required
          type: string
        signature:
          description: 'Required: must be non-empty'
          type: string
        signedBy:
          description: >-
            The fingerprint/id of the keypair used to create this signature and
            needed to verify.


            Required
          type: string
        signingAlgorithmSpec:
          description: |-
            The signing algorithm specification used to produce this signature

            Required
          type: string
    Duration:
      title: Duration
      type: object
      required:
        - seconds
        - nanos
      properties:
        seconds:
          type: integer
          format: int64
        nanos:
          type: integer
          format: int32
        unknownFields:
          $ref: '#/components/schemas/UnknownFieldSet'
          description: >-
            This field is automatically added as part of protobuf to json
            mapping
    Empty9:
      title: Empty
      type: object
    MinLedgerTimeAbs:
      title: MinLedgerTimeAbs
      type: object
      required:
        - value
      properties:
        value:
          type: string
    MinLedgerTimeRel:
      title: MinLedgerTimeRel
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/Duration'
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
