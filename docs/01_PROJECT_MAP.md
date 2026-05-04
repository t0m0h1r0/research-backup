# GENERATED - do NOT edit directly. Edit prompts/meta/kernel-*.md and regenerate.

# 01_PROJECT_MAP - Heavy-Tail Ransomware Paper Agent Project

## §1 Source Artifacts

| Artifact | Path | Status | Rule |
|----------|------|--------|------|
| Original PDF | `paper/source/heavy_tail_backup_v13.pdf` | IMMUTABLE | PR-2 |
| Extracted text | `paper/source/heavy_tail_backup_v13.txt` | DERIVED SOURCE | PR-2 |

## §2 Research Focus

The active paper studies ransomware dwell time under heavy-tailed Pareto latency,
a composite semi-Markov attack/defense model, optimal backup interval design,
detection investment phase-transition behavior, and dynamic retention extension.

## §3 Interface Contracts

| Contract | Producer | Consumer | Purpose |
|----------|----------|----------|---------|
| `docs/interface/SourceClaimMap.md` | T | T/R/E/A | map paper claims to source locations |
| `docs/interface/CheckSpec.md` | T | R | define symbolic/numerical checks |
| `docs/interface/AnalysisPackage/` | R | E/A | reproducible check outputs |
| `docs/interface/EvidencePackage/` | E | A | citation and empirical support |
| `docs/interface/RevisionBrief.md` | T/E | A | signed basis for paper edits |

## §4 Directory Map

| Directory | Owner | Use |
|-----------|-------|-----|
| `docs/memo/` | T | proof and model audits |
| `docs/evidence/` | E | literature and empirical notes |
| `analysis/` | R | reproducible scripts and outputs |
| `paper/sections/` | A | proposed manuscript edits |
| `artifacts/M/` | M | workflow lessons and prompt-improvement notes |
| `prompts/meta/` | P/M | kernel source of truth |
| `prompts/agents-*` | P | generated agent prompts |

## §5 Implementation Constraints

- Do not overwrite files in `paper/source/`.
- Do not promote a paper edit without a source reference or signed revision brief.
- Do not add literature claims without source verification.
- Do not treat paper completion as higher priority than agent-workflow improvement.

## §6 Initial Paper Audit Targets

| ID | Target | Suggested owner |
|----|--------|-----------------|
| ASM-001 | Renewal-reward applicability under all alpha > 0 | TheoryArchitect |
| ASM-002 | Tauber remainder bound and uniformity conditions | TheoryArchitect |
| ASM-003 | Uniqueness of closed-form optimal backup interval | TheoryAuditor |
| ASM-004 | Compactness proof for frequency-asymptotic independence | TheoryAuditor |
| ASM-005 | Citation support for ransomware dwell-time heavy tails | EvidenceAnalyst |
| ASM-006 | Numerical example reproducibility for 19.7-day interval | TestRunner |

## §6b Python Numerical Evaluation Standard

Use one folder per study:

```text
analysis/{study}/
  run.py
  README.md
  results/
    manifest.json
    run.log
    metrics.csv or metrics.json
    figures/*.pdf
```

The manifest is the EvidencePackage entry point for numerical work. A paper claim
may cite a Python result only if the manifest has a PASS or INCONCLUSIVE verdict
with source references and the exact command used to produce the result.

## §7 Paper Structure

Extracted sections: abstract, introduction, model formulation, renewal-reward
conditions, Tauber asymptotics, optimal backup design, dynamic retention extension,
numerical examples, conclusion.

## §8 Matrix Domain Map

Use `prompts/meta/kernel-domains.md` as the authority for T/R/E/A/M/P/Q/K ownership.
