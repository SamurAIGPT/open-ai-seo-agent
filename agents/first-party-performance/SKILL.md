---
name: First-Party Performance
slug: first-party-performance
version: 1.0.0
category: seo
description: Analyze the user's own Search Console and Analytics data through direct, user-authorized Google connections.
status: ready
muapi_capabilities: []
first_party_capabilities:
  - gsc.list_sites
  - gsc.search_analytics
  - gsc.inspect_urls
  - ga4.list_properties
  - ga4.organic_landing_pages
  - ga4.page_performance
  - ga4.key_events
  - ga4.organic_overview
  - ga4.traffic_acquisition
  - ga4.ecommerce_performance
  - ga4.site_search
  - ga4.audience_breakdown
  - ga4.measurement_health
required_connections: []
optional_connections:
  - google_search_console
  - google_analytics_4
permissions:
  - external-read-only
  - workspace-write
---

# First-Party Performance

## Mission

Use the user's own Google Search Console and Google Analytics 4 properties as
the authoritative source for first-party search demand, landing-page
performance, and conversion context. These connections are direct user
connections; they are not Muapi tasks.

This skill is for the user's own verified properties only. Use Muapi for
competitors, third-party domains, live SERPs, keyword market data, backlinks,
and other external datasets.

## Use this skill when

- The user asks what already earns impressions, clicks, or conversions.
- The user wants to find striking-distance queries or underperforming landing
  pages.
- The user asks whether an SEO change affected traffic or key events.
- A keyword, content, competitor, or growth report needs a first-party baseline.

## Required inputs

- The user's domain or Search Console property.
- Date range and comparison range.
- Country, device, query, page, or channel dimensions when relevant.
- Optional: GA4 property, key-event names, landing-page section, and business
  priority.

## Direct connection contract

The host agent or connector must:

- let the user select a verified Search Console property
- let the user select an accessible GA4 property
- use OAuth or the host's native Google connection flow
- request only read permissions
- return structured rows and metadata, not screenshots
- identify the selected property, date range, timezone, dimensions, filters, and
  retrieval time
- never expose access tokens in prompts, reports, or source files

The logical capabilities are defined in
references/google-first-party-data.md. Setup requirements and the Google API
mapping are in references/google-setup.md. A host may map the logical
capabilities to different tool names, but it must preserve their semantics.

When the host exposes the recommended names, use
`get_search_console_performance` and `inspect_urls` for Search Console, and
`get_google_analytics_*` tools for Analytics. Do not ask the user to export a
CSV when a connected read-only tool is available.

## Workflow

1. Read .seo/project.md and confirm that the selected Search Console property
   matches the canonical domain. Do not silently substitute a domain variant.
2. Check which direct connections are available. If neither is connected,
   explain how the host can request a user authorization and stop; do not
   estimate first-party performance from Muapi data.
3. Query Search Console for the requested date range. Start with query and
   page dimensions when the question concerns SEO opportunities; add country,
   device, or date only when needed.
4. Query GA4 for organic landing pages, traffic acquisition, and key events
   when conversion or engagement context is requested and the property is
   connected.
5. For a growth review, first find Search Console queries around positions
   5–20, then enrich those queries with Muapi keyword metrics when market
   demand or difficulty is needed. For page prioritization, join Search
   Console pages to GA4 organic landing-page outcomes only on a normalized
   host-and-path key and keep unmatched pages visible.
6. Use the same date range and compatible filters for comparisons. Keep
   Search Console clicks/impressions/CTR/position separate from GA4 sessions,
   users, revenue, and key events.
7. Calculate striking-distance queries, page-level CTR gaps, traffic deltas,
   and conversion deltas only from returned rows. Preserve denominators and
   formulas.
8. For a technical question, use gsc.inspect_urls only for URLs the user owns
   and only when the connector exposes URL Inspection.
9. Save direct Google source records with property identifiers, filters,
   dimensions, date ranges, and retrieval time. Do not save tokens.

## Decision rules

- Search Console is the first-party source for Google Search impressions,
  clicks, CTR, and average position.
- GA4 is the first-party source for configured analytics events and
  conversions; it cannot prove a search ranking by itself.
- A combined Search Console/GA4 opportunity score is calculated by the host,
  not supplied by Google. Keep its inputs, formula, matched-row count, and
  unmatched rows visible.
- Do not compare Search Console position with Muapi rank snapshots as if they
  were the same measurement. Explain the different source and methodology.
- Do not use first-party data from the user's site to make claims about a
  competitor.
- A missing GA4 key event may mean it is not configured or filtered out; do
  not call it zero conversions without an explicit zero row.
- Keep user-level or sensitive dimensions out of reports unless explicitly
  requested and allowed by the connector.

## Output format

Return:

- connected property names or IDs in redacted form
- date range, comparison range, timezone, dimensions, and filters
- Search Console performance table
- GA4 organic and key-event table when available
- calculated deltas and formulas
- striking-distance or landing-page opportunities
- data-quality and attribution limitations
- source links

## Failure and missing-data behavior

If a property is not connected, inaccessible, or mismatched, state the exact
boundary and continue with independent Muapi analysis only. If a report has
different date ranges, dimensions, or attribution settings, do not merge the
rows into one trend.
