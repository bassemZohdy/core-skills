# Install Core Skills

One source of skill definitions at `plugin/skills/`, packaged for both Claude and Codex. Do not copy the definitions into separate platform folders.

## Claude Code

From Claude Code, add this GitHub repository as a marketplace and install the plugin:

```text
/plugin marketplace add bassemZohdy/core-skills
/plugin install core-skills@core-skills
```

For a local clone, test with Claude Code's plugin loader against `./plugin`. After installing, inspect the skill list and run one targeted prompt per skill.

## Codex / ChatGPT plugin-capable environments

The Codex plugin manifest is at `plugin/.codex-plugin/plugin.json` and references `./skills/`. The local marketplace file is `.agents/plugins/marketplace.json`. Add the repository marketplace in a supported plugin environment; the host controls installation and activation. A plain skills-only alternative is copying `plugin/skills/*` to a supported user-level skills directory, such as `~/.agents/skills/`.

## Distribution and test status

All eight skills use Agent Skills-compatible `SKILL.md` frontmatter; plugin manifests do not invoke tools themselves. Run `python3 scripts/check.py` to validate paths, metadata and manifest links before release. This checker does not launch Claude or Codex and cannot establish runtime behavior or directory publication. Do not describe this repository as marketplace-approved until submission succeeds.

Official references: [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) and [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
