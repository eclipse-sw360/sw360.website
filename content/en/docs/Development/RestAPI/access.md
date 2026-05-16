---
title: "API Access"
linkTitle: "API Access"
weight: 10
description: "Comprehensive SW360 REST API authentication guide with curl examples for Basic, API Token, OAuth2 grants, and Keycloak."
---

This page is the canonical authentication guide for calling SW360 REST API
endpoints with curl.

For endpoint-level resource documentation, see
[SW360 Rest API]({{< relref path="Dev-REST-API.md" >}}).

## Setup

Use these environment variables in the examples:

```bash
SW360_HOST='https://<my_sw360_server>'
RESOURCE_API="$SW360_HOST/resource/api"
AUTH_SERVER="$SW360_HOST/authorization"

ADMIN_USER='<admin@sw360.org>'
ADMIN_PASS='<admin-password>'

API_USER='<normal.user@sw360.org>'
API_PASS='<user-password>'

CLIENT_ID='<oauth-client-id>'
CLIENT_SECRET='<oauth-client-secret>'

KC_TOKEN_URL='https://<keycloak-host>/realms/<realm>/protocol/openid-connect/token'
```

## Authentication Mechanisms Overview

| Mechanism | Header / Credential | Typical Use | Credential Lifecycle |
| --- | --- | --- | --- |
| HTTP Basic | `Authorization: Basic <base64(user:password)>` | One-off admin/debug calls | User password lifecycle |
| API Token | `Authorization: Token <token>` | User- or service-owned long-lived integrations | SW360 token validity settings |
| OAuth2 `client_credentials` | `Authorization: Bearer <jwt>` | Service-to-service automation | OAuth client + short-lived JWT |
| OAuth2 `authorization_code` (+ PKCE) | `Authorization: Bearer <jwt>` | End-user delegated UI access | Browser login + code exchange |
| Keycloak OIDC/OAuth2 | `Authorization: Bearer <jwt>` | External IAM/SSO deployments | Keycloak token lifecycle |

## Which Mechanism Should I Use?

- One-off admin debug or smoke test: use **HTTP Basic**.
- Long-lived integration owned by a SW360 user: use **API Token**.
- Non-interactive service-to-service integration: use **OAuth2 `client_credentials`**.
- End-user delegated access from browser/UI: use **OAuth2 `authorization_code` + PKCE**.
- Centralized enterprise identity/SSO: use **Keycloak**.

## Authorization Model in `resource-server`

- `GET /api/**` requires `TOKEN_READ`.
- `POST`, `PUT`, `PATCH`, `DELETE /api/**` require `TOKEN_WRITE`.

SW360 merges user-group authorities (for example `READ`, `WRITE`, `ADMIN`) with
token capability authorities (`TOKEN_READ`, `TOKEN_WRITE`) before endpoint checks.

## 1) HTTP Basic

### When to Use

- Local testing, admin diagnostics, short-lived manual calls.

### When Not to Use

- Production automation or integrations where credentials should not be sent each request.

### Prerequisites

- Basic auth must be enabled (`sw360.security.http-basic.enabled=true`).

### End-to-End curl

```bash
curl -sS \
  --user "$API_USER:$API_PASS" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

Expected: `200 OK` and JSON/HAL response.

### Common Failures

- `401 Unauthorized`: wrong username/password, or Basic auth disabled.
- `403 Forbidden`: authenticated user lacks required write capability for method.

## 2) API Token (Personal or Service Token)

### When to Use

- Scripted integration tied to a SW360 user identity.
- Read-only or read/write token capability requirements.

### When Not to Use

- You need delegated browser-based user consent flow.

### Prerequisites

- Token endpoint access with a valid SW360 user.
- Token validity configured via:
  - `rest.apitoken.read.validity.days`
  - `rest.apitoken.write.validity.days`

### End-to-End curl

Create a token (endpoint shape can vary by version; inspect live OpenAPI first):

```bash
curl -sS \
  --user "$API_USER:$API_PASS" \
  -H 'Content-Type: application/json' \
  -X POST "$RESOURCE_API/users/tokens" \
  -d '{"name":"ci-read-token","writeAccess":false}'
```

Use token for API call:

```bash
API_TOKEN='<token-value>'

curl -sS \
  -H "Authorization: Token $API_TOKEN" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

Expected: `200 OK`.

### Common Failures

- `401 Unauthorized`: token expired, malformed, or revoked.
- `403 Forbidden`: token has only read capability but request method requires write.

## 3) OAuth2 via SW360 Authorization Server

### 3.1 `client_credentials`

#### When to Use

- Headless service-to-service calls where no user interaction is possible.

#### When Not to Use

- User-delegated actions that require individual user identity (use `authorization_code` instead).

#### Prerequisites

Admin registers an OAuth client via `/authorization/client-management`:

```bash
curl -sS \
  --user "$ADMIN_USER:$ADMIN_PASS" \
  -H 'Content-Type: application/json' \
  -X POST "$AUTH_SERVER/client-management" \
  -d '{"description":"ci-client","scope":["READ","WRITE"],"authorities":["BASIC"],"access_token_validity":3600,"refresh_token_validity":3600}'
```

> [!IMPORTANT]
> Treat the returned `client_secret` as sensitive and store it immediately.
> Do not rely on list/read responses to retrieve plaintext credentials later —
> secrets are stored hashed after creation.

#### End-to-End curl

Mint token:

```bash
curl -sS \
  --user "$CLIENT_ID:$CLIENT_SECRET" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'grant_type=client_credentials&scope=READ' \
  "$AUTH_SERVER/oauth2/token"
```

Call API:

```bash
ACCESS_TOKEN='<jwt-access-token>'

curl -sS \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

#### Common Failures

- `401 Unauthorized`: wrong `client_id`/`client_secret`, unknown issuer, or token expired.
- `403 Forbidden`: token scope/capability mismatch (`READ` token used for write endpoint).

---

### 3.2 `authorization_code` (+ PKCE)

#### When to Use

- Browser-based or native applications acting on behalf of an end user.

#### When Not to Use

- Non-interactive server services — use `client_credentials` instead.

#### Prerequisites

- OAuth client registered with allowed redirect URI(s).
- PKCE-capable client (S256 code challenge method).

#### Flow Summary

1. Generate a random `code_verifier` and derive `code_challenge = BASE64URL(SHA256(code_verifier))`.
2. Redirect the browser to:
   ```
   $AUTH_SERVER/oauth2/authorize
     ?response_type=code
     &client_id=$CLIENT_ID
     &redirect_uri=https://<my-app>/oauth/callback
     &scope=openid READ WRITE
     &code_challenge=<code_challenge>
     &code_challenge_method=S256
   ```
3. User authenticates and approves.
4. Client receives `code` parameter on the redirect URI.
5. Client exchanges code for token:

```bash
AUTH_CODE='<authorization-code-from-redirect>'
CODE_VERIFIER='<original-pkce-code-verifier>'
REDIRECT_URI='https://<my-app>/oauth/callback'

curl -sS \
  --user "$CLIENT_ID:$CLIENT_SECRET" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=authorization_code&code=$AUTH_CODE&redirect_uri=$REDIRECT_URI&code_verifier=$CODE_VERIFIER" \
  "$AUTH_SERVER/oauth2/token"
```

#### Common Failures

- `400 invalid_grant`: code already used or expired (single-use).
- `400 invalid_client`: `client_id`/`client_secret` mismatch.

## 4) Keycloak (External OIDC)

Use this when SW360 `resource-server` is configured to trust a Keycloak issuer
via `sw360.security.jwt.issuers`. Each entry additionally accepts an optional
`jwk-set-uri` to fetch JWKS over a loopback / internal URL — see
[Resource Server Configuration](../../Deployment/Deploy-Configuration-Files.md#multi-issuer-jwt-setup).

### When to Use

- Enterprise/SSO environments with a central Keycloak instance.

### When Not to Use

- Deployments using the SW360 built-in Authorization Server only.

### Prerequisites

- Keycloak realm and SW360 client configured with required scopes (`READ`, `WRITE`).
- Backend trusted-issuer list includes the Keycloak realm URL.

For Keycloak deployment and realm/client setup, see
[Keycloak Authentication]({{< relref path="../../Deployment/Deploy-Keycloak-Authentication.md" >}}).

### End-to-End curl (`client_credentials` against Keycloak)

```bash
KC_CLIENT_ID='<keycloak-client-id>'
KC_CLIENT_SECRET='<keycloak-client-secret>'

curl -sS \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=client_credentials&client_id=$KC_CLIENT_ID&client_secret=$KC_CLIENT_SECRET&scope=openid email READ" \
  "$KC_TOKEN_URL"
```

Use token against SW360:

```bash
KC_ACCESS_TOKEN='<keycloak-jwt>'

curl -sS \
  -H "Authorization: Bearer $KC_ACCESS_TOKEN" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

### Common Failures (Keycloak)

- `401 Unauthorized`: issuer mismatch (`iss` not in trusted issuers), invalid signature, expired token.
- `403 Forbidden`: scope/capability missing (`READ`/`WRITE` not mapped as required by SW360).

## Refresh Tokens

When the grant returns a `refresh_token`, request a new access token without
re-authenticating the user:

```bash
REFRESH_TOKEN='<refresh-token>'

curl -sS \
  --user "$CLIENT_ID:$CLIENT_SECRET" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d "grant_type=refresh_token&refresh_token=$REFRESH_TOKEN" \
  "$AUTH_SERVER/oauth2/token"
```

## Troubleshooting

### 401 vs 403

- `401 Unauthorized`: authentication failed (bad/missing/expired credential).
- `403 Forbidden`: authentication succeeded, but capability/role is insufficient.

### Token endpoint returns HTML instead of JSON

- Usually reverse-proxy routing is wrong and request is not reaching
  `/authorization/oauth2/token`.

### Scope vs capability mismatch

- `GET /api/**` requires read capability.
- `POST/PUT/PATCH/DELETE /api/**` requires write capability.

### Clock skew on JWT validation

- Ensure system clocks are synchronized (NTP) across SW360, Keycloak, and callers.

## Companion Notes

- For lower-level technical details, see
  [SW360 Rest API]({{< relref path="Dev-REST-API.md" >}}).
- Legacy/historical auth flows are kept at
  [Legacy REST API Access Guide]({{< relref path="Legacy/Legacy-API-Access.md" >}}).
