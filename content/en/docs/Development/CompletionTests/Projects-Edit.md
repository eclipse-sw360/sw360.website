---
title: "Edit Project"
linkTitle: "Edit Project"
weight: 40
---

## SW360 "Edit Project" Page Test Cases

### Summary Tab

#### General Information Section
- **Test Case ID:** PROJ-EDIT-001
- **Description:** Verify the "General Information" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "General Information" section.
    3. Verify the presence of the following fields:
        - Project Name (required)
        - Version
        - Project visibility (required) (one of Private, Me and Moderators, Group and Moderators, Everyone (default))
        - Created By (no edit)
        - Project Type (required) (one of Customer Project, Internal Project, Product (default), Service, Inner Source, Cloud Backend)
        - Tag
        - Description (textbox)
        - Domain (one of Application Software, Documentation, Embedded Software, Hardware, Test and Diagnostics)
        - Vendor (click for popup) with a clear button beneath
        - Modified On (no edit)
        - Modified By (no edit)
        - 3 vulnerability checkboxes
- **Expected Result:** All specified fields are present and function as described.

#### External URLs Section
- **Test Case ID:** PROJ-EDIT-002
- **Description:** Verify the "External URLs" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "External URLs" section.
    3. Click on the "Click to add row to External URLs" button.
    4. Verify the presence of the following fields in the new row:
        - External URL key on the left
        - Type to get default values
        - External URL value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Roles Section
- **Test Case ID:** PROJ-EDIT-003
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Roles" section.
    3. Verify the presence of the following fields:
        - Group (required) (default user department) with a clear button beneath
        - Project Manager (single value)
        - Project Owner (single value)
        - Owner Accounting Unit
        - Owner Billing Group
        - Owner Country
        - Lead Architect (single value)
        - Moderators (multi value)
        - Contributors (multi value)
        - Security Responsibles (multi value)
- **Expected Result:** All specified fields are present and function as described.

#### Additional Roles Section
- **Test Case ID:** PROJ-EDIT-004
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Additional Roles" section.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External Ids Section
- **Test Case ID:** PROJ-EDIT-005
- **Description:** Verify the "External Ids" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "External Ids" section.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** PROJ-EDIT-006
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Additional Data" section.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

### Administration Tab

#### Clearing Section
- **Test Case ID:** PROJ-EDIT-007
- **Description:** Verify the "Clearing" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Clearing" section in the Administration Tab.
    3. Verify the presence of the following fields:
        - Project Clearing State (one of Open, In Progress, Closed)
        - Clearing Team dropdown (values from backend)
        - Deadline for pre-evaluation (date)
        - Clearing summary (text area)
        - Special risk Open Source Software (text area)
        - General risk 3rd party software (text area)
        - Special risks 3rd party software (text area)
        - Sales and delivery channels (text area)
        - Remarks additional requirements (text area)
- **Expected Result:** All specified fields are present and function as described.

#### Lifecycle Section
- **Test Case ID:** PROJ-EDIT-008
- **Description:** Verify the "Lifecycle" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Lifecycle" section in the Administration Tab.
    3. Verify the presence of the following fields:
        - Project State (required) (one of Active, Phaseout, Unknown)
        - System test begin (date)
        - System test end (date)
        - Delivery start date (date)
        - Phase-out date (date)
- **Expected Result:** All specified fields are present and function as described.

#### License Info Header Section
- **Test Case ID:** PROJ-EDIT-009
- **Description:** Verify the "License Info Header" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "License Info Header" section in the Administration Tab.
    3. Verify the presence of a text area with a default license info header and a bottom on the top right of the area to reset to default text.
- **Expected Result:** The text area with the default license info header and the reset button are present.

### Linked Releases And Projects Tab

#### Linked Projects Section
- **Test Case ID:** PROJ-EDIT-010
- **Description:** Verify the "Linked Projects" section in the Linked Releases And Projects Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Linked Projects" section in the Linked Releases And Projects Tab.
    3. Verify the presence of a table with the following columns:
        - Project name
        - Project version
        - Project Relation (info hover)
        - Enable SVM (checkbox)
    4. Click on the "Add Projects" button beneath to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Projects" button opens the search popup.

#### Linked Releases Section
- **Test Case ID:** PROJ-EDIT-011
- **Description:** Verify the "Linked Releases" section in the Linked Releases And Projects Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Linked Releases" section in the Linked Releases And Projects Tab.
    3. Verify the presence of a table with the following columns:
        - Release name
        - Release version
        - Release relation (info hover)
        - Project Mainline State (info hover)
        - Comments
    4. Click on the "Add Releases" button beneath to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Releases" button opens the search popup.

### Linked Packages Tab

#### Linked Packages Section
- **Test Case ID:** PROJ-EDIT-012
- **Description:** Verify the "Linked Packages" section in the Linked Packages Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Linked Packages" section in the Linked Packages Tab.
    3. Verify the presence of a table with the following columns:
        - Package Name
        - Package Version
        - License
        - Package Manager
    4. Click on the "Add Packages" button on top to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Packages" button opens the search popup.

### Attachments Tab

#### Attachments Table
- **Test Case ID:** PROJ-EDIT-013
- **Description:** Verify the "Attachments" table in the Attachments Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Attachments" table in the Attachments Tab.
    3. Verify the presence of the following columns:
        - Filename
        - Type
        - Comment (entered by uploader)
        - Group (department of uploader)
        - Name (name of uploader)
        - Date (date of upload)
        - Status (status set by approver)
        - Comment (entered by approver)
        - Group (department of approver)
        - Name (name of approver)
        - Date (date of approve)
        - Delete icon (remove attachment)
    4. Click on the "Add Attachment" button on the bottom to add a new attachment.
    5. Make sure the changed values about comment, status, etc. are saved.
    6. Verify if the Edit views shows the saved values for the comment, status, etc.
- **Expected Result:** The table with the specified columns is present, and the "Add Attachment" button allows adding a new attachment.

#### Delete Attachment
- **Test Case ID:** PROJ-EDIT-014
- **Description:** Verify the "Delete Attachment" functionality in the Attachments Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Attachments" table in the Attachments Tab.
    3. Click on the delete icon for an attachment.
    4. If the attachment was "Accepted", popup with error "An attachment cannot be deleted while it is approved. You have to reject the approval first." should appear.
    5. "Rejected" or "Unchecked" attachments should be deleted with a popup for confirmation.
- **Expected Result:** The delete functionality shows error for "Accepted" attachments, confirmation popup for other attachments.

### Obligations Tab

#### Obligations View or Release View Switch
- **Test Case ID:** PROJ-EDIT-015
- **Description:** Verify the "Obligations View or Release View" switch in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Obligations View or Release View" switch in the Obligations Tab.
- **Expected Result:** The switch is present and functional.

#### Obligations Tabs
- **Test Case ID:** PROJ-EDIT-016
- **Description:** Verify the presence of the 4 tabs: License Obligation, Component Obligation, Project Obligation, Organisation Obligation.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the Obligations Tab.
    3. Verify the presence of the following tabs:
        - License Obligation
        - Component Obligation
        - Project Obligation
        - Organisation Obligation
- **Expected Result:** All specified tabs are present.

#### License Obligation Tab
- **Test Case ID:** PROJ-EDIT-017
- **Description:** Verify the "License Obligation" tab in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "License Obligation" tab in the Obligations Tab.
    3. Click on the leftmost expand button to expand everything.
    4. Verify the presence of the following fields:
        - License Obligation (title)
        - Licenses (show one, expand to show all)
        - Releases (show one, expand to show all)
        - Status (dropdown)
        - Type
        - Id
        - Comment
    5. Click on the button on the top right to "Add Obligations from License Database" and verify that a popup opens to get obligations not in the project and select to add.
- **Expected Result:** The specified fields are present, and the button to add obligations from the license database functions as described.

#### Component Obligation Tab
- **Test Case ID:** PROJ-EDIT-018
- **Description:** Verify the "Component Obligation" tab in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Component Obligation" tab in the Obligations Tab.
    3. Click on the leftmost expand button to expand to show the obligation text.
    4. Verify the presence of the following fields:
        - Component Obligation (title)
        - Status
        - Type
        - Id
        - Comment
- **Expected Result:** The specified fields are present.

#### Project Obligation Tab
- **Test Case ID:** PROJ-EDIT-019
- **Description:** Verify the "Project Obligation" tab in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Project Obligation" tab in the Obligations Tab.
    3. Verify the presence of the same fields as in the "Component Obligation" tab.
- **Expected Result:** The specified fields are present.

#### Organisation Obligation Tab
- **Test Case ID:** PROJ-EDIT-020
- **Description:** Verify the "Organisation Obligation" tab in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Organisation Obligation" tab in the Obligations Tab.
    3. Verify the presence of the same fields as in the "Component Obligation" tab.
- **Expected Result:** The specified fields are present.

#### Release View
- **Test Case ID:** PROJ-EDIT-021
- **Description:** Verify the "Release View" in the Obligations Tab.
- **Steps:**
    1. Navigate to the "Edit Project" page.
    2. Locate the "Obligations View or Release View" switch in the Obligations Tab and switch to "Release View."
    3. Verify that all releases are shown with the total license count in brackets.
    4. Expand a release to get Global or Other licenses.
    5. Further expand to get a list of licenses.
    6. Further expand a license to get the following fields:
        - Obligation (title)
        - Obligation text
        - Type
        - Id
        - Status (readonly)
        - Comment (readonly)
- **Expected Result:** The "Release View" shows all releases with the specified details and fields.
