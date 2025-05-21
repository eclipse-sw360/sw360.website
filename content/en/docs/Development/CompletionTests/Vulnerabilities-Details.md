---
title: "Vulnerability Detail"
linkTitle: "Vulnerability Detail"
weight: 270
---

## SW360 "Vulnerability Details" Page Test Cases

### General Page Behavior

#### Opening Vulnerability Detail
- **Test Case ID:** VUL-DTL-001
- **Description:** Verify that the vulnerability detail can be opened with its external ID.
- **Steps:**
    1. Navigate to the "Main Vulnerabilities" page.
    2. Click on the External ID of a vulnerability to open its detail.
- **Expected Result:** The vulnerability detail page is opened with the specified external ID.

#### Page Title
- **Test Case ID:** VUL-DTL-002
- **Description:** Verify that the vulnerability title is displayed in the page title.
- **Steps:**
    1. Navigate to the "Vulnerability Details" page.
    2. Locate the page title.
- **Expected Result:** The vulnerability title is displayed in the page title.

### Summary Tab

#### Vulnerability Summary Section
- **Test Case ID:** VUL-DTL-003
- **Description:** Verify the presence of the specified fields in the Vulnerability Summary section.
- **Steps:**
    1. Navigate to the "Vulnerability Details" page.
    2. Locate the Vulnerability Summary section in the Summary Tab.
    3. Verify the presence of the following fields:
        - Title
        - Description
        - External Id
        - Publish Date
        - Last update
        - Priority
        - Priority text
        - Action
        - Impact (if available, list of integrity, availability, confidentiality)
        - Legal Notice
        - Assigned external component ids (comma-separated list)
        - CVE references (comma-separated list)
        - Vendor advisories (list of vendor, name, url)
        - Vulnerablity scoring CVSS (score, date)
        - Access (list of complexity, vector, authentication)
        - Common weakness enumeration (CWE with link)
        - Vulnerable configurations (list of key-value pairs)
- **Expected Result:** All specified fields are present and function as described.

#### Releases Table
- **Test Case ID:** VUL-DTL-004
- **Description:** Verify the presence of the table of releases following the "Vulnerability Title is present in the following releases" title.
- **Steps:**
    1. Navigate to the "Vulnerability Details" page.
    2. Locate the table of releases in the Summary Tab.
    3. Verify the presence of the following columns:
        - Release (link to release)
        - CPE-ID
        - Release date (not creation date)
- **Expected Result:** The table with the specified columns is present.

### Metadata Tab

#### Vulnerability Metadata Section
- **Test Case ID:** VUL-DTL-005
- **Description:** Verify the display of the Vulnerability Metadata section if `cveFurtherMetaDataPerSource` is present in the object.
- **Steps:**
    1. Navigate to the "Vulnerability Details" page.
    2. Locate the Metadata Tab.
    3. Verify the presence of an unordered list of Key (bold): Value (another unordered list of Key (bold) Value) if `cveFurtherMetaDataPerSource` is present in the object.
- **Expected Result:** The specified unordered list is displayed if `cveFurtherMetaDataPerSource` is present.

### References Tab

#### Vulnerability References
- **Test Case ID:** VUL-DTL-006
- **Description:** Verify the presence of an unordered list of clickable URLs in the Vulnerability References section.
- **Steps:**
    1. Navigate to the "Vulnerability Details" page.
    2. Locate the References Tab.
    3. Verify the presence of an unordered list of clickable URLs.
- **Expected Result:** The unordered list of clickable URLs is present.
