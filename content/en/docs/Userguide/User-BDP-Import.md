# How to Import Projects from BDP into SW360

This page explains how to import a project from BDP into SW360 via the SW360 UI. 

## The Project Import Portlet

In SW360, open the `Import Portlet` as follows:

![](./images/UCBDPImport/01_OpenImportPortlet.png)

Make sure that you do not leave the `Import Portlet` page during the connection, selection an import process.

On the left hand side, you see a mask to enter connection data for the BDP server:

![](./images/UCBDPImport/02_ImportPortlet.png)

Make sure, that the `Selected data source` is `BDP`. As `Server URL`, enter the domain of the BDP server.
Enter your user credentials for the BDP Server in `Server user` and `Password`, respectively.
Now, click `Connect` and the connection with the BDP Server is established. On the right hand side, you can view the projects 
that are available to you on the BDP server. 

![](./images/UCBDPImport/03_ConnectionEstablished.png)

Select the projects that you want to import by clicking on the respective rows and click `Import`.

![](./images/UCBDPImport/04_SelectProjects.png)

Click `Import` if you are content with the choice. Now, SW360 tries to import your selected projects. If everything went fine, you see:

![](./images/UCBDPImport/05_ImportSuccess.png)

The import might fail for some projects. The reason usually is that these projects have been imported earlier and already exist in SW360.
In this case, SW360 does not re-import or overwrite the project. But all new projects are still imported.

## Inspecting the Results

The imported `project`, `components` and `licenses` can be viewed in the `Projects Portlet`, `Components Portlet` or `License Portlet` respectively.
Note that a `component` in BDP becomes a `release` in SW360. To view such a release for example, first open the `Components Portlet` and click on the name of the component:

![](./images/UCBDPImport/06_SelectComponent.png)

Select `Release Overview` on the left hand side: 

![](./images/UCBDPImport/07_SelectReleaseOverview.png)

Click on the `release version` to select a specific release:

![](./images/UCBDPImport/08_SelectRelease.png)
 
Now, you can view the release details:

![](./images/UCBDPImport/09_ReleaseDetails.png)
 


 

