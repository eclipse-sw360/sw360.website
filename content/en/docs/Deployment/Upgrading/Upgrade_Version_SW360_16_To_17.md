---
linkTitle: "Upgrade SW360 from 16.0 to 17.0"
title: "Upgrade SW360 from 16.0 to 17.0"
weight: 100
---


[Checkout source code SW360 to Tag Version 17](#ref1)

[Version of libraries](#ref2)

[Migrate Database](#ref3)

[Build and deploy SW360 Version 17](#ref4)

[Start and Configure Liferay](#ref5)


## Prepare source code to use release 17 {#ref1}

Link contains source: <https://github.com/eclipse/sw360.git>

* Path `SW360_REPOSITORY` = `/home/user/work16to17/sw360`

* Source code sw360 is in main branch with commit version 14.0 . User into `${SW360_REPOSITORY}` use git checkout to tag version 16 on the main branch of SW360
* Checkout to tag  Version 17.0.0

  * `$ git checkout sw360-17.0.0-M1`

* Check version thrift

  * `thrift --version`

* If thrift version 0.14.0 then upgrade Thrift from 0.14.0 to 0.16.0

  * Move to folder sw360 with path `/home/user/work16to17/sw360`

    To uninstall thrift version 0.14.0:

    * `./scripts/install-thrift.sh --uninstall`

    To install thrift version 0.16.0

    * `./scripts/install-thrift.sh`

* Download Liferay Portal CE 7.4.3.18 GA18

  * `$ cd work16to17`

  * `$ wget  https://github.com/liferay/liferay-portal/releases/download/7.4.3.18-ga18/liferay-ce-portal-tomcat-7.4.3.18-ga18-20220329092001364.tar.gz -O liferay-ce-portal-tomcat-7.4.3.18-ga18.tar.gz`

* Extract downloaded file

  * `$ tar -xzf liferay-ce-portal-tomcat-7.4.3.18-ga18.tar.gz`

* Create `portal-ext.properties` file in `liferay-ce-portal-7.4.3.18-ga18` folder

* Copy content from  https://github.com/eclipse/sw360/blob/sw360-17.0.0-M1/frontend/configuration/portal-ext.properties to portal-ext.properties

* Edit `portal-ext.properties`: uncomment below lines

  ```bash
        # default.admin.password=sw360fossy
        # default.admin.screen.name=setup
        # default.admin.email.address.prefix=setup
        # default.admin.first.name=Setup
        # default.admin.last.name=Administrator
    ```

*-* Add lines to setup Postgres. Change jdbc.default.username, jdbc.default.password

```ini
    # Postgres configuration
    jdbc.default.driverClassName=org.postgresql.Driver
    jdbc.default.url=jdbc:postgresql://localhost:5432/lportal
    jdbc.default.username=${postgres_user}
    jdbc.default.password=${postgres_password}
```

* Add lines to setup passsword policies

```ini
    # Passsword policies
    passwords.default.policy.change.required=false
    company.security.send.password.reset.link=false
    company.security.auto.login=false
    company.security.auth.type=emailAddress
    company.security.strangers=false
    company.security.strangers.with.mx=false
    company.security.strangers.verify=false
```

* Remove files in folder `hypersonic` with path: `/home/user/work16to17/liferay-ce-portal-7.4.3.18-ga18/data/hypersonic`

  `$ rm -rf /home/user/work16to17/liferay-ce-portal-7.4.3.18-ga18/data/hypersonic/*`

* Move folder `liferay-ce-portal-7.4.3.18-ga18` to `/opt`

  `$ sudo mv liferay-ce-portal-7.4.3.18-ga18 /opt`

* Set Environment for `${LIFERAY_INSTALL}`

  `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.4.3.18-ga18`

* Move folder `/home/user/work16to17/sw360` run command

  `$ mvn clean install -DskipTests`

* After run command "mvn clean install -DskipTests" above, copy dependency in folder `/home/user/work16to17/sw360/utils/deploy/jars` to  `${LIFERAY_INSTALL}/deploy`

  ```bash
     $ cd /home/user/work16to17/sw360/utils/deploy/jars
     $ sudo cp *.jar /opt/liferay-ce-portal-7.4.3.18-ga18/deploy/
  ```

* We also suggest you change the environment settings (frontend/configuration/setenv.sh) to avoid the lack of memory before making and building SW360.

  ```bash
     $ sudo rm -rf ${LIFERAY_INSTALL}/tomcat-9.0.56/bin/setenv.sh
     $ sudo cp /home/user/work16to17/sw360/frontend/configuration/setenv.sh ${LIFERAY_INSTALL}/tomcat-9.0.56/bin/
  ```

## Version of libraries {#ref2}

| Package Name  | Version  | 
|:--------------|:--------:|
|   Liferay     |  7.4.3   |
|   Tomcat      |  9.0.56  | 
|   Couchdb     |  3.2.2   |
|   Open JDK    |  11.0.15 |
|   Thrift      |  0.16.0  |

## Migrate database {#ref3}

* Check migrate scripts from 16.0 to 17.0 by <https://github.com/eclipse/sw360/tree/master/scripts/migrations>

* File migration:

  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/050_cleanup_eccinformation_duplicate_attributes.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/051_change_eccStatus.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/052_migrate_clearing_request_status.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/053_remove_whitespace_component_name.py`

* Install enviroment for python 2.7

  ```bash
    $ sudo apt-add-repository universe
    $ sudo apt update
    $ sudo apt install python2-minimal
  ```

* Check version

  `$ python2 --version`

* Install pip for python 2.7
  `curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py`

   if there is no proxy, skip option `--proxy=http://username:password@hostname`

     ```bash
        $ sudo python2 get-pip.py --proxy=http://username:password@hostname
        $ pip --version
     ```

* Import package couchdb
  `pip install --proxy=http://username:password@hostname couchdb`

    How to run migration data
    1. stop SW360 (i.e. the tomcat)
        * Set Environment for `${LIFERAY_INSTALL}`
          `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.4.3.18-ga18`

        * Stop SW360 version 16.0, ensure that couchdb is accessible (try to open `http://localhost:5984/_utils/`)
          `$ ${LIFERAY_INSTALL}/tomcat-9.0.56/bin/shutdown.sh`

    2. Ensure that couchdb is accessible (try to open http://localhost:5984/_utils/)

    3. run the migration scripts (i.e. for each script call python2 /PATH/TO/00?_some_migration_script.py)
       be aware that some scripts are using an internal dry-run switch which you have to change manually in the script's code.

       * Mmove to folder with path `/home/user/work16to17/sw360/scripts/migrations`

         Run command:

         ```bash
            $ python2 050_cleanup_eccinformation_duplicate_attributes.py
            $ python2 051_change_eccStatus.py
            $ python2 052_migrate_clearing_request_status.py
            $ python2 053_remove_whitespace_component_name.py
         ```

         Check data change in file log:

           * 050_cleanup_eccinformation_duplicate_attributes.py.log
           * 051_change_eccStatus.py.log
           * 052_migrate_clearing_request_status.log
           * 053_remove_whitespace_component_name.log

## Compile and deploy {#ref4}

* Please set `sw360.liferay.company.id = 20099` in config file `sw360.properties`
* Set Environment for `${LIFERAY_INSTALL}`
  `$ cd /home/user/work16to17/sw360`
  `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.4.3.18-ga18`

  To clean everything and install without running the tests
  `mvn clean install -DskipTests`

* For deployment run the command
  `mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.56/webapps -Drest.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.56/webapps -DskipTests`

## Start and Configure Liferay {#ref5}

* Set Environment for `${LIFERAY_INSTALL}`
  `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.4.3.18-ga18`

* Start liferay

  * `$ ${LIFERAY_INSTALL}/tomcat-9.0.56/bin/startup.sh`

* Log

  * `$ tail -f ${LIFERAY_INSTALL}/tomcat-9.0.56/logs/*`

* Url SW360 : `https://localhost:8080`

### Configure Liferay Portal

* Can follow the steps in the following link https://www.eclipse.org/sw360/docs/deployment/legacy/deploy-liferay7.3 or follow these steps:

- Import users
    1. 	Open the panel on the left side by clicking the button on the top left.
    2. 	Click on `SW360` on the top right to go to the homepage.
    3.	Click on `Start` inside the "Welcome" section.
    4.	Go to `Admin` -> `User` (URL: `/group/guest/users`).
    5.	Scroll down to section `UPLOAD USERS`, select a user file from the very
        beginning and click `Upload Users` on the right side. [A user file can be found here in the sw360vagrant project](https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv)
        * Download: `$ wget https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv`

- Setup liferay:

After successful , Then if you open the server with the URL `https://localhost:8080/` the following screen should appear:

{{< figure src="/sw360/img/sw360screenshots/deploy74/1.png" >}}

Note that the actual image changes with every liferay version. If there is weird html output without images and plain text, then likely some port settings did not work and the pages generated have wrong URLs inside.

{{< figure src="/sw360/img/sw360screenshots/deploy74/2.png" >}}

After login the sw360 is not setup, thus the server does not display much, but a screen like the following:

{{< figure src="/sw360/img/sw360screenshots/deploy74/3.png" >}}

#### User and Login Settings in Liferay

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

#### Setup SW360 for Liferay: Import *.lar Files

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

#### Import User Accounts for Testing

Click the SW360 `Admin` menu which is_the right and selection the `User` item.

{{< figure src="/sw360/img/sw360screenshots/deploy74/21.png" >}}

At the bottom of that view, select a User file to import for testing. Skip it if you will create users differently. You can find a [user account import file](https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv) to import in the `sw360vagrant` project in the folder `shared`. After the user have been imported successfully, they should appear in the table view.

{{< figure src="/sw360/img/sw360screenshots/deploy74/22.png" >}}

After the user have been imported successfully, they should appear in the table view. You can logout for now and use one of the just added accounts (see below):

{{< figure src="/sw360/img/sw360screenshots/deploy74/23.png" >}}

#### Real Login

One example user is `user@sw360.org` with the password `12345`. Note that in the import file with the example accounts, the password is provided with a hash. If you would like to generate new (salted) hashes, you can change your password and export the user list using the same portlet where you have imported the users. This functionality can be also used to migrate accounts between servers.

{{< figure src="/sw360/img/sw360screenshots/deploy74/24.png" >}}

After the successful login, SW360 will look as follows.

{{< figure src="/sw360/img/sw360screenshots/deploy74/25.png" >}}
