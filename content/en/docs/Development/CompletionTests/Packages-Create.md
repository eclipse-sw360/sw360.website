---
title: "Create Packages"
linkTitle: "Create Packages"
weight: 170
---

## SW360 "Create Packages" Page Test Cases

### General Page Behavior

#### Add Package Button
- **Test Case ID:** PKGS-CRT-001
- **Description:** Verify that clicking on the "Add Package" button opens a form to create a new package.
- **Steps:**
    1. Navigate to the Main Packages page.
    2. Click on the "Add Package" button.
- **Expected Result:** A form to create a new package is opened.

### Summary Tab

#### Information Fields
- **Test Case ID:** PKGS-CRT-002
- **Description:** Verify the presence of the specified information fields in the Summary Tab.
- **Steps:**
    1. Navigate to the "Create Packages" page.
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


### Create Package Button

#### Package Creation
- **Test Case ID:** PKGS-CRT-003
- **Description:** Verify that upon clicking the "Create Package" button, the package is created, and the user is redirected to the "Edit Package" page of the created package.
- **Steps:**
    1. Navigate to the "Create Packages" page.
    2. Fill in the required fields and any additional information.
    3. Click on the "Create Package" button.
- **Expected Result:** The package is created, and the user is redirected to the "Edit Package" page of the created package.
