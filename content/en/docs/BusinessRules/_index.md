---
title: "Business Rules"
linkTitle: "Business Rules"
weight: 7
icon: fas fa-scale-balanced
description: >
  SW360 Domain & Business Rules Specification Catalog based on OMG SBVR, RuleSpeak, and Specification by Example (SBE).
---

# SW360 Business Rules & Domain Specifications

This section serves as the authoritative, machine- and human-readable catalog of
functional domain constraints, business policies, and invariant behaviors
implemented across SW360.

While **[Architecture Decision Records (ADRs)](../Architecture/decisions)**
capture *why* specific architectural and technical stack decisions were chosen
(based on Arc42 / DAR), **Business Rules (BRs)** document the exact domain
requirements, behavioral policies, permission constraints, and side-effects that
govern SW360 entities (Projects, Components, Releases, Licenses, Clearing, and
Security).

---

## 1. Standards Foundation

Each SW360 Business Rule follows a formalized specification model combining:

1. **OMG SBVR & RuleSpeak® Notation:** For formal, unambiguous rule definitions
   and operative policy statements.
2. **EARS (Easy Approach to Requirements Syntax):** For clear state-, event-,
   and trigger-driven condition patterns.
3. **Specification by Example (SBE) & Gherkin (`Given-When-Then`):** For clear
   developer understanding and automated test-case generation by developers and
   AI agents.
4. **Visual Diagrams (Optional / Mermaid):** Diagrams should only be added when
   strictly necessary to clarify complex workflows or state machines. When included,
   they must be formatted as standard Mermaid diagrams (`flowchart`, `stateDiagram-v2`).

---

## 2. Rule Identification & Domains

Rules are uniquely identified using the scheme `BR-<DOMAIN>-<NNN>`:

| Domain Prefix | Subject Area | Description |
|---|---|---|
| `BR-PROJ-` | **Projects** | Project lifecycle, clearing states, hierarchy, visibility, and access control |
| `BR-COMP-` | **Components** | Component cataloging, metadata consistency, merging, and ownership |
| `BR-REL-` | **Releases** | Release lifecycle, source bundle handling, and license associations |
| `BR-LIC-` | **Licenses & Obligations** | License compatibility, obligation fulfillment, and profile rules |
| `BR-CLR-` | **Clearing Workflows** | Clearing states, requests, FOSSology integration, and report generation |
| `BR-SEC-` | **Security & Vulnerabilities** | SVM synchronization, vulnerability assessment, and CVE relevance |

---

## 3. Business Rule Catalog

### Projects (`BR-PROJ`)

| ID | Title | Governing Configuration | Status |
|---|---|---|---|
| [BR-PROJ-001](./Projects/BR-PROJ-001-closed-project-restrictions.md) | **Closed Project Update Restrictions** | `projects.closed.update.strict` | Approved |
| [BR-PROJ-002](./Projects/BR-PROJ-002-license-clearing-tab-badges.md) | **License Clearing Tab Status Badges** | `LicenseClearing.tsx` | Approved |

### Clearing (`BR-CLR`)

| ID | Title | Governing Configuration | Status |
|---|---|---|---|
| [BR-CLR-001](./Clearing/BR-CLR-001-release-clearing-state-determination.md) | **Release Clearing State Determination & Manual Transitions** | `ReleaseService` | Approved |

### Security (`BR-SEC`)

| ID | Title | Governing Configuration | Status |
|---|---|---|---|
| [BR-SEC-001](./Security/BR-SEC-001-security-user-role-restrictions.md) | **Security User Role & REST Filter Restrictions** | `EndpointsFilter` | Approved |

---

## 4. Contributing New Rules

When documenting newly discovered invariants or creating functional specifications for new features:
1. Copy the [Business Rule Specification Template](./BR-TEMPLATE.md).
2. Adhere to the `Given-When-Then` test scenario structure to allow direct
   verification by test automation and AI agents.
3. Avoid unnecessary diagrams; include Mermaid diagrams only if they simplify complex decision branching or multi-state transitions.
