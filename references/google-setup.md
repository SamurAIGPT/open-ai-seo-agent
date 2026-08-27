# Google first-party connector setup

This repository supplies the instructions for using first-party Google data;
it does not run OAuth, store tokens, or provide a hosted Google connector. The
host agent or its connector must own those responsibilities.

Use this guide when the user wants their own Search Console or Google
Analytics 4 data in an SEO workflow.

## What the host must provide

The host needs a direct Google OAuth or native Google connection that can:

- authorize the user's Google account with read-only access
- list the Search Console properties and GA4 properties that account can read
- let the user select the exact property for the project
- refresh and revoke the grant without exposing tokens to the agent
- return structured API rows and metadata to the skill

The repository never infers authorization from a domain name. A domain in a
prompt is a target; a selected Google property is the authorization boundary.

## User prerequisites

Before connecting, the user should have:

- read access to the verified Search Console property for the site
- at least Viewer access to the GA4 property whose reports should be read
- the correct Google account selected when more than one account is signed in

Search Console properties can be URL-prefix properties or domain properties.
Keep the selected property identifier exactly as Google returns it, such as
`sc-domain:example.com` or a URL-prefix property, and verify it matches the
project domain before querying.

## Google Cloud and OAuth setup

For a host that owns the OAuth application, complete these steps once:

1. Create or select a project in the
   [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the [Search Console API](https://console.cloud.google.com/apis/library/searchconsole.googleapis.com),
   [Google Analytics Admin API](https://console.cloud.google.com/apis/library/analyticsadmin.googleapis.com),
   and [Google Analytics Data API](https://console.cloud.google.com/apis/library/analyticsdata.googleapis.com).
   Only enable the APIs used by the host.
3. Configure the OAuth consent screen. Choose Internal for an eligible
   Workspace-only application or External for other users. While the app is in
   testing, add each connecting Google account as a test user. Follow Google's
   [OAuth consent and publishing guidance](https://support.google.com/cloud/answer/10311615).
4. Create an OAuth client for the host's application type. For a web host,
   register the exact HTTPS callback URL. The scheme, hostname, port, path,
   and trailing slash must match the callback sent to Google.
5. Request only these data scopes:

   - `https://www.googleapis.com/auth/webmasters.readonly` for Search Console
   - `https://www.googleapis.com/auth/analytics.readonly` for Analytics Admin
     property discovery and Analytics Data API reports
   - `openid`, `email`, and `profile` only when the host needs to identify the
     connected Google account

   Do not request write scopes for this read-only skill pack.
6. Store the client secret, encryption key, access tokens, and refresh tokens
   in the host's secret/token store. The variable names and callback routes are
   host-specific; none belong in this repository.

Google's [Search Console prerequisites](https://developers.google.com/webmaster-tools/v1/prereqs),
[Search Console authorization guide](https://developers.google.com/webmaster-tools/v1/how-tos/authorizing),
and [Analytics API quickstart](https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart)
are the authoritative setup references.

## Capability mapping

The skill uses stable logical names so host agents do not need identical tool
names. A connector can implement them with these Google API operations:

| Logical capability | Google operation | Purpose |
|---|---|---|
| `gsc.list_sites` | Search Console `sites.list` | Discover properties the user can access |
| `gsc.search_analytics` | Search Console `searchanalytics.query` | Query clicks, impressions, CTR, position, queries, pages, countries, and devices |
| `gsc.inspect_urls` | Search Console URL Inspection API | Inspect indexing information for a URL in a selected property |
| `ga4.list_properties` | Analytics Admin `accountSummaries.list` | Discover accessible GA4 properties and metadata |
| `ga4.organic_landing_pages` | Analytics Data `properties.runReport` | Report organic landing-page sessions and configured business metrics |
| `ga4.page_performance` | Analytics Data `properties.runReport` | Report page views, users, engagement, and configured events |
| `ga4.key_events` | Analytics Data `properties.runReport` | Report configured key events, optionally by landing page |
| `ga4.organic_overview` | Analytics Data `properties.runReport` | Summarize organic acquisition |
| `ga4.traffic_acquisition` | Analytics Data `properties.runReport` | Break down acquisition by channel/source dimensions |
| `ga4.ecommerce_performance` | Analytics Data `properties.runReport` | Report item, transaction, and revenue signals |
| `ga4.site_search` | Analytics Data `properties.runReport` | Report measured internal-search terms |
| `ga4.audience_breakdown` | Analytics Data `properties.runReport` | Report bounded device, country, or new/returning summaries |
| `ga4.measurement_health` | Analytics Admin/Data metadata and reports | Surface available metrics, restrictions, and data-quality limitations |

The live Google API response is authoritative. Do not promise a dimension or
metric merely because it appears in this table.

## Connection flow for an agent host

The host should expose a user-facing connection flow similar to:

1. User chooses **Connect Search Console** and/or **Connect Analytics**.
2. Host sends the user through Google consent with the read-only scopes.
3. Host lists accessible properties and asks the user to select one. Do not
   silently choose the first result.
4. Host stores only the selected property metadata and a reference to the
   encrypted grant. The agent receives no token.
5. The first-party skill performs a small verification call:
   `gsc.list_sites` or `ga4.list_properties`, followed by a bounded report for
   the selected property.
6. The host returns the property, date range, timezone, dimensions, filters,
   row counts, quota/thresholding metadata, and any Google error to the agent.

For an agency workflow, GSC and GA4 may be authorized by different Google
accounts. Keep their grants and selected properties independent.

The recommended project model is one selected Search Console property and one
selected GA4 property per SEO project. Store the mapping outside the skill
files, allow an authorized project member to replace it, and never let an agent
choose a property merely because its domain string looks similar.

Google calls are outside Muapi task billing, but they remain subject to Google
OAuth permissions, API quotas, reporting limits, data freshness, and property
configuration.

## Connector response contract

Every direct Google source record should preserve:

- `source_system`: `google_search_console` or `google_analytics_4`
- selected property identifier and a redacted display label when shared
- retrieval timestamp and property timezone
- requested and resolved date ranges
- dimensions, filters, channel, row limit, and pagination state
- metric definitions and the raw structured rows
- thresholding, sampling, quota, truncation, permission, and freshness warnings

Keep GSC and GA4 in separate source records. Search Console clicks and
impressions are not GA4 sessions, and Search Console average position is not a
Muapi live rank snapshot.

## Verification checklist

Before declaring the connection ready, confirm that:

- the selected Search Console property is verified and matches the project
  domain or URL prefix
- the selected GA4 property is a GA4 property with readable reporting data
- a small Search Console query returns rows or an explicit empty result
- a small GA4 report returns rows or an explicit empty result
- the source record contains dates, timezone, dimensions, filters, and metadata
- no access token, refresh token, client secret, or secret-bearing URL was
  returned to the agent or written under `.seo/`

## Common failures

- **No Search Console property:** the connected Google account lacks access, or
  the site has not been added and verified in Search Console.
- **No GA4 property:** the connected account lacks property access, the Admin
  API is disabled, or the property is not a GA4 property.
- **`redirect_uri_mismatch`:** the registered callback differs from the host's
  callback in scheme, host, port, path, or trailing slash.
- **`access_denied`:** the OAuth app is in testing and the connecting account is
  not listed as a test user, or the user declined the requested scope.
- **Empty Search Console report:** preserve it as an empty result. Check the
  selected property, date range, filters, and Google's data availability before
  treating it as an SEO conclusion.
- **Different GSC and GA4 totals:** expected when date boundaries, property
  timezone, attribution, reporting identity, or metric definitions differ.

Never convert a permission error, thresholded row, omitted row, or unavailable
property into zero performance.
