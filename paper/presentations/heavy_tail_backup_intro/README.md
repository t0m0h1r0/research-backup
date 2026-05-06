# Heavy-Tail Backup Intro Deck

status: ROUND2_ADDRESSED
created_by: ResearchArchitect
created_at_utc: 2026-05-06T04:35:17Z
round1_addressed_at_utc: 2026-05-06T04:47:07Z
round2_addressed_at_utc: 2026-05-06T04:52:08Z
deck_file: `heavy_tail_backup_intro.pptx`
slide_count: 5
worktree: `/private/tmp/research-backup-paper-presentation-zero-base`
branch: `codex/researcharchitect-paper-presentation-zero-base`

## Purpose

研究内容紹介用に，ローカル論文
`paper/sections/heavy_tail_backup_recast_xelatex.tex` および
`paper/sections/tex/*.tex` の内容から，スライド内容をゼロベースで
再作成したプレゼン資料。

既存デッキの文言・構成を前提にせず，初学者が研究の重要性を理解しやすい
ように，ランサムウェア発症時の復旧判断から入り，検知評価を
「清浄バックアップが残っているか」という運用指標へ翻訳し，最後に
清浄復旧ホライズンを設計する手順へ着地させる。

## Evidence Boundary

- 本デッキは，修正版の論文セクションに基づくモデル由来の説明である。
- `docs/wiki/ransomware_heavy_tail_backup_design.md` は内部コンパイル済み
  知識として参照したが，外部実証根拠としては扱わない。
- 外部の SOTA，ベンチマーク，実運用での尾指数・検知率・攻撃頻度に
  関する新規主張は追加していない。
- 数値例はスケール確認としてのみ扱い，実務推奨値や実証結果として
  扱わない。

## Zero-Base Narrative Spine

1. Incident-Day Question: 最新バックアップが，いちばん危ない復元先に
   なる場合がある。
2. Evaluation Reframe: 良いアラートは，清浄世代が消える前に鳴る。
3. Heavy-Tail Motivation: 重尾潜伏では，まれな長期感染が保持窓を壊す。
4. Paper Insight: まず決めるのは，間隔ではなく清浄復旧ホライズンである。
5. Operational Takeaway: バックアップは後始末ではなく，防御設計の入力に
   なる。

## Slide Source Map

| Slide | Lead message | Primary sources |
|-------|--------------|-----------------|
| 1 | 最新バックアップが，いちばん危ない復元先になる | `01_introduction.tex`, `02_model_formulation.tex` |
| 2 | 良いアラートは，清浄世代が消える前に鳴る | `02_model_formulation.tex`, `08_conclusion.tex` |
| 3 | 重尾潜伏では，まれな長期感染が保持窓を壊す | `01_introduction.tex`, `04_tauber_transition.tex` |
| 4 | まず決めるのは，間隔ではなく清浄復旧ホライズン | `05_backup_optimization.tex`, `08_conclusion.tex` |
| 5 | バックアップは後始末ではなく，防御設計の入力になる | `05_backup_optimization.tex`, `06_dynamic_retention.tex`, `07_numerical_examples.tex`, `docs/evidence/heavy_tail_backup_source_note.md` |

## Build And QA

- Build command used artifact-tool presentation modules in a temporary
  thread-scoped workspace.
- `build_artifact_deck.mjs --slide-count 5`: PASS.
- `check_layout_quality.mjs --layout ... --min-gap 8`: PASS with
  0 errors and 0 warnings.
- `unzip -t heavy_tail_backup_intro.pptx`: PASS.
- Rendered contact sheet was visually inspected after layout QA.
- Independent review Round 1 found no CRITICAL findings and multiple MAJOR /
  MINOR findings across beginner narrative, source fidelity, and visual
  hierarchy.
- All Round 1 findings were addressed by rebuilding the slide visuals and
  tightening language, conditions, notation, and operational caveats.
- Independent review Round 2 found one CRITICAL source-boundary issue on
  Slide 3 (`平均が同じに見えても`) plus MINOR polish items.
- All Round 2 findings were addressed by changing the claim to typical-case
  wording, tightening operational wording, and polishing notation.

## Review State

Round 2 findings have been addressed. Round 3 review is pending.
See `review_rounds.md`.
