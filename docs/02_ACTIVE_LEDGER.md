# GENERATED - live state file. Append rather than rewrite during normal agent work.

# 02_ACTIVE_LEDGER

## §ACTIVE_STATE

| Field | Value |
|-------|-------|
| phase | DEPLOYED |
| branch | main |
| current_objective | Deploy generic research-agent kernel for paper improvement |
| source_artifact | `paper/source/heavy_tail_backup_v13.pdf` |
| next_action | Dispatch first proof-audit task for ASM-001 or ASM-002 |
| updated_at_utc | 2026-05-04T02:14:45Z |

## §CHECKLIST

| ID | Status | Domain | Artifact | Note | Date |
|----|--------|--------|----------|------|------|
| CHK-001 | DONE | P | `prompts/meta/kernel-project.md` | replaced CFD profile with generic paper-agent profile | 2026-05-04 |
| CHK-002 | DONE | P | `prompts/meta/kernel-domains.md` | installed generic T/R/E/A research domain registry | 2026-05-04 |
| CHK-003 | DONE | M | `paper/source/heavy_tail_backup_v13.txt` | extracted PDF text for agent-readable source | 2026-05-04 |
| CHK-004 | READY | T | `docs/memo/asm_001_renewal_reward.md` | first recommended proof audit | 2026-05-04 |

## §ASSUMPTIONS

| ID | Status | Statement | Owner |
|----|--------|-----------|-------|
| ASM-001 | OPEN | The renewal-reward theorem is applicable for all alpha > 0 when beta(I) > 0. | T |
| ASM-002 | OPEN | Tauber remainder bound is sufficient for the claimed phase-transition result. | T |
| ASM-003 | OPEN | The closed-form optimal interval is the unique global minimizer under stated parameter constraints. | T |
| ASM-004 | OPEN | The compactness argument uses a lambda-independent bound strong enough for convergence. | T |

## §LESSONS

| ID | Status | Lesson | Artifact |
|----|--------|--------|----------|
| LES-001 | ACTIVE | Paper-improvement agents must output both research artifact and workflow artifact when PR-1 applies. | `prompts/meta/kernel-project.md` |

## §REPLAN_LOG

| ID | Date | Trigger | Decision |
|----|------|---------|----------|
| RPL-001 | 2026-05-04 | CFD-specific kernel used for non-CFD paper | Retarget kernel to generic research workflow and keep topic in project profile |

## §4 BRANCH_LOCK_REGISTRY

| ID | Branch | Worktree | Objective | Status | Updated |
|----|--------|----------|-----------|--------|---------|
| A-XELATEX-001 | `codex/researcharchitect-xelatex` | `worktrees/researcharchitect-xelatex` | XeLaTeX recast of `heavy_tail_backup_v13.pdf` | VALIDATED | 2026-05-04 |
| A-REVIEW-001 | `codex/researcharchitect-paper-review` | `worktrees/researcharchitect-paper-review` | Whole-paper reviewer audit, narrative repair, and notation unification | VALIDATED | 2026-05-04 |
