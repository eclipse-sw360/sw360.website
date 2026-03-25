---
title: "Version 20.x with Containers"
linkTitle: "Containers (v20.x)"
weight: 10
description: "Deployment guide for SW360 v20.x using containers (Docker or Podman)"
---

## Introduction

This guide details how to deploy SW360 version 20 using containers. The
deployment stack is designed to be generic and can be run with either **Docker
(Compose V2)** or **Podman (`podman-compose`)**. 

Using containers isolates the SW360 components and simplifies deploying the full
stack (backend, frontend, databases, and authentication server) consistently.

## Prerequisites

- Docker (with Compose V2) OR Podman (with `podman-compose`)
- Basic understanding of container networking and persistent volumes
- Terraform OR OpenTofu (required only if configuring Keycloak via automation)

## Architecture / Containers Utilized

The full-stack deployment consists of several interconnected containers:

- **`sw360`**: The core Java Spring Boot backend, running the main SW360 REST
  APIs and logic.
- **`couchdb` & `couchdb-nouveau`**: The primary NoSQL database and its
  full-text search sidecar used for fast indexing and querying across SW360
  data.
- **`sw360-frontend`**: The new Next.js-based user interface for version 20.
- **`keycloak`**: The OpenID Connect authentication server managing users and
  SSO.
- **`postgres`**: The relational database backing Keycloak configuration and
  user identities.
- **`web` (Nginx)**: An Nginx reverse proxy that provides SSL termination and
  routes traffic to the appropriate backend, frontend, or auth services.

## Configuration & Best Practices

The setup uses a mix of environment variables (`.env` files) for non-sensitive
configuration and Docker/Podman secrets for passwords and credentials. 

### Secrets vs Environment Variables

- **Environment Variables**: Defined in `.env` files within the `config/`
  directories (e.g., `config/front-end/.env.frontend`,
  `config/sw360/.env.backend`). These handle public URLs, domain names, and
  authentication providers.
- **Secrets**: Stored in flat files (e.g., `config/sw360/default_secrets`,
  `config/postgres/postgresql_password`). These handle sensitive information
  like CouchDB and Postgres database passwords safely without risking exposing
  them as environment variables during runtime. In production, these should be
  robustly managed (e.g., using a vault service or restricted file permissions).

### Nginx Reverse Proxy Configuration

The `web` container uses the `config/nginx/rev_proxy.template` to configure the
Nginx server dynamically via the `envsubst` mechanism, substituting variables
from the `.env` configuration file on startup.
- **Routing**: It routes root traffic `/` to the Next.js frontend
  (`sw360-frontend:3000`), backend traffic `/resource` and `/authorization` to
  the SW360 backend, and identity traffic `/kc` to Keycloak.
- **Headers**: Common proxy headers are maintained in an external configuration
  `config/nginx/proxy_params`, keeping the main reverse proxy template clean.

### Authentication Methods

SW360 v20 frontend and backend support three modes of authentication. These are
configured primarily using the `NEXT_PUBLIC_SW360_AUTH_PROVIDER` variable in the
`config/front-end/.env.frontend` file.

#### 1. Built-in Basic Auth (`sw360basic`)
This is the default setup. It relies on the built-in basic username and password
stored directly within the backend's database. No extra frontend configuration
is needed beyond defaults. The default setup user is `setup@sw360.org` /
`sw360fossie` (configurable in `.env.backend`).

#### 2. SW360 OAuth2 (`sw360oauth`)
Leverages SW360's internal OAuth2 authorization server.
To use this, you must first create a default OAuth client in your CouchDB
database using the setup script found in the core backend repository.

Clone the backend repository and run the script:
```bash
git clone https://github.com/eclipse-sw360/sw360.git
cd sw360
./scripts/addUnsafeDefaultClient.sh
```
*(By default, this sets up the client `trusted-sw360-client` with a secret of
`sw360-secret` interacting with `127.0.0.1:5984`. You can pass flags like
`--host`, `--user`, `--pass` to customize this or `-d` to delete the client
later).*

Update your `config/front-end/.env.frontend` to use this provider:
```env
NEXT_PUBLIC_SW360_AUTH_PROVIDER=sw360oauth
SW360_REST_CLIENT_ID=trusted-sw360-client
SW360_REST_CLIENT_SECRET=sw360-secret
```

#### 3. Keycloak OpenID Connect (`keycloak`)
Uses the external Keycloak container included in the full stack. This is the
**recommended setup for production**.

Keycloak requires a one-time realm and client setup which can be cleanly
automated via Terraform or OpenTofu. 
1. Obtain the Keycloak Terraform/OpenTofu scripts from the SW360 master
   repository at `third-party/keycloak-tf`.
2. Follow the
   [Keycloak Terraform/OpenTofu README](https://github.com/eclipse-sw360/sw360/blob/main/third-party/keycloak-tf/README.md)
   to log in and create an initial OIDC client for your master realm.
3. Copy the template `local.tfvars` as `prod.auto.tfvars`. Adjust variables
   such as `kc_client_id`, `kc_client_secret`, `redirect_uris`, and
   `frontend_base_url` as necessary.
4. Run `terraform apply` (or `tofu apply`) to generate the complete realm
   settings.

Update your `config/front-end/.env.frontend` to connect with Keycloak:
```env
NEXT_PUBLIC_SW360_AUTH_PROVIDER=keycloak
SW360_KEYCLOAK_CLIENT_ID=sw360ui
SW360_KEYCLOAK_CLIENT_SECRET=myoidcsecret
AUTH_ISSUER=https://localhost/kc/realms/sw360
```

## Networking & Volumes

All containers run inside an external network named `sw360net`. This allows
other standalone containers (like external analysis tools) to easily join the
network in the future without modifying the core compose file.

**Persistent Volumes:**
Data persistence is handled via dedicated volumes, ensuring that upgrades or
container restarts don't result in data loss:
- `couchdb`: Stores SW360 database data (`/opt/couchdb/data`).
- `etc`: Stores generated SW360 backend configuration (`/etc/sw360`).
- `postgres_storage`: Stores Keycloak user and configuration data
  (`/var/lib/postgresql`).

## Quick Start

The complete container configuration, including the `docker-compose-full.yml`
file and all `config/` directories, is located within the frontend repository.

1. Clone the frontend repository where the compose files are housed:

    ```bash
    git clone https://github.com/eclipse-sw360/sw360-frontend.git
    cd sw360-frontend
    ```

2. Create the shared external network:

    ```bash
    docker network create sw360net
    # OR for podman:
    # podman network create sw360net
    ```

3. Start the full stack using the full compose file (`docker-compose-full.yml`):

    ```bash
    docker compose -f docker-compose-full.yml up -d
    # OR for podman:
    # podman-compose -f docker-compose-full.yml up -d
    ```

4. Access the application:
   - **Frontend:** `https://localhost` (or your configured `SERVER_DOMAIN`)
   - **Backend API:** `https://localhost/resource`
   - **Keycloak Admin:** `https://localhost/kc`

### Further Configuration Reference

For a comprehensive explanation of all available environment variables,
specific secret mappings, and advanced container configuration options,
please consult the official Docker documentation located in the respective
repositories:

- **SW360 Backend Configuration:** [README_DOCKER.md (`eclipse-sw360/sw360`)](https://github.com/eclipse-sw360/sw360/blob/main/README_DOCKER.md)
- **SW360 Frontend Configuration:** [README_DOCKER.md (`eclipse-sw360/sw360-frontend`)](https://github.com/eclipse-sw360/sw360-frontend/blob/main/README_DOCKER.md)

## Troubleshooting & Logging

Should any part of the stack fail to initialize properly or encounter runtime
exceptions, checking individual container logs is the strongest diagnostic
resource available.

To stream the unified standard output strings of a single container, utilize the
compose `logs -f` command against the target container alias (`sw360`,
`sw360-frontend`, `keycloak`, `couchdb`, `web` or `postgres`):

```bash
docker compose logs -f sw360-frontend
# OR
docker compose logs -f keycloak
```

*(If utilizing Podman, replace `docker compose` with `podman-compose logs -f <service_name>`)*.

## FOSSology Integration

*Placeholder: Instructions for integrating FOSSology will be provided in a
separate Administration Guide document in the near future. Once published, it
will be linked here.*

## Disclaimer

> [!WARNING]
> The configuration values, environment parameters, and the
> `docker-compose-full.yml` file provided in this guide are intended **for
> reference and development purposes only**. System administrators must adapt and
> secure these configurations based on their specific operational requirements and
> their company's internal security policies before using them in a production
> environment.
