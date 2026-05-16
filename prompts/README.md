# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-*.md and regenerate.

# Prompt System

This prompt system deploys generic research agents for theory/claim audit,
evidence audit, reproducible implementation, experiment evaluation, paper
revision, and prompt/workflow evolution.

## Architecture

| Layer | Files | Purpose |
|-------|-------|---------|
| Pinned research-agent kernel | `prompts/research-agent` | Git submodule for the shared `research-agent` metaprompt source |
| Shared metaprompts | `prompts/meta/kernel-*.md` except `kernel-project.md` | local materialization of the pinned research-agent kernel files |
| Project profile | `prompts/meta/kernel-project.md` | project-specific source of truth |
| Generated agents | `prompts/agents-claude/`, `prompts/agents-codex/` | project-local executable role prompts |
| Skill capsules | `prompts/skills/` | project-local JIT operation details |
| Source record | `prompts/upstream.toml` | current metaprompt source revision |
| Runtime docs | `docs/00_GLOBAL_RULES.md`, `docs/01_PROJECT_MAP.md`, `docs/02_ACTIVE_LEDGER.md`, `docs/03_PROJECT_RULES.md` | compact working memory |

## Active Project

The active project is AI-assisted anomaly detection research. The initial scope
is registered in `docs/interface/ResearchBrief.md`; no source paper, benchmark
dataset, or application domain has been selected yet.

Substantial tasks should advance research evidence first and capture workflow
lessons when they improve the agent system.

## Operational Entry Points

External agents start from `AGENTS.md`, then read `docs/interface/ResearchBrief.md`,
`docs/02_ACTIVE_LEDGER.md`, `docs/03_PROJECT_RULES.md`, and `docs/01_PROJECT_MAP.md`.
Named agents read their environment `_base.yaml` before their role prompt.

Codex-facing operation is worktree-first: use a `codex/` task branch, commit
coherent checkpoints, preserve user edits, and merge to `main` only after
explicit user instruction with no-ff semantics.

All environments use wiki-first memory gates: search `docs/wiki/` before
difficult, investigative, ambiguous, or precedent-likely work, and classify
important validated findings for K-COMPILE before HAND-02 SUCCESS.

## Agent Roster

The Codex target contains 25 prompt files, including the `VerificationRunner`
micro-agent. Core roles include ResearchArchitect, TaskPlanner,
TheoryArchitect, TheoryAuditor, CodeArchitect, TestRunner, ExperimentRunner,
EvidenceAnalyst, PaperWriter, PaperReviewer, ConsistencyAuditor,
PresentationWriter, PromptArchitect, PromptAuditor, KnowledgeArchitect,
WikiAuditor, Librarian, and TraceabilityManager.

## Regeneration

For project retargeting, replace `prompts/meta/kernel-project.md` and regenerate
`docs/03_PROJECT_RULES.md`, `docs/01_PROJECT_MAP.md`, `docs/02_ACTIVE_LEDGER.md`,
`AGENTS.md`, local skills, agent prompts, and validation reports.

For shared metaprompt updates, update the pinned submodule at
`prompts/research-agent`, sync only shared `kernel*.md` files into
`prompts/meta/` while preserving `kernel-project.md`, then regenerate local
support artifacts and prompts. Do not import research-agent generated
`prompts/agents-*`, `prompts/skills/`, templates, or project scripts.

The local skill capsule manifest currently contains 9 skills:
`SKILL-HANDOFF-AUDIT`, `SKILL-GIT-WORKTREE`, `SKILL-TOOL-TRUST`,
`SKILL-CONDENSE-V2`, `SKILL-PROMPT-AUDIT`, `SKILL-PAPER-WRITING`,
`SKILL-SCHEME-CODE`, `SKILL-PRESENTATION-DECK`, and
`SKILL-PRESENTATION-ILLUSTRATION`.
