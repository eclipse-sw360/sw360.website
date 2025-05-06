---
linkTitle: "Dependency-Network-Feature"
title: "Dependency Network Feature"
weight: 100
description: 
  Dependency-Network-Feature
---

# **How to enable this feature**

To use this function, please:

1. Build the source code and deploy.

2. Add config **enable.flexible.project.release.relationship=true** (/etc/sw360/sw360.properties) to enable the feature.

The following changes will work when **enable.flexible.project.release.relationship=true** only.

3. Use the migration script (**056_migrate_project_dependency_network.py**) we provided to mograte the database.

 Before you run the script, please change two places in the script:

 (1) Line 30: ```DRY_RUN = True``` -> ```DRY_RUN = False```

 (2) Line 32: ```COUCHSERVER = 'http://localhost:5984/'``` -> ```COUCHSERVER = 'http://admin:password@localhost:5984/'```

 ```admin``` and ```password``` should be your username and password for CouchDB.

# **1. Introduction**

The dependency network feature is a new function to make the dependency management of a project more flexible by allowing the users to customize the dependency graphs of their projects.

# **2. How to use?**
This feature modify the GUI of the “Linked Releases And Projects” on the “project edits” page.
Now the “Linked Releases” table could show all dependencies of a project (both direct and transitive ones). Users can modify these dependencies as well.

{{< figure src="/sw360/img/sw360screenshots/dependency_network/new_edit_GUI.png" >}}

## **2.1. The changes of edit project GUI**
In this section, we will introduce the changes in GUI behaviors. We modified or added 5 sub-functions below: 
 
#### **a. Modify the “Add Releases” button: This button will add a direct dependency (release) in the dependency graph of this project.**

{{< figure src="/sw360/img/sw360screenshots/dependency_network/Add_root_release_button.png" >}}


#### **b. A new icon button to add a dependency (release) to another dependency (release) in the dependency graph. Note that this dependency added is seen as the transitive dependency of this project.**

{{< figure src="/sw360/img/sw360screenshots/dependency_network/Add_transitive_releases_buttons.png" >}}

#### **c. A new icon button to load the default dependency graph of a dependency (release) by importing the dependency information stored on the component page. Note that this button will load all dependencies (both direct and transitive ones) of the corresponding dependency (release).**

{{< figure src="/sw360/img/sw360screenshots/dependency_network/Load_default_network_from_releases.png" >}}

#### **d. The combo box allows the user to modify the version of a dependency.**

{{< figure src="/sw360/img/sw360screenshots/dependency_network/Select_version_box.png" >}}


#### **e. The “Check Dependency Network” button will compare and show the different dependency information which is not consistent with the default one stored on the component page by highlighting them. The inconsistency usually happens after users modified the dependency graph or imported an old project.**

{{< figure src="/sw360/img/sw360screenshots/dependency_network/Check_diff_button.png" >}}


## **2.3 Rest API changes**

### New Rest APIs

**a. 3.3.35. Get a single project with dependencies network**

The response will include the dependencyNetwork field(It will show the dependency network of project (direct and indirect releases)):
```
{
  "name" : "Emerald Web",
  "dependencyNetwork": [
      {
          "releaseId": "9efc5766cd0c41d4a40547b99f5b91ac",
          "releaseLink": [
              {
                  "releaseId": "3bed97a1c7ac4c32846ef4be985b648c",
                  "releaseLink": [
                      {
                          "releaseId": "6a8250852362462095c57535294039e4",
                          "releaseLink": [],
                          "releaseRelationship": "TO_BE_REPLACED",
                          "mainlineState": "PHASEOUT",
                          "comment": "Test Comment",
                          "createOn": "2023-05-15",
                          "createBy": "admin@sw360.org"
                      }
                  ],
                  "releaseRelationship": "INTERNAL_USE",
                  "mainlineState": "OPEN",
                  "comment": "Test Comment",
                  "createOn": "2023-05-15",
                  "createBy": "admin@sw360.org"
              }
          ],
          "releaseRelationship": "STATICALLY_LINKED",
          "mainlineState": "MAINLINE",
          "comment": "Test Comment",
          "createOn": "2023-05-15",
          "createBy": "admin@sw360.org"
      },
      {
          "releaseId": "f1d860e7576a44798ee3daff57a3a886",
          "releaseLink": [],
          "releaseRelationship": "OPTIONAL",
          "mainlineState": "OPEN",
          "comment": "Test Comment",
          "createOn": "2023-05-15",
          "createBy": "admin@sw360.org"
      }
  ]
}
```

**b. 3.3.36. Creating a project with dependencies network**

If the **dependencyNetwork** field is included in the request body, a dependency network will be registered for the project.

- Simple example request (modify releaseIds to the existing release ids in sw360):

```
{
    "name": "TestProject1",
    "dependencyNetwork": [
        {
            "releaseId": "9efc5766cd0c41d4a40547b99f5b91ac",
            "releaseLink": [
                {
                    "releaseId": "3bed97a1c7ac4c32846ef4be985b648c",
                    "releaseLink": [
                    ],
                    "releaseRelationship": "INTERNAL_USE",
                    "mainlineState": "OPEN",
                    "comment": "Test Comment",
                    "createOn": "2023-05-15",
                    "createBy": "admin@sw360.org"
                }
            ],
            "releaseRelationship": "STATICALLY_LINKED",
            "mainlineState": "MAINLINE",
            "comment": "Test Comment",
            "createOn": "2023-05-15",
            "createBy": "admin@sw360.org"
        },
        {
            "releaseId": "f1d860e7576a44798ee3daff57a3a886",
            "releaseLink": [],
            "releaseRelationship": "OPTIONAL",
            "mainlineState": "OPEN",
            "comment": "Test Comment",
            "createOn": "2023-05-15",
            "createBy": "admin@sw360.org"
        }
    ]
}
```

**c. 3.3.37. Update a project with dependencies network**

Same request body as "Creating a project with dependencies network".
