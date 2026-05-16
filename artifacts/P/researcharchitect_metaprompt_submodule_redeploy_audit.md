# ResearchArchitect Metaprompt Submodule Redeploy Audit

created_at_utc: 2026-05-16T09:36:35Z
status: VALIDATED
owner: ResearchArchitect
branch: codex/researcharchitect-metaprompt-submodule-redeploy
worktree: /private/tmp/research-backup-metaprompt-submodule-redeploy

## Scope

Added `research-agent` as the pinned upstream metaprompt submodule and redeployed
Codex-facing generated artifacts from the latest upstream metaprompt revision.
No `main` merge was performed.

## Upstream Intake

- Remote: `git@github.com:t0m0h1r0/research-agent.git`.
- Submodule path: `prompts/upstream/research-agent`.
- Imported revision: `f52ae6f63494c42bf4727cd173851f0d06615799`
  (`Merge pull request #1 from t0m0h1r0/codex/wiki-knowledge-deploy-gate-20260516`).
- Distribution mode recorded in `prompts/upstream.toml`: `git_submodule`.
- Project-local `prompts/meta/kernel-project.md` was preserved; shared kernel
  files were materialized from the submodule into `prompts/meta/`.

## Local Redeploy

- Target environment: Codex only, per user instruction.
- Updated `prompts/agents-codex/` to `v8.2.0-candidate` and 25 prompt files,
  adding `VerificationRunner.md` for the upstream micro-agent contract.
- Updated PromptArchitect and PromptAuditor for Stage 1b
  `WikiKnowledgePacket` distillation, 15-item Q3-AUDIT, `wiki_static_tokens`,
  and AP-17 wiki-over-injection checks.
- Updated K-domain and cross-domain Codex prompts with AP-17 where the upstream
  anti-pattern injection list applies.
- Updated `SKILL-PROMPT-AUDIT`, `schema_resolution_report.json`,
  `token_telemetry_report.json`, and `wiki_knowledge_injection_report.json`.
- Left Claude prompts unchanged because this run was explicitly Codex-targeted.

## Verification

| Check | Verdict | Evidence |
|---|---|---|
| Submodule revision | PASS | `git submodule status` -> `f52ae6f63494c42bf4727cd173851f0d06615799 prompts/upstream/research-agent` |
| Shared kernel sync | PASS | `cmp` matched all shared kernel files except project-local `kernel-project.md` |
| Project profile preserved | PASS | no diff to `prompts/meta/kernel-project.md` |
| Project rules count | PASS | `grep -c '^## PR-' docs/03_PROJECT_RULES.md` -> 6 |
| Codex agent count | PASS | `find prompts/agents-codex -maxdepth 1 -type f -name '*.md' | wc -l` -> 25 |
| Skill capsule count | PASS | `find prompts/skills -maxdepth 1 -type f -name 'SKILL-*.md' | wc -l` -> 9 |
| JSON reports | PASS | `python3 -m json.tool` passed for schema, token, and wiki injection reports |
| Codex Q3 wording | PASS | no `13 items` remains in `prompts/agents-codex/` or `prompts/skills/` |
| AP-17/wiki packet guard | PASS | AP-17 and `WikiKnowledgePacket` present in affected Codex prompts/reports |
| Main-merge guard | PASS | Codex prompts retain explicit-user/no-ff main merge language |
| Source integrity | PASS | no changed paths under `paper/source/` or `data/raw/` |
| Whitespace | PASS | `git diff --check` produced no findings |

## Prompt Audit

Q3-AUDIT summary:

| Item | Verdict | Evidence |
|---|---|---|
| Q3-01 local generation boundary | PASS | upstream supplies only submodule metaprompts; no upstream generated agents copied |
| Q3-10 main merge guard | PASS | Codex runtime and coordinator prompts preserve explicit-user/no-ff language |
| Q3-11 project profile preserved | PASS | `kernel-project.md` unchanged |
| Q3-13 telemetry | PASS_WITH_WAIVER | telemetry schema updated; tokenizer counts still waived |
| Q3-14 wiki packet source scope | PASS | `wiki_knowledge_injection_report.json` records deferred `WIKI-HTB` packet as reference/on-demand |
| Q3-15 wiki text compression | PASS | no full wiki prose embedded into Codex prompts |

## K-COMPILE

No new canonical wiki entry was created. The reusable lesson is recorded in the
active ledger as `LES-RESEARCH-PROMPT-SUBMODULE-001`; it is a prompt-maintenance
process note rather than a validated research knowledge card.
