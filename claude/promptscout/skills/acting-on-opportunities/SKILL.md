---
name: acting-on-opportunities
description: Review and act on PromptScout Opportunities, the concrete actions that can raise a brand's visibility in AI answers. Use when the user asks what to do next to improve AI visibility, wants to see or explain an Opportunity, or wants to mark one as done or dismiss it.
---

# Acting on Opportunities

An Opportunity is a concrete action PromptScout suggests to raise a brand's visibility in AI
answers. Opportunities are created on demand, when someone asks PromptScout for them.

This skill reads Opportunities freely. It changes data in the user's PromptScout account in only
three ways (complete, reject, generate), and each one needs the user's explicit confirmation
first, as described under "Writes".

## Tools

The tools come from the `promptscout` MCP server bundled with this plugin. In Claude Code their
full names are listed below. In claude.ai and Cowork the same tools come from the PromptScout
connector, under the short name after `__` (for example `promptscout_list_brands`).

| Step | Full tool name | Changes data |
| :- | :- | :- |
| List brands | `mcp__plugin_promptscout_promptscout__promptscout_list_brands` | No |
| Current Opportunities | `mcp__plugin_promptscout_promptscout__promptscout_get_current_opportunities` | No |
| What to do | `mcp__plugin_promptscout_promptscout__promptscout_get_opportunity_execution_package` | No |
| Why it matters | `mcp__plugin_promptscout_promptscout__promptscout_get_opportunity_evidence_summary` | No |
| Mark done | `mcp__plugin_promptscout_promptscout__promptscout_complete_opportunity` | Yes |
| Dismiss | `mcp__plugin_promptscout_promptscout__promptscout_reject_opportunity` | Yes |
| Create new ones | `mcp__plugin_promptscout_promptscout__promptscout_generate_opportunities` | Yes |

If the tools are missing or return an authentication error, tell the user to sign in to
PromptScout: in Claude Code run `/mcp`, select `plugin:promptscout:promptscout` and follow the
sign-in; in claude.ai open the plugin under Customize > Plugins and connect it on its
Connectors tab. Do not continue until the tools work.

## Steps

1. **Pick the brand.** Call `mcp__plugin_promptscout_promptscout__promptscout_list_brands`. If
   there are several brands and the user did not name one, ask which one. If there are none, say
   the account has not granted any brand to Claude yet and stop.
2. **Read the current Opportunities.** Call
   `mcp__plugin_promptscout_promptscout__promptscout_get_current_opportunities` and show them as
   a numbered list: title, what it targets (prompt, engine or source) and its status.
   - If there are none, say so. Offer to create new ones, which is the "Create new Opportunities"
     write below. Do not create them without that confirmation.
3. **Open one Opportunity.** When the user picks one, call
   `mcp__plugin_promptscout_promptscout__promptscout_get_opportunity_execution_package` for the
   steps and `mcp__plugin_promptscout_promptscout__promptscout_get_opportunity_evidence_summary`
   for the evidence. Explain what to do in plain steps, and back each claim about an AI answer
   with the engine, the date and the source link the tools returned. Never invent any of them.
4. **Help with the work.** Offer to draft the content or outreach the execution package
   describes, in the conversation. Drafting text here changes nothing in PromptScout.
5. **Record the outcome** only through the writes below.

## Writes

Each write below changes the user's PromptScout account. Every write follows the same rule:

- Before the call, show exactly what will change: the brand, the Opportunity title (or, for
  creating, the brand only) and the action.
- Ask a direct yes/no question and end your turn. Call the tool only after the user's next
  message clearly confirms it, such as "yes" or "go ahead". This is the explicit confirmation.
- A request made before you showed the summary does not count as confirmation. Silence, a
  question, "maybe" or a change of subject means no: do not call the tool.
- Confirm one write at a time. Never complete, reject or create several items from one
  confirmation unless the user confirmed that exact list.
- After the call, report what the tool returned. If it failed, say so and do not retry without
  asking again.

### Mark an Opportunity done

Tool: `mcp__plugin_promptscout_promptscout__promptscout_complete_opportunity`.

Use when the user says they have finished the work. Ask: "Mark '<title>' for <brand> as done in
PromptScout? (yes/no)". Call the tool only after the explicit confirmation described above.

### Dismiss an Opportunity

Tool: `mcp__plugin_promptscout_promptscout__promptscout_reject_opportunity`.

Use when the user does not want to act on it. Ask for a short reason if the tool accepts one,
then ask: "Dismiss '<title>' for <brand> in PromptScout? (yes/no)". Call the tool only after
the explicit confirmation described above.

### Create new Opportunities

Tool: `mcp__plugin_promptscout_promptscout__promptscout_generate_opportunities`.

Use when the user asks for new Opportunities or there are none. Ask: "Ask PromptScout to create
new Opportunities for <brand> now? (yes/no)". Call the tool only after the explicit confirmation
described above. Then call
`mcp__plugin_promptscout_promptscout__promptscout_get_current_opportunities` to show what was
created. If the tool says creation is still in progress, say so and offer to check again later.
