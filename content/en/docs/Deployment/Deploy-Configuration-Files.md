### Introduction

This wiki page shows all SW360 configurable property keys!

List of all applicable property files in sw360:
- sw360.properties
- fossology.properties
- couchdb.properties
- search.properties
- orgmapping.properties
- databasetest.properties
- authorization/application.yml
- rest/application.yml


### SW360.properties (/etc/sw360/sw360.properties)

The following table shall give an overview about the general sw360 configuration settings.

| Property Key | Default|
|:-----------|:------------|
| licenseinfo.spdxparser.use-license-info-from-files | true/false |
| mainline.state.enabled.for.user | true/false |
| key.auth.email | EMAIL |
| key.auth.extid | EXTID |
| key.auth.givenname | GIVENNAME |
| key.auth.surname | SURNAME |
| key.auth.department | DEPARTMENT |
| backend.url | http://127.0.0.1:8080 |
| cvesearch.vendor.threshold | 1 |
| cvesearch.product.threshold | 0 | 
| cvesearch.cutoff | 6 |
| combined.cli.parser.external.id.correlation.key | - |
| schedule.cvesearch.firstOffset.seconds | 0 |
| schedule.cvesearch.interval.seconds | "(24*60*60)" |
| autostart | - |
| rest.write.access.usergroup | SW360_ADMIN |
| rest.access.token.validity.seconds | 3600 |
| rest.security.client.id | sw360-trusted-client |
| rest.security.client.secret | sw360-secret |
| programming.languages | ActionScript,AppleScript, Asp,Bash,BASIC, C,C++,C#,Cocoa,Clojure, COBOL,ColdFusion,D, Delphi,Erlang,Fortran, Go,Groovy,Haskell, JSP,Java,JavaScript,Objective-C, Ocaml,Lisp,Perl, PHP,Python,Ruby,SQL ,SVG,Scala,SmallTalk Scheme,Tcl,XML, Node.js,JSON |
| software.platforms | Adobe AIR,Adobe Flash, Adobe Shockwave,Binary Runtime Environment for Wireless,Cocoa (API),Cocoa Touch,Java (software platform)|
| operating.systems | Android,BSD,iOS, Linux,OS X,QNX, Microsoft Windows,Windows Phone,IBM z/OS |
| clearing.teams | org1,org2,org3 |
| state | Active,Phase out,Unknown |
| project.type | Customer Project,Internal Project,Product,Service,Inner Source |
| project.externalkeys | internal.id |
| license.identifiers | - |
| component.categories | framework,SDK,big-data, build-management,cloud,content, database,graphics,http, javaee,library,mail,mobile, security,testing,virtual-machine, web-framework,xml |
| component.externalkeys | com.github.id,com.gitlab.id,purl.id | desc |
| custommap.project.roles |Stakeholder,Analyst,Contributor,Accountant,End user,Quality manager,Test manager,Technical writer,Key user |
| custommap.component.roles | Committer,Contributor,Expert |
| custommap.release.roles | Committer,Contributor,Expert |
| custommap.release.externalIds | - |
| release.externalkeys | org.maven.id,com.github.id,com.gitlab.id,purl.id |
| projectimport.hosts | - |
| preferred.country.codes | DE,AT,CH,US |
| MailUtil_from | _No_Reply__@sw360.org |
| MailUtil_host | - |
| MailUtil_port | 25 |
| MailUtil_enableStarttls | false |
| MailUtil_enableSsl |false |
| MailUtil_isAuthenticationNecessary | true |
| MailUtil_login | - |
| MailUtil_password | - |
| MailUtil_enableDebug | false |
| MailUtil_supportMailAddress | - |
| defaultBegin | - |
| defaultEnd | - |
| unsubscribeNoticeBefore | - |
| unsubscribeNoticeAfter | - |


### fossology.properties (/etc/sw360/fossology.properties)

These configuration parameters are necessary to connect to a fossology server.

| Property Key | Default|
|:-----------|:------------|
| fossology.host | localhost |
| fossology.port | 22 |
| fossology.user | sw360 |
| fossology.key.file | /fossology.id_rsa |
| fossology.key.pub.file | [fossology.key.file] + .pub |



### couchdb.properties (/etc/sw360/couchdb.properties)

CouchDB and Lucene serach configuration properties.

| Property Key | Default|
|:-----------|:------------|
| couchdb.url | http://localhost:5984 |
| couchdb.database | sw360db |
| couchdb.user | - |
| couchdb.password | - |
| couchdb.userdb | sw360users |
| couchdb.attachments | sw360attachments |
| couchdb.fossologyKeys | sw360fossologyKeys |
| couchdb.vulnerability_management | sw360vm |
| lucenesearch.limit | 25 | desc |
| lucenesearch.leading.wildcard* | false |

> \* If you enable lucene leading wildcards you have to enable this configuration also in couchdb-lucene.ini! Leading wildcard search is disabled as default because its a expensive operation. _(couchdb-lucene.ini is part of the couchdb-lucene .war package)_ <br>
> [lucene] <br>
> allowLeadingWildcard=true


### search.properties (/etc/sw360/search.properties)

The following table shall give an overview about the specific search properties

| Property Key | Default|
|:-----------|:------------|
| search.name.max.length | 64 |



### orgmapping.properties (/etc/sw360/orgmapping.properties)

This configuration file is used to activate the sw360 orgmapping feature.

| Property Key | Default|
|:-----------|:------------|
| match.prefix | false |
| enable.custom.mapping | false |


### databasetest.properties (/etc/sw360/databasetest.properties)

Just for couchdb database test purpose.

| Property Key | Default|
|:-----------|:------------|
| couch_db_url | http://localhost:5984 |
| couch_db_database | datahandlertestdb |
| couchdb.username | - |
| couchdb.password | - |

### authorization/application.yml (/etc/sw360/authorization/application.yml)

All of the following built-in properties can be overridden:

```

# Port to open in standalone mode
server:
  port: 8090

# Connection to the couch databases. Will be used to store client credentials
couchdb:
  url: http://localhost:5984
  database: sw360oauthclients
  # if your couchdb does not use authentication, pls just don't use the settings for username and password
  #username:
  #password:

spring:
  jackson:
    serialization:
      indent_output: true

# Common SW360 properties
sw360:
  # The url of the Liferay instance
  sw360-portal-server-url: ${SW360_PORTAL_SERVER_URL:http://127.0.0.1:8080}
  # The id of the company in Liferay that sw360 is run for
  sw360-liferay-company-id: ${SW360_LIFERAY_COMPANY_ID:20155}
  # Allowed origins that should be set in the header
  cors:
    allowed-origin: ${SW360_CORS_ALLOWED_ORIGIN:#{null}}

security:
  # Configuration for enabling authorization via headers, e.g. when using SSO
  # in combination with a reverse proxy server
  customheader:
    headername:
      # You have to enable authorization by headers explicitly here
      enabled: false
      # Attention: please make sure that the proxy is removing there headers
      # if they are coming from anywhere else then the authentication server
      intermediateauthstore: custom-header-auth-marker
      email: authenticated-email
      extid: authenticated-extid
      # also available - at least in saml pre auth - are "givenname", "surname" and "department"

  oauth2:
    resource:
      id: sw360-REST-API
```

### rest/application.yml (/etc/sw360/rest/application.yml)

All of the following built-in properties can be overridden:

```
server:
  port: 8091

spring:
  http:
    multipart:
      max-file-size: 500MB
      max-request-size: 600MB

  data:
    rest:
      base-path: /api

# logging:
#   level:
#     org.springframework.web: DEBUG

security:
  oauth2:
    resource:
      id: sw360-REST-API
      filter-order: 3
      jwt:
        keyValue: |
          -----BEGIN PUBLIC KEY-----
          MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApz8Cr1o5yHMv/FUdF5uy
          VptilqdWtNvw5S6Tr4IaQ4XR9QPt8nlRsjOngfG4QCcKMBWJISldFg8PlJWUBeV+
          6TwQUidxokl2GbO6/+QA+lz1a5Ei1Y1pcnvFeRb2pdYlH3Yg6fXMxS6QwDLk27pZ
          5xbpSDIGISDesyaIMvwaKdhAbFW/tTb/oJY7rCPvmYLT80kJzilijJ/W01jMMSHg
          9Yi5cCt1eU/s78co+pxHzwNXO0Ul4iRpo/CXprQCsSIsdWkJTo6btal1xzd292Da
          d+9xq499JEsNbcqLfCq8DBQ7CEz6aJjMvPkvZiCrFIGxC/Gqmw35DQ4688rbkKSJ
          PQIDAQAB
          -----END PUBLIC KEY-----

sw360:
  thrift-server-url: ${SW360_THRIFT_SERVER_URL:http://localhost:8080}
  test-user-id: admin@sw360.org
  test-user-password: sw360-password
  couchdb-url: ${SW360_COUCHDB_URL:http://localhost:5984}
  cors:
    allowed-origin: ${SW360_CORS_ALLOWED_ORIGIN:#{null}}
```