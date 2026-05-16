# Review Round 4: Clarity Pass

status: ACCEPTED_AFTER_FIX
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:40:06Z
review_target: `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`
max_severity_before_fix: MAJOR
max_severity_after_fix: NONE

## Trigger

User found three audience-facing clarity issues in the theatrical deck: specialist
terms were unclear, graph axes were not self-explanatory, and the formula slide
did not say where to look first.

## Changes

- Replaced unclear specialist wording with plain Japanese audience language,
  especially `判断手順` for the final operating slide.
- Added axis labels and direction cues to the timeline, clean-recovery horizon,
  and dwell-time distribution graphics.
- Rebuilt the formula slide so the eye lands on three chunks: numerator,
  denominator, and division by generation count.
- Kept the theatrical dark-room style, red/green semantics, source footers, and
  six-slide evidence boundary intact.

## Findings And Responses

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R4-M01 | MAJOR | 6 | The final slide used specialist terminology that did not help a first-time listener. | Reworded the slide around `判断手順` and plain cost/loss language. |
| R4-M02 | MAJOR | 1-3 | The proof graphics did not label their axes clearly enough for room reading. | Added Japanese axis labels and direction cues to the timeline, horizon, and distribution views. |
| R4-M03 | MAJOR | 5 | The formula was visually striking, but did not identify the part the audience should inspect. | Split the formula into numerator, denominator, and generation-count focus points, then added the takeaway line about `a*`. |

## Verification After Fix

- Artifact-tool build: PASS, 6 slides.
- Layout QA: PASS with 0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_refined_theatrical.pptx`: PASS.
- Package slide count: PASS, six `ppt/slides/slide*.xml` entries.
- Contact sheet: visually inspected after fixes.

## Decision

STOP. The theatrical deck now keeps the stronger stage presence while making the
specialist wording, chart reading direction, and formula focus explicit.
