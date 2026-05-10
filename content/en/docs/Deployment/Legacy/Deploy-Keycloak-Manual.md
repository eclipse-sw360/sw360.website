---
linkTitle: "Manual Keycloak Configuration"
title: "Manual Keycloak Configuration (Legacy)"
weight: 10
description: 
  Historical documentation for manual configuration of Keycloak for SW360.
---

> [!IMPORTANT]
> This document is provided for **historical purposes** and to help developers
> understand the logic behind the automated Terraform/OpenTofu scripts. For all
> modern installations of SW360 v20+, please refer to the
> [Keycloak Authentication](../Deploy-Keycloak-Authentication.md) guide.

## Legacy / Manual Configuration (Keycloak Admin Console)

*(Not Recommended for production environments. Use the Terraform instructions if
possible.)*

These guides are here for understanding the Keycloak configuration. But the most
up-to-date and recommended way to configure Keycloak is using Terraform/OpenTofu.

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
      `issuer`. It will look something like `http://localhost:8083/realms/sw360`
      {{< figure src="/sw360/img/keycloak/keycloak-jwks.png" >}}
    * Update the `issuer-uri` as `http://localhost:8083/realms/sw360` and in the
      `application.yml`.
    * Build and install the backend one more time.

* Create Client in Keycloak.

  {{< figure src="/sw360/img/keycloak/keycloak-client.png" >}}

    * Follow the below steps for client creation:
        * Under *General settings*, enter Client ID which will be used in `.env` file (SW360 Frontend Repo) as well as in rest.

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
    * Goto Clients, then select your newly created client in *Client lists* page.
    * Goto *Client scopes* page, click on Add client scope and there you will see your *READ* and *WRITE* scopes that you need to add.
    * Select both scopes and then click on Add (default).

      {{< figure src="/sw360/img/keycloak/keycloak-client-scope-add.png" >}}

* Create Groups.
    * Goto *Groups* and create different groups that we are going to use in sw360.

      {{< figure src="/sw360/img/keycloak/keycloak-groups.png" >}}

    * Create 7 groups: `ADMIN`, `CLEARING_ADMIN`, `CLEARING_EXPERT`, `ECC_ADMIN`, `SECURITY_ADMIN`, `SW360_ADMIN`, `USER`.

      {{< figure src="/sw360/img/keycloak/keycloak-groups-create.png" >}}

* Create an Attribute.
    * Goto Realm settings then click on *User profile* page where we can create a new attribute.

      {{< figure src="/sw360/img/keycloak/keycloak-attribute.png" >}}

    * Create a new attribute by the name `Department` and give the required permissions as shown in screenshot.

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
    * Goto Authentication and apply the permissions in *Required actions* as shown in screenshot.

      {{< figure src="/sw360/img/keycloak/keycloak-authentication-settings.png" >}}

* Create Users
    * To create a new user one can goto Users section.

      {{< figure src="/sw360/img/keycloak/keycloak-users-create.png" >}}
    * Also check whether user is created in CouchDB or not.
    * Set password for the newly created user by selecting the user and going to the *Credentials* page.

      {{< figure src="/sw360/img/keycloak/keycloak-users-password.png" >}}

## Adding Identity Providers in Keycloak for Azure AD Integration

*(Manual procedure for reference)*

### Step 1: Create an Application in Azure AD
### Step 2: Configure the Application
### Step 3: Configure Keycloak

1. Log in to the Keycloak admin console.
2. Select the realm sw360 to add the identity provider.
3. Go to **Identity Providers** and select **OpenID Connect v1.0** from the dropdown.
4. Fill in the following details:
   - **Alias**: `azure-foss360`
   - **Display Name**: `Login with AzureAD`
   - **Authorization URL**: `https://login.microsoftonline.com/<your-tenant-id>/oauth2/v2.0/authorize`
   - **Token URL**: `https://login.microsoftonline.com/<your-tenant-id>/oauth2/v2.0/token`
   - **Logout URL**: `https://login.microsoftonline.com/<your-tenant-id>/oauth2/v2.0/logout`
   - **User Info URL**: `https://graph.microsoft.com/oidc/userinfo`
   - **Issuer**: `https://login.microsoftonline.com/<your-tenant-id>/v2.0`
   - **JWKS URL**: `https://login.microsoftonline.com/<your-tenant-id>/discovery/v2.0/keys`
   - **Validate Signatures**: ON
   - **Use JWKS URL**: ON
   - **Trust Email**: ON
   - **Client ID**: The Application (client) ID from Azure AD
   - **Client Secret**: The client secret you created in Azure AD
   - **Default Scopes**: `openid profile email`
5. Click **Save**.

### Step 4: Test the Integration
1. Click on Authentication from Left hand Configure Group section
2. Click on Browser Flow
3. Click config of Identity Provider Redirector  {{< figure src="/sw360/img/keycloak/keycloak-browser-flow-identity-provider-redirector-config.png" >}}
4. Provide Default Identity Provider as the value which was given in Identity Providers Alias ( e.g. `azure-foss360` in previous section) and click on save.
5. With this configuration update now access http://localhost:8080 and verify the automatic login with Azure ID redirect.
