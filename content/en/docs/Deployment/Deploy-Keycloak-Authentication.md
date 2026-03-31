---
linkTitle: "Keycloak Authentication"
title: "Keycloak Authentication"
weight: 70
description: 
  Modern Keycloak authentication setup for SW360 using Terraform automation.
---

This guide covers the installation and configuration of Keycloak for SW360.
While manual configuration is possible, **using the provided Terraform scripts
is the highy recommended approach** to maintain a modern, version-controlled
authentication setup.

## Installation (Brief)

**Prerequisites:**

1. **Java 21**: Ensure OpenJDK 21 is installed and `JAVA_HOME` is set.
2. **PostgreSQL**: Install PostgreSQL 14 or higher and create a database/user
   for Keycloak:
    ```sql
    CREATE USER keycloak WITH ENCRYPTED PASSWORD 'mystrongpassword';
    CREATE DATABASE keycloak;
    GRANT ALL PRIVILEGES ON DATABASE keycloak TO keycloak;
    ```
3. **Keycloak**: Download the latest Keycloak (e.g., v26+) and extract it
   to `/opt/keycloak`.

## Keycloak Configuration (`keycloak.conf`)

For a development setup, you can use the following `keycloak.conf`. For
production, refer to the [Production Tips](#production-deployment-tips) below.

```properties
# Database
db=postgres
db-username=keycloak
db-password=mystrongpassword
db-url=jdbc:postgresql://localhost/keycloak

# SW360 Initial Admin
keycloak-admin=admin
keycloak-admin-password=admin

# HTTP/HTTPS Configuration
http-enabled=true
http-port=8083
https-port=8533

# Logging
log=console,file
```

### Production Deployment Tips
- **Hostname**: Set `hostname=<your-domain>` and `hostname-strict=true`.
- **HTTPS**: Configure `https-certificate-file` and
  `https-certificate-key-file`.
- **Database**: Tune `db-pool-initial-size` and `db-pool-max-size` for your
  load.
- **Proxy**: If behind a reverse proxy, set `proxy=edge` (or appropriate mode).

## Building the Backend & Deploying Providers

SW360 uses custom Keycloak providers for user storage and event listening. These
must be built and copied to the Keycloak `providers` directory.

Use the `-Dlistener.deploy.dir` flag during the Maven build to automate this:

```bash
mvn clean install -DskipTests -P deploy \
    -Dbase.deploy.dir=/opt/apache-tomcat/ \
    -Dlistener.deploy.dir=/opt/keycloak/providers
```

After the build, ensure the following JARs are present in your Keycloak
`providers/` folder:
- `sw360-keycloak-user-storage-provider.jar`
- `sw360-keycloak-event-listener.jar`
- (And other required dependencies like `spring-security-crypto`, etc.)

**Note:** The previous dependency on external Thrift servers for Keycloak
providers has been removed; providers now communicate directly with the
necessary data layers.

## Automated Realm Configuration (Terraform)

SW360 provides
[Terraform/OpenTofu scripts](https://github.com/eclipse-sw360/sw360/tree/main/third-party/keycloak-tf)
to fully automate the creation of the realm, clients, scopes, and groups.

### 1. Initialization
Log into your Keycloak master realm and create an OIDC client with "Client
Credentials" grant to allow Terraform to authenticate, as described in the
[Keycloak Terraform README](https://github.com/eclipse-sw360/sw360/blob/main/third-party/keycloak-tf/README.md).

### 2. Configuration Variables
Copy `local.tfvars` to `prod.auto.tfvars` and configure the following
variables:

| Variable | Description |
| :--- | :--- |
| `kc_base_url` | Base URL where Keycloak is running (e.g., `http://localhost:8083`). |
| `kc_client_id` / `kc_client_secret` | Credentials for the master realm OIDC client. |
| `frontend_base_url` | Base URL of your SW360 frontend. |
| `redirect_uris` | Allowed callback URLs for the frontend. |
| `smtp_*` | SMTP settings for email notifications (host, port, username, password, etc.). |
| `tenant` / `azure_client_id` | *(Optional)* Azure EntraID integration settings. |
| `azure_idp_alias` | Custom alias for the Azure Identity Provider. |
| `dashboard_base_url` | *(Optional)* URL for a Grafana dashboard integration. |

### 3. Apply
Run `tofu init` and `tofu apply` to provision the setup.

## User Client Management

To allow external tools or users to access the SW360 REST API, you can create
dedicated OpenID clients using the `l-sw360-clients-list.tf` file.

1. Edit `l-sw360-clients-list.tf` in the `third-party/keycloak-tf` directory.
2. Add an entry to `sw360_read_clients` or `sw360_write_clients` in the
   `locals` block:
    ```hcl
    {
      user_email    = "user@example.com"
      creator_email = "admin@example.com"
      user_group    = "RESEARCH"
      creation_date = "2026-03-31"
    }
    ```
3. Run `tofu apply`.
4. Retrieve the generated **Client ID** and **Client Secret** from the Keycloak
   Admin Console (under the "sw360" realm -> Clients).

### Token Creation Information
Users can generate tokens using the following settings:
- **Grant Type**: Client Credentials
- **Token URL**: `https://<keycloak-server>/realms/sw360/protocol/openid-connect/token`
- **Scope (Read)**: `openid email READ`
- **Scope (Read/Write)**: `openid email READ WRITE`

## Migrating Legacy OAuth Clients

If you are migrating from an older SW360 installation, you can use the
`export_clients.py` script to import existing Liferay OAuth clients into
Keycloak.

Detailed instructions and the script can be found in the
[Keycloak Terraform README](https://github.com/eclipse-sw360/sw360/blob/main/third-party/keycloak-tf/README.md#migrating-legacy-oauth-clients).

---

## Historical Reference
For a deeper understanding of the manual configuration steps performed by these
scripts, or for legacy setups, please refer to the
[Manual Keycloak Configuration Guide](./Legacy/Deploy-Keycloak-Manual.md).
