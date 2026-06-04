---
title: "Canton Console Reference"
slug: "global-synchronizer-reference-canton-console-reference"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/reference/canton-console-reference.md"
source_title: "Canton Console Reference"
tags:
  - global-synchronizer
  - reference
  - canton-console-reference
---

# Canton Console Reference

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Canton Console Reference

> Reference for Canton console commands used by validators and SV operators on the Global Synchronizer

For more involved debugging and disaster recovery, direct access to the console of a Canton node (participant, sequencer, mediator) might be required. Steps to obtain such access:

Requirements:

* Direct access to the Canton node process
* Canton binary

Once you see the following banner for the console you have successfully gained access

```text theme={"theme":{"light":"github-light","dark":"github-dark"}}
_____            _
/ ____|          | |
| |     __ _ _ __ | |_ ___  _ __
| |    / _` | '_ \| __/ _ \| '_ \
| |___| (_| | | | | || (_) | | | |
\_____\__,_|_| |_|\__\___/|_| |_|

Welcome to Canton!
```

## Participant console

1. Obtain an authentication token as specified in [the Canton authentication docs](/global-synchronizer/reference/security-configuration#configure-api-authentication-and-authorization-with-jwt)

2. Ensure you can access the participant's ports 5001 and 5002

3. Add the configuration to a local file `console.conf`
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

4. Run the docker command

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

Running docker with the default network (`splice-validator`):

<Tabs>
  <Tab title="DevNet (0.6.4)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network splice-validator -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </Tab>
</Tabs>

## Sequencer console

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Ensure you can access the sequencer's ports 5008 and 5009

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </Tab>
</Tabs>

## Mediator console

<Tabs>
  <Tab title="DevNet (0.6.4)">
    1. Ensure you can access the mediator's port 5007

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.4 --console
    ```
  </Tab>

  <Tab title="TestNet (0.6.3)">
    1. Ensure you can access the mediator's port 5007

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.3 --console
    ```
  </Tab>

  <Tab title="MainNet (0.6.2)">
    1. Ensure you can access the mediator's port 5007

    2. Add the configuration to a local file `console.conf`

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

    3. Run the docker command

    ```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
    docker run -it --rm --network host -v $(pwd)/console.conf:/app/app.conf ghcr.io/digital-asset/decentralized-canton-sync/docker/canton:0.6.2 --console
    ```
  </Tab>
</Tabs>

## Access in a K8s cluster

In a K8s cluster you can use a debug pod to access the console directly from the cluster.

First you can create a pod running the right canton version using:

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
kubectl debug "${POD_NAME}" --image "$(kubectl get pod "${POD_NAME}" -o json | jq -re '.spec.containers[0].image')" -i -t -- bash
```

where `POD_NAME` is the name of the participant/sequencer/mediator pod.

Once you are inside the running pod you can install a text editor and create the config file `console.conf` that is described above.

```bash theme={"theme":{"light":"github-light","dark":"github-dark"}}
$ apt-get update
$ apt-get install -y vim
$ vim console.conf # paste in the config from above
$ /app/bin/canton -v -c console.conf
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
