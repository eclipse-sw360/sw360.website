---
linkTitle: "Version 19.x on Debian 12"
title: "Version 19.x on Debian 12"
weight: 101
description: Bare metal deployment with Debian based Linux for SW360 v19.x
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
* CouchDB >= 3.4.x
* Thrift 0.20.0
* NodeJS >= 20.x
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

To install Apache Thrift using the helper script in the SW360 project, run the install-thrift.sh script located in `third-party/thrift/install-thrift.sh`: [here](https://github.com/eclipse-sw360/sw360/blob/d7869d252c4b4c84e6ee389cbed44543cd37f7ac/third-party/thrift/install-thrift.sh)

```bash
sudo ./scripts/install-thrift.sh
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

Get the latest version of Apache Tomcat 11 from https://tomcat.apache.org/download-11.cgi
and install it in `/opt`

```shell
curl -L 'https://dlcdn.apache.org/tomcat/tomcat-11/v11.0.4/bin/apache-tomcat-11.0.4.tar.gz' -o ~/Downloads/tomcat-11.0.4.tar.gz
sudo tar -xzvf ~/Downloads/tomcat-11.0.4.tar.gz -C /opt
sudo chown -R $USER:$USER /opt/apache-tomcat-11.0.4/
```

### 1.6. Install KeyCloak (optional)

You can configure KeyCloak with SW360 for IAM. SW360 on its own can do
authentication and authorization, but for corporate setup, you might want to
offload to KeyCloak. Thus, this step is optional.

Get the latest 26.x.x version from https://www.keycloak.org/downloads

```shell
curl -L 'https://github.com/keycloak/keycloak/releases/download/26.1.3/keycloak-26.1.3.tar.gz' -o ~/Downloads/keycloak-26.1.3.tar.gz
sudo tar -xzvf ~/Downloads/keycloak-26.1.3.tar.gz -C /opt
sudo chown -R $USER:$USER /opt/keycloak-26.1.3/
```

Install PostgreSQL used by KeyCloak for management.

```bash
sudo apt install postgresql
```

or whatever package version is suitable here, for example version 15 for Debian 12.

Follow the [Keycloak based authentication](../Deploy-Keycloak-Authentication.md)
guide to set up KeyCloak for SW360 after the installation from 1.8 is done.

### 1.7. Clone and build sw360 version 19.x

* Clone sw360 source code to folder
    - `$ git clone https://github.com/eclipse-sw360/sw360.git`
* Create config properties
    - `$ sudo mkdir -p /etc/sw360 /etc/sw360/autorization /etc/sw360/rest`
    - Find the relevant configurations at [Configurable Property Keys](../Deploy-Configuration-Files.md)
* Compile and install the application
    - `$ mvn clean install -Dbase.deploy.dir=/opt/apache-tomcat-11.0.4/ -Dlistener.deploy.dir=/opt/keycloak-26.1.3/providers -P deploy`

This will install the jar and war files at appropriate locations.

### 1.8. Start backend service

* Start tomcat server
    - `$ /opt/apache-tomcat-11.0.4/bin/startup.sh`
* Check tomcat logs
    - `$ tail -f100 /opt/apache-tomcat-11.0.4/logs/catalina.out`

Once you see message like
`org.apache.catalina.startup.Catalina.start Server startup in [**] milliseconds`
in the logs, the backend is up and can load the OpenAPI docs at
[http://localhost:8080/resource/v3/api-docs](http://localhost:8080/resource/v3/api-docs)

The backend install SwaggerUI as well and accessible via
[http://localhost:8080/resource/swagger-ui/index.html](http://localhost:8080/resource/swagger-ui/index.html)

## 2. Installing frontend services

Since version 19, SW360 has separated the front-end as a React based project.
It is hosted at https://github.com/eclipse-sw360/sw360-frontend/ and needs to be
installed as well.

### 2.1. Install node 20

First we need to install Node and NPM version 20 or above. Setting nvm is the
easiest and fastest way to do it for your user. Follow the guide from
https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating

```shell
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 20
```

### 2.2. Install pnpm

pnpm is an advanced package manager for node dependencies and can be installed
with the new npm installed above.

```shell
npm install -g pnpm@latest-10
```

### 2.3. Clone and install frontend

* Clone sw360 source code to folder
    - `$ git clone https://github.com/eclipse-sw360/sw360-frontend.git`
* Setup `.env` file
    - ```ini
      NEXTAUTH_SECRET='secret'
      NEXT_PUBLIC_SW360_API_URL='http://localhost:8080'
      NEXTAUTH_URL='http://localhost:3000'
      # possible values are sw360basic, sw360oauth, keycloak
      NEXT_PUBLIC_SW360_AUTH_PROVIDER='sw360basic'

      # Enable if using KeyCloak
      #SW360_KEYCLOAK_CLIENT_ID='client-from-kc'
      #SW360_KEYCLOAK_CLIENT_SECRET='secret-from-kc'
      #AUTH_ISSUER='http://localhost:8083/realms/sw360'
      #NEXT_PUBLIC_SW360_AUTH_PROVIDER='keycloak'
      ```
* Install dependencies and build pages
    - ```shell
      $ pnpm install
      $ pnpm build
      ```
* Start the server and visit [http://localhost:3000](http://localhost:3000)
    - `$ pnpm start`
