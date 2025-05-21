---
title: "Create Vulnerability"
linkTitle: "Create Vulnerability"
weight: 260
---

## SW360 "Add Vulnerability" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** VUL-CRT-001
- **Description:** Verify the presence of the "Create Vulnerability" and "Cancel" buttons on top.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Create Vulnerability" and "Cancel" buttons are present.

### Vulnerability Detail Section

#### Fields
- **Test Case ID:** VUL-CRT-002
- **Description:** Verify the presence of the specified fields in the Vulnerability Detail section.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vulnerability Detail section.
    3. Verify the presence of the following fields:
        - External ID (required)
        - Title
        - Description (text area)
        - Priortiy
        - Priority Text
        - Action
        - Legal Notice
        - Cwe ("CWE-" then a textbox)
        - Extended Description
        - CVSS Score (floating numbers)
        - CVSS Date
        - CVSS Time
        - Publish Date
        - Publish Time
        - Last External Update Date
        - Last External Update Time
- **Expected Result:** All specified fields are present and function as described.

### Vulnerability Impact Section

#### Fields
- **Test Case ID:** VUL-CRT-003
- **Description:** Verify the presence of the specified fields in the Vulnerability Impact section.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vulnerability Impact section.
    3. Verify the presence of the following fields:
        - Availability (dropdown)
        - Confidentiality (dropdown)
        - Integrity (dropdown)
- **Expected Result:** All specified fields are present and function as described.

### Vulnerability Access Section

#### Fields
- **Test Case ID:** VUL-CRT-004
- **Description:** Verify the presence of the specified fields in the Vulnerability Access section.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vulnerability Access section.
    3. Verify the presence of the following fields:
        - Authentication (dropdown)
        - Complexity (dropdown)
        - Vecotr (dropdown)
- **Expected Result:** All specified fields are present and function as described.

### CVE References Section

#### Add CVE Reference Button
- **Test Case ID:** VUL-CRT-005
- **Description:** Verify the presence of the "Add CVE Reference" button and the ability to add a row with the specified fields.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the CVE References section.
    3. Click on the "Add CVE Reference" button.
    4. Verify the presence of a row with the following fields:
        - CVE Year (required)
        - CVE Number (required)
        - Delete row button
- **Expected Result:** The "Add CVE Reference" button is present, and a row with the specified fields is added.

### Assigned External Component Ids Section

#### Add Assigned External Component Id Button
- **Test Case ID:** VUL-CRT-006
- **Description:** Verify the presence of the "Add Assigned External Component Id" button and the ability to add a row with the specified field.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Assigned External Component Ids section.
    3. Click on the "Add Assigned External Component Id" button.
    4. Verify the presence of a row with the following field:
        - External Component Id
        - Delete row button
- **Expected Result:** The "Add Assigned External Component Id" button is present, and a row with the specified field is added.

### Vulnerability References Section

#### Add Vulnerability Reference Button
- **Test Case ID:** VUL-CRT-007
- **Description:** Verify the presence of the "Add Vulnerability Reference" button and the ability to add a row with the specified field.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vulnerability References section.
    3. Click on the "Add Vulnerability Reference" button.
    4. Verify the presence of a row with the following field:
        - Reference
        - Delete row button
- **Expected Result:** The "Add Vulnerability Reference" button is present, and a row with the specified field is added.

### Vendor Advisories Section

#### Add Vendor Advisory Button
- **Test Case ID:** VUL-CRT-008
- **Description:** Verify the presence of the "Add Vendor Advisory" button and the ability to add a row with the specified fields.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vendor Advisories section.
    3. Click on the "Add Vendor Advisory" button.
    4. Verify the presence of a row with the following fields:
        - Advisory Vendor (required)
        - Adivsory Name (required)
        - Advisory URL (required)
        - delete row button
- **Expected Result:** The "Add Vendor Advisory" button is present, and a row with the specified fields is added.

### Vulnerability Configuration Section

#### Add Vulnerability Configuration Button
- **Test Case ID:** VUL-CRT-009
- **Description:** Verify the presence of the "Add Vulnerability Configuration" button and the ability to add a row with the specified fields.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Locate the Vulnerability Configuration section.
    3. Click on the "Add Vulnerability Configuration" button.
    4. Verify the presence of a row with the following fields:
        - Configuration Key
        - Configuration Value
        - delete row button
- **Expected Result:** The "Add Vulnerability Configuration" button is present, and a row with the specified fields is added.

### Create Vulnerability Button

#### Vulnerability Creation
- **Test Case ID:** VUL-CRT-010
- **Description:** Verify that clicking on the "Create Vulnerability" button saves the vulnerability and redirects the user to the main vulnerability page with the message "Vulnerability (external ID) added successfully!" displayed.
- **Steps:**
    1. Navigate to the "Add Vulnerability" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create Vulnerability" button.
- **Expected Result:** The vulnerability is saved, the user is redirected to the main vulnerability page, and the message "Vulnerability (external ID) added successfully!" is displayed.
