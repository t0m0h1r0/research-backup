# Review Rounds

status: ROUND2_ADDRESSED
review_target: `paper/presentations/heavy_tail_backup_intro/heavy_tail_backup_intro.pptx`
created_at_utc: 2026-05-06T04:35:17Z

## Zero-Base Rebuild

Reviewer: ResearchArchitect
Trigger: User requested the slide content be recreated from zero, then reviewed
with as many findings as possible per round and all findings addressed until
MAJOR-or-higher findings disappear or the loop exceeds 10 rounds.
Verdict: PASS_SELF_QA
Max severity after self-QA: NONE

Changes:
- Recreated the deck narrative from source material instead of editing the prior
  slide story.
- Started from the incident-day recovery question: newest backup may be unsafe.
- Reframed detection as whether the alert arrives before the clean-backup
  horizon expires.
- Added heavy-tail motivation without promoting empirical tail claims.
- Recast the formula around the clean-recovery horizon `a* = nΔ*`.
- Ended with an operations workflow: estimate loss, measure recovery, decide
  horizon, and extend retention when risk changes.

Self-QA checks:
- Slide count is 5.
- Every slide has one lead, one proof visual, and a source footer.
- Post-intrusion backups are marked as contaminated in the timeline.
- `Δ*` as interval and `a* = nΔ*` as clean-recovery horizon are separated.
- No empirical recommendation, SOTA claim, benchmark claim, or unverified
  ransomware statistic was added.
- Numerical example remains labeled as a scale check, not a recommendation.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_intro.pptx`: PASS.

## Round 1: Independent Review

Reviewers: Parfit, Nash, Gauss
Verdict: CHANGES_REQUIRED
Max severity: MAJOR
CRITICAL findings: NONE

Major findings and response:

| ID | Slide | Finding | Response |
|----|-------|---------|----------|
| R1-M01 | 1 | Timeline competed with the black research-entry box, weakening thumbnail comprehension. | Removed the black box and made the timeline the full-width primary visual with a smaller bottom takeaway. |
| R1-M02 | 1 | The decision boundary between safe and contaminated backups was not strong enough. | Added a red post-intrusion contamination zone, heavier detection marker, selected clean candidate, and latest-backup danger marker. |
| R1-M03 | 1 | The story implied intrusion time is known exactly. | Changed language to estimated intrusion/pre-intrusion clean candidate and added a restore-before-cleanliness-check note. |
| R1-M04 | 2 | `a_n(Δ)=nΔ` appeared before `n` and `Δ` were explained. | Added a legend for `n`, `Δ`, `a_n`, and the evaluation domain `nΔ>t_m`. |
| R1-M05 | 2 | “復旧可能” and “全損扱い” sounded too absolute. | Reworded to infection age within `nΔ` is treated as recoverable, and beyond horizon is modeled as clean-recovery failure/full-loss equivalent. |
| R1-M06 | 2 | Formula and bullet card had equal weight; the evaluation shift was not dominant. | Rebuilt the slide around the dominant visual phrase “検知性能 → 清浄復旧できたか” and a thicker horizon bar. |
| R1-M07 | 3 | The average-versus-tail story did not explain why average-based reasoning fails. | Recast the panel labels as short-latency-only versus tail-aware retention and added a same-average/long-tail takeaway. |
| R1-M08 | 3 | The visual did not directly show tail samples crossing the retention boundary. | Added a red tail region crossing the same retention boundary, with the failure mechanism called out. |
| R1-M09 | 3 | The heavy-tail headline sounded empirical rather than model-bound. | Changed the headline to “Pareto型の潜伏モデルでは...” and kept the footer evidence caveat. |
| R1-M10 | 4 | Formula was too compressed and math-first for beginners. | Rebuilt the slide as “損失・復旧時間・スキャン負荷から a* を出す,” with both `Δ*` and `a*` shown. |
| R1-M11 | 4 | Interior design conditions were only in the footer. | Added the condition line `L > d₁τ_R+d₀`, `κ_s>0`, `Δ*∈D` and a plain-language guardrail for invalid/out-of-range cases. |
| R1-M12 | 4 | Formula terms and interpretation were visually disconnected. | Added direct labels for interval, horizon, variables, loss difference, recovery loss, and scan-load cost. |
| R1-M13 | 5 | Workflow was generic and visually dense. | Rebuilt steps as loss, recovery, detection delay, and retention design, with the final retention step visually privileged. |
| R1-M14 | 5 | Operational flow omitted detection delay / dwell-time evidence. | Added a dedicated “遅れを見る” step for detection delay and dwell distribution versus `a*`. |
| R1-M15 | 5 | `n_ext` was undefined and dynamic retention was underspecified. | Avoided the symbol in the main flow and added additional-retention cost plus recovery-failure penalty as the integer-evaluation inputs. |

Minor findings and response:

- Global: enlarged chapter labels and slide numbers, shortened/strengthened
  source footers, and varied slide rhythm with more dominant single visuals.
- Slide 1: changed the lead to “なりうる,” added silent-contamination language,
  reduced repetitive status tagging, and strengthened the detection marker.
- Slide 2: made the subtitle operational, removed the subtle card-to-card arrow,
  and tied colors to the horizon legend.
- Slide 3: added compact axis meaning, clarified the retention boundary as a
  policy boundary, and replaced “average-based” wording with source-safer
  short-latency/typical-case language.
- Slide 4: introduced “清浄復旧ホライズン” through plain language, showed both
  `Δ*` and `a*`, and changed “L is large” to a loss-difference reading.
- Slide 5: simplified the subtitle, removed the tiny legend, and rewrote the
  numerical caveat as an operational punchline: values must be recomputed for
  the organization and are not empirical estimates.

Verification after response:
- `build_artifact_deck.mjs --slide-count 5`: PASS.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_intro.pptx`: PASS.
- Contact sheet visually inspected.

## Review Loop Status

Round 1 findings addressed.

## Round 2: Independent Review

Reviewers: Tesla, Leibniz, Ptolemy
Verdict: CHANGES_REQUIRED
Max severity: CRITICAL

Findings and response:

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R2-C01 | CRITICAL | 3 | “平均が同じに見えても” implied a same-mean distribution comparison not supported by the source and risky because Pareto means may be undefined. | Replaced with source-safer wording: “典型例が短く見えても、少数の長期潜伏が保持窓を超える.” |
| R2-m01 | MINOR | 2 | `a_n` and `t_m` rendered with visible underscores. | Changed to typographic subscripts `aₙ` and `tₘ` in display and legend. |
| R2-m02 | MINOR | 4 | Formula slide remained dense. | Trimmed variable bullets and kept the slide as the technical anchor while preserving the condition and guardrail. |
| R2-m03 | MINOR | 5 | Step-card body copy could be more direct for non-technical audiences. | Tightened Step 3 to the operational object: infection age at detection versus `a*`. |
| R2-m04 | MINOR | 4 | “安全に戻れる” sounded broader than the model supports. | Changed lead to “清浄に戻れる.” |
| R2-m05 | MINOR | 5 | “潜伏分布が a* を超える” was abstract. | Reworded to “検知時点の感染後経過時間が a* を超えないかを見る.” |

Verification after response:
- `build_artifact_deck.mjs --slide-count 5`: PASS.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_intro.pptx`: PASS.

## Review Loop Status

Round 2 findings addressed. Round 3 pending.
