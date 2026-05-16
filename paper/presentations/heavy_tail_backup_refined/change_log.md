# Change Log

status: THEATRICAL_FORMULA_READING_VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:00:58Z
updated_at_utc: 2026-05-16T22:55:04Z

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

## 2026-05-17 Formula Reading Pass

- Expanded the theatrical deck from 6 to 7 slides so the formula explanation no
  longer competes with the design-target takeaway.
- Added a dedicated formula-reading slide that reads `a*` first, then explains
  the numerator as "full-loss avoidance value", the denominator as "load of
  restoring further back", and `n` as the conversion from clean-history length
  to backup interval.
- Split the former formula slide into a reading slide and a design-target slide:
  `a*` is now the first design question, while `Delta* = a*/n` is the interval
  consequence.
- Reran artifact-tool build, layout QA, rendered preview inspection, package
  integrity, and slide-count checks after the edits.
