---
linkTitle: "System Requirements"
title: "System Requirements"
weight: 20
description: 
  SW360 minimal system requirements based on system class
---

For deploying SW360 v20, the following hardware and software requirements apply.
Note that the architecture has shifted from a monolithic Liferay setup to a
microservices-based stack (Spring Boot Backend, Next.js Frontend, Keycloak
Authentication).

Recommended deployment method is [container-based](./Containers/_index.md) for
ease of management.

## Hardware and Infrastructure

### Development / Test instances

For personal development or small test instances with minimal data:

* **CPU**: 2 cores
* **RAM**: 8GB (4GB for Tomcat/Backend, 1GB for Keycloak, 1GB for Frontend,
  2GB for OS/CouchDB)
* **Storage**: 40GB SSD
* **Network**: 10Mbit Ethernet link

### Staging instances

Testing and working with medium data sets for staging and pre-productive
testing. Requires enough RAM to run a full stack including Keycloak and
monitoring services.

* **CPU**: 4 cores
* **RAM**: 16GB
* **Storage**: 100GB SSD
* **Network**: 100Mbit Ethernet link

### Productive instances

For a production environment with e.g. 8K+ projects and 2K+ users, it is
recommended to split the database and the application server.

#### Application Server (SW360 + Keycloak + Frontend)
* **CPU**: 8+ cores
* **RAM**: 16GB - 24GB (At least **8GB** must be allocated to the SW360
  Backend/Tomcat)
* **Storage**: 500GB SSD
* **Network**: 1GBit Ethernet link

#### Database Server (CouchDB + Postgres)
> [!IMPORTANT]
> For production, it is highly recommended to run **CouchDB on a separate
> machine** rather than inside a container on the same host.

* **CPU**: 4 cores
* **RAM**: 15GB+ (CouchDB requires significant memory for indexing large
  datasets)
* **Storage**: 500GB SSD (Database grade)
* **Network**: 1GBit Ethernet link

### Network

The following table gives an overview of the required inbound ports:

| Port | Service | Description |
| :--- | :--- | :--- |
| `443` | HTTPS (Nginx Proxy) | Main access to the SW360 Frontend and Keycloak |
| `3000` | SW360 Frontend | Internal: The Next.js application |
| `8080` | SW360 Backend | Internal: The Spring Boot Resource Server |
| `8443` | Keycloak | Authentication service |
| `5984` | CouchDB | Direct access to database (if required for admin) |
| `5432` | Postgres | Database for Keycloak |
| `22` | SSH | Remote administration |

Overview of required outbound ports:

| Port | Service | Description |
| :--- | :--- | :--- |
| `443` | HTTPS | External service consumption (e.g., Vulnerability pulling, Fossology) |
| `53` | DNS | Domain Name System |
| `123` | NTP | Time synchronization |

## Software

SW360 v20 is built on a modern Java and Node.js stack. The recommended platforms
for deployment are:

### Operating System
* **Ubuntu 24.04 LTS (or later)**: Highly recommended for production
  (includes commercial ESM support).
* **Debian 12 (or later)**: Lightweight and stable, ideal for general
  deployments.

### Runtime Stack
* **Java**: OpenJDK **21**
* **Tomcat**: Tomcat **11**
* **Node.js**: **20+** (LTS versions 20, 22, and 24 are tested)
* **Keycloak**: Version **26+**

### Persistence & Search
* **CouchDB**: Version **3.5**
* **CouchDB Nouveau**: **Mandatory**. Nouveau must be installed and enabled for
  search functionality to work.
* **Postgres**: Version **15+** (Required for Keycloak authentication storage)

More information can be found in the
[Release Notes](https://github.com/eclipse-sw360/sw360/releases).
