---
title: "com.digitalasset.canton.crypto.admin.v30"
slug: "reference-admin-api-protobuf-packages-com-digitalasset-canton-crypto-admin-v30"
locale: "zh"
category: "reference"
source_url: "https://docs.canton.network/reference/admin-api/protobuf/packages/com-digitalasset-canton-crypto-admin-v30.md"
source_title: "com.digitalasset.canton.crypto.admin.v30"
tags:
  - reference
  - admin-api
  - protobuf
  - packages
---

# com.digitalasset.canton.crypto.admin.v30

> com.digitalasset.canton.crypto.admin.v30 的包级别概述。

<p class="x2mdx-ref-back"><a href="/zh/docs/canton/reference-admin-api-protobuf-index">返回概览</a></p>

<div class="x2mdx-ref-hero">
  <p class="x2mdx-ref-eyebrow">Protobuf 包</p>

  <h1 class="x2mdx-ref-title">com.digitalasset.canton.crypto.admin.v30</h1>

  <p class="x2mdx-ref-summary">1 个服务、12 个端点、33 条消息</p>

  <div class="x2mdx-ref-badges">
    <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>
  </div>

  <dl class="x2mdx-ref-meta-grid">
    <div class="x2mdx-ref-meta-item">
      <dt>文件</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>服务</dt>
      <dd>1</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>端点</dt>
      <dd>12</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>消息</dt>
      <dd>33</dd>
    </div>

    <div class="x2mdx-ref-meta-item">
      <dt>枚举</dt>
      <dd>0</dd>
    </div>
  </dl>
</div>

## 源文件

<div class="x2mdx-ref-card-grid">
  <div class="x2mdx-ref-card x2mdx-ref-card--static">
    <div class="x2mdx-ref-card-head">
      <h3>community/base/src/main/protobuf/com/digitalasset/canton/crypto/admin/v30/vault\_service.proto</h3>
    </div>

    <p class="x2mdx-ref-card-summary">最新发布的描述符快照中的当前源文件。</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>服务</dt>
        <dd>1</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>消息</dt>
        <dd>32</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>枚举</dt>
        <dd>0</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>来源</dt>
        <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/crypto/admin/v30/vault_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/crypto/admin/v30/vault\_service.proto</a></dd>
      </div>
    </dl>
  </div>
</div>

## VaultService

<dl class="x2mdx-ref-meta-grid">
  <div class="x2mdx-ref-meta-item">
    <dt>源文件</dt>
    <dd><a href="https://github.com/DACH-NY/canton/blob/v3.5.1/community/base/src/main/protobuf/com/digitalasset/canton/crypto/admin/v30/vault_service.proto">community/base/src/main/protobuf/com/digitalasset/canton/crypto/admin/v30/vault\_service.proto</a></dd>
  </div>

  <div class="x2mdx-ref-meta-item">
    <dt>操作</dt>
    <dd>12</dd>
  </div>
</dl>

<div class="x2mdx-ref-card-grid">
  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-deletekeypair">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.DeleteKeyPair</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.DeleteKeyPair(com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-exportkeypair">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.ExportKeyPair</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.ExportKeyPair(com.digitalasset.canton.crypto.admin.v30.ExportKeyPairRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.ExportKeyPairResponse);</p><dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ExportKeyPairRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ExportKeyPairResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-generateencryptionkey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.GenerateEncryptionKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.GenerateEncryptionKey(com.digitalasset.canton.crypto.admin.v30.GenerateEncryptionKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.GenerateEncryptio...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GenerateEncryptionKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GenerateEncryptionKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-generatesigningkey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.GenerateSigningKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.GenerateSigningKey(com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyRespo...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-getwrapperkeyid">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.GetWrapperKeyId</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.GetWrapperKeyId(com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a><a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-importkeypair">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.ImportKeyPair</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.ImportKeyPair(com.digitalasset.canton.crypto.admin.v30.ImportKeyPairRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.ImportKeyPairResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ImportKeyPairRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ImportKeyPairResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-importpublickey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.ImportPublicKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.ImportPublicKey(com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-listmykeys">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.ListMyKeys</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.ListMyKeys(com.digitalasset.canton.crypto.admin.v30.ListMyKeysRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.ListMyKeysResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ListMyKeysRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ListMyKeysResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-listpublickeys">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.ListPublicKeys</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.ListPublicKeys(com.digitalasset.canton.crypto.admin.v30.ListPublicKeysRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.ListPublicKeysResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ListPublicKeysRequest</dd>
      </div><div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.ListPublicKeysResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-registerkmsencryptionkey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.RegisterKmsEncryptionKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.RegisterKmsEncryptionKey(com.digitalasset.canton.crypto.admin.v30.RegisterKmsEncryptionKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.RegisterKms...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RegisterKmsEncryptionKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RegisterKmsEncryptionKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-registerkmssigningkey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.RegisterKmsSigningKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.RegisterKmsSigningKey(com.digitalasset.canton.crypto.admin.v30.RegisterKmsSigningKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.RegisterKmsSignin...</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RegisterKmsSigningKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RegisterKmsSigningKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>

  <a class="x2mdx-ref-card" href="/zh/docs/canton/reference-admin-api-protobuf-operations-com-digitalasset-canton-crypto-admin-v30-vaultservice-rotatewrapperkey">
    <div class="x2mdx-ref-card-head">
      <h3>VaultService.RotateWrapperKey</h3>

      <div class="x2mdx-ref-badges">
        <span class="x2mdx-ref-badge x2mdx-ref-badge--protocol">gRPC</span>

        <span class="x2mdx-ref-badge x2mdx-ref-badge--linked">自 3.4.0 起</span>
      </div>
    </div>

    <p class="x2mdx-ref-card-summary">rpc VaultService.RotateWrapperKey(com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyRequest) 返回 (com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyResponse);</p>

    <dl class="x2mdx-ref-meta-grid">
      <div class="x2mdx-ref-meta-item">
        <dt>请求</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyRequest</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>回应</dt>
        <dd>com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyResponse</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>客户端流</dt>
        <dd>否</dd>
      </div>

      <div class="x2mdx-ref-meta-item">
        <dt>服务器流</dt>
        <dd>否</dd>
      </div>
    </dl>
  </a>
</div>

## 类型库存

这些是发布版本快照中的包级消息和枚举形状。

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-deletekeypairrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairRequest</h3><p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">指纹</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-deletekeypairresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.DeleteKeyPairResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-exportkeypairrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ExportKeyPairRequest</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">指纹</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">协议\_版本</code>
        <span class="x2mdx-ref-type-badge">int32</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密码</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-exportkeypairresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ExportKeyPairResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key\_pair</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generatecertificaterequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateCertificateRequest</h3>

    <p class="x2mdx-ref-schema-summary">4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">唯一\_identifier</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">证书\_key</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">附加\_主题</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">主题\_alternative\_names</code>
        <span class="x2mdx-ref-type-badge">重复字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generatecertificateresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateCertificateResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">x509\_cert</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generateencryptionkeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateEncryptionKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key\_spec</code>
        <span class="x2mdx-ref-type-badge">加密密钥规范</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generateencryptionkeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateEncryptionKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_key</code>
        <span class="x2mdx-ref-type-badge">加密公钥</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generatesigningkeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key\_spec</code>
        <span class="x2mdx-ref-type-badge">签名密钥规范</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">用法</code>
        <span class="x2mdx-ref-type-badge">重复SigningKeyUsage</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-generatesigningkeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GenerateSigningKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_key</code>
        <span class="x2mdx-ref-type-badge">签名公钥</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-getwrapperkeyidrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdRequest</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-getwrapperkeyidresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.GetWrapperKeyIdResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包装\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importcertificaterequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportCertificateRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">x509\_cert</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importcertificateresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportCertificateResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">证书\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importkeypairrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportKeyPairRequest</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">key\_pair</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">密码</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importkeypairresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportKeyPairResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importpublickeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_key</code>
        <span class="x2mdx-ref-type-badge">字节</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-importpublickeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ImportPublicKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">指纹</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listcertificaterequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListCertificateRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">过滤器\_uid</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listcertificateresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListCertificateResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">结果</code>
        <span class="x2mdx-ref-type-badge">重复结果</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listcertificateresponse-result">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListCertificateResponse.Result</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div><div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">x509\_cert</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listkeysfilters">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListKeysFilters</h3>

    <p class="x2mdx-ref-schema-summary">4 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">指纹</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">目的</code>
        <span class="x2mdx-ref-type-badge">重复KeyPurpose</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">用法</code>
        <span class="x2mdx-ref-type-badge">重复SigningKeyUsage</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listmykeysrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListMyKeysRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">过滤器</code>
        <span class="x2mdx-ref-type-badge">ListKeysFilters</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listmykeysresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListMyKeysResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">私有\_keys\_metadata</code>
        <span class="x2mdx-ref-type-badge">重复的 PrivateKeyMetadata</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-privatekeymetadata">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.PrivateKeyMetadata</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">public\_key\_with\_name</code>
        <span class="x2mdx-ref-type-badge">PublicKeyWithName</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">包装\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">kms\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listpublickeysrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListPublicKeysRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">过滤器</code>
        <span class="x2mdx-ref-type-badge">ListKeysFilters</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-listpublickeysresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.ListPublicKeysResponse</h3><p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_keys</code>
        <span class="x2mdx-ref-type-badge">重复的 PublicKeyWithName</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-registerkmsencryptionkeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RegisterKmsEncryptionKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">2 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">kms\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-registerkmsencryptionkeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RegisterKmsEncryptionKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_key</code>
        <span class="x2mdx-ref-type-badge">加密公钥</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-registerkmssigningkeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RegisterKmsSigningKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">3 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">kms\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">名称</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>

    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">用法</code>
        <span class="x2mdx-ref-type-badge">重复SigningKeyUsage</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-registerkmssigningkeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RegisterKmsSigningKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">公共\_key</code>
        <span class="x2mdx-ref-type-badge">签名公钥</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-rotatewrapperkeyrequest">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyRequest</h3>

    <p class="x2mdx-ref-schema-summary">1 个字段</p>
  </div>

  <div class="x2mdx-ref-fields">
    <div class="x2mdx-ref-field-row">
      <div class="x2mdx-ref-field-main">
        <code class="x2mdx-ref-field-name">新\_wrapper\_key\_id</code>
        <span class="x2mdx-ref-type-badge">字符串</span>
      </div>
    </div>
  </div>
</div>

<div class="x2mdx-ref-schema" id="schema-com-digitalasset-canton-crypto-admin-v30-rotatewrapperkeyresponse">
  <div class="x2mdx-ref-schema-head">
    <h3>com.digitalasset.canton.crypto.admin.v30.RotateWrapperKeyResponse</h3>

    <p class="x2mdx-ref-schema-summary">0 个字段</p>
  </div>
</div>

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
