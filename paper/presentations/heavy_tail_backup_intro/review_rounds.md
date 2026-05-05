# Review Rounds

status: COMPLETE
review_target: `paper/presentations/heavy_tail_backup_intro/heavy_tail_backup_intro.pptx`
stop_rule: stop when no MAJOR-or-higher findings remain, or after more than 10 rounds

## Round 0: Builder Self-QA

Reviewer: ResearchArchitect
Verdict: PASS_FOR_REVIEW
Max severity: MINOR

Checks:
- Slide count is 5.
- Each slide has one lead message, one primary visual, and source references.
- No empirical recommendation or SOTA/benchmark claim was added.
- Layout checker passed with 0 errors and 0 warnings.
- Contact sheet was visually inspected for readability and flow.

Findings:
- None blocking before external review.

## Round 1: Independent Review

Reviewer: Raman
Verdict: CHANGES_REQUIRED
Max severity: MAJOR

Findings and response:

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R1-F1 | MAJOR | 2 | `η` branch from `S_S` did not visually connect to `S_I`, despite the model defining symptom-detection success as `S_S -> S_I`. | Addressed by redrawing the green `η` connector as an explicit routed branch into `S_I`. |
| R1-F2 | MAJOR | 3 | Tail-probability sketch placed teal points below the x-axis, implying negative probability. | Addressed by rescaling the sketch so all tail-probability points remain at or above the axis. |
| R1-F3 | MAJOR | 5 | Bottom caution band overlapped the step 3 card, and the title orphaned `保持` on a separate line. | Addressed by shortening the title and moving the caution band below the card area. |
| R1-F4 | MINOR | 5 | Parameter box omitted key units and baseline conditions from the numerical example. | Addressed by adding units for `d1`, `L`, `c_b`, `lambda`, `eta`, and `d0` from the numerical section and manifest. |

## Round 2: Independent Review

Reviewer: Raman
Verdict: NO_MAJOR_OR_HIGHER
Max severity: MINOR

Findings and response:

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R2-F1 | MINOR | 3 | The final teal tail-probability marker sat on or slightly straddled the x-axis at thumbnail size. | Addressed by rescaling the chart markers so the final points are visibly above the probability baseline. |

## Round 3: Independent Review

Reviewer: Raman
Verdict: PASS
Max severity: NONE

Findings:
- No CRITICAL, MAJOR, or MINOR issues remain.
