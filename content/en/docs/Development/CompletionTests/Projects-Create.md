---
title: "Add Project"
linkTitle: "Add Project"
weight: 30
---

## SW360 "Add Project" Page Test Cases

### General Page Behavior

#### New Page Opening
- **Test Case ID:** PROJ-CRT-001
- **Description:** Verify that upon clicking "Add Project," a new page opens with a message on top "Creating new Project."
- **Steps:**
    1. Navigate to the Main Projects page.
    2. Click on the "Add Project" button.
- **Expected Result:** A new page opens with the message "Creating new Project" on top.

### Summary Tab

#### General Information Section
- **Test Case ID:** PROJ-CRT-002
- **Description:** Verify the "General Information" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
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
- **Test Case ID:** PROJ-CRT-003
- **Description:** Verify the "External URLs" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "External URLs" section.
    3. Click on the "Click to add row to External URLs" button.
    4. Verify the presence of the following fields in the new row:
        - External URL key on the left
        - Type to get default values
        - External URL value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Roles Section
- **Test Case ID:** PROJ-CRT-004
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
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
- **Test Case ID:** PROJ-CRT-005
- **Description:** Verify the "Additional Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Additional Roles" section.
    3. Click on the "Click to add row to Additional Roles" button.
- **Expected Result:** A new row is added for additional roles.

#### External Ids Section
- **Test Case ID:** PROJ-CRT-006
- **Description:** Verify the "External Ids" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "External Ids" section.
    3. Click on the "Click to add row to External Ids" button.
    4. Verify the presence of the following fields in the new row:
        - External Id key on the left
        - Type to get default values
        - External Id value on the right
        - Row delete button on the end
- **Expected Result:** A new row is added with the specified fields.

#### Additional Data Section
- **Test Case ID:** PROJ-CRT-007
- **Description:** Verify the "Additional Data" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Additional Data" section.
    3. Click on the "Click to add row to Additional Data" button.
- **Expected Result:** A new row is added for additional data.

### Administration Tab

#### Clearing Section
- **Test Case ID:** PROJ-CRT-008
- **Description:** Verify the "Clearing" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
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
- **Test Case ID:** PROJ-CRT-009
- **Description:** Verify the "Lifecycle" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Lifecycle" section in the Administration Tab.
    3. Verify the presence of the following fields:
        - Project State (required) (one of Active, Phaseout, Unknown)
        - System test begin (date)
        - System test end (date)
        - Delivery start date (date)
        - Phase-out date (date)
- **Expected Result:** All specified fields are present and function as described.

#### License Info Header Section
- **Test Case ID:** PROJ-CRT-010
- **Description:** Verify the "License Info Header" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "License Info Header" section in the Administration Tab.
    3. Verify the presence of a text area with a default license info header and a bottom on the top right of the area to reset to default text.
- **Expected Result:** The text area with the default license info header and the reset button are present.

### Linked Releases And Projects Tab

#### Linked Projects Section
- **Test Case ID:** PROJ-CRT-011
- **Description:** Verify the "Linked Projects" section in the Linked Releases And Projects Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Linked Projects" section in the Linked Releases And Projects Tab.
    3. Verify the presence of a table with the following columns:
        - Project name
        - Project version
        - Project Relation (info hover)
        - Enable SVM (checkbox)
        - Delete icon
    4. Click on the "Add Projects" button beneath to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Projects" button opens the search popup.

#### Linked Releases Section
- **Test Case ID:** PROJ-CRT-012
- **Description:** Verify the "Linked Releases" section in the Linked Releases And Projects Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Linked Releases" section in the Linked Releases And Projects Tab.
    3. Verify the presence of a table with the following columns:
        - Release name
        - Release version
        - Release relation (info hover)
        - Project Mainline State (info hover)
        - Comments
        - Delete icon
    4. Click on the "Add Releases" button beneath to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Releases" button opens the search popup.

### Linked Packages Tab

#### Linked Packages Section
- **Test Case ID:** PROJ-CRT-013
- **Description:** Verify the "Linked Packages" section in the Linked Packages Tab.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Locate the "Linked Packages" section in the Linked Packages Tab.
    3. Verify the presence of a table with the following columns:
        - Package Name
        - Package Version
        - License
        - Package Manager
    4. Click on the "Add Packages" button on top to open the search popup.
- **Expected Result:** The table with the specified columns is present, and the "Add Packages" button opens the search popup.

### Create Project Button

#### Project Creation
- **Test Case ID:** PROJ-CRT-014
- **Description:** Verify that upon hitting the "Create Project" button, the project is saved, and the user is redirected to the project edit page for the newly created project.
- **Steps:**
    1. Navigate to the "Add Project" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create Project" button.
- **Expected Result:** The project is saved, and the user is redirected to the project edit page for the newly created project.
