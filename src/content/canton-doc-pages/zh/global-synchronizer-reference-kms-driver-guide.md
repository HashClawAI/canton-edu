---
title: "KMS 驱动开发指南"
slug: "global-synchronizer-reference-kms-driver-guide"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/kms-driver-guide.md"
source_title: "Canton KMS Driver Developer Guide"
tags:
  - global-synchronizer
  - reference
  - kms-driver-guide
---

# KMS 驱动开发指南

> 开发自定义 Canton KMS Driver 的开发者指南。

> 开发自定义 Canton KMS 驱动程序。


## 简介

Canton 协议依赖于非对称加密和数字签名等加密操作。为了最大限度地提高 Canton 节点的运行安全性，相应的私钥不应以明文形式存储或处理。密钥管理系统 (KMS) 或硬件安全模块 (HSM) 允许您执行此类加密操作，其中私钥安全地驻留在 KMS/HSM 内。 Canton 内的所有节点都可以使用 KMS。

自 Canton v2.7 起支持 AWS KMS 和 Google Cloud KMS。为了扩大对其他 KMS 和 HSM 的支持，Canton v2.9 引入了一种称为 KMS 驱动程序的插件方法，它允许实施自定义集成。本文档解释了 KMS 驱动程序必须实现的 API，提供了实现指南，并描述了如何配置 Canton 以与 KMS 驱动程序一起运行。目前，KMS 驱动程序仅在 Scala 实现中可用。

您可以在 Canton 社区存储库中找到基于软件加密库构建的“模拟”KMS 驱动程序实现。

## KMS 驱动程序 API

KMS 驱动程序所需的两个主要 API 是：

* Driver Factory：实现驱动程序如何实例化；和主条目
  点让 Canton 加载驱动程序。

* KMS驱动程序：提供基于KMS的加密操作。

稳定的 API 使用单一主版本号进行版本控制。对工厂或驱动程序 API 的重大更改会导致这些 API 出现新的主要版本。当前且唯一的版本是 **v1**，它是各个 API 接口的模块路径的一部分。

### KMS 驱动程序工厂 API v1

该工厂由两个接口组成：通用 v1 DriverFactory 和特定 v1 KmsDriverFactory。

`v1.DriverFactory` 为通用驱动程序定义了以下方面：

* 驱动程序类型
* 唯一标识驱动程序的名称
* 驱动程序实现的 API 版本和可选的构建信息（驱动程序版本号或提交哈希）
* 具有配置解析器和编写器的特定于驱动程序的配置对象
* 使用该工厂实例化驱动程序的创建方法

具体来说，Scala 中的接口定义如下：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

package com.digitalasset.canton.driver.api.v1

import com.digitalasset.canton.driver.api
import org.slf4j.Logger
import pureconfig.{ConfigReader, ConfigWriter}

import scala.concurrent.ExecutionContext

/** The corresponding factory for an implementation of a [[Driver]] that can instantiate a new
  * driver.
  */
trait DriverFactory extends api.DriverFactory {

  /** The name of the driver that is instantiated by an implementation of the driver factory. */
  def name: String

  /** The version of the driver API this factory is implemented against. */
  def version: Int

  /** Optional information for the build of the driver factory, e.g., git commit hash. */
  def buildInfo: Option[String]

  /** The driver-specific configuration type. */
  type ConfigType

  /** The parser to load the driver-specific configuration. */
  def configReader: ConfigReader[ConfigType]

  /** The configuration writer for the driver-specific configuration.
    *
    * @param confidential
    *   If the flag is true, the config writer should omit any sensitive configuration items, such
    *   as credentials.
    */
  def configWriter(confidential: Boolean): ConfigWriter[ConfigType]

  /** The creation method of a driver by this factory. If the creation of the driver fails this
    * method should throw an exception.
    *
    * @param config
    *   The driver-specific configuration.
    * @param loggerFactory
    *   A logger factory that should be used by the driver to create a logger for a particular
    *   class.
    * @param executionContext
    *   The execution context that should be used by the driver.
    *
    * @return
    *   A new instance of [[Driver]].
    */
  def create(
      config: ConfigType,
      loggerFactory: Class[?] => Logger,
      executionContext: ExecutionContext,
  ): Driver
}
```

`v1.KmsDriverFactory` 是通用 DriverFactory 的特化，它将驱动程序类型定义为 KmsDriver，将 API 版本定义为 1。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

package com.digitalasset.canton.crypto.kms.driver.api

import com.digitalasset.canton.driver.api.DriverFactory

trait KmsDriverFactory extends DriverFactory {
  override type Driver <: KmsDriver
}
```

####驱动配置读取&解析

Canton 使用 [pureconfig](https://github.com/pureconfig/pureconfig) 配置库来读取其配置。由于驱动程序的配置可以嵌入 Canton 配置文件中，因此驱动程序的工厂需要指定配置的类型以及配置读取器和写入器。 `ConfigType` 可以是案例类，也可以与 `Map[String, String]` 一样基本。在后一种情况下，配置读取器和写入器可以定义为：

* `val configReader = pureconfig.ConfigReader.mapReader[String]`
* `val configWriter = pureconfig.ConfigWriter.mapWriter[String]`

### KMS 驱动程序 API v1

API 的主要部分是`v1.KmsDriver` API，它为 KMS 驱动程序定义了以下操作：

* 密钥生成：非对称签名和加密密钥对以及对称加密密钥
* 支持的密钥和算法规格：驱动程序支持的规格，例如 RSA 2048 密钥和 RSA OAEP SHA256 非对称加密。
* 签名：使用 KMS 中的密钥和指定的算法对数据进行签名。
* 非对称解密：用KMS中的私钥和指定的算法解密密文。
* 对称加密和解密：使用来自 KMS 的对称加密密钥进行加密或解密。使用KMS默认的对称加密算法。
* 密钥管理：获取KMS中存储的私钥的公钥、检查密钥是否存在、删除密钥。
* Health：返回KMS Driver实例的健康状况。

该 API 被设计为使用 Futures 的异步 API。 OpenTelemetry 跟踪上下文从 Canton 传递到 KMS 驱动程序操作中，以便能够将 Canton 请求链接到 KMS 中的操作。驱动程序负责将跟踪上下文传播到 KMS 中。

具体来说，Scala接口定义如下：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// Copyright (c) 2025 Digital Asset (Switzerland) GmbH and/or its affiliates. All rights reserved.
// SPDX-License-Identifier: Apache-2.0

package com.digitalasset.canton.crypto.kms.driver.api

trait KmsDriver
```

### 错误处理和健康状况

如果驱动程序遇到错误，操作的 `Future` 将会失败，并显示 `KmsDriverException`。当异常的标志可重试为 true 时，调用方（即 Canton）将执行指数退避重试。此行为适用于暂时性错误，例如网络问题、资源耗尽等。

如果出现永久性错误，则应抛出不可重试的异常，这要么使调用加密操作的当前操作失败，要么导致 Canton 节点出现致命错误。

驱动程序应通过健康方法报告其健康状况。 Canton 节点定期查询驱动程序的健康状况并将其报告为节点整体健康状况的一部分。

## 开发并测试 KMS 驱动程序

### 设置 API 依赖关系

Canton KMS 驱动程序 API 作为工件发布在 Digital Asset 的 JFrog Artifactory 上：

[https://digitalasset.jfrog.io/ui/repos/tree/General/canton-kms-driver-api](https://digitalasset.jfrog.io/ui/repos/tree/General/canton-kms-driver-api)

您必须拥有Canton企业许可证和帐户才能访问该工件。您可能需要配置构建系统以使用 JFrog Artifactory 的个人访问令牌进行身份验证。

在您选择的构建系统中，您需要将 API 作为常规 Maven 风格的工件来依赖：

* 组织：com.digitalasset.canton
*神器：kms-driver-api
* version：Canton发布版本，例如3.3.0

### 实现 API 并构建驱动程序

通过指定驱动程序的名称、读取器/写入器的配置类型以及通过创建 `KmsDriver` 实现的新类实例来实例化驱动程序的创建方法来实现 `v1.KmsDriverFactory`。在文件中指定工厂类的完全限定名称：`src/main/resources/META-INF/services/com.digitalasset.canton.crypto.kms.driver.api.v1.KmsDriverFactory`

以及基本驱动程序工厂的以下文件（不带 v1）：

`src/main/resources/META-INF/services/com.digitalasset.canton.crypto.kms.driver.api.KmsDriverFactory`

实现的主要部分是特定于要集成的 KMS/HSM 的`v1.KmsDriver`。可以根据底层 KMS/HSM 的功能静态定义支持的密钥和算法规范。为了确保与其他 Canton 节点的最佳兼容性，应支持所有当前指定的密钥和算法规范。

底层 KMS/HSM 所需的任何凭据都可以作为特定于驱动程序的配置的一部分通过 Canton 配置文件传递，其中机密可以从环境中解析，或者由驱动程序直接从环境或任何其他特定于驱动程序的方式检索。

将您的驱动程序捆绑到一个独立的 jar 中，即所有必需的库都包含在该 jar 中。这样，当使用 KMS 驱动程序启动 Canton 时，您只需要一个驱动程序 jar。

### KMS 驱动程序测试

KMS 驱动程序的可重用测试套件发布于 [canton-kms-driver-testing]()。配置您的构建系统以在项目的测试范围内依赖此 Maven 工件（例如，对于 sbt 附加 % Test 以限制对测试范围的依赖）。

#### KmsDriver测试

测试套件的主要部分是`KmsDriverTest`，它根据`KmsDriver` API 测试驱动程序的功能。

以最简单的形式，特定的驱动程序测试类扩展了 `KmsDriverTest` 并允许生成新密钥作为测试的一部分：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
class AwsKmsDriverTest extends KmsDriverTest {

  override protected def newKmsDriver(): KmsDriver = {
    val awsKms = AwsKms
      .create(
        KmsConfig.Aws.defaultTestConfig,
        timeouts,
        loggerFactory,
        NoReportingTracerProvider,
      )
      .valueOrFail("failed to create AWS KMS")

    new AwsKmsDriver(awsKms)
  }

  "AWS KMS Driver" must {
    behave like kmsDriver(allowKeyGeneration = true)
  }

}
```

在开发过程中运行测试时，生成新密钥的成本可能会很高，特别是对于基于云的 KMS。为了缓解这种情况，还可以将测试套件配置为使用预定义密钥来测试 KMS 驱动程序 API 的大部分部分（密钥生成除外）：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
class AwsKmsDriverWithPredefinedKeysTest extends KmsDriverTest {

  override val predefinedSigningKeys: Map[SigningKeySpec, String] =
    Map(
      SigningKeySpec.EcP256 -> "alias/canton-kms-test-signing-key",
      SigningKeySpec.EcP384 -> "alias/canton-kms-test-signing-key-P384",
    )

  override val predefinedEncryptionKeys: Map[EncryptionKeySpec, String] =
    Map(EncryptionKeySpec.Rsa2048 -> "alias/canton-kms-test-asymmetric-key")

  override val predefinedSymmetricKey: Option[String] = Some("alias/canton-kms-test-key")

  override protected def newKmsDriver(): KmsDriver = {
    val awsKms = AwsKms
      .create(
        KmsConfig.Aws.defaultTestConfig,
        timeouts,
        loggerFactory,
        NoReportingTracerProvider,
      )
      .valueOrFail("failed to create AWS KMS")

    new AwsKmsDriver(awsKms)
  }

  "AWS KMS Driver" must {
    behave like kmsDriver(allowKeyGeneration = false)
  }

}
```

对于每个受支持的签名/加密密钥规范，可以将现有密钥别名/ID 配置为预定义密钥映射的一部分。运行测试套件时不允许生成新密钥。

#### KmsDriverFactory测试

KMS 驱动程序工厂的测试套件的结构与上述类似：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
class AwsKmsDriverFactoryTest extends KmsDriverFactoryTest {

  override type Factory = AwsKmsDriverFactory

  override protected lazy val factory: AwsKmsDriverFactory =
    new AwsKmsDriverFactory

  override protected lazy val config: AwsKmsDriverFactory#ConfigType = {
    val aws = KmsConfig.Aws.defaultTestConfig
    AwsKmsDriverConfig(region = aws.region, multiRegionKey = aws.multiRegionKey)
  }

  "AWS KMS Driver Factory" must {
    behave like kmsDriverFactory()
  }
}
````KmsDriverFactory` 可以写入特定于驱动程序的配置，并且机密标志为 true，这意味着配置中的任何敏感信息（例如凭据）都应从写入的配置中省略。如果您的驱动程序特定配置包含任何机密信息，则应添加特定的测试用例，并断言敏感信息已被忽略。

## 使用 KMS 驱动程序运行 Canton

配置 Canton 以使用 KMS 驱动程序运行，例如，对于参与者参与者1：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.参与方s.参与方1.crypto.provider = kms
canton.参与方s.参与方1.crypto.kms {
  type = driver
  name = "aws-kms"
    config = {
      region = us-east-1
      multi-region-key = false
      audit-logging = true
    }
}
```

在类路径上使用驱动程序 jar 运行 Canton：

`java -cp driver.jar:canton.jar com.digitalasset.canton.CantonEnterpriseApp -c canton.conf # further canton arguments`

其中canton.jar取决于Canton版本，例如`lib/canton-enterprise-3.3.3.jar`。 `canton.conf` 是一个配置文件，需要配置至少一个节点才能使用如上所述的驱动程序 KMS。例如，使用 `参与方1.health.ping(参与方1)` 运行 ping，以验证参与者是否可以使用配置的 KMS 和驱动程序。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
