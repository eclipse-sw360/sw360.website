---
title: "Create Release"
linkTitle: "Create Release"
weight: 100
---

## SW360 "Add Releases" Page Test Cases

### General Page Behavior

#### Button Visibility
- **Test Case ID:** RED-CRT-001
- **Description:** Verify that the button to open the "Add Releases" page is visible from the "Edit Component" page, under the "Releases" Tab only.
- **Steps:**
    1. Navigate to the "Edit Component" page.
    2. Locate the "Releases" Tab.
- **Expected Result:** The button to open the "Add Releases" page is present.

### Summary Tab

#### Release Summary Section
- **Test Case ID:** RED-CRT-002
- **Description:** Verify the "Release Summary" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
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
- **Test Case ID:** RED-CRT-003
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Locate the "Additional Roles" section in the Summary Tab.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External IDs Section
- **Test Case ID:** RED-CRT-004
- **Description:** Verify the "External IDs" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Locate the "External IDs" section in the Summary Tab.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** RED-CRT-005
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Locate the "Additional Data" section in the Summary Tab.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

#### Release Repository Section
- **Test Case ID:** RED-CRT-006
- **Description:** Verify the "Release Repository" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Locate the "Release Repository" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Repository Type (dropdown)
        - Repository URL (textbox)
- **Expected Result:** The specified fields are present and function as described.

### Linked Releases Tab

#### Click to Add Releases Button
- **Test Case ID:** RED-CRT-007
- **Description:** Verify the "Click to add Releases" button and the releases table in the Linked Releases Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
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
- **Test Case ID:** RED-CRT-008
- **Description:** Verify the "Add Packages" button and the table in the Linked Packages Tab.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Locate the Linked Packages Tab.
    3. Click on the "Add Packages" button.
    4. Verify the presence of a table with the following columns:
        - Package Name
        - Package Version
        - License
        - Package Manager
        - delete icon
- **Expected Result:** The button and table with the specified columns are present.

### Create Release Button

#### Release Creation
- **Test Case ID:** RED-CRT-009
- **Description:** Verify that upon clicking the "Create Release" button, the release is created, and the user is redirected to the "Edit Release" page of the created release.
- **Steps:**
    1. Navigate to the "Add Releases" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create Release" button.
- **Expected Result:** The release is created, and the user is redirected to the "Edit Release" page of the created release.
