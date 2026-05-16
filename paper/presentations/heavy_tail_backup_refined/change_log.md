# Change Log

status: THEATRICAL_CLARITY_VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:00:58Z
updated_at_utc: 2026-05-16T22:40:06Z

## 2026-05-17 Planning Pass

- Created the refined deck project at `paper/presentations/heavy_tail_backup_refined/`.
- Registered the task in `docs/02_ACTIVE_LEDGER.md` with branch lock
  `RESEARCH-PRESENTATION-REFINE-001`.
- Set a 6-slide arc that adds a model/loss-decomposition bridge before the
  formula slide.
- Bound the evidence scope to local manuscript sections and internal compiled
  wiki memory; no external empirical or benchmark claims are introduced.

## 2026-05-17 Build / Review Round 1

- Generated a 6-slide editable PPTX with artifact-tool.
- Fixed layout QA issues from the first render: title/subtitle overlap boxes,
  boundary label overflow, and slide 3 panel padding.
- Tightened presentation-facing notation by removing inline-code backticks from
  slide subtitles.
- Reworded slide 6 from "同じ表で更新する" to "一緒に更新する" and replaced the
  tiny dynamic-retention equation with a readable operational sentence.

## 2026-05-17 Theatrical Pass

- Added `heavy_tail_backup_refined_theatrical.pptx` as a more theatrical variant.
- Shifted the visual system from warm-paper research style to a dark incident-room
  style with large claim typography, red/green hazard semantics, and English
  accent words such as `LATEST ≠ SAFE`, `ALERT`, and `a* FIRST`.
- Preserved the same six-slide source-grounded narrative and did not add
  empirical ransomware statistics, benchmark claims, SOTA claims, or new numeric
  recommendations.
- Fixed first-pass accent-word layout overlaps and reran QA to 0 errors / 0 warnings.

## 2026-05-17 Clarity Pass

- Removed unclear incident-response jargon from the theatrical deck and replaced
  it with audience-facing Japanese wording such as `判断手順`.
- Added explicit Japanese axis labels to the timeline, clean-horizon, and dwell
  distribution visuals so viewers know what direction and quantity each graphic
  encodes.
- Rebuilt the formula slide around three visible attention points: the numerator,
  the denominator, and the final division by the number of generations.
- Reran artifact-tool build, layout QA, package integrity, and slide-count checks
  after the edits.
