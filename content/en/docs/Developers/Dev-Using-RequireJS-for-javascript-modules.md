# Status quo
Today most of the javascript code runs in the global namespace. This increases the risk of overwriting symbols in the global namespace due to different libraries and snippets.

# Goal
We want to use RequireJS (http://requirejs.org/) to modularize our code and to have clear namespaces for each component. In addition some of the code may be reused more easily. Other advantages:
- libraries like jquery or datatables can be imported by name but without a specified version
- if necessary, specific versions can be imported for parts of the page
- it is very easy to only load needed dependencies
- good support of webjars due to webjars-locator. Webjars a are automatically accessible through RequireJS.

# How to use - example
There is a new jspf-file to be included in jsps to enable RequireJS support:

    <%@ include file="/html/utils/includes/requirejs.jspf" %>

When RequireJS is enabled with the above include, all libraries can be accessed and code can be scoped:

    require(['jquery', 'module/quickfilter', 'module/confirm', /* jquery-plugins: */ 'datatables', 'jquery-ui'], function($, quickfilter, confirm) {
        // code goes here, libraries can be used through the variables $, quickfilter and confirm
        // Note: jquery-plugins does not have to be bound to variables since they directly register themselves in the jquery object
    });

**NOTE/WARNING**: since not all code is using RequireJS at the moment it is highly recommended to include RequireJS just before the script tag using it. DO NOT include it at the beginning of the file! Therefore use the following pattern:

    <%@ include file="/html/utils/includes/requirejs.jspf" %>
    <script>
        require(['jquery'], function($) {
            // js stuff
        });
    </script>

**Explanation**: some the the jQuery-plugins are already module safe. This means the look if something like RequireJS is available and - if this is the case - register themselves as anonymous modules. If someone in some include in the page loads such a plugin via script plugin it may happen that the plugins registers itself twice as an anonymous module which causes errors in RequireJS. Loading RequireJS after all script tags will prevent this and ensure that every plugin is only registered once.

# Migration
## Migrate a JSP
To migrate a JSP to use RequireJS the following steps have to be done:

1. Enable RequireJS support by including `requirejs.jspf`. Do it JUST before the script tag with the main code (see NOTE above).
1. Enclose the existing code in a `require`-function (**Attention:** Also read "Co-existence with AUI().use()" below)
1. Remove existing `script`-tags that loads the javascript files "manually"
1. Rewrite code that access functions inside the new `require`-function from outside (e.g. click handlers, see below)

## Co-existence with AUI().use()
If you need to use AUI().use() in your code, e.g. to grab the PortletURL object, you have to call this function first and call `require` inside. Otherwise the code may not be executed correclty if the 'Drag&Drop' error occurs to early during page loading:

    AUI().use('liferay-portlet-url', function () {
        require(['jquery', 'module/quickfilter') {
            // AUI and require modules loaded and available
        });
    });

## Migrate click-handlers
Since none of the defined functions remains in the global scope click handlers defined in the attributes of a tag would no longer work. Use jQuery to attach a click handler instead:

    $('#exportSpreadsheetButton').on('click.components', exportSpreadsheet)

This click handler is added inside the RequireJS-scope where the function `exportSpreadsheet` is defined.
You may also attach handler for distinct elements in each row of a table:

    $('#componentsTable').on('click.components', 'img.delete', function(event) {
         // do stuff
    });

## Make a module out of a jspf-include
There are many jspf-includes which contain html as well as javascript code. They should be converted as followed:

1. Move the javascript code to an own file. Place it below the 'html/js'-folder, following the same structure as the jspf-file. If the jspf-file is `html/components/includes/vendors/addVendor.jspf` place the javascript code in the file `js/components/includes/vendors/addVendor.js`.

1. Enclose the code in a define statement to define a new module:

        define('components/includes/vendors/addVendor', [ /* dependencies */ ], function() {
            // define module code
        });

In order to use the new module include the jspf-file and load the js-code via RequireJS:

    <%@ include "html/components/includes/vendors/addVendor.jspf" %>
        
    require(['components/includes/vendors/addVendor'], function(addVendor) {
        // use addVendor
    });

## Make a module out of a javascript file or function
There are several javascript files and functions below `/html/js'. They can be make compatible to RequireJS as follows:

1. Create a new file inside `/html/js/component` with a proper name that describes the functionality for the new component
1. Define the module and point to the legacy function, e.g.

        define('module/confirm', ['jquery', /* jquery-plugins: */ 'jquery-confirm', /* legacy code */ 'main' ], function($) {
            return {
                confirmDeletion: deleteConfirmed /* pointer to legacy method in main.js */
            };
        });

1. Afterwards the module can be loaded using the name `component/confirm`, e.g.

        require(['module/confirm'], function(confirm) {
            confirm.confirmDeletion(/*...*/);
        });

**Note** The legacy function should be moved inside the module as soon as the function is no longer accessed directly but via RequireJS only.
**Note** You can also require legacy javascript files if you need them as dependency as pointed out in the examples above.



 