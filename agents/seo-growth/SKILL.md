---
name: SEO Growth
slug: seo-growth
version: 2.0.0
category: seo
description: Find, validate, and prioritize ranking and organic-growth opportunities from domain, keyword, SERP, and page data.
status: ready
muapi_capabilities:
  - seo.domain_overview
  - seo.rank_track_batch
  - seo.keyword_overview
  - seo.keywords_search_volume
  - seo.google_serp
  - seo.relevant_pages
required_connections:
  - muapi
optional_connections:
  - google_search_console
  - google_analytics_4
first_party_capabilities:
  - gsc.search_analytics
  - ga4.organic_landing_pages
  - ga4.key_events
permissions:
  - external-read-only
  - workspace-write
---

# SEO Growth

## Mission

Turn current domain visibility into a ranked list of opportunities with a
specific page or content lever. Focus on evidence-supported page-two wins,
weakly covered topics, and validated new opportunities.

## Required inputs

- Target domain.
- Country, language, and device.
- Optional: priority products, services, URL groups, keyword list, and
  comparison date.

## Workflow

1. Read .seo/project.md and any compatible ranking snapshot.
2. If direct Google connections are available, query Search Console for the
   user's actual queries/pages and GA4 for organic landing-page or key-event
   context. Keep those first-party observations separate from Muapi estimates.
3. Call seo.domain_overview with a useful limit to establish the domain's
   visible keywords, pages, distribution, and provider-listed competitors.
4. Segment returned keywords into page-one, page-two, and lower-visibility
   groups. Treat the returned limit as a sampling boundary; do not call the
   result exhaustive if the provider returned only a subset.
5. For the highest-value candidates, call seo.rank_track_batch with the exact
   keyword list and confirmed target domain. Keep batches to 50 or fewer and
   preserve the search context.
6. Validate opportunity metrics with seo.keyword_overview or
   seo.keywords_search_volume. Use the endpoint that supplies the requested
   fields and keep the provider's currency, period, and null values.
7. Call seo.relevant_pages when a page assignment is unclear. Use
   seo.google_serp for representative terms to inspect the current result
   format, ranking URLs, and SERP features.
8. Classify each opportunity as refresh, internal-linking, consolidation,
   technical investigation, or new content. Explain the evidence for the
   chosen lever.
9. Save a dated report and source records when requested.

## Decision rules

- Page-two terms are a useful prioritization heuristic, not a guaranteed win.
- Favor business-priority pages over volume alone when the user supplied those
  priorities.
- Never recommend a new page without validating demand and intent.
- Do not call a page a cannibalization or technical problem without page or SERP
  evidence.
- Separate provider metrics from calculated priority.
- Use Search Console for the user's own query/page opportunity and GA4 for
  landing-page or key-event impact when connected; do not replace either with
  third-party estimates.
- A missing rank is not automatically a rank of zero.

## Output format

Return an opportunity table with:

- keyword and current position
- ranking URL
- search volume, difficulty, and intent when returned
- page or cluster
- evidence from the domain, rank, and SERP calls
- recommended lever
- priority and rationale
- source links

## Failure and missing-data behavior

If the domain has no ranked keywords, switch to topic-led keyword research and
state that there are no observed quick wins. If only a subset is returned,
state the coverage boundary.
