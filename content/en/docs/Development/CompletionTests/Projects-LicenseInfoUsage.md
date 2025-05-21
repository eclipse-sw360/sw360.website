---
title: "Project - License Info Usages"
linkTitle: "Project - License Info Usages"
weight: 52
---

## SW360 "Generate License Info" Page Test Cases

### General Page Behavior

#### Page Similarity
- **Test Case ID:** PROJ-LI-AU-001
- **Description:** Verify that the page shown when the "Generate License Info" button is clicked in the "License Clearing Tab" is similar to the Attachment Usages page.
- **Steps:**
    1. Navigate to the "License Clearing Tab" in a project.
    2. Click on the "Generate License Info" button.
- **Expected Result:** A page similar to the Attachment Usages page is shown.

#### Top Buttons and Toggles
- **Test Case ID:** PROJ-LI-AU-002
- **Description:** Verify the presence of the "Download" button and the "Show All" or "Only Approved" toggle on top. The "Only Approved" toggle should show only approved CLI attachments.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the top section of the page.
    3. Click on the "Only Approved" toggle.
- **Expected Result:** The "Download" button and toggles are present. The "Only Approved" toggle shows only approved CLI attachments.

#### Selection Restore Message
- **Test Case ID:** PROJ-LI-AU-003
- **Description:** Verify the display of the selection restore message.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the message section.
- **Expected Result:** The selection restore message is displayed.

### License Info Table

#### Columns
- **Test Case ID:** PROJ-LI-AU-004
- **Description:** Verify the presence of the specified columns in the License Info Table.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the License Info Table.
    3. Verify the presence of the following columns:
        - Checkbox (clicking will uncheck all checkboxes (except self) and restore selection at page load)
        - Lvl (starts at 1, increases at each subproject)
        - Name
        - Conclusions
        - Type
        - State
        - Uploaded by
        - Clearing Team
- **Expected Result:** All specified columns are present and function as described.

#### Row Colors
- **Test Case ID:** PROJ-LI-AU-005
- **Description:** Verify the row colors based on the number of attachments.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the License Info Table.
    3. Verify the row colors:
        - Red for no attachments
        - Green for 1 attachment
        - Yellow for more than 1 attachment
- **Expected Result:** The row colors are displayed as specified.

#### Release Clearing State
- **Test Case ID:** PROJ-LI-AU-006
- **Description:** Verify that the State column displays the Release's clearing state.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the License Info Table.
- **Expected Result:** The State column displays the Release's clearing state.

#### Attachment Rows
- **Test Case ID:** PROJ-LI-AU-007
- **Description:** Verify the details displayed for each attachment row.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the License Info Table.
    3. Click on an attachment row to expand it.
    4. Verify the presence of the following details:
        - Checkbox if License Info is selected for the attachment
        - Level number
        - If file ends with .rdf and concluded license is enabled, a checkbox for that
        - If used in number of projects else show "Not used in any projects yet" in the Type column
        - Attachment status
        - Uploader name
        - Uploader Department
- **Expected Result:** All specified details are present and function as described.

#### Expanded Attachment Details
- **Test Case ID:** PROJ-LI-AU-008
- **Description:** Verify the details displayed when an attachment is expanded.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the License Info Table.
    3. Click on an attachment row to expand it.
    4. Verify the presence of the following details:
        - Lvl
        - Name of license
        - License text from the CLI
    5. Click on a license name to verify the checkbox behavior.
- **Expected Result:** The specified details are present and function as described. Clicking on a license name enables the checkbox of the attachment, and individual licenses can be excluded.

#### Subprojects
- **Test Case ID:** PROJ-LI-AU-009
- **Description:** Verify the presence of the "Use selection of this subproject" button and the warning next to it. Clicking this button should import the usage for the subproject.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Locate the subproject section.
    3. Click on the "Use selection of this subproject" button.
- **Expected Result:** The button and warning are present. Clicking the button imports the usage for the subproject.

### Download Button

#### Report Generation Options
- **Test Case ID:** PROJ-LI-AU-010
- **Description:** Verify that clicking the "Download" button shows a report generation options popup. Clicking "Download" on the popup triggers the report and also saves the attachment usage of the current page.
- **Steps:**
    1. Navigate to the "Generate License Info" page.
    2. Click on the "Download" button.
    3. Verify the report generation options popup.
    4. Click on the "Download" button in the popup.
- **Expected Result:** The report generation options popup is shown. Clicking "Download" in the popup triggers the report and saves the attachment usage of the current page.
