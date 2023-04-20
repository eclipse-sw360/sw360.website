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
