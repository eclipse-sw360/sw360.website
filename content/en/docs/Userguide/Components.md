---
linkTitle: "Components"
title: "Components"
Weight: 4
---

# 2.0 Components

## 2.01 Introduction

The components page displays the list of components and releases that are available in SW360. A component is a list of releases with metadata. A release is a specific version of a component. 

To open a component page, click **Components** tab from the main menu. 
You can find a particular component with Advanced Search, you can also add and edit components in this page.  

{{< figure src="/sw360/img/ImagesBasic/Componentpage/ComponentPage.png" >}}

|Sl.No.|Description|
|:----:|:----------|
|1| [Advanced Search](#203-component-search)|
|2|[Add Component](#204-add-component)|
|3| [Import SPDX BOM](#207-import-spdx-bom) |
|4| [Export Spreadsheet](#208-export-spreadsheet)|
|5| [Component List](#202-component-list) |

## 2.02 Component List

On the component page, you can view all the components that are relevant to you. The components are listed with the following information:
* **Vendor**: Vendor is organization which is selling the component or the community which is hosting the component. 
* **Component Name**: All components are listed by their names. 
* **Main Licenses**: The list of main licenses available for a component are displayed. 
* **Component Type**: Lists all the components by their type. For more information on component types, refer to [A. General Info](#a-general-information).
* **Actions**: You can perform the following actions for a component:

    | Action |Description |
    |:--:|:--|
    |{{< figure src="/sw360/img/ImagesBasic/Edit_Pen.png" >}} | To edit a component |
    |{{< figure src="/sw360/img/ImagesBasic/Delete_Trash.png" >}} | To delete the component from SW360. |
  
**NOTE: CLICK ON {{< figure src="/sw360/img/ImagesBasic/SortIcon.png" >}} TO SORT LICENSE INFORMATION ALPHABETICALLY.**

## 2.03 Component Search 

**Advanced Search** dialogue box is used to search for a particular component. 

1. Search the component with **Component Name** and **Categories**.
2. Search the component with **Component Type**. Select the component type from the drop-down list. For more information on the component types, refer to [A. General Information](#a-general-information).
3. Search components with their coding **Languages**, **Software Platforms**, **Operating Systems**, **Vendors** and **Main Licenses**.
4. Search components with **Created by (Email)**.
5. You can use **Created on** field to search for the components created on specific dates or specific time frames.

## 2.04 Add Component

To add a new component, click **Add Component** from the component page, this will redirect you to another page where you can add component summary information. 

### **1. Summary**
#### **A. General Information**

```NOTE: FIELDS MARKED "*" ARE MANDATORY.```
![](/sw360/img/ImagesBasic/Componentpage/Component_General_Info.png)

1. Enter the **Name** of the component you want to create.</BR>
   ```NOTE: MAKE SURE THAT THERE ARE NO DUPLICATES.```</BR>
2. Select the **Component Type** from the drop-down list.
    - OSS: Open-Source Software
    - COTS: Commercial off-the-shelf
    - Internal: Internally used
    - Inner Source: OSS within a particular organization
    - Services: Developed as a service 
    - Freeware: Software that is available free of cost
    - Code snippet: A small code which shows how to accomplish a specific task 
3. The field **Created by** is set automatically to the creator/owner of the component.
4. Click on **Default Vendor** field.
    * This opens a dialogue box, use the type field to search for the vendors.
    * Select the vendors
    * Click on **Select Vendor**.
5. When you start typing in the **Categories** field, a list of categories that match are displayed to choose from.
6. Enter the **Homepage URL**, this is the web address for your component.
7. Enter a **Short Description** for your component.
8. Enter the **Blog URL**, this is the web address for the blog of your component. 
9.  **Modified on** date will be set automatically.
10. Enter the **Wiki URL**, this is web address for the wiki page of your component.
11. **Modified by** will be set automatically. 
12. Enter the **Mailing List URL**, this is the web address of the mailing list of your component.

#### **B. Roles**

![](/sw360/img/ImagesBasic/Componentpage/Component_Roles.png)

1. **Component owner** holds the component. Click on the field to select **Component Owner**.
    * This opens a dialogue box, use the type field to search for the Component Owner.
    * Select the users
    * Click on **Select Users**.

   ![](/sw360/img/ImagesBasic/Addproject_5.png)

2. Select a country from the list to assign as **Owner Country**.
3. Enter the **Owner Accounting Unit**.
4. **Moderator** is the user responsible for the component. Click on the field to select moderators. 
    * This opens a dialogue box, use the type field to search for the moderator.
    * Select the users
    * Click on **Select Users**.

``` NOTE: ALL CLEARING EXPERTS, CLEARING ADMINS AND SW360 ADMINS ARE MODERATORS BY DEFAULT.```
1. Enter the **Owner Billing Group**.


#### **C. Additional Roles**

To assign more roles to your project, use **Click to Add Additional Roles**.

![](/sw360/img/ImagesBasic/additionalroles1.png)

1. Select the type of **role** from the drop-down list.
   * Committer
   * Contributor
   * Expert
2. Enter **Email address** of the responsible personnel. To add multiple additional roles, repeat the same
procedure.

   ![](/sw360/img/ImagesBasic/Componentpage/Component_Additional_Role2.png)


3. To delete an additional role, click on ![](/sw360/img/ImagesBasic/Delete_Trash.png).


#### **D. External Ids**

For more information on how to add an **External ID** for your component, refer to [E. External Ids](Project.md/#e-external-ids).

#### **E. Additional Data**

For more information on how to add an **Additional Data** for your component, refer to [F. Additional Data](Project.md/#f-additional-data).
 
After all the summary information is filled click on **Create Component**, which redirects you to another page where you can add more component information. Following are the two new sections to be filled:
  * **Releases**
  * **Attachments**

### **2. Releases**

A release is a specific version of a component. To add Release information for your component:

1. Click on **Releases**.
   
   ![](/sw360/img/ImagesBasic/Componentpage/Componentreleases.png)

2. Then click on **Add Releases**. You will be redirected to another page to add more information about the release you want to create. Following are the two sections where you must enter information</br>
    * **Summary**
    * **Linked Releases**

#### **A. Summary**

```NOTE: FIELDS MARKED "*" ARE MANDATORY.```

![](/sw360/img/ImagesBasic/Componentpage/Create_Release1.png)

1. Click on the field to select the **Vendor** for your component. This opens a dialogue box, search and select the vendor and click on **Select Vendor**.
2. Enter the **Programming Languages** used for the release.
3. **Name** for the release will be auto generated from the name given to the component.
4. Enter the **Operating Systems** used for the release.
5. Enter the **Version** for the release.
6. Enter the **CPE (Common Platform Enumeration) ID** for the release.

![](/sw360/img/ImagesBasic/Componentpage/Create_Release2.png)

7. Enter the **Software Platforms** for the release.
8. Click on the field **Other License** to set other license information for the release. This opens a dialogue box, search and select the licenses and click on **Select Licenses**.
9. Set **Release Date**.
10. Enter the **Source Code Download URL**. This is the web address from where source code of the release can be downloaded.
11. Click on the field **Main License** to set other license information for the release. This opens a dialogue box, search and select the licenses and click on **Select Licenses**.
12. Enter **Binary Download URL**. This is the web address from where binary of the release can be downloaded.
13. **Clearing state** will be set to "new" by default. 
14. Select the value for the **Release Mainline State** from the drop-down list.
    * Open: No license clearing
    * Mainline: Permissive license with no specific obligations
    * Specific: Permissive license with additional obligations with standard obligations
    * Phaseout: Not used anymore
    * Denied: Not to be used because of a specific reason
15. **Created on** is set automatically.

    ![](/sw360/img/ImagesBasic/Componentpage/Create_Release3.png)

16. **Created by** is set automatically.
17. **Modified on** is set automatically.
18. Click on the field to select **Contributors**. This opens a dialogue box, search and select the contributors and click on **Select Users**.
19. **Modified by** is set automatically.
20. **Moderator** is the user responsible for the release. Click on the field to select moderators. 
    * This opens a dialogue box, use the type field to search for the moderator.
    * Select the users
    * Click on **Select Users**.

**Additional Roles**, refer to [3. Additional Roles](#3-additional-roles).

**External Ids**, refer to [4. External Ids](#4-external-ids).

**Additional Data**, refer to [5. Additional Data](#5-additional-data).

**Release Repository**

You can add a release repository URL for your release. To add a release repository: 

1. Select the **Repository Type** from the drop-down list.
2. Enter the **Repository URL**.
   
   ![](/sw360/img/ImagesBasic/Componentpage/Releaserepository.png)</br>

#### **B. Linked Releases**

To add linked releases to your release, click on linked releases. For more information, refer to [B. Linking Releases](Project.md/#b-linking-releases).

Click on **Create Release** to add more information for this release.

#### **C. Clearing Details**

Clearing details contains important information that are required for the license clearing activities. This information is useful for the reuse of license clearing results.
To add clearing information to your release, click on **Clearing Details**.

![](/sw360/img/ImagesBasic/Componentpage/Release_Clearing_Details.png)


* Check the boxes for all applicable clearing details.
* Enter the applicable data for **Scanned** and  **Clearing Standard**. For e.g., date or specific version of your License Scanner.
* Enter **External URL** for the release.
* Add **Comments**. 

**Request Information**

![](/sw360/img/ImagesBasic/Componentpage/Release_Clearing_Details2.png)

To request more information regarding the release, follow the procedure:

* Enter **Request ID** and **Additional request Info**.
* Set **Evaluation Start** and **Evaluation End** date.

**Supplemental Information**

![](/sw360/img/ImagesBasic/Componentpage/Release_Clearing_Details3.png)

You can enter internal supplier ID and number of security vulnerabilities for your release. To add this information.

* Enter **External Supplier Id** and the count of **Vulnerabilities**.
  
#### **D. ECC Details** 

```NOTE: ECC DETAILS ARE SET AUTOMATICALLY FOR OSS RELEASES.```

![](/sw360/img/ImagesBasic/Componentpage/Release_ECC_Details.png)


To enter ECC details for a release click on **ECC Details**.

* Select the **ECC Status** from the drop-down list.
    * Open
    * In progress
    * Approved
    * Rejected
* Add **ECC Comment**, if required.
* Enter **Ausfuhrliste**, this is a German ECC number.
* Enter **ECCN** and **Material Index Number**.
* **Assessor Contact Person**, **Assessor Department** and **Assessment date** will be set automatically.

#### **E. Attachments**

You can add or modify the attachments to your release. To add attachments, click on **Attachments** on the left. For more information on how to add attachments to the release, refer to [1.06 Edit project](Project.md/#106-edit-project).

##

After entering all the release information, click on **Update Release**.

To delete the release, click on **Delete Release**.

If you do not want to create a release, click on **Cancel**.


## 2.05 Edit Component

1. Search for the components you want to edit or navigate from the component list.
2. Click on ![](/sw360/img/ImagesBasic/Edit_Pen.png) from the actions column. You can also edit a component by clicking on the component and then clicking on **Edit Component**.
3. You can view summary, releases, and attachment information of the component. 
4. Click on **Summary** to edit component summary information. For more information on the fields to edit, refer to [1. Summary](#1-summary).
5. Click on **Releases** to view all the releases that are linked to the component. If you want to add more releases to the component click on **Add Releases** at the bottom of the list. For more information on how to add a release, refer to [2. Releases](#2-releases).
6. Click on **Attachments** to view all the attachments that are linked to the component. If you want to add more attachments to the components, refer to paragraph 4 of [1.06 Edit project](Project.md/#106-edit-project). 
7. To update the new component information, click on **Update Component**.
8. To delete the component, click on **Delete Component**.
9. If you do not want to edit the component, click on **Cancel**.


## 2.06 View Component

To open a view mode for a component:

1. Search for the components you want to edit or navigate from the component list. 
2. Click on the component name.
3. You are now in view mode of the component, and you can view all the details of the components like summary, release overview, attachments, vulnerabilities and change logs.
4. You can edit a component, Merge a component, Split a component, Subscribe to a component in this mode.
   
### **A. Merge**

This functionality is used when there is a duplication of components, and this functionality helps us to combine all the duplicates into one single component.
To merge a component with another, click on **Merge**. This action will redirect you to another page where you can:

1. Choose the from the list of components that should be merged into the current one.
2. Merge the data from the source into the target component.
3. Check the merged component and confirm the merge.

### **B. Split**

This functionality is used when we want to copy the information from a component. This is a shortcut to create a component and change aspects like version or release instead of creating a new one entirely.

To Split a component, click on **Split**. This action will redirect you to another page where you can:

1. Choose a target component into which the current component needs to split.
2. Split the data from current component to the target component.
3. Check the split version of the component and confirm the split.

### **C. Subscribe**

You can **Subscribe** to a component to get notified with emails when any changes are made to the component.

To not get notified for a particular component, click **Unsubscribe**. 

### **D. View Component Information**

You can view component information by navigating the navigation tree.

1. To view component summary, click on **Summary**. To edit summary information for the component, refer to [2.05 Edit Component](#205-edit-component).
2. Click on **Release Overview** to view all the releases for the component. To edit details for any of the linked releases click on ![](/sw360/img/ImagesBasic/Edit_Pen.png)
   from the actions column, this will redirect you to a release view page where you can view the following:
   * Release Summary
   * Linked Releases
   * Clearing Details
   * ECC details
   * Attachments
   * Vulnerabilities
   * Change Log
  
For more information on these sections, refer to [2. Releases](#2-releases).

#### **Clearing Details**

You can view the following clearing information for the release in view mode: 
* SPDX Attachments
* Assessment Summary info
  
**SPDX Attachments**

SPDX attachments are the clearing reports which are in XML formats. You will need an approved clearing report to use this release.

![](/sw360/img/ImagesBasic/Componentpage/Component_SPDX_Attachments_1.png)

* Click on **Show license info** to view main license Ids and Other license ids.

![](/sw360/img/ImagesBasic/Componentpage/ComponentSPDXattachment2.png)

* If you want to add this data to the current release, click on **Add data to this release**.
  
**Assessment Summary Info**

You can view if the clearing expert has added any summary in the clearing report.

* To view the summary, click on **Show Assessment Summary info**.
* If there are multiple approved releases, this section will display text "**multiple approved CLI found in release**".

#### **Vulnerabilities**

All the vulnerabilities that are linked to the release/component are listed in the vulnerability section.

![](/sw360/img/ImagesBasic/Componentpage/Component_Vulnerability.png)
 
1. Click on **Vulnerability** on the left to view all the linked vulnerabilities for this release/component.
2. You can sort the vulnerabilities by their external ids, priority, matched by, title, verification and actions.
3. To view more information on the vulnerability, click on the external id of the vulnerability. You will be redirected to another page with all the information about the selected vulnerability.
 
#### **Change Log**

You can see all the changes that are done for the release/component in change log section.

![](/sw360/img/ImagesBasic/Componentpage/Component_ChangeLog.png)

1. To view all the changes done for the release click on **Change Log**.
2. You can now view change date, change log id, change type and user.
3. Click on ![](/sw360/img/ImagesBasic/Componentpage/Changelog1.png) to view all the changes done for a change log id.
4. Click on ![](/sw360/img/ImagesBasic/Componentpage/Changelog2.png) to view the moderation request details for a change log id.
   

## 2.07 Import SPDX BOM

For more information on importing SBOM, refer to [1.05 Import SBOM](1.ProjectPage.md/#105-import-sbom).

## 2.08 Export Spreadsheet

For more information on exporting spreadsheet, refer to [1.13 Export Spreadsheet](1.ProjectPage.md/#113-export-spreadsheet).