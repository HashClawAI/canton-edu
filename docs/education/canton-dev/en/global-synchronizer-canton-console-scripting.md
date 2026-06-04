---
title: "Scripting"
slug: "global-synchronizer-canton-console-scripting"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/scripting.md"
source_title: "Scripting"
tags:
  - global-synchronizer
  - canton-console
  - scripting
---

# Scripting

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Scripting

> Writing scripts for the Canton console using Scala

The Canton console is built on [Ammonite](http://ammonite.io), a Scala-based scripting and REPL framework. Every command you type is valid Scala, which means you can write loops, define functions, bind variables, and compose operations just as you would in any Scala program.

This page covers the practical side of scripting: how to write `.canton` script files, how to run them, and common patterns for automating operator tasks.

## Scala basics in the console

The console accepts standard Scala syntax. A few patterns come up repeatedly in operator scripts.

**Variable binding**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val id = participant1.id
    id : ParticipantId = PAR::participant1::12201ff69b1d...
```

**String interpolation**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ println(s"Participant ID: $id")
```

**Collections and iteration**

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participants.all.foreach { p => println(s"${p.name}: ${p.health.status}") }
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.status match { case status if status.isActive.contains(true) => println("Healthy"); case _ => println("Check this node") }
```

The console also provides implicit type conversions for convenience. When a command expects a `SynchronizerAlias`, `Fingerprint`, or `Identifier`, you can pass a plain `String` and it will be converted automatically.

## Loading and running script files

Canton scripts use the `.canton` file extension by convention. You can run them in two ways.

**Run a script at startup**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run myscript.canton -c myconfig.conf
```

This starts the console, executes the script, and exits. It is the standard approach for unattended automation.

**Load a script inside the console**

From an interactive session, load a script file with Ammonite's `interp.load` mechanism or the `utils` helper:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
utils.run_script("path/to/myscript.canton")
```

You can also load compiled JARs (for example, Daml codegen bindings) into the console:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
interp.load.cp(os.Path("codegen.jar", base = os.pwd))

@ // the @ triggers compilation so imports are available afterward

import com.myorg.mypackage._
```

**Bootstrap scripts**

A bootstrap script runs automatically when the console starts:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton -c myconfig.conf --bootstrap myscript.canton
```

Unlike `run`, the console stays open after the bootstrap script completes, which is useful for setting up initial state and then switching to interactive use.

## Timeouts

Console command timeouts are configured in the Canton configuration file:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.parameters.timeouts.console {
  bounded = 1.minute
  unbounded = 10.minutes
}

```

* `bounded` applies to commands that are expected to complete within a known duration.
* `unbounded` applies to long-running commands where completion time is unpredictable.

You can also pass timeouts directly in script commands:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.health.ping(participant1, timeout = 30.seconds)
    res5: Duration = 1875 milliseconds
```

The console imports `scala.concurrent.duration._` by default, so expressions like `10.seconds` and `1.minute` work without additional imports.

## Automation patterns

### Health checks

A simple health check script that verifies all local nodes are running:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ nodes.local.foreach { node => val status = node.health.status; if (!status.isActive.getOrElse(false)) { println(s"WARNING: ${node.name} is not active") } }
```

For a targeted ping test between two participants:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val roundTrip = participant1.health.ping(participant2, timeout = 30.seconds)
    roundTrip : Duration = 1823 milliseconds
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ println(s"Round trip: ${roundTrip}")
```

### Batch operations

Upload a DAR to all local participants:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res9: String = "8287d565fd2ff8ed827bcea37cee0b66edd7278fe0d712abbce3fbb7313a1e25"
```

The generic node references (`participants.local`, `participants.remote`, `participants.all`) support batch operations directly. You can also iterate when you need more control:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participants.all.foreach { p => println(s"DARs on ${p.name}: ${p.dars.list().size}") }
```

### Scheduled tasks with external orchestration

The Canton console does not include a built-in scheduler. For recurring tasks, call your `.canton` scripts from an external scheduler such as `cron` or a Kubernetes CronJob:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# crontab entry: run health check every 5 minutes
*/5 * * * * /opt/canton/bin/canton run /opt/canton/scripts/health-check.canton -c /opt/canton/config/remote-participant.conf
```

This approach keeps automation logic in version-controlled `.canton` files while relying on battle-tested scheduling infrastructure.

## Common scripting recipes

### List connected synchronizers

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.list_connected().foreach { sync => println(s"Connected to: ${sync.synchronizerAlias}") }
```

### Check party hosting

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.parties.list().foreach { party => println(s"Party: ${party.party}") }
```

### Export and import DARs

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Export all DARs to a directory
participant1.dars.download("backup/dars/")

// Upload a DAR
participant1.dars.upload("backup/dars/my-model.dar")
```

### Remote administration

If your nodes run as daemons, you can script against them from a remote console. Configure a remote participant in your config:

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
  admin-api {
    address = "participant-host"
    port = 5012
  }
  ledger-api {
    address = "participant-host"
    port = 5011
  }
}
```

Then run scripts against the remote node:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
./bin/canton run myscript.canton -c remote-config.conf
```

<Note>
  Some commands are only available from the local console of the node process itself. Remote consoles cover most administrative operations, but a few low-level operations require local access.
</Note>

## Tips for production scripts

* Always specify explicit timeouts rather than relying on defaults. A script that hangs indefinitely is harder to diagnose than one that fails fast.
* Use `try/catch` blocks around operations that might fail, especially network calls and DAR uploads.
* Log output with `println` or write to files -- the console does not persist output by default.
* Keep scripts idempotent where possible. If a script is safe to re-run, recovery from partial failures is straightforward.
* Test scripts against a LocalNet environment before running them in production.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
