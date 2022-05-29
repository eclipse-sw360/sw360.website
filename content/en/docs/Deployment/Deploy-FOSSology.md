```diff
- The following part covers the old ssh-based interaction
- with FOSSology. It si not part of the recent versions of
- SW360 anymore. Whenever you can, consider the REST-based
- connection with FOSSology
```

### Configuration of sw360 and FOSSology

To enable interaction between fossology and sw360 we need to prepare both sides. Overview:

1. Create a key pair for a sw360 user to log into the fossology server in order to transfer uploads from sw360 to fossology via ssh
1. Create the user on the server that runs fossology
1. Create the user in the fossology application
1. Configure the sw360 application with the networking and login information (and the key file locations)
1. Configure and test the transfer in the sw360 application

### Create a Key Pair

We need to create a key with 

```
#!bash

ssh-keygen
```
and the public key should be put in the authorized_keys file, for simplicity we use the transparently mounted folder on the host machine of our vagrant deployment. The keys will be in the vagrant deployment ```/opt/apache-tomcat-7.0.X/webapps/fossology/WEB-INF/classes```
note that you will need usually to create them there. If you deploy from source and would like to have packaged as part of the service (for whatever reason), the keys could be placed in ```backend/backend/src/src-fossology/src/main/resources```.

### On the Server on which FOSSology runs

The following snippet creates a user sw360, and copies the prepared authorized_keys file to the right location.

```sh
#!bash
ssh vagrant@127.0.0.1 -p 2222
sudo useradd -m sw360 -g fossy
sudo -i sw360
mkdir ~/.ssh
chmod 700 ~/.ssh

cp /vagrant/sw360ssh/authorized_keys ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

Note that ```sudo -i``` may not work in your environment, try ```sudo su sw360``` instead.

### In the FOSSology Application

* Create incoming folder(s) with the same name as the clearing team name(s) configured in sw360
* Create groups with the same name as the clearing team name(s) configured in sw360

> NOTE! The default group on the SW360 for clearing team is 'Unknown'. If a user does not change this value, this will not be sent to FOSSology. Please select a valid clearing team before you proceed to upload the project to FOSSology.

* Add user sw360 (Read + Write ), passwd sw360 (or what is configured in the shell script utilsSW360)
* Add the user to the clearing team groups as advisor

### On the server on which sw360 runs

Here we need to edit the file [src]/backend/src/src-fossology/src/main/resources/fossology.properties

```
#!java

fossology.host = 127.0.0.1
fossology.port = 2222
fossology.user = sw360
fossology.key.file = /fossology.id_rsa
fossology.key.pub.file = /fossology.id_rsa.pub
```
Note the the paths are relative to the resources folder. In addition, the fossology user must be configured (note the user on the ubuntu server, but the user created in the fossology application: This setting is set in the script ```backend/src/src-fossology/src/main/resources/scripts/utilsSW360```.

### The sw360 FossologyAdmin UI

Here we can trust the finger print of the fossology server, after trusting it we copy the deployment scripts. The deployment scripts are placed in the folder 
  [src[/backend/src/src-fossology/src/main/resources/scripts
Here the password for the sw360 user is stored in the file 
  utilsSW360
We can change it here or, after copying to the server, change the password there.

### Troubleshooting

In the sw360, there is an error? first have a look in the tomcat log file. The java library for the ssh connection will provide information there what failed.

#### Error shown after transfer to FOSSology

First of all, try to establish the connection manually by using the shell command ssh, may look like the follwing:

```
ssh sw360@your.fossology.server.com -p 2222 -i fossologyprivatekey.id_rsa
```

and check the outcome. In case, adjust the ```fossology.properties``` file with the corrected data. Any other things worth to check:

* Are the access rights for the private key correct? (should be 600)
* Is the fingerprint of the server accepted? Try to load the Admin / Fossology page to see and check in case.
* Maybe the release does not have an all right attachment or there are two source files attachments? In such cases, also an "Error" will be shown, however, not revealing the entire information the user may change the attachment configuration of the release.

If you even have trouble with the ssh login, try to check what the ssh client does with using the ```-v``` option. Also, checking what happens on the server using ```tail –f –n 100 /var/log/auth.log``` can be super helpful.