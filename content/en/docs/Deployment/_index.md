---
title: "Deployment"
linkTitle: "Deployment"
weight: 20
icon: fas fa-truck
description: SW360 Deployment Guides
---

## Recommended SW360 Deployment (Version 20.x)

The recommended method for deploying the modern SW360 version 20 stack is using containers (compatible with both Docker and Podman). This containerized setup provides the complete ecosystem including the new Next.js frontend, Keycloak authentication, CouchDB, and the Spring Boot backend out-of-the-box.

👉 **[Start Here: SW360 v20.x Container Deployment Guide](containers/deploy-20-containers/)**

*If you are looking for bare metal or legacy deployments, please consult the guides available in the sidebar.*

## General Topics

* [Deployment Authorization Concept](deploy-authorization-concept)
* [Properties explained](deploy-configuration-files)
* [Deployment Requirements](deploy-requirements)
* [Secure Deployment Notes](deploy-secure-deployment)

## Special Topics

After install and setup sw360, this are possible topice to be considered:

* [Special Coverage of Country Codes](deploy-configuration-country-codes), when countries are displayed, then it uses country codes in the DB 
* [How to export data and import it to a new instance](deploy-export-and-import)
