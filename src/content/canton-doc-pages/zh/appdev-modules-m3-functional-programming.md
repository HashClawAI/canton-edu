---
title: "函数式编程入门"
slug: "appdev-modules-m3-functional-programming"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-functional-programming.md"
source_title: "Functional Programming 101"
tags:
  - appdev
  - modules
  - m3-functional-programming
---

# 函数式编程入门

> 学习 Daml 中的函数式编程概念——函数、控制流、fold 与递归

# 函数式编程入门

本章将更深入地学习如何在 Daml 这类函数式语言中表达复杂逻辑，具体包括：

* 函数签名与函数
* 高级控制流（`if...else`、fold、递归、`when`）

<Note>
  本章有项目模板 `daml-intro-functional-101`，包含本节代码片段。
</Note>

## 与 Haskell 的关系

Daml 入门前几章主要讲模板结构及其与 Daml Ledger Model 的联系；choice 的 `do` 块内逻辑相对简单。本章将深入 Daml 的表达式语言——即在 `do` 块中编写逻辑的部分。此处只能浅尝辄止；Daml 大量借鉴 [Haskell](https://www.haskell.org)。若要深入学习，可参考 Haskell 经典读物：

* [Finding Success and Failure in Haskell (Julie Moronuki, Chris Martin)](https://joyofhaskell.com/)
* [Haskell Programming from first principles (Christopher Allen, Julie Moronuki)](http://haskellbook.com/)
* [Learn You a Haskell for Great Good! (Miran Lipovača)](http://learnyouahaskell.com/)
* [Programming in Haskell (Graham Hutton)](http://www.cs.nott.ac.uk/~pszgmh/pih.html)
* [Real World Haskell (Bryan O'Sullivan, Don Stewart, John Goerzen)](http://book.realworldhaskell.org/)

对比 Daml 与 Haskell 时需注意：

* Haskell 是惰性语言，可写 `head [1..]`（取无穷列表首元）。Daml 是**严格**求值，表达式会完全求值，无法使用无穷数据结构。
* Daml 有记录的 `with` 语法与字段的点访问语法，Haskell 没有；但 Daml 支持 Haskell 的花括号记录写法。
* Daml 默认启用多种 Haskell 编译器扩展。
* Daml 不支持 Haskell 类型系统的全部特性，例如没有存在类型或 GADT。
* Haskell 中的 Action 在 Daml 中称为 Monad。

## 函数

在 `data` 中你已学习 Daml 类型系统的一半：数据类型。现在学习另一半：函数类型。函数类型可通过 `->` 识别，可读作「映射到」。

例如 `Int -> Int` 将整数映射到整数。例如：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment : Int -> Int
increment n = n + 1
```

可见函数声明与定义是分开的。若编译器可推断类型，声明可省略；但对顶层函数（与模板同级、直接在模块下），为可读性通常建议保留。

对 `increment` 可省略声明。同理可不给 `add` 写声明：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add n m = n + m
```

若想知道编译器推断的类型，可在 IDE 中悬停函数名：

```
add
  : Additive a
  => a -> a -> a

Defined at /tmp/daml-intro-9/daml/Main.daml:20:1
add n m = n + m
```

这里签名稍复杂：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add : Additive a => a -> a -> a
```

有两点值得注意：

1. 有多个 `->`。
2. 有类型参数 `a` 及约束 `Additive a`。

### 函数应用

先看右侧 `a -> a -> a`。`->` **右结合**，故 `a -> a -> a` 等价于 `a -> (a -> a)`。按「映射到」理解，即「`a` 映射到一个将 `a` 映射到 `a` 的函数」。

确实如此。可通过**部分应用** `add` 定义另一种 `increment`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment2 = add 1
```

在 IDE 中尝试，编译器会再次推断为 `Int -> Int`，因为字面量 `1 : Int`。

若有 `f : a -> b -> c -> d` 与 `valA : a`，则 `f valA : b -> c -> d`，即可**逐参数**应用。若有 `valB : b`，则 `f valA valB : c -> d`。说明函数**应用**是**左结合**：`f valA valB == (f valA) valB`。

### 中缀函数

`add` 显然是 `+` 的别名，那 `+` 是什么？`+` 只是函数，因以符号开头而默认为**中缀**，可写在两参数之间，故可写 `1 + 2` 而非 `+ 1 2`。中缀与前缀转换规则简单：中缀函数用括号包起来作前缀；普通函数用反引号作中缀：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
three = 1 `add` 2
```

据此可更简洁地将 `add` 定义为别名：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
add2 : Additive a => a -> a -> a
add2 = (+)
```

部分应用中缀运算可写：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
increment3 = (1 +)
double = (* 2)
```

#### 结合性与优先级

多个中缀运算符时，**优先级**决定解析方式。例如 `x + y * z`，因 `*` 高于 `+`，解析为 `x + (y * z)` 而非 `(x + y) * z`。同优先级时，**结合性**决定解析，例如 `+`、`-` 左结合，故 `x + y - z` 解析为 `(x + y) - z`。内置运算符已预定义；用户定义运算符须自行定义，见 [Daml 参考：Fixity、结合性与优先级](/appdev/reference/daml-language-reference#fixity-associativity-and-precedence)。

### 类型约束

`add` 签名中的 `Additive a =>` 是对类型参数 `a` 的**类型约束**。`Additive` 是**类型类**，你已见过 `Eq`、`Show` 等。`Additive` 表示可对 `a` 做加法，即存在 `(+) : a -> a -> a`。完整读法：「在 `a` 有 `Additive` 实例的前提下，`a` 映射到将 `a` 映射到 `a` 的函数」。

Daml 类型类类似其他语言的接口：要用 `+` 相加，类型须「暴露」（有实例）`Additive` 接口（类型类）。

与接口不同，类型类可有多个类型参数。好例子是 `exercise` 的签名，也演示多约束：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise : (Template t, Choice t c r) => ContractId t -> c -> Update r
```

用自然语言：`t` 为模板类型，且 `t` 有返回类型为 `r` 的 choice `c` 时，`exercise` 将类型 `t` 的 `ContractId` 映射到：接受类型 `c` 的 choice 参数并返回 `Update r` 的函数。

表述较长，且需理解类型类 `Choice` 对 `t`、`c`、`r` 的语义，但在许多场景下可从上下文或类型类/变量名推断。

单字母参数常见但非必须。展开参数名可稍清晰，代价是更长：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exercise : (Template template, Choice template choice result) =>
             ContractId template -> choice -> Update result
```

### 参数中的模式匹配

你已在 `case` 表达式中使用模式匹配。也可在**函数参数**层匹配，例如实现 `uncurry`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry : (a -> b -> c) -> (a, b) -> c
```

`uncurry` 将两参数函数变为从二元组到 `c` 的函数。三种实现：元组访问器、`case` 匹配、函数参数匹配：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
uncurry1 f t = f t._1 t._2

uncurry2 f t = case t of
  (x, y) -> f x y

uncurry f (x, y) = f x y
```

`case` 中能做的模式匹配在函数层也能做；编译器会在未覆盖所有情况时警告（non-exhaustive）。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
fromSome : Optional a -> a
fromSome (Some x) = x
```

上述会产生警告：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
warning:
  Pattern match(es) are non-exhaustive
  In an equation for ‘fromSome’: Patterns not matched: None
```

未覆盖所有情况的函数称为**部分函数**。`fromSome None` 会导致运行时错误。

可结合**记录通配符（Record Wildcards）**在函数参数层写 `issueAsset`：

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

模式中的 `..` 表示将记录各字段绑定为局部变量，故有 `issuer`、`owner` 等。

倒数第二行的 `..` 表示用同名局部变量填充新记录各字段，此处（按 `Issue_Asset` 定义）为 `symbol`、`quantity`，来自函数参数 `asset`。等价于：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
exerciseCmd ahCid Issue_Asset with symbol = asset.symbol, quantity = asset.quantity
```

因 `asset@(Asset with ..)` 将 `asset` 绑定为整条记录，同时把各字段绑定为局部变量。

### 函数无处不在

在 Daml 中，凡可放值之处也可放函数，甚至可在数据类型内：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data Predicate a = Predicate with
  test : a -> Bool
```

更常见是在 `let` 等局部定义函数。好例子是 `dependencies` 模型中 `Trade_Settle` choice 内局部定义的 `validate` 与 `transfer`：

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

此处函数签名由上下文推断。仔细查看（或在 IDE 悬停）可见签名为

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
validate : (HasFetch r, Eq r, HasField "observers" r a) => (r, ContractId r) -> Update ()
```

<Note>
  函数不可序列化，不能用于模板参数、choice 输入或输出。通常也不为数据类型派生 `Eq` 或 `Show` 实例。
</Note>

`mapA` 与 `mapA_` 遍历资产与审批列表，对每项应用 `validate`、`transfer` 并执行所得 `Update` 动作。下文 `loops` 节将详述。

### Lambda

Daml 支持内联函数（lambda），语法为 `(\x y z -> ...)`。例如 lambda 版 `increment` 为 `(\n -> n + 1)`。

## 控制流

本节涵盖分支与循环，并介绍将过程式代码译为函数式代码的常见模式。

### 分支

在 `compose` 之前，主要控制流是强大的 `case`。

#### if-else 表达式

`constraints` 中出现过看似不言自明的 `if ... else`，未展开。实现 `boolToInt : Bool -> Int`，将 `True` 映射为 1、`False` 为 0，用 `case`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boolToInt b = case b of
  True -> 1
  False -> 0
```

在 IDE 中编写会得到 linter 建议：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
Suggestion: Use if
Found:
case b of
    True -> 1
    False -> 0
Perhaps:
if b then 1 else 0
```

linter 知道等价关系并建议：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
boolToInt2 b = if b
  then 1
  else 0
```

简言之：`if ... else` 与 `case` 等价，但常更易读。

#### 控制流即表达式

`case` 与 `if ... else` 会短路：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
doError t = case t of
  "True" -> True
  "False" -> False
  _ -> error ("Not a Bool: " <> t)
```

仅当传入无效文本时才会求值 `error`。

函数则不同，所有参数会立即求值：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ifelse b t e = if b then t else e
boom = ifelse True 1 (error "Boom")
```

此处 `boom` 会出错。

`case` 与 `if ... else` 在求值后产生值。上文函数体即整个 `case` 或 `if ... else`，其值即函数值。各分支须同类型，否则无法确定类型。下列函数不编译，因一分支返回 `Int`、另一返回 `Text`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
typeError b = if b
  then 1
  else "a"
```

若函数可返回两种（或更多）类型，须在返回类型中编码，两种时常用 `Either`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
intOrText : Bool -> Either Int Text
intOrText b = if b
  then Left 1
  else Right "a"
```

多于两种（有时两种也）时，可定义自己的变体类型包装所有可能。

#### 动作中的分支

在 `do` 块中最常见：一种情况创建一种合约，另一种创建另一种。例如有两种模板，条件满足时创建 `S`，否则创建 `T`：

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

简单 `if ... else` 很诱人，但若各分支返回不同类型则无法通过类型检查：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
typeError b p = if b
  then create T with p
  else create S with p
```

两种做法：

1. 使用上文 `Either` 技巧。
2. 去掉返回类型差异。

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

后者极常见，`DA.Action` 提供 `void : Functor f => f a -> f ()` 去掉返回类型：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
ifThenSElseT3 b p = if b
  then void (create S with p)
  else void (create T with p)
```

`void` 也用于表达「仅当条件满足时创建 `T`」：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conditionalS b p = if b
  then void (create S with p)
  else return ()
```

仍需要同类型 `()` 的 `else`。该模式封装在 `DA.Action.when : (Applicative f) => Bool -> f () -> f ()`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
conditionalS2 b p = when b (void (create S with p))
```

尽管 `when` 像普通函数，编译器会做魔法使其像 `if ... else`、`case` 一样短路：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
noop : Update () = when False (error "Foo")
```

`case`、`if ... else`、`void`、`when` 可表达全部分支。另可学习 **guards** 以避免深层嵌套 `if ... else`；本章未详述，Haskell 资料有更深讲解。示例：

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

### 循环

除分支外，最常见控制流是循环，通常用于迭代修改状态。本节用 JavaScript 说明过程式写法。

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function sum(intArr) {
  var result = 0;
  intArr.forEach (i => {
    result += i;
  });
  return result;
}
```

更一般的循环：

```JavaScript theme={"theme":{"light":"github-light","dark":"github-dark"}}
function whileF(init, cont, step, finalize) {
  var state = init();
  while (cont(state)) {
    state = step(state);
  }
  return finalize(state);
}
```

两种情形都在**变异**状态：`result` 或 `state`。Daml 值不可变，故用 **fold** 与**递归**。

#### Fold

Fold 对应带显式迭代器的过程式 `for`/`forEach`。最常见迭代器是列表，如上文 `sum`。Daml 有 `foldl`（`l` 表示从左处理列表），也有 `foldr`。

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
foldl : (b -> a -> b) -> b -> [a] -> b
```

语义化类型参数：`b` 为状态，`a` 为元素。第一参数为「状态 + 元素 → 新状态」的函数（对应 `forEach` 内层），然后是初始状态与元素列表，结果为最终状态。对应关系下，`sum` 几乎可直接译为 Daml：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sum ints = foldl (+) 0 ints
```

更啰嗦可写 lambda `(\result i -> result + i)`，与 JavaScript 的 `result += i` 对应更清晰。

几乎所有带显式迭代器的循环都可译为 fold；翻译 `for` 循环时需注意性能：

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

若能得到 `[0..(l-1)]` 数组，将 `for` 译为 `forEach` 较易。Daml 用**范围**：`[0..(l-1)]` 是 `enumFromTo 0 (l-1)` 的简写。

Daml 还有 `(!!) : [a] -> Int -> a` 取列表元素。可能想这样写 `sumArrs`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs : [Int] -> [Int] -> [Int]
sumArrs arr1 arr2 =
  let l = min (length arr1) (length arr2)
      sumAtI i = (arr1 !! i) + (arr2 !! i)
   in foldl (\state i -> (sumAtI i) :: state) [] [1..(l-1)]
```

但 Daml 列表为链表，`(!!)` 对此类迭代过慢。更好做法是去掉索引 `i`，先用 `zip` 合并列表再迭代：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs2 arr1 arr2 = foldl (\state (x, y) -> (x + y) :: state) [] (zip arr1 arr2)
```

`zip : [a] -> [b] -> [(a, b)]` 将两列表合并为二元组列表，并丢弃较长列表余下元素，故无需 `min` 逻辑。

#### Map

传给 `foldl` 的 lambda 往往只处理单个（zip 后）元素，但仍须拼接整个状态。仅对每元素单独操作的模式有专用函数 `map : (a -> b) -> [a] -> [b]`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
sumArrs3 arr1 arr2 = map (\(x, y) -> (x + y)) (zip arr1 arr2)
```

经验法则：结果与输入同形且无需跨迭代累积状态时用 `map`；需累积状态用 fold。

#### 递归

无显式迭代器时用递归。例如反转列表且避免 `(!!)`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
reverseWorker rev rem = case rem of
  [] -> rev
  x::xs -> reverseWorker (x::rev) xs
reverse xs = reverseWorker [] xs
```

可能想把 `reverseWorker` 放在 `reverse` 内局部定义，但 Daml 仅支持**顶层**函数递归，故 `reverseWorker` 须为顶层。

#### 动作上下文中的 fold 与 map

上文 fold、`map` 为**纯**的：映射函数无副作用。多包模型中可见 `mapA`、`mapA_`、`forA`，在 `Action` 中起类似作用。例：`testMultiTrade` 脚本中的 `mapA`：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
let rels =
        [ Relationship chfbank alice
        , Relationship chfbank bob
        , Relationship gbpbank alice
        , Relationship gbpbank bob
        ]
  [chfha, chfhb, gbpha, gbphb] <- mapA setupRelationship rels
```

有 `[Relationship]` 列表与 `setupRelationship : Relationship -> Script (ContractId AssetHolder)`，需要 `[ContractId AssetHolder]`。`map setupRelationship rels` 类型为 `[Update (ContractId AssetHolder)]`——`Update` 动作列表，每项产生 `ContractId AssetHolder`。我们需要的是产生 `[ContractId AssetHolder]` 的**单个** `Update`——列表与 `Update` 嵌套顺序不对。

直观修复：依次执行列表中每个动作。有函数 `sequence : Applicative m => [m a] -> m [a]`，可「把 `Update` 从列表中取出」。可写 `sequence (map setupRelationship rels)`，极常见故封装为 `mapA`，一种实现为

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
mapA f xs = sequence (map f xs)
```

`mapA` 中 `A` 表示 Action；许多与「循环」相关的函数都有 `A` 变体。最根本的是 `foldlA : Action m => (b -> a -> m b) -> b -> [a] -> m b`，带副作用的左 fold，内层函数有副作用 `m`，结果 `m b` 为所有副作用之和。

为熟悉这些概念，可尝试用 `foldl` 实现 `foldlA`，以及用 `foldlA` 实现 `sequence`、`mapA`。一种可能实现：

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

`forA` 即参数顺序颠倒的 `mapA`，当元素列表已是变量而函数是较长 lambda 时更易读：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
[usdCid, chfCid] <- forA [usdCid, chfCid] (\cid -> submit alice do
    exerciseCmd cid SetObservers with
      newObservers = [bob]
    )
```

有时用 `mapA_` 而非 `mapA`，下划线表示不使用结果：`mapA_ fn xs == void (mapA fn xs)`。Daml Linter 会提示何时可用 `mapA_`/`forA_`。

## 下一步

你已掌握纯上下文与 Action 上下文中的函数与控制流基础。多包示例表明仅凭本章工具即可做很多事，但 Daml 标准库还为常见场景提供更多函数与类型类。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
