---
title: "Backend Logging"
linkTitle: "Backend Logging"
weight: 11
description: "How to configure logging for SW360 backend services"
icon: fas fa-file-lines
---

## Overview

SW360's backend runs two kinds of applications on the same Tomcat instance:

| Kind | Examples | Framework | Logging stack |
|------|----------|-----------|---------------|
| **Thrift servlet WARs** | `vmcomponents.war`, `components.war`, `schedule.war`, `licenses.war`, … | Plain Java servlets (`web.xml`) | Log4j2, via `log4j-1.2-api` bridge |
| **Spring Boot WARs** | `resource.war` (REST API), `authorization.war` (OAuth) | Spring Boot (`@SpringBootApplication`) | Log4j2, via `spring-boot-starter-log4j2` |

Both use **Log4j2** under the hood, but they are configured differently.

---

## Spring Boot applications (REST API & Authorization Server)

The REST resource-server (`resource.war`) and authorization-server
(`authorization.war`) are full Spring Boot applications deployed as WARs.
Spring Boot's `LoggingSystem` manages Log4j2 and reads log levels from
`application.yml`.

### Where to configure

SW360's Spring Boot apps automatically load an **external**
`application.yml` from `/etc/sw360/<app-name>/` as an additional config
location (via `spring.config.additional-location`). This file overrides the
bundled defaults — no need to modify the source tree.

| Application | External config file | Source default (reference only) |
|---|---|---|
| REST API | `/etc/sw360/rest/application.yml` | `rest/resource-server/src/main/resources/application.yml` |
| Auth server | `/etc/sw360/authorization/application.yml` | `rest/authorization-server/src/main/resources/application.yml` |

> **How it works:** `PropertyUtils.createDefaultProperties(APPLICATION_ID)`
> sets `spring.config.additional-location=file:/etc/sw360/<APPLICATION_ID>/`
> at startup. Properties in the external file take precedence over the
> bundled WAR defaults.

### Changing log levels

Add or edit the `logging.level` section in `/etc/sw360/rest/application.yml`:

```yaml
logging:
  level:
    # SW360 REST layer
    org.eclipse.sw360.rest: DEBUG
    # SW360 shared libraries (Thrift clients, DB handlers, etc.)
    org.eclipse.sw360.datahandler: DEBUG
    # Spring Security (auth debugging)
    org.springframework.security: DEBUG
    # IBM Cloudant SDK (CouchDB connection issues)
    com.ibm.cloud.cloudant: DEBUG
```

Then restart Tomcat (or just the specific webapp via the Tomcat manager).

### Using an external Log4j2 config file (alternative)

If `setenv.sh` sets `-Dlog4j2.configurationFile=/etc/sw360/log4j2.properties`
(see [Thrift WARs](#thrift-servlet-wars-backend-services) below), Spring Boot
will detect the property and use that file **instead of** `application.yml`
logging settings. The two approaches are mutually exclusive:

- **`/etc/sw360/rest/application.yml`** — recommended for Spring Boot apps;
  simple YAML, takes effect on restart.
- **External `log4j2.properties`** — gives you a single file for all WARs
  (Thrift + Spring Boot) and supports hot-reload without restart.

> **Tip:** If you want `application.yml` to control the REST apps while the
> external `log4j2.properties` controls Thrift WARs, add this to
> `/etc/sw360/rest/application.yml`:
> ```yaml
> logging:
>   config: classpath:org/springframework/boot/logging/log4j2/log4j2.xml
> ```
> This tells Spring Boot to ignore the `-D` flag and use its own internal
> config (which then respects `logging.level.*` from the YAML).
> In practice, using the external `log4j2.properties` for everything is
> simpler if you want hot-reload.

### Runtime changes

| Method | Change takes effect |
|---|---|
| `/etc/sw360/rest/application.yml` | After Tomcat restart |
| External `log4j2.properties` (with `monitorInterval = 30`) | Within 30 seconds — no restart |

---

## Thrift servlet WARs (backend services)

The Thrift backend WARs (`vmcomponents.war`, `components.war`, `schedule.war`,
etc.) are **plain servlet applications** — they are not Spring Boot apps.
Although `spring-boot.jar` is on their classpath as a transitive dependency,
no `@SpringBootApplication` or Spring `LoggingSystem` is initialised.

This means:

- `application.yml` / `logging.level.*` has **no effect**.
- Log4j2 must be configured via the JVM system property
  `-Dlog4j2.configurationFile=…`.

### Quick Start (3 steps)

#### 1. Create `/etc/sw360/log4j2.properties`

```properties
name = sw360
status = warn
monitorInterval = 30

appender.console.type = Console
appender.console.name = Console
appender.console.target = SYSTEM_OUT
appender.console.layout.type = PatternLayout
appender.console.layout.pattern = %d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n

rootLogger.level = info
rootLogger.appenderRef.console.ref = Console
```

#### 2. Create `$CATALINA_HOME/bin/setenv.sh`

```bash
#!/bin/sh
CATALINA_OPTS="$CATALINA_OPTS -Dlog4j2.configurationFile=/etc/sw360/log4j2.properties"
```

```bash
chmod +x $CATALINA_HOME/bin/setenv.sh
```

#### 3. Restart Tomcat

```bash
$CATALINA_HOME/bin/shutdown.sh && $CATALINA_HOME/bin/startup.sh
```

### Changing log levels at runtime

With `monitorInterval = 30`, Log4j2 checks the file every 30 seconds.
Edit and save — **no Tomcat restart needed**.

### Per-package DEBUG examples

Add logger blocks to `log4j2.properties`:

```properties
# VM Components / SVM sync
logger.svm.name = org.eclipse.sw360.vmcomponents
logger.svm.level = debug
logger.svm.additivity = false
logger.svm.appenderRef.console.ref = Console

# Component service
logger.comp.name = org.eclipse.sw360.components
logger.comp.level = debug
logger.comp.additivity = false
logger.comp.appenderRef.console.ref = Console

# IBM Cloudant SDK (CouchDB session/auth debugging)
logger.cloudant.name = com.ibm.cloud.cloudant
logger.cloudant.level = debug
logger.cloudant.additivity = false
logger.cloudant.appenderRef.console.ref = Console
```

### Rolling file appender (optional)

Useful for the changelog feature (`DatabaseHandlerUtil`). Requires the Tomcat
user having write access to the target directory.

```properties
appender.rolling.type = RollingFile
appender.rolling.name = ChangeLogFile
appender.rolling.fileName = /var/log/sw360changelog.log
appender.rolling.filePattern = /var/log/sw360changelog-%d{yyyy-MM-dd}-%i.log
appender.rolling.layout.type = PatternLayout
appender.rolling.layout.pattern = %d{yyyy-MM-dd HH:mm:ss} %-5p %c{1}:%L - %m%n
appender.rolling.policies.type = Policies
appender.rolling.policies.size.type = SizeBasedTriggeringPolicy
appender.rolling.policies.size.size = 10MB
appender.rolling.strategy.type = DefaultRolloverStrategy
appender.rolling.strategy.max = 3

logger.changelog.name = org.eclipse.sw360.datahandler.db.DatabaseHandlerUtil
logger.changelog.level = debug
logger.changelog.additivity = false
logger.changelog.appenderRef.rolling.ref = ChangeLogFile
logger.changelog.appenderRef.console.ref = Console
```

> **Important:** If you do **not** need the changelog file, omit the
> `ChangeLogFile` appender entirely. Do not reference an appender name that is
> not defined — Log4j2 will emit
> `ERROR Unable to locate appender "ChangeLogFile"` at startup.

---

## Architecture summary

```
┌──────────────────────────────────────────────────────────────────┐
│ Tomcat JVM                                                       │
│                                                                  │
│  -Dlog4j2.configurationFile=/etc/sw360/log4j2.properties         │
│                                                                  │
│  ┌─────────────────────────────┐ ┌──────────────────────────────┐│
│  │ resource.war (Spring Boot)  │ │ vmcomponents.war (Servlet)   ││
│  │                             │ │                              ││
│  │ Logging config:             │ │ Logging config:              ││
│  │  Option A: application.yml  │ │  /etc/sw360/log4j2.properties││
│  │  Option B: log4j2.properties│ │  (via -D system property)    ││
│  │  (via -D system property)   │ │                              ││
│  └─────────────────────────────┘ └──────────────────────────────┘│
│                                                                  │
│  ┌──────────────────────────┐  ┌───────────────────────────┐     │
│  │ authorization.war (SB)   │  │ components.war (Servlet)  │     │
│  │ (same as resource.war)   │  │ schedule.war (Servlet)    │     │
│  │                          │  │ licenses.war (Servlet)    │     │
│  │                          │  │ ... (all other .war)      │     │ 
│  └──────────────────────────┘  └───────────────────────────┘     │
└──────────────────────────────────────────────────────────────────┘
```

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ERROR Unable to locate appender "X"` | Logger references an undefined appender | Define the appender or remove the `appenderRef` |
| DEBUG lines not showing | Logger not configured or wrong package name | Check `logger.xxx.name` matches the Java package |
| `application.yml` logging changes have no effect on Thrift WARs | Thrift WARs are not Spring Boot apps | Use `-Dlog4j2.configurationFile` via `setenv.sh` |
| `application.yml` logging ignored on REST apps | `-Dlog4j2.configurationFile` overrides Spring Boot | Remove the `-D` flag or add `logging.config:` in `application.yml` |
| External `application.yml` not loaded | File not in `/etc/sw360/rest/` (or `/etc/sw360/authorization/`) | Verify path matches: `/etc/sw360/<APPLICATION_ID>/application.yml` |
| Config file changes not picked up | `monitorInterval` not set | Add `monitorInterval = 30` to the config file |
| Config file ignored entirely | `setenv.sh` missing or not executable | Verify file exists and has `chmod +x` |
