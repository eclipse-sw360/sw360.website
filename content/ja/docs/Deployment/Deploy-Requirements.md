---
linkTitle: "System Requirements"
title: "System Requirements"
weight: 100
description: 
  SW360 minimal system requirements based on system class
---

For deploying the SW360, there are the following hardware requirements below. Please note that the main memory consumer is the tomcat application container. Accordingly, this requires different settings (see `$TOMCAT_HOME/bin/setenv.sh`).

Please note that you can review the current memory situation of the application in the liferay administration section as well (see `Configuration`-> `Server Administration`).

## Hardware and Infrastructure

### CD-based test instances

When there is a continuous deployment and continuous delivery directly deployed to machine the following machine is recommended:

* 1 core
* 4GB RAM
* 40GB normal file system
* 10Mbit Ethernet link

In this case, the sw360 solution runs fairly well for clicking around and creation of a few data sets. Note that Tomcat should have 2GB.

### Staging instances

Testing and working with normal data sets for staging and pre-productive testing. Pre productive does not need to have the same execution speed of the machine, however, requires enough RAM and file system to run a clone on the data set.

* 2 cores
* 8GB RAM
* 500GB normal file system
* 100Mbit Ethernet link

The tomcat should be adjusted to 4GB RAM

### Productive instances

Productive with for example: 10K releases, 2k users which deploys the entire solution onto a single larger machine. It does not apply to a docker based setup.

* 4 cores
* 16GB RAM
* 500GB SSD based file system
* 1GBit link Ethernet link

Tomcat should be adjusted to 10-12GB RAM. Note: normally, you could also run Tomcat with significantly lees RAM, if you put common dependencies in a shared lib folder.

### Network

The following table shall give an overview about the inbound ports

| Port | Service | Remarks|
|:-----------|:------------|:------------|
| 443 | https | Accessing the application |
| 22  | ssh | Administering the application |
| 80 | http | if you would like to access the solution over http |
| 5984/5985 | http/https | if access to the couchdb (admin) interface is required |

Overview about the *additional* outbound ports:

| Port | Service | Remarks|
|:-----------|:------------|:------------|
| 3269 | sldap | If you do authentication using secure LDAP |
| 443 | sldap | If you do consume services over https (e.g. vulnerabilty pulling) |
| 53 | dns | ... |
| 22 | ssh | the old way of calling a fossology server |

Outbound ports for http / https may be required for downloading system updates. Ports for ssh may not be required outbound.

## Software:

As for the software, the sw360 can be run on many platforms, even on Windows seven. We have the following reference platform for development:

until 5:

* OpenJDK 8
* Unbunu 16.04 LTS

after 5:

* openjdk 8
* ubuntu 18.04 LTS

after 11:

* openjdk 11
* ubuntu 18.04 LTS

More information about requirements can be found here: https://github.com/sw360/sw360vagrant/wiki
