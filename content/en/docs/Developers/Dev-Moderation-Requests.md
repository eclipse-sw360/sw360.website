## General

The concept of moderation is good for two things:

* to cope with a large number of potential edits on documents. 
* to allow every user to propose edits.

Allowing every user to edit opposed to propose edits would lad to a large number of changes, potentially, not making everyone happy. As such, the changes should be reviewed by an experienced person and can be then approved.

## Application Flow

A user changes a moderated document, which are component, release, project and todo's of licenses (and the white list):

* The user switches in edit mode and applies a change.
* The user submits the change by clicking "Update ..."
* The application checks, if the permissions are sufficient
* For sufficient permissions, see here: https://github.com/siemens/sw360portal/wiki/Dev-Role-Authorisation-Model
* If the permissions do not allow the edit right away, a moderation request is created.

* Moderators can see the moderation request in the moderation portlet
* Having selected the moderation request, the moderator can accept the request, decline, postpone or remove himself from the list of moderators

## Technical Description
### Checking Document Permissions

If a moderation requests needs to be created, because the user does not have sufficient permissions:

* The request goes through the stack, for example: project portlet, project handler, project database handler.
* Then the project database handler checks for permissions using `makePermission()` (`DocumentPermission` is the base class, then `ProjectPermissions` is the referring here for projects) and `isActionAllowed()`.
* For moderation requests, we assume that this action is not allowed. Then, the `ProjectModerator` is called (see package `...sw360.datahandler.entitlement`).
* This class (which is part of the project service) creates a thrift client to the moderation service (also on the backend) and creates a moderation request using this client.

Every moderation request is created using the thrift-based API.

### Writing a Moderation Request to the Database

The generation of moderation request is performed by the moderation service. The moderation service handles incoming request in the following way:

* The requests arrives in the `ModerationDatabaseHandler`.
* This handler writes the request to the database.

### Creation Details in the Service

The handler writes one moderation request per user and document. If a moderation request from the same user for the same document exists, added moderation requests are merged. Or, the request is new either with a new user, new document or both, then the moderation request is created.

Each moderation requests has recipients, the moderators. The moderation database handler selects the moderators depending on the document type, which are usually the creator of the document and the listed moderators for this document. See details in the `ModerationDatabaseHandler` class. At the same location the check for deletion is performed. 

### What is in the Database?

The moderation request is a document in the couchdb. Technically, the moderation requests holds the affected document as field where the values is a nested JSON dictionary.

The following screen shot shows an example for a moderation request for a project.

![Example Moderation Request in Database](https://raw.githubusercontent.com/wiki/siemens/sw360portal/images/036-oss-sw360-20160310-screenshot-moderation-reqeust-document-example.png)


### Evaluating the Moderation Request

On the moderation portlet all moderations will be shown, for which the user is a moderator.
Only open moderation requests can be selected. Approved and declined moderation requests will only be shown.
On selecting the moderation requests, both documents (original and the updated out of the moderation request) will be compared in the `merge.jsp` and all differences will be shown to the moderator. This is done via tags such as the `sw360:CompareProject`-tag. Opening the detailed view of the moderation request changes the state to `in progress` to show other moderators that the moderation request is in work.

The following actions are possible:
* `Accept request`: the document within the moderation request will be accepted and written to the DB via e.g. the `ProjectService`. The state is set to `ACCEPTED`.
* `Remove Me from Moderators`: the state of the moderation requests is set to `PENDING` again and the logged in moderator will be removed from the moderation list.
* `Decline request`: the moderation requests will be set to `REJECTED` and still shown in the list
* `Postpone request`: the state will be `IN PROGRESS`.
* `Cancel`: the moderation state is set to `PENDING` and the moderation request will still be shown in the moderation request list