---
title: "Securing SW360"
linkTitle: "Securing SW360"
weight: 5
description: >
  Production security guide covering four authentication methods, JWT signing
  keys, Basic auth hardening, and secret rotation for SW360 v20+.
---

This page is the single reference for securing an SW360 installation. It
covers application-level authentication and credential management. For
infrastructure-level hardening (TLS, network isolation, file permissions,
reverse proxy) see
[Security Best Practices](../Deployment/Deploy-Secure-Deployment.md).

---

## 1. Authentication Modes

SW360 v20 supports four authentication methods, selectable per deployment.
Both bare-metal and container setups configure the same properties, just in
different files.

| Mode | Frontend provider | When to use |
|------|-------------------|-------------|
| `sw360basic` | HTTP Basic username/password | Local development only |
| `sw360oauth` | Built-in OAuth2 Authorization Server | Internal / automation-heavy setups |
| `keycloak` | External Keycloak OIDC | **Recommended for production** |
| `api-token` | Personal Bearer API key (REST API token) | CI, automation, service scripts |

### 1.1. Built-in Basic Auth (`sw360basic`)

The default mode. No extra configuration is required; the frontend sends an
`Authorization: Basic …` header on every request.

**Backend** — default, no change needed.

**Frontend** `.env` (bare-metal) / `config/front-end/.env.frontend` (containers):
```ini
NEXT_PUBLIC_SW360_AUTH_PROVIDER=sw360basic
```

> [!WARNING]
> Basic auth transmits credentials on every request. Disable it in production
> once you have switched to OAuth2 or Keycloak (see [§3](#3-disable-http-basic-auth)).

### 1.2. SW360 Built-in OAuth2 Authorization Server (`sw360oauth`)

SW360 ships a Spring Authorization Server at the `/authorization` endpoint.
It issues JWT access tokens and supports the `client_credentials` and
`authorization_code + PKCE` grant types.

#### Create the default OAuth2 client

Run the helper script once against CouchDB:
```bash
./scripts/addUnsafeDefaultClient.sh
# Flags: --host, --user, --pass to target a remote CouchDB
#        -d  to later delete the client
```
This creates client `trusted-sw360-client` / secret `sw360-secret`.

#### Backend configuration

In `/etc/sw360/rest/application.yml`, add the authorization server issuer to
the trusted-issuer list (or use the single-issuer fallback):

```yaml
sw360:
  security:
    jwt:
      trusted-issuers:
        - http://localhost:8080/authorization
```

For multi-issuer setups (Authorization Server + Keycloak) see
[SW360 Configurations — Multi-Issuer JWT](../Deployment/Deploy-Configuration-Files.md#multi-issuer-jwt-setup).

#### Frontend configuration

Bare-metal `.env` / container `config/front-end/.env.frontend`:
```ini
NEXT_PUBLIC_SW360_AUTH_PROVIDER=sw360oauth
SW360_REST_CLIENT_ID=trusted-sw360-client
SW360_REST_CLIENT_SECRET=sw360-secret
```

#### Generating a token manually

```bash
AUTH_URL=http://localhost:8080/authorization
CLIENT_ID=trusted-sw360-client
CLIENT_SECRET=sw360-secret

# client_credentials — useful for automation/scripts
curl -s -u "$CLIENT_ID:$CLIENT_SECRET" \
  -d 'grant_type=client_credentials&scope=READ WRITE' \
  "$AUTH_URL/oauth2/token" | jq -r .access_token
```

For `authorization_code + PKCE` (interactive browser login):
```
Well-Known URL:      http://localhost:8080/authorization/.well-known/oauth-authorization-server
Authorization URL:   http://localhost:8080/authorization/oauth2/authorize
Token URL:           http://localhost:8080/authorization/oauth2/token
Grant type:          authorization_code
Scope:               openid READ WRITE ADMIN
PKCE:                true
```

### 1.3. Keycloak OpenID Connect (`keycloak`)

The recommended production setup. SW360 ships custom Keycloak user-storage and
event-listener providers.

#### Install and configure Keycloak

See the full installation and Terraform automation guide:
[Keycloak Authentication](../Deployment/Deploy-Keycloak-Authentication.md).

#### Backend configuration

Trust the Keycloak realm issuer in `/etc/sw360/rest/application.yml`:

```yaml
sw360:
  security:
    jwt:
      trusted-issuers:
        - https://keycloak.example.org/realms/sw360
```

To accept tokens from **both** the built-in Authorization Server and Keycloak:
```yaml
sw360:
  security:
    jwt:
      trusted-issuers:
        - http://localhost:8080/authorization
        - https://keycloak.example.org/realms/sw360
```

After changing this, rebuild and reinstall the backend (bare-metal) or restart
the `sw360` container (containers).

#### Frontend configuration

Bare-metal `.env` / container `config/front-end/.env.frontend`:
```ini
NEXT_PUBLIC_SW360_AUTH_PROVIDER=keycloak
SW360_KEYCLOAK_CLIENT_ID=sw360ui
SW360_KEYCLOAK_CLIENT_SECRET=<secret-from-keycloak-admin>
AUTH_ISSUER=https://keycloak.example.org/realms/sw360
```

### 1.4. API Keys (REST API Tokens)

SW360 also supports user-generated long-lived Bearer API keys. These tokens are
independent of interactive browser login and are useful for CI jobs, scripts,
and external integrations.

Users can create API keys in the UI under **Preferences → REST API Tokens**.

```bash
RESOURCE_API=http://localhost:8080/resource/api
API_TOKEN=<user-generated-token>

curl -H "Authorization: Bearer $API_TOKEN" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

Token validity is controlled by `rest.apitoken.read.validity.days` and
`rest.apitoken.write.validity.days` in `sw360.properties`.

---

## 2. JWT Signing Keystore

The built-in Authorization Server (`sw360oauth`) signs JWT tokens with an RSA
key stored in a JKS keystore. The _same_ keystore must be used on every
Authorization Server instance and must persist across restarts; otherwise
previously issued tokens stop validating.

### 2.1. Default development keystore

A bundled default keystore is shipped inside the SW360 WAR as a classpath
resource. It is loaded automatically in development and CI. **Do not use it in
production.**

### 2.2. Generate a production keystore

Use the helper script from the SW360 repository:

```bash
# Set a strong password — keep it secret
JWT_SECRET_KEY='choose-a-strong-password' \
  ./rest/authorization-server/tools/generateJwtStore.sh /etc/sw360/jwt-keystore.jks
```

Or run `keytool` directly:
```bash
keytool -genkeypair \
  -alias jwt \
  -keyalg RSA -keysize 2048 \
  -dname "CN=jwt, O=Your Org, L=City, C=CC" \
  -validity 3650 \
  -keypass 'your-password' \
  -keystore /etc/sw360/jwt-keystore.jks \
  -storepass 'your-password'
```

### 2.3. Configure the password

Set `jwt.secretkey` (bare-metal) or `JWT_SECRETKEY` (containers) to match the
keystore password you chose:

**Bare-metal** `/etc/sw360/authorization/application.yml`:
```yaml
jwt:
  secretkey: your-password
```

**Containers** `config/sw360/.env.backend`:
```env
JWT_SECRETKEY=your-password
```

### 2.4. Container keystore source order

For container deployments the entrypoint resolves the keystore in this order:

1. Docker secret `JWT_KEYSTORE` (operator override — highest priority)
2. Existing `/etc/sw360/jwt-keystore.jks` in the persisted `etc` volume
3. Bundled fallback keystore shipped with the image

To supply your own keystore via Docker secret, point the secret file at your
generated JKS:
```yaml
# docker-compose.yml
secrets:
  JWT_KEYSTORE:
    file: /path/to/your/jwt-keystore.jks
```

### 2.5. Print the active public key

To verify which key is in use (useful after keystore replacement):
```bash
JWT_SECRET_KEY='your-password' \
  ./rest/authorization-server/tools/printKeyPair.sh /etc/sw360/jwt-keystore.jks
```

### 2.6. Keystore rotation

> **Note:** Zero-downtime rotation (publishing two `kid` values simultaneously)
> is planned for a future release. The current process requires a brief
> coordinated restart.

1. Generate a new keystore on the host.
2. Replace the `JWT_KEYSTORE` secret (containers) or copy the new JKS to
   `/etc/sw360/jwt-keystore.jks` on every node (bare-metal).
3. Update `JWT_SECRETKEY` / `jwt.secretkey` if the password changed.
4. Restart the Authorization Server(s).
5. Previously issued tokens will fail validation until clients re-authenticate
   (the resource server refreshes its JWKS cache within one token TTL period).

---

## 3. Disable HTTP Basic Auth

HTTP Basic authentication is enabled by default so the development workflow
works without additional setup. Disable it for production deployments.

### Bare-metal: Spring `prod` profile (recommended)

Add the `prod` profile to Tomcat's JVM options (this picks up
`application-prod.yml` which sets `sw360.security.http-basic.enabled=false`):

```shell
# In /etc/systemd/system/tomcat.service
Environment="JAVA_OPTS=-Dspring.profiles.active=prod"
```

Or as an environment variable before starting:
```shell
export SPRING_PROFILES_ACTIVE=prod
```

### Bare-metal: explicit property override

Add to both `/etc/sw360/rest/application.yml` and
`/etc/sw360/authorization/application.yml`:

```yaml
sw360:
  security:
    http-basic:
      enabled: false
```

### Containers

```env
# config/sw360/.env.backend
SW360_SECURITY_HTTP_BASIC_ENABLED=false
```

After disabling Basic auth all clients must authenticate via one of:
- OAuth2/JWT from the built-in Authorization Server ([§1.2](#12-sw360-built-in-oauth2-authorization-server-sw360oauth))
- OAuth2/JWT from Keycloak ([§1.3](#13-keycloak-openid-connect-keycloak))
- SW360 API keys ([§1.4](#14-api-keys-rest-api-tokens))

---

## 4. SW360 API Keys Details

Users can generate personal long-lived Bearer API keys directly from the SW360
UI under **Preferences → REST API Tokens**, or via the REST endpoint. These
tokens work independently of the OAuth2 flow and are useful for CI/scripting.

```bash
RESOURCE_API=http://localhost:8080/resource/api
TOKEN=<user-generated-token>

curl -H "Authorization: Bearer $TOKEN" \
  "$RESOURCE_API/projects?page=0&page_entries=5"
```

Token validity is controlled by `rest.apitoken.read.validity.days` and
`rest.apitoken.write.validity.days` in `sw360.properties`.

---

## 5. Credential Rotation Checklist

After any initial setup, rotate the following immediately:

- [ ] **JWT signing keystore** — replace the bundled default with a production
  keystore (§2.2 above).
- [ ] **JWT keystore password** (`JWT_SECRETKEY` / `jwt.secretkey`) — change
  from the default `sw360SecretKey`.
- [ ] **OAuth2 client secret** — replace `sw360-secret` with a strong random
  value in both CouchDB and the frontend env.
- [ ] **Keycloak OIDC client secret** — update in both the Keycloak Admin
  Console and the frontend `SW360_KEYCLOAK_CLIENT_SECRET` variable.
- [ ] **Keycloak admin password** (`KC_KEYCLOAK_ADMIN_PASSWORD`) — change on
  first login via the Keycloak Console.
- [ ] **SW360 initial admin password** — change `admin@sw360.org` / `setup@sw360.org`
  immediately after first login.
- [ ] **CouchDB / Postgres passwords** — ensure non-default; disable CouchDB
  "Admin Party" mode if still active.
- [ ] **`NEXTAUTH_SECRET`** — set to a unique random string in the frontend env.

For infrastructure hardening (TLS, network isolation, Tomcat) see
[Security Best Practices](../Deployment/Deploy-Secure-Deployment.md).
