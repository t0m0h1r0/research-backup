# Review Round 5: Formula Reading Pass

status: ACCEPTED_AFTER_FIX
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:55:04Z
review_target: `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`
max_severity_before_fix: MAJOR
max_severity_after_fix: NONE

## Trigger

User reported that the formula still had no explanation of how to read it.
Round 4 made the parts visible, but did not yet teach the audience how those
parts become a design judgment.

## Changes

- Expanded the theatrical deck from 6 to 7 slides.
- Added a dedicated formula-reading slide before the design-target slide.
- Reframed the formula around `a*` first: the clean-history length to preserve.
- Explained the numerator as avoided full-loss value, the denominator as the
  load of restoring further back, and `n` as the conversion from clean-history
  length to backup interval.
- Kept the source boundary and interior-condition caveat from
  `05_backup_optimization.tex`.

## Findings And Responses

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R5-M01 | MAJOR | 5 | The formula was decomposed visually, but the audience still did not know how to interpret the expression. | Added a formula-reading slide with explicit reading order and plain-language meaning for each expression block. |
| R5-M02 | MINOR | 1 | First rendered rebuild had a right-side note crossing the timeline. | Shortened the timeline and boxed the note so it no longer overlays the proof object. |

## Verification After Fix

- Artifact-tool build: PASS, 7 slides.
- Layout QA: PASS with 0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_refined_theatrical.pptx`: PASS.
- Package slide count: PASS, seven `ppt/slides/slide*.xml` entries.
- Contact sheet and formula-critical slides were visually inspected.

## Decision

STOP. The theatrical deck now explains the formula as a reading sequence and a
design judgment, not just as notation.
