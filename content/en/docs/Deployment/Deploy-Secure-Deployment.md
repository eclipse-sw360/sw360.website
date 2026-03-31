---
linkTitle: "Security Best Practices"
title: "Security Best Practices"
weight: 100
description: 
  SW360 security checklist pre and post deployment for v20+
---

Securing an SW360 deployment involves multiple layers, from the infrastructure
and container orchestration to the application and identity management. For v20,
the architecture relies on a microservices stack (Spring Boot, Next.js, Keycloak)
which necessitates new security patterns.

## Recommended: Container-Based Security

The easiest way to manage a secure SW360 instance is through **container-based
deployments** using Docker or Podman. This allows for clear service isolation and
centralized secret management.

### 1. Secret Management
Never store plain-text passwords in environment variables if possible. Use **Docker
Secrets** for sensitive data:
* **Postgres**: Use `POSTGRES_PASSWORD_FILE` to point to a mounted secret.
* **SW360 Backend**: Use `SW360_SECRETS` and `COUCHDB_SECRETS` mount points.
* **Next.js Frontend**: Ensure `NEXTAUTH_SECRET` is set to a unique, random
  string in production.

### 2. Network Isolation
In a typical `docker-compose` setup, all SW360 services should reside in an
**internal network** (e.g., `sw360net`).
* **Do not expose service ports** (8080, 3000, 5432, 5984) directly to the host
  machine.
* Only the **Nginx Reverse Proxy** should have port **443** exposed to the outer
  network.

### 3. Nginx and TLS
The reference
[docker-compose-full.yml](https://github.com/eclipse-sw360/sw360-frontend/blob/main/docker-compose-full.yml)
uses Nginx with **snakeoil (self-signed) certificates** for convenience during
development.
> [!CAUTION]
> **DO NOT** use default snakeoil certificates in production. Replace them with
> valid certificates from a trusted CA (e.g., Let's Encrypt).

## Mandatory: Credential Rotation

After the initial setup, several default accounts and credentials **must** be
rotated immediately.

### 1. Keycloak Administrative Account
The default Keycloak admin (initially set via `KC_KEYCLOAK_ADMIN_PASSWORD`) has
full control over your authentication realm.
* Change the password via the Keycloak Console (`/kc/admin`).
* Disable or remove the emergency admin account once you have created a personal
  administrator user.

### 2. SW360 Initial Admin User
The default seeded administrator (often `admin@sw360.org` or `setup@sw360.org`)
should be secured:
* Log in and change the password immediately.
* Refer to the
  [Frontend Docker README](https://github.com/eclipse-sw360/sw360-frontend/blob/main/README_DOCKER.md)
  for instructions on overriding these defaults via `COUCHDB_ADMIN_EMAIL` and
  `COUCHDB_ADMIN_PASSWORD` before the first run.

### 3. OIDC Client Secrets
The communication between the SW360 components and Keycloak uses OIDC Client
Secrets.
* The default `SW360_KEYCLOAK_CLIENT_SECRET` (e.g., `myoidcsecret`) must be
  changed in both the **Keycloak Admin Console** and your **frontend `.env`
  configuration**.
* Rotate the `AUTH_SECRET` used by NextAuth to encrypt session tokens.

### 4. Database Passwords
Ensure that the passwords for **CouchDB** and **Postgres** (for Keycloak) are
unique and non-default. CouchDB "Admin Party" (no password) must be disabled.

## Bare Metal & General Security Tips

If you are running SW360 on bare metal or custom virtual machines, follow these
additional guidelines:

### 1. File System Permissions
* Ensure that configuration files containing secrets (e.g., `sw360.properties`,
  `.env`) are set to `600` (readable only by the owner).
* The SW360 runtime user (e.g., `sw360`) should **not** have `sudo` rights. You
  never know what your JVM can access.

### 2. Service Binding
* Limit internal services (CouchDB, Redis, Postgres) to bind to `localhost`
  (`127.0.0.1`) only.
* Use a local firewall (e.g., `ufw` or `firewalld`) to block all inbound traffic
  except for SSH (restricted) and HTTPS.

### 3. Java and Tomcat Hardening
* Run Tomcat as a non-privileged system user.
* Disable the Tomcat Manager app and other default web applications in
  production.
* Keep the OpenJDK runtime updated to the latest security patch for Java 21.

## Post-Deployment Checklist
- [ ] HTTPS is mandatory and enforced via HSTS in Nginx.
- [ ] No default passwords remain for Keycloak, Databases, or SW360 Admin.
- [ ] OIDC client secrets are rotated and not stored in public repositories.
- [ ] Docker images are periodically scanned for vulnerabilities.
- [ ] Backup procedures for CouchDB and Postgres are encrypted and verified.
