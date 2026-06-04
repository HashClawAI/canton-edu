---
title: "Canton Console 参考"
slug: "global-synchronizer-reference-canton-console-reference"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/canton-console-reference.md"
source_title: "Canton Console Reference"
tags:
  - global-synchronizer
  - reference
  - canton-console-reference
---

# Canton Console 参考

> Global Synchronizer 运维使用的 Canton Console 参考。

> 全局同步器上验证器和 SV 操作员使用的 Canton 控制台命令参考

对于更多涉及的调试和灾难恢复，可能需要直接访问 Canton 节点（参与者、定序器、调解器）的控制台。获得此类访问权限的步骤：

要求：

* 直接访问Canton节点流程
* Canton 二进制

一旦您看到控制台的以下横幅，您就已成功获得访问权限

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
_____            _
/ ____|          | |
| |     __ _ _ __ | |_ ___  _ __
| |    / _` | '_ \| __/ _ \| '_ \
| |___| (_| | | | | || (_) | | | |
\_____\__,_|_| |_|\__\___/|_| |_|

Welcome to Canton!
```

## 参与者控制台

1. 获取 [Canton 身份验证文档](/zh/docs/canton/global-synchronizer-reference-security-configuration#configure-api-authentication-and-authorization-with-jwt) 中指定的身份验证令牌

2. 确保您可以访问与会者的端口5001和5002

3. 将配置添加到本地文件`console.conf`
   ```
   canton {
     remote-participants {
       participant {
         admin-api {
           port = 5002
           address = localhost
         }
         ledger-api {
           port = 5001
           address = localhost
         }
         token = "<auth token>"
       }
     }
     features.enable-preview-commands = yes
     features.enable-testing-commands = yes
     features.enable-repair-commands = yes
   }
   ```

4.运行docker命令

<标签>
  <Tab title="DevNet (0.6.4)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </标签>

  <Tab title="测试网 (0.6.3)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </标签>
</标签>

<警告>
  如果您使用 docker compose setup 运行参与者，则必须使用参与者使用的 docker 网络运行 docker 命令。调整配置以连接到参与者容器：
</警告>

```
canton {
  remote-participants {
    participant {
      admin-api {
        port = 5002
        address = 参与方
      }
      ledger-api {
        port = 5001
        address = 参与方
      }
      token = "<auth token>"
    }
  }
  features.enable-preview-commands = yes
  features.enable-testing-commands = yes
  features.enable-repair-commands = yes
}
```

使用默认网络运行 docker (`splice-验证者`)：

<标签>
  <Tab title="DevNet (0.6.4)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-验证者 -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </标签>

  <Tab title="测试网 (0.6.3)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-验证者 -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-验证者 -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </标签>
</标签>

## 音序器控制台

<标签>
  <Tab title="DevNet (0.6.4)">
    1. 确保您可以访问定序器的端口 5008 和 5009

    2. 将配置添加到本地文件`console.conf````
    canton {
      remote-sequencers {
        sequencer {
          public-api {
            port = 5008
            address = localhost
          }
          admin-api {
            port = 5009
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </标签>

  <Tab title="测试网 (0.6.3)">
    1. 确保您可以访问定序器的端口 5008 和 5009

    2. 将配置添加到本地文件`console.conf`

    ```
    canton {
      remote-sequencers {
        sequencer {
          public-api {
            port = 5008
            address = localhost
          }
          admin-api {
            port = 5009
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    1. 确保您可以访问定序器的端口 5008 和 5009

    2. 将配置添加到本地文件`console.conf`

    ```
    canton {
      remote-sequencers {
        sequencer {
          public-api {
            port = 5008
            address = localhost
          }
          admin-api {
            port = 5009
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </标签>
</标签>

## 中介控制台

<标签>
  <Tab title="DevNet (0.6.4)">
    1.确保可以访问Mediator的5007端口

    2. 将配置添加到本地文件`console.conf`

    ```
    canton {
      remote-mediators {
        mediator {
          admin-api {
            port = 5007
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </标签>

  <Tab title="测试网 (0.6.3)">
    1.确保可以访问Mediator的5007端口

    2. 将配置添加到本地文件`console.conf`

    ```
    canton {
      remote-mediators {
        mediator {
          admin-api {
            port = 5007
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </标签>

  <Tab title="主网 (0.6.2)">
    1.确保可以访问Mediator的5007端口

    2. 将配置添加到本地文件`console.conf`

    ```
    canton {
      remote-mediators {
        mediator {
          admin-api {
            port = 5007
            address = localhost
          }
        }
      }
      features.enable-preview-commands = yes
      features.enable-testing-commands = yes
      features.enable-repair-commands = yes
    }
    ```

    3.运行docker命令```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </标签>
</标签>

## K8s集群中的访问

在 K8s 集群中，您可以使用调试 Pod 直接从集群访问控制台。

首先，您可以使用以下命令创建一个运行正确 Canton 版本的 Pod：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl debug "${POD_NAME}" --image "$(kubectl get pod "${POD_NAME}" -o json | jq -re '.spec.containers[0].image')" -i -t -- bash
```

其中 `POD_NAME` 是参与者/排序器/中介器 Pod 的名称。

进入正在运行的 Pod 后，您可以安装文本编辑器并创建如上所述的配置文件 `console.conf`。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
$ apt-get update
$ apt-get install -y vim
$ vim console.conf # paste in the config from above
$ /app/bin/canton -v -c console.conf
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
