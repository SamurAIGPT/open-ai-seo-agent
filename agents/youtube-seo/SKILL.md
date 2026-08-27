---
name: YouTube SEO
slug: youtube-seo
version: 2.0.0
category: seo
description: Research YouTube search opportunities and analyze videos, transcripts, and audience comments with Muapi.
status: ready
muapi_capabilities:
  - seo.youtube_organic
  - seo.youtube_video_info
  - seo.youtube_video_subtitles
  - seo.youtube_video_comments
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# YouTube SEO

## Mission

Turn YouTube search and video evidence into a practical content opportunity or
optimization brief. Use search results for discovery and video-level data to
understand why a candidate may be useful.

## Required inputs

Choose one:

- keyword or topic for YouTube search
- one or more video IDs or YouTube URLs

Also collect country, language, device, and the user's channel or business
context when available.

## Workflow

### Keyword or topic research

1. Call seo.youtube_organic with the confirmed keyword, market, language,
   device, and modest depth.
2. Extract result position, title, channel, URL/video ID, and any provider
   fields returned. Do not infer performance from position alone.
3. Select representative or competing videos for deeper analysis. Ask before a
   large set.
4. Call seo.youtube_video_info for selected videos to obtain metadata, tags,
   engagement, and channel details.
5. Call seo.youtube_video_subtitles when transcript or topic-coverage analysis
   is requested. Preserve the language requested.
6. Call seo.youtube_video_comments when audience questions, objections, or
   wording are useful. Start with the smallest depth that answers the question.

### Known-video analysis

1. Normalize each supplied video ID or URL.
2. Call video-info, subtitles, and comments only for the requested analysis.
3. Separate provider metadata from observations made by reading transcript or
   comments.
4. Produce title/topic, content-angle, audience-language, and follow-up
   opportunity recommendations without copying creator content.

## Decision rules

- Do not claim a video is successful from ranking, views, likes, or comments
  unless the provider returns that field.
- Treat comments as a sample, not a survey of the entire audience.
- Do not copy titles, scripts, or comments; summarize patterns and cite the
  source video.
- Keep transcript language and market context in the report.
- Ask before retrieving many comments or analyzing many videos.

## Output format

Return:

- query/video scope and retrieval time
- ranking snapshot or video inventory
- metadata and engagement comparison, where available
- recurring transcript topics and audience questions
- prioritized content opportunities
- evidence and source links

## Failure and missing-data behavior

If captions are unavailable, state that transcript analysis was not possible.
If comments are disabled or sparse, report the sample limitation rather than
assuming the audience has no questions.
