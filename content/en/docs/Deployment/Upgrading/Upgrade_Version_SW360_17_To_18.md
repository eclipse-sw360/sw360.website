---
linkTitle: "Upgrade SW360 from 17.0 to 18.1.0"
title: "Upgrade SW360 from 17.00 to 18.1.0"
weight: 100
---

[Version of libraries](#ref1)

[Checkout source code SW360 to Tag Version 18.1.0](#ref2)

[Config Couchdb Lucene](#ref3)

[Build and deploy](#ref4)

[Start and Configure Liferay](#ref5)

[Setup SW360 for Liferay: Import *.lar Files](#ref6)

## Version of libraries {#ref1}

| Package Name | Version |
| :----------- | :-----: |
| Liferay      |  7.4.3  |
| Tomcat       | 9.0.56  |
| Couchdb      |  3.2.2  |
| Open JDK     | 11.0.15 |
| Thrift       | 0.16.0  |

To check couchdb version: run `curl http://localhost_or_yourcouchdbserver:5984 | json_pp`

## Prepare source code to use release 18.1.0 {#ref2}

Link contains source: <https://github.com/eclipse/sw360.git>

Create folder to store new source code of version 18.1.0:

```sh
mkdir /home/user/work17to18
```

Clone source code from github:

```sh
git clone https://github.com/eclipse/sw360.git
```

Checkout to tag Version 18.1.0

```sh
git checkout sw360-18.1.0-M1
```

Set Environment for `${LIFERAY_INSTALL_7_4}`

```sh
export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18
```

Move folder `/home/user/work17to18/sw360` run command

```sh
mvn clean install -DskipTests
```

Copy dependencies from folder **/home/user/work17to18/sw360/deploy/jars** to **${LIFERAY_INSTALL_7_4}/osgi/modules**

```sh
cd /home/user/work17to18/sw360/utils/jars
sudo cp *.jar /opt/liferay-ce-portal-7.4.3.18-ga18/osgi/modules/
```

## Config Couchdb Lucene {#ref3}

Run following commands to config Couchdb Lucene (remember to replace **COUCHDB_USER** and **COUCHDB_PASSWORD** by username and password of couchdb):

```sh
cd /home/user/work17to18/sw360/third-party/couchdb-lucene/
sed -i "s/allowLeadingWildcard=false/allowLeadingWildcard=true/" ./src/main/resources/couchdb-lucene.ini
sed -i "s/localhost:5984/COUCHDB_USER:COUCHDB_USER@localhost:5984/" ./src/main/resources/couchdb-lucene.ini
mvn clean install war:war
cp target/couchdb-lucene-*.war /opt/liferay-ce-portal-7.4.3.18-ga18/tomcat-9.0.56/webapps/couchdb-lucene.war
```

## Build and deploy {#ref4}

Set Environment for `${LIFERAY_INSTALL_7_4}`

```sh
cd /home/user/work17to18/sw360
export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18
```

To clean everything and install without running the tests

```sh
mvn clean install -DskipTests
```

For deployment run the command

```sh
mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL_7_4}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/webapps -Drest.deploy.dir=${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/webapps -Dtest=org/eclipse/sw360/rest/resourceserver/restdocs/* -Dsurefire.failIfNoSpecifiedTests=false -DRunRestIntegrationTest=true
```

## Start and Configure Liferay {#ref5}

Set Environment for `${LIFERAY_INSTALL_7_4}`

```sh
export LIFERAY_INSTALL_7_4=/opt/liferay-ce-portal-7.4.3.18-ga18`
```

Start liferay

```sh
${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/bin/startup.sh
```

Log

```sh
tail -f ${LIFERAY_INSTALL_7_4}/tomcat-9.0.56/logs/catalina.out
```

SW360 url : [https://localhost:8080](https://localhost:8080)

## Setup SW360 for Liferay: Import \*.lar Files {#ref6}

**You need over-import lar files to the portet can show the sw360 icons/images**

For the setup of SW360 in Liferay, the portal description files, `*.lar` files need not be imported. There is no way except from doing this in the UI. If we are wrong with this, please let us know, because it is very annoying that these ever occurring steps cannot be automated with Liferay.

{{< figure src="/sw360/img/sw360screenshots/deploy73/2020-01-24_14.49.41.png" >}}

The go into > `Publishing` > `Import` which shows like this:

{{< figure src="/sw360/img/sw360screenshots/deploy74/13.png" >}}

Then, click on the plus sign in order to import the \*.lar file for public pages. You will find the lar files in the [frontend/configuration](https://github.com/eclipse/sw360/tree/master/frontend/configuration) folder of the sw360 repository.

{{< figure src="/sw360/img/sw360screenshots/deploy74/14.png" >}}

As for import settings, follow the selection as shown on the screenshot. It is very important that for the `Public_Pages_7_4_3_18_GA18.lar` file the selection `Public_Pages_7_4_3_18_GA18.lar` is made.

{{< figure src="/sw360/img/sw360screenshots/deploy74/15.png" >}}

Importing permission makes sure that pages are visible according to users rights. For public pages, it is irrelevant_the moment. Overwriting and the write as current user needs to be selected.

After successful importing, the same steps shall be repeated for the `Private_Pages_7_4_3_18_GA18.lar` file.

{{< figure src="/sw360/img/sw360screenshots/deploy74/16.png" >}}

Make sure that `Private_Pages_7_4_3_18_GA18.lar` is selected. Follow the other selections made as shown on the screenshot ... importing permissions ... mirror with overwriting, use the current author ...

{{< figure src="/sw360/img/sw360screenshots/deploy74/17.png" >}}
