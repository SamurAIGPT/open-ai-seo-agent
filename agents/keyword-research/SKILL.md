---
name: Keyword Research
slug: keyword-research
version: 2.0.0
category: seo
description: Discover, validate, expand, and prioritize SEO keywords using Muapi search data and live SERP evidence.
status: ready
muapi_capabilities:
  - seo.keyword_research
  - seo.keywords_search_volume
  - seo.keywords_for_keywords
  - seo.related_keywords
  - seo.keyword_overview
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

# Keyword Research

## Mission

Create a decision-ready keyword set, not a list of plausible phrases. Every
recommended term must have provider evidence for the selected market and a
clear intent or business role.

## Required inputs

- Seed topic, product, service, or explicit keyword list.
- Target country and language.
- Optional: business priority, audience, funnel stage, competitor domains,
  volume threshold, and maximum number of terms.

## Workflow

1. Read .seo/project.md when available and inherit its domain, market,
   language, business priorities, and existing keyword lists.
2. If a direct Search Console connection is available for the user's own
   property, query `gsc.search_analytics` first with query/page dimensions and
   a bounded high row limit. Filter striking-distance positions (roughly 5–20)
   client-side, preserve the actual rows, and enrich those queries with Muapi
   metrics before broad discovery.
3. Normalize seed terms by trimming whitespace and removing exact duplicates.
   Preserve the original wording in the report.
4. For a small number of topics, call seo.keyword_research to obtain seed
   metrics and ideas. For an explicit list, prefer
   seo.keywords_search_volume or seo.keyword_overview rather than one call per
   term.
5. Expand promising seeds with seo.keywords_for_keywords and
   seo.related_keywords. Keep expansion depth and limits modest until the user
   approves a broad run.
6. Deduplicate case, punctuation, and obvious singular/plural variants while
   retaining variants that may have different search intent.
7. Validate the final candidate set with the multi-keyword metrics endpoint
   available for the required fields. Preserve volume, difficulty, CPC, intent,
   and any provider confidence fields exactly as returned.
8. Call seo.google_serp for representative terms across each important intent
   and priority tier. Inspect ranking domains, result types, SERP features, and
   whether the query is actually relevant to the user's business.
9. Assign a business priority using explicit user priorities first, then
   provider metrics and SERP evidence. Send the terms to the keyword-clustering
   skill when several terms may map to one page.
10. Save source records and, if requested, a dated keyword research report.

## Decision rules

- Search volume is evidence of demand, not a promise of traffic.
- Search Console queries are first-party evidence of the user's existing demand;
  they do not replace market volume or difficulty metrics from Muapi.
- Difficulty, CPC, and intent must not be invented when absent from a response.
- Do not recommend a keyword solely because a competitor ranks for it.
- Use SERP evidence to distinguish informational, commercial, navigational,
  local, and mixed intent.
- Never create separate content targets for near-duplicate terms without
  checking SERP overlap.
- If the user supplies a minimum volume, apply it after preserving low-volume
  terms in an excluded section with the reason for exclusion.
- Keep market, language, device, and date consistent across comparisons.

## Output format

Return a prioritized table containing:

- cluster or topic
- primary keyword and variants
- provider search volume and difficulty, when returned
- intent and SERP format
- business priority
- recommended page or next action
- source record links

Also include excluded terms, assumptions, and missing fields.

When first-party data was available, identify which recommendations came from
the user's Search Console rows and which were expanded or validated with Muapi.

## Failure and missing-data behavior

If an endpoint returns partial ideas or no metrics, separate discovery from
validation and say which terms remain unvalidated. Do not turn a failed
provider call into a zero-volume conclusion.
