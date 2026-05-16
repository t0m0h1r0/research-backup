# Comeback Scorecard

status: PASS
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:14:20Z
deck: `heavy_tail_backup_refined.pptx`
primary_deck_profile: engineering-platform
reference_delta: n/a

## Rubric

| Dimension | Score | Note |
|-----------|-------|------|
| story | 5 | Clear arc from restore risk to clean-recovery horizon and operating loop. |
| specificity | 5 | Claims depend on ransomware backup contamination, Pareto dwell modeling, and the manuscript formula. |
| rhythm | 4 | Six slides use timeline, horizon bar, paired tail visual, branch diagram, formula anchor, and operating loop. |
| whitespace | 4 | Spacious enough for presentation use; formula slide is the densest by design. |
| chart clarity | 4 | Authored editable proof visuals directly support the claims; no native chart parts required. |
| typography | 4 | Large claims and consistent labels; footers intentionally remain provenance-only. |
| restraint | 5 | No decorative icons, logos, filler boxes, or unsupported metrics. |
| precision | 5 | Formula conditions and source boundaries are explicitly stated. |
| coherence | 5 | Warm paper system, teal/amber/red semantics, and consistent footers/kickers across slides. |

Total: 41 / 45. Required minimum without reference: 40 / 45. No dimension below 4.

## Mechanical QA

- PPTX exists and is non-empty: PASS.
- Expected slide count: PASS, 6 slides.
- Artifact-tool render to PNG: PASS.
- Contact sheet inspection: PASS.
- Layout quality: PASS, 0 errors and 0 warnings.
- Package integrity: PASS, `unzip -t` found no compressed-data errors.
- Empty media files: PASS by package inspection; no embedded media assets are used.

## Residual Risk

The deck is a source-grounded research presentation, not empirical validation.
It should not be used to claim ransomware dwell-time distribution facts,
benchmark performance, SOTA, or deployment readiness.
