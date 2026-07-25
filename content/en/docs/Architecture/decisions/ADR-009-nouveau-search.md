---
title: "ADR-009: Modernize Nouveau Search Architecture"
linkTitle: "ADR-009: Using CouchDB Nouveau for Search"
weight: 9
---

# Decision Analysis and Resolution: CouchDB Nouveau Search Architecture Modernization

**Created by:** SW360 Architecture Team
**Decision Date:** July 2026
**Status:** Proposed

---

## Table of Contents

1. [Context and Problem Statement](#1-context-and-problem-statement)
2. [Goal](#2-goal)
3. [Key Principles](#3-key-principles)
4. [Options Analysis](#4-options-analysis)
   - [Status Quo](#41-status-quo)
   - [Edge N-Gram Indexing with Tiered Conjunction Querying](#42-edge-n-gram-indexing-with-tiered-conjunction-querying)
5. [Criteria for Making a Decision](#5-criteria-for-making-a-decision)
   - [Positive Consequences](#51-positive-consequences)
   - [Negative Consequences](#52-negative-consequences)
6. [Technical Specification](#6-technical-specification)
   - [CouchDB Nouveau Design Document Definition](#61-couchdb-nouveau-design-document-definition)
   - [Reference Java Implementation](#62-reference-java-implementation)
   - [Native Nouveau Sorting Matrix](#63-native-nouveau-sorting-matrix)

---

## 1. Context and Problem Statement

The current SW360 search mechanism constructs queries by appending trailing
wildcards to every input token (`term1* OR term2* OR term3*`). While this
maximizes recall for unknown terms, it causes severe issues in production
environments:
1. **High Noise & Poor Precision:** For multi-word queries (e.g.,
  `"My test project"`), the default OR logic matches any document containing
  any word starting with those prefixes, returning hundreds of irrelevant
  entries (e.g., 340+ results) instead of the few actual matches.
2. **Performance Penalties:** Query-time `*` wildcards bypass standard Lucene
  token analysis and force expensive term-expansion scans across inverted
  index segments.
3. **Legacy Generic Concatenation:** Global generic searches rely on manually
  concatenating strings into custom `all` fields, destroying field token
  boundaries and preventing field-specific relevance scoring.
4. **Inefficient Cluster Pagination:** Requesting page $N$ in the REST backend
  currently executes $N$ sequential HTTP requests to CouchDB to walk the
  bookmark chain. In a multi-node CouchDB cluster, sequential bookmark
  requests can land on different cluster nodes, creating unnecessary
  inter-node RPC overhead and potential bookmark state mismatches.
5. **Redundant Sorting Overhead:** Search results sorted by UI columns undergo
  double-sorting—once in Lucene and again in Java memory via Comparator calls
  after document hydration.

We need a search architecture that brings "Google-like" precision (exact matches
at #1, minimal noise) while preserving fast prefix matching, native catch-all
search capabilities, stateless high-performance cluster pagination, and
offloading multi-field sorting entirely to the search engine.

---

## 2. Goal

The end goal is to implement a modernized search architecture for SW360 that:
- Provides high precision and recall for user queries, minimizing irrelevant
  results.
- Reduces query execution time and resource consumption in CouchDB clusters.
- Supports stateless pagination and efficient sorting without redundant
  processing.

One of the biggest problem currently experienced by users is the noise in search
results. For example, they created a project called "My test Project" and when
searching for it next day, they get results like
* "A test project" (noise)
* "Aa project" (noise)
* "My test project" (actual match)
* "Test project" (noise)

On an environment with 10000+ projects, for a simple query, you might get 700+
results back and you'd have to scroll through them manually to find the actual
match.

The goal is to reduce the noise in search results and provide a more accurate
and efficient search experience for users, while also improving the performance
of the search functionality in the SW360 application.

The major change is to move away from current `"word1*" OR "word2*"` style
queries to a more structured query approach that leverages CouchDB Nouveau's
capabilities for Lucene-based full-text search. Improve the search query
construction to `"word1" AND "word2*"` style queries, reducing the irrelevant
results. At the same time, use Lucene's scoring and ranking capabilities to
ensure that the most relevant results are returned first, improving the overall
user experience.

---

## 3. Key Principles

* **Precision & Relevance:** Exact phrase matches must automatically rank at
  position #1.
* **Low Noise:** Search for 3–4 word project names should return only matching
  documents rather than hundreds of partial-match hits.
* **Native Catch-All Search:** Utilize CouchDB Nouveau's reserved `default`
  field pattern instead of manual string concatenation.
* **Stateless Cluster-Friendly Pagination:** Calculate top-$N$ offsets
  (`limit = pageNumber * pageSize`) to execute 1 single request to CouchDB
  Nouveau per page jump, slicing the result page in Java memory. This eliminates
  multi-node bookmark dependencies and keeps the REST layer completely
  stateless.
* **Architectural Simplicity:** Eliminate redundant Java-side in-memory sorting
  by utilizing native CouchDB Nouveau multi-field sorting.
* **Query Performance (additional):** Prefix searching should operate in $O(1)$
  time rather than requiring expensive query-time wildcard expansions.

---

## 4. Options Analysis

### 4.1. Status Quo

**Option 1: Status Quo (Query-Time Wildcards + Manual String Concatenation +
$N$-Sequential Bookmarks + Java Re-Sorting)**
* Retain trailing `*` on every token, concatenate strings for generic searches,
  and rely on Java-side post-processing to re-rank and filter results.

### 4.2. Edge N-Gram Indexing with Tiered Conjunction Querying

**Option 2: CouchDB Nouveau with JS Index-Time Edge N-Grams, Tiered Conjunction
(`AND`) Querying, Single-Query Top-$N$ Offset Slicing, and Native Sorting**
* Index catch-all content under Nouveau's reserved "`default`" field name for
  field-less generic searches.
* Generate prefix N-gram tokens directly inside the CouchDB Nouveau JavaScript
  `index()` function, assigned to standard Lucene analyzers (`whitespace` /
  `standard` / `keyword`).
* Use a 2-tier query structure enforcing `AND` conjunction logic with phrase
  boosting (`^100`).
* Request `limit = pageNumber * pageSize` in a single HTTP call to CouchDB and
  extract the target page sublist in Java memory (`subList`).
* Index dedicated un-analyzed `string` fields for native Lucene column sorting
  and tie-breaking.

---

## 5. Criteria for Making a Decision

The single biggest pain point for the SW360 user community is the high noise in
search results. The current search architecture returns hundreds of irrelevant
results for multi-word queries. This is best when you don't know what you are
looking for, but remember only a fragment. However, when you know the exact
thing you want and search for it, the results are so noisy that users generally
give up on the results. Instead, they have started to share direct links to one
another. The single most important criterion for making a decision is to reduce
the noise in search results and provide a more accurate and efficient search
experience for users. If in the process of achieving this, we could also improve
the performance of the search functionality in the SW360 application, that would
be a bonus. The following criteria were considered in making the decision:
1. **Precision & Relevance:** The new search architecture must return exact
  phrase matches at the top of the results list.
2. **Low Noise:** The new search architecture must return only matching
  documents for multi-word queries, rather than hundreds of partial-match hits.

### 5.1. Positive Consequences

* **Native Generic Search:** Utilizing Nouveau's reserved "`default`" field
  removes artificial string concatenation and preserves proper token boundaries
  for global search bar inputs.
* **Instant Prefix Lookup:** JS-generated Edge N-Grams turn prefix searches into
  exact inverted index term lookups ($O(1)$ time).
* **100% CouchDB Nouveau Compliant:** Uses standard named analyzer strings
  (`"standard"`, `"whitespace"`, `"keyword"`) supported by Nouveau's
  `default_analyzer` and `field_analyzers` options.
* **Cluster-Safe Stateless Pagination:** Single top-$N$ requests eliminate
  $N$-sequential bookmark calls and work seamlessly across load-balanced
  multi-node CouchDB clusters without needing sticky sessions or external
  caching layers.
* **Noise Reduction:** Switching default multi-word queries from loose `OR` to
  strict `AND` conjunction reduces result sets from 300+ entries down to exact
  matches.
* **Exact Match Launching:** Tier 1 phrase boosting (`^100`) guarantees that
  exact matches always rocket to position #1.
* **Zero Java Re-sorting:** CouchDB Nouveau returns results pre-sorted by
  Lucene, removing duplicate Java Comparator sorting overhead.

### 5.2. Negative Consequences

* **Index Size Growth:** Pre-computing N-Gram tokens increases disk usage for
  CouchDB Nouveau index segments (typically 15–25% increase).
* **Re-indexing Required:** Existing CouchDB databases must re-index documents
  against the new Nouveau design document.

---

## 6. Technical Specification

### 6.1. CouchDB Nouveau Design Document Definition

Note: In CouchDB Nouveau, `default_analyzer` and `field_analyzers` map field
names to built-in Lucene analyzer names (`"standard"`, `"whitespace"`,
`"keyword"`, `"english"`, etc.). Custom token filters like `edge_ngram` are
generated directly within the JavaScript `index()` function.

```json
{
  "_id": "_design/sw360_search",
  "nouveau": {
    "indexes": {
      "projects": {
        "default_analyzer": "standard",
        "field_analyzers": {
          "default": "standard",
          "default_ngram": "whitespace",
          "name_exact": "standard",
          "name_ngram": "whitespace",
          "version_ngram": "keyword",
          "tag_ngram": "whitespace"
        },
        "index": "function(doc) {
          if (doc.type === 'project') {

            // Helper function to generate Edge N-Grams in JavaScript
            function emitEdgeNGrams(fieldName, text, minGram, maxGram) {
              if (!text) return;
              var words = text.toLowerCase().split(/\\s+/);
              for (var i = 0; i < words.length; i++) {
                var word = words[i];
                var limit = Math.min(word.length, maxGram);
                for (var len = minGram; len <= limit; len++) {
                  index('text', fieldName, word.substring(0, len));
                }
              }
            }

            // --- 1. RESERVED 'DEFAULT' FIELD (CATCH-ALL GENERIC SEARCH) ---
            if (doc.name) {
              index('text', 'default', doc.name);
              emitEdgeNGrams('default_ngram', doc.name, 2, MAX_GRAM_BOUND);
            }
            if (doc.description) {
              index('text', 'default', doc.description);
            }
            if (doc.version) {
              index('text', 'default', doc.version);
            }
            if (doc.tag) {
              index('text', 'default', doc.tag);
            }

            // --- 2. SPECIFIC FIELD PREFIX & EXACT FIELDS ---
            if (doc.name) {
              index('text', 'name_exact', doc.name);
              emitEdgeNGrams('name_ngram', doc.name, 2, 25);
              index('string', 'name_sort', doc.name.toLowerCase());
            }

            if (doc.version) {
              var ver = doc.version.toLowerCase();
              emitEdgeNGrams('version_ngram', ver, 1, ver.length);
              index('string', 'version_sort', ver);
            }

            if (doc.tag) {
               emitEdgeNGrams('tag_ngram', doc.tag, 2, 10);
            }

            // --- 3. EXACT MATCH ONLY FIELDS ---
            if (doc.license) {
              index('string', 'license', doc.license);
            }

            // --- 4. SORTABLE NUMERIC / DATE FIELDS ---
            if (doc.createdOn) {
              index('double', 'created_on', doc.createdOn);
            }
          }
        }"
      }
    }
  }
}
```

### 6.2. Reference Java Implementation

The following service utility constructs Nouveau queries, supports reserved
`default` generic searches, and provides simple offset limit calculation for
single-query page extraction:

```java
package org.eclipse.sw360.datahandler.search;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SW360NouveauSearchBuilder {

    private static final int MAX_GRAM_CAP = 25;

    /**
     * Constructs a tiered Lucene query string for a target field.
     */
    public static String buildFieldQuery(String fieldExact, String fieldNgram, String rawInput) {
        if (rawInput == null || rawInput.trim().isEmpty()) {
            return "*:*";
        }

        String trimmed = rawInput.trim();

        // Exact phrase search if quoted
        if (trimmed.startsWith("\"") && trimmed.endsWith("\"") && trimmed.length() > 2) {
            String phrase = trimmed.substring(1, trimmed.length() - 1);
            // + name_exact:"My test project"
            return "+" + fieldExact + ":\"" + sanitizeLuceneChars(phrase) + "\"";
        }

        String[] tokens = Arrays.stream(trimmed.split("\\s+"))
                .map(SW360NouveauSearchBuilder::sanitizeLuceneChars)
                .filter(s -> !s.isEmpty())
                .toArray(String[]::new);

        if (tokens.length == 0) {
            return "*:*";
        }

        // Single-word query pattern
        if (tokens.length == 1) {
            String token = capToken(tokens[0].toLowerCase());
            // (name_exact:my^100 OR name_ngram:my)
            return String.format("(%s:%s^100 OR %s:%s)", fieldExact, token, fieldNgram, token);
        }

        // Multi-word tiered query pattern
        String fullPhrase = String.join(" ", tokens);
        String phraseClause = fieldExact + ":\"" + fullPhrase + "\"^100";

        StringBuilder andClause = new StringBuilder();
        andClause.append("(");
        for (int i = 0; i < tokens.length; i++) {
            if (i > 0) {
                andClause.append(" AND ");
            }
            if (i == tokens.length - 1) {
                // Last token uses n-gram for prefix matching
                andClause.append(fieldNgram).append(":").append(capToken(tokens[i].toLowerCase()));
            } else {
                // Earlier tokens use exact match
                andClause.append(fieldExact).append(":").append(tokens[i].toLowerCase());
            }
        }
        andClause.append(")");

        /*
         * (
         *   name_exact:"My test project"^100
         *   OR
         *   (
         *     name_exact:my AND name_exact:test AND name_ngram:project
         *   )
         * )
         */
        return String.format("(%s OR %s)", phraseClause, andClause.toString());
    }

    /**
     * Constructs generic "search anything" bar queries targeting reserved 'default' fields.
     */
    public static String buildGenericQuery(String genericInput) {
        return buildFieldQuery("default", "default_ngram", genericInput);
    }

    /**
     * Combines multiple explicit field criteria into a composite query.
     */
    public static String buildCompositeQuery(String nameInput, String version, String tag, String vendor) {
        List<String> clauses = new ArrayList<>();

        if (nameInput != null && !nameInput.trim().isEmpty()) {
            clauses.add("+(" + buildFieldQuery("name_exact", "name_ngram", nameInput) + ")");
        }
        if (version != null && !version.trim().isEmpty()) {
            clauses.add("+version_ngram:" + capToken(sanitizeLuceneChars(version.trim().toLowerCase())));
        }
        if (tag != null && !tag.trim().isEmpty()) {
            clauses.add("+tag_ngram:" + capToken(sanitizeLuceneChars(tag.trim().toLowerCase())));
        }
        if (vendor != null && !vendor.trim().isEmpty()) {
            clauses.add("+vendor:\"" + sanitizeLuceneChars(vendor.trim()) + "\"");
        }

        if (clauses.isEmpty()) {
            return "*:*";
        }

        /*
         * +(name_exact:"My test project"^100 OR (name_exact:my AND name_exact:test AND name_ngram:project))
         * AND
         * +version_ngram:1.0.0
         * AND
         * +tag_ngram:department
         * AND
         * +vendor:"eclipse"
         */
        return String.join(" AND ", clauses);
    }

    /**
     * Maps UI column sort requests directly to Nouveau sort parameters.
     * Uses more than 1 tiebreaker field to ensure deterministic sort order for identical values.
     */
    public static List<String> buildSortParameters(String uiColumn, boolean isAscending) {
        String direction = isAscending ? "" : "-";

        if (uiColumn == null || uiColumn.isEmpty() || "score".equalsIgnoreCase(uiColumn)) {
            return List.of("<score>", "name_sort<string>", "version_sort<string>");
        }

        return switch (uiColumn.toLowerCase()) {
            case "name" -> List.of(direction + "name_sort<string>", "<score>", "version_sort<string>");
            case "version" -> List.of(direction + "version_sort<string>", "name_sort<string>", "<score>");
            case "vendor" -> List.of(direction + "vendor_sort<string>", "name_sort<string>", "<score>");
            case "createdon", "date" -> List.of(direction + "created_on<double>", "name_sort<string>");
            default -> List.of(direction + uiColumn + "<string>", "<score>");
        };
    }

    /**
     * Calculates the top-N limit to fetch from CouchDB Nouveau in a single query.
     */
    public static int calculateFetchLimit(int pageNumber, int pageSize) {
        int page = Math.max(1, pageNumber);
        int size = Math.max(1, pageSize);
        return page * size;
    }

    /**
     * Extracts the requested page sublist in Java memory from the single top-N result set.
     */
    public static <T> List<T> extractPageSublist(List<T> allHits, int pageNumber, int pageSize) {
        if (allHits == null || allHits.isEmpty()) {
            return List.of();
        }
        int page = Math.max(1, pageNumber);
        int size = Math.max(1, pageSize);

        int startIndex = (page - 1) * size;
        if (startIndex >= allHits.size()) {
            return List.of();
        }
        int endIndex = Math.min(startIndex + size, allHits.size());
        return allHits.subList(startIndex, endIndex);
    }

    private static String capToken(String token) {
        return token.length() > MAX_GRAM_CAP ? token.substring(0, MAX_GRAM_CAP) : token;
    }

    private static String sanitizeLuceneChars(String input) {
        if (input == null) return "";
        return input.replaceAll("([+\\-!\\(\\)\\{\\}\\[\\]\\^\"\\~\\*\\?\\:\\\\/])", "\\\\$1")
                .replaceAll("&&", "\\\\&&")
                .replaceAll("\\|\\|", "\\\\||")
        ;
    }
}
```

### 6.3. Native Nouveau Sorting Matrix

| User Action                 | Nouveau "sort" Parameter                                    | Description                                                                 |
|-----------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------------|
| Default Search              | `["<score>", "name_sort<string>", "version_sort<string>"]`  | Ranks exact phrase matches (#1) by BM25 score, tie-breaking alphabetically. |
| Sort by Name (asc)          | `["name_sort<string>", "<score>", "version_sort<string>"]`  | Pure alphabetical sort with score as secondary tie-breaker.                 |
| Sort by Version (desc)      | `["-version_sort<string>", "name_sort<string>", "<score>"]` | Descending version sort with multi-field tie-breaking.                      |
| Sort by Created Date (desc) | `["-created_on<double>", "name_sort<string>"]`              | Sorts newest first.                                                         |

---

*This program and the accompanying materials are made available under the terms of the Eclipse Public License 2.0 which is available at https://www.eclipse.org/legal/epl-2.0/*
