---
linkTitle: "Authorization Concept"
title: "Authorization Concept"
weight: 100
description: >
  Describe different roles of authorization concepts on SW360
---

The authorization concept describes the different roles of the solution - mainly for documentation of the authorization of different roles of the sw360. It is not focusing for the roles like being a moderator, it is described on a separate page for users: [role and access model](https://github.com/eclipse/sw360/wiki/Dev-Role-Authorisation-Model)

## Roles Overview

SW360 offers two choices for doing the roles: one is setting access rights at every record individually. Another are general roles that can be set for every user. An admin of SW360 can set user roles at the Liferay Users and Roles UI.

#### Setup Admin (Liferay Role)

The setup admin is the Liferay administrator, which can configure the entire liferay app, such as which portlets are shown on which page.

#### SW360 Admin (Liferay Role)

The SW360 admin can change all data and promote users for more access rights, such as promoting a user to role `CLEARING_ADMIN`. So its use case is to promote users to clearing admins after some time without always asking the site administrator to do this. To enhance the `SW360_ADMIN` role to allow users of this role to promote other users's roles, follow these steps:

1. Go to control panel
2. Select the `Users` section
3. To subsection `Roles`
4. Select row for `SW360 Admin` and select action `Define permissions`.

When defining permissions the idea is to reduce the permissions to the lowest level possible. Just allow for changing users.

#### Clearing Admin (Liferay Role)

The clearing admin can change all component and release records and project records of the same group.

#### Security Admin (Liferay Role)

In addition to the user rights, the security admin can set security vulnerabilities to irrelevant

#### ECC Admin (Liferay Role)

In addition to the user rights, the ECC admin can manipulate ECC data.

#### User

A user can create, modify and delete all own (=self created) records. A user cannot change records of others

#### Summary

### Moderation Requests

If a user with user or other access role rights is not entitled to write or change a record, a moderation request will be created. The moderation request contains the changes an will be routed for approval to the users who can write this record.
