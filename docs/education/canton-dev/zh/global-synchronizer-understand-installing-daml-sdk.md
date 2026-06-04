---
title: "安装兼容的 Daml SDK"
slug: "global-synchronizer-understand-installing-daml-sdk"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/understand/installing-daml-sdk.md"
source_title: "Installing a Compatible Daml SDK"
tags:
  - global-synchronizer
  - understand
  - installing-daml-sdk
---

# 安装兼容的 Daml SDK

> 安装与当前 Splice 版本兼容的 Daml SDK 的方法。

您无需安装用于构建此 Splice 版本的完全相同的 Daml SDK 版本。这些版本仅供参考。由旧版 3.x Daml SDK 构建的`.dar` 文件通常与此 Splice 版本中使用的 Canton 版本兼容。

为了测试您的应用程序与验证者节点的交互，我们建议使用此 Splice 版本中使用的 Canton 版本，如果您使用验证者部署说明来部署验证者节点，就是这种情况。

为了从 Daml SDK 的最新功能和错误修复中获益，我们建议使用最新的 Daml SDK 版本，该版本与此 Splice 版本中使用的 Canton 版本具有“相同的主要版本和次要版本”。

请按照以下步骤安装最新的兼容 OSS Daml SDK 版本：

1. 选择与上述相同主要版本和次要版本的最新稳定版本。

2. 使用以下命令安装该版本

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -sSL https://get.digitalasset.com/ | sh
   ```

有关安装 Daml SDK 的更多信息，请参阅[DPM 安装指南](/sdks-tools/cli-tools/dpm)。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
