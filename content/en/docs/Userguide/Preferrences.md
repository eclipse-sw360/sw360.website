---
linkTitle: "Preferences"
title: "Preferences"
description: "SW360 Preferences"
Weight: 8
---

# 8. Preferences

The Preferences page allows you to modify the E-mail notification preferences for changes that occur to project/component/release/license.
To open the Preferences page, click on the **Preference** tab from the main menu.

![](/sw360/img/ImagesBasic/Preferences%20Page/Preferences_Page.png)

|Sl.No.|Description|
|:----:|:----------|
|1| [Email Notification Preferences](#82-email-notification-preferences)|
|2|[SW360 User Information](#81-sw360-user-information)|
|3| [REST API Token](#83-rest-api-tokens) |

## 8.1 SW360 User Information

On the **SW360 User** section you can view the following information:

* **Name**
* **E-mail**  
* **Primary Department**
* **External ID**: This is your organization ID.
* **Primary Department Role**: This is the role you are assigned in SW360.
* **Secondary Departments and Roles**: Any other roles which are assigned.

## 8.2 Email Notification preferences

To modify your email notifications, follow the procedure:

![](/sw360/img/ImagesBasic/Preferences%20Page/Edit_email_preferences.png)

1. Check the **Enable E-mail notifications** box which activates Email notifications.
2. Click on the particular section for which you want to change the preference. For e.g., if you want to change the preference for projects, click on the **Project** section. This section will display an expanded view of the available roles.
3. Select the roles that you want to be notified.
4. You can repeat the above procedure for other sections, i.e., **Component**, **Release**, **Moderation** and, **Clearing**.
5. Click on **Update Settings** to update the changes done.

## 8.3 REST API Tokens

REST API is an interface that two computer systems use to exchange information securely over the internet. Via REST endpoint data can be read or written in the database. As a normal user only read token can be generated.

You can generate a REST API token for read access, by following the procedure:

1. Enter a token **Name**.
2. Check the **Authorities** box if you wish to give read access.
3. Set an **Expiration Date** for the token.
4. Click on **Generate Token**.

![](/sw360/img/ImagesBasic/Preferences%20Page/REST_API_TOKENS.png)
