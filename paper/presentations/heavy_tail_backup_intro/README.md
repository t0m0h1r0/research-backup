# Heavy-Tail Backup Intro Deck

status: VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-05T07:47:45Z
deck_file: `heavy_tail_backup_intro.pptx`
slide_count: 5

## Purpose

研究内容紹介用に，ローカル論文
`paper/sections/heavy_tail_backup_recast_xelatex.tex` および
`paper/sections/tex/*.tex` の内容を 5 枚程度に圧縮したプレゼン資料。
対象聴衆は，リスクモデル・セキュリティ運用・数理最適化に関心のある
研究者または技術者を想定する。

## Evidence Boundary

- 本デッキは，修正版の論文セクションに基づくモデル由来の説明である。
- 数値例は `analysis/paper_review_checks/results/manifest.json` で再計算された
  式のスケール確認であり，実務推奨値や実証結果として扱わない。
- 外部の SOTA，ベンチマーク，実運用での尾指数・検知率・攻撃頻度に関する
  新規主張は追加していない。

## Narrative Spine

1. Problem: 検知の速さだけでは，汚染後バックアップにより復旧可能性を
   失う危険を評価できない。
2. Model: Pareto 潜伏時間と指数検知を合成半マルコフ分岐として扱い，
   早期検知・症状検知・全損の費用を分離する。
3. Insight: 正の検知率は暦時間費用率を有限にするが，保持境界なしでは
   重尾リスクの相転移が残る。
4. Design: 内点条件で得られる閉形式解は，まず清浄復旧可能期間
   `a* = nΔ*` として読む。
5. Implication: 数値例は，損失・復旧時間・スキャン負荷・保持世代数から
   初期設計を作る読み替えを示す。

## Slide Source Map

| Slide | Lead message | Primary sources |
|-------|--------------|-----------------|
| 1 | 検知の速さだけでは，復旧点は守れない | `00_abstract.tex`, `01_introduction.tex`, `02_model_formulation.tex` |
| 2 | 攻撃の潜伏と防疫の分岐を一つの費用式に載せる | `02_model_formulation.tex` |
| 3 | 検知は潜伏を打ち切るが，保持境界なしでは尾が残る | `03_renewal_reward.tex`, `04_tauber_transition.tex` |
| 4 | 閉形式解は「清浄に戻れる期間」として読む | `05_backup_optimization.tex` |
| 5 | 5世代保持なら，例では約18.67日間隔・約93.33日保持 | `05_backup_optimization.tex`, `06_dynamic_retention.tex`, `07_numerical_examples.tex`, `analysis/paper_review_checks/results/manifest.json` |

## Build And QA

- Build command used artifact-tool presentation modules in a temporary
  thread-scoped workspace.
- `build_artifact_deck.mjs --slide-count 5`: PASS.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- Rendered contact sheet was visually inspected after layout QA.

## Review State

Independent review reached no remaining CRITICAL, MAJOR, or MINOR findings in
Round 3. See `review_rounds.md`.
