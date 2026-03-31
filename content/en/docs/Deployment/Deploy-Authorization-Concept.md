---
linkTitle: "Authorization Concept"
title: "Authorization Concept"
weight: 60
description: 
  Modernized authorization roles and visibility concepts for SW360 v20
---

SW360 uses a tiered authorization model that balances global roles with
granular, record-level access. In v20, the architecture clearly separates
**Authentication** (handled by **Keycloak** or an OIDC provider) from
**Authorization** (handled by the **SW360 Backend** using CouchDB as the
source of truth).

## Role Management

Role management is performed through the SW360 Frontend in the **Admin > Users**
section. An administrator can search for users and modify their primary and
secondary roles. These changes are stored in CouchDB and synchronized to Keycloak
(if enabled) via federation.

---

## 1. The Visibility Foundation: Departments & Business Units

Visibility in SW360 is largely driven by a user's **Department** and a project's
**Business Unit (BU)**.

### Department/BU Matching
There is a **1-to-1 relationship** between a user's department and the project's
business unit. For projects with `BUSINESSUNIT_AND_MODERATORS` visibility (the
default), users can view records belonging to their own department.

### Secondary Identities (Multi-Tenancy)
Users can act within multiple departments with different roles. This is stored as
a map of `secondaryDepartmentsAndRoles`. For example:
* **Primary**: `Clearance Expert` in *Department A*.
* **Secondary**: `Clearing Admin` in *Department B*.
* **Secondary**: `ECC Admin` in *Department C*.

A user's effective permissions for a specific record are determined by the
project's Business Unit and the user's role within that corresponding
department.

---

## 2. Core Roles Overview

### SW360 Admin
The SW360 Admin is a global administrative role responsible for system
maintenance and user promotion.
* **Capabilities**: Promote users, manage global configurations, and view system
  logs.
* **Private Access Toggle**: By default, admins are restricted from viewing
  `PRIVATE` projects of other users. However, the configuration
  `IS_ADMIN_PRIVATE_ACCESS_ENABLED` can be toggled to allow admins to manage
  orphaned or locked private projects.

### Clearing Admin vs. Clearing Expert
These roles manage the clearance status of components and releases.
* **Clearing Admin**: A high-level role for managing clearance across a
  department or globally. Actions taken by a Clearing Admin **do not** generate
  moderation requests.
* **Clearing Expert**: A subject matter expert who can perform clearings. Their
  actions may still be subject to moderation depending on specific backend
  configurations.

### Security Admin vs. Security User
These roles are dedicated to vulnerability management.
* **Security Admin**: Can view all vulnerabilities across the instance and has
  the authority to **suppress** or resolve them.
* **Security User**: A read-only security practitioner. They can view
  vulnerability data but cannot suppress findings. They also have a "limited
  view" of all projects in their department to assess risk without seeing
  proprietary project details.

### ECC Admin
The Export Control and Customs (ECC) Admin has the authority to manipulate and
verify ECC-specific data within component and release records.

### User
A standard user can create, modify, and delete their own records. If a user
attempts to change a record they do not own (and they lack a higher
administrative role), a **Moderation Request** is automatically generated.

---

## 3. Record-Level Access (ACLs)

An owner of a record (Component, Release, or Project) can delegate `WRITE`
access to other specific users without administrator intervention.

### Moderators and Contributors
* **Moderators**: Users in this list have full "owner-equivalent" rights for
  that specific record, including the ability to add other moderators.
* **Contributors**: Users who are granted the right to edit the record but
  cannot manage the ACLs or delete the record.

---

## 4. Moderation Workflow

If a user lacks the necessary role or ownership rights to modify a record, the
SW360 Backend creates a **Moderation Request**. 
1. The request contains the proposed changes.
2. It is routed to the authorized moderators of the record (or Clearing Admins
   for clearance data).
3. The change is only applied to the primary record once a moderator approves
   the request.
