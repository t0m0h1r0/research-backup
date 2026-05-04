# GENERATED - live state file. Append rather than rewrite during normal agent work.

# 02_ACTIVE_LEDGER

## §ACTIVE_STATE

| Field | Value |
|-------|-------|
| phase | DEPLOYED |
| branch | main |
| current_objective | Start AI-assisted anomaly detection research with deployed research agents |
| active_brief | `docs/interface/ResearchBrief.md` |
| source_artifact | none registered yet |
| next_action | Dispatch ASM-AD-001 to TaskPlanner for domain/taxonomy/research-question framing |
| updated_at_utc | 2026-05-04T03:01:56Z |

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

## §ASSUMPTIONS

| ID | Status | Statement | Owner |
|----|--------|-----------|-------|
| ASM-AD-001 | OPEN | The user wants broad AI-based anomaly detection research support before narrowing domain or dataset. | M |
| ASM-AD-002 | OPEN | No active source paper, benchmark dataset, or application domain has been selected yet. | M/E |
| ASM-AD-003 | OPEN | Literature and benchmark protocol should precede any SOTA or performance claim. | E |
| ASM-AD-004 | OPEN | Existing T/R/E/A domains can route model design, implementation, evaluation, and writing without kernel changes. | Q |

## §LESSONS

| ID | Status | Lesson | Artifact |
|----|--------|--------|----------|
| LES-AD-001 | ACTIVE | Project retargeting should change `kernel-project.md` and generated runtime docs while keeping the generic kernel stable. | `prompts/meta/kernel-project.md` |
| LES-AD-002 | ACTIVE | Anomaly detection research needs explicit leakage, thresholding, and benchmark-compatibility gates before writing claims. | `docs/03_PROJECT_RULES.md` |

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
