---
name: Content Gap
slug: content-gap
version: 2.0.0
category: seo
description: Find competitor-covered topics that a domain lacks or covers weakly, then turn them into non-cannibalizing content briefs.
status: ready
muapi_capabilities:
  - seo.domain_overview
  - seo.relevant_pages
  - seo.keyword_overview
  - seo.keywords_search_volume
  - seo.keywords_for_keywords
  - seo.google_serp
required_connections:
  - muapi
optional_connections:
  - google_search_console
first_party_capabilities:
  - gsc.search_analytics
permissions:
  - external-read-only
  - workspace-write
---

# Content Gap

## Mission

Identify demand-backed topics where competitors have visible coverage and the
user's domain has no or weak coverage. End with a page brief and intent
decision, not an unfiltered keyword dump.

## Required inputs

- User's domain.
- Two to five competitor domains.
- Country and language.
- Optional: topic scope, URL section, minimum volume, business priority, and
  maximum number of briefs.

## Workflow

1. Read .seo/project.md and confirm canonical domains and priority sections.
2. If connected, query the user's Search Console query/page performance to
   verify owned coverage and identify pages already earning impressions. Keep
   this first-party evidence separate from competitor estimates.
3. Call seo.domain_overview for the user's domain and each competitor with
   matching market, language, and useful limits.
4. Call seo.relevant_pages for the user domain when page-level coverage needs
   verification. Use returned pages as evidence, not as proof that a page
   satisfies an intent.
5. Normalize returned keyword records and create:
   - hard gaps: competitors rank in the available data and the user domain has
     no matching record
   - weak coverage: the user domain ranks, but competitors or current SERPs
     show a materially stronger result
   Treat both sets as bounded by provider result limits.
6. Expand important candidates with seo.keywords_for_keywords and validate the
   final terms with seo.keyword_overview or seo.keywords_search_volume.
7. Use seo.google_serp on representative terms to determine intent, dominant
   page format, ranking URL patterns, and SERP features.
8. Group near-duplicate terms into one cluster. Identify an existing page to
   refresh when evidence supports it; otherwise propose one new page.
9. Prioritize clusters using explicit business priority first, then validated
   demand, competitor coverage, intent fit, and effort. Label this as a
   calculated prioritization, not a provider score.
10. Save the source records and content-brief report.

## Decision rules

- A hard gap means absent from the returned dataset, not proof that the domain
  has never appeared.
- Do not propose one page per keyword variant.
- A competitor ranking does not prove that the topic is commercially valuable.
- Do not recommend a page when SERP evidence shows a different intent from the
  user's business.
- Keep volume thresholds user-configurable and preserve excluded candidates
  with reasons.
- Never copy competitor wording, claims, or content structure.

## Output format

For each brief, return:

- cluster and primary keyword
- secondary terms
- validated provider metrics
- gap type and competitor evidence
- current page or new-page recommendation
- intent and SERP format
- suggested audience, angle, and information requirements
- priority, confidence, and source links

## Failure and missing-data behavior

If a competitor has no keyword data, omit it from the diff and say why. If
metrics or SERPs are unavailable, label the brief provisional and do not
present it as a validated opportunity.
