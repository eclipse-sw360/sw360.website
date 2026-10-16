---
title: "BR-PROJ-001: Closed Project Update Restrictions"
linkTitle: "BR-PROJ-001: Closed Projects"
weight: 10
id: "BR-PROJ-001"
domain: "Projects"
rule_type: "Behavioral"
status: "Approved"
governing_config: "projects.closed.update.strict"
impacted_services:
  - "ProjectPermissions"
  - "ProjectService"
last_verified: "2026-09-07"
---

# BR-PROJ-001: Closed Project Update Restrictions

> **Standard Classification:** Behavioral Constraint / Access Control
> **Target Entity:** `Project`, Linked Dependencies (`Release`, `Project`, `Package`)
> **Status:** Approved
> **Governing Configuration:** `projects.closed.update.strict` (Default: `false`)

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** a Project has clearing state `CLOSED` (`project.clearingState == ProjectClearingState.CLOSED`):
  * **If** `projects.closed.update.strict` is `false`:
    * The system **shall allow** users with role `CLEARING_ADMIN` (or above) as well as the project team (Creator, Project Responsible, Project Owner, Moderators, Contributors, and Lead Architects) to modify project fields.
  * **If** `projects.closed.update.strict` is `true`:
    * The system **shall allow only** users with role `ADMIN` (or `SW360_ADMIN`) to modify any field and linked dependencies across the project without restriction.
    * The system **shall allow** project team members (Creator, Project Responsible, Project Owner, Lead Architect, Moderators, Contributors) **and** users with role `CLEARING_ADMIN` (regardless of whether they are a member of the project team) to modify **only** the following 11 allowlisted operational maintenance fields:
      1. **Enable Security Monitoring** (`enableSvm`)
      2. **Enable Displaying Vulnerabilities** (`enableVulnerabilitiesDisplay`)
      3. **Project Responsible** (`projectResponsible`)
      4. **Project Owner** (`projectOwner`)
      5. **Lead Architect** (`leadArchitect`)
      6. **Moderators** (`moderators`)
      7. **Contributors** (`contributors`)
      8. **Security Responsibles** (`securityResponsibles`)
      9. **External IDs** (`externalIds`)
      10. **Project State** (`state`, e.g., Active, Phase-out)
      11. **Phase-out Date** (`phaseOutSince`)
    * The system **shall strictly prohibit** project team members, Clearing Admins, and regular users from modifying linked releases (`linkedReleases`), linked sub-projects (`linkedProjects`), linked packages (`packages`), or any non-allowlisted fields.
  * **Otherwise** (unauthorized users, or attempts by team members or Clearing Admins to modify non-allowlisted fields or linked dependencies in strict mode), the system **shall reject** the update request with HTTP `403 Forbidden` and **shall not** generate any moderation request.

### 1.2 Purpose & Risk Mitigated
This restriction is enforced strictly for **audit and compliance purposes**.
A project transitions into the **CLOSED** clearing state only after its
open-source license clearing is certified and signed off. Once closed, any
addition, removal, or modification of linked releases, sub-projects, packages,
or clearing data creates **license clearing drift**, invalidating the audited
compliance baseline. Enforcing strict closed mode prevents audit violations
while permitting project teams and clearing administrators to maintain
operational lifecycle details (such as vulnerability monitoring toggles,
security contacts, project ownership, team maintainers, and phase-out
milestones).

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Meaning | Field / Attribute Reference |
|---|---|---|
| **Closed Project** | A project whose license clearing process is completed and certified. | `Project.clearingState == CLOSED` |
| **Project Team** | Collaborative owners and maintainers of the project. | `creator`, `projectOwner`, `projectResponsible`, `leadArchitect`, `moderators`, `contributors` |
| **Clearing Admin** | Global role responsible for overseeing organizational clearing operations. | `UserRole.CLEARING_ADMIN` |
| **Strict Closed Mode** | System mode enforcing the 11-field allowlist and blocking non-admin modifications. | `projects.closed.update.strict` |
| **Linked Dependencies** | Software bill of materials (SBOM) associations governing compliance. | `linkedReleases`, `linkedProjects`, `packages` |
| **Operational Maintenance Fields** | The 11 non-clearing fields permissible for team and Clearing Admin updates in strict mode. | Listed in Section 1.1 |

---

## 3. Specifications & Behavioral Invariants

### 3.1 Permissions Matrix by Configuration Mode

| Actor / Role | `projects.closed.update.strict = false` | `projects.closed.update.strict = true` | Enforcement on Disallowed Update |
|---|---|---|---|
| **System Admin (`ADMIN` or `SW360_ADMIN`)** | Can modify **all** fields & dependencies | Can modify **all** fields & dependencies | — |
| **Clearing Admin (`CLEARING_ADMIN`)** | Can modify **all** fields | Can **only** modify the 11 allowlisted fields (even if not on project team; No linked releases/projects/packages) | `403 Forbidden` (No moderation request) |
| **Project Team** (Creator, Owner, Responsible, Lead Architect, Moderator, Contributor) | Can modify **all** fields | Can **only** modify the 11 allowlisted fields (No linked releases/projects/packages) | `403 Forbidden` (No moderation request) |
| **Other Registered Users** | Update denied | Update denied | `403 Forbidden` (No moderation request) |

### 3.2 Invariants on Linked Entities & Automated Cascades
* **Dependency Immutability:** Any request attempting to add, modify relation types, or delete entries from `linkedReleases`, `linkedProjects`, or `packages` on a closed project MUST be rejected with HTTP `403 Forbidden` unless initiated by an `ADMIN` or `SW360_ADMIN`. Neither Project Team members nor Clearing Admins can modify dependencies.
* **Automated Merge Reference Updates:** When an administrator merges two Releases or Components, backend data handlers automatically update foreign key references in closed projects to preserve referential integrity without unlocking user-level edit permissions.

---

## 4. Executable Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: Project Responsible updates allowlisted fields in strict mode
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"alice"` who is listed as `projectResponsible` on the project
* **When** `"alice"` sends an update request changing `enableSvm` to `true`, `projectOwner` to `"bob@example.com"`, and setting `phaseOutSince`
* **Then** the update is accepted with HTTP `200 OK`
* **And** the updated fields are persisted in the database.

### Scenario 2: Clearing Admin (non-team member) updates allowlisted fields in strict mode
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"claire_clearing"` who has role `CLEARING_ADMIN` and is NOT listed on the project team
* **When** `"claire_clearing"` sends an update request updating `securityResponsibles` and `moderators`
* **Then** the update is accepted with HTTP `200 OK`
* **And** the updated fields are persisted in the database.

### Scenario 3: Project Owner attempts to update linked releases in strict mode (Disallowed)
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"bob"` who is listed as `projectOwner` on the project
* **When** `"bob"` sends an update request attempting to add a new release to `linkedReleases`
* **Then** the system rejects the update with HTTP `403 Forbidden`
* **And** no changes are made to `linkedReleases`
* **And** no moderation request is created.

### Scenario 4: Clearing Admin attempts to update linked dependencies in strict mode (Disallowed)
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"claire_clearing"` who has role `CLEARING_ADMIN`
* **When** `"claire_clearing"` attempts to modify `linkedReleases`, `linkedProjects`, or `packages`
* **Then** the request is rejected with HTTP `403 Forbidden`
* **And** dependencies remain unchanged.

### Scenario 5: Project Team member attempts to update non-allowlisted field (Disallowed)
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"carol"` who is listed as a `moderator` on the project
* **When** `"carol"` sends an update request attempting to modify the project `description` or `businessUnit`
* **Then** the system rejects the update with HTTP `403 Forbidden`
* **And** the project remains unchanged.

### Scenario 6: Admin updates linked dependencies on a closed project (Allowed)
* **Given** the configuration `projects.closed.update.strict` is set to `true`
* **And** a project `"smart-meter-firmware"` with clearing state `CLOSED`
* **And** user `"root_admin"` with role `ADMIN`
* **When** `"root_admin"` updates `linkedReleases`, `linkedProjects`, or `packages`
* **Then** the request is accepted with HTTP `200 OK`
* **And** the dependency changes are persisted.

---

## 5. Implementation & Traceability

- **Permission Utility:** `org.eclipse.sw360.datahandler.permissions.ProjectPermissions.isActionAllowed(...)`
- **Backend Service:** `org.eclipse.sw360.datahandler.thrift.projects.ProjectService.updateProject(...)`
- **Configuration Key:** `projects.closed.update.strict` in `sw360.properties`
- **Data Model:** `org.eclipse.sw360.datahandler.thrift.projects.Project`
- **Integration Tests:** `org.eclipse.sw360.datahandler.permissions.ClosedProjectStrictPermissionsTest`

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-09-04 | SW360 Core Team | Initial specification of closed project permissions and strict mode toggle |
| 2.0 | 2026-09-07 | Gaurav Mishra | Defined explicit 11 allowlisted fields for team updates, restricted full override to `ADMIN` only (excluding `CLEARING_ADMIN`), and enforced strict immutability on linked releases, sub-projects, and packages |
| 2.1 | 2026-09-07 | Gaurav Mishra | Extended allowlisted field update privileges to `CLEARING_ADMIN` (regardless of project team membership) in strict mode |
