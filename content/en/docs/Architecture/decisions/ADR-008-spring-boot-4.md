---
title: "ADR-008: Upgrade to Spring Boot 4.x and Spring Security 7.x"
linkTitle: "ADR-008: Spring Boot 4.x Upgrade"
weight: 9
---

# Decision Analysis and Resolution: Spring Boot 4.x and Spring Security 7.x Upgrade

**Created by:** SW360 Architecture Team  
**Decision Date:** April 2026
**Status:** Accepted  
**Supersedes:** ADR-004 (Spring Boot 3.x Migration)  
**Reference:** [eclipse-sw360/sw360#4054](https://github.com/eclipse-sw360/sw360/pull/4054)

---

## 1. Context and Problem Statement

Spring Boot 3.x, while still supported, is approaching its maintenance window end. Spring Boot 4.x (based on Spring Framework 7.x and Spring Security 7.x) introduces performance improvements, modern Java alignment, and security enhancements. However, the upgrade involves breaking changes in package relocations, removed deprecated APIs, and module restructuring.

### Key Drivers

- **Spring Boot 4.x** released with Spring Framework 7.x foundation
- **Spring Security 7.x** introduces stricter authorization defaults
- **Spring REST Docs 4.x** removes deprecated test utilities
- **Module splits** in Spring Boot require additional dependencies

---

## 2. Decision

Upgrade SW360 REST and authorization modules to:

| Component | Version |
|-----------|---------|
| Spring Boot | 4.0.5 |
| Spring Framework | 7.0.6 |
| Spring Security | 7.0.4 |
| Spring REST Docs | 4.0.0 |

---

## 3. Breaking Changes and Migration Impact

### 3.1 Package Relocations (Spring Boot 4.x)

| Old Package | New Package |
|-------------|-------------|
| `org.springframework.boot.actuate.health.Health` | `org.springframework.boot.health.contributor.Health` |
| `org.springframework.boot.actuate.health.HealthIndicator` | `org.springframework.boot.health.contributor.HealthIndicator` |

### 3.2 Removed APIs (Spring REST Docs 4.0)

| Removed | Replacement |
|---------|-------------|
| `JUnitRestDocumentation` | `ManualRestDocumentation` with explicit `beforeTest()`/`afterTest()` lifecycle |

### 3.3 Type Hierarchy Changes (Spring Framework 7.x)

- `MockMultipartHttpServletRequestBuilder` no longer extends `MockHttpServletRequestBuilder`
- Requires `var` type inference or interface-level typing in tests

### 3.4 Bean Type Mismatches

- `BCryptPasswordEncoder` declarations must use `PasswordEncoder` interface type to match `@Bean` method signatures

### 3.5 New Module Dependencies (Spring Boot 4.x Module Split)

| New Dependency | Reason |
|----------------|--------|
| `spring-boot-restclient` | `TestRestTemplate` depends on `RestTemplateBuilder` which moved to this module |

---

## 4. Impact Assessment

| Area | Files Changed | Effort |
|------|---------------|--------|
| Root POM (versions) | 1 | Low |
| Main source (rest) | 3 | Low |
| Test base classes | 3 | Medium |
| REST docs spec tests | 5 | Medium |
| Integration tests | 20 | Low (import updates) |
| POM dependencies | 2 | Low |
| Deleted obsolete code | 1 | Low |
| **Total** | **42** | **Medium** |

Net change: +97 / -200 lines (reduction due to removed obsolete code)

---

## 5. Alternatives Considered

### 5.1 Stay on Spring Boot 3.x

- **Pro:** No migration effort, currently stable
- **Con:** Will reach end of OSS support; increasingly behind on security patches

### 5.2 Skip to Next LTS Only

- **Pro:** Less frequent migrations
- **Con:** Larger migration gaps accumulate more breaking changes; miss security updates

---

## 6. Consequences

### Positive

- ✅ Active security patch support from Spring team
- ✅ Performance improvements (Spring Framework 7.x optimizations)
- ✅ Cleaner code (removed deprecated patterns)
- ✅ Modern health indicator API
- ✅ Net code reduction (-103 lines)

### Negative

- ❌ All downstream forks must apply same migration
- ❌ Test infrastructure changes may confuse contributors unfamiliar with Spring REST Docs 4.x
- ❌ `var` usage in tests may reduce readability for some developers

### Risks

- Custom Keycloak providers may need updates for Spring Security 7.x authorization model changes
- Third-party libraries that depend on Spring Boot 3.x APIs may lag behind

---

## 7. Decision Outcome

The migration was completed successfully ([PR #4054](https://github.com/eclipse-sw360/sw360/pull/4054)) and merged on April 15, 2026. All tests pass. The upgrade was primarily mechanical (package relocations and API replacements) with no fundamental architecture changes required.

---

*This program and the accompanying materials are made available under the terms of the Eclipse Public License 2.0 which is available at https://www.eclipse.org/legal/epl-2.0/*

