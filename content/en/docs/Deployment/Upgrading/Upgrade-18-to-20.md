---
linkTitle: "Upgrade v18 to v20"
title: "Upgrading from Version 18 to Version 20"
weight: 10
description: A comprehensive guide on migrating data and upgrading SW360 from version 18.x to 20.x.
---

## Overview and Major Architectural Changes

Upgrading from SW360 Version 18 to Version 20 introduces several major
architectural shifts. Please read the following notices carefully before
beginning the upgrade process:

> [!WARNING]
> **New Frontend Architecture:** The legacy Liferay UI has been unequivocally
> removed. SW360 v20 is entirely powered by a modern React/Next.js frontend.
> 
> **Search & Indexing Engine Changes:** The search engine has been heavily
> redesigned to support full-text search. You **must** upgrade CouchDB to
> version >= 3.5 **and** install the new `couchdb-nouveau` package alongside it.
> 
> **Index Rebuilding Expected Downtime:** Because of the completely restructured
> CouchDB indexes, the database will take considerable time to rebuild its
> search trees the first time it starts. Please plan this upgrade during an
> acceptable **downtime window** corresponding to your database size.

---

## Upgrade Procedure

Unlike prior versions, SW360 v20 cleanly separates out the application
layers. You do not need to perform an in-place reinstallation over your old
Liferay setup. Instead, you will prepare your database, run the sequential
migration scripts, and then deploy the v20 application stack fresh using either
containers or bare metal.

### Step 1: Stop Services and Prepare Backup
1. **Stop SW360:** Gracefully shut down your existing SW360 v18 application
   servers (Tomcat).
2. **Stop CouchDB:** Halt the CouchDB background service safely so no state
   changes can occur mid-backup.
3. **CRITICAL:** Take a complete backup of your CouchDB database (e.g., copying
   your `/opt/couchdb/data/*.couch` files natively or replicating). Should a
   migration script fail, you will need this snapshot to restore cleanly.

### Step 2: Upgrade the Database Layer
1. Upgrade your CouchDB installation on the host to **version 3.5.x or higher**.
2. Ensure you have the **`couchdb-nouveau`** module installed and running to
   support the new search indexing parameters. *(Note: If you are upgrading your
   deployment directly to the new Docker Container stack, both components
   natively ship combined in the default Compose file).*
3. Start the upgraded CouchDB and `couchdb-nouveau` services.

### Step 3: Execute Consecutive Migration Scripts

SW360 provides a suite of Python migration scripts explicitly parameterized to
securely mutate your v18 data structures into the modern v20 schema formats.

You **must** execute the migration scripts sequentially to bridge the gap
between v18 and v20 correctly. Retrieve the scripts directly from the core
SW360 repository:

**[SW360 Migration Scripts Directory](https://github.com/eclipse-sw360/sw360/tree/main/scripts/migrations)**

Please comprehensively consult the `README.md` within that directory to
determine exactly which scripts correlate to the incremental version jumps
(e.g., migrating v17 -> v18 -> v20) and run them in chronological order against
your running CouchDB instance.

### Step 4: Deploy the Version 20 Application

Once the database migration sequentially modifies the CouchDB records spanning
across the v20 schema, you are fully ready to boot up the newly structured
application layer.

Choose your preferred deployment framework definitively from our official guides
and follow the instructions to spin up the backend, Keycloak, and Next.js
frontend, connecting them directly against your successfully upgraded CouchDB
database:

*   👉 **[Recommended: Container Deployment (Docker / Podman)](../../containers/deploy-20-containers/)**
*   👉 **[Alternative: Bare Metal Deployment](../../baremetal/deploy-20-natively/)**

Once your chosen stack is configured and initialized, the overarching upgrade
from v18 to v20 is officially complete!
