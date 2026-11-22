# Install Core Skills

One source of skill definitions at `plugin/skills/`, packaged for both Claude and Codex. Do not copy the definitions into separate platform folders.

## Claude Code

> **Tested 2026-11-11 (Claude Code 2.1.322, Windows, scratch config dir):** `claude plugin marketplace add bassemZohdy/core-skills` then `claude plugin install core-skills@core-skills` installed the plugin with all eight skills; the installed version is the source commit's short SHA because the manifest has no `version`. Invoking `/core-skills:plan` from the installed copy (loaded with `--plugin-dir` on the cache directory) worked. Not tested: the one-step `/plugin install ... --marketplace` form typed inside a session. `claude plugin validate` passes for both the marketplace and the plugin.

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

> **Tested 2026-11-11 (Codex 0.167.0, Windows, scratch `CODEX_HOME`):** `codex plugin marketplace add bassemZohdy/core-skills` then `codex plugin add core-skills@core-skills` installed the plugin, enabled, at version 0.1.0 with all eight skills and the icon. A later `codex exec '$plan ...'` run in a signed-in Codex used the skill. Not tested: the interactive `/plugins` browser. The manifest follows the current Codex submission docs, but no Codex validator was run.

```text
codex plugin marketplace add bassemZohdy/core-skills
codex plugin add core-skills@core-skills
```

Or run `codex` and open `/plugins` to browse and install. The Codex plugin manifest is at `plugin/.codex-plugin/plugin.json` and references `./skills/`; the repository marketplace file is `.agents/plugins/marketplace.json`. Mention a skill with `$<skill>` or use `/skills`.

## Cursor

> **Not tested.** Written from the Cursor plugin reference (cursor.com/docs/reference/plugins, read 2026-11-22). No Cursor client was run, and the plugin is not submitted to the Cursor marketplace.

The repository has a Cursor marketplace file at `.cursor-plugin/marketplace.json` and a plugin manifest at `plugin/.cursor-plugin/plugin.json`; the skills are the same `plugin/skills/`. Cursor also loads the Agent Plugins manifest `plugin/plugin.json`. To list it in Cursor's public marketplace, submit the repository at cursor.com/marketplace/publish (the Cursor team reviews submissions; not done).

## GitHub Copilot (VS Code, Copilot CLI, Copilot app)

> **Not tested.** Written from the VS Code and GitHub Docs plugin references (read 2026-11-22). The Copilot CLI was not installed here, so no `copilot plugin` command was run.

These clients read the Agent Plugins 1.0 manifest `plugin/plugin.json` (skills from `plugin/skills/`) and the existing `.claude-plugin/marketplace.json`, so no extra files are needed. In Copilot CLI:

```text
copilot plugin marketplace add bassemZohdy/core-skills
copilot plugin install core-skills@core-skills
```

In VS Code, run **Chat: Install Plugin from Source** with `https://github.com/bassemZohdy/core-skills`, or add the marketplace in the Agent Customizations editor.

## Gemini CLI

> **Not tested.** The local Gemini CLI (0.22.5) predates `gemini skills`, so nothing was run. Written from geminicli.com/docs/cli/skills and /docs/extensions/reference (read 2026-11-22).

There is no Gemini extension. A Gemini extension needs `gemini-extension.json` and a `skills/` directory at the repository root, which would mean a second copy of the skills. Install the skills directly instead:

```text
gemini skills install https://github.com/bassemZohdy/core-skills.git --path plugin/skills
```

or copy `plugin/skills/*` to `~/.gemini/skills/` or `~/.agents/skills/` (user) or `.agents/skills/` (workspace).

## Other Agent Skills hosts

Any host that reads the [Agent Skills](https://agentskills.io/) format can use `plugin/skills/` through the skills-only install below. Hosts without a plugin system (for example OpenCode) have no marketplace entry here, and none was tested.

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
