---
title: "Generate a Keycloak Token for REST API"
linkTitle: "Keycloak Token"
weight: 35
icon: fas fa-key
---

This guide explains how to generate a Keycloak access token for SW360 REST API
usage with the `client_credentials` flow.

## Before you generate a token: create a client

For SW360 deployments, first create a dedicated Keycloak client and obtain
its `client_id` and `client_secret`.

Follow the existing deployment guide:

- [Keycloak Authentication - User Client Management]({{< relref path="../Deployment/Deploy-Keycloak-Authentication.md#user-client-management" >}})

After that step, come back here with:

- Keycloak base URL (for example `https://<keycloak-host>`)
- Realm name (for example `sw360`)
- `client_id`
- `client_secret`

## Token endpoint and discovery

You can discover the token endpoint from OIDC metadata:

```bash
curl -sS 'https://<keycloak-host>/realms/<realm>/.well-known/openid-configuration'
```

Look for `token_endpoint` in the response.

Typical token endpoint:

```text
https://<keycloak-host>/realms/<realm>/protocol/openid-connect/token
```

## Generate a token (client credentials)

SW360 integrations with Keycloak use:

- `grant_type=client_credentials`
- No password grant

### Read token

```bash
curl --request POST 'https://<keycloak-host>/realms/<realm>/protocol/openid-connect/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'client_id=<client-id>' \
  --data-urlencode 'client_secret=<client-secret>' \
  --data-urlencode 'scope=openid email READ'
```

### Read/Write token

Request `WRITE` only when your integration must modify data:

```bash
curl --request POST 'https://<keycloak-host>/realms/<realm>/protocol/openid-connect/token' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'grant_type=client_credentials' \
  --data-urlencode 'client_id=<client-id>' \
  --data-urlencode 'client_secret=<client-secret>' \
  --data-urlencode 'scope=openid email READ WRITE'
```

Example response format:

```json
{
  "access_token": "<jwt-access-token>",
  "expires_in": 36000,
  "refresh_expires_in": 0,
  "token_type": "Bearer",
  "scope": "email READ WRITE profile"
}
```

### Token validity note

Token lifetime is defined by your Keycloak server configuration. In the
Terraform setup shipped with SW360, user clients are configured with an access
token lifespan of 10 hours (`36000` seconds).

Compared with older long-lived REST tokens (for example up to 90 days), this
can feel less convenient, but it improves security posture by reducing exposure
time if a token is leaked. The `client_credentials` flow is machine-friendly,
so services can request fresh tokens automatically without manual intervention.

| Dimension | Short-lived Keycloak tokens (recommended) | Older long-lived tokens |
| --- | --- | --- |
| Exposure window if leaked | Limited lifetime (for example 10h by default Terraform setup) | Much longer lifetime (for example up to 90 days) |
| Impact of secret/token compromise | Reduced blast radius due to faster expiry | Higher risk because token may remain usable for weeks |
| Rotation behavior | Natural rotation through frequent automated renewal | Often renewed infrequently, which increases stale credential risk |
| Operational model | Designed for machine-to-machine `client_credentials` flows | Commonly depended on manual/human lifecycle actions |
| Audit and incident response | Short validity helps contain incidents quickly | Longer validity can delay effective containment |
| Least-privilege usage | Encourages requesting only needed scopes per integration run | Long-lived broad-scope tokens are harder to control over time |

In practice, short-lived access tokens plus automated retrieval provide stronger
security with minimal operational overhead for service integrations.

## Use token with SW360 REST API

Use the returned token as Bearer authorization:

```bash
curl -X GET \
  -H 'Authorization: Bearer <jwt-access-token>' \
  'https://<my_sw360_server>/resource/api/projects'
```

### Verify your token identity with `/resource/api/users/profile`

Use the same token to verify that:

- the token is accepted by SW360
- the resolved user matches your expected identity

```bash
curl -sS -X GET \
  -H 'Authorization: Bearer <jwt-access-token>' \
  'https://<my_sw360_server>/resource/api/users/profile'
```

Typical successful response may look like:

```json
{
  "email": "admin@sw360.org",
  "userGroup": "ADMIN",
  "department": "DEPARTMENT",
  "fullName": "Test Admin",
  "givenName": "Test",
  "lastName": "Admin",
  "_links": {
    "self": {
      "href": "https://<my_sw360_server>/resource/api/users/byid/<user-id>"
    }
  }
}
```

Check that `email` is your expected account and that `userGroup` matches the
permissions your integration should have.

Live troubleshooting examples from a local test instance:

```text
GET /resource/api/users/profile without token -> 401 Unauthorized
GET /resource/api/users/profile with valid auth -> 200 OK
```

For authentication models and endpoint authorization behavior, see:

- [API Access]({{< relref path="../Development/RestAPI/access.md" >}})

## Common errors

### `invalid_client`

- Wrong `client_id` or `client_secret`
- Client authentication method is not configured as expected

### `invalid_scope`

- Requested scope is not allowed for this client
- `WRITE` requested but the client has only read permissions

### `unauthorized_client`

- Client is not allowed to use `client_credentials`

### `404 Not Found`

- Wrong Keycloak URL, realm, or endpoint path

## Security notes

- Never commit `client_secret` into source control.
- Store secrets in a secret manager or protected CI/CD variables.
- Use HTTPS endpoints only.
- Use the least privilege: request `READ` unless `WRITE` is required.
