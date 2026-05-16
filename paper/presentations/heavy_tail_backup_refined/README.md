# Heavy-Tail Backup Refined Deck

status: VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:14:20Z
deck_file: `heavy_tail_backup_refined.pptx`
slide_count: 6
worktree: `/private/tmp/research-backup-presentation-refine`
branch: `codex/researcharchitect-presentation-refine`

## Purpose

研究発表用に，既存の5枚デッキ
`paper/presentations/heavy_tail_backup_intro/heavy_tail_backup_intro.pptx`
を踏まえつつ，6枚構成の改訂版として再生成したプレゼン資料。

改訂の主眼は，直感的な復旧リスクから設計式へ飛ばず，検知失敗・保持超過・
復旧不能の分解を経由してから清浄復旧ホライズンの式へ進めること。

## Evidence Boundary

- 本デッキは，修正版の論文セクション `paper/sections/tex/*.tex` に基づく
  モデル由来の説明である。
- `docs/wiki/ransomware_heavy_tail_backup_design.md` は内部コンパイル済み
  知識として参照したが，外部実証根拠としては扱わない。
- 外部の SOTA，ベンチマーク，実運用での尾指数・検知率・攻撃頻度に
  関する新規主張は追加していない。
- 数値例はスケール確認としてのみ扱い，実務推奨値や実証結果として
  扱わない。

## Refined Narrative Spine

1. 最新バックアップだけを見ると，復旧先を間違える。
2. 良いアラートは，清浄復旧ホライズン内で鳴る。
3. 重尾潜伏では，少数の長期感染が保持窓を破る。
4. モデルは復旧失敗を，検知失敗と保持超過に分けて数える。
5. まず決めるのは，間隔ではなく清浄履歴の長さ。
6. 運用では，検知遅れ・復旧時間・追加保持を一緒に更新する。

## Source Map

| Slide | Lead message | Primary sources |
|-------|--------------|-----------------|
| 1 | 最新バックアップだけを見ると，復旧先を間違える | `01_introduction.tex`, `02_model_formulation.tex` |
| 2 | 良いアラートは，清浄復旧ホライズン内で鳴る | `02_model_formulation.tex`, `08_conclusion.tex` |
| 3 | 重尾潜伏では，少数の長期感染が保持窓を破る | `01_introduction.tex`, `04_tauber_transition.tex` |
| 4 | モデルは復旧失敗を，検知失敗と保持超過に分けて数える | `02_model_formulation.tex`, `05_backup_optimization.tex` |
| 5 | まず決めるのは，間隔ではなく清浄履歴の長さ | `05_backup_optimization.tex`, `08_conclusion.tex` |
| 6 | 運用では，検知遅れ・復旧時間・追加保持を一緒に更新する | `05_backup_optimization.tex`, `06_dynamic_retention.tex`, `07_numerical_examples.tex` |

## Build And QA

- Build command used artifact-tool presentation modules in a temporary
  thread-scoped workspace.
- `build_artifact_deck.mjs --slide-count 6`: PASS.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_refined.pptx`: PASS.
- Rendered contact sheet and full-size slides 4 and 6 were visually inspected.
- Package contains six `ppt/slides/slide*.xml` files.
- No embedded media assets are used.

## Review State

Review loop stopped after Round 2 because no unresolved CRITICAL, MAJOR, HIGH,
or MINOR findings remained.

- Round 1 found presentation-polish and layout issues; all were addressed.
- Round 2 story/source/visual review found no remaining issues.
- Final scorecard: 41 / 45, PASS.

See `review_reports/`, `issue_register.yaml`, `convergence_dashboard.md`, and
`comeback_scorecard.md`.
