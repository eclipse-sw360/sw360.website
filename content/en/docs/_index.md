---
title: "SW360 Documentation"
linkTitle: "Documentation"

menu:
  main:
    weight: 90
---

## Overview
**SW360** is a software catalogue application designed to provide a central place for sharing information about software components used by an organization. It is designed to neatly integrate into existing infrastructures related to the management of software artifacts and projects by providing separate backend services for distinct tasks and a set of portlets to access these services. A complete deployment unit exists (vagrant box or docker container) that contains a complete configuration of all services and portlets.

SW360 comprises the following main use case areas:

- Component: Handling of information and processes related to components, e.g. name, vendor
- License: Handling of information regarding licenses, e.g. obligations, license texts etc
- Project: handling of project information providing a context for the use of components
- Vulnerability: Collecting Security Vulnerability Management Information and matching them with components stored in the component service

## Functionality
The SW360 is a software catalogue application which is:

- Based on the Open Source Liferay portal server
- Integrated with Fossology

 With SW360, you can

- Manage your components and projects
- Send source packages to the clearing tool Fossology
- Reuse cleared components and releases for your project
- Import cleared components with clearing reports and other documents
- Browse licenses and their obligations

In order to work with SW360, please note a fundamental setup in the data model when dealing with components:

- A component is a list of releases with metadata. vice versa, releases refer to a component.
- A vendor is separate from a component and releases. The link to the vendor is set at the release. (think of Sun and Oracle)
- A project refers to a number of releases of components accordingly, not components.

## Getting started

| Name | URL | Remarks |
| --- | --- | --- |
| Main home page | https://www.eclipse.org/sw360/ | main home page with general info |
| Project @ Github | https://github.com/eclipse/sw360 | where the music plays |
| Developer mailing list | sw360-dev@eclipse.org | for developers, discussion about developing |
| Slack Channel | https://sw360chat.slack.com/ | the main chat spot, everybody is welcome |
| Slack Channel Invitation Link | [Sharable join link to join](https://join.slack.com/t/sw360chat/shared_invite/enQtNzg5NDQxMTQyNjA5LThiMjBlNTRmOWI0ZjJhYjc0OTk3ODM4MjBmOGRhMWRmN2QzOGVmMzQwYzAzN2JkMmVkZTI1ZjRhNmJlNTY4ZGI) | that should bring you in |
| sw360 developer meeting | [Meeting Info](Developer-Meetings) | Everyone is welcome!
