# Reports and snapshots

The host agent is responsible for turning Muapi responses into useful,
reviewable workspace artifacts. These files provide persistence without
requiring a separate SEO database or runtime service.

## Directory layout

~~~text
.seo/
  project.md
  reports/
    YYYY-MM-DD/
      <run-slug>.md
  sources/
    YYYY-MM-DD/
      <run-slug>/
        <task-name>.json
        gsc-<query>.json
        ga4-<report>.json
  snapshots/
    rankings/
      <market-slug>/
        YYYY-MM-DD.json
    backlinks/
      YYYY-MM-DD.json
    ai-visibility/
      YYYY-MM-DD.json
    local/
      <location-slug>/
        YYYY-MM-DD.json
    youtube/
      <market-slug>/
        YYYY-MM-DD.json
~~~

Create directories only when a user requests a report or asks for history.
Keep raw sources separate from the summary so a later run can be audited.

## Project context

If the user gives an ongoing domain, create or update .seo/project.md with:

- canonical domain and important URL prefixes
- brand, products, audiences, and business priorities
- primary markets, locations, languages, and devices
- confirmed competitors and why each is relevant
- target conversion or business outcomes
- keyword lists and their owner or source
- date created and last reviewed
- known data limitations

Do not infer sensitive business details. Mark unknown fields as unknown and ask
only for information needed by the selected workflow.

## Source record

Each Muapi call used in a report should be saved as JSON. Use a wrapper like:

~~~json
{
  "capability": "seo.domain_overview",
  "task_name": "seo-domain-overview",
  "retrieved_at": "2026-01-01T00:00:00Z",
  "request_id": "provider-request-id",
  "request": {
    "domain": "example.com",
    "location": "United States",
    "language": "English",
    "limit": 10
  },
  "result": {},
  "billing": {}
}
~~~

The request ID and billing object are optional only when the connector does not
return them. Never include API keys, authorization headers, or secret-bearing
URLs in a source file.

Direct Google sources use the same wrapper shape, replacing capability and
task_name with the direct connector capability and source system:

~~~json
{
  "source_system": "google_search_console",
  "capability": "gsc.search_analytics",
  "retrieved_at": "2026-01-01T00:00:00Z",
  "property": "sc-domain:example.com",
  "request": {
    "start_date": "2025-12-01",
    "end_date": "2025-12-31",
    "dimensions": ["query", "page"],
    "filters": []
  },
  "result": {}
}
~~~

Redact property identifiers when a report leaves the user's project. Never
save OAuth tokens or refresh credentials.

## Report contract

Every report should contain:

1. Scope: domain, keywords, competitors, market, device, date window, and
   requested question.
2. Executive answer: the few findings that change what the user should do.
3. Observed data: values copied or directly normalized from source records.
4. Calculated data: formulas and inputs for any derived score, delta, share, or
   grouping.
5. Recommendations: one action, owner, expected evidence, and priority per
   item.
6. Uncertainty and missing data: failed calls, empty results, incompatible
   comparisons, and hypotheses.
7. Sources: relative links to every source JSON file used.
8. Retrieval time and next suggested check.

Use a short table for findings. Do not present a calculated priority as if it
were a provider metric.

## Trend comparisons

Before comparing two snapshots, verify that these dimensions match:

- canonical domain or target
- exact keyword text and list membership
- location, language, device, and depth
- endpoint and relevant filters
- date window and timezone
- provider response completeness

Useful calculations:

- rank change = previous position minus current position; positive means an
  improvement
- visibility rate = keywords with a found position divided by tracked keywords
- top-10 rate = keywords in positions 1-10 divided by tracked keywords
- referring-domain change = current count minus previous count
- AI share of voice = target mentions divided by target plus comparison mentions,
  when all values use the same platform and window

Treat an unranked result as unknown or not found according to the provider
response. Do not silently convert it to a numeric position.

## Run discipline

- Save one source record per distinct Muapi call.
- Reuse a compatible source from the same run instead of repeating the call.
- Save a new dated snapshot for a later comparison; never overwrite the prior
  snapshot.
- If a task fails, preserve the error and continue only with workflows that do
  not depend on that task.
- If the user asks for recommendations but the evidence is incomplete, return a
  conditional recommendation and state what would confirm it.
