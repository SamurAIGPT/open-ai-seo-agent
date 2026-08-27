---
name: Local SEO
slug: local-seo
version: 2.0.0
category: seo
description: Analyze local search visibility and business-profile health across rankings, listings, reviews, questions, and updates.
status: ready
muapi_capabilities:
  - seo.local_serp
  - seo.business_listings
  - seo.business_profile
  - seo.business_reviews
  - seo.google_qa
  - seo.business_updates
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# Local SEO

## Mission

Connect local ranking observations with the business information, reviews,
questions, and updates that a customer can see. Keep rank, listing health, and
reputation as separate evidence categories.

## Required inputs

- Business name and target location.
- One or more local search terms or categories.
- Country and language accepted by the Muapi schema.
- Optional: place ID, CID, named competitors, service area, and comparison
  window.

## Workflow

1. Read .seo/project.md and confirm the business identity, location, service
   area, and competitors. Disambiguate chains and businesses with similar
   names.
2. Call seo.local_serp for each important keyword and location using a
   consistent search type, device, depth, and language.
3. Call seo.business_listings to discover the wider local set when the business
   or competitors are not identified, then retain the returned identifiers.
4. Call seo.business_profile for the target business and named competitors.
   Prefer place_id or cid when available for exact lookup.
5. Call seo.business_reviews to compare rating, review count, review themes,
   owner responses, and any returned review metadata.
6. Call seo.google_qa to surface recurring customer questions and
   seo.business_updates to inspect visible posts, offers, events, or updates.
7. Separate observed profile fields, review patterns, local ranking positions,
   and calculated comparisons. Flag a mismatch for review rather than claiming
   it caused a ranking result.
8. Save a location-specific report and raw sources when requested.

## Decision rules

- A local result is tied to keyword, location, device, search type, and depth.
- Do not compare map results from different locations as one ranking trend.
- A high rating with a small review sample is not equivalent to a high rating
  with a large sample.
- Reviews and questions may contain useful customer language, but do not expose
  personal information in the report.
- Do not state that a profile field caused ranking movement without a controlled
  comparison or supporting evidence.
- Never edit, respond to, or publish business-profile content.

## Output format

Return:

- local query and location scope
- ranking snapshot by keyword
- business identity and profile-health checklist
- rating, review-volume, and response comparison
- recurring questions and update themes
- prioritized manual actions with evidence
- limitations and source links

## Failure and missing-data behavior

If a query returns no local results, say that no result was returned for that
location and search context. If identity matching is ambiguous, stop profile
comparison until the user confirms the correct business.
