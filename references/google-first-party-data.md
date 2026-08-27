# Direct Google first-party data

Search Console and Analytics are user-owned data sources. They are intentionally
separate from the Muapi provider boundary.

## Connection boundary

The host agent or its connector owns OAuth, consent, token storage, property
selection, refresh, and revocation. This repository supplies instructions for
using the resulting read-only connection; it must never contain client secrets,
refresh tokens, access tokens, or service-account keys.

The user must select and authorize:

- a verified Google Search Console property
- an accessible Google Analytics 4 property

Do not infer authorization from a domain string. Always use the property
selected by the connector and report a redacted property identifier.

## Logical capabilities

Hosts may expose different tool names. The skill uses these logical contracts:

| Logical capability | Data | Typical dimensions or inputs |
|---|---|---|
| gsc.list_sites | Search Console properties the user can access | account connection |
| gsc.search_analytics | Search clicks, impressions, CTR, and average position | date range, query, page, country, device, date |
| gsc.inspect_urls | Indexing/inspection result for owned URLs | property, URL, inspection time |
| ga4.list_properties | Analytics properties the user can access | account connection |
| ga4.organic_landing_pages | Organic landing-page traffic and events | property, date range, landing page, channel |
| ga4.page_performance | Page engagement and configured metrics | property, date range, page |
| ga4.key_events | Configured key events or conversions | property, date range, event, landing page |
| ga4.organic_overview | Organic acquisition totals | property, date range, channel |
| ga4.traffic_acquisition | Channel/source/medium acquisition | property, date range, channel dimensions |
| ga4.measurement_health | Measurement and event-quality signals | property, date range |

The live Google API schema and the connector's returned fields are
authoritative. Do not promise a metric merely because it appears in this
catalog.

## Recommended host-facing tool names

The logical names above are the portable contract. A host may expose friendly
tool names such as these and map them back to the same semantics:

| Logical capability | Recommended tool name |
|---|---|
| `gsc.search_analytics` | `get_search_console_performance` |
| `gsc.inspect_urls` | `inspect_urls` |
| `ga4.organic_landing_pages` | `get_google_analytics_organic_landing_pages` |
| `ga4.page_performance` | `get_google_analytics_page_performance` |
| `ga4.key_events` | `get_google_analytics_key_events` |
| `ga4.organic_overview` | `get_google_analytics_organic_overview` |
| `ga4.traffic_acquisition` | `get_google_analytics_traffic_acquisition` |
| `ga4.ecommerce_performance` | `get_google_analytics_ecommerce_performance` |
| `ga4.site_search` | `get_google_analytics_site_search` |
| `ga4.audience_breakdown` | `get_google_analytics_audience_breakdown` |
| `ga4.measurement_health` | `get_google_analytics_measurement_health` |

These are read-only adapter names, not requirements for the host. If the host
uses different names, it should publish the equivalent mapping in its tool
instructions.

## Bounded request contracts

For Search Console performance, the connector should support a bounded,
paginated query over `query`, `page`, `country`, `device`, and `date` dimensions.
Use simple AND filters, a maximum of 1,000 rows per call, and a `startRow`
offset. The default window should end approximately three days before today to
avoid presenting fresh incomplete data, with a maximum lookback of 16 months.
The response should return `keys`, `clicks`, `impressions`, `ctr`, and
`position`, along with the resolved dates, row count, and pagination state.
Filter striking-distance positions client-side because Search Console orders
rows by clicks rather than exposing position as a filter.

For URL Inspection, accept one to ten absolute URLs per call and return a
separate result or error for each URL. Google remains responsible for deciding
whether an inspected URL belongs to the selected property.

For Analytics, expose fixed read-only reports rather than an unrestricted
report builder. Use a numeric GA4 property selected by the user, inclusive
`YYYY-MM-DD` date ranges, a default of the last 28 complete property days, a
maximum of 90 days for bounded workflows, and limit/offset pagination up to
1,000 rows. Organic Search should be the default channel; an all-channel query
must be explicit. Preserve property timezone, currency, reporting identity,
sampling, thresholding, `(other)`-row loss, quota, and restricted-metric
metadata.

Recommended fixed Analytics reports are:

- organic landing pages: sessions, users, engagement, key events, transactions,
  and revenue
- page performance: page views, users, engagement duration, and key events
- key events: event counts and users, optionally by organic landing page
- organic overview: totals and a comparable prior-period trend
- traffic acquisition: channel, source/medium, or campaign performance
- ecommerce performance: item or landing-page transaction and revenue signals
- site search: measured internal-search terms and engagement
- audience breakdown: device, country, or new-versus-returning summaries
- measurement health: data streams, measurement IDs, enhanced measurement,
  key events, and available definitions

An optional combined **search opportunities** workflow can take Search Console
pages with average positions around 4–20, join them to GA4 organic landing-page
rows by normalized host and path, and rank the matched pages using an explicitly
calculated score. Keep unmatched pages visible and unscored; never treat a
missing GA4 row as zero business value.

The host should reject arbitrary dimensions, metrics, filters, and report JSON
unless it explicitly owns the resulting privacy, quota, and schema contract.

## When to use each source

- Use Search Console first for the user's existing query demand, pages,
  impressions, clicks, CTR, and average position.
- Use GA4 when the question involves sessions, engagement, revenue, or
  configured key events.
- Use both when prioritizing SEO work: Search Console identifies search
  opportunity; GA4 helps identify business impact.
- Use Muapi for external keyword market data, live SERPs, competitor domains,
  backlink data, local results, AI visibility, and YouTube data.

## Reconciliation rules

Search Console and Muapi rankings are different observations. Search Console
average position is aggregated over the user's impressions and may differ from
a location/device-specific live SERP snapshot. GA4 attribution and Search
Console clicks also measure different stages of the journey.

Reports must label:

- source system
- property and timezone
- date range
- dimensions and filters
- metric definitions
- whether a value is observed or calculated

Never blend rows from incompatible date ranges, properties, attribution
settings, filters, or dimensions.

## Privacy rules

- Minimize query and page detail to what the user requested.
- Do not export user-level identifiers.
- Redact property IDs when a report will be shared outside the project.
- Keep OAuth credentials and tokens outside .seo/ sources.
- Preserve connector errors so an authorization problem is not mistaken for
  zero traffic.
