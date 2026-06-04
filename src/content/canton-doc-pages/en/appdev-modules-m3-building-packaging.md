---
title: "Building and Packaging"
slug: "appdev-modules-m3-building-packaging"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m3-building-packaging.md"
source_title: "Building and Packaging"
tags:
  - appdev
  - modules
  - m3-building-packaging
---

# Building and Packaging

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Building and Packaging

> Build Daml projects, manage dependencies, and package DAR files for deployment

# Work with dependencies

The application from `compose` is a complete and secure model for atomic swaps of assets, but there is plenty of room for improvement. However, one can't implement all features before going live with an application so it's important to understand how to change already running code. There are fundamentally two types of change one may want to make:

1. Upgrades, which change existing logic. For example, one might want the `Asset` template to have multiple signatories.
2. Extensions, which merely add new functionality through additional templates.

Upgrades are covered in their own section outside this introduction to Daml: [smart contract upgrades](/docs/canton/appdev-deep-dives-smart-contract-upgrade),
so in this section we will extend the `compose` model with a simple second workflow: a multi-leg trade. In doing so, you'll learn about:

* The software architecture of the Daml stack
* Dependencies and data dependencies
* Identifiers

Since we are extending `compose`, the setup for this chapter is slightly more complex:

1. In a base directory, load the `compose` project using `dpm new intro-compose  --template daml-intro-compose`. The directory `intro7` here is important as it'll be referenced by the other project we are creating.
2. In the same directory, load this chapter's project using `dpm new intro-9  --template daml-intro-9`.

`Dependencies` contains a new module `Intro.Asset.MultiTrade` and a corresponding test module `Test.Intro.Asset.MultiTrade`.

## DAR files, Daml-LF, and the engine

In `compose` you already learnt a little about projects, Daml-LF, DAR files, and dependencies. In this chapter we will actually need to have dependencies from the current project to the `compose` project so it's time to learn a little more about all this.

Let's have a look inside the DAR file of `compose`. DAR files, like Java JAR files, are just ZIP archives, but the SDK also has a utility to inspect DARs out of the box:

1. Navigate into the `intro7` directory.
2. Build using `dpm build -o assets.dar`
3. Run `dpm damlc inspect-dar assets.dar`

You'll get a whole lot of output. Under the header "DAR archive contains the following files:" you'll see that the DAR contains:

1. `*.dalf` files for the project and all its dependencies
2. The original Daml source code
3. `*.hi` and `*.hie` files for each `*.daml` file
4. Some meta-inf and config files

The first file is something like `intro7-1.0.0-887056cbb313b94ab9a6caf34f7fe4fbfe19cb0c861e50d1594c665567ab7625.dalf` which is the actual compiled package for the project. `*.dalf` files contain Daml-LF, which is Daml's intermediate language. The file contents are a binary encoded protobuf message defined by the [Daml-LF tooling in the `digital-asset/daml` repository](https://github.com/digital-asset/daml/tree/main/sdk/daml-lf). Daml-LF is evaluated on the ledger by the Daml Engine, which is a JVM component that is part of tools like the IDE's script runner, the Sandbox, or proper production ledgers. If Daml-LF is to Daml what Java Bytecode is to Java, the Daml Engine is to Daml what the JVM is to Java.

## Hashes and identifiers

Under the heading "DAR archive contains the following packages:" you get a similar looking list of package names, paired with only the long random string repeated. That hexadecimal string, `887056cbb313b94ab9a6caf34f7fe4fbfe19cb0c861e50d1594c665567ab7625` in this case, is the package hash and the primary and only identifier for a package that's guaranteed to be available and preserved. Meta information like name ("intro7") and version ("1.0.0") help make it human readable but should not be relied upon. You may not always get DAR files from your compiler, but be loading them from a running ledger, or get them from an artifact repository.

We can see this in action. When a DAR file gets deployed to a ledger, not all meta information is preserved.

1. Note down your main package hash from running `inspect-dar` above
2. Start the project by running a ledger and uploading the `assets.dar` DAR:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
cat <<EOF
canton.parameters.enable-alpha-state-via-config = yes
canton.parameters.state-refresh-interval = 5s
canton.participants.sandbox.alpha-dynamic.dars = [
  { location = "./assets.dar" }
]
EOF > config.conf

dpm sandbox -c config.conf
```

3. Open another terminal and use the gRPC Ledger API to download the dar, making sure to replace the hash with the appropriate one

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
grpcurl  localhost:6866 com.digitalasset.canton.admin.participant.v30.PackageService.GetDar \
  -d '{"mainPackageId": "887056cbb313b94ab9a6caf34f7fe4fbfe19cb0c861e50d1594c665567ab7625"}' \
  -plaintext | jq -r '.payload' | base64 --decode > assets_ledger.dar
```

4. Run `dpm damlc inspect-dar assets_ledger.dar`

You'll notice two things. Firstly, a lot of the dependencies have lost their names, they are now only identifiable by hash. We could of course also create a second project `intro7-1.0.0` with completely different contents so even when name and version are available, package hash is the only safe identifier.

That's why over the Ledger API, all types, like templates and records are identified by the triple `(entity name, module name, package hash)`. Your client application should know the package hashes it wants to interact with. To aid that, `inspect-dar` also provides a machine-readable format for the information it emits: `dpm damlc inspect-dar --json assets_ledger.dar`. The `main_package_id` field in the resulting JSON payload is the package hash of our project.

Secondly, you'll notice that all the `*.daml`, `*.hi` and `*.hie` files are gone. This leads us to data dependencies.

## Dependencies and data dependencies

Dependencies under the `daml.yaml` `dependencies` group rely on the `*.hi` files. The information in these files is crucial for dependencies like the Daml standard library, which provide functions, types, and typeclasses.

However, as you can see above, this information isn't preserved. Furthermore, preserving this information may not even be desirable. Imagine we had built `intro7` with SDK 1.100.0, and are building `intro9` with SDK 1.101.0. All the typeclasses and instances on the inbuilt types may have changed and are now present twice -- once from the current SDK and once from the dependency. This gets messy fast, which is why the SDK does not support `dependencies` across SDK versions. For dependencies on contract models that were fetched from a ledger, or come from an older SDK version, there is a simpler kind of dependency called `data-dependencies`. The syntax for `data-dependencies` is the same, but they only rely on the "binary" `*.dalf` files. The name tries to confer that the main purpose of such dependencies is to handle data: Records, Choices, Templates. The stuff one needs to use contract composability across projects.

For an extension model like this one,`data-dependencies` are appropriate, so the current project includes `compose` that way:

You'll notice a module `Test.Intro.Asset.TradeSetup`, which is almost a carbon copy of the `compose` trade setup Scripts. `data-dependencies` is designed to use existing contracts and data types. Daml Script is not imported. In practice, we also shouldn't expect that the DAR file we download from the ledger using the Ledger API to contain test scripts. For larger projects it's good practice to keep them separate and only deploy templates to the ledger.

## About project structures

As you've seen here, identifiers depend on the package as a whole and packages always bring all their dependencies with them. Thus changing anything in a complex dependency graph can have significant repercussions. It is therefore advisable to keep dependency graphs simple, and to separate concerns which are likely to change at different rates into separate packages.

For example, in all our projects in this intro, including this chapter, our scripts are in the same project as our templates. In practice, that means changing a test changes all identifiers, which is not desirable. It's better for maintainability to separate tests from main templates. If we had done that in [Design Patterns](/docs/canton/appdev-modules-m3-design-patterns), that would also have saved us from copying those modules.

Similarly, we included `Trade` in the same project as `Asset` in [Design Patterns](/docs/canton/appdev-modules-m3-design-patterns), even though `Trade` is a pure extension to the core `Asset` model. If we expect `Trade` to need more frequent changes, it may be a good idea to split it out into a separate project from the start.

## Next up

The `MultiTrade` model has more complex control flow and data handling than previous models. In [Language Fundamentals](/docs/canton/appdev-modules-m3-language-fundamentals) you'll learn how to write more advanced logic: control flow, folds, common typeclasses, custom functions, and the Daml standard library. We'll be using the same projects so don't delete your folders just yet.

## Building with dpm

When working on Canton Network projects, use the [`dpm`](/sdks-tools/cli-tools/dpm) tool for all build operations:

* `dpm build` — Compile your Daml project and produce a DAR file
* `dpm build --all` — Build all packages in a multi-package project
* `dpm test` — Run all Daml Script tests in the current package
* `dpm codegen-java` — Generate Java bindings from your Daml model
* `dpm codegen-js` — Generate TypeScript/JavaScript bindings from your Daml model
* `dpm sandbox` — Start a local Canton sandbox for integration testing

The `dpm` tool wraps the Daml compiler and build system with Canton Network defaults, handling SDK versioning and dependency resolution automatically.

# How to build Daml Archive (.dar) files

This guide shows you how to organize the source code defining your Daml workflows and how to build and package that code as Daml Archive (.dar) files, which you can deploy to the ledger or use to develop applications against. The guide is organized into the following smaller how-tos:

* How to define and build one or more Daml packages
* How to manage dependencies on third-party Daml packages
* How to decide what Daml code to put into what package

If you would like to learn more about the exact relationship between Daml package and Daml Archive (.dar) files, see Daml packages and Daml Archive (.dar) files. However, you do not need to know this in detail to use this guide. At a high-level you can just think of a Daml archive file to be the result of building a specific Daml package.

## How to define Daml packages

### Single package

All Daml packages require a daml.yaml file. Create this file at the root of your package directory. You will need the following information to populate this file:

* SDK Version: call `dpm version` to determine the installed SDK versions
* Package name: lower-skewer-case name that is unique to your package and company.

Add the following to your `daml.yaml`, replacing the `&lt;place-holders&gt;` as appropriate.

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: <such as 3.4.9>
name: &lt;your-package-name&gt;
version: 1.0.0
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
```

The source code (`.daml` files) for the package are placed in the directory specified by the source field above. Create a daml folder at the root of your package. Write your .daml files in this directory, the file name must match the module header in the file, treating dots as directories, as shown:

* `MyModule.daml` contains `module MyModule where`
* `Path/To/My/Module.daml` contains `module Path.To.My.Module where`

Directory and .daml file names must be in UpperCamel casing.

The dpm new command provides pre-made templates for various package structures and tutorials, see this DPM page for more information.

### Multiple packages

Your Daml project will usually need at least two packages, for workflows and testing. Daml provides support for building and developing these packages via the `multi-package.yaml` file. In a directory above your package(s) directories, create a `multi-package.yaml` file. List the relative paths to your packages in this file using the following structure:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
packages:
  - ./my-package1
  - ./my-package2
```

These are paths to the directories containing the `daml.yaml`, not to the `daml.yaml` itself.

### Environment variables in configuration files

When your project has more than one package, consider using environment variables to avoid duplication of information like the `sdk-version`. Replace the `sdk-version` field with `sdk-version: $SDK_VERSION` (or any other valid environment variable name), and ensure this variable is set before building. `SDK_VERSION=3.4.9 dpm build --all`

Variables can also be placed inline, and are supported on all string fields in the daml.yaml, as the following example shows:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
sdk-version: $SDK_VERSION
name: my-package-$PACKAGE_SUFFIX
version: 1.0.$MAIN_PATCH
source: daml
dependencies:
  - daml-prim
  - daml-stdlib
```

See Environment Variable Interpolation for more information.

## How to build Daml packages

To build a single package, navigate to its root directory and run `dpm build`. To build all packages in a multi-package project, navigate to the directory containing the `multi-package.yaml` and run `dpm build --all`. By default these will create a Daml Archive (.dar) file for each package built in `&lt;package-directory&gt;/.daml/dist/&lt;package-name&gt;-&lt;package-version&gt;.dar`. .dar files are used both for uploading to the Canton Ledger, and for package dependencies. The location where the .dar is created can be overridden using the `--output` flag for dpm build, which can also be provided in the `daml.yaml` file under the `build-options` field:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
build-options:
  - --output=./output-bin/my-package.dar
```

See Daml Build Options for a full list of dpm build options, or run `dpm build --help`, which includes options for changing the LF version and configuring warnings. All of these options can also be provided via `build-options` above. Consider reading Recommended Build Options for our recommended set of warning flags.

If you face issues when changing configuration options like the `sdk-version`, or the LF version, cleaning the package(s) may help. To clean a single package, run `daml clean` from the package directory. To clean all packages in a project, run `daml clean --all` from the directory containing the `multi-package.yaml`

## How to depend on Daml packages

Dependencies in Daml are specified by their Daml Archive (.dar) file. To add a dependency to your package, add the paths to your dependency .dar files to your `daml.yaml` as follows:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
...
data-dependencies:
  - ./path/to/your/dep.dar
  - ./path/to/a/package/.daml/dist/my-package-1.0.0.dar
```

Note the use of `data-dependencies` instead of the previously covered `dependencies` field, the latter is reserved for `daml-prim`, `daml-stdlib`, and the optional testing library daml-script. Once added to the `daml.yaml`, modules from the dependency .dar can be imported from the modules of this package. In the event of collision between module names, either with this package or other dependencies, see module-prefixes.

When depending on .dar files from packages listed in the `multi-package.yaml`, calling `dpm build` and `dpm build --all` will build the relevant packages in the correct order for you.

## How to manage dependencies on third-party Daml packages

To build composed transactions, you will need to depend on the .dar files of third-party applications. At the time of writing there is no dedicated package repository for Daml Archives. However .dar files are reasonably small and change infrequently. You thus best check them into your repository, in a dars/vendored directory. If you instead retrieve the .dar files as part of a build step, check the hashes of these dars as part of this step.

If you intend to distribute your .dar files for others to build on, include the retrieval process in your documentation.

### Depending on daml-script test libraries

The `daml-script` library is not cross compatible with other releases from different Daml SDK versions. Therefore, when using Daml script test code shared by third-party apps, we recommend you to vendor in that Daml script code. For example, by checking it into a daml/vendored/ directory in your repository. A good example is the Canton Network Token Standard test harness provided by splice here: `https://github.com/DACH-NY/canton-network-node/tree/main/token-standard/splice-token-standard-test`. Adding these packages to your `multi-package.yaml` will ensure they are built as needed.

## How to decide what Daml code to put into what package

Use the following criteria to organize your project into separate packages:

**Separate workflow definitions from their tests**
Place tests for workflow definitions in a separate package to the workflows, to avoid distributing and uploading said tests to the ledger. Specifically avoid uploading the daml-script package to any production ledger.

**Separate public APIs from implementations**
If your application includes public APIs, intended to be used by other applications, define these APIs using Daml interfaces and place these interfaces in a different package to their implementation. See for example the interfaces defined in the Canton Network Token Standard here: [https://github.com/DACH-NY/canton-network-node/blob/da5dbe251b17f9c4c5d3e96840f486d14dc8e43e/token-standard/splice-api-token-holding-v1/daml/Splice/Api/Token/HoldingV1.daml](https://github.com/DACH-NY/canton-network-node/blob/da5dbe251b17f9c4c5d3e96840f486d14dc8e43e/token-standard/splice-api-token-holding-v1/daml/Splice/Api/Token/HoldingV1.daml)

**Separate by business domains**
Consider splitting workflows from different business domains into separate packages, so that stakeholders from one domain do not need to audit and vet the workflows from others domains that they do not directly interact with.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
