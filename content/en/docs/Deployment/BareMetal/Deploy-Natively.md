---
linkTitle: "Ubuntu 22.04 / Debian 11"
title: "Ubuntu 22.04 / Debian 11"
weight: 100
description: Bare metal deployment with Debian based Linux
---

## Introduction

We are covering the update for Debian based Linux distros, because that is our main / agreed base system for running sw360. sw360 may run on a varienty of other linux distributions or OSes such as Mac OSX (amd64 only).

## Requirements

The installation consists of quite some tasks, as an overview:

* Java 11
* Postgresql >= 15.x
* CouchDB >= 3.2.x
* Thrift 0.18.1
* Liferay CE 7.4.3 GA18

## Initial steps

In order to "calibrate the system" just run the update / upgrade cycle once:

```shell
sudo apt update
sudo apt upgrade
```

## PostgreSQL

You can go ahead install postgresql:

```bash
sudo apt install postgresql
```

or whatever package version is suitable here, for example version 12 for ubuntu 20.04. 

The configuration for Liferay will come later.

## CouchDB

CouchDB is not part of the Ubuntu package management anymore. Thus, you need to add the Apache CouchDB package repository to install it, first the key for signing:

```shell
apt install curl gpg
curl https://couchdb.apache.org/repo/keys.asc | sudo gpg –dearmor -o /etc/apt/trusted.gpg.d/couchdb-archive-keyring.gpg
echo “deb https://apache.jfrog.io/artifactory/couchdb-deb/ $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main” | sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null
sudo apt-get update -y
sudo apt-get install -y couchdb
```

The installer will ask a couple of questions:

1. Bind address: for CouchDB and SW360 `127.0.0.1` (localhost) is a good bind address, if you would like to access the server from a remote computer because your sw360 runs as a server in the network, you would need to change accordingly.
2. Unless you know what you are doing, use standalone install intead of clustered option, for a regular single instalation.
3. Admin user: For fresh installation for sure a very good idea. You can set the password at sw360 for CouchDB in `couchdb.properties` and place it centrally in `/etc/sw360`

In case you added an admin accidentally and would like to remove it, 

## Thrift

For thrift, the helper install script is located on sw360 `scripts/install-thrift.sh`:

```bash
sudo ./install-thrift.sh
```

In case there is thrift in the package management of the OS you re running on, just make sure, you have version 0.16

## Java 11

If you do not have installed java 11 yet on your setup:

```shell
curl https://packages.adoptium.net/artifactory/api/gpg/key/public | sudo tee /etc/apt/trusted.gpg.d/apache-temurin.gpg >/dev/null
echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | sudo tee /etc/apt/sources.list.d/adoptium.gpg
```

## Dependencies

Use the included script located in:
```bash
./scripts/download_dependencies.sh
```

Required dependencies will be downloaded on the deps folder.

For liferay, unpack it, ideally in the `/opt` directory.

## Install Couchdb Lucene

SW360 uses for searching the contents of the couchdb databases a lucene-based server named couchdb-lucene. The main issue here is that it requires a patch for the use in the normal SW3360 setups. The reason for the patch is that the developers presume that couchdb-lucene runs as the only component in the application server, while in the sw360 setup, there is a setup in which couchdb-lucene runs along with other components in the same application container.

For build the custom CLucene jar:

```shell
#!/bin/bash

CLUCENE_VERSION=2.1.0
mkdir /tmp/build
curl -JL https://github.com/rnewson/couchdb-lucene/archive/v"$CLUCENE_VERSION".tar.gz | tar -C /tmp/build -xz --strip-components=1
cp ./scripts/patches/couchdb-lucene.patch /tmp/build
cp ./scripts/docker/couchdb-lucene.ini /tmp/build/src/main/resources/couchdb-lucene.ini 
cd /tmp/build || exit 1
patch -p1 < couchdb-lucene.patch \
mvn -X install war:war \

## Deploy New SW360

Build with:

```bash
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.4.3-ga18/deploy/ \
  -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.4.3-ga18/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.4.18-ga4/tomcat-9.0.33/webapps/ -DskipTests
```

Skipping tests has the reason that usually, the sw360 is tested in the CI and thus, local tests are note necessary, if the code has not been changed locally. Note that the REST API documentation framework is based on building test cases and thus for deploying a version with REST API documentation, tests should be executed:

```bash
cd rest
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.4.3-ga18/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.4.3-ga18/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/
```

## Final Steps in Liferay

Liferay CE 7.3 will need to have some manual steps applied in order to complete the setup. Unfortunately, these cannot be automated (if you know how, please let us know). For earlier versions of Liferay, please refer to the main wiki page. 

This is the legacy guide for Liferay CE 7.3.3 but is valid for current 7.4.3 deployment:

https://www.eclipse.org/sw360/docs/deployment/legacy/deploy-liferay7.3/

