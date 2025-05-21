---
title: "Preferences Page"
linkTitle: "Preferences Page"
weight: 300
---

## SW360 "Preferences" Page Test Cases

### General Page Behavior

#### Update Settings Button
- **Test Case ID:** PREF-001
- **Description:** Verify the presence of the "Update Settings" button at the top.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Update Settings" button is present.

### E-Mail Notification Preferences Section

#### Enable E-Mail Notifications Checkbox
- **Test Case ID:** PREF-002
- **Description:** Verify the presence of the "Enable E-Mail Notifications" checkbox and its behavior.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the E-Mail Notification Preferences section.
    3. Uncheck the "Enable E-Mail Notifications" checkbox.
- **Expected Result:** The checkbox is present, and unchecking it disables all checkboxes in this section.

#### Individual Checkboxes
- **Test Case ID:** PREF-003
- **Description:** Verify the presence of individual checkboxes for Project, Component, Release, Moderation & Clearing in the form of a Carousel.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the E-Mail Notification Preferences section.
    3. Verify the presence of the following checkboxes:
        - Project
        - Component
        - Release
        - Moderation & Clearing
- **Expected Result:** All specified checkboxes are present and function as described.

### SW360 User Section

#### User Details
- **Test Case ID:** PREF-004
- **Description:** Verify the presence of the specified details in the SW360 User section.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the SW360 User section.
    3. Verify the presence of the following details:
        - Name
        - E-mail (mailto link)
        - Primary Department
        - External Id
        - Primary Department Role
        - Secondary Departments and Roles (unordered list of Department (Bold): Role)
- **Expected Result:** All specified details are present and function as described.

### Rest API Token Section

#### Fields
- **Test Case ID:** PREF-005
- **Description:** Verify the presence of the specified fields in the Rest API Token section.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the Rest API Token section.
    3. Verify the presence of the following fields:
        - Name
        - Authorities (checkbox "Read Access", (if enabled) "Write Access")
        - Expiration Date
        - Token (info hover)
- **Expected Result:** All specified fields are present and function as described.

#### Generate Token Button
- **Test Case ID:** PREF-006
- **Description:** Verify the presence of the "Generate Token" button and its behavior.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the Rest API Token section.
    3. Click on the "Generate Token" button.
- **Expected Result:** The button is present, and clicking it submits a request to generate a new token, which is then displayed in the "Token" field above.

### Token Table

#### Columns
- **Test Case ID:** PREF-007
- **Description:** Verify the presence of the specified columns in the Token table.
- **Steps:**
    1. Navigate to the "Preferences" page.
    2. Locate the Token table.
    3. Verify the presence of the following columns:
        - Token Name
        - Created on
        - Expiration Date
        - Authorities (`[list]`)
        - Action (Revoke Token button)
- **Expected Result:** All specified columns are present and function as described.
