---
title: "Create License"
linkTitle: "Create License"
weight: 210
---

## SW360 "Create License" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** LIC-CRT-001
- **Description:** Verify the presence of the "Create License" and "Cancel" buttons on top.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Create License" and "Cancel" buttons are present.

### License Tab

#### License Details Section
- **Test Case ID:** LIC-CRT-002
- **Description:** Verify the presence of the specified fields in the License Details section.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the License Details section in the License Tab.
    3. Verify the presence of the following fields:
        - Fullname (required)
        - Shortname (required)
        - License Type (dropdown, dynamic)
        - OSI Approved? (one of (n/a), Yes)
        - FSF Free/Libre? (one of (n/a), Yes)
        - Is checked (checkbox)
        - Note (text area)
- **Expected Result:** All specified fields are present and function as described.

#### License Text Section
- **Test Case ID:** LIC-CRT-003
- **Description:** Verify the presence of a big text area for license text.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the License Text section in the License Tab.
- **Expected Result:** The big text area for license text is present.

### Linked Obligations Tab

#### Add Obligation Button
- **Test Case ID:** LIC-CRT-004
- **Description:** Verify the presence of the "Add Obligation" button on top.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the Linked Obligations Tab.
- **Expected Result:** The "Add Obligation" button is present.

#### Obligations Table
- **Test Case ID:** LIC-CRT-005
- **Description:** Verify the presence of the specified columns in the obligations table.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the Linked Obligations Tab.
    3. Verify the presence of a table with the following columns:
        - Collapse
        - Obligation Title
        - Obligation Type
        - Action (delete icon)
    4. Click on the "Expand" button to reveal the obligation text.
- **Expected Result:** The table with the specified columns is present, and the "Expand" button reveals the obligation text.

#### Add Obligation Popup
- **Test Case ID:** LIC-CRT-006
- **Description:** Verify that clicking on the "Add Obligation" button opens a popup showing obligations which can be added.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Locate the Linked Obligations Tab.
    3. Click on the "Add Obligation" button.
- **Expected Result:** A popup showing obligations which can be added is opened.

### Create License Button

#### License Creation
- **Test Case ID:** LIC-CRT-007
- **Description:** Verify that clicking on the "Create License" button saves the license, shows the message "License created," and navigates the user back to the Main Licenses page.
- **Steps:**
    1. Navigate to the "Create License" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create License" button.
- **Expected Result:** The license is saved, the message "License created" is shown, and the user is navigated back to the Main Licenses page.
