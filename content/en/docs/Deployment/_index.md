---
title: "Deployment"
linkTitle: "Deployment"
weight: 20
icon: fas fa-tools
description: SW360 Deployment Guides
---

# Deploying sw360

For the deployment of the SW360, it is about deploying a Liferay server application. Please understand, that apart from trying sw360 for a short while, for deployments of SW360 in your organisation you will need knowledge about how to deploy Java server applications. Regardless of the deployment approach the following main elements need to be considered:

* A [Liferay Community Edition bundeled with Tomcat](https://www.liferay.com/de/downloads-community).
* Install CouchDB (this is where SW360 stores all the source code, SPDX files and metadata), depending on your platform, there are a number of ways to use CouchDB. Currently, we tested with CouchDB 2.1.2, other versions of CouchDB may work as well.
* For productive deployments, you do not want to go with the (Hypersonic) DB bundled with Tomcat, but install some normal DB server. We use PostgreSQL. The relation DB server is used by Liferay and should be thus compatible to it.
* For searches, consider CouchDB Lucene [CouchDb Lucene](https://github.com/rnewson/couchdb-lucene/archive/v1.0.2.tar.gz).
* There is a number of additional "prerequisites" for SW360, more detailed [in the Vagrant deployment setup](https://github.com/sw360/sw360vagrant/blob/master/download-packages.sh).

In order to install sw360, you can choose between the following ways:

* Use the Vagrant-based installation. Please refer to the [sw360 vagrant project](https://github.com/sw360/sw360vagrant) and the included Readme file. Basic prerequisites are
  * VirtualBox
  * Vagrant and some vagrant plugins
  * Presumeably a git client
* You could install the sw360portal project natively on the machine. This will require more work in order to install the prerequisites. The above mentioned vagrant project documents very precisely what to do in order to install the sw360portal.
* Checkout the docker suite [sw360chores](https://github.com/sw360/sw360chores) and generate a pre-built container where you can deploy the `*.war` files of sw360portal (both frontend and backend). **Important** this is work in progress now and likely not working out of the box.

### Frequently Experienced Problems

1. The most experienced confusion is about the Liferay setup user: the setup user cannot be used to work with the sw360 because the setup user is missing an organisation assignment. For every user an organisation assignment is required for sw360 to work properly. Unfortunately, you cannot assign a liferay setup user to an organisation. So you do need to import users or create users with organisation.

2. Currently, you need Java 11, we test it with OpenJDK. Newer or older versions may work, but currently, reports tell that for example Java 8 does not work.

3. Thrift: for compiling the software you need to install [Apache Thrift](https://github.com/apache/thrift) (a command line tool). We test with version 0.13.

### General Topcis

* [Deployment Authorization Concept](Deploy-authorization-concept)
* [Properties explained](Deploy-Configuration-Files)
* [Setup of connection with Fossology](Deploy-FOSSology)
* [Deployment Requirements](Deploy-Requirements)
* [Secure Deployment Notes](Deploy-Secure-Deployment)

### Special Topics

After installing sw360 more topics may include:

1. [Special Coverage of Country Codes](Deploy-configuration-country-codes), when countries are displayed, then it uses country codes in the DB 
1. [How to export data and import it to a new instance](Deploy-Export-and-Import)
1. [How to migrate an existing sw360portal to a new instance](Deploy-Migrating-to-a-new-Server)
1. [Using costco to modify the couchdb database](Dev-Database-Migration-using-Costco)
