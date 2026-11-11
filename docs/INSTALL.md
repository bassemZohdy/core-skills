# Install Core Skills

One source of skill definitions at `plugin/skills/`, packaged for both Claude and Codex. Do not copy the definitions into separate platform folders.

## Claude Code

> **Tested 2026-11-11 (Claude Code 2.1.322, Windows, scratch config dir):** `claude plugin marketplace add bassemZohdy/core-skills` then `claude plugin install core-skills@core-skills` installed the plugin with all eight skills; the installed version is the source commit's short SHA because the manifest has no `version`. Not tested: the one-step `/plugin install ... --marketplace` form typed inside a session, and invoking a skill from the installed copy. `claude plugin validate` passes for both the marketplace and the plugin.

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

> **Tested 2026-11-11 (Codex 0.167.0, Windows, scratch `CODEX_HOME`):** `codex plugin marketplace add bassemZohdy/core-skills` then `codex plugin add core-skills@core-skills` installed the plugin, enabled, at version 0.1.0 with all eight skills and the icon. Not tested: the interactive `/plugins` browser and invoking a `$<skill>` prompt (needs a signed-in Codex). The manifest follows the current Codex submission docs, but no Codex validator was run.

```text
codex plugin marketplace add bassemZohdy/core-skills
codex plugin add core-skills@core-skills
```

Or run `codex` and open `/plugins` to browse and install. The Codex plugin manifest is at `plugin/.codex-plugin/plugin.json` and references `./skills/`; the repository marketplace file is `.agents/plugins/marketplace.json`. Mention a skill with `$<skill>` or use `/skills`.

## Skills only, without the plugin

Copy the skill directories to a user-level skills directory:

- Claude Code: `~/.claude/skills/`
- Codex and other Agent Skills hosts: `~/.agents/skills/`

```text
cp -r plugin/skills/* ~/.agents/skills/
```

Prefer the plugin install on Claude Code. Plugin skills are registered only under the namespace (`/core-skills:plan`, `/core-skills:review`, and so on); with the plugin loaded, no bare `plan` or `review` entry is added (checked 2026-11-11 on Claude Code 2.1.322 by listing the session's slash commands). A user-level copy is different: a copy of `plan` and `review` in `~/.claude/skills/` registers the bare names `plan` and `review`, and if the plugin is also installed both sets appear. Claude Code's docs say a personal skill replaces a built-in command of the same name but not its aliases; whether the built-in `/plan` or `/review` is shadowed in an interactive session was not tested here. Codex does not merge skills with duplicate names; both can appear in its selector.

## Checking a clone

```text
python scripts/check.py
python -m unittest discover -s tests
```

On Windows, use `python` (a `python3` command may be a Microsoft Store stub). The checker does not launch Claude or Codex and cannot establish runtime behavior or directory publication. Do not describe this repository as marketplace-approved until submission succeeds.

Official references: [Claude Code plugin documentation](https://code.claude.com/docs/en/plugins) and [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins).
