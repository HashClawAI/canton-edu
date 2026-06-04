---
title: "Prelude"
slug: "appdev-reference-daml-standard-library-prelude"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/prelude.md"
source_title: "Prelude"
tags:
  - appdev
  - reference
  - daml-standard-library
  - prelude
---

# Prelude

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Prelude

> Reference documentation for Daml module Prelude.

<span id="module-prelude-72703" />

# Prelude

The pieces that make up the Daml language.

## Module Snapshot

<CardGroup cols={2}>
  <Card title="Lifecycle">
    Stable.
  </Card>

  <Card title="Notices">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

## Data Types

<span id="type-da-internal-any-anychoice-86490" />

### `data AnyChoice`

Existential choice type that can wrap an arbitrary choice.

Constructors:

<span id="constr-da-internal-any-anychoice-64121" />

* `AnyChoice`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyChoice | Any |  |
  \| getAnyChoiceTemplateTypeRep | TemplateTypeRep |  |

Instances:

* `instance Eq AnyChoice`
* `instance Ord AnyChoice`

<span id="type-da-internal-any-anycontractkey-68193" />

### `data AnyContractKey`

Existential contract key type that can wrap an arbitrary contract key.

Constructors:

<span id="constr-da-internal-any-anycontractkey-82848" />

* `AnyContractKey`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyContractKey | Any |  |
  \| getAnyContractKeyTemplateTypeRep | TemplateTypeRep |  |

Instances:

* `instance Eq AnyContractKey`
* `instance Ord AnyContractKey`

<span id="type-da-internal-any-anytemplate-63703" />

### `data AnyTemplate`

Existential template type that can wrap an arbitrary template.

Constructors:

<span id="constr-da-internal-any-anytemplate-32540" />

* `AnyTemplate`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getAnyTemplate | Any |  |

Instances:

* `instance Eq AnyTemplate`
* `instance Ord AnyTemplate`

<span id="type-da-internal-any-templatetyperep-33792" />

### `data TemplateTypeRep`

Unique textual representation of a template Id.

Constructors:

<span id="constr-da-internal-any-templatetyperep-57303" />

* `TemplateTypeRep`
  \| Field | Type | Description |
  \| :---- | :--- | :---------- |
  \| getTemplateTypeRep | TypeRep |  |

Instances:

* `instance Eq TemplateTypeRep`
* `instance Ord TemplateTypeRep`

<span id="type-da-internal-down-down-61433" />

### `data Down a`

The `Down` type can be used for reversing sorting order.
For example, `sortOn (\x -> Down x.field)` would sort by descending `field`.

Constructors:

<span id="constr-da-internal-down-down-26630" />

* `Down a`

Instances:

* `instance Action Down`
* `instance Applicative Down`
* `instance Functor Down`
* `instance Eq a => Eq (Down a)`
* `instance Ord a => Ord (Down a)`
* `instance Show a => Show (Down a)`

<span id="type-da-internal-interface-implements-92077" />

### `type Implements = (HasInterfaceTypeRep i, HasToInterface t i, HasFromInterface t i)`

(Daml-LF >= 1.15) Constraint that indicates that a template implements an interface.

<span id="type-da-internal-lf-anyexception-7004" />

### `data AnyException`

A wrapper for all exception types.

<Warning>
  Deprecated: Exceptions are deprecated, prefer `failWithStatus`, and avoid using catch.
</Warning>

<Warning>
  Deprecated: Use `-Wno-deprecated-exceptions` to disable this warning.
</Warning>

Instances:

* `instance HasFromAnyException AnyException`
* `instance HasMessage AnyException`
* `instance HasToAnyException AnyException`

<span id="type-da-internal-lf-contractid-95282" />

### `data ContractId a`

The `ContractId a` type represents an ID for a contract created from a template `a`.
You can use the ID to fetch the contract, among other things.

Instances:

* `instance Eq (ContractId a)`
* `instance Ord (ContractId a)`
* `instance Show (ContractId a)`

<span id="type-da-internal-lf-date-32253" />

### `data Date`

The `Date` type represents a date, for example `date 2007 Apr 5`.
The bounds for Date are 0001-01-01 and 9999-12-31.

Instances:

* `instance Eq Date`
* `instance Ord Date`
* `instance Bounded Date`
* `instance Enum Date`
* `instance Show Date`

<span id="type-da-internal-lf-map-90052" />

### `data Map a b`

The `Map a b` type represents an associative array from keys of type `a`
to values of type `b`. It uses the built-in equality for keys. Import
`DA.Map` to use it.

Instances:

* `instance Ord k => Foldable (Map k)`
* `instance Ord k => Monoid (Map k v)`
* `instance Ord k => Semigroup (Map k v)`
* `instance GetField map (Set k) (Map k ())`
* `instance SetField map (Set k) (Map k ())`
* `instance Ord k => Traversable (Map k)`
* `instance Ord k => Functor (Map k)`
* `instance (Ord k, Eq v) => Eq (Map k v)`
* `instance (Ord k, Ord v) => Ord (Map k v)`
* `instance (Show k, Show v) => Show (Map k v)`

<span id="type-da-internal-lf-party-57932" />

### `data Party`

The `Party` type represents a party to a contract.

Instances:

* `instance HasFromHex (Optional Party)`
* `instance HasToHex Party`
* `instance IsParties Party`
* `instance IsParties (Optional Party)`
* `instance IsParties (NonEmpty Party)`
* `instance IsParties (Set Party)`
* `instance IsParties [Party]`
* `instance Eq Party`
* `instance Ord Party`
* `instance Show Party`

<span id="type-da-internal-lf-textmap-11691" />

### `data TextMap a`

The `TextMap a` type represents an associative array from keys of type
`Text` to values of type `a`.

Instances:

* `instance Foldable TextMap`
* `instance Monoid (TextMap b)`
* `instance Semigroup (TextMap b)`
* `instance GetField meta FailureStatus (TextMap Text)`
* `instance SetField meta FailureStatus (TextMap Text)`
* `instance Traversable TextMap`
* `instance Functor TextMap`
* `instance Eq a => Eq (TextMap a)`
* `instance Ord a => Ord (TextMap a)`
* `instance Show a => Show (TextMap a)`

<span id="type-da-internal-lf-time-63886" />

### `data Time`

The `Time` type represents a specific datetime in UTC,
for example `time (date 2007 Apr 5) 14 30 05`.
The bounds for Time are 0001-01-01T00:00:00.000000Z and
9999-12-31T23:59:59.999999Z.

Instances:

* `instance Eq Time`
* `instance Ord Time`
* `instance Bounded Time`
* `instance Show Time`

<span id="type-da-internal-lf-update-68072" />

### `data Update a`

The `Update a` type represents an `Action` to update or query the ledger,
before returning a value of type `a`. Examples include `create` and `fetch`.

Instances:

* `instance CanAssert Update`
* `instance ActionCatch Update`
* `instance ActionThrow Update`
* `instance ActionFailWithStatus Update`
* `instance CanAbort Update`
* `instance HasTime Update`
* `instance Action Update`
* `instance ActionFail Update`
* `instance Applicative Update`
* `instance Functor Update`

<span id="type-da-internal-prelude-optional-37153" />

### `data Optional a`

The `Optional` type encapsulates an optional value.  A value of type
`Optional a` either contains a value of type `a` (represented as `Some a`),
or it is empty (represented as `None`).  Using `Optional` is a good way to
deal with errors or exceptional cases without resorting to drastic
measures such as `error`.

The `Optional` type is also an `Action`.  It is a simple kind of error
`Action`, where all errors are represented by `None`.  A richer
error `Action` could be built using the `Data.Either.Either` type.

Constructors:

<span id="constr-da-internal-prelude-none-34906" />

* `None`

<span id="constr-da-internal-prelude-some-71164" />

* `Some a`

Instances:

* `instance HasFromHex (Optional Party)`
* `instance HasFromHex (Optional Int)`
* `instance HasFromHex (Optional Text)`
* `instance Foldable Optional`
* `instance Action Optional`
* `instance ActionFail Optional`
* `instance Applicative Optional`
* `instance IsParties (Optional Party)`
* `instance Traversable Optional`
* `instance Functor Optional`
* `instance Eq a => Eq (Optional a)`
* `instance Ord a => Ord (Optional a)`
* `instance Show a => Show (Optional a)`

<span id="type-da-internal-template-archive-15178" />

### `data Archive`

The data type corresponding to the implicit `Archive`
choice in every template.

Constructors:

<span id="constr-da-internal-template-archive-55291" />

* `Archive`
  (no fields)

Instances:

* `instance Eq Archive`
* `instance Show Archive`

<span id="type-da-internal-template-functions-choice-82157" />

### `type Choice = (Template t, HasExercise t c r, HasToAnyChoice t c r, HasFromAnyChoice t c r)`

Constraint satisfied by choices.

<span id="type-da-internal-template-functions-template-31804" />

### `type Template = (HasTemplateTypeRep t, HasToAnyTemplate t, HasFromAnyTemplate t)`

<span id="type-da-internal-template-functions-templatekey-95200" />

### `type TemplateKey = (Template t, HasKey t k, HasLookupByKey t k, HasFetchByKey t k, HasMaintainer t k, HasToAnyContractKey t k, HasFromAnyContractKey t k)`

Constraint satisfied by template keys.

## Typeclasses

<span id="class-da-internal-assert-canassert-67323" />

### `class Action m => CanAssert m`

Constraint that determines whether an assertion can be made
in this context.

Methods:

* `assertFail : Text -> m t`
  Abort since an assertion has failed. In an Update, Scenario,
  or Script context this will throw an AssertionFailed
  exception. In an `Either Text` context, this will return the
  message as an error.

Instances:

* `instance CanAssert Update`
* `instance CanAssert (Either Text)`

<span id="class-da-internal-interface-hasinterfacetyperep-84221" />

### `class HasInterfaceTypeRep i`

(Daml-LF >= 1.15) Exposes the `interfaceTypeRep` function. Available only for interfaces.

<span id="class-da-internal-interface-hastointerface-68104" />

### `class HasToInterface t i`

(Daml-LF >= 1.15) Exposes the `toInterface` and `toInterfaceContractId` functions.

<span id="class-da-internal-interface-hasfrominterface-43863" />

### `class HasFromInterface t i`

(Daml-LF >= 1.15) Exposes `fromInterface` and `fromInterfaceContractId`
functions.

Methods:

* `fromInterface : i -> Optional t`
  (Daml-LF >= 1.15) Attempt to convert an interface value back into a
  template value. A `None` indicates that the expected template
  type doesn't match the underyling template type for the
  interface value.

  For example, `fromInterface @MyTemplate value` will try to convert
  the interface value `value` into the template type `MyTemplate`.

<span id="class-da-internal-interface-hasinterfaceview-4492" />

### `class HasInterfaceView i v`

Methods:

* `_view : i -> v`

<span id="class-da-internal-lf-hastime-96546" />

### `class HasTime m`

The `HasTime` class is for where the time is available: `Update`

Methods:

* `getTime : HasCallStack => m Time`
  Get the current time.

Instances:

* `instance HasTime Update`

<span id="class-da-internal-lf-canabort-29060" />

### `class Action m => CanAbort m`

The `CanAbort` class is for `Action` s that can be aborted.

Methods:

* `abort : Text -> m a`
  Abort the current action with a message.

Instances:

* `instance CanAbort Update`
* `instance CanAbort (Either Text)`

<span id="class-da-internal-prelude-applicative-9257" />

### `class Functor f => Applicative f`

Methods:

* `pure : a -> f a`
  Lift a value.
* `<*> : f (a -> b) -> f a -> f b`
  Sequentially apply the function.

  A few functors support an implementation of `<*>` that is more
  efficient than the default one.
* `liftA2 : (a -> b -> c) -> f a -> f b -> f c`
  Lift a binary function to actions.

  Some functors support an implementation of `liftA2` that is more
  efficient than the default one. In particular, if `fmap` is an
  expensive operation, it is likely better to use `liftA2` than to
  `fmap` over the structure and then use `<*>`.
* `*> : f a -> f b -> f b`
  Sequence actions, discarding the value of the first argument.
* `<* : f a -> f b -> f a`
  Sequence actions, discarding the value of the second argument.

Instances:

* `instance Applicative (-> r)`
* `instance Applicative (State s)`
* `instance Applicative Down`
* `instance Applicative Update`
* `instance Applicative Optional`
* `instance Applicative Formula`
* `instance Applicative NonEmpty`
* `instance Applicative (Validation err)`
* `instance Applicative (Either e)`
* `instance Applicative []`

<span id="class-da-internal-prelude-action-68790" />

### `class Applicative m => Action m`

Methods:

* `>>= : m a -> (a -> m b) -> m b`
  Sequentially compose two actions, passing any value produced
  by the first as an argument to the second.

Instances:

* `instance Action (-> r)`
* `instance Action (State s)`
* `instance Action Down`
* `instance Action Update`
* `instance Action Optional`
* `instance Action Formula`
* `instance Action NonEmpty`
* `instance Action (Either e)`
* `instance Action []`

<span id="class-da-internal-prelude-actionfail-34438" />

### `class Action m => ActionFail m`

This class exists to desugar pattern matches in do-notation.
Polymorphic usage, or calling `fail` directly, is not recommended.
Instead consider using `CanAbort`.

Methods:

* `fail : Text -> m a`
  Fail with an error message.

Instances:

* `instance ActionFail Update`
* `instance ActionFail Optional`
* `instance ActionFail (Either Text)`
* `instance ActionFail []`

<span id="class-da-internal-prelude-semigroup-78998" />

### `class Semigroup a`

The class of semigroups (types with an associative binary operation).

Methods:

* `<> : a -> a -> a`
  An associative operation.

Instances:

* `instance Ord k => Semigroup (Map k v)`
* `instance Semigroup (TextMap b)`
* `instance Semigroup All`
* `instance Semigroup Any`
* `instance Semigroup (Endo a)`
* `instance Multiplicative a => Semigroup (Product a)`
* `instance Additive a => Semigroup (Sum a)`
* `instance Semigroup (NonEmpty a)`
* `instance Ord a => Semigroup (Max a)`
* `instance Ord a => Semigroup (Min a)`
* `instance Ord k => Semigroup (Set k)`
* `instance Semigroup (Validation err a)`
* `instance Semigroup Ordering`
* `instance Semigroup Text`
* `instance Semigroup [a]`

<span id="class-da-internal-prelude-monoid-6742" />

### `class Semigroup a => Monoid a`

The class of monoids (types with an associative binary operation that has an identity).

Methods:

* `mempty : a`
  Identity of `(<>)`
* `mconcat : [a] -> a`
  Fold a list using the monoid.
  For example using `mconcat` on a list of strings would concatenate all strings to one lone string.

Instances:

* `instance Ord k => Monoid (Map k v)`
* `instance Monoid (TextMap b)`
* `instance Monoid All`
* `instance Monoid Any`
* `instance Monoid (Endo a)`
* `instance Multiplicative a => Monoid (Product a)`
* `instance Additive a => Monoid (Sum a)`
* `instance Ord k => Monoid (Set k)`
* `instance Monoid Ordering`
* `instance Monoid Text`
* `instance Monoid [a]`

<span id="class-da-internal-template-functions-hassignatory-17507" />

### `class HasSignatory t`

Exposes `signatory` function. Part of the `Template` constraint.

Methods:

* `signatory : t -> [Party]`
  The signatories of a contract.

<span id="class-da-internal-template-functions-hasobserver-3182" />

### `class HasObserver t`

Exposes `observer` function. Part of the `Template` constraint.

Methods:

* `observer : t -> [Party]`
  The observers of a contract.

<span id="class-da-internal-template-functions-hasensure-18132" />

### `class HasEnsure t`

Exposes `ensure` function. Part of the `Template` constraint.

Methods:

* `ensure : t -> Bool`
  A predicate that must be true, otherwise contract creation will fail.

<span id="class-da-internal-template-functions-hascreate-45738" />

### `class HasCreate t`

Exposes `create` function. Part of the `Template` constraint.

Methods:

* `create : t -> Update (ContractId t)`
  Create a contract based on a template `t`.

<span id="class-da-internal-template-functions-hasfetch-52387" />

### `class HasFetch t`

Exposes `fetch` function. Part of the `Template` constraint.

Methods:

* `fetch : ContractId t -> Update t`
  Fetch the contract data associated with the given contract ID.
  If the `ContractId t` supplied is not the contract ID of an active
  contract, this fails and aborts the entire transaction.

<span id="class-da-internal-template-functions-hassoftfetch-65731" />

### `class HasSoftFetch t`

Exposes `softFetch` function

<span id="class-da-internal-template-functions-hassoftexercise-29758" />

### `class HasSoftExercise t c r`

<span id="class-da-internal-template-functions-hasarchive-7071" />

### `class HasArchive t`

Exposes `archive` function. Part of the `Template` constraint.

Methods:

* `archive : ContractId t -> Update ()`
  Archive the contract with the given contract ID.

<span id="class-da-internal-template-functions-hastemplatetyperep-24134" />

### `class HasTemplateTypeRep t`

Exposes `templateTypeRep` function in Daml-LF 1.7 or later.
Part of the `Template` constraint.

<span id="class-da-internal-template-functions-hastoanytemplate-94418" />

### `class HasToAnyTemplate t`

Exposes `toAnyTemplate` function in Daml-LF 1.7 or later.
Part of the `Template` constraint.

<span id="class-da-internal-template-functions-hasfromanytemplate-95481" />

### `class HasFromAnyTemplate t`

Exposes `fromAnyTemplate` function in Daml-LF 1.7 or later.
Part of the `Template` constraint.

<span id="class-da-internal-template-functions-hasexercise-70422" />

### `class HasExercise t c r`

Exposes `exercise` function. Part of the `Choice` constraint.

Methods:

* `exercise : ContractId t -> c -> Update r`
  Exercise a choice on the contract with the given contract ID.

<span id="class-da-internal-template-functions-haschoicecontroller-39229" />

### `class HasChoiceController t c`

Exposes `choiceController` function. Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-haschoiceobserver-31221" />

### `class HasChoiceObserver t c`

Exposes `choiceObserver` function. Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-hasexerciseguarded-97843" />

### `class HasExerciseGuarded t c r`

(1.dev only) Exposes `exerciseGuarded` function.
Only available for interface choices.

Methods:

* `exerciseGuarded : (t -> Bool) -> ContractId t -> c -> Update r`
  (1.dev only) Exercise a choice on the contract with
  the given contract ID, only if the predicate returns `True`.

<span id="class-da-internal-template-functions-hastoanychoice-82571" />

### `class HasToAnyChoice t c r`

Exposes `toAnyChoice` function for Daml-LF 1.7 or later.
Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-hasfromanychoice-81184" />

### `class HasFromAnyChoice t c r`

Exposes `fromAnyChoice` function for Daml-LF 1.7 or later.
Part of the `Choice` constraint.

<span id="class-da-internal-template-functions-haskey-87616" />

### `class HasKey t k`

Exposes `key` function. Part of the `TemplateKey` constraint.

Methods:

* `key : t -> k`
  The key of a contract.

<span id="class-da-internal-template-functions-haslookupbykey-92299" />

### `class HasLookupByKey t k`

Exposes `lookupByKey` function. Part of the `TemplateKey` constraint.

Methods:

* `lookupByKey : k -> Update (Optional (ContractId t))`
  Look up the contract ID `t` associated with a given contract key `k`.

  You must pass the `t` using an explicit type application. For
  instance, if you want to look up a contract of template `Account` by its
  key `k`, you must call `lookupByKey @Account k`.

<span id="class-da-internal-template-functions-hasfetchbykey-54638" />

### `class HasFetchByKey t k`

Exposes `fetchByKey` function. Part of the `TemplateKey` constraint.

Methods:

* `fetchByKey : k -> Update (ContractId t, t)`
  Fetch the contract ID and contract data associated with a given
  contract key.

  You must pass the `t` using an explicit type application. For
  instance, if you want to fetch a contract of template `Account` by its
  key `k`, you must call `fetchByKey @Account k`.

<span id="class-da-internal-template-functions-hasmaintainer-28932" />

### `class HasMaintainer t k`

Exposes `maintainer` function. Part of the `TemplateKey` constraint.

<span id="class-da-internal-template-functions-hastoanycontractkey-35010" />

### `class HasToAnyContractKey t k`

Exposes `toAnyContractKey` function in Daml-LF 1.7 or later.
Part of the `TemplateKey` constraint.

<span id="class-da-internal-template-functions-hasfromanycontractkey-95587" />

### `class HasFromAnyContractKey t k`

Exposes `fromAnyContractKey` function in Daml-LF 1.7 or later.
Part of the `TemplateKey` constraint.

<span id="class-da-internal-template-functions-hasexercisebykey-36549" />

### `class HasExerciseByKey t k c r`

Exposes `exerciseByKey` function.

<span id="class-da-internal-template-functions-isparties-53750" />

### `class IsParties a`

Accepted ways to specify a list of parties: either a single party, or a list of parties.

Methods:

* `toParties : a -> [Party]`
  Convert to list of parties.

Instances:

* `instance IsParties Party`
* `instance IsParties (Optional Party)`
* `instance IsParties (NonEmpty Party)`
* `instance IsParties (Set Party)`
* `instance IsParties [Party]`

## Functions

<span id="function-da-internal-assert-assert-75697" />

### `assert`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assert : CanAssert m => Bool -> m ()
```

Check whether a condition is true. If it's not, abort the transaction.

<span id="function-da-internal-assert-assertmsg-31545" />

### `assertMsg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertMsg : CanAssert m => Text -> Bool -> m ()
```

Check whether a condition is true. If it's not, abort the transaction
with a message.

<span id="function-da-internal-assert-assertafter-43038" />

### `assertAfter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertAfter : (CanAssert m, HasTime m) => Time -> m ()
```

Check whether the given time is in the future. If it's not, abort the transaction.

<span id="function-da-internal-assert-assertbefore-99854" />

### `assertBefore`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
assertBefore : (CanAssert m, HasTime m) => Time -> m ()
```

Check whether the given time is in the past. If it's not, abort the transaction.

<span id="function-da-internal-date-dayssinceepochtodate-57782" />

### `daysSinceEpochToDate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
daysSinceEpochToDate : Int -> Date
```

Convert from number of days since epoch (i.e. the number of days since
January 1, 1970) to a date.

<span id="function-da-internal-date-datetodayssinceepoch-98906" />

### `dateToDaysSinceEpoch`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dateToDaysSinceEpoch : Date -> Int
```

Convert from a date to number of days from epoch (i.e. the number of days
since January 1, 1970).

<span id="function-da-internal-interface-interfacetyperep-28987" />

### `interfaceTypeRep`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interfaceTypeRep : HasInterfaceTypeRep i => i -> TemplateTypeRep
```

(Daml-LF >= 1.15) Obtain the `TemplateTypeRep` for the template given in the interface value.

<span id="function-da-internal-interface-tointerface-33774" />

### `toInterface`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toInterface : HasToInterface t i => t -> i
```

(Daml-LF >= 1.15) Convert a template value into an interface value.
For example `toInterface @MyInterface value` converts a template
`value` into a `MyInterface` type.

<span id="function-da-internal-interface-tointerfacecontractid-24085" />

### `toInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toInterfaceContractId : HasToInterface t i => ContractId t -> ContractId i
```

(Daml-LF >= 1.15) Convert a template contract id into an interface
contract id. For example, `toInterfaceContractId @MyInterface cid`.

<span id="function-da-internal-interface-frominterfacecontractid-39614" />

### `fromInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromInterfaceContractId : HasFromInterface t i => ContractId i -> ContractId t
```

(Daml-LF >= 1.15) Convert an interface contract id into a template
contract id. For example, `fromInterfaceContractId @MyTemplate cid`.

Can also be used to convert an interface contract id into a contract id of
one of its requiring interfaces.

This function does not verify that the interface contract id
actually points to a template of the given type. This means
that a subsequent `fetch`, `exercise`, or `archive` may fail, if,
for example, the contract id points to a contract that implements
the interface but is of a different template type than expected.

Therefore, you should only use `fromInterfaceContractId` in situations
where you already know that the contract id points to a contract of the
right template type. You can also use it in situations where you will
fetch, exercise, or archive the contract right away, when a transaction
failure is the appropriate response to the contract having the wrong
template type.

In all other cases, consider using `fetchFromInterface` instead.

<span id="function-da-internal-interface-coerceinterfacecontractid-23361" />

### `coerceInterfaceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
coerceInterfaceContractId : (HasInterfaceTypeRep i, HasInterfaceTypeRep j) => ContractId i -> ContractId j
```

(Daml-LF >= 1.15) Convert an interface contract id into a contract id of a
different interface. For example, given two interfaces `Source` and `Target`,
and `cid : ContractId Source`,
`coerceInterfaceContractId @Target @Source cid : ContractId Target`.

This function does not verify that the contract id
actually points to a contract that implements either interface. This means
that a subsequent `fetch`, `exercise`, or `archive` may fail, if,
for example, the contract id points to a contract of template `A` but it was
coerced into a `ContractId B` where `B` is an interface and there's no
interface instance B for A.

Therefore, you should only use `coerceInterfaceContractId` in situations
where you already know that the contract id points to a contract of the right
type. You can also use it in situations where you will fetch, exercise, or
archive the contract right away, when a transaction failure is the
appropriate response to the contract having the wrong type.

<span id="function-da-internal-interface-fetchfrominterface-99354" />

### `fetchFromInterface`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fetchFromInterface : (HasFromInterface t i, HasFetch i) => ContractId i -> Update (Optional (ContractId t, t))
```

(Daml-LF >= 1.15) Fetch an interface and convert it to a specific
template type. If conversion is succesful, this function returns
the converted contract and its converted contract id. Otherwise,
this function returns `None`.

Can also be used to fetch and convert an interface contract id into a
contract and contract id of one of its requiring interfaces.

Example:

```
do
  fetchResult <- fetchFromInterface @MyTemplate ifaceCid
  case fetchResult of
    None -> abort "Failed to convert interface to appropriate template type"
    Some (tplCid, tpl) -> do
       ... do something with tpl and tplCid ...
```

<span id="function-da-internal-interface-exerciseinterfaceguard-49471" />

### `_exerciseInterfaceGuard`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
_exerciseInterfaceGuard : a -> b -> c -> Bool
```

<span id="function-da-internal-interface-view-38554" />

### `view`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
view : HasInterfaceView i v => i -> v
```

<span id="function-da-internal-lf-partytotext-91600" />

### `partyToText`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partyToText : Party -> Text
```

Convert the `Party` to `Text`, giving back what you passed to `getParty`.
In most cases, you should use `show` instead. `show` wraps
the party in `'ticks'` making it clear it was a `Party` originally.

<span id="function-da-internal-lf-partyfromtext-17681" />

### `partyFromText`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partyFromText : Text -> Optional Party
```

Converts a `Text` to `Party`. It returns `None` if the provided text contains
any forbidden characters. See Daml-LF spec for a specification on which characters
are allowed in parties. Note that this function accepts text *without*
single quotes.

This function does not check on whether the provided
text corresponds to a party that "exists" on a given ledger: it merely converts
the given `Text` to a `Party`. The only way to guarantee that a given `Party`
exists on a given ledger is to involve it in a contract.

This function, together with `partyToText`, forms an isomorphism between
valid party strings and parties. In other words, the following equations hold:

```haskell-force theme={"theme":{"light":"github-light","dark":"github-dark"}}
∀ p. partyFromText (partyToText p) = Some p
∀ txt p. partyFromText txt = Some p ==> partyToText p = txt
```

This function will crash at runtime if you compile Daml to Daml-LF \< 1.2.

<span id="function-da-internal-lf-coercecontractid-14371" />

### `coerceContractId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
coerceContractId : ContractId a -> ContractId b
```

Used to convert the type index of a `ContractId`, since they are just
pointers. Note that subsequent fetches and exercises might fail if the
template of the contract on the ledger doesn't match.

<span id="function-da-internal-prelude-curry-6393" />

### `curry`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
curry : ((a, b) -> c) -> a -> b -> c
```

Turn a function that takes a pair into a function that takes two arguments.

<span id="function-da-internal-prelude-uncurry-79420" />

### `uncurry`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry : (a -> b -> c) -> (a, b) -> c
```

Turn a function that takes two arguments into a function that takes a pair.

<span id="function-da-internal-prelude-gtgt-56231" />

### `>>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
>> : Action m => m a -> m b -> m b
```

Sequentially compose two actions, discarding any value produced
by the first. This is like sequencing operators (such as the semicolon)
in imperative languages.

<span id="function-da-internal-prelude-ap-60204" />

### `ap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ap : Applicative f => f (a -> b) -> f a -> f b
```

Synonym for `<*>`.

<span id="function-da-internal-prelude-return-15945" />

### `return`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
return : Applicative m => a -> m a
```

Inject a value into the monadic type. For example, for `Update` and a
value of type `a`, `return` would give you an `Update a`.

<span id="function-da-internal-prelude-join-43001" />

### `join`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
join : Action m => m (m a) -> m a
```

Collapses nested actions into a single action.

<span id="function-da-internal-prelude-identity-53027" />

### `identity`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
identity : a -> a
```

The identity function.

<span id="function-da-internal-prelude-guard-82483" />

### `guard`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
guard : ActionFail m => Bool -> m ()
```

<span id="function-da-internal-prelude-foldl-3431" />

### `foldl`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl : (b -> a -> b) -> b -> [a] -> b
```

This function is a left fold, which you can use to inspect/analyse/consume lists.
`foldl f i xs` performs a left fold over the list `xs` using
the function `f`, using the starting value `i`.

Examples:

```
>>> foldl (+) 0 [1,2,3]
6

>>> foldl (^) 10 [2,3]
1000000
```

Note that foldl works from left-to-right over the list arguments.

<span id="function-da-internal-prelude-find-82808" />

### `find`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
find : (a -> Bool) -> [a] -> Optional a
```

`find p xs` finds the first element of the list `xs` where the
predicate `p` is true. There might not be such an element, which
is why this function returns an `Optional a`.

<span id="function-da-internal-prelude-length-32819" />

### `length`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
length : [a] -> Int
```

Gives the length of the list.

<span id="function-da-internal-prelude-any-88476" />

### `any`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
any : (a -> Bool) -> [a] -> Bool
```

Are there any elements in the list where the predicate is true?
`any p xs` is `True` if `p` holds for at least one element of `xs`.

<span id="function-da-internal-prelude-all-93363" />

### `all`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
all : (a -> Bool) -> [a] -> Bool
```

Is the predicate true for all of the elements in the list?
`all p xs` is `True` if `p` holds for every element of `xs`.

<span id="function-da-internal-prelude-or-54324" />

### `or`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
or : [Bool] -> Bool
```

Is at least one of elements in a list of `Bool` true?
`or bs` is `True` if at least one element of `bs` is `True`.

<span id="function-da-internal-prelude-and-20777" />

### `and`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
and : [Bool] -> Bool
```

Is every element in a list of Bool true?
`and bs` is `True` if every element of `bs` is `True`.

<span id="function-da-internal-prelude-elem-84192" />

### `elem`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
elem : Eq a => a -> [a] -> Bool
```

Does this value exist in this list?
`elem x xs` is `True` if `x` is an element of the list `xs`.

<span id="function-da-internal-prelude-notelem-95004" />

### `notElem`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
notElem : Eq a => a -> [a] -> Bool
```

Negation of `elem`:
`elem x xs` is `True` if `x` is *not* an element of the list `xs`.

<span id="function-da-internal-prelude-ltdollargt-82160" />

### `<$>`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
<$> : Functor f => (a -> b) -> f a -> f b
```

Synonym for `fmap`.

<span id="function-da-internal-prelude-optional-80885" />

### `optional`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
optional : b -> (a -> b) -> Optional a -> b
```

The `optional` function takes a default value, a function, and a `Optional`
value.  If the `Optional` value is `None`, the function returns the
default value.  Otherwise, it applies the function to the value inside
the `Some` and returns the result.

Basic usage examples:

```
>>> optional False (> 2) (Some 3)
True
```

```
>>> optional False (> 2) None
False
```

```
>>> optional 0 (*2) (Some 5)
10
>>> optional 0 (*2) None
0
```

This example applies `show` to a `Optional Int`. If you have `Some n`,
this shows the underlying `Int`, `n`. But if you have `None`, this
returns the empty string instead of (for example) `None`:

```
>>> optional "" show (Some 5)
"5"
>>> optional "" show (None : Optional Int)
""
```

<span id="function-da-internal-prelude-either-9020" />

### `either`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
either : (a -> c) -> (b -> c) -> Either a b -> c
```

The `either` function provides case analysis for the `Either` type.
If the value is `Left a`, it applies the first function to `a`;
if it is `Right b`, it applies the second function to `b`.

Examples:

This example has two values of type `Either [Int] Int`, one using the
`Left` constructor and another using the `Right` constructor. Then
it applies `either` the `length` function (if it has a `[Int]`)
or the "times-two" function (if it has an `Int`):

```
>>> let s = Left [1,2,3] : Either [Int] Int in either length (*2) s
3
>>> let n = Right 3 : Either [Int] Int in either length (*2) n
6
```

<span id="function-da-internal-prelude-concat-86947" />

### `concat`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concat : [[a]] -> [a]
```

Take a list of lists and concatenate those lists into one list.

<span id="function-da-internal-prelude-plusplus-64685" />

### `++`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
++ : [a] -> [a] -> [a]
```

Concatenate two lists.

<span id="function-da-internal-prelude-flip-60304" />

### `flip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
flip : (a -> b -> c) -> b -> a -> c
```

Flip the order of the arguments of a two argument function.

<span id="function-da-internal-prelude-reverse-91564" />

### `reverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverse : [a] -> [a]
```

Reverse a list.

<span id="function-da-internal-prelude-mapa-5250" />

### `mapA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA : Applicative m => (a -> m b) -> [a] -> m [b]
```

Apply an applicative function to each element of a list.

<span id="function-da-internal-prelude-fora-2999" />

### `forA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
forA : Applicative m => [a] -> (a -> m b) -> m [b]
```

`forA` is `mapA` with its arguments flipped.

<span id="function-da-internal-prelude-sequence-43906" />

### `sequence`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sequence : Applicative m => [m a] -> m [a]
```

Perform a list of actions in sequence and collect the results.

<span id="function-da-internal-prelude-eqltlt-62567" />

### `=<<`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
=<< : Action m => (a -> m b) -> m a -> m b
```

`=<<` is `>>=` with its arguments flipped.

<span id="function-da-internal-prelude-concatmap-18810" />

### `concatMap`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
concatMap : (a -> [b]) -> [a] -> [b]
```

Map a function over each element of a list, and concatenate all the results.

<span id="function-da-internal-prelude-replicate-97857" />

### `replicate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replicate : Int -> a -> [a]
```

`replicate i x` gives the list `[x, x, x, ..., x]` with `i` copies of `x`.

<span id="function-da-internal-prelude-take-28256" />

### `take`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
take : Int -> [a] -> [a]
```

Take the first `n` elements of a list.

<span id="function-da-internal-prelude-drop-39374" />

### `drop`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
drop : Int -> [a] -> [a]
```

Drop the first `n` elements of a list.

<span id="function-da-internal-prelude-splitat-62285" />

### `splitAt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitAt : Int -> [a] -> ([a], [a])
```

Split a list at a given index.

<span id="function-da-internal-prelude-takewhile-28496" />

### `takeWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhile : (a -> Bool) -> [a] -> [a]
```

Take elements from a list while the predicate holds.

<span id="function-da-internal-prelude-dropwhile-40350" />

### `dropWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhile : (a -> Bool) -> [a] -> [a]
```

Drop elements from a list while the predicate holds.

<span id="function-da-internal-prelude-span-51013" />

### `span`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
span : (a -> Bool) -> [a] -> ([a], [a])
```

`span p xs` is equivalent to `(takeWhile p xs, dropWhile p xs)`.

<span id="function-da-internal-prelude-partition-74270" />

### `partition`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
partition : (a -> Bool) -> [a] -> ([a], [a])
```

The `partition` function takes a predicate, a list and returns
the pair of lists of elements which do and do not satisfy the
predicate, respectively; i.e.,

> partition p xs == (filter p xs, filter (not . p) xs)

```
>>> partition (<0) [1, -2, -3, 4, -5, 6]
([-2, -3, -5], [1, 4, 6])
```

<span id="function-da-internal-prelude-break-18317" />

### `break`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
break : (a -> Bool) -> [a] -> ([a], [a])
```

Break a list into two, just before the first element where the predicate holds.
`break p xs` is equivalent to `span (not . p) xs`.

<span id="function-da-internal-prelude-lookup-7541" />

### `lookup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookup : Eq a => a -> [(a, b)] -> Optional b
```

Look up the first element with a matching key.

<span id="function-da-internal-prelude-enumerate-9854" />

### `enumerate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
enumerate : (Enum a, Bounded a) => [a]
```

Generate a list containing all values of a given enumeration.

<span id="function-da-internal-prelude-zip-87479" />

### `zip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zip : [a] -> [b] -> [(a, b)]
```

`zip` takes two lists and returns a list of corresponding pairs.
If one list is shorter, the excess elements of the longer list are discarded.

<span id="function-da-internal-prelude-zip3-8569" />

### `zip3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zip3 : [a] -> [b] -> [c] -> [(a, b, c)]
```

`zip3` takes three lists and returns a list of triples, analogous to `zip`.

<span id="function-da-internal-prelude-zipwith-13207" />

### `zipWith`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipWith : (a -> b -> c) -> [a] -> [b] -> [c]
```

`zipWith` takes a function and two lists.
It generalises `zip` by combining elements using the function, instead of forming pairs.
If one list is shorter, the excess elements of the longer list are discarded.

<span id="function-da-internal-prelude-zipwith3-3785" />

### `zipWith3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipWith3 : (a -> b -> c -> d) -> [a] -> [b] -> [c] -> [d]
```

`zipWith3` generalises `zip3` by combining elements using the function, instead of forming triples.

<span id="function-da-internal-prelude-unzip-18278" />

### `unzip`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unzip : [(a, b)] -> ([a], [b])
```

Turn a list of pairs into a pair of lists.

<span id="function-da-internal-prelude-unzip3-67086" />

### `unzip3`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unzip3 : [(a, b, c)] -> ([a], [b], [c])
```

Turn a list of triples into a triple of lists.

<span id="function-da-internal-prelude-traceraw-94102" />

### `traceRaw`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traceRaw : Text -> a -> a
```

`traceRaw msg a` prints `msg` and returns `a`, for debugging purposes.

The default configuration on the participant logs these messages at DEBUG level.

<span id="function-da-internal-prelude-trace-56451" />

### `trace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
trace : Show b => b -> a -> a
```

`trace b a` prints `b` and returns `a`, for debugging purposes.

The default configuration on the participant logs these messages at DEBUG level.

<span id="function-da-internal-prelude-traceid-75962" />

### `traceId`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traceId : Show b => b -> b
```

`traceId a` prints `a` and returns `a`, for debugging purposes.

The default configuration on the participant logs these messages at DEBUG level.

<span id="function-da-internal-prelude-debug-24649" />

### `debug`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
debug : (Show b, Action m) => b -> m ()
```

`debug x` prints `x` for debugging purposes.

The default configuration on the participant logs these messages at DEBUG level.

<span id="function-da-internal-prelude-debugraw-7384" />

### `debugRaw`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
debugRaw : Action m => Text -> m ()
```

`debugRaw msg` prints `msg` for debugging purposes.

The default configuration on the participant logs these messages at DEBUG level.

<span id="function-da-internal-prelude-fst-55341" />

### `fst`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fst : (a, b) -> a
```

Return the first element of a tuple.

<span id="function-da-internal-prelude-snd-88623" />

### `snd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
snd : (a, b) -> b
```

Return the second element of a tuple.

<span id="function-da-internal-prelude-truncate-45759" />

### `truncate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
truncate : Numeric n -> Int
```

`truncate x` rounds `x` toward zero.

<span id="function-da-internal-prelude-inttonumeric-99696" />

### `intToNumeric`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intToNumeric : NumericScale n => Int -> Numeric n
```

Convert an `Int` to a `Numeric`.

<span id="function-da-internal-prelude-inttodecimal-16628" />

### `intToDecimal`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intToDecimal : Int -> Decimal
```

Convert an `Int` to a `Decimal`.

<span id="function-da-internal-prelude-roundbankers-80419" />

### `roundBankers`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
roundBankers : Int -> Numeric n -> Numeric n
```

Bankers' Rounding: `roundBankers dp x` rounds `x` to `dp` decimal places, where a `.5` is rounded to the nearest even digit.

<span id="function-da-internal-prelude-roundcommercial-50292" />

### `roundCommercial`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
roundCommercial : NumericScale n => Int -> Numeric n -> Numeric n
```

Commercial Rounding: `roundCommercial dp x` rounds `x` to `dp` decimal places, where a `.5` is rounded away from zero.

<span id="function-da-internal-prelude-round-17808" />

### `round`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
round : NumericScale n => Numeric n -> Int
```

Round a `Numeric` to the nearest integer, where a `.5` is rounded away from zero.

<span id="function-da-internal-prelude-floor-26810" />

### `floor`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
floor : NumericScale n => Numeric n -> Int
```

Round a `Decimal` down to the nearest integer.

<span id="function-da-internal-prelude-ceiling-19727" />

### `ceiling`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ceiling : NumericScale n => Numeric n -> Int
```

Round a `Decimal` up to the nearest integer.

<span id="function-da-internal-prelude-null-12330" />

### `null`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
null : [a] -> Bool
```

Is the list empty? `null xs` is true if `xs` is the empty list.

<span id="function-da-internal-prelude-filter-41317" />

### `filter`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
filter : (a -> Bool) -> [a] -> [a]
```

Filters the list using the function: keep only the elements where the predicate holds.

<span id="function-da-internal-prelude-sum-46659" />

### `sum`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sum : Additive a => [a] -> a
```

Add together all the elements in the list.

<span id="function-da-internal-prelude-product-15907" />

### `product`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
product : Multiplicative a => [a] -> a
```

Multiply all the elements in the list together.

<span id="function-da-internal-prelude-undefined-12708" />

### `undefined`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
undefined : a
```

A convenience function that can be used to mark something not implemented.
Always throws an error with "Not implemented."

<span id="function-da-internal-template-functions-softfetch-60405" />

### `softFetch`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
softFetch : HasSoftFetch t => ContractId t -> Update t
```

<span id="function-da-internal-template-functions-softexercise-80500" />

### `softExercise`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
softExercise : HasSoftExercise t c r => ContractId t -> c -> Update r
```

<span id="function-da-internal-template-functions-stakeholder-47883" />

### `stakeholder`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stakeholder : (HasSignatory t, HasObserver t) => t -> [Party]
```

The stakeholders of a contract: its signatories and observers.

<span id="function-da-internal-template-functions-maintainer-44226" />

### `maintainer`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maintainer : HasMaintainer t k => k -> [Party]
```

The list of maintainers of a contract key.

<span id="function-da-internal-template-functions-exercisebykey-78695" />

### `exerciseByKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseByKey : HasExerciseByKey t k c r => k -> c -> Update r
```

Exercise a choice on the contract associated with the given key.

You must pass the `t` using an explicit type application. For
instance, if you want to exercise a choice `Withdraw` on a contract of
template `Account` given by its key `k`, you must call
`exerciseByKey @Account k Withdraw`.

<span id="function-da-internal-template-functions-createandexercise-2676" />

### `createAndExercise`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
createAndExercise : (HasCreate t, HasExercise t c r) => t -> c -> Update r
```

Create a contract and exercise the choice on the newly created contract.

<span id="function-da-internal-template-functions-templatetyperep-92004" />

### `templateTypeRep`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
templateTypeRep : HasTemplateTypeRep t => TemplateTypeRep
```

Generate a unique textual representation of the template id.

<span id="function-da-internal-template-functions-toanytemplate-14372" />

### `toAnyTemplate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyTemplate : HasToAnyTemplate t => t -> AnyTemplate
```

Wrap the template in `AnyTemplate`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-fromanytemplate-39771" />

### `fromAnyTemplate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyTemplate : HasFromAnyTemplate t => AnyTemplate -> Optional t
```

Extract the underlying template from `AnyTemplate` if the type matches
or return `None`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-toanychoice-22033" />

### `toAnyChoice`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyChoice : (HasTemplateTypeRep t, HasToAnyChoice t c r) => c -> AnyChoice
```

Wrap a choice in `AnyChoice`.

You must pass the template type `t` using an explicit type application.
For example `toAnyChoice @Account Withdraw`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-fromanychoice-95102" />

### `fromAnyChoice`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyChoice : (HasTemplateTypeRep t, HasFromAnyChoice t c r) => AnyChoice -> Optional c
```

Extract the underlying choice from `AnyChoice` if the template and
choice types match, or return `None`.

You must pass the template type `t` using an explicit type application.
For example `fromAnyChoice @Account choice`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-toanycontractkey-75916" />

### `toAnyContractKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toAnyContractKey : (HasTemplateTypeRep t, HasToAnyContractKey t k) => k -> AnyContractKey
```

Wrap a contract key in `AnyContractKey`.

You must pass the template type `t` using an explicit type application.
For example `toAnyContractKey @Proposal k`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-fromanycontractkey-60533" />

### `fromAnyContractKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromAnyContractKey : (HasTemplateTypeRep t, HasFromAnyContractKey t k) => AnyContractKey -> Optional k
```

Extract the underlying key from `AnyContractKey` if the template and
choice types match, or return `None`.

You must pass the template type `t` using an explicit type application.
For example `fromAnyContractKey @Proposal k`.

Only available for Daml-LF 1.7 or later.

<span id="function-da-internal-template-functions-visiblebykey-51464" />

### `visibleByKey`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
visibleByKey : HasLookupByKey t k => k -> Update Bool
```

True if contract exists, submitter is a stakeholder, and all maintainers
authorize. False if contract does not exist and all maintainers authorize.
Fails otherwise.

## Orphan Typeclass Instances

* `instance Eq a => Eq (Down a)`

* `instance Show a => Show (Down a)`

* `instance Functor Down`

* `instance Functor a`

* `instance Functor []`

* `instance Functor (-> r)`

* `instance Functor (Either e)`

* `instance Ord a => Ord (Down a)`

* `instance Ord TemplateTypeRep`

* `instance Eq Archive`

* `instance Show Archive`

* `instance Eq AnyTemplate`

* `instance Eq AnyChoice`

* `instance Eq AnyContractKey`

* `instance Ord AnyTemplate`

* `instance Ord AnyChoice`

* `instance Ord AnyContractKey`

* `instance Eq TemplateTypeRep`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
