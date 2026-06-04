---
title: "/v2/commands/async/submit-reassignment"
slug: "reference-json-api-reference-v2commandsasyncsubmit-reassignment"
locale: "en"
category: "reference"
source_url: "https://docs.canton.network/reference/json-api-reference/v2commandsasyncsubmit-reassignment.md"
source_title: "/v2/commands/async/submit-reassignment"
tags:
  - reference
  - json-api-reference
  - v2commandsasyncsubmit-reassignment
---

# /v2/commands/async/submit-reassignment

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# /v2/commands/async/submit-reassignment

> Submit a single reassignment.



## OpenAPI

````yaml /openapi/json-ledger-api/openapi.yaml post /v2/commands/async/submit-reassignment
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
  /v2/commands/async/submit-reassignment:
    post:
      summary: /v2/commands/async/submit-reassignment
      description: Submit a single reassignment.
      operationId: postV2CommandsAsyncSubmit-reassignment
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SubmitReassignmentRequest'
        required: true
      responses:
        '200':
          description: ''
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmitReassignmentResponse'
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
    SubmitReassignmentRequest:
      title: SubmitReassignmentRequest
      type: object
      required:
        - reassignmentCommands
      properties:
        reassignmentCommands:
          $ref: '#/components/schemas/ReassignmentCommands'
          description: |-
            The reassignment command to be submitted.

            Required
    SubmitReassignmentResponse:
      title: SubmitReassignmentResponse
      type: object
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
    ReassignmentCommands:
      title: ReassignmentCommands
      type: object
      required:
        - commandId
        - submitter
        - commands
      properties:
        workflowId:
          description: |-
            Identifier of the on-ledger workflow that this command is a part of.
            Must be a valid LedgerString (as described in ``value.proto``).

            Optional
          type: string
        userId:
          description: >-
            Uniquely identifies the participant user that issued the command.

            Must be a valid UserIdString (as described in ``value.proto``).

            Required unless authentication is used with a user token.

            In that case, the token's user-id will be used for the request's
            user_id.


            Optional
          type: string
        commandId:
          description: >-
            Uniquely identifies the command.

            The triple (user_id, submitter, command_id) constitutes the change
            ID for the intended ledger change.

            The change ID can be used for matching the intended ledger changes
            with all their completions.

            Must be a valid LedgerString (as described in ``value.proto``).


            Required
          type: string
        submitter:
          description: >-
            Party on whose behalf the command should be executed.

            If ledger API authorization is enabled, then the authorization
            metadata must authorize the sender of the request

            to act on behalf of the given party.

            Must be a valid PartyIdString (as described in ``value.proto``).


            Required
          type: string
        submissionId:
          description: >-
            A unique identifier to distinguish completions for different
            submissions with the same change ID.

            Typically a random UUID. Applications are expected to use a
            different UUID for each retry of a submission

            with the same change ID.

            Must be a valid LedgerString (as described in ``value.proto``).


            If omitted, the participant or the committer may set a value of
            their choice.


            Optional
          type: string
        commands:
          description: |-
            Individual elements of this reassignment. Must be non-empty.

            Required: must be non-empty
          type: array
          items:
            $ref: '#/components/schemas/ReassignmentCommand'
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
    ReassignmentCommand:
      title: ReassignmentCommand
      type: object
      properties:
        command:
          $ref: '#/components/schemas/Command1'
    Command1:
      title: Command
      description: >-
        A command can either create a new contract or exercise a choice on an
        existing contract.
      oneOf:
        - type: object
          required:
            - AssignCommand
          properties:
            AssignCommand:
              $ref: '#/components/schemas/AssignCommand'
        - type: object
          required:
            - Empty
          properties:
            Empty:
              $ref: '#/components/schemas/Empty2'
        - type: object
          required:
            - UnassignCommand
          properties:
            UnassignCommand:
              $ref: '#/components/schemas/UnassignCommand'
    AssignCommand:
      title: AssignCommand
      description: Assign a contract
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/AssignCommand1'
    Empty2:
      title: Empty
      type: object
    UnassignCommand:
      title: UnassignCommand
      description: Unassign a contract
      type: object
      required:
        - value
      properties:
        value:
          $ref: '#/components/schemas/UnassignCommand1'
    AssignCommand1:
      title: AssignCommand
      description: Assign a contract
      type: object
      required:
        - reassignmentId
        - source
        - target
      properties:
        reassignmentId:
          description: |-
            The ID from the unassigned event to be completed by this assignment.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        source:
          description: |-
            The ID of the source synchronizer
            Must be a valid synchronizer id

            Required
          type: string
        target:
          description: |-
            The ID of the target synchronizer
            Must be a valid synchronizer id

            Required
          type: string
    UnassignCommand1:
      title: UnassignCommand
      description: Unassign a contract
      type: object
      required:
        - contractId
        - source
        - target
      properties:
        contractId:
          description: |-
            The ID of the contract the client wants to unassign.
            Must be a valid LedgerString (as described in ``value.proto``).

            Required
          type: string
        source:
          description: |-
            The ID of the source synchronizer
            Must be a valid synchronizer id

            Required
          type: string
        target:
          description: |-
            The ID of the target synchronizer
            Must be a valid synchronizer id

            Required
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
