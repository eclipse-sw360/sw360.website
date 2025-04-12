---
linkTitle: "Upgrade Sw360 from 15.0 to 16.0"
title: "Upgrade Sw360 from 15.0 to 16.0"
weight: 100
description:
  Upgrade Sw360 from 15.0 to 16.0
---

# Upgrade SW360 version 16.0

## 1. Upgrade sw360 from 15.0 to 16.0

```
1.1 Checkout source code SW360 to Tag Version 16
1.2 Version of libraries
1.3 Migrate database
1.4 Build and deploy Sw360 Version 16
1.5 Start and Configure Liferay 
```

### 1.1 Create Folder contains source code SW360 to Tag Version 16

Link contains source: <https://github.com/eclipse/sw360.git>

* Path `SW360_REPOSITORY` = `/home/user/work15to16/sw360`

* Source code sw360 is in main branch with commit version 14.0 . User into `${SW360_REPOSITORY}` use git checkout to tag version 16 on the main branch of SW360
* Checkout to tag  Version 16.0.0 or checkout commit "d15db4a1b07112fff126016103c1a8d8dd03c230"
  * `$ git checkout d15db4a1b07112fff126016103c1a8d8dd03c230` or  `$ git checkout sw360-16.0.0-M1`

* Upgrade Thrift from 0.14.0 to 0.16.0
  * Move to folder sw360 with path `/home/user/work15to16/sw360`

    Run command line:

    Uninstall thrift version 0.14.0

  * `./scripts/install-thrift.sh --uninstall`

    Install thrift version 0.16.0

  * `./scripts/install-thrift.sh`

    Check version thrift

  * `thrift --version`

* Update Dependency for SW360 version 16

    Download dependency:
  * `wget https://search.maven.org/remotecontent?filepath=commons-io/commons-io/2.7/commons-io-2.7.jar -O commons-io-2.7.jar`
  * `wget https://search.maven.org/remotecontent?filepath=com/google/code/gson/gson/2.8.9/gson-2.8.9.jar -O gson-2.8.9.jar`
  * `wget https://search.maven.org/remotecontent?filepath=com/google/guava/guava/31.0.1-jre/guava-31.0.1-jre.jar -O guava-31.0.1-jre.jar`
  * `wget https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-annotations/2.13.2/jackson-annotations-2.13.2.jar -O jackson-annotations-2.13.2.jar`
  * `wget https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-core/2.13.2/jackson-core-2.13.2.jar -O jackson-core-2.13.2.jar`
  * `wget https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-databind/2.13.2.2/jackson-databind-2.13.2.2.jar -O jackson-databind-2.13.2.2.jar`
  * `wget https://repo1.maven.org/maven2/org/apache/thrift/libthrift/0.16.0/libthrift-0.16.0.jar -O libthrift-0.16.0.jar`

    Move dependency to folder `/opt/liferay-ce-portal-7.3.4-ga5/deploy`

### 1.2 Version of libraries

| Package Name  | Version  |
|:--------------|:--------:|
|   Liferay     |  7.3.4   |
|   Tomcat      |  9.0.33  |
|   Couchdb     |  3.2.2   |
|   Open JDK    |  11.0.15 |
|   Thrift      |  0.16.0  |

### 1.3 Migrate database

* Check migrate scripts from 15.0 to 16.0 by <https://github.com/eclipse/sw360/tree/master/scripts/migrations>

* 3 file migration:

* `https://github.com/eclipse/sw360/blob/main/scripts/migrations/048_add_component_businessunit.py`
* `https://github.com/eclipse/sw360/blob/main/scripts/migrations/049_migrate_admin_obligation.py`
* `https://github.com/eclipse/sw360/blob/main/scripts/utilities/003_update_project_field_value_couchdb_2_x.py`

    Install enviroment for python 2.7
  * `$ sudo apt-add-repository universe`
  * `$ sudo apt update`
  * `$ sudo apt install python2-minimal`

    Check version
  * `$ python2 --version`

    Install pip for python 2.7
    -`curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.py`
    -`sudo python2 get-pip.py --proxy=http://username:password@hostname`
    -`pip --version`

    Import package couchdb
    -`pip install --proxy=http://username:password@hostname couchdb`

    How to run migration data
    1. stop SW360 (i.e. the tomcat)
        * Set Environment for `${LIFERAY_INSTALL}`
        * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

        * Stop SW360 version 15.0, ensure that couchdb is accessible (try to open `http://localhost:5984/_utils/`)
        * `$ ${LIFERAY_INSTALL}/tomcat-9.0.33/bin/shutdown.sh`

    2. ensure that couchdb is accessible (try to open <http://localhost:5984/_utils/>)

    3. run the migration scripts (i.e. for each script call python2 /PATH/TO/00?_some_migration_script.py)
        be aware that some scripts are using an internal dry-run switch which you have to change manually in the script's code.

        3.1 move to folder with path `/home/user/work15to16/sw360/scripts/migrations`

        Run command:
        * `python2 048_add_component_businessunit.py`
        * `python2 049_migrate_admin_obligation.py`

        Check data change in file log:
        * 048_add_component_businessunit.log
        * 049_migrate_admin_obligation.log

        3.2 move to folder with path `/home/user/work15to16/sw360/scripts/utilities`
        * `python2 003_update_project_field_value_couchdb_2_x.py`

        Check data change in file log:
        * 003_update_project_field_value_couchdb_2_x.log

### 1.4. Compile and deploy

* Set Environment for `${LIFERAY_INSTALL}`
  * `$ cd /home/user/work/sw360`
  * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

    To clean everything and  install without running the tests

  * `mvn clean install -DskipTests`

    For deployment run the command
  * `mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.33/webapps -Drest.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.33/webapps -DskipTests`

### 1.5 Start and Configure Liferay

* Set Environment for `${LIFERAY_INSTALL}`
  * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

* Start liferay
  * `$ ${LIFERAY_INSTALL}/tomcat-9.0.33/bin/startup.sh`
* Log
  * `$ tail -f ${LIFERAY_INSTALL}/tomcat-9.0.33/logs/*`

* Url SW360 : `https://localhost:8080`
