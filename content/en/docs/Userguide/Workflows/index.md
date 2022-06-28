---
title: "Workflows"
linkTitle: "Workflows"
weight: 20
oem_ignore: true
description: "SW360 User Workflows"
---

This page is one of the basic user workflow documentation pages. It can give orientation how the sw360 can be used - as guidance or orientation. There is no particular need to follow these workflows, it is just one way. Workflows are shown as flow charts.

### Create Component and Release

So, the user would like to create an entry for zlib-1.2.8 for example in sw360. The main thing to know (see page basic concepts)is that sw360 separates releases from components: the release is the zlib-1.2.8 but the component is the zlib. By this approach, components as a kind of container type in sw360, holding several releases.

Therefore, for a new component the user needs to create a component entry first, and then add a release to it. Just adding a release will not work. If a component with a different release already exists, the users add a release to the existing component.

The intended roles for this can be a developer that would like to start caring for an OSS component or release. In addition a project owner / project owner can care for the components and releases part of the product or process.

{{< figure src="/img/workflow/worklfow-adding-component-and-release-to-a-project.png">}}

### Create a Project

A project is a structure to keep track on releases inside project, as well as other projects. Please note that a project can be also a product, depending on the type of business. the use of the term 'project' is used also for subsuming the term 'product'.

As for the integration case with the OSS software FOSSology, the project view allows for an overview, which of the used components have been analyzed with FOSSology already.

In the diagram, the "clearing process" is mentioned, because the clearing process affects the software components of a project. The main approach is the following:

* A project responsible sets up a project with used releases.
* For the releases that were not analyzed before, the project responsible requests a clearing - source files can be transferred to FOSSology.
* Once analyses for all releases are complete, the "clearing process" is finished for this project.

A project it self does not need much information, it is just about the name and the version. Note that some of the information is like to be set at that time:

* Visibility level
* Project contacts
* Important Dates for the project

{{< figure src="/img/workflow/workflow-add-project.png">}}

### Moderation

The moderation is the basic way of applying changes if the document is not created by someone else. In sw360 the following person can edit documents right away (without moderation request):

* The creator of a document (document is a project entry, a release entry etc)
* Admins
* Clearing admins
* Moderators of this document
* Other special roles, such as project responsible 

Please see the page [about the Role Authorization Model]({{< ref "../../Development/Dev-Role-Authorisation-Model.md" >}} "Dev Role" ) for more information.

If the user who wishes to change a document and is not one of these, the moderator workflow kicks in. Then changes applied to the document are not really applied, but are sent to a moderator. Moderators are:

* The creator of a document (document is a project entry, a release entry etc)
* Admins
* Clearing admins
* Moderators of this document

The moderator can review, approve or decline the request. Then, the requesting user can delete the request. The moderator request workflow is shown below.

{{< figure src="/img/workflow/workflow-moderation.png">}}
