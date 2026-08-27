# Muapi SEO tool catalog

This is the tool map used by the skills in this repository. The task names and
request fields below mirror the SEO tasks currently registered by Muapi.

The live OpenAPI schema is authoritative when a field, enum, limit, or response
shape changes:

- https://api.muapi.ai/openapi.json
- https://muapi.ai/docs/api-reference

## Request lifecycle

For an HTTP connector:

1. POST the JSON request to
   https://api.muapi.ai/api/v1/<task-name>.
2. Preserve the returned request ID.
3. Poll GET
   https://api.muapi.ai/api/v1/predictions/<request-id>/result until the task
   completes.
4. Store both result and billing in the source record.

An MCP connector may hide this lifecycle. The host agent must still retain the
retrieved result, request parameters, timestamp, and billing information.

All task results normally contain:

~~~json
{
  "result": {},
  "billing": {}
}
~~~

Do not assume that a successful task means that a domain, keyword, business, or
video had positive data. Inspect the result and report empty or partial data.

## Complete task map

| Logical capability | Muapi task | Required request fields | Important optional fields | Use |
|---|---|---|---|---|
| seo.google_serp | seo-google-serp | keyword | location, language, device, depth 10-100 | Google organic SERP snapshot with normalized rankings and SERP features |
| seo.keyword_research | seo-keyword-research | keyword | location, language, limit 1-100 | Seed keyword metrics and related ideas |
| seo.domain_overview | seo-domain-overview | domain | location, language, limit 1-100 | Domain visibility, ranked keywords, top pages, and competitors |
| seo.backlinks | seo-backlinks | domain | limit 1-100, include_subdomains | Backlink summary, referring domains, link types, and anchors |
| seo.lighthouse_audit | seo-lighthouse-audit | url | device desktop or mobile | Lighthouse performance, accessibility, best practices, SEO, and Core Web Vitals |
| seo.rank_track | seo-rank-track | keyword | target_domain, location, language, device, depth 10-100 | One-keyword ranking position and ranking URL |
| seo.rank_track_batch | seo-rank-track-batch | keywords | target_domain, location, language, device, depth 10-100; up to 50 keywords | Comparable ranking snapshot for a keyword set |
| seo.local_serp | seo-local-serp | keyword | location, language, depth 10-100, search_type maps or local_finder, device | Local pack or Maps ranking snapshot |
| seo.business_listings | seo-business-listings | none | keyword, location, limit 1-100 | Discover businesses by name, category, keyword, and location |
| seo.business_profile | seo-business-profile | keyword | location, language, place_id, cid | Business profile details and identifiers |
| seo.business_reviews | seo-business-reviews | keyword | location, language, depth 10-100, extended | Reviews, ratings, owner responses, and review metadata |
| seo.ai_mentions | seo-ai-mentions | target | platforms chat_gpt or google, limit 1-100 | Brand, product, and domain mentions or citations in AI-search results |
| seo.ai_response | seo-ai-response | prompt | model, web_search, max_tokens 2000-4000, country | Test an answer against a selected AI model |
| seo.keywords_search_volume | seo-keywords-search-volume | keywords | location, language | Search volume for an explicit keyword list |
| seo.keywords_for_keywords | seo-keywords-for-keywords | keywords | location, language, limit 1-100 | Expand multiple seed terms into keyword ideas |
| seo.related_keywords | seo-related-keywords | keyword | location, language, depth 1-4, limit 1-100 | Related terms for one seed keyword |
| seo.keyword_overview | seo-keyword-overview | keywords | location, language | Metrics for multiple explicit keywords |
| seo.relevant_pages | seo-relevant-pages | target | location, language, limit 1-100 | Pages relevant to a domain, subdomain, or target |
| seo.backlinks_pages | seo-backlinks-pages | target | limit 1-100, include_subdomains | Pages receiving the most backlinks |
| seo.backlinks_history | seo-backlinks-history | target | date_from, date_to | Historical backlink and referring-domain changes |
| seo.ai_mentions_metrics | seo-ai-mentions-metrics | target | competitors, platforms, date_from, date_to | AI visibility metrics and share-of-voice comparisons |
| seo.google_qa | seo-google-qa | keyword | location, language, depth 1-50 | Questions associated with a business or local query |
| seo.business_updates | seo-business-updates | keyword | location, language | Business posts, offers, events, and updates |
| seo.account_status | seo-account-status | none | force_check | Muapi/provider connection, balance, limits, and rates |
| seo.youtube_organic | seo-youtube-organic | keyword | location, language, device, depth 10-100 | YouTube organic search result snapshot |
| seo.youtube_video_info | seo-youtube-video-info | video_id | location, language | Video metadata, engagement, channel details, and tags |
| seo.youtube_video_subtitles | seo-youtube-video-subtitles | video_id | subtitles_language, location, language | Captions and transcript text |
| seo.youtube_video_comments | seo-youtube-video-comments | video_id | depth 20-100 | Comments, replies, authors, dates, and likes |

## Selection rules

- Use seo.domain_overview to establish domain-level context before interpreting
  competitor or content-gap data.
- Use seo.keyword_research for discovery and seo.keywords_search_volume or
  seo.keyword_overview when validating a fixed list.
- Use seo.google_serp to verify the live result page for high-priority terms;
  do not infer SERP format from keyword metrics alone.
- Use seo.rank_track_batch for a comparable set and save the returned snapshot
  before calculating a trend.
- Use seo.backlinks_pages and seo.backlinks_history when the question concerns
  important linked pages or change over time; seo.backlinks alone is a summary.
- Use seo.google_qa and seo.business_updates as part of a complete local
  profile review, not just map rank.
- Use seo.ai_mentions_metrics for aggregate comparisons and seo.ai_mentions for
  the individual citations needed to explain the comparison.
- Use seo.ai_response to test a specific question, not as a substitute for
  aggregate visibility measurement.
- Use the four YouTube tasks together when the user asks for a video or channel
  strategy: discover results, inspect candidates, read transcripts, and mine
  comments for audience language.
- Check seo.account_status before a large or unfamiliar run when balance,
  limits, or provider availability is unknown.

## Cost and batch guardrails

- Start with the smallest result depth and limit that can answer the question.
- Batch only comparable keywords with the same location, language, device, and
  depth.
- Do not send more than 50 keywords in a rank-track batch.
- Ask the user before deep SERP requests, large keyword expansions, repeated
  competitor scans, AI-response tests, or broad YouTube comment retrieval.
- If billing is returned, quote the actual settled amount from billing rather
  than estimating it from a generic rate.
