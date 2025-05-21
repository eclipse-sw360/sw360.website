---
title: "License Detail"
linkTitle: "License Detail"
weight: 220
---

## SW360 "License Details" Page Test Cases

### General Page Behavior

#### License Fullname and Status
- **Test Case ID:** LIC-DTL-001
- **Description:** Verify the display of the License Fullname (License Shortname) on top and the status of whether the license is checked or unchecked (green or red).
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The License Fullname and status are displayed as specified.

#### Edit License Button
- **Test Case ID:** LIC-DTL-002
- **Description:** Verify the presence of the "Edit License" button.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Edit License" button is present.

### Details Tab

#### Unchecked License Warning
- **Test Case ID:** LIC-DTL-003
- **Description:** Verify the display of a red warning "This license is UNCHECKED" if the license is unchecked.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the Details Tab.
- **Expected Result:** The red warning is displayed if the license is unchecked.

#### License Details Section
- **Test Case ID:** LIC-DTL-004
- **Description:** Verify the presence of the specified fields in the License Details section.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the License Details section in the Details Tab.
    3. Verify the presence of the following fields:
        - Fullname
        - Shortname
        - Is checked
        - Type
        - OSI Approved? (Yes in green, else red)
        - FSF Free/Libre? (Yes in green, else red)
        - External link for more information (text box with Save button)
        - Note
- **Expected Result:** All specified fields are present and function as described.

### Text Tab

#### License Text Section
- **Test Case ID:** LIC-DTL-005
- **Description:** Verify the presence of the License Text section with the license text in pre-formatted font.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the Text Tab.
- **Expected Result:** The License Text section with the license text in pre-formatted font is present.

### Obligations Tab

#### Edit Whitelist Button
- **Test Case ID:** LIC-DTL-006
- **Description:** Verify the presence of the "Edit Whitelist" button if obligations are linked. Clicking on the button should show the whitelist table.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the Obligations Tab.
    3. Click on the "Edit Whitelist" button.
- **Expected Result:** The "Edit Whitelist" button is present, and clicking on it shows the whitelist table.

#### Obligations Table
- **Test Case ID:** LIC-DTL-007
- **Description:** Verify the presence of the specified columns in the obligations table.
- **Steps:**
    1. Navigate to the "License Details" page.
    2. Locate the Obligations Tab.
    3. Verify the presence of a table with the following columns:
        - Expand (show obligation text)
        - Obligation
        - Obligation Type
        - Further properties
    4. Verify the presence of a search bar on top.
- **Expected Result:** The table with the specified columns is present, and the search bar is functional.

### Change Log Tab

#### Change Log Table
- **Test Case ID:** [PROJ-DTL-021]({{< relref path="Projects-Details.md">}}#toggle-on-top),
  [PROJ-DTL-022]({{< relref path="Projects-Details.md">}}#changelog-table),
  [PROJ-DTL-023]({{< relref path="Projects-Details.md">}}#opening-changelog),
  [PROJ-DTL-024]({{< relref path="Projects-Details.md">}}#basic-info-section),
  [PROJ-DTL-025]({{< relref path="Projects-Details.md">}}#changed-fields-table) and
  [PROJ-DTL-026]({{< relref path="Projects-Details.md">}}#returning-to-list)
