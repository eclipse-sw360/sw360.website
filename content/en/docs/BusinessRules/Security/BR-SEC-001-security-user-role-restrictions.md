---
title: "BR-SEC-001: Security User Role & Token Scope REST Filter Restrictions"
linkTitle: "BR-SEC-001: Security User & Token Scopes"
weight: 10
id: "BR-SEC-001"
domain: "Security"
rule_type: "Behavioral"
status: "Approved"
governing_config: "EndpointsFilter"
impacted_services:
  - "EndpointsFilter"
  - "TokenService"
  - "PermissionUtils"
  - "ProjectPermissions"
last_verified: "2026-09-07"
---

# BR-SEC-001: Security User Role & Token Scope REST Filter Restrictions

> **Standard Classification:** Role Definition & Behavioral Constraint / Access Control  
> **Target Entity:** `User` (Role: `SECURITY_USER`), `Token` (Scopes: `READ`, `WRITE`), `Project`, `Vulnerability`, REST Endpoints  
> **Status:** Approved  
> **Enforcement Points:** Backend Permissions (`PermissionUtils`, `ProjectPermissions`) and Resource Server (`EndpointsFilter`)

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** an authenticated user has the role `SECURITY_USER`:
  * The system **shall grant read access** to **all** projects (including `PRIVATE` projects of any department or owner), but **only** to their **Summary** and **Vulnerabilities** information.
  * The system **shall deny access** to clearing, ECC (Export Control and Customs), compliance, attachments, and license obligations details for those projects.
  * The system **shall not allow** the user to create, modify, or delete core catalog entities across the system (strictly read-only role).
* **While** an incoming REST API request is authenticated via an API Token or initiated by a `SECURITY_USER`:
  * **If** the token possesses `READ` scope (or the authenticated user is `SECURITY_USER`):
    * The REST API Gateway (`EndpointsFilter`) **shall intercept and block** all HTTP `POST`, `PUT`, `PATCH`, and `DELETE` requests with HTTP `503 Service Unavailable` / `403 Forbidden`.
    * **Otherwise**, the gateway **shall allow** safe non-mutating query endpoints and self-service token lifecycle operations:
      1. `POST /api/releases/batch-summary` (Batch data retrieval requiring a JSON request payload).
      2. `POST /api/users/tokens` (Self-service generation of `READ` or `WRITE` scoped user API tokens from the UI/client).
      3. `DELETE /api/users/tokens` (Self-service revocation and cleanup of the user's own API tokens).
  * **If** the token possesses `WRITE` scope and the user is not `SECURITY_USER`, the system **shall permit** standard HTTP mutation verbs (`POST`, `PUT`, `PATCH`, `DELETE`) subject to standard domain permission checks.

### 1.2 Purpose & Risk Mitigated
The `SECURITY_USER` role and `READ` token scopes allow automated security scanners, audit tools, and read-only integrations global visibility into vulnerabilities and security posture across the entire organization's software catalog without exposure to proprietary project internals, compliance data, or the ability to alter database records. Enforcing strict read-only behavior at the HTTP filter level guarantees defense-in-depth against unauthorized mutation attempts while explicitly allowing batch query POST requests and self-service token generation and revocation (to ensure users can manage their own security credentials and immediately invalidate compromised tokens).

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Meaning | Implementation Reference |
|---|---|---|
| **Security User** | A global read-only role dedicated to vulnerability analysis across all projects. | `UserRole.SECURITY_USER` |
| **Token Scope (READ)** | Restricts the client token strictly to query/read operations; blocks entity-mutating HTTP methods. | `Token.Scope.READ` |
| **Token Scope (WRITE)** | Allows state mutation and creation within the bounds of the user's role permissions. | `Token.Scope.WRITE` |
| **Self-Service Token Lifecycle** | Creation (`POST`) and immediate revocation (`DELETE`) of personal API credentials. | `/api/users/tokens` |
| **Limited Project View** | Access restricted strictly to project summary metadata and security vulnerability lists; proprietary licensing/ECC hidden. | `ProjectPermissions.isVisible(...)` |
| **REST Write Filter** | Servlet filter that inspects incoming requests and blocks write operations for security users and `READ`-scoped tokens. | `org.eclipse.sw360.rest.resourceserver.filter.EndpointsFilter` |
| **Filter Whitelist Exemption** | Endpoints permitted through the filter regardless of read-only status (batch queries and self token management). | `POST /api/releases/batch-summary`, `POST /api/users/tokens`, `DELETE /api/users/tokens` |

---

## 3. Specifications & Behavioral Invariants

### 3.1 Permissions Matrix for `SECURITY_USER` & Token Scopes

| Domain / Resource | Operation / Verb | `SECURITY_USER` | `READ` Token Scope | `WRITE` Token Scope | Notes / Constraints |
|---|---|---|---|---|---|
| **Projects (Public, BU, Private)** | `GET` Summary & Vulnerabilities | **Allowed** | **Allowed** | **Allowed** | Can view vulnerability tracking and summary metadata across projects |
| **Projects (All)** | `GET` Clearing, ECC, Licenses | **Denied** | Subject to user role | Subject to user role | Clearing reports and obligations hidden from `SECURITY_USER` |
| **Core Entities** (Projects, Components, Releases) | `POST`, `PUT`, `PATCH`, `DELETE` | **Denied** (503/403) | **Denied** (503/403) | **Allowed** | Blocked at `EndpointsFilter` for `READ` tokens / `SECURITY_USER` |
| **Batch Summary** (`/api/releases/batch-summary`) | `POST` (Body: Release IDs) | **Allowed** | **Allowed** | **Allowed** | Exemption: Read-only query requiring body payload |
| **Token Generation** (`/api/users/tokens`) | `POST` (Create Token) | **Allowed** | **Allowed** | **Allowed** | Exemption: Self-service UI / client token creation |
| **Token Revocation** (`/api/users/tokens`) | `DELETE` (Revoke Token) | **Allowed** | **Allowed** | **Allowed** | Exemption: Self-service token revocation for credential security |
| **Vulnerabilities** | Suppress / Modify findings | **Denied** | **Denied** | Subject to `SECURITY_ADMIN` | Modification requires `SECURITY_ADMIN` |

### 3.2 REST Endpoint Filter Rules (`EndpointsFilter`)

* **Default Write Blocker:** Any request with HTTP method `POST`, `PUT`, `PATCH`, or `DELETE` initiated by a `SECURITY_USER` or a token with `READ` scope is intercepted and rejected before hitting service controllers.
* **Filter Whitelist Exemptions:**
  1. **Batch Summary Endpoint:** `POST /api/releases/batch-summary` is permitted because it functions as an idempotent batch query where IDs are transmitted in the HTTP body.
  2. **Self-Service Token Creation:** `POST /api/users/tokens` is permitted to allow authenticated clients and UI sessions to generate new API access tokens.
  3. **Self-Service Token Revocation:** `DELETE /api/users/tokens` (and sub-paths) is permitted to ensure clients and users can immediately revoke compromised or expired credentials.

---

## 4. Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: Security user views vulnerabilities of a private project
* **Given** a user `"sec_auditor"` assigned role `SECURITY_USER`
* **And** a project `"secret-ai-platform"` with visibility `PRIVATE` owned by user `"dev_lead"`
* **When** `"sec_auditor"` requests the summary and vulnerability list for `"secret-ai-platform"`
* **Then** the request is accepted with HTTP `200 OK`
* **And** the vulnerabilities data is returned.

### Scenario 2: READ-scoped token executes batch summary retrieval via POST
* **Given** an API token generated with scope `READ`
* **When** the client sends an HTTP `POST` request to `/api/releases/batch-summary` with a list of release IDs in the JSON payload
* **Then** the request passes `EndpointsFilter`
* **And** the release summaries are returned with HTTP `200 OK`.

### Scenario 3: User creates a new API Token via self-service endpoint
* **Given** an authenticated user or client session with `READ` access
* **When** the client sends an HTTP `POST` request to `/api/users/tokens` with token metadata (name and requested scope)
* **Then** `EndpointsFilter` allows the request through
* **And** the server generates the token and responds with HTTP `201 Created` (or `200 OK`).

### Scenario 4: User revokes an API Token via self-service endpoint
* **Given** an authenticated user or client session with `READ` access
* **When** the client sends an HTTP `DELETE` request to `/api/users/tokens?name=token-uuid-1234`
* **Then** `EndpointsFilter` allows the request through
* **And** the server revokes the token and responds with HTTP `204 No Content`.

### Scenario 5: READ-scoped token attempts to modify or delete a component/project
* **Given** an API token generated with scope `READ`
* **When** the client sends an HTTP `DELETE` request to `/api/projects/proj-123`
* **Then** `EndpointsFilter` intercepts and blocks the request
* **And** the server responds with HTTP `503 Service Unavailable` (or `403 Forbidden`)
* **And** no entity is deleted from the database.

---

## 5. Implementation & Traceability

- **Resource Server Filter:** `org.eclipse.sw360.rest.resourceserver.filter.EndpointsFilter`
- **Permissions Helper:** `org.eclipse.sw360.datahandler.permissions.PermissionUtils.isSecurityUser(...)`
- **Token Controller / Service:** `org.eclipse.sw360.rest.resourceserver.user.UserController` / `TokenService`
- **REST Endpoints:**
  - `POST /api/releases/batch-summary`
  - `POST /api/users/tokens`
  - `DELETE /api/users/tokens`
- **Administration Guide:** [Administration Guide: User Management & Roles](../../AdministrationGuide/user-management-roles.md)

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-09-05 | SW360 Core Team | Initial specification of `SECURITY_USER` role, read scope, and EndpointsFilter POST exemption |
| 1.1 | 2026-09-07 | Gaurav Mishra | Added token scope (`READ`/`WRITE`) enforcement, `POST /api/users/tokens` self-service exemption, and `POST /api/releases/batch-summary` exemption |
| 1.2 | 2026-09-07 | Gaurav Mishra | Added `DELETE /api/users/tokens` exemption for self-service token revocation and security lifecycle management |
