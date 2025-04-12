---
title: "User Guides"
linkTitle: "User Guides"
weight: 10
icon: fas fa-users
description: This guide provides an overview of SW360 and how to get started with using it. It covers the basic usage, and tips for configuring SW360 to work with your software development tools
---

# SW360 INTRODUCTION
SW360 is a comprehensive software catalogue application that helps organizations manage their software components and licenses effectively. This application provides detailed information about the software components used in various projects, including their licenses, clearing information, and other relevant data. With SW360, organizations can easily track and manage the software components used in their projects, ensuring compliance with licensing requirements and minimizing legal risks.

SW360 can also be used with the license scanner, "FOSSology" which provides license clearing, which is then integrated into the workflows. SW360 integrates software artifacts and projects into the related existing infrastructures. SW360 also provides backend services for distinct tasks and a set of portlets to access these services.

Use case areas:

- Handling project information where open-source software components and other third-party software are used.
- SBOM (Software Bill Of Materials ) Management.
- Handling component information and its associated processess. E.g.: name, vendor, version, ECCN information, license compliance information.
- Handling license information. E.g., obligations, license texts, etc.
- Collecting security vulnerability management information and matching them with components stored in component services
- Compiling and creating all license related documentation. E.g., Readme, source code bundle, that are supported by workflows.

## SW360 Functionality

With SW360 you can:

- Manage your components and projects
- Send source packages to the license scanner, FOSSology
- Reuse cleared components and release for projects
- Import cleared components with reports and other documents
- Browse licenses and their obligations

## Data Model

### **Project**

Projects can be products, platforms, any kind of "SW bill of material (BOM)", etc, that manages a list of 3rd party components. Projects are created for a product, service, inner source, customer project or an internal project. Project types are software only, system, platform or Cloud service.

### **Components**

A component is a SW component with metadata. The versions of this component are linked as releases. It is a catalogue to register a component type (OSS/ COTS/ Freeware/ code snippet / Service) from a specific vendor or open-source community. For e.g., Commons by Apache, Windows server 2019 by Microsoft etc.

### **Release**

A release refers to a particular version of a software component that has been made available for use. It points to a stable and functional iteration of the component. Releases can include bug fixes, new features, and updates to improve the component's overall performance and user experience.

### **Vendor**

SW360 can be used to manage components and licenses from various vendors, including open source and proprietary software vendors. Vendor can be different from a component or releases. Vendors can be added to SW360's database and their components and licenses can be tracked and managed through the tool's interface. This allows organizations to gain better visibility into their software assets and ensure compliance with license obligations. A link to the vendor is set at the release level, as the vendor can change with new releases.

### **Licenses**

The project ensures that all license information pertaining to its releases are thoroughly documented and made available to the customers. This information is typically provided in the form of a ReadmeOSS file, which includes details regarding the relevant licenses, as well as any other pertinent information such as acknowledgements, copyright notices, and applicable third-party software licenses. The project strives to maintain transparency and comply with all legal requirements in relation to licensing and intellectual property, and takes necessary steps to ensure that its customers are fully informed about the licensing terms and conditions of the software they are using.

### **Obligations**

Obligations refer to the license obligations resulting from license interpretations. These obligations must be fulfilled by the organization to use the third-party software in a compliant manner. They are categorized based on grants, redistribution rights, specific contractual agreements, internal uses, risk related to patents, permission for modification of code etc.

Each license obligation will be provided with Clearing Report by the Clearing Experts. The clearing report must verify that the third party software is used in compliance with license and have fulfilled all the obligations.

OSS license obligations are typically provided centrally.
COTS license obligations must be analyzed individually for every commercial contract.

### **Vulnerabilities**

The Security Vulnerability Monitoring (SVM) system is responsible for monitoring a specified list of security vulnerabilities and list all the vulnerabilities in this tab. These vulnerabilities are tracked and can be transferred to other systems or security experts as needed. The SVM has the capability to transfer the vulnerability lists via API to SW360 or the designated security expert responsible for managing them. By utilizing this system, the project can effectively monitor and manage potential security threats, ensuring the integrity and security of the software.

### **Product Clearing**

Product Clearing is the approval of use of all third-party software components in a product and assessing any risks before the product is approved for a specific license or sales model and supplied to third parties. This can be done by creating a 'Project Clearing Report' from SW360.

### **Administration**

Administration is responsible for storing and maintaining various project-related information, including the current Project Clearing State (Open, Closed, In-progress), Clearing Summary, and any risks associated with the usage of third-party software, as assessed during the project clearing process. This information is crucial to ensuring that the project is effectively managed and remains in compliance with all relevant policies and regulations. The administrative team takes necessary measures to ensure the security and integrity of the stored data, and regularly updates the information as needed to reflect changes in the project's status or risk profile.

### **Attachments and Attachment Usages**

The project management system includes support for attachments, which are used to store and manage various types of information relevant to the project. Attachments can be stored at both the project and release levels, with release-level attachments typically consisting of source code, contracts, component license information, and Readme files, among other things.

The project management team ensures that all necessary attachments are properly labeled and organized, allowing for easy access and retrieval when needed. By utilizing this system, the project team can effectively manage and track important project-related information, helping to ensure the success and compliance of the project.

### **Clearing Requests**

These are the requests that are raised to the clearing experts to get the OSS license clearing for a project. These requests can only be raised at a project level and must be done once all the linked releases and projects are assigned to the parent project. This should be done in advance to give the clearing experts adequate time to get the license clearing report. The clearing results are further assessed by responsible experts and the project management.

### **Export Controls and Customs (ECC)**

Export Controls and Customs (ECC) numbers are automatically assigned to components, with the exception of Commercial Off-The-Shelf (COTS) components. In the case of COTS components, an ECC expert is responsible for setting the appropriate ECC numbers. By accurately identifying and assigning ECC numbers to components, organizations can prevent potential legal and financial penalties, as well as safeguard national security interests.

### **Source Code Bundles**

These are multiple source code packages which are attachments to a specific release to perform license analysis. The source code bundle is generated for a project to fulfill the license obligations “make source code available” which is required by some of the OSS licenses.

## Important Links

| Page | URL | Note |
|------|-----|------|
|Public Project Homepage | <https://www.eclipse.org/sw360/> | Main project homepage |
|Public project GitHub Page  | <https://github.com/eclipse/sw360/> | Main project |
|Project Information in Eclipse  | <https://projects.eclipse.org/projects/technology.sw360> | Information on Eclipse SW360 |
|Public project home page SW360 Antenna | <https://github.com/eclipse/antenna> | Antenna Connects to SW360 to exchange information right from the build time |
|Public project SW360 Vagrant in GitHub | <https://github.com/sw360/sw360vagrant> | Vagrant Set up for SW360 |
|Public Project for SW360 chores at GitHub | <https://github.com/sw360/sw360chores> |Docker setup for SW360 |
|Public Project SW360 slides in GitHub | <https://github.com/sw360/sw360slides> | Main slide deck of SW360 published as Git repository |
