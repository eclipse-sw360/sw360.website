---
title: "Licenses Page"
linkTitle: "Licenses Page"
weight: 200
---

## SW360 "Licenses" Page Test Cases

### General Page Behavior

#### Quick Filter
- **Test Case ID:** LIC-001
- **Description:** Verify the presence of a Quick Filter on the left which allows the user to filter the license table as they type. The filter works for License Shortname and License Fullname.
- **Steps:**
    1. Navigate to the "Licenses" page.
    2. Locate the Quick Filter on the left.
    3. Type in the filter and observe the changes in the license table.
- **Expected Result:** The license table filters based on the input for License Shortname and License Fullname.

#### Top Buttons
- **Test Case ID:** LIC-002
- **Description:** Verify the presence of the "Add License" button and "Export Spreadsheet" button on top.
- **Steps:**
    1. Navigate to the "Licenses" page.
    2. Locate the top section of the page.
- **Expected Result:** The "Add License" button and "Export Spreadsheet" button are present.

### License Table

#### Pagination Parameters
- **Test Case ID:** LIC-003
- **Description:** Verify the presence of pagination parameters in the license table.
- **Steps:**
    1. Navigate to the "Licenses" page.
    2. Locate the license table.
- **Expected Result:** Pagination parameters are present in the license table.

#### Columns
- **Test Case ID:** LIC-004
- **Description:** Verify the presence of the specified columns in the license table.
- **Steps:**
    1. Navigate to the "Licenses" page.
    2. Locate the license table.
    3. Verify the presence of the following columns:
        - License Shortname (clickable link to open license)
        - License Fullname
        - Is checked? (red or green)
        - License Type ("--" if missing)
- **Expected Result:** All specified columns are present and function as described.
