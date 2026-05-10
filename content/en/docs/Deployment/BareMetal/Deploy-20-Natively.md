---
linkTitle: "Version 20.x on Debian 12"
title: "Version 20.x on Debian 12"
weight: 100
description: Bare metal deployment with Debian based Linux for SW360 v20.x
---

## Introduction

We are covering the installation for Debian based Linux distros. sw360 may run
on a variety of other linux distributions or OSes such as Mac OSX (amd64 only).

This is a guide with detailed explanation of how to install and run SW360
natively on you local machine. It includes installation of all dependencies
manually, and will not use docker or other container system during the
installation or run.

## Requirements

The installation consists of quite some tasks, as an overview:

* Java 21
* Maven >= 3.5.0
* Tomcat 11.0
* Postgresql >= 16
* CouchDB >= 3.5.x
* Thrift 0.20.0
* NodeJS >= 22.x
* pnpm

## Initial steps

In order to "calibrate the system" just run the update / upgrade cycle once:

```shell
sudo apt update
sudo apt upgrade
```

## 1. Installing backend services

### 1.1. CouchDB

CouchDB manages their own package repository, and we will be using it to get
latest packages for installation.

Starting with adding keys and sources to APT and installing the couchdb and the
couchdb-nouveau (full-text search engine) packages.

```shell
apt install curl gnupg2 apt-transport-https lsb-release
curl 'https://couchdb.apache.org/repo/keys.asc' | gpg2 --dearmor | sudo tee /etc/apt/trusted.gpg.d/couchdb-archive-keyring.gpg >/dev/null 2>&1
sudo chown root:root /etc/apt/trusted.gpg.d/couchdb-archive-keyring.gpg
sudo chmod 0644 /etc/apt/trusted.gpg.d/couchdb-archive-keyring.gpg
echo "deb [signed-by=/etc/apt/trusted.gpg.d/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/couchdb.list
sudo chmod 0644 /etc/apt/sources.list.d/couchdb.list
sudo apt-get update -y
sudo apt-get install -y couchdb couchdb-nouveau
```

The installer will ask a couple of questions:

1. Bind address: for CouchDB and SW360 `127.0.0.1` (localhost) is a good bind
   address, if you would like to access the server from a remote computer
   because your sw360 runs as a server in the network, you would need to change
   accordingly.
2. Unless you know what you are doing, use standalone installation instead of
   clustered option, for a regular single installation.
3. Enable Nouveau in CouchDB (if installed)?: We want to enable it so SW360 can
   use it for search interface. Later, it can be customized to change index
   storage location, if needed.
4. Admin user: For fresh installation for sure a very good idea. You can set the
   password at sw360 for CouchDB in `couchdb.properties` and place it centrally
   in `/etc/sw360`.

### 1.2. Java 21

If you do not have installed java 21 yet on your setup:

```shell
curl 'https://packages.adoptium.net/artifactory/api/gpg/key/public' | gpg2 --dearmor | sudo tee /etc/apt/trusted.gpg.d/apache-temurin.gpg >/dev/null 2>&1
sudo chown root:root /etc/apt/trusted.gpg.d/apache-temurin.gpg
sudo chmod 0644 /etc/apt/trusted.gpg.d/apache-temurin.gpg
echo "deb [signed-by=/etc/apt/trusted.gpg.d/apache-temurin.gpg] https://packages.adoptium.net/artifactory/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/adoptium.list
sudo chmod 0644 /etc/apt/sources.list.d/adoptium.list
sudo apt-get update -y
sudo apt-get install -y temurin-21-jdk
```

### 1.3. Thrift

To install Apache Thrift using the helper script in the SW360 project, run the
install-thrift.sh script located in
[third-party/thrift/install-thrift.sh](https://github.com/eclipse-sw360/sw360/blob/d7869d252c4b4c84e6ee389cbed44543cd37f7ac/third-party/thrift/install-thrift.sh)

```bash
sudo ./third-party/thrift/install-thrift.sh
```

In case there is thrift in the package management of the OS you are running on,
just make sure, you have version 0.20

### 1.4. Maven

If your OS has maven version 3.5.0 or above, you can simply go and install it.

Otherwise, you can install maven manually:

```shell
curl -L 'https://dlcdn.apache.org/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz' -o ~/Downloads/maven-3.9.9.tar.gz
sudo tar -xzvf ~/Downloads/maven-3.9.9.tar.gz -C /opt
sudo find /opt/apache-maven-3.9.9/ -type d -exec chmod 755 {} \;
sudo update-alternatives --install /usr/bin/mvn mvn /opt/apache-maven-3.9.9/bin/mvn 399
printf 'export M2_HOME=/opt/apache-maven-3.9.9\nexport PATH=${M2_HOME}/bin:${PATH}' | sudo tee /etc/profile.d/maven.sh
sudo chmod 0644 /etc/profile.d/maven.sh
```

### 1.5. Install Apache Tomcat 11

Get the latest version of [Apache Tomcat 11](https://tomcat.apache.org/download-11.cgi).
and install it in `/opt`

```shell
curl -L 'https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.4/bin/apache-tomcat-11.0.4.tar.gz' -o ~/Downloads/tomcat-11.0.4.tar.gz
sudo tar -xzvf ~/Downloads/tomcat-11.0.4.tar.gz -C /opt
sudo chown -R $USER:$USER /opt/apache-tomcat-11.0.4/
```

### 1.6. Clone SW360 backend and create default user

* Clone sw360 source code to folder
    ```shell
    git clone https://github.com/eclipse-sw360/sw360.git
    ```
* Create default user `admin@sw360.org` with password `admin`.
    ```shell
    ./scripts/addUnsafeDefaultClient.sh
    ```
* You may pass following flags to the script
  * `-d` : Should delete default client
  * `-du` : Should delete default user
  * `--host` : To change host from `http://127.0.0.1:5984`
  * `--user` : To change username from `admin`
  * `--pass` : To change password from `admin`

### 1.7. Build sw360 version 20.x

* Create config properties
  * `sudo mkdir -p /etc/sw360 /etc/sw360/autorization /etc/sw360/rest`
  * Find the relevant configurations at [Configurable Property Keys](../../Deployment/Deploy-Configuration-Files.md)
* Compile and install the application
  * `mvn clean install -Dbase.deploy.dir=/opt/apache-tomcat-11.0.4/ -P deploy`

This will install the jar and war files at appropriate locations.

### 1.8. Start backend service

* Start tomcat server
    ```shell
    /opt/apache-tomcat-11.0.4/bin/startup.sh
    ```
* Check tomcat logs
    ```shell
    tail -f100 /opt/apache-tomcat-11.0.4/logs/catalina.out
    ```

Once you see message like
`org.apache.catalina.startup.Catalina.start Server startup in [**] milliseconds`
in the logs, the backend is up and can load the OpenAPI docs at
[http://localhost:8080/resource/v3/api-docs](http://localhost:8080/resource/v3/api-docs)

The backend install SwaggerUI as well and accessible via
[http://localhost:8080/resource/swagger-ui/index.html](http://localhost:8080/resource/swagger-ui/index.html)

## 2. Installing frontend services

Since version 19, SW360 has separated the front-end as a React based project.
It is hosted at [Github SW360 Frontend repository](https://github.com/eclipse-sw360/sw360-frontend/) and needs to be
installed as well.

### 2.1. Install node 22

First we need to install Node and NPM version 22 or above. Setting nvm is the
easiest and fastest way to do it for your user. Follow the
[guide from installing and updating](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating)

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 22
```

### 2.2. Install pnpm

pnpm is an advanced package manager for node dependencies and can be installed
with the new npm installed above.

```shell
npm install -g pnpm@latest-10
```

### 2.3. Clone and install frontend

* Clone sw360 source code to folder
    ```shell
    git clone https://github.com/eclipse-sw360/sw360-frontend.git
    ```
* Setup `.env` file
    ```ini
    NEXTAUTH_SECRET='secret'
    NEXT_PUBLIC_SW360_API_URL='http://localhost:8080'
    NEXTAUTH_URL='http://localhost:3000'
    # possible values are sw360basic, sw360oauth, keycloak
    NEXT_PUBLIC_SW360_AUTH_PROVIDER='sw360basic'
    ```
* Install dependencies and build pages
    ```shell
    pnpm install
    pnpm build
    ```
* Start the server and visit [http://localhost:3000](http://localhost:3000)
    ```shell
    pnpm run dev
    ```

If done correctly, you should see the SW360 frontend and upon clicking on the
"Sign In" button, you should get a popup asking for username and password.
The default username and password is "admin:admin" setup by the
`addUnsafeDefaultClient.sh` script.

## 3. Setup OAuth based logins for SW360

SW360 backend can support 3 types of authentication:
1. Basic authentication with username and password
2. OAuth2 authentication with builtin authorization server
3. OAuth2 authentication with Keycloak

### 3.1. Basic authentication

This is the default authentication method. You can use the default admin user
to login. The Authorization header for the REST API call should look like this:

```
Authorization: Basic <base64-encoded-username:password>
```

The frontend config from [2.3](#23-clone-and-install-frontend) defines it using
`NEXT_PUBLIC_SW360_AUTH_PROVIDER='sw360basic'` in the `.env` file.

### 3.2. OAuth2 authentication with builtin authorization server

SW360 also ships with a builtin authorization server built on Spring Security
and is available at `/authorization` endpoint. The same can be used for
generating OAuth tokens for calling backend with username and password.

The well-known endpoint for the authorization server is:
[http://localhost:8080/authorization/.well-known/oauth-authorization-server](http://localhost:8080/authorization/.well-known/oauth-authorization-server)

During the installation of the backend at step
[1.6](#16-clone-sw360-backend-and-create-default-user), with the script
`addUnsafeDefaultClient.sh`, a default user is created as well as a default
client to user with authorization server. The client id is
`trusted-sw360-client` and the client secret is `sw360-secret`.

#### 3.2.1. Setup the backend

To make sure the authorization server is configured correctly, in the backend
code, make sure the `rest/resource-server/src/main/resources/application.yml`
configuration file has the following properties set. If not, modify the file
and install the backend server again.

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: http://localhost:8080/authorization/oauth2/jwks
          jwk-set-uri: http://localhost:8080/authorization/oauth2/jwks
```

**Notice** the `jwks` urls are pointing to the authorization server.

#### 3.2.2. Setup the frontend to use OAuth2 authentication

The frontend can be configured to use the OAuth2 authentication with the
following changes in the `.env` file:

```ini
NEXT_PUBLIC_SW360_REST_CLIENT_ID='trusted-sw360-client'
NEXT_PUBLIC_SW360_REST_CLIENT_SECRET='sw360-secret'
NEXT_PUBLIC_SW360_AUTH_PROVIDER='sw360oauth'
```

If everything done correctly, next time you open the frontend, upon clicking on
"Sign In", you should be redirected to the authorization server login page
instead of seeing a popup asking for username and password.

#### 3.2.3. Generate OAuth2 token

Using the above-mentioned configurations, you can generate an OAuth2 token from
any application of your choice. But to summarize, you need to:

```
Well-Known URL: http://localhost:8080/authorization/.well-known/oauth-authorization-server
Authorization URL: http://localhost:8080/authorization/oauth2/authorize
Token URL: http://localhost:8080/authorization/oauth2/token
Grant Type: authorization_code

Client ID: trusted-sw360-client
Client Secret: sw360-secret
Scope: openid READ WRITE ADMIN
PKCE: true
```

### 3.3. OAuth2 authentication with Keycloak

SW360 frontend and backend can also be configured to use Keycloak as an external
authorization server. This is an involved process and requires a running
Keycloak server.

#### 3.3.1. Install Keycloak

Get the latest 26.x.x version from [Keycloak downloads](https://www.keycloak.org/downloads).

```shell
curl -L 'https://github.com/keycloak/keycloak/releases/download/26.1.3/keycloak-26.1.3.tar.gz' -o ~/Downloads/keycloak-26.1.3.tar.gz
sudo tar -xzvf ~/Downloads/keycloak-26.1.3.tar.gz -C /opt
sudo chown -R $USER:$USER /opt/keycloak-26.1.3/
```

Install PostgreSQL used by Keycloak for management.

```bash
sudo apt install postgresql
```

or whatever package version is suitable here, for example version 15 for
Debian 12.

After installation, it is considered best practice to set up and configure your
Keycloak realm, clients, and roles using Terraform/OpenTofu. This ensures that
all components, scopes, and roles are appropriately aligned with SW360
requirements, especially doing so after periodic upgrades prevents out-of-sync
configurations.

1. Clone the repository and navigate to the Terraform directory:
    ```bash
    git clone https://github.com/eclipse-sw360/sw360.git
    cd sw360/third-party/keycloak-tf
    ```
2. Following the
   [Keycloak Terraform README](https://github.com/eclipse-sw360/sw360/blob/main/third-party/keycloak-tf/README.md),
   create an initial OIDC client for your master realm.
3. Copy `local.tfvars` as `prod.auto.tfvars` and configure the necessary
   variables (e.g., `kc_client_id`, `kc_client_secret`, and your
   `redirect_uris`).
4. Run `terraform apply` (or `tofu apply`) to provision all required Keycloak
   scopes and roles.

#### 3.3.2. Configure backend to use Keycloak

For backend to authenticate JWT tokens generated by Keycloak, you need to tell
it the location of JWKs endpoint exposed by Keycloak. Modify the
`rest/resource-server/src/main/resources/application.yml` configuration file
and point the `issuer-uri` and `jwk-set-uri` to the Keycloak server for your
realm.

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: http://localhost:8083/realms/sw360
          jwk-set-uri: https://localhost:8083/realms/sw360/protocol/openid-connect/certs
```

Once the changes are done, compile and reinstall the application with additional
flag for Keycloak listener.
```shell
mvn clean install -Dbase.deploy.dir=/opt/apache-tomcat-11.0.4/ -Dlistener.deploy.dir=/opt/keycloak-26.1.3/providers -P deploy
```

This will install the jar and war files at appropriate locations.

#### 3.3.3. Configure frontend to use KeyCloak

The frontend also has to be configured to use Keycloak as the authentication
provider. Modify the `.env` file to include the following properties:

```ini
SW360_KEYCLOAK_CLIENT_ID='client-from-kc'
SW360_KEYCLOAK_CLIENT_SECRET='secret-from-kc'
AUTH_ISSUER='http://localhost:8083/realms/sw360'
NEXT_PUBLIC_SW360_AUTH_PROVIDER='keycloak'
```

If everything done correctly, next time you open the frontend, upon clicking on
"Sign In", you should be redirected to the Keycloak login page instead of
seeing a popup asking for username and password.

## 4. Recommended for Production

For robust deployment in a true production environment, it is highly
recommended to adapt the application stack from a manual layout to a
service-based architecture guarded by a reverse proxy.

### 4.0. Security Hardening

Before going live, review and apply the following security flags.

#### Disable HTTP Basic Authentication

HTTP Basic authentication is useful for development and testing but should
be disabled in production. When Basic auth is active, credentials are
transmitted with every request and browser-based clients may be exposed to
additional risks.

SW360 ships with **Basic auth enabled by default** (so the bare-metal
development workflow works out of the box). Disable it by activating the
`prod` Spring profile on Tomcat startup, or by setting the property
explicitly.

**Option A - Spring `prod` profile (recommended)**

Add the `prod` profile to the Tomcat JVM options so it picks up
`application-prod.yml` which sets `sw360.security.http-basic.enabled=false`:

```shell
# In /etc/systemd/system/tomcat.service (or catalina.sh / setenv.sh)
Environment="JAVA_OPTS=-Dspring.profiles.active=prod"
```

Or set the environment variable:
```shell
export SPRING_PROFILES_ACTIVE=prod
```

**Option B - Explicit property override**

Alternatively, add the property directly to `/etc/sw360/rest/application.yml`
and `/etc/sw360/authorization/application.yml`:

```yaml
sw360:
  security:
    http-basic:
      enabled: false
```

After disabling Basic auth, all clients (including the frontend) must
authenticate via:
- OAuth2/JWT from the built-in authorization server (see
  [3.2](#32-oauth2-authentication-with-builtin-authorization-server)), or
- OAuth2/JWT from Keycloak (see
  [3.3](#33-oauth2-authentication-with-keycloak)), or
- SW360 API tokens (generated per-user via the UI or REST API).

### 4.1. Process Management (systemd)

Instead of running components like Tomcat, Keycloak, or the Next.js `pnpm dev`
scripts interactively in a foreground terminal, you should manage them via
`systemd` to strictly enforce crash-restarts, centralized logging, and start-up
synchronization on boot.

Use the following services as template and create the services in
`/etc/systemd/system/` directory. Make sure to replace the placeholder values
with the actual values.

**Tomcat Service (`tomcat.service`)**
```ini
[Unit]
Description=Apache Tomcat Web Application Container
After=network.target

[Service]
Type=forking

# Environment variables
Environment="JAVA_HOME=/path/to/jdk-home"
Environment="CATALINA_HOME=/path/to/tomcat-home"
Environment="CATALINA_BASE=/path/to/tomcat-home"
Environment="CATALINA_PID=/path/to/tomcat-home/temp/tomcat.pid"

# SW360 Environment variables
Environment="SW360_CORS_ALLOWED_ORIGIN=http://localhost"

# Command to start Tomcat
ExecStart=/path/to/tomcat-home/bin/startup.sh
ExecStop=/path/to/tomcat-home/bin/shutdown.sh

# User and group
User=non-privileged-user
Group=non-privileged-group

# Restart on failure
Restart=on-failure

WorkingDirectory=/path/to/tomcat-home

[Install]
WantedBy=multi-user.target
```

**Keycloak Service (`keycloak.service`)**
```ini
[Unit]
Description=Keycloak Application Server
After=syslog.target network.target

[Service]
Type=idle

# Environment variables
Environment="JAVA_HOME=/path/to/jdk-home"
Environment="KC_TRANSACTION_XA_ENABLED=true"
Environment="QUARKUS_TRANSACTION_MANAGER_ENABLE_RECOVERY=true"

# Command to start Tomcat
ExecStart=/path/to/keycloak-home/bin/kc.sh start-dev

# User and group
User=non-privileged-user
Group=non-privileged-group

# Restart on failure
Restart=on-failure
RemainAfterExit=yes

WorkingDirectory=/path/to/keycloak-home

[Install]
WantedBy=multi-user.target
```

**SW360 Frontend Service (`sw360-frontend.service`)**
*Note: Ensure to run `pnpm build` first.*
```ini
[Unit]
Description=SW360 front-end application
After=network.target

[Service]
Type=simple

# Environment variables
Environment="NODE_ENV=production"
Environment="PORT=3000"
Environment="PATH=/path/to/node/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
Environment="NODE_TLS_REJECT_UNAUTHORIZED=0"

# Command to start
ExecStart=/path/to/node/bin/node .next/standalone/server.js

# User and group
User=non-privileged-user
Group=non-privileged-group

# Restart on failure
Restart=always

WorkingDirectory=/path/to/sw360-frontend
StandardOutput=journal
StandardError=journal
SyslogIdentifier=sw360FrontendApp

[Install]
WantedBy=multi-user.target
```

After creating the services, enable and start them:
```shell
sudo systemctl daemon-reload
sudo systemctl enable --now tomcat.service
sudo systemctl enable --now keycloak.service
sudo systemctl enable --now sw360-frontend.service
```

Check the status of the services:
1. `sudo systemctl status tomcat.service`
2. `sudo systemctl status keycloak.service`
3. `sudo systemctl status sw360-frontend.service`

### 4.2. Reverse Proxy & SSL Termination

It is recommended to place a reverse proxy (such as **Nginx** or **Apache**) in
front of the application for SSL termination, rather than opening ports 8080
(backend), 8083 (Keycloak), and 3000 (frontend) to the internet directly.

Deploying a reverse proxy unifies the services under a single, secure domain,
routing paths identically to how the container architecture behaves:
- `/` routes upstream to `localhost:3000` (SW360 Frontend)
- `/resource` config and `/authorization` routes upstream to `localhost:8080`
  (SW360 Backend)
- `/kc` routes upstream to `localhost:8083` (Keycloak Administrator & Issuer)

## 5. Troubleshooting & Logging

Depending on your production setup, logs can be found across several directories
or within the `systemd` journal. Check these paths dynamically when debugging
startup connection or interface issues:

- **SW360 Backend (Tomcat):** If running interactively, verify the default
  Tomcat log sink `tail -f /opt/apache-tomcat-11.0.4/logs/catalina.out`. If
  managed by `systemd`, use `journalctl -u tomcat.service -f`.
- **Keycloak:** If configured conventionally by the archive, review application
  errors under `tail -f /opt/keycloak-26.1.3/data/log/server.log`. Alternatively
  utilize `journalctl -u keycloak.service -f`.
- **Frontend / Next.js:** Unless deliberately forwarded to a custom log file or
  managed by PM2, `systemd` commands are the most reliable tracking mechanism:
  `journalctl -u sw360-frontend.service -f`.
