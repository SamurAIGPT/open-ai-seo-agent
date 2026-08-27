# Installation for existing agents

This repository is a set of plain-text skills. It does not replace the host
agent's planning or tool loop.

## 1. Connect Muapi

Configure the host agent's MCP client with:

- server URL: https://api.muapi.ai/mcp
- credential: a Muapi API key stored in the client's secret or environment
  store

For clients that use a local Muapi MCP command, provide the key through an
environment variable rather than putting it in a checked-in file. For
HTTP-only clients, use the client's secure header configuration. Follow the
client-specific instructions at https://muapi.ai/docs/mcp.

Verify the connection with seo.account_status before running a paid workflow.
Do not paste keys into prompts, reports, source records, or shell history.

## 2. Install skills

For a host with directory-based skill discovery, copy the required skill
directory so that SKILL.md remains at the skill root:

~~~text
<project>/.claude/skills/keyword-research/SKILL.md
<project>/.claude/skills/competitor-seo/SKILL.md
~~~

The same files can be loaded from agents/ by hosts that accept explicit
instruction files. Do not combine unrelated skills into one prompt if the host
supports selective loading.

## 3. Give the host agent a useful request

Include the target and measurement context:

~~~text
Analyze example.com for organic growth opportunities.
Market: United States
Language: English
Device: desktop
Priority: commercial pages and page-two keywords
Save the report and Muapi source records under .seo/.
~~~

For competitor, local, AI-visibility, and YouTube work, also provide the
competitor set, business location, target brand, platforms, or video IDs.

## 4. Connector contract

The Muapi connector should:

- expose all task names in references/muapi-seo-tools.md
- validate required fields against the live schema
- preserve request IDs and billing
- poll asynchronous tasks until completion
- return structured JSON instead of only a rendered URL
- surface provider errors without rewriting them as successful results

If the host already exposes Muapi tools, no adapter code belongs in this
repository. If it only supports HTTP, its connector must implement the POST
and result-polling flow described in muapi-seo-tools.md.

## 5. Host-agent behavior

Before calling tools, the host agent should:

1. identify the applicable skill
2. collect missing required inputs
3. state the planned calls and any expensive batch
4. check existing .seo/project.md and compatible sources
5. ask for approval when the run is broad or cost is uncertain

After calling tools, it should:

1. save source records
2. separate observations from calculations and hypotheses
3. produce the skill's output format
4. save the report only if requested or if the host convention permits it
5. state limitations and failed calls
