---
title: "Secure Design"
linkTitle: "Secure Design"
weight: 40
description: "Security design principles applied in the SW360 project."
---

# SW360 Secure Design Principles

This document outlines how the SW360 project incorporates fundamental security
design principles into its architecture and development processes.

## 1. Fail-safe Defaults
- **In-depth Authorization**: By default, any new API endpoint or UI action
  requires authentication. Access is denied unless explicitly permitted by the
  user's roles.
- **Secure Configuration**: The system is designed to run in a secure state
  out-of-the-box. Environment variables are used for sensitive configurations,
  ensuring that secrets are never hardcoded in the repository.

## 2. Complete Mediation
- **Centralized Authentication**: Every access request is mediated through the
  core **Authorization Server** (OIDC/OAuth2). No resource can be accessed
  without a valid, verified token. Integration with **Keycloak** is supported
  for enhanced IAM features.
- **REST Interceptors**: Spring Security and customized filters serve as
  mediators for all REST traffic, ensuring that every request is checked
  against the user's authority before being processed.

## 3. Least Privilege
- **Role-Based Access Control (RBAC)**: SW360 uses granular roles (e.g., USER,
  ADMIN, MAINTAINER). Users are granted only the minimum permissions necessary
  for their tasks.
- **Record-Level Permissions**: Visibility and edit rights are enforced at the
  data handler level, ensuring that users can only interact with projects and
  components they have specific rights to view.

## 4. Defense in Depth
- **Multi-layer Validation**: Input validation is performed at both the frontend
  (Next.js) and the backend (Spring Boot/Data Handler) to prevent malformed or
  malicious data from reaching the database.
- **Network Security**: The architecture separation of frontend, backend, and
  database provides multiple layers where security controls can be applied
  (e.g., CSP on the frontend, TLS between services).

## 5. Economy of Mechanism (Keep it Simple)
- **Standardized Frameworks**: By utilizing established frameworks like Spring
  Security and Next.js, the project avoids the complexities and vulnerabilities
  associated with "rolling your own" security solutions.
- **Clean Architecture**: The modular separation of concerns ensures that
  security logic is isolated and easy to audit.

## 6. Open Design
- **Open Standards**: The project relies on open, widely-scrutinized standards
  such as OIDC and OAuth2 for security, rather than proprietary or "hidden"
  mechanisms.
- **Public Auditability**: As an open-source project, the security policy,
  source code, and design are public, allowing for continuous community review
  and transparency.

## 7. Psychological Acceptability
- **SSO Integration**: By using Keycloak for Single Sign-On, we minimize
  "password fatigue" for users while maintaining robust security controls.
- **Intuitive UI**: Security-related states (e.g., read-only vs. edit mode) are
  clearly reflected in the UI, making it easy for users to understand their
  current permission level.
