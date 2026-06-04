---
title: "Language Fundamentals"
slug: "appdev-modules-m3-language-fundamentals"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-language-fundamentals.md"
source_title: "Language Fundamentals"
tags:
  - appdev
  - modules
  - m3-language-fundamentals
---

# Language Fundamentals

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Language Fundamentals

> Learn the fundamentals of Daml - a functional programming language designed for smart contracts

## Introduction

In this chapter, you will learn more about expressing complex logic in a functional language like Daml. Specifically, you'll learn about:

* Function signatures and functions
* Advanced control flow (`if...else`, folds, recursion, `when`)

<Note>
  There is a project template `daml-intro-functional-101` for this chapter, containing the code snippets from this section.
</Note>

## The Haskell connection

The previous chapters of this introduction to Daml have mostly covered the structure of templates, and their connection to the Daml Ledger Model. The logic of what happens within the `do` blocks of choices has been kept relatively simple. In this chapter, we will dive deeper into Daml's expression language, the part that allows you to write logic inside those `do` blocks. But we can only scratch the surface here. Daml borrows a lot of its language from [Haskell](https://www.haskell.org). If you want to dive deeper, or learn about specific aspects of the language you can refer to standard literature on Haskell. Some recommendations:

* [Finding Success and Failure in Haskell (Julie Moronuki, Chris Martin)](https://joyofhaskell.com/)
* [Haskell Programming from first principles (Christopher Allen, Julie Moronuki)](http://haskellbook.com/)
* [Learn You a Haskell for Great Good! (Miran Lipovača)](http://learnyouahaskell.com/)
* [Programming in Haskell (Graham Hutton)](http://www.cs.nott.ac.uk/~pszgmh/pih.html)
* [Real World Haskell (Bryan O'Sullivan, Don Stewart, John Goerzen)](http://book.realworldhaskell.org/)

When comparing Daml to Haskell it's worth noting:

* Haskell is a lazy language, which allows you to write things like `head [1..]`, meaning "take the first element of an infinite list". Daml by contrast is strict. Expressions are fully evaluated, which means it is not possible to work with infinite data structures.
* Daml has a `with` syntax for records and a dot syntax for record field access, neither of which is present in Haskell. However, Daml supports Haskell's curly brace record notation.
* Daml has a number of Haskell compiler extensions active by default.
* Daml doesn't support all features of Haskell's type system. For example, there are no existential types or GADTs.
* Actions are called Monads in Haskell.

## Functions

In `data` you learnt about one half of Daml's type system: Data types. It's now time to learn about the other, which are Function types. Function types in Daml can be spotted by looking for `->` which can be read as "maps to".

For example, the function signature `Int -> Int` maps an integer to another integer. There are many such functions, but one would be:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment : Int -> Int
increment n = n + 1
```

You can see here that the function declaration and the function definitions are separate. The declaration can be omitted in cases where the type can be inferred by the compiler, but for top-level functions (ie ones at the same level as templates, directly under a module), it's often a good idea to include them for readability.

In the case of `increment` it could have been omitted. Similarly, we could define a function `add` without a declaration:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add n m = n + m
```

If you do this, and wonder what type the compiler has inferred, you can hover over the function name in the IDE:

```
add
  : Additive a
  => a -> a -> a

Defined at /tmp/daml-intro-9/daml/Main.daml:20:1
add n m = n + m
```

What you see here is a slightly more complex signature:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add : Additive a => a -> a -> a
```

There are two interesting things going on here:

1. We have more than one `->`.
2. We have a type parameter `a` with a constraint `Additive a`.

### Function application

Let's start by looking at the right hand part `a -> a -> a`. The `->` is right associative, meaning `a -> a -> a` is equivalent to `a -> (a -> a)`. Using the "maps to" way of reading `->`, we get "`a` maps to a function that maps `a` to `a`".

And this is indeed what happens. We can define a different version of `increment` by *partially applying* `add`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment2 = add 1
```

If you try this out in your IDE, you'll see that the compiler infers type `Int -> Int` again. It can do so because of the literal `1 : Int`.

So if we have a function `f : a -> b -> c -> d` and a value `valA : a`, we get `f valA : b -> c -> d`, i.e. we can apply the function argument by argument. If we also had `valB : b`, we would have `f valA valB : c -> d`. What this tells you is that function *application* is left associative: `f valA valB == (f valA) valB`.

### Infix functions

Now `add` is clearly just an alias for `+`, but what is `+`? `+` is just a function. It's only special because it starts with a symbol. Functions that start with a symbol are *infix* by default which means they can be written between two arguments. That's why we can write `1 + 2` rather than `+ 1 2`. The rules for converting between normal and infix functions are simple. Wrap an infix function in parentheses to use it as a normal function (i.e. *prefix*), and wrap a normal function in backticks to make it infix:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
three = 1 `add` 2
```

With that knowledge, we could have defined `add` more succinctly as the alias that it is:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add2 : Additive a => a -> a -> a
add2 = (+)
```

If we want to partially apply an infix operation we can also do that as follows:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment3 = (1 +)
double = (* 2)
```

#### Associativity and Precedence

When dealing with multiple infix operators, precedence determines how the Daml compiler should parse an expression. For example, for the expression `x + y * z`, because `\*` has a higher precedence than `+`, the expression is parsed as `x + (y * z)` instead of `(x + y) * z`. When dealing with infix operators with the same precedence, associativity determines how the Daml compiler should parse an expression. For example, because `+` and `-` are left-associative, the expression `x + y - z` is parsed as `(x + y) - z` instead of `x + (y - z)`. For built-in operators this has been predefined, for user-defined operators, it must be user-defined. See the [Daml reference on Fixity, Associativity and Precedence](/appdev/reference/daml-language-reference#fixity-associativity-and-precedence) for details.

### Type constraints

The `Additive a =>` part of the signature of `add` is a type constraint on the type parameter `a`. `Additive` here is a typeclass. You already met typeclasses like `Eq` and `Show` earlier. The `Additive` typeclass says that you can add a thing, i.e. there is a function `(+) : a -> a -> a`. Now the way to read the full signature of `add` is "Given that `a` has an instance for the `Additive` typeclass, `a` maps to a function which maps `a` to `a`".

Typeclasses in Daml are a bit like interfaces in other languages. To be able to add two things using the `+` function, those things need to "expose" (have an instance for) the `Additive` interface (typeclass).

Unlike interfaces, typeclasses can have multiple type parameters. A good example, which also demonstrates the use of multiple constraints at the same time, is the signature of the `exercise` function:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise : (Template t, Choice t c r) => ContractId t -> c -> Update r
```

Let's turn this into prose: Given that `t` is the type of a template, and that `t` has a choice `c` with return type `r`, the `exercise` function maps a `ContractId` for a contract of type `t` to a function that takes the choice arguments of type `c` and returns an `Update` resulting in type `r`.

That's quite a mouthful, and does require one to know what *meaning* the typeclass `Choice` gives to parameters `t` `c` and `r`, but in many cases, that's obvious from the context or names of typeclasses and variables.

Using single letters, while common, is not mandatory. The above may be made a little bit clearer by expanding the type parameter names, at the cost of making the code a bit longer:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise : (Template template, Choice template choice result) =>
             ContractId template -> choice -> Update result
```

### Pattern matching in arguments

You met pattern matching earlier, using `case` expressions which is one way of pattern matching. However, it can also be convenient to do the pattern matching at the level of function arguments. Think about implementing the function `uncurry`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry : (a -> b -> c) -> (a, b) -> c
```

`uncurry` takes a function with two arguments (or more, since `c` could be a function), and turns it into a function from a 2-tuple to `c`. Here are three ways of implementing it, using tuple accessors, `case` pattern matching, and function pattern matching:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry1 f t = f t._1 t._2

uncurry2 f t = case t of
  (x, y) -> f x y

uncurry f (x, y) = f x y
```

Any pattern matching you can do in `case` you can also do at the function level, and the compiler helpfully warns you if you did not cover all cases, which is called "non-exhaustive".

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromSome : Optional a -> a
fromSome (Some x) = x
```

The above will give you a warning:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
warning:
  Pattern match(es) are non-exhaustive
  In an equation for ‘fromSome’: Patterns not matched: None
```

A function that does not cover all its cases, like `fromSome` here, is called a *partial* function. `fromSome None` will cause a runtime error.

We can use function level pattern matching together with a feature called *Record Wildcards* to write the function `issueAsset`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
issueAsset : Asset -> Script (ContractId Asset)
issueAsset asset@(Asset with ..) = do
  assetHolders <- queryFilter @AssetHolder issuer
    (\ah -> (ah.issuer == issuer) && (ah.owner == owner))

  case assetHolders of
    (ahCid, _)::_ -> submit asset.issuer do
      exerciseCmd ahCid Issue_Asset with ..
    [] -> abort ("No AssetHolder found for " <> show asset)
```

The `..` in the pattern match here means bind all fields from the given record to local variables, so we have local variables `issuer`, `owner`, etc.

The `..` in the second to last line means fill all fields of the new record using local variables of the matching names, in this case (per the definition of `Issue_Asset`), `symbol` and `quantity`, taken from the `asset` argument to the function. In other words, this is equivalent to:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseCmd ahCid Issue_Asset with symbol = asset.symbol, quantity = asset.quantity
```

because the notation `asset@(Asset with ..)` binds `asset` to the entire record, while also binding all of the fields of `asset` to local variables.

### Functions everywhere

You have probably already guessed it: Anywhere you can put a value in Daml you can also put a function. Even inside data types:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Predicate a = Predicate with
  test : a -> Bool
```

More often it makes sense to define functions locally, inside a `let` clause or similar. Good examples of this are the `validate` and `transfer` functions defined locally in the `Trade_Settle` choice of the model from `dependencies`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let
          validate (asset, assetCid) = do
            fetchedAsset <- fetch assetCid
            assertMsg
              "Asset mismatch"
              (asset == fetchedAsset with
                observers = asset.observers)

        mapA_ validate (zip baseAssets baseAssetCids)
        mapA_ validate (zip quoteAssets quoteAssetCids)

        let
          transfer (assetCid, approvalCid) = do
            exercise approvalCid TransferApproval_Transfer with assetCid

        transferredBaseCids <- mapA transfer (zip baseAssetCids baseApprovalCids)
        transferredQuoteCids <- mapA transfer (zip quoteAssetCids quoteApprovalCids)
```

You can see that the function signature is inferred from the context here. If you look closely (or hover over the function in the IDE), you'll see that it has signature

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
validate : (HasFetch r, Eq r, HasField "observers" r a) => (r, ContractId r) -> Update ()
```

<Note>
  Bear in mind that functions are not serializable, so you can't use them inside template arguments, as choice inputs, or as choice outputs. They also don't have instances of the `Eq` or `Show` typeclasses which one would commonly want on data types.
</Note>

The `mapA` and `mapA_` functions loop through the lists of assets and approvals, and apply the functions `validate` and `transfer` to each element of those lists, performing the resulting `Update` action in the process. We'll look at that more closely under `loops` below.

### Lambdas

Daml supports inline functions, called "lambda"s. They are defined using the `(\x y z -> ...)` syntax. For example, a lambda version of `increment` would be `(\n -> n + 1)`.

## Control flow

In this section, we will cover branches and loops, and look at a few common patterns of how to translate procedural code into functional code.

### Branches

Until `compose` the only real kind of control flow introduced has been `case`, which is a powerful tool for branching.

#### If-else expression

`constraints` also showed a seemingly self-explanatory `if ... else` expression, but didn't explain it further. Let's implement the function `boolToInt : Bool -> Int` which in typical fashion maps `True` to `1` and `False` to `0`. Here is an implementation using `case`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boolToInt b = case b of
  True -> 1
  False -> 0
```

If you write this function in the IDE, you'll get a warning from the linter:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Suggestion: Use if
Found:
case b of
    True -> 1
    False -> 0
Perhaps:
if b then 1 else 0
```

The linter knows the equivalence and suggests a better implementation:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boolToInt2 b = if b
  then 1
  else 0
```

In short: `if ... else` expressions are equivalent to `case` expressions, but can be easier to read.

#### Control flow as expressions

`case` and `if ... else` expressions really are control flow in the sense that they short-circuit:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
doError t = case t of
  "True" -> True
  "False" -> False
  _ -> error ("Not a Bool: " <> t)
```

This function behaves as you would expect: the error only gets evaluated if an invalid text is passed in.

This is different from functions, where all arguments are evaluated immediately:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ifelse b t e = if b then t else e
boom = ifelse True 1 (error "Boom")
```

In the above, `boom` is an error.

While providing proper control flow, `case` and `if ... else` expressions do result in a value when evaluated. You can actually see that in the function definitions above. Since each of the functions is defined just as a `case` or `if ... else` expression, the value of the evaluated function is just the value of the `case` or `if ... else` expression. Values have a type: the `if ... else` expression in `boolToInt2` has type `Int` as that is what the function returns; similarly, the `case` expression in `doError` has type `Bool`. To be able to give such expressions an unambiguous type, each branch needs to have the same type. The below function does not compile as one branch tries to return an `Int` and the other a `Text`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
typeError b = if b
  then 1
  else "a"
```

If we need functions that can return two (or more) types of things we need to encode that in the return type. For two possibilities, it's common to use the `Either` type:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intOrText : Bool -> Either Int Text
intOrText b = if b
  then Left 1
  else Right "a"
```

When you have more than two possible types (and sometimes even just for two types), it can be clearer to define your own variant type to wrap all possibilities.

#### Branches in actions

The most common case where this becomes important is inside `do` blocks. Say we want to create a contract of one type in one case, and of another type in another case. Let's say we have two template types and want to write a function that creates an `S` if a condition is met, and a `T` otherwise.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template T
  with
    p : Party
  where
    signatory p

template S
  with
    p : Party
  where
    signatory p
```

It would be tempting to write a simple `if ... else`, but it won't typecheck if each branch returns a different type:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
typeError b p = if b
  then create T with p
  else create S with p
```

We have two options:

1. Use the `Either` trick from above.
2. Get rid of the return types.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ifThenSElseT1 b p = if b
  then do
    cid <- create S with p
    return (Left cid)
  else do
    cid <- create T with p
    return (Right cid)

ifThenSElseT2 b p = if b
  then do
    create S with p
    return ()
  else do
    create T with p
    return ()
```

The latter is so common that there is a utility function in `DA.Action` to get rid of the return type: `void : Functor f => f a -> f ()`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ifThenSElseT3 b p = if b
  then void (create S with p)
  else void (create T with p)
```

`void` also helps express control flow of the type "Create a `T` only if a condition is met.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conditionalS b p = if b
  then void (create S with p)
  else return ()
```

Note that we still need the `else` clause of the same type `()`. This pattern is so common, it's encapsulated in the standard library function `DA.Action.when : (Applicative f) => Bool -> f () -> f ()`.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conditionalS2 b p = when b (void (create S with p))
```

Despite `when` looking like a simple function, the compiler does some magic so that it short-circuits evaluation just like `if ... else` and `case`. The following `noop` function is a no-op (i.e. "does nothing"), not an error as one might otherwise expect:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
noop : Update () = when False (error "Foo")
```

With `case`, `if ... else`, `void` and `when`, you can express all branching. However, one additional feature you may want to learn is guards. They are not covered here, but can help avoid deeply nested `if ... else` blocks. Here's just one example. The Haskell sources at the beginning of the chapter cover this topic in more depth.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tellSize : Int -> Text
tellSize d
  | d < 0 = "Negative"
  | d == 0 = "Zero"
  | d == 1 = "Non-Zero"
  | d < 10 = "Small"
  | d < 100 = "Big"
  | d < 1000 = "Huge"
  | otherwise = "Enormous"
```

### Loops

Other than branching, the most common form of control flow is looping. Looping is usually used to iteratively modify some state. We'll use JavaScript in this section to illustrate the procedural way of doing things.

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function sum(intArr) {
  var result = 0;
  intArr.forEach (i => {
    result += i;
  });
  return result;
}
```

A more general loop looks like this:

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function whileF(init, cont, step, finalize) {
  var state = init();
  while (cont(state)) {
    state = step(state);
  }
  return finalize(state);
}
```

In both cases, state is being mutated: `result` in the former, `state` in the latter. Values in Daml are immutable, so it needs to work differently. In Daml we will do this with folds and recursion.

#### Folds

Folds correspond to looping with an explicit iterator: `for` and `forEach` loops in procedural languages. The most common iterator is a list, as is the case in the `sum` function above. For such cases, Daml has the `foldl` function. The `l` stands for "left" and means the list is processed from the left. There is also a corresponding `foldr` which processes from the right.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl : (b -> a -> b) -> b -> [a] -> b
```

Let's give the type parameters semantic names. `b` is the state, `a` is an item. `foldl`s first argument is a function which takes a state and an item, and returns a new state. That's the equivalent of the inner block of the `forEach`. It then takes a state, which is the initial state, and a list of items, which is the iterator. The result is again a state. The `sum` function above can be translated to Daml almost instantly with those correspondences in mind:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sum ints = foldl (+) 0 ints
```

If we wanted to be more verbose, we could replace `(+)` with a lambda `(\result i -> result + i)` which makes the correspondence to `result += i` from the JavaScript clearer.

Almost all loops with explicit iterators can be translated to folds, though we have to take a bit of care with performance when it comes to translating `for` loops:

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function sumArrs(arr1, arr2) {
  var l = min (arr1.length, arr2.length);
  var result = new int[l];
  for(var i = 0; i < l; i++) {
    result[i] = arr1[i] + arr2[i];
  }
  return result;
}
```

Translating the `for` into a `forEach` is easy if you can get your hands on an array containing values `[0..(l-1)]`. And that's how you do it in Daml, using *ranges*. `[0..(l-1)]` is shorthand for `enumFromTo 0 (l-1)`, which returns the list you'd expect.

Daml also has an operator `(!!) : [a] -> Int -> a` which returns an element in a list. You may now be tempted to write `sumArrs` like this:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs : [Int] -> [Int] -> [Int]
sumArrs arr1 arr2 =
  let l = min (length arr1) (length arr2)
      sumAtI i = (arr1 !! i) + (arr2 !! i)
   in foldl (\state i -> (sumAtI i) :: state) [] [1..(l-1)]
```

Unfortunately, that's not a very good approach. Lists in Daml are linked lists, which makes access using `(!!)` too slow for this kind of iteration. A better approach in Daml is to get rid of the `i` altogether and instead merge the lists first using the `zip` function, and then iterate over the "zipped" up lists:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs2 arr1 arr2 = foldl (\state (x, y) -> (x + y) :: state) [] (zip arr1 arr2)
```

`zip : [a] -> [b] -> [(a, b)]` takes two lists, and merges them into a single list where the first element is the 2-tuple containing the first element of the two input lists, and so on. It drops any left-over elements of the longer list, thus making the `min` logic unnecessary.

#### Maps

In effect, the lambda passed to `foldl` only "wants" to act on a single element of the (zipped-up) input list, but still has to manage the concatenation of the whole state. Acting on each element separately is a common-enough pattern that there is a specialized function for it: `map : (a -> b) -> [a] -> [b]`. Using it, we can rewrite `sumArr` to:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs3 arr1 arr2 = map (\(x, y) -> (x + y)) (zip arr1 arr2)
```

As a rule, use `map` if the result has the same shape as the input and you don't need to carry state from one iteration to the next. Use folds if you need to accumulate state in any way.

#### Recursion

If there is no explicit iterator, you can use recursion. Let's try to write a function that reverses a list, for example. We want to avoid `(!!)` so there is no sensible iterator here. Instead, we use recursion:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverseWorker rev rem = case rem of
  [] -> rev
  x::xs -> reverseWorker (x::rev) xs
reverse xs = reverseWorker [] xs
```

You may be tempted to make `reverseWorker` a local definition inside `reverse`, but Daml only supports recursion for top-level functions so the recursive part `recurseWorker` has to be its own top-level function.

#### Folds and maps in action contexts

The folds and `map` function above are pure in the sense introduced earlier: The functions used to map or process items have no side effects. If you have looked at the multi-package models, you'll have noticed `mapA`, `mapA_`, and `forA`, which seem to serve a similar role but within `Action`s . A good example is the `mapA` call in the `testMultiTrade` script:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let rels =
        [ Relationship chfbank alice
        , Relationship chfbank bob
        , Relationship gbpbank alice
        , Relationship gbpbank bob
        ]
  [chfha, chfhb, gbpha, gbphb] <- mapA setupRelationship rels
```

Here we have a list of relationships (type `[Relationship]`) and a function `setupRelationship : Relationship -> Script (ContractId AssetHolder)`. We want the `AssetHolder` contracts for those relationships, i.e. something of type `[ContractId AssetHolder]`. Using the map function almost gets us there, but `map setupRelationship rels` would have type `[Update (ContractId AssetHolder)]`. This is a list of `Update` actions, each resulting in a `ContractId AssetHolder`. What we need is an `Update` action resulting in a `[ContractId AssetHolder]`. The list and `Update` are nested the wrong way around for our purposes.

Intuitively, it's clear how to fix this: we want the compound action consisting of performing each of the actions in the list in turn. There's a function for that: `sequence : : Applicative m => [m a] -> m [a]`. It implements that intuition and allows us to "take the `Update` out of the list", so to speak. So we could write `sequence (map setupRelationship rels)`. This is so common that it's encapsulated in the `mapA` function, a possible implementation of which is

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA f xs = sequence (map f xs)
```

The `A` in `mapA` stands for "Action", and you'll find that many functions that have something to do with "looping" have an `A` equivalent. The most fundamental of all of these is `foldlA : Action m => (b -> a -> m b) -> b -> [a] -> m b`, a left fold with side effects. Here the inner function has a side-effect indicated by the `m` so the end result `m b` also has a side effect: the sum of all the side effects of the inner function.

To improve your familiarity with these concepts, try implementing `foldlA` in terms of `foldl`, as well as `sequence` and `mapA` in terms of `foldlA`. Here is one set of possible implementations:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldlA2 fn init xs =
  let
    work accA x = do
      acc <- accA
      fn acc x
   in foldl work (pure init) xs

mapA2 fn [] = pure []
mapA2 fn (x :: xs) = do
  y <- fn x
  ys <- mapA2 fn xs
  return (y :: ys)

sequence2 [] = pure []
sequence2 (x :: xs) = do
  y <- x
  ys <- sequence2 xs
  return (y :: ys)
```

`forA` is just `mapA` with its arguments reversed. This is useful for readability if the list of items is already in a variable, but the function is a lengthy lambda.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
[usdCid, chfCid] <- forA [usdCid, chfCid] (\cid -> submit alice do
    exerciseCmd cid SetObservers with
      newObservers = [bob]
    )
```

Lastly, you'll have noticed that in some cases we used `mapA_`, not `mapA`. The underscore indicates that the result is not used, so `mapA_ fn xs fn == void (mapA fn xs)`. The Daml Linter will alert you if you could use `mapA_` instead of `mapA`, and similarly for `forA_`.

## Next up

You now know the basics of functions and control flow, both in pure and Action contexts. The multi-package example shows just how much can be done with just the tools you have encountered here, but there are many more tools at your disposal in the Daml standard library, which provides functions and typeclasses for many common circumstances.

{/* COPIED_START source="docs-website:docs/replicated/daml/3.4/sdk/tutorials/smart-contracts/data.rst" hash="22bd66ce" */}

# Data types

In `contracts`, you learnt about contract templates, which specify the types of contracts that can be created on the ledger, and what data those contracts hold in their arguments.

In `daml-scripts`, you learnt about the script view in Daml Studio, which displays the current ledger state. It shows one table per template, with one row per contract of that type and one column per field in the arguments.

This actually provides a useful way of thinking about templates: like tables in databases. Templates specify a data schema for the ledger:

* each template corresponds to a table
* each field in the `with` block of a template corresponds to a column in that table
* each contract of that type corresponds to a table row

In this section, you'll learn how to create rich data schemas for your ledger. Specifically you'll learn about:

* Daml's built-in and native data types
* Record types
* Derivation of standard properties
* Variants
* Data manipulation
* Contract manipulation

After this section, you should be able to use a Daml ledger as a simple database where individual parties can write, read, and delete complex data.

<Tip>
  Remember that you can load all the code for this section into a folder called `intro-data` by running `dpm new intro-data  --template daml-intro-data`
</Tip>

## Native types

You have already encountered a few native Daml types: `Party` in `contracts`, and `Text` and `ContractId` in `daml-scripts`. Here are those native types and more:

* `Party` Stores the identity of an entity that is able to act on the ledger, in the sense that they can sign contracts and submit transactions. In general, `Party` is opaque.
* `Text` Stores a unicode character string like `"Alice"`.
* `ContractId a` Stores a reference to a contract of type `a`.
* `Int` Stores signed 64-bit integers. For example, `-123`.
* `Decimal` Stores fixed-point number with 28 digits before and 10 digits after the decimal point. For example, `0.0000000001` or `-9999999999999999999999999999.9999999999`.
* `Bool` Stores `True` or `False`.
* `Date` Stores a date.
* `Time` Stores absolute UTC time.
* `RelTime` Stores a difference in time.

The below script instantiates each one of these types, manipulates it where appropriate, and tests the result:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Native.daml
-- [Include actual code example here]
```

Despite its simplicity, there are quite a few things to note in this script:

* The `import` statements at the top import two packages from the Daml standard library, which contain all the date and time related functions we use here as well as the functions used in Daml Scripts. More on packages, imports and the standard library later.

* Most of the variables are declared inside a `let` block.

  That's because the `script do` block expects script actions like `submit` or `allocateParty`. An integer like `123` is not an action, it's a pure expression, something we can evaluate without any ledger. You can think of the `let` as turning variable declaration into an action.

* Most variables do not have annotations to say what type they are.

  That's because Daml is very good at *inferring* types. The compiler knows that `123` is an `Int`, so if you declare `my_int = 123`, it can infer that `my_int` is also an `Int`. This means you don't have to write the type annotation `my_int : Int = 123`.

  However, if the type is ambiguous so that the compiler can't infer it, you do have to add a type annotation. This is the case for `0.001` which could be any `Numeric n`. Here we specify `0.001 : Decimal` which is a synonym for `Numeric 10`. You can always choose to add type annotations to aid readability.

* The `assert` function is an action that takes a boolean value and succeeds with `True` and fails with `False`.

  Try putting `assert False` somewhere in a script and see what happens to the script result.

With templates and these native types, it's already possible to write a schema akin to a table in a relational database. Below, `Token` is extended into a simple `CashBalance`, administered by a party in the role of an accountant:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Native.daml
-- [Include actual code example here]
```

## Assemble types

There's quite a lot of information on the `CashBalance` above and it would be nice to be able to give that data more structure. Fortunately, Daml's type system has a number of ways to assemble these native types into much more expressive structures.

### Tuples

A common task is to group values in a generic way. Take, for example, a key-value pair with a `Text` key and an `Int` value. In Daml, you could use a two-tuple of type `(Text, Int)` to do so. If you wanted to express a coordinate in three dimensions, you could group three `Decimal` values using a three-tuple `(Decimal, Decimal, Decimal)`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Tuple.daml
-- [Include actual code example here]
```

You can access the data in the tuples using:

* functions `fst`, `snd`, `fst3`, `snd3`, `thd3`
* a dot-syntax with field names `_1`, `_2`, `_3`, etc.

Daml supports tuples with up to 20 elements, but accessor functions like `fst` are only included for 2- and 3-tuples.

### Lists

Lists in Daml take a single type parameter defining the type of thing in the list. So you can have a list of integers `[Int]` or a list of strings `[Text]`, but not a list mixing integers and strings.

That's because Daml is statically and strongly typed. When you get an element out of a list, the compiler needs to know what type that element has.

The below script instantiates a few lists of integers and demonstrates the most important list functions.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/List.daml
-- [Include actual code example here]
```

Note the type annotation on `empty : [Int] = []`. It's necessary because `[]` is ambiguous. It could be a list of integers or of strings, but the compiler needs to know which it is.

### Records

You can think of records as named tuples with named fields. Declare them using the `data` keyword: `data T = C with`, where `T` is the type name and `C` is the data constructor. In practice, it's a good idea to always use the same name for type and data constructor:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Record.daml
-- [Include actual code example here]
```

You'll notice that the syntax to declare records is very similar to the syntax used to declare templates. That's no accident because a template is really just a special record. When you write `template Token with`, one of the things that happens in the background is that this becomes a `data Token = Token with`.

In the `assert` statements above, we always compared values of in-built types. If you wrote `assert (my_record == my_record)` in the script, you may be surprised to get an error message `No instance for (Eq MyRecord) arising from a use of ‘==’`. Equality in Daml is always value equality and we haven't written a function to check value equality for `MyRecord` values. But don't worry, you don't have to implement this rather obvious function yourself. The compiler is smart enough to do it for you, if you use `deriving (Eq)`:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Record.daml
-- [Include actual code example here]
```

`Eq` is what is called a *typeclass*. You can think of a typeclass as being like an interface in other languages: it is the mechanism by which you can define a set of functions (for example, `==` and `/=` in the case of `Eq`) to work on multiple types, with a specific implementation for each type they can apply to.

There are some other typeclasses that the compiler can derive automatically. Most prominently, `Show` to get access to the function `show` (equivalent to `toString` in many languages) and `Ord`, which gives access to comparison operators `<`, `>`, `<=`, `>=`.

It's a good idea to always derive `Eq` and `Show` using `deriving (Eq, Show)`. The record types created using `template T with` do this automatically, and the native types have appropriate typeclass instances. For example, `Int` derives `Eq`, `Show`, and `Ord`. As another example, `ContractId a` derives `Eq` and `Show`.

Records can give the data on `CashBalance` a bit more structure:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Record.daml
-- [Include actual code example here]
```

If you look at the resulting script view, you'll see that this still gives rise to one table. The records are expanded out into columns using dot notation.

### Variants and pattern matching

Suppose now that you also wanted to keep track of cash in hand. Cash in hand doesn't have a bank, but you can't just leave `bank` empty. Daml doesn't have an equivalent to `null`. Variants can express that cash can either be in hand or at a bank:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Variants.daml
-- [Include actual code example here]
```

The way to read the declaration of `Location` is "*A Location either has value* `InHand` *OR has a value* `InAccount a` *where* `a` *is of type Account*". This is quite an explicit way to say that there may or may not be an `Account` associated with a `CashBalance` and gives both cases suggestive names.

Another option is to use the built-in `Optional` type. The `None` value of type `Optional a` is the closest Daml has to a `null` value:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Variants.daml
-- [Include actual code example here]
```

Variant types where none of the data constructors take a parameter are called enums:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Variants.daml
-- [Include actual code example here]
```

To access the data in variants, you need to distinguish the different possible cases. For example, you can no longer access the account number of a `Location` directly, because if it is `InHand`, there may be no account number.

To do this, you can use *pattern matching* and either throw errors or return compatible types for all cases:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Variants.daml
-- [Include actual code example here]
```

## Manipulate data

You've got all the ingredients to build rich types expressing the data you want to be able to write to the ledger, and you have seen how to create new values and read fields from values. But how do you manipulate values once created?

All data in Daml is immutable, meaning once a value is created, it will never change. Rather than changing values, you create new values based on old ones with some changes applied:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/Record.daml
-- [Include actual code example here]
```

`changed_record` and `better_changed_record` are each a copy of `eq_record` with the field `my_int` changed. `better_changed_record` shows the recommended way to change fields on a record. The syntax is almost the same as for a new record, but the record name is replaced with the old value: `eq_record with` instead of `EqRecord with`. The `with` block no longer needs to give values to all fields of `EqRecord`. Any missing fields are taken from `eq_record`.

Throughout the script, `eq_record` never changes. The expression `"Zero" :: eq_record.my_list` doesn't change the list in-place, but creates a new list, which is `eq_record.my_list` with an extra element in the beginning.

## Manipulate contracts

Daml's type system allows you to store structured data within Daml contracts. Like records and other data structures, contracts are immutable. They can only be created and archived. If you need to change a contract, you must archive the original contract and create a new one with the updated data.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/ContractManipulation.daml
-- [Include actual code example here]
```

The script above uses `archiveCmd` and `createCmd` to modify a contract of type `Account` in the same transaction. This process creates a new contract, and a new, distinct contract ID, as shown by `newAccountCid =/= accountCid`

When you modify a contract, by archiving it and creating a new one, you generate a new contract ID. That makes contract IDs unstable, and it can cause stale references.

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
-- Code from: daml/daml-intro-data/daml/ContractManipulation.daml
-- [Include actual code example here]
```

In the script above, the `ContractId` in `balance.account` still refers to the archived contract. Consequently, querying the `balance.account` fails and returns `None`.

## Next up

You can now define data schemas for the ledger, read, write, and delete data from the ledger.

In `choices` you'll learn how to define data transformations and give other parties the right to manipulate data in restricted ways.

## Standard library

For an overview of the Prelude, important types from the standard library, and how to search the library, see [The Daml Standard Library](/appdev/modules/m3-standard-library).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
