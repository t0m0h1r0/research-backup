# Heavy-Tail Backup Refined Deck Profile Plan

status: PLANNED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:00:58Z
task_mode: create-from-existing-source
primary_deck_profile: engineering-platform
secondary_profile_gates: strategy-leadership, appendix-light research traceability

## Objective

既存の5枚デッキを土台に，研究発表として「直感 -> モデル分解 -> 設計式
-> 運用判断」の橋渡しを強めた改訂版を作る。既存デッキの初学者向けの
入口は保ちつつ，数式へ飛ぶ前に検知失敗・保持超過・復旧不能の分解を
1枚追加し，聴衆が式の意味を追える状態にする。

## Required Proof Objects

- Incident-day backup timeline showing clean candidate versus contaminated recent backups.
- Clean-recovery horizon visual for `a_n(Delta)=nDelta`.
- Heavy-tail retention-boundary visual bounded to the Pareto dwell-time model assumption.
- Branch/loss decomposition connecting `H_beta`, `M_beta`, and recovery failure.
- Formula anchor for `Delta*` and `a*` with explicit interior-condition caveat.
- Operational workflow connecting loss estimates, recovery time, detection delay, and dynamic retention.

## Source And Asset Requirements

- Primary source: `paper/sections/tex/*.tex`.
- Prior deck reference: `paper/presentations/heavy_tail_backup_intro/heavy_tail_backup_intro.pptx`.
- Internal memory: `docs/wiki/ransomware_heavy_tail_backup_design.md`, as model-derived knowledge only.
- No external empirical claims, SOTA claims, ransomware frequency claims, or benchmark claims.
- No logos, product UI, or identity assets are needed.

## QA Gates

- One supported claim per slide.
- Every formula or variable shown must have a nearby plain-language reading.
- Slide 3 must not imply same-mean comparison or empirical tail evidence.
- Slide 5 must state the interior/admissible-domain condition before presenting the design formula as actionable.
- Final deck must render to PNG, export to PPTX, pass package checks, and pass layout QA or document false-positive warnings.
