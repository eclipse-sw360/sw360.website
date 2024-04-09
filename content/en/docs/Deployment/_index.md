---
title: "Deployment"
linkTitle: "Deployment"
weight: 20
icon: fas fa-truck
description: SW360 Deployment Guides
---

## Recommended SW360 Deployment

For current SW360 deployment is recommended use docker compose, as base setup of the necessary third party tools are present.

You can find [SW360 official docker-compose reference here](https://github.com/eclipse-sw360/sw360/raw/main/docker-compose.yml).

This docker compose comes with default admin passwords for couchdb and postgres. Is recommended for production to customize this file.

Donload the file mentioned above an just run:

```bash
docker compose -d
```

Three nested docker containers will be created for sw360, couchdb and postgres, and the respective volumes for the containers. They run in a closed sw360 docker network.

After this, you need to execute the [18.x.x. series initial setup](deploy-initial-setup18)

### General Topics

* [Deployment Authorization Concept](deploy-authorization-concept)
* [Properties explained](deploy-configuration-files)
* [Deployment Requirements](deploy-requirements)
* [Secure Deployment Notes](deploy-secure-deployment)

### Special Topics

After install and setup sw360, this are possible topice to be considered:

* [Special Coverage of Country Codes](deploy-configuration-country-codes), when countries are displayed, then it uses country codes in the DB 
* [How to export data and import it to a new instance](deploy-export-and-import)
