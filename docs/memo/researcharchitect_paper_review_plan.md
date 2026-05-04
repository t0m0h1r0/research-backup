# ResearchArchitect Paper Review Plan

## Scope

- Target: `paper/sections/tex/*.tex` and the generated wrapper `paper/sections/heavy_tail_backup_recast_xelatex.tex`.
- Source evidence: `paper/source/heavy_tail_backup_v13.txt`; never overwrite `paper/source/heavy_tail_backup_v13.pdf`.
- Branch lock: `A-REVIEW-001` on `codex/researcharchitect-paper-review`.

## Review Emphasis

1. Reviewer-grade correctness: assumptions, theorem statements, proof dependencies, citations, and claims.
2. Narrative coherence: contribution, model, renewal-reward reduction, heavy-tail transition, optimization, and dynamic policy should read as one argument.
3. Notation consistency: backup interval, lifetime law, survival/tail notation, cost symbols, cache-mix symbols, and asymptotic regimes.
4. Root-cause repair: fix confusing structure or definitions at their first point of use rather than patching symptoms locally.

## Execution Path

1. Audit the compiled paper sections and source text for discrepancies, narrative gaps, and notation drift.
2. Apply structural paper edits in `paper/sections/tex/`.
3. Add an audit memo in `docs/memo/` recording findings, fixes, and residual risks.
4. Verify with LaTeX compilation when a local TeX engine is available, plus text-level consistency checks.
