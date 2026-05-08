---
title: "API Access"
linkTitle: "API Access"
weight: 10
---

This page describes the current SW360 REST API authentication options and the
runtime authorization behavior in the `resource-server`.

## Authentication Mechanisms (Current)

SW360 supports four mechanisms for REST API access:

| Mechanism | Header / Credential | Typical Use |
| --- | --- | --- |
| Basic Auth | `Authorization: Basic <base64(user:password)>` | Human/admin tools and simple scripts |
| API Token | `Authorization: Token <api-token>` | Long-lived personal or service integration |
| OAuth2 Authorization Server | `Authorization: Bearer <jwt>` | OAuth client flow with `/authorization/oauth2/token` |
| Keycloak | `Authorization: Bearer <jwt>` | OIDC/OAuth2 from external IAM |

## Authorization Model in `resource-server`

- `GET /api/**` requires `TOKEN_READ`.
- `POST`, `PUT`, `PATCH`, `DELETE /api/**` require `TOKEN_WRITE`.
- Common read-only endpoints such as `/health`, `/version`, and report download
  can be exposed separately from the write-protected resource endpoints.

SW360 merges user group authorities (for example `READ`, `WRITE`, `ADMIN`) with
token capability authorities (`TOKEN_READ`, `TOKEN_WRITE`) before endpoint checks.

## JWT Validation

Bearer JWTs used with the REST API are validated in two layers:

This applies to Bearer tokens issued either by the SW360 `authorization-server`
or by Keycloak.

1. **Spring Security resource-server validation** using
   `spring.security.oauth2.resourceserver.jwt.issuer-uri` and
   `spring.security.oauth2.resourceserver.jwt.jwk-set-uri` from
   `resource-server` `application.yml`.
2. **SW360 JWKS validation mode** when `jwks.validation.enabled=true` in
   `sw360.properties`. In this path SW360 validates:
   - token signature against `jwks.endpoint.url`
   - expected issuer from `jwks.issuer.url`
   - required time claims such as expiration and issued-at
   - optional audience (`aud`) from `jwt.claim.aud`

If `jwt.claim.aud` is empty, audience validation is skipped. Scope values are
then translated into `TOKEN_READ` and `TOKEN_WRITE` capabilities.

## 1) Basic Authentication

Basic auth authenticates SW360 user credentials and assigns both
`TOKEN_READ` and `TOKEN_WRITE` capabilities after successful login.

```mermaid
sequenceDiagram
    participant Client
    participant RS as Resource Server
    participant UDS as UserDetails Service
    participant DB as SW360 User Store

    Client->>RS: Authorization: Basic base64(user:pass)
    RS->>UDS: loadUserByUsername(user)
    UDS->>DB: Resolve SW360 user
    DB-->>UDS: User + group
    UDS-->>RS: UserDetails + group authorities
    RS->>RS: Password check + add TOKEN_READ/TOKEN_WRITE
    RS-->>Client: Authenticated request processing
```

Example:

```bash
curl -X GET \
  -H "Authorization: Basic <BASE64_USER_PASSWORD>" \
  "https://<my_sw360_server>/resource/api/projects"
```

## 2) API Token (Read or Read/Write)

API tokens are user-owned tokens generated through REST API user endpoints. The
token carries capability authorities (`READ` or `READ+WRITE`) that are mapped to
`TOKEN_READ`/`TOKEN_WRITE` and merged with user group roles.

```mermaid
sequenceDiagram
    participant Client
    participant RS as Resource Server
    participant APIF as API Token Filter
    participant APIP as API Token Provider
    participant DB as SW360 User Store

    Client->>RS: Authorization: Token <token>
    RS->>APIF: Parse token header
    APIF->>APIP: Authenticate token
    APIP->>DB: Find user by token hash
    DB-->>APIP: User + stored token metadata
    APIP->>APIP: Validate expiration + capabilities
    APIP-->>RS: Authenticated principal + merged authorities
    RS-->>Client: Authenticated request processing
```

Token management endpoints:

- `GET /api/users/tokens`
- `POST /api/users/tokens`
- `DELETE /api/users/tokens?name=<token-name>`

Example:

```bash
curl -X GET \
  -H "Authorization: Token <API_TOKEN>" \
  "https://<my_sw360_server>/resource/api/projects"
```

## 3) OAuth2 via SW360 Authorization Server

In this flow, the client obtains a JWT from SW360 `authorization-server` and
calls `resource-server` with `Bearer` token.

```mermaid
sequenceDiagram
    participant Client
    participant AS as Authorization Server
    participant RS as Resource Server

    Client->>AS: Request access token (/authorization/oauth2/token)
    AS-->>Client: JWT access token (+ optional refresh token)
    Client->>RS: Authorization: Bearer <jwt>
    RS->>RS: Decode JWT + map scope to TOKEN_READ/TOKEN_WRITE
    RS-->>Client: Authenticated request processing
```

Example token request:

```bash
curl -X POST \
  --user '<client-id>:<client-secret>' \
  -d 'grant_type=client_credentials&scope=READ' \
  'https://<my_sw360_server>/authorization/oauth2/token'
```

Example API request:

```bash
curl -X GET \
  -H "Authorization: Bearer <ACCESS_TOKEN>" \
  "https://<my_sw360_server>/resource/api/projects"
```

## 4) Keycloak (OIDC/OAuth2)

In Keycloak mode, clients obtain JWTs from Keycloak and call SW360 resource
endpoints with `Bearer` token. Scope values are interpreted as capabilities:

- `READ` => `TOKEN_READ`
- `WRITE` => `TOKEN_READ` + `TOKEN_WRITE`

```mermaid
sequenceDiagram
    participant Client
    participant KC as Keycloak
    participant RS as Resource Server
    participant US as SW360 User Service

    Client->>KC: Token request (OIDC/OAuth2)
    KC-->>Client: JWT (scope includes READ/WRITE)
    Client->>RS: Authorization: Bearer <jwt>
    RS->>US: Resolve SW360 user by email/user_name
    US-->>RS: User + user group
    RS->>RS: Merge group roles with token capabilities
    RS-->>Client: Authenticated request processing
```

For Keycloak setup and realm/client automation, see
[Keycloak Authentication]({{< relref path="../../Deployment/Deploy-Keycloak-Authentication.md" >}}).

## Legacy Guide

Older and historical workflows were moved to:

- [Legacy REST API Access Guide]({{< relref path="Legacy/Legacy-API-Access.md" >}})

