# Review Rounds

status: ZERO_BASE_SELF_QA
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

## Review Loop Status

Pending independent review Round 1.
