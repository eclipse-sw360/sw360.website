---
linkTitle: "Ubuntu 18.04 and Java 11"
title: "Ubuntu 18.04 LTS, Java 11"
weight: 100
description: 
  Bare metal deployment with Ubuntu 18.04 LTS and Java 11
---

## Introduction

We are covering the update for Ubuntu 18.04 LTS here because it is our main and agreed-upon base system for running SW360. While SW360 may run on a variety of other Linux distributions or operating systems such as macOS, we have agreed to use Ubuntu Long-Term Releases as a reference OS to avoid compatibility issues. The author of this guide also uses macOS with Homebrew, which works fairly well.



Please note that during the time, the dependencies are updated and the version info might change.

## Overview

The installation consists of quite some tasks, as an overview:

5. Java 11
6. Postgresql, if we want to use it instead of hypersonic db
7. CouchDB 2.X at the time of starting this guide, but 3.1.X seems to work well
8. Thrift to 0.13, later updated to 0.14
9. Liferay CE 7.3.3 and 7.3.4 has been also tested
10. Adjust `/etc/ini.d/tomcat` with path of new liferay
13. Adjust `$liferay_install` variable
14. add Java prerequisites to OSGi container
15. Install couchdb-lucene (2.1)
16. Deploy new version of sw360
17. Go ahead with Liferay steps

## Initial steps

In order to "calibrate the system" just run the update / upgrade cycle once:

`# sudo apt update`

`# sudo apt upgrade`

## PostgreSQL

You can go ahead install postgresql 10:

`sudo apt install postgresql-10`

or whatever package version is suitable here, for example version 12 for ubuntu 20.04. 

The configuration for Liferay will come later.

## CouchDB

CouchDB is not part of the Ubuntu package management anymore. Thus, you need to add the Apache CouchDB package repository to install it, first the key for signing:

`curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc | sudo apt-key add -`

The add the repo to the sources:

`echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list`

Then, add its contents to the package database by updating apt:

`sudo apt-get update -y`

Ultimately install CouchDB, we tried with 2.1.2 install:

`sudo apt-get install -y couchdb=2.1.2~bionic`

The installer will ask a couple of questions:

1. Bind address: for CouchDB and SW360 `127.0.0.1` (localhost) is a good bind address, if you would like to access the server from a remote computer because your sw360 runs as a server in the network, you would need to change accordingly.
2. Admin user: For fresh installation for sure a very good idea. You can set the password at sw360 for CouchDB in `couchdb.properties` and place it centrally in `/etc/sw360`

In case you added an admin accidentally and would like to remove it, 

## Thrift

For thrift, we need version 0.13. The installation script in `scripts/install-thrift.sh` will help you:

`sudo ./install-thrift.sh`

In case there is thrift in the package management of the OS you re running on, just make sure, you have version 0.13

## OpenJDK 11 

First check, what is installed.

`# sudo apt list openjdk* --installed`

Then you could check what is available:

`# sudo apt list openjdk*`

And install OpenJDK 11

`# sudo apt install openjdk-11-jdk`

Then the `$JAVA_HOME` needs to be updated, most likely in `/etc/environment`. Please check for your installation how to set the `$JAVA_HOME` correctly (most likely: `JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64`).

## Liferay CE 7.3.3

Download Liferay from this link

https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.3.3%20GA4/liferay-ce-portal-tomcat-7.3.3-ga4-20200701015330959.tar.gz

and unpack it, ideally in the `/opt` directory, so resulting path would look like `/opt/liferay-ce-portal-7.3.3-ga4`.

Then, you need to update the `$LIFERAY_INSTALL` in `/etc/environment` from `LIFERAY_INSTALL=/opt/liferay-portal-7.2.0-ga1/
` to `LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.3-ga4.

### Auto Start

For auto start, you need an according init.d entry. It could be a file like `/etc/init.d/tomcat`. The file could be created if not there already, with the following contents:

```
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

Te user `siemagrant` is used in the sw360vagrant project. it is the username of the user where the liefray / sw360 server should run under. In the ideal case, it is unprivileged user.

### Adjust Memory

When you have downloaded the liferay distribution, Tomcat is likely configured with very basic memory settings. For trying sw360, the standard memory settings are OK. But of course, the memory settings in `$LIFERAY_HOME/tomcat-X.0.XX/bin/setenv.sh` should be adapted again.

### PostgreSQL instead of Hypersonic

Liferay CE comes with the hypersonic database. Just for making a long-term setup in the berginning, we are advising to use postgresql from the start. The settings for postgrsql can be found in `portal-ext.properties`. Please do not forget to create the user and the database in the database server first. 

## Install Prerequisites

There are some install libraries to be downloaded and installed as OSGi modules. You can check the download script from the sw360vaghrant project for list of URLs that help you.

https://github.com/sw360/sw360vagrant/blob/master/download-packages.sh

An URL for libtrift is:

https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.13.0/libthrift-0.13.0.jar

An URL for commons-compress is:

https://repo1.maven.org/maven2/org/apache/commons/commons-compress/1.20/commons-compress-1.20.jar

If you have downloaded every thing, copy them to the `deploy` folder of your liferay installation:

```
# cp libthrift-0.13.0.jar $LIFEARY_HOME/deploy/
# cp commons-lang-2.4.jar $LIFERAY_HOME/deploy
# cp commons-io-2.6.jar $LIFERAY_HOME/deploy
# cp commons-csv-1.4.jar $LIFERAY_HOME/deploy
# cp commons-collections4-4.4.jar $LIFERAY_HOME/deploy
# cp commons-codec-1.12.jar $LIFERAY_HOME/deploy
# cp commons-compress-1.20.jar $LIFERAY_HOME/deploy
# cp commons-logging-1.2.jar $LIFERAY_HOME/deploy
# cp gson-2.8.5.jar $LIFERAY_HOME/deploy
# cp guava-21.0.jar $LIFERAY_HOME/deploy
# cp jackson-annotations-2.11.3.jar $LIFERAY_HOME/deploy
# cp jackson-core-2.11.3.jar $LIFERAY_HOME/deploy
# cp jackson-databind-2.11.3.jar $LIFERAY_HOME/deploy
```

if you use PostgreSQL as your database, you need to install  postgres.jar in Liferay. 

```
# wget https://jdbc.postgresql.org/download/postgresql-42.2.9.jar postgresql-42.2.9.jar
# cp postgresql-42.2.9.jar $LIFERAY_HOME/tomcat-9.0.33/lib/ext
```

[Note] In case you use other database with Liferay, you need to set other jar file of corresponding database.

## Install Couchdb Lucene

SW360 uses for searching the contents of the couchdb databases a lucene-based server named couchdb-lucene. The main issue here is that it requires a patch for the use in the normal SW3360 setups. The reason for the patch is that the developers presume that couchdb-lucene runs as the only component in the application server, while in the sw360 setup, there is a setup in which couchdb-lucene runs along with other components in the same application container.

Start with downloading the couchdb-lucene and rename the archive so the resulting URL path element will be `couchdb-lucene`:

`# wget https://github.com/rnewson/couchdb-lucene/archive/v2.1.0.tar.gz ./couchdb-lucene.tar.gz`

Please refer to the script in sw360vagrant how to apply the patch to couchdb-lucene:

https://github.com/sw360/sw360vagrant/blob/master/shared/scripts/install-lucene.sh

Please note that the patching issue is well known in the project and it is unclear why it is not merged:

* https://github.com/rnewson/couchdb-lucene/issues/161 "allow context-root other than "/" when running in servlet container"
* https://github.com/rnewson/couchdb-lucene/pull/162
* https://github.com/rnewson/couchdb-lucene/pull/152

## Deploy New SW360

You will need to checkout new Java-11 based version of the SW360, which is either tagged version 11 (or later) or some few commits before that. Then build in the sw360 project root using:

`mvn clean install -DskipTests`

This will install new artfacts, such as lib-datahandler in your maven repostiory. Then apply in the same directory:

```
# mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -DskipTests
```

Skipping tests has the reason that usually, the sw360 is tested in the CI and thus, local tests are note necessary, if the code has not been changed locally. Note that the REST API documentation framework is based on building test cases and thus for deploying a version with REST API documentation, tests should be executed:

```
# cd rest
# mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/
```

## Final Steps in Liferay

Liferay CE 7.3 will need to have some manual steps applied in order to complete the setup. Unfortunately, these cannot be automated (if you know how, please let us know). For earlier versions of Liferay, please refer to the main wiki page. For Liferay CE 7.3.3 please continue here:

https://github.com/eclipse/sw360/wiki/Deploy-Liferay7.3

