---
title: "Screenshots"
description: "A picture is worth a thousand words"
menu:
  main:
    weight: 11
---


{{< blocks/cover image_anchor="top" height="sm" color="primary" >}}
{{< page/header >}}
{{< /blocks/cover >}}

<div class="container l-container--padded">


<div class="row">
<div class="col-12 col-lg-8">

The SW360 application is divided into several sections around managing a catalogue of software components and the software bill-of-material of your software projects, products or services. The menu bar as shown on home screen cover the following main sections.

### Home

A dashboard listing the components and projects created by the user logged in. With this overview, the own projects and components can be directly accessed.

{{< figure src="../img/sw360screenshots/sw360screenshot-home.png" width="700" height="440">}}

<br/><br/>

### Projects

The main area of work in the projects section. SW360 uses the term project as synonym for products, services, or internal projects. The projects area starts with a listing of all projects which are visible to the user, according to the visibility setting of the project.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-projectlist.png" width="700" height="440">}}

<br/>

As for individual projects, a number of subsections is provided, allowing for managing different aspects of a project: license compliance, export control (ECC), vulnerabilities, locking of attachments for project use, and vulnerabilities.

For each project, a number of attributes can be maintained, most notably external ids, which allow for a mapping to the dataset in SW360 with external systems.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-projects01.png" width="700" height="440">}}

<br/>

For the license compliance, SW360 allows for maintaining a global clearing status for each release of a component. In addition, a clearing status can be set for use at each individual project.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-projects02.png" width="700" height="440">}}

<br/>

Not only the clearing status for each use of a release can be captured by SW360. Also, the type of usage (contained, side-by-side installation, etc.) can be saved as attribute.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-projects04.png" width="700" height="440">}}

<br/><br/>

### Components

Components in SW360 can have multiple types, such as OSS, commercial component or a service (and more types), since license compliance matters for type of software, not only OSS. Components are in fact a container for releases, because license compliance information and other attributes change between different releases of a component.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-components02.png" width="700" height="440">}}

<br/>

At each release, basic attributes can be stored, some of them are informal, but can give relevant input to usage statistics of software in an organisation.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-components01.png" width="700" height="440">}}

<br/>

Of course, when if comes to license clearing, more relevant attributes can be found.

<br/>


{{< figure src="../img/sw360screenshots/sw360screenshot-components04.png" width="700" height="440">}}

<br/><br/>


### Special: Export Control and Customs

Once the software bill-of-material has been setup, not only license compliance per component can be checked. But also the export control and customs (ECC) relevant information can be assessed for each project.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-projects03.png" width="700" height="440">}}

<br/>

ECC classifications can be set for each release of a component - SW360 supports a specific role for ECC experts who are the only users which can modify ECC data. Other users can enter ECC data which requires approval by ECC experts with the particular role.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-components03.png" width="700" height="440">}}

<br/><br/>

### Search

SW360 provides an index for all data, thus searching for keywords will yield results for all different datasets, such as projects, components, licenses, etc. Search for terms can be filtered by data set types.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-search.png" width="700" height="440">}}

<br/><br/>

### Preferences

<br/>

The preferences section of SW360 shows the basic user information. In addition, this is the area where users can generate access tokens for the REST API. Access tokens can be configured to have a limited validity or set for only allowing for read access. Once issued access tokens cannot be shown anymore because SW360 stores only a hash. Thus deletion of access tokens requires a designating name for each token.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-preferences01.png" width="700" height="440">}}

<br/>

Moreover, in the preferences section, each user can define own notification settings - depending on the user's needs.

<br/>

{{< figure src="../img/sw360screenshots/sw360screenshot-preferences02.png" width="700" height="440">}}

</div>

</div>
</div>
