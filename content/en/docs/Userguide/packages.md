---
linkTitle: "Packages"
title: "Packages"
Weight: 5
---

# 4.0 Packages

## 4.01 Introduction

The Packages page in SW360 displays all available software packages. A package is a collection of files and details about a specific version of software. Each package includes details such as its version, license, package manager, and other key information.

To view packages, navigate to the **Packages** tab in the main menu. You can use the Advanced Search to locate a package by various criteria. Additionally, this page allows you to add new packages and edit existing ones.

{{< figure src="/img/ImagesBasic/PackagesPage/PackagePage.png" >}}



|Sl.No.|Description|
|:----:|:----------|
|1| [Advanced Search](#403-package-search)|
|2|[Add Package](#404-add-package)|
|3| [Package List](#402-package-list) |

## 4.02 Package List

On the Packages page, you can view all the packages relevant to you. The packages are listed with the following information:
* **Package Name (Version)**: The name of the package along with its version. 
* **Release Name (Version)**: The corresponding release name and version of the package.
* **Release Clearing State**: Indicates the compliance and approval status of the package release in SW360. 
* **Licenses**: The primary licenses under which the package is distributed.
* **Package Manager**: Specifies the package management system used for the package.
* **Actions**: You can perform the following actions for a Package:

    | Action |Description |
    |:--:|:--|
    |{{< figure src="/img/ImagesBasic/Edit_Pen.png" >}} | To edit a package |
    |{{< figure src="/img/ImagesBasic/Delete_Trash.png" >}} | To delete the package from SW360. |
  
**NOTE: USE {{< figure src="/img/ImagesBasic/SortIcon.png" >}} TO SORT THE LIST ALPHABETICALLY OR IN ASCENDING/DESCENDING ORDER.**

## 4.03 Package Search 

**Advanced Search** dialogue box is used to efficiently find specific packages. 

1. **Package Name**: Search for a package using its exact name or keywords.
2. **Package Version**: Specify the version number to find a particular release of the package.
3. **Package Manager**: Search for packages based on the package manager they are associated with.
4. **License**: Filter packages by their associated software license(s).
5. **Created By (Email)**: Search for packages created by a specific user using their email address.


## 4.04 Add Package

To add a new package, click **Add Package** from the package page, this will redirect you to another page where you can add package summary information. 

### **Summary**

```NOTE: FIELDS MARKED "*" ARE MANDATORY.```
{{< figure src="/img/ImagesBasic/PackagesPage/AddPackage.png" >}}

1. Enter the **Name** of the package you want to create.</BR>
   ```NOTE: MAKE SURE THAT THERE ARE NO DUPLICATES.```</BR>
2. Enter the unique **PURL (Package URL)** identifier.</BR>
   ```NOTE: PURL FOLLOWS A STANDARD FORMAT TO UNIQUELY IDENTIFY THE PACKAGE.``` </BR>
3. Specify the **Version** of the package.
4. **Package Manager** will be set automatically based on the provided PURL.
5. Select the **Package Type** from the drop-down list.
    - **Application**: A software program designed for end users.
    - **Container**: A lightweight, isolated environment for running software.
    - **Device**: Software made for hardware devices and embedded systems.
    - **File**: A package containing essential software components in a single file.
    - **Firmware**: Software that controls how hardware works.
    - **Framework**:  A set of tools and code that help developers build software.
    - **Library**: A collection of prewritten code that helps software perform specific tasks without writing everything from scratch.
    - **Operating System**: The main software that manages computer hardware(eg. Linux, Windows).
6. Enter the **VCS (Version Control System)** URL used for the package.
7. **Main Licenses**: Click to set License.
8. **Created On**: This field is automatically set to the current date.
9. **Release**: Click to link a release.
10. **Created By**: The field is automatically set to the creator of the package.
11. Enter the **Homepage URL**, this is the web address for your package.
12. **Modified By**: This field is automatically set to the user making modifications.
13. Provide a **Description** of the package, outlining its functionality and purpose.


## 4.05 Edit Package

1. Search for the package you want to edit or navigate from the package list.
2. Click on ![](/img/ImagesBasic/Edit_Pen.png) from the actions column. You can also edit a package by clicking on the package and then clicking on **Edit Package**.
3. You can view summary information of the package. 
4. Click on **Update Package** to update the new package information.
5. Click on **Delete Package** To delete the package.
6. If you do not want to edit the package, click on **Cancel**.


## 4.06 View Package

To open a view mode for a package:

1. Search for the package you want to edit or navigate from the package list. 
2. Click on the package name.
3. You are now in the view mode of the package, where you can view the **summary** of the package and **change logs**.

   
### **Summary**

In this section, you can view the details of the package, including all essential information related to it.
{{< figure src="/img/ImagesBasic/PackagesPage/EditPackage.png" >}}

1. **Id**: This field shows the unique identifier assigned to the package.
2. **Name**: Displays the name of the package.
3. **Version**: Shows the version of the package.
4. **Package Type**: Displays the type of the package (e.g., Application, Container, Device, etc.).
5. **PURL (Package URL)**: Shows the unique Package URL, which is used to reference the package.
6. **Package Manager**: The package manager used to manage the package (e.g., Npm, Deb, etc.).
7. **VCS (Version Control System)**: Displays the version control system used for the package (e.g., Git etc.).
8. **Homepage URL**: The URL of the homepage for the package.
9. **Licenses**: Lists the licenses associated with the package.
10. **Linked Release**: Shows the release linked to the package.
11. **Description**: Provides a detailed description of the package.
12. **Created By**: Displays the user who created the package.
13. **Modified On**: Displays the last modification date for the package.
14. **Modified By**: Displays the user who last modified the package.


### **Change Log**

You can see all the changes that are done for the package in the change log section.

![](/img/ImagesBasic/PackagesPage/ChangeLog.png)

1. To view all the changes done for the package, click on **Change Log**.
2. You can now view the change date, change log ID, change type, and the user who made the change.
3. Click on ![](/img/ImagesBasic/PackagesPage/action.png) to view all the changes made for a specific change log ID.
