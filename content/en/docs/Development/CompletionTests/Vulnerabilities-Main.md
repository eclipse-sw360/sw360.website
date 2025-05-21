---
title: "Vulnerabilities Page"
linkTitle: "Vulnerabilities Page"
weight: 250
---

## SW360 "Main Vulnerabilities" Page Test Cases

### General Page Behavior

#### Quick Filter
- **Test Case ID:** VUL-001
- **Description:** Verify the presence of a Quick Filter on the left which updates the vulnerability table as the user types.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the Quick Filter on the left.
    3. Type in the filter and observe the changes in the vulnerability table.
- **Expected Result:** The vulnerability table updates based on the input in the Quick Filter.

#### Advanced Filter
- **Test Case ID:** VUL-002
- **Description:** Verify the presence of an Advanced Filter on the left with CVE ID and Vulnerable Configuration inputs and a "Filter" button.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the Advanced Filter on the left.
    3. Enter values in the CVE ID and Vulnerable Configuration inputs and click on the "Filter" button.
- **Expected Result:** The vulnerability table filters based on the input in the Advanced Filter.

#### Page Title
- **Test Case ID:** VUL-003
- **Description:** Verify that the page title displays "Vulnerabilities (count of total vulnerabilities)".
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the page title.
- **Expected Result:** The page title displays "Vulnerabilities (count of total vulnerabilities)".

#### Top Buttons
- **Test Case ID:** VUL-004
- **Description:** Verify the presence of the "Add Vulnerability" button and the "Show 200/500/1000/All" dropdown on top.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Add Vulnerability" button and the "Show 200/500/1000/All" dropdown are present.

### Vulnerability Table

#### Columns
- **Test Case ID:** VUL-005
- **Description:** Verify the presence of the specified columns in the vulnerability table.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the vulnerability table.
    3. Verify the presence of the following columns:
        - External ID (clickable to open vulnerability)
        - Title (tooltip of info)
        - Weighting (note: check https://code.siemens.com/sw360/sw360portal/blob/c397e64d48b93b6120681a75ed8c9c4a58eb630d/frontend/sw360-portlet/src/main/resources/META-INF/resources/html/vulnerabilities/view.jsp#L219)
        - Publish Date
        - Last update
        - Actions (edit icon and delete icon) (Clicking on delete should open a confirmation dialog)
- **Expected Result:** All specified columns are present and function as described.

#### Pagination Parameters
- **Test Case ID:** VUL-006
- **Description:** Verify the presence of pagination parameters around the vulnerability table.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Locate the vulnerability table.
- **Expected Result:** Pagination parameters are present around the vulnerability table.
