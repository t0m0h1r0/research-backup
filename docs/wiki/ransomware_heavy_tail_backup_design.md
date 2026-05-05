# Ransomware Heavy-Tail Backup Design Knowledge

status: COMPILED
compiled_by: ResearchArchitect
source_scope: local manuscript and recast manuscript sections
primary_sources:
- `paper/source/heavy_tail_backup_v13.txt`
- `paper/sections/tex/01_introduction.tex`
- `paper/sections/tex/02_model_formulation.tex`
- `paper/sections/tex/03_renewal_reward.tex`
- `paper/sections/tex/04_tauber_transition.tex`
- `paper/sections/tex/05_backup_optimization.tex`
- `paper/sections/tex/06_dynamic_retention.tex`
- `paper/sections/tex/07_numerical_examples.tex`
- `paper/sections/tex/08_conclusion.tex`

## Boundary

This page records knowledge worth carrying forward from the ransomware
heavy-tail backup manuscript. It is model-derived internal knowledge. It should
not be cited as external empirical evidence, benchmark evidence, or SOTA
evidence without a separate evidence package.

The active AI anomaly-detection project has not yet selected a target domain or
dataset. The items below are therefore reusable design ideas and research
questions, not a locked project direction.

## Core Knowledge

### WIKI-HTB-001: Detection and backup are coupled controls

Ransomware defense should not treat faster detection and backup recovery as
separate problems. If backups taken after intrusion are contaminated, the key
recovery question is not only how recent the latest backup is, but how far back
the system can roll to a clean recovery point.

Research use: anomaly-detection work should evaluate the action attached to an
alert. A detector that improves time-to-detection but still allows clean backups
to age out may fail the operational objective.

Conditions: applies when post-intrusion backups may be contaminated and recovery
requires a clean historical state.

### WIKI-HTB-002: Heavy-tailed dwell time breaks average-case intuition

Pareto dwell time has survival probability
`P(T_d > t) = (t_m / t)^alpha` for `t >= t_m`. When `alpha <= 1`, the mean dwell
time is infinite. Average-dwell-time reasoning can therefore understate rare
long latent infections that exceed backup retention.

Research use: anomaly-detection benchmarks for cyber operations should preserve
time-to-detection and censoring information where possible. Point labels alone
are not enough to study long-latency risk.

Conditions: the Pareto model is a modeling assumption. Empirical tail claims
require verified incident data or literature evidence.

### WIKI-HTB-003: Semi-Markov framing is useful for non-exponential dwell times

A semi-Markov process keeps Markovian state transitions while allowing arbitrary
state residence-time distributions. This is a natural fit when latent infection
dwell time is heavy-tailed rather than exponential.

Research use: if the anomaly project studies attack progression or delayed
detection, model state duration explicitly instead of forcing an exponential
continuous-time Markov chain.

Conditions: the current manuscript uses a one-incident path/accounting view in
the recast sections, not a full system-regeneration claim for overlapping
incidents.

### WIKI-HTB-004: Positive detection rate truncates latent-state residence time

For `T_det ~ Exp(beta)` independent of Pareto dwell time `T_d`,
`E[min(T_det, T_d)]` is finite for every `alpha > 0` when `beta > 0`. The upper
incomplete gamma term is finite because the integration lower bound is positive.

Research use: even when dwell time itself has infinite mean, a positive
detection process can make the latent-state residence time finite. This supports
calendar-time risk accounting under explicit detection assumptions.

Conditions: requires `beta > 0`, independence between detection time and dwell
time, and finite early-detection cost.

### WIKI-HTB-005: Separate early-detection cost from residual late-detection loss

The recast manuscript separates early-detection costs that do not depend on the
backup interval from the residual loss after early detection fails. The residual
loss uses tilted branch quantities:

- `L_beta = E[e^{-beta T_d}]`
- `H_beta(Delta) = E[e^{-beta T_d} 1{T_d > n Delta}]`
- `M_beta(Delta) = E[T_d e^{-beta T_d} 1{T_d <= n Delta}]`

Research use: cost-aware anomaly detection should distinguish costs that are
independent of the threshold or backup policy from residual costs that are
changed by the decision variable.

Conditions: the older extracted source text used unconditioned Pareto quantities
in places. Prefer the corrected recast manuscript sections for mathematical
claims.

### WIKI-HTB-006: Clean-backup horizon is `n Delta`

With `n` retained generations and backup interval `Delta`, the effective clean
recovery horizon is `a_n(Delta) = n Delta`. Pareto tail probabilities for
backup loss should be evaluated on the domain `Delta > t_m / n`.

Research use: detection evaluation should include whether the alert occurs
before the clean-backup horizon expires. This turns time-to-detection into an
actionability metric.

Conditions: assumes every backup after intrusion is contaminated and that
retained generations are evenly spaced.

### WIKI-HTB-007: Backup provides a finite boundary for heavy-tail risk

Without a retention boundary, the residual loss has an `alpha = 1` transition
under positive scan-load cost `kappa_s > 0`: low-detection-rate residual scan
loss diverges for `alpha <= 1` and remains finite for `alpha > 1`.

Research use: in heavy-tailed latent-risk domains, finite retention horizons and
recovery actions can be part of the detection design, not merely downstream
operations.

Conditions: this is a model result for the backup-free or boundaryless limit and
depends on the residual-loss definition and `kappa_s > 0`.

### WIKI-HTB-008: Closed-form interior design target

Under the recast model's interior design conditions,

`Delta*_infty = [L - (d1 tau_R + d0)] / (d1 kappa_s n)`.

This is the unique minimizer of the backup-interval-dependent residual loss on
the admissible interval when it lies inside that interval.

Research use: the formula gives a first-pass operational design target from
loss quantities: total-loss damage `L`, daily downtime loss `d1`, mean recovery
time `tau_R`, fixed recovery cost `d0`, scan-load multiplier `kappa_s`, and
retained generations `n`.

Conditions: requires `L > d1 tau_R + d0`, `kappa_s > 0`, and an admissible
service-level interval containing the interior point. If the point is outside
the interval, endpoints must be evaluated.

### WIKI-HTB-009: Read the formula as a clean-recovery horizon

The more stable operational quantity is

`a* = n Delta*_infty = [L - (d1 tau_R + d0)] / (d1 kappa_s)`.

The interval `Delta*_infty` changes with the number of retained generations, but
the target clean-recovery horizon `a*` does not.

Research use: this suggests separating two design layers: first choose the
needed clean-history horizon, then choose the number of generations and interval
that implement it.

Conditions: the interpretation inherits the same assumptions as WIKI-HTB-008.

### WIKI-HTB-010: High attack frequency makes fixed backup cost secondary

On a compact service-level interval, the minimizer of
`c_b / Delta + lambda Q_full(Delta)` converges to `Delta*_infty` as
`lambda -> infinity`. The fixed backup cost term becomes negligible relative to
incident loss.

Research use: for high-frequency threat environments, initial design can focus
on the residual-loss minimizer, while finite-frequency correction accounts for
backup fixed cost.

Conditions: convergence is stated on a compact admissible policy interval. The
finite-frequency correction still depends on tail density, detection rate,
symptom-detection probability, and attack frequency.

### WIKI-HTB-011: Dynamic retention is an integer convex trade-off

Temporary extra retention can be modeled as

`B(n_ext) = c_ext n_ext + L_fail (t_m / ((n + n_ext) Delta))^alpha`.

The continuous relaxation has a closed-form stationary point; the integer
optimum is found by evaluating the neighboring feasible integers around the
constrained continuous optimum.

Research use: retention extension can be handled as a small discrete decision
problem triggered by incident risk, threat campaigns, or recovery drills.

Conditions: use the floor/ceiling candidate-set rule around the constrained
continuous point. Do not use a ceiling-only rule.

### WIKI-HTB-012: Numerical values are sanity checks, not evidence

The recast numerical example uses `t_m = 1`, `d1 = 1666.7`, `L = 50000`,
`n = 5`, `tau_R = 2.0`, and `kappa_s = 0.3`, yielding
`Delta*_infty = 18.67` days and `n Delta*_infty = 93.33` days.

Research use: these values are useful for checking formula behavior and scale,
but should not be promoted as empirical recommendations without validating the
input parameters against the intended domain.

Conditions: the older extracted source text reports a different illustrative
number because later recast repairs changed the numerator and units. Use the
recast manuscript for current values.

## Carry-Forward Questions for AI Anomaly Detection

1. What is the observation unit: event, host, user, service, container, or
   incident path?
2. Can the dataset represent time-to-detection, dwell-time censoring, and the
   alert action, or only static labels?
3. Does the detector improve the probability of detection before a recovery
   horizon expires?
4. How should anomaly scores map to `beta`, time-to-detection, or threshold
   policy?
5. What recovery action follows each alert, and what cost changes with the
   threshold?
6. Which quantities are operational estimates and which require external
   literature or empirical measurement?
7. How should heavy-tail uncertainty be propagated into threshold and retention
   decisions?

## Do Not Promote Without More Evidence

- Do not claim that ransomware dwell time is Pareto in a target deployment
  without external evidence or fitted data.
- Do not claim empirical performance, SOTA, or benchmark superiority from this
  model-only manuscript.
- Do not use the numerical example as a recommendation for a specific industry
  without a parameter provenance note.
- Do not treat `Delta*_infty` as globally valid outside its admissible design
  interval or when `kappa_s = 0`.
- Do not compare directly with static security-investment rules unless the
  different optimization objectives are stated.
