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
last_verified: "2026-09-04"
---

# BR-PROJ-001: Closed Project Update Restrictions

> **Standard Classification:** Behavioral Constraint / Access Control  
> **Target Entity:** `Project`  
> **Status:** Approved  
> **Governing Configuration:** `projects.closed.update.strict` (Default: `false`)

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** a Project has clearing state `CLOSED` (`project.clearingState == ProjectClearingState.CLOSED`):
  * **If** `projects.closed.update.strict` is `false`, **then** the system **shall allow** users with role `CLEARING_ADMIN` (or above) as well as the project team (Creator, Project Responsible, Moderators, Contributors, and Lead Architects) to modify all fields of the project.
  * **If** `projects.closed.update.strict` is `true`, **then** the system **shall allow** only `CLEARING_ADMIN` (or above) to modify all fields. The project team (Creator, Project Responsible, Moderators, Contributors, and Lead Architects) **shall only be allowed** to modify the allowlisted maintenance fields:
    1. **Project State** (`state`, project status, not clearing state)
    2. **Project Responsibles** (`projectResponsible`)
    3. **Project Owner** (`projectOwner`)
    4. **Security Responsible** (`securityResponsible`)
    5. **Enable Security Vulnerability Monitoring** (`securityVulnerabilitiesMonitoring`)
    6. **Display Vulnerabilities** (`displayVulnerabilities`)
    7. **Phase-out date** (`phaseOutDate`)
    8. **External IDs** (`externalIds`)
  * **If** any other user attempts an update, or if a restricted user attempts to modify non-allowlisted fields in strict mode, the system **shall reject** the request with HTTP `403 Forbidden` and **shall not** generate any moderation request.

### 1.2 Purpose & Risk Mitigated
This restriction is enforced strictly for **audit and compliance purposes**. A project is transitioned into the **CLOSED** clearing state only after its license clearing process is fully completed and approved. Once in the closed state, no changes that could result in a **drift of license clearing** (such as unauthorized modifications, additions, or removals of components, releases, attachments, or license obligations) shall be allowed. This guarantees that the cleared and certified baseline remains immutable and audit-compliant, while still permitting non-clearing operational lifecycle maintenance (e.g., updating security contacts, phase-out dates, or project ownership).

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Meaning | Field / Attribute Reference |
|---|---|---|
| **Closed Project** | A project whose license clearing process has finished and has been marked as completed. | `Project.clearingState == CLOSED` |
| **Project Team** | The collective set of users assigned administrative or collaborative ownership of the project. | `creator`, `projectOwner`, `projectResponsible`, `moderators`, `contributors`, `leadArchitect` |
| **Strict Closed Mode** | System operational mode enforcing a strict allowlist of editable maintenance fields for closed projects. | `projects.closed.update.strict` in `SW360_CONFIGURATION` |
| **Project State** | The operational lifecycle phase of the project (e.g., Active, Phase-out), distinct from the clearing state. | `Project.state` |

---

## 3. Specifications & Behavioral Invariants

### 3.1 Permissions Matrix by Configuration Mode

| Actor Role | `projects.closed.update.strict = false` | `projects.closed.update.strict = true` | Enforcement Result on Disallowed Update |
|---|---|---|---|
| **Admin / Clearing Admin** | Can modify **all** fields | Can modify **all** fields | — |
| **Project Team** (Creator, Project Responsible, Owner, Moderator, Contributor, Lead Architect) | Can modify **all** fields | Can **only** modify the 8 allowlisted fields | `403 Forbidden` (No moderation request created) |
| **Other Registered Users** | Update denied | Update denied | `403 Forbidden` (No moderation request created) |

### 3.2 System Invariant: Component/Release Merges
* **Automatic Reference Updates:** If an administrator or user merges two Components or Releases, and the source entity is referenced by a closed project, the backend **shall force-update** the reference in the closed project automatically to prevent broken references, bypassing user-level update restrictions.

---

## 4. Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: Project Responsible updates lifecycle and contacts in strict mode
* **Given** a project with ID `"proj-123"` having `clearingState = CLOSED`
* **And** configuration property `projects.closed.update.strict` is set to `true`
* **And** user `"alice"` is defined as `projectResponsible` for `"proj-123"`
* **When** `"alice"` submits an update changing `phaseOutDate = "2028-12-31"` and `securityResponsible = "bob@example.com"`
* **Then** the update is accepted with status code `200 OK`
* **And** the project record reflects the updated `phaseOutDate` and `securityResponsible`.

### Scenario 2: Contributor attempts editing dependencies in strict mode
* **Given** a project with ID `"proj-123"` having `clearingState = CLOSED`
* **And** configuration property `projects.closed.update.strict` is set to `true`
* **And** user `"carol"` is a `contributor` on `"proj-123"`
* **When** `"carol"` attempts to add a new release to the project's linked releases
* **Then** the request is rejected with status code `403 Forbidden`
* **And** no moderation request is generated in the system.

### Scenario 3: Non-team member attempts update in non-strict mode
* **Given** a project with ID `"proj-123"` having `clearingState = CLOSED`
* **And** configuration property `projects.closed.update.strict` is set to `false`
* **And** user `"dave"` is a regular user not listed in the project team and not a Clearing Admin
* **When** `"dave"` attempts to update the project description
* **Then** the request is rejected with status code `403 Forbidden`
* **And** no moderation request is generated in the system.

### Scenario 4: Automated merge cascade on closed project
* **Given** a project `"proj-123"` with `clearingState = CLOSED` referencing Release `"rel-v1.0"`
* **When** an administrator merges Release `"rel-v1.0"` into `"rel-v1.0-final"`
* **Then** the backend updates `"proj-123"` to point to `"rel-v1.0-final"`
* **And** the project's `clearingState` remains `CLOSED`.

---

## 5. Traceability & References

- **User & Admin Docs:** [Administration Guide: User Management & Roles](../../AdministrationGuide/user-management-roles.md#projects-closed)
- **Configuration Reference:** [Deployment: Configuration Files](../../Deployment/Deploy-Configuration-Files.md#sw360-container-backend)
- **Architecture Model:** [Development: Role Authorization Model](../../Development/Dev-Role-Authorisation-Model.md)
- **Implementation Classes:** `com.siemens.sw360.datahandler.permissions.ProjectPermissions`, `ProjectService`

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-09-04 | SW360 Core Team | Initial formalization of closed project update restrictions and 8 allowlisted fields |
