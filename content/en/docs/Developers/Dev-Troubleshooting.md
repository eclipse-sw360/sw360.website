This page shall list small issues / tips when developing for sw360.

### Development: problems building sw360portal with maven?

Before building the sw360portal with maven, ensure that the following components are installed in the development environment:
* A git client
* Apache Maven 3.0.X
* Apache Thrift 0.9.3
* Java 1.8.X
* CouchDB, at least 1.5 (only if the tests will be executed locally)

### Development: problems using Eclipse?

Please do not use Eclipse, because the integration of Apache Thrift is an open issue and we found no plugin for Eclipse to solve the shown compiler errors.
Recommended is IntelliJ IDEA or NetBeans.

### Liferay: problems with displaying changes to page?

When developing changes to a page and these changes do not show in browser - even after redeployment, then the internal liferay optimisation mechanisms may kick in. Try to add to the URL string the following key value parameters:

```
js_fast_load=0&css_fast_load=0&strip=0
```

### Liferay: where are the initial admin user settings?

It is the file ```portal-ext.properties``` in sw360/opt.

### Maven: build generally fails

You just try to compile parts or all of it and it fails? Most of the stuff depends on the module /build-configuration. Execute either "mvn install" on top level or inside build configuration.

#### Backend: problems with company proxy?

maybe try instead:

```
/opt/apache-tomcat-/bin/startup.sh
```
just this: 
```
CATALINA_OPTS="-Dhttps.proxy..." /opt/apache-tomcat-/bin/startup.sh
```
for lucene it might be necessary to add:
```
[httpd_global_handlers]
_fti = {couch_httpd_proxy, handle_proxy_req, <<"http://127.0.0.1:8085/couchdblucene">>}
```
in lucene.ini of local.d of your CouchDB installation

#### Backend: are thrift services up?

1. Check tomcat manager (if the services are there)
2. Check if the service is accessible:
   ```
   http://your.url.to.server.com:8085/components  
   ```
   Should return "Welcome to ...".
3. Check if the service thrift page is there:
   ```
   http://your.url.to.server.com:8085/components/thrift
   ```
   Should return HTTP status code 500, because in the browser, no valid thrift message was formed.

#### Backend: org.ektorp.DbAccessException

What do I do if I get: org.ektorp.DbAccessException: com.fasterxml.jackson.databind.exc.UnrecognizedPropertyException: Unrecognized field "_id" 

You add the class you have been trying to serialize to 
THRIFT_CLASSES in
sw360/src/libraries/lib-datahandler/src/main/java/com/siemens/sw360/datahandler/thrift/ThriftUtils.java

#### Backend: maven failed tomcat7 deploy

If the deployment via maven of the backend does fail with an error like this 

```
Uploading: http://localhost:8085/manager/text/deploy?path=%2Flicenses
2302/17930 KB   
Uploading: http://localhost:8085/manager/text/deploy?path=%2Flicenses
2102/17930 KB   
Uploading: http://localhost:8085/manager/text/deploy?path=%2Flicenses
2064/17930 KB   
Uploading: http://localhost:8085/manager/text/deploy?path=%2Flicenses
2064/17930 KB   
[INFO] ------------------------------------------------------------------------
[INFO] Reactor Summary:
[INFO] 
[INFO] backend ........................................... SUCCESS [2.579s]
[INFO] backend-src ....................................... SUCCESS [0.058s]
[INFO] src-licenses ...................................... SUCCESS [10.544s]
[INFO] src-users ......................................... SUCCESS [1.485s]
[INFO] src-vendors ....................................... SUCCESS [6.929s]
[INFO] src-search ........................................ SUCCESS [5.837s]
[INFO] src-components .................................... SUCCESS [19.439s]
[INFO] src-projects ...................................... SUCCESS [14.280s]
[INFO] src-attachments ................................... SUCCESS [6.188s]
[INFO] src-moderation .................................... SUCCESS [1.169s]
[INFO] src-fossology ..................................... SUCCESS [6.259s]
[INFO] backend-svc ....................................... SUCCESS [0.038s]
[INFO] svc-licenses ...................................... FAILURE [3.630s]
[INFO] svc-users ......................................... SKIPPED
[INFO] svc-vendors ....................................... SKIPPED
[INFO] svc-search ........................................ SKIPPED
[INFO] svc-components .................................... SKIPPED
[INFO] svc-projects ...................................... SKIPPED
[INFO] svc-attachments ................................... SKIPPED
[INFO] svc-moderation .................................... SKIPPED
[INFO] svc-fossology ..................................... SKIPPED
[INFO] backend-utils ..................................... SKIPPED
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time: 1:19.836s
[INFO] Finished at: Mon May 04 15:57:46 CEST 2015
[INFO] Final Memory: 24M/311M
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.tomcat.maven:tomcat7-maven-plugin:2.2:deploy (default-cli) on project svc-licenses: Cannot invoke Tomcat manager: Broken pipe -> [Help 1]
[ERROR] 
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR] 
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
[ERROR] 
[ERROR] After correcting the problems, you can resume the build with the command
[ERROR]   mvn <goals> -rf :svc-licenses
voyager:backend sam$
```

One solution is that you deployed already and the tomcat7 plugin does not like to have multiple deploy commands. Instead you will need to issue a ```mvn tomcat7:redeploy``` command.

#### Deployment: liferay not accessible

If the virtual machine was shut down and started up again, the backend services and frontend liferay require manual restart. Please contribute a change in the vagrant deployment if you feel that this could be changed. The actual places to call are:

```
/opt/apache-tomcat-.../bin/.startup.sh
/opt/liferay-.../tomcat-.../bin/.startup.sh
``` 