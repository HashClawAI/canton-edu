---
title: "Advanced Canton Console"
slug: "global-synchronizer-production-operations-canton-console"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/canton-console.md"
source_title: "Advanced Canton Console"
tags:
  - global-synchronizer
  - production-operations
  - canton-console
---

# Advanced Canton Console

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Advanced Canton Console

> Use the Canton admin console for advanced operations on participant and synchronizer nodes.

# Canton Console

Canton offers a console (REPL) where entities can be dynamically started and stopped, and a variety of administrative or debugging commands can be run.

All console commands must be valid Scala (the console is built on [Ammonite]() - a Scala-based scripting and [REPL]() framework). Note that we also define a set of implicit type [conversions]() to improve the console usability: notably, whenever a console command requires a [SynchronizerAlias](), [Fingerprint]() or [Identifier](), you can instead also call it with a `String` which will be automatically converted to the correct type.

The `examples/` sub-directories contain some sample scripts, with the extension `.canton`.

<div className="contents" local="">
  Contents
</div>

Commands are organized by thematic groups. Some commands also need to be explicitly turned on via configuration directives to be accessible.

Some operations are available on both types of nodes, whereas some operations are specific to either participant nodes or synchronizers. For consistency, we organize the manual by node type, which means that some commands will appear twice. However, the detailed explanations are only given within the participant documentation.

## Remote Administration

The Canton console works with both local in-process nodes and remote nodes. Once you've configured the network address, port, and authentication information, you can use a single Canton console to administer all the nodes in your system.

As an example, you might have previously started a Canton instance in daemon mode using something like the following:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton daemon -c <some config>
```

You can then execute commands against this up-and-running participant using a `remote-participant` configuration such as:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Example remote participant configuration

// Include TLS configuration
include required("../tls/mtls-admin-api.conf")
include required("../tls/tls-ledger-api.conf")
canton {
    remote-participants.participant {
        ledger-api {
            address = localhost
            port = 10001
            tls = ${?_shared.ledger-api-client-tls}
        }
        admin-api {
            address = localhost
            port = 10002
            tls = ${?_shared.admin-api-client-mtls}
        }
    }
}
```

Given a remote config file, start a local Canton console configured to execute commands on a remote Canton instance like this:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c config/remote-participant1.conf
```

Additionally, you can use the remote configuration to run a script:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run &lt;some-canton-script&gt; -c config/remote-participant1.conf
```

Note that most Canton commands can be executed from a remote console. However, a few commands can only be called from the local console of the node itself.

Given a participant's config file, you can generate a skeleton remote config file using the `generate` command:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton generate remote-config -c participant1.conf
```

Depending on your network, you might need to manually edit the auto-generated configuration to adjust the hostname. To access multiple remote nodes, consolidate the auto-generated configurations into a single remote configuration file or include all configuration files on the command line:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c participant1.conf,participant2.conf,mysynchronizer.conf
```

### TLS and Authorization

For production use cases, in particular if the Admin API is not just bound to localhost, we recommend to enable TLS with mutual authentication.

The remote console can be used in installations that utilize authorization, so long as it has a valid access token. This can be achieved by modifying the configuration or by adding an option to the remote console's launch command as in the following snippet:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton daemon \
   -c remote-participant1.conf \
   -C canton.remote-participants.&lt;remote-participant-name&gt;.token="&lt;encoded-and-signed-access-token-as-string&gt;" \
   --bootstrap &lt;some-script&gt;
```

The remote console uses the token in its interactions with the Ledger API of the target participant. It also extracts the user ID from the token and uses it to populate the userId field in the command submission and completion subscription requests. This affects the following console commands:

* ledger\_api.commands.submit
* ledger\_api.commands.submit\_flat
* ledger\_api.commands.submit\_async
* ledger\_api.completions.list
* ledger\_api.completions.list\_with\_checkpoint
* ledger\_api.completions.subscribe

<div className="todo">
  \#22917: Fix broken ref note:: If you want to know more about the authorization please read the following article about the ref:authorization tokens
</div>

## Node References

To issue the command on a particular node, you must refer to it via its reference, which is a Scala variable. Named variables are created for all synchronizer entities and participants using their configured identifiers. For example, the sample `examples/01-simple-topology/simple-topology.conf` configuration file references the synchronizer `mysynchronizer`, and participants `participant1` and `participant2`. These are available in the console as `mysynchronizer`, `participant1` and `participant2`.

The console also provides additional generic references that allow you to consult a list of nodes by type. The generic node reference supports three subsets of each node type: local, remote or all nodes of that type. For the participants, you can use:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.local
participants.remote
participants.all
```

The generic node references can be used in a Scala syntactic way:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.all.foreach(_.dars.upload("my.dar"))
```

but the participant references also support some generic commands for actions that often have to be performed for many nodes at once, such as:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participants.local.dars.upload("my.dar")
```

The available node references are:

\<console-topic-marker: Generic Node References>

## Help

Canton can be very helpful if you ask for help. Try to type

help

or

participant1.help()

to get an overview of the commands and command groups that exist. `help()` works on every level (e.g. `participant1.synchronizers.help()`) or can be used to search for particular functions (`help("list")`) or to get detailed help explanation for each command (`participant1.parties.help("list")`).

## Lifecycle Operations

These are supported by individual and sequences of synchronizers and participants. If called on a sequence, operations will be called sequentially in the order of the sequence. For example:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nodes.local.start()
```

can be used to start all configured local synchronizers and participants.

If the node is running with database persistence, it will support the database migration command (`db.migrate`). The migrations are performed automatically when the node is started for the first time. However, new migrations added as part of new versions of the software must be by default run manually using the command. In some rare cases, it may also be necessary to run `db.repair_migration` before running `db.migrate` - please refer to the description of `db.repair_migration` for more details. If desired, the database migrations can be performed also automatically by enabling the "migrate-and-start" mode using the following configuration option:

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.storage.parameters.migrate-and-start = yes

```

Note that data continuity (and therefore database migration) is only guaranteed to work across minor and patch version updates.

The synchronizer, sequencer and mediator nodes might need extra setup to be fully functional. Check synchronizer bootstrapping for more details.

## Timeouts

Console command timeouts can be configured using the respective console command timeout section in the configuration file:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters.timeouts.console = {
    bounded = 2.minutes
    unbounded = Inf // infinity
    ledger-command = 2.minutes
    ping = 30.seconds
}
```

The `bounded` argument is used for all commands that should finish once processing has completed, whereas the `unbounded` timeout is used for commands where we do not control the processing time. This is used in particular for potentially very long-running commands.

Some commands have specific timeout arguments that can be passed explicitly as type `NonNegativeDuration`. For convenience, the console includes by default the implicits of `scala.concurrent.duration._` and an implicit conversion from the Scala type `scala.concurrent.duration.FiniteDuration` to `NonNegativeDuration`. As a result, you can use normal Scala expressions and write timeouts as

participant1.health.ping(participant1, timeout = 10.seconds)

while the implicit conversion will take care of converting it to the right types.

Generally, there is no need to reconfigure the timeouts and we recommend using the safe default values.

## Code-Generation in Console

The Daml SDK provides code-generation [utilities]() which create **Java** or **Scala** bindings for Daml models. These bindings are a convenient way to interact with the ledger from the console in a typed fashion. The linked documentation explains how to create these bindings using the `daml` command. The **Scala** bindings are not officially supported, so should not be used for application development.

Once you have successfully built the bindings, you can then load the resulting `jar` into the Canton console using the magic **Ammonite** import trick within console scripts:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
interp.load.cp(os.Path("codegen.jar", base = os.pwd))

@ // the at triggers the compilation such that we can use the imports subsequently

import ...
```

## Canton Administration APIs

Canton provides the console as a builtin mode for administrative interaction. However, under the hood, all administrative console actions are effected using the administration gRPC API. Therefore, it is also possible to write your own administration application and connect it to the administration gRPC endpoints.

The `protobuf/` sub-directories in the release artifacts contain the gRPC underlying protocol buffers. In particular, the administrative gRPC APIs are located within the `admin` sub-directories.

For example, the Ping Pong Service which implements a simple workflow to smoke-test a deployment is defined with the protocol buffer `*/protobuf/*/admin/*/ping_pong_service.proto` (where `*` denotes intermediary directories). This service is then used by the console command health.ping.

The protocol buffers are also available within the [repository]() following a similar sub-directory structure as mentioned.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
