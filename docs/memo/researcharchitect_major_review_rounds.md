# ResearchArchitect Major Review Rounds

## Stopping Rule

Repeat reviewer audit and repair until either:

- no MAJOR-or-higher findings remain; or
- more than 10 review rounds have been attempted.

Severity vocabulary:

- BLOCKER: invalidates the paper artifact or prevents verification.
- CRITICAL: invalidates a central theorem or numerical conclusion.
- MAJOR: a reviewer could reasonably reject without repair because a claim,
  definition, or reproducibility path is materially incomplete or inconsistent.
- MINOR: style, local clarity, or non-central polish.

## Round 1

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R1-MAJ-01 | MAJOR | The manuscript states `C=\lambda Q+\cdots` as an exact renewal-reward rate even though an ordinary regenerative semi-Markov cycle would divide rewards by a cycle length containing attack-arrival and recovery times. | Recast the rate theorem as a calendar-time marked-Poisson incident-accounting result; keep the semi-Markov path as the per-incident reward kernel; add an explicit finite early-detection reward assumption. |
| R1-MAJ-02 | MAJOR | The backup definition uses `k=\lceil T/\Delta\rceil`, but the loss model uses the retention horizon `n\Delta`. These are off by one for generation counting. | Define the primitive recovery rule by the holding horizon `a_n=n\Delta`; use `\lfloor T/\Delta\rfloor` only as a mnemonic generation count. |
| R1-MAJ-03 | MAJOR | The reproducible check reports `\Delta^\ast` from the first derivative root without explicitly comparing endpoints and other stationary points on the compact policy band. | Update the script to evaluate all stationary candidates and endpoints using the same residual-loss definition as the manuscript. |

### Status

DONE. All three MAJOR findings were repaired and verified.

## Round 2

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R2-MAJ-01 | MAJOR | After R1-MAJ-01, the model introduction still described full loss or recovery as the end of an "update cycle", which conflicted with the revised calendar-time Poisson accounting. | Reworded the semi-Markov object as a per-incident path whose terminal event records the incident reward. |

### Status

DONE. The stale renewal-cycle wording was removed from the manuscript.

## Round 3

### MAJOR Findings

None.

### Verification

- `python3 analysis/paper_review_checks/run.py`: PASS.
- `latexmk -xelatex heavy_tail_backup_recast_xelatex.tex` from `paper/sections`: PASS.
- Final LaTeX log scan for `Warning`, `Overfull`, `Underfull`, `undefined`, `Undefined`, `Error`, and `Missing`: no matches.
- Stale-claim scans for renewal-cycle wording, old ceiling-based generation counting, fixed numbered assumptions, old first-root-only numerical check, and stale unit text: no manuscript matches.

## Stop Decision

Stopped after Round 3 because MAJOR-or-higher findings are zero. This is below
the 10-round cap.
