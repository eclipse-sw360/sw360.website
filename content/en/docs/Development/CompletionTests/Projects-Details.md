---
title: "Project Details"
linkTitle: "Project Details"
weight: 50
---

## SW360 "Project Details" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** PROJ-PROJ-DTL-001
- **Description:** Verify the presence of the "Edit Project", "Link to Projects", "Import SBOM", and "Export SBOM" buttons on top.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The specified buttons are present.

### Summary Tab

#### General Information Section
- **Test Case ID:** PROJ-PROJ-DTL-002
- **Description:** Verify the "General Information" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "General Information" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - ID of the project
        - Name
        - Version
        - Visibility
        - Created on
        - Created by (mailto link)
        - Modified on
        - Modified by (mailto link)
        - Project type
        - Domain
        - Tag
        - External IDs (as UL, key in bold, value next to it)
        - Additional data (same as External IDs)
        - External URLs (same as External IDs display, but values are clickable URLs)
- **Expected Result:** All specified fields are present and function as described.

#### Roles Section
- **Test Case ID:** PROJ-PROJ-DTL-003
- **Description:** Verify the "Roles" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Roles" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Group of project
        - Project Responsible
        - Project Owner
        - Owner Accounting Unit
        - Owner Billing Group
        - Owner Country
        - Lead Architect
        - Moderators
        - Contributors
        - Security Responsibles
        - Additional Roles
    4. Verify that all users displayed are mailto links.
    5. Verify that Moderators, Contributors, and Security Responsibles are displayed as a comma-separated list.
    6. Verify that Additional Roles are displayed similar to External URLs.
- **Expected Result:** All specified fields are present and function as described.

#### Project Vendor Section
- **Test Case ID:** PROJ-PROJ-DTL-004
- **Description:** Verify the "Project Vendor" section in the Summary Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Project Vendor" section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Vendor's Full Name
        - Short Name
        - URL
- **Expected Result:** All specified fields are present and function as described.

### Administration Tab

#### Clearing Section
- **Test Case ID:** PROJ-DTL-005
- **Description:** Verify the "Clearing" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Clearing" section in the Administration Tab.
    3. Verify the presence of the following fields:
        - Project clearing state
        - Clearing details (New releases count, Under clearing count, Report available count, Approved count)
        - Clearing Team
        - Deadline for pre-evaluation
        - Clearing summary
        - Special risk Open Source Software
        - General risks 3rd party software
        - Special risks 3rd party software
        - Sales and delivery channels
        - Remarks additional requirements
    4. Verify that the values for Clearing summary, Special risk Open Source Software, General risks 3rd party software, Special risks 3rd party software, Sales and delivery channels, Remarks additional requirements are in a readonly text area.
- **Expected Result:** All specified fields are present and function as described.

#### Lifecycle Section
- **Test Case ID:** PROJ-DTL-006
- **Description:** Verify the "Lifecycle" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Lifecycle" section in the Administration Tab.
    3. Verify the presence of the following fields:
        - Project state
        - System test begin
        - System test end
        - Delivery start
        - Phase-out since
- **Expected Result:** All specified fields are present and function as described.

#### License Info Header Section
- **Test Case ID:** PROJ-DTL-007
- **Description:** Verify the "License Info Header" section in the Administration Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "License Info Header" section in the Administration Tab.
    3. Verify the presence of the license info header of the project in a big text area.
- **Expected Result:** The license info header is displayed in a big text area.

### Obligation Tab

#### Tab Name and Count
- **Test Case ID:** PROJ-DTL-008
- **Description:** Verify that the tab name itself shows the count of "Status changed obligations / Total obligations."
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Obligation Tab.
- **Expected Result:** The tab name shows the count of "Status changed obligations / Total obligations."

#### Obligation Information
- **Test Case ID:** PROJ-DTL-009
- **Description:** Verify the display of obligation information as per test cases EDIT-014, EDIT-015, EDIT-016, EDIT-017, EDIT-018, and EDIT-019.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Obligation Tab.
- **Expected Result:** The obligation information is displayed as per the specified test cases.

#### Create Project Clearing Report Dropdown
- **Test Case ID:** PROJ-DTL-010
- **Description:** Verify the presence of the "Create Project Clearing Report" dropdown on top with "Project only" and "Project with sub project" options.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Obligation Tab.
    3. Verify the presence of the "Create Project Clearing Report" dropdown.
- **Expected Result:** The dropdown is present with the specified options.

#### Report Button
- **Test Case ID:** PROJ-DTL-011
- **Description:** Verify that clicking on the report button redirects to the CLI Attachment usage view with a "Download" button.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Obligation Tab.
    3. Click on the report button.
- **Expected Result:** The page redirects to the CLI Attachment usage view with a "Download" button.

### ECC Tab

#### ECC Information Table
- **Test Case ID:** PROJ-DTL-012
- **Description:** Verify the display of ECC information for all releases (including sub projects) in a table with the specified columns.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the ECC Tab.
    3. Verify the presence of a table with the following columns:
        - Status
        - Release name (clickable link to open release)
        - Release version
        - Creator Group
        - ECC Assessor
        - ECC Assessor Group
        - ECC Assessment Date
        - ECCN
- **Expected Result:** The table with the specified columns is present.

### Vulnerability Tracking Status Tab

#### Vulnerability State Information Section
- **Test Case ID:** PROJ-DTL-013
- **Description:** Verify the "Vulnerability State Information" section in the Vulnerability Tracking Status Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Vulnerability Tracking Status Tab.
    3. Verify the presence of the following fields:
        - "Security Vulnerability Monitoring" for the project as Enabled / Disabled
        - "Do not create monitoring list, but use list from external id" for the project as Enabled / Disabled
        - "com.siemens.svm.monitoringlist.id" for the project
- **Expected Result:** All specified fields are present and function as described.

#### Tracking Status Table
- **Test Case ID:** PROJ-DTL-014
- **Description:** Verify the table below with the tracking status of releases displaying the specified columns.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Vulnerability Tracking Status Tab.
    3. Verify the presence of a table with the following columns:
        - Name (clickable link to open the release)
        - Project Origin (which project release is linked with)
        - SVM Tracking Status (tracked or not)
        - Short Status
        - Type
- **Expected Result:** The table with the specified columns is present.

### Attachments Tab

#### Download Attachment Bundle Button
- **Test Case ID:** PROJ-DTL-015
- **Description:** Verify the presence of the "Download Attachment Bundle" button on top, which opens Attachment Usage for SRC.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Attachments Tab.
    3. Click on the "Download Attachment Bundle" button.
- **Expected Result:** The Attachment Usage for SRC is opened.

#### Attachments Table
- **Test Case ID:** PROJ-DTL-016
- **Description:** Verify the display of the following column information in the Attachments Table.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Attachments Tab.
    3. Verify the presence of the following columns:
        - Download button to download all attachments as a zip. In rows, it will act as an expand button, showing
          SHA1, Uploaded On, Uploaded Comment, Checked On, and Checked Comment.
        - File name (uploaded file name)
        - Size (file size)
        - Type (attachment type)
        - Group (uploader's Department)
        - Uploaded by (uploader)
        - Group (approver Department, in green if approved, red or black)
        - Checked by (approver, green, red, or black)
        - Usages (attachment usage count)
        - Actions (download button for attachment)
- **Expected Result:** The table with the specified columns is present. The data is correct from the database.

### Vulnerabilities Tab

#### Dropdown on Top
- **Test Case ID:** PROJ-DTL-017
- **Description:** Verify the dropdown on top with options to show the latest 200/500/1000/All vulnerabilities.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Vulnerabilities Tab.
- **Expected Result:** The dropdown with the specified options is present.

#### Tabs
- **Test Case ID:** PROJ-DTL-018
- **Description:** Verify the presence of tabs: Summary, Current project, Child projects, etc. If no child project, only 1 tab: Current project.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Vulnerabilities Tab.
- **Expected Result:** The specified tabs are present.

#### Summary Tab
- **Test Case ID:** PROJ-DTL-019
- **Description:** Verify the "Summary" tab in the Vulnerabilities Tab.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Summary" tab in the Vulnerabilities Tab.
    3. Verify the presence of the following fields:
        - Total vulnerabilities (current + child projects)
        - Vulnerabilities table with columns: Project name, Release, External ID (link to vulnerability), Priority (hover info with value), Matched by, Title, Relevance for project (hover info with value), Actions
- **Expected Result:** The specified fields are present and function as described.

#### Project Tab
- **Test Case ID:** PROJ-DTL-020
- **Description:** Verify the "Project" tab in the Vulnerabilities Tab (only tab if no sub project).
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the "Project" tab in the Vulnerabilities Tab.
    3. Verify the presence of the following fields:
        - Total vulnerabilities (current)
        - Vulnerability state information: Security Vulnerabilities Display Enabled/Disabled
        - Vulnerabilities table with columns: Checkbox, Release, External ID (link to vulnerability), Priority (hover info with value), Matched by, Title, Relevance for project (hover info with value), Actions
        - Change rating and action of selected vulnerabilities with "Change" button, open popup with Selected vulnerabilities count, Rating, Action, and comment, and Change Rating button to submit
        - Vulnerability Matching statistic with Matched By histogram
- **Expected Result:** The specified fields are present and function as described.

### Changelog Tab

#### Toggle on Top
- **Test Case ID:** PROJ-DTL-021
- **Description:** Verify the presence of the "Change Log" and "Changes" toggle on top.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
- **Expected Result:** The toggle is present with the specified options.

#### Changelog Table
- **Test Case ID:** PROJ-DTL-022
- **Description:** Verify the display of the table with the specified columns.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
    3. Verify the presence of a table with the following columns:
        - Date
        - Change Log Id
        - Change Type
        - User
        - Actions (button to open changelog)
- **Expected Result:** The table with the specified columns is present.

#### Opening Changelog
- **Test Case ID:** PROJ-DTL-023
- **Description:** Verify that opening a changelog changes the toggle on top to "Changes."
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
    3. Click on the "Actions" button to open a changelog.
- **Expected Result:** The toggle on top changes to "Changes."

#### Basic Info Section
- **Test Case ID:** PROJ-DTL-024
- **Description:** Verify the "Basic Info" section when a specific changelog is open.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
    3. Open a changelog.
    4. Verify the presence of the following fields in the "Basic Info" section:
        - User
        - Date
        - Operation
        - Document Id
        - Document Type
        - Reference Doc (list)
- **Expected Result:** The specified fields are present and function as described.

#### Changed Fields Table
- **Test Case ID:** PROJ-DTL-025
- **Description:** Verify the display of each changed field as a separate table with original value in left (in red), new value in right (in green), and diff highlighted between old and new value.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
    3. Open a changelog.
    4. Verify the presence of a table for each changed field with the specified details.
- **Expected Result:** The table with the specified details is present.

#### Returning to List
- **Test Case ID:** PROJ-DTL-026
- **Description:** Verify that clicking on the "Change Log" toggle on top returns to the list.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Changelog Tab.
    3. Open a changelog.
    4. Click on the "Change Log" toggle on top.
- **Expected Result:** The page returns to the list view.

### License Clearing Tab

#### New Buttons on Top
- **Test Case ID:** PROJ-DTL-027
- **Description:** Verify the presence of the "Tree View | List View" toggle, Export Spreadsheet dropdown, Generate License Info dropdown, Generate Source Code Bundle, and Create Clearing Request button on top.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the License Clearing Tab.
- **Expected Result:** The specified buttons and dropdowns are present.

#### Conditional Buttons
- **Test Case ID:** PROJ-DTL-028
- **Description:** Verify the presence of conditional buttons based on user roles and project permissions.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the License Clearing Tab.
    3. Verify the presence of the "Add License Info to Release" button if the user is with Clearing Admin role or above.
    4. Verify the presence of the "Sync Linked Releases" button if the project has linked Packages and the user has write access to the current project.
- **Expected Result:** The specified buttons are present based on the user's role and project permissions.

#### Linked Release Table
- **Test Case ID:** PROJ-DTL-029
- **Description:** Verify the display of the linked release table with the specified columns.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the License Clearing Tab.
    3. Verify the presence of a table with the following columns:
        - Name (release name and version, clickable link to open release, expand button next to subproject and release with linked releases)
        - Type (filterable)
        - Relation (filterable)
        - Main licenses (truncated, but expandable, i next to it to show license info, if multiple release "Failed to load source")
        - Other licenses (same as Main licenses)
        - State (filterable)
        - Release Mainline State
        - Project Mainline State
        - Release Linked Date
        - Comment
        - Actions (edit icon to edit release or subproject)
- **Expected Result:** The table with the specified columns is present.

#### List View Toggle
- **Test Case ID:** PROJ-DTL-030
- **Description:** Verify the behavior of the "List View" toggle.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the License Clearing Tab.
    3. Toggle to "List View" from "Tree View."
    4. Verify that all releases expand from current or sub projects recursively, no more expand button, and a new column "Project Path" is added showing the current project or path to sub project from where the release is coming.
- **Expected Result:** The specified behavior is observed when toggling to "List View."

### Linked Packages Tab

#### Linked Packages Table
- **Test Case ID:** PROJ-DTL-031
- **Description:** Verify the display of the linked packages table with the specified columns.
- **Steps:**
    1. Navigate to the "Project Details" page.
    2. Locate the Linked Packages Tab.
    3. Verify the presence of a table with the following columns:
        - Vendor (filterable)
        - Package Name Version (filterable)
        - Release Name version (filterable)
        - Release clearing state (filterable)
        - Licenses (filterable)
        - Package Manager (filterable)
        - Actions (with edit icon to edit package)
- **Expected Result:** The table with the specified columns is present.
