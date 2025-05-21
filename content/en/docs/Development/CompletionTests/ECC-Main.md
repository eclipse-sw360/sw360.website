---
title: "ECC Page"
linkTitle: "ECC Page"
weight: 240
---

## SW360 "ECC Main" Page Test Cases

### General Page Behavior

#### Quick Filter
- **Test Case ID:** ECC-001
- **Description:** Verify the presence of a Quick Filter on the left which updates the ECC Overview table as the user types.
- **Steps:**
    1. Navigate to the "ECC Main" page.
    2. Locate the Quick Filter on the left.
    3. Type in the filter and observe the changes in the ECC Overview table.
- **Expected Result:** The ECC Overview table updates based on the input in the Quick Filter.

### ECC Overview Table

#### Columns
- **Test Case ID:** ECC-002
- **Description:** Verify the presence of the specified columns in the ECC Overview table.
- **Steps:**
    1. Navigate to the "ECC Main" page.
    2. Locate the ECC Overview table.
    3. Verify the presence of the following columns:
        - Status
        - Release name
        - Release version
        - Creator Group
        - ECC Assessor
        - ECC Assessor Group
        - Ecc Assessment Date
- **Expected Result:** All specified columns are present and function as described.

#### Pagination Parameters
- **Test Case ID:** ECC-003
- **Description:** Verify the presence of pagination parameters in the ECC Overview table.
- **Steps:**
    1. Navigate to the "ECC Main" page.
    2. Locate the ECC Overview table.
- **Expected Result:** Pagination parameters are present in the ECC Overview table.
