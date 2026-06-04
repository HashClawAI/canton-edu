---
title: "Values in the Ledger API"
slug: "appdev-deep-dives-values-in-the-ledger-api"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/deep-dives/values-in-the-ledger-api.md"
source_title: "Values in the Ledger API"
tags:
  - appdev
  - deep-dives
  - values-in-the-ledger-api
---

# Values in the Ledger API

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Values in the Ledger API

> Validation, normalization, and dynamic package resolution rules for values exchanged over the Ledger API.

Commands and queries have relaxed validation rules for ingested values. Returned values are subject to normalization.

### Value Validation in Commands

In the following examples, the *target template* of a command is the template or interface identified by the `template_id` field of the command after dynamic package resolution.

A value featured in a command (e.g. `create_arguments`) has *expected type* `T` if the value needs to type-check against `T` in order to satisfy the type signatures of the target template of the command. Note that this definition necessarily extends to sub-values.

In a record value of the form `Constructor { field1 = v1, ..., fieldn = vn }`, `vi` is a *trailing None* if for all `n >= j >= i`, `vj = None`.

On submission of a command, the validation rules for values are relaxed as follows:

> * The `record_id`, `variant_id`, and `enum_id` fields of values, if present, are only checked against the module and type name of the expected type for that value. The package ID component of these fields is ignored.
> * In record values where all field names are provided, *any* fields of value None may be omitted.
> * In record values where not all field names are provided, fields must be provided in the same order as that of the record type definition, and trailing Nones may be omitted.

These rules apply for all sub-values.

**Example 1**

Assume a package called `example1-1.0.0` which defines a template called `T` in a module called `Main`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Main where

template T
  with
    p : Party
  where
    signatory p
```

Assume another package called `other-1.0.0` which defines a different template also called `T` in a module also called `Main`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Main where

template T
  with
    s : Party
    i : Int
  where
    signatory s
```

Then the ledger API will accept Create commands for `example1-1.0.0:Main.T` whose create arguments are annotated with type `other-1.0.0:T:Main.T`, even though the type annotation is wrong. In other words, the following console commands succeed:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val createCmd = Command(
    command = Command.Command.Create(
      value = CreateCommand(
        templateId = Some(
          value = Identifier(packageId = packageIdExample1, moduleName = "Main", entityName = "T")),
        createArguments = Some(
          value = Record(
            recordId = Some(
              Identifier(
                packageId = packageIdOther,
                moduleName = "Main",
                entityName = "T"
              )
            ),
            fields = Seq(
              RecordField(
                label = "p",
                value = Some(
                  value = Value(sum = Value.Sum.Party(value = sandbox.adminParty.toLf))
                )
              )
            )
          )
        )
      )
    )
  )

@ sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd))
```

This is because the module and type names of the type annotation, `Main` and `T`, match those of the expected type: `example1-1.0.0:Main.T`.

**Example 2**

Assume a package called `example2-1.0.0` which defines a template with two optional fields: one in leading position, and one in trailing position.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Main where

template T
  with
    i : Optional Int
    p : Party
    j : Optional Int
  where
    signatory p
```

Then submitting a Create command for `example2-1.0.0:Main.T` which only provides `p` by name and no other field succeeds:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val createCmd = Command(
    command = Command.Command.Create(
      value = CreateCommand(
        templateId = Some(value = Identifier(packageId = packageIdExample2, moduleName = "Main", entityName = "T")),
        createArguments = Some(
          value = Record(
            recordId = None,
            fields = Seq(
              RecordField(
                label = "p",
                value = Some(value = Value(sum = Value.Sum.Party(value = sandbox.adminParty.toLf)))
              )
            )
          )
        )
      )
    )
  ) 

@ sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd)) 
res13: com.daml.ledger.api.v1.transaction.TransactionTree = TransactionTree(
  ...
  eventsById = Map(
    "#122062d3d0b89f011ac651ea0139f381a73fe080ab215e5970a8c7bf804edeec932c:0" -> TreeEvent(
      kind = Created(
        value = CreatedEvent(
          ...
          createArguments = Some(
            value = Record(
              recordId = Some(value = Identifier(packageId = "627f4ad4df901b80bae208eded1c03932f38ed9c1f44c50468f27c88ef988e25", moduleName = "Main", entityName = "T")),
              fields = Vector(
                RecordField(label = "i", value = Some(value = Value(sum = Optional(value = Optional(value = None))))),
                RecordField(label = "p", value = Some(value = Value(sum = Party(value = "sandbox::1220077e3366037ffce33cba97d757506fc1c72ad957a9b86c6bf137404637c7fee3")))),
                RecordField(label = "j", value = Some(value = Value(sum = Optional(value = Optional(value = None)))))
              )
            )
          ),
          ...
        )
      )
    )
  ),
  ...
)
```

Submitting the same command but with no label for field `p` fails:

```
@ val createCmd = Command(
    command = Command.Command.Create(
      value = CreateCommand(
        templateId = Some(value = Identifier(packageId = packageIdExample2, moduleName = "Main", entityName = "T")),
        createArguments = Some(
          value = Record(
            recordId = None,
            fields = Seq(
              RecordField(
                label = "",
                value = Some(value = Value(sum = Value.Sum.Party(value = sandbox.adminParty.toLf)))
              )
            )
          )
        )
      )
    )
  ) 

@ sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd)) 

ERROR c.d.c.e.CommunityConsoleEnvironment - Request failed for sandbox.
  GrpcClientError: INVALID_ARGUMENT/COMMAND_PREPROCESSING_FAILED(8,b880be91): Missing non-optional field "p", cannot upgrade non-optional fields.
  Request: SubmitAndWaitTransactionTree(
  actAs = sandbox::1220077e3366...,
  readAs = Seq(),
  commandId = '',
  workflowId = '',
  submissionId = '',
  deduplicationPeriod = None(),
  applicationId = 'CantonConsole',
  commands = ...
)
...
```

However, providing all but the trailing optional field `j` suceeds, even without labels:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val createCmd = Command(
    command = Command.Command.Create(
      value = CreateCommand(
        templateId = Some(value = Identifier(packageId = packageIdExample2, moduleName = "Main", entityName = "T")),
        createArguments = Some(
          value = Record(
            recordId = None,
            fields = Seq(
              RecordField(label = "", value = Some(value = Value(sum = Value.Sum.Optional(value = Optional(value = None))))),
              RecordField(
                label = "",
                value = Some(value = Value(sum = Value.Sum.Party(value = sandbox.adminParty.toLf)))
              )
            )
          )
        )
      )
    )
  ) 

@ sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd)) 
res22: com.daml.ledger.api.v1.transaction.TransactionTree = TransactionTree(
  ...
  eventsById = Map(
    "#12203bb4082d4868c393ca2c969bb639757d21992cbac2a1abad271d688a30dbcae6:0" -> TreeEvent(
      kind = Created(
        value = CreatedEvent(
          ...
          createArguments = Some(
            value = Record(
              recordId = Some(value = Identifier(packageId = "627f4ad4df901b80bae208eded1c03932f38ed9c1f44c50468f27c88ef988e25", moduleName = "Main", entityName = "T")),
              fields = Vector(
                RecordField(label = "i", value = Some(value = Value(sum = Optional(value = Optional(value = None))))),
                RecordField(label = "p", value = Some(value = Value(sum = Party(value = "sandbox::1220077e3366037ffce33cba97d757506fc1c72ad957a9b86c6bf137404637c7fee3")))),
                RecordField(label = "j", value = Some(value = Value(sum = Optional(value = Optional(value = None)))))
              )
            )
          ),
          ...
        )
      )
    )
  ),
  ...
)
```

### Value normalization in Ledger API responses

A Ledger API value (e.g. `create_arguments` in a `CreatedEvent`) is said to be in normal form if none of its sub-values (itself included) has trailing Nones.

Starting with Daml 3.3.0, values in Ledger API non-verbose responses are subject to normalization. The normalization extends to all sub-values.

**Example**

Assume a package called `example1-1.0.0` which defines a template `T` and a record `Record` in a module called `Main`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
module Main where

data Record = Record { ri : Optional Int, rj : Int, rk : Optional Int }
  deriving (Eq, Show)

template T
  with
    p : Party
    i : Optional Int
    r : Record
    j : Optional Int
  where
    signatory p
```

Also assume a ledger that contains a contract of type `T` written by `example1-1.0.0` where all the optional fields are set to `None`.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val createCmd = ledger_api_utils.create(
  packageIdExample1, 
  "Main",
  "T", 
  Map(
    "p" -> sandbox.adminParty, 
    "i" -> None,
    "r" -> Map("ri" -> None, "rj" -> 1, "rk" -> None),
    "j" -> None))

sandbox.ledger_api.commands.submit(Seq(sandbox.adminParty), Seq(createCmd))
```

Then querying the ledger's active contract set in non-verbose mode returns the following:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ sandbox.ledger_api.acs.of_party(sandbox.adminParty, verbose=false) 
res15: Seq[com.digitalasset.canton.admin.api.client.commands.LedgerApiTypeWrappers.WrappedCreatedEvent] = List(
  WrappedCreatedEvent(
    event = CreatedEvent(
      ... 
      createArguments = Some(
        value = Record(
          recordId = None,
          fields = Vector(
            RecordField(
              label = "",
              value = Some(value = Value(sum = Party(value = "sandbox::122010fdef685011beecd318f03c9d82bf1e2d45950bdb0fceb3497a112ee17f9476")))
            ),
            RecordField(label = "", value = Some(value = Value(sum = Optional(value = Optional(value = None))))),
            RecordField(
              label = "",
              value = Some(
                value = Value(
                  sum = Record(
                    value = Record(
                      recordId = None,
                      fields = Vector(
                        RecordField(label = "", value = Some(value = Value(sum = Optional(value = Optional(value = None))))),
                        RecordField(label = "", value = Some(value = Value(sum = Int64(value = 1L))))
                      )
                    )
                  )
                )
              )
            )
          )
        )
      ),
      ... 
    )
  )
)
```

Note that not only has the third template argument (originally `j`) been omitted from the response, but also the third field of the nested record (originally `rk`). Note also that despite being optional fields of value `None`, the second template argument (originally `i`) and the first nested record field (originally `ri`) are present in the response because they are not in trailing positions.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
