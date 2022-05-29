## Basis of communication between SW360 and FOSSology

Basic communication with the FOSSology server is done over an SSH connection: the fossology service of SW360 executes remote commands on the FOSSology server.

The commands that are executed are the bash scripts found inside `src-fossology/src/main/resources/scripts/`, they are copied into the home directory of the ssh user (either manually or through the admin portlet).
See [Setup of connection with Fossology](Fossology-Setup) for configuration details.

```
\- src-fossology/src/main/resources/
 \- scripts/
  |- duplicateUpload
  |- folderManager
  |- getStatusOfUpload
  |- uploadFromSW360
  \- utilsSW360
```

These scripts utilize the standard command line tools to interact natively with FOSSology (these are the tools found in the src/cli folder of FOSSology, such as `cp2foss fossjobs fossupload_status fo_usergroup fo_chmod fo_folder ...`).

* `utilsSW360` contains common functions used by the other scripts and some FOSSology configuration such as the user/password pair used to run the cli utils and the UNIX group of the FOSSology processes
* `folderManager` (uses FO:`fo_folder`): get information about the folder structure of FOSSology to allow sharing of uploads between groups
* `getStatusOfUpload` (uses FO:`fossupload_status`): to get the clearing status given an uploadId and a group
* `uploadFromSW360` (uses FO:`cp2foss fossjobs`): to create a new upload from the standard input and schedule scanners
* `duplicateUpload` (uses FO:`fo_chmod` SW:`folderManager`): to make a previously uploaded file available for another group

### Java libraries and settings

The java code utilizes the package `com.jcraft.jsch` to connect to the SSH server. It is set to strictly check the fingerprint of the remote server against the accepted which are stored in couchDB.

### Conventions

the sw360 user in FOSSology (the actual name is configured in `utilsSW360`) **must be a member of every group** to which it should be able to send Releases to be cleared.
File uploaded from SW360 are placed inside a folder with the same name as the group and permission will be set at the group level (default of cp2foss).

### Datamodel and thrift service

* each Release object in SW360 can have only one attachment of type SOURCE.
* when a Release is sent *for the first time* to FOSSology through the Thrift method `sendToFossology(1: string releaseId, 2: string clearingTeam )` its SOURCE attachement is sent as stdin to the script `uploadFromSW360`. 

    The field `map<string, FossologyStatus> clearingTeamToFossologyStatus` is then updated to contain the corresponding entry for the chosen Clearing Team (aka. the name of the FOSSology group which will receives the upload for clearing).
* when the same Release is *sent again for another team* a new *link* in the corresponding group folder is created and the old upload is made available for the new group (as in giving permission using FO:`fo_chmod`).

    At the moment this gives access only to the files, not to the relative clearing decision.
    In order to make the clearing decisions available a reuser needs to be scheduled from the Jobs menu. [ it could be possible to schedule the job from SW360: its user is member of all the groups; but it is not currently implemented since there is no cli interface for reuser yet ]
* when the current status is requested using the Thrift method `Release getStatusInFossology(1: string releaseId, 2: string clearingTeam )` the newest status is fetched from FOSSology and it is stored in the map for the relative clearingTeam

### Notes

* Releases have a ClearingState field, but this is ignored by the Thrift service and used only in the SW360 user interface. 
* Projects link to Releases and the summary of their FOSSology status can be monitored. This is also ignored by the FOSSology Thrift service and handled by the Component service: the FOSSology service just updates the status of the Release objects.