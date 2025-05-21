---
title: "Edit Package"
linkTitle: "Edit Package"
weight: 180
---

## SW360 "Edit Packages" Page Test Cases

### General Page Behavior

#### Top Buttons
- **Test Case ID:** PKGS-EDIT-001
- **Description:** Verify the presence of the "Update Package", "Delete Package" (disabled if used in a project), and "Cancel" buttons on top.
- **Steps:**
    1. Navigate to the "Edit Packages" page.
    2. Locate the top section of the page.
- **Expected Result:** The specified buttons are present.

### Summary Tab

#### Information Fields
- **Test Case ID:** PKGS-EDIT-002
- **Description:** Verify the presence of the specified information fields in the Summary Tab.
- **Steps:**
    1. Navigate to the "Edit Packages" page.
    2. Locate the Summary Tab.
    3. Verify the presence of the following fields:
        - Name (required)
        - Version (required)
        - Package Type (required) (one of CDX package type) (info hover beneath)
        - PURL (required)
        - Package Manager (required) (readonly)
        - VCS
        - Main licenses
        - Release (click to open popup with clear button)
        - Homepage URL
        - Created on (readonly)
        - Created by (readonly)
        - Modified By (readonly)
        - Description (text area)
- **Expected Result:** All specified fields are present and function as described.

### Update Package Button

#### Package Update
- **Test Case ID:** PKGS-EDIT-003
- **Description:** Verify that clicking the "Update Package" button saves the changes and takes the user to the "Package Details" page of the current package.
- **Steps:**
    1. Navigate to the "Edit Packages" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Update Package" button.
- **Expected Result:** The changes are saved, and the user is redirected to the "Package Details" page of the current package.

### Cancel Button

#### Discard Changes
- **Test Case ID:** PKGS-EDIT-004
- **Description:** Verify that clicking the "Cancel" button discards the changes and takes the user to the "Package Details" page of the current package.
- **Steps:**
    1. Navigate to the "Edit Packages" page.
    2. Make changes to the fields.
    3. Click on the "Cancel" button.
- **Expected Result:** The changes are discarded, and the user is redirected to the "Package Details" page of the current package.
