---
title: "BR-PROJ-003: Clearing Admin Group-Scoped Project Modification Privileges"
linkTitle: "BR-PROJ-003: Clearing Admin Project Rights"
weight: 30
id: "BR-PROJ-003"
domain: "Projects"
rule_type: "Behavioral"
status: "Approved"
governing_config: "none"
impacted_services:
  - "ProjectPermissions"
  - "DocumentPermissions"
  - "SW360Utils"
  - "ProjectDatabaseHandler"
  - "ProjectService"
---

# BR-PROJ-003: Clearing Admin Group-Scoped Project Modification Privileges

> **Standard Classification:** Role Definition & Authorization Invariant
> **Target Entity:** `Project`, `User` (Role: `CLEARING_ADMIN`), `ModerationRequest`
> **Status:** Approved
> **Governing Configuration:** `none` (Interacts with `projects.closed.update.strict` via [BR-PROJ-001](./BR-PROJ-001-closed-project-restrictions.md))

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** an authenticated user holds the `CLEARING_ADMIN` role for a group `DEPT` (either via their primary department and primary user group, or via an entry in `secondaryDepartmentsAndRoles` whose derived Business Unit prefix matches `DEPT`):
  * **When** the user modifies an **open** Project (`project.clearingState != ProjectClearingState.CLOSED`) belonging to the same group `DEPT` (`project.businessUnit == DEPT`):
    * The system **shall allow** the user to directly modify the project and its attachments regardless of whether the user holds any project-level role (such as Creator, Project Owner, Project Responsible, Lead Architect, Moderator, or Contributor).
    * The system **shall bypass** the moderation workflow (no `ModerationRequest` shall be created, and no moderation comment shall be required).
  * **When** the user modifies a **closed** Project (`project.clearingState == ProjectClearingState.CLOSED`) belonging to the same group `DEPT` (`project.businessUnit == DEPT`):
    * The system **shall allow** the user to modify the project directly without generating a `ModerationRequest`, regardless of whether the user holds any project-level role, **subject to** the field and dependency restrictions defined in [BR-PROJ-001](./BR-PROJ-001-closed-project-restrictions.md) (i.e., all fields when `projects.closed.update.strict == false`, or only the 11 allowlisted operational maintenance fields when `projects.closed.update.strict == true`).
  * **Otherwise** (when the user holds `CLEARING_ADMIN` only for groups other than the project's `businessUnit` and is not a member of the project team):
    * For an **open** Project, the system **shall not** grant direct write privileges and **shall route** any modification through a `ModerationRequest`.
    * For a **closed** Project, the system **shall reject** the modification and **shall not** generate any `ModerationRequest`.

Existing visibility checks and separately authorized ECC/security operations remain unchanged. These statements assume no other independent authorization, such as an administrator role or project-team membership. The existing Clearing Expert role hierarchy is preserved; this rule does not redefine it.

### 1.2 Purpose & Risk Mitigated
Clearing Administrators act as group/department-level compliance and governance leads. Requiring a `CLEARING_ADMIN` to be explicitly listed on every individual project's ACL (or forcing them through a Moderation Request that they themselves would be routed to approve) creates unnecessary operational friction. Conversely, granting `CLEARING_ADMIN` unrestricted cross-department edit privileges would violate organizational boundaries. Scoping direct modification privileges to the matching Business Unit (across both primary and secondary department memberships) enables seamless group-level administration while preserving strict compliance boundaries and closed-project audit integrity ([BR-PROJ-001](./BR-PROJ-001-closed-project-restrictions.md)).

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Concept & Meaning | Source Attribute / Field |
|---|---|---|
| **Project Group (Business Unit)** | The organizational unit owning the project. A user's department is uppercased and reduced to its first three whitespace-separated tokens before comparison with the stored Business Unit. | `Project.businessUnit` / `SW360Utils.getBUFromOrganisation(...)` |
| **Primary Group Role** | The user's primary department and global role assignment. | `User.department` + `User.userGroup` |
| **Secondary Group Role** | Additional department-specific role assignments granted to a user. | `User.secondaryDepartmentsAndRoles` (`Map<String, Set<UserGroup>>`) |
| **Same-Group Clearing Admin** | A user who has `CLEARING_ADMIN` in their primary group (where `getBUFromOrganisation(user.department) == project.businessUnit`) **or** in any secondary group entry `(secDept, roles)` where `getBUFromOrganisation(secDept) == project.businessUnit` and `roles` contains `CLEARING_ADMIN`. | `DocumentPermissions.isUserOfOwnGroupHasRole(...)` |
| **Project Team** | Users with existing project-level write authorization. Project Owner alone is not currently part of this ACL calculation. | `createdBy`, `projectResponsible`, `leadArchitect`, `moderators`, `contributors` |
| **Moderation Bypass** | Applying project updates directly to the database without creating a `ModerationRequest`. | `ProjectPermissions.isActionAllowed(RequestedAction.WRITE) == true` |

---

## 3. Detailed Specifications & Behavioral Invariants

### 3.1 Preconditions & Group Matching Invariants
- **Business Unit Normalization:** Department strings (both `user.department` and keys in `user.secondaryDepartmentsAndRoles`) are normalized via `SW360Utils.getBUFromOrganisation(dept)` before comparing against `project.businessUnit`.
- **Multi-Department Evaluation:** If a user belongs to multiple departments that normalize to the same Business Unit (for example, primary department `"DE PT BU"` with role `USER`, and secondary department `"DE PT BU SUB"` with role `CLEARING_ADMIN`), **all** matching department entries must be evaluated so that the `CLEARING_ADMIN` privilege is recognized. A secondary assignment also applies when its department key equals the primary department.
- **Nonempty Group:** An absent or empty Business Unit or department does not grant group-based privileges.

### 3.2 Authorization & Role Permissions Matrix

| Actor / Role | Group Match (`businessUnit == DEPT`) | Project Team Member? | Open Project (`clearingState != CLOSED`) | Closed Project (`strict = false`) | Closed Project (`strict = true`) |
|---|---|---|---|---|---|
| **`ADMIN` / `SW360_ADMIN`** | Any | Any | Direct edit (all fields & dependencies; no MR) | Direct edit (all fields & dependencies; no MR) | Direct edit (all fields & dependencies; no MR) |
| **`CLEARING_ADMIN` (Primary Group)** | **Yes (`DEPT`)** | **No (or Yes)** | **Direct edit (all fields, dependencies, attachments; no MR)** | **Direct edit (all fields; no MR)** | **Direct edit of 11 allowlisted fields only (no MR); other fields/dependencies `403 Forbidden`** |
| **`CLEARING_ADMIN` (Secondary Group)** | **Yes (`DEPT`)** | **No (or Yes)** | **Direct edit (all fields, dependencies, attachments; no MR)** | **Direct edit (all fields; no MR)** | **Direct edit of 11 allowlisted fields only (no MR); other fields/dependencies `403 Forbidden`** |
| **`CLEARING_ADMIN` (Other Group)** | No (`OTHER != DEPT`) | No | Moderation Request required | Denied (no MR) | Denied (no MR) |
| **Project Team Member (`USER`)** | Any | Yes | Direct edit (all fields; no MR) | Direct edit (all fields; no MR) | Direct edit of 11 allowlisted fields only (no MR); other fields/dependencies `403 Forbidden` |
| **Regular `USER`** | Any | No | Moderation Request required | Denied (no MR) | Denied (no MR) |

### 3.3 Interaction with Closed Project Restrictions (BR-PROJ-001)
- This rule grants **write equivalence (moderation bypass)** to a same-group `CLEARING_ADMIN` so that their permitted edits are applied directly without creating a `ModerationRequest`.
- It **does not** override the closed-project immutability constraints of [BR-PROJ-001](./BR-PROJ-001-closed-project-restrictions.md): when `project.clearingState == CLOSED` and `projects.closed.update.strict == true`, a same-group `CLEARING_ADMIN` is still restricted to the 11 allowlisted operational maintenance fields and cannot modify linked releases, linked projects, packages, or non-allowlisted fields.

---

## 4. Executable Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: Primary-group Clearing Admin directly modifies an open project without project role
* **Given** an open project `"cloud-gateway"` with `businessUnit = "DEPT"` and `clearingState = OPEN`
* **And** an authenticated user `"claire"` with primary `department = "DEPT"`, primary `userGroup = CLEARING_ADMIN`, and no role in `"cloud-gateway"`
* **When** `"claire"` updates the project description, linked releases, or project owner without a moderation comment
* **Then** the system applies the changes directly with HTTP `200 OK`
* **And** no `ModerationRequest` is created.

### Scenario 2: Secondary-group Clearing Admin directly modifies an open project without project role
* **Given** an open project `"edge-controller"` with `businessUnit = "DEPT"` and `clearingState = OPEN`
* **And** an authenticated user `"sam"` with primary `department = "OTHER"`, primary `userGroup = USER`, and secondary role `CLEARING_ADMIN` for `"DEPT"`
* **When** `"sam"` modifies `"edge-controller"`
* **Then** the system applies the changes directly with HTTP `200 OK`
* **And** no `ModerationRequest` is created.

### Scenario 3: User with primary USER role in same BU and secondary CLEARING_ADMIN role in sub-department of same BU
* **Given** a project `"iot-firmware"` with `businessUnit = "DE PT BU"`
* **And** an authenticated user `"pat"` with primary `department = "DE PT BU"` (`userGroup = USER`) and secondary department `"DE PT BU SUB"` (`roles` contains `CLEARING_ADMIN`)
* **When** `"pat"` modifies `"iot-firmware"`
* **Then** the system evaluates all matching departments for `"DE PT BU"` and grants `RequestedAction.WRITE`
* **And** the update succeeds directly without creating a `ModerationRequest`.

### Scenario 4: Same-group Clearing Admin modifies allowlisted fields on a closed project in strict mode
* **Given** `projects.closed.update.strict` is `true`
* **And** a closed project `"smart-sensor"` with `businessUnit = "DEPT"` and `clearingState = CLOSED`
* **And** user `"claire"` has `CLEARING_ADMIN` for `"DEPT"` (primary or secondary) and is not on the project team
* **When** `"claire"` updates `enableSvm`, `projectOwner`, or `phaseOutSince`
* **Then** the update succeeds directly with HTTP `200 OK` without a `ModerationRequest`
* **And** when `"claire"` attempts to modify `description` or `linkedReleases`, the request is rejected with HTTP `403 Forbidden`.

### Scenario 5: Clearing Admin of a different group modifies an open project (Moderation Required)
* **Given** an open project `"cloud-gateway"` with `businessUnit = "DEPT"`
* **And** user `"alex"` has `CLEARING_ADMIN` only for `"OTHER_DEPT"` and is not on the project team
* **When** `"alex"` submits an update to `"cloud-gateway"` with a moderation comment
* **Then** the system does not apply the update directly
* **And** a `ModerationRequest` is created (`202 Accepted`).

### Scenario 6: Clearing Admin of a different group attempts to modify a closed project (Forbidden)
* **Given** a closed project `"smart-sensor"` with `businessUnit = "DEPT"` and `clearingState = CLOSED`
* **And** user `"alex"` has `CLEARING_ADMIN` only for `"OTHER_DEPT"` and is not on the project team
* **When** `"alex"` attempts to update a field on `"smart-sensor"` with a moderation comment
* **Then** the system rejects the update with HTTP `403 Forbidden`
* **And** no `ModerationRequest` is created.

Requests failing REST input validation (for example, a missing required moderation comment for a user without write permission) can return `400 Bad Request` before the closed-project check. Such requests still cannot change the project or create a Moderation Request.

---

## 5. Implementation & Traceability

- **Project Permissions:** `org.eclipse.sw360.datahandler.permissions.ProjectPermissions` (`isActionAllowed`, `getUserEquivalentOwnerGroup`, `getDepartmentsIfUserInBU`)
- **Base Document Permissions:** `org.eclipse.sw360.datahandler.permissions.DocumentPermissions.isUserOfOwnGroupHasRole(...)`
- **Closed Project Check:** `org.eclipse.sw360.datahandler.common.SW360Utils.isUserAllowedToEditClosedProject(...)` and `org.eclipse.sw360.datahandler.db.ProjectDatabaseHandler.isProjectUpdateAllowed(...)`
- **REST Moderation Validation:** `org.eclipse.sw360.rest.resourceserver.moderationrequest.ModerationRequestController.validateModerationRequest(...)`
- **REST Project Updates:** `org.eclipse.sw360.rest.resourceserver.project.ProjectController.patchProject(...)` and `patchProjectWithNetwork(...)` evaluate write permission against the persisted project, not a partial request body.
- **Unit & Integration Tests:**
  - `org.eclipse.sw360.datahandler.permissions.ProjectGroupPermissionsTest`
  - `org.eclipse.sw360.datahandler.db.ProjectDatabaseHandlerClosedUpdateTest`
  - `org.eclipse.sw360.rest.resourceserver.integration.ProjectTest` (network regression requires `enable.flexible.project.release.relationship=true`)

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-11-05 | SW360 Core Team | Initial specification of group-scoped (primary and secondary department) `CLEARING_ADMIN` direct project modification privileges and moderation bypass |
