# Enumerations

This page explains all enumeration values for the internal thrift API for the thrift files as found in:

https://github.com/eclipse/sw360/tree/master/libraries/lib-datahandler/src/main/thrift

Which is comprised of the following methods:

* attachments 
* codescoop 
* components 
* cvesearch 
* fossology 
* importstatus 
* licenseinfo 
* licenses 
* moderation 
* projectimport 
* projects 
* schedule 
* search 
* sw360 
* users 
* vendors 
* vulnerabilities 


## Attachments

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/attachments.thrift

### AttachmentType

| Value  | Description.  |
|---|---|
| DOCUMENT | justa document |
| SOURCE | original course code |
| DESIGN  | design document  |
| REQUIREMENT  | requirements document  |
| CLEARING_REPORT  | OSS licensing reporting  |
| COMPONENT_LICENSE_INFO_XML  | XML document with licenseing information - e.g. SPDX  |
| COMPONENT_LICENSE_INFO_COMBINED  | XML document with licensing information covering multiple componnts at once - e.g. SPDX |
| SCAN_RESULT_REPORT  | Output what a scanner for licenses has found |
| SCAN_RESULT_REPORT_XML  | Output what a scanner for licenses has found this time in XML |
| SOURCE_SELF  | Self assembled source code distribution  |
| BINARY  | Binary of component from vendor  |
| BINARY_SELF  | Self built binary |
| DECISION_REPORT  |  documenting importing decisions for using this item |
| LEGAL_EVALUATION  | Some legal evaluation created for this item |
| LICENSE_AGREEMENT  | A ruling license agreement for this item, note that this could be for commercial software for example  |
| SCREENSHOT  | Screenshot, usually screenshot of the Website with licensing information |
| OTHER  |  anything that dos not match to the given above |

### CheckStatus 

| Value  | Description.  |
|---|---|
| NOTCHECKED | Default value after upload. |
| ACCEPTED | Reviewed and confirmed attachment. |
| REJECTED | Document or attachment cannot be used. |

## CodeScoop Thrift File

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/codescoop.thrift

## Components 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/components.thrift

## cvesearch 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/cvesearch.thrift

| Value  | Description |
|---|---|
| NEW | ...  |
| UPDATED | New information for a notification message, so it is updated |
| OLD | ...  |
| FAILED | ...  |

## Fossology 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/fossology.thrift

_No enumerations provided_

## Importstatus 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/importstatus.thrift

_No enumerations provided_

## License Info 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/licenseinfo.thrift

_No enumerations provided_

### LicenseInfoRequestStatus

| Value  | Description |
|---|---|
| SUCCESS | ...  |
| NO_APPLICABLE_SOURCE | ...  |
| FAILURE  | ...  |

### OutputFormatVariant

| Value  | Description |
|---|---|
| REPORT | ...  |
| DISCLOSURE | ...  |

## Licenses 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/licenses.thrift

_No enumerations provided_

## Moderation 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/moderation.thrift

### DocumentType 

| Value  | Description |
|---|---|
| COMPONENT | ...  |
| RELEASE | ...  |
| PROJECT | ...  |
| LICENSE | ...  |
| USER | ...  |

## Project Import 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/projectimport.thrift

_No enumerations provided_

## Projects 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/projects.thrift

### Project State

| Value  | Description |
|---|---|
| ACTIVE | _well_  |
| PHASE_OUT | _well_  |
| UNKNOWN | _well_  |

### Project Type

| Value  | Description |
|---|---|
| CUSTOMER | Project that delivers artifacts to customer outside organisation  |
| INTERNAL | Project that provides artifacts or service for internal use |
| PRODUCT | Just that it is a product instead of a project  |
| SERVICE | Project that provides services to customer outside organisation  |
| INNER_SOURCE | Inner source project, meaning that everyone inside org can use it |

### Project Relationship

| Value  | Description |
|---|---|
| UNKNOWN | _unknown_ |
| REFERRED | Sister project |
| CONTAINED | Sub project |
| DUPLICATE | _duplicate_ |

### Project Clearing State

| Value  | Description |
|---|---|
| OPEN | not started |
| IN_PROGRESS | ... |
| CLOSED | ... |

## Schedule 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/schedule.thrift

_No enumerations provided_

## Search 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/search.thrift

_No enumerations provided_

## General SW360 Thrift

### Software Mainline States

| Value  | Description |
|---|---|
| OPEN   | Not decided so far  |
| MAINLINE   | Organisation or person thinks that use of this software is recommended, which included multiple versions.  |
| SPECIFIC   | The software is not recommended in general, but for special use case or for this particular version it is acceptable.  | 
| PHASE_OUT   | The software has issues, please consider removing it soon, if in use.   |
| DENIED   | Software which is not allowed for use. For example, software that does not have licensing. |


## General SW360 Thrift

### Software Mainline States

| Value  | Description.  |
|---|---|
| OPEN   | Not decided so far  |
| MAINLINE   | Organisation or person thinks that use of this software is recommended, which included multiple versions.  |
| SPECIFIC   | The software is not recommended in general, but for special use case or for this particular version it is acceptable.  | 
| PHASE_OUT   | The software has issues, please consider removing it soon, if in use.   |
| DENIED   | Software which is not allowed for use. For example, software that does not have licensing. |

### Moderation States

| Value  | Description  |
|---|---|
| PENDING | Not opened so far.  |
| APPROVED | A person who has received the moderation request (which could be creator of the document, a clearing admin, a moderator, etc.) has approved the moderation request. It could be deleted then. |
| REJECTED | A person who has received the moderation request (which could be creator of the document, a clearing admin, a moderator, etc.) has rejected the moderation request.  | 
| INPROGRESS | A person who has received the moderation request (which could be creator of the document, a clearing admin, a moderator, etc.) has opened / viewed the moderation request, but did not decide. |

### Visibility 

| Value  | Description  |
|---|---|
| PRIVATE | Only visible by creator (and admin which applies to all visibility levels). |
| ME_AND_MODERATORS | Visible by creator and moderators. |
| BUISNESSUNIT_AND_MODERATORS | All users of the same group and the moderators. | 
| EVERYONE | Every user who is logged into the system. |

### Verification State

| Value  | Description  |
|---|---|
| NOT_CHECKED | No one has yet looked at this and verified it. |
| CHECKED  | It is verified. |
| INCORRECT  | It was decided that the verification should be rejected. | 

### Release Relationship

| Value  | Description | Clearing releav nt |
|---|---|---|
| CONTAINED | If you just do not know whether it is dynamically linked. | Yes |
| REFERRED | Referencing a stand alone used other part.  | No |
| UNKNOWN | If you just do not know.  | Yes |
| DYNAMICALLY_LINKED | Software dynamically linked - as the name says.  | Yes |
| STATICALLY_LINKED | Software statically linked - as the name says. | Yes |
| SIDE_BY_SIDE | Not decided so far. | Yes |
| STANDALONE | Software is given as standalone delivery, ie. not technically connected.  |  Yes |
| INTERNAL_USE | Used for creating or building or  ? the product or projects but not delivered.  |  Yes |
| OPTIONAL   | Is not mandatory part of the installation.   | Yes |
| TO_BE_REPLACED | Is there but should be moved out. | Yes |

## Users 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/users.thrift

## Vendors 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/vendors.thrift

_No enumerations provided_

## Vulnerabilities 

https://github.com/eclipse/sw360/blob/master/libraries/lib-datahandler/src/main/thrift/vulnerabilities.thrift

_No enumerations provided_