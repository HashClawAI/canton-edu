---
title: "DA.List"
slug: "appdev-reference-daml-standard-library-da-list"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-list.md"
source_title: "DA.List"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-list
---

# DA.List

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.List

> Reference documentation for Daml module DA.List.

<span id="module-da-list-85985" />

# DA.List

List

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

## Functions

<span id="function-da-list-sort-96399" />

### `sort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sort : Ord a => [a] -> [a]
```

The `sort` function implements a stable sorting algorithm. It is
a special case of `sortBy`, which allows the programmer to supply
their own comparison function.

Elements are arranged from lowest to highest, keeping duplicates in
the order they appeared in the input (a stable sort).

<span id="function-da-list-sortby-71202" />

### `sortBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortBy : (a -> a -> Ordering) -> [a] -> [a]
```

The `sortBy` function is the non-overloaded version of `sort`.

<span id="function-da-list-minimumby-84625" />

### `minimumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumBy : (a -> a -> Ordering) -> [a] -> a
```

`minimumBy f xs` returns the first element `x` of `xs` for which `f x y`
is either `LT` or `EQ` for all other `y` in `xs`. `xs` must be non-empty.

<span id="function-da-list-maximumby-22187" />

### `maximumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumBy : (a -> a -> Ordering) -> [a] -> a
```

`maximumBy f xs` returns the first element `x` of `xs` for which `f x y`
is either `GT` or `EQ` for all other `y` in `xs`. `xs` must be non-empty.

<span id="function-da-list-sorton-99758" />

### `sortOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortOn : Ord k => (a -> k) -> [a] -> [a]
```

Sort a list by comparing the results of a key function applied to
each element. `sortOn f` is equivalent to `sortBy (comparing f)`,
but has the performance advantage of only evaluating `f` once for
each element in the input list. This is sometimes called the
decorate-sort-undecorate paradigm.

Elements are arranged from from lowest to highest, keeping
duplicates in the order they appeared in the input.

<span id="function-da-list-minimumon-90785" />

### `minimumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumOn : Ord k => (a -> k) -> [a] -> a
```

`minimumOn f xs` returns the first element `x` of `xs` for which `f x`
is smaller than or equal to any other `f y` for `y` in `xs`. `xs` must be
non-empty.

<span id="function-da-list-maximumon-98335" />

### `maximumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumOn : Ord k => (a -> k) -> [a] -> a
```

`maximumOn f xs` returns the first element `x` of `xs` for which `f x`
is greater than or equal to any other `f y` for `y` in `xs`. `xs` must be
non-empty.

<span id="function-da-list-mergeby-31951" />

### `mergeBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mergeBy : (a -> a -> Ordering) -> [a] -> [a] -> [a]
```

Merge two sorted lists using into a single, sorted whole, allowing
the programmer to specify the comparison function.

<span id="function-da-list-combinepairs-8661" />

### `combinePairs`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
combinePairs : (a -> a -> a) -> [a] -> [a]
```

Combine elements pairwise by means of a programmer supplied
function from two list inputs into a single list.

<span id="function-da-list-foldbalanced1-46720" />

### `foldBalanced1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldBalanced1 : (a -> a -> a) -> [a] -> a
```

Fold a non-empty list in a balanced way. Balanced means that each
element has approximately the same depth in the operator
tree. Approximately the same depth means that the difference
between maximum and minimum depth is at most 1. The accumulation
operation must be associative and commutative in order to get the
same result as `foldl1` or `foldr1`.

<span id="function-da-list-group-62411" />

### `group`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
group : Eq a => [a] -> [[a]]
```

The 'group' function groups equal elements into sublists such
that the concatenation of the result is equal to the argument.

<span id="function-da-list-groupby-62666" />

### `groupBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
groupBy : (a -> a -> Bool) -> [a] -> [[a]]
```

The 'groupBy' function is the non-overloaded version of 'group'.

<span id="function-da-list-groupon-4918" />

### `groupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
groupOn : Eq k => (a -> k) -> [a] -> [[a]]
```

Similar to 'group', except that the equality is done on an
extracted value.

<span id="function-da-list-dedup-27230" />

### `dedup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedup : Ord a => [a] -> [a]
```

`dedup l` removes duplicate elements from a list. In particular,
it keeps only the first occurrence of each element. It is a
special case of `dedupBy`, which allows the programmer to supply
their own equality test.
`dedup` is called `nub` in Haskell.

<span id="function-da-list-dedupby-29335" />

### `dedupBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupBy : (a -> a -> Ordering) -> [a] -> [a]
```

A version of `dedup` with a custom predicate.

<span id="function-da-list-dedupon-81495" />

### `dedupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOn : Ord k => (a -> k) -> [a] -> [a]
```

A version of `dedup` where deduplication is done
after applyng function. Example use: `dedupOn (.employeeNo) employees`

<span id="function-da-list-dedupsort-78698" />

### `dedupSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSort : Ord a => [a] -> [a]
```

The `dedupSort` function sorts and removes duplicate elements from a
list. In particular, it keeps only the first occurrence of each
element.

<span id="function-da-list-dedupsortby-97595" />

### `dedupSortBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSortBy : (a -> a -> Ordering) -> [a] -> [a]
```

A version of `dedupSort` with a custom predicate.

<span id="function-da-list-unique-23008" />

### `unique`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unique : Ord a => [a] -> Bool
```

Returns True if and only if there are no duplicate elements in the given list.

<span id="function-da-list-uniqueby-86149" />

### `uniqueBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueBy : (a -> a -> Ordering) -> [a] -> Bool
```

A version of `unique` with a custom predicate.

<span id="function-da-list-uniqueon-39349" />

### `uniqueOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueOn : Ord k => (a -> k) -> [a] -> Bool
```

Returns True if and only if there are no duplicate elements in the given list
after applyng function. Example use: `assert $ uniqueOn (.employeeNo) employees`

<span id="function-da-list-replace-72492" />

### `replace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replace : Eq a => [a] -> [a] -> [a] -> [a]
```

Given a list and a replacement list, replaces each occurance of
the search list with the replacement list in the operation list.

<span id="function-da-list-dropprefix-26566" />

### `dropPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropPrefix : Eq a => [a] -> [a] -> [a]
```

Drops the given prefix from a list. It returns the original
sequence if the sequence doesn't start with the given prefix.

<span id="function-da-list-dropsuffix-41813" />

### `dropSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropSuffix : Eq a => [a] -> [a] -> [a]
```

Drops the given suffix from a list. It returns the original
sequence if the sequence doesn't end with the given suffix.

<span id="function-da-list-stripprefix-65866" />

### `stripPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripPrefix : Eq a => [a] -> [a] -> Optional [a]
```

The `stripPrefix` function drops the given prefix from a list.
It returns `None` if the list did not start with the prefix
given, or `Some` the list after the prefix, if it does.

<span id="function-da-list-stripsuffix-23153" />

### `stripSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripSuffix : Eq a => [a] -> [a] -> Optional [a]
```

Return the prefix of the second list if its suffix matches the
entire first list.

<span id="function-da-list-stripinfix-68205" />

### `stripInfix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripInfix : Eq a => [a] -> [a] -> Optional ([a], [a])
```

Return the string before and after the search string or `None`
if the search string is not found.

```
>>> stripInfix [0,0] [1,0,0,2,0,0,3]
Some ([1], [2,0,0,3])

>>> stripInfix [0,0] [1,2,0,4,5]
None
```

<span id="function-da-list-isprefixof-27346" />

### `isPrefixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isPrefixOf : Eq a => [a] -> [a] -> Bool
```

The `isPrefixOf` function takes two lists and returns `True` if
and only if the first is a prefix of the second.

<span id="function-da-list-issuffixof-26645" />

### `isSuffixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSuffixOf : Eq a => [a] -> [a] -> Bool
```

The `isSuffixOf` function takes two lists and returns `True` if
and only if the first list is a suffix of the second.

<span id="function-da-list-isinfixof-7159" />

### `isInfixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isInfixOf : Eq a => [a] -> [a] -> Bool
```

The `isInfixOf` function takes two lists and returns `True` if
and only if the first list is contained anywhere within the second.

<span id="function-da-list-mapaccuml-18387" />

### `mapAccumL`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapAccumL : (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
```

The `mapAccumL` function combines the behaviours of `map` and
`foldl`; it applies a function to each element of a list, passing
an accumulating parameter from left to right, and returning a final
value of this accumulator together with the new list.

<span id="function-da-list-mapwithindex-75685" />

### `mapWithIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapWithIndex : (Int -> a -> b) -> [a] -> [b]
```

A generalisation of `map`, `mapWithIndex` takes a mapping
function that also depends on the element's index, and applies it to every
element in the sequence.

<span id="function-da-list-inits-75071" />

### `inits`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
inits : [a] -> [[a]]
```

The `inits` function returns all initial segments of the argument,
shortest first.

<span id="function-da-list-intersperse-31314" />

### `intersperse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intersperse : a -> [a] -> [a]
```

The `intersperse` function takes an element and a list and
"intersperses" that element between the elements of the list.

<span id="function-da-list-intercalate-85238" />

### `intercalate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intercalate : [a] -> [[a]] -> [a]
```

`intercalate` inserts the list `xs` in between the lists in `xss`
and concatenates the result.

<span id="function-da-list-tails-57647" />

### `tails`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tails : [a] -> [[a]]
```

The `tails` function returns all final segments of the argument,
longest first.

<span id="function-da-list-dropwhileend-92606" />

### `dropWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhileEnd : (a -> Bool) -> [a] -> [a]
```

A version of `dropWhile` operating from the end.

<span id="function-da-list-takewhileend-40268" />

### `takeWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhileEnd : (a -> Bool) -> [a] -> [a]
```

A version of `takeWhile` operating from the end.

<span id="function-da-list-transpose-84171" />

### `transpose`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
transpose : [[a]] -> [[a]]
```

The `transpose` function transposes the rows and columns of its
argument.

<span id="function-da-list-breakend-41551" />

### `breakEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakEnd : (a -> Bool) -> [a] -> ([a], [a])
```

Break, but from the end.

<span id="function-da-list-breakon-39026" />

### `breakOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakOn : Eq a => [a] -> [a] -> ([a], [a])
```

Find the first instance of `needle` in `haystack`.
The first element of the returned tuple is the prefix of `haystack`
before `needle` is matched. The second is the remainder of
`haystack`, starting with the match.  If you want the remainder
*without* the match, use `stripInfix`.

<span id="function-da-list-breakonend-30980" />

### `breakOnEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakOnEnd : Eq a => [a] -> [a] -> ([a], [a])
```

Similar to `breakOn`, but searches from the end of the
string.

The first element of the returned tuple is the prefix of `haystack`
up to and including the last match of `needle`.  The second is the
remainder of `haystack`, following the match.

<span id="function-da-list-linesby-68954" />

### `linesBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
linesBy : (a -> Bool) -> [a] -> [[a]]
```

A variant of `lines` with a custom test. In particular, if there
is a trailing separator it will be discarded.

<span id="function-da-list-wordsby-74460" />

### `wordsBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wordsBy : (a -> Bool) -> [a] -> [[a]]
```

A variant of `words` with a custom test. In particular, adjacent
separators are discarded, as are leading or trailing separators.

<span id="function-da-list-head-92101" />

### `head`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
head : [a] -> a
```

Extract the first element of a list, which must be non-empty.

<span id="function-da-list-tail-16805" />

### `tail`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tail : [a] -> [a]
```

Extract the elements after the head of a list, which must be
non-empty.

<span id="function-da-list-last-56071" />

### `last`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
last : [a] -> a
```

Extract the last element of a list, which must be finite and
non-empty.

<span id="function-da-list-init-2389" />

### `init`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
init : [a] -> [a]
```

Return all the elements of a list except the last one. The list
must be non-empty.

<span id="function-da-list-foldl1-60813" />

### `foldl1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1 : (a -> a -> a) -> [a] -> a
```

Left associative fold of a list that must be non-empty.

<span id="function-da-list-foldr1-23463" />

### `foldr1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1 : (a -> a -> a) -> [a] -> a
```

Right associative fold of a list that must be non-empty.

<span id="function-da-list-repeatedly-9930" />

### `repeatedly`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
repeatedly : ([a] -> (b, [a])) -> [a] -> [b]
```

Apply some operation repeatedly, producing an element of output
and the remainder of the list.

<span id="function-da-list-chunksof-64138" />

### `chunksOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
chunksOf : Int -> [a] -> [[a]]
```

Splits a list into chunks of length @n\@.
@n@ must be strictly greater than zero.
The last chunk will be shorter than @n@ in case the length of the input is
not divisible by @n\@.

<span id="function-da-list-delete-22340" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Eq a => a -> [a] -> [a]
```

`delete x` removes the first occurrence of `x` from its list argument.
For example,

```
> delete "a" ["b","a","n","a","n","a"]
["b","n","a","n","a"]
```

It is a special case of 'deleteBy', which allows the programmer to
supply their own equality test.

<span id="function-da-list-deleteby-50465" />

### `deleteBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
deleteBy : (a -> a -> Bool) -> a -> [a] -> [a]
```

The 'deleteBy' function behaves like 'delete', but takes a
user-supplied equality predicate.

```
> deleteBy (<=) 4 [1..10]
[1,2,3,5,6,7,8,9,10]
```

<span id="function-da-list-x-54181" />

### `\\`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
\\ : Eq a => [a] -> [a] -> [a]
```

The `\\` function is list difference (non-associative).
In the result of `xs \\ ys`, the first occurrence of each element of
`ys` in turn (if any) has been removed from `xs`.  Thus

```
(xs ++ ys) \\ xs == ys
```

Note this function is *O(n\*m)* given lists of size *n* and *m*.

<span id="function-da-list-singleton-17649" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : a -> [a]
```

Produce a singleton list.

```
>>> singleton True
[True]
```

<span id="function-da-list-bangbang-90127" />

### `!!`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
!! : [a] -> Int -> a
```

List index (subscript) operator, starting from 0.
For example, `xs !! 2` returns the third element in `xs`.
Raises an error if the index is not suitable for the given list.
The function has complexity *O(n)* where *n* is the index given,
unlike in languages such as Java where array indexing is *O(1)*.

<span id="function-da-list-elemindex-4965" />

### `elemIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
elemIndex : Eq a => a -> [a] -> Optional Int
```

Find index of element in given list.
Will return `None` if not found.

<span id="function-da-list-findindex-82181" />

### `findIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
findIndex : (a -> Bool) -> [a] -> Optional Int
```

Find index, given predicate, of first matching element.
Will return `None` if not found.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
