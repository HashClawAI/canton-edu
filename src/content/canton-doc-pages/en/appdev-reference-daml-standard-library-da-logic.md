---
title: "DA.Logic"
slug: "appdev-reference-daml-standard-library-da-logic"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-logic.md"
source_title: "DA.Logic"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-logic
---

# DA.Logic

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Logic

> Reference documentation for Daml module DA.Logic.

<span id="module-da-logic-59184" />

# DA.Logic

Logic -  Propositional calculus.

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

<span id="type-da-logic-types-formula-34794" />

### `data Formula t`

A `Formula t` is a formula in propositional calculus with
propositions of type t.

Constructors:

<span id="constr-da-logic-types-proposition-6173" />

* `Proposition t`
  `Proposition p` is the formula p

<span id="constr-da-logic-types-negation-48969" />

* `Negation (Formula t)`
  For a formula f, `Negation f` is ¬f

<span id="constr-da-logic-types-conjunction-51637" />

* `Conjunction [Formula t]`
  For formulas f1, ..., fn, `Conjunction [f1, ..., fn]` is f1 ∧ ... ∧ fn

<span id="constr-da-logic-types-disjunction-65549" />

* `Disjunction [Formula t]`
  For formulas f1, ..., fn, `Disjunction [f1, ..., fn]` is f1 ∨ ... ∨ fn

Instances:

* `instance Action Formula`
* `instance Applicative Formula`
* `instance Functor Formula`
* `instance Eq t => Eq (Formula t)`
* `instance Ord t => Ord (Formula t)`
* `instance Show t => Show (Formula t)`

## Functions

<span id="function-da-logic-ampampamp-55265" />

### `&&&`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
&&& : Formula t -> Formula t -> Formula t
```

`&&&` is the ∧ operation of the boolean algebra of formulas, to
be read as "and"

<span id="function-da-logic-pipepipepipe-30747" />

### `|||`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
||| : Formula t -> Formula t -> Formula t
```

`|||` is the ∨ operation of the boolean algebra of formulas, to
be read as "or"

<span id="function-da-logic-true-31438" />

### `true`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
true : Formula t
```

`true` is the 1 element of the boolean algebra of formulas,
represented as an empty conjunction.

<span id="function-da-logic-false-99028" />

### `false`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
false : Formula t
```

`false` is the 0 element of the boolean algebra of formulas,
represented as an empty disjunction.

<span id="function-da-logic-neg-1597" />

### `neg`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
neg : Formula t -> Formula t
```

`neg` is the ¬ (negation) operation of the boolean algebra of
formulas.

<span id="function-da-logic-conj-82504" />

### `conj`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conj : [Formula t] -> Formula t
```

`conj` is a list version of `&&&`, enabled by the associativity
of ∧.

<span id="function-da-logic-disj-92448" />

### `disj`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
disj : [Formula t] -> Formula t
```

`disj` is a list version of `|||`, enabled by the associativity
of ∨.

<span id="function-da-logic-frombool-36630" />

### `fromBool`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromBool : Bool -> Formula t
```

`fromBool` converts `True` to `true` and `False` to `false`.

<span id="function-da-logic-tonnf-87354" />

### `toNNF`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toNNF : Formula t -> Formula t
```

`toNNF` transforms a formula to negation normal form
(see [https://en.wikipedia.org/wiki/Negation\_normal\_form](https://en.wikipedia.org/wiki/Negation_normal_form)).

<span id="function-da-logic-todnf-90852" />

### `toDNF`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toDNF : Formula t -> Formula t
```

`toDNF` turns a formula into disjunctive normal form.
(see [https://en.wikipedia.org/wiki/Disjunctive\_normal\_form](https://en.wikipedia.org/wiki/Disjunctive_normal_form)).

<span id="function-da-logic-traverse-17816" />

### `traverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
traverse : Applicative f => (t -> f s) -> Formula t -> f (Formula s)
```

An implementation of `traverse` in the usual sense.

<span id="function-da-logic-zipformulas-28999" />

### `zipFormulas`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
zipFormulas : Formula t -> Formula s -> Formula (t, s)
```

`zipFormulas` takes to formulas of same shape, meaning only
propositions are different and zips them up.

<span id="function-da-logic-substitute-65872" />

### `substitute`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substitute : (t -> Optional Bool) -> Formula t -> Formula t
```

`substitute` takes a truth assignment and substitutes `True` or
`False` into the respective places in a formula.

<span id="function-da-logic-reduce-40218" />

### `reduce`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reduce : Formula t -> Formula t
```

`reduce` reduces a formula as far as possible by:

1. Removing any occurrences of `true` and `false`;
2. Removing directly nested Conjunctions and Disjunctions;
3. Going to negation normal form.

<span id="function-da-logic-isbool-80820" />

### `isBool`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isBool : Formula t -> Optional Bool
```

`isBool` attempts to convert a formula to a bool. It satisfies
`isBool true == Some True` and `isBool false == Some False`.
Otherwise, it returns `None`.

<span id="function-da-logic-interpret-88386" />

### `interpret`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interpret : (t -> Optional Bool) -> Formula t -> Either (Formula t) Bool
```

`interpret` is a version of `toBool` that first substitutes using
a truth function and then reduces as far as possible.

<span id="function-da-logic-substitutea-61566" />

### `substituteA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substituteA : Applicative f => (t -> f (Optional Bool)) -> Formula t -> f (Formula t)
```

`substituteA` is a version of `substitute` that allows for truth
values to be obtained from an action.

<span id="function-da-logic-interpreta-14928" />

### `interpretA`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interpretA : Applicative f => (t -> f (Optional Bool)) -> Formula t -> f (Either (Formula t) Bool)
```

`interpretA` is a version of `interpret` that allows for truth
values to be obtained form an action.

## Orphan Typeclass Instances

* `instance Eq t => Eq (Formula t)`

* `instance Ord t => Ord (Formula t)`

* `instance Show t => Show (Formula t)`

* `instance Functor Formula`

* `instance Applicative Formula`

* `instance Action Formula`

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
