---
title: "Development"
linkTitle: "Development"
weight: 30
icon: fab fa-github
description: SW360 Development Information
---

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

1. [How to write a new portlet]({{< relref path="Dev-Adding-a-new-portlet-Frontend.md" >}})
1. [Adding a new backend service]({{< relref path="Dev-Adding-a-new-portlet-Backend.md" >}})
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
