# Install Core Skills

One source of skill definitions at `plugin/skills/`, packaged for both Claude and Codex. Do not copy the definitions into separate platform folders.

## Claude Code

> **Untested:** the marketplace commands below follow the Claude Code documentation but have not yet been run against this repository (see `docs/RELEASE-CHECKLIST.md`). `claude plugin validate` passes for both the marketplace and the plugin, which checks the manifests only, not installation.

Install from the GitHub marketplace, either in one step or in two:

```text
/plugin install core-skills --marketplace bassemZohdy/core-skills
```

```text
/plugin marketplace add bassemZohdy/core-skills
/plugin install core-skills@core-skills
```

To try a local clone without installing:

```text
claude --plugin-dir ./plugin
```

After editing a skill, run `/reload-plugins` in the session. Then inspect the skill list and run one targeted prompt per skill. Plugin skills are invoked as `/core-skills:<skill>`.

## Codex / ChatGPT plugin-capable environments

> **Untested:** the Codex packaging has not been installed in any Codex host yet, and its manifest fields have not been checked by a Codex validator.

```text
codex plugin marketplace add bassemZohdy/core-skills
```

Then run `codex` and open `/plugins` to browse and install. The Codex plugin manifest is at `plugin/.codex-plugin/plugin.json` and references `./skills/`; the repository marketplace file is `.agents/plugins/marketplace.json`. Mention a skill with `$<skill>` or use `/skills`.

## Skills only, without the plugin

Copy the skill directories to a user-level skills directory:

- Claude Code: `~/.claude/skills/`
- Codex and other Agent Skills hosts: `~/.agents/skills/`

```text
cp -r plugin/skills/* ~/.agents/skills/
```

Prefer the plugin install on Claude Code. A personal skill named `plan` or `review` sits next to Claude Code's built-in commands of the same names and can take their place, whereas plugin skills are namespaced (`/core-skills:plan`) and do not collide. Codex does not merge skills with duplicate names; both can appear in its selector.

## Checking a clone

```text
python scripts/check.py
python -m unittest discover -s tests
```

On Windows, use `python` (a `python3` command may be a Microsoft Store stub). The checker does not launch Claude or Codex and cannot establish runtime behavior or directory publication. Do not describe this repository as marketplace-approved until submission succeeds.

Official references: [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) and [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
