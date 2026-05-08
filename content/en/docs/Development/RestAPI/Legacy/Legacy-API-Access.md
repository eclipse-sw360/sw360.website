---
title: "Legacy API Access"
linkTitle: "Legacy API Access"
weight: 10
---

This page keeps older authentication and token workflows for reference only.
For current guidance, use [API Access]({{< relref path="../access.md" >}}).

## Legacy: Browser-Based Client Management

Historically, OAuth clients were managed by opening:

- `https://<my_sw360_server>/authorization/client-management`

and issuing `POST`/`DELETE` requests from browser developer tools.

## Legacy: Token Header Conventions

Earlier guides used these token formats:

- `Authorization: Token <Token-Value>`
- `Authorization: Bearer <JWT-Value>`

Both remain useful as historical context, but current mechanism guidance is
maintained in [API Access]({{< relref path="../access.md" >}}).

## Legacy: Password Grant Examples

Older environments frequently used direct password grant requests:

```bash
curl -X POST --user 'trusted-sw360-client:sw360-secret' \
  -d 'grant_type=password&username=user@sw360.org&password=12345' \
  'https://<my_sw360_server>/authorization/oauth/token'
```

This can still appear in legacy deployments, but modern production setups are
typically based on managed OAuth/OIDC and Keycloak configuration.

