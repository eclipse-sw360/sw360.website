---
title: "How to add a frontend portlet to sw360"
linkTitle: "Add frontend portlet"
weight: 10
---

We create a class in 
```
sw360/src/frontend/sw360-portlets/src/main/java/com/siemens/sw360/portal/portlets/admin/
```

called
```
DatabaseSanitation.java
```

Here are some code snippets that are important:

```java
public class DatabaseSanitation extends Sw360Portlet 
```

the base class Sw360Portlet adds some convenience methods to render the most common return values of functions into messages.

```java
@Override
public void doView(RenderRequest request, RenderResponse response) throws IOException, PortletException {
    // Proceed with page rendering
    super.doView(request, response);
}
```

This method is used to render different pages, a common pattern would be to have if/else tree like 
```java
//! VIEW and helpers
@Override
public void doView(RenderRequest request, RenderResponse response) throws IOException, PortletException {
    String pageName = request.getParameter(PAGENAME);
    if (PAGENAME_EDIT.equals(pageName)) {
        prepareVendorEdit(request);
        include("/html/vendors/edit.jsp", request, response);
    } else {
        prepareStandardView(request);
        super.doView(request, response);
    }
}
```

but since we only have one page this is all we need. The jsp that is rendered by super.doView is set in 

```java
sw360/src/frontend/sw360-portlets/src/main/webapp/WEB-INF/portlet.xml
```
but more on that later.

The next method in DatabaseSanitation handles resource requests, which are responses to AJAX calls:
```
@Override
public void serveResource(ResourceRequest request, ResourceResponse response) throws IOException, PortletException {
    String action = request.getParameter(PortalConstants.ACTION);
    if (PortalConstants.DUPLICATES.equals(action)) {
              serveDuplicates(request, response);
    }
}
```

similar to the PAGENAME tree, here we have an ACTION if/else block. We only have one action, so this is simple.


Let's have a look at 

```java
private void serveDuplicates(ResourceRequest request, ResourceResponse response) throws IOException, PortletException {

    Map<String, List<String>> duplicateComponents=null;
    Map<String, List<String>> duplicateReleases=null;
    try {
        final ComponentService.Iface componentClient = thriftClients.makeComponentClient();
        duplicateComponents = componentClient.getDuplicateComponents();
        duplicateReleases = componentClient.getDuplicateReleases();
    } catch (TException e) {
        log.error("Error in component client", e);
    }

    if(duplicateComponents== null || duplicateReleases==null) {
        renderRequestStatus(request,response, RequestStatus.FAILURE);
    } else if(duplicateComponents.isEmpty()  && duplicateReleases.isEmpty()) {
        renderRequestStatus(request,response, RequestStatus.SUCCESS);
    } else {
        request.setAttribute(PortalConstants.DUPLICATE_RELEASES, duplicateReleases);
        request.setAttribute(PortalConstants.DUPLICATE_COMPONENTS, duplicateComponents);
        include("/html/admin/databaseSanitation/duplicatesAjax.jsp", request, response, PortletRequest.RESOURCE_PHASE);
    }
}
```    

The member variable thriftClients is inherited from the Sw360Portlet. This is how we talk to the backend.
We call the methods that we wrote in the first part of the tutorial.
The error handling is reported with renderRequestStatus, also from Sw360Portlet.
When we have findings then we report them by rendering a jsp in the RESOURCE_PHASE.
This is then some html that our AJAX function gets as data.

Then we have to register the portlets in some xml files:

```
sw360/src/frontend/sw360-portlets/src/main/webapp/WEB-INF/liferay-display.xml
```

```xml
...
<portlet id="databaseSanitation"/>
```

```
sw360/src/frontend/sw360-portlets/src/main/webapp/WEB-INF/liferay-portlet.xml
```

```xml
...
<portlet>
    <portlet-name>databaseSanitation</portlet-name>
    <icon>/icon.png</icon>
    <instanceable>false</instanceable>
    <header-portlet-css>/css/main.css</header-portlet-css>
    <header-portlet-javascript>/js/main.js</header-portlet-javascript>
    <header-portlet-javascript>/js/external/jquery-1.11.1.min.js</header-portlet-javascript>
</portlet>
```
Note that here it is important to include things like jquery in this way so that on multiple portlet pages there are no namespace conflicts.

```
sw360/src/frontend/sw360-portlets/src/main/webapp/WEB-INF/portlet.xml
```

```xml
...
<portlet>
    <portlet-name>databaseSanitation</portlet-name>
    <display-name>databaseSanitation</display-name>
    <portlet-class>
        com.siemens.sw360.portal.portlets.admin.DatabaseSanitation
    </portlet-class>
    <init-param>
        <name>view-template</name>
        <value>/html/admin/databaseSanitation/view.jsp</value>
    </init-param>
    <expiration-cache>0</expiration-cache>
    <supports>
        <mime-type>text/html</mime-type>
        <portlet-mode>view</portlet-mode>
    </supports>
    <portlet-info>
        <title>databaseSanitation</title>
        <short-title>databaseSanitation</short-title>
        <keywords/>
    </portlet-info>
    <security-role-ref>
        <role-name>administrator</role-name>
    </security-role-ref>
</portlet>
```

After these changes we compile the frontend and then we have to add new page to the Layout and add it to the lar file.
We sign in as admin, 
go to 
```
Admin -> Site administration 
-> Private Pages

```
To add the portlet to the page, we first change the theme of Private Pages to Classic, then select Add Page. We can drag and drop it under the Admin Page.
Then we select the Private Pages under My Sites.
We can then go to the page we have just created. 
On the left side there is a plus sign, which opens a side menu with the available portlets that we can add to our page.
Under SW360 we find the portlet DatabaseSanitation and we click add.
Then we can change the option (The cog symbol on the right) Look and Feel  to Show Borders -> No and we save that.
Then we change the theme of Private Pages back to SW360-Theme.

Now we can change the theme back and export a new lar file as described else where.
