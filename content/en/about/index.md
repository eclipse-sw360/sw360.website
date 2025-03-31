---
title: "About Eclipse SW360"
linkTitle: About
menu:
    main:
        weight: 10
---

{{< blocks/cover image_anchor="top" height="sm" color="primary" >}}
{{< page/header >}}
{{< /blocks/cover >}}

<div class="container l-container--padded">

<div class="row">
<div class="col-12 col-lg-8">

In most cases, modern software is not built from scratch but is instead assembled using various prepackaged third-party software components. As a result, organizations face several challenges:

* **Verifying compliance** when using third-party software components, including license compliance, ECC checks, and IP assessments.
* **Sharing knowledge** about software components and their qualities, such as which components should be recommended and which should be phased out based on specific criteria.
* **Providing a broad overview** of the components used in an organization and its supply chain to track which assets are integrated into different products or solutions.

These three main use cases cater to different roles within an organization, including quality managers, software developers, legal counsels, software architects, and R&D managers. However, all these roles share a common need for a centralized hub that manages insights into software components.

**SW360** is an open-source software project licensed under EPL-2.0 that provides both a web application and a repository for collecting, organizing, and making software component information available. It serves as a central hub for managing software components within an organization. SW360 enables:

* Tracking components used in a project or product.
* Assessing security vulnerabilities.
* Maintaining license obligations.
* Enforcing policies.
* Generating legal documents.

For instance, SW360 can trigger a clearing process in the open-source compliance tool **FOSSology** and import the resulting
clearing reports. Data can either be stored in SW360’s database or imported dynamically from external sources.

In the future, we plan to establish federations of SW360 instances that share selected information.

In addition to its web-based UI, all functionalities of SW360 are accessible via an API, allowing seamless integration into existing DevOps tools.

</div>
</div>
</div>
