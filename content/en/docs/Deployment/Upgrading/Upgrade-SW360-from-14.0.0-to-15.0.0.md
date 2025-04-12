---
linkTitle: "Upgrade Sw360 from 14.0 to 15.0"
title: "Upgrade Sw360 from 14.0 to 15.0"
weight: 100
description:
  Upgrade Sw360 from 14.0 to 15.0
---

# Upgrade SW360 version 15.0

## 1. Upgrade sw360 from 14.0 to 15.0

```
1.1 Checkout source code SW360 to Tag Version 15
1.2 Version of libraries
1.3 Migrate database
1.4 Build and deploy Sw360 Version 15.0
```

### 1.1 Checkout source code SW360 to Tag Version 15

Link contains source: <https://github.com/eclipse/sw360.git>

* Path `SW360_REPOSITORY` = `/home/user/work/sw360`

* Source code sw360 is in master branch with commit version 14.0 . User into `${SW360_REPOSITORY}` use git checkout to tag version 15 on the master branch of SW360
* Checkout to tag  Version 15.0.0
  * `$ git checkout .`
  * `$ git checkout sw360-15.0.0-M1`

### 1.2 Version of libraries

| Package Name  | Version  |
|:--------------|:--------:|
|   Liferay     |  7.3.4   |
|   Tomcat      |  9.0.33  |
|   Couchdb     |  3.2.2   |
|   Open JDK    |  11.0.15 |
|   Thrift      |  0.14.0  |
|   SW360       |  14.0.0  |

### 1.3 Migrate database

* Check migrate scripts from 14.0 to 15.0 by <https://github.com/eclipse/sw360/tree/master/scripts/migrations>

* There is no migrate script, skip this step.

### 1.4 Build and deploy SW360 Version 15.0

* Set Environment for `${LIFERAY_INSTALL}`
  * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

* Stop SW360 version 14.0, ensure that couchdb is accessible (try to open `http://localhost:5984/_utils/`)
  * `$ ${LIFERAY_INSTALL}/tomcat-9.0.33/bin/shutdown.sh`

## 2. Compile and deploy

* Start couchdb
  * `$ sudo service couchdb start`

* Set Environment for `${LIFERAY_INSTALL}`
  * `$ cd /home/user/work/sw360`
  * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

1. To clean everything and  install without running the tests
    * `$ mvn clean install -DskipTests`

2. For deployment run the command
    * `mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.33/webapps -Drest.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.33/webapps -DskipTests`

### 2.1 Start and Configure Liferay

* Set Environment for `${LIFERAY_INSTALL}`
  * `$ export LIFERAY_INSTALL=/opt/liferay-ce-portal-7.3.4-ga5`

* Start liferay
  * `$ ${LIFERAY_INSTALL}/tomcat-9.0.33/bin/startup.sh`
* Log
  * `$ tail -f ${LIFERAY_INSTALL}/tomcat-9.0.33/logs/*`

* Url SW360 : `https://localhost:8080`

### 2.2 Configure Liferay Portal

* Can follow the steps in the following link <https://www.eclipse.org/sw360/docs/deployment/legacy/deploy-liferay7.3> or follow these steps:

* Import users
    1. Open the panel on the left side by clicking the button on the top left.
    2. Click on `SW360` on the top right to go to the homepage.
    3. Click on `Start` inside the "Welcome" section.
    4. Go to `Admin` -> `User` (URL: `/group/guest/users`).
    5. Scroll down to section `UPLOAD USERS`, select a user file from the very
        beginning and click `Upload Users` on the right side. [A user file can be found here in the sw360vagrant project](https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv)
        * Download: `$ wget https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv`
