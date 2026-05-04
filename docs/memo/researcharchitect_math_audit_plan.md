# ResearchArchitect Math Audit Plan

## Scope

- Target: mathematical derivations in `paper/sections/tex/*.tex`, with priority on
  the loss model, Pareto/Tauber asymptotics, backup-interval optimum, and dynamic
  retention rule.
- Evidence inputs: manuscript sources in `paper/sections/tex/`, extracted source
  text in `paper/source/heavy_tail_backup_v13.txt`, and reproducible checks under
  `analysis/paper_review_checks/`.
- Protected source artifact: do not modify `paper/source/heavy_tail_backup_v13.pdf`.
- Branch lock: `codex/researcharchitect-math-audit`,
  session `fae80cac-2527-40e9-b80a-8d3a891de483`, id prefix `RESEARCH`.

## Classification

- Task class: FULL-PIPELINE because the request targets proof correctness and may
  require manuscript changes.
- Owning domains: T for derivation audit and fixes, A for manuscript patches, R/E
  for reproducible numerical checks if equations or tables change.
- Stopping rule: continue review/repair rounds until no MAJOR-or-higher
  derivation finding remains, or stop with a concrete blocker.

## Execution Path

1. Re-derive the central equations from primitive branch probabilities before
   editing prose.
2. Classify findings by severity and record them in `docs/memo/`.
3. Apply source-level repairs in the earliest owning section, not local cosmetic
   patches.
4. Re-run reproducible checks and LaTeX/text consistency checks.
5. Commit coherent units as PLAN, FIX, and VERIFY/AUDIT checkpoints.
