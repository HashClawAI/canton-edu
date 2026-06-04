---
title: "自定义配置"
slug: "global-synchronizer-deployment-configuration"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/configuration.md"
source_title: "Custom Configuration"
tags:
  - global-synchronizer
  - deployment
  - configuration
---

# 自定义配置

> Global Synchronizer 验证者节点自定义配置参数。

> Canton Network验证节点的关键配置参数

所有应用程序都有一组扩展的配置选项，可能需要根据不同的场景进行调整。这些配置以 [HOCON](https://github.com/lightbend/config/blob/main/HOCON.md) 格式接受。

## 添加临时配置

每个应用程序都通过环境变量接受额外的配置。所有传递给应用程序的以`ADDITIONAL_CONFIG`开头的环境变量都将被处理，并在应用程序启动时应用配置。

<Note>
  Example env: ADDITIONAL\_CONFIG\_EXAMPLE="canton.example.key=value"
</Note>

每个应用程序的完整配置可以在 scala 代码中观察到，与 scala 代码中的驼峰式大小写相比，配置键是 kebab 大小写：

* [ValidatorAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/validator/src/main/scala/org/lfdecentralizedtrust/splice/validator/config/ValidatorAppConfig.scala#L141)
* [SvAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/sv/src/main/scala/org/lfdecentralizedtrust/splice/sv/config/SvAppConfig.scala#L199)
* [ScanAppConfig.scala](https://github.com/canton-network/splice/blob/main/apps/scan/src/main/scala/org/lfdecentralizedtrust/splice/scan/config/ScanAppConfig.scala#L28)

此外，参与者和其他同步器组件也可以独立配置。有关此类配置的更多信息可以在 [Canton 文档](/zh/docs/canton/global-synchronizer-reference-canton-configuration-guide) 中找到。

<Note>
  Examples in the Canton docs might have different root configuration keys for the configured nodes; Splice participants/mediators/sequencers are always configured under `canton.participants.participant {`/`canton.mediators.mediator {`/`canton.sequencers.sequencer {`, respectively.
</Note>

<div className="todo">
  point to the release that these docs are built from; or inline the source code or Scaladoc to avoid confusion
</div>

## 自定义引导脚本

Canton 和 splice 都支持初始化期间的引导脚本。虽然这通常不需要，因为验证器应用程序负责初始化节点，但在某些情况下它可能很有用。为此，您需要将 `OVERRIDE_BOOTSTRAP_SCRIPT` 环境变量设置为引导脚本的内容。请注意，脚本必须包装在 `main` 函数中，例如，

```
def main() {
  logger.info(s"Participant id from bootstrap script: ${participant.id}")
}
```

您可以通过`additionalEnvVars`设置此环境变量，如下所述。

请注意，这会覆盖容器映像中包含的所有引导脚本。因此，如果您在那里添加了自定义功能，则需要在覆盖中复制此功能。

### Helm 图表支持

helm 图表可以通过值 `additionalEnvVars` 进行配置，它将值作为环境变量传递给应用程序。

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
additionalEnvVars:
    - name: ADDITIONAL_CONFIG_EXAMPLE
      value: canton.example.key=value
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
