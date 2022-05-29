*** 
**NOTE**: In order to follow this guide, you have to work on sw360 version 5.0 or later which uses the Liferay 7.2 Community Edition GA1 version (as of Sept 2019).
***

| [[images/liferay_7_welcome_page.png]] | [[images/liferay_7_home_page.png]] |
|------|------|

# 	Quick overview:

1. [Install CouchDB](#deploy-couchdb)
1. [Install CouchDB Lucene](#deploy-couchdb-lucene)
1. [Deploy Liferay 7.2 to your instance](#deploy-liferay-7.2-to-your-instance)
1. [Start Liferay](#start-liferay)
1. 	[Deploy needed dependencies as OSGi modules](#deploy-needed-dependencies-as-OSGi-modules)
1. 	[Deploy SW360](#deploy-sw360)
1. 	[Configure Liferay Portal](#configure-liferay-portal)
1. 	[Import SW360 site](#import-sw360-site)
1. 	[Import users](#re-import-users)
1. 	[Finish upgrade](#finish-upgrade)

If you are familiar with Vagrant and Puppet, you can also follow the scripted deployment instructions in the [sw360/sw360vagrant](https://github.com/sw360/sw360vagrant) project.

# Prerequisites

You need a clone or download of the SW360 repository to follow this guide. The location of the clone will be referred as `SW360_REPOSITORY` in the following.

# Deploy CouchDB

CouchDB is available on a number of platforms. Please note that the currently used search framework based on Lucene will not work with CouchDB versions or later. As such, please use the versions before 2. One case is to install couchdb as a package from your Linux distro. For example with Ubuntu 16.04, couchdb 1.7.1 is available.

# Deploy CouchDB Lucene

CouchDB Lucene can be downloaded and installed into the same Tomcat container, which is also used by the Liferay installation: 

1. Download [CouchDB Lucene](https://github.com/rnewson/couchdb-lucene/archive/v1.0.2.tar.gz).
2. Replace the original `couchdb-lucene-1.0.2/src/main/resources/couchdb-lucene.ini` with this file [couchdb-lucene.ini](https://github.com/sw360/sw360vagrant/blob/master/shared/couchdb-lucene.ini) file.
3. Apply the [patch](https://github.com/sw360/sw360vagrant/blob/master/shared/couchdb-lucene.patch) on `couchdb-lucene-1.0.2/`
4. Build the `couchdb-lucene-1.0.2/` again with `mvn clean install war:war`
2. Once available, copy the resultign war file (in the target folder) to the deployment folder of the Tomcat (usually something like `${CATALINA_HOME}/webapps`)

# Deploy Liferay 7.2

1. 	Download Liferay with Tomcat from
    https://sourceforge.net/projects/lportal/files/Liferay%20Portal/7.2.0%20GA1/liferay-ce-portal-tomcat-7.2.0-ga1-20190531153709761.tar.gz/download. Its SHA256 checksum is `0d7dc6bab406e910048bbf4de41189495691625dc43acb65eab5400ec826d124`.
1. 	Extract it to the folder you wish Liferay to start from. This folder will 
	be called `LIFERAY_INSTALL` during the rest of the guide.
1.	Copy the file `${SW360_REPOSITORY}/frontend/configuration/setenv.sh` to `${LIFERAY_INSTALL}/tomcat-9.0.17/bin` by overwriting the
	existing file. Check the content and adapt it to your needs, at least the Java memory settings.
1.	Copy the file `${SW360_REPOSITORY}/frontend/configuration/portal-ext.properties` to `${LIFERAY_INSTALL}`.
	This file includes needed, useful and some optional settings to optimize running SW360 in Liferay.
1.	Open the file `${LIFERAY_INSTALL}/portal-ext.properties` and uncomment all properties starting with
	`default.admin.`. This will define a default administrator used to do the setup in the following 
	steps. You will be rememembered to change or deactivate this user at the end of the upgrade.

**Note** In case the `sw360.properties` do not kick in and you need to login to a "factory-new" liferay instance, the initial user credentials to login are (usually):

```
test@liferay.com
test
```

## 	Adapt and cleanup properties

From the sw360 repository you should have (at least) the following files in `/etc/sw360`:

*	`couchdb.properties`: Database connection for SW360.
*	`sw360.properties`: Custom properties for SW360 application.

In additon, copy the following property file form the Liferay installation:

*	`portal-ext.properties`: Custom properties for Liferay Portal.

Please check if your `/etc/sw360/portal-ext.properties` now overrides some of the properties in `${LIFERAY_INSTALL}/portal-ext.properties` and comment or remove them if necessary.

1. 	Adjust `sw360.properties`

	You may skip this step if you did not customize one of the following 
	options from the previous step:

	* `auto.login.hooks`
	* `login.events.post`
	* `servlet.service.events.pre`
    
	Otherwise copy the following block into your `/etc/sw360/sw360.properties` 
	and adapt it to your needs. Activate the necessary components depending on 
	the settings of the old three properties. You should be
	able to easily match the old options with new component names. Do no remove
	any componentes if you do not know what they are doing!
	```
	# Activation of Dynamic Components
	# Possible components to be enabled:
	#	- org.eclipse.sw360.portal.users.TestAutoLogin		(A stub for testing single sign on. Everyone will be logged in as user@sw360.org)
	#	- org.eclipse.sw360.portal.users.SSOAutoLogin		(A single sign on class relaying on headers in the request)
	#	- org.eclipse.sw360.portal.users.LoginAction		(Default login action. Do not disable unless you know what you are doing)
	#	- org.eclipse.sw360.portal.users.LandingPageAction 	(Liferay does not redirect to landing page when the login is taken over by SSOAutoLogin. Activate this one if using SSOAutoLogin component)
	#	- org.eclipse.sw360.portal.components.BuildInfoTemplateContextContributor	(Provide build information of SW360 for templates)
	#	- org.eclipse.sw360.portal.components.FossologyCheckConnectionOnStartupHook (Checks at startup if fossology is reachable)
	components.activate= \
	org.eclipse.sw360.portal.users.LoginAction, \
	org.eclipse.sw360.portal.components.BuildInfoTemplateContextContributor, \
	org.eclipse.sw360.portal.components.FossologyCheckConnectionOnStartupHook
	```
	No other options have to be touched for this upgrade.


##	Create Liferay Database in Case

Liferay comes with a Hypersonic database. This can be absolutely fine. In case you would like to change it. Please refer to the Liferay documentation how to install Liferay with another database.

##	Deploy needed dependencies as OSGi modules

The following dependencies are needed to run SW360 and therefore must be 
downloaded and copied to `${LIFERAY_INSTALL}/deploy`:

*	[Apache Commons Codec 1.12](https://search.maven.org/remotecontent?filepath=commons-codec/commons-codec/1.12/commons-codec-1.12.jar)
* 	[Apache Commons Collections4 4.1](https://search.maven.org/remotecontent?filepath=org/apache/commons/commons-collections4/4.1/commons-collections4-4.1.jar)
* 	[Apache Commons CSV 1.4](https://search.maven.org/remotecontent?filepath=org/apache/commons/commons-csv/1.4/commons-csv-1.4.jar)
*	[Apache Commons IO 2.6](https://search.maven.org/remotecontent?filepath=commons-io/commons-io/2.6/commons-io-2.6.jar)
*	[Apache Commons Lang 2.4](https://search.maven.org/remotecontent?filepath=commons-lang/commons-lang/2.4/commons-lang-2.4.jar)
*	[Apache Commons Logging](https://search.maven.org/remotecontent?filepath=commons-logging/commons-logging/1.2/commons-logging-1.2.jar)
*	[Google Gson 2.8.5](https://search.maven.org/remotecontent?filepath=com/google/code/gson/gson/2.8.5/gson-2.8.5.jar)
*	[Google Guava 21.0](https://search.maven.org/remotecontent?filepath=com/google/guava/guava/21.0/guava-21.0.jar)
*	[Jackson Annotations 2.9.8](https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-annotations/2.9.8/jackson-annotations-2.9.8.jar)
*	[Jackson Core 2.9.8](https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-core/2.9.8/jackson-core-2.9.8.jar)
*	[Jackson Databind 2.9.8](https://search.maven.org/remotecontent?filepath=com/fasterxml/jackson/core/jackson-databind/2.9.8/jackson-databind-2.9.8.jar)
    
 
#	Deploy SW360

With the dependencies in place you may deploy SW360 modules now. The following 
describes a setup where the Apache Tomcat bundled with Liferay will also 
host the backend and REST services.

You may run the following command inside `${SW360_REPOSITORY}` to automatically deploy SW360 modules to the 
correct locations:

```
mvn package -P deploy -Dbase.deploy.dir=. -Dliferay.deploy.dir=${LIFERAY_INSTALL}/deploy -Dbackend.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.17/webapps -Drest.deploy.dir=${LIFERAY_INSTALL}/tomcat-9.0.17/webapps
```

If you want to copy the artifacts manually, please use the following destinations depending on the module:

* backend/* goes to `${LIFERAY_INSTALL}/tomcat-9.0.17/webapps`
* frontend/* goes to `${LIFERAY_INSTALL}/deploy`
* libraries/* goes to `${LIFERAY_INSTALL}/deploy`
* rest/* goes to `${LIFERAY_INSTALL}/tomcat-9.0.17/webapps`

# Start and Configure Liferay

Starting the new Liferay should be pretty much the same as starting the
old Liferay version. So calling the following command should be sufficient:
```
${LIFERAY_INSTALL}/tomcat-9.0.17/bin/startup.sh
```
**Note**: If you had some start services in place to start your Liferay instancen
you might have to change them since the bundled version of Apache Tomcat has been
upgrade and thus the folder is now named `tomcat-9.0.17`.

## Configure Liferay Portal

To apply the following steps, login as default administrator as configured above. If you
have copied all properties from this guide, the login is `setup@sw360.org` with password 
`sw360fossy`.

You'll get a `Not Found` message after login. Do not worry that is alright for the moment.

You should change the password for that user in order to prevent any one else to login 
with the login data from the property file:
1.	Click on the user icon on the top right and select `Account Settings`.
1.	Click on `Password` on the left side of the tab `General`.
1.	Change your password using the displayed form.

The following sections will now describe the single steps to configure Liferay.

## User Association

1. 	Open the panel on the left side by clicking the button on the top left.
1.	Go to `Control Panel` -> `Configuration` -> `Instance settings`.
1.	Click on `Users` (inside section `Platform`).
1.	Click on `Default User Associations` on the left side.
1.	Fill the field `Sites` on the top with `SW360` and click on `Save`.

**Note**: This way newly created users are automatically assigned to the site `SW360` and can
access the content on it. This is important for the import of the users later on. Normally you
would keep this settings afterwards as well. Otherwise you would have to assign all new users
manually.

## Import SW360 site

1. 	Open the panel on the left side by clicking the button on the top left.
1. 	Go to `SW360` -> `Publishing` -> `Import`.
1.	Import the following page archives (in that order) from
	`${SW360_REPOSITORY}/frontend/configuration`...
	1. 	`Public_Pages.lar`
	1. 	`Private_Pages.lar`
	1. 	`Private_Pages_BDP_Import.lar` (optional; only if you need BDP Import)
	1.	`Private_Pages_WS_Import.lar` (optional; only if you need WS Import)
1.	...by following theses steps:
	1.	Click on `+` on the top right.
	1. 	Select the appropiate file and click `Continue`.
	1.	Select `Public Pages` or `Private Pages` depending on the prefix of the filename.
	1.	Change the following options according to the selected file:
		* *Theme Settings*
		* *Logo*
		* *Site Page Settings*
		* *Site Template Settings*
		* *Delete Missing Pages*
		
		They sould be enabled or disabled dependening on the select file:
		* `Public_Pages.lar`, `Private_Pages.lar`: **Enable** all options.
		* All other files: **Disable** all options.

	1.	No options need to be checked inside section `DELETIONS`.
	1. 	Be sure to check `Import Permissions` inside section `PERMISSIONS`.
	1. 	Expand section `Update Data` and select `Mirror with overwriting`.
	1. 	Expand section `Authorship of the Content` and select `Use the Current User as 
		Author`.
	1.	Click `Import`.

## Check Theme

For unknown reason Liferay does not always seem to set the theme correctly. Follow these steps to
check if the correct theme has been configured:

1. 	Open the panel on the left side by clicking the button on the top left.
1. 	Go to `SW360` -> `Site Builder` -> `Pages`.
1.	Select `Public Pages` in the left column.
1.  Click on the `cog`-icon to configure the pages.
1. 	Inside the `LOOK AND FEEL` section check if the current theme is named `SW360`.
1.  Otherwise click on `Change Curren Theme` and select theme `SW360`.
1.	Repeat step 3.-6. with `Private Pages`.

**Note**: In general SW360 should also work with the `Classic Theme` provided by liferay since the 
theme is mainly to adjust colors. However we do not test the `Classic Theme` extensivly. If you want
to change the colors of SW360 consider forking the project `liferay-theme` inside the SW360
repository.

## Hide portlet decorators

**OPTIONAL**: This is only needed if you do your daily work as an Liferay administrator (not 
recommended). In all other cases you may skip this step.

This will hide the portlet decorators for Liferay administrators. These decorators are very 
irritating when doing normal SW360 work. Normal Liferay user will not see the decorators anyway.

1. 	Open the panel on the left side by clicking the button on the top left.
1. 	Go to `SW360` -> `Site Builder` -> `Pages`.
1.	Select `Public Pages` in the left column.
1.  Click on the `cog`-icon to configure the pages.
1.  Switch on the option `Hide Portlet Decorators for Edit` under `Settings`.
1.	Do step 3.-5. for `Private Pages` as well.

## Import users

**Note**: You will not see some content like projects or components as the default Liferay 
administrator which is most likely `setup@sw360.org`. Please do no worry, if you see emtpy tables on these pages before completing the installation with users.

1. 	Open the panel on the left side by clicking the button on the top left.
1. 	Click on `SW360` on the top right to go to the homepage.
1.	Click on `Start` inside the "Welcome" section.
1.	Go to `Admin` -> `User` (URL: `/group/guest/users`).
1.	Scroll down to section `UPLOAD USERS`, select a user file from the very
	beginning and click `Upload Users` on the right side. [A user file can be found here in the sw360vagrant project](https://github.com/sw360/sw360vagrant/blob/master/shared/test_users_with_passwords_12345.csv)

## Finish upgrade

1.	Please log out as setup administrator.
1.	Please log in as one of the other SW360 users now and check the content, especially the 		projects and components.
