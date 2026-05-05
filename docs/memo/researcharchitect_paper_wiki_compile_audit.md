# ResearchArchitect Paper-to-Wiki Compile Audit

## Task

Compile knowledge worth carrying forward from the local ransomware heavy-tail
backup manuscript into the project wiki. Repeat extraction until no new
wiki-ready knowledge appears or the process exceeds 20 rounds.

## Source Material

- `paper/source/heavy_tail_backup_v13.txt`
- `paper/source/heavy_tail_backup_v13.pdf` was not modified.
- `paper/sections/tex/*.tex`
- Prior repair/audit context:
  - `docs/memo/researcharchitect_paper_review_audit.md`
  - `docs/memo/researcharchitect_math_derivation_audit.md`
  - `docs/memo/researcharchitect_major_review_rounds.md`

## Method

PLAN:
Read the active research contract, project rules, ledger, manuscript source,
recast sections, and prior audits.

EXECUTE:
Iteratively scan the paper for reusable research knowledge. Add an item only
when it is distinct, useful for future research, and can be bounded by explicit
assumptions.

VERIFY:
Cross-check each candidate against recast manuscript sections and prior audits
so obsolete source-text formulas are not promoted.

AUDIT:
Record the round log, stopping condition, outputs, and residual risks.

## Round Log

| Round | New wiki-ready knowledge | Disposition |
|-------|--------------------------|-------------|
| 1 | Detection and backup are coupled controls under contaminated backups. | Added WIKI-HTB-001 |
| 2 | Heavy-tailed dwell time invalidates average-case backup reasoning when `alpha <= 1`. | Added WIKI-HTB-002 |
| 3 | Semi-Markov framing handles non-exponential residence times. | Added WIKI-HTB-003 |
| 4 | Positive detection rate makes `E[min(T_det,T_d)]` finite for all `alpha > 0`. | Added WIKI-HTB-004 |
| 5 | Early-detection cost should be separated from residual late-detection loss. | Added WIKI-HTB-005 |
| 6 | The clean-backup horizon is `n Delta`, with domain `Delta > t_m/n`. | Added WIKI-HTB-006 |
| 7 | Holding-boundary removal yields an `alpha=1` residual-loss transition under `kappa_s > 0`. | Added WIKI-HTB-007 |
| 8 | Interior residual-loss minimizer has a closed form under explicit conditions. | Added WIKI-HTB-008 |
| 9 | The design formula is better read as a clean-recovery horizon `a* = n Delta*`. | Added WIKI-HTB-009 |
| 10 | High attack frequency makes fixed backup cost secondary on a compact policy band. | Added WIKI-HTB-010 |
| 11 | Dynamic retention is an integer convex trade-off; evaluate neighboring integers. | Added WIKI-HTB-011 |
| 12 | Numerical example values are sanity checks and must not be promoted as empirical recommendations. | Added WIKI-HTB-012 |
| 13 | Candidate questions for AI anomaly detection concern observation unit, time-to-detection, alert action, and recovery horizon. | Added carry-forward question list |
| 14 | No distinct new wiki-ready knowledge; remaining material was proof detail or bibliography. | Saturation check |
| 15 | No distinct new wiki-ready knowledge after rechecking conclusion and prior audits. | Stop: no new knowledge before 20-round cap |

## Produced Artifacts

- `docs/wiki/00_index.md`
- `docs/wiki/ransomware_heavy_tail_backup_design.md`
- `docs/evidence/heavy_tail_backup_source_note.md`

## Verification Notes

- Source files under `paper/source/` were not modified.
- The wiki uses the corrected recast manuscript sections for formulas that were
  previously repaired by audit.
- The older extracted source text is treated as provenance, not as final
  mathematical authority.
- The process stopped after 15 rounds because two consecutive saturation rounds
  produced no distinct new wiki-ready knowledge, below the 20-round cap.

## Residual Risks

- External ransomware reports and standards cited by the manuscript were not
  independently re-verified in this task.
- The wiki page is a research-memory artifact, not a complete literature review.
- The active AI anomaly-detection domain remains unset; the page should be used
  as a source of design questions unless ResearchArchitect later registers a
  ransomware-backup domain.
