# DA.List

> Daml 模块 DA.List 的参考文档。

<span id="module-da-list-85985" />

# DA.List

列表

## 模块概览

<CardGroup cols={2}>
  <Card title="生命周期">
    稳定。
  </Card>

  <Card title="说明">
    Status: `active`
    Introduced in: `3.4.9`
    Removed in: `-`
    Warnings: `0`
    Deprecations: `0`
    Deprecated since: `-`
  </Card>
</CardGroup>

## 函数

<span id="function-da-list-sort-96399" />

### `sort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sort : Ord a => [a] -> [a]
```

`sort` 实现稳定排序算法，是 `sortBy` 的特例，后者允许提供自定义比较函数。

元素从低到高排列，重复项保持输入中的出现顺序（稳定排序）。

<span id="function-da-list-sortby-71202" />

### `sortBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortBy : (a -> a -> Ordering) -> [a] -> [a]
```

`sortBy` 是 `sort` 的非重载版本。

<span id="function-da-list-minimumby-84625" />

### `minimumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumBy : (a -> a -> Ordering) -> [a] -> a
```

`minimumBy f xs` 返回 `xs` 中首个对所有其他 `y` 满足 `f x y` 为 `LT` 或 `EQ` 的元素 `x`。`xs` 必须非空。

<span id="function-da-list-maximumby-22187" />

### `maximumBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumBy : (a -> a -> Ordering) -> [a] -> a
```

`maximumBy f xs` 返回 `xs` 中首个对所有其他 `y` 满足 `f x y` 为 `GT` 或 `EQ` 的元素 `x`。`xs` 必须非空。

<span id="function-da-list-sorton-99758" />

### `sortOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sortOn : Ord k => (a -> k) -> [a] -> [a]
```

按键函数对每个元素的返回值比较并排序列表。`sortOn f` 等价于 `sortBy (comparing f)`，但对输入中每个元素只求值一次 `f`，性能更好（有时称为 decorate-sort-undecorate）。

元素从低到高排列，重复项保持输入顺序。

<span id="function-da-list-minimumon-90785" />

### `minimumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
minimumOn : Ord k => (a -> k) -> [a] -> a
```

`minimumOn f xs` 返回 `xs` 中首个满足 `f x` 不大于任何其他 `f y` 的元素 `x`。`xs` 必须非空。

<span id="function-da-list-maximumon-98335" />

### `maximumOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
maximumOn : Ord k => (a -> k) -> [a] -> a
```

`maximumOn f xs` 返回 `xs` 中首个满足 `f x` 不小于任何其他 `f y` 的元素 `x`。`xs` 必须非空。

<span id="function-da-list-mergeby-31951" />

### `mergeBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mergeBy : (a -> a -> Ordering) -> [a] -> [a] -> [a]
```

将两个已排序列表按指定比较函数合并为一个有序列表。

<span id="function-da-list-combinepairs-8661" />

### `combinePairs`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
combinePairs : (a -> a -> a) -> [a] -> [a]
```

用程序员提供的二元函数将两个列表输入逐对合并为单个列表。

<span id="function-da-list-foldbalanced1-46720" />

### `foldBalanced1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldBalanced1 : (a -> a -> a) -> [a] -> a
```

以平衡方式 fold 非空列表。平衡指运算符树中各元素深度大致相同（最大与最小深度差至多为 1）。累加运算须结合且可交换，才能得到与 `foldl1` 或 `foldr1` 相同的结果。

<span id="function-da-list-group-62411" />

### `group`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
group : Eq a => [a] -> [[a]]
```

`group` 将相等元素分组为子列表，使结果拼接后等于原列表。

<span id="function-da-list-groupby-62666" />

### `groupBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
groupBy : (a -> a -> Bool) -> [a] -> [[a]]
```

`groupBy` 是 `group` 的非重载版本。

<span id="function-da-list-groupon-4918" />

### `groupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
groupOn : Eq k => (a -> k) -> [a] -> [[a]]
```

类似 `group`，但相等性基于提取的值。

<span id="function-da-list-dedup-27230" />

### `dedup`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedup : Ord a => [a] -> [a]
```

`dedup l` 移除列表中的重复元素，仅保留每个元素的首次出现。它是 `dedupBy` 的特例，后者允许自定义相等性测试。
在 Haskell 中称为 `nub`。

<span id="function-da-list-dedupby-29335" />

### `dedupBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupBy : (a -> a -> Ordering) -> [a] -> [a]
```

带自定义谓词的 `dedup` 版本。

<span id="function-da-list-dedupon-81495" />

### `dedupOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupOn : Ord k => (a -> k) -> [a] -> [a]
```

在应用函数后再去重的 `dedup` 版本。示例：`dedupOn (.employeeNo) employees`

<span id="function-da-list-dedupsort-78698" />

### `dedupSort`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSort : Ord a => [a] -> [a]
```

`dedupSort` 对列表排序并去重，仅保留每个元素的首次出现。

<span id="function-da-list-dedupsortby-97595" />

### `dedupSortBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dedupSortBy : (a -> a -> Ordering) -> [a] -> [a]
```

带自定义谓词的 `dedupSort` 版本。

<span id="function-da-list-unique-23008" />

### `unique`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
unique : Ord a => [a] -> Bool
```

当且仅当给定列表无重复元素时返回 True。

<span id="function-da-list-uniqueby-86149" />

### `uniqueBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueBy : (a -> a -> Ordering) -> [a] -> Bool
```

带自定义谓词的 `unique` 版本。

<span id="function-da-list-uniqueon-39349" />

### `uniqueOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uniqueOn : Ord k => (a -> k) -> [a] -> Bool
```

在应用函数后，当且仅当列表无重复元素时返回 True。示例：`assert $ uniqueOn (.employeeNo) employees`

<span id="function-da-list-replace-72492" />

### `replace`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
replace : Eq a => [a] -> [a] -> [a] -> [a]
```

在操作列表中将搜索列表的每次出现替换为替换列表。

<span id="function-da-list-dropprefix-26566" />

### `dropPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropPrefix : Eq a => [a] -> [a] -> [a]
```

从列表去掉给定前缀；若序列不以该前缀开头则返回原序列。

<span id="function-da-list-dropsuffix-41813" />

### `dropSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropSuffix : Eq a => [a] -> [a] -> [a]
```

从列表去掉给定后缀；若序列不以该后缀结尾则返回原序列。

<span id="function-da-list-stripprefix-65866" />

### `stripPrefix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripPrefix : Eq a => [a] -> [a] -> Optional [a]
```

`stripPrefix` 去掉列表的给定前缀；若列表不以该前缀开头返回 `None`，否则返回 `Some` 及前缀之后的列表。

<span id="function-da-list-stripsuffix-23153" />

### `stripSuffix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripSuffix : Eq a => [a] -> [a] -> Optional [a]
```

若第二列表的后缀与第一列表完全匹配，则返回第二列表的前缀部分。

<span id="function-da-list-stripinfix-68205" />

### `stripInfix`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
stripInfix : Eq a => [a] -> [a] -> Optional ([a], [a])
```

返回搜索串之前与之后的部分，未找到则返回 `None`。

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

`isPrefixOf` 当且仅当第一列表是第二列表的前缀时返回 `True`。

<span id="function-da-list-issuffixof-26645" />

### `isSuffixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isSuffixOf : Eq a => [a] -> [a] -> Bool
```

`isSuffixOf` 当且仅当第一列表是第二列表的后缀时返回 `True`。

<span id="function-da-list-isinfixof-7159" />

### `isInfixOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
isInfixOf : Eq a => [a] -> [a] -> Bool
```

`isInfixOf` 当且仅当第一列表出现在第二列表任意位置时返回 `True`。

<span id="function-da-list-mapaccuml-18387" />

### `mapAccumL`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapAccumL : (acc -> x -> (acc, y)) -> acc -> [x] -> (acc, [y])
```

`mapAccumL` 结合 `map` 与 `foldl`：对列表每元素应用函数，从左到右传递累加器，并返回累加器最终值与新列表。

<span id="function-da-list-mapwithindex-75685" />

### `mapWithIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapWithIndex : (Int -> a -> b) -> [a] -> [b]
```

`mapWithIndex` 是 `map` 的推广，映射函数还依赖元素索引，并应用于序列中每个元素。

<span id="function-da-list-inits-75071" />

### `inits`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
inits : [a] -> [[a]]
```

`inits` 返回参数的所有前缀段，最短者优先。

<span id="function-da-list-intersperse-31314" />

### `intersperse`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intersperse : a -> [a] -> [a]
```

`intersperse` 接受一个元素与列表，在该列表元素之间插入该元素。

<span id="function-da-list-intercalate-85238" />

### `intercalate`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intercalate : [a] -> [[a]] -> [a]
```

`intercalate` 在 `xss` 中的列表之间插入 `xs` 并拼接结果。

<span id="function-da-list-tails-57647" />

### `tails`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tails : [a] -> [[a]]
```

`tails` 返回参数的所有后缀段，最长者优先。

<span id="function-da-list-dropwhileend-92606" />

### `dropWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
dropWhileEnd : (a -> Bool) -> [a] -> [a]
```

从末尾操作的 `dropWhile` 版本。

<span id="function-da-list-takewhileend-40268" />

### `takeWhileEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
takeWhileEnd : (a -> Bool) -> [a] -> [a]
```

从末尾操作的 `takeWhile` 版本。

<span id="function-da-list-transpose-84171" />

### `transpose`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
transpose : [[a]] -> [[a]]
```

`transpose` 转置参数的行列。

<span id="function-da-list-breakend-41551" />

### `breakEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakEnd : (a -> Bool) -> [a] -> ([a], [a])
```

从末尾拆分。

<span id="function-da-list-breakon-39026" />

### `breakOn`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakOn : Eq a => [a] -> [a] -> ([a], [a])
```

在 `haystack` 中查找 `needle` 的首次出现。返回元组首项为匹配前的前缀，第二项为从匹配开始的剩余部分；若要不包含匹配的剩余部分，请用 `stripInfix`。

<span id="function-da-list-breakonend-30980" />

### `breakOnEnd`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
breakOnEnd : Eq a => [a] -> [a] -> ([a], [a])
```

类似 `breakOn`，但从末尾搜索。返回元组首项为 `haystack` 至最后一次匹配 `needle`（含匹配）的前缀，第二项为匹配之后的剩余部分。

<span id="function-da-list-linesby-68954" />

### `linesBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
linesBy : (a -> Bool) -> [a] -> [[a]]
```

带自定义测试的 `lines` 变体；若有尾随分隔符会被丢弃。

<span id="function-da-list-wordsby-74460" />

### `wordsBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
wordsBy : (a -> Bool) -> [a] -> [[a]]
```

带自定义测试的 `words` 变体；相邻及首尾分隔符会被丢弃。

<span id="function-da-list-head-92101" />

### `head`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
head : [a] -> a
```

提取列表首元素，列表必须非空。

<span id="function-da-list-tail-16805" />

### `tail`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
tail : [a] -> [a]
```

提取列表首元素之后的部分，列表必须非空。

<span id="function-da-list-last-56071" />

### `last`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
last : [a] -> a
```

提取列表末元素，列表须有限且非空。

<span id="function-da-list-init-2389" />

### `init`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
init : [a] -> [a]
```

返回除末元素外的所有元素，列表必须非空。

<span id="function-da-list-foldl1-60813" />

### `foldl1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl1 : (a -> a -> a) -> [a] -> a
```

对必须非空的列表做左结合 fold。

<span id="function-da-list-foldr1-23463" />

### `foldr1`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldr1 : (a -> a -> a) -> [a] -> a
```

对必须非空的列表做右结合 fold。

<span id="function-da-list-repeatedly-9930" />

### `repeatedly`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
repeatedly : ([a] -> (b, [a])) -> [a] -> [b]
```

重复应用某操作，每次产生一个输出元素与列表剩余部分。

<span id="function-da-list-chunksof-64138" />

### `chunksOf`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
chunksOf : Int -> [a] -> [[a]]
```

将列表按长度 @n@ 分块。
@n@ 必须严格大于零。
若输入长度不能被 @n@ 整除，最后一块会短于 @n@。

<span id="function-da-list-delete-22340" />

### `delete`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
delete : Eq a => a -> [a] -> [a]
```

`delete x` 从列表参数中移除 `x` 的首次出现。例如：

```
> delete "a" ["b","a","n","a","n","a"]
["b","n","a","n","a"]
```

它是 `deleteBy` 的特例，后者允许自定义相等性测试。

<span id="function-da-list-deleteby-50465" />

### `deleteBy`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
deleteBy : (a -> a -> Bool) -> a -> [a] -> [a]
```

`deleteBy` 行为类似 `delete`，但接受用户提供的相等谓词。

```
> deleteBy (<=) 4 [1..10]
[1,2,3,5,6,7,8,9,10]
```

<span id="function-da-list-x-54181" />

### `\\`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
\\ : Eq a => [a] -> [a] -> [a]
```

`\\` 是列表差（非结合）。在 `xs \\ ys` 的结果中，依次从 `xs` 中移除 `ys` 中各元素的首次出现。因此

```
(xs ++ ys) \\ xs == ys
```

注意：列表规模为 *n* 与 *m* 时，本函数为 *O(n\*m)*。

<span id="function-da-list-singleton-17649" />

### `singleton`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
singleton : a -> [a]
```

生成单元素列表。

```
>>> singleton True
[True]
```

<span id="function-da-list-bangbang-90127" />

### `!!`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
!! : [a] -> Int -> a
```

列表下标运算符，从 0 起。例如 `xs !! 2` 返回 `xs` 中第三个元素。索引不合法时会报错。复杂度为 *O(n)*（*n* 为给定索引），不同于 Java 等语言的 *O(1)* 数组索引。

<span id="function-da-list-elemindex-4965" />

### `elemIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
elemIndex : Eq a => a -> [a] -> Optional Int
```

在列表中查找元素索引，未找到返回 `None`。

<span id="function-da-list-findindex-82181" />

### `findIndex`

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
findIndex : (a -> Bool) -> [a] -> Optional Int
```

按谓词查找首个匹配元素的索引，未找到返回 `None`。