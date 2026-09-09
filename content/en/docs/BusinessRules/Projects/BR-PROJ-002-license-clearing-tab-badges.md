---
title: "BR-PROJ-002: License Clearing Tab Status Badges & Color Representation"
linkTitle: "BR-PROJ-002: License Clearing UI Badges"
weight: 20
id: "BR-PROJ-002"
domain: "Projects"
rule_type: "Definitional"
status: "Approved"
governing_config: "none"
impacted_services:
  - "ProjectDetailsView"
  - "LicenseClearingPortlet"
  - "ReleaseClearingBadgeComponent"
last_verified: "2026-09-07"
---

# BR-PROJ-002: License Clearing Tab Status Badges & Color Representation

> **Standard Classification:** Definitional Rule / UI Presentation Invariant  
> **Target Entity:** `Project`, `Release`, Project Details UI (`License Clearing` Tab)  
> **Status:** Approved  
> **Enforcement Points:** Frontend UI Views (`ListView.tsx`, `TreeView.tsx`)

---

## 1. Executive Summary & Formal Statements

### 1.1 Formal Statement (RuleSpeak® / EARS)

* **While** an authenticated user is viewing an accessible `Project` in details mode under the **License Clearing** tab:
    * The system **shall render** a hierarchical table displaying all linked releases (direct and transitive sub-project releases).
    * The system **shall display** state indicator badges with abbreviations:
        * `(PS)` for **Project Clearing State**.
        * `(CS)` for **Release Clearing State**.
    * **When** rendering the `(PS)` badge for a project row, the system **shall apply** the exact background color mapped to the project clearing state:
        * `Closed` $\rightarrow$ **Green** (`#68C17C`)
        * `In-progress` $\rightarrow$ **Yellow** (`#FFD351`)
        * `Open` $\rightarrow$ **Red** (`#E6717C`)
        * `Not Applicable` / `Unknown` $\rightarrow$ **Grey** (`#DEE2E6`)
    * **When** rendering the `(CS)` badge for a release row, the system **shall apply** the exact background color mapped to the release clearing state:
        * `NEW_CLEARING` $\rightarrow$ **Red** (`#E6717C`)
        * `UNDER_CLEARING` $\rightarrow$ **Yellow** (`#FFD350`)
        * `SENT_TO_CLEARING_TOOL` or `SCAN_AVAILABLE` $\rightarrow$ **Orange** (`#F7941E`)
        * `REPORT_AVAILABLE` $\rightarrow$ **Blue** (`#0D6EFD`)
        * `INTERNAL_USE_SCAN_AVAILABLE` $\rightarrow$ **Purple** (`#9370DB`)
        * `APPROVED` $\rightarrow$ **Green** (`#69C17D`)
        * `null`, `undefined`, or unmapped $\rightarrow$ **Grey** (`#DEE2E6`)
    * **When** a user hovers over any `(PS)` or `(CS)` badge, the system **shall render a tooltip** displaying the full, human-readable state name.

### 1.2 Purpose & Risk Mitigated
Compact color-coded badge representations allow project managers, architects, and clearing officers to assess compliance and clearing readiness across deeply nested dependency trees at a single glance. Standardizing the color mappings prevents misinterpretation of clearing risk across different pages and ensures accessibility via hover tooltips.

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Concept & Meaning | UI / Model Reference |
|---|---|---|
| **License Clearing Tab** | Project details view aggregating all direct and indirect dependencies for compliance evaluation. | `LicenseClearing.tsx` |
| **PS Badge** | Visual UI pill/button representing Project Clearing State (`ProjectClearingState`). | Badge element `(PS)` |
| **CS Badge** | Visual UI pill/button representing Release Clearing State (`ClearingState`). | Badge element `(CS)` |
| **State Tooltip** | Hover overlay providing the unabbreviated domain state string. | `title` / `data-bs-toggle="tooltip"` |

---

## 3. Detailed Specifications & Behavioral Invariants

### 3.1 Project Row `(PS)` Badge Color Mappings

| Indicator | Domain State | Visual Color | Hex Code | Tooltip Display Text |
|---|---|---|---|---|
| **PS** | `CLOSED` | Green | `#68C17C` | "Closed" |
| **PS** | `IN_PROGRESS` | Yellow | `#FFD351` | "In-progress" |
| **PS** | `OPEN` | Red | `#E6717C` | "Open" |
| **PS** | `NOT_APPLICABLE` / `UNKNOWN` | Grey | `#DEE2E6` | "Not Applicable" |

### 3.2 Release Row `(CS)` Badge Color Mappings

| Release Clearing State Enum | Visual Color | Hex Code | Tooltip Display Text |
|---|---|---|---|
| `NEW_CLEARING` | Red | `#E6717C` | "New Clearing" |
| `UNDER_CLEARING` | Yellow | `#FFD350` | "Under Clearing" |
| `SENT_TO_CLEARING_TOOL` | Orange | `#F7941E` | "Sent to Clearing Tool" |
| `SCAN_AVAILABLE` | Orange | `#F7941E` | "Scan Available" |
| `REPORT_AVAILABLE` | Blue | `#0D6EFD` | "Report Available" |
| `INTERNAL_USE_SCAN_AVAILABLE` | Purple | `#9370DB` | "Internal Use Scan Available" |
| `APPROVED` | Green | `#69C17D` | "Approved" |
| *Fallback / Unknown / Null* | Grey | `#DEE2E6` | "Unknown" |

---

## 4. Executable Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: Rendering release in APPROVED state
* **Given** a project containing release `"openssl-3.0.8"`
* **And** `"openssl-3.0.8"` has clearing state `APPROVED`
* **When** the user navigates to the "License Clearing" tab
* **Then** the `(CS)` badge for `"openssl-3.0.8"` is rendered with background color `#69C17D` (Green)
* **And** hovering on the badge displays tooltip `"Approved"`.

### Scenario 2: Rendering release in SCAN_AVAILABLE or SENT_TO_CLEARING_TOOL state
* **Given** a project containing release `"curl-8.1.0"` with clearing state `SCAN_AVAILABLE`
* **And** release `"zlib-1.2.13"` with clearing state `SENT_TO_CLEARING_TOOL`
* **When** the user views the "License Clearing" tab
* **Then** both releases display an `(CS)` badge with background color `#F7941E` (Orange)
* **And** hovering over `"curl-8.1.0"` displays tooltip `"Scan Available"`
* **And** hovering over `"zlib-1.2.13"` displays tooltip `"Sent to Clearing Tool"`.

### Scenario 3: Rendering release in INTERNAL_USE_SCAN_AVAILABLE state
* **Given** a project containing release `"internal-helper-2.0"` with clearing state `INTERNAL_USE_SCAN_AVAILABLE`
* **When** the user views the "License Clearing" tab
* **Then** the `(CS)` badge is rendered with background color `#9370DB` (Purple)
* **And** hovering on the badge displays tooltip `"Internal Use Scan Available"`.

### Scenario 4: Handling unmapped or null clearing states
* **Given** a release record with a `null` or unrecognized clearing state
* **When** the table row is rendered in the "License Clearing" tab
* **Then** the `(CS)` badge is rendered with background color `#DEE2E6` (Grey)
* **And** the tooltip displays `"Unknown"`.

---

## 5. Implementation & Traceability

- **Frontend View:** `src/app/[locale]/projects/detail/[id]/components/LicenseClearing.tsx` (`ListView` and `TreeView` components rendered by this)
- **Data Models:**
    - `org.eclipse.sw360.datahandler.thrift.projects.ProjectClearingState`
    - `org.eclipse.sw360.datahandler.thrift.components.ClearingState`

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | 2026-09-07 | Gaurav Mishra | Formalized visual badge mapping, color palette hex codes, and tooltip presentation invariants for Project and Release states |
