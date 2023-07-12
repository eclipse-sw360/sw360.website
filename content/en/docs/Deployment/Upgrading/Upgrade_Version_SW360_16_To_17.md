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

* Source code sw360 is in main branch with commit version 16.0.0 . User into `${SW360_REPOSITORY}` use git checkout to tag version 16 on the main branch of SW360
* Checkout to tag  Version 17.0.0

  * `$ git checkout 6c1aeacea3b0c5f37dc1752b5409cce1433e40c2`

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

* Copy file `portal-ext.properties` from `liferay-ce-portal-7.3.4-ga5` folder to `liferay-ce-portal-7.4.3.18-ga18` folder

* Remove files in folder `hypersonic` with path: `/home/user/work16to17/liferay-ce-portal-7.4.3.18-ga18/data/hypersonic`

  `$ rm -rf /home/user/work16to17/liferay-ce-portal-7.4.3.18-ga18/data/hypersonic/*`

* Copy all file `liferay-ce-portal-7.3.4-ga5/osgi/configs` folder to `liferay-ce-portal-7.4.3.18-ga18/osgi/configs` folder

## Liferay Database Migration


* Go to `liferay-ce-portal-7.4.3.18-ga18/tools/portal-tools-db-upgrade-client` folder

* Edit `app-server.properties` to add the following parameters:

```
  dir={LIFERAY_PATH_7.4}/tomcat-9.0.56
  extra.lib.dirs=/bin
  global.lib.dir=/lib
  portal.dir=/webapps/ROOT
  server.detector.server.id=tomcat
```

* Edit `portal-upgrade-database.properties` to add the following parameters:

```
  jdbc.default.driverClassName=org.postgresql.Driver
  jdbc.default.url=jdbc:postgresql://{POSTGRE_HOST}:5432/lportal
  jdbc.default.username={POSTGRES_USER}
  jdbc.default.password={POSTGRES_PASSWORD}
```

* Edit `portal-upgrade-ext.properties` to add the following parameter:

```
  liferay.home={LIFERAY_PATH_7.4}
```

* Finally, you can run the script with the following command:

```
$ ./db_upgrade.sh -j "-Xmx8000m -Dfile.encoding=UTF-8 -Duser.timezone=GMT"
```

* Move folder `liferay-ce-portal-7.4.3.18-ga18` to `/opt`

  `$ sudo mv liferay-ce-portal-7.4.3.18-ga18 /opt`

* Set Environment for `${LIFERAY_INSTALL_7_4}`

  `$ export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18`

* Move folder `/home/user/work16to17/sw360` run command

  `$ mvn clean install -DskipTests`

* After run command "mvn clean install -DskipTests" above, copy dependency in folder `/home/user/work16to17/sw360/deploy/jars` to  `${LIFERAY_INSTALL_7_4}/deploy`

  ```bash
     $ cd /home/user/work16to17/sw360/deploy/jars
     $ sudo cp *.jar /opt/liferay-ce-portal-7.4.3.18-ga18/deploy/
  ```

* We also suggest you change the environment settings (frontend/configuration/setenv.sh) to avoid the lack of memory before making and building SW360 or can reuse 7.3.4's setenv.sh.

  ```bash
     $ sudo rm -rf ${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/bin/setenv.sh
     $ sudo cp /home/user/work16to17/sw360/frontend/configuration/setenv.sh ${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/bin/
  ```

## Install Couchdb Lucene

* SW360 uses for searching the contents of the couchdb databases a lucene-based server named couchdb-lucene

* Run command download Couchdb Lucene
    - `wget --no-check-certificate https://github.com/rnewson/couchdb-lucene/archive/v2.1.0.tar.gz -O couchdb-lucene.tar.gz`

* Note extract couchdb-lucene to folder `work` with path of work: `/home/user/work`
    - `tar -xzf couchdb-lucene.tar.gz`

* Run command:
    - `cd couchdb-lucene-2.1.0`
    - `sed -i "s/allowLeadingWildcard=false/allowLeadingWildcard=true/" ./src/main/resources/couchdb-lucene.ini `
    - `sed -i "s/localhost:5984/admin:password@localhost:5984/" ./src/main/resources/couchdb-lucene.ini `
    - `wget https://raw.githubusercontent.com/sw360/sw360vagrant/master/shared/couchdb-lucene.patch `
    - `patch -p1 < couchdb-lucene.patch `
    - `mvn clean install war:war`
    - `sudo cp target/couchdb-lucene-*.war /opt/liferay-ce-portal-7.4.3.18-ga18/tomcat-9.0.56/webapps/couchdb-lucene.war`

## Version of libraries {#ref2}

| Package Name  | Version  | 
|:--------------|:--------:|
|   Liferay     |  7.4.3   |
|   Tomcat      |  9.0.56  | 
|   Couchdb     |  3.2.2   |
|   Open JDK    |  11.0.15 |
|   Thrift      |  0.16.0  |

* To check couchdb version: run `curl http://localhost_or_yourcouchdbserver:5984 | json_pp` or ''
## Migrate database {#ref3}

* Check migrate scripts from 16.0 to 17.0 by <https://github.com/eclipse/sw360/tree/master/scripts/migrations>

* File migration:

  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/050_cleanup_eccinformation_duplicate_attributes.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/051_change_eccStatus.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/052_migrate_clearing_request_status.py`
  * `https://github.com/eclipse/sw360/blob/main/scripts/migrations/053_remove_whitespace_component_name.py`


* Install pip for python 3

   if there is no proxy, skip option `--proxy=http://username:password@hostname:port`

     ```bash
        $ sudo apt update
        $ sudo apt install python3-pip
     ```

* Import package couchdb
  `pip3 install --proxy=http://username:password@hostname:port couchdb`

    How to run migration data
    1. stop SW360 (i.e. the tomcat)
        * Set Environment for `${LIFERAY_INSTALL_7_4}`
          `$ export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18`

        * Stop SW360 version 16.0 with path `LIFERAY_INSTALL_7_3= /opt/liferay-ce-portal-7.3.4-ga5`
          `$ ${LIFERAY_INSTALL_7_3}/tomcat-9.0.33/bin/shutdown.sh`

    2. Ensure that couchdb is accessible (try to open `http://localhost:5984/_utils/`)

    3. run the migration scripts (i.e. for each script call python3 /PATH/TO/00?_some_migration_script.py)
       be aware that some scripts are using an internal dry-run switch which you have to change manually in the script's code.

       * Move to folder with path `/home/user/work16to17/sw360/scripts/migrations`
       * Edit file migration to add the following parameters:

              ```
                DRY_RUN = False
                # set admin name and password for couchdb3
                DB_USER_NAME = 'admin'
                DB_USER_PASSWORD = 'password'
                # set credentials for couchdb3
                couch.resource.credentials=(DB_USER_NAME, DB_USER_PASSWORD)
              ```
       * Need to update 052 for python script
          - Python 2.x code with Python 3.x. In Python 2, print is a statement and can be used without parentheses. However, in Python 3, print is a function and therefore always requires parentheses.
        - Install library `pandas` of python.
          - ```$ pip3 install pandas ```

        - Run command:

         ```bash
            $ python3 050_cleanup_eccinformation_duplicate_attributes.py
            $ python3 051_change_eccStatus.py
            $ python3 052_migrate_clearing_request_status.py
            $ python3 053_remove_whitespace_component_name.py
         ```

         Check data change in file log:

           * 050_cleanup_eccinformation_duplicate_attributes.py.log
           * 051_change_eccStatus.py.log
           * 052_migrate_clearing_request_status.log
           * 053_remove_whitespace_component_name.log

## Compile and deploy {#ref4}

* Set Environment for `${LIFERAY_INSTALL_7_4}`
  `$ cd /home/user/work16to17/sw360`
  `$ export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18`

  To clean everything and install without running the tests
  `mvn clean install -DskipTests`

* For deployment run the command
  `mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL_7_4}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/webapps -Drest.deploy.dir=${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/webapps -Dtest=org/eclipse/sw360/rest/resourceserver/restdocs/* -Dsurefire.failIfNoSpecifiedTests=false -DRunRestIntegrationTest=true `

## Start and Configure Liferay {#ref5}

* Set Environment for `${LIFERAY_INSTALL_7_4}`
  `$ export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18`

* Start liferay

  * `$ ${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/bin/startup.sh`

* Log

  * `$ tail -f ${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/logs/*`

* Url SW360 : `https://localhost:8080`


### Re-indexing search indexes is required for major version upgrades. Here’s how to re-index:

```
1. Click on the Global Menu (Global Menu icon) and select the Control Panel tab. The Control Panel appears.

2. Click on Search in the Configuration section, select the Index Actions tab, and click Execute for Re-index all search indexes. The re-index executes and displays a success message when done.
```

{{< figure src="/sw360/img/sw360screenshots/ReIndexSearch.png" >}}


### Setup SW360 for Liferay: Import *.lar Files

- ```You need over-import *.lar files to the portet can show the sw360 icons/images```

For the setup of SW360 in Liferay, the portal description files, `*.lar` files need not be imported. There is no way except from doing this in the UI. If we are wrong with this, please let us know, because it is very annoying that these ever occurring steps cannot be automated with Liferay.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.49.41.png" >}}


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
