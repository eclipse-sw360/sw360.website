---
title: "Roles and Authorization"
linkTitle: "Roles and Authorization"
weight: 10
description: "SW360 Roles and Authorization"
---

Like any other system, SW360 allows for setting different levels of access for different users. Technically, the decision when user should be able to see or to do something happens (generally) on the backend server. This ensures consistency between the REST API and the portal application.

For setting roles of a user, the Liferay control panel is being used (Admin menu -> Control Panel -> Users and Organisations -> Users -> select one user and Edit -> Roles). Setting access at individual records happens in the edit view of that record.

## Roles Overview

SW360 offers two choices for doing the roles: one is setting access rights at every record individually. Another are general roles that can be set for every user. An admin of SW360 can set user roles at the Liferay Users and Roles UI.

#### Setup Admin (Liferay Role)

The setup admin is the Liferay administrator, which can configure the entire liferay app, such as which portlets are shown on which page.

#### SW360 Admin (Liferay Role)

The SW360 admin can change all data and promote users for more access rights, such as promoting a user to role `CLEARING_ADMIN`. This role can change data from other groups, limited by visibility setting of a project.

#### Clearing Admin (Liferay Role)

The clearing admin can change all component and release records and project records of the same group. This can be seen as group administrator.

#### Security Admin (Liferay Role)

In addition to the user rights, the security admin can set security vulnerabilities to irrelevant

#### ECC Admin (Liferay Role)

In addition to the user rights, the ECC admin can manipulate ECC data.

#### User

A user can create, modify and delete all own (=self created) records. A user cannot change records of others

### Moderation Requests

If a user with user or other access role rights is not entitled to write or change a record, a moderation request will be created. The moderation request contains the changes an will be routed for approval to the users who can write this record.

In addition there are ACL-style roles, meaning that per data item access settings can be made:

1. **creator** - a creator can modify in addition to the user's read abilities, a user can be creator of a data item
2. **moderator** - a creator can define moderators for a data item. Moderators can change a data item as a creator can. 
3. **contributor** (Component) - is a contributor to a component, project, similar (but not the same) to a moderator. In addition to moderator, this role has been added to identify contributors (or that contributors get the fame).
In contrast, the contributor cannot delete data items.
5. **project responsible** (Project) - is a contributor, just named differently to identify the responsible person.
6. **lead architect** (Project) - is a contributor, just named differently to identify the responsible person. an architect refers to the person who has that role of the project or product. This role has been added to identify architects to have a contact person for technical questions.
7. **contact** (Release) - deprecated, should be renamed to contributor see #100.

`group (department)`, `contributor`, `moderator` and `owner` roles are entity specific, `user`, `clearing admin` and `admin` are roles assigned to a user.

### Additional Project Visibility

In addition to the roles mentioned above, each project has a separate visibility setting (technically an attribute of the project document). There are four project visibility levels:

1. Private - no one but the creator can read.
2. Me and moderators - involves all moderators and contributors, basically all names that are named among the attributes (lead architect, project responsible, contributors)
3. Department / business unit (should be renamed) - refer to the group the users are in.
4. Public - all registered users of the liferay / sw360 application (login required).

The access rules are implemented in`lib-datahandler`. In the package, `com.siemens.sw360.datahandler.permissions` this is implemented in `ProjectPermissions`. See methods `isVisible` and `userIsEquivalentToModeratorinProject()` for the actual rules.

### Overall Access Matrix

The following table presents the SW360 Role-Authorisation-Model.

The row specifies which action to take, the column the role of the actor. Cell entries specify which entity type can be acted upon.

|     | creator | moderator | contributor | user | clearing admin | (sw360)admin |
| --- | ----------- | --------- | ----- | ---- | -------- | ----- |
| create | - | - | - | PCRV | PCRVL | PCRVL |
| read | P | P | P | (P²)CRVL | (P²)CRVL | PCRVL |
| edit | PCR | PCR | PCR | (all created ones) | PCRVL | PCRVL |
| delete | PCR | PCR | - | (all created ones)  | L | PCRVL |

P² : only if the user is member of the group of the project (or has created the project)

Note that ECC Admins and Security Admins have only the ability to write ECC and security data respectively at given records. However, as for the other access rights this role does not enhance anything above users.

#### Legend

| acronym | description |
| ------- | ----------- |
| P | project |
| C | component|
| R | release |
| V | vendor |
| L | license |

## Technical Info

The role access rules are put into `lib-datahandler`. In the package, `com.siemens.sw360.datahandler.permissions` there are implementing classes of a template class `DocumentPermissions`. As an example, `ProjectPermissions` extends abstract class `DocumentPermissions`.

At run time, a permissions object consisting of a document and a user is created: In `PermissionUtils` (same package) there is a static method `makePermissions<T>()` that creates a permissions object. The received permissions object instance can be asked if a particular operation is allowed.

Note that the general application of these permission operations runs in the backend (Thrift services). An application in the front end of `PermissionUtils` for example, is for displaying buttons depending on the user main role (user, clearing admin or admin). Then the portlet makes plain use of the `lib-datahandler` library.

## Further plans

1. Actually, creating stuff should be checked in lib-datahandler, starting with creation of licenses,which should ot be permitted to users: [Issue #106](https://github.com/siemens/sw360portal/issues/106)

2. [Issue #101](https://github.com/siemens/sw360portal/issues/101) for

|     | contributor | moderator | creator | user | clearing admin | admin |
| --- | ----------- | --------- | ----- | ---- | -------- | ----- |
| download OSS sources | - | - | - | R | R | R |
| download internal sources | R | R | R | - | - | R |

3. [Issue #102](https://github.com/siemens/sw360portal/issues/102) for

|     | contributor | moderator | creator | user | clearing admin | admin |
| --- | ----------- | --------- | ----- | ---- | -------- | ----- |
| send to clearing | - | P | P | - | - | PCRL |

4. [Issue #103](https://github.com/siemens/sw360portal/issues/103) for

|     | contributor | moderator | creator | user | clearing admin | admin |
| --- | ----------- | --------- | ----- | ---- | -------- | ----- |
| edit clearing report | - | R | R | - | R? | PCRL |



