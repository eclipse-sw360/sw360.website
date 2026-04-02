---
linkTitle: "User Management Roles"
title: "User Management Roles"
weight: 10
---

Every user can create records and edit their own records. However, to change
records owned by others, approval is required. This is handled through a
**Moderation Request** — a set of proposed changes that are not applied
immediately, but are routed to:

- The creator of the record
- The moderators defined for that record
- The Clearing Admin(s) of the same department

The proposed changes can then be approved or rejected by any of the above.

## Global Roles

Global roles are assigned to users by an administrator via **Admin > Users**.
They define a user's system-wide capabilities.

1. **User** — The default role. A user can create and edit their own records.
   To modify records owned by others, they must submit a Moderation Request.

2. **Clearing Expert** — Member of the clearing team. Can work on projects
   within their own group, edit licenses, and respond to clearing requests.

3. **Clearing Admin** — A higher-level clearing role. Has the same capabilities
   as a Clearing Expert, but actions taken by a Clearing Admin **do not**
   generate Moderation Requests.

4. **ECC Admin** — The only users who can edit or approve ECC (Export Control
   and Customs) classifications on components and releases.

5. **Security Admin** — Can view and suppress security vulnerabilities across
   the instance. They can assess risk across all projects in their department.

6. **Security User** — A read-only security role. Can view vulnerability data
   but cannot suppress findings. Assigned and managed via **Admin > Users**.

7. **SW360 Admin** — Full administrative rights on all visible records.
   Can promote other users to any role. Use this role for users who need
   administrative capabilities within the application.

8. **Admin** — Identical privileges to SW360 Admin. This role originates from
   the legacy Liferay deployment and is retained for backwards compatibility.
   Typically used for system-level administrators.

> [!NOTE]
> `Admin` and `SW360 Admin` have equivalent privileges. The two roles exist
> for historical reasons. See the
> [Authorization Concept](../Deployment/Deploy-Authorization-Concept.md)
> for details on department-based visibility and secondary role mapping.

## Record-Level Roles (ACLs)

In addition to global roles, SW360 supports record-level access control. These
roles are set per data item (Component, Release, or Project) by the item's
creator or moderator:

1. **Creator** — The user who created the record. Can always edit it without
   a Moderation Request.
2. **Moderator** — Defined by the creator. Has the same edit rights as the
   creator for that specific record.
3. **Contributor** *(Component/Release)* — Can edit the record but cannot delete
   it or manage its ACL settings.
4. **Project Owner** — The user designated as owner of a project.
5. **Lead Architect** *(Project)* — A contributor role used to identify the
   person responsible for technical architecture decisions.
6. **Project Responsible** *(Project)* — A contributor role used to identify
   the person accountable for the project overall.
7. **Security Responsible** *(Project)* — Users designated as responsible for
   the security posture of a specific project.

---

## Global Role Capabilities

| Capability | User | Clearing Expert | Clearing Admin | ECC Admin | Security Admin | Security User | SW360 Admin |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Create records | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Edit own records | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Edit others' records directly | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Approve moderation requests | ❌ | ❌ | ✅ <sup>1</sup> | ❌ | ❌ | ❌ | ✅ |
| Edit license details | ❌ | ✅ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Import / delete licenses (OSADL, SPDX) | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Edit obligations | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Handle clearing requests | ❌ | ✅ | ✅ <sup>2</sup> | ❌ | ❌ | ❌ | ✅ |
| Delete clearing requests | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ✅ |
| Edit ECC classifications | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ✅ |
| View vulnerability data | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ <sup>3</sup> | ✅ |
| Suppress vulnerabilities | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Manage users & promote roles | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Access admin configurations | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

*<sup>1</sup> Clearing Admin are added can approve Moderation Requests for records
within their own department.*<br />
*<sup>2</sup> Clearing Admin is the **default moderator** for clearing
requests.*<br />
*<sup>3</sup> Security User has read-only access to vulnerability data and a
limited view of projects (even private) in their department.*<br />

> [!NOTE]
> `SW360 Admin` and `Admin` share identical capabilities. Both rows would be
> identical in this table. See the [note above](#global-roles) for context.

---

## Project Visibility

Every project in SW360 has a **Visibility** setting that controls who can see
it. There are four levels, each granting access to a progressively wider
audience:

### Private
Only the most restricted set of users can view this project.

* Project Creator
* Security User *(limited, read-only view)*
* SW360 Admin / Admin *(only if `IS_ADMIN_PRIVATE_ACCESS_ENABLED` is enabled — off by default)*

### Me and Moderators
In addition to Private access, this level grants visibility to all users with
a project-level role:

* Project Creator
* Project Responsible
* Lead Architect
* Defined Project Moderators
* Defined Project Contributors
* Security User *(limited, read-only view)*
* SW360 Admin / Admin *(only if `IS_ADMIN_PRIVATE_ACCESS_ENABLED` is enabled — off by default)*

### Business Unit and Moderators *(Default)*
This is the **default visibility level**. In addition to Me+Moderators access:

* All users whose primary department matches the project's Business Unit
* All users with a matching secondary department
* Clearing Admin / Clearing Expert
* SW360 Admin / Admin *(always, regardless of `IS_ADMIN_PRIVATE_ACCESS_ENABLED`)*

> [!NOTE]
> The Business Unit match uses the **department prefix** extracted from the
> user's organization string, not the full department name.

### Everyone
All logged-in users can view the project regardless of their department,
role, or project membership.

---

## Per-Record Permissions

The backend enforces the following access rules per document type. For
**Components**, **Releases**, and **Projects**, denied writes result in a
**Moderation Request** being generated instead. For **Licenses**, **Vendors**,
and **Vulnerabilities**, there is no moderation fallback — the action either
succeeds or fails outright.

### Components

Components support an **optional** visibility restriction
(`IS_COMPONENT_VISIBILITY_RESTRICTION_ENABLED`). When enabled, the same
visibility logic as projects applies (Private, Me+Mods, BU+Mods, Everyone).
When disabled (the default), all logged-in users can read all components.

| Action | Minimum Requirement | Fallback |
|---|---|---|
| Read | Depends on visibility setting | — |
| Write / Attachments | Admin, Clearing Admin/Expert (same dept), or record Moderator/Contributor | → Moderation Request |
| Delete / Clearing | Admin, Clearing Admin (same dept), or record Moderator | → Moderation Request |

### Releases

Releases are always readable by all logged-in users.

| Action | Minimum Requirement | Fallback |
|---|---|---|
| Read | Any logged-in user | — |
| Write / Attachments | Admin, Clearing Admin/Expert (same dept), or record Moderator/Contributor | → Moderation Request |
| Delete / Clearing | Admin, Clearing Admin (same dept), or record Moderator | → Moderation Request |
| Write ECC | ECC Admin (primary **or** any secondary department role) | → Moderation Request |

### Projects (Open)

For **open** (non-closed) projects, access follows the standard rule-set.
Note that for Projects, **moderators** includes: Creator, Project Responsible,
and defined Moderators. **Contributors** additionally includes: Lead Architect
and defined Contributors.

| Action | Minimum Requirement | Fallback |
|---|---|---|
| Read | Depends on Visibility setting | — |
| Write / Attachments | Admin, Clearing Admin/Expert (same dept), or record Moderator/Contributor | → Moderation Request |
| Delete / Clearing | Admin, Clearing Admin (same dept), or record Moderator | → Moderation Request |
| Write ECC | Admin only | → Moderation Request |

### Projects (Closed)

Once a project's clearing state is set to **CLOSED**, permissions become more
restrictive. Only specific fields remain editable (e.g., `state`,
`securityResponsibles`, `externalIds`). Attachments and obligations cannot be
modified by anyone except admins.

| Action | Minimum Requirement | Fallback |
|---|---|---|
| Read | Depends on Visibility setting | — |
| Write / Attachments | Admin, Clearing Admin/Expert (same dept), Creator, Project Responsible, Moderator, Contributor, or Lead Architect | → Moderation Request |
| Delete / Clearing / Write ECC | **Admin only** | → Moderation Request |

### Licenses

Clearing actions and deletion of licenses are restricted. There is no
moderation fallback for licenses.

| Action | Minimum Requirement |
|---|---|
| Read | Any logged-in user |
| Delete / Clearing | Clearing Admin or above (Admin/SW360 Admin) |

### Vendors

Vendors have a dedicated **Admin > Vendors** management UI. Vendor records
have no record-level ACLs (no moderators or contributors), so role-based
checks apply globally. There is no moderation fallback.

| Action | Minimum Requirement |
|---|---|
| Read | Any logged-in user |
| Write | Admin or Clearing Admin (same dept) |
| Delete | Admin or Clearing Admin (same dept) |

### Vulnerabilities

Vulnerability records have no record-level ACLs and no moderation fallback.

| Action | Minimum Requirement |
|---|---|
| Read | Any logged-in user |
| Write | Admin or Clearing Admin (same dept) |
| Delete | Admin or Clearing Admin (same dept) |
