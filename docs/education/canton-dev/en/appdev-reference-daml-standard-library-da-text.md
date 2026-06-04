---
title: "DA.Text"
slug: "appdev-reference-daml-standard-library-da-text"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/reference/daml-standard-library/da-text.md"
source_title: "DA.Text"
tags:
  - appdev
  - reference
  - daml-standard-library
  - da-text
---

# DA.Text

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# DA.Text

> Reference documentation for Daml module DA.Text.

<span id="module-da-text-83238" />

# DA.Text

Functions for working with Text.

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

<span id="function-da-text-explode-24206" />

### `explode`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
explode : Text -> [Text]
```

<span id="function-da-text-implode-82253" />

### `implode`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
implode : [Text] -> Text
```

<span id="function-da-text-isempty-39554" />

### `isEmpty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isEmpty : Text -> Bool
```

Test for emptiness.

<span id="function-da-text-isnotempty-43984" />

### `isNotEmpty`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isNotEmpty : Text -> Bool
```

Test for non-emptiness.

<span id="function-da-text-length-94326" />

### `length`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
length : Text -> Int
```

Compute the number of symbols in the text.

<span id="function-da-text-trim-11808" />

### `trim`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
trim : Text -> Text
```

Remove spaces from either side of the given text.

<span id="function-da-text-replace-9445" />

### `replace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replace : Text -> Text -> Text -> Text
```

Replace a subsequence everywhere it occurs. The first argument
must not be empty.

<span id="function-da-text-lines-25154" />

### `lines`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
lines : Text -> [Text]
```

Breaks a `Text` value up into a list of `Text`'s at newline
symbols. The resulting texts do not contain newline symbols.

<span id="function-da-text-unlines-66467" />

### `unlines`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unlines : [Text] -> Text
```

Joins lines, after appending a terminating newline to each.

<span id="function-da-text-words-34636" />

### `words`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
words : Text -> [Text]
```

Breaks a 'Text' up into a list of words, delimited by symbols
representing white space.

<span id="function-da-text-unwords-40113" />

### `unwords`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unwords : [Text] -> Text
```

Joins words using single space symbols.

<span id="function-da-text-linesby-11211" />

### `linesBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
linesBy : (Text -> Bool) -> Text -> [Text]
```

A variant of `lines` with a custom test. In particular, if there
is a trailing separator it will be discarded.

<span id="function-da-text-wordsby-15461" />

### `wordsBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wordsBy : (Text -> Bool) -> Text -> [Text]
```

A variant of `words` with a custom test. In particular, adjacent
separators are discarded, as are leading or trailing separators.

<span id="function-da-text-intercalate-63059" />

### `intercalate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intercalate : Text -> [Text] -> Text
```

`intercalate` inserts the text argument `t` in between the items
in `ts` and concatenates the result.

<span id="function-da-text-dropprefix-62361" />

### `dropPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropPrefix : Text -> Text -> Text
```

`dropPrefix` drops the given prefix from the argument. It returns
the original text if the text doesn't start with the given prefix.

<span id="function-da-text-dropsuffix-37682" />

### `dropSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropSuffix : Text -> Text -> Text
```

Drops the given suffix from the argument. It returns the original
text if the text doesn't end with the given suffix. Examples:

```
  dropSuffix "!" "Hello World!"  == "Hello World"
  dropSuffix "!" "Hello World!!" == "Hello World!"
  dropSuffix "!" "Hello World."  == "Hello World."
```

<span id="function-da-text-stripsuffix-58624" />

### `stripSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripSuffix : Text -> Text -> Optional Text
```

Return the prefix of the second text if its suffix matches the
entire first text. Examples:

```
  stripSuffix "bar" "foobar" == Some "foo"
  stripSuffix ""    "baz"    == Some "baz"
  stripSuffix "foo" "quux"   == None
```

<span id="function-da-text-stripprefix-74987" />

### `stripPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripPrefix : Text -> Text -> Optional Text
```

The `stripPrefix` function drops the given prefix from the
argument text.  It returns `None` if the text did not start with
the prefix.

<span id="function-da-text-isprefixof-82357" />

### `isPrefixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isPrefixOf : Text -> Text -> Bool
```

The `isPrefixOf` function takes two text arguments and returns
`True` if and only if the first is a prefix of the second.

<span id="function-da-text-issuffixof-35218" />

### `isSuffixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSuffixOf : Text -> Text -> Bool
```

The `isSuffixOf` function takes two text arguments and returns
`True` if and only if the first is a suffix of the second.

<span id="function-da-text-isinfixof-98358" />

### `isInfixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isInfixOf : Text -> Text -> Bool
```

The `isInfixOf` function takes two text arguments and returns
`True` if and only if the first is contained, wholly and intact,
anywhere within the second.

<span id="function-da-text-takewhile-40431" />

### `takeWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhile : (Text -> Bool) -> Text -> Text
```

The function `takeWhile`, applied to a predicate `p` and a text,
returns the longest prefix (possibly empty) of symbols that satisfy
`p`.

<span id="function-da-text-takewhileend-32455" />

### `takeWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhileEnd : (Text -> Bool) -> Text -> Text
```

The function 'takeWhileEnd', applied to a predicate `p` and a
'Text', returns the longest suffix (possibly empty) of elements
that satisfy `p`.

<span id="function-da-text-dropwhile-46373" />

### `dropWhile`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhile : (Text -> Bool) -> Text -> Text
```

`dropWhile p t` returns the suffix remaining after `takeWhile p
t`.

<span id="function-da-text-dropwhileend-2917" />

### `dropWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhileEnd : (Text -> Bool) -> Text -> Text
```

`dropWhileEnd p t` returns the prefix remaining after dropping
symbols that satisfy the predicate `p` from the end of `t`.

<span id="function-da-text-spliton-44082" />

### `splitOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitOn : Text -> Text -> [Text]
```

Break a text into pieces separated by the first text argument
(which cannot be empty), consuming the delimiter.

<span id="function-da-text-splitat-25614" />

### `splitAt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
splitAt : Int -> Text -> (Text, Text)
```

Split a text before a given position so that for `0 <= n <= length t`,
`length (fst (splitAt n t)) == n`.

<span id="function-da-text-take-27133" />

### `take`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
take : Int -> Text -> Text
```

`take n`, applied to a text `t`, returns the prefix of `t` of
length `n`, or `t` itself if `n` is greater than the length of `t`.

<span id="function-da-text-drop-34163" />

### `drop`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
drop : Int -> Text -> Text
```

`drop n`, applied to a text `t`, returns the suffix of `t` after
the first `n` characters, or the empty `Text` if `n` is greater
than the length of `t`.

<span id="function-da-text-substring-36270" />

### `substring`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
substring : Int -> Int -> Text -> Text
```

Compute the sequence of symbols of length `l` in the argument
text starting at `s`.

<span id="function-da-text-ispred-73747" />

### `isPred`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isPred : (Text -> Bool) -> Text -> Bool
```

`isPred f t` returns `True` if `t` is not empty and `f` is `True`
for all symbols in `t`.

<span id="function-da-text-isspace-72803" />

### `isSpace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSpace : Text -> Bool
```

`isSpace t` is `True` if `t` is not empty and consists only of
spaces.

<span id="function-da-text-isnewline-85831" />

### `isNewLine`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isNewLine : Text -> Bool
```

`isSpace t` is `True` if `t` is not empty and consists only of
newlines.

<span id="function-da-text-isupper-58977" />

### `isUpper`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isUpper : Text -> Bool
```

`isUpper t` is `True` if `t` is not empty and consists only of
uppercase symbols.

<span id="function-da-text-islower-60966" />

### `isLower`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isLower : Text -> Bool
```

`isLower t` is `True` if `t` is not empty and consists only of
lowercase symbols.

<span id="function-da-text-isdigit-15622" />

### `isDigit`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isDigit : Text -> Bool
```

`isDigit t` is `True` if `t` is not empty and consists only of
digit symbols.

<span id="function-da-text-isalpha-72233" />

### `isAlpha`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isAlpha : Text -> Bool
```

`isAlpha t` is `True` if `t` is not empty and consists only of
alphabet symbols.

<span id="function-da-text-isalphanum-87978" />

### `isAlphaNum`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isAlphaNum : Text -> Bool
```

`isAlphaNum t` is `True` if `t` is not empty and consists only of
alphanumeric symbols.

<span id="function-da-text-parseint-736" />

### `parseInt`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseInt : Text -> Optional Int
```

Attempt to parse an `Int` value from a given `Text`.

<span id="function-da-text-parsenumeric-9858" />

### `parseNumeric`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseNumeric : NumericScale n => Text -> Optional (Numeric n)
```

Attempt to parse a `Numeric` value from a given `Text`.
To get `Some` value, the text must follow the regex
`(-|\+)?[0-9]+(\.[0-9]+)?`
In particular, the shorthands `".12"` and `"12."` do not work,
but the value can be prefixed with `+`.
Leading and trailing zeros are fine, however spaces are not.
Examples:

```
  parseNumeric "3.14" == Some 3.14
  parseNumeric "+12.0" == Some 12
```

<span id="function-da-text-parsedecimal-57278" />

### `parseDecimal`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
parseDecimal : Text -> Optional Decimal
```

Attempt to parse a `Decimal` value from a given `Text`.
To get `Some` value, the text must follow the regex
`(-|\+)?[0-9]+(\.[0-9]+)?`
In particular, the shorthands `".12"` and `"12."` do not work,
but the value can be prefixed with `+`.
Leading and trailing zeros are fine, however spaces are not.
Examples:

```
  parseDecimal "3.14" == Some 3.14
  parseDecimal "+12.0" == Some 12
```

<span id="function-da-text-sha256-29291" />

### `sha256`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sha256 : Text -> Text
```

Computes the SHA256 hash of the UTF8 bytes of the `Text`, and returns it in its hex-encoded
form. The hex encoding uses lowercase letters.

This function will crash at runtime if you compile Daml to Daml-LF \< 1.2.

<span id="function-da-text-reverse-37387" />

### `reverse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverse : Text -> Text
```

Reverse some `Text`.

```
  reverse "Daml" == "lmaD"
```

<span id="function-da-text-tocodepoints-44801" />

### `toCodePoints`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
toCodePoints : Text -> [Int]
```

Convert a `Text` into a sequence of unicode code points.

<span id="function-da-text-fromcodepoints-94464" />

### `fromCodePoints`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromCodePoints : [Int] -> Text
```

Convert a sequence of unicode code points into a `Text`. Raises an
exception if any of the code points is invalid.

<span id="function-da-text-asciitolower-24557" />

### `asciiToLower`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asciiToLower : Text -> Text
```

Convert the uppercase ASCII characters of a `Text` to lowercase;
all other characters remain unchanged.

<span id="function-da-text-asciitoupper-96826" />

### `asciiToUpper`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
asciiToUpper : Text -> Text
```

Convert the lowercase ASCII characters of a `Text` to uppercase;
all other characters remain unchanged.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
