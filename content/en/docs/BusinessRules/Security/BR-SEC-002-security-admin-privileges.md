---
title: "BR-SEC-002: ECC Admin Role Privileges & Moderation Bypass"
linkTitle: "BR-SEC-002: ECC Admin Privileges"
weight: 20
id: "BR-SEC-002"
domain: "Security"
rule_type: "Behavioral"
status: "Approved"
governing_config: "none"
impacted_services:
  - "PermissionUtils"
  - "ModerationService"
  - "ComponentPermissions"
  - "ReleasePermissions"
  - "AttachmentService"
last_verified: "2026-09-07"
---

# BR-SEC-002: ECC Admin Role Privileges & Moderation Bypass

> **Standard Classification:** Role Definition & Authorization Invariant  
> **Target Entity:** `User` (Role: `ECC_ADMIN`), `Component`, `Release`, `Attachment`, `ModerationRequest`  
> **Status:** Approved  
> **Enforcement Points:** Backend Permissions (`PermissionUtils`, `ComponentPermissions`, `ReleasePermissions`) and Moderation Layer (`ModerationService`)

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** an authenticated user possesses the role `ECC_ADMIN`:
    * The system **shall allow** the user to update Export Control and Customs (ECC) metadata fields on **any** `Release` across the entire catalog, regardless of project/release ownership, visibility, or restriction states.
    * **When** the user uploads an `Attachment` to any `Component` or `Release`:
        * The system **shall persist** the attachment directly to the target entity.
        * The system **shall bypass** the moderation workflow (no `ModerationRequest` shall be generated or required for attachment additions).
    * **Otherwise** (for non-ECC field updates on components or releases where the user is not an owner or moderator), the system **shall continue to enforce** standard moderation or access constraints.
    * The system **shall prohibit** the `ECC_ADMIN` from modifying the verification status (`checkStatus` -> `ACCEPTED` / `REJECTED`) of any uploaded attachment.

### 1.2 Purpose & Risk Mitigated
ECC (Export Control and Customs) officers require unhindered authority to inspect, classify, and certify compliance data and technical documentation (e.g., ECCN classification sheets, cryptographic questionnaires, export licenses)
across all software components and releases. Granting direct attachment upload rights without moderation overhead eliminates operational bottlenecks during compliance audits while maintaining data integrity by scoping write privileges strictly to ECC data and audit-supporting artifacts.

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Meaning | Implementation Reference |
|---|---|---|
| **ECC Admin** | Global administrative role responsible for export control classification and customs compliance. | `UserRole.ECC_ADMIN` |
| **ECC Information** | Export Control and Customs classification metadata (e.g., AL, ECCN, ECC status, cryptographic indicators). | `Release.eccInformation` |
| **Moderation Request** | Approval ticket generated when an unauthorized/non-owner user attempts to modify a catalog entity. | `ModerationRequest` |
| **Moderation Bypass** | Direct write/persistence execution without creating a pending moderation entry. | `ModerationService.requiresModeration(...) == false` |
| **Target Entities** | Structural catalog assets accepting compliance artifacts. | `Component`, `Release` |

---

## 3. Specifications & Behavioral Invariants

### 3.1 Permissions & Moderation Matrix for `ECC_ADMIN`

| Entity | Action / Target Field | Standard User (Non-Owner) | `ECC_ADMIN` | Moderation Triggered? |
|---|---|---|---|---|
| **Release** | Update ECC Metadata (`eccInformation`) | Restricted / Moderated | **Allowed (Direct)** | No |
| **Release** | Update Non-ECC Core Fields (Name, Version, Vendors) | Moderation Required | Moderation Required | Yes |
| **Release** | Upload / Add `Attachment` | Moderation Required | **Allowed (Direct)** | **No (Bypassed)** |
| **Component** | Update General Metadata | Moderation Required | Moderation Required | Yes |
| **Component** | Upload / Add `Attachment` | Moderation Required | **Allowed (Direct)** | **No (Bypassed)** |
| **Release / Component** | Delete Entity | Denied / Moderated | Denied / Moderated | Yes |
| **Attachment** | Update `checkStatus` (Approve / Reject) | Denied | **Denied** | No (Strictly prohibited) |

### 3.2 Authorization Rules

1. **Global ECC Scope:** Write permissions for `release.eccInformation` evaluate to `true` globally when `isUserAtLeast(UserGroup.ECC_ADMIN)`.
2. **Direct Attachment Persistence:** The moderation check `ModerationService.isModerationRequiredForAttachment(user, entity)` must evaluate to `false` for `ECC_ADMIN` on both `Component` and `Release` entities.
3. **Core Entity Protection:** Direct edits to core release metadata (outside `eccInformation` and attachments) remain guarded by standard ownership and moderation rules.

---

## 4. Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: ECC Admin directly updates ECC fields on a restricted release
* **Given** an authenticated user `"ecc_officer"` with role `ECC_ADMIN`
* **And** a release `"crypto-engine-2.4"` where `"ecc_officer"` is neither creator nor contributor
* **When** `"ecc_officer"` updates the ECC classification details (e.g., `al = "5D002"`, `eccn = "5E002"`)
* **Then** the changes are committed directly to the database
* **And** no `ModerationRequest` is created.

### Scenario 2: ECC Admin uploads an attachment to a Component without moderation
* **Given** an authenticated user `"ecc_officer"` with role `ECC_ADMIN`
* **And** a component `"apache-commons-codec"` owned by another department
* **When** `"ecc_officer"` uploads a compliance document `"crypto_declaration.pdf"` to the component
* **Then** the attachment is immediately persisted and associated with the component
* **And** the operation completes with HTTP `200 OK` (or `201 Created`)
* **And** no moderation request is generated in the moderation queue.

### Scenario 3: ECC Admin uploads an attachment to a Release without moderation
* **Given** an authenticated user `"ecc_officer"` with role `ECC_ADMIN`
* **And** a release `"lib-ssl-1.1"` in status `APPROVED` owned by a separate project team
* **When** `"ecc_officer"` uploads an export classification document `"eccn_matrix.xlsx"` to the release
* **Then** the attachment is attached directly to `"lib-ssl-1.1"`
* **And** no moderation workflow is initiated.

### Scenario 4: Standard user attempts attachment upload on non-owned release (Contrast)
* **Given** an authenticated user `"regular_dev"` with role `USER` (not `ECC_ADMIN` or owner)
* **When** `"regular_dev"` uploads an attachment to release `"lib-ssl-1.1"`
* **Then** the system creates a pending `ModerationRequest`
* **And** the attachment is not visible as an approved release document until approved by a moderator.

### Scenario 5: ECC Admin attempts to modify core release metadata (Boundary)
* **Given** an authenticated user `"ecc_officer"` with role `ECC_ADMIN`
* **When** `"ecc_officer"` attempts to rename the release or alter its main source code repository URL on a non-owned release
* **Then** the system routes the request through the standard moderation workflow
* **And** a `ModerationRequest` is created for project moderator review.

### Scenario 6: ECC Admin cannot approve or reject attachments (Negative Case)
* **Given** an authenticated user `"ecc_officer"` with role `ECC_ADMIN`
* **And** an attachment `"eccn_matrix.xlsx"` associated with release `"lib-ssl-1.1"` in status `UNCHECKED`
* **When** `"ecc_officer"` attempts to set `checkStatus` to `ACCEPTED` or `REJECTED`
* **Then** the request is rejected with HTTP `403 Forbidden`
* **And** the attachment status remains unchanged.

---

## 5. Implementation & Traceability

- **Permissions Utility:** `org.eclipse.sw360.datahandler.permissions.PermissionUtils.isEccAdmin(User user)`
- **Component Permissions:** `org.eclipse.sw360.datahandler.permissions.ComponentPermissions`
- **Release Permissions:** `org.eclipse.sw360.datahandler.permissions.ReleasePermissions`
- **Moderation Handler:** `org.eclipse.sw360.moderation.ModerationService.isModerationRequired(...)`
- **Data Models:**
    - `org.eclipse.sw360.datahandler.thrift.users.UserRole.ECC_ADMIN`
    - `org.eclipse.sw360.datahandler.thrift.components.Release`
    - `org.eclipse.sw360.datahandler.thrift.attachments.Attachment`
- **Integration Tests:** `org.eclipse.sw360.datahandler.permissions.EccAdminPermissionsTest`

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-09-07 | Gaurav Mishra | Formalized ECC Admin role permissions: global ECC updates and moderation bypass for component/release attachments |
