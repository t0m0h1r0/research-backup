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

Round 3 had no MAJOR-or-higher findings under the prior audit scope. The
subsequent user request required a stricter reviewer pass focused on narrative,
notation, and logical consistency, so review continued at Round 4.

## Round 4

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R4-MAJ-01 | MAJOR | The phase-transition theorem used a simplified `Q_\infty` that did not equal the backup-free limit of the manuscript's repaired residual loss: it omitted `\eta`, `\kappa_s`, `d_0`, and the late full-loss term. This weakens both logical consistency and narrative credibility. | Redefine the theorem using the actual `\Qfull` limit as the holding boundary is removed, state the `\alpha=1` transition under `\kappa_s>0`, and update abstract/introduction/conclusion language. |
| R4-MAJ-02 | MAJOR | The attack-phase definition retained an exponential destruction time `T_e`, but no cost, transition diagram, theorem, or numerical check used it. This creates a dead stochastic object and makes the model look more general than the loss kernel. | Remove `T_e` from the active model and describe the post-onset outcome as the symptom-detection branch already used by `\Qfull`. |
| R4-MAJ-03 | MAJOR | The paper still invoked "renewal reward" as part of its core narrative after the rate formula had been repaired to marked-Poisson/Campbell accounting. The narrative therefore pointed readers toward the wrong denominator-free justification. | Replace core narrative and proof wording with Poisson reward process / Campbell formula language. |
| R4-MAJ-04 | MAJOR | The numerical section assigns `c_b` units of `万円・日`, but the model defines `c_b/\Delta`; therefore `c_b` must be a per-backup fixed cost, not cost times time. | Correct the unit wording to per-backup cost and keep the table values unchanged. |

### Status

DONE. The manuscript now uses the actual backup-free limit of `\Qfull` for the
phase-transition theorem, removes dead `T_e` notation, uses Poisson/Campbell
language for the rate argument, and corrects the `c_b` unit.

## Round 5

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R5-MAJ-01 | MAJOR | The manuscript uses `c_n n_{\mathrm{ext}}` both in the calendar-time cost rate and in the dynamic-retention single-period objective. In the rate equation it must be a cost rate, while in the retention objective it is a one-period storage cost. Reusing the same symbol makes the units inconsistent and undermines the notation discipline. | Define `c_I` and `c_n` in the rate equation as operating cost rates, introduce a separate `c_{\mathrm{ext}}` for the single-period retention objective, and update the reproducible check and numerical caption. |

### Status

DONE. The calendar-time rate keeps `c_n` as an operating cost rate, while the
single-period retention problem now uses the separate symbol `c_{\mathrm{ext}}`.
The Python check and generated result parameters were updated accordingly.

## Round 6

### MAJOR Findings

None.

### Verification

- `python3 analysis/paper_review_checks/run.py`: PASS.
- `latexmk -xelatex heavy_tail_backup_recast_xelatex.tex` from
  `paper/sections`: PASS.
- Final LaTeX log scan for `Error`, `undefined`, `Undefined`, `Overfull`,
  `Underfull`, and `Missing`: no matches. Remaining matches are xeCJK font
  redefinition warnings only.
- Stale-claim scan found no active-manuscript matches for dead `T_e`,
  `純粋検知`, old `Q_\infty`, `万円・日`, old `c_n=50`, or old
  dynamic-retention positivity notation.

## Round 6 Interim Stop Decision

Stopped after Round 6 because MAJOR-or-higher findings are zero. This is below
the 10-round cap. A subsequent user review reopened the narrative audit for
applied-research clarity.

## Round 7

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R7-MAJ-01 | MAJOR | The abstract and conclusion foregrounded derivation details while leaving the applied conclusion implicit. For an applied ransomware-defense paper, a reader should immediately understand what the formulas recommend for defense and backup recovery operations. | Rewrite the abstract and conclusion around the practical takeaway: detection alone is insufficient, clean-backup recovery horizon is a first-class defense variable, and the design formula gives an operational rule for backup interval and retained generations. Move the detailed interpretation of the formula into Section 5 as part of the derivation discussion. |

### Status

DONE. The abstract now opens with the applied conclusion and three practical
recommendations. The conclusion now states the defense and recovery implications
in plain language before summarizing the mathematical contributions. Section 5
now includes a dedicated practical interpretation of the closed-form design
rule.

## Round 8

### MAJOR Findings

None.

### Verification

- `python3 analysis/paper_review_checks/run.py`: PASS.
- `latexmk -xelatex heavy_tail_backup_recast_xelatex.tex` from
  `paper/sections`: PASS.
- Final LaTeX log scan for `Warning`, `Overfull`, `Underfull`, `undefined`,
  `Undefined`, `Error`, and `Missing`: only existing xeCJK font redefinition
  warnings remain.
- Active-manuscript scan found no matches for stale reviewer-facing wording such
  as `査読上`, `小難しい`, or `未条件化`. Historical memo entries remain only as
  audit history.

## Round 8 Interim Stop Decision

Stopped after Round 8 because MAJOR-or-higher findings are zero. This remains
below the 10-round cap. A subsequent user review reopened the narrative audit
for consistency between research motivation and the applied conclusion.

## Round 9

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| R9-MAJ-01 | MAJOR | After R7, the abstract and conclusion clearly stated that detection alone is insufficient and that clean-backup recovery horizon is the applied design variable, but the title, introduction, numerical examples, and dynamic-retention setup still foregrounded mathematical generality more than the operational motivation. This left the manuscript's narrative arc inconsistent. | Retitle the paper around clean-backup retention and ransomware defense, rewrite the introduction from the practical problem of contaminated recent backups, recast the contribution list around recovery-horizon design, and add applied framing to the numerical and dynamic-retention sections. |

### Status

DONE. The manuscript now opens from the practical defense problem, introduces
heavy-tailed dwell time as the reason recent backups may be contaminated, frames
the model around the effective clean-recovery horizon `n\Delta`, and connects
the numerical and dynamic-retention sections back to operational backup
decisions.

## Round 10

### MAJOR Findings

None.

### Verification

- `python3 analysis/paper_review_checks/run.py`: PASS.
- `latexmk -xelatex heavy_tail_backup_recast_xelatex.tex` from
  `paper/sections`: PASS.
- Final LaTeX log scan for `Warning`, `Overfull`, `Underfull`, `undefined`,
  `Undefined`, `Error`, and `Missing`: only existing xeCJK font redefinition
  warnings remain.
- Narrative scan confirmed that the title, abstract, introduction, numerical
  examples, dynamic retention, and conclusion all use the same core terms:
  detection limitation, clean backup, recovery horizon, backup interval, and
  operational design.

## Round 10 Interim Stop Decision

Stopped after Round 10 because MAJOR-or-higher findings are zero. This reaches
but does not exceed the 10-round cap. A subsequent user review reopened the
strict-review loop, so the next pass is tracked as a new post-Round-10 cycle
rather than extending the closed 10-round sequence.

## Post-Round-10 Cycle, Round 1

### MAJOR Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| P10-R1-MAJ-01 | MAJOR | The dynamic-retention section defined the effective retention horizon as `(n+n_ext)\Delta-\tau_R`, while the manuscript's backup schedule and residual-loss model define the clean-backup horizon as generation count times interval. This made the additional-retention theorem and numerical table use a different recovery rule from the main model. | Rebase dynamic retention on the same effective horizon `T(n_ext)=(n+n_ext)\Delta`, update the continuous optimum, feasibility set, proof, reproducible script, and numerical table values. |
| P10-R1-MAJ-02 | MAJOR | The numerical-example opening described `\Dstar` as the amount of old clean backup to keep, but `\Dstar` is an interval; the actual clean-recovery horizon is `n\Dstar`. This blurred the central practical recommendation. | Rewrite the numerical-example framing to distinguish backup interval `\Dstar` from clean-recovery horizon `n\Dstar`, and state the baseline horizon `n\Dstar=93.33` days. |

### Minor Findings

| ID | Severity | Finding | Repair |
|----|----------|---------|--------|
| P10-R1-MIN-01 | MINOR | The finite-frequency curvature symbol `Q''_\infty` suggested an old limit object rather than curvature at `\Dstar`. | Rename it to `Q''_\star`. |
| P10-R1-MIN-02 | MINOR | The practical input lists in the abstract and introduction omitted scan load even though the design formula depends on `\kappa_s`. | Add scan load to the operational-quantity lists. |

### Status

DONE. The dynamic-retention model now uses the same clean-backup horizon
definition as the main loss model; the Python check and numerical table were
regenerated; and the practical wording now keeps interval, retained horizon,
and scan load distinct.

## Post-Round-10 Cycle, Round 2

### MAJOR Findings

None.

### Verification

- `python3 analysis/paper_review_checks/run.py`: PASS.
- `latexmk -xelatex heavy_tail_backup_recast_xelatex.tex` from
  `paper/sections`: PASS.
- Final LaTeX log scan for `Warning`, `Overfull`, `Underfull`, `undefined`,
  `Undefined`, `Error`, and `Missing`: only existing xeCJK font redefinition
  warnings remain.
- Stale-scan found no active matches for the old dynamic-retention
  `-\tau_R` horizon, old numerical table values, or `Q''_\infty`.

## Final Stop Decision

Stopped after Post-Round-10 Cycle Round 2 because MAJOR-or-higher findings are
zero, well below the reopened 10-round cap.
