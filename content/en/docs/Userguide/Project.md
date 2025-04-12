---
linkTitle: "Project"
title: "Project"
Weight: 3
---

# 1.0 Project Page

## 1.01 Introduction

Navigate to your project overview by clicking the menu item Projects. Here you can find the list of projects with description and other related details. On the left side of project list you can find a advanced filters to filter out specific project.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/Projectpage.png" >}}

|Sl.No.|Description|
|:----:|:----------|
|1| [Advanced Search](#103-project-search)|
|2|[Add Project](#104-add-project)|
|3| [Import SPDX BOM](#105-import-sbom) |
|4| [Export Spreadsheet](#113-export-spreadsheet)|
|5| [Project List](#102-project-list) |

## 1.02 Project List
The Project List lists all the relevant projects with the following information:

* **Project name**: All the projects are listed with their names.
* **Description**: The description for the project is displayed here.
* **Project responsible**: The email address of the person responsible for the project is displayed.
* **State**: Displays the state of the project and clearing requests. The status for PS and CS is indicated by colors.

    | Color | Project State (PS) | Project Clearing State (CS) |
    |-----:|:------------------|:------------------|
    |<span style="color:#68C17C"> **Green** </span> | Active |Closed |
    |<span style="color:#FFD351"> **Yellow** </span> |Not Applicable | In-progress |
    |<span style="color:#E6717C"> **Red** </span> | Open | Open |
    |<span style="color:#DEE2E6"> **Grey** </span> | Phase out/ Unknown |Not Applicable |

* **License Clearing** displays the clearing states for releases for the project including sub projects.
* **Actions**: you can perform the following actions for a project:

    | Action | Description </span>  |
    |:--:|:--                                                                                           |
    |{{< figure src="/sw360/img/ImagesBasic/Project_Page/Edit_Pen.png" >}}| To edit a Project           |
    |{{< figure src="/sw360/img/ImagesBasic/Project_Page/ClearingRequest.png" >}} | To create clearing request the OSS clearing team    |
    |{{< figure src="/sw360/img/ImagesBasic/Project_Page/Copy_Duplicate.png" >}}| To duplicate current version of existing project. This action will also duplicate all the linked projects, releases along with the general information and is used to create different versions of the project.|
    |{{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}| To delete the project from SW360.                     |

**NOTE: CLICK ON {{< figure src="/sw360/img/ImagesBasic/Project_Page/SortIcon.png" >}} TO SORT LICENSE INFORMATION ALPHABETICALLY.**

## 1.03 Project Search

**Advanced search** dialogue box allows you to search for a particular project. To search for a project follow the procedure:

1. Enter the **Project name** and **Version** of the project that you want to search.
2. Select the **Project Type** from the drop-down list. For more information regarding the project type, refer to paragraph 4. of [General Information](#a-general-information).
3. Search the project by **Project Responsible** email.
4. Search projects by their **Group**, select the group from the drop-down list.</br>```NOTE: BY DEFAULT, THE SEARCH RETURNS ONLY THE RESULTS OF YOUR GROUP. HOWEVER, YOU CAN ALSO SELECT THE GROUPS FROM THE DROP-DOWN LIST.```
5. Search projects by their project **State**, select the options available from the drop-down list. For more information regarding project state, refer to [1.02 Project List](#102-project-list).
6. You can search the projects by their **Clearing State**, select the options available from the drop-down list. For more information regarding project state, refer to [1.02 Project List](#102-project-list).
7. You can search projects by their **Tags**. If there are multiple tags that you want to search, use a comma to separate.
8. You can search projects by **Additional Data**.  

## 1.04 Add Project

To add a new project, click on the **Add Project** on the project page, this redirects you to another page that allows you to add project information add project information for the project you want to create. Following are the three sections where you must enter information:

* **Summary**
* **Administration**
* **Linked Releases and Projects**

### **1.** **Summary**

#### **A.** **General Information**

```NOTE: FIELDS MARKED "*" ARE MANDATORY```

{{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectGeneralInfo%20(1).png" >}}

1. Enter the **Name** of the project you want to create.
2. The field **Created by** is set automatically to the creator/owner of the project.
3. **Version** of a project indicates there are new changes compared to the previous version of the project. Enter the version for your project as required.
4. Select the **Project Type** from the drop-down list.
    * Customer: Delivered to the customer
    * Internal: Internally used but can also be used in other projects as a sub-project
    * Product: Developed as a product and delivered to the customer
    * Services: Developed as a service and delivered to the customer
    * Inner Source: OSS within a particular organization

5. **Project Visibility** describes if the project is visible to all or only selected personnel. The default is set to "everyone", you can select the project visibility from the drop-down list.
    * Private: Only visible to creator or admin
    * Me and Moderators: Visible to creator, moderators and admins
    * Group and Moderators: Visible to all users of the same group and the moderators
    * Everyone: All logged in users

6. **Tags** are words assigned to a project that assist in quick searching. You can create a tag by assigning a word to your project.
7. Check or uncheck the following fields as required:
    * **Enable Security Vulnerability Monitoring** (activated only if security responsible are added), refer to [C. Roles](#c-roles).
    * **Do not create monitoring list**, but use from the external id, refer to [E. External IDs](#e-external-ids).
    * **Enable Displaying Vulnerabilities** if you want the vulnerabilities to be visible.

8. **Modified on** date will be set automatically on creating the project.
9. **Description**: You can enter details of your project.
10. **Modified by** will be set automatically.
11. Select the **Domain** for your project from the drop-down list.
    * Application software
    * Documentation
    * Embedded Software
    * Hardware
    * Test and diagnostics
12. Click on the field to select the **Vendor** for your project.
     * This opens a dialogue box, use the type field to search for the vendors.
     * Select the vendors
     * Click on **Add Vendor**.

#### **B. External URLs**

Click on **Click to add row to external URLs** to add URLs of your project.</br>
    {{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectExternalURL1.png" >}}

1. Select **External URL Key** from the drop-down list.
    * Homepage: Link for homepage
    * Wiki page: Link for wiki page
    * Clearing:
2. Enter **External URL Value**. It is the web address for the above mentioned external URL key. To add multiple external URLs, repeat the same procedure.</br>
    {{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectExternalURL2.png" >}}

3. To delete an external URL, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

#### **C. Roles**

{{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectRoles.png" >}}

1. **Group** is the department you/project owner belongs to. Click on the group field to select a **Group** for your project.
     * This opens a dialogue box, use the type field to search for the group.
     * Select the group.
     * Click on **Select**

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Addproject4.png" >}}

2. Enter the **Owners Accounting Unit**.  

3. Project manager is the user who manages the project. Click on the field to select **Project Manager**.
     * This opens a dialogue box, use the type field to search for the Project Manager.
     * Select the Users.
     * Click on **Select Users**.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Addproject_5.png" >}}

4. Enter the **Owners Billing Group**.
5. **Project Owner** holds the project. Click on the field to select **Project Owner**.
     * This opens a dialogue box, use the type field to search for the Project Owner.
     * Select the Users.
     * Click on **Select Users**.
6. Select the **Owner Country** from the drop-down list.
7. **Security responsible** is the list of users responsible for the security of the project. Click on the field to select **Security responsible**.  
     * This opens a dialogue box, use the type field to search for the Security responsible.
     * Select the Users
     * Click on **Select Users**.
8. Click on the field to select **Lead Architect**.
     * This opens a dialogue box, use the type field to search for the Lead Architect.
     * Select the Users.
     * Click on **Select Users**.
9. **Moderator** is the user responsible for the project. Click on the field to select moderators.
     * This opens a dialogue box, use the type field to search for the Moderators.
     * Select the Users.
     * Click on **Select Users**.
10. Click on the field to select **Contributors**.
     * This opens a dialogue box, use the type field to search for the Contributors.
     * Select the Users.
     * Click on **Select Users**.

#### **D. Additional Roles**

To assign more roles to your project, use **Click to Add Additional Roles**.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/additionalroles1.png" >}}

1. Select the type of **Role** from the drop-down list.
   * Stakeholder
   * Analyst
   * Contributor
   * Accountant
   * End user
   * Quality manager
   * Test Manager
   * Technical writer
   * Key user
2. Enter **Email address** of the responsible personnel. To add multiple additional roles, repeat the same procedure.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/additionalroles2.png" >}}

3. To delete an additional role, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

#### **E. External Ids**

Click on **Click to add row to External Ids** to add external Ids to your project.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/Project_external_ID_1.png" >}}

1. Click on field to enter **External Id Key** and select from the drop-down list.
2. Enter **External Id Value**. To add multiple external Ids, repeat the same procedure.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/Project_external_ID_2.png" >}}

1. To delete an External Id, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

#### **F. Additional Data**

You can add data keys and corresponding data values for your project.

To add more additional data keys, click on **Click to add rows to additional data**.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/Additional_data_1.png" >}}

1. Enter **additional data key**.
2. Enter **additional data value**. To add multiple additional data, repeat the same procedure.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Additional_data_2.png" >}}.

3. To delete an additional data, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

### **2.** **Administration**</br>
Administration section contains license clearing and lifecycle information of the project. To edit these fields, click on "Administration", use navigation section. </br>

{{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectAdministration.png" >}}

#### **A.** **Clearing information**

{{< figure src="/sw360/img/ImagesBasic/Project_Page/Clearing_Information.png" >}}

To add clearing information for your project:

1. Select the values for **Project Clearing State** from the drop-down list.
    * Open Project
    * In progress
    * Closed
2. Clearing team is responsible for project clearing. To assign a clearing team, select the values for **Clearing team** from the drop-down list.
3. Pre-evaluation is important for the project development to understand the status of the license and estimate the effort for clearing activities. Set **Deadline for pre-evaluation** date.
4. Following information should be entered manually:
    * **Clearing summary**: Overview of the clearing for the project management.
    * **Special risk open source software**: Risks which occur out from usage of specific OSS components.
    * **General risk 3rd party software**: General risk which occur always from using OSS and commercial SW like for e.g., patent infringements.
    * **Special risk 3rd party software**: Specific risks which occur by using specific projects, including commercial projects.
    * **Sales and delivery channels**: To know when the software will be delivered via resellers as a reseller license has to be procured and to decide how to fulfill the obligations of the licenses.  
    * **Remarks and additional requirements**:  Any additional relevant requirement.

    ```NOTE: THE ABOVE INFORMATION IS NECESSARY FOR PROJECT MANAGEMENT TO UNDERSTAND THE STATUS OF THE LICENSE AND ESTIMATE THE EFFORT FOR CLEARING ACTIVITIES.```

#### **B.** **Lifecycle information**

{{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectLifecycle.png" >}}

To add lifecycle information for your project:

1. Select the values for **Project state** from the drop-down list.
   * Active
   * Phase-out
   * Unknown
2. Set **System test begin** and **System test end** dates. System test begin date can be used in licensing and risk perspective. System test end date is the latest date for component releases.
3. Set  **Delivery start** and **Phase out** dates. After the phase out date, maintenance is not required for the project.

   ```NOTE: LICENSE CLEARING FOR THE PROJECT MUST BE FINISHED BEFORE THE PROJECT DELIVERY DATE.```

#### **C.** **License Info Header**

The license info header can be set as a default header. However, you can edit this field as required.

### **3.** **Linked Releases and Projects**

You can link other projects and releases to the project that you are adding. Click on **Linked Releases and Projects**, use navigation section.

{{< figure src="/sw360/img/ImagesBasic/Project_Page/ProjectLinkedreleasesandprojects.png" >}}

#### **A.** **Linking Projects**

To add existing projects as a sub-project:

1. Click on **Add Projects**, this action opens a dialogue box.

   {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linked-projects_1.png" >}}

2. Search and select the projects which you would like to link.
3. Click on **Link Projects**.  

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linked-projects_2.png" >}}

4. After the project is linked, you can select the **Project Relation** for your sub-project from the drop-down list.
   * Sub-project
   * Duplicate
   * Unknown
   * Related
5. Check or uncheck **Enable SVM** as required.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linked-projects_3.png" >}}

6. To link multiple projects, repeat the same procedure.
7. To delete a linked project, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

#### **B.** **Linking releases**

To add releases to your project:

1. Click on **Add Releases**, this action opens a dialogue box.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Link_release_1.png" >}}

2. **Search** for the releases which you want to link or click on **Releases of linked projects** to view all the releases which are linked to the project.
3. Select all the releases which you want to link and click on **Link releases**.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Link_release_2.png" >}}

4. After the release is linked, you can select the value for the **Release relation** from the drop-down list.
   * Unknown
   * Contained
   * Related
   * Dynamically linked
   * Statically linked
   * Side by side
   * Standalone
   * Internal Use
   * Optional
   * To be replaced
   * Code snippet
5. Select the value for the **Release Mainline State** from the drop-down list.
   * Open
   * Mainline
   * Specific
   * Phaseout
   * Denied
6. Add **Comments**, if required.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Link_release_3.png" >}}

7. To link multiple releases/components, repeat the same procedure.
8. To delete a linked release, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.

After all the information for the new project is filled out. Click on "**Create Project**" at the top.

If you do not want to create a project on any point of time, click on "**Cancel**" at the top.

## 1.05 Import SBOM

SPDX is a common format for communicating compliance information or list of components across all suppliers. Importing an SBOM will create a project/component. To import a SBOM:

1. Click on **Import SBOM** on the project page. This will open a dialogue box for you to upload the Bill Of Materials (BOM).
2. Drag and drop the file from your local system to the dialogue box or click on **Browse File** and select the file you want to import.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/ImportSBOM.png" >}}

    ```NOTE: ONLY SPDX RDF/XML FILES WITH UNIQUE DESCRIBED TOP LEVEL NODE ARE SUPPORTED.```</br>
3. After uploading is done SW360 checks for duplicates, if there are no duplicates found, a Component from the uploaded SBOM is created.

## 1.06 Edit Project

You can edit an existing project in SW360, provided you have required rights. To edit a project follow the procedure:

1. Search for the projects you want to edit or navigate from the project list.
2. Click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Edit_Pen.png" >}} from the actions column. You can also edit a project by clicking on the project and click on **Edit Project**.
3. Change the data for the project as required. For more information, refer to [1.04 Add Project](#104-add-project).
4. In this view, you can also add attachments for the project in this view, click on **Attachments**, use navigation section.</br>
    {{< figure src="/sw360/img/ImagesBasic/Project_Page/EditProject_Attachments.png" >}}</br>
    * Click on **Add Attachment**, this action opens a dialogue box.</br>
    * Browse and select the files which you want to upload or drag and drop them into the area.</br>
    * Click on **Upload**.</br>
    * Select the type of file from the drop-down list. </br>
    * Select the status from the drop-down list.</br>
    * If required, add **comments**</br>

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Attachment_2.png" >}}

    * To delete an attachment, click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}}.</br>
5. After you modify the required fields, click on "**Update Project**".
6. To delete the project, click on "**Delete Project**".
7. To cancel any changes that you made click on "**Cancel**".

## 1.07 Duplicate a Project

Duplicating a project is commonly used to create different versions of the project. This helps in reducing efforts as fewer modifications are required to create a new version. To duplicate a project:

1. Search for the projects you want to duplicate or navigate from the project list.
2. Click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Copy_Duplicate.png" >}} from the actions column to duplicate the project.
3. Modify the data for the duplicate project as required. For more information, refer to [1.04 Add Project](#104-add-project).
4. Click on "**Create Project**" after all changes are made.
5. To cancel any changes that you made click on "**Cancel**".

## 1.08 Deleting a Project

You can delete an existing project in SW360, provided you have required rights. To delete a project follow the procedure:

```WARNING: DELETING A PROJECT CAN ONLY BE DONE IF THERE ARE NO LINKED PROJECTS OR COMPONENTS. IF NOT, THERE WILL BE MISSING LINKS FOR THE PROJECTS.```

1. Search for the projects you want to delete or navigate from the project list.
2. Click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/Delete_Trash.png" >}} from the actions column to delete the project.
3. The software will prompt for a confirmation of deleting the project. You can also add comments for the action in the prompt box before deleting.
4. Click on **Delete Project**.
5. To cancel any changes that you made click on **Cancel**.</br>

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Deleteproject1.png" >}}

## 1.09 Linking A Project

There are multiple ways that you can link a project to another.

### **A. Linking to a parent project**

1. Search for the projects you want to link or navigate from the project list. Click on the required project.
2. This will display the view mode of the selected project. Click on "**Link Projects**" on the top. This will open a dialogue box to search for the projects.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linked-projects_1.png" >}}

3. Search for the projects which you want to link.
4. Select the projects and click on **Link Projects**.
5. Once the project is successfully linked, you will see the prompt in green. If you want to edit the project further, click on the    **click here to edit the project relation** on the green prompt.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linking_project.png" >}}

6. Again, the project opens up in edit mode.
7. Modify the project details as required for the linked project. Refer to [Link Projects](#a-linking-projects).  
8. Click on **"Update Project"** to save your changes.

### **B. Linking a child project**

To add child projects to a parent project, refer to [3. Linked Releases and Projects](#3-linked-releases-and-projects).

## 1.10 Linking Components or Releases

You can directly link a component or release to a parent project, refer to [3. Linked Releases and Projects](#3-linked-releases-and-projects).

### **A. Link Component**

You can also link a component to a project while editing a project.

1. Search for the projects you want to delete or navigate from the project list. Click on the required project.
2. This will display the view mode of the selected project, click on **license clearing**, use navigation section.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/LicenseClearing_1.png" >}}

3. Select the component/release from the list displayed. After which, which redirects you to its component page.
4. Click on "**Link to Projects**" to link this release/component to a project. This will open a dialogue box to search for the projects.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Linked-projects_2.png" >}}

5. If you want to view the projects which are already linked to the components/release, check the box for **show already linked projects**.
6. Select the project which you want to link the component / release to and then click on **link to project**.

## 1.11 Security Vulnerability tracking for Projects

You can view all the security vulnerabilities for your project. To view vulnerability tracking status:

1. Search for the projects or navigate from the project list. Click on the required project.
2. This will display the view mode of the selected project, click on **Vulnerability Tracking Status**.
3. Here you can view Security Vulnerability Monitoring is enabled or not. The Security Vulnerabilities are only visible in the edit project mode when the "security responsible" is assigned. Refer to paragraphs [C. Roles](#c-roles).
4. You can track the vulnerabilities by name, project origin, SVM tracking status, short status and type.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/SVM_Tracking.png" >}}

5. To view all the listed vulnerabilities for sub-projects of the parent project click on **Vulnerabilities**.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/SVM_Tracking_2.png" >}}

6. If you want to view the complete data for a vulnerability, refer to [5. Vulnerability](../New%20Userguide/5.%20Vulnerabilities.pdf).

## 1.12 Clearing Requests

Each project needs license clearing and it is a project level activity.

### **A. Create Clearing Requests**

To create a clearing request:

1. Search for the projects or navigate from the project list. Click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/ClearingRequest.png" >}} or,
2. Search for the projects or navigate from the project list. Click on the required project, this will display the view mode of the of the selected project. Click on **License Clearing**, use navigation section.
3. Click on **Create Clearing Request**, a dialogue box will appear.

   {{< figure src="/sw360/img/ImagesBasic/Project_Page/Create_clearing_request.png" >}}

4. Enter the clearing team email id by clicking on the field and searching for the email of the clearing team. Select the contact from the list and click on **Select Users**.
5. Select the **Preferred Clearing Date**.
6. If required, add **Comments**.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/License_Clearing_request.png" >}}

7. Click on "**Create Request**".
8. To cancel any changes that you made click on **Cancel**.

### **B. View Clearing Requests**

You can view the existing clearing requests which are already created for a project. To view the clearing requests, follow the procedure:

1. Search for the projects or navigate from the project list. Click on {{< figure src="/sw360/img/ImagesBasic/Project_Page/ClearingRequest.png" >}} or,
2. Click on the required project.
3. Select **License Clearing**, use navigation section.
4. Click on **View Clearing Request**.

   {{< figure src="/sw360/img/ImagesBasic/Project_Page/View_Clearing_request.png" >}}

5. A new dialogue box with the clearing request information will be displayed.

   {{< figure src="/sw360/img/ImagesBasic/Project_Page/View_Clearing_Request_2.png" >}}

### **C. Edit Clearing Requests**

For more information on how to edit the existing clearing requests, refer to [6. Requests](Requests.md/#6-requests).

## 1.13 Export Spreadsheet

You can generate the excel sheet for an advanced search. For e.g., List of all projects created for group "SHS".

1. Go to project home page.
2. If required, you can filter the projects using the advanced search options. Refer to [1.02 Project Search](#103-project-search).
3. After the search gives a result, click on **Export Spreadsheet** and select the option from the drop-down list.
    * Projects only
    * Projects with linked releases
4. A file will now be downloaded to your local system with the required information.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Export_spreadsheet.png" >}}

```NOTE: YOU CAN ALSO USE THE EXPORT SPREADSHEET OPTION ON MULTIPLE PAGES, LIKE LICENSE CLEARING PAGE OF A PROJECT/COMPONENT, EDIT VIEW OF A COMPONENT, ECC PAGE OF PROJECT ETC.```

## 1.14 Generate License Info

You can generate a read me OSS file of all the license information for a project. To generate license information:

1. Search for the projects or navigate from the project list. Click on the required project.
2. Select **License Clearing**, use navigation section.
3. The page displays the list of all the releases listed and their respective release clearing state in the ***state*** column. Each of the releases has license information in the form of CLI files. You can view this information in the ***main licenses*** or ***other licenses*** column.
Generating a license info will create a read me OSS document combining all the licenses.
4. Click on **Generate license info** and select the options from the drop-down list.
    * Project only
    * Project with sub project

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Generate_license_info.png" >}}

5. After your selection, you are redirected to another page where you can further modify the output of the license information.
6. Select **Show all** to view all the license information or **Only Approved** to view approved licenses.
7. Select which CLI you want to publish the information from the list displayed below.

   {{< figure src="/sw360/img/ImagesBasic/Project_Page/Generate_license_info_2%20.png" >}}

8. Click on **Download**. A new Dialogue box will appear asking for your preferences.
9. Check the required boxes and select an output format.
10. Click on **Download** to get a Readme.OSS file.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Generate_license_info_3.png" >}}

## 1.15 Generate Source Code Bundle

Few components have obligations, for example, sharing source code. The organization must share the source code to the user in a disc format. To generate Source Code Bundle:

1. To select the project, use the search option or navigate from the project list and click on it.
2. Select **License Clearing**, use navigation section.
3. The window shows a list of all the releases listed.  Click on **Generate Source Code Bundle** and select the option from the drop-down list.
    * Project only
    * Project with sub project
  
    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Source_code_1.png" >}}

4. After you select, you are redirected to another page which lists all the source code information.
5. Select the required source code and click **Download**.
6. A combined zip file comprising of all the select source code will be downloaded.

    {{< figure src="/sw360/img/ImagesBasic/Project_Page/Source_code_2.png" >}}
