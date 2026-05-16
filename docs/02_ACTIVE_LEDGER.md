# GENERATED - live state file. Append rather than rewrite during normal agent work.

# 02_ACTIVE_LEDGER

## §ACTIVE_STATE

| Field | Value |
|-------|-------|
| phase | PRESENTATION_THEATRICAL_CLARITY_VALIDATED |
| branch | `codex/researcharchitect-presentation-refine` |
| current_objective | Refine the heavy-tail backup research presentation, regenerate polished and theatrical editable decks, iterate review/fix loops to convergence, and preserve traceable presentation artifacts |
| active_brief | `docs/interface/ResearchBrief.md` |
| source_artifact | prompt task: `prompts/research-agent` at `ed388737ed01c479df4905925f1ec6791ff0f47d`; `prompts/meta/kernel-project.md` preserved at SHA-256 `38823508fca2e28a5cc884081be8e4b1c954329e5ebc301d60fde2865aa8e61d`; anomaly-detection research source still not selected |
| next_action | Await user review or explicit merge instruction for the clarified theatrical heavy-tail backup deck; do not merge to main without explicit user instruction |
| updated_at_utc | 2026-05-16T22:40:06Z |

## §CHECKLIST

| ID | Status | Domain | Artifact | Note | Date |
|----|--------|--------|----------|------|------|
| CHK-AD-001 | DONE | P | `prompts/meta/kernel-project.md` | retargeted project profile to AI anomaly detection research | 2026-05-04 |
| CHK-AD-002 | DONE | P | `docs/03_PROJECT_RULES.md` | regenerated PR-1..PR-6 for anomaly detection | 2026-05-04 |
| CHK-AD-003 | DONE | M | `docs/01_PROJECT_MAP.md` | registered active brief, directories, and initial task queue | 2026-05-04 |
| CHK-AD-004 | DONE | M | `docs/interface/ResearchBrief.md` | captured initial user scope as active contract | 2026-05-04 |
| CHK-AD-005 | DONE | P | `prompts/agents-codex/`, `prompts/agents-claude/` | 23 agent files per environment verified | 2026-05-04 |
| CHK-AD-006 | READY | M | `docs/memo/anomaly_detection_problem_frame.md` | first recommended planning artifact | 2026-05-04 |
| CHK-RESEARCH-001 | DONE | T | `docs/memo/researcharchitect_math_derivation_audit.md` | strict derivation audit classified three MAJOR root-cause issues | 2026-05-04 |
| CHK-RESEARCH-002 | DONE | A/R | `paper/sections/tex/`, `analysis/paper_review_checks/run.py` | repaired theorem domains, added tilted-moment proof, and guarded reproducible checks | 2026-05-04 |
| CHK-RESEARCH-003 | DONE | Q | `analysis/paper_review_checks/results/manifest.json` | Python recomputation and XeLaTeX build passed after math repairs | 2026-05-04 |
| CHK-RESEARCH-004 | DONE | A/T | `paper/sections/tex/04_tauber_transition.tex`, `paper/sections/tex/02_model_formulation.tex` | reviewer Round 4 aligned narrative, removed dead `T_e`, and recast the transition theorem around the repaired residual loss | 2026-05-04 |
| CHK-RESEARCH-005 | DONE | A/R | `paper/sections/tex/06_dynamic_retention.tex`, `analysis/paper_review_checks/run.py` | reviewer Round 5 separated cost-rate retention notation from one-period retention cost notation | 2026-05-04 |
| CHK-RESEARCH-006 | DONE | Q | `docs/memo/researcharchitect_major_review_rounds.md` | reviewer Round 6 found no MAJOR-or-higher findings before the 10-round cap | 2026-05-04 |
| CHK-RESEARCH-007 | DONE | A/Q | `paper/sections/tex/00_abstract.tex`, `paper/sections/tex/05_backup_optimization.tex`, `paper/sections/tex/08_conclusion.tex` | reviewer Rounds 7-8 repaired applied-research takeaway clarity and verified no MAJOR-or-higher findings | 2026-05-04 |
| CHK-RESEARCH-008 | DONE | A/Q | `paper/sections/tex/00_title.tex`, `paper/sections/tex/01_introduction.tex`, `paper/sections/tex/06_dynamic_retention.tex`, `paper/sections/tex/07_numerical_examples.tex` | reviewer Rounds 9-10 aligned research motivation and section framing with the clean-backup recovery-horizon conclusion | 2026-05-04 |
| CHK-RESEARCH-009 | DONE | A/R/Q | `paper/sections/tex/06_dynamic_retention.tex`, `paper/sections/tex/07_numerical_examples.tex`, `analysis/paper_review_checks/run.py` | reopened strict review repaired dynamic-retention horizon consistency and verified no MAJOR-or-higher findings | 2026-05-04 |
| CHK-RESEARCH-010 | DONE | P/M | `AGENTS.md`, `prompts/agents-codex/`, `prompts/meta/kernel-roles.md`, `prompts/meta/kernel-deploy.md`, `artifacts/P/codex_config_optimization_audit.md` | optimized Codex worktree, commit, user-change, and explicit-user/no-ff main-merge guardrails | 2026-05-04 |
| CHK-RESEARCH-011 | DONE | P/M | `AGENTS.md`, `prompts/README.md`, `prompts/meta/kernel-deploy.md`, `artifacts/P/agents_instruction_optimization_audit.md` | refined external-agent first-read instructions, artifact placement map, research gates, and prompt-maintenance path | 2026-05-04 |
| CHK-RESEARCH-012 | DONE | M/E | `docs/wiki/ransomware_heavy_tail_backup_design.md`, `docs/evidence/heavy_tail_backup_source_note.md`, `docs/memo/researcharchitect_paper_wiki_compile_audit.md` | compiled 12 reusable manuscript-derived knowledge items after 15 extraction rounds and stopped on saturation before the 20-round cap | 2026-05-05 |
| CHK-RESEARCH-013 | DONE | P/A/M | `prompts/agents-codex/PresentationWriter.md`, `prompts/agents-claude/PresentationWriter.md`, `prompts/skills/SKILL-PRESENTATION-DECK.md`, `artifacts/P/presentation_agent_deployment_audit.md` | deployed a paper-grounded presentation-materials agent with lead-line, visual-plan, traceability, and prompt-audit gates | 2026-05-05 |
| CHK-RESEARCH-014 | DONE | P/A/M | `prompts/skills/SKILL-PRESENTATION-DECK.md`, `prompts/agents-codex/PresentationWriter.md`, `prompts/agents-claude/PresentationWriter.md`, `prompts/agents-codex/PaperReviewer.md`, `prompts/agents-claude/PaperReviewer.md` | added narrative-spine design, slide-budget compression, message-budget output, and third-party listener critique for presentation decks | 2026-05-05 |
| CHK-RESEARCH-015 | DONE | P/K/M | `prompts/meta/kernel-workflow.md`, `prompts/meta/kernel-ops.md`, `prompts/agents-codex/_base.yaml`, `prompts/agents-claude/_base.yaml`, `artifacts/P/wiki_memory_gate_deployment_audit.md` | added WIKI-RETRIEVAL-GATE and WIKI-COMPILE-GATE so agents search prior wiki knowledge before difficult work and compile important validated findings back to wiki memory | 2026-05-05 |
| CHK-RESEARCH-016 | DONE | P/M/Q | `prompts/skills/SKILL-PROMPT-AUDIT.md`, `prompts/skills/SKILL-PRESENTATION-DECK.md`, `prompts/meta/kernel-roles.md`, `artifacts/P/prompt_roi_review_audit.md` | completed 4 prompt-engineering review rounds, removed broad-read instructions, compressed presentation skill, and added token-ROI/broad-preload self-audit gates | 2026-05-05 |
| CHK-RESEARCH-017 | DONE | A/Q | `paper/presentations/heavy_tail_backup_intro/` | created a 5-slide paper-grounded research presentation and completed 3 review rounds with no remaining CRITICAL, MAJOR, or MINOR findings | 2026-05-05 |
| CHK-RESEARCH-018 | DONE | P/M/Q | `prompts/meta/kernel-roles.md`, `prompts/agents-codex/PromptAuditor.md`, `prompts/agents-claude/PromptAuditor.md`, `artifacts/P/researcharchitect_agent_refresh_audit.md` | pulled latest main, verified no pending remote meta delta, and refreshed PromptAuditor main-merge guardrail wording plus validation reports | 2026-05-05 |
| CHK-RESEARCH-019 | DONE | P/M/Q | `prompts/meta/`, `prompts/skills/`, `prompts/agents-codex/`, `prompts/agents-claude/`, `prompts/upstream.toml`, `artifacts/P/researcharchitect_metaprompt_redeploy_audit.md` | synced upstream metaprompt revision `c985b65`, preserved `kernel-project.md`, regenerated local support artifacts and prompts, and ran prompt audit checks | 2026-05-06 |
| CHK-RESEARCH-020 | DONE | A/Q | `paper/presentations/heavy_tail_backup_intro/` | zero-base recreated the 5-slide heavy-tail backup presentation, completed 3 review rounds, addressed all findings, and stopped after Round 3 because no MAJOR-or-higher findings remained | 2026-05-06 |
| CHK-RESEARCH-PROMPT-003 | DONE | P/M/Q | `.gitmodules`, `prompts/upstream/research-agent`, `prompts/meta/`, `prompts/agents-codex/`, `wiki_knowledge_injection_report.json`, `artifacts/P/researcharchitect_metaprompt_submodule_redeploy_audit.md` | added `research-agent` as pinned metaprompt submodule at `f52ae6f`, preserved `kernel-project.md`, redeployed Codex prompts to 25 files including `VerificationRunner`, and validated Q3/AP-17/wiki-packet checks | 2026-05-16 |
| CHK-RESEARCH-PROMPT-004 | DONE | P/M/Q | `.gitmodules`, `prompts/research-agent`, `prompts/meta/`, `prompts/agents-codex/`, `prompts/agents-claude/`, `prompts/skills/`, `token_roi_report.json`, `artifacts/P/researcharchitect_direct_metaprompt_zero_deploy_audit.md` | removed the `prompts/upstream/` directory, pinned direct research-agent revision `ed388737`, preserved `kernel-project.md` by SHA guard, and zero-base redeployed generated prompts, skills, telemetry, token ROI, and schema reports to `v8.7.0-candidate` | 2026-05-17 |
| CHK-RESEARCH-PRESENTATION-REFINE-001 | DONE | A/M/Q | `paper/presentations/heavy_tail_backup_refined/`, `docs/02_ACTIVE_LEDGER.md` | refined the heavy-tail backup presentation into a stronger 6-slide research talk, completed 2 review rounds, passed artifact-tool render/layout/package QA, and stopped with no unresolved findings | 2026-05-17 |
| CHK-RESEARCH-PRESENTATION-REFINE-002 | DONE | A/M/Q | `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`, `paper/presentations/heavy_tail_backup_refined/review_reports/round3.md` | created a more theatrical dark-room version with stronger contrast and larger visual claims while preserving source boundaries; layout and package QA passed | 2026-05-17 |
| CHK-RESEARCH-PRESENTATION-REFINE-003 | DONE | A/M/Q | `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`, `paper/presentations/heavy_tail_backup_refined/review_reports/round4.md` | clarified the theatrical deck after user review by replacing unclear terminology, labeling chart axes, and adding formula-focus guidance; layout and package QA passed | 2026-05-17 |

## §ASSUMPTIONS

| ID | Status | Statement | Owner |
|----|--------|-----------|-------|
| ASM-AD-001 | OPEN | The user wants broad AI-based anomaly detection research support before narrowing domain or dataset. | M |
| ASM-AD-002 | OPEN | No active source paper, benchmark dataset, or application domain has been selected yet. | M/E |
| ASM-AD-003 | OPEN | Literature and benchmark protocol should precede any SOTA or performance claim. | E |
| ASM-AD-004 | OPEN | Existing T/L/E/A domains can route model design, implementation, evaluation, and writing without kernel changes. | Q |
| ASM-AD-005 | OPEN | The ransomware heavy-tail backup manuscript provides model-derived wiki questions, but does not by itself select the active anomaly-detection domain or benchmark. | M/E |

## §LESSONS

| ID | Status | Lesson | Artifact |
|----|--------|--------|----------|
| LES-AD-001 | ACTIVE | Project retargeting should change `kernel-project.md` and generated runtime docs while keeping the generic kernel stable. | `prompts/meta/kernel-project.md` |
| LES-AD-002 | ACTIVE | Anomaly detection research needs explicit leakage, thresholding, and benchmark-compatibility gates before writing claims. | `docs/03_PROJECT_RULES.md` |
| LES-RESEARCH-CODEX-001 | ACTIVE | Codex agent prompts need an inherited runtime profile plus local coordinator wording so no generated role implies unilateral `main` merge. | `prompts/agents-codex/_base.yaml` |
| LES-RESEARCH-CODEX-002 | ACTIVE | External-agent instructions work best as a read-order and artifact-placement map, with detailed operation bodies kept in kernel files and skill capsules. | `AGENTS.md` |
| LES-RESEARCH-WIKI-001 | ACTIVE | When a protected source extract and repaired manuscript sections differ, wiki compilation should prefer the repaired sections and leave a source-boundary note. | `docs/evidence/heavy_tail_backup_source_note.md` |
| LES-RESEARCH-PRESENTATION-001 | ACTIVE | Paper-to-presentation agents need a source map, one-message slide discipline, large 1-2 line lead text, and a concrete or abstract visual plan per slide to avoid unsupported narrative drift. | `prompts/skills/SKILL-PRESENTATION-DECK.md` |
| LES-RESEARCH-PRESENTATION-002 | ACTIVE | Deck creation should first compress the paper into a narrative spine and message budget, then require an independent listener-perspective critique of clarity, recall, and cognitive load. | `prompts/skills/SKILL-PRESENTATION-DECK.md` |
| LES-RESEARCH-WIKI-002 | ACTIVE | Wiki memory needs explicit start-of-task retrieval triggers and end-of-task compilation triggers; otherwise agents treat `docs/wiki/` as archival rather than operational memory. | `prompts/meta/kernel-workflow.md` |
| LES-RESEARCH-PROMPT-ROI-001 | ACTIVE | Prompt evolution should reject broad preloading and low-ROI text by default; details belong in JIT skills or kernel references unless they change agent behavior enough to justify token cost. | `prompts/skills/SKILL-PROMPT-AUDIT.md` |
| LES-RESEARCH-PROMPT-MERGE-001 | ACTIVE | PromptAuditor main-merge checks should name the required explicit-user and no-ff guardrails directly so safety scans do not mistake a fail condition for an unsafe permission. | `prompts/meta/kernel-roles.md` |
| LES-RESEARCH-PROMPT-UPSTREAM-001 | ACTIVE | Upstream metaprompt sync must copy only shared kernel sources, preserve project-local `kernel-project.md`, and regenerate local skills/prompts before removing `REDEPLOY_REQUIRED`. | `prompts/upstream.toml` |
| LES-RESEARCH-PROMPT-SUBMODULE-001 | ACTIVE | Pinning `research-agent` as a submodule makes upstream metaprompt provenance reviewable while `prompts/meta/kernel-project.md` remains the project-local profile overlay. | `prompts/upstream.toml` |
| LES-RESEARCH-PROMPT-DIRECT-001 | ACTIVE | The metaprompt submodule should live directly at `prompts/research-agent`; the `prompts/upstream/` directory adds a needless layer and increases profile-preservation risk. | `prompts/research-agent` |

## §REPLAN_LOG

| ID | Date | Trigger | Decision |
|----|------|---------|----------|
| RPL-AD-001 | 2026-05-04 | Previous project profile did not match new anomaly detection research objective | Retarget project profile and redeploy runtime docs/reports for anomaly detection |

## §4 BRANCH_LOCK_REGISTRY

| ID | Branch | Worktree | Objective | Status | Updated |
|----|--------|----------|-----------|--------|---------|
| none | main | n/a | no active branch lock | INACTIVE | 2026-05-04 |
| A-XELATEX-001 | `codex/researcharchitect-xelatex` | `worktrees/researcharchitect-xelatex` | XeLaTeX recast of `heavy_tail_backup_v13.pdf` | VALIDATED | 2026-05-04 |
| A-REVIEW-001 | `codex/researcharchitect-paper-review` | `worktrees/researcharchitect-paper-review` | Whole-paper reviewer audit, narrative repair, and notation unification | MERGED | 2026-05-04 |
| RESEARCH-MATH-001 | `codex/researcharchitect-math-audit` | `worktrees/researcharchitect-math-audit` | Strict derivation audit and root-cause repair for manuscript equations; session `fae80cac-2527-40e9-b80a-8d3a891de483`; id_prefix `RESEARCH` | VALIDATED | 2026-05-04 |
| RESEARCH-CODEX-001 | `codex/researcharchitect-codex-config` | `/private/tmp/research-backup-codex-config` | Optimize Codex agent configuration files; session `073ed11d-d33c-4fde-989e-446bd7544029`; id_prefix `RESEARCH` | MERGED | 2026-05-04 |
| RESEARCH-WIKI-001 | `codex/researcharchitect-paper-wiki` | `/private/tmp/research-backup-paper-wiki` | Compile manuscript-derived ransomware heavy-tail backup knowledge into wiki; id_prefix `RESEARCH` | VALIDATED | 2026-05-05 |
| RESEARCH-PRESENTATION-001 | `codex/researcharchitect-presentation-agent` | `/private/tmp/research-backup-presentation-agent` | Deploy a paper-grounded presentation-materials agent and prompt audit gates; id_prefix `RESEARCH` | VALIDATED | 2026-05-05 |
| RESEARCH-PRESENTATION-DECK-001 | `codex/researcharchitect-paper-presentation` | `/private/tmp/research-backup-paper-presentation` | Create and review a 5-slide paper-grounded research presentation for the heavy-tail backup manuscript; id_prefix `RESEARCH-PRESENTATION-DECK` | VALIDATED | 2026-05-05 |
| RESEARCH-PROMPT-001 | `codex/researcharchitect-agent-update` | `/private/tmp/research-backup-agent-update` | Refresh generated agents after prompt-system update check; id_prefix `RESEARCH-PROMPT` | VALIDATED | 2026-05-05 |
| RESEARCH-PROMPT-002 | `codex/researcharchitect-meta-master-redeploy` | `/private/tmp/research-backup-meta-master-redeploy` | Sync and redeploy upstream metaprompt revision `c985b65`; id_prefix `RESEARCH-PROMPT` | VALIDATED | 2026-05-06 |
| RESEARCH-PROMPT-003 | `codex/researcharchitect-metaprompt-submodule-redeploy` | `/private/tmp/research-backup-metaprompt-submodule-redeploy` | Add pinned `research-agent` metaprompt submodule, sync revision `f52ae6f`, and redeploy Codex prompts; session `B1E9BE83-0B3E-4FCD-B417-18FA6719912F`; id_prefix `RESEARCH-PROMPT` | VALIDATED | 2026-05-16 |
| RESEARCH-PROMPT-004 | `codex/researcharchitect-direct-metaprompt-zero-deploy` | `/private/tmp/research-backup-direct-metaprompt-zero-deploy` | Remove `prompts/upstream/`, pin direct `prompts/research-agent` revision `ed388737`, preserve `kernel-project.md`, and zero-base redeploy generated prompt artifacts; session `56003F54-E3F9-4EB9-BD81-7D9980B7714D`; id_prefix `RESEARCH-PROMPT` | VALIDATED | 2026-05-17 |
| RESEARCH-PRESENTATION-ZERO-001 | `codex/researcharchitect-paper-presentation-zero-base` | `/private/tmp/research-backup-paper-presentation-zero-base` | Recreate the heavy-tail backup presentation from zero and complete review/fix loops; id_prefix `RESEARCH-PRESENTATION-ZERO` | VALIDATED | 2026-05-06 |
| RESEARCH-PRESENTATION-REFINE-001 | `codex/researcharchitect-presentation-refine` | `/private/tmp/research-backup-presentation-refine` | Refine and regenerate the heavy-tail backup presentation with a stronger 6-slide research narrative and convergence review; id_prefix `RESEARCH-PRESENTATION-REFINE` | VALIDATED | 2026-05-17 |
