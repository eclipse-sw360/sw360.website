---
title: "Data Backup Strategy"
linkTitle: "Data Backup"
weight: 30
description: "Guidelines for backing up and restoring SW360 data across container and bare metal deployments."
---

## Introduction

*(Placeholder: Explain the importance of regular backups for SW360 environments.)*

## Container Deployments

### Backing Up Docker Volumes

*(Placeholder: Instructions on tar-balling the `couchdb` and `postgres_storage` volumes.)*

### Restoring Docker Volumes

*(Placeholder: Instructions on restoring data to fresh Docker volumes.)*

## Bare Metal Deployments

### PostgreSQL Database (Keycloak)

*(Placeholder: Instructions for `pg_dump` and `pg_restore`.)*

### CouchDB Database

*(Placeholder: Instructions for replicating or backing up CouchDB `.couch` files.)*

## File System Backups

*(Placeholder: Instructions on backing up `/etc/sw360` and other configuration files.)*
