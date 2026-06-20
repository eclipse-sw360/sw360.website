---
title: "Database migration using Costco"
linkTitle: "Database Migration"
weight: 10
---

### Preamble

Please note that database migrations are done now in python scripts at

> https://github.com/eclipse/sw360/tree/master/scripts/migrations

This page is retained because Costco might be useful for development, testing, and quick adaptations

### Problem

The main problem with changing field names in thrift is that existing documents in the couchdb need adjustments. Unfortunately, the futon interface of the couchdb does not offer bulk edits. As a consequence, looking into every document is tedious, for more than 100 documents, maybe unfeasible.

### Solution

Use Costco, an open source project that

- is a couchapp (right, this implies that you install the couchapp environment)
- offers a Web interface as sub path of the couchdb database
- allows iterating through the documents of a database and then apply modifications on a particular document
- allows to perform modifications on documents using Javascript

More information

- Project website: https://github.com/harthur/costco
- Useful examples: http://harthur.github.io/costco/

Note that Costco does not allow to perform operations involving several documents at once, for example, setting values in one document that results from querying from several other documents. Costco is perfect for corrections on the couchdb document 'schema' (not in the classic sense as there is no schema in couchdb).

### Troubleshooting

If you try to install Costco, you try to install couchapp mst likely. However, it might be that some python packages are missing which results in a 'not-so-obvious' python error during install of couchapp. The following line could be the dependencies that you might need:

```Bash
sudo apt-get install python-dev libxml2-dev libxslt-dev
```

### Cheat Sheet: Installing costco inside an sw360vagrant deployment

If you've read this far, here are a few commands to execute to install Costco on a machine deployed with our Vagrant setup.

```Bash
$ sudo apt-get install python-dev libxml2-dev libxslt-dev
$ sudo pip install couchapp
$ git clone http://github.com/harthur/costco.git
$ cd costco
$ couchapp push . http://localhost:5984/sw360db
```

### Examples in sw360

The following examples show some costco code from the use with sw360.

#### Renaming a key

In order to rename a field's key, the following code might be helpful. In the following example, the field's key `developement` into `development` (correcting a typo in the data model).

```JavaScript
function(doc) {
   if(doc.type == 'todo') {
     doc.development = doc.developement;
     delete doc.developement;
    }
  return doc;
}
```

#### Renaming a key in a subdocument

Similar thing as above, rename a key from `comment` to `createdcomment`, but this time inside a nested list of documents.

```JavaScript
function(doc) {
  if (doc.type == 'release') {
     for (var f = 0, len = doc.attachments.length; f < len; f +=1 ) {
       doc.attachments[f].createdComment = doc.attachments[f].comment;
       delete  doc.attachments[f].comment;
     }
  }
  return doc;
}
```

### More JavaScript Examples with CouchDB

In addition to Costco, also the couchdb map-reduce functions can help to track down issues in the data sets.

The following example searched for attachments of type `SOURCE` at releases, which do not have the `createdBy` set:

```JavaScript
function(doc) {
  if ((doc.type == 'release')
       && (doc.attachments)) {
         doc.attachments.forEach(attachment => {
                if (!attachment.createdBy && attachment.attachmentType === 'SOURCE') {
           emit(doc._id, attachment.filename);
  }
});
  }
}
```

The following example looks into date fields, in this case `createdOn`, and checks if it uses dots (for changing them into dashes).

```JavaScript
function(doc) {
  if(
      (doc.type == 'release')
      && (doc.createdOn.indexOf('.') !== -1)
    )
  {
      emit(doc.name, doc)
  }
}
```
