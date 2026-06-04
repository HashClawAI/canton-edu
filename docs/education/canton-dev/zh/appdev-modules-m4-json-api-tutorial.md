---
title: "Canton 与 JSON Ledger API"
slug: "appdev-modules-m4-json-api-tutorial"
locale: "zh"
category: "appdev"
source_url: "https://docs.canton.network/appdev/modules/m4-json-api-tutorial.md"
source_title: "Canton and the JSON Ledger API"
tags:
  - appdev
  - modules
  - m4-json-api-tutorial
---

# Canton 与 JSON Ledger API

> 使用 curl 与 TypeScript 入门 Canton 与 JSON Ledger API

## 使用 Canton 与 JSON Ledger API 入门

本教程演示如何从命令行经 JSON Ledger API 与 Canton Ledger 交互，使用 `curl`，可选 `websocat`。

### 概览

本示例展示如何：

* 在 Canton 配置中启用 JSON Ledger API
* 用 JSON Ledger API 与基本 Bash 工具（`curl`）创建合约
* 用 `curl` 列出活跃合约
* 基本错误处理与排错

### 前置条件

#### 工具

运行项目前确保已安装：

* 兼容 Bash 的终端（如 macOS Terminal、Git Bash 等）
* **Dpm** — 按说明安装

<div className="parsed-literal">
  curl -sSL [https://get.digitalasset.com/install/install.sh](https://get.digitalasset.com/install/install.sh) | sh -s

  （在 bash 控制台输入 `dpm version --active` 检查已安装 dpm 版本，应至少为指定版本）
</div>

* `canton` — 含安装与示例的 Canton 发行版，详见 Canton demo
* `curl` — 命令行 HTTP 客户端：[https://github.com/curl/curl](https://github.com/curl/curl)（安装：[https://curl.se/download.html](https://curl.se/download.html)）
* （可选）`jq` — 命令行 JSON 处理器：[https://github.com/jqlang/jq](https://github.com/jqlang/jq)（安装：[https://jqlang.org/download/](https://jqlang.org/download/)）

#### Daml 模型

演示 JSON Ledger API 需要示例 Daml 模型。

在控制台运行：

```
dpm new json-tests
```

应创建名为 `json-tests` 的文件夹。检查内容并查看 `daml/Main.daml` 中的代码。

应含名为 `Asset` 的 template：

```
template Asset
  with
    issuer : Party
    owner  : Party
    name   : Text
  where
    ensure name /= ""
    signatory issuer
    observer owner
    choice Give : AssetId
      with
        newOwner : Party
      controller owner
      do create this with
        owner = newOwner
```

继续前，在文件夹内运行以下命令编译 Daml 模型：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
dpm build
```

应创建 `.daml/dist/json-tests-0.0.1.dar`。

### 启动带 JSON Ledger API 的 Canton

首先确保能运行启用了 JSON Ledger API 的 Canton sandbox。

启动 Canton sandbox，提供已创建 `dar` 文件的路径：

```
dpm sandbox --json-api-port 7575 --dar &lt;path_to_json_tests_project&gt;/.daml/dist/json-tests-0.0.1.dar
```

<Note>
  为简化本教程，未使用安全配置。你可以任意用户身份发送命令。
</Note>

打开新 Bash 终端，保持 Canton sandbox 运行。

#### 验证 — 下载 OpenAPI

验证 JSON Ledger API 是否工作，检查文档端点是否可用。

在新 Bash 终端运行：

```
curl localhost:7575/docs/openapi
```

应收到以以下内容开头的长 YAML 文档：

```
openapi: 3.0.3
info:
  title: JSON Ledger API HTTP endpoints
  version: 3.3.0
paths:
  /v2/commands/submit-and-wait:
    post:
```

此 `openapi.yaml` 概述可用端点，可粘贴到 [https://editor-next.swagger.io](https://editor-next.swagger.io) 等工具。

也可用于生成 `Java` 或 `TypeScript` 等语言的客户端 stub。

<Note>
  可用 `http://localhost:757/livez` 端点检查服务器是否运行，生产环境可用作健康检查。
</Note>

#### 创建 party

在终端运行：

```
curl -d '{"partyIdHint":"Alice", "identityProviderId": ""}' -H "Content-Type: application/json" -X POST localhost:7575/v2/parties
```

应返回类似：

```
{"partyDetails":{"party":"Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141","isLocal":true,"localMetadata":{"resourceVersion":"0","annotations":{}},"identityProviderId":""}}
```

记下 party ID，后续步骤使用。本例为：

`Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141` — 你的环境会不同。

### 创建合约

创建 `create.json`，内容如下，将 `\<partyId\>` 替换为实际 party ID：

```
{
  "commands": [
    {
      "CreateCommand": {
        "createArguments": {
          "issuer": "<partyId>",
          "owner": "<partyId>",
          "name": "Example Asset Name"
        },
        "templateId": "#json-tests:Main:Asset"
      }
    }
  ],
  "userId": "ledger-api-user",
  "commandId": "example-app-create-1234",
  "actAs": [
    "<partyId>"
  ],
  "readAs": [
    "<partyId>"
  ]
}
```

提交请求：

```
curl localhost:7575/v2/commands/submit-and-wait -H "Content-Type: application/json" -d@create.json
```

成功响应类似：

```
{"updateId":"...","completionOffset":20}
```

确认合约已在账本上创建。

### 查询账本

查询活跃合约，先创建 `acs.json`：

```
{
  "eventFormat": {
    "filtersByParty": {},
    "filtersForAnyParty": {
      "cumulative": [
        {
          "identifierFilter": {
            "WildcardFilter": {
              "value": {
                "includeCreatedEventBlob": true
              }
            }
          }
        }
      ]
    },
    "verbose": false
  },
  "verbose": false,
  "activeAtOffset": <offset>
}
```

将 `\<offset\>` 替换为之前收到的 `completionOffset`（如 `20`）。

运行查询：

```
curl localhost:7575/v2/state/active-contracts -H "Content-Type: application/json" -d@acs.json
```

应收到含合约信息的响应。

为提高可读性，管道到 `jq`：

```
curl localhost:7575/v2/state/active-contracts -H "Content-Type: application/json" -d@acs.json | jq
```

查找 `createdEvent` 段，含合约详情如：

```
"createdEvent": {
      "offset": 20,
      "nodeId": 0,
      "contractId": "00572c50513ced94f9cddaf1e6d2d3f050ae35d7fea0affe06f65f4238e84136edca1112202d01e45b5cfafb61e3942e4610547689dbebfebd3ea7d10d57944401fc17e81b",
      "templateId": "6fd1d46124d5ab0c958ce35e9bb370bb2835b2672a0d6fa039a3855c11b8801d:Main:Asset",
      "contractKey": null,
      "createArgument": {
        "issuer": "Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141",
        "owner": "Alice::122084768362d0ce21f1ffec870e55e365a292cdf8f54c5c38ad7775b9bdd462e141",
        "name": "Example Asset Name"
      },
  ...
}
```

### 排错

用 curl 调用遇问题时，启用 `-v`（verbose）查看请求与响应详情，例如：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl -v -d '{"partyIdHint":"Alice", "identityProviderId": ""}' -H "Content-Type: application/json" -X POST localhost:7575/v2/parties
```

HTTP 响应非 200（如 400、404）表示错误，响应体含错误详情。

若仍无法解决，查看 canton sandbox 终端或 `\<canton_installation\>/logs/canton.log` 中的日志。

查询 `localhost:7575/v2/state/active-contracts` 无返回时，确保 offset 正确且对应 `localhost:7575/v2/commands/submit-and-wait` 的 `completionOffset`。也可运行以下命令查看当前 offset：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
curl localhost:7575/v2/state/ledger-end
```

### 下一步

#### Canton 示例

涉及两个 party 的更高级场景，见 Canton 安装附带的示例：`\<canton_installation\>/examples/json-ledger-api\>`

另有 `TypeScript` 版本演示如何在 Web 浏览器中创建 JSON Ledger API 客户端。

#### OpenAPI 与 AsyncAPI

阅读 Canton JSON Ledger API 的 OpenAPI 与 AsyncAPI 规范：`references_json-api`。

#### 认证与安全

阅读如何配置并使用 jwt token 访问 JSON Ledger API：`json-api-access-tokens`。

#### 错误码

JSON Ledger API 返回的错误码更多信息见 `json-error-codes`。

## 使用 Canton、JSON Ledger API 与 TypeScript 入门

本教程展示如何用 JSON Ledger API 与 TypeScript 与 Canton Ledger 交互。

### 概览

你将使用并修改 Canton 发行版提供的现有示例项目。

### 前置条件

应熟悉 TypeScript 基础及 `npm`、`node.js` 等工具。

#### 工具

开始前确保已安装：

* **Node.js 与 npm** — 从 [https://nodejs.org/en/download/](https://nodejs.org/en/download/) 下载。推荐版本 `18.20.x` 或更高。
* **Dpm** — 按说明安装

<div className="parsed-literal">
  curl -sSL [https://get.digitalasset.com/install/install.sh](https://get.digitalasset.com/install/install.sh) | sh -s
</div>

验证安装：

```shell theme={"theme":{"light":"github-light","dark":"github-dark"}}
  dpm version --active

```

应看到等于或高于要求的版本。

* **Canton** — 含预构建示例。详见 Canton demo。

#### 示例 TypeScript 项目

打开终端并进入 JSON Ledger API 示例文件夹：

```
cd &lt;canton_installation&gt;/examples/09-json-ledger-api
```

启动 Canton：

```
./run.sh
```

Canton 控制台就绪后，打开新终端进入 TypeScript 示例文件夹：

```
cd &lt;canton_installation&gt;/examples/09-json-ledger-api/typescript
```

### 运行示例

安装项目依赖：

```
npm install
```

可能看到警告，暂时可忽略。

JSON Ledger API 提供 OpenAPI 规范，可用于生成 TypeScript 客户端类（stub）。

生成 TypeScript 客户端：

```
npm run generate_api
```

检查 `generated/api` 文件夹中的生成代码，应含 API 的 TypeScript 类。

```
less generated/api/ledger-api.d.ts
```

该文件含服务与模型定义，如 `/v2/commands/submit-and-wait`、`CreateCommand` 等。

接下来从 Daml 模型生成 TypeScript 类型：

```
npm run generate_daml_bindings
```

在 `./generated` 文件夹创建绑定。每个 Daml 模块有子文件夹，例如 `generated/model-tests-1.0.0/lib/Iou`。

编译 TypeScript 代码：

```
npm run build
```

构建成功后运行示例：

```
npm run scenario
```

应看到类似输出：

```
Alice creates contract
Ledger offset: 23
...
Bob accepts transfer
...
End of scenario
```

### 代码要点

JSON Ledger API 客户端在 `src/client.ts` 中配置：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
import type { paths } from "../generated/api/ledger-api";

export const client = createClient<paths>({ baseUrl: "http://localhost:7575" });
```

使用 `openapi-fetch` 库创建 API 客户端。

#### 分配 Party

在 `src/user.ts` 中分配 party：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const resp = await client.POST("/v2/parties", {
    body: {
        partyIdHint: user,
        identityProviderId: "",
    }
});
```

<Note>
  `openapi-fetch` 使用 TypeScript 索引访问类型提供类型安全。上例看起来像无类型 JavaScript，实际是类型安全的。
</Note>

#### 创建合约

在 `src/commands.ts` 中创建合约：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export async function createContract(userParty: string): Promise<components["schemas"]["SubmitAndWaitResponse"]> {
    const iou: Iou.Iou = {
        issuer: userParty,
        owner: userParty,
        currency: "USD",
        amount: "100",
        observers: []
    };

    const command: components["schemas"]["CreateCommand"] = {
        createArguments: iou,
        templateId: Iou.Iou.templateId
    };

    const jsCommands = makeCommands(userParty, [{ CreateCommand: command }]);
    const resp = await client.POST("/v2/commands/submit-and-wait", {
        body: jsCommands
    });

    return valueOrError(resp);
}
```

#### 查询合约

在 `src/index.ts` 中查询合约：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
const { data, error } = await client.POST("/v2/state/active-contracts", {
    body: filter
});

if (data === undefined)
    return Promise.reject(error);
else {
    const contracts: components["schemas"]["CreatedEvent"][] = data
        .map((res) => res.contractEntry)
        .filter((res) => "JsActiveContract" in res)
        .map((res) => res.JsActiveContract.createdEvent);

    return Promise.resolve(contracts);
}
```

### 扩展示例

本步为 `Iou` template 添加新字段并相应更新 TypeScript 代码。

1. 打开 `canton/examples/09-json-ledger-api/model` 中的 `Io.daml`。
2. 修改 `Iou` template 添加 `comment` 字段：

```haskell theme={"theme":{"light":"github-light","dark":"github-dark"}}
template Iou
  with
    issuer : Party
    owner : Party
    currency : Text
    amount : Decimal
    observers : [Party]
    comment : Optional Text -- added field
  where
    -- leave the rest of the template unchanged
```

> `comment` 字段为可选，属向后兼容变更。

3. 停止 Canton 服务器（`Ctrl+C`）并重启：

```
./run.sh
```

4. 重建 TypeScript 绑定：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
npm run generate_daml_bindings
```

5. 更新 `src/commands.ts` 中的 `createContract` 函数以包含新字段：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
export async function createContract(userParty: string): Promise<components["schemas"]["SubmitAndWaitResponse"]> {
    const iou: Iou.Iou = {
        issuer: userParty,
        owner: userParty,
        currency: "USD",
        amount: "100",
        observers: [],
        comment: "This is a test comment" // new field
    };
    // leave the rest of the function unchanged
```

6. 重建 TypeScript 代码：

```
npm run build
```

7. 运行示例：

```
npm run scenario
```

输出中尚看不到新 `comment` 字段。要显示它，修改 `src/index.ts` 中的 `showAcs` 调用以包含新字段：

```typescript theme={"theme":{"light":"github-light","dark":"github-dark"}}
showAcs(contracts, ["owner", "amount", "currency", "comment"], c => [c.owner, c.amount, c.currency, c.comment]);
```

然后再次执行 `npm run scenario`。

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
