---
title: "Using RequireJS for JavaScript Modules"
linkTitle: "Using RequireJS"
weight: 10
---

Modern JavaScript code often runs in the global namespace, increasing the risk of symbol overwrites due to multiple libraries and code snippets. To avoid this, we use **RequireJS** to modularize our code, ensuring clear namespaces for each component and improving reusability.

## Advantages of RequireJS
- Libraries like **jQuery** and **DataTables** can be imported by name without specifying a version.
- Different versions of libraries can be loaded for different parts of the page.
- Only required dependencies are loaded, optimizing performance.
- **WebJars support**: WebJars are automatically accessible through RequireJS due to `webjars-locator`.

## How to Use RequireJS (Example)
To enable RequireJS, include the following file in your **JSP**:

```jsp
<%@ include file="/html/utils/includes/requirejs.jspf" %>
```

When RequireJS is enabled, libraries can be accessed in a modular way:

```javascript
require(['jquery', 'module/quickfilter', 'module/confirm', /* jQuery plugins: */ 'datatables', 'jquery-ui'],
function($, quickfilter, confirm) {
    // Code goes here, libraries are accessible via $, quickfilter, and confirm.
    // jQuery plugins register themselves automatically.
});
```

### Important Warning
Since not all code uses RequireJS, **include RequireJS just before the script tag using it.** Do not include it at the beginning of the file.

**Correct usage:**
```jsp
<%@ include file="/html/utils/includes/requirejs.jspf" %>
<script>
    require(['jquery'], function($) {
        // JavaScript code
    });
</script>
```

#### Explanation
Some jQuery plugins are **module-safe**, meaning they check for RequireJS before registering. If a plugin is loaded manually before RequireJS, it might register twice, causing errors. **Loading RequireJS after all scripts prevents this issue.**

## Migrating to RequireJS
### Migrating a JSP File
Follow these steps:
1. **Enable RequireJS**: Include `requirejs.jspf` just before the script tag with the main code.
2. **Wrap existing code** inside a `require` function.
3. **Remove manual script tags** that load JavaScript files.
4. **Refactor external function calls** to be inside the `require` function (e.g., for click handlers).

### Co-existence with `AUI().use()`
If you need to use **AUI().use()** (e.g., for `PortletURL`), call it first and nest `require` inside:

```javascript
AUI().use('liferay-portlet-url', function () {
    require(['jquery', 'module/quickfilter'], function($, quickfilter) {
        // Both AUI and RequireJS modules are loaded.
    });
});
```

### Migrating Click Handlers
Since functions are no longer in the global scope, inline click handlers won’t work. Use jQuery to attach event handlers:

```javascript
$('#exportSpreadsheetButton').on('click.components', exportSpreadsheet);
```
For dynamic elements (e.g., table rows):

```javascript
$('#componentsTable').on('click.components', 'img.delete', function(event) {
    // Handle deletion
});
```

## Creating Modules
### Converting a `jspf`-Include to a Module
Some `.jspf` files contain both HTML and JavaScript. Follow these steps to convert them:

1. **Move JavaScript code** to a separate file under `js/`, maintaining the same directory structure.
   - Example: If `jspf` file is `html/components/includes/vendors/addVendor.jspf`, place JavaScript in `js/components/includes/vendors/addVendor.js`.
2. **Wrap the JavaScript code** in a `define` statement to create a module:

   ```javascript
   define('components/includes/vendors/addVendor', [ /* dependencies */ ], function() {
       // Module code
   });
   ```
3. **Include the JSP file** and load the module using RequireJS:

   ```jsp
   <%@ include "html/components/includes/vendors/addVendor.jspf" %>

   <script>
   require(['components/includes/vendors/addVendor'], function(addVendor) {
       // Use addVendor module
   });
   </script>
   ```

### Converting a JavaScript File to a Module
For JavaScript files in `/html/js/`, follow these steps:

1. Create a new file in `/html/js/component/`, naming it appropriately.
2. Define the module and reference existing functions:

   ```javascript
   define('module/confirm', ['jquery', 'jquery-confirm', 'main'], function($) {
       return {
           confirmDeletion: deleteConfirmed // Reference legacy function from main.js
       };
   });
   ```
3. Load the module using RequireJS:

   ```javascript
   require(['module/confirm'], function(confirm) {
       confirm.confirmDeletion(/* ... */);
   });
   ```

### Note:
- **Legacy functions** should be moved inside modules once they are no longer accessed globally.
- **Legacy JavaScript files** can still be required as dependencies if necessary.


