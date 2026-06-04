---
title: "验证者安全"
slug: "global-synchronizer-production-operations-validator-security"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/validator-security.md"
source_title: "Validator Security"
tags:
  - global-synchronizer
  - production-operations
  - validator-security
---

# 验证者安全

> 验证者节点安全加固与 KMS 配置。

> 验证者节点的安全加固和KMS配置

## 使用外部 KMS 管理参与者密钥

默认情况下，Canton 参与者使用由参与者自己生成并存储在参与者使用的常规数据库中的加密[密钥](/zh/docs/canton/appdev-modules-m7-security)。为了提高密钥安全性，参与者可以配置为使用外部密钥管理系统（KMS）来生成和存储密钥。请参阅官方 [Canton 有关 KMS 支持的文档](/zh/docs/canton/global-synchronizer-production-operations-kms-operations)，了解更多详细信息以及受支持的 KMS 提供商列表。作为 Splice 部署的一部分部署的参与者支持 KMS 使用的[外部密钥存储](/zh/docs/canton/global-synchronizer-production-operations-key-management)模式。

下面，我们将描述如何配置验证者，使其参与者密钥由外部 KMS 管理。本指南假设您使用基于 Helm 的验证者部署。基于 Docker Compose 的部署目前不支持使用 KMS。

### 迁移现有验证器以使用外部 KMS

不支持将现有参与者从“非基于 KMS”操作迁移到“基于 KMS”操作，或从一个 KMS 提供商迁移到另一个 KMS 提供商。其主要原因是参与者的根命名空间密钥无法轮换，并且将其从潜在不安全的位置导入 KMS 会降低使用 KMS 的安全增益。此外，一些KMS提供商根本不支持导入现有密钥，只能用于管理KMS本身生成的密钥。

我们推荐的切换到使用 KMS 的方法是：

1. 使用所需的 KMS 配置从头开始设置一个新的验证者。 （本指南的其余部分。）
2. 将所有相关资产从现有的非 KMS 验证者转移到新的启用 KMS 的验证者。
3. 停用非 KMS 验证者。

### 配置新的验证者以使用外部 KMS

只需对 `splice-participant` Helm 图表进行配置更改即可部署支持 KMS 的验证者。

请参阅 [有关配置 KMS 支持的 Canton 文档](/zh/docs/canton/global-synchronizer-reference-kms-driver-guide)，以确定与您所需的 KMS 提供商和设置相匹配的正确配置选项。我们在下面提供了 Google Cloud (GCP) KMS 和 Amazon Web Services (AWS) KMS 的最小 Helm 配置示例。

<Warning>
  GCP 和 AWS KMS 驱动程序仅适用于 Canton Enterprise 的许可用户。
</Warning>

无论您选择什么 KMS 提供商，请注意：

* 参与者 Helm 图表的 `kms` 部分中的值隐式映射到 Canton 参与者 `crypto.kms` 配置。这意味着 Canton 支持的所有配置键都受支持，而不仅仅是上面示例中显示的配置键。驼峰命名法中的键名称会自动转换为短横线命名法。
* 要设置额外的环境变量和安装文件以配置 KMS 身份验证，您可以使用 Splice 参与者 Helm 图表的 `.additionalEnvVars`、`.extraVolumeMounts` 和 `.extraVolumes` 字段（请参阅示例）。
* 确保您的 KMS 配置始终包含在您传递给 `helm install participant ...` 或 `helm upgrade participant ...` 的值文件中。
* Canton 参与者使用[会话密钥](/zh/docs/canton/global-synchronizer-production-operations-key-management#configure-session-keys) 来减少协议执行过程中非对称加密操作的数量，从而提高性能并降低 (KMS) 成本。默认情况下，Splice 参与者使用生命周期为一小时的会话**加密**密钥。对于启用 KMS 的参与者的安全影响是，有权访问内存快照的对手可能能够获取对称密钥，从而允许解密最多一小时的加密消息。可以通过配置覆盖来覆盖默认会话密钥参数。请参阅 [Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-key-management#configure-session-keys) 以获取相关参数的概述。 Splice 参与者尚不支持使用会话**签名**密钥。

另请记住，您需要部署一个**新**参与者才能正确使用 KMS，这意味着您还需要重新设置其余的验证器组件（见上文）。

#### 谷歌云 KMS以下 GCP KMS 的模拟配置包含在 `splice-node/examples/sv-helm/kms-participant-gcp-values.yaml` 中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Participant using GCP KMS (mock values; please modify to match your setup)
# See [Canton KMS operations](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-google-cloud-provider-gcp-kms)

kms:
  type: gcp
  # Replace LOCATION_ID, PROJECT_ID, and KEY_RING_ID based on your GCP KMS setup
  locationId: LOCATION_ID
  projectId: PROJECT_ID
  keyRingId: KEY_RING_ID
  # All other Canton options are supported as well;
  # camelCase keys here are automatically converted to kebab-case

# Example for configuring authentication to the GCP KMS.
# Adds an env var on the participant pod that points to the location of the Google
# credentials file and mounts that file as a volume, reading its contents from a secret.
# In order for this to work as-is, you need to create the appropriate k8s secret
# and ensure that it holds the contents of a valid Google credentials file
# (under the `googleCredentials` key).
additionalEnvVars:
  - name: GOOGLE_APPLICATION_CREDENTIALS
    value: "/app/gcp-credentials.json"
extraVolumeMounts:
  - name: gcp-credentials
    mountPath: "/app/gcp-credentials.json"
    subPath: googleCredentials
extraVolumes:
  - name: gcp-credentials
    secret:
      secretName: gke-credentials
```

请参阅 [Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-google-cloud-provider-gcp-kms)，了解受支持的配置选项及其含义的列表，以及有关配置 KMS 身份验证的说明。再次注意，Splice 参与者支持 KMS 使用的外部密钥存储模式，因此（根据 [相关 Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-key-management)）您提供的身份验证凭据必须对应于具有以下 IAM 权限的 GCP 服务帐户：

* `cloudkms.cryptoKeyVersions.create`
* `cloudkms.cryptoKeyVersions.useToDecrypt`
* `cloudkms.cryptoKeyVersions.useToSign`
* `cloudkms.cryptoKeyVersions.get`
* `cloudkms.cryptoKeyVersions.viewPublicKey`

例如，您可以将 `Cloud KMS Admin` 和 `Cloud KMS Crypto Operator` 角色授予验证者 KMS 服务帐户。

#### 亚马逊网络服务 KMS

以下 AWS KMS 的模拟配置包含在 `splice-node/examples/sv-helm/kms-participant-aws-values.yaml` 中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Participant using AWS KMS (mock values; please modify to match your setup)
# See [Canton KMS operations](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-amazon-web-services-aws-kms)
kms:
  type: aws
  # Replace REGION based on your AWS KMS setup
  region: REGION
  # All other Canton options are supported as well;
  # camelCase keys here are automatically converted to kebab-case

# Example for configuring authentication to the AWS KMS.
# Adds env vars on the participant pod with credentials read from a k8s secret.
# In order for this to work as-is, you need to create the appropriate k8s secret
# and ensure that it holds valid credentials
# (under the `accessKeyId` and `secretAccessKey` keys).
additionalEnvVars:
  - name: AWS_ACCESS_KEY_ID
    valueFrom:
      secretKeyRef:
        name: aws-credentials
        key: accessKeyId
  - name: AWS_SECRET_ACCESS_KEY
    valueFrom:
      secretKeyRef:
        name: aws-credentials
        key: secretAccessKey
```

请参阅 [Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-amazon-web-services-aws-kms)，了解受支持的配置选项及其含义的列表，以及有关配置 KMS 身份验证的说明。再次注意，拼接参与者支持 KMS 使用的外部密钥存储模式，因此（根据[相关 Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-key-management)）您提供的身份验证凭证必须对应于具有以下 IAM 权限的实体：

* `kms:CreateKey`
* `kms:TagResource`
* `kms:Decrypt`
* `kms:Sign`
* `kms:DescribeKey`
* `kms:GetPublicKey`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
