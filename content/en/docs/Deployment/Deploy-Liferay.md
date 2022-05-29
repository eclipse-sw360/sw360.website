### Important Notice

We are in the process of updating documentation. The documentation below is outdated. For the time being refer to the part `Running SW360 for the First Time` at:

https://github.com/sw360/sw360vagrant/wiki

### Liferay administrator steps

This part describes how to setup a new liferay instance after you went through the initial Liferay setup: create an admin account, confirm the license and terms and fill out your personal details. Alternatively in the [sw360vagrant](https://github.com/sw360/sw360vagrant) or the [sw360chores](https://github.com/sw360/sw360chores) deployment, the default setup user credentials are `setup@sw360.org` with the unsafe password `sw360fossy`.

1. Login as setup administrator (if you are using the default unsafe password, you should replace it on productive instances)

2. Go to
     
     Menu Admin -> Item Control Panel -> Section Users, Password Policies -> Default Password Policy -> Actions -> Edit
 
3. Then 

     uncheck ```Change Required``` and then 
     save

4. Then we need to grant new users the right to see SW360

     Control Panel -> Configuration -> Users(on the right) ->  Default User Associations

     check ```Apply to Existing Users``` 
     write in Sites: ```SW360 ```
     save (on the right)

4. Do not allow stranger to create accounts ...

     Control Panel -> Configuration -> Users(on the right) ->  Authentication

     uncheck ```Allow strangers to create ...``` 
     uncheck ```Allow strangers to verify ...```
     save (on the right)


5. Then, to deactivate self registration

   Control Panel -> Authentication -> remove checkmarks for creating accounts by strangers
   save (on the right)

   Note, disabling self registration is required because the current Liferay self registration does not create accounts in the backend service. (hence using the importer is required)

6. Then we go to 

    Admin -> Pages

7. and import the lar files from

   ```
   frontend/configuration/public_pages.lar
   frontend/configuration/private_pages.lar
   ```
   for the respective pages, using the tabs ```Public Pages``` and ```Private Pages```. Please note that the provided *.lar files are for Liferay 6.2 GA5 only (fun!). If you run a different liferay version, you will need to add the portlets manually until the *.lar files are updated manually.

8. ( DO NOT CHECK Pages -> Change -> Delete Missing Pages)
    
    We check on first page
    
    Application Configuration -> Choose Applications (leave all checked)

    Permissions -> Permissions

    Permissions -> Permissions Assigned to Roles

    => Click Continue

9. We check on second page of the import agent:

     Update Data -> Mirror with overwriting

     Authorship of the Content -> Use the Current User as Author

10. If this was successful we can go to 
    
    Private Pages -> users
    
11. We can then import a csv file that looks like that
     
    ```
     GivenName,Lastname,Email,Department,UserGroup,GID,isMale,PasswdHash
     user last name, user first name, first.last@sw360.org,TOP ORG CODE TEAM,USER,SW360_0004,true,AAAAoAAB9ACem9mZj9zptlEjFSMEF5MdOSUzgyxFDmKDGQDK
    ```

   Note that

    1. The GID must be unique
    1. The hash here means "t"
    1. The GID is called external Id in the thrift-based datamodel

### Some notes and troubleshooting

#### Check Liferay Configuration Options

There are plenty of useful settings to setup for your instance - you should check them depending on your desired use. Just a few examples, you could disable or enable:

* Auto login or self registration functionality
* Site statistics
* Password policies
* Configurability options
* many more, it makes sense to browse the Liferay Admin area (in the optimal case, using the setup-admin login) and check all the options.

#### Liferay crashes at startup with exception: Dockbar

If the dockbar error occurs, the file named in the error log must be replaced with an original one, because it is corrupted. Note that this represents a bug of the Liferay 6.2 (search in your favorite search engine for dockbar liferay problem ...).

#### Strange behavior

If the server has problems in terms of long running requests, maybe the memory setting is not allright, consider:

```
CATALINA_OPTS="$CATALINA_OPTS -Xms2048m -Xmx2048m
- -XX:NewSize=512m -XX:MaxNewSize=512m -XX:PermSize=512m
- -XX:MaxPermSize=512m"
```

if you run Java prior to 8.

#### Surfing to the main page shows blank page with exception message

If the "null pointer page" shows up (just a simple white page saying a null pointer exception occurred), remove the hsql folder inside the data folder from the liferay distro (shutdown before and restart after).