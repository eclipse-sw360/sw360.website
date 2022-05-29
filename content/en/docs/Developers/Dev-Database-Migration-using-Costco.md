### Praeamble

Please note that database migrations are done now in python scripts at

> https://github.com/eclipse/sw360/tree/master/scripts/migrations

keeping the following page because Costco might be useful for development / testing / quick adaptations.

### Problem

The main problem with changing field names in thrift is that existing documents in the couchdb need adjustments. Unfortunately, the futon interface of the couchdb does not offer bulk edits. As a consequence, looking into every document is tedious, for more than 100 documents, maybe unfeasible.

### Solution

Use costco, an open source project that

* is a couchapp (right, this implies that you install the couchapp environment)
* offers a Web interface as sub path of the couchdb database
* allows to iterate through the documents of a database and then apply modifications on a particular document
* allows to perform modifications on documents using Java script

More information

* Project website: https://github.com/harthur/costco
* Useful examples: http://harthur.github.io/costco/

Note that costco does not allow to perform operations involving several documents at once, for example, setting values in one document that results from querying from several other documents. Costco is perfect for corrections on the couchdb document 'schema' (not in the classic sense as there is no schema in couchdb).

### Troubleshooting

If you try to install costco, you try to install couchapp mst likely. However, it might be that some python packages are missing which results in a 'not-so-obvious' python error during install of couchapp. The following line could be th dependencies that you might need:
```
sudo apt-get install python-dev libxml2-dev libxslt-dev
```

### Cheat Sheet: Installing costco inside an sw360vagrant deployment

OK, if you read until here, to make it easy for you just the few lines to have executed to install costco when youi have a machine that is deployed with our vagrant:

```
$ sudo apt-get install python-dev libxml2-dev libxslt-dev
$ sudo pip install couchapp
$ git clone http://github.com/harthur/costco.git
$ cd costco
$ couchapp push . http://localhost:5984/sw360db
```

### Examples in sw360

The following examples show some costco code from the use with sw360.

#### Renaming a key

In order to rename a field's key, the following code might be helpful. In the following example, the field's key ```developement``` into ```development``` (correcting a typo in the datamodel).

```
function(doc) {
   if(doc.type == 'todo') {
     doc.development = doc.developement;
     delete doc.developement;
    }
  return doc;
}
```

#### Renaming a key in a subdocument

Similar thing as above, rename a key from ```comment``` to ```createdcomment```, but this time inside a nested list of documents.

```
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

In addition to costco, also the couchdb map-reduce functions can help to track down issues in the data sets.

The following example searched for attachments of type `SOURCE` at releases, which do not have the `createdBy` set:

```
function(doc) { 
  if ((doc.type == 'release') 
       && (doc.attachments)) {
    for (var attachment in doc.attachments) {
      if (!doc.attachments[attachment].createdBy) {
        if (doc.attachments[attachment].attachmentType== 'SOURCE') {
          emit(doc._id, doc.attachments[attachment].filename);
        }
      }
    }
  }
}
```

The following example looks into date fields, in this case `createdOn`, and checks if it uses dots (for changing them into dashes).

```
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