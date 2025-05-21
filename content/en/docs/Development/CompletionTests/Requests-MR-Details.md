---
title: "Requests - Moderation Request Details"
linkTitle: "Requests - Moderation Request Details"
weight: 320
---

## SW360 "Moderation Request Details" Page Test Cases

### General Page Behavior

#### Assignment Message
- **Test Case ID:** MR-DTL-001
- **Description:** Verify the display of the message "Success: You have assigned yourself to this moderation request" when a user first opens a Moderation Request in Open state and can be a moderator.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page of an Open state request.
    2. Locate the top section of the page.
- **Expected Result:** The message "Success: You have assigned yourself to this moderation request" is displayed.

#### Top Buttons
- **Test Case ID:** MR-DTL-002
- **Description:** Verify the presence of the "Accept Request", "Decline Request", "Postpone Request", "Remove Me from moderators", and "Cancel" buttons on top. Clicking on them should open a popup. If the moderation request is closed, no buttons should be displayed on top.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page of an Open state request.
    2. Locate the top section of the page.
    3. Click on each of the buttons to verify the popup.
    4. Navigate to the "Moderation Request Details" page of a closed request.
- **Expected Result:** The specified buttons are present and function as described for Open state requests. No buttons are displayed for closed requests.

#### Document Name and Type
- **Test Case ID:** MR-DTL-003
- **Description:** Verify the display of the document name and type on the top right.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page.
    2. Locate the top right section of the page.
- **Expected Result:** The document name and type are displayed on the top right.

### Moderation Request Information Section

#### Moderation Request Fields
- **Test Case ID:** MR-DTL-004
- **Description:** Verify the presence of the specified fields in the Moderation Request section.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page.
    2. Locate the Moderation Request Information section.
    3. Verify the presence of the following fields:
        - Requesting user
        - Submitted on
        - Comment on Moderation Request (text area)
- **Expected Result:** All specified fields are present and function as described.

#### Moderation Decision Fields
- **Test Case ID:** MR-DTL-005
- **Description:** Verify the presence of the specified fields in the Moderation Decision section.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page.
    2. Locate the Moderation Request Information section.
    3. Verify the presence of the following fields:
        - Status
        - Moderator
        - Comment on Moderation Decision (text area) (used for Accept/Decline)
- **Expected Result:** All specified fields are present and function as described.

### Proposed Changes Section

#### View Based on Document Type
- **Test Case ID:** MR-DTL-006
- **Description:** Verify that the Proposed Changes section shows a view based on the document type.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page.
    2. Locate the Proposed Changes section.
- **Expected Result:** The Proposed Changes section shows a view based on the document type.

### Current Component Section

#### Display of Component
- **Test Case ID:** MR-DTL-007
- **Description:** Verify that the Current Component section shows the entire component based on the document type.
- **Steps:**
    1. Navigate to the "Moderation Request Details" page.
    2. Locate the Current Component section.
- **Expected Result:** The Current Component section shows the entire component based on the document type.
