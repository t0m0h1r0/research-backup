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

## Round 4

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R4-MAJ-01 | MAJOR | The phase-transition theorem used a simplified `Q_\infty` that did not equal the backup-free limit of the manuscript's repaired residual loss: it omitted `\eta`, `\kappa_s`, `d_0`, and the late full-loss term. This weakens both logical consistency and narrative credibility. | Redefine the theorem using the actual `\Qfull` limit as the holding boundary is removed, state the `\alpha=1` transition under `\kappa_s>0`, and update abstract/introduction/conclusion language. |
| R4-MAJ-02 | MAJOR | The attack-phase definition retained an exponential destruction time `T_e`, but no cost, transition diagram, theorem, or numerical check used it. This creates a dead stochastic object and makes the model look more general than the loss kernel. | Remove `T_e` from the active model and describe the post-onset outcome as the symptom-detection branch already used by `\Qfull`. |
| R4-MAJ-03 | MAJOR | The paper still invoked "renewal reward" as part of its core narrative after the rate formula had been repaired to marked-Poisson/Campbell accounting. The narrative therefore pointed readers toward the wrong denominator-free justification. | Replace core narrative and proof wording with Poisson reward process / Campbell formula language. |
| R4-MAJ-04 | MAJOR | The numerical section assigns `c_b` units of `万円・日`, but the model defines `c_b/\Delta`; therefore `c_b` must be a per-backup fixed cost, not cost times time. | Correct the unit wording to per-backup cost and keep the table values unchanged. |

### Status

IN PROGRESS. Root-level manuscript and check-script repairs are being applied.

## Round 5

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R5-MAJ-01 | MAJOR | The manuscript uses `c_n n_{\mathrm{ext}}` both in the calendar-time cost rate and in the dynamic-retention single-period objective. In the rate equation it must be a cost rate, while in the retention objective it is a one-period storage cost. Reusing the same symbol makes the units inconsistent and undermines the notation discipline. | Define `c_I` and `c_n` in the rate equation as operating cost rates, introduce a separate `c_{\mathrm{ext}}` for the single-period retention objective, and update the reproducible check and numerical caption. |

### Status

IN PROGRESS. Unit/notation separation is being applied.
