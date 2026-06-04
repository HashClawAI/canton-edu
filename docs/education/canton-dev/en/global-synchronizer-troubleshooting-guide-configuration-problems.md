---
title: "Configuration Problems"
slug: "global-synchronizer-troubleshooting-guide-configuration-problems"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/troubleshooting-guide/configuration-problems.md"
source_title: "Configuration Problems"
tags:
  - global-synchronizer
  - troubleshooting-guide
  - configuration-problems
---

# Configuration Problems

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuration Problems

> Diagnosing HOCON parsing errors, permission issues, and environment variable conflicts

Configuration errors are among the most common reasons a validator fails to start. They range from HOCON syntax mistakes to subtle environment variable conflicts.

## HOCON Parsing Errors

Canton uses HOCON (Human-Optimized Config Notation) for its configuration files. Syntax errors prevent the validator from starting and produce messages like:

```
com.typesafe.config.ConfigException$Parse: ... Expecting close brace } or a comma
```

**Common mistakes and fixes:**

* **Missing closing brace.** HOCON files can be deeply nested. Use an editor that highlights matching braces, or run a linter before deploying.

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Wrong -- missing closing brace
canton {
  participants {
    participant {
      storage {
        type = postgres
      }
    # <-- missing }
}
```

* **Unquoted special characters.** Values containing `://`, `=`, or `#` must be quoted.

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Wrong
url = https://sequencer.sync.global:443

# Correct
url = "https://sequencer.sync.global:443"
```

* **Wrong value types.** If the schema expects a duration and you provide an integer without a unit, parsing fails.

```hocon theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Wrong
timeout = 30

# Correct
timeout = 30s
```

* **Trailing commas.** HOCON is more forgiving than JSON, but some constructs still break on trailing commas inside arrays.

To validate a HOCON file before applying it:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Quick check using the JVM-based typesafe-config library
java -cp "canton.jar" com.typesafe.config.impl.Parseable < your-config.conf
```

## File Permission Issues

The validator process must be able to read its configuration files. On Linux and in containers, this often means adjusting ownership or permissions.

```
java.io.FileNotFoundException: /etc/canton/participant.conf (Permission denied)
```

Fix:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Ensure the canton user (UID 1000) can read the file
chmod 644 /etc/canton/participant.conf
chown 1000:1000 /etc/canton/participant.conf
```

### Kubernetes Secrets Not Mounted

If a configuration file references a Kubernetes Secret that is not mounted into the pod, the validator fails with a `FileNotFoundException` on the expected path. Verify:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Check that the secret exists
kubectl get secret validator-config -n validator

# Check the pod spec for volume mounts
kubectl get pod -n validator -o yaml | grep -A5 volumeMounts
```

Common causes:

* The secret name in the Helm values does not match the actual secret name.
* The secret was created in a different namespace.
* A `subPath` mount is pointing to a key that does not exist in the secret.

## Environment Variable Conflicts

Canton and Splice components read configuration from both files and environment variables. When both are set, environment variables take precedence, which can produce unexpected behavior.

### `DPM_SDK_VERSION` Overriding `daml.yaml`

If you set `DPM_SDK_VERSION` as an environment variable, it overrides the `sdk-version` field in your project's `daml.yaml`. This can cause version mismatch errors during builds:

```
Error: SDK version 3.3.0 from environment does not match 3.2.0 in daml.yaml
```

Fix: unset the environment variable or align it with `daml.yaml`:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
unset DPM_SDK_VERSION
```

### Conflicting `.env` Files

Docker Compose loads `.env` from the working directory. If you have multiple `.env` files (e.g., from a previous deployment), stale values can override current configuration.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Show which .env file Docker Compose is using
docker compose config | head -20
```

Check for variables that might conflict:

* `SPLICE_APP_VERSION` -- must match the Helm chart or Docker image version
* `PARTICIPANT_HOST` -- must resolve from inside the container, not just from the host
* `AUTH_URL` -- must be reachable from the validator container

### Debugging Configuration Resolution

To see the final merged configuration that Canton will use:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Print resolved config (redacts secrets)
docker exec validator-app cat /proc/1/environ | tr '\0' '\n' | sort
```

For HOCON files, Canton logs the resolved configuration at `DEBUG` level on startup. Temporarily set `canton.monitoring.logging.api.level = DEBUG` to capture it.

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
