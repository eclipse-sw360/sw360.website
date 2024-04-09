---
linkTitle: "Initial Setup of Liferay 7.4 and sw360"
title: "Initial Setup of Liferay 7.4 and sw360"
weight: 100
---

After successful , Then if you open the server with the URL `https://localhost:8080/` the following screen should appear:

{{< figure src="/sw360/img/sw360screenshots/deploy74/1.png" >}}

Note that the actual image changes with every liferay version. If there is weird html output without images and plain text, then likely some port settings did not work and the pages generated have wrong URLs inside.

{{< figure src="/sw360/img/sw360screenshots/deploy74/2.png" >}}

After login the sw360 is not setup, thus the server does not display much, but a screen like the following:

{{< figure src="/sw360/img/sw360screenshots/deploy74/3.png" >}}

## User and Login Settings in Liferay

Go into the control panel area by clicking the items icon (nine small cubes) in the upper right corner and select the control panel tab:

{{< figure src="/sw360/img/sw360screenshots/deploy74/4.png" >}}

Edit this password policy and disable `change Required` if you wish to do so. Click on Save_the bottom of the page to save the selection.

{{< figure src="/sw360/img/sw360screenshots/deploy74/6.png" >}}

Then, go: in `Configuration` >  `Instance Settings` > `Users` >

{{< figure src="/sw360/img/sw360screenshots/deploy74/7.png" >}}

In this area, select `Default User Associations` to enter SW360 and apply it also to existing users. Click on Save to save the selection:

{{< figure src="/sw360/img/sw360screenshots/deploy74/8.png" >}}

Then, in `Configuration` >  `Instance Settings` > `User Authentication` > `General` to disable all kind of auto login to make sure only authenticated users can log in. You may want to switch off the e-mail verification, because for most of the development times it will not be of much value.

{{< figure src="/sw360/img/sw360screenshots/deploy74/9.png" >}}

Finally, sice Liferay 7.4 some of the bundled modules need to be activated:

* jquery
* font awesome

In oder to do this, please select from the `Configuration` >  `System Settings` > `Third Party` and go to jquery, select the enablement and click on Update:

{{< figure src="/sw360/img/sw360screenshots/deploy74/10.png" >}}

Do the same for Font Awesome:

{{< figure src="/sw360/img/sw360screenshots/deploy74/11.png" >}}

Note that you need to reload the browser or load a new browser window to take changes to effect.

## Setup SW360 for Liferay: Import *.lar Files

For the setup of SW360 in Liferay, the portal description files, `*.lar` files need not be imported. there is no way except from doing this in the UI. If we are wrong with this, please let us know, because it is very annoying that these ever occurring steps cannot be automated with Liferay.

In order to go ahead, switch to the `SW360` area where you can apply site settings:

{{< figure src="/sw360/img/sw360screenshots/deploy74/12.png" >}}

The go into >  `Publishing` > `Import` which shows like this:

{{< figure src="/sw360/img/sw360screenshots/deploy74/13.png" >}}

Then, click on the plus sign in order to import the *.lar file for public pages. You will find the lar files in the [frontend/configuration](https://github.com/eclipse/sw360/tree/master/frontend/configuration) folder of the sw360 repository.

{{< figure src="/sw360/img/sw360screenshots/deploy74/14.png" >}}

As for import settings, follow the selection as shown on the screenshot. It is very important that for the `Public_Pages_7_4_3_18_GA18.lar` file the selection `Public_Pages_7_4_3_18_GA18.lar` is made.

{{< figure src="/sw360/img/sw360screenshots/deploy74/15.png" >}}

Importing permission makes sure that pages are visible according to users rights. For public pages, it is irrelevant_the moment. Overwriting and the write as current user needs to be selected.

After successful importing, the same steps shall be repeated for the `Private_Pages_7_4_3_18_GA18.lar` file.

{{< figure src="/sw360/img/sw360screenshots/deploy74/16.png" >}}

Make sure that `Private_Pages_7_4_3_18_GA18.lar ` is selected. Follow the other selections made as shown on the screenshot ... importing permissions ... mirror with overwriting, use the current author ...

{{< figure src="/sw360/img/sw360screenshots/deploy74/17.png" >}}


If you click then the liferay logo_the upper left corner where the SW360 is, you will return to the application and the following screen should appear:

{{< figure src="/sw360/img/sw360screenshots/deploy74/18.png" >}}

You can close the left menu area by clicking on the upper left icon:

{{< figure src="/sw360/img/sw360screenshots/deploy74/19.png" >}}

Click `Start` to open the private pages. You are still logged in, so the setup account is used to view the pages.

__Important__ The setup account does not belong to a group. Thus, not all view are functional because they require a group membership to work correctly.

{{< figure src="/sw360/img/sw360screenshots/deploy74/20.png" >}}

## Create User Accounts for Test

Click the SW360 `Admin` menu which is_the right and selection the `User` item.

{{< figure src="/sw360/img/sw360screenshots/deploy74/21.png" >}}

Create at least one user with Admin properties. Example:

{{< figure src="/sw360/img/sw360screenshots/deploy74/26.png" >}}


## Real Login

One example user is `user@sw360.org` with the password `12345`. Note that in the import file with the example accounts, the password is provided with a hash. If you would like to generate new (salted) hashes, you can change your password and export the user list using the same portlet where you have imported the users. This functionality can be also used to migrate accounts between servers.

{{< figure src="/sw360/img/sw360screenshots/deploy74/24.png" >}}

After the successful login, SW360 will look as follows.

{{< figure src="/sw360/img/sw360screenshots/deploy74/25.png" >}}
