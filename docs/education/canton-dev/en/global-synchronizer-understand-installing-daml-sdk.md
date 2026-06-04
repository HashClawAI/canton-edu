---
title: "Installing a Compatible Daml SDK"
slug: "global-synchronizer-understand-installing-daml-sdk"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/understand/installing-daml-sdk.md"
source_title: "Installing a Compatible Daml SDK"
tags:
  - global-synchronizer
  - understand
  - installing-daml-sdk
---

# Installing a Compatible Daml SDK

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Installing a Compatible Daml SDK

> How to install a Daml SDK version compatible with the current Splice release

You are not required to install the exact same Daml SDK versions used to build this Splice release. These versions are provided for reference only. `.dar` files built by older 3.x Daml SDKs are generally compatible with the Canton version used in this Splice release.

For testing the interaction of your app with a Validator Node, we do recommend to use the Canton version used in this Splice release, which is the case if you deploy your Validator Node using the validator deployment instructions.

To profit from the most recent features and bug fixes of the Daml SDK, we recommend to use a recent Daml SDK release that has the *same major and minor version* as the Canton version used in this Splice release.

Follow these steps to install a recent, compatible OSS Daml SDK version:

1. Select the most recent stable release with the same major and minor version as above.

2. Install that release using

   ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
   curl -sSL https://get.digitalasset.com/ | sh
   ```

For more information about installing the Daml SDK, see the [DPM installation guide](https://docs.canton.network/sdks-tools/cli-tools/dpm).

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
