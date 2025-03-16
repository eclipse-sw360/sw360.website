---
title: "SW360 Documentation"
linkTitle: "Documentation"

menu:
  main:
    weight: 90
---

## **Overview**
**SW360** is a software catalog application designed to facilitate the sharing of information about software components within an organization. Its primary objective is to manage software license information while supporting compliance workflows.  

SW360 integrates with **FOSSology**, an open-source license scanning tool, to analyze source code for licenses, copyrights, and other relevant details.  

To ensure seamless adoption, SW360 is designed to integrate with existing software artifact and project management infrastructures. It provides:  
- **Backend services** for different tasks.  
- **A set of portlets** to access these services.  
- **Deployment options** via a pre-configured **Vagrant box** or **Docker container**, ensuring an easy setup process.  

#### **Key Use Cases**
SW360 supports various use cases, including:  
- **Projects:** Manage project details, including open-source and third-party software components.  
- **Components & Releases:** Store component details such as name, vendor, version, ECCN, and license compliance.  
- **Licenses:** Maintain records of license texts, copyrights, acknowledgments, and obligations.  
- **Vulnerabilities:** Track security vulnerabilities and match them with components in the system.  
- **License Compliance Documentation:** Generate required compliance documents such as README files and source code bundles.  

---

## **Functionality**
With **SW360**, you can:  
- Manage software components and projects.  
- Analyze source packages using **FOSSology**.  
- Reuse previously cleared components for new projects.  
- Import cleared components along with compliance reports and other related documents.  
- Browse and review software licenses and their obligations.  

#### **Key Features**
- **Built on the Open Source Liferay Portal Server.**  
- **Integrated with FOSSology** for license scanning and compliance analysis.  

#### **Data Model Concepts**
Understanding SW360’s data model is essential:  
- A **Component** consists of multiple releases, each with its own metadata.  
- A **Release** represents a specific version of a component with metadata and associated attachments.  
- A **Project** consists of multiple component releases, not just components.  
- A **Vendor** is independent of a component or release. The vendor link is assigned at the release level.  
  *(For example, Sun Microsystems and Oracle—ownership changed in a later release.)*  

---

## **Getting Started** 

| Name | URL | Description |
| --- | --- | --- |
| **Main Home Page** | [Eclipse SW360](https://www.eclipse.org/sw360/) | Official project homepage with general information. |
| **GitHub Repository** | [SW360 on GitHub](https://github.com/eclipse/sw360) | The source code and development discussions. |
| **Developer Mailing List** | `sw360-dev@eclipse.org` | For development-related discussions. |
| **Slack Channel** | [SW360 Chat](https://sw360chat.slack.com/) | Main chat hub—everyone is welcome! |
| **Slack Invitation** | [Join SW360 Slack](https://join.slack.com/t/sw360chat/shared_invite/enQtNzg5NDQxMTQyNjA5LThiMjBlNTRmOWI0ZjJhYjc0OTk3ODM4MjBmOGRhMWRmN2QzOGVmMzQwYzAzN2JkMmVkZTI1ZjRhNmJlNTY4ZGI) | Use this link to join our Slack community. |
| **SW360 Developer Meeting** | [Meeting Info](Developer-Meetings) | Open to all contributors! |

---

