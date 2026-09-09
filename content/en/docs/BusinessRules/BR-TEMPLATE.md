---
title: "Business Rule Specification Template"
linkTitle: "BR Template (SBVR/SBE)"
weight: 99
---

# Business Rule Specification Template

> **Template Version:** 1.0  
> **Standards Basis:** OMG SBVR / RuleSpeak® + Specification by Example (SBE) / ISO/IEC/IEEE 29148 + EARS

---

```yaml
---
id: "BR-[DOMAIN]-[NNN]"
title: "[Rule Title]"
domain: "[Projects | Components | Releases | Licenses | Clearing | Security]"
rule_type: "[Behavioral | Definitional | Constraint]"
status: "[Draft | Approved | Deprecated]"
governing_config: "[Optional configuration key or none]"
impacted_services:
  - "[ServiceName / Component]"
related_issues:
  - "[#IssueNumber]"
last_verified: "YYYY-MM-DD"
---
```

## 1. Executive Summary & Statement

### 1.1 Formal Statement (RuleSpeak® / EARS)
* **While** [precondition state, e.g. entity in status X],
* **If** [condition/trigger, e.g. configuration property Y is enabled],
* **Then** the system **shall** [allow/deny/execute specific behavior].
* **Otherwise**, the system **shall** [fallback / default behavior].

### 1.2 Purpose & Risk Mitigated
[Describe why this business rule exists, what business or operational risks it prevents, and the domain rationale.]

---

## 2. Business Vocabulary & Domain Definitions (SBVR)

| Term | Domain Concept & Meaning | Source Attribute / Field |
|---|---|---|
| **[Term 1]** | [Definition in SW360 context] | `entity.fieldName` |
| **[Term 2]** | [Definition in SW360 context] | `entity.fieldName` |

---

## 3. Detailed Specifications & Behavioral Invariants

### 3.1 Preconditions & Activation
- **Trigger Conditions:** [When does this rule take effect?]
- **Config Key / Feature Flag:** `[property.name]` (Default: `[true | false]`)

### 3.2 Authorization & Role Permissions Matrix
| Actor / Role | Conditions Met | Action Allowed | Side Effects / Fallback |
|---|---|---|---|
| **[Role A]** | [Condition] | [Allowed Operations / Fields] | [HTTP Status / Event] |
| **[Role B]** | [Condition] | [Allowed Operations / Fields] | [HTTP Status / Event] |

### 3.3 Cascading Side-Effects & System Invariants
- [Describe any automated backend jobs, merge cascades, synchronization hooks, or data updates triggered.]

---

## 4. Executable Acceptance Scenarios (Specification by Example / Gherkin)

### Scenario 1: [Positive Case Title]
- **Given** [initial state context]
- **And** [additional context or configuration]
- **When** [actor performs action]
- **Then** [expected successful outcome]
- **And** [expected state changes or side effects]

### Scenario 2: [Negative / Boundary Case Title]
- **Given** [initial state context]
- **And** [additional context or configuration]
- **When** [actor performs unauthorized or invalid action]
- **Then** [expected error status code / exception]
- **And** [expected absence of unwanted side effects, e.g. no moderation request created]

---

## 5. Implementation & Traceability

- **Backend Enforcement:** `[Path to service/class/method implementing the rule]`
- **Frontend / UI Handling:** `[Path to UI component/page displaying or constraining the action]`
- **REST API Endpoint:** `[HTTP Method + Path]`
- **Test References:** `[Link or name of unit / integration / JGiven test suite]`

---

## 6. Revision History

| Version | Date | Author | Description |
|---|---|---|---|
| 1.0 | YYYY-MM-DD | [Author Name] | Initial approved specification |
