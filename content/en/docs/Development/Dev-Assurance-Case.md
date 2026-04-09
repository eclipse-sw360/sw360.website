---
title: "Assurance Case"
linkTitle: "Assurance Case"
weight: 50
description: "Security assurance case for SW360."
---

# SW360 Security Assurance Case

This document provides a formal justification for why the SW360 project's
security requirements are met. It serves as a comprehensive "argument for
security" based on design, tools, and processes.

## 1. Threat Model & Trust Boundaries

### Assets to Protect
- **Intellectual Property**: Component data, license information, and project
  metadata.
- **System Integrity**: The correctness of moderation requests and project
  status, ensured through **audit trails and changelogs** for all records.
- **Availability**: Continuous access for organizational software compliance.

### Trust Boundaries
1. **User/System Boundary**: The point where external users (or automated
   clients) interact with the SW360 Frontend or REST layer (Authorization and
   Resource Servers).
2. **Frontend/Backend Boundary**: The interaction between the Next.js
   application and the REST layer services.
3. **Internal service Boundary**: Communication between the REST layer and the
   business logic (Thrift).
4. **Data layer Boundary**: Interaction between the backend services and the
   CouchDB database.

## 2. Secure Design Application
As detailed in [Secure Design](./Dev-Secure-Design.md), the project strictly
follows:
- **Least Privilege**: Ensured via RBAC and record-level permissions.
- **Fail-safe Defaults**: All actions are denied by default.
- **Complete Mediation**: All requests are checked by the Authorization Server.

## 3. Countermeasures for Common Weaknesses

The project implements specific countermeasures against the **OWASP Top 10** and
other common vulnerabilities:

### A. Broken Access Control
- **Countermeasure**: Centralized authorization check in every REST controller
  and enforced record-level visibility in the DB layer.

### B. Cryptographic Failures
- **Countermeasure**: Mandatory TLS for all external communication. Secure
  storage of secrets using environment variables (no hardcoded secrets).

### C. Injection (SQL, NoSQL, CMD)
- **Countermeasure**: Use of CouchDB (which is not susceptible to standard SQLi)
  and strict input validation/sanitization in the backend services.

### D. Insecure Design
- **Countermeasure**: This assurance case and the
  [Secure Design](./Dev-Secure-Design.md) document certify that security was a
  primary consideration, not an afterthought.

### E. Security Misconfiguration
- **Countermeasure**: Automated dependency monitoring via **Dependabot** and
  static analysis via **CodeQL** to identify misconfigurations in code or
  dependencies.

### F. Vulnerable and Outdated Components
- **Countermeasure**: Dependencies are maintained in **machine-readable
  formats** (Maven POM, package.json), enabling continuous monitoring for known
  vulnerabilities. Tools like **Dependabot** are used to provide automated
  alerts and updates.

## 4. Verification & Validation

### Static Analysis
Continuous integration (CI) includes:
- **CodeQL**: For identifying security vulnerabilities and code quality issues.
- **Checkstyle**: To ensure adherence to coding standards.

### Dynamic Analysis
- Deployment testing via Docker ensures that security configurations (like CORS
  and OAuth2 flows) work correctly in a production-like environment.

### External and Community Reviews
- **Public Code Review**: Every change to the codebase MUST be proposed via a
  **public Pull Request**. This process is transparent, recorded, and requires
  explicit review and approval from project maintainers.
- **Security Audits**: The project has undergone external security reviews and
  penetration testing (e.g., Siemens AG review in Feb 2026), with findings
  incorporated into the development roadmap.
- **Vulnerability Reporting**: The project maintains a clear vulnerability
  reporting policy as part of the **Eclipse Foundation** standards. Security
  issues can be reported following the process outlined in the project's
  [SECURITY.md](https://github.com/eclipse-sw360/.github/blob/main/SECURITY.md).
