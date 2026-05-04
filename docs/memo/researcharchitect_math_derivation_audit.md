# ResearchArchitect Math Derivation Audit

## Scope

- Audited files: `paper/sections/tex/02_model_formulation.tex`,
  `03_renewal_reward.tex`, `04_tauber_transition.tex`,
  `05_backup_optimization.tex`, `06_dynamic_retention.tex`,
  `07_numerical_examples.tex`, `00_abstract.tex`, and `08_conclusion.tex`.
- Reproducible check: `analysis/paper_review_checks/run.py`.
- Protected source: `paper/source/heavy_tail_backup_v13.pdf` was not modified.

## Independent Derivation Summary

For a fixed dwell time $T_d=t$, early detection fails with probability
$e^{-\beta t}$. Therefore the recoverable late-detection branch is governed by
$\E[e^{-\beta T_d}\mathbf{1}_{T_d\le n\Delta}]$, the unrecoverable late branch by
$\E[e^{-\beta T_d}\mathbf{1}_{T_d>n\Delta}]$, and the scan-time loss by
$\E[T_de^{-\beta T_d}\mathbf{1}_{T_d\le n\Delta}]$. Differentiating these
primitive tilted integrals gives
\[
  H_\beta'(\Delta)=-ne^{-\beta n\Delta}f_{T_d}(n\Delta),\qquad
  M_\beta'(\Delta)=n^2\Delta e^{-\beta n\Delta}f_{T_d}(n\Delta),
\]
so the residual-loss derivative is
\[
  \frac{\partial Q_{\mathrm{full}}}{\partial\Delta}
  =\eta ne^{-\beta n\Delta}f_{T_d}(n\Delta)
    \{d_1\kappa_s n\Delta-[L-(d_1\tau_R+d_0)]\}.
\]
The algebra is correct, but the manuscript must explicitly restrict the theorem
to the parameter region where the displayed interior minimizer is defined.

## Findings

### MAJ-01. Interior optimum theorem is missing the positive scan-cost condition

The model permits $\kappa_s\ge0$, but the theorem defines
$\Delta_\infty^\ast=\Lambda/(d_1\kappa_s n)$. If $\kappa_s=0$, the expression is
undefined and the derivative is strictly negative when $\Lambda>0$, so the
interior-minimizer theorem is false. Root repair: keep the general model
$\kappa_s\ge0$, but make Theorem 5's design condition require $\kappa_s>0$ and
state the abstract/conclusion claim under that condition.

### MAJ-02. The phase-transition theorem relies on an unproved tilted-moment lemma

The stated asymptotic for $\E[T_de^{-\beta T_d}]$ is correct, but the manuscript
uses it to prove the $\alpha=1$ transition without showing the derivation. Root
repair: add a proof from the integral representation and incomplete-gamma
asymptotics, including the logarithmic boundary case.

### MAJ-03. Dynamic-retention convexity needs explicit positivity assumptions

The proposition divides by $c_n$ and uses strict convexity from
$L_{\mathrm{fail}}\alpha(\alpha+1)t_m^\alpha\Delta^2T^{-(\alpha+2)}>0$, but the
statement does not explicitly require $c_n>0$, $L_{\mathrm{fail}}>0$,
$\Delta>0$, and nonempty feasibility. Root repair: move those conditions into
the definition/proposition so the integer optimum rule is mathematically scoped.

## Fix Plan

1. Patch the manuscript at the owning mathematical statements, not only in the
   surrounding prose.
2. Add validation guards in `analysis/paper_review_checks/run.py` for the same
   parameter domain.
3. Re-run the table generator and LaTeX/text checks.
