---
title: "Deployment"
linkTitle: "Deployment"
weight: 20
icon: fas fa-truck
description: SW360 Deployment Guides
---

## Recommended SW360 Deployment (Version 20.x)

The recommended method for deploying the modern SW360 version 20 stack is using containers (compatible with both Docker and Podman). This containerized setup provides the complete ecosystem including the new Next.js frontend, Keycloak authentication, CouchDB, and the Spring Boot backend out-of-the-box.

👉 **[Start Here: SW360 v20.x Container Deployment Guide](./Containers/)**

*If you are looking for bare metal or legacy deployments, please consult the guides available in the sidebar.*

## General Topics

* [System Requirements](./Deploy-Requirements.md)
* [Configuration Files](./Deploy-Configuration-Files.md)
* [Authorization Concept](./Deploy-Authorization-Concept.md)
* [Keycloak Authentication](./Deploy-Keycloak-Authentication.md)
* [Security Best Practices](./Deploy-Secure-Deployment.md)

## Operations & Maintenance

* [Data Backup Strategy](./Deploy-Data-Backup.md)
* [Export and Import](./Deploy-Export-and-Import.md)
* [CVE Search](./Deploy-CVE-search.md)
* [Upgrading SW360](./Upgrading/)

---

## Special Topics

After installing and setting up SW360, these are additional topics to be considered:

* [Special Deployment Guides](./Deploy-SpecialDeployment.md)
