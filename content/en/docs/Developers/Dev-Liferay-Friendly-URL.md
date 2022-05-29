### Introduction

The normal generated portlet URLs containing a set of internal Liferay request parameters. <br>
These long URLs of links or forms are mostly not readable and its not easy to share it somewhere else.

General Liferay portlet URL: <br>
```
http://localhost:8080/web/guest/examples?p_p_id=example_WAR_ExamplePortlet&p_p_lifecycle=1&p_p_state=normal&p_p_mode=view&p_p_col_id=column-1&p_p_col_count=1&_example_WAR_ExamplePortlet_javax.portlet.action=new
```

Explanation of the Liferay request parameters: <br>
**p_p_id:** The portlet ID (example_WAR_ExamplePortlet)<br>
**p_p_state:** Liferay windows pages state - 1 (normal) 2 (maximize) 3 (minimize) <br>
**p_p_mode**: Mode of the portlet look like - (view) (edit) (help) <br>
**p_p_lifecycle:** This is life cycle of portlet - 0 (render) 1 (action) 2 (server) <br>
**p_p_col_id:** The reference ID of the column in Liferay template <br>
**p_p_col_pos:** Specifiy the column position if the the layout having more than one columns <br>
**p_p_col_count:** Shows the no of columns in the current layout

### Friendly URL Mapper configuration

Liferay provides a mechanism to shorten the generated URLs by using the Friendly URL Mapper feature. <br> <br>
How to configure the friendly URL Mapper in Liferay? <br> <br>
**Configuration of URL routes in XML files** <br>

_CREATE example-friendly-url-routes.xml_ <br>
```
<?xml version="1.0"?>
<!DOCTYPE routes PUBLIC "-//Liferay//DTD Friendly URL Routes 6.2.2//EN"
"http://www.liferay.com/dtd/liferay-friendly-url-routes_6_0_0.dtd">
<routes>
	<route>
		<pattern>/action/{actionName}</pattern>
		<generated-parameter name="javax.portlet.action">{actionName}</generated-parameter>
		<ignored-parameter name="p_auth"/>
		<ignored-parameter name="p_p_id"/>
		<implicit-parameter name="p_p_lifecycle">1</implicit-parameter>
		<implicit-parameter name="p_p_state">normal</implicit-parameter>
		<implicit-parameter name="p_p_mode">view</implicit-parameter>
	</route>
</routes>
```

Explanation of the Liferay Friendly Mapper route parameters: <br>
**routes:** Routes element which contains all route entries <br>
**route:** Single route element entry  <br>
**pattern:** Pattern of the mapped friendly URL (visible in address bar) <br>
**generated-parameter:** These parameters will be generated from parameters in the request URL <br>
**ignored-parameter:** These parameters will be igored and not included in generated URLs <br>
**implicit-parameter:** Used for static attributes which can be ignored by recognition <br>
**overridden-parameter:** Parameter that should be set to a certain value when a URL is recognized <br>
<br>
It is necessary to order the parameters as described above. <br>
These files should located in the resources folder otherwise they will not be available on Apache Tomcat and cannot be initialized by Liferay. <br>
<br>
**Configuration of friendly URL Java class** <br>
<br>
_MODIFY liferay-portlet.xml_
<br>
```
<friendly-url-mapper-class>com.liferay.portal.kernel.portlet.DefaultFriendlyURLMapper</friendly-url-mapper-class>
<friendly-url-mapping>example</friendly-url-mapping>
<friendly-url-routes>com/.../example-friendly-url-routes.xml</friendly-url-routes>
```
<br>
In the next step we need one java implementation class to generate the Liferay friendly URLs. <br>

Liferay provides the _DefaultFriendlyURLMapper_ class to create the URLs based on our rules. <br>

The Liferay Friendly URL Mapper configuration is placed after `<icon/>` and before `<instanceable>` 
tag.

### Friendly URL Mapper outcome

**Liferay will generate the following friendly URL** <br>
```
http://localhost:8080/web/guest/examples/-/example/action/new
```
<br>

1. The liferay framework will add "-" (dash)
1. Friendly URL mapper name which is configured in `<friendly-url-mapping>` (liferay-portlet.xml) element
1. Pattern name with generated parameters which is same as in `<pattern>` (example-friendly-url-routes.xml) defined.

### Additional

Friendly URL Mapper functionality is not working if the portletURL API is used to generate the Liferay URL in local Javascript. <br>
It is helpful to generate `<portlet:renderURL>` placeholder and replace them by using dummy values.
