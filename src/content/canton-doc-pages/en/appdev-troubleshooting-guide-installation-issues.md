---
title: "Installation Issues"
slug: "appdev-troubleshooting-guide-installation-issues"
locale: "en"
category: "appdev"
source_url: "https://docs.canton.network/appdev/troubleshooting-guide/installation-issues.md"
source_title: "Installation Issues"
tags:
  - appdev
  - troubleshooting-guide
  - installation-issues
---

# Installation Issues

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Installation Issues

> Troubleshooting Nix, Docker, and memory problems when setting up Canton Network development

This page covers common installation problems you may encounter when setting up a Canton Network development environment, including Nix shell failures, Docker configuration, and memory allocation.

## Nix Problems

### Nix shell fails to start

If `nix-shell` exits with a hash mismatch or download error, your local Nix cache may be stale.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Clear the Nix store cache for the affected derivation
nix-collect-garbage -d

# Retry
nix-shell
```

When `nix-shell` hangs during evaluation, check that your `NIX_PATH` is set correctly and that no conflicting Nix channels exist:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
nix-channel --list
```

Remove any unexpected channels and re-run `nix-shell`.

### "command not found: nix" after installation

Your shell profile may not source the Nix environment. Add the following to your `~/.bashrc` or `~/.zshrc`:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
source ~/.nix-profile/etc/profile.d/nix.sh
```

Alternatively, restart your terminal session entirely. On macOS, after a system update Nix sometimes needs reinstallation:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Uninstall first
/nix/nix-installer uninstall

# Reinstall from https://nixos.org/download
```

### PATH conflicts between Nix and system packages

If a system-installed tool (e.g., a different Java version) takes precedence over the Nix-provided one, verify your PATH ordering:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
which java
# Should point to /nix/store/... if using nix-shell
```

Inside `nix-shell`, Nix prepends its paths to `$PATH`. If you still see system binaries, check whether your shell profile appends paths after Nix or overrides them.

## Docker Configuration

### Insufficient memory for LocalNet

LocalNet runs a full Canton topology locally and needs significant resources. If containers crash with OOM (Out of Memory) kills or fail to start, increase Docker's memory allocation.

**Minimum requirements for LocalNet:**

* Memory: 16 GB
* CPU: 4 cores
* Disk: 50 GB free

**Docker Desktop:** Settings > Resources > set Memory to 16 GB or higher, then Apply & Restart.

**Colima (macOS):**

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
colima stop
colima start --memory 16 --cpu 4
```

### Volume mount permission errors

On Linux, Docker containers may fail to write to mounted volumes if your user ID does not match the container's expected UID. Fix this by ensuring the host directory has appropriate permissions:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
chmod -R 777 .data/
```

Or run Docker with the `--user` flag matching your host UID:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose run --user "$(id -u):$(id -g)" <service>
```

### Docker Compose version mismatch

Canton Quickstart requires Docker Compose 2.26.0 or higher. If you see:

```
'env_file[1]' expected type 'string', got unconvertible type 'map[string]interface {}'
```

Upgrade Docker Compose:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker compose version  # Check current version

# macOS with Homebrew
brew install docker-compose

# Or update Docker Desktop to the latest version
```

## Memory Allocation

### JVM heap for sandbox

The Daml sandbox runs on the JVM and defaults to conservative heap settings. If you encounter `java.lang.OutOfMemoryError: Java heap space`, increase the heap:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
export JAVA_OPTS="-Xmx4g -Xms2g"
dpm sandbox
```

### OOM kills on LocalNet

When Docker kills containers silently, check for OOM events:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
docker inspect <container_name> --format='{{.State.OOMKilled}}'
```

If this returns `true`, you need to increase Docker's memory allocation (see the Docker section above). You can also check system-level OOM events:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dmesg | grep -i "out of memory"
```

### Resource limits summary

| Environment   | Min Memory | Recommended Memory | Min CPU |
| ------------- | ---------- | ------------------ | ------- |
| Sandbox only  | 4 GB       | 8 GB               | 2 cores |
| LocalNet      | 16 GB      | 24 GB              | 4 cores |
| cn-quickstart | 8 GB       | 16 GB              | 4 cores |

<Note>
  Before running cn-quickstart, you must execute `make setup` and `make build` before `make start`. Skipping these steps causes startup failures that can look like resource problems.
</Note>

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
