---
title: "Edit Release"
linkTitle: "Edit Release"
weight: 110
---

## SW360 "Edit Release" Page Test Cases

### Summary Tab

#### Release Summary Section
- **Test Case ID:** EDIT-REL-001
- **Description:** Verify the "Release Summary" section in the Summary Tab, which is the same as the "Add Releases" page.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the "Release Summary" section in the Summary Tab.
    3. Verify the presence of the following fields in the form:
        - Vendor (set the default value if Component has default vendor set) (clear button beneath)
        - Name (required, readonly with component name)
        - Version (required)
        - Programming Languages (type to get default values, multivalue)
        - Operating Systems (type to get default values, multivalue)
        - CPE ID (hover info beneath)
        - Software Platforms (type to get default values, multivalue)
        - Release date
        - Main Licenses (multivalue)
        - Other licenses (multivalue)
        - Source Code Download URL
        - Binary Download URL
        - Clearing State (New, readonly)
        - Release Mainline State (dropdown, with info hover beneath)
        - Created On
        - Created By
        - Contributors (multivalue)
        - Moderators (multivalue)
        - Modified On
        - Modified By
- **Expected Result:** All specified fields are present and function as described.

#### Additional Roles Section
- **Test Case ID:** EDIT-REL-002
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the "Additional Roles" section in the Summary Tab.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External IDs Section
- **Test Case ID:** EDIT-REL-003
- **Description:** Verify the "External IDs" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the "External IDs" section in the Summary Tab.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** EDIT-REL-004
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the "Additional Data" section in the Summary Tab.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

#### Release Repository Section
- **Test Case ID:** EDIT-REL-005
- **Description:** Verify the "Release Repository" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the "Release Repository" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Repository Type (dropdown)
        - Repository URL (textbox)
- **Expected Result:** The specified fields are present and function as described.

### Linked Releases Tab

#### Click to Add Releases Button
- **Test Case ID:** EDIT-REL-006
- **Description:** Verify the "Click to add Releases" button and the releases table in the Linked Releases Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the Linked Releases Tab.
    3. Click on the "Click to add Releases" button.
    4. Verify the presence of a table with the following columns:
        - Vendor name
        - Release name
        - Release version
        - Release relation (info hover) (dropdown)
        - delete icon
- **Expected Result:** The button and table with the specified columns are present.

### Linked Packages Tab

#### Add Packages Button
- **Test Case ID:** EDIT-REL-007
- **Description:** Verify the "Add Packages" button and the table in the Linked Packages Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the Linked Packages Tab.
    3. Click on the "Add Packages" button.
    4. Verify the presence of a table with the following columns:
        - Package Name
        - Package Version
        - License
        - Package Manager
        - delete icon
- **Expected Result:** The button and table with the specified columns are present.

### Clearing Details Tab

#### Clearing Details Section
- **Test Case ID:** EDIT-REL-008
- **Description:** Verify the "Clearing Details" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - 13 checkboxes
        - Scanned text box
        - Clearing Standard text box
        - External URL text box
        - Comments text box
- **Expected Result:** All specified fields are present and function as described.

#### Request Information Section
- **Test Case ID:** EDIT-REL-009
- **Description:** Verify the "Request Information" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - Request ID
        - Additional request Info
        - Evaluation Start
        - Evaluation End
- **Expected Result:** All specified fields are present and function as described.

#### Supplemental Information Section
- **Test Case ID:** EDIT-REL-010
- **Description:** Verify the "Supplemental Information" section in the Clearing Details Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the Clearing Details Tab.
    3. Verify the presence of the following fields:
        - External Supplier ID
        - Count of Security Vulnerabilities
- **Expected Result:** All specified fields are present and function as described.

### ECC Details Tab

#### ECC Information Section
- **Test Case ID:** EDIT-REL-011
- **Description:** Verify the "ECC Information" section in the ECC Details Tab.
- **Steps:**
    1. Navigate to the "Edit Release" page.
    2. Locate the ECC Details Tab.
    3. Verify the presence of the following fields:
        - ECC Status (dropdown) (info hover beneath)
        - ECC Comment
        - Ausfuhrliste
        - ECCN
        - Material Index Number
        - Assessor Contact Person (readonly)
        - Assessor Department (readonly)
        - Assessment Date (readonly)
- **Expected Result:** All specified fields are present and function as described.

### Attachments Tab

#### Attachments Table
- **Test Case ID:** [PROJ-EDIT-013]({{< relref path="Projects-Edit.md">}}#attachments-table)
