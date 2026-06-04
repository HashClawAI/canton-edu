---
title: "超级验证者安全"
slug: "global-synchronizer-production-operations-sv-security"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/sv-security.md"
source_title: "SV Security"
tags:
  - global-synchronizer
  - production-operations
  - sv-security
---

# 超级验证者安全

> 超级验证者节点安全加固与 KMS 配置。

> 超级验证者节点的安全加固、KMS配置、额外DAR通知

{/* TODO：上游 splice:docs/src/sv_operator/sv_security.rst 源中的“第三方 Daml 应用程序”部分为空。内容空白 - 当上游提供时填写或删除。 */}

<Warning>
  作为 SV 运营商，我们非常欢迎您查看、安装和使用第三方 Daml 应用程序，前提是您**在与 SV 节点分开的验证器节点上安装第三方 Daml 应用程序**。

  不支持在 SV 节点上安装额外的 Daml 应用程序，这可能会损害其安全操作。特别是，请避免手动上传额外的`.dar`文件到您的SV节点或手动将其连接到第三方同步器。
</Warning>

## 使用外部 KMS 管理参与者密钥

<KmsParticipantsContext />

下面，我们将介绍如何配置 SV，使其参与者密钥由外部 KMS 管理。本指南假设您按照 `sv-helm` 来部署 SV。

计划在未来版本中正式支持作为 SV 部署一部分的排序器和中介器的基于 KMS 的操作。

### 迁移现有 SV 以使用外部 KMS 作为参与者密钥

不支持将现有参与者从“非基于 KMS”操作迁移到“基于 KMS”操作，或从一个 KMS 提供商迁移到另一个 KMS 提供商。其主要原因是参与者的根命名空间密钥无法轮换，并且将其从潜在不安全的位置导入 KMS 会降低使用 KMS 的安全增益。此外，一些KMS提供商根本不支持导入现有密钥，只能用于管理KMS本身生成的密钥。

切换到使用 KMS 获取 SV 参与者密钥同时最大限度地降低失去奖励的风险的一种方法是：

1. 使用所需的 KMS 配置从头开始设置新的 SV。 （本指南的其余部分。）与其他 SV 操作员协调，以重量 0 装载它。
2. 与其他 SV 操作员协调，将您的 SV 权重移至新 SV，将旧 SV 的权重设置为 0。
3. 将所有相关资产从旧的 SV 转移到验证器或新的启用 KMS 的 SV。
4. 与其他 SV 操作员协调以下架旧的 SV。
5. 淘汰旧的 SV。

### 配置新的 SV 以使用外部 KMS

除了对参与者 Helm 图表本身进行配置更改之外，与默认设置相比，您还需要更改 CometBFT 治理密钥的管理方式。

#### CometBFT治理密钥的外部管理

默认情况下，CometBFT 治理密钥由 SV 应用程序透明管理，使用参与者进行密钥生成和存储。支持 KMS 的参与者不支持实现这一点的具体方式。因此，希望使用外部 KMS 来管理其参与者密钥的 SV 运营商必须在外部管理其 SV 的 CometBFT 治理密钥。

这涉及以下步骤：

1. 生成新的 CometBFT 治理密钥。
2. 配置您的 SV 应用程序以使用此外部生成的密钥。

##### 生成 CometBFT 治理密钥

使用以下 shell 命令生成预期格式的密钥对：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
# Generate the private key
openssl genpkey -algorithm ed25519 -out cometbft-governance-keys.pem

# Extract and encode the keys
public_key_base64=$(openssl pkey -in cometbft-governance-keys.pem -pubout -outform DER | tail -c 32 | base64 | tr -d "\n")
private_key_base64=$(openssl pkey -in cometbft-governance-keys.pem -outform DER | tail -c 32 | base64 | tr -d "\n")

echo "{"
# Output the keys
echo "  \"publicKey\": \"$public_key_base64\","
echo "  \"privateKey\": \"$private_key_base64\""
echo "}"

# Clean up
rm cometbft-governance-keys.pem
```

这些命令应该产生类似于以下内容的输出：

```json theme={"theme":{"light":"github-light","dark":"github-dark"}}
{
  "publicKey": "A9tWyYq/HIJ3B73ym1eIUV8yqnDBligGJUE8463CBUM=",
  "private": "FDG16PaSh9hGLu2fXzEHmTECMjSyQuZnEg+w5HKCEtg="
}
```

将此输出保存到文件中，例如`cometbft-governance-keys.json`。

##### 配置 SV 应用程序以使用外部生成的 CometBFT 治理密钥

您可以通过将外部生成的 CometBFT 治理密钥存储在名为 `splice-app-sv-cometbft-governance-key` 的 k8s 密钥中，将其注入到 SV 应用程序中。假设您的 SV 部署驻留在 `sv` 命名空间中，请使用以下命令从上面生成的 JSON 文件创建密钥：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl create secret --namespace sv generic splice-app-sv-cometbft-governance-key \
  --from-literal=publicKey="$(jq -r .public cometbft-governance-keys.json)" \
  --from-literal=privateKey="$(jq -r .private cometbft-governance-keys.json)"
```

要指示 SV 应用程序使用外部管理的 CometBFT 治理密钥而不是自行生成新的治理密钥，请将 `splice-sv-node` Helm 图表中的 `cometBFT.externalGovernanceKey` 值设置为 `true`。 （您可以注释掉`splice-node/examples/sv-helm/sv-values.yaml`中的相应行。）

#### 配置参与者使用外部 KMS

除了上述 SV 应用程序部署的更改之外，使用外部 KMS 的 SV 参与者的设置与使用 KMS 的验证者参与者的设置相同。它涉及对 `splice-participant` Helm 图表的配置更改，具体取决于您选择的 KMS 提供商。

请参阅 [有关配置 KMS 支持的 Canton 文档](/zh/docs/canton/global-synchronizer-reference-kms-driver-guide)，以确定与您所需的 KMS 提供商和设置相匹配的正确配置选项。我们在下面提供了 Google Cloud (GCP) KMS 和 Amazon Web Services (AWS) KMS 的最小 Helm 配置示例。

<Warning>
  GCP 和 AWS KMS 驱动程序仅适用于 Canton Enterprise 的许可用户。
</Warning>

无论您选择什么 KMS 提供商，请注意：

* 参与者 Helm 图表的 `kms` 部分中的值隐式映射到 Canton 参与者 `crypto.kms` 配置。这意味着 Canton 支持的所有配置键都受支持，而不仅仅是上面示例中显示的配置键。驼峰命名法中的键名称会自动转换为短横线命名法。
* 要设置额外的环境变量和安装文件以配置 KMS 身份验证，您可以使用 Splice 参与者 Helm 图表的 `.additionalEnvVars`、`.extraVolumeMounts` 和 `.extraVolumes` 字段（请参阅示例）。
* 确保您的 KMS 配置始终包含在您传递给 `helm install participant ...` 或 `helm upgrade participant ...` 的值文件中。
* Canton 参与者使用[会话密钥](/zh/docs/canton/global-synchronizer-production-operations-key-management#configure-session-keys) 来减少协议执行过程中非对称加密操作的数量，从而提高性能并降低 (KMS) 成本。默认情况下，Splice 参与者使用生命周期为一小时的会话**加密**密钥。对于启用 KMS 的参与者的安全影响是，有权访问内存快照的对手可能能够获取对称密钥，从而允许解密最多一小时的加密消息。可以通过配置覆盖来覆盖默认会话密钥参数。请参阅 [Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-key-management#configure-session-keys) 以获取相关参数的概述。 Splice 参与者尚不支持使用会话**签名**密钥。

另请记住，您需要部署**新**参与者才能正确使用 KMS，这意味着您还需要重新设置其余的 SV 组件（见上文）。

##### 谷歌云 KMS

以下 GCP KMS 的模拟配置包含在 `splice-node/examples/sv-helm/kms-participant-gcp-values.yaml` 中：

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 使用 GCP KMS 的参与者（模拟值；请修改以匹配您的设置）
# 请参阅[广州 KMS 操作](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-google-cloud-provider-gcp-kms)

公里数：
  类型：gcp
  # 根据您的 GCP KMS 设置替换 LOCATION_ID、PROJECT_ID 和 KEY_RING_ID
  位置 ID：LOCATION_ID
  项目 ID：PROJECT_ID
  密钥环 ID：KEY_RING_ID
  # 也支持所有其他 Canton 选项；
  # 这里的camelCase键会自动转换为kebab-case# 配置GCP KMS认证示例。
# 在参与者 Pod 上添加一个指向 Google 位置的环境变量
# 凭证文件并将该文件安装为卷，从秘密中读取其内容。
# 为了使其按原样工作，您需要创建适当的 k8s 密钥
# 并确保它包含有效的 Google 凭据文件的内容
#（在`googleCredentials`键下）。
附加环境变量：
  - 名称：GOOGLE_APPLICATION_CREDENTIALS
    值：“/app/gcp-credentials.json”
额外卷安装：
  - 名称：gcp-credentials
    挂载路径：“/app/gcp-credentials.json”
    子路径：googleCredentials
额外卷：
  - 名称：gcp-credentials
    秘密：
      秘密名称：gke-credentials
```

Please refer to the [Canton documentation](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-google-cloud-provider-gcp-kms) for a list of supported configuration options and their meaning, as well as for instructions on configuring authentication to the KMS. Note again that Splice participants support the External Key Storage mode of KMS usage, so that (per the [relevant Canton docs](/zh/docs/canton/global-synchronizer-production-operations-key-management)) the authentication credentials you supply must correspond to a GCP service account with the following IAM permissions:

* `cloudkms.cryptoKeyVersions.create`
* `cloudkms.cryptoKeyVersions.useToDecrypt`
* `cloudkms.cryptoKeyVersions.useToSign`
* `cloudkms.cryptoKeyVersions.get`
* `cloudkms.cryptoKeyVersions.viewPublicKey`

For example, you can grant the `Cloud KMS Admin` and `Cloud KMS Crypto Operator` roles to the 验证者 KMS service account.

##### Amazon Web Services KMS

The mock configuration below for AWS KMS is included in `splice-node/examples/sv-helm/kms-participant-aws-values.yaml`:

```yaml theme={"theme":{"light":"github-light","dark":"github-dark"}}
# 使用 AWS KMS 的参与者（模拟值；请修改以匹配您的设置）
# 请参阅[广州 KMS 操作](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-amazon-web-services-aws-kms)
公里数：
  类型：AWS
  # 根据您的 AWS KMS 设置替换 REGION
  地区： 地区
  # 也支持所有其他 Canton 选项；
  # 这里的camelCase键会自动转换为kebab-case

# 配置 AWS KMS 身份验证的示例。
# 使用从 k8s 密钥读取的凭据在参与者 Pod 上添加环境变量。
# 为了使其按原样工作，您需要创建适当的 k8s 密钥
# 并确保它拥有有效的凭据
#（在`accessKeyId`和`secretAccessKey`键下）。
附加环境变量：
  - 名称：AWS_ACCESS_KEY_ID
    值来自：
      秘密密钥参考：
        名称：aws-凭证
        密钥：accessKeyId
  - 名称：AWS_SECRET_ACCESS_KEY
    值来自：
      秘密密钥参考：
        名称：aws-凭证
        密钥：秘密访问密钥
````

请参阅 [Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-kms-operations#configure-a-amazon-web-services-aws-kms)，了解受支持的配置选项及其含义的列表，以及有关配置 KMS 身份验证的说明。再次注意，拼接参与者支持 KMS 使用的外部密钥存储模式，因此（根据[相关 Canton 文档](/zh/docs/canton/global-synchronizer-production-operations-key-management)）您提供的身份验证凭证必须对应于具有以下 IAM 权限的实体：

* `kms:CreateKey`
* `kms:TagResource`
* `kms:Decrypt`
* `kms:Sign`
* `kms:DescribeKey`
* `kms:GetPublicKey`

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
