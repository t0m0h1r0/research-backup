# Source Note: Heavy-Tail Backup Manuscript

status: SOURCE_NOTE
source_files:
- `paper/source/heavy_tail_backup_v13.pdf`
- `paper/source/heavy_tail_backup_v13.txt`
- `paper/sections/tex/*.tex`

## Evidence Boundary

The protected source PDF and extracted text are local manuscript artifacts.
The recast `paper/sections/tex/*.tex` files include later mathematical repairs
recorded in `docs/memo/researcharchitect_paper_review_audit.md`,
`docs/memo/researcharchitect_math_derivation_audit.md`, and
`docs/memo/researcharchitect_major_review_rounds.md`.

For current mathematical claims, prefer the recast manuscript sections over the
older extracted source text. The extracted source remains useful for provenance
and for identifying earlier claims, but it contains formulations that were later
audited and repaired.

## Current Wiki Consumer

- `docs/wiki/ransomware_heavy_tail_backup_design.md`

## Claim Hygiene

- Model-derived formulas may be used as internal research hypotheses or design
  prompts.
- Empirical statements about ransomware frequency, dwell-time distributions,
  EDR detection rates, recovery durations, or incident losses require separate
  verification before supporting a paper claim.
- Numerical examples are reproducibility checks and scale illustrations unless
  backed by a manifest and source evidence for the parameter values.
