---
title: "About Eclipse SW360"
linkTitle: About
menu:
    main:
        weight: 10

---

# About

In most cases, software today is not built from scratch, but rather assembled from various prepackaged third-party software components. As a result, organizations face the following challenges:

* Verifying various aspects of compliance when using third-party software components: license compliance, ECC checks, IP assessments, etc.
* Sharing knowledge about software components and their qualities. For example, which software components should be recommended, which should be phased out based on which criteria?
* Providing a broad overview of the components used: An organization and its supply chain management must have information about which assets are integrated into which products or solutions.

These three main use cases target different roles in an organization: quality managers, software developers, legal counsels, software architects, R&D managers etc. However, all these use cases share a common need for a central hub that manages insights into software components.

SW360 is an open source software project licensed under the EPL-1.0 that provides both a web application and a repository to collect, organize and make available information about software components. It establishes a central hub for software components in an organization. SW360 allows for

* tracking components used by a project/product,
* assessing security vulnerabilities,
* maintaining license obligations,
* enforcing policies, and
* generating legal documents.

For example, SW360 can trigger a clearing process in the open source compliance tool FOSSology and import the resulting clearing reporting. Data is either stored in SW360’s database or on the fly imported from external sources. In future we plan to have federations of SW360 instances that share selected information. Besides its web-based UI, all functionality of SW360 is available through an API that allows an integration into existing devops tools.

### Further Information

You can find more detailed information on the project [wiki](https://github.com/eclipse/sw360/wiki).
