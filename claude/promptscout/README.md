# PromptScout for Claude

![PromptScout](assets/icon.png)

PromptScout shows how often AI assistants such as ChatGPT, Perplexity, Gemini and Claude mention
your brand, which sources they cite, and what you can do to appear more often. This plugin
connects Claude to your PromptScout account and adds three workflows:

- **checking-ai-visibility**: lists the brands you granted, then reads share of voice, competitor
  rankings and cited sources. Answers name the AI engine, the date and the source link.
- **acting-on-opportunities**: reads your current Opportunities and the steps for one, then marks
  it done or dismisses it only after you confirm.
- **drafting-content-briefs**: lists and reads your content briefs, and creates a new one only
  after you confirm.

## Setup

You need a PromptScout account. The plugin connects to PromptScout's hosted MCP server at
`https://mcp.promptscout.app/mcp`. Sign in to PromptScout the first time Claude uses it: in
Claude Code run `/mcp` and select `plugin:promptscout:promptscout`; on claude.ai connect it on
the plugin's **Connectors** tab under **Customize > Plugins**.

Install it from the marketplace in https://github.com/lukasz-starosta/promptscout-plugins:

```text
/plugin marketplace add lukasz-starosta/promptscout-plugins
/plugin install promptscout@promptscout
```

## What it reads and writes

The plugin stores nothing and runs nothing on your computer. It reads your brands, visibility
data, Opportunities and content briefs through PromptScout's server. It writes only after you
confirm in the conversation: marking an Opportunity done, dismissing one, asking PromptScout to
create new Opportunities, and creating a content brief. Privacy policy:
https://www.promptscout.app/privacy.

## Support

https://www.promptscout.app (contact form at https://www.promptscout.app/contact).

## License

MIT for the code and manifests; see [LICENSE](LICENSE). The PromptScout name and logo are not
licensed.
