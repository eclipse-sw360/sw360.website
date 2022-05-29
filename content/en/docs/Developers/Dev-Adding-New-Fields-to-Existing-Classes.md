How to add fields to an existing class
======================================

The license portlet is different from the other portlets as there is no Details/Edit page for each element. There is only a combined edit/view page.
We will add the license text to licenses in the thrift file:
```
13: optional string text;
```

To update the text we write a liferay Action in the LicensesPortlet:
```
    @UsedAsLiferayAction
    public void changeText(ActionRequest request, ActionResponse response) throws PortletException, IOException {
        String licenseId = request.getParameter(LICENSE_ID);
        String text = request.getParameter(License._Fields.TEXT.name());

        if(!Strings.isNullOrEmpty(licenseId)) {

            try {
                User user = UserCacheHolder.getUserFromRequest(request);
                LicenseService.Iface client = thriftClients.makeLicenseClient();
                final License license = client.getFromID(licenseId);

                license.setText(CommonUtils.nullToEmptyString(text));
                final RequestStatus requestStatus = client.updateLicense(license, user);

                renderRequestStatus(request,response,requestStatus);
            } catch (TException e) {
                log.error("Error updating license", e);
            }
        }

        response.setRenderParameter(LICENSE_ID, licenseId);
        response.setRenderParameter(PAGENAME, PAGENAME_DETAIL);
        response.setRenderParameter(SELECTED_TAB, "LicenseText");
    }
```

To integrate it in the jsp we make the according changes, important to note is the ActionUrl that we define:
```
<portlet:actionURL var="changeLicenseTextURL" name="changeText">
    <portlet:param name="<%=PortalConstants.LICENSE_ID%>" value="${licenseDetail.id}" />
</portlet:actionURL>
```
A good practice to name fields in jsps is to use the thrift field names:

```
  <textarea name="<portlet:namespace/><%=License._Fields.TEXT%>" rows="5"  style="width: 100%" id="<portlet:namespace/><%=License._Fields.TEXT%>"
            placeholder="Enter the License-Text here..."
          >${licenseDetail.text}</textarea>
```