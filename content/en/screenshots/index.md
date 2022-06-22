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

The SW360 application is divided into several sections around managing a catalogue of software components and the software bill-of-material of your software projects, products or services. The menu bar as shown on home screen cover the following main sections.

<br>

## Home

A dashboard listing the components and projects created by the user logged in. With this overview, the own projects and components can be directly accessed.

{{< gallery/gallery >}} 

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-home.png" title="Home" >}}
  
  {{< /gallery/card >}}

{{< /gallery/gallery >}}


## Project

As for individual projects, a number of subsections is provided, allowing for managing different aspects of a project: license compliance, export control (ECC), vulnerabilities, locking of attachments for project use, and vulnerabilities.
For each project, a number of attributes can be maintained, most notably external ids, which allow for a mapping to the dataset in SW360 with external systems.

The main area of work in the projects section. SW360 uses the term project as synonym for products, services, or internal projects. The projects area starts with a listing of all projects which are visible to the user, according to the visibility setting of the project.

For the license compliance, SW360 allows for maintaining a global clearing status for each release of a component. In addition, a clearing status can be set for use at each individual project.

Not only the clearing status for each use of a release can be captured by SW360. Also, the type of usage (contained, side-by-side installation, etc.) can be saved as attribute.

{{< gallery/gallery >}} 

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-projectlist.png" title="Main area" >}}
  {{< /gallery/card >}}

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-projects01.png" title="Summary" >}}
  {{< /gallery/card >}}

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-projects02.png" title="Clearing Status" >}}
  {{< /gallery/card >}}

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-projects03.png" title="ECC Clearing Status" >}}
  {{< /gallery/card >}}

{{< gallery/card src="../img/sw360screenshots/sw360screenshot-projects04.png" title="Releases and Projects" >}}
  {{< /gallery/card >}}
{{< /gallery/gallery >}}

## Components

Components in SW360 can have multiple types, such as OSS, commercial component or a service (and more types), since license compliance matters for type of software, not only OSS. Components are in fact a container for releases, because license compliance information and other attributes change between different releases of a component.

At each release, basic attributes can be stored, some of them are informal, but can give relevant input to usage statistics of software in an organisation.

{{< gallery/gallery >}} 

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-components02.png" title="Component" >}}
  {{< /gallery/card >}}

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-components01.png" title="Component Edit" >}}
  {{< /gallery/card >}}

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-components04.png" title="Component Clearance" >}}
  {{< /gallery/card >}}

{{< /gallery/gallery >}}


## Search

SW360 provides an index for all data, thus searching for keywords will yield results for all different datasets, such as projects, components, licenses, etc. Search for terms can be filtered by data set types.

{{< gallery/gallery >}} 

  {{< gallery/card src="../img/sw360screenshots/sw360screenshot-search.png" title="Search" >}}
  {{< /gallery/card >}}

{{< /gallery/gallery >}}

</div>

