# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-*.md and regenerate.

# Prompt System

This prompt system deploys generic research agents for theory/claim audit,
evidence audit, reproducible implementation, experiment evaluation, paper
revision, and prompt/workflow evolution.

## Architecture

| Layer | Files | Purpose |
|-------|-------|---------|
| Kernel | `prompts/meta/kernel-*.md` | source of truth |
| Generated agents | `prompts/agents-claude/`, `prompts/agents-codex/` | executable role prompts |
| Skill capsules | `prompts/skills/` | JIT operation details |
| Runtime docs | `docs/00_GLOBAL_RULES.md`, `docs/01_PROJECT_MAP.md`, `docs/02_ACTIVE_LEDGER.md`, `docs/03_PROJECT_RULES.md` | compact working memory |

## Active Project

The active project is AI-assisted anomaly detection research. The initial scope
is registered in `docs/interface/ResearchBrief.md`; no source paper, benchmark
dataset, or application domain has been selected yet.

Substantial tasks should advance research evidence first and capture workflow
lessons when they improve the agent system.

## Agent Roster

The deployed roster contains 23 roles per environment, including ResearchArchitect,
TaskPlanner, TheoryArchitect, TheoryAuditor, CodeArchitect, TestRunner,
ExperimentRunner, EvidenceAnalyst, PaperWriter, PaperReviewer, ConsistencyAuditor,
PromptArchitect, PromptAuditor, KnowledgeArchitect, WikiAuditor, Librarian, and
TraceabilityManager.

## Regeneration

For project retargeting, replace `prompts/meta/kernel-project.md` and regenerate
`docs/03_PROJECT_RULES.md`, `docs/01_PROJECT_MAP.md`, `docs/02_ACTIVE_LEDGER.md`,
`AGENTS.md`, and validation reports. For workflow changes, update the relevant
kernel file, regenerate agent prompts, then run prompt audit before using changed
agents.
