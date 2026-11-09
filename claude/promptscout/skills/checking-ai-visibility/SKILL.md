---
name: checking-ai-visibility
description: Check how visible a brand is in AI answers with PromptScout. Use for questions like "How visible is my brand in AI answers?", how often ChatGPT, Perplexity, Gemini or Claude mention the user's brand, how it compares with competitors, its share of voice, or which sources and threads AI answers cite. Load it before answering even when the PromptScout server is not connected or needs sign-in, because it gives the exact sign-in steps.
---

# Checking AI visibility

This skill only reads data. It never changes anything in the user's PromptScout account.

## Tools

The tools come from the `promptscout` MCP server bundled with this plugin. In Claude Code their
full names are listed below. In claude.ai and Cowork the same tools come from the PromptScout
connector, under the short name after `__` (for example `promptscout_list_brands`).

| Step | Full tool name |
| :- | :- |
| List brands | `mcp__plugin_promptscout_promptscout__promptscout_list_brands` |
| Check setup | `mcp__plugin_promptscout_promptscout__promptscout_get_brand_setup_status` |
| Share of voice | `mcp__plugin_promptscout_promptscout__promptscout_read_share_of_voice` |
| Competitor rankings | `mcp__plugin_promptscout_promptscout__promptscout_read_competitor_rankings` |
| Cited sources | `mcp__plugin_promptscout_promptscout__promptscout_read_sources` |
| Cited threads | `mcp__plugin_promptscout_promptscout__promptscout_read_cited_threads` |
| AI engines tracked | `mcp__plugin_promptscout_promptscout__promptscout_read_ai_providers` |
| Tracked prompts | `mcp__plugin_promptscout_promptscout__promptscout_list_prompts` |

If the tools are missing or return an authentication error, tell the user to sign in to
PromptScout: in Claude Code run `/mcp`, select `plugin:promptscout:promptscout` and follow the
sign-in; in claude.ai open the plugin under Customize > Plugins and connect it on its
Connectors tab. Do not continue until the tools work.

## Steps

1. **Pick the brand.** Call `mcp__plugin_promptscout_promptscout__promptscout_list_brands`.
   - No brands: say the account has not granted any brand to Claude yet, and that the user can
     sign in again and grant one, or add a brand at [www.promptscout.app](https://www.promptscout.app/?utm_source=claude-plugin&utm_medium=skill&utm_campaign=claude-plugin). Stop there.
   - One brand: use it and name it in your answer.
   - Several brands: list them by name and ask which one to check, unless the user already named
     one.
2. **Check the setup when data looks empty.** If a read below returns no data, call
   `mcp__plugin_promptscout_promptscout__promptscout_get_brand_setup_status` and tell the user
   which setup step is missing instead of reporting zero visibility.
3. **Read the core numbers** for that brand:
   - `mcp__plugin_promptscout_promptscout__promptscout_read_share_of_voice`
   - `mcp__plugin_promptscout_promptscout__promptscout_read_competitor_rankings`
   - `mcp__plugin_promptscout_promptscout__promptscout_read_sources`
4. **Go deeper only when asked or when it explains a number:**
   `mcp__plugin_promptscout_promptscout__promptscout_read_ai_providers` for which engines are
   tracked, `mcp__plugin_promptscout_promptscout__promptscout_list_prompts` for which prompts
   are tracked, and `mcp__plugin_promptscout_promptscout__promptscout_read_cited_threads` for
   the discussion threads AI answers cite.

## How to answer

- Lead with the main number: the brand's share of voice and its rank among competitors, with the
  period it covers.
- Every claim about what an AI engine said names the **engine**, the **date** of the check, and
  the **source link** it cited, exactly as the tool returned them. Quote the answer text when the
  tool returns it. Never invent or guess an engine, date or URL; if the tool did not return one,
  say it is not available.
- Show competitors in a short table: brand, share of voice, rank, change since the previous
  period when the tool returns it.
- List the most cited sources with their links, and say whether each one mentions the user's
  brand when the data shows it.
- Give confidence as High, Medium or Low, based on how many prompts and engines the numbers
  cover, not as a precise percentage.
- Say what was not checked, such as engines or prompts PromptScout does not track for this brand.
- End with one suggested next step, such as reviewing Opportunities with the
  `acting-on-opportunities` skill.
