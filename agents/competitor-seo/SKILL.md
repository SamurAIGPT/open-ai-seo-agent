---
name: Competitor SEO
slug: competitor-seo
version: 2.0.0
category: seo
description: Compare a domain with relevant competitors across visibility, rankings, SERPs, pages, and backlinks.
status: ready
muapi_capabilities:
  - seo.domain_overview
  - seo.relevant_pages
  - seo.rank_track_batch
  - seo.google_serp
  - seo.backlinks
  - seo.backlinks_pages
  - seo.backlinks_history
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Competitor SEO

## Mission

Explain where competitors have a measurable search advantage and what evidence
could account for it. Produce comparable observations, not speculation about
competitor strategy.

## Required inputs

- User's domain.
- Two to five competitor domains, or permission to use provider-listed
  competitors as research candidates.
- Country, language, device, and keyword/topic scope.
- Optional: previous snapshot and comparison window.

## Workflow

1. Confirm canonical domains and remove duplicates or domains that are not
   actual search competitors. Keep provider-discovered candidates separate from
   user-confirmed competitors.
2. Call seo.domain_overview for the user's domain and each competitor with
   matching market, language, and limit.
3. Call seo.relevant_pages for the user's domain and selected competitors when
   page-level content or linked-page comparison is needed.
4. Build a comparable keyword set from the user's list, compatible snapshots,
   and returned ranked keywords. Do not treat different limits as equal
   coverage.
5. Run seo.rank_track_batch for the same keyword chunks and same search context
   against each domain. Ask before a wide multi-domain batch.
6. Use seo.google_serp for representative high-value queries to verify current
   ranking URLs, SERP features, and result formats.
7. For material differences, call seo.backlinks and, when change over time is
   requested, seo.backlinks_pages and seo.backlinks_history with compatible
   dates. A backlink correlation is not proof of causation.
8. Save compatible snapshots, calculate overlaps and position deltas, and
   produce one evidence-backed opportunity per important gap.

## Decision rules

- A domain listed as a SERP competitor may not be a business competitor.
- Compare like-for-like market, language, device, depth, keyword, and date
  context.
- Require a consistent multi-keyword pattern before describing a broad gain.
- Attribute a change to links, content, or SERP format only when the relevant
  data supports that hypothesis; otherwise say unclear.
- Do not copy competitor content or recommend copying their structure.
- A backlink count is not a measure of link quality by itself.

## Output format

Return:

- competitor scope and relevance notes
- visibility and keyword-overlap table
- shared-keyword ranking comparison
- representative live SERP observations
- page and backlink comparison where requested
- likely driver labelled observed, calculated, or hypothesized
- prioritized response opportunities
- source and snapshot links

## Failure and missing-data behavior

If one domain has no data, keep it in an explicit unavailable section and
continue only with comparisons that remain valid. Never fill a competitor's
missing metrics from another domain.
