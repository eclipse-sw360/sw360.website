---
title: "SW360 Architecture"
linkTitle: "SW360 Architecture"
weight: 1
description: >
  Comprehensive architecture documentation for SW360 following the Arc42 template.
---

# SW360 Architecture Documentation

**Version:** 1.0  
**Date:** March 2026  
**Classification:** Public  

---

## Document Information

| Attribute | Value |
|-----------|-------|
| Document Title | SW360 Architecture Documentation |
| Version | 1.0 |
| Status | Released |
| Last Updated | March 2026 |
| Template | Based on Arc42 |
| License | EPL-2.0 |

---

## Table of Contents

1. [Introduction and Goals](#1-introduction-and-goals)
2. [Executive Summary](#2-executive-summary)
3. [Architecture Constraints](#3-architecture-constraints)
4. [System Context](#4-system-context)
5. [Solution Strategy](#5-solution-strategy)
6. [Building Block View](#6-building-block-view)
7. [Runtime View](#7-runtime-view)
8. [Deployment View](#8-deployment-view)
9. [Cross-cutting Concepts](#9-cross-cutting-concepts)
10. [Architecture Decisions](#10-architecture-decisions)
11. [Quality Requirements](#11-quality-requirements)
12. [Risks and Technical Debt](#12-risks-and-technical-debt)
13. [Testing Strategy](#13-testing-strategy)
14. [Glossary](#14-glossary)
15. [Frontend Architecture (React UI)](#15-frontend-architecture-react-ui)

---

## 1. Introduction and Goals

### 1.1 Purpose

SW360 is an open source software component management application designed for large organizations to track, manage, and ensure compliance of open source software components. This document provides a comprehensive architecture overview following the Arc42 template.

### 1.2 Goals and Requirements

**Primary Goals:**

- Provide centralized catalog of software components, releases, and licenses
- Enable license compliance tracking and clearing workflows
- Support vulnerability management and security tracking
- Offer REST API for integration with CI/CD pipelines and other tools
- Maintain audit trail for compliance and regulatory requirements

**Key Requirements:**

- Scalable to handle 100,000+ components
- Support for 100+ concurrent users
- REST API response times under 200ms
- High availability (99%+ uptime during business hours)
- Integration with external tools (FOSSology, CVE databases)

### 1.3 Technology Stack Overview

![Technology Stack](/sw360/img/architecture/01-technology-stack.svg)

| Layer | Technology | Version |
|-------|------------|---------|
| Runtime | Java | 21 (LTS) |
| Framework | Spring Boot | 4.0.x |
| Internal RPC | Apache Thrift | 0.20.0 |
| Database | Apache CouchDB | 3.4 |
| Search | Nouveau (CouchDB) | Native |
| Auth | Keycloak | 26.x |
| Container | Docker | Latest |
| Build | Maven | 3.9+ |

---

## 2. Executive Summary

### 2.1 What is SW360?

SW360 is an open source software component catalog designed to:

- **Manage**: Components, releases, licenses, projects, and vendors
- **Track**: Vulnerabilities (CVE), security advisories, and clearing status
- **Comply**: License obligations, export control, and audit requirements
- **Integrate**: REST API, FOSSology, CVE-Search, SBOM import/export

### 2.2 Essential Features

![Core Capabilities](/sw360/img/architecture/02-core-capabilities.svg)

### 2.3 Stakeholders

| Role | Concerns | Contact with System |
|------|----------|---------------------|
| **Developers** | Use components in projects, need to know license requirements | View components, releases, licenses |
| **Project Managers** | Track project compliance status, create clearing requests | Manage projects, link components |
| **License Compliance Officers** | Clear licenses, manage obligations, approve releases | Clearing workflow, obligation management |
| **Security Team** | Monitor vulnerabilities, assess security risks | Vulnerability tracking, CVE management |
| **Legal Team** | Ensure license compliance, review obligations | License database, obligation tracking |
| **Open Source Program Office (OSPO)** | Oversee OSS strategy, manage clearing teams | Administration, reporting, dashboards |
| **System Administrators** | Deploy, configure, maintain SW360 | Infrastructure, Keycloak, CouchDB |
| **External Systems** | CI/CD pipelines, SBOM tools | REST API integration |
| **Auditors** | Verify compliance status | Reports, export functions |

### 2.4 Quality Goals

The top quality goals for SW360 architecture (in priority order):

| Priority | Quality Goal | Scenario |
|----------|--------------|----------|
| 1 | **Data Integrity** | Component, license, and clearing data must be accurate and consistent |
| 2 | **Security** | Access control must protect sensitive clearing and legal information |
| 3 | **Availability** | System must be available during business hours (99%+ uptime) |
| 4 | **Scalability** | Must handle thousands of components and hundreds of concurrent users |
| 5 | **Interoperability** | REST API must support integration with external tools |
| 6 | **Maintainability** | Modular architecture to support community contributions |

### 2.5 Document Scope

This architecture documentation covers:

- ✅ SW360 backend services (Thrift-based)
- ✅ REST API layer
- ✅ Database layer (CouchDB)
- ✅ Authentication integration (Keycloak)
- ✅ External tool integrations (FOSSology, CVE-Search)
- ✅ Deployment architecture (Docker)
- ✅ [SW360 Frontend Architecture]({{< relref "SW360-Frontend-Architecture" >}})

Out of scope:
- ❌ Legacy Liferay UI (deprecated)
- ❌ Third-party tool internal architecture

---

## 3. Architecture Constraints

This section describes the constraints that influenced the architecture decisions for SW360.

### 3.1 Technical Constraints

#### 3.1.1 Programming Languages & Frameworks

| Constraint | Description | Rationale |
|------------|-------------|-----------|
| **Java 21** | LTS version of Java | Long-term support, modern features, performance |
| **Spring Boot 4.0.x** | REST API framework | Industry standard, extensive ecosystem, Spring Security |
| **Apache Thrift 0.20.0** | Internal service communication | Efficient binary protocol, cross-language support |
| **Maven** | Build tool | Widely adopted in Java ecosystem |

#### 3.1.2 Database

| Constraint | Description | Rationale |
|------------|-------------|-----------|
| **Apache CouchDB 3.4** | Document database | Schema flexibility, replication, REST API |
| **Nouveau** | Full-text search engine | CouchDB's native Lucene integration (replaces legacy manual Lucene addon) |
| **No SQL joins** | Document-based queries only | CouchDB design, eventual consistency model |

#### 3.1.3 Authentication & Security

| Constraint | Description | Rationale |
|------------|-------------|-----------|
| **Keycloak 26.x** | Identity provider | Industry standard, OAuth2/OIDC, SSO support |
| **JWT tokens** | API authentication | Stateless, scalable authentication |
| **EPL-2.0** | Open source license | Eclipse Foundation requirement |

#### 3.1.4 Deployment

| Constraint | Description | Rationale |
|------------|-------------|-----------|
| **Docker** | Container runtime | Portable deployment, infrastructure as code |
| **Linux (Ubuntu 22.04 LTS)** | Reference platform | Stability, long-term support |
| **Tomcat 11.x** | Servlet container | Embedded in Spring Boot for WAR deployment |

### 3.2 Enterprise Environment Constraints

#### Legacy System Integration
- **Constraint**: Must integrate with existing enterprise systems (LDAP, Active Directory, existing databases)
- **Impact**: Required flexible authentication mechanisms and data federation capabilities
- **Solution**: Keycloak with pluggable user storage providers and OAuth2/OIDC standards

#### Compliance and Audit Requirements
- **Constraint**: Full audit trails required for compliance (SOX, GDPR, internal policies)
- **Impact**: Every data modification must be logged with user attribution and timestamps
- **Solution**: CouchDB's built-in revision system and dedicated changelog database

#### Multi-tenancy Support
- **Constraint**: Multiple departments/organizations sharing same SW360 instance
- **Impact**: Data isolation and role-based access control at multiple levels
- **Solution**: Domain-driven design with clear boundaries and RBAC implementation

### 3.3 Performance and Scalability Constraints

#### Large Dataset Handling
- **Constraint**: Systems may contain 100,000+ components and complex dependency graphs
- **Impact**: Traditional RDBMS queries become inefficient for graph traversal
- **Solution**: CouchDB views with pre-computed indices and Lucene/Nouveau search integration

#### Concurrent User Load
- **Constraint**: 100+ simultaneous users with responsive UI requirements (<200ms response)
- **Impact**: Stateless architecture required with efficient caching strategies
- **Solution**: Stateless REST services with connection pooling and view-based caching

### 3.4 Organizational Constraints

| Constraint | Description | Impact |
|------------|-------------|--------|
| **Eclipse Foundation** | Project governance | DCO sign-off required, ECA for contributors |
| **Open Source** | Community-driven development | Public code reviews, transparent roadmap |
| **Multi-organization** | Contributors from multiple companies | Consensus-based decisions |
| **Backward Compatibility** | Support existing deployments | API versioning, migration scripts |

### 3.5 Architecture Principles

The following principles guide architectural decisions:

#### Principle 1: Separation of Concerns

![Separation of Concerns](/sw360/img/architecture/03-separation-of-concerns.svg)

- REST layer handles HTTP concerns
- Backend services contain business logic
- Database layer handles persistence

#### Principle 2: Domain-Driven Design
- Core entities: Component, Release, Project, License, Vulnerability
- Bounded contexts per domain area
- Thrift definitions as domain contracts

#### Principle 3: API-First
- REST API is the primary interface
- OpenAPI specification for documentation
- Backward compatibility for API changes

#### Principle 4: Security by Design
- Role-based access control (RBAC)
- Document-level permissions
- External identity provider (Keycloak)

---

## 4. System Context

This section describes how SW360 interacts with its environment, including users, external systems, and integrations.

### 4.1 System Context Diagram

![System Context](/sw360/img/architecture/04-system-context.svg)

### 4.2 External Interfaces

#### 4.2.1 User Interfaces

| Interface | Protocol | Description |
|-----------|----------|-------------|
| **REST API** | HTTPS (JSON/HAL) | Primary interface for all clients |
| **OpenAPI/Swagger UI** | HTTPS | Interactive API documentation |
| **Health Endpoint** | HTTPS | `/health` for monitoring |

#### 4.2.2 External Systems

| System | Direction | Protocol | Purpose |
|--------|-----------|----------|---------|
| **Keycloak** | Bidirectional | OAuth2/OIDC | Authentication, user management |
| **FOSSology** | Outbound | REST | License scanning, clearing reports |
| **CVE-Search** | Inbound | REST | Vulnerability data synchronization |
| **SCA Tools (SPDX, CycloneDX)** | Import/Export | SBOM (File) | Software Composition Analysis - SBOM import/export |

### 4.3 Context Table

| Actor/System | Input to SW360 | Output from SW360 |
|--------------|----------------|-------------------|
| **Developers** | Component usage, project setup | License info, clearing status |
| **Compliance Team** | Clearing decisions, obligations | Compliance reports |
| **Security Team** | Vulnerability assessments | CVE alerts, risk reports |
| **CI/CD Pipeline** | SBOM files, component queries | License validation results |
| **FOSSology** | Scan requests | Clearing reports, scan results |
| **CVE-Search** | CVE database updates | Vulnerability matches |
| **Keycloak** | User authentication | User provisioning events |

### 4.4 Network Ports

| Port | Service | Protocol | Purpose |
|------|---------|----------|---------|
| **8080** | SW360 (REST + Backend) | HTTP | REST API & Thrift services |
| **11311** | Thrift Server | TCP | Internal service communication |
| **5984** | CouchDB | HTTP | Database access |
| **8083** | Keycloak | HTTP | Authentication server |
| **5987-5988** | Nouveau | HTTP | Full-text search |

### 4.5 Data Flow Overview

![Data Flow Overview](/sw360/img/architecture/18-data-flow-overview.svg)

---

## 5. Solution Strategy

This section describes the fundamental architecture decisions and solution approaches for SW360.

### 5.1 Technology Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Backend Language** | Java 21 | Enterprise-grade, type-safe, rich ecosystem, LTS |
| **REST Framework** | Spring Boot 4.0.x | Industry standard, security, documentation |
| **Internal RPC** | Apache Thrift | Efficient binary protocol, strict contracts |
| **Database** | Apache CouchDB | Schema-flexible, replication, RESTful |
| **Authentication** | Keycloak | OAuth2/OIDC, SSO, enterprise features |

### 5.2 Why These Choices?

#### Java + Spring Boot
```
✅ Strong typing catches errors at compile time
✅ Mature ecosystem (security, testing, monitoring)
✅ Enterprise adoption ensures long-term viability
✅ Excellent IDE support for development productivity
```

#### Apache Thrift
```
✅ Efficient binary serialization (smaller payloads)
✅ Language-independent service contracts
✅ Strict interface definitions prevent drift
✅ Supports complex data types and nested structures
```

#### CouchDB (Document Database)
```
✅ Flexible schema adapts to evolving domain model
✅ Built-in replication for disaster recovery
✅ RESTful API simplifies operations
✅ MVCC prevents write conflicts
✅ Attachments stored directly in documents
```

### 5.3 Architecture Patterns

<div style="page-break-before: always;"></div>

#### 5.3.1 Layered Architecture

SW360 follows a strict layered architecture:

![Layered Architecture](/sw360/img/architecture/05-layered-architecture.svg)

#### 5.3.2 Key Design Patterns

| Pattern | Usage | Example |
|---------|-------|---------|
| **Repository Pattern** | Database abstraction | `ComponentRepository`, `ProjectRepository` |
| **Service Layer** | Business logic encapsulation | `Sw360ProjectService` |
| **DTO Pattern** | Thrift-generated data transfer | `Component`, `Release`, `Project` |
| **Factory Pattern** | Thrift client creation | `ThriftClients` |
| **Strategy Pattern** | Permission checking | `DocumentPermissions` |
| **Observer Pattern** | Changelog tracking | `DatabaseChangeLogs` |
| **Adapter Pattern** | External integrations | `CVESearchAdapter`, `FossologyAdapter` |
| **Facade Pattern** | Complex subsystem access | `ComponentManagementFacade` |

#### 5.3.3 Domain-Driven Design Elements

![Bounded Contexts](/sw360/img/architecture/06-bounded-contexts.svg)

### 5.4 Security Strategy

#### 5.4.1 Authentication Flow

![Authentication Flow](/sw360/img/architecture/07-authentication-flow.svg)

#### 5.4.2 Authorization Model

| Level | Mechanism | Description |
|-------|-----------|-------------|
| **API Level** | `@PreAuthorize` | Role-based endpoint access |
| **Service Level** | `PermissionUtils` | Business rule validation |
| **Document Level** | `DocumentPermissions` | Owner/moderator checks |

#### 5.4.3 User Roles Hierarchy

![User Roles Hierarchy](/sw360/img/architecture/08-user-roles-hierarchy.svg)

### 5.5 Data Strategy

#### 5.5.1 Database Design Approach

- **Document-oriented**: Each entity is a self-contained document
- **Denormalization**: Related data embedded where appropriate
- **ID References**: Cross-document relationships via ID fields
- **Views**: Pre-computed indexes for common queries
- **Attachments**: Binary files stored with parent documents

#### 5.5.2 Consistency Model

| Scenario | Approach |
|----------|----------|
| **Single document** | Optimistic locking via revision |
| **Cross-document** | Eventually consistent |
| **Aggregations** | Computed on read or via views |
| **Conflicts** | Automatic conflict detection, manual resolution |

---

## 6. Building Block View

This section describes the static decomposition of SW360 into modules.

### 6.1 Level 1: System Overview

| Module | Path | Description |
|--------|------|-------------|
| **rest** | `rest/` | REST API layer with Spring Boot |
| **backend** | `backend/` | Thrift-based business services |
| **libraries** | `libraries/` | Shared libraries and utilities |
| **keycloak** | `keycloak/` | Keycloak integration providers |
| **clients** | `clients/` | Java client SDK |

### 6.2 REST Layer

#### Controllers and Services

| Package | Purpose | Key Classes |
|---------|---------|-------------|
| `*.project` | Project management | `ProjectController`, `Sw360ProjectService` |
| `*.component` | Component management | `ComponentController`, `Sw360ComponentService` |
| `*.release` | Release management | `ReleaseController`, `Sw360ReleaseService` |
| `*.license` | License database | `LicenseController`, `Sw360LicenseService` |
| `*.vulnerability` | CVE tracking | `VulnerabilityController`, `Sw360VulnerabilityService` |
| `*.packages` | Package (pURL) management | `PackageController`, `SW360PackageService` |
| `*.user` | User management | `UserController`, `Sw360UserService` |
| `*.vendor` | Vendor management | `VendorController`, `Sw360VendorService` |
| `*.obligation` | Obligation management | `ObligationController`, `Sw360ObligationService` |
| `*.core` | Shared utilities | `RestControllerHelper`, `JacksonCustomizations` |

#### Core Components
- **RestControllerHelper**: Common utilities for controllers (pagination, user extraction)
- **JacksonCustomizations**: JSON serialization mixins for Thrift objects
- **RestExceptionHandler**: Global exception handling with @ControllerAdvice
- **ThriftClients**: Factory for creating Thrift service clients

### 6.3 Backend Services

| Module | Thrift Service | Responsibilities |
|--------|----------------|------------------|
| **components** | `ComponentService` | Component/Release CRUD, search, clearing states |
| **projects** | `ProjectService` | Project management, linked releases, clearing requests |
| **licenses** | `LicenseService` | License database, obligations, license types |
| **vulnerabilities** | `VulnerabilityService` | CVE data, release-vulnerability relations |
| **attachments** | `AttachmentService` | File uploads, attachment validation |
| **moderation** | `ModerationService` | Moderation requests, approval workflows |
| **users** | `UserService` | User management, authentication data |
| **vendors** | `VendorService` | Vendor database management |
| **packages** | `PackageService` | Package URLs (pURL) management |
| **fossology** | `FOSSologyService` | FOSSology integration |
| **cvesearch** | `CVESearchService` | CVE-Search synchronization |
| **schedule** | `ScheduleService` | Scheduled tasks (CVE updates, etc.) |
| **licenseinfo** | `LicenseInfoService` | License info parsing and generation |
| **changelogs** | `ChangeLogsService` | Audit trail and change tracking |

#### Handler Pattern

Each backend module follows this pattern:
- **Handler** (e.g., `ComponentHandler`): Implements Thrift service interface
- **DatabaseHandler** (e.g., `ComponentDatabaseHandler`): Business logic
- **Repository** (e.g., `ComponentRepository`): CouchDB access
- **SearchHandler** (optional): Full-text search implementation

### 6.4 Libraries

| Library | Purpose |
|---------|---------|
| **datahandler** | Thrift definitions, CouchDB client, common utilities |
| **commonIO** | Attachment handling, SPDX/CycloneDX parsing |
| **exporters** | License info export (README_OSS), Excel reports |
| **importers** | SPDX, CycloneDX, CSV import functionality |

#### datahandler Key Components
- **Thrift Definitions** (`src/main/thrift/`): All entity definitions
- **CouchDB Client** (`cloudantclient/`): Database access layer
- **Common Utilities** (`common/`): SW360Utils, CommonUtils, SW360Assert
- **Permissions** (`permissions/`): Document-level permission checking

### 6.5 Keycloak Integration

| Component | Purpose |
|-----------|---------|
| **user-storage-provider** | Reads users from SW360 CouchDB for Keycloak auth |
| **event-listeners** | Creates SW360 users when registered in Keycloak |

### 6.6 Data Model

#### Core Entities

| Entity | Description | Key Fields |
|--------|-------------|------------|
| **Component** | Software component | name, componentType, vendor |
| **Release** | Specific version | version, clearingState, mainLicenseIds |
| **Project** | Collection of releases | name, linkedReleases, clearingState |
| **License** | License definition | shortName, fullName, obligations |
| **Obligation** | License obligation | title, text, obligationLevel |
| **Vulnerability** | CVE/security issue | externalId, cvss, references |
| **Package** | Distribution with pURL | name, version, purl |
| **User** | Application user | email, department, userGroup |
| **Vendor** | Component vendor | fullname, shortname, url |

#### Entity Relationships

- Component 1:N Release (one component has many releases)
- Project N:M Release (projects link to releases)
- Release N:M License (releases have licenses)
- License N:M Obligation (licenses have obligations)
- Release N:M Vulnerability (releases affected by vulnerabilities)
- Component N:1 Vendor (components have one vendor)

### 6.7 Thrift Service Architecture

![Thrift Service Architecture](/sw360/img/architecture/17-thrift-service-architecture.svg)

---

## 7. Runtime View

This section describes the behavior of the system at runtime through important use cases and scenarios.

### 7.1 Component Creation Flow

![Component Creation Flow](/sw360/img/architecture/09-component-creation-flow.svg)

> **Note:** Search indexing occurs asynchronously - CouchDB's view update mechanism notifies Nouveau directly, not through the SW360 application.

### 7.2 Authentication Flow (JWT)

![JWT Authentication Flow](/sw360/img/architecture/19-jwt-authentication-flow.svg)

### 7.3 Clearing Request Workflow

![Clearing Request Workflow](/sw360/img/architecture/10-clearing-request-workflow.svg)

### 7.4 Vulnerability Synchronization

![Vulnerability Sync](/sw360/img/architecture/11-vulnerability-sync.svg)

### 7.5 SBOM Import Flow

![SBOM Import Flow](/sw360/img/architecture/12-sbom-import-flow.svg)

### 7.6 API Caching Flow

SW360 implements a file-based API response cache for resource-intensive endpoints like `GET /releases?allDetails=true`. This caching mechanism avoids JVM heap pressure by storing pre-serialized JSON responses on disk.

![API Caching Flow](/sw360/img/architecture/21-api-caching-flow.svg)

**Key Design Decisions:**

| Aspect | Approach |
|--------|----------|
| **Storage** | File-based (avoids heap memory pressure) |
| **Per-Role Variants** | Separate cache files per UserGroup (ADMIN, USER, etc.) |
| **Invalidation** | TTL-based + manual via Admin API + automatic on data mutations |
| **Stale Handling** | Stale-while-revalidate pattern for background refresh |

> **Reference:** See [ADR-007: File-Based API Response Cache](decisions/ADR-007-api-caching.md) for detailed rationale and implementation guidance.

---

## 8. Deployment View

This section describes the infrastructure and deployment architecture of SW360.

### 8.1 Deployment Overview

![Deployment Architecture](/sw360/img/architecture/13-deployment-architecture.svg)

### 8.2 Container Specification

#### 8.2.1 SW360 Application Container

| Attribute | Value |
|-----------|-------|
| **Image** | `ghcr.io/eclipse-sw360/sw360:latest` |
| **Base** | Eclipse Temurin JDK 21 |
| **Exposed Ports** | 8080 (REST), 11311 (Thrift) |
| **Health Check** | `/health` endpoint |

**Environment Variables:**

| Variable | Description | Default |
|----------|-------------|---------|
| `SW360_BASE_URL` | Base URL for SW360 | `http://localhost:8080` |
| `COUCHDB_URL` | CouchDB connection URL | `http://couchdb:5984` |
| `COUCHDB_USER` | CouchDB username | - |
| `COUCHDB_PASSWORD` | CouchDB password | - |

#### 8.2.2 CouchDB Container

| Attribute | Value |
|-----------|-------|
| **Image** | `couchdb:3.4` |
| **Exposed Ports** | 5984 (HTTP API) |
| **Data Volume** | `couchdb:/opt/couchdb/data` |

**Databases:**

| Database | Purpose |
|----------|---------|
| `sw360db` | Main application data |
| `sw360users` | User data |
| `sw360attachments` | Attachment metadata |

#### 8.2.3 Keycloak Container

| Attribute | Value |
|-----------|-------|
| **Image** | `quay.io/keycloak/keycloak:26.x` |
| **Exposed Ports** | 8083 (HTTP), 8533 (HTTPS) |
| **Database** | PostgreSQL |

### 8.3 Docker Compose Configuration

```yaml
# docker-compose.yml (simplified)
services:
  sw360:
    image: ghcr.io/eclipse-sw360/sw360:latest
    ports:
      - "8080:8080"
      - "11311:11311"
    depends_on:
      - couchdb
    volumes:
      - etc:/etc/sw360
      - ./config/sw360:/app/sw360/config
    environment:
      - SW360_BASE_URL=http://localhost:8080

  couchdb:
    image: couchdb:3.4
    ports:
      - "5984:5984"
    volumes:
      - couchdb:/opt/couchdb/data
      - ./config/couchdb/sw360_setup.ini:/opt/couchdb/etc/local.d/sw360_setup.ini

  couchdb-nouveau:
    image: couchdb:3.4-nouveau
    ports:
      - "5987:5987"
      - "5988:5988"

volumes:
  couchdb:
  etc:

networks:
  default:
    name: sw360net
```

### 8.4 Production Deployment Considerations

#### 8.4.1 High Availability Architecture

![High Availability Architecture](/sw360/img/architecture/14-ha-architecture.svg)

> **Load Balancing:** CouchDB cluster deployments require a load balancer (e.g., HAProxy, nginx) in front of cluster nodes to distribute client requests and provide failover.

#### 8.4.2 Scaling Guidelines

| Component | Scaling Strategy |
|-----------|------------------|
| **SW360 REST/Backend** | Horizontal (stateless) |
| **CouchDB** | Cluster mode (3+ odd nodes for quorum) |
| **Keycloak** | Cluster mode with shared DB |
| **Attachments** | External storage (S3/NFS) recommended; currently stored in CouchDB |

#### 8.4.3 Minimum Requirements

| Component | CPU | Memory | Storage |
|-----------|-----|--------|---------|
| **SW360 (per instance)** | 2 cores | 4 GB | 1 GB |
| **CouchDB (per node)** | 2 cores | 4 GB | 50+ GB |
| **Keycloak** | 1 core | 1 GB | 1 GB |
| **PostgreSQL (Keycloak)** | 1 core | 1 GB | 10 GB |

### 8.5 Configuration Files

For detailed configuration file reference, see the existing deployment documentation:  
👉 [Deploy Configuration Files]({{< relref "/docs/deployment/deploy-configuration-files" >}})

### 8.6 Deployment Checklist

#### Pre-deployment

- [ ] CouchDB databases created and initialized
- [ ] Keycloak realm and client configured
- [ ] SSL certificates provisioned
- [ ] Secrets managed (Vault, K8s secrets, etc.)
- [ ] Network firewall rules configured

#### Post-deployment

- [ ] Health endpoint responding (`/health`)
- [ ] Authentication working (Keycloak login)
- [ ] Database connectivity verified
- [ ] API endpoints accessible
- [ ] Scheduled tasks running (CVE sync)
- [ ] Logging configured and working

### 8.7 Infrastructure as Code (IaC)

For reproducible and version-controlled deployments, SW360 infrastructure can be defined using IaC tools:

| Tool | Use Case | Examples |
|------|----------|----------|
| **Terraform** | Cloud infrastructure provisioning | VMs, networks, storage |
| **Ansible** | Configuration management | SW360 installation, CouchDB setup |
| **Helm** | Kubernetes deployments | SW360 Helm charts |
| **Docker Compose** | Local/dev environments | Development setup |

**IaC Principles:**
- Store infrastructure definitions in version control
- Use parameterized templates for environment-specific values
- Implement CI/CD for infrastructure changes
- Maintain separate configurations for dev/staging/production

---

## 9. Cross-cutting Concepts

This section describes cross-cutting technical concepts that apply across the entire SW360 system.

### 9.1 Security Concepts

#### 9.1.1 Authentication

SW360 supports multiple authentication mechanisms:

| Method | Use Case | Configuration |
|--------|----------|---------------|
| **Keycloak JWT** | Primary (OAuth2/OIDC) | `spring.security.oauth2.resourceserver.jwt.*` |
| **API Token** | Programmatic access | `rest.apitoken.*` in sw360.properties |
| **Basic Auth** | Development/testing | Spring Security basic |

#### 9.1.2 Authorization Model

![Authorization Model](/sw360/img/architecture/20-authorization-model.svg)

#### 9.1.3 User Roles

| Role | Level | Capabilities |
|------|-------|--------------|
| `USER` | Base | View, create components/projects |
| `CLEARING_EXPERT` | Elevated | Clearing workflow actions |
| `CLEARING_ADMIN` | Admin | Approve clearings, manage obligations |
| `ECC_ADMIN` | Admin | Export control management |
| `SECURITY_ADMIN` | Admin | Vulnerability management |
| `SW360_ADMIN` | Super | Full application admin |
| `ADMIN` | System | System-level administration |

#### 9.1.4 Document Visibility

```java
enum Visibility {
    PRIVATE,                    // Only creator
    ME_AND_MODERATORS,          // Creator + moderators
    BUISNESSUNIT_AND_MODERATORS,// Same business unit
    EVERYONE                    // All authenticated users
}
```

### 9.2 Persistence Concepts

#### 9.2.1 CouchDB Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Document-oriented** | Each entity is a self-contained JSON document |
| **ID-based references** | Related documents linked by ID fields |
| **Optimistic locking** | `_rev` field for conflict detection |
| **Views for queries** | MapReduce views for common query patterns |
| **Attachments** | Binary files stored with documents |

#### 9.2.2 Repository Pattern

```java
// Base repository class
public class ComponentRepository extends DatabaseRepositoryCloudantClient<Component> {
    
    public ComponentRepository(DatabaseConnectorCloudant db) {
        super(db, Component.class);
        initStandardDesignDocument(getViews(), db);
    }
    
    // Query using CouchDB views
    public List<Component> getByName(String name) {
        return queryView("byName", name);
    }
    
    // Query using Mango selectors
    public List<Component> getByType(ComponentType type) {
        Map<String, Object> selector = eq("componentType", type.name());
        return db.queryBySelector(selector, Component.class);
    }
}
```

#### 9.2.3 Query Operators

```java
import static org.eclipse.sw360.datahandler.cloudantclient.DatabaseConnectorCloudant.*;

// Equality
eq("field", "value")

// In list
in("field", List.of("a", "b", "c"))

// Exists
exists("field", true)

// Logical operators
and(condition1, condition2)
or(condition1, condition2)

// Element match (arrays)
elemMatch("releases", eq("clearingState", "APPROVED"))
```

### 9.3 API Design Concepts

#### 9.3.1 REST Conventions

| Aspect | Convention |
|--------|------------|
| **Base path** | `/api` |
| **Resource naming** | Plural nouns (`/projects`, `/components`) |
| **HTTP methods** | GET (read), POST (create), PATCH (update), DELETE |
| **Response format** | HAL+JSON |
| **Pagination** | `page`, `page_entries` parameters |
| **Error format** | Problem Details (RFC 7807) |

#### 9.3.2 HATEOAS Links

HATEOAS (Hypermedia as the Engine of Application State) is a REST constraint that enables clients to navigate the API dynamically through hyperlinks embedded in responses. Rather than hardcoding API endpoints, clients discover available actions from the `_links` object returned with each resource. This decouples client logic from server URL structure, enabling API evolution without breaking clients.

```json
{
  "name": "My Project",
  "_links": {
    "self": { "href": "/api/projects/abc123" },
    "sw360:releases": { "href": "/api/projects/abc123/releases" },
    "sw360:attachments": { "href": "/api/projects/abc123/attachments" },
    "curies": [{ "name": "sw360", "href": "/docs/{rel}.html" }]
  },
  "_embedded": {
    "sw360:releases": [...]
  }
}
```

### 9.4 Error Handling

#### 9.4.1 Exception Hierarchy

```
Exception
├── SW360Exception (Thrift layer)
│   └── errorCode: 400, 403, 404, 409, 500
├── ResourceNotFoundException (REST)
├── AccessDeniedException (REST)
├── BadRequestClientException (REST)
└── DataIntegrityViolationException (REST)
```

#### 9.4.2 Global Exception Handler

```java
@ControllerAdvice
public class RestExceptionHandler {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ErrorResponse> handleNotFound(ResourceNotFoundException ex) {
        return ResponseEntity.status(404).body(
            new ErrorResponse(404, "Not Found", ex.getMessage())
        );
    }
    
    @ExceptionHandler(AccessDeniedException.class)
    public ResponseEntity<ErrorResponse> handleAccessDenied(AccessDeniedException ex) {
        return ResponseEntity.status(403).body(
            new ErrorResponse(403, "Forbidden", ex.getMessage())
        );
    }
}
```

### 9.5 Logging

#### 9.5.1 Logging Standards

| Level | Usage |
|-------|-------|
| `DEBUG` | Detailed debugging information |
| `INFO` | Business events, state changes |
| `WARN` | Potential issues, deprecations |
| `ERROR` | Failures requiring attention |

#### 9.5.2 Structured Logging

```java
// Good: Parameterized logging
log.info("Processing {} releases for project {}", count, projectId);

// Bad: String concatenation
log.info("Processing " + count + " releases for project " + projectId);
```

### 9.6 Validation

#### 9.6.1 Input Validation

```java
import static org.eclipse.sw360.datahandler.common.SW360Assert.*;

public void createComponent(Component component, User user) throws SW360Exception {
    // Validate inputs
    assertNotNull(component, "Component cannot be null");
    assertNotEmpty(component.getName(), "Component name is required");
    assertUser(user);
    
    // Business validation
    if (componentExists(component.getName())) {
        throw new SW360Exception("Component already exists")
            .setErrorCode(409);
    }
}
```

---

## 10. Architecture Decisions

This section documents key architecture decisions using the ADR (Architecture Decision Record) format.

### ADR-001: Use Apache Thrift for Internal Services

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2014) |
| **Context** | SW360 needed efficient, reliable communication between web layer and backend services. Apache Thrift was introduced primarily to enable integration with FOSSology, which at the time did not have a REST API (neither did SW360). Thrift's cross-language support made it ideal for inter-system communication. |
| **Decision** | Use Apache Thrift as the internal RPC framework |

**Rationale:**
1. **Efficient Binary Protocol**: Thrift's binary protocol is more compact than JSON/XML
2. **Interface Definition Language (IDL)**: Formal contracts between services
3. **Code Generation**: Generates strongly-typed Java classes
4. **Complex Data Structures**: Native support for nested structs, maps, sets, lists
5. **Cross-Language Support**: Supports Python, C++, PHP for future integration

**Consequences:**
- ✅ Strong typing, performance, clear contracts, backward compatibility
- ❌ Learning curve, build complexity, debugging difficulty

### ADR-002: Use CouchDB as Primary Database

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2014) |
| **Context** | SW360 manages software components with complex, evolving data structures |
| **Decision** | Use Apache CouchDB as the primary database |

**Rationale:**
1. **Schema Flexibility**: Documents can have different structures without migrations
2. **Attachment Storage**: Binary attachments stored directly with documents
3. **RESTful HTTP API**: Simple integration without special drivers
4. **Replication**: Built-in master-master replication for disaster recovery
5. **MVCC**: Optimistic locking via `_rev` field prevents concurrent update conflicts

**Consequences:**
- ✅ Flexible data model, attachment handling, HTTP API, replication
- ❌ No SQL joins, eventual consistency, query limitations

### ADR-003: Use Keycloak for Authentication

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2022) |
| **Context** | Migration away from Liferay required a new authentication solution |
| **Decision** | Use Keycloak as the identity provider |

**Rationale:**
1. **Open Source & Self-Hosted**: No vendor lock-in, full control over user data
2. **Enterprise Features**: LDAP/AD federation, SAML 2.0, OIDC, MFA
3. **Standard Protocols**: OAuth 2.0 for API authentication, OIDC for identity
4. **Customization**: Custom user storage providers, event listeners
5. **Active Community**: Red Hat backing, regular security updates

**Consequences:**
- ✅ SSO support, JWT tokens, federation, security, API tokens
- ❌ Additional component to maintain, OAuth2 complexity

### ADR-004: Migrate to Spring Boot 3.x

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2024) |
| **Context** | Spring Boot 2.x reached end of support |
| **Decision** | Migrate to Spring Boot 3.5.x with Java 21 |

**Rationale:**
1. **Long-term Support**: Spring Boot 3.x is actively maintained
2. **Security Improvements**: Spring Security 6 includes enhanced OAuth2 support
3. **Performance**: Java 21 virtual threads, improved GC
4. **Modern APIs**: Records, pattern matching, sealed classes
5. **Ecosystem**: Latest versions of SpringDoc, Jackson, etc.

**Key Changes:**
- Namespace migration: `javax.*` → `jakarta.*`
- Security configuration: New DSL, authorization changes
- OpenAPI/SpringDoc: Version upgrade, annotation changes

### ADR-005: Use Apache Tomcat as Servlet Container

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2014) |
| **Context** | SW360 was originally built on Liferay Portal, requiring servlet container support for multiple web applications |
| **Decision** | Use Apache Tomcat as the servlet container |

**Rationale:**
1. **Liferay Compatibility**: Liferay portal required a servlet container
2. **Multiple Web Applications**: Tomcat supports deployment of individual WAR files
3. **Industry Standard**: Widely adopted, well-documented, production-proven
4. **Spring Boot Integration**: Embedded Tomcat in Spring Boot 3.x (Tomcat 11.x)

**Consequences:**
- ✅ Standard servlet deployment, mature ecosystem, excellent documentation
- ❌ Additional configuration for performance tuning

### ADR-006: Migrate to Cloudant SDK for CouchDB Access

| Attribute | Value |
|-----------|-------|
| **Status** | Accepted (2024) |
| **Context** | The Ektorp library (previous CouchDB client) became deprecated and unmaintained |
| **Decision** | Migrate to IBM Cloudant SDK for CouchDB access |

**Rationale:**
1. **Ektorp Deprecation**: Original CouchDB client library no longer maintained
2. **IBM Corporate Support**: IBM unified their cloud support SDKs, backing active development
3. **CouchDB Compatibility**: Cloudant SDK works with standard CouchDB (not just IBM Cloudant)
4. **Modern Java Support**: Full Java 21 compatibility and async operations

**Consequences:**
- ✅ Active maintenance, corporate backing, modern API
- ❌ API migration effort, IBM branding (though works with any CouchDB)

---

## 11. Quality Requirements

This section describes the quality requirements for SW360 and how the architecture addresses them.

### 11.1 Quality Tree

![Quality Tree](/sw360/img/architecture/15-quality-tree.svg)

### 11.2 Quality Scenarios

#### 11.2.1 Performance

| ID | Scenario | Target |
|----|----------|--------|
| P1 | Get single component by ID | < 200ms |
| P2 | List 100 components | < 500ms |
| P3 | Search across 10,000 components | < 2s |
| P4 | Upload 50MB attachment | < 30s |
| P5 | Generate clearing report for project with 500 releases | < 60s |

#### 11.2.2 Security

| ID | Scenario | Expected Response |
|----|----------|-------------------|
| S1 | Invalid JWT token presented | 401 Unauthorized returned |
| S2 | User without WRITE permission tries to modify | 403 Forbidden, moderation request created |
| S3 | API token expires | User must regenerate token |
| S4 | Cross-site scripting attempt | Input sanitized, XSS filter applied |
| S5 | Brute force login attempt | Keycloak rate limiting kicks in |

#### 11.2.3 Scalability

| ID | Scenario | Expected Behavior |
|----|----------|-------------------|
| SC1 | 100 concurrent API requests | System handles without degradation |
| SC2 | Database grows to 1M documents | Query performance acceptable with proper indexes |
| SC3 | 1000 users in system | Authentication/authorization performs normally |

### 11.3 Quality Measures

#### 11.3.1 Code Quality

| Metric | Target | Tool |
|--------|--------|------|
| Test coverage | > 60% | JaCoCo |
| Code formatting | 100% compliant | Spotless |
| Static analysis | No critical issues | SonarQube |
| Dependency vulnerabilities | No critical CVEs | OWASP Dependency Check, GitHub Dependabot |

#### 11.3.2 Operational Quality

| Metric | Target | Monitoring |
|--------|--------|------------|
| Availability | 99% uptime | Health endpoint |
| Error rate | < 1% of requests | Log analysis |
| Response time P95 | < 1s | Metrics |

### 11.4 Quality Trade-offs

| Trade-off | Decision | Rationale |
|-----------|----------|-----------|
| Strong typing vs. flexibility | Strong typing (Thrift) | Prevents runtime errors |
| Performance vs. simplicity | Simplicity first | Optimize when needed |
| Features vs. maintenance | Core features only | Community-driven scope |
| Consistency vs. availability | Eventual consistency | CouchDB design fits use case |

---

## 12. Risks and Technical Debt

This section documents known risks and technical debt in the SW360 architecture.

### 12.1 Technical Risks

#### 12.1.1 High Priority Risks

| ID | Risk | Impact | Probability | Mitigation |
|----|------|--------|-------------|------------|
| R1 | **CouchDB scaling limits** | Performance degradation with millions of documents | Medium | Monitor growth, consider sharding strategy |
| R2 | **Thrift protocol changes** | Breaking changes in Thrift 0.21+; pinned versions miss security patches | Medium | Pin version, test upgrades thoroughly, monitor security advisories |
| R3 | **Keycloak provider compatibility** | Custom providers break on Keycloak upgrades | Medium | Test providers with each Keycloak version |
| R4 | **Single point of failure** | CouchDB instance unavailable | Medium | Implement replication, monitoring |

#### 12.1.2 Medium Priority Risks

| ID | Risk | Impact | Probability | Mitigation |
|----|------|--------|-------------|------------|
| R5 | **JWT token security** | Token theft enables unauthorized access | Low | Short expiry, token rotation |
| R6 | **Attachment storage limits** | Large attachments consume disk space | Medium | Implement quotas, archival strategy |
| R7 | **Search performance** | Nouveau search degrades with scale | Medium | Monitor, tune indexes |
| R8 | **Dependency vulnerabilities** | CVEs in third-party libraries | Medium | Regular dependency updates, scanning |

### 12.2 Technical Debt

#### 12.2.1 High Priority Debt

| ID | Description | Impact | Proposed Solution |
|----|-------------|--------|-------------------|
| D1 | **Inconsistent error handling** | Different error formats across endpoints | Standardize on Problem Details (RFC 7807) |
| D2 | **Missing pagination on some endpoints** | Memory issues with large result sets | Add pagination to all list endpoints |
| D3 | **Hardcoded configuration values** | Difficult to customize deployments | Move to Spring Configuration properties |

#### 12.2.2 Medium Priority Debt

| ID | Description | Impact | Proposed Solution |
|----|-------------|--------|-------------------|
| D4 | **Limited test coverage** | Regression risks | Increase coverage to 70%+ |
| D5 | **Duplicated validation logic** | Maintenance burden | Extract to shared validators |
| D6 | **Inconsistent API naming** | Confusing for API consumers | Establish naming conventions |
| D7 | **Legacy Liferay references** | Confusing, unused code | Remove obsolete code |
| D8 | **Monolithic backend deployment** | All services in one WAR | Consider microservices (long-term) |

### 12.3 Risk Monitoring

#### 12.3.1 Key Metrics to Watch

| Metric | Warning Threshold | Critical Threshold |
|--------|-------------------|-------------------|
| Database size | 50 GB | 100 GB |
| Document count | 500,000 | 1,000,000 |
| Response time P95 | 2s | 5s |
| Error rate | 1% | 5% |
| Memory usage | 80% | 95% |

### 12.4 Debt Reduction Plan

#### Short-term (Next Release)
- [ ] Standardize error responses
- [ ] Add missing pagination
- [ ] Update documentation

#### Medium-term (6 months)
- [ ] Increase test coverage to 70%
- [ ] Remove legacy Liferay code
- [ ] Implement comprehensive logging

#### Long-term (12+ months)
- [ ] Evaluate microservices architecture
- [ ] Consider caching layer
- [ ] Implement webhooks/async processing

---

## 13. Testing Strategy

This section describes the testing approach for SW360, following the Testing Trophy methodology.

### 13.1 Current State vs Target State

| Aspect | Current State | Target State |
|--------|---------------|--------------|
| Shape | Pyramid | Trophy |
| Static Analysis | Spotless only | Spotless + SpotBugs + ArchUnit |
| Unit Tests | 60% | 25% |
| Integration Tests | 35% | 55% |
| E2E Tests | 5% (manual) | 5% (automated) |
| CouchDB Testing | Mocked | Testcontainers |

### 13.2 Test Pyramid vs Testing Trophy

#### Test Pyramid (Traditional)
```
                    /\
                   /  \      E2E Tests (Few, Slow, Expensive)
                  /----\
                 /      \    Integration Tests (Some)
                /--------\
               /          \  Unit Tests (Many, Fast, Cheap)
              --------------
```

#### Testing Pyramid (SW360 Approach)

![Testing Pyramid](/sw360/img/architecture/16-testing-pyramid.svg)

### 13.3 Test Level Breakdown

| Level | Scope | SW360 Example |
|-------|-------|---------------|
| Unit | Single class/method | ComponentRepositoryTest |
| Integration | Multiple components | REST → Service → Handler → CouchDB |
| System | Complete deployed app | Full SW360 + Keycloak + CouchDB |
| Acceptance | Business requirements | "Can I generate clearing report?" |

### 13.4 Key Testing Principles

1. **Test behavior at the REST layer** — that's what users consume
2. **Static analysis is free testing** — maximize it (Spotless, SpotBugs, ArchUnit)
3. **Unit test complex logic only** — not glue code
4. **E2E tests are expensive** — use sparingly for critical paths
5. **If you mock too much, test at a higher level**
6. **Refactoring should not break tests** — if it does, tests are too coupled

### 13.5 Recommended Tools

| Purpose | Tool |
|---------|------|
| Unit Testing | JUnit 5, Mockito |
| Integration Testing | Testcontainers (CouchDB, Keycloak) |
| Static Analysis | Spotless, SpotBugs, ArchUnit |
| E2E Testing | Playwright |
| Code Coverage | JaCoCo |

### 13.6 Critical User Journeys for E2E

1. **Authentication Flow**: Login → Access protected resource → Logout
2. **Component Lifecycle**: Create Component → Add Release → Upload Source → Trigger Clearing
3. **Project Clearing**: Create Project → Link Releases → Generate Clearing Report
4. **License Compliance**: Search License → Check Obligations → Export Report

---

## 14. Glossary

This section defines terms used throughout the SW360 architecture documentation.

### 14.1 Domain Terms

| Term | Definition |
|------|------------|
| **Clearing** | The process of reviewing and approving open source components for use |
| **Clearing Request (CR)** | A formal request to review and clear the components used in a project |
| **Clearing State** | The status of license review: NEW_CLEARING, UNDER_CLEARING, REPORT_AVAILABLE, APPROVED |
| **Component** | A software package or library without version information |
| **COTS** | Commercial Off-The-Shelf software; proprietary software purchased from vendors |
| **CVE** | Common Vulnerabilities and Exposures; unique identifiers for security vulnerabilities |
| **CVSS** | Common Vulnerability Scoring System; numerical score indicating vulnerability severity |
| **ECC** | Export Control Classification; regulations governing export of technology |
| **License Obligation** | Requirements imposed by a license (e.g., attribution, source disclosure) |
| **Moderation Request** | A request for moderators to review changes when user lacks permissions |
| **OSS** | Open Source Software; software with source code freely available |
| **OSPO** | Open Source Program Office; team managing open source strategy |
| **Package** | A specific distribution of a release, identified by a pURL |
| **Project** | A software product that uses components/releases |
| **pURL** | Package URL; a standardized way to identify software packages |
| **Release** | A specific version of a component |
| **SBOM** | Software Bill of Materials; list of components in a software product |
| **Vendor** | The organization that creates/maintains a component |
| **Vulnerability** | A security weakness in software that could be exploited |

### 14.2 Technical Terms

| Term | Definition |
|------|------------|
| **CouchDB** | Apache CouchDB; document-oriented database used by SW360 |
| **HAL** | Hypertext Application Language; JSON format for hypermedia APIs |
| **HATEOAS** | Hypermedia as the Engine of Application State; REST constraint |
| **JWT** | JSON Web Token; compact token format for secure claims transmission |
| **Keycloak** | Open source identity and access management solution |
| **Nouveau** | CouchDB's built-in full-text search engine |
| **OAuth2** | Authorization framework for secure API access |
| **OIDC** | OpenID Connect; identity layer on top of OAuth2 |
| **REST** | Representational State Transfer; architectural style for web services |
| **Thrift** | Apache Thrift; framework for scalable cross-language services |

### 14.3 Standards and Specifications

| Term | Definition |
|------|------------|
| **CycloneDX** | SBOM standard focused on security and supply chain |
| **EPL-2.0** | Eclipse Public License 2.0; SW360's license |
| **RFC 7807** | Problem Details for HTTP APIs; standard error format |
| **SPDX** | Software Package Data Exchange; standard for SBOM and license info |

### 14.4 Abbreviations

| Abbreviation | Full Form |
|--------------|-----------|
| ADR | Architecture Decision Record |
| API | Application Programming Interface |
| CI/CD | Continuous Integration/Continuous Deployment |
| CRUD | Create, Read, Update, Delete |
| DTO | Data Transfer Object |
| IDL | Interface Definition Language |
| JWT | JSON Web Token |
| LTS | Long-Term Support |
| MVCC | Multi-Version Concurrency Control |
| RBAC | Role-Based Access Control |
| RPC | Remote Procedure Call |
| SSO | Single Sign-On |

---

## 15. Frontend Architecture (React UI)

For the full frontend architecture documentation, see the dedicated document:  
👉 [SW360 Frontend Architecture]({{< relref "SW360-Frontend-Architecture" >}})

---

## Appendix A: Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | March 2026 | SW360 Architecture Team | Initial document |
| 1.1 | May 2026 | SW360 Architecture Team | Added frontend placeholder, ADR-008 (Spring Boot 4.x) |

---

## Appendix B: References

1. **Arc42 Template**: https://arc42.org/
2. **Eclipse SW360**: https://eclipse.dev/sw360/
3. **Apache CouchDB**: https://couchdb.apache.org/
4. **Apache Thrift**: https://thrift.apache.org/
5. **Keycloak**: https://www.keycloak.org/
6. **Spring Boot**: https://spring.io/projects/spring-boot
7. **SPDX Specification**: https://spdx.dev/
8. **CycloneDX Specification**: https://cyclonedx.org/

---

*This program and the accompanying materials are made available under the terms of the Eclipse Public License 2.0 which is available at https://www.eclipse.org/legal/epl-2.0/*
