---
title: "支持的密码学方案"
slug: "global-synchronizer-reference-crypto-schemes"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/crypto-schemes.md"
source_title: "Supported Cryptographic Schemes"
tags:
  - global-synchronizer
  - reference
  - crypto-schemes
---

# 支持的密码学方案

> Canton 支持的密码学方案与密钥格式参考。

> Canton 支持的加密方案和密钥格式参考

## 支持的加密方案和格式

在 Canton 中，我们使用签名、对称加密和非对称加密的加密原语，以及以下支持的加密方案和格式。对于非对称签名和加密，每个方案都分为密钥和算法规范。

<Note>
  **下表的图例：**

  * **S** = 支持
  * **P1** = 部分支持——仅支持签名验证，不支持私钥签名
  * **P²** = 部分支持 — 仅支持加密，不支持私钥解密
  * 括号中的值 (**\[\<scheme>]**) 表示要在 Canton 中使用的配置字符串
</Note>

**支持的非对称加密和签名密钥规范**

|主要规格| JCE|KMS |目的|
| -------------------------------- | --- | --- | ------------------- |
| EC 曲线25519 `[ec-curve-25519]` | S | P1|签约|
| EC-P256 `[ec-p-256]` | S | S |签名、加密 |
| EC-P384 `[ec-p-384]` | S | S |签约|
| EC-Secp256k1 `[ec-secp-256k-1]` | S | S |签约|
| RSA-2048 `[rsa-2048]` | S | S |加密 |

**支持的签名算法规范**

|算法| JCE|KMS |支持的关键规格 |
| -------------------------------- | ---| --- | -------------------- |
| Ed25519 `[ed-25519]` | S | P1| EC 曲线25519 |
| EC-DSA-SHA256 `[ec-dsa-sha-256]` | S | S | EC-P256、EC-Secp256k1 |
| EC-DSA-SHA384 `[ec-dsa-sha-384]` | S | S | EC-P384 |

**支持的非对称加密算法规格**

|算法| JCE|KMS |支持的关键规格 |
| -------------------------------------------------------------------------------- | --- | --- | ------------------- |
| ECIES-HMAC-SHA256-AES128-CBC `[ecies-hkdf-hmac-sha-256-aes-128-cbc]` | S | P²| EC-P256 |
| RSA-OAEP-SHA256 `[rsa-oaep-sha-256]` | S | S | RSA-2048 |

| **加密货币提供商** | JCE默认方案| KMS默认方案|
| --------------------------------------- | -------------------------------------------------- | ---------------------------------- |
|签名密钥规范| EC 曲线25519 | EC-P256 |
|签名算法规范 |Ed25519 | EC-DSA-SHA256 |
|非对称加密密钥规范| EC-P256 | RSA-2048 |
|非对称加密算法 |具有 HMAC-SHA256 和 AES128-CBC 的 ECIES |具有 OAEP 和 SHA-256 的 RSA |
|对称加密方案[^1] | AES128-GCM |与 JCE 相同 |
|哈希算法[^2] | SHA-256 |与 JCE 相同 |
| PBKDF[^3] |Argon2id |与 JCE 相同 |

默认加密方案

**使用密钥管理服务 (KMS) 进行外部密钥的密钥配置**

|供应商|签约 |加密|
| -------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
|亚马逊AWS | **主要目的：** `SIGN_VERIFY`<br />**关键算法：** `ECC_NIST_P256` 或 `ECC_NIST_P384` | **主要目的：** `ENCRYPT_DECRYPT`<br />**关键算法：** `RSA_2048` |
| GCP | **主要目的：** `ASYMMETRIC_SIGN`<br />**关键算法：** `EC_SIGN_P256_SHA256` 或 `EC_SIGN_P384_SHA384` | **主要目的：** `ASYMMETRIC_DECRYPT`<br />**关键算法：** `RSA_DECRYPT_OAEP_2048_SHA256` |
|司机 |必须兼容`EC_P256_SHA256`或`EC_P384_SHA384`|必须兼容`RSA_OAEP_2048_SHA256` || **密钥类型** |格式（配置）|格式（gRPC / Protobuf）|
| ----------------- | ---------------- | ---------------------------------------------------------------- |
|公钥| `der-x-509-spki` | `CRYPTO_KEY_FORMAT_DER_X509_SUBJECT_PUBLIC_KEY_INFO` |
|私钥| `der-pkcs-8-pki` | `CRYPTO_KEY_FORMAT_DER_PKCS8_PRIVATE_KEY_INFO` |
|对称密钥[^4] | `raw` | `CRYPTO_KEY_FORMAT_RAW` |

按密钥类型支持的加密密钥格式

**以支持的格式导出密钥的命令和标志**

|钥匙类型|支持的格式 | OpenSSL | GCP KMS | AWS KMS | AWS KMS Java 安全 | Python（密码学）|
| ------------- | -------------------------------------------------- | -------------- | ------------------------ | ------------------------ | -------------------------- | --------------------------------------------------------------------------- |
|公钥| DER SPKI (X.509SubjectPublicKeyInfo) | `-outform DER` |密钥默认为 DER SPKI |密钥默认为 DER SPKI |密钥默认为 DER SPKI | `public_bytes(Encoding.DER, PublicFormat.SubjectPublicKeyInfo)` |
|私钥| DER PKCS#8 私钥信息 | `-outform DER` |不适用 |不适用 |密钥默认为 DER PKCS#8 | `private_bytes(Encoding.DER, PrivateFormat.PKCS8)` |
|对称密钥|原始字节 |不适用 |不适用 |不适用 |键默认为原始字节 |键默认为原始字节 |

| **签名算法规范** |签名格式（配置）|签名格式（gRPC / Protobuf）|
| ------------------------------------------------ | ---------------------------------- | ---------------------------------- |
|Ed25519 | `concat` | `SIGNATURE_FORMAT_CONCAT` |
| EC-DSA-SHA256 | `der` | `SIGNATURE_FORMAT_DER` |
| EC-DSA-SHA384 | `der`| `SIGNATURE_FORMAT_DER` |

签名算法规范支持的加密签名格式

<Note>
  Canton 当前支持的签名格式与使用 OpenSSL、Java 或 Python（`cryptography` 包）生成签名时使用的默认签名格式一致。
</Note>

[^1]：默认且唯一支持的方案；不可配置。

[^2]：默认且仅支持的哈希算法；不可配置。

[^3]：默认且仅支持PBKDF；不可配置。

[^4]：对称密钥仅在内部使用。节点运营商不会对对称密钥进行操作；此条目仅供参考。节点操作员期望与之交互的唯一密钥格式是`X.509`公钥。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
