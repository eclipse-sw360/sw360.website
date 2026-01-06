---
title: "How to add a backend portlet to sw360"
linkTitle: "Add backend portlet"
weight: 10
---

This page how to add some operations / service calls on the backend for the portlet writing on the page that covers the front end. Note that this page does not create a new (thrift service), but just explains how to add more operations.

This explanation follows bottom up approach where we first add the backend methods and then call them later in the frontend. Quick summary:

1. Add methods to the thrift idl definition
1. Add methods to the data handler interface
1. Add implementation
1. Add tests

## Thrift

First we add some methods to the thrift files, components.thrift
```java
//new Methods to ensure uniqueness of Identifiers
map <string, list<string>> getDuplicateComponents();
map <string, list<string>> getDuplicateReleases();
```

## Datahandler

then we install lib-datahandler. That way we see which methods we have to implement.
We have chosen to change the interface of the ComponentService. That means we need to implement them in the ComponentHandler.

```java
@Override
public Map<String, List<String>> getDuplicateComponents() throws TException {
    return handler.getDuplicateComponents();
}

@Override
public Map<String, List<String>> getDuplicateReleases() throws TException {
    return handler.getDuplicateReleases();
}
```

## Implementation

The methods there are only a reference to the ComponentDatabaseHandler.java. 
In the ComponentHandler we only assert that the input is correct. 
Since we implement methods without parameters, there is nothing else for us to do.
In the ComponentDatabaseHandler.java we actually do some work and implement the methods

```java
public Map<String, List<String>> getDuplicateComponents() {
    ListMultimap<String, String> componentIdentifierToComponentId = ArrayListMultimap.create();

    for (Component component : componentRepository.getSummaryForExport()) {
        componentIdentifierToComponentId.put(SW360Utils.printName(component), component.getId());
    }
    return CommonUtils.getIdentifierToListOfDuplicates(componentIdentifierToComponentId);
}

public Map<String, List<String>> getDuplicateReleases() {
    ListMultimap<String, String> releaseIdentifierToReleaseId = ArrayListMultimap.create();

    for (Release release : releaseRepository.getReleaseSummary()) {
        releaseIdentifierToReleaseId.put(SW360Utils.printName(release), release.getId());
    }

    return CommonUtils.getIdentifierToListOfDuplicates(releaseIdentifierToReleaseId);
}
```

## Tests

We then write some tests in ComponentDatabaseHandlerTest.java

```java
@Test
public void testDuplicateComponentIsFound() throws Exception {
    String originalComponentId = "C3";
    final Component tmp = handler.getComponent(originalComponentId, user1);
    tmp.unsetId();
    tmp.unsetRevision();
    String newComponentId = handler.addComponent(tmp, email1);

    final Map<String, List<String>> duplicateComponents = handler.getDuplicateComponents();

    assertThat(duplicateComponents.size(), is(1));
    assertThat(duplicateComponents.get(printName(tmp)), containsInAnyOrder(newComponentId,originalComponentId));

}


@Test
public void testDuplicateReleaseIsFound() throws Exception {

    String originalReleaseId = "R1A";
    final Release tmp = handler.getRelease(originalReleaseId, user1);
    tmp.unsetId();
    tmp.unsetRevision();
    String newReleaseId = handler.addRelease(tmp, email1);

    final Map<String, List<String>> duplicateReleases = handler.getDuplicateReleases();

    assertThat(duplicateReleases.size(), is(1));
    assertThat(duplicateReleases.get(printName(tmp)), containsInAnyOrder(newReleaseId,originalReleaseId));
}
```

Then we install the backend to make our methods available.
