# ResearchArchitect Paper Review Audit

## Source Evidence

- Recast manuscript: `paper/sections/tex/*.tex`
- Extracted source: `paper/source/heavy_tail_backup_v13.txt`
- Protected source artifact: `paper/source/heavy_tail_backup_v13.pdf` was not modified.

## Reviewer Findings

### F1. Missed-detection losses use an unconditioned dwell distribution

`Q_{\mathrm{full}}` multiplies a no-early-detection probability by restoration and failure terms that are functions of the unconditioned Pareto law.  Since
`T_{\mathrm{det}}\ge T_d` exponentially tilts the dwell distribution by
`e^{-\beta T_d}`, this is not a harmless notation issue: it affects the stated
loss model, finite-frequency corrections, and the compactness proof.

Required repair: define the residual loss from primitive branch probabilities
`E[e^{-\beta T_d}1_{...}]` and truncated moments
`E[T_d e^{-\beta T_d}1_{...}]`, then redo the derivative proof from those
objects.

### F2. The admissible interval domain is missing

The expression `(t_m/(n\Delta))^\alpha` is a Pareto tail probability only when
`n\Delta\ge t_m`.  The manuscript optimizes over `\Delta>0`, so the proof uses
probabilities outside their domain and incorrectly claims lower-bound
coercivity as `\Delta\to0+`.

Required repair: introduce the design domain `\Delta>t_m/n` and an operational
upper bound `\bar\Delta` (or equivalent service-level constraint) for the
frequency-asymptotic theorem.

### F3. The scan-time symbol is inconsistent

The model says `T_{\mathrm{scan}}=\kappa_sT_{\mathrm{det}}`, while the loss
formula uses a dwell-time moment.  The numerical section then gives `\kappa_s`
units as days/generation, which is incompatible with the closed-form
`\Delta_\infty^\ast`.

Required repair: define `\kappa_s` as a dimensionless scan-time multiplier for
the relevant infection age, and use `T_d` in the missed-detection branch.

### F4. The high-frequency minimizer theorem overclaims existence

After the correct exponential tilt is used, the residual loss can have a finite
limit as `\Delta\to\infty`; fixed backup cost alone does not force a finite
global minimizer for every attack rate.  The claimed convergence remains valid
on a compact admissible policy band containing the interior minimizer.

Required repair: state the theorem on a service-level band and prove uniform
convergence of `G(\Delta;\lambda)/\lambda` to the residual loss.

### F5. Dynamic retention integer rounding is wrong

For a convex function on integers, the minimizer is among the neighboring
integers around the continuous optimum, not always the ceiling.  Several table
entries can change.

Required repair: state the candidate-set rule and recompute the numerical table.

### F6. Narrative and notation drift obscure the contribution

The introduction claims a "complete model" but the actual theorem is about the
`\Delta`-dependent residual loss; `\alpha` and `\alpha(I)`, `\beta` and
`\beta(I)`, `F` and `ET`, and cost symbols are introduced unevenly.  References
are listed but not cited in the narrative.

Required repair: add a notation/cost glossary, cite representative prior-work
groups in the introduction and model sections, and align the abstract,
introduction, theorem names, and conclusion around the corrected residual-loss
claim.

## Planned Fix Status

| Finding | Status | Target |
|---------|--------|--------|
| F1 | TODO | `02_model_formulation.tex`, `05_backup_optimization.tex` |
| F2 | TODO | `02_model_formulation.tex`, `05_backup_optimization.tex` |
| F3 | TODO | `02_model_formulation.tex`, `07_numerical_examples.tex` |
| F4 | TODO | `05_backup_optimization.tex` |
| F5 | TODO | `06_dynamic_retention.tex`, `07_numerical_examples.tex` |
| F6 | TODO | abstract, introduction, conclusion, references |
