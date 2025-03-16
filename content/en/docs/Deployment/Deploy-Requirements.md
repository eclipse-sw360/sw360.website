---
linkTitle: "System Requirements"
title: "System Requirements"
weight: 100
description: 
  SW360 minimal system requirements based on system class
---

For deploying SW360, the following hardware requirements are recommended. Please note that the main memory consumer is the Tomcat application container. Accordingly, this requires different settings (see `$TOMCAT_HOME/bin/setenv.sh`).

Please note that you can review the current memory situation of the application in the Liferay administration section as well (see `Configuration` -> `Server Administration`).

## Hardware and Infrastructure

### CD-based Test Instances

For continuous deployment and continuous delivery directly deployed to a machine, the following specifications are recommended:

- 1 core
- 4GB RAM
- 40GB normal file system
- 10Mbit Ethernet link

In this case, the SW360 solution runs fairly well for basic interactions and the creation of a few data sets. Note that Tomcat should have 2GB allocated.

### Staging Instances

For testing and working with normal data sets in staging and pre-production environments. Pre-production does not need to have the same execution speed as the production environment; however, it requires enough RAM and file system capacity to run a clone of the data set.

- 2 cores
- 8GB RAM
- 500GB normal file system
- 100Mbit Ethernet link

Tomcat should be adjusted to 4GB RAM.

### Productive Instances

For production environments with, for example, 10K releases and 2K users, deploying the entire solution onto a single larger machine is recommended. This does not apply to a Docker-based setup.

- 4 cores
- 16GB RAM
- 500GB SSD-based file system
- 1GBit Ethernet link

Tomcat should be adjusted to 10-12GB RAM. Note: Normally, you could also run Tomcat with significantly less RAM if you place common dependencies in a shared lib folder.

### Network

The following table provides an overview of the inbound ports:

| Port | Service | Remarks                               |
|------|---------|---------------------------------------|
| 443  | https   | Accessing the application             |
| 22   | ssh     | Administering the application         |
| 80   | http    | If you would like to access over http |
| 5984 | http    | If access to the CouchDB (admin) interface is required |
| 5985 | https   | If access to the CouchDB (admin) interface is required |

Overview of the *additional* outbound ports:

| Port | Service | Remarks                                                      |
|------|---------|--------------------------------------------------------------|
| 3269 | sldap   | If you do authentication using secure LDAP                   |
| 443  | https   | If you consume services over https (e.g., vulnerability pulling) |
| 53   | dns     | ...                                                          |
| 22   | ssh     | The old way of calling a FOSSology server                    |

Outbound ports for http/https may be required for downloading system updates. Ports for ssh may not be required outbound.

## Software

SW360 can run on many platforms. The following reference platforms are recommended:

- **OpenJDK 11**
- **Ubuntu 22.04 LTS**

More information about requirements can be found here: [https://github.com/eclipse/sw360vagrant/wiki](https://github.com/eclipse/sw360vagrant/wiki)
