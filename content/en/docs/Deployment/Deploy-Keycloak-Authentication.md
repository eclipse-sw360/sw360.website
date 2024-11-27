---
linkTitle: "Keycloak based authentication"
title: "Keycloak based authentication"
weight: 101
description: 
  Using Keycloak based authentication for the new SW360 setup.
---

## Install Java 21

* Update the package index: `sudo apt update`
* Install OpenJDK 21: `sudo apt install openjdk-21-jdk`

## Set JAVA_HOME

* Edit the `~/.bashrc` file: `vim ~/.bashrc`
* Add the following line at the end of the file: `export JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64`
* Save and exit the editor.
* Update the environment variables: `source ~/.bashrc`
* Or you can set environment variable in `/etc/environment` file

## Install PostgreSQL

* Install PostgreSQL 14 or higher.
```
sudo apt update && sudo apt upgrade -y
sudo apt install postgresql-14
```

## Set Username and Password in PostgreSQL

* Switch to the PostgreSQL user: `sudo su postgres`
* Access the PostgreSQL console: `psql`
* Execute the following SQL commands:
```
CREATE USER keycloak WITH ENCRYPTED PASSWORD 'mystrongandsecurepassword';
CREATE DATABASE keycloak;
GRANT ALL PRIVILEGES ON DATABASE keycloak TO keycloak;
```

## Install Keycloak

* Download Keycloak 26.0.6 from the official repository.
* Or download the tar file `wget https://github.com/keycloak/keycloak/releases/download/26.0.6/keycloak-26.0.6.tar.gz`
* Extract the downloaded file to the /opt folder, `sudo tar -xvf myfiles.tar -C /opt`
* Goto `/opt/keycloak-26.x.x/conf` folder and setup the following in `keycloak.conf` file:
```
# Database

# The database vendor.
db=postgres

# The username of the database user.
db-username=keycloak

# The password of the database user.
db-password=mystrongandsecurepassword

# The full database JDBC URL. If not provided, a default URL is set based on the selected database vendor.
db-url=jdbc:postgresql://localhost/keycloak

# Changes for SW360
keycloak-admin=admin
keycloak-admin-password=admin

log=console,file

# Should be true for productive
hostname-strict-backchannel=false
hostname-strict-https=false

# Should be false for productive
http-enabled=true
http-port=8083

https-port=8533
```

## Start Keycloak

* Navigate to the Keycloak directory, `cd /opt/keycloak-26.x.x/bin`
* Run the start-dev command for development (with HTTP):
```
./kc.sh start-dev
```
* Run the start command for productive (with HTTPS):
```
./kc.sh start
```
* Run the start command with the necessary parameters(with debug mode):
```
sudo ./kc.sh start-dev  --log="console,file" --debug  --log-level=INFO,org.eclipse.sw360.keycloak.spi:debug,org.eclipse.sw360.keycloak.event.listener:debug
```

## Build the Backend

* Build the SW360 backend code using Maven,
  ```shell
  mvn clean install -DskipTests -Dbase.deploy.dir=/opt/apache-tomcat-11.x.x/ -Dlistener.deploy.dir=/opt/keycloak-26.x.x/providers -P deploy
  ```
* Start the Apache Tomcat server.

## Keycloak Providers and Libraries
Providers are used to read users from SW360 DB and register users from keycloak to SW360 DB.

* After building the backend with deploy profile, following files should be
  copied and available at `/opt/keycloak-26.x.x/providers/`:
```
commonIO-19.0.0.jar
datahandler-19.0.0.jar
httpcore5-5.2.5.jar
libthrift-0.20.0.jar
spring-security-crypto-6.3.3.jar
sw360-keycloak-event-listener.jar
sw360-keycloak-user-storage-provider.jar
```

## Keycloak Admin Console

* Login to Keycloak admin console.

  {{< figure src="/sw360/img/keycloak/keycloak-signin.png" >}}

  ```
  username: admin
  password: admin
  ```

* Create Realm and name it sw360.

  {{< figure src="/sw360/img/keycloak/keycloak-realm.png" >}}

* Get the JWT issuer and key set for realm and update the backend file at
  `rest/resource-server/src/main/resources/application.yml` and reinstall the
  backend. Restart the Tomcat server.
    * Select "OpenID Endpoint Configuration" from the "Realm Settings" and copy
      `jwks_uri`. It will look something like
      `http://localhost:8083/realms/sw360/protocol/openid-connect/certs`
      {{< figure src="/sw360/img/keycloak/keycloak-jwks.png" >}}
    * Update the `issuer-uri` and `jwk-set-uri` in the `application.yml` file
      with this copied `jwks_uri`.
    * Build and install the backend one more time.

* Create Client in Keycloak.

  {{< figure src="/sw360/img/keycloak/keycloak-client.png" >}}

    * Follow the below steps for client creation:
        * Under *General settings*, enter Client ID which will be used in `.env`
          file (SW360 Frontend Repo) as well as in rest.

          {{< figure src="/sw360/img/keycloak/keycloak-create-client.png" >}}

        * In *Capability config* enable Client authentication.

          {{< figure src="/sw360/img/keycloak/keycloak-client-authentication.png" >}}

        * Goto *Login settings* and enter below fields:

          {{< figure src="/sw360/img/keycloak/keycloak-client-settings.png" >}}

          ```
          Home URL: http://localhost:3000
          Valid redirect URIs: http://localhost:3000/api/auth/callback/keycloak, https://oauth.pstmn.io/v1/callback
          Valid post logout redirect URIs: +
          Web origins: *
          ```

* Create Client Scopes.
    * Create `READ` scope by clicking on *Create client scope* button.

      {{< figure src="/sw360/img/keycloak/keycloak-client-scope.png" >}}

    * Similarly create `WRITE` scope.

* Add Scopes to our Client.
    * Goto Clients, then select your newly created client in *Client lists*
      page.
    * Goto *Client scopes* page, click on Add client scope and there you will
      see your *READ* and *WRITE* scopes that you need to add.
    * Select both scopes and then click on Add (default).

      {{< figure src="/sw360/img/keycloak/keycloak-client-scope-add.png" >}}

* Create Groups.
    * Goto *Groups* and create different groups that we are going to use in
      sw360.

      {{< figure src="/sw360/img/keycloak/keycloak-groups.png" >}}

    * Create 7 groups: `ADMIN`, `CLEARING_ADMIN`, `CLEARING_EXPERT`,
      `ECC_ADMIN`, `SECURITY_ADMIN`, `SW360_ADMIN`, `USER`.

      {{< figure src="/sw360/img/keycloak/keycloak-groups-create.png" >}}

* Create an Attribute.
    * Goto Realm settings then click on *User profile* page where we can create
      a new attribute.

      {{< figure src="/sw360/img/keycloak/keycloak-attribute.png" >}}

    * Create a new attribute by the name `Department` and give the required
      permissions as shown in screenshot.

      {{< figure src="/sw360/img/keycloak/keycloak-attribute-settings.png" >}}

* Add Event Listener.
    * Goto *Events* page in Realm settings.
    * Click on event listeners dropdown and select *sw360-add-user-to-couchdb*.

      {{< figure src="/sw360/img/keycloak/keycloak-event-listener.png" >}}

* Access to external Databases.
    * Goto User federation and select *sw360-user-storage-jpa providers*.

      {{< figure src="/sw360/img/keycloak/keycloak-providers.png" >}}

    * Give proper name and create the custom provider.

      {{< figure src="/sw360/img/keycloak/keycloak-providers-create.png" >}}

* Check Authentication Settings
    * Goto Authentication and apply the permissions in *Required actions* as
      shown in screenshot.

      {{< figure src="/sw360/img/keycloak/keycloak-authentication-settings.png" >}}

* Create Users
    * To create a new user one can goto Users section.

      {{< figure src="/sw360/img/keycloak/keycloak-users-create.png" >}}
    * Also check whether user is created in CouchDB or not.
    * Set password for the newly created user by selecting the user and going to
      the *Credentials* page.

      {{< figure src="/sw360/img/keycloak/keycloak-users-password.png" >}}

## Clone SW360 Frontend Repository

* Run the git clone command,
  `git clone git@github.com:eclipse-sw360/sw360-frontend.git`
* Create `.env` file inside the repository and add the following data:
```
NEXTAUTH_SECRET = 'secret'
NEXT_PUBLIC_SW360_API_URL = 'http://localhost:8080'
NEXTAUTH_URL='http://localhost:3000'
NEXT_PUBLIC_SW360_REST_CLIENT_ID='trusted-sw360-client'
NEXT_PUBLIC_SW360_REST_CLIENT_SECRET='sw360-secret'
NEXT_PUBLIC_ENABLE_SW360_OAUTH_PROVIDER='true'
#possible values are sw360basic, sw360oauth, keycloak
NEXT_PUBLIC_SW360_AUTH_PROVIDER='keycloak'
SW360_KEYCLOAK_CLIENT_ID=
SW360_KEYCLOAK_CLIENT_SECRET=
AUTH_ISSUER=http://localhost:8083/realms/sw360
```
* Get `SW360_KEYCLOAK_CLIENT_ID` and `SW360_KEYCLOAK_CLIENT_SECRET` from
  Keycloak console
  * `SW360_KEYCLOAK_CLIENT_ID` will be present in your client's *Settings* page.
  * `SW360_KEYCLOAK_CLIENT_SECRET` will be present in your client's
    *Credentials* page

## Install NVM

* Installs NVM (Node Version Manager)
  `curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.4/install.sh | bash`
* Download and Install Node.js
  `nvm install 20.5.1`
* Verifies the right Node.js version is in the environment
  `node -v` # should print `v20.5.1`
* Verifies the right NPM version is in the environment
  `npm -v` # should print `10.2.4`

## Build the Frontend
```
npm install
npm run build
npm run start
/usr/bin/google-chrome-stable --disable-web-security --user-data-dir="/home/${USER}/cors" --allow-file-access-from-files
```

## Token Creation for REST

* Type of authorization will be OAuth 2.0.
* Enter the below details while creating a new Bearer token:

  {{< figure src="/sw360/img/keycloak/keycloak-postman.png" >}}

```
Clallback URL: https://oauth.pstmn.io/v1/callback
Auth URL: http://localhost:8083/realms/sw360/protocol/openid-connect/auth
Access Token URL: http://localhost:8083/realms/sw360/protocol/openid-connect/token
Get Client Id and Client Secret from Keycloak client
Scope: openid READ WRITE
```
