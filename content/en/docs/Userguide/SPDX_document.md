---
linkTitle: "SPDX Document"
title: "SPDX Document"
weight: 100
description:
  SPDX Document
---

# **How to enable this feature**

To use this function, please:

1. Build the source code and deploy.

2. Add config **spdx.document.enabled = true** (/etc/sw360/sw360.properties) to enable the feature.

The following changes will work when **spdx.document.enabled = true** only.

# **1. Introduction**

SPDX Document manages Document Creation Information, Package Information, Other Licensing Information Detected, Relationships between SPDX Elements, Annotations

# **2. How to use?**
**1. File Test Import**: <https://github.com/spdx/tools-java/blob/master/testResources/SPDXRdfExample-v2.3.spdx.rdf>

**2. Import SPDX in Page Component**

#### Import

- Support RDF/XML, SPDX.
- Import all Packages in the SPDX file (main package and dependent packages)
- Import relationships related to Packages and SPDX Documents (relationships related to File and Snippet are not imported)

#### Steps

1. Go to component page
2. Click "Import SPDX BOM" button
3. Upload SPDXRdfExample-v2.3.spdx.rdf

#### Validate

- "Apache Commons Lang", "glibc",  "Jena" and "Saxon" components were created
- "glibc (2.11.1)", "Saxon(8.8)" and " Jena (3.12.0) " releases were created
- Tab SPDX Document  exits in release glibc (2.11.1), Jena (3.12.0) and Saxon (8.8)

#### Result

##### Tab SPDX Document - Full Page of Release Glibc(2.11.1)

{{< figure src="/sw360/img/sw360screenshots/spdx_document/Full_Page_of_Release_Glibc.png" >}}

##### Tab SPDX Document - Lite Page of Release Glibc(2.11.1)
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Lite_Page_of_Release_Glibc(2.11.1).png" >}}

##### Tab SPDX Document  - Full Page of Release Jena (3.12.0)
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Full_Page_of_Release_Jena_(3.12.0).png" >}}

##### Tab SPDX Document - Lite Page of Release  Jena (3.12.0)
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Lite_Page_of_Release_Jena_(3.12.0).png" >}}

##### Tab SPDX Document  - Full Page of Release Saxon (8.8)
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Full_Page_of_Release_Saxon_(8.8).png" >}}

##### Tab SPDX Document - Lite Page of Release  Saxon (8.8)
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Lite_Page_of_Release_Saxon_(8.8).png" >}}

**3. Feature: Edit , Add tab SPDX Document in Release**

##### Edit tab SPDX Document - Full Page
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Edit_tab_SPDX_Document_Full_Page.png" >}}

##### Edit tab SPDX Document - Lite Page
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Edit_tab_SPDX_Document_Lite_Page.png" >}}

##### Add tab SPDX Document
{{< figure src="/sw360/img/sw360screenshots/spdx_document/Add_tab_SPDX_Document.png" >}}
