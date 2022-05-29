For the filters that are shown for components and listings, there are some options:

1. The **Keyword search** works directly on the table shown on the main right area. For example in the components portlet, this is in components/view.jsp. 

2. The **filters** actually result in a new search request, when hitting apply filters button. The project portlet reads the fields and creates a map. Then, `ProjectPortlet` calls the thrift service `refineSearch()`, which is handled in `ProjectHandler`. This method takes the map and the user as input. The search service has a server-side JavaScript function (LuceneSearchView) defined for this particular filter in `ProjectSearchHandler.java`. This is called with the `LuceneAwareDatabaseConnector.java`. After filtering, the visibility constraints for the requesting user are applied. 

3. Then for each release table, there is a search field in the upper right corner. This again works on the data of the Release summary object and then filters what is on the client (web browser).