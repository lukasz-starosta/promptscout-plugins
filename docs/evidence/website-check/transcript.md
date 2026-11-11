# Website check without a PromptScout account: recorded Claude Code runs

Recorded on 2026-11-11 in a cloud container with headless Claude Code (`claude -p`), loading this
branch's plugin with `--plugin-dir ./claude/promptscout`. This environment has never signed in to
PromptScout: at the start of every run the account server `plugin:promptscout:promptscout` reports
`needs-auth`, and no run calls it. Only the public website audit server is used.

`$ALLOWED` pre-approves the three website audit tools and `Bash(sleep:*)`, so the headless runs
do not stop at permission prompts:

```text
ALLOWED="mcp__plugin_promptscout_promptscout-website-audit__promptscout_start_website_audit,mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_website_audit,mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_aeo_geo_guidance,Bash(sleep:*)"
```

What the runs show:

- Runs 1 and 3: `/promptscout:checking-website-readiness <domain>` returns a full report with no
  sign-in prompt, no `/mcp` step and no link to PromptScout's site. Run 3 had no cached result, so
  Claude waited the 15 seconds the server asked for before reading it.
- Run 2: only when the user says they have no account and asks what to do next does Claude give
  the one pointer to the free check, after the fixes.
- Run 4: a general question loads the `aeo-geo-evidence-guide` skill on its own and answers with
  the guide's sources and review date, again with no sign-in.

Tool results are trimmed to 600 characters; Claude's answers are complete. The raw stream files
are not committed because they also list the recording machine's own tools and settings.

## 1. Website check on example.com (cached result)

```text
claude -p "/promptscout:checking-website-readiness example.com" --plugin-dir ./claude/promptscout --output-format stream-json --verbose --allowedTools "$ALLOWED"
```

- Claude Code 2.1.322, model `claude-opus-5-5`.
- PromptScout servers at start: `plugin:promptscout:promptscout` (needs-auth), `plugin:promptscout:promptscout-website-audit` (connected). No PromptScout sign-in was ever done in this environment.
- Result: `success`, error: false, turns: 4.

### Tool calls

1. `ToolSearch` with `{"query": "select:mcp__plugin_promptscout_promptscout-website-audit__promptscout_start_website_audit,mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_website_audit", "max_results": 2}`
   - Returned: mcp__plugin_promptscout_promptscout-website-audit__promptscout_start_website_audit mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_website_audit
2. `promptscout_start_website_audit` with `{"website": "example.com", "request_key": "3f8a2c71-9b4e-4d6a-a1f2-7c5e8d903b14"}`
   - Returned: {"ready":true,"reference":"41586d83-4924-4f15-af7a-d32606b77f4c","cached":true,"expires_in_days":7,"summary":"A cached audit is ready. Read its result using the returned reference before reporting a status or findings."}
3. `promptscout_get_website_audit` with `{"reference": "41586d83-4924-4f15-af7a-d32606b77f4c"}`
   - Returned: {"ready":true,"status":"success","reference":"41586d83-4924-4f15-af7a-d32606b77f4c","cached":true,"summary":"Analyzed 1 page. Found 5 items to address.","report":{"method":"technical_website_audit","profile":"public_mcp_v1","observed_at":"2026-11-11T09:40:03.372Z","pages_analyzed":1,"pages_attempted":1,"checklist":[{"title":"Sitemap not found","result":"needs_attention","pages":[],"problem":"The scanner did not find a sitemap at the checked locations.","where":"The website's sitemap endpoint and the Sitemap entry in /robots.txt.","fix":"Link an existing XML sitemap from robots.txt, or publish  …(trimmed)

### Claude's answer, word for word

> ## Website readiness check: example.com
>
> The check **succeeded** and found 5 items to fix. It ran on 2026-11-11 at 09:40 UTC. It analyzed 1 of the 1 page it tried, and this result came from the cache.
>
> ### Needs attention
>
> **Access**
>
> 1. **HTTP version does not redirect to HTTPS**
>    - **Problem:** The `http://` homepage shows a page instead of sending visitors to `https://`.
>    - **Where:** The redirect rules in your server, CDN or hosting settings.
>    - **Fix:** Add a permanent redirect (301 or 308) from every `http://` URL to the same `https://` URL.
>    - **Why:** When both versions work, every page has a duplicate. Search signals get split between them, and visitors can land on an unencrypted copy.
>
> 2. **www and non-www both serve the site**
>    - **Problem:** The homepage loads on both `www.example.com` and `example.com`, and neither one redirects to the other.
>    - **Where:** The redirect rules and domain settings in your server, CDN or hosting settings.
>    - **Fix:** Pick one main host. Permanently redirect the other host to the same path on the main one.
>    - **Why:** Two hosts with the same content create a duplicate URL for every page.
>
> **Indexing and discovery**
>
> 3. **No sitemap found**
>    - **Problem:** The check found no sitemap at the places it looked.
>    - **Where:** The sitemap address on the site and the `Sitemap:` line in `/robots.txt`.
>    - **Fix:** If you already have an XML sitemap, link it from robots.txt. If not, publish one at `/sitemap.xml`.
>    - **Why:** A sitemap helps search engines find your public URLs. It doesn't guarantee they'll be indexed.
>
> **Content and structure**
>
> 4. **No main heading**
>    - **Problem:** The page's HTML has no `<h1>` heading.
>    - **Where:** `https://example.com/`, in the visible main content inside `<body>`.
>    - **Fix:** Add a visible `<h1>` that states what the page is about.
>    - **Why:** A main heading helps readers and screen readers understand the page topic.
>
> **Metadata**
>
> 5. **No meta description**
>    - **Problem:** The page's HTML has no usable meta description.
>    - **Where:** `https://example.com/`, inside `<head>`.
>    - **Fix:** Add `<meta name="description" content="…">` with a short, accurate summary of the page.
>    - **Why:** Search engines can use it as the page summary in search results.
>
> ### Passed
> - **Page analysis:** 1 page was analyzed.
> - **Page titles:** the analyzed page has a `<title>` tag.
> - **Search crawler rules:** there is no robots.txt, so it blocks nothing for the checked URL.
>
> ### Notes
> - llms.txt is missing. It's optional, so nothing needs fixing.
> - The check looks at up to five pages, and here only one was analyzed. It doesn't cover the whole site.
> - These technical checks don't show whether AI assistants index, cite or recommend the site. A test that uses a crawler's name doesn't prove the real AI provider can reach it.
> - A new check within 24 hours may return this same cached result.
>
> **Next step:** Add a permanent HTTP → HTTPS redirect for every URL. Then open `http://example.com/` and confirm it sends you to the `https://` version.


## 2. Follow-up in the same session: no account, what next

```text
claude -p "I don't have a PromptScout account. What should I do next?" --resume <session of run 1> --plugin-dir ./claude/promptscout --output-format stream-json --verbose --allowedTools "$ALLOWED"
```

- Claude Code 2.1.322, model `claude-opus-5-5`.
- PromptScout servers at start: `plugin:promptscout:promptscout` (needs-auth), `plugin:promptscout:promptscout-website-audit` (connected). No PromptScout sign-in was ever done in this environment.
- Result: `success`, error: false, turns: 1.

### Tool calls

No tool calls: Claude answered from the report earlier in the session.

### Claude's answer, word for word

> You don't need an account for the fixes. Work through them in this order:
>
> 1. **Redirect HTTP to HTTPS.** In your server, CDN or hosting settings, add a permanent redirect (301 or 308) from every `http://` URL to the same `https://` URL. To check it, open `http://example.com/` and confirm you end up on `https://`.
> 2. **Pick one host.** Choose either `www.example.com` or `example.com`, and permanently redirect the other one to the same path. To check it, open the other host and confirm it redirects.
> 3. **Publish a sitemap.** If you don't have one, put an XML sitemap at `/sitemap.xml`. Then add a `Sitemap: https://example.com/sitemap.xml` line to robots.txt, using your chosen host.
> 4. **Add an `<h1>`** to the homepage that says what the page is about, and make sure visitors can see it.
> 5. **Add a meta description** inside `<head>` that gives a short, accurate summary of the page.
>
> After you make the changes, ask me to run the check again. The website check needs no account. A new run within 24 hours may return the same cached result, so wait a day or check the changed pages yourself first. It also only looked at your homepage, so check your other important pages for the same heading and description gaps.
>
> These fixes help AI assistants read your site, but they don't tell you whether assistants actually mention your brand. If you want to find that out, PromptScout has a free check that doesn't need an existing account: [www.promptscout.app/get-started](https://www.promptscout.app/get-started?utm_source=claude-plugin&utm_medium=skill&utm_campaign=claude-plugin).


## 3. Website check on iana.org (fresh result, waits for the audit)

```text
claude -p "/promptscout:checking-website-readiness iana.org" --plugin-dir ./claude/promptscout --output-format stream-json --verbose --allowedTools "$ALLOWED"
```

- Claude Code 2.1.322, model `claude-opus-5-5`.
- PromptScout servers at start: `plugin:promptscout:promptscout` (needs-auth), `plugin:promptscout:promptscout-website-audit` (connected). No PromptScout sign-in was ever done in this environment.
- Result: `success`, error: false, turns: 5.

### Tool calls

1. `ToolSearch` with `{"query": "select:mcp__plugin_promptscout_promptscout-website-audit__promptscout_start_website_audit,mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_website_audit", "max_results": 2}`
   - Returned: mcp__plugin_promptscout_promptscout-website-audit__promptscout_start_website_audit mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_website_audit
2. `promptscout_start_website_audit` with `{"website": "iana.org", "request_key": "7c3e9a2f-4b1d-4e8a-9f6c-2d5b8e1a3c47"}`
   - Returned: {"ready":false,"reference":"e155c57e-a5a7-48bf-8e37-7b4184b52880","cached":false,"retry_after_seconds":15,"expires_in_days":7,"summary":"Your audit is running. Check the result in 15 seconds. No final result is available yet."}
3. `Bash` with `{"command": "sleep 15", "description": "Wait for audit to run"}`
   - Returned: (Bash completed with no output)
4. `promptscout_get_website_audit` with `{"reference": "e155c57e-a5a7-48bf-8e37-7b4184b52880"}`
   - Returned: {"ready":true,"status":"success","reference":"e155c57e-a5a7-48bf-8e37-7b4184b52880","cached":false,"summary":"Analyzed 5 pages. Found 3 items to address.","report":{"method":"technical_website_audit","profile":"public_mcp_v1","observed_at":"2026-11-11T09:44:00.674Z","pages_analyzed":5,"pages_attempted":5,"checklist":[{"title":"Sitemap not found","result":"needs_attention","pages":[],"problem":"The scanner did not find a sitemap at the checked locations.","where":"The website's sitemap endpoint and the Sitemap entry in /robots.txt.","fix":"Link an existing XML sitemap from robots.txt, or publis …(trimmed)

### Claude's answer, word for word

> **iana.org** was checked on 2026-11-11 at 09:44 UTC and the check succeeded. It analyzed 5 of the 5 pages it tried and found 3 things to fix. This is a fresh result, not one from the cache.
>
> ## Needs attention
>
> **Indexing and discovery**
>
> 1. **No sitemap found**
>    - **Problem:** The check looked in the usual places and did not find a sitemap.
>    - **Where:** At `/sitemap.xml`, and in the `Sitemap:` line of `/robots.txt`.
>    - **Fix:** If you already have an XML sitemap, add a link to it in robots.txt. If you don't, publish one at `/sitemap.xml`.
>    - **Why:** A sitemap helps search engines find your public pages. It does not guarantee they will be indexed.
>
> 2. **Declared URLs use a different host or scheme**
>    - **Problem:** Some URLs the site declares don't match the homepage address it actually serves. The check found the mismatch in the homepage's canonical tag or JSON-LD `url`, or in the sitemap's URLs. For example, one might use `http` while the site serves `https`, or `www` while the site serves the bare domain.
>    - **Where:** The `<link rel="canonical">` tag and the JSON-LD `url` on the homepage, and the `<loc>` entries in any sitemap.
>    - **Fix:** Change each of these URLs to the exact scheme and host the site ends up on after redirects.
>    - **Why:** These URLs tell search engines which address to index. When they point to a host that redirects, or to a duplicate host, search engines get mixed signals.
>
> **Metadata**
>
> 3. **No meta description**
>    - **Problem:** The HTML of these pages has no usable meta description.
>    - **Where:** In the HTML `<head>` of https://iana.org/, /contact, /about, /domains and /numbers.
>    - **Fix:** Add a short, accurate summary for each page, like this: `<meta name="description" content="…">`.
>    - **Why:** Search engines can use this summary in the snippet they show under the page in results.
>
> ## Passed
> - All 5 sampled pages loaded and could be analyzed.
> - Every sampled page has a title tag.
> - Every sampled page has an H1 heading.
> - robots.txt allows the search crawlers the check tested.
>
> ## Notes
> - The site has no llms.txt file. It's optional, so you don't need to add one.
> - The check only looks at a sample of up to five pages, not the whole site.
> - It checks technical setup only. It doesn't measure whether AI assistants index, cite or recommend the site. Passing a test that uses a crawler's name doesn't prove the real AI provider can reach the site.
> - If you run the check again within 24 hours, you may get this cached result.
>
> **Next step:** Publish an XML sitemap at `/sitemap.xml`, or link your existing one from robots.txt. Then confirm it loads at that address.


## 4. Guide question, no skill named

```text
claude -p "Do I need llms.txt for my website to show up in ChatGPT answers?" --plugin-dir ./claude/promptscout --output-format stream-json --verbose --allowedTools "$ALLOWED"
```

- Claude Code 2.1.322, model `claude-opus-5-5`.
- PromptScout servers at start: `plugin:promptscout:promptscout` (needs-auth), `plugin:promptscout:promptscout-website-audit` (connected). No PromptScout sign-in was ever done in this environment.
- Result: `success`, error: false, turns: 5.

### Tool calls

1. `Skill` with `{"skill": "promptscout:aeo-geo-evidence-guide", "args": "Do I need llms.txt for my website to show up in ChatGPT answers?"}`
   - Returned: Launching skill: promptscout:aeo-geo-evidence-guide
2. `ToolSearch` with `{"query": "select:mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_aeo_geo_guidance", "max_results": 1}`
   - Returned: mcp__plugin_promptscout_promptscout-website-audit__promptscout_get_aeo_geo_guidance
3. `promptscout_get_aeo_geo_guidance` with `{"question": "llms-txt"}`
   - Returned: {"version":"1.1.0","reviewedOn":"2026-10-01","scope":"This is general guidance. It does not assess your website or measure current AI visibility.","evidenceBasis":"PromptScout reviewed this public guide. It combines editorial advice with scoped provider references. It supplies no customer evidence or measured performance lift.","responseRules":["Start with a direct answer. Use short sentences and familiar words.","Give one instruction per sentence. Define technical terms when the reader needs them.","Separate supplied observations, source-supported practices and possible causes.","Check the re …(trimmed)

### Claude's answer, word for word

> No, you don't need it. llms.txt is optional. It is not a switch that makes ChatGPT cite your site. (llms.txt is a proposed plain-text file at your site's root that lists your key pages for AI tools.)
>
> For ChatGPT, access and content matter more. ChatGPT search finds pages through OpenAI's search crawler, called **OAI-SearchBot**. If that crawler can't reach your pages, or your pages don't clearly answer the question, adding llms.txt won't fix it.
>
> **What to do instead**
> 1. **Check crawler access.** Open your `robots.txt` (the file that tells crawlers what they may visit). Make sure it doesn't block `OAI-SearchBot`. Check your CDN or firewall rules too. A CDN is the service that delivers and protects your site.
> 2. **Keep search and training separate.** `OAI-SearchBot` controls whether your pages can appear in ChatGPT search. `GPTBot` controls whether OpenAI can use your content for training. `ChatGPT-User` covers pages fetched when a user asks ChatGPT to open them. You can block training and still allow search.
> 3. **Check the page itself.** It should load without errors and allow indexing. Its main text should be readable without logging in or clicking anything. It should answer the question directly.
> 4. **Add llms.txt only if you want to.** It does little harm, but don't count on it getting you cited.
>
> **How to check it worked:** After a fix, test the same URL again and note the date and the new result. Your server or CDN logs will show whether `OAI-SearchBot` is actually visiting your pages. A test that uses a crawler's name doesn't prove the real crawler can get in. Allowing the crawler also doesn't guarantee your pages will be shown or cited.
>
> **Sources**
> - [OpenAI: Overview of OpenAI crawlers](https://developers.openai.com/api/docs/bots): what each OpenAI crawler is for and how to control it. Allowing a crawler doesn't guarantee your pages will be shown, cited or recommended.
> - [Google: AI features and your website](https://developers.google.com/search/docs/appearance/ai-features): Google says its AI Overviews and AI Mode need no special AI text file. This covers Google only.
> - [Google: Optimizing for generative AI search](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide): Google's advice for AI search. It doesn't describe how ChatGPT chooses sources.
>
> This comes from PromptScout's guide, last reviewed on 2026-10-01. It's general advice, not a check of your site or of how often ChatGPT cites you. I can check whether your site is technically ready for AI crawlers if you share the domain.


