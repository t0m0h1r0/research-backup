# Story Map

status: THEATRICAL_FORMULA_READING_VALIDATED
created_by: ResearchArchitect
created_at_utc: 2026-05-16T22:00:58Z
updated_at_utc: 2026-05-16T22:55:04Z

## Thesis

ランサムウェア防御では，検知の速さだけでなく，検知時点で清浄な復旧点が
残っているかを同じ設計問題として扱う必要がある。

## One-Line Arc

事故当日の復旧判断から入り，検知評価を清浄復旧ホライズンへ翻訳し，
重尾潜伏が保持窓を破る理由を示し，モデル分解を経由して設計式を
読み解き，運用手順に落とす。

## Slide Claims

| Slide | Kicker | Claim title | Proof object | Source |
|-------|--------|-------------|--------------|--------|
| 1 | Incident question | 最新バックアップだけを見ると，復旧先を間違える | Clean/contaminated backup timeline | `01_introduction.tex`, `02_model_formulation.tex` |
| 2 | Evaluation shift | 良いアラートは，清浄復旧ホライズン内で鳴る | Horizon bar showing `a_n(Delta)=nDelta` | `02_model_formulation.tex`, `08_conclusion.tex` |
| 3 | Tail risk | 重尾潜伏では，少数の長期感染が保持窓を破る | Typical-versus-tail dwell-time visual | `01_introduction.tex`, `04_tauber_transition.tex` |
| 4 | Loss accounting | モデルは復旧失敗を，検知失敗と保持超過に分けて数える | Branch/loss decomposition diagram | `02_model_formulation.tex`, `05_backup_optimization.tex` |
| 5 | Formula reading | 式は，計算ではなく「何を残すべきか」として読む | Three-part formula reading panel for `a*` | `05_backup_optimization.tex` |
| 6 | Design target | まず決めるのは，間隔ではなく清浄履歴の長さ | `a*` to `Delta*` translation panel | `05_backup_optimization.tex`, `08_conclusion.tex` |
| 7 | Operating loop | 運用では，検知遅れ・復旧時間・追加保持を一緒に更新する | Four-step operating loop plus retention extension cue | `05_backup_optimization.tex`, `06_dynamic_retention.tex`, `07_numerical_examples.tex` |

## Omission Notes

- 外部のランサムウェア頻度，実測 dwell time，EDR 性能，SOTA，ベンチマーク
  比較は入れない。
- 数値例は必要なら口頭補足に留め，スライド本文では実務推奨値に見せない。
- `alpha<=1` の相転移は詳細証明ではなく，保持境界が必要になる理由として
  1枚の文脈に留める。
