---
title: "Interfaces"
slug: "appdev-modules-m3-interfaces"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-interfaces.md"
source_title: "Interfaces"
tags:
  - appdev
  - modules
  - m3-interfaces
---

# Interfaces

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Interfaces

> Define and implement Daml interfaces for polymorphic contract behavior and cross-template interoperability

# Reference: Interfaces

In Daml, an interface defines an abstract type together with a behavior specified by its view type, method signatures, and choices. For a template to conform to this interface, there must be a corresponding `interface instance` definition where all the methods of the interface (including the special `view` method) are implemented. This allows decoupling such behavior from its implementation, so other developers can write applications in terms of the interface instead of the concrete template.

## Configuration

To use this feature your Daml project must target Daml-LF version `1.15` or higher, which is the current default.

If using Canton, the protocol version of the sync domain should be `4` or higher, see Canton protocol version for more details.

## Interface Declaration

An interface declaration is somewhat similar to a template declaration.

### Interface Name

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface MyInterface where
```

* This is the name of the interface.
* It's preceded by the keyword `interface` and followed by the keyword `where`.
* It must begin with a capital letter, like any other type name.

### Implicit abstract type

* Whenever an interface is defined, an abstract type is defined with the same name. "Abstract" here means:
  * Values of this type cannot be created using a data constructor. Instead, they are constructed by applying the function `toInterface` to a template value.
  * Values of this type cannot be inspected directly via case analysis. Instead, use functions such as `fromInterface`.
  * See `daml-ref-interface-functions` for more information on these and other functions for interacting with interface values.
* An interface value carries inside it the type and parameters of the template value from which it was constructed.
* As for templates, the existence of a local binding `b` of type `I`, where `I` is an interface does not necessarily imply the existence on the ledger of a contract with the template type and parameters used to construct `b`. This can only be assumed if `b` the result of a fetch from the ledger within the same transaction.

### Interface Methods

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
method1 : Party
  method2 : Int
  method3 : Bool -> Int -> Int -> Int
```

* An interface may define any number of methods.
* A method definition consists of the method name and the method type, separated by a single colon `:`. The name of the method must be a valid identifier beginning with a lowercase letter or an underscore.
* A method definition introduces a top level function of the same name:
  * If the interface is called `I`, the method is called `m`, and the method type is `M` (which might be a function type), this introduces the function `m : I -> M`:

    ```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
    func1 : MyInterface -> Party
    func1 = method1

    func2 : MyInterface -> Int
    func2 = method2

    func3 : MyInterface -> Bool -> Int -> Int -> Int
    func3 = method3
    ```

  * The first argument's type `I` means that the function can only be applied to values of the interface type `I` itself. Methods cannot be applied to template values, even if there exists an `interface instance` of `I` for that template. To use an interface method on a template value, first convert it using the `toInterface` function.

  * Applying the function to such argument results in a value of type `M`, corresponding to the implementation of `m` in the interface instance of `I` for the underlying template type `t` (the type of the template value from which the interface value was constructed).
* One special method, `view`, must be defined for the viewtype. (see **Viewtype** below).

### Interface View Type

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

### Interface Choices

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

### Empty Interfaces

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
data EmptyInterfaceView = EmptyInterfaceView {}

interface YourInterface where
  viewtype EmptyInterfaceView
```

* It is possible (though not necessarily useful) to define an interface without methods, precondition or choices. However, a view type must always be defined, though it can be set to unit.

## Interface Instances

For context, a simple template definition:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template NameOfTemplate
  with
    field1 : Party
    field2 : Int
  where
    signatory field1
```

### `interface instance` clause

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

### Empty `interface instance` clause

* If the interface has no methods, the interface instance only needs to implement the `view` method:

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
interface instance YourInterface for NameOfTemplate where
      view = EmptyInterfaceView
```

## Interface Functions

### `interfaceTypeRep`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>HasInterfaceTypeRep i =></code><br />
      <code>i -> TemplateTypeRep</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>MyInterface -> TemplateTypeRep</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>The value of the resulting <code>TemplateTypeRep</code> indicates what template was used to construct the interface value.</td>
    </tr>
  </tbody>
</table>

### `toInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>t -> i</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>MyTemplate -> MyInterface</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Converts a template value into an interface value.</td>
    </tr>
  </tbody>
</table>

### `fromInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>HasFromInterface t i =></code><br />
      <code>i -> Optional t</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>MyInterface -> Optional MyTemplate</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Attempts to convert an interface value back into a template value. The result is <code>None</code> if the expected template type doesn't match the underlying template type used to construct the contract.</td>
    </tr>
  </tbody>
</table>

### `toInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>forall i t.</code><br />
      <code>HasToInterface t i =></code><br />
      <code>ContractId t -> ContractId i</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>ContractId MyTemplate -> ContractId MyInterface</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Converts a template Contract ID into an Interface Contract ID.</td>
    </tr>
  </tbody>
</table>

### `fromInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>forall t i.</code><br />
      <code>HasFromInterface t i =></code><br />
      <code>ContractId i -> ContractId t</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>ContractId MyInterface -> ContractId MyTemplate</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Converts an interface contract id into a template contract id. This function does not verify that the given contract id actually points to a contract of the resulting type; if that is not the case, a subsequent <code>fetch</code>, <code>exercise</code> or <code>archive</code> will fail. Therefore, this should only be used when the underlying contract is known to be of the resulting type, or when the result is immediately used by a <code>fetch</code>, <code>exercise</code> or <code>archive</code> action and a transaction failure is the desired behavior in case of mismatch. In all other cases, consider using <code>fetchFromInterface</code> instead.</td>
    </tr>
  </tbody>
</table>

### `coerceInterfaceContractId`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>forall j i.</code><br />
      <code>(HasInterfaceTypeRep i, HasInterfaceTypeRep j) =></code><br />
      <code>ContractId i -> ContractId j</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><code>ContractId SourceInterface -> ContractId TargetInterface</code></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Converts an interface contract id into a contract id of a different interface. This function does not verify that the given contract id actually points to a contract of the resulting type; if that is not the case, a subsequent <code>fetch</code>, <code>exercise</code> or <code>archive</code> will fail. Therefore, this should only be used when the underlying contract is known to be of the resulting type, or when the result is immediately used by a <code>fetch</code>, <code>exercise</code> or <code>archive</code> action and a transaction failure is the desired behavior in case of mismatch.</td>
    </tr>
  </tbody>
</table>

### `fetchFromInterface`

<table>
  <tbody>
    <tr class="odd">
      <td>Type</td>
      <td><p><code>forall t i.</code><br />
      <code>(HasFromInterface t i, HasFetch i) =></code><br />
      <code>ContractId i -> Update (Optional (ContractId t, t))</code></p></td>
    </tr>

    <tr class="even">
      <td>Instantiated Type</td>
      <td><p><code>ContractId MyInterface -></code><br />
      <code>Update (Optional (ContractId MyTemplate, MyTemplate))</code></p></td>
    </tr>

    <tr class="odd">
      <td>Notes</td>
      <td>Attempts to fetch and convert an interface contract id into a template, returning both the converted contract and its contract id if the conversion is successful, or <code>None</code> otherwise.</td>
    </tr>
  </tbody>
</table>

## Required Interfaces

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

### Interface Functions

| Function                  | Notes                                                                                                                              |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `toInterface`             | Can also be used to convert an interface value to one of its required interfaces.                                                  |
| `fromInterface`           | Can also be used to convert a value of an interface type to one of its requiring interfaces.                                       |
| `toInterfaceContractId`   | Can also be used to convert an interface contract id into a contract id of one of its required interfaces.                         |
| `fromInterfaceContractId` | Can also be used to convert an interface contract id into a contract id of one of its requiring interfaces.                        |
| `fetchFromInterface`      | Can also be used to fetch and convert an interface contract id into a contract and contract id of one of its requiring interfaces. |

## Interfaces on Canton Network

Interfaces are central to interoperability across the Canton Network. Two Canton Improvement Proposals (CIPs) define standard interfaces that app developers should be aware of:

* [CIP-0056 — Token Standard](https://github.com/global-synchronizer-foundation/cips/blob/main/cip-0056/cip-0056.md): Defines a standard interface for fungible tokens on Canton Network. If your application issues or transfers tokens, implementing this interface ensures compatibility with wallets and other applications in the ecosystem.

* [CIP-0103 — dApp Standard](https://github.com/mjuchli-da/cips/blob/cip-dapp-standard/cip-0103/cip-0103.md): Defines standard interfaces for decentralized applications. This CIP is particularly relevant for developers coming from Ethereum, as it maps familiar ERC-style patterns to Daml interfaces.

When building applications on Canton Network, implementing these standard interfaces lets your contracts participate in the broader ecosystem without requiring custom integration with each counterparty.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
