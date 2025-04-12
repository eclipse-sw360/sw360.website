---
linkTitle: "Export and Import"
title: "Export and Import"
weight: 100
description:
  SW360 Export and Import
---

```diff
- note that only export and import of users is active,
- everything else is deprecated functionality.
- The export and import functionality has not been
- updated at some point and thus will not function
- properly anymore.
```

Full Export
===========

The easiest way to fully export the data is to copy all the .couch files of Couch-DB. Where the files are can be found out from Futon.
e.g.

```
http://localhost:5984/_utils/config.html
```

under

```
view_index_dir  /var/lib/couchdb
```

This method of exporting has the advantage that all Ids remain the same.
An equally simple method it to use the Couch-DB replicator from Futon.

This method might fail when there are changes to the document structure as Ektorp might stumble over unset required or surplus fields. The method of choice here is to repair the DB (after a backup) with

```
https://github.com/couchapp/couchapp
```

and then follows the instructions from

```
http://harthur.github.io/costco/
```

and

```
couchapp push . http://localhost:5984/sw360users
```

then you go to

```
http://localhost:5984/sw360users/_design/costco/index.html
```

and you can run functions like:

```
function(doc) {
  if (doc.type == 'user') {
    if(doc.fullname == 'Homer J. Simons') {
       doc.fullname =  'Homer Jay Simons';
    }
  }
  return doc;
}
```

You can also change the names of properties, e.g.

```
function(doc) {
  if (doc.type == 'user') {
    if(doc.fullname ) {
       doc.fullname2 = doc.fullname;
       delete doc.fullname;
      }
  }
  return doc;
}
```

CSV Export
==========

## Users
The export of users was already described, this is very important as this also creates the users in the liferay database. The mere export of the users.couch is not enough.

## Projects

There is no CSV export or import for projects currently.

## Components and Releases

To Export the components and releases you need to do the following:
As Components and Releases are identified by their identifier ([name] or [name(version)]), these identifiers need to be unique. When importing duplicates in the identifiers are ignored and they are also not exported.
Therefore in the admin page you can check the database for such duplicates.

After that "Download Component CSV" creates a CSV with components, releases and their source attachments.
The source attachments are created if the "DownloadURL" is a valid url.
These remote-only attachments will be download once the first download request occurs.
If the URL does not exist you get an error.

Alternatively you can use

```
sw360/src/backend/utils/src/main/java/com/siemens/sw360/attachments/db/RemoteAttachmentDownloader.java
```

to bulk download the source only attachments.
The command line call to use it from the Siemens network looks like this:

```
 java -jar -Dhttp.proxyHost=proxyfarm.3dns.netz.sbs.de -Dhttps.proxyHost=proxyfarm.3dns.netz.sbs.de -Dhttp.proxyPort=84 -Dhttps.proxyPort=84 /home/siemagrant/.m2/repository/com/siemens/sw360/backend-utils/0.1.1-SNAPSHOT/backend-utils-0.1.1-SNAPSHOT-jar-with-dependencies.jar -d
```

## Attachments

Here we have a mixed strategy, as there is a CSV export for the attachments, which only stores the meta information about the files. The files themselves need to be brought into a new instance via the sw360attachments.couch database.

The ids of the attachments are also in the CSV, so they are not portable without the sw360attachments.couch. This is meant as a form of recovery, but it should not be used on an instance that has been worked on, so only a fresh set up.

This will overwrite the auto generated attachments from the component CSV if the have the same URL as one of the imported attachments. This feature is needed to render the procedure idempotent.

The admin interface provides the possibility to delete attachment contents that do not have a project, component or release with an attachment that references it.

If you copy the sw360attachments.couch to your instance and then click this before you import than the db should be empty afterwards.

If there was no error after importing the csv, running this job should yield no deletions if there was no error and the exported attachments where complete.

In general this should only be necessary if errors have occurred.
It is a good idea to run this before you export the attachments.

## Release links

Links between releases can be exported or imported.
Because release links are stored in maps, the procedure is idempotent by construction.
The old links are overwritten with the imported data.

## Suggested Order for Exports

1. Freeze the application, so that others can not change the data at the moment (By external means, like closing a port forwarding)
2. Clean up the attachments
3. Look for duplicate identifiers and resolve conflicts (Important as duplicates do not get exported or imported)
4. Export the Users, Components, Attachment Infos and release links
5. copy the sw360attachments.couch, this might be a huge files

## Suggested Order for Imports
### On a fresh installation

1. Copy the sw360attachments.couch in its place
2. Start the licenses importer
3. restart the backend to make the design documents available and boot the frontend
4. Import the users
5. Import the component CSV
6. Import the Attachment Infos
7. Import the Release Link Infos.

### Regular Maintenance Operations

1. Run the attachments clean up
2. Resolve name crashes with the search for duplicate Identifiers

### Imports on a running instance

1. New components can be imported via the CSV at any time. Duplicates to existing components will be ignored, but there is a log message.
2. Users can be added via CSV.
3. Release links can be added via CSV, duplicates overwrite existing links

Attachments should not be imported on a running instance!
This should not break much, as without the entries in the couchDB there will be no import.
But potentially remote-only Attachments get deleted.
Nevertheless this scenario is not intended and maybe there are unforeseen side effects.

## Troubleshooting

#### Import failing in the Backend: No Department

The import fails with some error message that a user does not have a department?

1. First of all, the importing admin requires a group assignment. Otherwise the adding component action will fail.
2. If a group is added to the admin, not that in addition to the Liferay group setting, this information must be also placed into the "sw360users" database in couchdb.
3. Note that changes to groups and similar things will require a restart of the Liferay server (=tomcat). Otherwise the user caching kicks in and might not reflect all updates.
