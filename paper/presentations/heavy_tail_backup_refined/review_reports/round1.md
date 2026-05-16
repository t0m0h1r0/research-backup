# Review Round 1

status: CHANGES_REQUIRED_ADDRESSED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:14:20Z
review_target: `paper/presentations/heavy_tail_backup_refined/heavy_tail_backup_refined.pptx`
max_severity_before_fix: MAJOR
max_severity_after_fix: NONE

## Findings And Responses

| ID | Severity | Slide | Finding | Response |
|----|----------|-------|---------|----------|
| R1-M01 | MAJOR | Global | Audience-facing subtitles used inline-code backticks around formulas, making the deck feel like source notes rather than a finished talk. | Removed backticks from slide subtitles and kept formula notation as presentation text. |
| R1-M02 | MAJOR | 6 | The slide title promised a table, while the visual was an operating loop; the tiny dynamic-retention formula was not readable enough to justify occupying the bottom rail. | Reworded the claim to "一緒に更新する" and replaced the tiny formula with a readable operational sentence. |
| R1-M03 | MAJOR | Global | Initial layout QA found title/subtitle box overlap and a slide 3 bottom-padding defect. | Adjusted title/subtitle bounding boxes, shifted labels, increased panel padding, and reran layout QA to 0 errors / 0 warnings. |

## Verification After Fix

- Artifact-tool build: PASS, 6 slides.
- Layout QA: PASS with 0 errors and 0 warnings.
- Contact sheet: visually inspected after fixes.
