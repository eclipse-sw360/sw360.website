---
linkTitle: "SW360 Configurations"
title: "SW360 Configurations"
weight: 50
description:
  SW360 Configurable Property Keys (Files and Database)
---


## Introduction

SW360 configurations are divided into two main categories: **Non-changeable (File-based)** and **Changeable (Database-backed)**.

#### Applicable Property Files:
- `sw360.properties` (Core configurations)
- `couchdb.properties` (CouchDB and Lucene connectivity)
- `orgmapping.properties` (Organization mapping features)
- `couchdb-test.properties` (CouchDB test purpose)
- `authorization/application.yml` (Authorization server settings)
- `rest/application.yml` (Resource server settings)

#### Database Configurations:
Most of the SW360-related properties (UI settings and backend features) are now moved to a database and are accessible via a REST endpoint. These are divided into two containers:
- `SW360_CONFIGURATION` (Backend)
- `UI_CONFIGURATION` (Frontend)

More details can be found in the [Database Configurations](#database-configurations) section below.


### SW360.properties (/etc/sw360/sw360.properties)

The `sw360.properties` file contains properties that are considered non-changeable via the UI and require a Tomcat restart to take effect after updating.

| Property Key | Description | Default |
| :--- | :--- | :--- |
| `backend.url` | Base URL for Thrift | `http://localhost:8080` |
| `MailUtil_host` | SMTP server host address | - |
| `MailUtil_from` | Default sender address for system emails | `__No_Reply__@sw360.org` |
| `MailUtil_port` | SMTP server port | `25` |
| `MailUtil_enableStarttls` | Enable STARTTLS for mail encryption | `false` |
| `MailUtil_enableSsl` | Enable SSL for mail encryption | `false` |
| `MailUtil_isAuthenticationNecessary` | Whether SMTP requires authentication | `false` |
| `MailUtil_login` | SMTP username | - |
| `MailUtil_password` | SMTP password | - |
| `MailUtil_enableDebug` | Enable debugging for mail operations | `false` |
| `MailUtil_supportMailAddress` | Support contact email address | - |
| `defaultBegin` | Header text template for system emails | `*** This is an automatically generated email...` |
| `defaultEnd` | Footer text template for system emails | `With best regards...` |
| `unsubscribeNoticeBefore` | Unsubscribe notice prefix | `*** If you do not wish to receive...` |
| `unsubscribeNoticeAfter` | Unsubscribe notice suffix | `. ***` |
| `svm.components.url` | SVM: Components monitoring endpoint | - |
| `svm.actions.url` | SVM: Actions monitoring endpoint | - |
| `svm.priorities.url` | SVM: Priorities monitoring endpoint | - |
| `svm.components.vulnerabilities.url` | SVM: Component vulnerabilities endpoint | - |
| `svm.vulnerabilities.url` | SVM: Vulnerabilities detail endpoint | - |
| `svm.sw360.api.url` | SVM: Base URL for SVM if not configuring individual SVM endpoints above | - |
| `schedule.svmsync.firstOffset.seconds` | Time offset for SVM sync job (seconds) since 00:00 | `3600` |
| `schedule.svmsync.interval.seconds` | Interval for SVM sync job (seconds) | `86400` |
| `schedule.svmsync.delta.offset.days` | Delta sync overlap window in days; `modified_after` for each delta call is calculated as last sync end-date minus this value | `1` |
| `schedule.svmsync.cleanup.frequency.days` | Days between full syncs; after this many days the next run is a full sync (without `modified_after`) so SVM-side deletions can be purged locally | `7` |
| `schedule.svmmatch.firstOffset.seconds` | Time offset for SVM matching job (seconds) since 00:00 | `7200` |
| `schedule.svmmatch.interval.seconds` | Interval for SVM matching job (seconds) | `86400` |
| `schedule.svmlistupdate.interval.seconds` | Interval for SVM list updates (seconds) | `86400` |
| `schedule.trackingfeedback.firstOffset.seconds` | Time offset for tracking feedback (seconds) since 00:00 | `10800` |
| `schedule.delete.attachment.firstOffset.seconds` | Time offset for attachment deletion (seconds) since 00:00 | `0` |
| `schedule.delete.attachment.interval.seconds` | Interval for attachment deletion (seconds) | `86400` |
| `schedule.department.firstOffset.seconds` | Time offset for department sync (seconds) since 00:00 | `0` |
| `schedule.department.interval.seconds` | Interval for department sync (seconds) | `3600` |
| `subjectFor*` / `textFor*` | Various mail notification subjects and body patterns | - |
| `enable.sw360.change.log` | Enable system-wide changelog writing to a file (in addition to CouchDB) | `false` |
| `sw360changelog.output.path` | Output path for the change log file | `sw360changelog/sw360changelog` |


### couchdb.properties (/etc/sw360/couchdb.properties)

CouchDB and Lucene search configuration properties.

| Property Key | Description | Default |
| :--- | :--- | :--- |
| `couchdb.url` | Base URL of the CouchDB instance | `http://localhost:5984` |
| `couchdb.user` | Database auth username | - |
| `couchdb.password` | Database auth password | - |
| `couchdb.database` | Main SW360 project database | `sw360db` |
| `couchdb.userdb` | Database for user profiles | `sw360users` |
| `couchdb.attachments` | Database for file attachments | `sw360attachments` |
| `couchdb.vulnerability_management` | Database for vulnerability data | `sw360vm` |
| `lucenesearch.limit` | Maximum results for search queries | `25` |
| `lucenesearch.leading.wildcard` | Allow leading wildcards in search | `false` |

> [!NOTE]
> New integration with CouchDB Nouveau does not allow leading wildcards (e.g.
> *sw360) for efficiency and thus this feature should remain disabled.


### orgmapping.properties (/etc/sw360/orgmapping.properties)

This configuration file is used to activate the sw360 orgmapping feature.

| Property Key | Description | Default |
| :--- | :--- | :--- |
| `match.prefix` | Enable prefix matching for organization mapping | `false` |
| `enable.custom.mapping` | Activate custom organization mapping features | `false` |
| `mapping.<id>` | What to match | |
| `mapping.<id>.target` | What to map to | |


### couchdb-test.properties (/etc/sw360/couchdb-test.properties)

This file is used solely for the purpose of CouchDB database connectivity during testing.

| Property Key | Description | Default |
| :--- | :--- | :--- |
| `couch_db_url` | Base URL for test database | `http://localhost:5984` |
| `couch_db_database` | Test database name | `datahandlertestdb` |
| `couchdb.username` | Database auth username (test) | - |
| `couchdb.password` | Database auth password (test) | - |

### authorization/application.yml (/etc/sw360/authorization/application.yml)

The Authorization Server handles OAuth2 tokens and client credentials.

```yaml
server:
  port: 8090

couchdb:
  url: http://localhost:5984
  database: sw360oauthclients
  username: sw360
  password: sw360fossie

jwt:
  secretkey: sw360SecretKey
  auth:
    converter:
      principle-attribute: email

spring:
  jackson:
    serialization:
      indent_output: true
  main:
    allow-circular-references: true

sw360:
  cors:
    allowed-origin: ${SW360_CORS_ALLOWED_ORIGIN:#{null}}

security:
  customheader:
    headername:
      enabled: false
      intermediateauthstore: custom-header-auth-marker
      email: authenticated-email
      extid: authenticated-extid
  oauth2:
    resource:
      id: sw360-REST-API
  accesstoken:
    validity: 30
logging:
  level:
    org.springframework.security: DEBUG
```

#### Getting a REST API Token via `client_credentials`

Clients created in the SW360 Authorization Server can request REST API access
tokens via the OAuth2 `client_credentials` grant. Use the client ID and the
one-time client secret shown when the client was created.

```bash
AUTH_URL=http://localhost:8080/authorization
CLIENT_ID='<client-id>'
CLIENT_SECRET='<client-secret>'

# Read-only token: usable for GET requests and read-side permission checks.
READ_TOKEN=$(curl -s -u "$CLIENT_ID:$CLIENT_SECRET" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials' \
  -d 'scope=READ' \
  "$AUTH_URL/oauth2/token" | jq -r '.access_token')

# Read/write token: required for POST, PUT, PATCH, and DELETE requests.
WRITE_TOKEN=$(curl -s -u "$CLIENT_ID:$CLIENT_SECRET" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials' \
  -d 'scope=READ WRITE' \
  "$AUTH_URL/oauth2/token" | jq -r '.access_token')
```

Use the token against the Resource Server with the standard Bearer scheme:

```bash
# Standalone Resource Server: http://localhost:8091/api
# Tomcat/WAR deployment:     http://localhost:8080/resource/api
RESOURCE_API_URL=http://localhost:8091/api

curl -i \
  -H "Authorization: Bearer $READ_TOKEN" \
  "$RESOURCE_API_URL/projects?page=0&page_entries=5"
```

The token scope limits HTTP method access at the Resource Server:

| Scope | Intended REST API access |
| :--- | :--- |
| `READ` | `GET` requests only |
| `READ WRITE` | `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests |

User roles are still evaluated separately. For example, a read-only token for an
admin user can access admin-restricted read endpoints, but it still cannot use
write HTTP methods unless the token also contains `WRITE` scope.

For a more detailed REST API flow description, see
[API Access](../Development/RestAPI/access.md) and
[REST API](../Development/RestAPI/Dev-REST-API.md#oauth2-access-token).
For Keycloak-issued client-credentials tokens, see
[Keycloak Token](../Userguide/Keycloak-Token.md).

### rest/application.yml (/etc/sw360/rest/application.yml)

The Resource Server provides the SW360 REST API.

```yaml
server:
  servlet:
    context-path: /

management:
  endpoints:
    web:
      base-path: /
      exposure:
        include: health,info
      path-mapping:
        health: /api/health
        info: /api/info
  endpoint:
    health:
      show-details: always
      enabled: true
    info:
      enabled: true
  security:
    enabled: true
  health:
    diskspace:
      enabled: true    # Disable to hide sensitive system information
    ping:
      enabled: true
    ssl:
      enabled: false   # Disabled as not used

spring:
  profiles:
    active: SECURITY_MOCK
  application:
    name: resource
  servlet:
    multipart:
      max-file-size: 500MB
      max-request-size: 600MB
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: http://localhost:8080/authorization

#logging:
#  level:
#    org.springframework.security: DEBUG
#    org.springframework.security.oauth2: DEBUG
#    org.springframework.security.oauth2.provider.endpoint: DEBUG
#    org.springframework.security.oauth2.provider.error: DEBUG
#    org.springframework.security.oauth2.provider.token: DEBUG
#    org.springframework.security.oauth2.provider.token.store: DEBUG
#    org.springframework.security.oauth2.provider.token.store.jwk: DEBUG

jwt:
  auth:
    converter:
      resource-id: sw360-rest-api
      principle-attribute: email

sw360:
  thrift-server-url: ${SW360_THRIFT_SERVER_URL:http://localhost:8080}
  base-url: ${SW360_BASE_URL:http://localhost:8080}
  test-user-id: admin@sw360.org
  test-user-password: 12345
  couchdb-url: ${SW360_COUCHDB_URL:http://localhost:5984}
  cors:
    allowed-origin: ${SW360_CORS_ALLOWED_ORIGIN:#{null}}
  security:
    http-basic:
      enabled: true
    jwt:
      trusted-issuers:
        - http://localhost:8080/authorization
        - http://localhost:8083/realms/sw360

blacklist:
  sw360:
    rest:
      api:
        endpoints:

springdoc:
  api-docs:
    enabled: true
    path: /v3/api-docs
    security:
      oauth2:
        enabled: true
  swagger-ui:
    enabled: true
    path: /index.html
    security:
      oauth2:
        enabled: true
  default-consumes-media-type: application/json
  default-produces-media-type: application/hal+json
```

#### Multi-Issuer JWT Setup

The Resource Server can trust JWTs from more than one issuer. This is useful
when the deployment accepts tokens from both:

* the SW360 Authorization Server, for SW360-managed OAuth clients and
  `client_credentials` tokens; and
* Keycloak, for browser login and externally managed OIDC clients.

Configure all trusted issuer URLs under `sw360.security.jwt.trusted-issuers`:

```yaml
sw360:
  security:
    jwt:
      trusted-issuers:
        - https://sw360.example.org/authorization
        - https://keycloak.example.org/realms/sw360
```

The issuer value must exactly match the token's `iss` claim, including scheme,
host, port, context path, and absence or presence of a trailing slash. The
Resource Server uses issuer discovery to obtain the corresponding JWKS, so each
issuer must publish its OpenID Connect or OAuth2 Authorization Server metadata.
The full `rest/application.yml` example above shows the equivalent local
development values.

If `sw360.security.jwt.trusted-issuers` is not configured, the Resource Server
falls back to the single Spring Boot issuer property:

```yaml
spring:
  security:
    oauth2:
      resourceserver:
        jwt:
          issuer-uri: http://localhost:8080/authorization
```

After changing issuer configuration, restart the Resource Server. Once both
issuers are configured, switching between SW360 Authorization Server tokens and
Keycloak tokens does not require another Resource Server restart.

HTTP Basic authentication is controlled by
`sw360.security.http-basic.enabled`. The example above keeps the development
default (`true`). For production hardening guidance, including disabling Basic
auth via the `prod` profile or an explicit property override, see
[Disable HTTP Basic Authentication](BareMetal/Deploy-20-Natively.md#disable-http-basic-authentication).

## Database Configurations

A significant portion of SW360's configuration is now stored in the database.
These settings are dynamic and can be managed via REST API endpoints without 
requiring a full system restart in most cases.

The configurations are partitioned into two containers:
1. **SW360_CONFIGURATION**: Backend and core logic settings.
2. **UI_CONFIGURATION**: Frontend and UI-specific settings (categories, roles, 
   platforms, etc.).

### SW360 Container (Backend)

| Property Key | Description | Default Value |
| :--- | :--- | :--- |
| `spdx.document.enabled` | This configuration allow to turn ON/OFF SPDX document feature (SPDX Document Tab in release detail page) | `false` |
| `component.visibility.restriction.enabled` | Enable the component visibility restriction feature | `false` |
| `licenseinfo.spdxparser.use-license-info-from-files` | Use license info from files | `true` |
| `mainline.state.enabled.for.user` | Enable editing of mainline state for user | `false` |
| `enable.attachment.store.to.file.system` | Allows storing attachments in the file system | `false` |
| `attachment.delete.no.of.days` | Delete attachments after a specified number of days | `30` |
| `attachment.store.file.system.location` | Configure attachment storage location | `/var/lib/sw360/attachments` |
| `auto.set.ecc.status` | Enable auto set ECC status | `false` |
| `send.project.spreadsheet.export.to.mail.enabled` | Enable sending project spreadsheet export via mail | `false` |
| `send.component.spreadsheet.export.to.mail.enabled` | Enable sending component spreadsheet export via mail | `false` |
| `bulk.release.deleting.enabled` | Enable bulk release deleting feature | `false` |
| `disable.clearing.fossology.report.download` | Disable the ISR generation in fossology process | `false` |
| `rest.force.update.enabled` | Enable force update feature | `false` |
| `sbom.import.export.access.usergroup` | SBOM Import Export Access User Group | `USER` |
| `sw360.tool.name` | The tool name in exported CycloneDx SBOM | `sw360` |
| `sw360.tool.vendor` | The tool vendor in exported CycloneDx SBOM | `eclipse` |
| `package.portlet.enabled` | Enable/disable the package management feature | `true` |
| `package.portlet.write.access.usergroup` | Control the write access user role for packages | `USER` |
| `admin.private.project.access.enabled` | Allow ADMIN users to access private resources | `false` |
| `release.sourcecodeurl.skip.domains` | Regex for domains to skip URL check in Release Source Download URL | `git(hub\|lab).com` |
| `release.friendly.url` | Create URLs in Doc reports | `http://localhost:3000/...` |
| `combined.cli.parser.external.id.correlation.key` | Find correlation key for combined CLI | - |
| `rest.apitoken.length` | Configure the length of generated REST API tokens | `20` |
| `inherit.attachment.usages` | Inherit attachmentUsages of subproject by default | `false` |
| `vcs.hosts` | RepositoryURL class to handle VCS from SBOM | `[]` |
| `svm.notification.url` | Configure the SVM notification URL | - |
| `non.pkg.managed.comps.prop` | Properties of non-package managed components while importing CDX SBOM | - |

### UI Container (Frontend)

| Property Key | Description | Default Value (Snippet) |
| :--- | :--- | :--- |
| `ui.clearing.teams` | List of Clearing Teams for Projects | `["DEPT1", "DEPT2", "DEPT3"]` |
| `ui.clearing.team.unknown.enabled` | Allow 'Unknown' as Clearing Team in Projects | `false` |
| `ui.component.categories` | List of Categories for Components | `["framework", "SDK", ...]` |
| `ui.component.externalkeys` | List of External Keys for Components | `["com.github.id", ...]` |
| `ui.custommap.component.roles` | List of Additional Roles for Components | `["Committer", "Expert"]` |
| `ui.custommap.project.roles` | List of Roles for Projects | `["Stakeholder", ...]` |
| `ui.custommap.release.roles` | List of Custom Roles for Releases | `["Committer", "Expert"]` |
| `ui.custom_welcome_page_guideline` | Enable or Disable Custom Welcome Page Guidelines | `false` |
| `ui.domains` | List of domains allowed for Projects | `["Embedded Software", ...]` |
| `ui.enable.add.license.info.to.release.button` | Enable 'Add License Info to Release' button in Release View | `true` |
| `ui.enable.security.vulnerability.monitoring` | Allow enabling Security Vulnerability Monitoring for Projects | `false` |
| `ui.operating.systems` | Operating Systems to display in Releases | `["Linux", "Windows", ...]` |
| `ui.org.eclipse.sw360.disable.clearing.request.for.project.group` | List of Project Groups for which Clearing Requests are disabled | `["DEPT1", "DEPT2", "DEPT3"]` |
| `ui.programming.languages` | List of programming languages to display in Releases | `["Java", "Python", "C++", ...]` |
| `ui.project.externalkeys` | List of External Keys for Projects | `["internal.id"]` |
| `ui.project.externalurls` | List of External URLs for Projects | `["wiki", "issue-tracker"]` |
| `ui.project.tag` | List of Tags for Projects | `[]` |
| `ui.project.type` | List of types to classify Projects | `["Product", "Service", ...]` |
| `ui.release.externalkeys` | List of External Keys for Releases | `["org.maven.id", ...]` |
| `ui.software.platforms` | List of Software Platforms to display in Releases | `["Java Platform", "Mono", ...]` |
| `ui.state` | List of allowed Project lifecycle states | `["Active", "Phase out"]` |

## Configuration Management via the UI
Since these configurations are accessible over REST API, they can be manipulated
directly from the frontend.

From an **ADMIN** account, goto the frontend, under Admin section, you'd find
Configurations tab, which allows you to manage these configurations. There will
be 2 tabs for each container defined bellow which helps you mainpulate these
configurations directly from the UI.

## Configuration Management via REST API

Configurations can be retrieved and updated using the following endpoints
provided by the Resource Server.

#### Retrieve Configurations
* **Get All Configurations**: `GET /configurations?changeable=<bool>`
    * `changeable=true`: Returns keys managed in the database.
    * `changeable=false`: Returns keys defined in `sw360.properties`.
* **Get Container-Specific Configurations**: `GET /configurations/container/{configFor}?changeable=<bool>`
    * `configFor`: `SW360_CONFIGURATION` (Backend) or `UI_CONFIGURATION`
      (Frontend).

#### Update Configurations
* **Update Database Configs**: `PATCH /configurations/container/{configFor}`
    * Content-Type: `application/json`
    * Description: Updates one or more keys in the specified container.

#### Reloading Policy
* **Database Configs (Changeable)**: Updates are applied immediately upon
  successful `PATCH` operation.
* **File Configs (Non-changeable)**: Updates must be made by editing the
  `sw360.properties` file on the server. A **Tomcat restart** is required to
  load the new values.
