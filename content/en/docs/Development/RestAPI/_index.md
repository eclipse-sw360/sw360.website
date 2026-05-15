---
title: "SW360 RESTful API"
linkTitle: "RESTful API"
weight: 2
---

Using the Web interface makes sense for some use cases, for some other cases the tool integration is more useful. The SW360 software offers a RESTful API. It has been initially developed by a colleague of the BT division - an excellent example of how Inner Source works for projects. Now it has been integrated to the official main project as component that can be deployed along with a SW360 solution.

## Methods of Authentication

Current authentication mechanisms:

1. HTTP Basic (`Authorization: Basic ...`)
2. API Token (`Authorization: Token ...`)
3. OAuth2 `client_credentials` (`Authorization: Bearer ...`)
4. OAuth2 `authorization_code` + PKCE
5. Keycloak OIDC/OAuth2 (`Authorization: Bearer ...`)

See the canonical curl guide here:

- [API Access]({{< relref path="access.md" >}})

Legacy workflows are kept separately:

- [Legacy REST API Guides]({{< relref path="Legacy/_index.md" >}})

API Documentation is available on the instances deployed:

- `https://<my_sw360_server>/resource/docs/api-guide.html`

## Brief Specs
| | |
| --- | --- |
| Implementation Technology | Java-based Spring framework |
| REST Flavor | Hypermedia-driven (HAL) |
| Authentication | Multi-mechanism: Basic, API Token, OAuth2 grants, Keycloak |
| More Technical Information | [SW360 Rest API]({{< relref path="Dev-REST-API.md" >}}) |
