---
title: "Daml Language Reference"
slug: "appdev-reference-daml-language-reference"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-language-reference.md"
source_title: "Daml Language Reference"
tags:
  - appdev
  - reference
  - daml-language-reference
---

# Daml Language Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Daml Language Reference

> Reference for Daml templates, choices, data types, expressions, packages, interfaces, exceptions, and more.

## Overview: Template Structure

This page covers what a template looks like: what parts of a template there are, and where they go.

For the structure of a Daml file *outside* a template, see `file-structure`.

### Template Outline Structure

Here’s the structure of a Daml template:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    exampleParty : Party
    exampleParty2 : Party
    exampleParty3 : Party
    exampleParameter : Text
    -- more parameters here
  where
    signatory exampleParty
    observer exampleParty2
    ensure
      -- boolean condition
      True
    key (exampleParty, exampleParameter) : (Party, Text)
    maintainer (exampleFunction key)
    -- a choice goes here; see next section
```

[template name](#template-name)
`template` keyword

[parameters](#template-parameters)
`with` followed by the names of parameters and their types

template body
`where` keyword

Can include:

[template-local definitions (deprecated)](#template-local-definitions-deprecated)
`let` keyword

Lets you make definitions that have access to the contract arguments and are available in the rest of the template definition.

[signatories](#signatory-parties)
`signatory` keyword

Required. The parties (see the [Party](#built-in-types) type) who must consent to the creation of this contract. You won't be able to create this contract until all of these parties have authorized it.

[observers](#observers)
`observer` keyword

Optional. Parties that aren't signatories but who you still want to be able to see this contract.

[a precondition](#preconditions)
`ensure` keyword

Only create the contract if the conditions after `ensure` evaluate to true.

[a contract key](#contract-keys-and-maintainers)
`key` keyword

Optional. Lets you specify a combination of a party and other data that uniquely identifies a contract of this template. See [Contract Keys and Maintainers](#contract-keys-and-maintainers).

[maintainers](#contract-keys-and-maintainers)
`maintainer` keyword

Required if you have specified a `key`. Keys are only unique to a `maintainer`. See [Contract Keys and Maintainers](#contract-keys-and-maintainers).

[choices](#choices)
`choice NameOfChoice : ReturnType controller nameOfParty do`

Defines choices that can be exercised. See [Choice structure](#choice-structure) for what can go in a choice.

### Choice Structure

Here is the structure of a choice inside a template:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoice
  : () -- replace () with the actual return type
  with
    party : Party -- parameters here
  controller party
  do
    return () -- replace this line with the choice body
```

[consumption annotation](#contract-consumption)
Optionally one of `preconsuming`, `postconsuming`, `nonconsuming`, which changes the behavior of the choice with respect to privacy and if and when the contract is archived. See [contract consumption in choices](#contract-consumption) for more details.

[a name](#choice-name)
Must begin with a capital letter. Must be unique - choices in different templates can't have the same name.

[a return type](#return-type)
after a `:`, the return type of the choice

[choice arguments](#choice-arguments)
`with` keyword

If you include a `Party` as a choice argument, you can make that `Party` the `controller` of the choice. This means that the controller can be specified when the choice is exercised, rather than when the contract is created. For the exercise to work, the party needs to be able to see the contract, i.e. it must be an `observer` or a `signatory`.

[a controller (or controllers)](#controllers)
`controller` keyword

Who can exercise the choice.

[choice observers](#choice-observers)
`observer` keyword

Optional. Additional parties that are guaranteed to be informed of an exercise of the choice.

To specify choice observers, you must start you choice with the `choice` keyword.

The optional `observer` keyword must precede the mandatory `controller` keyword.

[a choice body](#choice-body)
After `do` keyword

What happens when someone exercises the choice. A choice body can contain update statements: see [Choice body structure](#choice-body-structure) below.

### Choice Body Structure

A choice body contains `Update` expressions, wrapped in a [do](#do) block.

The update expressions are:

[create](#create)
Create a new contract of this template.

`create NameOfContract with contractArgument1 = value1; contractArgument2 = value2; ...`

[exercise](#exercise)
Exercise a choice on a particular contract.

`exercise idOfContract NameOfChoiceOnContract with choiceArgument1 = value1; choiceArgument2 = value 2; ...`

[fetch](#fetch)
Fetch a contract using its ID. Often used with assert to check conditions on the contract’s content.

`fetchedContract <- fetch IdOfContract`

[fetchByKey](#fetchbykey)
Like `fetch`, but uses a [contract key](#contract-keys-and-maintainers) rather than an ID.

`fetchedContract <- fetchByKey @ContractType contractKey`

[lookupByKey](#lookupbykey)
Confirm that a contract with the given [contract key](#contract-keys-and-maintainers) exists.

`fetchedContractId <- lookupByKey @ContractType contractKey`

[abort](#abort)
Stop execution of the choice, fail the update.

`if False then abort`

[assert](#assert)
Fail the update unless the condition is true. Usually used to limit the arguments that can be supplied to a contract choice.

`assert (amount > 0)`

[getTime](#gettime)
Gets the ledger time. Usually used to restrict when a choice can be exercised.

`currentTime <- getTime`

[return](#return)
Explicitly return a value. By default, a choice returns the result of its last update expression. This means you only need to use `return` if you want to return something else.

`return ContractID ExampleTemplate`

The choice body can also contain:

[let keyword](#let)
Used to assign values or functions.

assign a value to the result of an update statement
For example: `contractFetched <- fetch someContractId`

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/templates.rst" hash="964a20f1" */}

## Reference: Templates

This page gives reference information on templates:

For the structure of a template, see `structure`.

### Template Name

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
```

* This is the name of the template. It's preceded by `template` keyword. Must begin with a capital letter.
* This is the highest level of nesting.
* The name is used when creating a contract of this template (usually, from within a choice).

### Template Parameters

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
with
  exampleParty : Party
  exampleParty2 : Party
  exampleParty3 : Party
  exampleParam : Text
  -- more parameters here
```

* `with` keyword. The parameters are in the form of a record type.
* Passed in when creating a contract from this template. These are then in scope inside the template body.
* A template parameter can't have the same name as any choice arguments inside the template.
* For all parties involved in the contract (whether they're a `signatory`, `observer`, or `controller`) you must pass them in as parameters to the contract, whether individually or as a list (`[Party]`).

### Implicit Record

Whenever a template is defined, a record is implicitly defined with the same name and fields as that template. This record structure is used in Daml code to represent the data of a contract based on that template.

Note that in the general case, the existence of a local binding `b` of type `T`, where `T` is a template (and thus also a record), does not necessarily imply the existence of a contract with the same data as `b` on the ledger. You can only assume the existence of such a contract if `b` is the result of a fetch from the ledger within the same transaction.

You can create a new instance of a record of type `T` without any interaction with the ledger; in fact, this is how you construct a create command.

### `this` and `self`

Within the body of a template we implicitly define a local binding `this` to represent the data of the current contract. For a template `T`, this binding is of type `T`, i.e. the implicit record defined by the template.

Within choices, you can additionally use the binding `self` to refer to the contract ID of the current contract (the one on which the choice is being executed). For a contract of template `T`, the `self` binding is of type `ContractId T`.

### Template-local Definitions (Deprecated)

<div className="todo">
  Fix or remove this literal include
</div>

* `let` keyword. Starts a block and is followed by any number of definitions, just like any other `let` block.
* Template parameters as well as `this` are in scope, but `self` is not.
* Definitions from the `let` block can be used anywhere else in the template's `where` block.

<Warning>
  Since Daml 2.8.0, template-local definitions are deprecated and their presence will result in the following warning:

  ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
  Template-local binding syntax ("template-let") is deprecated,
  it will be removed in a future version of Daml.
  Instead, use plain top level definitions, taking parameters
  for the contract fields or body ("this") if necessary.
  ```

  The reason for this deprecation is that some uses of the `this` keyword in template-local definitions would create implicit circular dependencies, causing an infinite loop upon evaluation.
</Warning>

#### Migration

Users are strongly encouraged to adapt their code to avoid this feature. This involves replacing each template-local definition with a regular top-level definition. If the old definition made use of contract fields or the contract body ("this"), the new definition should take them as parameters. Correspondingly, the use sites of these definitions should supply the appropriate values as arguments.

For example, consider the template `Person` below. It defines and uses a template-local binding `fullName`, which now triggers the deprecation warning.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Person
  with
    owner : Party
    first : Text
    last : Text
  where
    signatory owner
    let fullName = last <> ", " <> first
    nonconsuming choice GetDescription : ()
      controller owner
      do
        let desc = "An account owned by " <> fullName <> "."
        debug desc
```

To ensure this code keeps working after the feature is removed, `fullName` should be defined as a top-level function, and its use site now passes `this` explicitly.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fullName : Person -> Text
fullName Person {first, last} = last <> ", " <> first
-- takes 'Person' as an explicit parameter and unpacks required fields

template Person
  with
    owner : Party
    first : Text
    last : Text
  where
    signatory owner
    nonconsuming choice GetDescriptionV3 : ()
      controller owner
      do
        -- let bindings in choice bodies are unaffected
        let desc = "An account owned by " <> fullName this <> "."
                                             -- 'this' is passed explicitly
        debug desc
```

#### Turning off the warning

This warning is controlled by the warning flag `template-let`, which means that it can be toggled independently of other warnings. This is especially useful for gradually migrating code that used this syntax.

To turn off the warning within a Daml file, add the following line at the top of the file:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
{-# OPTIONS_GHC -Wno-template-let #-}
```

To turn it off for an entire Daml project, add the following entry to the `build-options` field of the project's `daml.yaml` file

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
build-options:
- --ghc-option=-Wno-template-let
```

Within a project where the warning has been turned off via the `daml.yaml` file, it can be turned back on for individual Daml files by adding the following line at the top of each file:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
{-# OPTIONS_GHC -Wtemplate-let #-}
```

### Signatory Parties

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
signatory exampleParty
```

* `signatory` keyword. After `where`. Followed by at least one `Party`.

* Signatories are the parties (see the `Party` type) who must consent to the creation of this contract. They are the parties who would be put into an *obligable position* when this contract is created.

  Daml won't let you put someone into an obligable position without their consent. So if the contract will cause obligations for a party, they *must* be a signatory. **If they haven't authorized it, you won't be able to create the contract.** In this situation, you may see errors like:

  `NameOfTemplate requires authorizers Party1,Party2,Party, but only Party1 were given.`

* When a signatory consents to the contract creation, this means they also authorize the consequences of choices that can be exercised on this contract.

* The contract is visible to all signatories (as well as the other stakeholders of the contract). That is, the compiler automatically adds signatories as observers.

* Each template **must** have at least one signatory. A signatory declaration consists of the `signatory` keyword followed by a comma-separated list of one or more expressions, each expression denoting a `Party` or collection thereof.

### Observers

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
observer exampleParty2
```

* `observer` keyword. After `where`. Followed by at least one `Party`.
* Observers are additional stakeholders, so the contract is visible to these parties (see the `Party` type).
* Optional. You can have many, either as a comma-separated list or reusing the keyword. You could pass in a list (of type `[Party]`).
* Use when a party needs visibility on a contract, or be informed or contract events, but is not a signatory or controller.
* If you start your choice with `choice` rather than `controller` (see `daml-ref-choices` below), you must make sure to add any potential controller as an observer. Otherwise, they will not be able to exercise the choice, because they won't be able to see the contract.

### Choices

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoice
  : ()  -- replace () with the actual return type
  with
    exampleParameter : Text -- parameters here
  controller exampleParty
  do
    return () -- replace this line with the choice body
```

* A right that the contract gives the controlling party. Can be *exercised*.
* This is essentially where all the logic of the template goes.
* By default, choices are *consuming*: that is, exercising the choice archives the contract, so no further choices can be exercised on it. You can make a choice non-consuming using the `nonconsuming` keyword.
* See `choices` for full reference information.

### Serializable Types

Every parameter to a template, choice argument, and choice result must have a *serializable type*. This does not merely mean "convertible to bytes"; it has a specific meaning in Daml. The serializability rule serves three purposes:

1. Offer a stable means to store ledger values permanently.
2. Provide a sensible encoding of them over the `ledger-api`.
3. Provide sensible *types* that directly match their Daml counterparts in languages like Java for language codegen.

For example, certain kinds of type parameters Daml offers are compatible with (1) and (2), but have no proper counterpart in (3), so they are disallowed. Similarly, function types have sensible Java counterparts, satisfying (3), but no reliable way to store or share them via the API, thus failing (1) and (2).

The following types are *not serializable*, and thus may not be used in templates.

* Function types.
* Record types with any non-serializable field.
* Variant types with any non-serializable value case.
* Variant and enum types with no constructors.
* References to a parameterized data type with any non-serializable type argument. This applies whether or not the data type definition uses the type parameter.
* Defined data types with any type parameter of kind `Nat`, or any kind other than `*`. This means higher-kinded types, and types that take a parameter just to pass to `Numeric`, are not serializable.

#### Migration

Users should remove any agreement declarations from their code, as this feature has been fully removed from the language.

### Preconditions

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ensure
  True -- a boolean condition goes here
```

* `ensure` keyword, followed by a boolean condition.
* Used on contract creation. `ensure` limits the values on parameters that can be passed to the contract: the contract can only be created if the boolean condition is true.

### Contract Keys and Maintainers<span id="daml-ref-contract-keys" />

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
key (exampleParty, exampleParam) : (Party, Text)
maintainer (exampleFunction key)
```

* `key` and `maintainer` keywords.

* This feature lets you specify a "key" that you can use to uniquely identify this contract as an instance of this template.

* If you specify a `key`, you must also specify a `maintainer`. This is a `Party` that will ensure the uniqueness of all the keys it is aware of.

  Because of this, the `key` must include the `maintainer` `Party` or parties (for example, as part of a tuple or record), and the `maintainer` must be a signatory.

* For a full explanation, see `contractkeys`.

### Interface Instances

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance MyInterface for NameOfTemplate where
  view = MyInterfaceViewType "NameOfTemplate" 100
  method1 = field1
  method2 = field2
  method3 False _ _ = 0
  method3 True x y
    | x > 0 = x + y
    | otherwise = y
```

* Used to make a template an instance of an existing interface.
* The clause must start with the keywords `interface instance`, followed by the name of the interface, then the keyword `for` and the name of the template (which must match the enclosing declaration), and finally the keyword `where`, which introduces a block where **all** the methods of the interface must be implemented.
* See `interfaces` for full reference information on interfaces, or section `interface-instances` for interface instances specifically.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/choices.rst" hash="a391ce22" */}

## Reference: Choices

This page gives reference information on choices. For information on the high-level structure of a choice, see `structure`.

### Choice Name

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice ExampleChoice
  : () -- replace () with the actual return type
```

* `choice` keyword
* The name of the choice. Must begin with a capital letter.
* Must be unique in the module. Different templates defined in the same module cannot share a choice name.

### Controllers

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
controller exampleParty
```

* `controller` keyword

* The controller is a comma-separated list of values, where each value is either a party or a collection of parties.

  The conjunction of **all** the parties are required to authorize when this choice is exercised.

<Warning>
  You **must** make sure that the controller parties are observers (or signatories) of the contract, otherwise they cannot see the contract (and therefore cannot exercise the choice).
</Warning>

### Choice Observers

*Choice observers* can be attached to a choice using the `observer` keyword. The choice observers are a list of parties who are not stakeholders but who see all the consequences of the action.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice NameOfChoiceWithObserver
  : () -- replace () with the actual return type
  with
    party : Party -- parameters here
  observer party -- optional specification of choice observers
  controller exampleParty
  do
    return () -- replace this line with the choice body
```

#### Contract Consumption

If no qualifier is present, choices are *consuming*: the contract is archived before the evaluation of the choice body and both the controllers and all contract stakeholders see all consequences of the action.

### Preconsuming Choices

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
preconsuming choice ExamplePreconsumingChoice
  : () -- replace () with the actual return type
```

* `preconsuming` keyword. Optional.
* Makes a choice pre-consuming: the contract is archived before the body of the exercise is executed.
* The create arguments of the contract can still be used in the body of the exercise, but cannot be fetched by its contract id.
* The archival behavior is analogous to the *consuming* default behavior.
* Only the controllers and signatories of the contract see all consequences of the action. Other stakeholders merely see an archive action.
* Can be thought as a non-consuming choice that implicitly archives the contract before anything else happens

### Postconsuming Choices

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
postconsuming choice ExamplePostconsumingChoice
  : () -- replace () with the actual return type
```

* `postconsuming` keyword. Optional.
* Makes a choice post-consuming: the contract is archived after the body of the exercise is executed.
* The create arguments of the contract can still be used in the body of the exercise as well as the contract id for fetching it.
* Only the controllers and signatories of the contract see all consequences of the action. Other stakeholders merely see an archive action.
* Can be thought as a non-consuming choice that implicitly archives the contract after the choice has been exercised

### Non-consuming Choices

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
nonconsuming choice ExampleNonconsumingChoice
  : () -- replace () with the actual return type
```

* `nonconsuming` keyword. Optional.
* Makes a choice non-consuming: that is, exercising the choice does not archive the contract.
* Only the controllers and signatories of the contract see all consequences of the action.
* Useful in the many situations when you want to be able to exercise a choice more than once.

#### Return Type

* Return type is written immediately after choice name.
* All choices have a return type. A contract returning nothing should be marked as returning a "unit", ie `()`.
* If a contract is/contracts are created in the choice body, usually you would return the contract ID(s) (which have the type `ContractId <name of template>`). This is returned when the choice is exercised, and can be used in a variety of ways.

### Choice Arguments

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
with
  exampleParameter : Text
```

* `with` keyword.
* Choice arguments are similar in structure to `daml-ref-template-parameters`: a record type.
* A choice argument can't have the same name as any parameter to the template the choice is in.
* Optional - only if you need extra information passed in to exercise the choice.

### Choice Body

* Introduced with `do`
* The logic in this section is what is executed when the choice gets exercised.
* The choice body contains `Update` expressions. For detail on this, see `updates`.
* By default, the last expression in the choice is returned. You can return multiple updates in tuple form or in a custom data type. To return something that isn't of type `Update`, use the `return` keyword.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/updates.rst" hash="f8b9a0ff" */}

## Reference: Updates

This page gives reference information on Updates. For the structure around them, see `structure`.

### Background

* An `Update` is ledger update. There are many different kinds of these, and they're listed below.
* They are what can go in a choice body.

### Binding Variables

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boundVariable <- UpdateExpression1
```

* One of the things you can do in a choice body is bind (assign) an Update expression to a variable. This works for any of the Updates below.

### do

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
   updateExpression1
   updateExpression2
```

* `do` can be used to group `Update` expressions. You can only have one update expression in a choice, so any choice beyond the very simple will use a `do` block.

* Anything you can put into a choice body, you can put into a `do` block.

* By default, `do` returns whatever is returned by the **last expression in the block**.

  So if you want to return something else, you'll need to use `return` explicitly - see `daml-ref-return` for an example.

### archive

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
archive ContractId
```

* `archive` function.
* Archives a contract already created and residing on the ledger. The contract is fetched by its unique contract identifier `ContractId <name of template>` and then exercises the `Archive` choice on it.
* Returns unit.
* Requires authorization from the contract controllers/signatories. Without the required authorization, the transaction fails. For more detail on authorization, see `daml-ref-signatories`.
* All templates implicitly have an `Archive` choice that cannot be removed, which is equivalent to:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Archive : ()
  controller (signatory this)
  do return ()
```

### create

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
create NameOfTemplate with exampleParameters
```

* `create` function.

* Creates a contract on the ledger. When a contract is committed to the ledger, it is given a unique contract identifier of type `ContractId <name of template>`.

* Creating the contract returns that `ContractId`.

* Use `with` to specify the template parameters.

* Requires authorization from the signatories of the contract being created. This is given by being signatories of the contract from which the other contract is created, being the controller, or explicitly creating the contract itself.

  If the required authorization is not given, the transaction fails. For more detail on authorization, see `daml-ref-signatories`.

### exercise

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise IdOfContract NameOfChoiceOnContract with choiceArgument1 = value1
```

* `exercise` function.
* Exercises the specified choice on the specified contract.
* Use `with` to specify the choice parameters.
* Requires authorization from the controller(s) of the choice. If the authorization is not given, the transaction fails.

### exerciseByKey

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseByKey @ContractType contractKey NameOfChoiceOnContract with choiceArgument1 = value1
```

* `exerciseByKey` function.
* Like `exercise`, but the contract is specified by contract key, instead of contract ID.
* For details see Reference: Contract Keys: exerciseByKey

### fetch

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContract <- fetch IdOfContract
```

* `fetch` function.
* Fetches the contract with that ID. Usually used with a bound variable, as in the example above.
* Often used to check the details of a contract before exercising a choice on that contract. Also used when referring to some reference data.
* `fetch cid` fails if `cid` is not the contract id of an active contract, and thus causes the entire transaction to abort.
* The submitting party must be an observer or signatory on the contract, otherwise `fetch` fails, and similarly causes the entire transaction to abort.

### fetchByKey

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContract <- fetchByKey @ContractType contractKey
```

* `fetchByKey` function.
* Like `fetch`, but fetches the contract with that contract key, instead of the contract ID.
* For details see Reference: Contract Keys: fetchByKey.

### visibleByKey

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isVisible <- visibleByKey @ContractType contractKey
```

* `visibleByKey` function.
* Use this to check whether a contract with the given contract key exists.
* For details see Reference: Contract Keys: visibleByKey

### lookupByKey

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchedContractId <- lookupByKey @ContractType contractKey
```

* `lookupByKey` function.
* Use this to confirm that a contract with the given contract key exists.
* For details see Reference: Contract Keys: lookupByKey

### abort

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
abort errorMessage
```

* `abort` function.
* Fails the transaction - nothing in it will be committed to the ledger.
* `errorMessage` is of type `Text`. Use the error message to provide more context to an external system (e.g., it gets displayed in Daml Studio script results).
* You could use `assert False` as an alternative.

### assert

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assert (condition == True)
```

* `assert` keyword.
* Fails the transaction if the condition is false. So the choice can only be exercised if the boolean expression evaluates to `True`.
* Often used to restrict the arguments that can be supplied to a contract choice.

Here's an example of using `assert` to prevent a choice being exercised if the `Party` passed as a parameter is on a blacklist:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Transfer : ContractId RestrictedPayout
  with newReceiver : Party
  controller receiver
  do
    assert (newReceiver /= blacklisted)
    create RestrictedPayout with receiver = newReceiver; giver; blacklisted; qty
```

### getTime

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
currentTime <- getTime
```

* `getTime` keyword.
* Gets the ledger time. (You will usually want to immediately bind it to a variable in order to be able to access the value.)
* Used to restrict when a choice can be made. For example, with an `assert` that the time is later than a certain time.

Here's an example of a choice that uses a check on the current time:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice Complete : ()
  controller party
  do
    -- bind the ledger effective time to the tchoose variable using getTime
    tchoose <- getTime
    -- assert that tchoose is no earlier than the begin time
    assert (begin <= tchoose && tchoose < addRelTime begin period)
```

### return

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
return ()
```

* `return` keyword.
* Used to return a value from `do` block that is not of type `Update`.

Here's an example where two contracts are created in a choice and both their ids are returned as a tuple:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
  firstContract <- create SomeContractTemplate with arg1; arg2
  secondContract <- create SomeContractTemplate with arg1; arg2
  return (firstContract, secondContract)
```

### let

See the documentation on `daml-ref-let`.

Let looks similar to binding variables, but it's very different! This code example shows how:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
do
  -- defines a function, createdContract, taking a single argument that when
  -- called _will_ create the new contract using argument for issuer and owner
  let createContract x = create NameOfContract with issuer = x; owner = x

  createContract party1
  createContract party2
```

### this

`this` lets you refer to the current contract from within the choice body. This refers to the contract, *not* the contract ID.

It's useful, for example, if you want to pass the current contract to a helper function outside the template.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/data-types.rst" hash="e8514698" */}

## Reference: Data Types

This page gives reference information on Daml's data types.

### Built-in Types

#### Table of built-in primitive types

| Type        | For                                    | Example                           | Notes                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------- | -------------------------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`       | integers                               | `1`, `1000000`, `1_000_000`       | `Int` values are signed 64-bit integers which represent numbers between `-9,223,372,036,854,775,808` and `9,223,372,036,854,775,807` inclusive. Arithmetic operations raise an error on overflows and division by `0`. To make long numbers more readable you can optionally add underscores.                                                                                                       |
| `Decimal`   | short for `Numeric 10`                 | `1.0`                             | `Decimal` values are rational numbers with precision 38 and scale 10.                                                                                                                                                                                                                                                                                                                               |
| `Numeric n` | fixed point decimal numbers            | `1.0`                             | `Numeric n` values are rational numbers with `38` total digits. The scale parameter `n` controls the number of digits after the decimal point, so for example, `Numeric 10` values have 28 digits before the decimal point and 10 digits after it, and `Numeric 20` values have 18 digits before the decimal point and 20 digits after it. The value of `n` must be between `0` and `37` inclusive. |
| `Text`      | strings                                | `"hello"`                         | `Text` values are strings of characters enclosed by double quotes.                                                                                                                                                                                                                                                                                                                                  |
| `Bool`      | boolean values                         | `True`, `False`                   |                                                                                                                                                                                                                                                                                                                                                                                                     |
| `Party`     | unicode string representing a party    | `alice <- getParty "Alice"`       | Every *party* in a Daml system has a unique identifier of type `Party`. To create a value of type `Party`, use binding on the result of calling `getParty`. The party text can only contain alphanumeric characters, `-`, `_` and spaces.                                                                                                                                                           |
| `Date`      | models dates                           | `date 2007 Apr 5`                 | Permissible dates range from `0001-01-01` to `9999-12-31` (using a year-month-day format). To create a value of type `Date`, use the function `date` (to get this function, import `DA.Date`).                                                                                                                                                                                                      |
| `Time`      | models absolute time (UTC)             | `time (date 2007 Apr 5) 14 30 05` | `Time` values have microsecond precision with allowed range from `0001-01-01` to `9999-12-31` (using a year-month-day format). To create a value of type `Time`, use a `Date` and the function `time` (to get this function, import `DA.Time`).                                                                                                                                                     |
| `RelTime`   | models differences between time values | `seconds 1`, `seconds (-2)`       | `RelTime` values have microsecond precision with allowed range from `-9,223,372,036,854,775,808ms` to `9,223,372,036,854,775,807ms` There are no literals for `RelTime`. Instead they are created using one of `days`, `hours`, `minutes`, `seconds`, `milliseconds` and `microseconds` (to get these functions, import `DA.Time`).                                                                 |

#### Escaping Characters

`Text` literals support backslash escapes to include their delimiter (`\"`) and a backslash itself (`\\`).

#### Time

Definition of time on the ledger is a property of the execution environment. Daml assumes there is a shared understanding of what time is among the stakeholders of contracts.

### Lists

`[a]` is the built-in data type for a list of elements of type `a`. The empty list is denoted by `[]` and `[1, 3, 2]` is an example of a list of type `[Int]`.

You can also construct lists using `[]` (the empty list) and `::` (which is an operator that appends an element to the front of a list). For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
twoEquivalentListConstructions =
  script do
    assert ( [1, 2, 3] == 1 :: 2 :: 3 :: [] )
```

#### Sum a List

To sum a list, use a *fold* (because there are no loops in Daml). See `daml-ref-folding` for details.

### Records and Record Types

You declare a new record type using the `data` and `with` keyword:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyRecord = MyRecord
  with
    label1 : type1
    label2 : type2
    ...
    labelN : typeN
  deriving (Eq, Show)
```

where:

* `label1`, `label2`, ..., `labelN` are *labels*, which must be unique in the record type
* `type1`, `type2`, ..., `typeN` are the types of the fields

There's an alternative way to write record types:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyRecord = MyRecord { label1 : type1; label2 : type2; ...; labelN : typeN }
  deriving (Eq, Show)
```

The format using `with` and the format using `{ }` are exactly the same syntactically. The main difference is that when you use `with`, you can use newlines and proper indentation to avoid the delimiting semicolons.

The `deriving (Eq, Show)` ensures the data type can be compared (using `==`) and displayed (using `show`). The line starting `deriving` is required for data types used in fields of a `template`.

In general, add the `deriving` unless the data type contains function types (e.g. `Int -> Int`), which cannot be compared or shown.

For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- This is a record type with two fields, called first and second,
-- both of type `Int`
data MyRecord = MyRecord with first : Int; second : Int
  deriving (Eq, Show)

-- An example value of this type is:
newRecord = MyRecord with first = 1; second = 2

-- You can also write:
newRecord = MyRecord 1 2
```

#### Data Constructors

You can use `data` keyword to define a new data type, for example `data Floor a = Floor a` for some type `a`.

The first `Floor` in the expression is the *type constructor*. The second `Floor` is a *data constructor* that can be used to specify values of the `Floor Int` type: for example, `Floor 0`, `Floor 1`.

In Daml, data constructors may take *at most one argument*.

An example of a data constructor with zero arguments is `data Empty = Empty {}`. The only value of the `Empty` type is `Empty`.

<Note>
  In `data Confusing = Int`, the `Int` is a data constructor with no arguments. It has nothing to do with the built-in `Int` type.
</Note>

#### Access Record Fields

To access the fields of a record type, use dot notation. For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Access the value of the field `first`
val.first

-- Access the value of the field `second`
val.second
```

#### Update Record Fields

You can also use the `with` keyword to create a new record on the basis of an existing replacing select fields.

For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
myRecord = MyRecord with first = 1; second = 2

myRecord2 = myRecord with second = 5
```

produces the new record value `MyRecord with first = 1; second = 5`.

If you have a variable with the same name as the label, Daml lets you use this without assigning it to make things look nicer:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- if you have a variable called `second` equal to 5
second = 5

-- you could construct the same value as before with
myRecord2 = myRecord with second = second

-- or with
myRecord3 = MyRecord with first = 1; second = second

-- but Daml has a nicer way of putting this:
myRecord4 = MyRecord with first = 1; second

-- or even
myRecord5 = r with second
```

<Note>
  The `with` keyword binds more strongly than function application. So for a function, say `return`, either write `return IntegerCoordinate with first = 1; second = 5` or `return (IntegerCoordinate {first = 1; second = 5})`, where the latter expression is enclosed in parentheses.
</Note>

#### Parameterized Data Types

Daml supports parameterized data types.

For example, to express a more general type for 2D coordinates:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Here, a and b are type parameters.
-- The Coordinate after the data keyword is a type constructor.
data Coordinate a b = Coordinate with first : a; second : b
```

An example of a type that can be constructed with `Coordinate` is `Coordinate Int Int`.

### Type Synonyms

To declare a synonym for a type, use the `type` keyword.

For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type IntegerTuple = (Int, Int)
```

This makes `IntegerTuple` and `(Int, Int)` synonyms: they have the same type and can be used interchangeably.

You can use the `type` keyword for any type, including `daml-ref-built-in-types`.

#### Function Types

A function's type includes its parameter and result types. A function `foo` with two parameters has type `ParamType1 -> ParamType2 -> ReturnType`.

Note that this can be treated as any other type. You could for instance give it a synonym using `type FooType = ParamType1 -> ParamType2 -> ReturnType`.

### Algebraic Data Types

An algebraic data type is a composite type: a type formed by a combination of other types. The enumeration data type is an example. This section introduces more powerful algebraic data types.

#### Product Types

The following data constructor is not valid in Daml: `data AlternativeCoordinate a b = AlternativeCoordinate a b`. This is because data constructors can only have one argument.

To get around this, wrap the values in a record: `data Coordinate a b = Coordinate {first: a; second: b}`.

These kinds of types are called *product* types.

A way of thinking about this is that the `Coordinate Int Int` type has a first and second dimension (that is, a 2D product space). By adding an extra type to the record, you get a third dimension, and so on.

#### Sum Types

Sum types capture the notion of being of one kind or another.

An example is the built-in data type `Bool`. This is defined by `data Bool = True | False deriving (Eq,Show)`, where `True` and `False` are data constructors with zero arguments . This means that a `Bool` value is either `True` or `False` and cannot be instantiated with any other value.

Please note that all types which you intend to use as template or choice arguments need to derive at least from `(Eq, Show)`.

A very useful sum type is `data Optional a = None | Some a deriving (Eq,Show)`. It is part of the Daml standard library.

`Optional` captures the concept of a box, which can be empty or contain a value of type `a`.

`Optional` is a sum type constructor taking a type `a` as parameter. It produces the sum type defined by the data constructors `None` and `Some`.

The `Some` data constructor takes one argument, and it expects a value of type `a` as a parameter.

#### Pattern Matching

You can match a value to a specific pattern using the `case` keyword.

The pattern is expressed with data constructors. For example, the `Optional Int` sum type:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Daml.Script
import DA.Assert

optionalIntegerToText (x : Optional Int) : Text =
  case x of
    None -> "Box is empty"
    Some val -> "The content of the box is " <> show val

optionalIntegerToTextTest =
  script do
```

In the `optionalIntegerToText` function, the `case` construct first tries to match the `x` argument against the `None` data constructor, and in case of a match, the `"Box is empty"` text is returned. In case of no match, a match is attempted for `x` against the next pattern in the list, i.e., with the `Some` data constructor. In case of a match, the content of the value attached to the `Some` label is bound to the `val` variable, which is then used in the corresponding output text string.

Note that all patterns in the case construct need to be *complete*, i.e., for each `x` there must be at least one pattern that matches. The patterns are tested from top to bottom, and the expression for the first pattern that matches will be executed. Note that `_` can be used as a catch-all pattern.

You could also case distinguish a `Bool` variable using the `True` and `False` data constructors and achieve the same behavior as an if-then-else expression.

As an example, the following is an expression for a `Text`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}


tmp =
  let
    l = [1, 2, 3]
  in case l of
```

Notice the use of nested pattern matching above.

<Note>
  An underscore was used in place of a variable name. The reason for this is that Daml Studio produces a warning for all variables that are not being used. This is useful in detecting unused variables. You can suppress the warning by naming the variable with an initial underscore.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/expressions.rst" hash="ed2e9625" */}

## Reference: Expressions

This page gives reference information for Daml expressions that are not updates.

### Definitions

Use assignment to bind values or functions at the top level of a Daml file or in a contract template body.

#### Values

For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

-- The TubeSurfaceArea example.

module TubeSurfaceArea where


pi = 3.1415926535

tubeSurfaceArea2 (r : Decimal) (h : Decimal) : Decimal =
  2.0 * pi * r * h

tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h

tubeSurfaceArea3 = \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

The fact that `pi` has type `Decimal` is inferred from the value. To explicitly annotate the type, mention it after a colon following the variable name:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

-- The TubeSurfaceArea example.

module TubeSurfaceArea2 where

-- Type synonym for Decimal -> Decimal -> Decimal
type BinaryDecimalFunction = Decimal -> Decimal -> Decimal

pi : Decimal = 3.1415926535

tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

#### Functions

You can define functions. Here's an example: a function for computing the surface area of a tube:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h
```

Here you see:

* the name of the function

* the function's type signature `Decimal -> Decimal -> Decimal`

  This means it takes two Decimals and returns another Decimal.

* the definition `= 2.0 * pi * r * h` (which uses the previously defined `pi`)

### Arithmetic Operators

| Operator                          | Works for                   |
| --------------------------------- | --------------------------- |
| `+`                               | `Int`, `Decimal`, `RelTime` |
| `-`                               | `Int`, `Decimal`, `RelTime` |
| `*`                               | `Int`, `Decimal`            |
| `/` (integer division)            | `Int`                       |
| `%` (integer remainder operation) | `Int`                       |
| `^` (integer exponentiation)      | `Int`                       |

The result of the modulo operation has the same sign as the dividend:

* `7 / 3` and `(-7) / (-3)` evaluate to `2`
* `(-7) / 3` and `7 / (-3)` evaluate to `-2`
* `7 % 3` and `7 % (-3)` evaluate to `1`
* `(-7) % 3` and `(-7) % (-3)` evaluate to `-1`

To write infix expressions in prefix form, wrap the operators in parentheses. For example, `(+) 1 2` is another way of writing `1 + 2`.

### Comparison Operators

| Operator             | Works for                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `<`, `<=`, `>`, `>=` | `Bool`, `Text`, `Int`, `Decimal`, `Party`, `Time`                                                                        |
| `==`, `/=`           | `Bool`, `Text`, `Int`, `Decimal`, `Party`, `Time`, and identifiers of contracts stemming from the same contract template |

### Logical Operators

The logical operators in Daml are:

* `not` for negation, e.g., `not True == False`
* `&&` for conjunction, where `a && b == and a b`
* `||` for disjunction, where `a || b == or a b`

for `Bool` variables `a` and `b`.

### If-then-else

You can use conditional *if-then-else* expressions, for example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
if owner == scroogeMcDuck then "sell" else "buy"
```

### Let

To bind values or functions to be in scope beneath the expression, use the block keyword `let`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
doubled =
  -- let binds values or functions to be in scope beneath the expression
  let
    double (x : Int) = 2 * x
    up = 5
  in double up
```

You can also use `let` inside `do` blocks:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
blah = script
  do
    let
      x = 1
      y = 2
      -- x and y are in scope for all subsequent expressions of the do block,
      -- so can be used in expression1 and expression2.
    expression1
    expression2
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/functions.rst" hash="2a0983ac" */}

## Reference: Functions

This page gives reference information on functions in Daml.

Daml is a functional language. It lets you apply functions partially and also have functions that take other functions as arguments. This page discusses these *higher-order functions*.

### Defining Functions

In `expressions`, the `tubeSurfaceArea` function was defined as:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : Decimal -> Decimal -> Decimal 
tubeSurfaceArea r h  =
  2.0 * pi * r * h
```

You can define this function equivalently using lambdas, involving `\`, a sequence of parameters, and an arrow `->` as:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

### Partial Application

The type of the `tubeSurfaceArea` function described previously, is `Decimal -> Decimal -> Decimal`. An equivalent, but more instructive, way to read its type is: `Decimal -> (Decimal -> Decimal)`: saying that `tubeSurfaceArea` is a function that takes *one* argument and returns another function.

So `tubeSurfaceArea` expects one argument of type `Decimal` and returns a function of type `Decimal -> Decimal`. In other words, this function returns another function. *Only the last application of an argument yields a non-function.*

This is called *currying*: currying is the process of converting a function of multiple arguments to a function that takes just a single argument and returns another function. In Daml, all functions are curried.

This doesn't affect things that much. If you use functions in the classical way (by applying them to all parameters) then there is no difference.

If you only apply a few arguments to the function, this is called *partial application*. The result is a function with partially defined arguments. For example:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
multiplyThreeNumbers : Int -> Int -> Int -> Int
multiplyThreeNumbers xx yy zz =
  xx * yy * zz

multiplyTwoNumbersWith7 = multiplyThreeNumbers 7

multiplyWith21 = multiplyTwoNumbersWith7 3

multiplyWith18 = multiplyThreeNumbers 3 6
```

You could also define equivalent lambda functions:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
multiplyWith18_v2 : Int -> Int
multiplyWith18_v2 xx =
  multiplyThreeNumbers 3 6 xx
```

### Functions are Values

The function type can be explicitly added to the `tubeSurfaceArea` function (when it is written with the lambda notation):

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Type synonym for Decimal -> Decimal -> Decimal
type BinaryDecimalFunction = Decimal -> Decimal -> Decimal

pi : Decimal = 3.1415926535

tubeSurfaceArea : BinaryDecimalFunction =
  \ (r : Decimal) (h : Decimal) -> 2.0 * pi * r * h
```

Note that `tubeSurfaceArea : BinaryDecimalFunction = ...` follows the same pattern as when binding values, e.g., `pi : Decimal = 3.14159265359`.

Functions have types, just like values. Which means they can be used just like normal variables. In fact, in Daml, functions are values.

This means a function can take another function as an argument. For example, define a function `applyFilter: (Int -> Int -> Bool) -> Int -> Int -> Bool` which applies the first argument, a higher-order function, to the second and the third arguments to yield the result.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
applyFilter (filter : Int -> Int -> Bool)
    (x : Int)
    (y : Int) = filter x y

compute = script do
    applyFilter (<) 3 2 === False
    applyFilter (/=) 3 2 === True

    round (2.5 : Decimal) === 3
    round (3.5 : Decimal) === 4

    explode "me" === ["m", "e"]

    applyFilter (\a b -> a /= b) 3 2 === True
```

The `daml-ref-folding` section looks into two useful built-in functions, `foldl` and `foldr`, that also take a function as an argument.

<Note>
  Daml does not allow functions as parameters of contract templates and contract choices. However, a follow up of a choice can use built-in functions, defined at the top level or in the contract template body.
</Note>

### Generic Functions

A function is *parametrically polymorphic* if it behaves uniformly for all types, in at least one of its type parameters. For example, you can define function composition as follows:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
compose (f : b -> c) (g : a -> b) (x : a) : c = f (g x)
```

where `a`, `b`, and `c` are any data types. Both `compose ((+) 4) ((*) 2) 3 == 10` and `compose not ((&&) True) False` evaluate to `True`. Note that `((+) 4)` has type `Int -> Int`, whereas `not` has type `Bool -> Bool`.

You can find many other generic functions including this one in the Daml standard library.

<Note>
  Daml currently does not support generic functions for a specific set of types, such as `Int` and `Decimal` numbers. For example, `sum (x: a) (y: a) = x + y` is undefined when `a` equals the type `Party`. *Bounded polymorphism* might be added to Daml in a later version.
</Note>

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/file-structure.rst" hash="4bb0b27c" */}

## Reference: Daml File Structure

This page gives reference information on the structure of Daml files outside of templates.

### File Structure

* This file's module name (`module NameOfThisFile where`).

  Part of a hierarchical module system to facilitate code reuse. Must be the same as the Daml file name, without the file extension.

  For a file with path `./Scenarios/Demo.daml`, use `module Scenarios.Demo where`.

### Imports

* You can import other modules (`import OtherModuleName`), including qualified imports (`import qualified AndYetOtherModuleName`, `import qualified AndYetOtherModuleName as Signifier`). Can't have circular import references.
* To import the `Prelude` module of `./Prelude.daml`, use `import Prelude`.
* To import a module of `./Scenarios/Demo.daml`, use `import Scenarios.Demo`.
* If you leave out `qualified`, and a module alias is specified, top-level declarations of the imported module are imported into the module's namespace as well as the namespace specified by the given alias.

### Libraries

A Daml library is a collection of related Daml modules.

Define a Daml library using a `LibraryModules.daml` file: a normal Daml file that imports the root modules of the library. The library consists of the `LibraryModules.daml` file and all its dependencies, found by recursively following the imports of each module.

Errors are reported in Daml Studio on a per-library basis. This means that breaking changes on shared Daml modules are displayed even when the files are not explicitly open.

### Comments

Use `--` for a single line comment. Use `{-` and `-}` for a comment extending over multiple lines.

### Contract Identifiers

When an instance of a template (that is, a contract) is added to the ledger, it's assigned a unique identifier, of type `ContractId <name of template>`.

The runtime representation of these identifiers depends on the execution environment: a contract identifier from the Sandbox may look different to ones on other Daml Ledgers.

You can use `==` and `/=` on contract identifiers of the same type.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/packages.rst" hash="4011d059" */}

## Reference: Daml Packages

This page gives reference information on Daml package dependencies.

### Building Daml Archives

When a Daml project is compiled, the compiler produces a `Daml archive`. These are platform-independent packages of compiled Daml code that can be uploaded to a Daml ledger or imported in other Daml projects.

Daml archives have a `.dar` file ending. By default, when you run `dpm build`, it will generate the `.dar` file in the `.daml/dist` folder in the project root folder. For example, running `dpm build` in project `foo` with project version `0.0.1` will result in a Daml archive `.daml/dist/foo-0.0.1.dar`.

You can specify a different path for the Daml archive by using the `-o` flag:

```sh theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build -o foo.dar

The rest of this page will focus on how to import a Daml package in other Daml projects.
```

### Inspecting DARs

Refer to the section on decoding DARs and DALF files.

### Import Daml Packages

There are two ways to import a Daml package in a project: via `dependencies`, and via `data-dependencies`. They each have certain advantages and disadvantages. To summarize:

* `dependencies` allow you to import a Daml archive as a library. The definitions in the dependency will all be made available to the importing project. However, the dependency must be compiled with the same SDK version, so this method is only suitable for breaking up large projects into smaller projects that depend on each other, or to reuse existing libraries.
* `data-dependencies` allow you to import a Daml archive (.dar) or a Daml-LF package (.dalf), including packages that have already been deployed to a ledger. These packages can be compiled with any previous SDK version. On the other hand, not all definitions can be carried over perfectly, since the Daml interface needs to be reconstructed from the binary.

The following sections will cover these two approaches in more depth.

#### Import a Daml package via Dependencies

A Daml project can declare a Daml archive as a dependency in the `dependencies` field of `daml.yaml`. This lets you import modules and reuse definitions from another Daml project. The main limitation of this method is that the dependency must be built for the same SDK version as the importing project.

Let's go through an example. Suppose you have an existing Daml project `foo`, located at `/home/user/foo`, and you want to use it as a dependency in a project `bar`, located at `/home/user/bar`.

To do so, you first need to generate the Daml archive of `foo`. Go into `/home/user/foo` and run `dpm build -o foo.dar`. This will create the Daml archive, `/home/user/foo/foo.dar`.

Next, we will update the project config for `bar` to use the generated Daml archive as a dependency. Go into `/home/user/bar` and change the `dependencies` field in `daml.yaml` to point to the created \`Daml archive\`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
  - daml-prim
  - daml-stdlib
  - ../foo/foo.dar
```

The import path can also be absolute, for example, by changing the last line to:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
- /home/user/foo/foo.dar
```

When you run `dpm build` in the `bar` project, the compiler will make the definitions in `foo.dar` available for importing. For example, if `foo` exports the module `Foo`, you can import it in the usual way:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import Foo
```

By default, all modules of `foo` are made available when importing `foo` as a dependency. To limit which modules of `foo` get exported, you may add an `exposed-modules` field in the `daml.yaml` file for `foo`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
exposed-modules:
- Foo
```

#### Import a Daml Archive via `data-dependencies`

You can import a Daml archive (.dar) or Daml-LF package (.dalf) using `data-dependencies`. Unlike `dependencies`, this can be used when the SDK versions do not match.

For example, you can import `foo.dar` as follows:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- ../foo/foo.dar
```

When importing packages this way, the Daml compiler will try to reconstruct the original Daml interface from the compiled binaries. However, to allow `data-dependencies` to work across SDK versions, the compiler has to abstract over some details which are not compatible across SDK versions. This means that there are some Daml features that cannot be recovered when using `data-dependencies`. In particular:

1. Export lists cannot be recovered, so imports via `data-dependencies` can access definitions that were originally hidden. This means it is up to the importing module to respect the data abstraction of the original module. Note that this is the same for all code that runs on the ledger, since the ledger does not provide special support for data abstraction.
2. If you have a `dependency` that limits the modules that can be accessed via `exposed-modules`, you can get an error if you also have a `data-dependency` that references something from the hidden modules (even if it is only reexported). Since `exposed-modules` are not available on the ledger in general, we recommend to not make use of them and instead rely on naming conventions (e.g., suffix module names with `.Internal`) to make it clear which modules are part of the public API.
3. Prior to Daml-LF version 1.8, typeclasses could not be reconstructed. This means if you have a package that is compiled with an older version of Daml-LF, typeclasses and typeclass instances will not be carried over via data-dependencies, and you won't be able to call functions that rely on typeclass instances. This includes the template functions, such as `create`, `signatory`, and `exercise`, as these rely on typeclass instances.
4. Starting from Daml-LF version 1.8, when possible, typeclass instances will be reconstructed by re-using the typeclass definitions from dependencies, such as the typeclasses exported in `daml-stdlib`. However, if the typeclass signature has changed, you will get an instance for a reconstructed typeclass instead, which will not interoperate with code from dependencies.

#### Transitive dependency management

The Daml compiler identifies each DAR dependency in the project by its `packageId` and fully qualified name (Daml project package name and version number).

If you have a Daml project which contains multiple common transitive DAR dependencies, those common transitive dependencies must either:

* Have identical contents if they have the same name and version specified in their Daml project's `daml.yaml` file, or
* Have a different value for the `version` entry in their respective `daml.yaml` files.

Otherwise, the Daml project cannot be built into a deployable DAR due to package identification conflicts.

For example:

* Daml project X (top-level) has dependencies `DarA` and `DarB`.
* `DarA` and `DarB` both contain DAR dependency `DarC`

When compiling Daml project X, you must ensure that the `DarC` dependency referenced by both `DarA` and `DarB` either has identical Daml contents or has a different version number if the contents differ. The version number is defined in the daml.yaml file of the Daml project producing `DarC`, under the `version` key.

#### Reference Daml Packages Already On the Ledger

Daml packages that have been uploaded to a ledger can be imported as data dependencies, given you have the necessary permissions to download these packages. To import such a package, add the package name and version separated by a colon to the data-dependencies stanza as follows:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
ledger:
  host: localhost
  port: 6865
dependencies:
- daml-prim
- daml-stdlib
data-dependencies:
- foo:1.0.0
```

If your ledger runs at the default host and port (`localhost:6865`), the ledger stanza can be omitted. This will fetch and install the package `foo-1.0.0`. A `daml.lock` file is created at the root of your project directory, pinning the resolved packages to their exact package ID:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
dependencies:
- pkgId: 51255efad65a1751bcee749d962a135a65d12b87eb81ac961142196d8bbca535
  name: foo
  version: 1.0.0
```

The `daml.lock` file needs to be checked into version control of your project. This assures that package name/version tuples specified in your data dependencies are always resolved to the same package ID. To recreate or update your `daml.lock` file, delete it and run `dpm build` again.

### Handling Module Name Collisions

Sometimes you will have multiple packages with the same module name. In that case, a simple import will fail, since the compiler doesn't know which version of the module to load. Fortunately, there are a few tools you can use to approach this problem.

The first is to use package qualified imports. Supposing you have packages with different names, `foo` and `bar`, which both expose a module `X`, you can select which one you want with a package qualified import.

To get `X` from `foo`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "foo" X
```

To get `X` from `bar`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "bar" X
```

To get both, you need to rename the module as you perform the import:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import "foo" X as FooX
import "bar" X as BarX
```

Sometimes, package qualified imports will not help, because you are importing two packages with the same name. For example, if you're loading different versions of the same package. To handle this case, you need the `--package` build option.

Suppose you are importing packages `foo-1.0.0` and `foo-2.0.0`. Notice they have the same name `foo` but different versions. To get modules that are exposed in both packages, you will need to provide module aliases. You can do this by passing the `--package` build option. Open `daml.yaml` and add the following `build-options`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
build-options:
- '--package'
- 'foo-1.0.0 with (X as Foo1.X)'
- '--package'
- 'foo-2.0.0 with (X as Foo2.X)'
```

This will alias the `X` in `foo-1.0.0` as `Foo1.X`, and alias the `X` in `foo-2.0.0` as `Foo2.X`. Now you will be able to import both `X` by using the new names:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
import qualified Foo1.X
import qualified Foo2.X
```

It is also possible to add a prefix to all modules in a package using the `module-prefixes` field in your `daml.yaml`. This is particularly useful for upgrades where you can map all modules of version `v` of your package under `V$v`. For the example above you can use the following:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
module-prefixes:
  foo-1.0.0: Foo1
  foo-2.0.0: Foo2
```

That will allow you to import module `X` from package `foo-1.0.0` as `Foo1.X` and `X` from package `foo-2.0.0` as `Foo2`.

You can also use more complex module prefixes, e.g., `foo-1.0.0: Foo1.Bar` which will make module `X` available under `Foo1.Bar.X`.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/contract-keys.rst" hash="85971992" */}

## Reference: Contract Keys

<Warning>
  Contract keys coming in the Canton 3.5 release. This documentation will be updated at that time.
</Warning>

### Unsupported feature

Contract keys are an optional addition to templates. They let you specify a way of uniquely identifying contracts, using the parameters to the template - similar to a primary key for a database.

Contract keys do not change and can be used to refer to a contract even when the contract id changes.

Here's an example of setting up a contract key for a bank account, to act as a bank account ID:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
type AccountKey = (Party, Text)

template Account with
    bank : Party
    number : Text
    owner : Party
    balance : Decimal
    observers : [Party]
  where
    signatory [bank, owner]
    observer observers

    key (bank, number) : AccountKey
    maintainer key._1
```

### What Can Be a Contract Key

The key can be an arbitrary serializable expression that does **not** contain contract IDs. However, it **must** include every party that you want to use as a `maintainer` (see [Specify Maintainers](#specify-maintainers) below).

It's best to use simple types for your keys like `Text` or `Int`, rather than a list or more complex type.

### Specify Maintainers

If you specify a contract key for a template, you must also specify a `maintainer` or maintainers, in a similar way to specifying signatories or observers. The maintainers "own" the key in the same way the signatories "own" a contract. Just like signatories of contracts prevent double spends or use of false contract data, maintainers of keys prevent double allocation or incorrect lookups. Since the key is part of the contract, the maintainers **must** be signatories of the contract. However, maintainers are computed from the `key` instead of the template arguments. In the example above, the `bank` is ultimately the maintainer of the key.

Uniqueness of keys is guaranteed per template. Since multiple templates may use the same key type, some key-related functions must be annotated using the `@ContractType` as shown in the examples below.

When you are writing Daml models, the maintainers matter since they affect authorization -- much like signatories and observers. You don't need to do anything to "maintain" the keys. In the above example, it is guaranteed that there can only be one `Account` with a given `number` at a given `bank`.

Checking of the keys is done automatically at execution time, by the Daml execution engine: if someone tries to create a new contract that duplicates an existing contract key, the execution engine will cause that creation to fail.

### Contract Lookups

The primary purpose of contract keys is to provide a stable, and possibly meaningful, identifier that can be used in Daml to fetch contracts. There are two functions to perform such lookups: `fetchbykey` and `lookupbykey`. Both types of lookup are performed at interpretation time on the submitting Participant Node, on a best-effort basis. Currently, that best-effort means lookups only return contracts if the submitting Party is a stakeholder of that contract.

In particular, the above means that if multiple commands are submitted simultaneously, all using contract lookups to find and consume a given contract, there will be contention between these commands, and at most one will succeed. For more information, see the section on Avoiding [Contention]().

Limiting key usage to stakeholders also means that keys cannot be used to access a divulged contract, i.e. there can be cases where `fetch` succeeds and `fetchByKey` does not. See the example at the end of this section for details.

#### fetchByKey

`(fetchedContractId, fetchedContract) <- fetchByKey @ContractType contractKey`

Use `fetchByKey` to fetch the ID and data of the contract with the specified key. It is an alternative to `fetch` and behaves the same in most ways.

It returns a tuple of the ID and the contract object (containing all its data).

Like `fetch`, `fetchByKey` needs to be authorized by at least one stakeholder.

`fetchByKey` fails and aborts the transaction if:

* The submitting Party is not a stakeholder on a contract with the given key, or
* A contract was found, but the `fetchByKey` violates the authorization rule, meaning no stakeholder authorized the `fetch`.

This means that if it fails, it doesn't guarantee that a contract with that key doesn't exist, just that the submitting Party doesn't know about it, or there are issues with authorization.

#### visibleByKey

`boolean <- visibleByKey @ContractType contractKey`

Use `visibleByKey` to check whether you can see an active contract for the given key with the current authorizations. If the contract exists and you have permission to see it, returns `True`, otherwise returns `False`.

To clarify, ignoring contention:

1. `visibleByKey` will return `True` if all of these are true: there exists a contract for the given key, the submitter is a stakeholder on that contract, and at the point of call we have the authorization of **all** of the maintainers of the key.
2. `visibleByKey` will return `False` if all of those are true: there is no contract for the given key, and at the point of call we have authorization from **all** the maintainers of the key.
3. `visibleByKey` will abort the transaction at interpretation time if, at the point of call, we are missing the authorization from any one maintainer of the key.
4. `visibleByKey` will fail at validation time (after returning `False` at interpretation time) if all of these are true: at the point of call, we have the authorization of **all** the maintainers, and a valid contract exists for the given key, but the submitter is not a stakeholder on that contract.

While it may at first seem too restrictive to require **all** maintainers to authorize the call, this is actually required in order to validate negative lookups. In the positive case, when you can see the contract, it's easy for the transaction to mention which contract it found, and therefore for validators to check that this contract does indeed exist, and is active as of the time of executing the transaction.

For the negative case, however, the transaction submitted for execution cannot say *which* contract it has not found (as, by definition, it has not found it, and it may not even exist). Still, validators have to be able to reproduce the result of not finding the contract, and therefore they need to be able to look for it, which means having the authorization to ask the maintainers about it.

#### lookupByKey

`optionalContractId <- lookupByKey @ContractType contractKey`

Use `lookupByKey` to check whether a contract with the specified key exists. If it does exist, `lookupByKey` returns the `Some contractId`, where `contractId` is the ID of the contract; otherwise, it returns `None`.

`lookupByKey` is conceptually equivalent to

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookupByKey : forall c k. (HasFetchByKey c k) => k -> Update (Optional (ContractId c))
lookupByKey k = do
  visible <- visibleByKey @c k
  if visible then do
    (contractId, _ignoredContract) <- fetchByKey @c k
    return $ Some contractId
  else
    return None
```

Therefore, `lookupByKey` needs all the same authorizations as `visibleByKey`, for the same reasons, and fails in the same cases.

To get the data from the contract once you've confirmed it exists, you'll still need to use `fetch`.

### exerciseByKey

`exerciseByKey @ContractType contractKey`

Use `exerciseByKey` to exercise a choice on a contract identified by its `key` (compared to `exercise`, which lets you exercise a contract identified by its `ContractId`). Just like `exercise`, running `exerciseByKey` requires visibility of the contract (either through divulgence, `readAs` or being a stakeholder) and authorization from the controllers of the choice.

### Example

A complete example of possible success and failure scenarios of `fetchByKey` and `lookupByKey` is shown below.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
-- SPDX-License-Identifier: Apache-2.0

module Keys where

import Daml.Script
import DA.Assert
import DA.Optional

template Keyed
  with
    sig : Party
    obs : Party
  where
    signatory sig
    observer obs

    key sig : Party
    maintainer key

template Divulger
  with
    divulgee : Party
    sig : Party
  where
    signatory divulgee
    observer sig

    nonconsuming choice DivulgeKeyed
      : Keyed
      with
        keyedCid : ContractId Keyed
      controller sig
      do
        fetch keyedCid

template Delegation
  with
    sig : Party
    delegees : [Party]
  where
    signatory sig
    observer delegees

    nonconsuming choice CreateKeyed
      : ContractId Keyed
      with
        delegee : Party
        obs : Party
      controller delegee
      do
        create Keyed with sig; obs

    nonconsuming choice ArchiveKeyed
      : ()
      with
        delegee : Party
        keyedCid : ContractId Keyed
      controller delegee
      do
        archive keyedCid

    nonconsuming choice UnkeyedFetch
      : Keyed
      with
        cid : ContractId Keyed
        delegee : Party
      controller delegee
      do
        fetch cid

    nonconsuming choice VisibleKeyed
      : Bool
      with
        key : Party
        delegee : Party
      controller delegee
      do
        visibleByKey @Keyed key

    nonconsuming choice LookupKeyed
      : Optional (ContractId Keyed)
      with
        lookupKey : Party
        delegee : Party
      controller delegee
      do
        lookupByKey @Keyed lookupKey

    nonconsuming choice FetchKeyed
      : (ContractId Keyed, Keyed)
      with
        lookupKey : Party
        delegee : Party
      controller delegee
      do
        fetchByKey @Keyed lookupKey

template Helper
  with
    p : Party
  where
    signatory p

    choice FetchByKey : (ContractId Keyed, Keyed)
      with
        keyedKey : Party
      controller p
      do fetchByKey @Keyed keyedKey

    choice VisibleByKey : Bool
      with
        keyedKey : Party
      controller p
      do visibleByKey @Keyed keyedKey

    choice LookupByKey : (Optional (ContractId Keyed))
      with
        keyedKey : Party
      controller p
      do lookupByKey @Keyed keyedKey

    choice AssertNotVisibleKeyed : ()
      with
        delegationCid : ContractId Delegation
        delegee : Party
        key : Party
      controller p
      do
        b <- exercise delegationCid VisibleKeyed with
          delegee
          key
        assert $ not b

    choice AssertLookupKeyedIsNone : ()
      with
        delegationCid : ContractId Delegation
        delegee : Party
        lookupKey : Party
      controller p
      do
        b <- exercise delegationCid LookupKeyed with
          delegee
          lookupKey
        assert $ isNone b

    choice AssertFetchKeyedEqExpected : ()
      with
        delegationCid : ContractId Delegation
        delegee : Party
        lookupKey : Party
        expectedCid : ContractId Keyed
      controller p
      do
        (cid, keyed) <- exercise delegationCid FetchKeyed with
          delegee
          lookupKey
        cid === expectedCid


lookupTest = script do

  -- Put four parties in the four possible relationships with a `Keyed`
  sig <- allocateParty "s" -- Signatory
  obs <- allocateParty "o" -- Observer
  divulgee <- allocateParty "d" -- Divulgee
  blind <- allocateParty "b" -- Blind

  keyedCid <- submit sig do createCmd Keyed with ..
  divulgercid <- submit divulgee do createCmd Divulger with ..
  submit sig do exerciseCmd divulgercid DivulgeKeyed with ..

  -- Now the signatory and observer delegate their choices
  sigDelegationCid <- submit sig do
    createCmd Delegation with
      sig
      delegees = [obs, divulgee, blind]
  obsDelegationCid <- submit obs do
    createCmd Delegation with
      sig = obs
      delegees = [divulgee, blind]

  -- TESTING LOOKUPS AND FETCHES

  -- Maintainer can fetch
  (cid, keyed) <- submit sig do
    Helper sig `createAndExerciseCmd` FetchByKey sig
  cid === keyedCid
  -- Maintainer can see
  b <- submit sig do
    Helper sig `createAndExerciseCmd` VisibleByKey sig
  assert b
  -- Maintainer can lookup
  mcid <- submit sig do
    Helper sig `createAndExerciseCmd` LookupByKey sig
  mcid === Some keyedCid


  -- Stakeholder can fetch
  (cid, l) <- submit obs do
    Helper obs `createAndExerciseCmd` FetchByKey sig
  keyedCid === cid
  -- Stakeholder can't see without authorization
  submitMustFail obs do
    Helper obs `createAndExerciseCmd` VisibleByKey sig

  -- Stakeholder can see with authorization
  b <- submit obs do
    exerciseCmd sigDelegationCid VisibleKeyed with
      delegee = obs
      key = sig
  assert b
  -- Stakeholder can't lookup without authorization
  submitMustFail obs do
    Helper obs `createAndExerciseCmd` LookupByKey sig
  -- Stakeholder can lookup with authorization
  mcid <- submit obs do
    exerciseCmd sigDelegationCid LookupKeyed with
      delegee = obs
      lookupKey = sig
  mcid === Some keyedCid

  -- Divulgee can't fetch the contract directly
  submitMustFail divulgee do
    exerciseCmd obsDelegationCid UnkeyedFetch with
        delegee = divulgee
        cid = keyedCid
  -- Divulgee can't fetch through the key
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` FetchByKey sig
  -- Divulgee can't see
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` VisibleByKey sig
  -- Divulgee can't see with stakeholder authority
  submitMustFail divulgee do
    exerciseCmd obsDelegationCid VisibleKeyed with
        delegee = divulgee
        key = sig
  -- Divulgee can't lookup
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` LookupByKey sig
  -- Divulgee can't lookup with stakeholder authority
  submitMustFail divulgee do
    exerciseCmd obsDelegationCid LookupKeyed with
        delegee = divulgee
        lookupKey = sig
  -- Divulgee can't do positive lookup with maintainer authority.
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegationCid = sigDelegationCid
      delegee = divulgee
      key = sig
  -- Divulgee can't do positive lookup with maintainer authority.
  -- Note that the lookup returns `None` so the assertion passes.
  -- If the assertion is changed to `isSome`, the assertion fails,
  -- which means the error message changes. The reason is that the
  -- assertion is checked at interpretation time, before the lookup
  -- is checked at validation time.
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` AssertLookupKeyedIsNone with
      delegationCid = sigDelegationCid
      delegee = divulgee
      lookupKey = sig
  -- Divulgee can't fetch with stakeholder authority
  submitMustFail divulgee do
    Helper divulgee `createAndExerciseCmd` AssertFetchKeyedEqExpected with
      delegationCid = obsDelegationCid
      delegee = divulgee
      lookupKey = sig
      expectedCid = keyedCid

  -- Blind party can't fetch
  submitMustFail blind do
    Helper blind `createAndExerciseCmd` FetchByKey sig
  -- Blind party can't see
  submitMustFail blind do
    Helper blind `createAndExerciseCmd` VisibleByKey sig
  -- Blind party can't see with stakeholder authority
  submitMustFail blind do
    exerciseCmd obsDelegationCid VisibleKeyed with
      delegee = blind
      key = sig
  -- Blind party can't see with maintainer authority
  submitMustFail blind do
    Helper blind `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegationCid = sigDelegationCid
      delegee = blind
      key = sig
  -- Blind party can't lookup
  submitMustFail blind do
    Helper blind `createAndExerciseCmd` LookupByKey sig
  -- Blind party can't lookup with stakeholder authority
  submitMustFail blind do
    exerciseCmd obsDelegationCid LookupKeyed with
      delegee = blind
      lookupKey = sig
  -- Blind party can't lookup with maintainer authority.
  -- The lookup initially returns `None`, but is rejected at
  -- validation time
  submitMustFail blind do
    Helper blind `createAndExerciseCmd` AssertLookupKeyedIsNone with
      delegationCid = sigDelegationCid
      delegee = blind
      lookupKey = sig
  -- Blind party can't fetch with stakeholder authority as lookup is negative
  submitMustFail blind do
    exerciseCmd obsDelegationCid FetchKeyed with
      delegee = blind
      lookupKey = sig
  -- Blind party can see nonexistence of a contract
  submit blind do
    Helper blind `createAndExerciseCmd` AssertNotVisibleKeyed with
      delegationCid = obsDelegationCid
      delegee = blind
      key = obs
  -- Blind can do a negative lookup on a truly nonexistant contract
  submit blind do
    Helper blind `createAndExerciseCmd` AssertLookupKeyedIsNone with
      delegationCid = obsDelegationCid
      delegee = blind
      lookupKey = obs

  -- TESTING CREATES AND ARCHIVES

  -- Divulgee can't archive
  submitMustFail divulgee do
    exerciseCmd sigDelegationCid ArchiveKeyed with
      delegee = divulgee
      keyedCid

  submit sig do
     exerciseCmd keyedCid Archive

  -- Divulgee can create
  keyedCid2 <- submit divulgee do
    exerciseCmd sigDelegationCid CreateKeyed with
      delegee = divulgee
      obs

  -- Stakeholder can archive
  submit obs do
    exerciseCmd sigDelegationCid ArchiveKeyed with
      delegee = obs
      keyedCid = keyedCid2
  -- Stakeholder can create
  keyedCid3 <- submit obs do
    exerciseCmd sigDelegationCid CreateKeyed with
      delegee = obs
      obs

  return ()
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/interfaces.rst" hash="fdeb13bb" */}

## Reference: Interfaces

In Daml, an interface defines an abstract type together with a behavior specified by its view type, method signatures, and choices. For a template to conform to this interface, there must be a corresponding `interface instance` definition where all the methods of the interface (including the special `view` method) are implemented. This allows decoupling such behavior from its implementation, so other developers can write applications in terms of the interface instead of the concrete template.

### Configuration

To use this feature your Daml project must target Daml-LF version `1.15` or higher, which is the current default.

If using Canton, the protocol version of the sync domain should be `4` or higher, see Canton protocol version for more details.

### Interface Declaration

An interface declaration is somewhat similar to a template declaration.

#### Interface Name

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface MyInterface where
```

* This is the name of the interface.
* It's preceded by the keyword `interface` and followed by the keyword `where`.
* It must begin with a capital letter, like any other type name.

#### Implicit abstract type

* Whenever an interface is defined, an abstract type is defined with the same name. "Abstract" here means:
  * Values of this type cannot be created using a data constructor. Instead, they are constructed by applying the function `toInterface` to a template value.
  * Values of this type cannot be inspected directly via case analysis. Instead, use functions such as `fromInterface`.
  * See `daml-ref-interface-functions` for more information on these and other functions for interacting with interface values.
* An interface value carries inside it the type and parameters of the template value from which it was constructed.
* As for templates, the existence of a local binding `b` of type `I`, where `I` is an interface does not necessarily imply the existence on the ledger of a contract with the template type and parameters used to construct `b`. This can only be assumed if `b` the result of a fetch from the ledger within the same transaction.

#### Interface Methods

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
method1 : Party
method2 : Int
method3 : Bool -> Int -> Int -> Int
```

* An interface may define any number of methods.
* A method definition consists of the method name and the method type, separated by a single colon `:`. The name of the method must be a valid identifier beginning with a lowercase letter or an underscore.
* A method definition introduces a top level function of the same name:
  * If the interface is called `I`, the method is called `m`, and the method type is `M` (which might be a function type), this introduces the function `m : I -> M`:

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
<DamlInterfacesINTERFACEMETHODSTOPLEVEL />
```

* The first argument's type `I` means that the function can only be applied to values of the interface type `I` itself. Methods cannot be applied to template values, even if there exists an `interface instance` of `I` for that template. To use an interface method on a template value, first convert it using the `toInterface` function.

* Applying the function to such argument results in a value of type `M`, corresponding to the implementation of `m` in the interface instance of `I` for the underlying template type `t` (the type of the template value from which the interface value was constructed).

* One special method, `view`, must be defined for the viewtype. (see `interface-viewtype` below).

#### Interface View Type

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data MyInterfaceViewType =
  MyInterfaceViewType { name : Text, value : Int }
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
viewtype MyInterfaceViewType
```

* All interface instances must implement a special `view` method which returns a value of the type declared by `viewtype`.
* The type must be a record.
* This type is returned by subscriptions on interfaces.

#### Interface Choices

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
choice MyChoice : (ContractId MyInterface, Int)
  with
    argument1 : Bool
    argument2 : Int
  controller method1 this
  do
    let n0 = method2 this
    let n1 = method3 this argument1 argument2 n0
    pure (self, n1)

nonconsuming choice MyNonConsumingChoice : Int
  controller method1 this
  do
    pure $ method2 this
```

* Interface choices work in a very similar way to template choices. Any contract of a template type for which an interface instance exists will grant the choice to the controlling party.
* Interface choices can only be exercised on values of the corresponding interface type. To exercise an interface choice on a template value, first convert it using the `toInterface` function.
* Interface methods can be used to define the controller of a choice (e.g. `method1`) as well as the actions that run when the choice is *exercised* (e.g. `method2` and `method3`).
* As for template choices, the `choice` keyword can be optionally prefixed with the `nonconsuming` keyword to specify that the contract will not be consumed when the choice is exercised. If not specified, the choice will be `consuming`. Note that the `preconsuming` and `postconsuming` qualifiers are not supported on interface choices.
* See `choices` for full reference information, but note that controller-first syntax is not supported for interface choices.

#### Empty Interfaces

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data EmptyInterfaceView = EmptyInterfaceView {}

interface YourInterface where
  viewtype EmptyInterfaceView
```

* It is possible (though not necessarily useful) to define an interface without methods, precondition or choices. However, a view type must always be defined, though it can be set to unit.

### Interface Instances

For context, a simple template definition:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    field1 : Party
    field2 : Int
  where
    signatory field1
```

#### `interface instance` clause

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance MyInterface for NameOfTemplate where
  view = MyInterfaceViewType "NameOfTemplate" 100
  method1 = field1
  method2 = field2
  method3 False _ _ = 0
  method3 True x y
    | x > 0 = x + y
    | otherwise = y
```

* To make a template an instance of an existing interface, an `interface instance` clause must be defined in the template declaration.
* The template of the clause must match the enclosing declaration. In other words, a template `T` declaration can only contain `interface instance` clauses where the template is `T`.
* The clause must start with the keywords `interface instance`, followed by the name of the interface, then the keyword `for` and the name of the template, and finally the keyword `where`, which introduces a block where **all** the methods of the interface must be implemented.
* Within the clause, there's an implicit local binding `this` referring to the contract on which the method is applied, which has the type of the template's data record. The template parameters of this contract are also in scope.
* Method implementations can be defined using the same syntax as for top level functions, including pattern matches and guards (e.g. `method3`).
* Each method implementation must return the same type as specified for that method in the interface declaration.
* The implementation of the special `view` method must return the type specified as the `viewtype` in the interface declaration.

#### Empty `interface instance` clause

* If the interface has no methods, the interface instance only needs to implement the `view` method:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance YourInterface for NameOfTemplate where
  view = EmptyInterfaceView
```

### Interface Functions

#### `interfaceTypeRep`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>HasInterfaceTypeRep i =></code><br />
      <code>i -> TemplateTypeRep</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>MyInterface -> TemplateTypeRep</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>The value of the resulting <code>TemplateTypeRep</code> indicates what template was used to construct the interface value.</td>
    </tr>
  </tbody>
</table>

#### `toInterface`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>t -> i</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>MyTemplate -> MyInterface</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Converts a template value into an interface value.</td>
    </tr>
  </tbody>
</table>

#### `fromInterface`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>HasFromInterface t i =></code><br />
      <code>i -> Optional t</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>MyInterface -> Optional MyTemplate</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Attempts to convert an interface value back into a template value. The result is <code>None</code> if the expected template type doesn't match the underlying template type used to construct the contract.</td>
    </tr>
  </tbody>
</table>

#### `toInterfaceContractId`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>ContractId t -> ContractId i</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>ContractId MyTemplate -> ContractId MyInterface</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Converts a template Contract ID into an Interface Contract ID.</td>
    </tr>
  </tbody>
</table>

#### `fromInterfaceContractId`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>forall t i.</code><br />
      <code>HasFromInterface t i =></code><br />
      <code>ContractId i -> ContractId t</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>ContractId MyInterface -> ContractId MyTemplate</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Converts an interface contract id into a template contract id. This function does not verify that the given contract id actually points to a contract of the resulting type; if that is not the case, a subsequent <code>fetch</code>, <code>exercise</code> or <code>archive</code> will fail. Therefore, this should only be used when the underlying contract is known to be of the resulting type, or when the result is immediately used by a <code>fetch</code>, <code>exercise</code> or <code>archive</code> action and a transaction failure is the desired behavior in case of mismatch. In all other cases, consider using <code>fetchFromInterface</code> instead.</td>
    </tr>
  </tbody>
</table>

#### `coerceInterfaceContractId`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>forall j i.</code><br />
      <code>(HasInterfaceTypeRep i, HasInterfaceTypeRep j) =></code><br />
      <code>ContractId i -> ContractId j</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><code>ContractId SourceInterface -> ContractId TargetInterface</code></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Converts an interface contract id into a contract id of a different interface. This function does not verify that the given contract id actually points to a contract of the resulting type; if that is not the case, a subsequent <code>fetch</code>, <code>exercise</code> or <code>archive</code> will fail. Therefore, this should only be used when the underlying contract is known to be of the resulting type, or when the result is immediately used by a <code>fetch</code>, <code>exercise</code> or <code>archive</code> action and a transaction failure is the desired behavior in case of mismatch.</td>
    </tr>
  </tbody>
</table>

#### `fetchFromInterface`

<table>
  <tbody>
    <tr className="odd">
      <td>Type</td>
      <td><p><code>forall t i.</code><br />
      <code>(HasFromInterface t i, HasFetch i) =></code><br />
      <code>ContractId i -> Update (Optional (ContractId t, t))</code></p></td>
    </tr>

    <tr className="even">
      <td>Instantiated Type</td>
      <td><p><code>ContractId MyInterface -></code><br />
      <code>Update (Optional (ContractId MyTemplate, MyTemplate))</code></p></td>
    </tr>

    <tr className="odd">
      <td>Notes</td>
      <td>Attempts to fetch and convert an interface contract id into a template, returning both the converted contract and its contract id if the conversion is successful, or <code>None</code> otherwise.</td>
    </tr>
  </tbody>
</table>

### Required Interfaces

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface OurInterface requires MyInterface, YourInterface where
  viewtype EmptyInterfaceView
```

* An interface can depend on other interfaces. These are specified with the `requires` keyword after the interface name but before the `where` keyword, separated by commas.

* For an interface declaration to be valid, its list of required interfaces must be transitively closed. In other words, an interface `I` cannot require an interface `J` without also explicitly requiring all the interfaces required by `J`. The order, however, is irrelevant.

  For example, given

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Shape where
    viewtype EmptyInterfaceView

  interface Rectangle requires Shape where
    viewtype EmptyInterfaceView
  ```

  This declaration for interface `Square` would cause a compiler error

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  -- Compiler error! "Interface Square is missing requirement [Shape]"
  interface Square requires Rectangle where
    viewtype EmptyInterfaceView
  ```

  Explicitly adding `Shape` to the required interfaces fixes the error

  ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  interface Square requires Rectangle, Shape where
    viewtype EmptyInterfaceView
  ```

* For a template `T` to be a valid `interface instance` of an interface `I`, `T` must also be an `interface instance` of each of the interfaces required by `I`.

#### Interface Functions

| Function                  | Notes                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `toInterface`             | Can also be used to convert an interface value to one of its required interfaces.                                                  |
| `fromInterface`           | Can also be used to convert a value of an interface type to one of its requiring interfaces.                                       |
| `toInterfaceContractId`   | Can also be used to convert an interface contract id into a contract id of one of its required interfaces.                         |
| `fromInterfaceContractId` | Can also be used to convert an interface contract id into a contract id of one of its requiring interfaces.                        |
| `fetchFromInterface`      | Can also be used to fetch and convert an interface contract id into a contract and contract id of one of its requiring interfaces. |

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/exceptions.rst" hash="0c6fee4c" */}

## Reference: Exceptions (Deprecated)

<Warning>
  User-defined Daml Exceptions, catching, and throwing have been deprecated and are being phased out in favour of the Canton error framework, which represents Daml errors as `InvalidGivenCurrentSystemStateOther`.
</Warning>

Exceptions are a deprecated Daml feature which provides a way to handle certain errors that arise during interpretation instead of aborting the transaction, and to roll back the state changes that lead to the error.

There are two types of errors:

### Builtin Errors

| Exception type       | Thrown on                                                   |
| -------------------- | ----------------------------------------------------------- |
| `GeneralError`       | Calls to `error` and `abort`                                |
| `ArithmeticError`    | Arithmetic errors like overflows and division by zero       |
| `PreconditionFailed` | `ensure` statements that return `False`                     |
| `AssertionFailed`    | Failed `assert` calls (or other functions from `DA.Assert`) |

Note that other errors cannot be handled via exceptions, e.g., an exercise on an inactive contract will still result in a transaction abort.

### User-defined Exceptions

Users can define their own exception types which can be thrown and caught. The definition looks similar to templates, and just like with templates, the definition produces a record type of the given name as well as instances to make that type throwable and catchable.

In addition to the record fields, exceptions also need to define a `message` function.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exception MyException
  with
    field1 : Int
    field2 : Text
  where
    message "MyException(" <> show field1 <> ", " <> show field2 <> ")"
```

### Throw Exceptions

There are two ways to throw exceptions:

1. Inside of an `Action` like `Update` or `Script` you can use `throw` from `DA.Exception`. This works for any `Action` that is an instance of `ActionThrow`.
2. Outside of `ActionThrow` you can throw exceptions using `throwPure`.

If both are an option, it is generally preferable to use `throw` since it is easier to reason about when exactly the exception will get thrown.

### Catch Exceptions

Exceptions are caught in try-catch blocks similar to those found in languages like Java. The `try` block defines the scope within which errors should be handled while the `catch` clauses defines which types of errors are handled and how the program should continue. If an exception gets caught, the subtransaction between the `try` and the the point where the exception is thrown is rolled back. The actions under rollback nodes are still validated, so, e.g., you can never fetch a contract that is inactive at that point or have two contracts with the same key active at the same time. However, all ledger state changes (creates, consuming exercises) are rolled back to the state before the rollback node.

Each try-catch block can have multiple `catch` clauses with the first one that applies taking precedence.

In the example below the `create` of `T` will be rolled back and the first `catch` clause applies which will create an `Error` contract.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
try do
  _ <- create (T p)
  throw MyException with
    field1 = 0
    field2 = "42"
catch
  (MyException field1 field2) ->
    create Error with
      p = p
      msg = "MyException"
  (ArithmeticError _) ->
    create Error with
      p = p
      msg = "ArithmeticError"
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/daml/working-with.rst" hash="56b3d265" */}

## Reference: Built-in Functions

This page gives reference information on built-in functions for working with a variety of common concepts.

### Work with Time

Daml has these built-in functions for working with time:

* `datetime`: creates a `Time` given year, month, day, hours, minutes, and seconds as argument.
* `subTime`: subtracts one time from another. Returns the `RelTime` difference between `time1` and `time2`.
* `addRelTime`: add times. Takes a `Time` and `RelTime` and adds the `RelTime` to the `Time`.
* `days`, `hours`, `minutes`, `seconds`: constructs a `RelTime` of the specified length.
* `pass`: (in Daml Script tests only) use `pass : RelTime -> Script Time` to advance the ledger time by the argument amount. Returns the new time.

### Work with Numbers

Daml has these built-in functions for working with numbers:

* `round`: rounds a `Decimal` number to `Int`.

  `round d` is the *nearest* `Int` to `d`. Tie-breaks are resolved by rounding away from zero, for example:

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  round 2.5 == 3    round (-2.5) == -3
  round 3.4 == 3    round (-3.7) == -4
  ```

* `truncate`: converts a `Decimal` number to `Int`, truncating the value towards zero, for example:

  ```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
  truncate 2.2 == 2    truncate (-2.2) == -2
  truncate 4.9 == 4    v (-4.9) == -4
  ```

* `intToDecimal`: converts an `Int` to `Decimal`.

The set of numbers expressed by `Decimal` is not closed under division as the result may require more than 10 decimal places to represent. For example, `1.0 / 3.0 == 0.3333...` is a rational number, but not a `Decimal`.

### Work with Text

Daml has these built-in functions for working with text:

* `<>` operator: concatenates two `Text` values.
* `show` converts a value of the primitive types (`Bool`, `Int`, `Decimal`, `Party`, `Time`, `RelTime`) to a `Text`.

To escape text in Daml strings, use `\`:

<table style={{width: "69%"}}>
  <colgroup>
    <col style={{width: "27%"}} />

    <col style={{width: "41%"}} />
  </colgroup>

  <thead>
    <tr className="header">
      <th>
        <blockquote>
          <p>Character</p>
        </blockquote>
      </th>

      <th>How to escape it</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td>`\`</td>
      <td>`\\`</td>
    </tr>

    <tr className="even">
      <td>`"`</td>
      <td>`\"`</td>
    </tr>

    <tr className="odd">
      <td><code>'</code></td>
      <td><code>'</code></td>
    </tr>

    <tr className="even">
      <td>Newline</td>
      <td><code>\n</code></td>
    </tr>

    <tr className="odd">
      <td>Tab</td>
      <td><code>\t</code></td>
    </tr>

    <tr className="even">
      <td>Carriage return</td>
      <td><code>\r</code></td>
    </tr>

    <tr className="odd">
      <td>Unicode (using <code>!</code> as an example)</td>

      <td>
        <ul>
          <li>Decimal code: <code>\33</code></li>
          <li>Octal code: <code>\o41</code></li>
          <li>Hexadecimal code: <code>\x21</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

### Work with Lists

Daml has these built-in functions for working with lists:

* `foldl` and `foldr`: see `daml-ref-folding` below.

#### Fold

A *fold* takes:

* a binary operator
* a first *accumulator* value
* a list of values

The elements of the list are processed one-by-one (from the left in a `foldl`, or from the right in a `foldr`).

<Note>
  We'd usually recommend using `foldl`, as `foldr` is usually slower. This is because it needs to traverse the whole list before starting to discharge its elements.
</Note>

Processing goes like this:

1. The binary operator is applied to the first accumulator value and the first element in the list. This produces a second accumulator value.
2. The binary operator is applied to the *second* accumulator value and the second element in the list. This produces a third accumulator value.
3. This continues until there are no more elements in the list. Then, the last accumulator value is returned.

As an example, to sum up a list of integers in Daml:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumList =
  script do
    assert (foldl (+) 0 [1, 2, 3] == 6)
```

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/reference/fixity.rst" hash="a12a5d86" */}

## Fixity, Associativity and Precedence

With normal, *prefix* operators (e.g. functions), the semantics of `f g h` is clear: `f` is a function that takes `g` and `h` as parameters. If we want `f` to take the result of applying `g` to `h` we write `f (g h)`.

In the case of *infix* operators (e.g. symbol operators such as `+` and `*`, or functions surrounded by backticks, for example `` `elem ```), it is less clear. What does ``x - y - z`mean? Subtracting`x`from`y`first (i.e.`(x - y) - z`) generally yields different results than subtracting `z`from`y`first (i.e.`x - (y - z)`). In Daml, the subtraction operator `-`is defined as a \*left-assocative\* operator. That is, when we write`x - y - z - ...`the parser associates \*to the left\*, meaning the parser interprets this as`((x - y) - z) - ...`\`.

Some operators are *right-associative*. We have already encountered one: function application! A function signature of `a -> b -> c -> ...` is parsed as `(a -> (b -> (c -> ...)))`.

Finally, some operators are non-associative. A good example are comparison operators such as `==` and `>`. This means any ambiguous usage of these operators (e.g. `a == b == c` or `a > b > c`) results in a **parse error**.

<Note>
  Non-associative operators are not to be confused with operators that are both left- *and* right-associative, such as `+` (since `(x + y) + z = x + (y + z))`). To obtain a deterministic parser, such operators must be declared as one of either left-associative or right-associative. In Daml the `+` operator has been declared as left-associative
</Note>

The *precedence* of operators defines, when combining different operators, which operator is processed first. For example, in general (and in Daml), multiplication *takes precedence* over addition. That is, `x + y * z` is parsed as `x + (y * z)`. Operator precedence is expressed as a number, where a higher number indicates a higher precedence. Operators of same precedence are associated to the left (e.g. `x + y - z` is parsed as `(x + y) - z`.

The fixity and precedence of an operator are declared using the `infixl`, `infix`, and `infixr` keywords (denoting left-, non-, and right-associativity, respectfully) that take an integer between 0 and 9 inclusive and an operator the fixity applies to. For example, `infixl 6 +` declares that `+` is a `left-associative` operator with precedence `6`. These keywords can be used for user-defined operators as well. The following table shows the fixity and precedence for operators that are built-in to the Daml language, such as `+` and `-`:

<table>
  <thead>
    <tr className="header">
      <th>Precedence</th>
      <th>Left-associative</th>
      <th>Non-associative</th>
      <th>Right-associative</th>
    </tr>
  </thead>

  <tbody>
    <tr className="odd">
      <td><p>9 8 7 6 5 4 3 2 1 0</p></td>
      <td><p><code>`!!</code></p> <p><code>*</code>, <code>/</code>, <code>%</code> <code>+</code>, <code>-</code></p> <p><code>&lt;$</code>, <code>&lt;$&gt;</code>, <code>$&gt;</code>, <code>&lt;*</code>, <code>&lt;*&gt;</code>, <code>*&gt;</code></p> <p><code>&gt;&gt;</code>, <code>&gt;&gt;=</code>, <code>&lt;&amp;&gt;</code></p></td> <td><p><code>==</code>, <code>/=</code>, <code>&lt;</code>, <code>&lt;=</code>, <code>&gt;==</code>, <code>&gt;</code>, <code>===</code>, <code>=/=</code></p></td> <td><p><code>.</code> <code>&lt;#&amp;&amp;&gt;</code>, <code>^</code>, <code>**</code></p> <p><code>&lt;&gt;</code> <code>`++</code>, <code>::</code></p>
      <p><code>&&</code>, <code>&&&</code> <code>||</code>, <code>|||</code> <code>=\<\<</code>, <code>\<=\<</code>, <code>>=></code> <code>\$</code></p></td>
    </tr>
  </tbody>
</table>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
