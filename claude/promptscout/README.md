# PromptScout for Claude

![PromptScout](assets/icon.png)

PromptScout shows how often AI assistants such as ChatGPT, Perplexity, Gemini and Claude mention
your brand, which sources they cite, and what you can do to appear more often. This plugin adds
five workflows to Claude. Two need no PromptScout account:

- **checking-website-readiness**: checks up to five public pages of any website for crawler
  rules, sitemap, redirects, page titles, headings and meta descriptions, and lists each fix.
- **aeo-geo-evidence-guide**: answers questions about appearing in AI answers, such as llms.txt
  or schema markup, from PromptScout's guide with public sources.

Three work with your PromptScout account:

- **checking-ai-visibility**: lists the brands you granted, then reads share of voice, competitor
  rankings and cited sources. Answers name the AI engine, the date and the source link.
- **acting-on-opportunities**: reads your current Opportunities and the steps for one, then marks
  it done or dismisses it only after you confirm.
- **drafting-content-briefs**: lists and reads your content briefs, and creates a new one only
  after you confirm.

## Setup

The website check and the guide use PromptScout's public website audit server at
`https://check.promptscout.app/mcp`: no account, no sign-in. They check technical setup only and
do not measure whether AI assistants cite your website.

The account skills connect to PromptScout's hosted MCP server at
`https://mcp.promptscout.app/mcp`. Sign in to PromptScout the first time Claude uses it: in
Claude Code run `/mcp` and select `plugin:promptscout:promptscout`; on claude.ai connect it on
the plugin's **Connectors** tab under **Customize > Plugins**.
Any PromptScout account with a brand can connect, on any plan. Free gets part of the visibility
data, Starter gets all of it, and Growth and higher also get Opportunities and content briefs.
PromptScout MCP is in beta; if your sign-in shows no brand to approve, [contact us](https://www.promptscout.app/contact?utm_source=claude-plugin&utm_medium=plugin-readme&utm_campaign=claude-plugin).

Install it from the marketplace in https://github.com/lukasz-starosta/promptscout-plugins:

```text
/plugin marketplace add lukasz-starosta/promptscout-plugins
/plugin install promptscout@promptscout
```

## What it reads and writes

The plugin stores nothing and runs nothing on your computer. The website check reads up to five
public pages of the website you name, plus its robots.txt and sitemap, and changes nothing. With
your account, it reads your brands, visibility data, Opportunities and content briefs through
PromptScout's account server. It writes only after you confirm in the conversation: marking an
Opportunity done, dismissing one, asking PromptScout to create new Opportunities, and creating a
content brief. Privacy policy:
https://www.promptscout.app/privacy.

## Support

[www.promptscout.app](https://www.promptscout.app/?utm_source=claude-plugin&utm_medium=plugin-readme&utm_campaign=claude-plugin) ([contact form](https://www.promptscout.app/contact?utm_source=claude-plugin&utm_medium=plugin-readme&utm_campaign=claude-plugin)).

## License

MIT for the code and manifests; see [LICENSE](LICENSE). The PromptScout name and logo are not
licensed.
