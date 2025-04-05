---
linkTitle: "Initial Setup of Liferay 6.2 and SW360"
title: "Initial Setup of Liferay 6.2 and SW360"
weight: 100
---

## Liferay Administrator Steps

This guide explains how to set up a new Liferay instance after completing the initial setup steps, which include creating an admin account, accepting the license and terms, and providing personal details. If using the [sw360vagrant](https://github.com/sw360/sw360vagrant) or [sw360chores](https://github.com/sw360/sw360chores) deployment, the default setup user credentials are:

- **Username:** `setup@sw360.org`
- **Password:** `sw360fossy` (Unsafe, must be changed in production)

### Steps to Configure Liferay

1. **Log in as a setup administrator.** If using the default password, change it for security reasons.

2. **Modify the password policy:**  
   - Navigate to:
     `Menu Admin -> Item Control Panel -> Section Users, Password Policies`
   - Click on **Default Password Policy** → Actions → Edit
   - Uncheck `Change Required` and save.

3. **Grant new users access to SW360:**  
   - Navigate to:
     `Control Panel -> Configuration -> Users (on the right) -> Default User Associations`
   - Check `Apply to Existing Users`
   - Under **Sites**, enter `SW360`
   - Click **Save**.

4. **Disable self-registration and restrict account creation:**  
   - Navigate to:
     `Control Panel -> Configuration -> Users (on the right) -> Authentication`
   - Uncheck:
     - `Allow strangers to create ...`
     - `Allow strangers to verify ...`
   - Click **Save**.

5. **Ensure self-registration is deactivated:**  
   - Navigate to:
     `Control Panel -> Authentication`
   - Uncheck the options for strangers creating accounts.
   - Click **Save**.
   - **Note:** Disabling self-registration is necessary as Liferay does not create backend service accounts automatically.

6. **Import `.lar` files for page setup:**  
   - Navigate to:
     `Admin -> Pages`
   - Import the following files:
     ```
     frontend/configuration/public_pages.lar
     frontend/configuration/private_pages.lar
     ```
   - Use the **Public Pages** and **Private Pages** tabs.
   - **Note:** These `.lar` files are for Liferay 6.2 GA5. If using another version, you may need to add portlets manually.

7. **Import settings correctly:**  
   - **Do not check:** `Pages -> Change -> Delete Missing Pages`
   - On the first page of the import agent:
     - **Application Configuration**: Choose Applications (leave all checked)
     - **Permissions**: Assign to Roles
   - Click **Continue**.
   - On the second page:
     - **Update Data**: Select `Mirror with overwriting`
     - **Authorship of Content**: Use the current user as author

8. **Verify successful import:**  
   - Navigate to:
     `Private Pages -> Users`

9. **Import user data via CSV:**  
   - The file format should be:
     ```
     GivenName,Lastname,Email,Department,UserGroup,GID,isMale,PasswdHash
     user last name, user first name, first.last@sw360.org,TOP ORG CODE TEAM,USER,SW360_0004,true,AAAAoAAB9ACem9mZj9zptlEjFSMEF5MdOSUzgyxFDmKDGQDK
     ```
   - **Notes:**
     - `GID` must be unique.
     - The hash value represents a password.
     - `GID` corresponds to `External ID` in the thrift-based data model.

## Notes and Troubleshooting

### Checking Liferay Configuration Options
Explore settings to customize your Liferay instance:

- Auto-login and self-registration
- Site statistics
- Password policies
- Additional configurations available in the **Admin Panel**

### Common Issues and Fixes

#### **Liferay Crashes at Startup (Dockbar Exception)**
- If the dockbar error occurs, replace the corrupted file mentioned in the error log with its original version.
- This is a known issue in Liferay 6.2. Search for "Dockbar Liferay problem" for more details.

#### **Performance Issues / Long-running Requests**
- Adjust memory settings in `CATALINA_OPTS` (for Java versions prior to 8):
  ```
  CATALINA_OPTS="$CATALINA_OPTS -Xms2048m -Xmx2048m \
  -XX:NewSize=512m -XX:MaxNewSize=512m \
  -XX:PermSize=512m -XX:MaxPermSize=512m"
  ```

#### **Blank Page (Null Pointer Exception on Main Page)**
- If a blank page with a null pointer error appears, delete the `hsql` folder inside the `data` directory in Liferay.
- Shut down Liferay before deleting the folder and restart after removal.

This completes the initial setup of Liferay 6.2 with SW360. Ensure to follow the steps carefully for a smooth installation and configuration process.

