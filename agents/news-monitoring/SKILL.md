---
name: SEO and PR News Monitoring
slug: news-monitoring
version: 2.0.0
category: seo
description: Reserved capability for SEO, search-engine, and PR news monitoring when Muapi exposes the required time-series and news sources.
status: unavailable
muapi_capabilities: []
required_connections:
  - muapi
permissions:
  - external-read-only
  - workspace-write
---

# SEO and PR News Monitoring

## Status

This capability is unavailable with the current Muapi SEO tool set. There is no
registered Muapi task in this repository that supplies search-performance
time-series, SERP-volatility history, algorithm-update data, or news/PR
monitoring.

## Required behavior

When a user asks for this analysis, state the missing data boundary and stop.
Do not report general industry news as if it affected the user's site. Do not
use current rank snapshots to manufacture a historical traffic anomaly.

This file remains as a clear extension point. It can become ready only when the
required Muapi tasks and their live schemas are available.
