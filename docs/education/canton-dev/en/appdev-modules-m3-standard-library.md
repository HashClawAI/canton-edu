---
title: "The Daml Standard Library"
slug: "appdev-modules-m3-standard-library"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-standard-library.md"
source_title: "The Daml Standard Library"
tags:
  - appdev
  - modules
  - m3-standard-library
---

# The Daml Standard Library

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# The Daml Standard Library

> Tour of the Daml standard library: the Prelude, important types and typeclasses, and how to browse and search the library.

In `data` and `functional-101` you learned how to define your own data types and functions. However, you don't have to implement everything from scratch. Daml comes with the Daml standard library, which contains types, functions, and typeclasses that cover a large range of use cases.

In this chapter, you'll get an overview of the essentials and learn how to browse and search the library to find functions. Being proficient with the standard library will make you considerably more efficient writing Daml code. Specifically, this chapter covers:

* The Prelude
* Important types from the standard library, and associated functions and typeclasses
* Typeclasses
* Important typeclasses like `Functor`, `Foldable`, and `Traversable`
* How to search the standard library

To go in depth on some of these topics, the literature referenced in `haskell-connection` covers them in much greater detail. The standard library typeclasses like `Applicative`, `Foldable`, `Traversable`, `Action` (called `Monad` in Haskell), and many more, are the bread and butter of Haskell programmers.

<Note>
  There is a project template `daml-intro-11` for this chapter, but it only contains a single source file with the code snippets embedded in this section.
</Note>

## The Prelude

You've already used a lot of functions, types, and typeclasses without importing anything. Functions like `create`, `exercise`, and `(==)`, types like `[]`, `(,)`, `Optional`, and typeclasses like `Eq`, `Show`, and `Ord`. These all come from the Prelude. The Prelude is module that gets implicitly imported into every other Daml module and contains both Daml specific machinery as well as the essentials needed to work with the inbuilt types and typeclasses.

## Important types from the Prelude

In addition to the `native-types`, the Prelude defines a number of common types:

### Lists

You've already met lists. Lists have two constructors `[]` and `x :: xs`, the latter of which is "prepend" in the sense that `1 :: [2] == [1, 2]`. In fact `[1,2]` is just syntactical sugar for `1 :: 2 :: []`.

### Tuples

In addition to the 2-tuple you have already seen, the Prelude contains definitions for tuples of size up to 15. Tuples allow you to store mixed data in an ad-hoc fashion. Common use-cases are return values from functions consisting of several pieces or passing around data in folds, as you saw in `folds`. An example of a relatively wide Tuple can be found in the test modules of the `exceptions` project. `Test.Intro.Asset.TradeSetup.tradeSetup` returns the allocated parties and active contracts in a long tuple. `Test.Intro.Asset.MultiTrade.testMultiTrade` puts them back into scope using pattern matching:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Test/Intro/Asset/TradeSetup.daml
-- [Include actual code example here]
```

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Test/Intro/Asset/MultiTrade.daml
-- [Include actual code example here]
```

Tuples, like lists have some syntactic magic. Both the types as well as the constructors for tuples are `(,,,)` where the number of commas determines the arity of the tuple. Type and data constructor can be applied with values inside the brackets, or outside, and partial application is possible:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

<Note>
  While tuples of great lengths are available, it is often advisable to define custom records with named fields for complex structures or long-lived values. Overuse of tuples can harm code readability.
</Note>

### Optional

The `Optional` type represents a value that may be missing. It's the closest thing Daml has to a "nullable" value. `Optional` has two constructors: `Some`, which takes a value, and `None`, which doesn't take a value. In many languages one would write code like this:

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
lookupResult = lookupByKey(k);

if( lookupResult == null) {
  // Do something
} else {
  // Do something else
}
```

In Daml the same thing would be expressed as:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

### Either

`Either` is used in cases where a value should store one of two types. It has two constructors, `Left` and `Right`, each of which take a value of one or the other of the two types. One typical use-case of `Either` is as an extended `Optional` where `Right` takes the role of `Some` and `Left` the role of `None`, but with the ability to store an error value. `Either Text`, for example behaves just like `Optional`, except that values with constructor `Left` have a text associated to them.

<Note>
  As with tuples, it's easy to overuse `Either` and harm readability. Consider writing your own more explicit type instead. For example if you were returning `South a` vs `North b` using your own type over `Either` would make your code clearer.
</Note>

## Typeclasses

You've seen typeclasses in use all the way from `data`. It's now time to look under the hood.

Typeclasses are declared using the `class` keyword:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

This is akin to an interface declaration of an interface with a getter and setter for a quantity. To *implement* this interface, you need to define instances of this typeclass:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-11/daml/Main.daml
-- [Include actual code example here]
```

Typeclasses can have constraints like functions. For example: `class Eq a => Ord a` means "everything that is orderable can also be compared for equality". And that's almost all there's to it.

## Important typeclasses from the Prelude

### Eq

The `Eq` typeclass allows values of a type to be compared for (in)-equality. It makes available two function: `==` and `/=`. Most data types from the standard library have an instance of `Eq`. As you already learned in `data`, you can let the compiler automatically derive instances of `Eq` for you using the `deriving` keyword.

Templates always have an `Eq` instance, and all types stored on a template need to have one.

### Ord

The `Ord` typeclass allows values of a type to be compared for order. It makes available functions: `<`, `>`, `<=`, and `>=`. Most of the inbuilt data types have an instance of `Ord`. Furthermore, types like `List` and `Optional` get an instance of `Ord` if the type they contain has one. You can let the compiler automatically derive instances of `Ord` for you using the `deriving` keyword.

### Show

`Show` indicates that a type can be serialized to `Text`, ie "shown" in a shell. Its key function is `show`, which takes a value and converts it to `Text`. All inbuilt data types have an instance for `Show` and types like `List` and `Optional` get an instance if the type they contain has one. It also supports the `deriving` keyword.

### Functor

Functors are the closest thing to "containers" that Daml has. Whenever you see a type with a single type parameter, you are probably looking at a `Functor`: `[a]`, `Optional a`, `Either Text a`, `Update a`. Functors are things that can be mapped over and as such, the key function of `Functor` is `fmap`, which does generically what the `map` function does for lists.

Other classic examples of Functors are Sets, Maps, Trees, etc.

### Applicative Functor

Applicative Functors are a bit like Actions, which you met in `constraints`, except that you can't use the result of one action as the input to another action. The only important Applicative Functor that isn't an action in Daml is the `Commands` type submitted in a `submit` block in Daml Script. That's why in order to use `do` notation in Daml Script, you have to enable the `ApplicativeDo` language extension.

### Action

Actions were already covered in `constraints`. One way to think of them is as "recipes" for a value, which need to be "executed to get at that value. Actions are always Functors (and Applicative Functors). The intuition for that is simply that `fmap f x` is the recipe in `x` with the extra instruction to apply the pure function `f` to the result.

The really important Actions in Daml are `Update` and `Script`, but there are many others, like `[]`, `Optional`, and `Either a`.

### Semigroup and Monoid

Semigroups and monoids are about binary operations, but in practice, their important use is for `Text` and `[]`, where they allow concatenation using the `{<>}` operator.

### Additive and Multiplicative

Additive and Multiplicative abstract out arithmetic operations, so that `(+)`, `(-)`, `(*)`, and some other functions can be used uniformly between `Decimal` and `Int`.

## Important modules in the standard library

For almost all the types and typeclasses presented above, the standard library contains a module:

* [DA.List](/docs/canton/appdev-reference-daml-standard-library-da-list) for Lists
* [DA.Optional](/docs/canton/appdev-reference-daml-standard-library-da-optional) for `Optional`
* [DA.Tuple](/docs/canton/appdev-reference-daml-standard-library-da-tuple) for Tuples
* [DA.Either](/docs/canton/appdev-reference-daml-standard-library-da-either) for `Either`
* [DA.Functor](/docs/canton/appdev-reference-daml-standard-library-da-functor) for Functors
* [DA.Action](/docs/canton/appdev-reference-daml-standard-library-da-action) for Actions
* [DA.Functor](/docs/canton/appdev-reference-daml-standard-library-da-functor) and [DA.Semigroup](/docs/canton/appdev-reference-daml-standard-library-da-semigroup) for Monoids and Semigroups
* [DA.Text](/docs/canton/appdev-reference-daml-standard-library-da-text) for working with `Text`
* [DA.Time](/docs/canton/appdev-reference-daml-standard-library-da-time) for working with `Time`
* [DA.Date](/docs/canton/appdev-reference-daml-standard-library-da-date) for working with `Date`

You get the idea, the names are fairly descriptive.

Other than the typeclasses defined in Prelude, there are two modules generalizing concepts you've already learned, which are worth knowing about: `Foldable` and `Traversable`. The examples earlier in this module were based on lists, but there are many other possible iterators. This is expressed in two additional typeclasses: [DA.Traversable](/docs/canton/appdev-reference-daml-standard-library-da-traversable) and [DA.Foldable](/docs/canton/appdev-reference-daml-standard-library-da-foldable). For more detail on these concepts, see [Foldable and Traversable on the Haskell wiki](https://wiki.haskell.org/Foldable_and_Traversable).

## Search the standard library

Being able to browse the standard library starting from the [Daml Standard Library reference](/docs/canton/appdev-reference-daml-standard-library-index) is a start, and the module naming helps, but it's not an efficient process for finding out what a function you've encountered does, even less so for finding a function that does a thing you need to do.

Daml has its own version of the [Hoogle](https://hoogle.haskell.org/) search engine: [Daml Hoogle](https://hoogle.daml.com). It offers standard library search both by name and by signature.

### Search for functions by name

Say you come across some functions you haven't seen before, like the ones in the `ensure` clause of the `MultiTrade`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-9/daml/Intro/Asset/MultiTrade.daml
-- [Include actual code example here]
```

You may be able to guess what `not` and `null` do, but try searching those names in the documentation search. Search results from the standard library will show on top. `not`, for example, gives

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
not

 : Bool -> Bool

 Boolean “not”
```

Signature (including type constraints) and description usually give a pretty clear picture of what a function does.

### Search for functions by signature

The other very common use case for the search is that you have some values that you want to do something with, but don't know the standard library function you need. On the `MultiTrade` template we have a list `baseAssets`, and thanks to your ensure clause we know it's non-empty. In the original `Trade` we used `baseAsset.owner` as the signatory. How do you get the first element of this list to extract the `owner` without going through the motions of a complete pattern match using `case`?

The trick is to think about the signature of the function that's needed, and then to search for that signature. In this case, we want a single distinguished element from a list so the signature should be `[a] -> a`. If you search for that, you'll get a whole range of results, but again, standard library results are shown at the top.

Scanning the descriptions, `head` is the obvious choice, as used in the `let` of the `MultiTrade` template.

You may notice that in the search results you also get some hits that don't mention `[]` explicitly. For example:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
fold

  : (Foldable t, Monoid m) => t m -> m

  Combine the elements of a structure using a monoid.
```

The reason is that there is an instance for `Foldable [a]`.

Let's try another search. Suppose you didn't want the first element, but the one at index `n`. Remember that `(!!)` operator from `functional-101`? There are now two possible signatures we could search for: `[a] -> Int -> a` and `Int -> [a] -> a`. Try searching for both. You'll see that the search returns `(!!)` in both cases. You don't have to worry about the order of arguments.

## Next up

In the following section, you'll find options for testing and interacting with Daml code. We also talk about the operational semantics of some keywords and their commonly associated failures, and a little bit about how coverage reports work in Daml testing.

{/* Mintlify preview rebuild marker. */}

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
