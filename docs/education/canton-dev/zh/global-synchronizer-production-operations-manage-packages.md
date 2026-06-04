---
title: "管理 Daml 包与归档"
slug: "global-synchronizer-production-operations-manage-packages"
locale: "zh"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/manage-packages.md"
source_title: "Manage Daml Packages and Archives"
tags:
  - global-synchronizer
  - production-operations
  - manage-packages
---

# 管理 Daml 包与归档

> 在Party节点上管理 Daml 包的上传、审查与取消审查。

> 在参与者节点上上传、审查和取消审查 Daml 包。


## 关于

包是与一个Daml项目相对应的已编译Daml代码的单元。该软件包包含已编译的 Daml-LF 代码。每个包都有一个独特的`package-id`。 Daml Archive (DAR) 文件由一个主包以及该主包所依赖的所有其他包组成。由于 DAR 只有一个主包，所以主 `package-id` 也可以用来指代 DAR。应用程序提供商将应用程序作为 DAR 的集合进行分发。

## 管理 DAR

### 上传 DAR

要上传 DAR，请使用 dars.upload 控制台命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.upload("dars/CantonExamples.dar", vetAllPackages = false)
    res1: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

运行应用程序的所有参与者节点必须独立加载应用程序 DAR，因为它们不共享。

### 列出 DAR

要列出 DAR，请使用 dars.list 控制台命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.list()
    res2: Seq[DarDescription] = Vector(
      DarDescription(
        mainPackageId = "de2cc2f90eb523414ff54e899951dadd8789a4c07e0f71f6d6c9eaf57d412a54",
        name = "canton-builtin-admin-workflow-ping",
        version = "3.4.0",
        description = "System package"
      ),
      DarDescription(
        mainPackageId = "dfaf1018ecbbc8a1be517858d24a93aa5d88b8401292ebae090df8a505973d4e",
        name = "CantonExamples",
        version = "1.0.0",
        description = "CantonExamples"
      )
    )
```

<Note>
  请注意，**canton-builtin-admin-workflow-ping** 软件包是 Canton 附带的软件包。它包含`participant.health.ping`命令使用的Daml模板。
</Note>

要过滤包列表，请为 `list` 方法提供条件。例如，要提取名为 **CantonExamples** 的 DAR 的描述，首先按名称过滤，然后使用 `head` 提取列表的第一个元素：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val cantonExampleDar = participant2.dars.list(filterName = "CantonExamples").head
    cantonExampleDar : DarDescription = DarDescription(
      mainPackageId = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4",
      name = "CantonExamples",
      version = "3.4.11",
      description = "CantonExamples"
    )
```

### 显示 DAR 的内容

要显示 DAR 的内容，请使用 dars.get\_contents 控制台命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val darContent = participant2.dars.get_contents(cantonExampleDar.mainPackageId)
    darContent : DarContents = DarContents(
      main = 5b5d7354ae89...,
      name = CantonExamples,
      version = 3.4.11,
      description = CantonExamples,
      packages = Seq(
        fcee8dfc1b81...,
        fa79192fe1cc...,
    ..
```

内容包括 DAR 的名称和版本，以及 DAR 中作为依赖项包含的包的名称和版本。<Note>
  所有 DAR 文件都包含来自 Daml 标准库的包（前缀为 **daml-**），例如 **daml-prim**。
</Note>

## 管理包审查

在提交命令时，参与事务的所有参与者节点必须具有解释事务所需的包，以便它们得出相同的结论。包审查拓扑信息是参与者节点向其他参与者节点传达它们支持的包的方式。将 DAR 文件上传到参与者节点会将审核信息发布到所有连接的同步器，使其可供其他参与者节点使用。使用 `拓扑.vetted_packages.list` 控制台命令列出经过审查的软件包。

要显示特定包过滤器的同步器/参与者节点审查状态，结果如下所示：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.upload("dars/CantonExamples.dar")
    res5: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.upload("dars/CantonExamples.dar")
    res6: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mainPackageId = participant2.dars.list(filterName = "CantonExamples").head.mainPackageId
    mainPackageId : String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

<div className="todo">
  \#25944：为下面的过滤/映射操作提供漂亮的打印宏
</div>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.vetted_packages.list().filter(_.item.packages.exists(_.packageId == mainPackageId)).map(r => (r.context.storeId, r.item.participantId))
    res8: Seq[(拓扑StoreId, ParticipantId)] = Vector(
      (同步器(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant1::12201ff69b1d...),
      (同步器(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant2::1220a4d7463b...)
    )
```

<Note>
  在输出中，称为 `Authorized` 的 `store` 是参与者节点本地的，并且不是同步器存储。
</Note>

如果任何 同步器 都不能满足所有包审查要求，则事务提交将失败，并返回 `FAILED_PRECONDITION/PACKAGE_SELECTION_FAILED` 错误消息。

### 取消主 DAR 包的审查

要删除对主 DAR 包的支持，请使用 dars.vetting.disable 控制台命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.vetting.disable(mainPackageId)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.vetted_packages.list().filter(_.item.packages.exists(_.packageId == mainPackageId)).map(r => (r.context.storeId, r.item.participantId))
    res10: Seq[(拓扑StoreId, ParticipantId)] = Vector(
      (同步器(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant1::12201ff69b1d...)
    )
```<Warning>
  无法取消对活动合约引用的包的审查。尝试此操作会导致 `FAILED_PRECONDITION/TOPOLOGY_PACKAGE_ID_IN_USE` 错误。
</Warning>

使用 dars.vetting.enable 控制台命令重新启用软件包的审查。

## 验证 DAR

使用 DAR 验证来确保 DAR 中包含的包与已在特定同步器上加载和审查的包兼容。例如，新模板重新定义具有相同包、模块和模板名称的现有模板是无效的。由于此端点验证 DAR 与当前审核状态的兼容性，因此必须将同步器连接到参与者。

默认情况下，DAR 在上传时进行验证。要独立验证 DAR，请使用 dars.validate 控制台命令。

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.validate("dars/CantonExamples.dar")
    res11: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

<Note>
  验证 DAR 文件不会更改参与者节点，也不会保留任何信息。
</Note>

## 获取包信息

### 列出包

要直接列出包，请使用：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.packages.list()
    res12: Seq[PackageDescription] = Vector(
      PackageDescription(
        packageId = 9e70a8b3510d...,
        name = ghc-stdlib-DA-Internal-Template,
        version = 1.0.0,
        uploadedAt = 2026-05-06T10:08:38.719745Z,
        size = 114
      ),
    ..
```

通过将条件传递给 `list` 方法来过滤列表。例如，要提取名为 **daml-prim** 的包的描述，首先按名称过滤，然后使用 `head` 提取列表的第一个元素：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val prim = participant2.packages.list(filterName = "daml-prim").head
    prim : PackageDescription = PackageDescription(
      packageId = 0e4a572ab1fb...,
      name = daml-prim-DA-Internal-Erased,
      version = 1.0.0,
      uploadedAt = 2026-05-06T10:08:38.719745Z,
      size = 98
    )
```

### 显示包的内容

要检查包，请使用packages.get\_contents 控制台命令。

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.packages.get_contents(prim.packageId)
    res14: PackageDescription.PackageContents = PackageContents(
      description = PackageDescription(
        packageId = 0e4a572ab1fb...,
        name = daml-prim-DA-Internal-Erased,
        version = 1.0.0,
        uploadedAt = 2026-05-06T10:08:38.719745Z,
        size = 98
      ),
    ..
```

### 查找引用包的 DAR

要查找引用包的 DAR，请使用packages.get\_references 控制台命令。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.packages.get_references(prim.packageId)
    res15: Seq[DarDescription] = Vector(
      DarDescription(
        mainPackageId = "de2cc2f90eb523414ff54e899951dadd8789a4c07e0f71f6d6c9eaf57d412a54",
        name = "canton-builtin-admin-workflow-ping",
        version = "3.4.0",
        description = "System package"
      ),
      DarDescription(
    ..
```

## 删除包和 DAR

<div className="危险">
  删除软件包可能会导致许多问题，包括：

  * 无法使用最初针对包创建的合约，即使在升级的上下文中使用也是如此。
  * 无法以详细模式对存档合约执行 Ledger API 报告。这是因为仍然需要该包来报告历史合约事件。

  **因此，您不应在生产环境中删除包或 DAR，除非您确定该包从未使用过或者对该包的所有引用均已删除。**
</div>

### 删除 DAR

DAR 删除仅删除与 DAR 关联的主包，而不删除其他包。

仅在以下情况下才可以删除 DAR：

* 没有引用该包的有效合同。
* 没有其他依赖于 DAR 包的包。
* DAR 的主包未经审查。

删除 DAR 包

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val packagesBefore = participant1.packages.list().map(_.packageId).toSet
    packagesBefore : Set[String] = HashSet(
      "99ea07e101ed25cdb8584e072278d8df62e10d72c172bfe1621ba0a51cee61ce",
      "590736e6f7bc01492007ecb27f3fe75995c19fbd3d41b384aada69619fd4f76c",
      "b70db8369e1c461d5c70f1c86f526a29e9776c655e6ffc2560f95b05ccb8b946",
      "f181cd661f7af3a60bdaae4b0285a2a67beb55d6910fc8431dbae21a5825ec0f",
      "5aee9b21b8e9a4c4975b5f4c4198e6e6e8469df49e2010820e792f393db870f4",
      "0e4a572ab1fb94744abb02243a6bbed6c78fc6e3c8d3f60c655f057692a62816",
      "52a1edd01a20137169a01217421f950883b9e84d5d773e6c3866e921bfaf918e",
      "52854220dc199884704958df38befd5492d78384a032fd7558c38f00e3d778a2",
      "c280cc3ef501d237efa7b1120ca3ad2d196e089ad596b666bed59a85f3c9a074",
    ..
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mainPackageId = participant1.dars.upload("dars/CantonExamples.dar")
    mainPackageId : String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val content = participant1.dars.get_contents(mainPackageId)
    content : DarContents = DarContents(
      main = 5b5d7354ae89...,
      name = CantonExamples,
      version = 3.4.11,
      description = CantonExamples,
      packages = Seq(
        e5411f3d75f0...,
        86d888f34152...,
    ..
```

使用 dars.remove 控制台命令删除 DAR：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.remove(mainPackageId)
```

DAR 删除仅删除与 DAR 关联的主包，而不删除其他包。```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val packageIds = content.packages.map(_.packageId).toSet.intersect(participant1.packages.list().map(_.packageId).toSet)
    packageIds : Set[String] = HashSet(
      "b70db8369e1c461d5c70f1c86f526a29e9776c655e6ffc2560f95b05ccb8b946",
      "f181cd661f7af3a60bdaae4b0285a2a67beb55d6910fc8431dbae21a5825ec0f",
      "bde4bd30749e99603e5afa354706608601029e225d4983324d617825b634253a",
      "5aee9b21b8e9a4c4975b5f4c4198e6e6e8469df49e2010820e792f393db870f4",
      "0e4a572ab1fb94744abb02243a6bbed6c78fc6e3c8d3f60c655f057692a62816",
      "60c61c542207080e97e378ab447cc355ecc47534b3a3ebbff307c4fb8339bc4d",
      "52854220dc199884704958df38befd5492d78384a032fd7558c38f00e3d778a2",
      "c280cc3ef501d237efa7b1120ca3ad2d196e089ad596b666bed59a85f3c9a074",
      "e5411f3d75f072b944bd88e652112a14a3d409c491fd9a51f5f6eede6d3a3348",
    ..
```

要删除与 DAR 捆绑在一起的各个软件包，请参阅以下说明。

此行显示不被任何其他包引用的非 **daml-** 前缀包，因此是要删除的候选包：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.list().filter(!_.name.startsWith("daml-")).filter(p => participant1.packages.get_references(p.packageId).isEmpty)
    res21: Seq[PackageDescription] = Vector()
```

#### 强制删除包

<div className="危险">
  强行移除包裹是一项危险的操作。因此，不要在生产环境中强制删除包，除非您确定该包未使用并且对该包的所有引用都已删除。
</div>

Canton 还支持删除单个软件包，使用户能够对系统进行更细粒度的控制。要删除软件包，请确保满足以下条件：

* 包未使用。这意味着不应该有与该包相对应的有效合同。
* 包裹未经审查。这意味着不应该有与该包相对应的活动审核交易。
* 参与者管理不需要该包（例如，包含 **Ping** 模板的包）

尝试删除所需的包会导致 `FAILED_PRECONDITION/PACKAGE_OR_DAR_REMOVAL_ERROR` 错误：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val my同步器 = bootstrap.同步器(同步器Name = "my同步器", sequencers = Seq(sequencer1), mediators = Seq(mediator1), 同步器Owners = Seq(sequencer1, mediator1), 同步器Threshold = PositiveInt.one, static同步器Parameters = Static同步器Parameters.defaultsWithoutKMS(ProtocolVersion.latest))
    my同步器 : PhysicalsynchronizerId = my同步器::1220a82692ab...::34-0
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, "my同步器")
``````none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mainPackageId = participant1.dars.upload("dars/CantonExamples.dar")
    mainPackageId : String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.remove(mainPackageId)
    ERROR com.digitalasset.canton.integration.EnvironmentDefinition$$anon$3:PackageDarManagementDocumentationIntegrationTest - Request failed for participant1.
      GrpcRequestRefusedByServer: FAILED_PRECONDITION/PACKAGE_OR_DAR_REMOVAL_ERROR(9,a4d7956b): Package 5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4 is currently vetted and available to use.
      Request: RemovePackage(5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4,false)
      DecodedCantonError(
      code = 'PACKAGE_OR_DAR_REMOVAL_ERROR',
      category = InvalidGivenCurrentSystemStateOther,
      cause = "Package 5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4 is currently vetted and available to use.",
      traceId = 'a4d7956b1a5a80bddd786d01e9e3d3e4',
      context = Seq('participant=>participant1', 'test=>PackageDarManagementDocumentationIntegrationTest')
    )
      Command ParticipantAdministration$packages$.remove invoked from cmd10000011.sc:1
```

首先检查包：

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.daml.lf.data.Ref.IdString.PackageId
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.拓扑.vetted_packages.propose_delta(participant1.id, store = my同步器, removes = Seq(PackageId.assertFromString(mainPackageId)))
```

然后强制删除包：

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.remove(mainPackageId, force = true)
```

---

> 本文由 CC Privacy Club 根据 Canton Network 官方文档（CC-BY-4.0）整理翻译，仅供学习；实现细节以官方最新版本为准。
