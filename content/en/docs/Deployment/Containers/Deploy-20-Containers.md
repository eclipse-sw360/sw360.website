---
title: "Version 20.x with Containers"
linkTitle: "Containers (v20.x)"
weight: 10
description: "Minimal entry page for SW360 v20 container deployments"
---

## Introduction

For SW360 v20 container deployments, the canonical operational guide is maintained in:

**[SW360 Frontend Docker Guide (`eclipse-sw360/sw360-frontend`)](https://github.com/eclipse-sw360/sw360-frontend/blob/main/README_DOCKER.md)**

This page intentionally stays minimal and points to the source of truth for:
* compose setup and startup flow
* service wiring
* secrets and runtime configuration files
* Keycloak initialization and frontend integration

## Prerequisites

* Docker (Compose V2) or Podman
* Basic container networking and volume knowledge
* OpenTofu/Terraform only if you bootstrap Keycloak via automation

## Container Topology (High-Level)

Typical SW360 v20 container deployments include:
* `sw360` (backend API)
* `couchdb` + `couchdb-nouveau` (database + search)
* `sw360-frontend` (UI)
* `keycloak` + `postgres` (identity)
* `web` (reverse proxy)

For exact compose definitions and current defaults, use the frontend Docker guide:
<https://github.com/eclipse-sw360/sw360-frontend/blob/main/README_DOCKER.md>

## Canonical References

* **Compose + stack operations (source of truth):**
  <https://github.com/eclipse-sw360/sw360-frontend/blob/main/README_DOCKER.md>
* **Backend image/runtime semantics (env vars, secrets, entrypoint behavior):**
  <https://github.com/eclipse-sw360/sw360/blob/main/README_DOCKER.md>
* **Security guidance:**
  [Securing SW360 (Administration Guide)](../../AdministrationGuide/Securing-SW360.md)

## Troubleshooting

Use compose logs for initial diagnostics:

```bash
docker compose logs -f <service>
```

For Podman, use equivalent compose log commands in your setup.

## Disclaimer

> [!WARNING]
> Container setup values are reference defaults only. Operators must adapt and
> harden all URLs, secrets, certificates, network exposure, and image tags for
> their own environments before production use.
