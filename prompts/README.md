# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-*.md and regenerate.

# Prompt System

This prompt system deploys generic research agents for proof audit, evidence audit,
reproducible analysis, paper revision, and prompt/workflow evolution.

## Architecture

| Layer | Files | Purpose |
|-------|-------|---------|
| Kernel | `prompts/meta/kernel-*.md` | source of truth |
| Generated agents | `prompts/agents-claude/`, `prompts/agents-codex/` | executable role prompts |
| Skill capsules | `prompts/skills/` | JIT operation details |
| Runtime docs | `docs/00_GLOBAL_RULES.md`, `docs/01_PROJECT_MAP.md`, `docs/02_ACTIVE_LEDGER.md`, `docs/03_PROJECT_RULES.md` | compact working memory |

## Active Project

The active source artifact is `paper/source/heavy_tail_backup_v13.pdf`.
The project is intentionally agent-first: every substantial paper-improvement task
should also capture a workflow lesson when it teaches the agent system something.

## Agent Roster

The inherited roster contains 23 roles per environment, including ResearchArchitect,
TaskPlanner, TheoryArchitect, TheoryAuditor, CodeArchitect, TestRunner,
ExperimentRunner, EvidenceAnalyst, PaperWriter, PaperReviewer, ConsistencyAuditor, PromptArchitect,
PromptAuditor, KnowledgeArchitect, WikiAuditor, Librarian, and TraceabilityManager.

## Regeneration

For project retargeting, replace `prompts/meta/kernel-project.md` and regenerate
`docs/03_PROJECT_RULES.md`. For workflow changes, update the relevant kernel file,
then run prompt audit before using changed agents.
