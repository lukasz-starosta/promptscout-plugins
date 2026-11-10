---
name: drafting-content-briefs
description: Read and create PromptScout content briefs, the outlines for pages or articles that help a brand appear in AI answers. Use when the user asks for a content brief, wants to see existing briefs, or wants to write content that AI assistants will cite.
---

# Drafting content briefs

A content brief is an outline PromptScout prepares for a page or article that should help a
brand appear in AI answers for a given prompt or topic.

This skill reads briefs freely. It changes data in the user's PromptScout account in only one
way, creating a new brief, and that needs the user's explicit confirmation first, as described
under "Write".

## Tools

The tools come from the `promptscout` MCP server bundled with this plugin. In Claude Code their
full names are listed below. In claude.ai and Cowork the same tools come from the PromptScout
connector, under the short name after `__` (for example `promptscout_list_brands`).

| Step | Full tool name | Changes data |
| :- | :- | :- |
| List brands | `mcp__plugin_promptscout_promptscout__promptscout_list_brands` | No |
| Tracked prompts | `mcp__plugin_promptscout_promptscout__promptscout_list_prompts` | No |
| List briefs | `mcp__plugin_promptscout_promptscout__promptscout_list_content_briefs` | No |
| Read a brief | `mcp__plugin_promptscout_promptscout__promptscout_get_content_brief` | No |
| Create a brief | `mcp__plugin_promptscout_promptscout__promptscout_generate_content_brief` | Yes |

If the tools are missing or return an authentication error, tell the user to sign in to
PromptScout: in Claude Code run `/mcp`, select `plugin:promptscout:promptscout` and follow the
sign-in; in claude.ai open the plugin under Customize > Plugins and connect it on its
Connectors tab. Do not continue until the tools work.

## Steps

1. **Pick the brand.** Call `mcp__plugin_promptscout_promptscout__promptscout_list_brands`. If
   there are several brands and the user did not name one, ask which one. If there are none, say
   the account has not granted any brand to Claude yet and stop.
2. **Look for an existing brief first.** Call
   `mcp__plugin_promptscout_promptscout__promptscout_list_content_briefs` and show the briefs
   with their title, topic or prompt, and date. If one already matches what the user wants, open
   it with `mcp__plugin_promptscout_promptscout__promptscout_get_content_brief` instead of
   creating a new one.
3. **Present a brief** in this order: target prompt or topic, audience, recommended title,
   outline (headings), points to cover, sources AI answers already cite (with links), and
   competitors to beat. Use only what the tool returned; if a section is missing, say so.
4. **Help write the content.** On request, draft the page or article from the brief in the
   conversation. Drafting text here changes nothing in PromptScout.
5. **Create a new brief** only through the write below, when no existing brief fits. If the user
   is unsure which prompt to target, call
   `mcp__plugin_promptscout_promptscout__promptscout_list_prompts` and suggest one.

## Write

### Create a content brief

Tool: `mcp__plugin_promptscout_promptscout__promptscout_generate_content_brief`.

This changes the user's PromptScout account. Follow this rule every time:

- Before the call, show what will be created: the brand and the prompt or topic the brief
  targets, plus any other input you will pass.
- Ask: "Create a content brief for <brand> on '<prompt or topic>' in PromptScout? (yes/no)" and
  end your turn. Call the tool only after the user's next message clearly confirms it, such as
  "yes" or "go ahead". This is the explicit confirmation.
- A request made before you showed the summary does not count as confirmation. Silence, a
  question, "maybe" or a change of subject means no: do not call the tool.
- Create one brief per confirmation.
- After the call, open the new brief with
  `mcp__plugin_promptscout_promptscout__promptscout_get_content_brief` and present it as in
  step 3. If creation is still in progress, say so and offer to check again later. If the call
  failed, say so and do not retry without asking again.
