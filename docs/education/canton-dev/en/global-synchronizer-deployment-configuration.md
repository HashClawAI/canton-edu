---
title: "Custom Configuration"
slug: "global-synchronizer-deployment-configuration"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/configuration.md"
source_title: "Custom Configuration"
tags:
  - global-synchronizer
  - deployment
  - configuration
---

# Custom Configuration

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Custom Configuration

> Key configuration parameters for Canton Network validator nodes

All the apps have an extended set of configuration options which might need tuning based on different scenarios. These configurations are accepted in the [HOCON](https://github.com/lightbend/config/blob/main/HOCON.md) format.

## Adding ad-hoc configuration

Every app accepts extra configuration through environment variables. All the environment variables passed to the apps, that start with `ADDITIONAL_CONFIG` will be processed and the configuration will be applied when the app starts.

<Note>
  Example env: ADDITIONAL\_CONFIG\_EXAMPLE="canton.example.key=value"
</Note>

The full configuration for each app can be observed in the scala code, with the configuration key being kebab case compared to the camel case in the scala code:

* [ValidatorAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/validator/src/main/scala/org/lfdecentralizedtrust/splice/validator/config/ValidatorAppConfig.scala#L141)
* [SvAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/sv/src/main/scala/org/lfdecentralizedtrust/splice/sv/config/SvAppConfig.scala#L199)
* [ScanAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/scan/src/main/scala/org/lfdecentralizedtrust/splice/scan/config/ScanAppConfig.scala#L28)

Furthermore, the participant and other synchronizer components can be configured independently as well. Further information on such configurations can be found in the [Canton docs](/global-synchronizer/reference/canton-configuration-guide).

<Note>
  Examples in the Canton docs might have different root configuration keys for the configured nodes; Splice participants/mediators/sequencers are always configured under `canton.participants.participant {`/`canton.mediators.mediator {`/`canton.sequencers.sequencer {`, respectively.
</Note>

<div className="todo">
  point to the release that these docs are built from; or inline the source code or Scaladoc to avoid confusion
</div>

## Custom bootstrap scripts

Both Canton and splice support bootstrap scripts during initialization. While this usually should not be needed as the validator app takes care of initializing the node, in some scenarios it can be useful. To do so, you need to set the `OVERRIDE_BOOTSTRAP_SCRIPT` environment variable to the content of your bootstrap script. Note that the script must be wrapped in a `main` function, e.g.,

```
def main() {
  logger.info(s"Participant id from bootstrap script: ${participant.id}")
}
```

You can set this environment variable through `additionalEnvVars` as described below.

Note that this overwrites any bootstrap scripts baked into the container image. So if you added custom functionality there, you will need to replicate this in the overwrite.

### Helm charts support

The helm charts can be configured through the value `additionalEnvVars`, which passes the values as environment variables to the apps.

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_EXAMPLE
      value: canton.example.key=value
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
