SW360 maintains attachments for projects, components and releases. Currently, SW360 cannot automatically detect these types and is dependent on that users select the appropriate type accordingly. If not, some functionality will not properly kick of that uses such attachments.

Also, maybe some of the types are redundant by now and are just legacy ideas that should be reviewed after two years now.

In summary, the following the types currently are as follows:

| Type name    |      Functionality      |  Description  |
|:-------------|:------------------------|:--------------|
| SOURCE  |  for sending to tools   | Source packages of a release as found on the Internet |
| COMPONENT_LICENSE_INFO_XML |    for project documentation generation    |  An XML-based description of the licenses and coprights involved |
| DESIGN | n.a. | Just nomenclature to name this not document |
| REQUIREMENT | n.a. | Just a general placeholder for an attachment |
| DOCUMENT | n.a. | Just a general placeholder for an attachment |
| CLEARING_REPORT | Setting clearing status | Reporting information for component license state |
| COMPONENT_LICENSE_INFO_COMBINED | (should be) for project documentation generation | Multiple components with component license information |
| SCAN_RESULT_REPORT | n.a. | Just description what scanners found without conclusions |
| SCAN_RESULT_REPORT_XML | n.a. | Just description what scanners found without conclusions in XML |
| SOURCE_SELF | (should be) for sending to tools    | Source packages build self, because not available in the Internet |
| BINARY | future: for sending to tool doing binary analysis | Binary from the publisher |
| BINARY_SELF | future: for sending to tool doing binary analysis | Self built binary |
| DECISION_REPORT | n.a. | Decision information ref. the component |
| LEGAL_EVALUATION | n.a. | Internally created legal evaluation |
| LICENSE_AGREEMENT | n.a. | Document describing the license agreement |
| SCREENSHOT | n.a. | If licensing information is captured with screenshot |
| OTHER | n.a. | If not document |