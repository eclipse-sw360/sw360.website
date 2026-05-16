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

## 3. Authentication Configuration (Bare-Metal)

This guide keeps only deployment-side configuration values. Security policy,
provider choice, API keys, credential generation, and rotation are centralized
in the Administration Guide:

**[Securing SW360 (Administration Guide)](../../AdministrationGuide/Securing-SW360.md)**

For bare-metal deployments, these are the key configuration surfaces:

- Frontend provider and client settings in `sw360-frontend/.env`
- Backend JWT issuer trust and HTTP-basic toggle in `/etc/sw360/rest/application.yml`
- Authorization server keystore password in `/etc/sw360/authorization/application.yml`

For full property details, see:

- [SW360 Configuration Technical Reference](../Deploy-Configuration-Files.md)

## 4. Recommended for Production

For robust deployment in a true production environment, it is highly
recommended to adapt the application stack from a manual layout to a
service-based architecture guarded by a reverse proxy.

### 4.0. Security Hardening

For production hardening choices (disable Basic auth, OAuth/Keycloak strategy,
API keys, secret generation, and rotation), use the dedicated guide:

**[Securing SW360 (Administration Guide)](../../AdministrationGuide/Securing-SW360.md)**

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
After=syslog.target network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple

# Environment variables
Environment="JAVA_HOME=/path/to/jdk-home"
Environment="KC_TRANSACTION_XA_ENABLED=true"
Environment="QUARKUS_TRANSACTION_MANAGER_ENABLE_RECOVERY=true"

# Bootstrap admin credentials (KEYCLOAK_BOOTSTRAP_ADMIN_USERNAME/_PASSWORD)
# and KC_DB_PASSWORD are loaded from this file. See "Loading secrets via
# EnvironmentFile" below for the one-time setup.
EnvironmentFile=-/etc/keycloak/keycloak.env

# Rebuild the optimized server image whenever conf changes; cheap when up-to-date.
ExecStartPre=/path/to/keycloak-home/bin/kc.sh build
# `start --optimized` skips rebuild on boot and refuses to start if conf
# changed without a prior build. Suitable for staging/production. Use
# `start-dev` only for local experiments.
ExecStart=/path/to/keycloak-home/bin/kc.sh start --optimized

# User and group
User=non-privileged-user
Group=non-privileged-group

# Restart on failure
Restart=on-failure
TimeoutStopSec=60
LimitNOFILE=65536

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

#### Loading secrets via `EnvironmentFile`

Keep credentials such as the Keycloak bootstrap admin password and the
PostgreSQL password out of `keycloak.conf` and out of unit files (which are
world-readable by default). Use a dedicated environment file owned by the
service user and referenced from the unit via `EnvironmentFile=`.

Create the file once with restrictive permissions:

```shell
sudo install -o <service-user> -g <service-group> -m 0600 /dev/null /etc/keycloak/keycloak.env
sudoedit /etc/keycloak/keycloak.env
```

Populate it with the secrets Keycloak expects on the environment (no quotes
around values, one per line):

```ini
KEYCLOAK_BOOTSTRAP_ADMIN_USERNAME=admin
KEYCLOAK_BOOTSTRAP_ADMIN_PASSWORD=<strong-password>
KC_DB_PASSWORD=<db-password>
```

Notes:
- `KEYCLOAK_BOOTSTRAP_ADMIN_USERNAME`/`_PASSWORD` are honoured only on first
  start (or until an admin user exists in the database). Rotate via the admin
  console after the initial run.
- `KC_DB_PASSWORD` overrides `db-password` from `keycloak.conf`, so the conf
  file no longer needs to carry the password in plaintext.
- The same `EnvironmentFile=` pattern can be used for `tomcat.service`
  whenever Tomcat needs secrets (e.g. external integration tokens) — define
  them in a similarly locked-down env file and reference it from the unit.

After editing the env file, restart the service to pick up the new values:

```shell
sudo systemctl restart keycloak.service
```

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
