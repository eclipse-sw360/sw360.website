# Motivation
In some cases inline documents are not sufficient for storing extended information to a document. This is especially the case if these information might be relevant from outside as well.
Projects, components and releases contain attachments. The metadata of these attachments are stored as inline documents inside its parent document (which is the project, component or release).
However these attachments may be used by other documents as well, e.g. license info files which are attached to releases are used by projects to generate the overall license information for that project.
In such cases an external document might be the better model. For example the attachment usage can be stored along the metadata without touching the owner document on update.

# Advantages of external documents
* single documents with a clear separation to other documents
* easy identification
* might be loaded and updated standalone

# Advantages of internal documents
* Very fast loading along with the owner
* Easy handling since only the owner must be loaded or updated

In any case it is highly dependent on the use case whether external documents are to be favored over internal documents.

# Possible implementations for linked documents
## Special ResponseHandler with special views from CouchDB

| Easy to use? | Performance? | Effort to use in existing code |
| ------------ | ------------ | ----------------------------- |
| :star::star: Middle, special views have to be created, fields of data objects has to be annotated. | :star::star::star: Very good, fetching of multiple documents with a single request. | :star: High, since existing code has to be changed |

### Couch-DB theory
At the time of writing, support of external (or linked) documents in Couch-DB is limited. Consider the following documents:
```javascript
project = {
   _id: "p1",
   type: "project",
   name: "Testproject",
   attachments: [
       { _id: "a1" },
       { _id: "z2" }
   ]
}
attachment1 = {
    _id: "a1",
    type: "attachment",
    name: "SourceFile",
    sha1: "abc1234"
}
attachment2 = {
    _id: "a2",
    type: "attachment",
    name: "LicenseFile",
    sha1: "fed9876"
}
```
Unfortunately there is no way to get the project document with the attachments directly included. With the correct view you are able to retrieve all these documents in a single request:
```javascript
function(doc) {
    if(doc.type === "attachment") {
        emit(doc._id, null);
        for(var in in doc.attachments) {
            emit(doc._id, { _id: doc.attachments[i]._id });
        }
    }
}
```
You might see the trick: the project document as well as the attachment documents are indexed with the id of the project. This way you get all three documents when querying the view with the id of the project:
```javascript
{
   "total_rows":5,
   "offset":0,
   "rows":[{
         "id":"p1",
         "key": "p1",
         "doc":{
            "_id":"p1",
            "attachments":[
               "a1", "a2"
            ],
            "name":"Testproject",
            ...
         },
         ...
      }, {
         "id":"p1",
         "doc":{
            "_id":"a1",
            name: "SourceFile",
            ...
         },
         ...
      }, {
         "id":"p1",
         "key": "p1",
         "value":null,
         "doc":{
            "_id":"a2",
            name: "LicenseFile",
            ...
         },
         ...
      }
    ]
}
```
**Note** is will only work if you query the view with `include_docs` set to `true`.
**Note** include_docs will only work at the top level of a value. In other words it will only recognize the following to situations: 
* null: if the value is null, the document which is identified by the key is included
* { _id: "..." }: the document identified by the given id is included.
To be clear: transitive inclusions will not work!
**Note** See also https://wiki.apache.org/couchdb/Introduction_to_CouchDB_views#Linked_documents.

### Implementation with Ektorp
https://github.com/eclipse/sw360/pull/596 show an implementation to transparently read such results from Couch-DB. It consists of:
* new methods in the database connector which are aware of loading linked documents
* a response handler used for parsing the results when requesting linked documents
* two annotation classes to mark fields which contain ids for linked documents
After the branch was merged, the new feature can be used in only three steps. You need:
1. A view that loads the "main" documents along with there linked documents
1. A special method in your database handler / database repository which calls the new method from the connector
1. A mixin for your data object which annotates the fields which contain ids to linked documents

#### Notes for 1.
Have a look at mapping function above in the theory section. Of course you may add more than one type of linked documents, e.g. not only attachments but releases as well.
You may also emit whole objects instead of ids only. This way Couch-DB does not have to lookup each entry. However including ids over objects is an own topic.
#### Notes for 2.
You should write methods in your repository as well as in your database handler that uses the new methods from the database connector.
#### Notes for 3.
Be sure that the used object mapper in your database handler is aware of the mixin. Of course you can annotate more than one field. All annotated fields will be respected on loading. However, if the view does not contain an object that should be resolved, it will be replaced by null. The LinkedDocuments-annotation even allows you to name a different destination field for the resolved objects for easier integration into the existing code.

## Usage with Ektorp

| Easy to use? | Performance? | Effort to use in existing code |
| ------------ | ------------ | ----------------------------- |
| :no_entry: does not work | :no_entry: | :no_entry: |

Since SW360 is using Ektorp as Objectmapper, a response like above is not suitable. Ektorp is just not able to parse the above response correctly.
However Ektorp has a linking feature as well: You may annotate fields with the `@DocumentReference`-Annotation to tell Ektorp to store the content within external documents. This only works with fields of type `Set` at the moment of writing. Since SW360 data objects are generated using Thrift, directly annotating the field is not possible. Due to the mixin feature of Ektorp this is not a big issue. Unfortunately making the `@DocumentReference`-annotation to work was not possible with a reasonable effort.

Internally Ektorp is also using special views for getting linked documents to work. A quick look into the source codes suggests that this feature is implemented using special serializers which would lead to additional requests on loading and storing as well. Therefore the same performance issues might be come across if the annotation would work.

## Own serializer/deserzialer

| Easy to use? | Performance? | Effort to use in existing code |
| ------------ | ------------ | ----------------------------- |
| :star::star::star: Quite easy, just some Jackson configuration necessary | :star::star: Good, but every type of linked objects needs an additional request | :star::star::star: Low, existing code does not have to be changed |

This method works just like the Ektorp way. In addition a slow transition from internal to external documents is possible, since the custom serialization methods will handle both cases directly. Any embedded documents will be externalized on first update of the owner object.
The following classes are needed:
1. Repository for the new external documents
1. DatabaseHandler for the new external documents
1. Mixin-Class to add annotations to the field with external documents
1. A new mapper factory to properly configure the custom serializer
1. Custom serializers/deserializer

### Example for externalizing attachments
#### Mixin-Class
This will configure Ektorp to use a special class for this field. We use a special serializer for the field instead of for the type (in this case Attachment), so we can do serialization/deserialization for all attachments at once. If we would use a special serializer, every 
```java
public abstract class SplitAttachmentsMixin extends DatabaseMixIn {
    @JsonSerialize(using = AttachmentSetSerializer.class)
    @JsonDeserialize(using = AttachmentSetDeserializer.class)
    public abstract void setAttachments(Set<Attachment> attachments);
}
```

#### Mapper factory
```java
public class SplitAttachmentsMapperFactory extends MapperFactory {

    private final AttachmentHandlerInstantiator handlerInitiator;

    public SplitAttachmentsMapperFactory(Supplier<HttpClient> httpClient, String dbName) throws MalformedURLException {
        handlerInitiator = new AttachmentHandlerInstantiator(httpClient, dbName);
    }

    @Override
    public ObjectMapper createObjectMapper() {
        ObjectMapper objectMapper = super.createObjectMapper();

        objectMapper.addMixInAnnotations(Project.class, SplitAttachmentsMixin.class);
        objectMapper.setHandlerInstantiator(handlerInitiator);

        return objectMapper;
    }

    private static class AttachmentHandlerInstantiator extends HandlerInstantiator {
        private final AttachmentSetSerializer attachmentSetSerializer;
        private final AttachmentSetDeserializer attachmentSetDeserializer;

        public AttachmentHandlerInstantiator(Supplier<HttpClient> httpClient, String dbName) throws MalformedURLException {
            attachmentSetSerializer = new AttachmentSetSerializer(httpClient, dbName);
            attachmentSetDeserializer = new AttachmentSetDeserializer(httpClient, dbName);
        }

        @Override
        public JsonDeserializer<?> deserializerInstance(DeserializationConfig config, Annotated annotated, Class<?> deserClass) {
            if (deserClass.isInstance(attachmentSetDeserializer)) {
                return attachmentSetDeserializer;
            }
            return null;
        }
        ...
    }

}
```

#### Serializer
```java
public class AttachmentSetSerializer extends JsonSerializer<Set<Attachment>> {

    private final AttachmentDatabaseHandler handler;

    public AttachmentSetSerializer(Supplier<HttpClient> httpClient, String dbName) throws MalformedURLException {
        this.handler = new AttachmentDatabaseHandler(httpClient, dbName);
    }

    @Override
    public void serialize(Set<Attachment> attachments, JsonGenerator jsonGenerator, SerializerProvider provider)
            throws IOException, JsonProcessingException {

        try {
            List<DocumentOperationResult> results = handler.bulkCreateOrUpdateAttachments(attachments);
            if (!results.isEmpty()) {
                throw new IOException("Cannot create or update attachments. Some failed: " + results);
            }
        } catch (SW360Exception exception) {
            throw new IOException("Cannot create or update attachments.", exception);
        }

        jsonGenerator.writeStartArray();
        for (Attachment attachment : attachments) {
            jsonGenerator.writeStartObject();
            jsonGenerator.writeStringField("_id", attachment.getId());
            jsonGenerator.writeEndObject();
        }
        jsonGenerator.writeEndArray();
    }
}
```

#### Deserializer
```java
public class AttachmentSetDeserializer extends JsonDeserializer<Set<Attachment>> {

    private final AttachmentDatabaseHandler handler;

    public AttachmentSetDeserializer(Supplier<HttpClient> httpClient, String dbName) throws MalformedURLException {
        this.handler = new AttachmentDatabaseHandler(httpClient, dbName);
    }

    @Override
    public Set<Attachment> deserialize(JsonParser jsonParser, DeserializationContext context) throws IOException, JsonProcessingException {
        Set<Attachment> attachments = Sets.newHashSet();

        if (!jsonParser.isExpectedStartArrayToken()) {
            throw new IllegalStateException("Expected array token but found: " + jsonParser.getCurrentToken().asString());
        }

        Set<String> attachmentIds = Sets.newHashSet();
        JsonToken token = jsonParser.nextToken();
        while (!JsonToken.END_ARRAY.equals(token)) {
            switch (token) {
            case START_OBJECT:
                Attachment attachment = jsonParser.readValueAs(Attachment.class);
                if (attachment.isSetId() && !attachment.isSetRevision()) {
                    attachmentIds.add(attachment.getId());
                } else {
                    attachments.add(attachment);
                }
                break;

            default:
                throw new IllegalStateException(
                        "Unexpected token. Expected object or string but found: " + jsonParser.getCurrentToken().asString());
            }

            token = jsonParser.nextToken();
        }

        if (!attachmentIds.isEmpty()) {
            try {
                attachments.addAll(handler.retrieveAttachments(attachmentIds));
            } catch (SW360Exception exception) {
                throw new IOException("Cannot load attachments (" + attachmentIds + ")", exception);
            }
        }

        return attachments;
    }

}
```