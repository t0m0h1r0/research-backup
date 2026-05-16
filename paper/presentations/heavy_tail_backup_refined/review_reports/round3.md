# Review Round 3: Theatrical Pass

status: ACCEPTED_AFTER_FIX
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:24:51Z
review_target: `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined_theatrical.pptx`
max_severity_before_fix: MAJOR
max_severity_after_fix: NONE

## Trigger

User asked whether the deck could have more 外連味. The calm refined deck was
already validated, so this round created a theatrical variant rather than
discarding the clean version.

## Changes

- Switched to a dark incident-room visual system with red top rail and green
  recovery rail.
- Increased title scale and used high-contrast English accent words:
  `LATEST ≠ SAFE`, `ALERT`, `CLEAN HISTORY EXPIRES`, and `a* FIRST`.
- Kept the six-slide source-grounded narrative: restore risk, clean-recovery
  horizon, heavy-tail boundary, loss decomposition, design target, operating loop.
- Preserved evidence boundaries: no empirical tail claim, no benchmark claim,
  no SOTA claim, and no new numerical recommendation.

## Findings And Responses

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R3-M01 | MAJOR | Global | Initial theatrical render had accent words overlapping title or subtitle boxes in layout QA. | Moved and resized the accent words on slides 1, 5, and 6, then rerendered. |
| R3-M02 | MAJOR | Global | Darker styling risked spectacle outrunning source fidelity. | Rechecked each slide against the existing source map and retained provenance footers and formula conditions. |

## Verification After Fix

- Artifact-tool build: PASS, 6 slides.
- Layout QA: PASS with 0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_refined_theatrical.pptx`: PASS.
- Package slide count: PASS, six `ppt/slides/slide*.xml` entries.
- Contact sheet: visually inspected after fixes.

## Decision

STOP. The theatrical deck is visually stronger while preserving source and model
boundaries. No unresolved CRITICAL, MAJOR, HIGH, or MINOR findings remain.
