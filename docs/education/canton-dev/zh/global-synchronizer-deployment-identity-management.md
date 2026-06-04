---
title: "Canton 身份管理"
slug: "global-synchronizer-deployment-identity-management"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/deployment/identity-management.md"
source_title: "Canton Identity Management"
tags:
  - global-synchronizer
  - deployment
  - identity-management
---

# Canton 身份管理

> Canton 身份架构、拓扑事务与用户/参与方身份管理参考。

> Canton 身份架构、拓扑事务和身份管理指南

将整个页面分成几个部分以获取特定的操作指南。概述站点涵盖了高级解释。

# 身份管理

账本上的身份管理侧重于 Canton 系统实体中身份的分布式方面，而用户身份管理则侧重于管理用户对其账本 API 的访问的各个参与者。

Canton 配备了内置身份管理系统，用于管理账本身份。技术细节在架构部分进行了解释，而本文的目的是提供高级解释。

身份管理系统是独立的，无需受信任的中央实体或预定义的根证书而构建，因此任何人都可以与任何人连接，无需某些中央批准，也没有失去自我主权的危险。

## 简介

### 什么是广州身份？

当两个系统实体（例如参与者、同步器拓扑管理器、中介器或定序器）相互通信时，它们将使用非对称加密技术来加密消息并对消息内容进行签名，以便只有接收者才能解密内容、验证消息的真实性或证明其来源。因此，我们需要一种唯一标识系统实体的方法以及将加密和签名密钥与其关联的方法。

最重要的是，Canton 使用合同语言 Daml，它通过[当事人](/zh/docs/canton/overview-understand-glossary) 代表合同所有权和权利。但政党并不是广州同步协议的主要成员。他们由参与者代表，因此我们需要唯一地标识政党并将其与参与者联系起来，以便一个参与者可以代表多个政党（在广州，一个政党可以由多个参与者代表）。

### 唯一标识符

坎顿身份由两个部分组成：随机字符串`X`和公钥指纹`N`。这种组合，`(X,N)`，被称为*唯一标识符*，并且被设计为全局唯一。此唯一标识符在 Canton 中用于指代特定各方、参与者或同步器实体。系统实体（例如一方）由角色（一方、参与者、中介者、定序器、同步器拓扑管理器）及其唯一标识符的组合来描述。系统实体需要了解相应其他实体用于加密和签名的密钥。这种知识是分布式的，因此，系统实体需要一种方法来验证实体与密钥的某种关联是否正确且有效。这就是唯一标识符中公钥指纹的目的，该标识符称为*命名空间*。相应命名空间的密钥充当该特定命名空间的“信任根”，如下所述。

### 拓扑事务

为了保持灵活性并能够更改密钥和加密算法，我们不使用单个静态密钥来识别实体，但我们需要一种方法来动态地将参与者或同步器实体与密钥以及各方与参与者相关联。我们通过拓扑事务来做到这一点。

拓扑事务建立唯一标识符与键的某种关联或与另一个标识符的关系。有几种不同类型的拓扑事务。最通用的是`OwnerToKeyMapping`，顾名思义，它将密钥与唯一标识符相关联。这样的拓扑事务将通知所有其他系统实体某个系统实体正在使用特定密钥用于特定目的，例如命名空间*12345..*的参与者*Alice*正在使用通过指纹*AABBCCDDEE..*识别的密钥来签署消息。

现在，这就提出了两个问题：谁授权这些交易，以及谁分发这些交易？

对于授权，我们需要查看唯一标识符的第二部分，*命名空间*。引用特定唯一标识符的拓扑事务在该命名空间上运行，我们要求这样的拓扑事务由相应的密钥通过序列化拓扑事务的加密签名进行授权。此授权可以是直接的（如果由命名空间的密钥签名）或间接的（如果由委托密钥签名）。要将签名权委托给另一个密钥，可以使用 *NamespaceDelegation* 或 *IdentifierDelegation* 类型的其他拓扑事务来执行此操作。命名空间委托将整个命名空间委托给某个密钥，例如通过指纹 *AABBCCDDEE...* 表示密钥标识符现在可以授权密钥 *VVWWXXYYZZ...* 的命名空间内的拓扑事务。拓扑事务的签名发生在`TopologyManager`中。 Canton 有许多拓扑管理器。每个参与节点和每个同步器都有拓扑管理器，其功能完全相同，只是影响不同。他们可以创建新的密钥、新的命名空间以及新参与者、各方和同步器的身份。他们可以导出这些拓扑事务，以便可以由另一个拓扑管理器导入。这使您可以通过多种方式管理 Canton 身份。参与者可以操作自己的拓扑管理器，这允许他们单独管理他们的各方。或者他们可以将自己与另一个拓扑管理器关联起来，让他们管理他们所代表的各方或他们使用的密钥。或者介于两者之间，具体取决于介绍的代表团和协会。

同步器拓扑管理器和参与者拓扑管理器之间的区别在于，同步器拓扑管理器通过以每个同步器成员最终具有相同拓扑状态的方式分发拓扑事务来在特定同步器中建立有效拓扑状态。然而，同步器拓扑管理器只是同步器的看门人，决定谁被允许进入以及谁不在该特定同步器上，但实际的拓扑语句源自各种来源。因此，同步器拓扑管理器只能阻止分发，而不能伪造拓扑事务。

参与者拓扑管理器仅管理孤立的拓扑状态。但是，有一个附加到此特定拓扑管理器的调度程序，它尝试通过将本地注册的身份发送到同步器拓扑管理器来向远程同步器注册，然后由同步器拓扑管理器决定是否要包含它们。

细心的读者会注意到，所描述的身份系统确实没有单一的信任根或决策者来判断谁是整个系统的一部分。而且分布式同步的拓扑状态因同步器而异，从而允许非常灵活的拓扑和设置。

### 法律身份在Canton，我们将系统身份与法律身份分开。虽然上述机制允许建立系统实体的公共、经过验证和授权的知识，但它并不能保证某个唯一标识符确实对应于特定的合法身份。更重要的是，虽然唯一标识符保持稳定，但合法身份可能会发生变化，例如在两家公司合并的情况下。因此，Canton 提供了一种管理命令，允许人们使用 `participant.parties.set_display_name` 命令将随机系统身份与人类可读的“显示名称”相关联。

<注意>
  聚会显示名称对于参与者来说是私有的。如果这些名称应该在参与者之间共享，我们建议构建相应的 Daml 工作流程和一些自动化逻辑，监听 Daml 工作流程的结果并相应地更新显示名称。
</注>

### 派对生活

在教程中，我们使用 `participant.parties.enable("name")` 函数在参与者上设置聚会。要了解广州的身份管理系统，了解添加新方的幕后步骤会有所帮助：1. `participant.parties.enable`函数确定参与者的唯一标识符：`participant.id`。
2. 队伍名称构建为 name::，其中`namespace` 为参与者之一。
3. 在管理 API 上授权新的参与方到参与者映射：`participant.topology.party_to_participant_mappings.authorize(...)`
4. GRPC 请求调用`ParticipantTopologyManager`，创建新的`SignedTopologyTransaction`，并测试是否可以将授权添加到本地拓扑状态。如果可以，则将新的拓扑事务添加到存储中。
5. `ParticipantTopologyDispatcher` 获取新事务，并通过定序器发送到拓扑管理器的 `RegisterTopologyTransactionRequest` 消息请求在所有同步器上进行添加。
6. 同步器接收该请求并根据策略（开放或许可）对其进行处理。默认设置是打开的。
7. 如果获得批准，请求服务将尝试将新的拓扑事务添加到`同步器TopologyManager`。
8. `同步器TopologyManager` 检查新的拓扑事务是否可以添加到同步器拓扑状态中。如果是，则将其写入本地拓扑存储。
9. `ParticipantTopologyDispatcher` 获取新交易并通过排序器将其发送给所有参与者（并返回给自身）。
10. 定序器为事务添加时间戳并将其嵌入到事务流中。
11. 参与者收到交易，根据拓扑状态验证完整性和正确性，并将其添加到带有定序器时间戳的状态中，这样每个人都有一个同步的拓扑状态。

请注意，仅当参与者自己控制其名称空间时，`participant.parties.enable` 宏才有效，无论是直接通过名称空间密钥还是通过委托（通过`NamespaceDelegation`）。

### 参与者入职

支持拓扑灵活性的关键是参与者可以轻松添加到新的同步器中。因此，新参与者加入同步器需要安全且方便。查看控制台命令，我们注意到在大多数示例中，我们使用 `connect` 命令将参与者连接到同步器。 connect 命令只是包装了一组 admin-api 命令：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val certificates = OptionUtil.emptyStringAsNone(certificatesPath).map { path =>
  BinaryFileUtil.readByteStringFromFile(path) match {
    case Left(err) => throw new IllegalArgumentException(s"failed to load $path: $err")
    case Right(bs) => bs
  }
}
同步器ConnectionConfig.tryGrpcSingleConnection(
  同步器Alias,
  sequencerAlias,
  connection,
  manualConnect,
  physical同步器Id,
  certificates,
  priority,
  initialRetryDelay,
  maxRetryDelay,
  timeTrackerConfig,
)
```

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// connect to the new 同步器
consoleEnvironment.run {
  ParticipantCommands.同步器s.connect(runner, config, validation)
}
```

我们注意到，从用户的角度来看，默认情况下需要发生的只是提供连接信息并接受服务条款（如果同步器需要）以建立新的同步器连接。没有执行单独的加入步骤，没有发生巨大的证书签名练习，一切都在第一次连接尝试期间设置。然而，在幕后发生了相当多的步骤。因此，我们在这里一步步简单总结一下这个过程：1. 现有参与者的管理员需要调用`同步器s.connect_local`命令添加新的同步器。强制参数是同步器*别名*（在内部用于指代特定连接）和定序器连接 URL（HTTP 或 HTTPS），包括可选端口 *http\[s]://hostname\[:port]/path*。可选的是自定义 TLS 证书链的证书路径（否则使用默认的 jre 根证书）和同步器的 *同步器 id*。 *同步器 id* 是同步器的唯一标识符，可以定义它来防止中间人攻击（与 SSH 密钥指纹非常相似）。
2. 参与者打开`SequencerConnectService`的GRPC通道。
3. 参与者联系`SequencerConnectService`，检查使用同步器是否需要签署特定的服务条款。如果需要，服务条款会显示给用户，并且批准会存储在参与者本地以供以后使用。如果获得批准，参与者将尝试连接到定序器。
4. 参与者使用`SequencerConnectService.handshake`验证远程同步器正在运行与参与者版本兼容的协议版本。如果参与者运行不兼容的协议版本，连接将会失败。
5. 参与者从同步器下载并验证同步器ID。同步器ID可用于验证同步器实体的拓扑事务的正确授权。如果之前在 `同步器s.connect_local` 调用期间（或在之前的会话中）提供了同步器 ID，则会比较这两个 ID。如果它们不相等，则连接失败。如果在 `同步器s.connect_local` 调用期间未提供同步器 ID，参与者将使用并存储下载的同步器 ID。我们在这里假设同步器 ID 是由参与者通过安全通道获取的，这样它就一定会与正确的同步器进行对话。因此，这个安全通道可以是在 Canton 之外发生的事情，也可以是在我们第一次联系同步器时由 TLS 提供的。
6. 参与者下载*静态同步器参数*，这是用于特定同步器上的交易协议的参数，例如该同步器支持的加密密钥。7. 参与者最初作为未经身份验证的成员连接到定序器。此类成员只能将事务发送到同步器拓扑管理器。然后，参与者将识别参与者所需的一组初始拓扑事务发送到`同步器TopologyManagerRequestService`并定义参与者使用的密钥。请求服务检查事务的有效性并根据配置的同步器加载策略做出决定。当前支持的策略是`open`（默认）和`permissioned`。虽然`open`对于无需许可的系统和开发来说很方便，但它会接受任何新的参与者和任何拓扑交易。仅当参与者事先被添加到允许列表中时，`permissioned` 政策才会接受参与者的入职交易。
8. 请求服务将事务转发到同步器拓扑管理器，后者尝试将它们添加到状态（从而触发向同步器上其他成员的分发）。加入请求的结果将发送给未经身份验证的成员，该成员在收到响应后会断开连接。
9. 如果加入请求获得批准，参与者现在将尝试作为实际参与者连接到排序器。
10. 一旦参与者在同步器上正确启用并且其签名密钥已知，参与者就可以使用其身份订阅`SequencerService`。为此并验证`SequencerService`上任何操作的授权，参与者必须从同步器获取授权令牌。为此，参与者向同步器请求`Challenge`。同步器将为其提供`nonce`和用于身份验证的密钥指纹。参与者使用相应的私钥对该随机数（与同步器 ID 一起）进行签名。指纹的原因很简单：参与者需要使用同步器拓扑状态定义的参与者签名密钥来签署令牌。然而，由于参与者只能通过读取`SequencerService`来了解真实的同步器拓扑状态，因此它无法知道密钥是什么。因此，同步器将这部分同步器拓扑状态公开为授权质询的一部分。
11. 使用创建的身份验证令牌，参与者开始使用*SequencerService*。在同步器一侧，同步器通过验证令牌是否是预期的令牌并由参与者的签名密钥签名来验证令牌的真实性和有效性。该令牌用于验证每个 GRPC 调用，需要定期更新。12. 参与者设置`ParticipantTopologyDispatcher`，该过程尝试将在参与者节点的拓扑管理器创建的所有拓扑事务推送到同步器拓扑管理器。如果参与者使用其拓扑管理器自行管理其身份，则这些事务包含有关注册方或支持的包的所有信息。
13.如上所述，参与者通过定序器接收的第一组消息包含同步器拓扑状态，其包括同步器实体的签名密钥。这些消息由定序器和拓扑管理器签名并且是自洽的。如果参与者知道同步器 ID，他们可以验证他们正在与预期的同步器对话，并且同步器实体的密钥已由管理同步器 ID 的密钥的所有者授权。
14. 一旦读取了初始拓扑事务，参与者就准备好处理事务并发送命令。
15.当（重新）启用参与者时，同步器拓扑调度器分析参与者之前错过的拓扑事务集。在公开启用参与者之前，它通过定序器将这些交易发送给参与者。因此，当参与者开始从定序器读取消息时，最初接收到的消息将是同步器的拓扑状态。### 默认初始化

参与节点和同步器的默认初始化行为是运行它们自己的拓扑管理器。这提供了一种方便、自动的方式来配置节点并使它们无需手动干预即可使用，但可以通过在首次启动之前**设置`auto-init = false`配置选项来关闭它。

在自动初始化期间，会发生以下步骤：

1. 在同步器上，我们生成四个签名密钥：一个用于命名空间，一个用于排序器、中介器和拓扑管理器。在参与者上，我们生成三个密钥：命名空间密钥、签名密钥和加密密钥。
2. 使用命名空间的指纹，我们生成参与者身份。为了便于理解，我们使用配置文件中使用的节点名称。出于隐私原因，这将更改为随机标识符。生成后，我们使用 `set_id` admin-api 调用进行设置。
3. 我们使用命名空间密钥创建根证书作为`NamespaceDelegation`，并使用命名空间密钥进行签名。
4. 然后，我们为参与者或同步器实体创建一个`OwnerToKeyMapping`。

可以设置`init.identity`对象来控制自动初始化的行为。例如，可以控制在初始化期间赋予节点的标识符名称。有 3 种可能的配置：

1.使用节点名称作为节点标识符

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.init.identity = {
  type = auto
  identifier.type = config
}
```

2. 显式设置名称

```conf theme={"theme":{"light":"github-light","dark":"github-dark"}}
  canton.participants.participant1.init.identity {
      type = auto
      identifier.type = random
  }

```

3. 生成随机名称

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.init.identity {
    type = auto
    identifier.type = random
}
```

### 身份设置指南

如前所述，Canton 节点默认自动初始化，运行自己的拓扑管理器。这有利于开发和原型设计。实际部署需要更加小心，因此本节应作为简要指南。

Canton 拓扑管理者有一项决不能失败的关键任务：不要失去对信任根（命名空间密钥）的访问或控制。任何其他密钥问题都可以通过撤销旧密钥并向密钥关联颁发新所有者来恢复。因此，建议参与者和各方与由拓扑管理器管理的命名空间关联，该拓扑管理器具有足够的操作设置以保证命名空间的安全性和完整性。因此，参与者或同步者可以

1. 使用其身份命名空间密钥作为参与者节点的一部分运行自己的拓扑管理器。
2. 在独立的计算机上以自建设置运行自己的拓扑管理器，导出拓扑事务并将其传输到相应的节点（即通过刻录的 CD ROM）。
3. 要求可信拓扑管理器在可信拓扑管理器的命名空间内发布一组标识符作为委托，并将委托导入到本地参与者拓扑管理器。
4. 让受信任的拓扑管理器代表管理所有拓扑状态。

显然，有更多可能的组合和选项，但这里的这些选项描述了一些具有不同安全性和可恢复性选项的常见选项。

为了降低丢失命名空间密钥的风险，可以创建额外的密钥并允许在特定命名空间上操作。事实上，我们建议这样做并避免将根密钥存储在活动节点上。

## 用户身份管理

到目前为止，我们已经介绍了如何管理账本身份。

每个参与者还需要管理对其本地 Ledger API 的访问，并能够代表各方授予应用程序读取或写入该 API 的权限。账本上的身份表示为一方，而账本 API 上的应用程序则表示为用户并进行管理。 Ledger API 服务器通过以下方式管理应用程序的身份：

* 身份验证：识别应用程序对应哪个用户（本质上是通过将应用程序名称与用户名进行匹配）
* 授权：了解经过身份验证的用户拥有哪些权限，并根据这些权限限制他们的 Ledger API 访问

身份验证基于 JWT，并在[授权深入研究](/zh/docs/canton/appdev-deep-dives-authorization) 中介绍；相关的 Ledger API 授权配置在 Ledger API JWT 配置部分中有介绍。

授权由 Ledger API 的用户管理服务管理。本质上，用户是从用户名到一组具有读或写权限的各方的映射。更详细地说，用户包括：

* 用户 ID（也称为用户名）
* 活动/停用状态（可用于暂时禁止用户访问 Ledger API）
* 可选的主要方（指示作为该用户提交 Ledger API 命令请求时默认使用哪一方）
* 一组用户权限（描述用户是否有权访问 Ledger API 的管理部分以及该用户可以充当或读取哪些方）
* 一组自定义注释（基于字符串的键值对，本地存储在 Ledger API 服务器上，可用于向该方附加额外信息，例如它与某些业务实体的关系）除用户 ID 之外的所有这些属性都可以修改。要了解有关注释的更多信息，请参阅 Ledger API 参考文档。有关 Ledger API 的 UserManagementService 的概述，请参阅 [Ledger API 参考](https://docs.canton.network/sdks-tools/api-reference/ledger-api)。

您可以通过 Canton 控制台用户管理命令（alpha 功能）来管理用户。请参阅下面的食谱，了解如何管理用户的一些具体示例。

## 食谱

### 管理用户

在本节中，我们将介绍如何使用 Canton 控制台命令管理参与者用户。首先，我们创建三个参与方，我们将在后续示例中使用它们：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val Seq(alice, bob, eve) = Seq("alice", "bob", "eve").map(p => participant1.parties.enable(name = p))
    Seq(alice, bob, eve) : Seq[PartyId] = List(alice::12201ff69b1d..., bob::12201ff69b1d..., eve::12201ff69b1d...)
```

#### 创建

接下来，创建一个名为 `myuser` 的用户，该用户具有充当 `alice` 和读取为 `bob` 权限以及活动用户状态。该用户的主要政党是`alice`。该用户不是管理员，并且有一些自定义注释。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val user = participant1.ledger_api.users.create(id = "myuser", actAs = Set(alice), readAs = Set(bob), primaryParty = Some(alice), participantAdmin = false, isDeactivated = false, annotations = Map("foo" -> "bar", "description" -> "This is a description"))
    user : User = User(
      id = "myuser",
      primaryParty = Some(value = alice::12201ff69b1d...),
      isDeactivated = false,
      annotations = Map("foo" -> "bar", "description" -> "This is a description"),
      identityProviderId = "",
      primaryPartyAuthentication = false
    )
```

对于有效注释键的构成有一些限制。相反，注释值的唯一约束是它们不能为空。要了解有关注释的更多信息，请参阅 Ledger API 参考文档。

####更新

您可以更新用户的主要方、活动/停用状态和注释。 （您还可以更改用户拥有的权限，但使用下面介绍的不同方法。）

在以下代码片段中，您将用户的主要方更改为未分配，保持活动/停用状态不变，并更新注释。在注释中，您更改 `description` 键的值，删除 `foo` 键并添加新的 `baz` 键。返回值包含用户的更新状态：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val updatedUser = participant1.ledger_api.users.update(id = user.id, modifier = user => { user.copy(primaryParty = None, annotations = user.annotations.updated("description", "This is a new description").removed("foo").updated("baz", "bar")) })
    updatedUser : User = User(
      id = "myuser",
      primaryParty = None,
      isDeactivated = false,
      annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
      identityProviderId = "",
      primaryPartyAuthentication = false
    )
```

您还可以更新用户的身份提供商 ID。在以下代码片段中，您将用户的身份提供商 ID 更改为新创建的 ID。请注意，最初用户属于默认身份提供者，其 id 表示为空字符串 `` `"" ``\`。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.identity_provider_config.create("idp-id1", isDeactivated = false, jwksUrl = "http://someurl", issuer = "issuer1", audience = None)
    res4: com.digitalasset.canton.ledger.api.IdentityProviderConfig = IdentityProviderConfig(
      identityProviderId = Id(value = "idp-id1"),
      isDeactivated = false,
      jwksUrl = JwksUrl(value = "http://someurl"),
      issuer = "issuer1",
      audience = None
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.update_idp("myuser", sourceIdentityProviderId="", targetIdentityProviderId="idp-id1")
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.get("myuser", identityProviderId="idp-id1")
    res6: User = User(
      id = "myuser",
      primaryParty = None,
      isDeactivated = false,
      annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
      identityProviderId = "idp-id1"
    )
```

您可以将用户的身份提供商 ID 更改回默认 ID：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.update_idp("myuser", sourceIdentityProviderId="idp-id1", targetIdentityProviderId="")
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.get("myuser", identityProviderId="")
    res8: User = User(
      id = "myuser",
      primaryParty = None,
      isDeactivated = false,
      annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
      identityProviderId = ""
    )
```

#### 检查

您可以按如下方式获取用户的当前状态：```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.get(user.id)
    res9: User = User(
      id = "myuser",
      primaryParty = None,
      isDeactivated = false,
      annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
      identityProviderId = "",
      primaryPartyAuthentication = false
    )
```

您可以查询用户拥有哪些权限：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.rights.list(user.id)
    res10: UserRights = UserRights(
      actAs = Set(alice::12201ff69b1d...),
      readAs = Set(bob::12201ff69b1d...),
      executeAs = Set(),
      readAsAnyParty = false,
      executeAsAnyParty = false,
      participantAdmin = false,
      identityProviderAdmin = false
    )
```

您可以授予更多权利。返回值仅包含新授予的权限；它不包含用户已经拥有的权限，即使您尝试再次授予它们（例如本例中的读为 `alice` 权限）：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.rights.grant(id = user.id, actAs = Set(alice, bob), readAs = Set(eve), participantAdmin = true)
    res11: UserRights = UserRights(
      actAs = Set(alice::12201ff69b1d..., bob::12201ff69b1d...),
      readAs = Set(eve::12201ff69b1d..., bob::12201ff69b1d...),
      executeAs = Set(),
      readAsAnyParty = false,
      executeAsAnyParty = false,
      participantAdmin = true,
      identityProviderAdmin = false
    )
```

您可以撤销用户的权利。同样，返回的值仅包含实际删除的权限：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.rights.revoke(id = user.id, actAs = Set(bob), readAs = Set(alice), participantAdmin = true)
    res12: UserRights = UserRights(
      actAs = Set(alice::12201ff69b1d...),
      readAs = Set(bob::12201ff69b1d..., eve::12201ff69b1d...),
      executeAs = Set(),
      readAsAnyParty = false,
      executeAsAnyParty = false,
      participantAdmin = false,
      identityProviderAdmin = false
    )
```

现在您已经授予和撤销了一些权限，您可以再次获取所有用户的权限并查看它们是什么：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.rights.list(user.id)
    res13: UserRights = UserRights(
      actAs = Set(alice::12201ff69b1d...),
      readAs = Set(bob::12201ff69b1d..., eve::12201ff69b1d...),
      executeAs = Set(),
      readAsAnyParty = false,
      executeAsAnyParty = false,
      participantAdmin = false,
      identityProviderAdmin = false
    )
```此外，还可以同时获取多个用户。为此，首先创建另一个名为 `myotheruser` 的用户，然后列出用户名以 `my` 开头的所有用户：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.create(id = "myotheruser")
    res14: User = User(
      id = "myotheruser",
      primaryParty = None,
      isDeactivated = false,
      annotations = Map(),
      identityProviderId = ""
    )
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.list(filterUser = "my")
    res15: UsersPage = UsersPage(
      users = Vector(
        User(
          id = "myotheruser",
          primaryParty = None,
          isDeactivated = false,
          annotations = Map(),
          identityProviderId = ""
        ),
        User(
          id = "myuser",
          primaryParty = None,
          isDeactivated = false,
          annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
          identityProviderId = ""
        )
      ),
      nextPageToken = ""
    )
```

#### 退役

您可以通过 ID 删除用户：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.delete("myotheruser")
```

您可以通过以下方式确认它已被删除：列出它：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.list("myotheruser")
    res17: UsersPage = UsersPage(users = Vector(), nextPageToken = "")
```

如果您想阻止用户访问 Ledger API，最好停用它而不是删除它。可以重新创建已删除的用户，就好像它从未存在过一样，而已停用的用户必须显式重新激活才能再次访问 Ledger API。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.ledger_api.users.update("myuser", user => user.copy(isDeactivated = true))
    res18: User = User(
      id = "myuser",
      primaryParty = None,
      isDeactivated = true,
      annotations = Map("description" -> "This is a new description", "baz" -> "bar"),
      identityProviderId = "",
      primaryPartyAuthentication = false
    )
```

#### 配置默认参与者管理员

新的参与者节点带有一个名为 `participant_admin` 的默认参与者管理员用户，可用于引导其他用户。您可能希望在参与者启动时准备好具有不同用户 ID 的管理员用户。对于此类情况，您可以使用您选择的用户 ID 指定其他参与者管理员用户。<注意>
  如果具有指定 ID 的用户已存在，则不会创建其他用户，即使先前存在的用户不是管理员用户。
</注>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
canton.participants.myparticipant.ledger-api.user-management-service.additional-admin-user-id = "my-admin-id"
```

### 向参与者添加新的聚会

最简单的操作是向参与者添加新的参与方。为此，我们通常将其添加到参与者的拓扑管理器中，在默认情况下，它是参与者节点的一部分。如果参与者正在运行自己的拓扑管理器，则有一个简单的宏可以在给定参与者上启用该方：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
val name = "Gottlieb"
val partyId = participant1.parties.enable(name)
```

这将在参与者的拓扑管理器的命名空间中创建一个新方。

还有对应的disable宏：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
participant1.parties.disable(partyId)
```

宏本身只是使用 `topology.party_to_participant_mappings.authorize` 创建新方，但添加了一些便利，例如自动确定 `authorize` 调用的参数。

<注意>
  请注意，`participant.parties.enable`宏会将各方添加到参与者所在的同一命名空间中。只有当参与者通过拥有根或委托密钥对该命名空间具有权限时，它才有效。
</注>

### 客户控制方

各方仅与参与者节点有弱联系。它们可以分配在自己的命名空间中，然后委托给给定的参与者。为了简单和方便，参与者默认在自己的命名空间中创建新的参与方，但在某些情况下这是不希望的。

一种常见的情况是，您首先代表客户端托管聚会，但随后将聚会移交给客户端的节点。使用默认政党分配，您仍然可以控制客户端的政党。

为了避免这种情况，您需要您的客户自己创建一个新政党并向您导出政党代表团。然后可以将该方委托导入到您的拓扑状态中，这将允许您代表该方进行操作。

对于此过程，我们使用不会连接到任何同步器的参与者节点。我们不需要完整的节点，只需要拓扑管理器。首先，我们需要找出托管节点的参与者ID：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ hosting.id.toProtoPrimitive
    res1: String = "PAR::participant2::1220a4d7463bd34b2ba3704401b48ab41d8f88cdcbe512fc1ef071aad97fef106161"
```该标识符需要传达给客户端，并且可以使用`ParticipantId.tryFromProtoPrimitive`导入。然后，客户端首先创建一个新密钥（他们可以使用创建的默认密钥）：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val secret = client.keys.secret.generate_signing_key("my-party-key", SigningKeyUsage.NamespaceOnly)
    secret : SigningPublicKey = SigningPublicKey(
      id = 122097960570...,
      format = DER-encoded X.509 SubjectPublicKeyInfo,
      keySpec = EC-Curve25519,
      usage = namespace
    )
```

以及该密钥的适当根证书：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val rootCert = client.topology.namespace_delegations.propose_delegation(Namespace(secret.fingerprint), secret, CanSignAllMappings)
    rootCert : SignedTopologyTransaction[TopologyChangeOp, NamespaceDelegation] = SignedTopologyTransaction(
      TopologyTransaction(
        NamespaceDelegation(
          12205ab17db1...,
          SigningPublicKey(
            id = 12205ab17db1...,
            format = DER-encoded X.509 SubjectPublicKeyInfo,
            keySpec = EC-Curve25519,
            usage = namespace
          ),
          CanSignAllMappings
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:1b02696c3358...
      ),
      signatures = 12205ab17db1...
    )
```

需要将此根证书导出到文件中：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.canton.util.BinaryFileUtil
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ rootCert.writeToFile("rootCert.bin")
```

定义您要创建的队伍的队伍 ID：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val partyId = PartyId.tryCreate("Client", secret.fingerprint)
    partyId : PartyId = Client::12205ab17db1...
```

创建并将该方导出为参与者代表团：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val partyDelegation = client.topology.party_to_participant_mappings.propose(partyId, Seq((hostingNodeId, ParticipantPermission.Submission)))
    partyDelegation : SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          Client::12205ab17db1...,
          PositiveNumeric(1),
          Vector(HostingParticipant(PAR::participant2::1220a4d7463b..., Submission, false)),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:f001470527e5...
      ),
      signatures = 12205ab17db1...,
      proposal
    )
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ partyDelegation.writeToFile("partyDelegation.bin")
```

客户端现在与托管节点共享 `rootCert.bin` 和 `partyDelegation.bin` 文件。托管节点将它们导入到其拓扑状态中：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ hosting.topology.transactions.load_single_from_files(
    files = Seq("rootCert.bin", "partyDelegation.bin"),
    store = 同步器Id,
)
```

最后，托管节点需要发出相应的拓扑交易以启用其节点上的一方：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ hosting.topology.party_to_participant_mappings.propose(partyId, Seq((hosting.id, ParticipantPermission.Submission)))
    res10: SignedTopologyTransaction[TopologyChangeOp, PartyToParticipant] = SignedTopologyTransaction(
      TopologyTransaction(
        PartyToParticipant(
          Client::12205ab17db1...,
          PositiveNumeric(1),
          Vector(HostingParticipant(PAR::participant2::1220a4d7463b..., Submission, false)),
          None
        ),
        serial = 1,
        operation = Replace,
        hash = SHA-256:f001470527e5...
      ),
      signatures = 1220a4d7463b...,
      proposal
    )
```

### 多节点聚会

跨多个参与者托管聚会可以提高其活跃度和容错能力，因为任何托管参与者都可以根据其权限代表聚会进行操作。虽然所有托管参与者都对该方的合约拥有相同的看法，但它们也都包含在其交易中。这会产生开销，限制该功能的可扩展性。对于与许多参与者共享数据，显式披露是更合适的方法。

### 手动初始化节点

在某些情况下，节点不应自动初始化，但您应该控制初始化的每个步骤。例如，当设置中的节点无法控制自己的身份时，当您出于安全原因不想在节点上存储身份密钥时，或者当您想要设置我们自己的密钥时（例如，当密钥外部存储在密钥管理服务 - KMS 中时），可能会出现这种情况。

下面演示了如何初始化节点的基本步骤：

#### 按键初始化

以下步骤描述了如何手动生成必要的 Canton 密钥（例如，对于参与者）：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
// 创建用于定义节点身份的签名密钥。
val 命名空间键 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Namespace.identifier}",
      SigningKeyUsage.NamespaceOnly，
    ）// 创建一个签名密钥，用于向 Sequencer 验证节点。
val 序列器验证密钥 =
  节点.keys.secret.generate_signing_key(
    name = node.name + s"-${SigningKeyUsage.SequencerAuthentication.identifier}",
    SigningKeyUsage.SequencerAuthenticationOnly，
  ）

// 创建用于签署协议消息的签名密钥。
val 签名密钥 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Protocol.identifier}",
      SigningKeyUsage.ProtocolOnly，
    ）

// 创建加密密钥。
val 加密密钥 =
  node.keys.secret.generate_encryption_key(name = node.name + "-加密")
```

<Note>
  Be aware that in some particular use cases, you might want to register keys rather than generate new ones (for instance when you have pre-generated KMS keys that you want to use). Please refer to External Key Storage with a Key Management Service (KMS) for more details.
</Note>

See [Initializing node identity manually](#initializing-node-identity-manually) below for the full manual initialization procedure.

{/* COPIED_START source="docs-website:docs/replicated/canton/3.4/participant/howtos/operate/identity/manual_identity_init.rst" hash="69f33a74" */}

# Initializing node identity manually

## Manual vs automatic identity initialization

A 参与方节点 is initialized automatically by default, though it can also be initialized manually. Manual initialization is useful in the following circumstances:

1. When a 参与方节点 does not control its own identity.
2. To avoid storing the identity key on the 参与方节点 for security reasons.
3. To explicitly set the 参与方节点 keys rather than relying on keys auto-generated by the 参与方节点.

To disable the automatic initialization of a 参与方节点, add the following to the configuration:

```无主题={"主题":{"light":"github-light","dark":"github-dark"}}
canton.participants.participant1.init = {
    生成拓扑交易和密钥 = false
    身份.类型 = 手动
}
```

Start the 参与方节点 with the above configuration settings.

## Key initialization

Besides a namespace key and signing keys, a 参与方节点 also has an asymmetric encryption key used to encrypt and decrypt transactions. By default, 参与方节点s create keys automatically, but if you choose to manually set up a 参与方节点, use the following commands to generate the namespace, signing, and encryption keys:

```scala 主题={"主题":{"light":"github-light","dark":"github-dark"}}
// 创建用于定义节点身份的签名密钥。
val 命名空间键 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Namespace.identifier}",
      SigningKeyUsage.NamespaceOnly，
    ）// 创建一个签名密钥，用于向 Sequencer 验证节点。
val 序列器验证密钥 =
  节点.keys.secret.generate_signing_key(
    name = node.name + s"-${SigningKeyUsage.SequencerAuthentication.identifier}",
    SigningKeyUsage.SequencerAuthenticationOnly，
  ）

// 创建用于签署协议消息的签名密钥。
val 签名密钥 =
  节点.keys.secret
    .generate_signing_key(
      name = node.name + s"-${SigningKeyUsage.Protocol.identifier}",
      SigningKeyUsage.ProtocolOnly，
    ）

// 创建加密密钥。
val 加密密钥 =
  node.keys.secret.generate_encryption_key(name = node.name + "-加密")
```

If you use a Key Management Service (KMS) to manage Canton's keys, and you want to use a set of pre-generated keys, use the commands `register_kms_signing_key()` and `register_kms_encryption_key()` instead. Please refer to External Key Storage with a Key Management Service (KMS) for more details.

## 参与方节点 manual initialization

After the keys have been generated, or in the case of KMS, the KMS-generated keys have been registered, manually initialize a 参与方节点 as follows:

```scala 主题={"主题":{"light":"github-light","dark":"github-dark"}}
// 使用该密钥的指纹作为节点身份。
val 命名空间 = 命名空间(namespaceKey.id)
节点.topology.init_id_from_uid(
  UniqueIdentifier.tryCreate("手动-" + node.name, 命名空间)
）

// 等待节点准备好接收节点身份。
node.health.wait_for_ready_for_node_topology()

// 创建自签名根证书。
node.topology.namespace_delegations.propose_delegation(
  命名空间，
  命名空间键，
  可以签署所有映射，
）

// 将新键分配给该节点。
节点.topology.owner_to_key_mappings.propose(
  成员=节点.id.成员，
  键= NonEmpty（Seq，sequencerAuthKey，signingKey，加密密钥），
  signedBy = Seq（namespaceKey.fingerprint，sequencerAuthKey.fingerprint，signingKey.fingerprint），
）
```

Wait for the 参与方节点 to initialize:

```scala 主题={"主题":{"light":"github-light","dark":"github-dark"}}
node.health.wait_for_initialized()
````

最后，您可以开始使用新的参与者节点。

{/* 已复制_END */}

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
