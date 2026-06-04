---
title: "IDE Setup"
slug: "appdev-tooling-ide-setup"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/tooling/ide-setup.md"
source_title: "IDE Setup"
tags:
  - appdev
  - tooling
  - ide-setup
---

# IDE Setup

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# IDE Setup

> Configure VS Code and other IDEs for Canton application development with Daml, Java, and full-stack tooling

A properly configured IDE makes Canton development significantly faster. This page covers setup for writing Daml contracts, building backend services, and working with the full application stack.

## Daml Studio (VS Code)

Daml Studio is the primary IDE for writing Daml smart contracts. It is a VS Code extension that provides language support purpose-built for Daml.

### Installation

1. Install [VS Code](https://code.visualstudio.com/) version 1.87 or later
2. Install [DPM](/sdks-tools/cli-tools/dpm) if you have not already
3. From your project directory, run:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm studio
```

This launches VS Code with the Daml extension configured for your project. Alternatively, search for "Daml" in the VS Code extensions marketplace and install it manually.

### Features

**Type checking** runs continuously as you edit. Errors and warnings appear inline, and the Problems panel shows a summary. Type checking catches most issues before you ever run a test.

**Script results** let you execute Daml Scripts directly from the editor. Click the "Script results" lens that appears above any script definition. The results panel shows the ledger state as a table: active contracts, archived contracts, and the transaction trace. This is the fastest way to verify that your contract logic behaves as expected.

**Go-to-definition** works for templates, choices, type definitions, and imported modules. Use `Ctrl+Click` (or `Cmd+Click` on macOS) on any identifier.

**Code completion** suggests template fields, choice parameters, standard library functions, and imported names as you type.

### Troubleshooting Daml Studio

If type checking is not working:

* Verify that `dpm build` succeeds from the command line. If the build fails, the IDE cannot type-check.
* Check that your `daml.yaml` file lists the correct SDK version and source directory.
* Restart the Daml language server: open the VS Code command palette (`Ctrl+Shift+P`) and run "Daml: Restart Language Server".

## Java and Scala Backend Development

If your backend is in Java or Scala (common for Canton applications using the Java bindings), IntelliJ IDEA provides the best experience.

### IntelliJ Setup

1. Install [IntelliJ IDEA](https://www.jetbrains.com/idea/) (Community or Ultimate edition)
2. Open your project. If using Maven or Gradle, IntelliJ auto-detects the build system.
3. After running `dpm codegen-java`, mark the generated code directory as a source root so IntelliJ indexes the generated classes.

IntelliJ provides type-safe navigation into the generated Daml Java bindings, which makes it straightforward to trace from your backend code into the contract definitions.

### TypeScript Backend Development

For TypeScript backends (as in cn-quickstart), VS Code is the natural choice. After running `dpm codegen-js`, the generated TypeScript types integrate with VS Code's built-in TypeScript language service for autocompletion and type checking.

## Recommended VS Code Extensions

Beyond Daml Studio, these extensions are useful for Canton full-stack development:

* **Daml** -- Daml language support (required)
* **YAML** (Red Hat) -- Syntax support for `daml.yaml`, `docker-compose.yml`, and configuration files
* **Docker** (Microsoft) -- Manage Docker containers, useful for LocalNet
* **Kubernetes** (Microsoft) -- Helpful if deploying to Kubernetes
* **ESLint** -- Linting for TypeScript/JavaScript frontend and backend code
* **Prettier** -- Code formatting for TypeScript, JSON, and YAML
* **GitLens** -- Enhanced Git integration

## Project-Level Configuration

For team consistency, consider adding a `.vscode/extensions.json` to your repository recommending the Daml extension:

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "recommendations": [
    "DigitalAssetHoldingsLLC.daml"
  ]
}
```

You can also add a `.vscode/settings.json` with project-specific settings like file associations and editor formatting rules.

## Next Steps

* [Development Tools Overview](/docs/canton/appdev-tooling-development-tools-overview) -- Summary of all Canton development tools
* [Development Environment Setup](/docs/canton/appdev-modules-m3-dev-environment) -- Getting started with Daml development
* [Debugging Tools](/docs/canton/appdev-tooling-debugging-tools) -- Troubleshoot issues during development

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
