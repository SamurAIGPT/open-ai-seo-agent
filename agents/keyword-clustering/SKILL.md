---
name: Keyword Clustering
slug: keyword-clustering
version: 2.0.0
category: seo
description: Group keywords into intent-led page opportunities using metrics, live SERP overlap, and existing relevant pages.
status: ready
muapi_capabilities:
  - seo.keyword_overview
  - seo.google_serp
  - seo.relevant_pages
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Keyword Clustering

## Mission

Map a keyword set to the smallest sensible set of pages. Use shared ranking
URLs and SERP composition as evidence of intent; semantic similarity alone is
not enough.

## Required inputs

- A keyword list or a source report from Keyword Research.
- Target domain when existing page mapping is requested.
- Country, language, and device.
- Optional: maximum clusters, page types, and business priorities.

## Workflow

1. Read the source keyword list and preserve its metrics and provenance.
2. Normalize terms for comparison but retain the original text and spelling.
3. Call seo.keyword_overview for explicit terms when metrics are absent or
   need to be made comparable.
4. Group obvious variants provisionally by topic, modifier, and funnel intent.
5. Select representative terms from each provisional group. Call
   seo.google_serp for those terms using the same market, language, device, and
   depth. Do not call every term unless the user asks for exhaustive evidence.
6. Compare the top organic URLs and result types. Merge terms when the same
   pages and intent dominate; split terms when the SERP leaders or user intent
   differ materially.
7. Call seo.relevant_pages for the target domain when the user wants existing
   page assignments. Match returned pages to clusters only with URL or topic
   evidence; do not claim a page covers a topic from its URL alone.
8. Assign one primary term per cluster, preserve secondary terms, and mark the
   page target as existing page, refresh candidate, or new page.
9. Save the cluster table and the representative SERP sources.

## Decision rules

- One cluster should represent one search intent and one primary page outcome.
- SERP overlap is supporting evidence, not a fixed universal threshold.
- Do not split terms merely because their wording differs.
- Do not merge terms when the user intent, result format, or dominant URLs
  materially differs.
- Flag ambiguous clusters for human review instead of forcing a decision.
- Do not recommend a new page when a suitable existing page is evidenced.

## Output format

Return:

- cluster name and primary keyword
- secondary keywords
- provider metrics
- intent and SERP-format evidence
- shared and differing ranking URLs
- existing target page, if evidenced
- recommended page action
- confidence and source links

## Failure and missing-data behavior

If representative SERPs cannot be retrieved, return provisional clusters
labelled as metric/semantic groupings and state that cannibalization risk is
unverified.
