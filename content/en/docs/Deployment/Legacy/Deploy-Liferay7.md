---
linkTitle: "Initial Setup of Liferay 7.2 and sw360"
title: "Initial Setup of Liferay 7.2 and sw360"
weight: 100
---

# Starting SW360 for the First Time

So, the vagrant setup has deployed sw360, but unfortunately, there is some major issue: With Liferay, certain configuration need to be applied manually in the UI. If you would know how to import *.lar files and apply some setting from the command line (without implementing an approach based on HTML testing frameworks, like selenium), please let us know.

Until then, some tasks need to be done manually, after everything has been built up:

* import *.lar files
* set password policies not to change after first login (it is annoying when developing)
* set the default area to be SW360 when users login to liferay
* apply some more settings, like users cannot create accounts on their own

# Setup Login

After successful installation, the screen should look like this. If there is weird html output without images and plain text, then likely some port settings did not work and the pages generated have wrong URLs inside.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.38.53.png" >}}

Sign in_the icon_the upper left corner. If you did not change the values in `configuration.rb`the default login is `setup@sw360.org` and `sw360fossy`.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.39.06.png" >}}

# User Settings in SW360

Go into the control panel area which can be unfold by clicking in the upper left corner. In this area, go for Users > Password Policies and disable `change Required` if you wish to do so. Click on Save to save the selection.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.39.56.png" >}}

Then, in `Configuration` >  `Instance Settings` > `Users` > `Default User Associations` to enter SW360 and apply it also to existing users. Click on Save to save the selection.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.43.32.png" >}}

Then, in `Configuration` >  `Instance Settings` > `User Authentication` > `General` to disable all kind of auto login to make sure only authenticated users can log in.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.46.49.png" >}}

Depending on your preferences make appropriate selections according to the screenshot. It is not advisable to allow users to self register in order to access the SW360 data.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.47.03.png" >}}

# Import *.lar Files

Then, in the `SW360` area >  `Publishing` > `Import` klick on the plus sign in order to import the *.lar file for public pages.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.49.41.png" >}}

As for import settings, follow the selection as shown on the screenshot. It is very important that for the `PublicPages.lar` file the selection `Public Pages` is made.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.51.10.png" >}}

Importing permission makes sure that pages are visible according to users rights. For public pages, it is irrelevant_the moment.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.52.14.png" >}}

Overwriting and the write as current user needs to be selected.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.51.21.png" >}}

After successful importing the following view should appear.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.52.23.png" >}}

The same steps shall be repeated for the `PrivatePages.lar` file.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.52.36.png" >}}

Make sure that `Private Pages` is selected. Follow the other selections made as shown on the screenshots.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.52.58.png" >}}

Importing permissions ...

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.53.01.png" >}}

Mirror with overwriting, use the current author ...

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.53.04.png" >}}

Then the successful result should be shown like this:

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.54.14.png" >}}

If you click then the liferay logo_the upper left corner where the SW360 is, you will return to the application and the following screen should appear. Click `Start` to open the private pages. You are still logged in, so the setup account is used to view the pages.

__Important__ The setup account does not belong to a group. Thus, not all view are functional because they require a group membership to work correctly.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.54.38.png" >}}

# Import User Accounts for Testing

Assuming you are still logged in, the main view of SW360 looks as follows:

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.54.55.png" >}}

Click the SW360 `Admin` menu which is_the right and selection the `User` item.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.55.00.png" >}}

At the bottom of that view, select a User file to import for testing. Skip it if you will create users differently.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.55.12.png" >}}

You can find a user file to import in the `sw360vagrant` project in the folder `shared`.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.55.38.png" >}}

After the user have been imported successfully, they should appear in the table view.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.55.59.png" >}}

After the user have been imported successfully, they should appear in the table view.

# Real Login

One example user is `user@sw360.org` with the password `12345`. Note that in the import file with the example accounts, the passwort is provided with a hash. If you would like to generate new (salted) hashes, you can change your password and export the user list using the same portlet where you have imported the users. This functionality can be also used to migrate accounts between users.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.56.06.png" >}}

After the successful login, SW360 will look as follows.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.56.16.png" >}}

After the successful login, SW360 will look as in the following screenshot.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.56.33.png" >}}

For example, click on `Projects` to see that no projects have been created so far ...

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.57.08.png" >}}
