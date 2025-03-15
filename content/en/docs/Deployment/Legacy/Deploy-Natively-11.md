---
linkTitle: "Ubuntu 18.04 and Java 11"
title: "Ubuntu 18.04 LTS, Java 11"
weight: 100
description: 
  Bare metal deployment with Ubuntu 18.04 LTS and Java 11
---

## Introduction

We are covering the update for Ubuntu 18.04 LTS here, because that is our main / agreed base system for running SW360. SW360 may run on a variety of other Linux distributions or OSes such as macOS, but in order to avoid problems we agreed on having a reference OS, which are the Ubuntu long term releases. The author of this guide also uses macOS and Homebrew which also works fairly well.

Please note that during the time, the dependencies are updated and the version info might change.

## Overview

The installation consists of quite some tasks, as an overview:

1. Java 11
2. PostgreSQL, if we want to use it instead of HyperSQL DB
3. CouchDB (version 3.1.X is recommended and works well)
4. Thrift 0.14
5. Liferay CE 7.3.3 or 7.3.4 (both tested)
6. Adjust `/etc/init.d/tomcat` with path of new Liferay
7. Adjust `$LIFERAY_INSTALL` variable
8. Add Java prerequisites to OSGi container
9. Install couchdb-lucene (2.1)
10. Deploy new version of SW360
11. Go ahead with Liferay steps

## Initial steps

In order to "calibrate the system" just run the update / upgrade cycle once:

```bash
sudo apt update
sudo apt upgrade
```

## PostgreSQL

You can go ahead and install PostgreSQL 10:

```bash
sudo apt install postgresql-10
```

or whatever package version is suitable here, for example version 12 for Ubuntu 20.04. 

The configuration for Liferay will come later.

## CouchDB

CouchDB is not part of the Ubuntu package management anymore. Thus, you need to add the Apache CouchDB package repository to install it, first the key for signing:

```bash
curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc | sudo apt-key add -
```

Then add the repo to the sources:

```bash
echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list
```

Then, add its contents to the package database by updating apt:

```bash
sudo apt-get update -y
```

Install CouchDB (we recommend version 3.1.X, though 2.1.2 has been tested as well):

```bash
sudo apt-get install -y couchdb=2.1.2~bionic
```

The installer will ask a couple of questions:

1. Bind address: for CouchDB and SW360 `127.0.0.1` (localhost) is a good bind address. If you would like to access the server from a remote computer because your SW360 runs as a server in the network, you would need to change accordingly.
2. Admin user: For fresh installation, it's a very good idea to set an admin user. You can set the password for CouchDB in `couchdb.properties` and place it centrally in `/etc/sw360`

## Thrift

For Thrift, we need version 0.14. The installation script in `scripts/install-thrift.sh` will help you:

```bash
sudo ./install-thrift.sh
```

In case there is Thrift in the package management of the OS you're running on, just make sure you have version 0.14.

## OpenJDK 11 

First check what is installed:

```bash
sudo apt list openjdk* --installed
```

Then you could check what is available:

```bash
sudo apt list openjdk*
```

And install OpenJDK 11:

```bash
sudo apt install openjdk-11-jdk
```

Then the `$JAVA_HOME` needs to be updated, most likely in `/etc/environment`. Please check for your installation how to set the `$JAVA_HOME` correctly (most likely: `JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64`).

## Liferay CE 7.3.3

Download Liferay from this link:

https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.3.3%20GA4/liferay-ce-portal-tomcat-7.3.3-ga4-20200701015330959.tar.gz

and unpack it, ideally in the `/opt` directory, so resulting path would look like `/opt/liferay-ce-portal-7.3.3-ga4`.

Then, you need to update the `$LIFERAY_INSTALL` in `/etc/environment` from `LIFERAY_INSTALL=/opt/liferay-portal-7.2.0-ga1/` to `LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.3-ga4`.

### Auto Start

For auto start, you need an according init.d entry. It could be a file like `/etc/init.d/tomcat`. The file could be created if not there already, with the following contents:

```bash
#!/bin/bash

### BEGIN INIT INFO
# Provides:        tomcat7
# Required-Start:  $network
# Required-Stop:   $network
# Default-Start:   2 3 4 5
# Default-Stop:    0 1 6
# Short-Description: Start/Stop Tomcat server
### END INIT INFO

PATH=/sbin:/bin:/usr/sbin:/usr/bin

start() {
 su -l siemagrant -c /opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/bin/startup.sh
}

stop() {
 su -l siemagrant -c /opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/bin/shutdown.sh
}

case $1 in
  start|stop) $1;;
  restart) stop; start;;
  *) echo "Run as $0 <start|stop|restart>"; exit 1;;
esac
```

The user `siemagrant` is used in the sw360vagrant project. It is the username of the user where the Liferay / SW360 server should run under. In the ideal case, it is an unprivileged user.

### Adjust Memory

When you have downloaded the Liferay distribution, Tomcat is likely configured with very basic memory settings. For trying SW360, the standard memory settings are OK. But of course, the memory settings in `$LIFERAY_HOME/tomcat-9.0.33/bin/setenv.sh` should be adapted again.

### PostgreSQL instead of HyperSQL

Liferay CE comes with the HyperSQL database. Just for making a long-term setup from the beginning, we are advising to use PostgreSQL from the start. The settings for PostgreSQL can be found in `portal-ext.properties`. Please do not forget to create the user and the database in the database server first. 

## Install Prerequisites

There are some install libraries to be downloaded and installed as OSGi modules. You can check the download script from the sw360vagrant project for list of URLs that help you:

https://github.com/sw360/sw360vagrant/blob/master/download-packages.sh

An URL for libthrift is:

https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.14.0/libthrift-0.14.0.jar

An URL for commons-compress is:

https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.20/commons-compress-1.20.jar

If you have downloaded everything, copy them to the `deploy` folder of your Liferay installation:

```bash
cp libthrift-0.14.0.jar $LIFERAY_HOME/deploy/
cp commons-lang-2.4.jar $LIFERAY_HOME/deploy
cp commons-io-2.6.jar $LIFERAY_HOME/deploy
cp commons-csv-1.4.jar $LIFERAY_HOME/deploy
cp commons-collections4-4.4.jar $LIFERAY_HOME/deploy
cp commons-codec-1.12.jar $LIFERAY_HOME/deploy
cp commons-compress-1.20.jar $LIFERAY_HOME/deploy
cp commons-logging-1.2.jar $LIFERAY_HOME/deploy
cp gson-2.8.5.jar $LIFERAY_HOME/deploy
cp guava-21.0.jar $LIFERAY_HOME/deploy
cp jackson-annotations-2.11.3.jar $LIFERAY_HOME/deploy
cp jackson-core-2.11.3.jar $LIFERAY_HOME/deploy
cp jackson-databind-2.11.3.jar $LIFERAY_HOME/deploy
```

If you use PostgreSQL as your database, you need to install postgres.jar in Liferay: 

```bash
wget https://jdbc.postgresql.org/download/postgresql-42.2.9.jar
cp postgresql-42.2.9.jar $LIFERAY_HOME/tomcat-9.0.33/lib/ext
```

[Note] In case you use another database with Liferay, you need to set the appropriate jar file of the corresponding database.

## Install CouchDB Lucene

SW360 uses a Lucene-based server named couchdb-lucene for searching the contents of the CouchDB databases. The main issue here is that it requires a patch for use in normal SW360 setups. The reason for the patch is that the developers presume that couchdb-lucene runs as the only component in the application server, while in the SW360 setup, couchdb-lucene runs along with other components in the same application container.

Start with downloading the couchdb-lucene and rename the archive so the resulting URL path element will be `couchdb-lucene`:

```bash
wget https://github.com/rnewson/couchdb-lucene/archive/v2.1.0.tar.gz -O couchdb-lucene.tar.gz
```

Please refer to the script in sw360vagrant on how to apply the patch to couchdb-lucene:

https://github.com/sw360/sw360vagrant/blob/master/shared/scripts/install-lucene.sh

Please note that the patching issue is well known in the project and it is unclear why it is not merged:

* https://github.com/rnewson/couchdb-lucene/issues/161 "allow context-root other than "/" when running in servlet container"
* https://github.com/rnewson/couchdb-lucene/pull/162
* https://github.com/rnewson/couchdb-lucene/pull/152

## Deploy New SW360

You will need to checkout the new Java-11 based version of SW360, which is either tagged version 11 (or later) or some few commits before that. Then build in the SW360 project root using:

```bash
mvn clean install -DskipTests
```

This will install new artifacts, such as lib-datahandler in your Maven repository. Then apply in the same directory:

```bash
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -DskipTests
```

Skipping tests is done because usually, SW360 is tested in the CI and thus, local tests are not necessary if the code has not been changed locally. Note that the REST API documentation framework is based on building test cases and thus for deploying a version with REST API documentation, tests should be executed:

```bash
cd rest
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/
```

## Final Steps in Liferay

Liferay CE 7.3 will need to have some manual steps applied in order to complete the setup. Unfortunately, these cannot be automated (if you know how, please let us know). For earlier versions of Liferay, please refer to the main wiki page. For Liferay CE 7.3.3 please continue here:

https://github.com/eclipse/sw360/wiki/Deploy-Liferay7.3