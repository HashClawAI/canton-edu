---
title: "Manage Daml Packages and Archives"
slug: "global-synchronizer-production-operations-manage-packages"
locale: "en"
category: "global-synchronizer"
source_url: "https://docs.canton.network/global-synchronizer/production-operations/manage-packages.md"
source_title: "Manage Daml Packages and Archives"
tags:
  - global-synchronizer
  - production-operations
  - manage-packages
---

# Manage Daml Packages and Archives

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.canton.network/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Daml Packages and Archives

> Upload, vet, and unvet Daml packages on a participant node.

# Manage Daml packages and archives

## About

A package is a unit of compiled Daml code corresponding to one Daml project. This package contains compiled Daml-LF code. Every package has a unique `package-id`. A Daml Archive (DAR) file consists of a main package along with all other packages on which the main package depends. As the DAR only has one main package the main `package-id` can also be used to refer to the DAR. App providers distribute apps as a collection of DARs.

## Manage DARs

### Upload a DAR

To upload a DAR use the dars.upload console command.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.upload("dars/CantonExamples.dar", vetAllPackages = false)
    res1: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

All Participant Nodes running the app must have the app DARs loaded independently as they aren't shared.

### List DARs

To list DARs use the dars.list console command.

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
  Please note that the package **canton-builtin-admin-workflow-ping** is a package that ships with Canton. It contains the Daml templates used by the `participant.health.ping` command.
</Note>

To filter the list of package provide a criteria to the `list` method. For example, to extract the description of the DAR named **CantonExamples**, first filter by name and then use `head` to extract the first element of the list:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val cantonExampleDar = participant2.dars.list(filterName = "CantonExamples").head
    cantonExampleDar : DarDescription = DarDescription(
      mainPackageId = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4",
      name = "CantonExamples",
      version = "3.4.11",
      description = "CantonExamples"
    )
```

### Display the contents of a DAR

To display the contents of a DAR use the dars.get\_contents console command.

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

The content includes the name and version of the DAR, as well as the names and versions of the packages included in the DAR as dependencies.

<Note>
  All DAR files include packages from the Daml standard library (prefixed with **daml-**), for example **daml-prim**.
</Note>

## Manage package vetting

On command submission all Participant Nodes involved in the transaction must have the packages necessary to interpret the transaction such that they come to the same conclusion. Package vetting topology information is the way that Participant Nodes communicate to other Participant Nodes what packages they support. Uploading a DAR file to a Participant Node publishes vetting information to all connected Synchronizers making it available to other Participant Nodes. Use the `topology.vetted_packages.list` console command to list vetted packages.

To display the Synchronizer/Participant Node vetting state for a specific package filter the results as shown:

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
  \#25944: Provide pretty printed macro for filter/map operations below
</div>

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list().filter(_.item.packages.exists(_.packageId == mainPackageId)).map(r => (r.context.storeId, r.item.participantId))
    res8: Seq[(TopologyStoreId, ParticipantId)] = Vector(
      (Synchronizer(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant1::12201ff69b1d...),
      (Synchronizer(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant2::1220a4d7463b...)
    )
```

<Note>
  In the output the `store` called `Authorized` is local to the Participant Node and is not a Synchronizer store.
</Note>

If all package vetting requirements aren't satisfied by any Synchronizer, the transaction submission fails returning a `FAILED_PRECONDITION/PACKAGE_SELECTION_FAILED` error message.

### Unvet the main DAR package

To remove support for the main DAR package use the dars.vetting.disable console command.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.vetting.disable(mainPackageId)
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.list().filter(_.item.packages.exists(_.packageId == mainPackageId)).map(r => (r.context.storeId, r.item.participantId))
    res10: Seq[(TopologyStoreId, ParticipantId)] = Vector(
      (Synchronizer(id = Right(value = da::1220a82692ab...::34-0)), PAR::participant1::12201ff69b1d...)
    )
```

<Warning>
  It's not possible to unvet a package referenced by active contracts. Attempting this results in a `FAILED_PRECONDITION/TOPOLOGY_PACKAGE_ID_IN_USE` error.
</Warning>

Use dars.vetting.enable console command to re-enable the vetting of a package.

## Validate a DAR

Use DAR validation to ensure that the packages contained within the DAR are compatible with the packages already loaded and vetted on a specific synchronizer. For example it's invalid for a new template to redefine an existing template that has the same package, module, and template names. Because this endpoint validates the DAR for compatibility with the current vetting state, a synchronizer must be connected to the participant.

By default DARs are validated on upload. To independently validate a DAR use the dars.validate console command.

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant2.dars.validate("dars/CantonExamples.dar")
    res11: String = "5b5d7354ae8940d21e6a558905ea9710f94e8668fa5243a15a2ae6a4865e80a4"
```

<Note>
  Validating a DAR file doesn't change the Participant Node, no information is persisted.
</Note>

## Get package information

### List packages

To directly list packages, use:

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

Filter the list by passing a criteria to the `list` method. For example, to extract the description of the package named **daml-prim**, first filter by name and then use `head` to extract the first element of the list:

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

### Display the contents of a package

To inspect packages use the packages.get\_contents console command.

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

### Find DARs that reference a package

To find DARs that reference a package use the packages.get\_references console command.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

## Remove packages and DARs

<div className="danger">
  Removing packages can lead to a number of issues, including:

  * Inability to use a contract originally created against the package, even if used in an upgraded context.
  * Inability perform Ledger API reporting on archived contracts in verbose mode. This is because the package is still needed to report historical contract events.

  **For this reason, you should not remove packages or DARs in production environments unless you are sure the package was never used or that all references to the package are pruned.**
</div>

### Remove a DAR

DAR removal only removes the main package associated with the DAR, not other packages.

You can remove a DAR only when:

* There are no active contracts referencing the package.
* There are no other packages that depend on the DAR package.
* The main package of the DAR is unvetted.

To remove the DAR package

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

Remove the DAR using the dars.remove console command:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.dars.remove(mainPackageId)
```

DAR removal only removes the main package associated with the DAR, not other packages.

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

To remove individual packages that where bundled with the DAR see the instructions below.

This line shows non **daml-** prefixed packages that aren't referenced by any other package, and so are candidates for removal:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.list().filter(!_.name.startsWith("daml-")).filter(p => participant1.packages.get_references(p.packageId).isEmpty)
    res21: Seq[PackageDescription] = Vector()
```

#### Force the removal of a package

<div className="danger">
  Force removing of a package is a dangerous operation. For this reason do not force remove packages in production environments unless you are sure the package is unused and that all references to the package are pruned.
</div>

Canton also supports removing individual packages, giving the user more fine-grained control over the system. To remove packages ensure the following conditions are true:

* The package is unused. This means that there shouldn't be an active contract corresponding to the package.
* The package is unvetted. This means there shouldn't be an active vetting transaction corresponding to the package.
* The package is not required for Participant administration (for example, the package containing the **Ping** template)

Attempting to remove a package that is required results in an `FAILED_PRECONDITION/PACKAGE_OR_DAR_REMOVAL_ERROR` error:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ val mySynchronizer = bootstrap.synchronizer(synchronizerName = "mysynchronizer", sequencers = Seq(sequencer1), mediators = Seq(mediator1), synchronizerOwners = Seq(sequencer1, mediator1), synchronizerThreshold = PositiveInt.one, staticSynchronizerParameters = StaticSynchronizerParameters.defaultsWithoutKMS(ProtocolVersion.latest))
    mySynchronizer : PhysicalSynchronizerId = mysynchronizer::1220a82692ab...::34-0
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.synchronizers.connect_local(sequencer1, "mysynchronizer")
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
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

First unvet the package:

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ import com.digitalasset.daml.lf.data.Ref.IdString.PackageId
```

```none theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.topology.vetted_packages.propose_delta(participant1.id, store = mySynchronizer, removes = Seq(PackageId.assertFromString(mainPackageId)))
```

Then force remove the package:

```scala theme={"theme":{"light":"github-light","dark":"github-dark"}}
@ participant1.packages.remove(mainPackageId, force = true)
```

---

> Mirrored from Canton Network official documentation (CC-BY-4.0) by CC Privacy Club for learning purposes.
