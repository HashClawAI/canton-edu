---
title: "Console 概览"
slug: "global-synchronizer-canton-console-console-overview"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/canton-console/console-overview.md"
source_title: "Console Overview"
tags:
  - global-synchronizer
  - canton-console
  - console-overview
---

# Console 概览

> 验证者与 SV 节点 Canton Console 访问方式概览。

> 访问并使用Canton Console进行验证器和SV节点操作

对于更多涉及的调试和灾难恢复，可能需要直接访问 Canton 节点（参与者、Sequencer、Mediator）的控制台。获得此类访问权限的步骤：

要求：

* 直接访问 Canton 节点进程
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

## Participant 控制台

1. 获取 [Canton 身份验证文档](/global-synchronizer/reference/security-configuration#configure-api-authentication-and-authorization-with-jwt) 中指定的身份验证令牌

2. 确保您可以访问participant 的端口5001和5002

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

<Tabs>
  <Tab title="DevNet (0.6.4)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </Tab>
</Tabs>

<Warning>
  If you run the participant using the docker compose setup the docker command must be run with the docker network used by the participant. Adjust the configuration to connect to the participant container:
</Warning>

```
canton {
  remote-participants {
    participant {
      admin-api {
        port = 5002
        address = participant
      }
      ledger-api {
        port = 5001
        address = participant
      }
      token = "<auth token>"
    }
  }
  features.enable-preview-commands = yes
  features.enable-testing-commands = yes
  features.enable-repair-commands = yes
}
```

使用默认网络运行 docker (`splice-validator`)：

<Tabs>
  <Tab title="DevNet (0.6.4)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </Tab><Tab title="TestNet (0.6.3)">
    ```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
      _____            _
     / ____|          | |
    | |     __ _ _ __ | |_ ___  _ __
    | |    / _` | '_ \| __/ _ \| '_ \
    | |___| (_| | | | | || (_) | | | |
     \_____\__,_|_| |_|\__\___/|_| |_|

     Welcome to Canton!
```
  </Tab>

  <Tab title="MainNet (0.6.2)">
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
  </Tab>
</Tabs>

## Sequencer 控制台

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```

    3. Run the docker command

    ```
canton {
  remote-participants {
    participant {
      admin-api {
        port = 5002
        address = participant
      }
      ledger-api {
        port = 5001
        address = participant
      }
      token = "<auth token>"
    }
  }
  features.enable-preview-commands = yes
  features.enable-testing-commands = yes
  features.enable-repair-commands = yes
}
```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>
</Tabs>

## Mediator 控制台

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1.确保可以访问Mediator的5007端口

    2. 将配置添加到本地文件`console.conf````
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
  </Tabs>

  <Tab title="TestNet (0.6.3)">
    1. Ensure you can access the mediator's port 5007

    2. Add the configuration to a local file `console.conf`

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Ensure you can access the mediator's port 5007

    2. Add the configuration to a local file `console.conf`

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```

    3. Run the docker command

    ```
canton {
  remote-participants {
    participant {
      admin-api {
        port = 5002
        address = participant
      }
      ledger-api {
        port = 5001
        address = participant
      }
      token = "<auth token>"
    }
  }
  features.enable-preview-commands = yes
  features.enable-testing-commands = yes
  features.enable-repair-commands = yes
}
```
  </Tab>
</Tabs>

## K8s集群中的访问

在 K8s 集群中，您可以使用调试 Pod 直接从集群访问控制台。

首先，您可以使用以下命令创建一个运行正确 Canton 版本的 Pod：

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl debug "${POD_NAME}" --image "$(kubectl get pod "${POD_NAME}" -o json | jq -re '.spec.containers[0].image')" -i -t -- bash
```

其中 `POD_NAME` 是参与者/排序器/中介 pod 的名称。

进入正在运行的 Pod 后，您可以安装文本编辑器并创建如上所述的配置文件 `console.conf`。

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
$ apt-get update
$ apt-get install -y vim
$ vim console.conf # paste in the config from above
$ /app/bin/canton -v -c console.conf
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
