"""Static checks for the PromptScout Claude plugin and its marketplace.

Run from the repository root:  python3 -m unittest discover -s tests -v
Standard library only.
"""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "claude" / "promptscout"
SKILLS = PLUGIN / "skills"
SKILL_NAMES = ["checking-ai-visibility", "acting-on-opportunities", "drafting-content-briefs"]

MCP_URL = "https://mcp.promptscout.app/mcp"
TOOL_PREFIX = "mcp__plugin_promptscout_promptscout__"

# Tools of the PromptScout account MCP server (task SL-1428).
KNOWN_TOOLS = {
    "promptscout_list_brands",
    "promptscout_get_brand_setup_status",
    "promptscout_read_share_of_voice",
    "promptscout_read_competitor_rankings",
    "promptscout_read_sources",
    "promptscout_read_cited_threads",
    "promptscout_read_ai_providers",
    "promptscout_read_search_performance",
    "promptscout_read_live_ai_traffic",
    "promptscout_list_prompts",
    "promptscout_get_current_opportunities",
    "promptscout_get_opportunity_execution_package",
    "promptscout_get_opportunity_evidence_summary",
    "promptscout_complete_opportunity",
    "promptscout_reject_opportunity",
    "promptscout_generate_opportunities",
    "promptscout_list_content_briefs",
    "promptscout_get_content_brief",
    "promptscout_generate_content_brief",
}
# Wording that gates a write on the user's explicit yes.
CONFIRMATION_GATE = re.compile(r"only after the (user's next message clearly confirms|explicit confirmation)")

WRITE_TOOLS = {
    "promptscout_complete_opportunity",
    "promptscout_reject_opportunity",
    "promptscout_generate_opportunities",
    "promptscout_generate_content_brief",
}

# Words that must not appear in user-facing text (skills and READMEs).
FORBIDDEN_WORDS = re.compile(
    r"\b(price|prices|priced|pricing|plan|plans|upgrade|upgrades|upgrading|"
    r"subscription|subscriptions|billing|trial|weekly|automatic|automatically)\b",
    re.IGNORECASE,
)

# Patterns that look like secrets or personal data.
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),              # OpenAI/Anthropic style keys
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),        # GitHub tokens
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),                # AWS access key id
    re.compile(r"xox[abposr]-[A-Za-z0-9-]{10,}"),       # Slack tokens
    re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),  # JWT
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._-]{12,}"),
    re.compile(r"(?i)(api[_-]?key|secret|password|token)\s*[\"']?\s*[:=]\s*[\"'][^\"']{6,}"),
    re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),  # email addresses
]


# A tool name stands alone or follows the "__" of a full plugin tool name.
TOOL_NAME = re.compile(r"(?:(?<![A-Za-z0-9_])|(?<=__))(promptscout_[a-z_]+)")


def tool_names(text):
    return set(TOOL_NAME.findall(text))


def read(path):
    return path.read_text(encoding="utf-8")


def skill_text(name):
    return read(SKILLS / name / "SKILL.md")


def frontmatter(text):
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def sections(text):
    """Split markdown into (heading, body) chunks at '#' headings."""
    parts = re.split(r"(?m)^(#{1,6} .*)$", text)
    chunks = [("", parts[0])]
    for i in range(1, len(parts), 2):
        chunks.append((parts[i], parts[i + 1] if i + 1 < len(parts) else ""))
    return chunks


def user_facing_files():
    files = [ROOT / "README.md", PLUGIN / "README.md"]
    files += [SKILLS / n / "SKILL.md" for n in SKILL_NAMES]
    return files


def published_files():
    return user_facing_files() + [
        ROOT / "LICENSE",
        PLUGIN / "LICENSE",
        ROOT / ".claude-plugin" / "marketplace.json",
        PLUGIN / ".claude-plugin" / "plugin.json",
        PLUGIN / ".mcp.json",
    ]


class ManifestTests(unittest.TestCase):
    def test_plugin_manifest_fields(self):
        data = json.loads(read(PLUGIN / ".claude-plugin" / "plugin.json"))
        self.assertEqual(data["name"], "promptscout")
        for field in ("description", "version", "license", "repository", "keywords"):
            self.assertTrue(data.get(field), field)
        self.assertEqual(data["author"]["name"], "PromptScout")
        self.assertEqual(data["homepage"], "https://www.promptscout.app")
        self.assertEqual(data["repository"], "https://github.com/lukasz-starosta/promptscout-plugins")
        self.assertEqual(data["license"], "MIT")
        self.assertTrue((PLUGIN / data["icon"]).is_file(), "icon file missing")

    def test_mcp_server_is_account_server_only(self):
        data = json.loads(read(PLUGIN / ".mcp.json"))
        self.assertEqual(list(data["mcpServers"]), ["promptscout"])
        server = data["mcpServers"]["promptscout"]
        self.assertEqual(server, {"type": "http", "url": MCP_URL})

    def test_no_website_audit_server(self):
        for path in published_files():
            self.assertNotIn("check.promptscout.app", read(path), path)

    def test_marketplace_lists_plugin(self):
        data = json.loads(read(ROOT / ".claude-plugin" / "marketplace.json"))
        self.assertEqual(data["name"], "promptscout")
        self.assertEqual(len(data["plugins"]), 1)
        entry = data["plugins"][0]
        self.assertEqual(entry["name"], "promptscout")
        self.assertEqual(entry["source"], "./claude/promptscout")
        self.assertTrue((ROOT / entry["source"] / ".claude-plugin" / "plugin.json").is_file())


class SkillTests(unittest.TestCase):
    def test_exactly_three_skills(self):
        found = sorted(p.name for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())
        self.assertEqual(found, sorted(SKILL_NAMES))

    def test_skill_frontmatter(self):
        for name in SKILL_NAMES:
            fields = frontmatter(skill_text(name))
            self.assertIsNotNone(fields, name)
            self.assertEqual(fields.get("name"), name)
            self.assertTrue(fields.get("description"), name)

    def test_every_tool_name_exists(self):
        for name in SKILL_NAMES:
            text = skill_text(name)
            mentioned = tool_names(text)
            self.assertGreaterEqual(len(mentioned), 3, name)
            unknown = mentioned - KNOWN_TOOLS
            self.assertFalse(unknown, f"{name} mentions unknown tools: {unknown}")

    def test_full_tool_names_use_plugin_prefix(self):
        for name in SKILL_NAMES:
            text = skill_text(name)
            for full in re.findall(r"mcp__[A-Za-z0-9_-]+__[a-z_]+", text):
                self.assertTrue(full.startswith(TOOL_PREFIX), f"{name}: {full}")
            # Every tool call in a table row is a full plugin tool name.
            for row in re.findall(r"(?m)^\|.*`[^`]*promptscout_[a-z_]+`.*\|$", text):
                for code in re.findall(r"`([^`]*promptscout_[a-z_]+)`", row):
                    self.assertTrue(code.startswith(TOOL_PREFIX), f"{name}: {code}")

    def test_writes_are_gated_on_confirmation(self):
        gate = CONFIRMATION_GATE
        for name in SKILL_NAMES:
            for heading, body in sections(skill_text(name)):
                for line in body.splitlines():
                    writes = tool_names(line) & WRITE_TOOLS
                    if not writes:
                        continue
                    if line.startswith("|"):
                        # Tools table: a write tool must be flagged as changing data.
                        self.assertTrue(line.rstrip().endswith("| Yes |"), f"{name}: {line}")
                    else:
                        # Prose: the section that names a write tool states the gate.
                        self.assertRegex(
                            " ".join((heading + body).split()), gate,
                            f"{name}: section '{heading}' mentions {writes} without a confirmation gate",
                        )

    def test_each_write_has_its_own_gated_section(self):
        expected = {
            "acting-on-opportunities": {
                "promptscout_complete_opportunity",
                "promptscout_reject_opportunity",
                "promptscout_generate_opportunities",
            },
            "drafting-content-briefs": {"promptscout_generate_content_brief"},
            "checking-ai-visibility": set(),
        }
        for name, tools in expected.items():
            text = skill_text(name)
            mentioned = tool_names(text) & WRITE_TOOLS
            self.assertEqual(mentioned, tools, name)
            for tool in tools:
                headed = [
                    body for heading, body in sections(text)
                    if heading.startswith("### ") and f"Tool: `{TOOL_PREFIX}{tool}`" in body
                ]
                self.assertEqual(len(headed), 1, f"{name}: no write section for {tool}")
                prose = " ".join(headed[0].split())
                self.assertIn("(yes/no)", prose)
                self.assertRegex(prose, CONFIRMATION_GATE)


class PublishedTextTests(unittest.TestCase):
    def test_no_pricing_or_schedule_words(self):
        for path in user_facing_files():
            hits = FORBIDDEN_WORDS.findall(read(path))
            self.assertFalse(hits, f"{path.relative_to(ROOT)}: {hits}")

    def test_no_secrets_or_personal_data(self):
        for path in published_files():
            text = read(path)
            for pattern in SECRET_PATTERNS:
                self.assertIsNone(pattern.search(text), f"{path.relative_to(ROOT)}: {pattern.pattern}")

    def test_readmes_long_enough(self):
        for path in (ROOT / "README.md", PLUGIN / "README.md"):
            prose = re.sub(r"```.*?```", "", read(path), flags=re.DOTALL)
            self.assertGreaterEqual(len(prose.split()), 40, path)

    def test_root_readme_covers_install_and_data(self):
        text = read(ROOT / "README.md")
        for needle in (
            "/plugin marketplace add lukasz-starosta/promptscout-plugins",
            "/plugin install promptscout@promptscout",
            "Customize > Plugins",
            "Add marketplace",
            MCP_URL,
            "PromptScout account",
            "sign in",
            "Reads",
            "Writes",
            "https://www.promptscout.app",
        ):
            self.assertIn(needle, text)

    def test_promptscout_links_are_tagged_for_counting(self):
        # Visits from the plugin's README and skill links are counted in PostHog by utm_source.
        tagged = re.compile(
            r"https://www\.promptscout\.app/(contact)?\?utm_source=claude-plugin"
            r"&utm_medium=(github-readme|plugin-readme|skill)&utm_campaign=claude-plugin"
        )
        files = {
            ROOT / "README.md": 2,
            PLUGIN / "README.md": 2,
            SKILLS / "checking-ai-visibility" / "SKILL.md": 1,
        }
        for path, expected in files.items():
            text = read(path)
            self.assertEqual(len(tagged.findall(text)), expected, path)
            # Home and contact links in these files are all tagged; privacy links stay plain.
            plain = re.findall(r"https://www\.promptscout\.app(?:/contact)?/?(?=[\s).,]|$)", text)
            self.assertFalse(plain, f"{path}: untagged home/contact link {plain}")

    def test_license_is_mit_with_trademark_note(self):
        for path in (ROOT / "LICENSE", PLUGIN / "LICENSE"):
            text = read(path)
            self.assertTrue(text.startswith("MIT License"), path)
            prose = " ".join(text.split())
            self.assertIn("The PromptScout name and logo", prose, path)
            self.assertIn("are not licensed under it", prose, path)


if __name__ == "__main__":
    unittest.main()
