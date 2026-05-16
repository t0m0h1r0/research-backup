# Heavy-Tail Backup Refined Deck

status: THEATRICAL_FORMULA_READING_VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:14:20Z
updated_at_utc: 2026-05-16T22:55:04Z
deck_file: `heavy_tail_backup_refined_theatrical.pptx`
alternate_deck_file: `heavy_tail_backup_refined.pptx`
slide_count: 7
worktree: `/private/tmp/research-backup-presentation-refine`
branch: `codex/researcharchitect-presentation-refine`

## Purpose

研究発表用に，既存の5枚デッキ
`paper/presentations/heavy_tail_backup_intro/heavy_tail_backup_intro.pptx`
を踏まえつつ，改訂版として再生成したプレゼン資料。

改訂の主眼は，直感的な復旧リスクから設計式へ飛ばず，検知失敗・保持超過・
復旧不能の分解を経由してから清浄復旧ホライズンの式へ進めること。

追加の外連味版 `heavy_tail_backup_refined_theatrical.pptx` では，暗い
インシデント対応室トーン，大きい一文，赤/緑の強い警告色，英字アクセント
を使い，初見の引っかかりを強めた。根拠境界と数式条件は維持している。

ユーザーレビュー後に，専門用語を平易な日本語に置き換え，グラフ図の軸と
方向を明示し，数式スライドでは分子・分母・世代数の3点に視線誘導を
追加した。

さらに数式の読み解き方が不足していたため，外連味版を7枚構成に更新し，
数式を「全損を避ける価値」「古く戻る負荷」「世代数で間隔に割る」の
順に読む専用スライドを追加した。

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
5. 式は，計算ではなく「何を残すべきか」として読む。
6. まず決めるのは，間隔ではなく清浄履歴の長さ。
7. 運用では，検知遅れ・復旧時間・追加保持を一緒に更新する。

## Source Map

| Slide | Lead message | Primary sources |
|-------|--------------|-----------------|
| 1 | 最新バックアップだけを見ると，復旧先を間違える | `01_introduction.tex`, `02_model_formulation.tex` |
| 2 | 良いアラートは，清浄復旧ホライズン内で鳴る | `02_model_formulation.tex`, `08_conclusion.tex` |
| 3 | 重尾潜伏では，少数の長期感染が保持窓を破る | `01_introduction.tex`, `04_tauber_transition.tex` |
| 4 | モデルは復旧失敗を，検知失敗と保持超過に分けて数える | `02_model_formulation.tex`, `05_backup_optimization.tex` |
| 5 | 式は，計算ではなく「何を残すべきか」として読む | `05_backup_optimization.tex` |
| 6 | まず決めるのは，間隔ではなく清浄履歴の長さ | `05_backup_optimization.tex`, `08_conclusion.tex` |
| 7 | 運用では，検知遅れ・復旧時間・追加保持を一緒に更新する | `05_backup_optimization.tex`, `06_dynamic_retention.tex`, `07_numerical_examples.tex` |

## Build And QA

- Build command used artifact-tool presentation modules in a temporary
  thread-scoped workspace.
- `build_artifact_deck.mjs --slide-count 6`: PASS for the refined deck.
- `build_artifact_deck.mjs --slide-count 7`: PASS for the theatrical deck.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_refined.pptx`: PASS.
- `unzip -t heavy_tail_backup_refined_theatrical.pptx`: PASS.
- Rendered contact sheets and full-size clarity-critical slides were visually
  inspected.
- The refined PPTX package contains six `ppt/slides/slide*.xml` files.
- The theatrical PPTX package contains seven `ppt/slides/slide*.xml` files.
- No embedded media assets are used.

## Review State

The calm refined deck review loop stopped after Round 2 because no unresolved
CRITICAL, MAJOR, HIGH, or MINOR findings remained. Round 3 added the theatrical
visual pass requested after validation and re-ran mechanical QA. Round 4
addressed user clarity feedback on specialist terms, graph axes, and formula
focus. Round 5 split the formula explanation into a dedicated reading slide and
a separate design-target slide.

- Round 1 found presentation-polish and layout issues; all were addressed.
- Round 2 story/source/visual review found no remaining issues.
- Round 3 created the theatrical dark-room variant and passed layout/package QA.
- Round 4 clarified audience language, graph axes, and formula attention points.
- Round 5 added explicit formula reading order and expanded the theatrical deck
  to seven slides.
- Final theatrical scorecard: 44 / 45, PASS.

See `review_reports/`, `issue_register.yaml`, `convergence_dashboard.md`, and
`comeback_scorecard.md`.
