---
title: "SW360 Documentation"
linkTitle: "Documentation"

menu:
  main:
    weight: 90
---

For development, please see the [README.md](https://github.com/eclipse/sw360/blob/master/README.md) file of the project first. Please check also the pages on the right widget of pages. Not every page there has a link on this page!

## Getting started

| Name | URL | Remarks |
| --- | --- | --- |
| Main home page | https://www.eclipse.org/sw360/ | main home page with general info |
| Project @ Github | https://github.com/eclipse/sw360 | where the music plays |
| Developer mailing list | sw360-dev@eclipse.org | for developers, discussion about developing |
| Slack Channel | https://sw360chat.slack.com/ | the main chat spot, everybody is welcome |
| Slack Channel Invitation Link | [Sharable join link to join](https://join.slack.com/t/sw360chat/shared_invite/enQtNzg5NDQxMTQyNjA5LThiMjBlNTRmOWI0ZjJhYjc0OTk3ODM4MjBmOGRhMWRmN2QzOGVmMzQwYzAzN2JkMmVkZTI1ZjRhNmJlNTY4ZGI) | that should bring you in |
| sw360 developer meeting | [Meeting Info](Developer-Meetings) | Everyone is welcome!


## Naming Policies for this Wiki

Please start every page with a prefix

1. **User**: topics suitable for admins and end users
1. **Deploy**: All things about deployment
1. **Dev**: All topics for developers
1. **Test**: Also a topic for developers, but also around testing

# Using sw360

For using the sw360 as a user, please see the following basic workflows:

* Basic workflows for [creating a component, release and projects](https://github.com/eclipse/sw360/wiki/User-Workflows:-sw360).
* Workflow how [FOSSology and sw360](https://github.com/eclipse/sw360/wiki/User-Workflows:-sw360-and-FOSSology) play together.
* How to [search](https://github.com/eclipse/sw360/wiki/User-Search) in sw360

### General

* Use case description importing projects, releases with licenses [BDP Import](User--BDP-Import)
* Use case description how to [manage vulnerabilities in your project](User-Vulnerability-Management)
* User documentation how to [use the cve-search server](User--Scheduling-CVE-Search-by-Admins)
* User documentation how to [check vulnerabilities for your projects](User-Check-Vulnerabilities-for-Your-Project)
* Documentation about the [handling of vulnerabilities](User-Vulnerability-Management)

### Special

1. Find information about the [role and access model](https://github.com/eclipse/sw360/wiki/Dev-Role-Authorisation-Model)
1. If you are interested in the concept about [moderation requests](https://github.com/eclipse/sw360/wiki/Dev-Moderation-Requests), read the documentation here.
1. Explaining [[enumerations used in SW360|https://github.com/eclipse/sw360/wiki/User-Data-Model-Enumerations]]

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

### General Deployment Guides

* [Comprehensive blog post on SW360 Installation in Japanese](https://qiita.com/K-Hama/items/1582b4e1bf248025eabb)
* [Install sw360 using Vagrant and Puppet](https://github.com/sw360/sw360vagrant): Please have a look at the sw360vagrant project itself how to go ahead with the installation.
* [Initial Setup of Liferay 6.2 and sw360](Deploy-Liferay): From the beginning until sw360 version 4
* [Initial Setup of Liferay 7.2 and sw360](Deploy-Liferay7): From sw360 version 5 onwards and until sw360 version 10
* [Initial Setup of Liferay 7.3 and sw360](Deploy-Liferay7.3): From sw360 version 11 onwards 
* [Install sw360 manually with Liferay 7.2](Deploy-Natively): From sw360 version 5 onwards and until sw360 version 10
* [Install sw360 manually with Liferay 7.3](Deploy-Natively-11): From sw360 version 11 onwards
* [Generate Documentation (sw360docs) into Artefacts](Deploy-sw360docs): From sw360 version 13.5 onwards
* [Setting CVE Search](Deploy-CVE-search): Get vulnerability information from an external provider of Common Vulnerability Enumeration (CVE) data.

### Special Deployment Guides

* [Migrate from Liferay 6.2 and sw360 4 to Liferay 7.2 and sw360 5](Deploy-Upgrade-to-Liferay-7.2)
* [Migrate from Liferay 7.2 and sw360 10 to Liferay 7.3 and sw360 11](Deploy-Upgrade-to-Liferay-7.3-and-Java-11)
* [Install sw360 on Windows using vagrant](Deploy-sw360-on-Windows-(with-Vagrant)). some particular notes for the Windows platform.
* [Install sw360 with Docker](Deploy-Docker)
* [More Install Information using Docker with sw360chores](https://github.com/sw360/sw360chores) : Please have a look at the sw360chores project itself how to go ahead with the installation. Note that currently (Sept 2020) the docker setup is currently wip and thus does not work out of the box.

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

# Developing sw360

The sw360 is Java-based application consisting of two main parts:

1. A Liferay/based front end application that allows users to work with sw360
1. A Java-based servlet infrastructure Thrift interfaces that allows the Liferay part and other applications to manage and store data
1. In the backend, couchdb is used for storing project, component, release and license information as well as attachments.

### Submitting Issues

Please report issues to the issue tracker, but please keep also in mind that someone else has to read them! Issues should include:

* What you intended to do?
* What did you observe?
* Why do you think it is wrong?
* Screenshots of what you have observed presumably gone wrong or link to pages were another person can follow
* Version where you have observed this.
* Common written English and use of line breaks!!! Use the preview function!

Please refer to the following pages for writing issues:

* https://issues.apache.org/bugwritinghelp.html
* https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines
* https://www.joelonsoftware.com/2000/11/08/painless-bug-tracking/

### Contribution Workflow

As basic introduction, the dev ops works as following:

1. We are issue-based, please do not hesitate to create issues - also for _questions_ (and set the issue tag)
1. The issues are organised by milestones which [do not represent releases anymore](Dev-Releasing-SW360). Milestone are meant to be useful packages of work done
1. Contributions are made through pull requests
1. We do conversations directly on issues and pull requests

More topics regarding "how" to develop:

1. [Definition of done and code style](Dev-DoD-and-Style)
1. [Creating a sw360 release](Dev-Releasing-SW360)
1. [Brief notes on the jgiven testing](Dev-Testing-Frameworks)
1. [For help with problems, you might want to check that](Dev-Troubleshooting)

### Architecture

sw360 is a server application using Java servlets. It did some faint steps towards micro services (ie. one maintaining licenses, another for vulnerabilities), the front end is a portlet applications using good old JSPs.

1. [Introduction and Scope](Dev-Arch-General)
2. [High Level View](Dev-Arch-View)
3. [Architecture Topics](Dev-Arch-Topics)

### General

1. [How to write a new portlet](https://github.com/eclipse/sw360/wiki/Dev-Adding-a-new-portlet:-Frontend)
1. [Adding a new backend service](https://github.com/eclipse/sw360/wiki/Dev-Adding-a-new-portlet:-Backend)
1. [Changing the data model](Dev-Adding-New-Fields-to-Existing-Classes)
1. [REST API overview](Dev-REST-API)
1. [Migrating to Javascript modules](Dev-Using-RequireJS-for-javascript-modules)

### Special

1. [Filtering in portlets](Dev-Filtering-in-Portlets)
1. [The FOSSology integration](Dev-Fossology-Integration)
1. [How moderation requests work](Dev-Moderation-Requests)
1. [Roles and access rights](Dev-Role-Authorisation-Model)
1. [Attachment Types Description](Dev-Attachment-File-Types)
1. [Our ideas of Google-Summer-of-Code 2019](https://wiki.eclipse.org/Google_Summer_of_Code_2019_Ideas#Eclipse_SW360)
1. [How Friendly URLs work with the Liferay Portlets](Dev-Liferay-Friendly-URL)

# Testing sw360

Generally, all modules have unit tests and these are executed (including deployment of couchdb) at CI times. In addtion, to test the front end, there are defined integration test cases for a manual check, if the sw360 is working properly in general:

1. [Test Cases: Components Functionality](Test-Cases-Components)
1. [Test Cases: Licenses Functionality](Test-Cases-Licenses)
1. [Test Cases: Moderations Functionality](Test-Cases-Moderations)
1. [Test Cases: Projects Functionality](Test-Cases-Projects)
