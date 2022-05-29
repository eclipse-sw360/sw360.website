The sw360 REST API provides access to sw360 resources for external clients. It consists currently of three Maven modules aggregated in one parent module `rest` in the sw360 distribution.

# Module Structure

The `rest` module provides a REST API infrastructure for sw360 including:
* Module `authorization-server` - OAuth2 Authorization Server, offering typical authorization steps of an OAuth2 workflow.
* Module `resource-server` - REST API Gateway, providing access to the data for authenticated and authorized users / clients.
* Module `rest-common` - only library code that is shared between the other rest modules.

The REST API implementation uses:
* Module `authorization-server` uses the Liferay user management via the Liferay REST API to authenticate users and the users thrift backend service to access user profile data.
* Module `resource-server` uses thrift backend services for accessing sw360 data to deliver it to the external clients.

# API Principles

## Security Principles

The basic security principles are following the OAuth2 standards. So there should be an authorization server which can be the one contained in this project. That one provides access tokens after it authenticated the client and the user using this client. In addition it checks which authorities this client should receive for operating in the user's name.
With this OAuth2 access token the client can query the resource server which will restrict access to the given authorities.
Every client gets an access token as well as an refresh token. As long as the refresh token is valid, the client can gather a new access token without the need of re-authorization of the user.

There are currently three different possibilities for an OAuth2 authorization server implemented:
* Using the contained authorization-server with username/password that are known by Liferay, no matter if Liferay is hosting the credentials itself or is attached to some central user management which it uses to authenticate users.
* Using the contained authorization-server inside an SSO network where an existing proxy can take care of the authentication and passing authenticated user information in configurable headers to the authorization-server which then performs authorization on top.
* Using keycloak as authorization-server. This case is not part of this wiki page and might need special configuration.

## Data Principles

The REST API provides Hypermedia using [HAL](http://stateless.co/hal_specification.html) (Hypertext Application Language).
The following example shows some ideas of the REST API. It can be obtained by

```
https://[hostname]:[port]/resource/api/browser/index.html#/resource/api
```
Note that the response below is maybe not the exact same response of your current version:
```
{
  "_links": {
    "sw360:attachments": {
      "href": "https://dev.sw360.siemens.com/resource/api/attachments{?sha1}",
      "templated": true
    },
    "sw360:components": {
      "href": "https://dev.sw360.siemens.com/resource/api/components"
    },
    "sw360:licenses": {
      "href": "https://dev.sw360.siemens.com/resource/api/licenses"
    },
    "sw360:licenseinfo": {
      "href": "https://dev.sw360.siemens.com/resource/api/licenseinfo"
    },
    "sw360:projects": {
      "href": "https://dev.sw360.siemens.com/resource/api/projects"
    },
    "sw360:releases": {
      "href": "https://dev.sw360.siemens.com/resource/api/releases"
    },
    "sw360:users": {
      "href": "https://dev.sw360.siemens.com/resource/api/users"
    },
    "sw360:vendors": {
      "href": "https://dev.sw360.siemens.com/resource/api/vendors"
    },
    "sw360:vulnerabilities": {
      "href": "https://dev.sw360.siemens.com/resource/api/vulnerabilities"
    },
    "profile": {
      "href": "https://dev.sw360.siemens.com/resource/api/profile"
    },
    "curies": [
      {
        "href": "https://dev.sw360.siemens.com/resource/docs/{rel}.html",
        "name": "sw360",
        "templated": true
      }
    ]
  }
}
```

# API Installation

Both, the `authorization-server` and the `resource-server` can be build using Maven like the rest of the project. Each is generating a Spring Boot server that can be deployed in an application container, e.g. Tomcat.

# API Configuration

Since the `authorization-server` and the `resource-server` are Spring Boot servers, they are configured as usual via `/src/main/resources/application.yml`. In addition some configuration comes historically from `sw360.properties`. Please note that all configurations could be provided centrally in the `/etc/sw360/` directory. As such, the `sw360.properties` sits directly in `/etc/sw360/`. For rest-specific configurations the application considers the location `/etc/sw360/rest`.

## Authorization Server Configuration

### Special Liferay Credentials Configuration

In addition to the general properties in [here](#general-config) the following needs to be configured in the `application.yml` when the authentication via Liferay username/password credentials should be possible:

| Key | Values | Default |
| --- | --- | --- |
| sw360:sw360-portal-server-url | the url of the Liferay instance | n/a (but could be given if environment variable is used like `${SW360_PORTAL_SERVER_URL:http://127.0.0.1:8080}`) |
| sw360:sw360-liferay-company-id | the id of the company in Liferay that sw360 is run for |(but could be given if environment variable is used like `${SW360_LIFERAY_COMPANY_ID:20155}`) |

### Special SSO Configuration

In addition to the general properties in [here](#general-config) the following needs to be configured in the `application.yml` when the authentication via SSO should be possible:

| Key | Values | Default |
| --- | --- | --- |
| security:customheader:enabled | Flag if the components needed for SSO should be active | false |
| security:customheader:headername:intermediateauthstore | the name of the header that can be used for internal data transfer inside one roundtrip - it can be configured here because the proxy has to make sure that this header will not be passed from clients and will be used truly internal only | custom-header-auth-marker |
| security:customheader:headername:email | the name of the header that holds the email of the authenticated user (should be set be the proxy and must never be passed from clients) | authenticated-email |
| security:customheader:headername:extid | the name of the header that holds the extid of the authenticated user (should be set be the proxy and must never be passed from clients) | authenticated-extid |

:heavy_exclamation_mark: Please configure your SSO server and the proxy accordingly. In general, no unauthenticated request should reach the authorization server. And the configured headers should only be set by the proxy. If they are already contained in client requests, they must be removed!

#### Removing Headers in Apache

In Apache you may use the [`mod_headers`](https://httpd.apache.org/docs/current/mod/mod_headers.html) module to remove headers from the client. Using the default values from the table above, at least the following directives should be present in your configuration for all requests that are routed to the `authorization-server`:

```
RequestHeader unset custom-header-auth-marker
RequestHeader unset authenticated-email
RequestHeader unset authenticated-extid
```

### <a name="general-config"></a>General Configuration

Possible properties in `sw360.properties` file are:

| Key | Values | Default |
| --- | --- | --- |
| backend.url | the url where the thrift services can be found | http://127.0.0.1:8080 |
| rest.write.access.usergroup | the user group level (`USER|CLEARING_ADMIN|...`) that is at least required for getting `WRITE` authority (if client has this scope as well) | `ADMIN` |
| rest.admin.access.usergroup | the user group level (`USER|CLEARING_ADMIN|...`) that is at least required for getting `WRITE` authority (is required for managing OAuth2 clients | `ADMIN` |

The values in `sw360.properties` should be migrated to the `application.yml` in the future.

Further important properties in `application.yml` file are:

| Key | Values | Default |
| --- | --- | --- |
| couchdb:url | the url of the CouchDB to use as client store | n/a |
| couchdb:database | the database name of the CouchDB database to use as client store | n/a |
| couchdb:username | if the CouchDB database needs authentication, enter the username here - if it does not need authentication, do not set this property at all, not even with an empty value | null |
| couchdb:password | if the CouchDB database needs authentication, enter the password here - if it does not need authentication, do not set this property at all, not even with an empty value | null |
| sw360:cors:allowed-origin | value for cross origin resource sharing | n/a |
| security:oauth2:resource:id | should just be the same then in the resource server | n/a |

After this configuration is done the normal REST service for client management should be usable. This one is only accessible for authenticated users that get the `ADMIN` authority (remember, the therefore necessary sw360 usergroup has just been configured). So the clients can be configured now.

# Client Management

In the scenarios of this page, the shipped authorization server is used. So the next step is to configure a valid OAuth2 client in this authorization server. There should be one OAuth2 client per external REST API client (which in turn can have many different users). Therefore the authorization server offers a REST API for basic CRUD operations for configuring the clients that are stored in the just configured CouchDB. Since sw360-`ADMIN` privileges are needed for client management, an authentication is needed to work with this API.

For SSO users (basic-auth Liferay users can use other tools as well because other tools can handle basic auth - but they can also use this workflow):
1. Open a browser with developer tools capabilities
2. Open
    ```
    https://[hostname]:[port]/authorization/client-management
    ```
    This page always shows the currently configured clients and can be refreshed after every manipulation of a client.

3. To add a new client, enter the following javascript in the dev tools console in the current browser tab - of course after manipulating the client data to suit your needs
    ```
    xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.open('POST', '/authorization/client-management', false);
    xmlHttpRequest.setRequestHeader('Content-Type', 'application/json');
    xmlHttpRequest.setRequestHeader('Accept', 'application/json');
    xmlHttpRequest.send(JSON.stringify(
      {
        "description" : "my first test client",
        "authorities" : [ "BASIC" ],
        "scope" : [ "READ" ],
        "access_token_validity" : 3600,
        "refresh_token_validity" : 3600
      }
    ));
    console.log(xmlHttpRequest.responseText);
    ```
4. to manipulate an existing client, do the same but add the clientid to the data object
    ```
        "client_id" : "9e358ca832ce4ce99a770c7bd0f8e066"
    ```
5. to remove an existing client, enter the following javascript in the dev tools console
    ```
    xmlHttpRequest = new XMLHttpRequest();
    xmlHttpRequest.open('DELETE', '/authorization/client-management/9e358ca832ce4ce99a770c7bd0f8e066', false);
    xmlHttpRequest.setRequestHeader('Content-Type', 'application/json');
    xmlHttpRequest.setRequestHeader('Accept', 'application/json');
    xmlHttpRequest.send();
    console.log(xmlHttpRequest.responseText);
    ```

This way the session cookie of the SSO login will be used for the REST calls. This might also be possible in postman or curl or similar tools if you want to try to copy cookies (depending also on the SSO configuration). As said before, if Liferay username/password credentials can be used to authenticate then a tool like postman or curl can be used for the whole process. Just pass the credentials as basic-auth.

### Client Management via Curl

The above described call to create a rest client can also be done directly via one curl call:

```bash
SW360_USER=[admin sw360 user]
SW360_PW=[corresponding sw360 admin user password]
curl -s -S \
     --user "${SW360_USER}:${SW360_PW}" \
     --header "Content-Type: application/json" \
     --header "Accept: application/json" \
     -X POST https://[hostname]:[port]/authorization/client-management \
     -d @- <<EOF
{
    "description" : "my first test client",
    "authorities" : [ "BASIC" ],
    "scope" : [ "READ" ],
    "access_token_validity" : 3600,
    "refresh_token_validity" : 3600
}
EOF
```

This only works with the liferay basic-auth mechanism, SSO is not supported via curl.

## OAuth2 Access Token

Now with a configured client it is possible to retrieve an access token for the REST API from the authorization server. There is again a difference in SSO environments and Liferay username/password environments.

### SSO Backed Access Token

Probably the browser has to be used again because many SSO environments are based on certificates that are read from keycards and the necessary libs are often built into the browser. So just call the URL
```
https://[hostname]:[port]/authorization/oauth/token?grant_type=password&client_id=[clientid]&client_secret=[clientsecret]
```
Of course the client id and the client secret should be replaced by the values of the configured client. The received response should look similar to
```
{
  "access_token" : "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsic3czNjAtUkVTVC1BUEkiXSwidXNlcl9uYW1lIjoiYWRtaW5Ac3czNjAub3JnIiwic2NvcGUiOlsiUkVBRCJdLCJleHAiOjE1NjM4MDYwNDQsImF1dGhvcml0aWVzIjpbIlJFQUQiXSwianRpIjoiZDY4ZWY1YWEtZTQ5My00Y2YxLWI2NGQtNWE5MTdkY2M2ZTYwIiwiY2xpZW50X2lkIjoiMTcyMmZmYzdkZWE3MTU3OGQ5ZWE1ZTZhNmMwMDA4NzMifQ.iO5sLrqRcZfzvMP5gjaJhk3caWyZLkUesdbMfqCGy4V5rbnU9QP1LjdybY0Udh8hvAvhlpqPfaxeKe1c3-gQs5MYlqG0lNQCyWcb7NRHj8VFlwLPuJRZJNk3tybvgITVm9r14pfAXogpVE0S4KihD2W1_SoKH4NzTa2vOEG0CK4VzCLetxUlUuePxZH8ugouqbS2d0SpyeeMTm-PzxzzeTb_4ulGpg63eE1v7GvTsI23uh2WfIgHBa1GRr5jWtE0Meq-5UFCVQkhMm8P-r8wO2iuRblCu6a-bWwy7bfdj3S2VDnqSQskE2dVrC_qMs-V2AGvCV1xvlF0P8A4tgwL-w",
  "token_type" : "bearer",
  "refresh_token" : "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsic3czNjAtUkVTVC1BUEkiXSwidXNlcl9uYW1lIjoiYWRtaW5Ac3czNjAub3JnIiwic2NvcGUiOlsiUkVBRCJdLCJhdGkiOiJkNjhlZjVhYS1lNDkzLTRjZjEtYjY0ZC01YTkxN2RjYzZlNjAiLCJleHAiOjE1NjM4MDYwNDQsImF1dGhvcml0aWVzIjpbIlJFQUQiXSwianRpIjoiM2VkZDcxODAtMTBlYi00Y2MwLTg0NTUtMGYwZmIyMWMwYmU0IiwiY2xpZW50X2lkIjoiMTcyMmZmYzdkZWE3MTU3OGQ5ZWE1ZTZhNmMwMDA4NzMifQ.iMGfdHWpJNseoxIk7tKCNTyC1w4_AJ4cSv6kO64_BkF54MLudvyf9uVSIHpAeHhSFdvhbjksynRqq_u78vW8ptY1la65Qx8glHz0sktWBfMDJsUA4ynU2iZbKU92f2OOf3wQRVt38-Y1mBUsDMIStyKTDeIXGT3LJr_8k5dRAGvayixaezxDFw3dWK2M6P9h-ZnfEP47HpIUZrG8cgwPmNCZ9gBXsqVnueDYZth6TaEKIvWbkZtwY0ikWKyJL2xLm78O1ii3lA5ENt5I0DTfTm8QuK_zcm679W9jF0jvwIR71fM0JSWjkBoXd2h9oLmE2CF2sFVaJor_ermk-L0LsA",
  "expires_in" : 3599,
  "scope" : "READ",
  "jti" : "d68ef5aa-e493-4cf1-b64d-5a917dcc6e60"
}
```
From this response the value of the `access_token` and probably `refresh_token` field is the one to copy-paste for later usage.

### Liferay Backed Access Token

With a Liferay backed authentication all REST clients that offer basic auth support can be used. For example `curl`:

```
curl -X POST --user '[clientid]:[clientsecret]' -d 'grant_type=password&username=[username]&password=[password]' https://[hostname]:[port]/authorization/oauth/token -k
```

Example response:

```
{
  "access_token" : "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsic3czNjAtUkVTVC1BUEkiXSwidXNlcl9uYW1lIjoiYWRtaW5Ac3czNjAub3JnIiwic2NvcGUiOlsiUkVBRCJdLCJleHAiOjE1NjM4MDYwNDQsImF1dGhvcml0aWVzIjpbIlJFQUQiXSwianRpIjoiZDY4ZWY1YWEtZTQ5My00Y2YxLWI2NGQtNWE5MTdkY2M2ZTYwIiwiY2xpZW50X2lkIjoiMTcyMmZmYzdkZWE3MTU3OGQ5ZWE1ZTZhNmMwMDA4NzMifQ.iO5sLrqRcZfzvMP5gjaJhk3caWyZLkUesdbMfqCGy4V5rbnU9QP1LjdybY0Udh8hvAvhlpqPfaxeKe1c3-gQs5MYlqG0lNQCyWcb7NRHj8VFlwLPuJRZJNk3tybvgITVm9r14pfAXogpVE0S4KihD2W1_SoKH4NzTa2vOEG0CK4VzCLetxUlUuePxZH8ugouqbS2d0SpyeeMTm-PzxzzeTb_4ulGpg63eE1v7GvTsI23uh2WfIgHBa1GRr5jWtE0Meq-5UFCVQkhMm8P-r8wO2iuRblCu6a-bWwy7bfdj3S2VDnqSQskE2dVrC_qMs-V2AGvCV1xvlF0P8A4tgwL-w",
  "token_type" : "bearer",
  "refresh_token" : "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsic3czNjAtUkVTVC1BUEkiXSwidXNlcl9uYW1lIjoiYWRtaW5Ac3czNjAub3JnIiwic2NvcGUiOlsiUkVBRCJdLCJhdGkiOiJkNjhlZjVhYS1lNDkzLTRjZjEtYjY0ZC01YTkxN2RjYzZlNjAiLCJleHAiOjE1NjM4MDYwNDQsImF1dGhvcml0aWVzIjpbIlJFQUQiXSwianRpIjoiM2VkZDcxODAtMTBlYi00Y2MwLTg0NTUtMGYwZmIyMWMwYmU0IiwiY2xpZW50X2lkIjoiMTcyMmZmYzdkZWE3MTU3OGQ5ZWE1ZTZhNmMwMDA4NzMifQ.iMGfdHWpJNseoxIk7tKCNTyC1w4_AJ4cSv6kO64_BkF54MLudvyf9uVSIHpAeHhSFdvhbjksynRqq_u78vW8ptY1la65Qx8glHz0sktWBfMDJsUA4ynU2iZbKU92f2OOf3wQRVt38-Y1mBUsDMIStyKTDeIXGT3LJr_8k5dRAGvayixaezxDFw3dWK2M6P9h-ZnfEP47HpIUZrG8cgwPmNCZ9gBXsqVnueDYZth6TaEKIvWbkZtwY0ikWKyJL2xLm78O1ii3lA5ENt5I0DTfTm8QuK_zcm679W9jF0jvwIR71fM0JSWjkBoXd2h9oLmE2CF2sFVaJor_ermk-L0LsA",
  "expires_in" : 3599,
  "scope" : "READ",
  "jti" : "d68ef5aa-e493-4cf1-b64d-5a917dcc6e60"
}
```

Of course, the username and password must be your user credentials and the client id and secret have to be replaced with the configured values. And again, the wanted value is the value of the field `access_token` and probably `refresh_token`.

More Links:

* OAuth2 more information: https://oauth.net/2/
* Decode Bearer tokens at: https://jwt.io/

## OAuth2 Refresh Token

The authorization server supports so called refresh tokens to generate new access tokens after they have been expired. New access tokens can be generated with the use of the `refresh_token` without further re-authorization of the user. The following url must be used:
```
  http://localhost/authorization/oauth/token?grant_type=refresh_token&refresh_token=<REFRESH_TOKEN>
```
The client must pass its credentials via basic authentication. Though a user authentication is not necessary. 
If you are authentication your users on a proxy, you have to configure that proxy in a way that it does not block requests to the above url. As marker the 'grant_type=refresh_token' query parameter may be used.

## Example Apache configuration
The following example shows the relevant part for an Apache proxy to configure
authentication of the `authorization-server` properly:
```
<Location /authorization/oauth/token>
    Order allow,deny
    Allow from all

    <If "%{QUERY_STRING} =~ /^grant_type=refresh_token\&/">
        # No authentication needed
    </If>
    <Else>
        # Configure your authentication here
    </Else>

    ProxyPass https://localhost:8443/authorization/oauth/token
    ProxyPassReverse https://localhost:8443/authorization/oauth/token
</Location>
```

# Resource Server Configuration

Now that access tokens can be generated, the resource server has to be configured. The same general ideas of [general config](#general-config) apply. The properties of the `application.yml` are

| Key | Values | Default |
| --- | --- | --- |
| sw360:thrift-server-url  | the url where the thrift services can be found, e.g. http://localhost:8080 | |
| sw360:test-user-id  | only for developing, simple test user short cut, must be pulled off for productive | |
| sw360:test-user-passwors | see above | |
| sw360:couchdb-url  | the url of the CouhDB server for attachment handling, e.g. https://localhost:5984 | |
| sw360:cors:allowed-origin | value for cross origin resource sharing | n/a |

The REST API is now completely usable via an own client or testwise with integrated tools.

# Tools

To get data and interact with the sw360 REST API the HAL-Browser is recommended. Currently, the HAL-Browser is also deployed on the sw360 development instance, but this is likely to change once the REST API has evolved more. Currently the URL of HAL-Browser is:

```
https://[hostname]:[port]/resource/api/browser/index.html#/resource/api
```
An example for a screenshot is as follows:

![rest-hal-explorer](https://user-images.githubusercontent.com/29916928/39576770-90b2b576-4edf-11e8-9d1b-742c10d88b8e.png)

When using other tools the access token has to be set as header parameter in the REST request. Please add a new header:
- Key: Authorization
- As value you need to enter: `Bearer [ACCESS_TOKEN]` where `[ACCESS_TOKEN]` actually contains the token

## Example – Get a list of projects

Here is an example how to query for all projects as HTTP GET Request. As for the resource endpoint, the request:
```
https://sw360.org/resource/api/projects (or /resource/api/projects)
```
will return the following response:

![rest-explorer2](https://user-images.githubusercontent.com/29916928/39579586-6b1d1736-4ee7-11e8-8faf-da71c8776680.png)

# API Documentation

sw360 deploys a REST API documentation at every instance. There are the following URLs offered at each instance

| URL | Description |
| --- | --- |
| https://[hostname]:[port]/resource/docs/index.html | Small overview page |
| https://[hostname]:[port]/resource/docs/api-guide.html | The API description for the currently running server |
| https://[hostname]:[port]/resource/api/browser/index.html#/resource/api | Integrated HAL browser to directly use the API |

# Known Problems

If you use Nginx or Apache as request front end server there maybe some configuration caveats: The REST API objects provides self links to reference to other objects also including the protocol prefix. These links are realized on Hypertext Application Language (HAL) for example you will find in REST responses:

```  
 "_links": {
    "self": {
     "href": "https://localhost:8443/resource/api/projects/065f3aa45c2683297fd1bb39296f519d"
 }
```

The REST spring boot applications are using the Tomcat environment configuration to generate the HAL links. If the Tomcat is only configured as HTTP, the generated links will contain the `http` protocol and port - which is a problem if the server should be contacted over `https`only. This problem occurs, if tomcat is used together with Nginx, Apache httpd or other Web servers, which are configured to repsond only to `https`.

Solution is to set for example in Nginx HTTP 'X-Forward-*' headers on a reverse proxy, for example:

```
 location / {
   ...
   proxy_set_header        X-Forwarded-Port   443;
   proxy_set_header        X-Forwarded-Proto  https;
 }
```

For other Web severs, there might a similar solution.
