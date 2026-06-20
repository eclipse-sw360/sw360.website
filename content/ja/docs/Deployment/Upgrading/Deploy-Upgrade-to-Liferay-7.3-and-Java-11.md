---
linkTitle: "Liferay 7.3 and Java 11"
title: "Liferay 7.3 and Java 11"
weight: 100
description: 
  Upgrading previous sw360 instances to Liferay 7.3.x and Java 11
---


## Introduction

We are covering the update for ubuntu here, because that is our main / agreed base system for running sw360. sw360 may run on a varienty of other linux distributions or OSes such as macosx, but in order to avoid problem we agreed on having a reference OS, which are the ubuntu long term releases.

With the update to Java 11, we upgraded from Ubuntu 16.04 to Ubuntu 18.04, both LTS version. This OS is used for example by the https://github.com/sw360/sw360vagrant project.

So the update covers the following:

| orign  | target  |
|---|---|
| Ubuntu 16.04 LTS  | Ubuntu 18.04 LTS  |
| CoucbdDB 1.X (comes with Ubuntu)  | CouchDB 2.X (not with Ubuntu anymore) |
| Postgresql 9.X (comes with Ubuntu)  | Postgresql 10.X  (comes with Ubuntu)  |
| OpenJDK 8 (comes with Ubuntu) | openJDK 11 (comes with Ubuntu) |
| Apache Thrift 0.11/0.12 | Apache Thrift 0.13 |

## Overview

The upgrade consists of quite some tasks, as an overview:

1. Make a backup
2. Execute sw360 migration scripts
3. Linux release upgrade
5. Java 11
6. Postgresql
7. CouchDB 2.X
8. Thrift to 0.13
9. Liferay ce 7.3.3
10. Copy your existing `portal-ext.properties` to now liferay_install location
11. copy from old liferay installation the `data/document_library` to the new liferay
12. Adjust `/etc/ini.d/tomcat` with path of new liferay
13. Adjust `$liferay_install` variable
14. add Java prerequisites to OSGi container
15. Update couchdb-lucene
16. Deploy new version of sw360
17. Adjust Liferay

## Initial steps

In order to "calibrate the system" just run the update / upgrade cycle once:

`# sudo apt update`

`# sudo apt upgrade`

### Keeping More Settings Files

**apache.conf:** Keep also the mod security conf files that are asked to update during installation

**sshd:** Changes on the ssh / sshd conf files should be kept in case you have setup up dome remote public private key login (usually the case for server installation). Otherwise you re locked out maybe.

**Maven:** if you change Maven, for example with your proxy settings, keep it too.

In general, whenever there is functionality you need, consider keeping existing settings files.

## Ubuntu Release Upgrade

There is maybe the remark to overwrite the current apache configuration. We propose to keep the currently installed apache files.

`# sudo do-release-upgrade`

Answer "yes" for the download of packages and also confirm the update of the glibc, of course. Update the `system.conf`(install maintainer's version), depending on if you actually edited this. Some for `sysctl.conf`.

## Migration of PostgreSQL

The existing 9.5 will not be upgraded, instead this message comes: After the release upgrade, you can check again if postgresql is installed:

`sudo apt list postgre* --installed`

Postgresql 9.5 should be the only installed. The old postgresql 9.5 must stay in fact, because the migration tool needs to be executing on a running postgresql 9.5 instance. Just having popstgresql 10 and a database only from postgresql 9.5 will not work. You can go ahead install postgresql 10:

`sudo apt install postgresql-10`

Then, apply the instruction to update from 9.5 to 10.0 from this page: https://stackoverflow.com/questions/47029055/how-do-i-upgrade-my-postgresql-9-5-to-postgresql-10-on-ubuntu-16-04

```
# service postgresql stop
...
# pg_dropcluster --stop 10 main
...
# pg_upgradecluster -m upgrade 9.5 main
...
# pg_dropcluster 9.5 main --stop
...
# apt-get autoremove --purge postgresql-9.5 
...
# service postgresql start
```
(note that # means you need to be root or execute with sudo)

## Migration of CouchDB

CouchDB is not part of the Ubuntu package management anymore. Thus, you need to add the Apache CouchDb package repository to install it, first the key for signing:

`curl -L https://couchdb.apache.org/repo/bintray-pubkey.asc | sudo apt-key add -`

The add the repo to the sources:

`echo "deb https://apache.bintray.com/couchdb-deb bionic main" | sudo tee -a /etc/apt/sources.list`

Then, add its contents to the package database by updating apt:

`sudo apt-get update -y`

Ultimately install CouchDB, we tried with 2.1.2 initiall not to make a too far jump from 1.X, later versions may work as well. Note that for upgrading to CouchDB 3.X you would need an upgrade to 2.X first.

`sudo apt-get install -y couchdb=2.1.2~bionic`

The installer will ask a couple of questions:

1. Bind address: for CouchDB and SW360 `127.0.0.1` (localhost) is a good bind address, if you would like to access the server from a remote computer because your sw360 runs as a server in the network, you would need to change accordingly.
2. Admin user: **Warning** The couchdb migration utility does not support authentication! Please do not enter an admin password, but apply it later. You can set the password for CouchDB in `couchdb.properties` and place it centrally in `/etc/sw360`
3. Migration: yes you need to use `couchup` for migrating the databases

In case you added an admin and need to remove it, try:

`curl -X DELETE http://admin:password@127.0.0.1:5984/_config/admins/admin`

where the two occurrences `admin` is the name of the admin user in the URL, whatever the user was called.

### Migration of CouchDB Databases

As a preparation: the CouchDB migration works by copying the databases, so the file system needs at least as much free space as the CouchDB databases use.

CouchDB offers a migration utility. It is advised that you remove all test databases as they do not seem to work with the migration utility. Important links are:

* https://docs.couchdb.org/en/2.3.1/install/upgrading.html
* https://github.com/apache/couchdb/pull/483

For some reason after installation, the `couchup`utility is not part of the path, so execute:

`/opt/couchdb/bin/couchup list`

It lists all DBs found. The go ahead with:

`/opt/couchdb/bin/couchup replicate -a`

It should replicate all databases in `/var/lib/couchdb`. Please refer to the couchup documentation, for the subsequent steps. A few remarks from our experience:

1. The rebuold of the couchdb does not work for our test databases. Please refer to the documentation how to do this manually if you like.
2. The couchup utility crashes for large DB sizes with a time out error. Consider using the timeout option: `/opt/couchdb/bin/couchup replicate -a --timeout==10000` (with almost infinite timeout here)
3. On very large attachment database sizes (500GB), the couchdb configuration must be changed. We increased almost every related value by factor 10 (timeouts, memory, etc) in `/opt/couchdb/etc/default.ini` and good success with this.

## Update Thrift

For thrift, we need version 0.13. The installation script `scripts/install-thrift.sh`allows for uninstalling old versions:

`sudo ./install-thrift.sh --uninstall`

and then install 

`sudo ./install-thrift.sh`

## From OpenJDK 8 to OpenJDK 11

First check, what is installed.

`# sudo apt list openjdk* --installed`

Then you could check what is available:

`# sudo apt list openjdk*`

It should be that OpenJDK 8 is installed and both OpenJDK 8 and 11 are available. Then, remove the OpenJDK 8 and install 11:

```
sudo apt remove openjdk-8-jdk
sudo apt remove openjdk-8-jre
sudo apt remove openjdk-8-jdk-headless
sudo apt remove openjdk-8-jre-headless
```

check if nothing is installed:

`# sudo apt list openjdk* --installed`

Then install the openjdk-11-jdk:

`# sudo apt install openjdk-11-jdk`

Then the `$JAVA_HOME` needs to be updated, most likely it is defined in `/etc/environment`. Please check for your installation how to set the `$JAVA_HOME` correctly.

## Updating Liferay

Download Liferay from this link

https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.3.3%20GA4/liferay-ce-portal-tomcat-7.3.3-ga4-20200701015330959.tar.gz

and unpack it, ideally in the `/opt` directory, so resulting path would look like `liferay-ce-portal-7.3.3-ga4`.

Then, you need to update the `$LIFERAY_INSTALL` in `/etc/environment` from `LIFERAY_INSTALL=/opt/liferay-portal-7.2.0-ga1/
` to `LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.3-ga4`.

First, you will need to copy the `portal-ext.properties` from the old liferay folder to the new liferay folder (or new `$LIFERAY_HOME`):

`# cp /$old-liferay/portal-ext.properties $LIFERAY_INSTALL/portal-ext.properties`

### Migration of existing database

For a version upgrade from Liferay CE 7.2 to Liferay 7.3, migration scripts must be applied, they are located in `$LIFERAY_HOME/
tools/portal-tools-db-upgrade-client`. From there the following files needs to be adapted:

* `app-server.properties`: most likely uncomment tomcat, because we re using liferay with tomcat.
* `portal-upgrade-database.properties`: uncomment postgresql section and add database user, default from installation is `liferay/liferay`, or it is stored in `portal-ext.properties` right where the JDBC driver is selected. Please note that your `portal-ext.properties` file in `$LIFERAY_INSTALL`can have the following line `include-and-override=/etc/sw360/portal-ext.properties`. In this case, consider the `portal-ext.properties`at that location.
* `portal-upgrade-ext.properties`: just the liferay home, you can leave it as it is

If everything is done (and the postgresql migration took place), execute:

`# ./db_upgrade.sh`

It should return a battery of `INFO` log level messages end with:

```
Completed Liferay core upgrade process in 96 seconds
Checking to see if all upgrades have completed... done.
```

### More Migration

The liferay migration covers apparently only the database, but not the files in the `$LIFERAY_HOME/data` folder. It would have been nicer, if that would have been covered too. Instead these must be copied manually. In fact, for the migration, it is advised to copy only the `/old-liferay/data/document_library` to the new location. Something like (different pwd ...):

`# cp -r _attic/liferay-portal-7.2.1-ga2/data/document_library/ liferay-ce-portal-7.3.3-ga4/data/`

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

Te user `siemagrant` is used in the sw360vagrant project. it is the username of the user where the liefray / sw360 server runs under in vagrant. Regardless how the user is named, it is important that liferay runs under an unprivileged user (for security reasons).

### Adjust Memory

When you have downloaded the liferay distribution, Tomcat is likely configured with very basic memory settings. For trying sw360, the standard memory settings are OK. But of course, the memory settings in `$LIFERAY_HOME/tomcat-X.0.XX/bin/setenv.sh` should be adapted again.

## Install Prerequisites

For old installations, libthrift is not there (which causes an error at container startup), it should be downloaded and deployed:

```
wget https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.13.0/libthrift-0.13.0.jar
mv libthrift-0.13.0.jar $LIFEARY_HOME/deploy/
```

The the existing prerequisites needs to be copied from the `osgi/modules` from the old liferay installation:

```
cp commons-lang-2.4.jar $LIFERAY_HOME/deploy
cp commons-io-2.6.jar $LIFERAY_HOME/deploy
cp commons-csv-1.4.jar $LIFERAY_HOME/deploy
cp commons-collections4-4.1.jar $LIFERAY_HOME/deploy
cp commons-codec-1.12.jar $LIFERAY_HOME/deploy
cp commons-logging-1.2.jar $LIFERAY_HOME/deploy
cp gson-2.8.5.jar $LIFERAY_HOME/deploy
cp guava-21.0.jar $LIFERAY_HOME/deploy
cp jackson-annotations-2.9.8.jar $LIFERAY_HOME/deploy
cp jackson-core-2.9.8.jar $LIFERAY_HOME/deploy
cp jackson-databind-2.9.8.jar $LIFERAY_HOME/deploy
```

note that with the [commit](https://github.com/eclipse/sw360/commit/71348b4fffa6e3e5fd761a3f63590a0a60663827) to sw360-13.0.0-M1 you need also another dependency for apache poi:

```
cp commons-compress-1.20.jar $LIFERAY_HOME/deploy
```

## Install Couchdb Lucene

SW360 uses for searching the contents of the couchdb databases a lucene-based server named couchdb-lucene. The main thing is that it requires pathing for the use in the normal SW3360 setups. The reason for the patch is that the developers presume that couchdb-lucene runs as the only component in the application server, while in the sw360 setup, there is a setup in which couchdb-lucene runs along with other components in the same application container.

Start with downloading the couchdb-lucene and rename the archive so the resulting URL path element will be `couchdb-lucene`:

`wget https://github.com/rnewson/couchdb-lucene/archive/v2.1.0.tar.gz ./couchdb-lucene.tar.gz`

Please refer to the script in sw360vagrant how to apply the patch to couchdb-lucene:

https://github.com/sw360/sw360vagrant/blob/master/shared/scripts/install-lucene.sh

Please note that the patching issue is well known in the project and it is unclear why it is not merged:

* https://github.com/rnewson/couchdb-lucene/issues/161 "allow context-root other than "/" when running in servlet container"
* https://github.com/rnewson/couchdb-lucene/pull/162
* https://github.com/rnewson/couchdb-lucene/pull/152

Now, for CouchDB 2.X the hook for integration of a search component has chaned compared to CouchDB 1.X. Accordingly, the old couchdb-lucene component must be replaced with the latest version.

## Deploy New SW360

You will need to checkout new Java-11 based version of the SW360, which is either tagged version 11 or some few commits before that. Then build in the sw360 project root using:

`mvn clean install -DskipTests`

This will install new artfacts, such as lib-datahandler in your maven repostiory. Then apply in the same:

```
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -DskipTests
```

Skipping tests has the reason that usually, the sw360 is tested in the CI and thus, local tests are note necessary, if the code has not been changed locally. Note that the REST API documentation framework is based on building test cases and thus for deploying a version with REST API documentation, tests should be executed:

```
cd rest
mvn clean package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/deploy/ -Dbackend.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/ -Drest.deploy.dir=/opt/liferay-ce-portal-7.3.3-ga4/tomcat-9.0.33/webapps/
```

## Final Steps in Liferay

Liferay CE 7.3 bring some changes that still require manually applied settings to the running liferay server. Thus, you could start the liferay server or just restart the entire machine. The following two things need to be adaptedin liferay after successful startup in order to get the migration done:

1. The automatic verification of e-mail adresses maybe be needed to be switched off, because it kicks in also for existing users. This can be done in "Control Panerl" -> "Instance Settings" -> "User Authentication" -> ""

2. The JavaScript components jquery and fontawesone (that come with liferay) must be manually enabled now. For this got into "Control Panel" -> "System Settings" -> "Thrid Party". and from then select the two JavaScript components from the left and enable them accordingly.

## Known Issues

### Database Availability Right after Update

Right after updating, the sw360 will not show up data at all, but sometimes nothing or "portlet unavailable". The problem is the re-indexing of the DB and the search index which takes a while. You can trigger reindexing in the systems. A lazy way is call all (main) views so the database stumbles accross it and starts the indexing tasks (see job view in the couchdb admin interface of Futon). The sam eis for searches, the first searches will fail and the lucene will do some internal updates. leaving the system working for some time and follow the log will help. Could take 30 minutes.

### E-Mail Verification Trap

Liferay has automatically enabled password verification for all accounts right after migration. Not sure what motivates persons to enable such feature by default right after migration from an instance where it was not there? In case you have attached the system to an external login solution, but your liferay is not configured to send mails, then it is a trap, because you cannot verify the e-mail address and thus, cannot login. You need to disable the external login solution and use the original initial setup user to login (which is not asked for verification by e-mail) to disable this feature (see above). 
