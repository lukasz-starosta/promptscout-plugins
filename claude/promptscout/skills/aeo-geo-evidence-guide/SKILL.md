---
name: aeo-geo-evidence-guide
description: Answer questions about appearing in AI answers (AEO, GEO and SEO) with PromptScout's sourced guide. Use for questions like how to get cited by ChatGPT search or Google AI Overviews, why AI answers mention competitors but not the user's brand, AI crawlers and training controls, llms.txt, schema markup, FAQs, comparison pages, reviews and mentions, or how to measure AI visibility. Needs no PromptScout account and no sign-in.
---

# AEO and GEO evidence guide

This skill answers general questions about appearing in AI answers from PromptScout's public
guide. It needs no PromptScout account and no sign-in. It does not check a website, read any
account or measure live results; it only reads the guide.

## Tools

The tool comes from the `promptscout-website-audit` MCP server bundled with this plugin. In
Claude Code its full name is listed below. In claude.ai and Cowork the same tool appears under
the short name after `__` (`promptscout_get_aeo_geo_guidance`).

| Step | Full tool name |
| :- | :- |
| Read the guide | `mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_aeo_geo_guidance` |

Do not ask the user to sign in to PromptScout for this skill. If the tool is missing, say the
guide is not connected in this session. In Claude Code, the user can run `/reload-plugins` and
then `/mcp` to see whether `plugin:promptscout:promptscout-website-audit` is connected.

## Steps

1. **Pick the question.** Call
   `mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_aeo_geo_guidance` with
   the one `question` ID that matches what the user asked:

   | The user asks | `question` |
   | :- | :- |
   | The difference between AEO, GEO and SEO | `aeo-geo-and-seo` |
   | How to appear in ChatGPT search | `appear-in-chatgpt` |
   | How to appear in Google AI Overviews or AI Mode | `appear-in-google-ai` |
   | Why AI answers mention competitors but not their brand | `brand-not-mentioned` |
   | Allowing AI search while blocking AI training | `search-vs-training` |
   | Whether they need llms.txt | `llms-txt` |
   | Whether schema markup helps | `structured-data` |
   | FAQs or longer pages | `faq-and-word-count` |
   | Which content to improve first | `content-priorities` |
   | Improving a comparison page | `comparison-pages` |
   | Reviews and external mentions | `independent-mentions` |
   | Measuring AI visibility and traffic | `measure-visibility` |
   | How long results take | `time-to-results` |
   | Updating a page or writing a new one | `update-existing-content` |

   When no question fits, send up to three `topics` instead (for example `technical-readiness`,
   `clear-answers` or `fair-comparisons`). Never send both. When you are unsure, call the tool
   with no arguments to get the list of questions and topics, then pick from it. Send only these
   IDs, never the user's own words.
2. **Use the user's evidence.** Keep any page, AI answer or data the user shared in the
   conversation. Check the evidence the guide asks for before you propose a specific fix. When
   that evidence is missing, keep the advice conditional and say what would confirm it.

## How to answer

- Start with a direct answer in one or two short sentences.
- Give the next steps as a short list, one instruction per step, then the way to check the
  result.
- List the sources the guide returned with their titles and links, and say what each one
  covers. Never add a source, number or timeline the guide did not return.
- Say the guide was reviewed on its `reviewedOn` date and is general advice: it is not a
  measurement of the user's website, citations or visibility.
- Keep crawler access, cited pages, brand mentions, recommendations and visits separate, and
  keep anything not shown as unknown. Do not invent a score.
- Define a technical term the first time you use it.
- If the user wants their own website checked, use the `checking-website-readiness` skill. If
  they want to see how often AI answers mention their brand and they are signed in to
  PromptScout, use the `checking-ai-visibility` skill.
